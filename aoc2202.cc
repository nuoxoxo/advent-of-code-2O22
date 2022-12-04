#include "iostream"
#include "sstream"
#include "map"

using	namespace std;

int	main()
{
	string	 	s;
	int		res = 0;
	map<char, int>	m{{'A',1}, {'B',2}, {'C',3}, {'X', 1}, {'Y', 2}, {'Z', 3}};

	int		res2 = 0;

	while (getline(cin, s))
	{
		stringstream	ss(s);
		char		L, R;
		int		l, r, rr;

		ss >> L >> R;
		l = m[L];
		r = m[R];

		//	part 1

		if (l == r)
			res += r + 3;
		else
		{
			res += r;
			rr = l + 1;
			if (rr > 3)
				rr = 1;
			if (rr == r)
				res += 6;
		}

		//	part 2

		if (r == 2)
			res2 += l + 3;
		else if (r == 1)
		{
			--l;
			if (l < 1)
				l = 3;
			res2 += l;
		}
		else // assert 3
		{
			++l;
			if (l > 3)
				l = 1;
			res2 += l + 6;
		}
	}
	cout << "Star 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;
}
