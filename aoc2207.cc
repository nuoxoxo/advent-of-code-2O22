#include "h.hpp"

bool	is_number(string &);

int	main()
{
	map<string, int> mp;
	map<string, int>::iterator it;
	vector<string>	a;
	vector<string>	lv; // current dir
	string		s;
	int		i, np;
	long long	ll;

	while (getline(cin, s))
		a.push_back(s);
	long long	r = 0;
	for (string & l: a)
	{
		stringstream	ss(l);
		string		n;

		ss >> n;
		/*
		if (is_number(n))
		{
			cout << "number - " << n << endl;
			long long t = stoll(n);
			cout << "number parsed - " << n << endl;
			if (t < 100000)
			{
				cout << "current - " << r << '+'<< endl;
				r = r + t;
				cout << "current - " << t << endl;
				cout << "current - " << r << endl;
			}
		}
		*/
		if (n == "$")
		{
			ss >> n;
			if (n != "cd")
				continue ;
			ss >> n;
			if (n == "..")
			{
				lv.pop_back();
			}
			else
			{
				lv.push_back(n);
			}
		}
		if (is_number(n))
		{
			cout << "number - " << n << endl;
			ll = stoll(n);
			//np = (int) lv;
			//cout << "number parsed - " << n << endl;
			
			mp["/"] += ll;
			i = 0;
			cout << lv.size() << endl;
			while (++i < (int) lv.size())
			{
				string	tmp = "/";
				int	ii = -1;
				while (++ii < i + 1)
				{
					tmp += lv[ii] + "/";
				}
				cout << tmp << endl;
				mp[tmp] += ll;
			}
		}
		/*
		if (n == "$")
		{
			ss >> n;
			if (n == "cd")
				cout << "cd - " << l << endl;
			if (n == "ls")
				cout << "ls - " << l << endl;
		}
		else
		{
			cout << "else - " << l << endl;
		}
		*/
	}
	it = mp.begin();
	while (it != mp.end())
	{
		cout << it->first << endl;
		if (it->second < 100000)
			r += it->second;
		it++;
	}
	cout << r << endl;
}

bool	is_number(string & s)
{
	string::iterator	it;

	it = s.begin();
	while (it != s.end() && isdigit(*it))
		++it;
	return !s.empty() && it == s.end();
}
