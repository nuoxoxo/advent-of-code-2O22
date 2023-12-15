#include "iostream"
#include "vector"
#include "set"

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
			
			set<char>	ss(l.begin()+i, l.begin()+i+4);
			
			if (ss.size() == 4)
			{
				r1 = i + 4;
				break ;
			}
		}
		i = -1;
		while (++i < n - p2)
		{
			s = l.substr(i, p2);

			set<char>	ss(l.begin()+i, l.begin()+i+p2);
			
			if (ss.size() == p2)
			{
				r2 = i + p2;
				break ;
			}
		}
	}
	cout << "Star 1: " << r1 << endl;
	cout << "Star 2: " << r2 << endl;
}
