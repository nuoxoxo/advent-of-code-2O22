#include "iostream"
#include "vector"
#include "deque"
#include "algorithm"
#include "cstdlib" // abs

#define ll long long

using	namespace std;

// p1
// 5376 @ 611 > hi
// 5842 @ 613

ll	solve(vector<ll>&, vector<ll>&, ll, int);

int	main()
{
	ll res = 0, n, i;
	vector<ll> a, aa;
	vector<ll>::iterator it;
	while (!cin.eof() && cin >> n)
	{
		a.push_back(n);
		aa.push_back(n); // p2
	}
	n = a.size();
	vector<ll> idx, idxx;
	i = -1;
	while (++i < n)
	{
		idx.push_back(i);
		idxx.push_back(i); // p2
	}
	ll index, value, move2 = 0;
	ll t = -1, times = 1;
	while (++t < times)
	{
		i = -1;
		while (++i < a.size())
		{
			if ((it = find(idx.begin(), idx.end(), i)) == idx.end()) // assert !end
				return 0 ;
			index = it - idx.begin();
			value = a[index];
			a.erase(a.begin() + index);
			ll N = index + value;
			ll S = (int)a.size();
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
			/* cout << i
			<< ' ' << index
			<< ' ' << value
			<< ' ' << move2 // buggy part
			<< endl; */
			if (move2 == 0 && value)
				move2 = a.size();
			else if (move2 == a.size())
				move2 = 0;
			a.insert(a.begin() + move2, value);
			
			idx.erase(idx.begin() + index);
			idx.insert(idx.begin()+ move2, i);
		}
		i = find(a.begin(), a.end(), 0) - a.begin();
		res = a[(1000 + i) % a.size()] +
		a[(2000 + i) % a.size()] + a[(3000 + i) % a.size()];
		// cout << "index " << i << ": " << res << "\n\n";
	}

	// part 2
	ll res2 = solve(aa, idxx, 811589153, 10);

	cout << "Star 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;
}

ll	solve(vector<ll>& a, vector<ll>& idx, ll key, int times)
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
		while (++i < a.size())
		{
			if ((it = find(idx.begin(), idx.end(), i)) == idx.end()) // assert !end
				return 0 ;
			index = it - idx.begin();
			value = a[index];
			a.erase(a.begin() + index);
			ll N = index + value;
			ll S = (int)a.size();
			if (N < 0)
				N = (((S + N) % S) + S) % S;
			else
				N = N % (a.size());
			move2 = N;
			if (move2 == 0 && value)
				move2 = a.size();
			else if (move2 == a.size())
				move2 = 0;
			a.insert(a.begin() + move2, value);
			idx.erase(idx.begin() + index);
			idx.insert(idx.begin()+ move2, i);
		}
		i = find(a.begin(), a.end(), 0) - a.begin();
		res = a[(1000 + i) % a.size()] +
		a[(2000 + i) % a.size()] + a[(3000 + i) % a.size()];
	}
	return res;
}
