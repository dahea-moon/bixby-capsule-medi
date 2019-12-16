# Medi (메디)

created by 문다혜 @dahea-moon, 최솔지 @soulgchoi

**Back-end**: Django + DRF,  **Front-end**: Bixby,  **Deploy**: Bixby (예정)



## 프로젝트 목표

사용자가 제공하는 위치 및 요일, 시간을 기반으로 병원, 약국, 수유실 또는 심장제세기를 찾아주는 빅스비 캡슐입니다. (12월 중으로 빅스비 마켓 릴리즈 예정)



## 캡슐 주요 기능

### **가장 가까운 기관 검색**

1. 사용자의 현재 위치, 요일, 시간 기반 (searchNearest)
2. 사용자가 원하는 장소와 현재 요일 및 시간 기반 (searchBasedonDestination)
3. 사용자가 원하는 장소와 요일 기반 (searchBasedonDestinationWeekday)
4. 사용자가 원하는 장소와 시간 기반 (searchBasedonDestinationTime)



### 검색과정

- 위치(경도, 위도), 요일, 시간을 Django Server에 요청
- 경도, 위도를 기준으로 주위 20km (사각형)에 있는 기관 중 가장 가깝고 현재 운영 중인 기관 3개의 상세 정보와 지도를 제공
- DRF을 사용하여 Bixby Client에 응답

​	

