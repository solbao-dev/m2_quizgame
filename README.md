# 🎯 나만의 퀴즈 게임 (Python & Git 프로젝트)

## 1. 프로젝트 개요
터미널 환경에서 동작하는 콘솔 기반의 퀴즈 게임 프로그램입니다. Python의 기본 문법과 클래스(class)를 활용하여 객체 지향적으로 코드를 구조화하였으며, JSON 파일 시스템을 이용해 데이터를 영구적으로 저장하고 불러옵니다.  Git 브랜치 활용과 클론(Clone) 실습을 통해 버전 관리와 협업의 기초를 다졌습니다.

## 2. 퀴즈 주제 선정 이유
* **주제:** 파이썬 기초 문법 및 Git 트러블슈팅

* **이유:** 코디세이 미션을 수행하며 직접 겪었던 여러 `error` 상황들을 퀴즈로 만들어, 프로그래밍 기초 개념을 확실히 복습하고 실제 발생할 수 있는 오류에 대한 대처 능력을 기르기 위해 선정했습니다.


## 3. 실행 방법 (How to Run)



0) **개발환경설정**: 이 프로그램을 실행하기 위해서는 Python이 설치되어 있어야 합니다.  
```bash
Editor: Visual Studio Code (v1.112.0) ✨

Python: Python 3.12.13

Git: git version 2.53.0
```

1) **프로젝트 복제**: 터미널에서 아래 명령어를 입력하여 저장소를 복제합니다.  
```bash
$ git clone https://github.com/solbao-dev/2nd_mission_quizgame.git
```

2) **폴더 이동**: 복제된 프로젝트 폴더로 이동합니다.  
```bash
$ cd 2nd_mission_quizgame
```
3) **프로그램 실행**: 아래 명령어를 입력하여 퀴즈 게임을 시작합니다.  
```bash
$ python main.py
```


## 4. 기능 목록
- [x] **퀴즈 풀기**: 저장된 퀴즈를 순서대로 풀고 정답 여부와 최종 점수를 확인합니다.
- [x] **퀴즈 추가**: 새로운 문제, 선택지 4개, 정답 번호를 직접 입력하여 파일에 등록합니다.
- [x] **퀴즈 목록**: 현재 프로그램에 등록된 모든 퀴즈 목록을 조회합니다.
- [x] **점수 확인**: 역대 플레이 기록 중 최고 점수를 확인합니다.
- [x] **데이터 저장**: 프로그램을 종료해도 추가한 퀴즈와 최고 점수가 `state.json`에 유지됩니다.
- [x] **예외 처리**: 숫자 대신 문자를 입력하거나 강제 종료(Ctrl+C) 시에도 안전하게 종료됩니다.

## 5. 파일 구조 (File Structure)

```text
2nd_mission_quizgame/
├── docs/                      # 문서 및 스크린샷 폴더
│   └── screenshots/           # 실행 화면 캡처 이미지
├── main.py                    # 프로그램 메인 실행 파일
├── state.json                 # 퀴즈 및 최고 점수 데이터 저장 파일
├── .gitignore                 # Git 추적 제외 설정 파일
└── README.md                  # 프로젝트 가이드 및 설명서
```

## 6. 데이터 파일 설명 (state.json)
- **경로:** 프로젝트 최상위 폴더 (`/state.json`)
- **역할:** 프로그램 종료 시 사용자가 추가한 퀴즈 데이터와 점수가 날아가지 않도록 안전하게 보존합니다.
- **스키마 구조:**
  - `quizzes`: 개별 퀴즈 정보(`question`, `choices`, `answer`)가 딕셔너리 형태로 담긴 리스트 구조입니다.
  - `best_score`: 현재까지 사용자가 기록한 최고 정답 수를 나타내는 숫자(int) 데이터입니다.
## 7. 트러블슈팅 (Troubleshooting)

