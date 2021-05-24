//https://www.acmicpc.net/problem/1158

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <queue> 
using namespace std;

int main() {

	int n, k;
	int temp;

	cin >> n >> k;

	queue<int>q;
	for (int i = 1; i < n+1; i++) {
		q.push(i);
	}
	cout << "<";

	while (q.empty() == 0) {
		for (int j = 0; j < k -1; j++) {
			temp = q.front();
			q.pop();
			q.push(temp);
		}
		cout << q.front() ;

		q.pop();
		if (q.empty() != 0) cout << ">";

		else cout << ", ";
	}

	return 0;
	
}

