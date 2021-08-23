#물품 개수, 버틸수 있는 무게
n, k  =map(int, input().split(' '))

#matrix
mat = [[0 for i in range(k+1)] for j in range(n)]

for i in range(n):
  #물건의 무게, 물건의 가치
  w, v = map(int, input().split(' '))
  for j in range(k+1):
    if i == 0: #가방이 비었을 때
      if j >= w: #버틸수 있는 무게보다 물건의 무게가 작으면
        mat[i][j] = v #일단 추가한다.
    else:
      if j < w: #버틸수 있는 무게보다 물건의 무게가 큰 경우 넣지 않는다.
        mat[i][j] = mat[i-1][j]
      else: #여유가 있으면 새로운 물건을 넣었을 때 그게 더 가치가 있는지 따져본다.
        mat[i][j] = max(mat[i-1][j-w]+v , mat[i-1][j])

print(mat[-1][k])