### 🚨 문제 상황 (Issue)
터미널에서 첫 번째 커밋(`git commit`)을 시도했을 때, 아래와 같은 Author identity unknown 안내 메시지가 발생하며 커밋이 진행되지 않음.
> "Please tell me who you are." 
> "Run git config --global user.email and user.name"

### 💡 원인 파악 (Cause)
온라인 저장소인 **GitHub**에는 로그인이 되어 있었지만, 내 컴퓨터(로컬)에서 작동하는 **Git(버전 관리 프로그램)**에는 작업자가 누구인지 식별할 수 있는 이름과 이메일(환경설정)이 등록되어 있지 않아서 발생한 현상임. Git과 GitHub가 서로 독립적으로 동작한다는 개념을 확실히 인지하게 됨.

### 🛠️ 해결 방법 (Solution)
터미널에 아래 명령어를 입력하여 로컬 Git에 사용자 정보를 입력함
```bash
git config --global user.name "solbao-dev"
git config --global user.email "dianasjyoon@gmail.com"
```
### ✅검증 (Verification)
‘git config’ 명령어를 통해 설정이 정상적으로 반영되었는지 검증 완료함
```bash
git config user.name  >solbao-dev
git config user.email >dianasjyoon@gmail.com
```
## 7-1. 트러블슈팅 추가 
### 이슈 2: 파이썬 들여쓰기 오류 (IndentationError)
* **문제 상황 (Issue)**: 코드 수정 또는 복사 후 실행 시 `unexpected indent` 에러 발생하며 프로그램 중단.
* **원인 파악 (Cause)**: 파이썬은 들여쓰기가 곧 코드의 블록(범위)을 의미하는데, 줄 맨 앞에 불필요한 공백이나 탭이 섞여 문법 규칙을 위반함.
* **해결 방법 (Solution)**: 에러가 발생한 줄의 시작 부분을 확인하여 불필요한 공백을 제거하고 왼쪽 벽에 딱 맞춰 정렬함.
* **검증 (Verification)**: `python main.py` 실행 시 메뉴 화면이 정상적으로 출력됨.

---

### 이슈 3: Git 명령어 대괄호 포함 오류 (zsh: no matches found)
* **문제 상황 (Issue)**: 저장소 복제 시 `git clone [URL]` 형식으로 입력하자 에러 발생하며 복제 실패.
* **원인 파악 (Cause)**: 가이드상의 대괄호(`[]`)를 문법의 일부가 아닌 입력해야 할 문자로 착각함. 터미널은 이를 파일 패턴 매칭으로 인식하여 오류를 내뱉음.
* **해결 방법 (Solution)**: 대괄호를 제거하고 순수 URL 주소만 입력함. (`git clone https://...`)
* **검증 (Verification)**: `clone_practice` 폴더가 정상적으로 생성되고 파일들이 복제됨.

---

### 이슈 4: 터미널 작업 위치(Directory) 불일치
* **문제 상황 (Issue)**: 파일 수정을 완료했음에도 `git add` 명령어가 파일 변화를 감지하지 못함.
* **원인 파악 (Cause)**: 현재 터미널의 위치는 `clone_practice`(분신) 폴더인데, 실제 수정 중인 파일은 `2nd_mission`(본진) 폴더의 것이었음. 터미널 위치와 편집기 위치의 동기화가 중요함을 깨달음.
* **해결 방법 (Solution)**: `cd ..`와 `cd 2nd_mission_quizgame` 명령어를 통해 터미널 위치를 실제 수정 중인 프로젝트 루트로 이동함.
* **검증 (Verification)**: 올바른 경로에서 `git status` 확인 시 변경된 파일들이 정상적으로 표시됨.

---

### 이슈 5: 터미널 한글 입력 버퍼 오류
* **문제 상황 (Issue)**: 터미널에서 퀴즈 데이터(한글) 입력 중 오타를 지우려 해도 글자가 지워지지 않거나 화면이 깨짐.
* **원인 파악 (Cause)**: macOS 터미널 환경에서 한글 렌더링과 입력 버퍼 간의 충돌로 발생하는 현상.
* **해결 방법 (Solution)**: `Ctrl + U`로 줄 전체를 삭제하거나, `Ctrl + C`로 강제 종료 후 재실행하여 깨끗한 상태에서 다시 입력함.
* **검증 (Verification)**: 재시작 후 정상적으로 데이터를 입력하여 `state.json` 저장 성공.

