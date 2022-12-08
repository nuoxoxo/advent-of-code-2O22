#include "h.hpp"

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
	int	peri = R * 2 + C * 2 - 4;
	int	i, j, r, c;
	int	res = 0;
	long long	res2 = 0;
	r = 0;
	while (++r < R - 1)
	{
		c = 0;
		int u, d, l, ri;
		while (++c < C - 1)
		{
			int	n = a[r][c];
			bool	ok;
			cout << "pos: "<< r << ' ' << c << endl;
			i = -1; // up
			ok = true;
			while (++i < r)
			{

				if (a[i][c] >= n)
					ok = false;
			}
			if (ok) { res++; cout<<"u: "<<r<<' '<<c<<' '<<n<<endl; continue ;}
			i = r; // down
			ok = true;
			while (++i < R)
			{
				if (a[i][c] >= n)
					ok = false;
			}


			if (ok) { res++; cout<<"d: "<<r<<' '<<c<<' '<<n<<endl; continue ;}
			ok = true;
			i = -1; // left
			while (++i < c)
			{
				if (a[r][i] >= n)
					ok = false;
			}

			if (ok) { res++; cout<<"l: "<<r<<' '<<c<<' '<<n<<endl; continue ;}
			ok = true;
			i = c; // right
			while (++i < C)
			{
				if (a[r][i] >= n)
					ok = false;
			}
			if (ok) { res++; cout<<"r: "<<r<<' '<<c<<' '<<n<<endl; continue ;}


			long long temp = u * d * l * ri;
			cout << "score : "<< temp << endl;
			res2 = res2 > temp ? res2 : temp;

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
			cout << "(u)(score) : " << u;

			d = 0;
			i = r;
			while (++i < R)
			{
				d++;
				if (a[i][c]>=n)
					break;
			}
			cout << " (d)(score) : " << d << endl;

			l = 0;
			i = c;
			while (--i > -1)
			{
				l++;
				if (a[r][i]>=n)
					break;
			}
			cout << "(l)(score) : " << l ;

			ri = 0;
			i = c;
			while (++i < C)
			{
				ri++;
				if (a[r][i]>=n)
					break ;
			}
			cout << " (r)(score) : " << ri << endl;

			long long temp = u * d * l * ri;
			cout << temp << endl;
			res2 = res2 > temp ? res2 : temp;
		}
		
		/*
		c = 0;
		while (++c < C - 1)
		{
			int	n = a[r][c];
			i = r;
			u = 0; // u
			while (-- i > -1)
			{
				if (a[i][r] <= n)
					u++;
				if (a[i][r] > n)
					break ;
			}
			i = r;
			d = 0; // down
			while (++i < R)
			{
				if (a[i][r] <= n)
					d++;
				if (a[i][r] > n)
					break ;
			}
			i = c;
			l = 0; // left
			while (--i > -1)
			{
				if (a[r][i] <= n)
					l++;
				if (a[r][i] > n)
					break ;
			}
			i = c;
			ri = 0; // u
			while (++i < C)
			{
				if (a[r][i] <= n)
					ri++;
				if (a[r][i] > n)
					break ;
			}
			long long temp = u * d * l * ri;
			res2 = temp > res2 ? temp : res2;
			cout << u << ' ' << d << ' ' << l << ' ' << ri << endl ;
			cout << "p2 = " << u * d * l * ri << endl ;
		}
		*/
	}
	cout << res << ' ' << peri << ' ' << res+peri << endl;
	cout << res2 << endl;
} 
