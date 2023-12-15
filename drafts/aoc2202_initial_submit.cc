#include "iostream"
#include "sstream"
#include "map"
#include "cctype"

using	namespace std;

/*
a b c
x y z

R P S

0 3 6
1 2 3
*/

int	main()
{
	string	 	s;
	int		res = 0;
	char 		a = 'a', b = 'b', c = 'c';
	map<char, int>	m{{a,1}, {b,2}, {c,3}};

	int		res2 = 0;

	while (getline(cin, s))
	{
		stringstream	ss(s);
		char		l, r, rr;

		ss >> l >> r;
		l = tolower(l);
		r = tolower(r) - ('x' - 'a');

		//	part 1

		if (l == r) // draw
		{
			res += m[r] + 3;
		}
		else // not draw
		{
			res += m[r];
			rr = l + 1;
			if (rr > c)
				rr = a;
			if (rr == r)
				res += 6;
		}

		//	part 2

		if (r == b) // draw
		{
			res2 += m[l] + 3;
		}
		else if (r == a) // l;ose
		{
			--l;
			if (l < a)
				l = c;
			res2 += m[l];
		}
		else if (r == c) // win
		{
			++l;
			if (l > c)
				l = a;
			res2 += m[l] + 6;
		}
	}
	cout << "Star 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;
}
