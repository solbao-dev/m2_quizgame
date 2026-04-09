# Quiz 클래스: 퀴즈 붕어빵을 찍어내는 '틀' 역할을 해요!
class Quiz:
    # 붕어빵이 갓 구워질 때 문제, 선택지, 정답을 세팅해 줍니다.
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용
        self.choices = choices    # 선택지 4개 (리스트 형태)
        self.answer = answer      # 정답 번호 (1~4)

    # 정답이 맞는지 확인해 주는 기능(메서드)이에요.
    def check_answer(self, user_answer):
        return str(self.answer) == str(user_answer)

# 기본 퀴즈 데이터 5개 구워내기! (코디세이 특별판✨)
quiz_data = [
    Quiz("1. 코디세이 미션에서 강조하는, 프로그래밍 언어를 배우는 가장 확실한 방법은 무엇일까요?", 
         ["문법 달달 외우기", "동작하는 프로그램을 처음부터 끝까지 직접 만들기", "유명한 강의 반복해서 보기", "남이 짠 코드 복사하기"], 2),
         
    Quiz("2. 미션 2에서 퀴즈 문제들을 쉽게 찍어내기 위해 우리가 만든 '붕어빵 틀'의 파이썬 문법 이름은 무엇일까요?", 
         ["변수(Variable)", "함수(Function)", "클래스(Class)", "리스트(List)"], 3),
         
    Quiz("3. 프로그램을 껐다 켜도 솔바오의 퀴즈 데이터와 점수가 날아가지 않게 보존해 주는 파일의 확장자는?", 
         [".txt", ".pdf", ".json", ".png"], 3),
         
    Quiz("4. 방금 전 로컬(내 컴퓨터)에 있는 파일들을 인터넷(GitHub)으로 쏘아 올릴 때 사용했던 마법의 명령어는?", 
         ["git clone", "git add", "git commit", "git push"], 4),
         
    Quiz("5. 우리가 GitHub에 첫 집터(저장소)를 만들 때, 충돌 에러를 막기 위해 절대 체크하지 않았던 것은?", 
         ["Public 설정", "Repository name", "Add a README file", "Create 버튼"], 3)
]


# 코드가 잘 작동하는지 테스트용으로 첫 번째 문제만 살짝 출력해 볼게요!
if __name__ == "__main__":
    print("🎯 퀴즈 데이터 세팅 완료!")
    print(quiz_data[0].question)
    for i, choice in enumerate(quiz_data[0].choices):
        print(f"{i+1}. {choice}")

