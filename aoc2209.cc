#include "iostream"
#include "set"
#include "vector"
#include "map"
#include "sstream"

using	namespace std;

int	main()
{
	vector<pair<char, int>>	a;
	string			s;
	char			c;
	int			n, i, j;

	while (getline(cin, s) && !cin.eof())
	{
		stringstream	ss(s);

		ss >> c >> n;
		a.push_back({c, n});
	}
	
	// part 1

	int			ex = 0, ey = 0, hx = 0, hy = 0, times;
	set<vector<int>>	seen({vector<int>({0, 0})});
	map<char, vector<int>>	dp = 
				{{'U', {0, 1}}, {'D', {0, -1}},
				{'L', {-1, 0}}, {'R', {1, 0}}};

	// part 2: (prep)
	
	set<vector<int>>	seen2({vector<int>({0, 0})});
	vector<vector<int>>	tt;

	i = -1;
	while (++i < 10)
		tt.push_back(vector<int>({0, 0}));
	// (end prep)
	
	for (pair<char, int>& p: a)
	{
		c = p.first;
		times = p.second;
		
		// part 1
		i = -1;
		while (++i < times)
		{
			hx += dp[c][0];
			hy += dp[c][1];
			if (abs(hx - ex) < 2 && abs(hy - ey) < 2)
				continue ;
			// head
			if (abs(ex - hx))
			{
				if (ex < hx)
					++ex;
				else
					--ex;
			}
			// tail
			if (abs(ey - hy))
			{
				if (ey < hy)
					++ey;
				else
					--ey;
			}
			seen.insert(vector<int>({ex, ey}));
		}

		// part 2
		i = -1;
		while (++i < times)
		{
			tt[0][0] += dp[c][0];
			tt[0][1] += dp[c][1];
			j = 0;
			while (++j < 10)
			{
				vector<int>	R( {tt[j][0], tt[j][1]} );
				vector<int>	L( {tt[j - 1][0], tt[j - 1][1]} );

				if (!(abs(R[0] - L[0]) == 2 || abs(R[1] - L[1]) == 2))
					continue ;
				if (abs(L[0] - R[0]))
				{
					if (L[0] > R[0])
						++R[0];
					else
						--R[0];
				}
				if (abs(L[1] - R[1]))
				{
					if (L[1] > R[1])
						++R[1];
					else
						--R[1];
				}
				tt[j][0] = R[0];
				tt[j][1] = R[1];
			}
			seen2.insert(vector<int>({tt[9][0], tt[9][1]}));
		}
	}
	cout << "Star 1: " << seen.size() << endl;
	cout << "Star 2: " << seen2.size() << endl;
}
