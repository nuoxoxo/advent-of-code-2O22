#include "iostream"
#include "vector"
#include "string"

using	namespace std;

int	calc(char c);

int	main()
{
	vector<string>	v;
	string		ss;
	int		x;
	int		r = 0;
	int		r2 = 0;

	while (cin >> ss)
		v.push_back(ss);
	x = -1;
	while (++x < (int) v.size())
	{
		string	s = v[x];
		int	len = (int) s.length();
		int	c;
		int	i, j;
		bool	ok = false, ok2 = false;

		i = -1;
		while (++i < len / 2 && !ok)
		{
			c = s[i];
			j = len / 2 - 1;
			while (++j < len && !ok)
			{
				if (c == s[j])
				{
					r += calc(c);
					ok = true;
				}
			}
		}

		//	part 2

		if (x > (int) v.size() - 3 || x % 3)
			continue ;

		string	n = v[x + 1]; // next
		string	nn = v[x + 2]; // next next

		i = -1;
		ok = false;
		ok2 = false;
		while (++i < len && !(ok && ok2))
		{
			int		it;
			
			ok = false;
			ok2 = false;

			c = s[i];
			it = n.find((char) c);
			if (it ^ string::npos)
				ok = true;
			it = nn.find((char) c);
			if (it ^ string::npos)
				ok2 = true;
			if (ok && ok2)
				r2 += calc(c);
		}
	}
	cout << "Star 1: " << r << endl;
	cout << "Star 2: " << r2 << endl;
}

int	calc(char c)
{
	if (c <= 'z' && c >= 'a')
		return c - 'a' + 1;
	else
		return c - 'A' + 27;
}
