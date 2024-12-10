# 인공지능 시인 - AI Poet

인공지능 시인은 사용자가 입력한 주제를 기반으로 OpenAI GPT 모델을 활용해 창의적이고 감성적인 시를 작성해주는 웹 애플리케이션입니다. 간단한 인터페이스와 직관적인 사용성을 제공하며, 누구나 쉽게 감성적인 시를 생성할 수 있습니다.


## 📚 주요 기능
- 주제 기반 시 생성: 사용자가 입력한 주제에 맞는 시를 AI가 작성.
- Streamlit 인터페이스: 간단하고 직관적인 UI로 손쉬운 사용.
- 빠른 응답: OpenAI API를 사용하여 실시간으로 결과 제공.


## 🌟 시작하기
### 1. 요구 사항
  - OpenAI API 키 ([API 키 발급 받기](https://platform.openai.com/signup))
### 2. 설치 방법
  - 리포지토리 클론:
```bash
git clone https://github.com/hs-2171098-hyunjinchoi/ai-poet.git
cd ai-poet
```
- 가상 환경 생성 및 활성화 (선택 사항):
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
- 의존성 설치:
```bash
pip install -r requirements.txt
```
- .env 파일 설정: `your_openai_api_key`는 발급받은 OpenAI API 키로 교체합니다.
```bash
OPENAI_API_KEY=your_openai_api_key
```
### 3. 실행 방법
- Streamlit 실행:
```bash
streamlit run main.py
```
- 웹 브라우저에서 실행:
  브라우저에서 [http://localhost:8501](http://localhost:8501)로 접속합니다.
  시의 주제를 입력하고 **시 작성** 버튼을 눌러 결과를 확인하세요.


## 🛠 프로젝트 구조
```
ai-poet/
├── main.py             # Streamlit 웹 애플리케이션
├── requirements.txt    # 의존성 리스트
├── .env                # OpenAI API 키 설정 파일
└── README.md           # 프로젝트 설명 파일
```


## 💡 추가 개발 아이디어
- **다양한 시 형식 지원**: 사용자가 원하는 시의 형식을 선택할 수 있도록 기능 확장.
- **다국어 지원**: 영어, 프랑스어, 일본어 등 다양한 언어로 시 작성.
- **주제 추천 기능**: 사용자가 입력하지 않아도 랜덤 주제를 제공.
- **저장 및 공유 기능**: 작성된 시를 저장하거나 소셜 미디어로 공유.


## 🌐 배포된 앱

[인공지능 시인 앱 바로가기](https://aipoet2171098.streamlit.app/)
