#include "h.hpp"

#define vvi vector<vector<int>>
#define vi vector<int>
#define vvc vector<vector<char>>
#define vc vector<char>
#define pi pair<int, int>

int	bfs(vector<string>, int, int, int, int);

int	main()
{
	vector<string>	a;
	string	s;
	while (cin >> s)
	{
		/*stringstream	ss(s);
		vc		temp;
		while (ss >> c)	temp.push_back(c);
		for (char &c: temp){cout << c;} cout << endl;*/
		a.push_back(s);
	}
	int	sr, er, sc, ec;
	vvi	D{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	//vvi	D{{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {1,-1}, {1,1},{-1,1},{-1,-1}};
	int	R = (int) a.size(), C = (int) a[0].length(), r = -1, c;
	// map<vi, vvi>	mp;
	//map<pair<int, int>, vector<pair<int, int>>> mp;
	while (++r < R)
	{
		c = -1;
		while (++c < C)
		{
			if (a[r][c] == 'S') { sr = r, sc = c;}
			if (a[r][c] == 'E') { er = r, ec = c;}
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
	//cout << "(S,E):\n"<< rs<<',' <<cs<< '\n'<<re << ','<< ce<< "\n\n" ;
	int res = bfs(a, sr, sc, er, ec);
	
	int res2 = (int) 1e9;
	r = -1;
	while (++r < R)
	{
		c = -1;
		while (++c < C)
		{
			if (a[r][c] != 'a')
				continue ;
			int B = bfs(a, r, c, er, ec);
			if (!B)
				continue ;
			// cout << res2 << ' ' << B << endl;
			res2 = min(res2, B);
		}
	}

	cout << "Star 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;



}

int	bfs(vector<string> a, int sr, int sc, int er, int ec)
{
	vvi	D{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	//vvi	D{{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {1,-1}, {1,1},{-1,1},{-1,-1}};
	int r = -1, c, R = (int) a.size(), C = (int) a[0].length();
	// map<vi, vvi>	mp;
	//map<pair<int, int>, vector<pair<int, int>>> mp;
	/*
	while (++r < R)
	{
		c = -1;
		while (++c < C)
		{
			//if (a[r][c] == 'S') { sr = r, sc = c;}
			//if (a[r][c] == 'E') { er = r, ec = c;}
			
			//for (vector<int> d: D) {
			//	int rr = r + d[0];
			//	int cc = c + d[1];
			//	if (rr > R - 1 || rr < 0 || cc > C - 1 || cc < 0)
			//		continue ;
			//	if (a[rr][cc] <= a[r][c] + 1)
			//		mp[{r,c}].push_back({rr,cc});
			//}
			
		}
	}*/
	
	int res = 0, len;
	vector<vector<bool>>	seen(R, vector<bool>(C, false));
	vector<vector<int>>	mp(R, vector<int>(C, 0));
	deque<pair<int, int>> dq;
	dq.push_back({sr, sc});

	a[sr][sc] = 'a';
	a[er][ec] = 'z';
	
	while (!dq.empty())
	{
		r = dq.front().first;
		c = dq.front().second;
		dq.pop_front();
		for (vector<int>& d: D)
		{
			int rr = r + d[0];
			int cc = c + d[1];
			if (rr < 0 || rr > R - 1 || cc < 0 || cc > C - 1)
				continue ;
			if (seen[rr][cc]) continue ;
			// cout << a[rr][cc] << a[r][c] << endl;
			if (a[rr][cc] - a[r][c] > 1)
				continue ;
			/*
			if (a[rr][cc] == 'E')
			{
				cout << mp[r][c] + 1 << endl;
				return 0;
			}
			*/
			mp[rr][cc] = mp[r][c] + 1;
			seen[rr][cc] = true;
			dq.push_back({rr, cc});
		}
		/*
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
		*/
	}
	// cout << mp[er][ec] << endl;
	return mp[er][ec] ;
}
