#include "iostream"

#include "sstream"
#include "vector"
using	namespace std;

string	split_movement(string&);
bool str_is_number(const string&);

int	solve(vector<string> G, string& movement);
int	solve2(vector<string> G, string& movement);

int	main()
{
	vector<string> G;
	string s;
	int i;
	int R, C, W = 0;
	while (!cin.eof() && getline(cin, s))
	{
		if (s == "")
			break ;
		G.push_back(s);
		W = max((int) s.length(), W);
	}
	// cout << "(original grid) \n";
	// for (string &x: G) cout << x << endl;

	// fill lines with 0s
	for (string &x: G)
	{
		i = -1;
		int len = (int) x.length();
		while (++i < W - len)
			x += ' ';
	}
	// cout << "(trailing 0s filled)\n";
	// for (string &x: G) cout << x << endl;
	
	cin >> s;
	string movement = split_movement(s);
	// cout << "(movement parsed) \n";
	// cout << movement << " / len: " << W << endl;
	int res, res2;
	res = solve(G, movement);
	cout << "\nStar 1: " << res << endl;
	
	res2 = solve2(G, movement);
	cout << "\nStar 2: " << res2 << endl;
	// Find starting point
	/*
	int r = 0;
	int c = 0;
	while (G[0][c] != '.') ++c;
	cout << "(starting point) " << r << ' ' << c << endl;
	C = (int) G[0].size();
	R = (int) G.size();
	int dr = 0;
	int dc = 1; // current facing: East
	int rr, cc;
	stringstream ss(movement);
	while (!ss.eof() && ss >> s)
	{
		if (str_is_number(s))
		{

			int val = stoi(s);
			i = -1;
			while (++i < val)
			{
				rr = r;
				cc = c;
				while (1)
				{
					//rr = (dr + rr) % R;
					//cc = (dc + cc) % C;
					// again, buggy C++ modulo 
					// do this: (b + (a % b)) % b
					rr = (R + (dr + rr) % R) % R;
					cc = (C + (dc + cc) % C) % C;
					if (G[rr][cc] != ' ')
						break ;
				}
				if (G[rr][cc] == '#')
					break ;
				r = rr;
				c = cc;
			}
		}
		if (s == "L")
		{
			swap(dr, dc);
			dr *= -1;
		}
		if (s == "R")
		{
			swap(dr, dc);
			dc *= -1;
		}
	}
	cout << "(final facing) " << dr << ' ' << dc << endl;
	int x = -1;
	if (dr)
	{
		if (dr == 1)
			x = 1;
		else
			x = 3;
	}
	else
	{
		if (dc == 1)
			x = 0;
		else
			x = 2;
	}
	int res = 1000 * (r + 1) + 4 * (c + 1) + x;
	cout << "\nStar 1: " << res << ' ' << R << ' ' << C << endl;
	*/
}

//	part 2

