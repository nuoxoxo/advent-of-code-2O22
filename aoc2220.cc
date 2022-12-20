#include "iostream"
#include "vector"
#include "deque"
#include "algorithm"
#include "cstdlib" // abs
#include "cassert"

#define ll long long

using	namespace std;

// part 1 :: 5842 @ 613 . 5376 @ 611 > hi

ll	solve(vector<ll>, vector<ll>, ll, int);

int	main()
{
	ll n, i;
	vector<ll> a;
	while (!cin.eof() && cin >> n)
		a.push_back(n);
	n = a.size();
	vector<ll> idx;
	i = -1;
	while (++i < n)
		idx.push_back(i);
	ll key = 811589153;
	ll res = solve(a, idx, 1, 1);
	ll res2 = solve(a, idx, key, 10);

	assert(res == 3 || res == 1087);
	assert(res2 == 1623178306 || res2 == 13084440324666);

	cout << "Star 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;
}

ll	solve(vector<ll> a, vector<ll> idx, ll key, int times)
{
	for (long long& n: a)
		n *= key;
	ll index, value, move2 = 0;
	ll res = 0;
	ll t = -1, i;
	vector<ll>::iterator it;
	while (++t < times)
	{
		i = -1;
		while (++i < (int) a.size())
		{
			if ((it = find(idx.begin(), idx.end(), i)) == idx.end()) // assert !end
				return 0 ;
			index = it - idx.begin();
			value = a[index];
			a.erase(a.begin() + index);
			ll N = index + value;
			ll S = (long long) a.size();
			if (N < 0)
				N = (((S + N) % S) + S) % S;
			else
				N = N % (a.size());
			// N = abs(((int) a.size() + N) % (int) a.size()); // old way is buggy
			//	because in c++ modulo between 2 arguments of different
			//	signs gives language-specific results.
			//	a common fix it is :
			//		(b + (a % b)) % b
			move2 = N;
			if (move2 == 0 && value)
				move2 = (long long) a.size();
			else if (move2 == (long long) a.size())
				move2 = 0;
			a.insert(a.begin() + move2, value);
			idx.erase(idx.begin() + index);
			idx.insert(idx.begin()+ move2, i);
		}
		i = find(a.begin(), a.end(), 0) - a.begin();
		ll S = (long long) a.size();
		res = a[(1000 + i) % S] + a[(2000 + i) % S] + a[(3000 + i) % S];
	}
	return res;
}
