#include "iostream"
#include "utility"
#include "vector"
#include "deque"

using	namespace std;

int	bfs(vector<string>, int, int, int, int);
int	bfs2(vector<string>, int, int);

int	main()
{
	vector<string>	a;
	string	s;
	int	R, C, sr, er, sc, ec, r = -1, c;
	int	res, res2;//, B;

	while (cin >> s)
	{
		a.push_back(s);
	}
	C = (int) a[0].size();
	R = (int) a.size();
	while (++r < R)
	{
		c = -1;
		while (++c < C)
		{
			if (a[r][c] == 'S') { sr = r, sc = c;}
			if (a[r][c] == 'E') { er = r, ec = c;}
		}
	}
	
	a[sr][sc] = 'a';
	a[er][ec] = 'z';
	
	// part 1
	res = bfs(a, sr, sc, er, ec);
	
	// part 2
	res2 = bfs2(a, er, ec);

	cout << "Star 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;
}


int	bfs2(vector<string> a, int er, int ec)
{
	int R = (int) a.size(), C = (int) a[0].length();
	int res = (int) 1e9 ;
	int r = -1, c, rr, cc;

	vector<vector<int>>	D{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	vector<vector<bool>>	seen(R, vector<bool>(C, false));
	vector<vector<int>>	mp(R, vector<int>(C, 0));
	deque<pair<int, int>>	dq;

	dq.push_back({er, ec});
	while (!dq.empty())
	{
		r = dq.front().first;
		c = dq.front().second;
		dq.pop_front();
		for (vector<int>& d: D)
		{
			rr = r + d[0];
			cc = c + d[1];
			if (rr < 0 || rr > R - 1 || cc < 0 || cc > C - 1)
				continue ;
			if (a[rr][cc] == 'a' && mp[rr][cc])
				res = min(res, mp[rr][cc]);
			if (seen[rr][cc])
				continue ;
			if (a[r][c] - a[rr][cc] > 1)
				continue ;
			/*
			cout << "next: " << rr << ' ' << cc << ' ';
			cout << a[rr][cc] << " - ";
			cout << "curr: " << r << ' ' << c << ' ';
			cout << a[r][c] << endl;
			*/
			seen[rr][cc] = true;
			mp[rr][cc] = mp[r][c] + 1;
			dq.push_back({rr, cc});
		}
	}
	return res;
}

int	bfs(vector<string> a, int sr, int sc, int er, int ec)
{
	int R = (int) a.size(), C = (int) a[0].length();
	int r = -1, c;
	int res = 0;

	vector<vector<int>>	D{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	vector<vector<bool>>	seen(R, vector<bool>(C, false));
	vector<vector<int>>	mp(R, vector<int>(C, 0));
	deque<pair<int, int>>	dq;

	dq.push_back({sr, sc});
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
			if (seen[rr][cc])
				continue ;
			if (a[rr][cc] - a[r][c] > 1)
				continue ;
			mp[rr][cc] = mp[r][c] + 1;
			seen[rr][cc] = true;
			dq.push_back({rr, cc});
		}
	}
	res = mp[er][ec];
	return (res ? res : -1);
}
