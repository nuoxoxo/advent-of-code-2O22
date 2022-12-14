#include "h.hpp"

int	main()
{
	vector<string>	a;
	string		s;

	while (cin >> s)
	{
		a.push_back( s );
		cout << s << endl;
	}
	cout << "(" << a.size() << " lines)\n";
}
