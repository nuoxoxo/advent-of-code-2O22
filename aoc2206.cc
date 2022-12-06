#include "iostream"
#include "vector"

using	namespace std;

int	main()
{
	vector<string>	a;
	string		s;
	int		n, i, j;
	int		r1, r2;

	while (cin >> s)
		a.push_back(s);

	bool	ok = false;
	int	p2 = 14;

	for (string& l : a)
	{

		i = -1;
		n = (int) l.length();
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
		while (++i < n - p2)
		{
			s = l.substr(i, p2);	
			sort(s.begin(), s.end());
			j = 0;
			ok = false;
			while (++j < p2 && !ok)
			{
				if (s[j - 1] == s[j])
				{
					ok = true;
					break ;
				}
			}
			if (!ok)
			{
				r2 = i + p2;
				break;
			}
		}
	}
	cout << "Star 1: " << r1 << endl;
	cout << "Star 2: " << r2 << endl;
}
