#include "iostream"
#include "sstream"
#include "vector"
#include "map"

using	namespace std;

bool	is_number(string &);

int	main()
{
	map<string, int>::iterator it;
	map<string, int> mp;
	vector<string>	a;
	vector<string>	lv; // current lvl
	string		s, sls = "/";
	int		i, np; // res;
	int		ii;
	long long	r;

	long long	ll, togo;
	long long 	top=4*(int)1e7;

	while (getline(cin, s))
		a.push_back(s);
	r = 0;
	for (string& l: a)
	{
		stringstream	ss(l);
		string		n;

		ss >> n;
		if (n == "$")
		{
			ss >> n;
			if (n != "cd")
				continue ;
			ss >> n;
			if (n == "..")
				lv.pop_back();
			else
				lv.push_back(n);
		}
		else if (is_number(n))
		{
			ll = stoll(n);
			i = 0;
			mp[sls] += ll;
			// cout << lv.size() << " levels" << endl;
			while (++i < (int) lv.size())
			{
				string	tmp = sls;
				
				ii = -1;
				while (++ii < i + 1)
					tmp += lv[ii] + sls;
				// cout << "composed: " << tmp << endl;
				mp[tmp] += ll;
			}
		}
	}

	long long	r2 = (int) 1e9;

	togo = mp[sls] - top;
	it = mp.begin();
	while (it != mp.end())
	{
		// cout << it->first << endl;
		
		if (it->second < 100000)
			r += it->second;
		if (it->second > togo)
			r2 = it->second < r2 ? it->second : r2;
		it++;
	}
	// cout << "\n";
	
	cout << "Star 1: " << r << endl;
	cout << "Star 2: " << r2 << endl;
}

bool	is_number(string &s)
{
	string::iterator	it;

	it = s.begin();
	while (it != s.end() && isdigit(* it))
		++it;
	return ( !s.empty() && it == s.end());
}
