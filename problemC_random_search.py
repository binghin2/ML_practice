import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  

# machine learning 과제
# Problem A----------------------------------
# 랜덤서치는 30번 내외로 지정, initial point는 임의로 선택
# random direction은 P = 10 

# problem B----------------------------------
# 방향벡터 d (step size)의 크기를 서로 다른 2개의 값을 사용하라
# 그에 따라 output에 미치는 영향 기술

def cost_function(x):
    return x[0]**2 + x[1]**2 + 5*np.sin(2*x[1])
# return x[0]**2 + x[1]**2 란 f(x , y) = x^2+y^2 꼴의 2차함수임
# 과제의 함수는 x^2+y^2+5sin(2y)임 
# 초기값 설정
x_current = np.array([5.0, 5.0])
f_current = cost_function(x_current)

alpha_s = 0.2  # step size
alpha_l = 1.0  # long step size
z = 20  # 반복 횟수
n_directions = 10  # 한 번에 시도할 방향 수

# 탐색 경로 기록용
path = [x_current.copy()]

# 탐색 반복
for i in range(z):
    candidates = []
    
    # 여러 방향 샘플링 및 평가
    for j in range(n_directions):
        # 무작위 방향 생성 (단위 벡터로 정규화)
        direction = np.random.uniform(-1, 1, 2)
        direction /= np.linalg.norm(direction)

        # short step size 방향으로 이동한 후보점
        x_candidate_s = x_current + alpha_s * direction
        f_candidate_s = cost_function(x_candidate_s)

        candidates.append((f_candidate_s, x_candidate_s, 'short'))

        # long step size 방향으로 이동한 후보점
        x_candidate_l = x_current + alpha_l * direction
        f_candidate_l = cost_function(x_candidate_l)

        candidates.append((f_candidate_l, x_candidate_l, 'long'))
    
    # 후보들 중 가장 Cost가 낮은 방향 선택
    candidates.sort(key=lambda tup: tup[0])
    best_f, best_x, best_step = candidates[0]
    
    # 더 나은 경우에만 이동
    if best_f < f_current:
        x_current = best_x
        f_current = best_f
        print(f"Iter {i}: Move to {x_current}, Cost: {f_current}, Step size: {best_step}")
    
    path.append(x_current.copy())

# 경로를 numpy 배열로 변환
path = np.array(path)

# ----------------- 3D 시각화 ------------------
# x, y 값에 대한 메쉬 생성
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = cost_function([X, Y])

# 3D 플롯 생성
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Cost 함수 표면 그리기
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

# 탐색 경로를 3D로 그리기 (z축은 cost function 값)
path_z = [cost_function(p) for p in path]
ax.plot(path[:, 0], path[:, 1], path_z, marker='o', color='red', label='Search Path')

# 시작점, 끝점 강조
ax.scatter(path[0, 0], path[0, 1], path_z[0], color='blue', s=100, label='Start Point')
ax.scatter(path[-1, 0], path[-1, 1], path_z[-1], color='green', s=100, label='End Point (Best)')

# 축 라벨 및 제목
ax.set_title('Machine Learning Problem C')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Cost (z)')
ax.legend()

plt.show()
