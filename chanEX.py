import numpy as np
import matplotlib.pyplot as plt

# 파라미터 설정
q0 = 0      # 초기 위치
qf = 1      # 종료 위치
T = 1.0     # 종료 시간

# 시간 벡터 생성 (0 <= t <= T)
t = np.linspace(0, T, 200)

# 5차 다항식 (위치 프로파일)
q = q0 + (qf - q0) * (10*(t/T)**3 - 15*(t/T)**4 + 6*(t/T)**5)

# 속도 프로파일 (위치의 1차 미분)
dq = np.gradient(q, t)

# 가속도 프로파일 (속도의 1차 미분)
ddq = np.gradient(dq, t)

# 그래프 그리기
plt.figure(figsize=(10, 6))

plt.subplot(3,1,1)
plt.plot(t, q, 'b-', linewidth=2)
plt.title('5차 다항식 경로 생성')
plt.ylabel('위치 q(t)')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, dq, 'r-', linewidth=2)
plt.ylabel('속도 q\'(t)')
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, ddq, 'g-', linewidth=2)
plt.xlabel('시간 t')
plt.ylabel('가속도 q\'\'(t)')
plt.grid(True)

plt.tight_layout()
plt.show()
