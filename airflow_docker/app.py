# app.py
# --------------------------------------------------------
# YOLOv12 Gradio Demo (single Blocks, model cache, 0.0.0.0:7860)
# --------------------------------------------------------

import os
import cv2
import gradio as gr
import tempfile
from ultralytics import YOLO

# --------- Model cache (avoid reloading .pt every request) ----------
_MODEL_CACHE: dict[str, YOLO] = {}

def get_model(model_id: str) -> YOLO:
    m = _MODEL_CACHE.get(model_id)
    if m is None:
        m = YOLO(model_id)
        _MODEL_CACHE[model_id] = m
    return m

# --------- Helpers ----------
def _ensure_video_path(video) -> str | None:
    """
    Gradio gr.Video 입력은 문자열 경로나 dict/바이트가 올 수 있으므로 안전 처리.
    반환: 읽을 수 있는 파일 경로 (없으면 None)
    """
    if video is None:
        return None
    if isinstance(video, str):
        return video
    if isinstance(video, dict) and "name" in video and isinstance(video["name"], str):
        return video["name"]  # Gradio가 dict로 넘기는 경우
    # 메모리/바이트류는 임시파일로 저장
    tmp = tempfile.mktemp(suffix=".webm")
    with open(tmp, "wb") as f:
        if hasattr(video, "read"):
            f.write(video.read())
        elif isinstance(video, (bytes, bytearray)):
            f.write(video)
        else:
            raise ValueError("지원되지 않는 video 입력 형식입니다.")
    return tmp

# --------- Inference ----------
def yolov12_inference(image, video, model_id, image_size, conf_threshold):
    """
    image 또는 video 중 하나만 사용.
    - image: PIL.Image (Gradio)
    - video: 파일 경로/딕셔너리/바이트 등
    반환: (RGB numpy image or None, video path or None)
    """
    model = get_model(model_id)

    # ----- Image -----
    if image is not None:
        results = model.predict(source=image, imgsz=image_size, conf=conf_threshold)
        annotated_bgr = results[0].plot()         # BGR
        annotated_rgb = annotated_bgr[:, :, ::-1] # RGB
        return annotated_rgb, None

    # ----- Video -----
    video_path = _ensure_video_path(video)
    if video_path is None or not os.path.exists(video_path):
        raise ValueError("유효한 동영상 입력이 없습니다.")

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 640
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 480

    out_path = tempfile.mktemp(suffix=".webm")
    fourcc = cv2.VideoWriter_fourcc(*"vp80")  # webm (VP8)
    out = cv2.VideoWriter(out_path, fourcc, fps, (w, h))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model.predict(source=frame, imgsz=image_size, conf=conf_threshold)
        annotated = results[0].plot()  # BGR
        out.write(annotated)

    cap.release()
    out.release()
    return None, out_path

def yolov12_inference_for_examples(image, model_path, image_size, conf_threshold):
    annotated_image, _ = yolov12_inference(image, None, model_path, image_size, conf_threshold)
    return annotated_image

# --------- UI ----------
def build_app():
    with gr.Blocks() as demo:
        gr.HTML(
            """
            <h1 style='text-align: center'>
            YOLOv12: Attention-Centric Real-Time Object Detectors
            </h1>
            <h3 style='text-align: center'>
            <a href='https://arxiv.org/abs/2502.12524' target='_blank'>arXiv</a> |
            <a href='https://github.com/sunsmarterjie/yolov12' target='_blank'>github</a>
            </h3>
            """
        )

        with gr.Row():
            with gr.Column():
                image = gr.Image(type="pil", label="Image", visible=True)
                video = gr.Video(label="Video", visible=False)
                input_type = gr.Radio(
                    choices=["Image", "Video"],
                    value="Image",
                    label="Input Type",
                )
                model_id = gr.Dropdown(
                    label="Model",
                    choices=["yolov12n.pt", "yolov12s.pt", "yolov12m.pt", "yolov12l.pt", "yolov12x.pt"],
                    value="yolov12m.pt",
                )
                image_size = gr.Slider(label="Image Size", minimum=320, maximum=1280, step=32, value=640)
                conf_threshold = gr.Slider(label="Confidence Threshold", minimum=0.0, maximum=1.0, step=0.05, value=0.25)
                btn = gr.Button(value="Detect Objects")

            with gr.Column():
                output_image = gr.Image(type="numpy", label="Annotated Image", visible=True)
                output_video = gr.Video(label="Annotated Video", visible=False)

        # 입력 종류에 따라 위젯 가시성 전환
        def update_visibility(kind):
            return (
                gr.update(visible=(kind == "Image")),  # image
                gr.update(visible=(kind == "Video")),  # video
                gr.update(visible=(kind == "Image")),  # output_image
                gr.update(visible=(kind == "Video")),  # output_video
            )

        input_type.change(
            fn=update_visibility,
            inputs=[input_type],
            outputs=[image, video, output_image, output_video],
        )

        # 실행
        def run(image, video, model_id, image_size, conf_threshold, kind):
            if kind == "Image":
                return yolov12_inference(image, None, model_id, image_size, conf_threshold)
            else:
                return yolov12_inference(None, video, model_id, image_size, conf_threshold)

        btn.click(
            fn=run,
            inputs=[image, video, model_id, image_size, conf_threshold, input_type],
            outputs=[output_image, output_video],
            api_name="predict"  # ← HTTP 호출용 엔드포인트 이름
        )

        # 예제 (캐시 이슈 회피 위해 cache_examples=False)
        gr.Examples(
            examples=[
                ["ultralytics/assets/bus.jpg",   "yolov12s.pt", 640, 0.25],
                ["ultralytics/assets/zidane.jpg","yolov12x.pt", 640, 0.25],
            ],
            fn=yolov12_inference_for_examples,
            inputs=[image, model_id, image_size, conf_threshold],
            outputs=[output_image],
            cache_examples=False,
        )

    return demo

if __name__ == "__main__":
    demo = build_app()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_api=False  # JSON schema 노출 끔(일부 버전에서 스키마 파싱 오류 회피)
    )

