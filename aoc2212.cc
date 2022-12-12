#include "h.hpp"

#define vvi vector<vector<int>>
#define vi vector<int>
#define vvc vector<vector<char>>
#define vc vector<char>
#define pi pair<int, int>

int	main()
{
	// vvc	a;
	vector<string>	a;
	char	ch;
	string	s;
	int	rs, re, cs, ce;
	vvi	D{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	//vvi	D{{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {1,-1}, {1,1},{-1,1},{-1,-1}};

	while (cin >> s)
	{
		/*stringstream	ss(s);
		vc		temp;
		while (ss >> c)	temp.push_back(c);
		for (char &c: temp){cout << c;} cout << endl;*/
		a.push_back(s);
	}
	int r = -1, c, R = (int) a.size(), C = (int) a[0].length();
	// map<vi, vvi>	mp;
	//map<pair<int, int>, vector<pair<int, int>>> mp;
	while (++r < R)
	{
		c = -1;
		while (++c < C)
		{
			if (a[r][c] == 'S') { rs = r, cs = c;}
			if (a[r][c] == 'E') { re = r, ce = c;}
			/*
			for (vector<int> d: D)
			{
				int rr = r + d[0];
				int cc = c + d[1];
				if (rr > R - 1 || rr < 0 || cc > C - 1 || cc < 0)
					continue ;
				if (a[rr][cc] <= a[r][c] + 1)
					mp[{r,c}].push_back({rr,cc});
			}
			*/
		}
	}
	cout << "(S,E):\n"<< rs<<',' <<cs<< '\n'<<re << ','<< ce<< "\n\n" ;
	int res = 0, len;
	vector<vector<bool>>	seen(R, vector<bool>(C));
	vector<vector<int>>	mp(R, vector<int>(C, 0));
	deque<pair<int, int>> dq;
	dq.push_back({rs, cs});
	
	a[rs][cs] = 'a';
	a[re][ce] = 'z';

	while (!dq.empty())
	{
		pi p = dq.front();
		dq.pop_front();
		r = p.first;
		c = p.second;
		if (seen[r][c])
			continue ;
		seen[r][c] = true;
		if (a[r][c] == 'E')
		{
			cout << mp[r][c] << endl;
			return 0;
		}
		for (vector<int>& d: D)
		{
			int rr = r + d[0];
			int cc = c + d[1];

			if (rr < 0 || rr > R - 1 || cc < 0 || cc > C - 1)
				continue ;
			//if (seen[rr][cc])
			//	continue ;
			if (a[rr][cc] == 'E')
			{
				cout << "end 2: " << mp[rr][cc] + 1 << endl;
				return 0;
			}
			if (a[r][c] - a[rr][cc] > 1)
				continue ;
			//seen[rr][cc] = true;
			dq.push_back({rr, cc});
			mp[rr][cc]++;
		}
	}		
}
