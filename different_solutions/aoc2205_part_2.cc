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
	string			res, res2;
	// int			res, res2;
	vector<deque<char>>	vd;

	// 1st half of input - piles

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
		vd.push_back(deque<char>());
	a.pop_back();
	for (string line : a)
	{
		i = 0;
		// 1st crate
		if (line[1] <= 'Z' && line[1] >= 'A')
			vd[i].push_front(line[1]);
		// subsequent crates
		while (++i < numc)
		{
			c = line[1 + 4 * i];
			if (c <= 'Z' && c >= 'A')
				vd[i].push_front(c);
		}
	}

	// 2nd half of input - operations
	
	// part 2 only

	while (getline(cin, s))
	{
		int	mov, from, to;

		sscanf(s.c_str(), "move %d from %d to %d", &mov, &from, &to);
		--from;
		--to;
		i = -1;

		// from here on, part 2 diffs from part 1

		string		E;

		while (++i < mov)
		{
			if (vd[from].empty())
				continue ;
			c = vd[from].back();
			E += c;
			vd[from].pop_back();
		}
		while (E != "")
		{
			c = E[E.length() - 1];
			E.pop_back();
			vd[to].push_back(c);
		}
	}
	i = -1;
	while (++i < numc)
		res2 += vd[i].back();

	cout << "Star 1: " << res << endl;
	cout << "Star 2: " << res2 << endl;
}