int	solve2(vector<string> G, string& movement)
{
	int r = 0;
	int c = 0;
	while (G[0][c] != '.') ++c;
	cout << "(starting point) " << r << ' ' << c << endl;
	int C = (int) G[0].size();
	int R = (int) G.size();
	int dr = 0;
	int dc = 1; // current facing: East
	int i, rr, cc;
	string s;
	stringstream ss(movement);
	while (!ss.eof() && ss >> s)
	{
		if (str_is_number(s))
		{
			int val = stoi(s);
			i = -1;
			while (++i < val)
			{
				int ddr = dr;
				int ddc = dc;
				rr = r + dr;
				cc = c + dc;
				// Case: ba .. ab
				// upper ba...lower ab...moving left
				if (0 <= rr && rr < 50 && cc == 49 && dc == -1)
				{
					dc = 1;
					rr = 149 - rr;
					cc = 0;
				}
				// lower ab...upper ba...moving left
				if (100 <= rr && rr < 150 && cc < 0 && dc == -1)
				{
					dc = 1;
					rr = 149 - rr;
					cc = 50;
				}
				// Case: be ... be
				// upper be...lower be...moving on Up
				if (rr < 0 && 50 <= cc && cc < 100 && dr == -1)
				{
					dr = 0;
					dc = 1;
					rr = cc + 100;
					cc = 0;
				}
				// lower be...upper be...moving Left
				if (cc < 0 && 150 <= rr && rr < 200 && dc == -1)
				{
					dr = 1;
					dc = 0;
					cc = rr - 100;
					rr = 0;
				}
				// Case: eD ... eD
				// upper eD...lower eD...moving Up
				if (rr < 0 && 100 <= cc && cc < 150 && dr == -1)
				{
					rr = 199;
					cc = cc - 100;
				}
				// lower eD...upper eD...moving Down
				if (200 <= rr && 0 <= cc && cc < 50 && dr == 1)
				{
					rr = 0;
					cc += 100;
				}
				// Case: Dc ... cD
				// upper Dc...lower cD...moving Right (dc is 1 to be flipped)
				if (cc >= 150 && 0 <= rr && rr < 50 && dc == 1)
				{
					dc = -1;
					rr = 149 - rr;
					cc = 99;
				}
				// lower cD...upper Dc...moving right (dc 1 to -1)
				if (cc == 100 && 100 <= rr && rr < 150 && dc == 1)
				{
					dc = -1;
					rr = 149 - rr;
					cc = 149;
				}
				// Case: a...
				// a dotted-edge 45-clockwise . moving Up
				if (0 <= cc && cc < 50 && rr == 99 && dr == -1)
				{
					dr = 0;
					dc = 1;
					rr = cc + 50;
					cc = 50;
				}
				// a dotted-edge 45-counterclockwise . moving left
				if (cc == 49 && 50 <= rr && rr <= 100 && dc == -1)
				{
					dr = 1;
					dc = 0;
					cc = rr - 50;
					rr = 100;
				}
				// Case: D...
				// D dotted-edge 45-clockwise . moving down
				if (rr == 150 && 50 <= cc && cc < 100 && dr == 1)
				{
					dr = 0;
					dc = -1;
					rr = cc + 100;
					cc = 49;
				}
				// D dotted-edge 45-counterclockwise . moving right
				if (cc == 50 && 150 <= rr && rr < 200 && dc == 1)
				{
					dr = -1;
					dc = 0;
					cc = rr - 100;
					rr = 149;
				}
				// Case: c...
				// c dotted-edge 45-clockwise . moving down
				if (rr == 50 && 100 <= cc && cc < 150 && dr == 1)
				{
					dr = 0;
					dc = -1;
					rr = cc - 50;
					cc = 99;
				}
				// c dotted-edge 45-counterclockwise . moving right
				if (50 <= rr && rr < 100 && cc == 100 && dc == 1)
				{
					dr = -1;
					dc = 0;
					cc = rr + 50;
					rr = 49;
				}
				// hit the wall
				if (G[rr][cc] == '#')
				{
					dr = ddr;
					dc = ddc;
					break ;
				}
				r = rr;
				c = cc;
			}
		}
		if (s == "L")
		{
			swap(dr, dc);
			dr *= -1;
		}
		if (s == "R")
		{
			swap(dr, dc);
			dc *= -1;
		}
	}
	cout << "(final facing) " << dr << ' ' << dc << endl;
	int x = -1;
	if (dr)
	{
		if (dr == 1)
			x = 1;
		else
			x = 3;
	}
	else
	{
		if (dc == 1)
			x = 0;
		else
			x = 2;
	}
	int res = 1000 * (r + 1) + 4 * (c + 1) + x;
	cout << res << " at " << R << ',' << C << endl;
	return res;
}



//	part 1

int	solve(vector<string> G, string& movement)
{
	int r = 0;
	int c = 0;
	while (G[0][c] != '.') ++c;
	cout << "(starting point) " << r << ' ' << c << endl;
	int C = (int) G[0].size();
	int R = (int) G.size();
	int dr = 0;
	int dc = 1; // current facing: East
	int i, rr, cc;
	string s;
	stringstream ss(movement);
	while (!ss.eof() && ss >> s)
	{
		if (str_is_number(s))
		{

			int val = stoi(s);
			i = -1;
			while (++i < val)
			{
				rr = r;
				cc = c;
				while (1)
				{
					//rr = (dr + rr) % R;
					//cc = (dc + cc) % C;
					// again, buggy C++ modulo 
					// do this: (b + (a % b)) % b
					rr = (R + (dr + rr) % R) % R;
					cc = (C + (dc + cc) % C) % C;
					if (G[rr][cc] != ' ')
						break ;
				}
				if (G[rr][cc] == '#')
					break ;
				r = rr;
				c = cc;
			}
		}
		if (s == "L")
		{
			swap(dr, dc);
			dr *= -1;
		}
		if (s == "R")
		{
			swap(dr, dc);
			dc *= -1;
		}
	}
	cout << "(final facing) " << dr << ' ' << dc << endl;
	int x = -1;
	if (dr)
	{
		if (dr == 1)
			x = 1;
		else
			x = 3;
	}
	else
	{
		if (dc == 1)
			x = 0;
		else
			x = 2;
	}
	int res = 1000 * (r + 1) + 4 * (c + 1) + x;
	cout << res << " at " << R << ',' << C << endl;
	return res;
}

//

string	split_movement(string& s)
{
	stringstream ss(s);
	char c;
	string S;
	while (!ss.eof())
	{
		ss >> c;
		if (!(c <= '9' && c >= '0'))
		{
			S += c;
			S += ' ';
			continue ;
		}
		string temp;
		temp += c;
		while (1)
		{
			if (!(ss.peek() <= '9' && ss.peek() >= '0'))
				break ;
			ss >> c;
			temp += c;
			continue ;
		}
		S += temp;
		S += ' ';
	}
	return S;
}

bool str_is_number(const string & s)
{
    string::const_iterator it = s.begin();
    while (it != s.end() && isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}
