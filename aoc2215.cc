#include "iostream"
#include "set"
#include "utility"
#include "vector"
#include "map"

using	namespace std;

int	man(int a, int b, int c, int d) {return (abs(a - c) + abs(b - d));}

int	main()
{
	vector<pair<int, int>>	clo, sen;
	set<pair<int, int>>	occupied, B;
	set<pair<int, int>>	S; // p2
	map<pair<int, int>,int>	M; // p2
	string			s;
	int	i, Y;// = 10;// 2000000
	int	a, b, c, d, x, res, D;//, i;
	long long res2;

	Y = 10;
	Y = 2000000;
	while (getline(cin, s))
	{
		sscanf(s.c_str(),
			"Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d",
			&a, &b, &c, &d);
		cout << a<< ' '<< b<< ' '<< c<< ' '<< d << endl;
		sen.push_back({a, b});
		clo.push_back({c, d});
	}
	i = -1;
	while (++i < (int) clo.size())
	{
		a = sen[i].first;
		b = sen[i].second;
		c = clo[i].first;
		d = clo[i].second;
		D = abs(a - c) + abs(b - d);
		x = a - D - 1;
		while (++x < a + D + 1)
		{
			if (man(a, b, x, Y) < D + 1)
				occupied.insert({x, Y});
		}
		B.insert({c, d});
		S.insert({a, b}); // p2
		M[{a, b}] = D; // p2
	}
	int len = (int) occupied.size();
	int contain = 0;
	set<pair<int, int>>::iterator it = B.begin();
	while (it != B.end())
	{
		a = it->first;
		b = it->second;
		if (occupied.find({a,b}) != occupied.end())
			++contain;
		++it;
	}
	res = len - contain;
	cout << "\n@ y=10: " << res;
	cout << "\n(" << len << " occupied spots.)";
	cout << "\n(" << B.size() << " unique beacons.) \n" << endl;

	// part 2
	
	vector<vector<int>> dirs = {{1, 1}, {1, -1}, {-1, 1},{-1, -1}};
	
	it = S.begin();
	int bound = (int) 4e6 + 1;
	while (it != S.end())
	{
		//int sx = it->first;
		//int sy = it->second;
		a = it->first;
		b = it->second;
		d = M[{a, b}];
		int x = -1;
		while (++x < d + 2)
		{
			int y = d - x + 1;
			for (vector<int>& v: dirs)
			{
				int xx = a + x * v[0];
				int yy = b + y * v[1];
				int ok;
				if (!(xx < bound && xx > -1 && yy <= bound && yy > -1))
					continue ;
				ok = 1;
				set<pair<int, int>>::iterator it2 = S.begin();
				while (it2 != S.end())
				{
					int aa = it2->first;
					int bb = it2->second;
					int dd = man(aa, bb, xx, yy);
					D = M[{aa, bb}];
					if (dd <= D)
					{
						ok = 0;
						break ;
					}
					++it2;
				}
				if (!ok)
					continue ;
				res2 = (long long) xx * (bound-1) + (long long) yy;
				cout << "END: " << xx << ' ' << yy << ' '
				<< res2 << endl;
				break ;
			}
			// test: looking for 56000011 at 14 11
		}
		++it;
	}
	cout << "\nStar 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;
}
