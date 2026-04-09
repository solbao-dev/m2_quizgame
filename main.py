import json

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return str(self.answer) == str(user_answer)

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = 0

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()
        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            choices.append(choice)
        while True:
            answer = input("정답 번호 (1-4): ").strip()
            if answer in ['1', '2', '3', '4']:
                break
            print("⚠️ 잘못된 입력입니다. 1에서 4 사이의 숫자를 입력하세요.")
        new_quiz = Quiz(question, choices, int(answer))
        self.quizzes.append(new_quiz)
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")

    def show_list(self):
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        for i, quiz in enumerate(self.quizzes):
            print(f"[{i+1}] {quiz.question}")
        print("----------------------------------------")

    # 🌟 [새로운 기능 3] 대망의 퀴즈 풀기 기능!
    def play_quiz(self):
        if not self.quizzes: # 바구니에 퀴즈가 하나도 없으면 튕겨내기!
            print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요!")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0 # 내 점수는 0점부터 시작

        # 퀴즈 목록을 하나씩 꺼내서 보여주기
        for i, quiz in enumerate(self.quizzes):
            print("\n----------------------------------------")
            print(f"[문제 {i+1}] {quiz.question}")
            for j, choice in enumerate(quiz.choices):
                print(f"{j+1}. {choice}")

            # 정답 입력 받기 (방어막 포함)
            while True:
                user_answer = input("정답 입력 (1-4): ").strip()
                if user_answer in ['1', '2', '3', '4']:
                    break
                print("⚠️ 잘못된 입력입니다. 1~4 사이의 숫자를 입력하세요.")

            # 정답 확인하기
            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                score += 1 # 맞추면 1점 획득!
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)")

        # 결과 발표
        print("\n========================================")
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        
        # 최고 점수 갱신 로직
        if score > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score # 장부에 내 최고 점수 기록!
        print("========================================")

    def show_menu(self):
        try:
            while True:
                print("\n========================================")
                print("        🎯 솔바오의 코디세이 퀴즈 🎯        ")
                print("========================================")
                print("1. 퀴즈 풀기")
                print("2. 퀴즈 추가")
                print("3. 퀴즈 목록")
                print("4. 점수 확인")
                print("5. 종료")
                print("========================================")
                
                choice = input("선택: ").strip()

                if choice == '1':
                    self.play_quiz() # 🌟 아까 만든 퀴즈 풀기 기능 연결!
                elif choice == '2':
                    self.add_quiz()
                elif choice == '3':
                    self.show_list()
                elif choice == '4':
                    # 🌟 점수 확인 기능도 뽀너스로 연결해 뒀어요!
                    print(f"\n🏆 현재 최고 점수: {self.best_score}점") 
                elif choice == '5':
                    print("\n게임을 종료합니다. 수고했어요 솔바오! 👋")
                    break
                else:
                    print("\n⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 앗! 갑자기 나가셨군요. 데이터를 안전하게 보호하며 식당 문을 닫습니다. 안녕히 가세요! 👋")


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

if __name__ == "__main__":
    game = QuizGame(quiz_data)
    game.show_menu()
    