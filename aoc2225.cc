#include "iostream"
#include "iomanip"
#include "assert.h"
#include "cstdint"
#define ll long long

using	namespace std;

void	reverse_string(string& s)
	{ int n=(int)s.length(), i=-1; while(++i < n/2) swap(s[i], s[n-i-1]); }

int	main()
{
	ll tt = 0;
	string base5 = "=-012";
	string line;
	int count = 0;
	// int place_value; // bug
	ll place_value;
	while (!cin.eof() && cin >> line)
	{
		place_value = 1;
		reverse_string(line);
		for (char c: line)
		{
			int value = base5.find(c);
			assert (value != std::string::npos);
			tt += (value - 2) * place_value;
			place_value *= 5;
		}
		cout << setfill('0') << setw(3) << count++;
		cout << ' ' << tt << '\n';
	}
	string res = "";
	ll dec = tt;
	ll remainder;
	while (tt)
	{
		remainder = tt % 5;
		tt /= 5;
		if (remainder > 2)
		{
			assert (remainder == 3 || remainder == 4);
			char sign = "=-"[remainder - 3];
			res = sign + res;
			++tt;
		}
		else
		{
			res = (char)(remainder + '0') + res;
		}
	}
	cout << "\nStar 1: " << res;
	cout << "\ndecimal " << dec << endl;
	assert (dec == 4890	|| dec == 35617696411945);
	assert (res == "2=-1=0"	|| res == "2-2=21=0021=-02-1=-0");
}
