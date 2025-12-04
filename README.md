# 1. 프로젝트 소개 
- 이번에 발생한 기록적인 침수 사례를 보며, 침수 상황을 실시간으로 감지하고 즉시 대응할 수 있는 시스템의 필요성을 느껴 이 프로젝트를 시작했습니다.
이 프로젝트는 로컬(Edge) 환경에서 침수 여부를 실시간 분석하고, 판단 결과를 즉시 알림 형태로 전송할 수 있는 경량화된 AI 기반 침수 감지 시스템을 구축하는 것을 목표로 합니다.

# 2. 시스템 아키텍처
![alt text](imges/system_flow.png)

# 3. 주요 기능 
- Edge AI 추론(MobileNetV3 + TFLite)
- 침수/비침수 이미지 실시간 분류
- MQTT Publish
- AWS EC2 MQTT Broker 수신
- 향후 확장(UART → STM32 물리 제어 등)

# 4. 기술 스택
- Raspberry Pi4
- PiCamera2
- TensorFlow / Keras / TFLite
- MobileNetV3 Fine-tuning
- colab
- OpenCV
- MQTT (paho-mqtt)
- AWS EC2 (Mosquitto Broker)
- Python 3.13


5. 데이터셋 & 학습 과정 (Dataset & Training)
## 📘 Dataset Samples
| Flood | Normal |
|-------|--------|
| ![alt text](imges/blue.png) | ![alt text](imges/no-water.png) |


# 5. 어려웠던 점 & 해결 과정

### 1) 모델 학습 불안정 문제
  - 초기: `no_water`, `blue`, `mid`, `red` 4-class 분류로 설계
  - 실제 데이터가 부족해 학습이 불안정하고 정확도가 낮게 나오는 문제가 발생
  - 문제 단순화를 위해 2-class(침수 / 비침수)로 재구성하고 파인튜닝

  → **결과:** 학습 안정화 및 실제 환경에서 분류 정확도가 크게 개선됨

### 2) MacOS 로컬 MQTT Broker 연결 문제
  - MacOS에서 Mosquitto Broker가 포트·권한 문제로 연결되지 않는 오류 발생
  - Raspberry Pi Publisher가 지속적으로 연결을 시도했지만 실패
  - 안정적 테스트를 위해 AWS EC2에 Mosquitto Broker를 새로 구성

  → **결과:** Raspberry Pi ↔ EC2 간 MQTT 통신이 안정적으로 동작

# 6. 향후 보안 
### 1) 물리적 제어 시스템 확장
  - STM32 보드와 UART 연동 예정  
  - 침수 감지 시 Raspberry Pi → STM32로 상태 값 전송  
  - STM32에서 LED, 부저 등 물리적 제어 수행  

### 2) 침수 단계 세분화 모델 재설계
