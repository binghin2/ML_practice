import numpy as np
import matplotlib.pyplot as plt

# 예시 2차원 Cost Function (볼록한 형태: 최소값은 (0,0))
def cost_function(x):
    return x[0]**2 + x[1]**2
# return x[0]**2 + x[1]**2 란 f(x , y) = x^2+y^2 꼴의 2차함수임

# 초기값 설정
x_current = np.array([5.0, 5.0])
f_current = cost_function(x_current)


alpha = 0.5  # step size
n_iterations = 50  # 반복 횟수
n_directions = 20  # 한 번에 시도할 방향 수

# 탐색 경로 기록용
path = [x_current.copy()]

# 탐색 반복
for i in range(n_iterations):
    candidates = []
    
    # 여러 방향 샘플링 및 평가
    for j in range(n_directions):
        # 무작위 방향 생성 (단위 벡터로 정규화)
        direction = np.random.uniform(-1, 1, 2)
        direction /= np.linalg.norm(direction)

        # 해당 방향으로 이동한 후보점
        x_candidate = x_current + alpha * direction
        f_candidate = cost_function(x_candidate)

        candidates.append((f_candidate, x_candidate))
    
    # 후보들 중 가장 Cost가 낮은 방향 선택
    candidates.sort(key=lambda tup: tup[0])
    best_f, best_x = candidates[0]
    
    # 더 나은 경우에만 이동
    if best_f < f_current:
        x_current = best_x
        f_current = best_f
        print(f"Iter {i}: Move to {x_current}, Cost: {f_current}")
    
    path.append(x_current.copy())

# 경로를 numpy 배열로 변환
path = np.array(path)

# --------------시각화--------------------
# 등고선 플롯을 위한 x, y 메쉬 생성 
x = np.linspace(-10, 6, 100)
y = np.linspace(-10, 6, 100)
X, Y = np.meshgrid(x, y)
Z = cost_function([X, Y])

# 등고선 그리기
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour)

# 탐색 경로 플롯
plt.plot(path[:, 0], path[:, 1], marker='o', color='red', label='Search Path')
plt.scatter(path[0, 0], path[0, 1], color='blue', label='Start Point', s=100)
plt.scatter(path[-1, 0], path[-1, 1], color='green', label='End Point (Best)', s=100)

# 제목과 라벨
plt.title('Enhanced Random Search in 2D (Multiple Directions)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
