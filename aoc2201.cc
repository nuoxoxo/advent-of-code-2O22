#include "iostream"
#include "vector"

#include "algorithm"

using	namespace std;

int	main()
{
	vector<int>	cl;
	string		s;
	int		n = 0;

	while (getline(cin, s))
	{
		if (s == "")
		{
			cl.push_back(n);
			n = 0;
		}
		else
		{
			n += stoi(s);
		}
	}

	n = *max_element(cl.begin(), cl.end());
	cout << "Star 1: " << n << endl;

	sort(cl.begin(), cl.end(), greater<int>());
	n = cl[0] + cl[1] + cl[2];
	cout << "Star 2: " << n << endl;
}