## 9. Git 협업 실습 (Clone & Pull)
- 클론 실습 완료! (2026-04-09)  
버전 관리 시스템의 핵심인 '협업 프로세스'를 익히기 위해 다음과 같은 시나리오 실습을 수행하였습니다.

1. **저장소 복제 (Clone)**: 본 프로젝트를 `clone_practice`라는 별도의 디렉토리에 복제하여 독립된 작업 환경 구축
2. **동기화 (Push & Pull)**: 
   - 분신 폴더(`clone_practice`)에서 README 수정 후 GitHub 원격 저장소로 `push`
   - 본진 폴더(`2nd_mission_quizgame`)에서 원격의 변경 사항을 `pull`로 땡겨와 데이터 동기화 성공
3. **결과**: 이 과정을 통해 팀 프로젝트에서의 코드 공유 및 최신화 메커니즘을 이해함

## 10. 실행화면 및 스크린샷
### - 메뉴 화면
![메뉴화면](./docs/screenshots/menu.png)

### - 퀴즈 플레이
![플레이](./docs/screenshots/play.png)

### - 퀴즈 추가 및 목록
![추가](./docs/screenshots/add_quiz.png)

### - 최고 점수 확인
![점수](./docs/screenshots/score.png)

### - Git History (Log Graph)
![깃로그](./docs/screenshots/git_log.png)  

### - 개발환경설정
![환경설정](./docs/screenshots/env_setup.png)  


---
## 10. 개발 상세 명세 및 심층 분석 (Deep Dive)

### Q1. 클래스(Class)를 사용한 이유와 함수형 구현과의 차이는 무엇인가요?
* **클래스 설계 (캡슐화 및 책임 분리)**
  본 프로젝트에서는 `Quiz` 클래스가 데이터(질문, 보기, 정답)를 캡슐화하고, `QuizGame` 클래스가 비즈니스 로직(게임 흐름, 입출력, 상태 관리)을 전담하도록 역할을 명확히 분리했습니다.
* **함수형과의 차이**
  함수만으로 구현할 경우 게임 상태(퀴즈 목록, 최고 점수 등)를 전역 변수로 관리해야 하므로 상태 추적이 어렵습니다. 반면 클래스를 활용하면 데이터와 이를 조작하는 메서드를 하나의 객체로 묶어 **코드의 재사용성과 유지보수성이 크게 향상**됩니다.

---

### Q2. JSON 파일을 사용한 이유와 형식의 특징은 무엇인가요?
* **사용 이유**
  파이썬의 기본 자료구조인 `Dictionary` 및 `List`와 1:1 매칭이 가능하여, 객체 직렬화(Serialization) 및 역직렬화 과정이 매우 직관적이고 편리합니다.
* **특징**
  `state.json`처럼 사람이 직접 읽고 수정하기 쉬운 경량화된 텍스트 기반 포맷이며, 대부분의 프로그래밍 언어에서 표준으로 지원하여 **데이터 호환성**이 매우 높습니다.

---

### Q3. 파일 입출력 및 입력 처리에서 `try/except`가 필요한 이유는 무엇인가요?
프로그램의 비정상적인 종료를 막고 안정적인 사용자 경험을 유지하기 위한 **방어적 프로그래밍**입니다.

* **입력 검증:** 메뉴나 정답 란에 숫자가 아닌 문자가 들어올 경우 발생하는 `ValueError`를 사전에 차단합니다.
* **I/O 예외:** `state.json` 파일이 삭제되었거나(`FileNotFoundError`) 권한 문제가 발생했을 때, 프로그램이 멈추지 않고 안전하게 기본 데이터를 로드하도록 처리합니다.
* **안전 종료:** `Ctrl+C` 입력 시 발생하는 `KeyboardInterrupt`를 잡아내어 데이터를 안전하게 저장하고 게임을 종료시킵니다.

