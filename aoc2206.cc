#include "h.hpp"

int	main()
{
	vector<string>	a;
	string		s;
	int		n, i, j;
	int		r1, r2;

	int		p = 4;
	int		p2 = 14;

	while (cin >> s)
	{
		a.push_back(s);
	}
	for (string& l : a)
	{
		bool ok = false;
		
		n = (int) l.length();
		i = -1;
		while (++i < n - 4)
		{
			s = l.substr(i, 4);	
			sort(s.begin(), s.end());
			j = 0;
			ok = false;
			while (++j < 4 && !ok)
			{
				if (s[j - 1] == s[j])
				{
					ok = true;
					break ;
				}
			}
			if (!ok)
			{
				r1 = i + 4;
				break;
			}
		}
		i = -1;
		ok = false;
		while (++i < n - 4)
		{
			s = l.substr(i, 4);	
			sort(s.begin(), s.end());
			j = 0;
			while (++j < 4 && !ok)
			{
				if (s[j - 1] == s[j])
				{
					ok = true;
					break ;
				}
			}
			if (!ok)
			{
				r1 = i + 4;
				break;
			}
		}
	}
}
