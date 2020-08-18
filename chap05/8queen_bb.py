# 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8  # 각 열에서 퀸의 우치
flag = [False] * 8  # 각 행에서 퀸을 배치했는지 체크


def put() -> None:
    # 각 열에 배치된 퀸의 위치를 출력
    for i in range(8):
        print(f'{pos[i] : 2}', end='')
    print()


def set(i: int) -> None:
    # i열의 알맞은 위치에 퀸 배치
    for j in range(8):
        if not flag[j]:  # j행에 퀸을 배치하지 않았으면
            pos[i] = j

            if i == 7:
                put()
            else:
                flag[j] = True
                set(i + 1)
                flag[j] = False


set(0)