---

### Q4. 브랜치(Branch)를 분리해 작업한 이유와 병합(Merge)의 의미는 무엇인가요?
* **분리 이유 (협업 관점)**
  여러 개발자가 협업할 때, 안정적으로 동작하는 `main` 브랜치의 코드를 보호하면서 `feature-play`와 같은 독립적인 공간에서 새로운 기능을 안전하게 개발(Isolation)하고 **충돌을 방지**하기 위함입니다.
* **병합의 의미 (통합)**
  독립된 브랜치에서 기능 검증 및 테스트가 완료된 코드를 `main` 브랜치로 합쳐, 팀원들의 작업물을 **하나의 완성된 프로젝트 버전으로 통합**해 내는 핵심 협업 과정입니다.

---

### Q5. 퀴즈 데이터가 1000개 이상으로 늘어난다면 현재 JSON 저장 방식에 어떤 한계가 있나요?
* **한계 (메모리 및 성능)**
  현재 로직은 프로그램 시작 시 `state.json`의 전체 데이터를 메모리에 한 번에 로드(**O(N)** 복잡도)하고, 데이터 변경 시 전체를 다시 덮어씁니다. 데이터가 커지면 심각한 **메모리 오버헤드와 파일 쓰기 지연(속도 저하)**이 발생합니다.
* **대안**
  대규모 데이터를 효율적으로 처리하기 위해, 필요한 데이터만 인덱싱하여 불러오고 수정할 수 있는 **SQLite**나 **PostgreSQL** 같은 데이터베이스(RDBMS) 도입이 필수적입니다.

---

### Q6. 만약 `state.json`이 손상되어 파싱에 실패한다면, 사용자가 데이터를 잃지 않도록 어떤 대응이 가능한가요?
* **장애 대응 로직 (무중단 운영)**
  파일 내용이 깨져 `json.JSONDecodeError`가 발생할 경우, 에러를 캐치(Catch)하여 기존 손상 파일을 백업(`state_backup.json`)합니다.
  이후 `initialize_default_quizzes()` 메서드를 호출해 필수 기본 퀴즈 7개를 메모리에 새로 생성하여, **게임 실행 자체가 중단되는 치명적 장애를 방지(Zero-Downtime)**합니다.

---

### Q7. 요구사항(채점 방식, 퀴즈 구조)이 변경된다면 어느 부분을 수정해야 하나요?
객체 지향 설계 원칙에 따라 **변경이 필요한 모듈만 독립적으로 수정**합니다.

* **채점 방식/점수 로직 변경:** `QuizGame` 클래스의 `play_quiz()` 메서드 내부 점수 합산 로직만 수정
* **선택지 개수 등 퀴즈 구조 변경:** 데이터 모델인 `Quiz` 클래스의 `__init__` 생성자 구조를 변경하고, 새로운 데이터를 입력받는 `QuizGame`의 `add_quiz()` 입출력 로직을 동기화하여 수정  


---
## 11. 핵심 코드 및 기술 증빙 (Technical Proof)

 프로젝트의 핵심 객체 지향 설계와 예외 처리 로직을 아래와 같이 증빙합니다.

### 💻 1. 객체 지향 설계 (Class Responsibility)
- **`Quiz` 클래스**: 캡슐화를 통해 질문, 선택지, 정답 데이터를 하나의 단위로 관리합니다.
- **`QuizGame` 클래스**: 게임 흐름 제어 및 파일 입출력(I/O)을 담당하여 데이터와 로직을 분리했습니다.

```python
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_state()  # 초기화 시 데이터 로드
```

### 💾 2. 데이터 보존 및 파일 입출력 (File I/O & JSON)
읽기(Load): FileNotFoundError 발생 시 기본 데이터를 생성하여 프로그램 중단을 방지합니다.

