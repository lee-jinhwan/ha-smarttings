# Homassistant Smarttings Custom Components
 Homeassistant-core에서 Samsung Smartthings 부족한 기능들을 추가한 컴포넌트 입니다.

## 최소 지원 버전
HomeAssistant `2022.7.0` 이상

## 설치
1. Git에서 코드를 다운 받습니다. 
2. `custom_components` 에 복사 합니다.
```
    └── ...
    └── configuration.yaml
    └── custom_components
        └── ...
        └── climate
            └── translations
            └── __init__.py
            └── const.py
            └── ...
        └── smartthings
            └── translations
            └── __init__.py
            └── binary_sensor.py
            └── ...            
```
3. HomeAssistant 재시작


## 지원 기능

### climate
 - 운전 모드 `AI 쾌적 (AI Comfort)` 추가

### smartthings
 - 에어컨 `자동` 모드는 `Heat/Cool`이 아닌 `Auto`로 변경
 - `송풍` 모드 지원
 - `AI 쾌적` 모드 지원
 - 에어컨 옵션 모드 추가 (무풍, 열대야 쾌면 등)
