참고 URL : https://github.com/maxkferg/metal-defect-detection

개발환경 구축 관련
1. environment.yml 으로 설치했지만, 버전 없는 부분 있어서 수동으로 수정해주고 설치함(pip나 conda 버전별로 다른 느낌)
2. 가상환경 base에서 conda install 시 python 버전도 업그레이드하는 경우가 있어서 다른 가상환경 만들어서 사용하는 방법을 추천
3. Cuda, cudnn, tensorflow-gpu 버전 미스매칭(버전이 불일치시 에러 발생 - 디펜던시 이슈)
 - cudnn 7.6.5안 맞아서 -> Tensorflow-gpu 1.5버전은 cuda 9.0, cudnn 7.0.5 버전 설치 진행

깃허브 최신화가 아님
- 2017~2018년도에 활발히 만들다가, 2020년을 마지막으로 업데이트가 없는것으로 보임
- 현재 진행된 곳까지 진행하여 확인

확인사항
- 스마트 팩토리 프로젝트로 images detection으로 사용가능한지 확인하려고 했지만, 확인된 부분까지만 진행 완료
- GPU 사용으로 학습 (CPU보다 훨씬 빠르다는걸 체감)
- GPU 학습할 때 온도 이슈 체크하면서 해야함(중간에 뻗어서, GPU 전력 사용량 제한하고 수행)

확인한 소스코드
•	GDxray.py Train ~
•	Coco.py Train ~
•	GDxray 쥬피터 노트북 파일 : inspect_data.ipynb
•	GDxray 쥬피터 노트북 파일 : inspect_model.ipynb
•	진행중인 내용(백그라운드) python gdxray.py evaluate ~
	- 로그 파일 확인시 tail 사용하는걸 추천(vi,vim 사용 X)
진행 완료 사항
파일 : inspect_model.ipynb
아래의 코드, 그림나오는 부분까지 진행 확인 완료
# Display positive anchors before refinement (dotted) and
# after refinement (solid).
visualize.draw_boxes(image, boxes=positive_anchors, refined_boxes=refined_anchors, ax=get_ax())