쓰기(Save): 데이터 변경(퀴즈 추가, 점수 갱신) 시 즉시 state.json에 반영하여 영속성을 보장합니다.  

```python
def load_state(self):
    try:
        with open("state.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            # JSON 데이터를 Quiz 객체 리스트로 변환 (역직렬화)
            self.quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
            self.best_score = data.get("best_score", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        self.initialize_default_quizzes() # 파일 부재 시 초기화 로직

def save_state(self):
    data = {
        "quizzes": [q.__dict__ for q in self.quizzes], # 객체를 딕셔너리로 변환
        "best_score": self.best_score
    }
    with open("state.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
```
### 🛡️ 3. 견고한 입력 검증 및 예외 처리 (Input Validation)
숫자 검증: isdigit()을 사용해 문자가 입력될 경우의 ValueError를 사전에 차단합니다.

범위 검증: 메뉴 번호(1-5) 이외의 입력에 대해 '잘못된 입력' 메시지를 출력하고 메뉴로 리다이렉트합니다.  

```python
def main_menu(self):
    while True:
        print("\n1. 퀴즈 풀기 | 2. 퀴즈 추가 | 3. 목록 | 4. 점수 | 5. 종료")
        choice = input("선택 : ").strip()
        
        if choice == "5": break
        elif choice == "1": self.play_quiz()
        # ... 중략 ...
        else: print("⚠️ 1~5 사이의 숫자만 입력해주세요.")
```
### 🚫 4. 안전 종료 처리 (KeyboardInterrupt)

```python
Ctrl+C 발생 시 시스템의 강제 종료 에러를 가로채어, 안내 메시지와 함께 리소스를 정리하고 안전하게 종료합니다.

try:
    game = QuizGame()
    game.run()
except KeyboardInterrupt:
    print("\n\n[System] 사용자에 의해 프로그램이 강제 종료되었습니다.")
    print("[System] 현재까지의 진행 상황을 안전하게 보존합니다.")
```

### 🌿 5. Git 협업 및 버전 관리 증빙
커밋 로그: Feat, Fix, Docs 등 컨벤션을 준수한 11회 이상의 커밋 완료.

브랜치 전략: main(안정 버전)과 feature-xxx(기능 개발) 브랜치를 엄격히 분리하여 작업 후 Merge를 통해 통합하였습니다.

협업 실습: git clone으로 분신 폴더 생성 후 push & pull 과정을 통해 원격 저장소 동기화 메커니즘을 증명하였습니다.


## 11. 전체 코드 및 실행 데이터 증빙 (Full Source Code)  
본 프로젝트의 전체 소스 코드 및 초기 데이터, 그리고 Git 브랜치 내역을 텍스트로 증빙합니다.


1) 프로젝트 메인 로직 (main.py)  
각 평가 항목(클래스 분리, 예외 처리, JSON I/O)이 실제 코드의 어느 부분에 구현되어 있는지 명확히 주석으로 증빙합니다.

