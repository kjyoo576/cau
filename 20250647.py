import random
import time

def play():
    print("=== 구구단 게임 (10문제) ===")
    total_score = 0
    for i in range(10):
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        correct = a * b
        print()
        print(f"문제 {i+1}: {a} x {b} = ?")
        start_time = time.time()
        answer = int(input("답 입력: "))
        end_time = time.time()
        elapsed = end_time - start_time
        elapsed_rounded = round(elapsed, 3)
        print(f"풀이 시간: {elapsed_rounded:.3f}초")

        if answer == correct and elapsed <= 3.0:
            elapsed_score = int(elapsed_rounded * 1000)
            score = 3000 - elapsed_score
            total_score += score
            print(f"정답! {score}점 획득")
        elif answer == correct and elapsed > 3.0:
            print("시간 초과")
        else:
            print(f"오답! 정답은 {correct}입니다.")

        print(f"현재점수 : {total_score}점")

    print()
    print(f"=== 라운드 종료! 총 점수: {total_score} ===")
    print()

    return total_score

###########################################################################

board = [0, 0, 0, 0, 0, 0]

while True:
    board[5] = play()
    board.sort(reverse=True)
    for i in range(5):
        print(f"{i+1}등 {board[i]}점")
    print()

    again = input("계속 하시겠습니까? (y/n): ").strip().lower()
    print()
    if again != 'y':
        print("게임을 종료합니다.")
        break