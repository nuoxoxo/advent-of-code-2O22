#include "_.hpp"

int	main()
{
	vector<pair<int, int>>	clo, sen;
	set<pair<int, int>>	occupied, B;
	string			s;
	int	i, Y;// = 10;// 2000000
	int	a, b, c, d, D;//, i;

	Y = 10;
	Y = 2000000;
	while (getline(cin, s))
	{
		// int	a, b, c, d, D, i;
		sscanf(s.c_str(),
			"Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d",
			&a, &b, &c, &d);
		cout << a << ' ' << b << ' ' << c << ' ' << d << endl;
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
		int ii = a - D - 1;
		while (++ii < a + D + 1)
		{
			if (abs(a - ii) + abs(b - Y) <= D)
			// if (abs(a - ii) + abs(b - Y) <= D)
				occupied.insert({ii, Y});
		}
		// B.insert({a, b});
		B.insert({c, d});
	}
	int len = (int) occupied.size();
	int contain = 0;
	// for (pair<int, int>& pos: clo)
	set<pair<int, int>>::iterator it = B.begin();
	while (it != B.end())
	{
		a = it->first;
		b = it->second;
		if (occupied.find({a,b}) != occupied.end())
			++contain;
		++it;
	}
	cout << len - contain << endl;
	cout << len << ' ' << B.size() << endl;
}