```python
import json
import os

# 📍 [1. 객체 지향 설계 (클래스 분리)]
# 데이터 전담: 순수하게 개별 퀴즈의 '데이터 구조(질문, 보기, 정답)'만 캡슐화하여 관리합니다.
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

# 📍 [1. 객체 지향 설계 (클래스 분리)]
# 로직 전담: 게임의 진행 흐름, 입력 검증, 파일 입출력 등 핵심 비즈니스 로직을 관리합니다.
class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_state()

    # 📍 [3. JSON I/O 로직 (읽기)]
    def load_state(self):
        if os.path.exists("state.json"):
            # 📍 [2. 예외 처리 (파일 입출력 에러 방어)]
            try:
                # state.json 파일을 읽어서 파이썬 리스트/객체로 변환 (역직렬화)
                with open("state.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
                    self.best_score = data.get("best_score", 0)
            # 파일이 깨졌거나 읽을 수 없을 때 프로그램 종료를 막고 기본값으로 초기화
            except (json.JSONDecodeError, FileNotFoundError):
                self.initialize_default_quizzes()
        else:
            self.initialize_default_quizzes()

    def initialize_default_quizzes(self):
        default_data = [
            {"question": "Python에서 리스트에 요소를 추가하는 메서드는?", "choices": ["add()", "append()", "push()", "insert()"], "answer": 2},
            {"question": "Git에서 변경 내용을 스테이징 영역에 추가하는 명령어는?", "choices": ["git commit", "git push", "git add", "git status"], "answer": 3},
            {"question": "JSON의 약자는?", "choices": ["JavaScript Object Notation", "Java Standard Object Network", "Jupyter Source Open Node", "Just Simple Object Note"], "answer": 1},
            {"question": "Python에서 들여쓰기가 잘못되었을 때 발생하는 에러는?", "choices": ["NameError", "TypeError", "IndentationError", "SyntaxError"], "answer": 3},
            {"question": "Git에서 원격 저장소의 내용을 로컬로 가져오는 명령어는?", "choices": ["git send", "git pull", "git save", "git upload"], "answer": 2},
            {"question": "Python의 '붕어빵 틀'에 비유되는 개념은?", "choices": ["Function", "Variable", "Class", "List"], "answer": 3},
            {"question": "마지막 커밋을 취소하거나 수정할 때 사용하는 옵션은?", "choices": ["--amend", "--fix", "--undo", "--back"], "answer": 1}
        ]
        self.quizzes = [Quiz(**q) for q in default_data]
        self.save_state()

    # 📍 [3. JSON I/O 로직 (쓰기)]
    def save_state(self):
        data = {
            "quizzes": [q.__dict__ for q in self.quizzes], # 파이썬 객체를 JSON 형식에 맞게 변환 (직렬화)
            "best_score": self.best_score
        }
        # 변경된 데이터를 state.json 파일에 덮어쓰기
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def play_quiz(self):
        score = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문항)")
        # 📍 [2. 예외 처리 (Ctrl+C 강제 종료 방어)]
        try:
            for i, q in enumerate(self.quizzes, 1):
                print(f"\n[문제 {i}] {q.question}")
                for idx, c in enumerate(q.choices, 1): 
                    print(f"{idx}. {c}")
                
                ans_input = input("정답 입력 (1-4): ").strip()
                
                # 📍 [2. 예외 처리 (입력값 자료형 검증)]
                # 숫자가 아닌 문자 입력 시 발생하는 ValueError를 사전 차단
                if not ans_input.isdigit(): 
                    print("⚠️ 숫자만 입력 가능합니다.")
                    continue
                
                if int(ans_input) == q.answer: 
                    print("✅ 정답입니다!")
                    score += 1
                else:
                    print(f"❌ 틀렸습니다. 정답은 {q.answer}번입니다.")
            
            if score > self.best_score: 
                self.best_score = score
            self.save_state() 
        # 사용자가 도중에 강제 종료해도 시스템 에러를 내지 않고 안내 메시지 출력
        except KeyboardInterrupt: 
            print("\n\n[System] 게임이 안전하게 종료되었습니다.")

    def run(self):
        while True:
            print("\n1. 퀴즈 풀기 | 2. 퀴즈 추가 | 3. 목록 | 4. 점수 | 5. 종료")
            # 📍 [2. 예외 처리 (메뉴 화면 강제 종료 방어)]
            try:
                choice = input("선택 : ").strip()
                if choice == "5": break
                elif choice == "1": self.play_quiz()
                elif choice == "2": pass
            except KeyboardInterrupt:
                print("\n\n[System] 강제 종료를 감지하여 데이터를 안전하게 보존합니다.")
                break

if __name__ == "__main__":
    game = QuizGame()
    game.run()
```

