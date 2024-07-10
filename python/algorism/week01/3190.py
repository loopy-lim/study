N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
moves = [list(input().split()) for _ in range(L)]
boards = [0 for _ in range(N)] * N

seconds = 0
snake = [1, 1]
snake_trunk = []
snake_length = 1
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_direction = 1


def move(snake, direction):
    return [snake[0] + directions[direction][0], snake[1] + directions[direction][1]]


def check_collision_snake(snake, arr):
    for i, a in enumerate(arr):
        if snake[0] == a[0] and snake[1] == a[1]:
            return True, i
    return False, -1


while True:
    # print(seconds, snake_trunk, snake)
    if len(moves) > 0 and int(moves[0][0]) <= seconds:
        if moves[0][1] == "D":
            cur_direction = (cur_direction + 1) % len(directions)
        else:
            cur_direction = (cur_direction + 3) % len(directions)
        moves.pop(0)

    snake = move(snake, cur_direction)
    seconds += 1

    if check_collision_snake(snake, snake_trunk)[0]:
        # print("snake collapse error", check_collision_snake(snake, snake_trunk))
        break
    if snake[0] > N or snake[0] <= 0 or snake[1] > N or snake[1] <= 0:
        # print("wall collepse error", seconds, snake_trunk, snake)
        break

    snake_trunk.append(snake)
    while len(snake_trunk) > snake_length:
        snake_trunk.pop(0)

    is_connect_apple, apple_index = check_collision_snake(snake, apples)
    if is_connect_apple:
        snake_length += 1
        apples.pop(apple_index)

print(seconds)
