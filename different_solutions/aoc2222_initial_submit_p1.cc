#include "iostream"

#include "sstream"
#include "vector"
using	namespace std;

string	split_movement(string&);
bool str_is_number(const string&);

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
	
	// Find starting point
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