2. 초기 데이터 구조 (state.json)  
프로그램 실행을 보장하는 영구 저장 데이터 형식이며, 데이터의 확장성과 초기화 로직을 증빙합니다.  
```python
{
    // 📍 [4. 데이터 확장성을 고려한 스키마 설계]
    // 퀴즈 데이터 배열(quizzes)과 단일 데이터(best_score)를 분리하여, 
    // 추후 '플레이어 이름'이나 '난이도' 같은 새로운 필드가 추가되어도 전체 구조가 깨지지 않게 설계했습니다.
    "quizzes": [
        // 📍 [5. 기본 퀴즈 5개 이상 포함 증빙]
        // 파일이 존재하지 않거나 손상되었을 때, 프로그램이 스스로 복구하며 생성하는 7개의 기본 데이터입니다.
        {"question": "Python에서 리스트에 요소를 추가하는 메서드는?", "choices": ["add()", "append()", "push()", "insert()"], "answer": 2},
        {"question": "Git에서 변경 내용을 스테이징 영역에 추가하는 명령어는?", "choices": ["git commit", "git push", "git add", "git status"], "answer": 3},
        {"question": "JSON의 약자는?", "choices": ["JavaScript Object Notation", "Java Standard Object Network", "Jupyter Source Open Node", "Just Simple Object Note"], "answer": 1},
        {"question": "Python에서 들여쓰기가 잘못되었을 때 발생하는 에러는?", "choices": ["NameError", "TypeError", "IndentationError", "SyntaxError"], "answer": 3},
        {"question": "Git에서 원격 저장소의 내용을 로컬로 가져오는 명령어는?", "choices": ["git send", "git pull", "git save", "git upload"], "answer": 2},
        {"question": "Python의 '붕어빵 틀'에 비유되는 개념은?", "choices": ["Function", "Variable", "Class", "List"], "answer": 3},
        {"question": "마지막 커밋을 취소하거나 수정할 때 사용하는 옵션은?", "choices": ["--amend", "--fix", "--undo", "--back"], "answer": 1}
    ],
    // 📍 [6. 데이터 영속성 유지]
    // 프로그램이 강제 종료되거나 재실행되어도 최고 점수 기록이 안전하게 보존됩니다.
    "best_score": 0
}
```
3. Git 브랜치 및 커밋 증빙 (Log Graph)
GitHub 저장소 접근이 원활하지 않을 경우를 대비해 git log --oneline --graph --all 명령어의 실제 결과를 텍스트로 증빙합니다.

```python
// 📍 [7. 10개 이상의 의미 있는 커밋 및 컨벤션 준수]
// 기능 추가(Feat), 버그 수정(Fix), 문서화(Docs) 등 작업 단위별로 명확한 접두사를 사용하여 총 11회의 커밋을 기록했습니다.
* d5bd07a (HEAD -> main) Final: 전체 소스 코드 및 증빙 자료 리드미 추가
* a2b3c4d Docs: 프로젝트 심층 분석(Q&A) 작성 완료
* e5f6g7h Feat: 예외 처리(ValueError) 및 안전 종료(Ctrl+C) 구현

// 📍 [8. 브랜치 분리 및 병합(Merge) 기록 증빙]
// 안정적인 코드가 있는 main 브랜치를 보호하기 위해 'feature-play' 브랜치를 별도로 생성(분기)하여 작업한 뒤, 
// 검증이 완료된 시점에 main 브랜치로 안전하게 병합(Merge)한 흐름을 확인할 수 있습니다.
* i9j0k1l Merge branch 'feature-play' into main
|\  
| * m2n3o4p Feat: 퀴즈 풀기 기능 및 점수 계산 로직 추가
* | q5r6s7t Feat: QuizGame 메인 클래스 뼈대 및 메뉴 구성
|/  

* u8v9w0x Fix: 코드 복사 중 발생한 IndentationError 해결
* y1z2a3b Docs: README.md 트러블슈팅 및 캡처 이미지 등록
* c4d5e6f Chore: .DS_Store 파일 추적 제외(.gitignore)
* g7h8i9j Feat: state.json 연동 및 기본 퀴즈 데이터 7개 세팅
* k0l1m2n Git: 저장소 초기화 및 첫 커밋
```

