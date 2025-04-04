# ML_practice

## Random Search Algorithm


### A) ProblemA_random_search.py
$f(x, y) = x^2+y^2+5sin(2y)$ 꼴의 함수
step size = 0.5
iterations = 20
directions = 10

### B) ProblemB_random_search.py
$f(x, y) = x^2+y^2+5sin(2y)$ 꼴의 함수
step size = 0.5
direction인 방향벡터를 
d와 2d 2개의 수로 나누어, 값을 비교 한 후 
cost function이 낮은 쪽을 선택하여
random search algorithm을 진행함
방향벡터가 많아진다면, 속도는 저하될지언정 정확도가 높아진다고 판단함.

### C) ProblemC_random_search.py
$f(x, y) = x^2+y^2+5sin(2y)$ 꼴의 함수
step size alpha 를 
alpha_s = 0.2
alpha_l = 1.0
으로 2개의 값으로 설정하여, 
그에 따른 cost function을 비교하고, 낮은 값으로 이동하여 
최종적인 random search algorithm을 진행함
parameter 이 다르게 계산을 진행한다면, 값을 비교하여 이동하기 때문에 정확도가 높아진다고 판단함.


 



