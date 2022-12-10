#include "iostream"
#include "vector"
#include "sstream"

using	namespace std;

int	main()
{
	vector<int>	a;
	string		s;
	int		r1, n, x, cc, i, ii;
	int		len, row;
	string		r2;	

	while (getline(cin, s))
	{
		stringstream	ss(s);
		
		a.push_back(0);
		if (s == "noop")
			continue ;
		ss >> s >> n;
		a.push_back(n);
	}

	// part 1

	r1 = 0;
	x = 1; // X
	i = 0;
	len = (int) a.size();
	cc = 0; // cycle
	while (1)
	{
		if (i == len)
			i %= len;
		n = a[i];
		ii = i + 1;
		if (ii == 20 || ii % 40 == 20)
			r1 += ii * x;
		x += n;
		++i;
		++cc;
		if (cc == 220)
			break ;
	}

	// part 2

	x = 1;
	i = 0;
	cc = 0;
	r2 = "\n";
	while (1)
	{
		if (i == len)
			i %= len;
		row = i % 40;
		if (row == x - 1 || row == x || row == x + 1)
			r2 += '@';
		else
			r2 += ' ';
		if (!((i + 1) % 40))
			r2 += '\n';
		x += a[i];
		++i;
		++cc;
		if (cc == 240) // (?)
			break ;
	}
	cout << "Star 1: " << r1 << endl;
	cout << "Star 2: " << r2 << endl;
}
