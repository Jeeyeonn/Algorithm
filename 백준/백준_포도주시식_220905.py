n = int(input())
array = [0]*10000
for i in range(n):
  array[i] = int(input())

d = [0]*10000

d[0] = array[0]
d[1] = array[0]+array[1]
d[2] = max(array[2]+array[0], array[2]+array[1], d[1])

# 만약 N번째 일 경우 경우의 수는 3가지
# 1) i번째 wine을 안 먹는 경우 -> 이 경우 [i-1]까지의 최대 와인섭취 결과를 그대로 이어간다.
#
# 2) i번째 wine을 먹고, i-1번째 와인은 안먹는 경우
#
#    ->이 경우 [i-2]까지의 결과에 i번째 wine의 양을 더해준다.
#
# 3) i번째 wine을 먹고, i-1번째 와인도 먹은 경우
#
#    -> 이 경우 [i-3]까지의 결과에 i번째 wine, i-1번째 wine의 양을 더해준다.

for i in range(3, n):
  d[i] = max(array[i]+d[i-2], array[i]+array[i-1]+d[i-3], d[i-1])

print(d[n-1])
