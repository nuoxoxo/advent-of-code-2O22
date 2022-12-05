#include "iostream"
#include "vector"
#include "sstream"
#include "deque"

using	namespace std;

int	main()
{
	vector<string>		a;
	string			s;
	int			i;
	char			c;
	string			res1, res2;
	// int			res, res2;
	vector<deque<char>>	vd1, vd2;

	// 1st half of input - crates

	while (getline(cin, s))
	{
		if (s == "")
			break ;
		a.push_back(s);
	}

	stringstream	ss(a[a.size() - 1]);
	int		numc;

	while (!ss.eof() && ss >> numc)
		;;
	i = -1;
	while (++i < numc)
	{
		vd1.push_back(deque<char>());
		vd2.push_back(deque<char>());
	}
	a.pop_back();
	for (string line : a)
	{
		// 1st crate
		i = 0;
		if (line[1] <= 'Z' && line[1] >= 'A')	
		{
			vd1[i].push_front(line[1]);
			vd2[i].push_front(line[1]);
		}
		// subsequent crates
		while (++i < numc)
		{
			c = line[1 + 4 * i];
			if (!(c <= 'Z' && c >= 'A'))
				continue ;
			vd1[i].push_front(c);
			vd2[i].push_front(c);
		}
	}
	
	// 2nd half of input - operations
	
	while (getline(cin, s))
	{
		int	M, F, T;
		int	move, from, to;

		sscanf(s.c_str(), "move %d from %d to %d", & M, & F, & T);

		// part 1

		from = F - 1;
		to = T - 1;
		move = M;
		i = -1;
		while (++i < move)
		{
			if (vd1[from].empty())
				continue ;
			c = vd1[from].back();
			vd1[from].pop_back();
			vd1[to].push_back(c);
		}

		// part 2

		string		E;

		from = F - 1;
		to = T - 1;
		move = M;
		i = -1;
		while (++i < move)
		{
			if (vd2[from].empty())
				continue ;
			c = vd2[from].back();
			E += c;
			vd2[from].pop_back();
		}
		while (E != "")
		{
			c = E[E.length() - 1];
			E.pop_back();
			vd2[to].push_back(c);
		}
	}
	i = -1;
	while (++i < numc)
	{
		res1 += vd1[i].back();
		res2 += vd2[i].back();
	}
	cout << "Star 1: " << res1 << endl;
	cout << "Star 2: " << res2 << endl;
}
