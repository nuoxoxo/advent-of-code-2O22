#include "h.hpp"

int	main()
{
	vector<string>	a;
	string		s;
	int		res = 0, res2 = 0, i;
	char	c;
	vector<deque<char>>	vd;


	while (getline(cin, s))
	{
		if (s == "")		break ;
		cout << s << endl;
		a.push_back(s);
	}
	stringstream	ss(a[a.size() - 1]);
	int	numc;
	while (!ss.eof() && ss >> numc) ;;
	cout << "total crates: " << numc << endl;
	i = -1;
	while (++i < numc) vd.push_back(deque<char>());
	cout << "length vd: " << vd.size() << endl;
	a.pop_back();
	for (string line : a)
	{
		i = 0;
		// 1st crate
		cout << "1st: " << line[1] << endl;
		if (line[1] <= 'Z' && line[1] >= 'A')
		{	vd[i].push_front(line[1]);
			cout << "1st added: " << vd[i].front() << endl;
		}
		while (++i < numc)
		{
			c = line[1 + 4 * i];
			cout << i+1 << "th: " << c << endl;	
			if (c <= 'Z' && c >= 'A')
				vd[i].push_front(c);
			//cout << i+1 << "th added: " << vd[i].front() << endl;
		}
	}
	i = -1;
	cout << "printing crates: " << endl;
	while (++i < numc)
	{
		for (char c: vd[i])
			cout << i << ": " << c << endl;
		cout << endl;
	}
	
	while (getline(cin, s))
	{
		int mov, from, to;
		sscanf(s.c_str(), "move %d from %d to %d", & mov, & from, & to);
		cout << mov << ' ' << from << ' ' << to << ' ' << endl;
		
		from--;
		to--;
		i = -1;
		while (++i < mov)
		{
			if (vd[from].empty())
				continue ;
			char 	n = vd[from].back();
			//if (!(n<= 'Z' && n >= 'A'))
			//	continue ;
			vd[from].pop_back();
			vd[to].push_back(n);
		}	
		int j = -1;
		while (++j < numc)
		{
			for (char c: vd[j])
				cout << j << ": " << c << endl;
			cout << endl;
		}
	}

	i = -1;
	while (++i < numc)
	{
		cout << vd[i].back();
	}
	cout << endl;

	// part 2

	

	//cout << "Star 1: " << res << endl;
	//cout << "Star 1: " << res2 << endl;
}
