#include "iostream"
#include "vector"
#include "algorithm"

using	namespace std;

int	main()
{
	vector<int>	cl;
	string		s;
	int		r = 0;

	while (getline(cin, s))
	{
		if (s == "")
			cl.push_back(r);
		r = s == "" ? 0 : r + stoi(s);
	}
	sort(cl.begin(), cl.end(), greater<int>());
	cout << "Star 1: " << cl[0] << endl;
	cout << "Star 2: " << cl[0] + cl[1] + cl[2] << endl;
}
