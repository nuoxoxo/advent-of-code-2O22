#include "_.hpp"

int	main()
{
	vector<string>	a;
	string	line;
	while (cin >> line && !cin.eof())
	{
		cout << line << endl;
		a.push_back(line);
	}
	for(string s: a) cout << s << endl;
}
