# 매칭 대기열에는 현재 NN 명의 유저가 있다. 편의상 유저는 번호가 11부터 NN까지 차례대로 매겨져 있다. 점수가 SS인 새로운 유저가 매칭을 요청했다. 매칭 시스템을 구현하기 위해서 새로 들어온 유저와 실력 점수가 가장 가까운 KK 명의 유저를 찾아보려고 한다.
#
# 실력 점수가 가깝다는 것은 실력 점수 차이가 작다는 것을 의미한다. 만약, 새로운 유저와 실력 점수 차이가 동일한 유저가 여러 명이라면 실력 점수가 낮은 유저가 더 가깝다고 생각하자.
#
# 입력 형식
# 첫 줄에 대기열에 있는 유저의 수를 나타내는 정수 NN이 주어진다. (1 <=leq 500<=000)(1≤N≤500 000)
# 둘째 줄에 새로 들어온 유저의 실력 점수를 나타내는 정수 SS와 찾아야 하는 유저의 수를 나타내는 정수 KK가 공백으로 구분되어 주어진다. (1 \leq S \leq 100\ 000\ 000;(1≤S≤100 000 000; 1 \leq K \leq N)1≤K≤N)
# 셋째 줄에 대기열에 있는 유저들의 실력 점수를 나타내는 NN 개의 정수가 공백으로 구분되어 주어진다. ii 번째로 주어지는 수는 ii 번 유저의 실력 점수를 의미한다. 이때, 주어지는 점수는 SS를 포함하여 모두 다르며, 11 이상 100\ 000\ 000100 000 000 이하다.
#
#
#
# 출력 형식
# 첫 줄에 새로운 유저의 실력 점수와 가장 가까운 유저 KK 명의 번호를 공백으로 구분하여 출력한다. 이때, 번호는 임의의 순서로 출력해도 된다.
# 이거임

import sys

def Samediff(a,b):
    if a<b :
        return a;
    else :
        return b;

first = sys.stdin.readline()#(1≤N≤500 000) 대기열 유저수 NN
second =list(map(int ,sys.stdin.readline().split()))#(1≤S≤100 000 000;1≤K≤N) 새로 들어온 유저의 실력 점수 SS 유저수 KK 공백으로 구분
third = list(map(int, sys.stdin.readline().split()))
