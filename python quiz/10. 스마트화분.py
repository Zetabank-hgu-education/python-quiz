# 10. 스마트 화분 관리 시스템
# 이 프로그램은 실내 화분의 수분 상태를 자동으로 모니터링합니다.
# 15초마다 수분 센서를 통해 화분의 수분 상태를 측정하고, 필요에 따라 자동으로 물을 줄 수 있도록 알림을 보내는 시스템을 만들어 봅시다.

import time
import random  # 실제 수분 센서가 아니므로 랜덤 값을 사용

def get_moisture_level():
    return random.randint(0, 100)  # 랜덤 수분 레벨 반환 (0 ~ 100% 사이)

def monitor_plant_moisture():
    while True:
        moisture_level = get_moisture_level()
        print(f"현재 수분 레벨: {moisture_level}%")

        if moisture_level < 20:
            print("경고: 화분의 수분 레벨이 너무 낮습니다! 물을 주세요.")
        elif moisture_level > 80:
            print("경고: 화분의 수분 레벨이 너무 높습니다! 물을 빼 주세요.")
        
        time.sleep(5)  # 15초 대기

if __name__ == "__main__":
    print("스마트 화분 관리 시스템을 시작합니다.")
    monitor_plant_moisture()