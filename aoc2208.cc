#include "iostream"
#include "vector"
#include "sstream"

using	namespace std;

int	main()
{
	vector<vector<int>>	a;
	string			s;

	while (cin >> s)
	{
		stringstream	ss(s);
		vector<int>	t;
		char		c;

		while (ss >> c)
			t.push_back(c - '0');
		a.push_back(t);
	}

	int	R = (int) a.size(), C = (int) a[0].size();
	int	i, j, r, c;
	int	peri = R * 2 + C * 2 - 4;
	int	res = peri;
	
	// part 2
	long long	res2 = 0, scen;
	int		u, d, l, rr;
	
	r = 0;
	while (++r < R - 1)
	{
		c = 0;	
		while (++c < C - 1)
		{
			int	n = a[r][c];
			bool	ok;
			
			i = -1; // up
			ok = true;
			while (++i < r)
			{
				if (a[i][c] >= n)
					ok = false;
			}
			if (ok)
			{
				res++;
				continue ;
			}
			i = r; // down
			ok = true;
			while (++i < R)
			{
				if (a[i][c] >= n)
					ok = false;
			}
			if (ok)
			{
				res++;
				continue ;
			}
			ok = true;
			i = -1; // left
			while (++i < c)
			{
				if (a[r][i] >= n)
					ok = false;
			}
			if (ok)
			{
				res++;
				continue ;
			}
			ok = true;
			i = c; // right
			while (++i < C)
			{
				if (a[r][i] >= n)
					ok = false;
			}
			if (ok)
			{
				res++;
				continue ;
			}
		}

		// part 2
		
		c = 0;
		while (++c < C - 1)
		{
			int	n = a[r][c];
			
			u = 0;
			i = r;
			while (--i > -1)
			{
				u++;
				if (a[i][c]>=n)
					break;
			}
			d = 0;
			i = r;
			while (++i < R)
			{
				d++;
				if (a[i][c]>=n)
					break;
			}
			l = 0;
			i = c;
			while (--i > -1)
			{
				l++;
				if (a[r][i]>=n)
					break;
			}
			rr = 0;
			i = c;
			while (++i < C)
			{
				rr++;
				if (a[r][i]>=n)
					break ;
			}
			scen = u * d * l * rr;
			res2 = res2 > scen ? res2 : scen;
		}
	}

	cout << "Star 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;
} 
