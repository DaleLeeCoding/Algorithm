//https://www.acmicpc.net/problem/1463
#include<bits/stdc++.h>

using namespace std;
int box[1000001];
int main()
{
	int num;
	scanf("%d", &num);
	for (int i = 0; i <= num; i++)
	{
		box[i] = 999999999;
	}
	for (int i = num; i > 0; i--)
	{
		box[num] = 0;
		if (i % 3 == 0) box[i / 3] = min({ box[i / 3], box[i] + 1 });
		if (i % 2 == 0) box[i / 2] = min({ box[i / 2], box[i] + 1 });
		box[i - 1] = min({ box[i - 1], box[i] + 1 });
	}
	printf("%d", box[1]);
	return 0;
}
