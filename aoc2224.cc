#include "iostream"
#include "fstream"
#include "vector"
#include "deque"
#include "set"

using namespace std;

const vector<vector<int>> D = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}, {0, 0}};
int Modulo(int, int);
int BFS(const vector<string> & , const pair<int, int> & , const pair<int, int> & ,int);

int main() {
    vector<string> a;
    string line;
    while (cin >> line)
        a.push_back(line);
    int R = (int)a.size(), C = (int) a[0].length();
    pair<int, int> pos_begin = {0, 1};
    pair<int, int> pos_end = {R - 1, C - 2};

    int res = BFS(a, pos_begin, pos_end, 0);

    int res2 = BFS(a, pos_end, pos_begin, res);
    res2 = BFS(a, pos_begin, pos_end, res2);

    cout << "Star 1: " << res << endl;
    cout << "Star 2: " << res2 << endl;
}

int Modulo(int a, int b) {
    if (a > 0)
        return a % b;
    return (a % b + b) % b;
}

int BFS(
    const vector<string> & a,
    const pair<int, int> & pos_begin,
    const pair<int, int> & pos_end,
    int t
) {
    int R = a.size();
    int C = a[0].size();
    set<pair<pair<int, int>, int>> seen;
    seen.insert(make_pair(pos_begin, t));

    deque<pair<int, pair<pair<int, int>, int>>> dq;
    dq.push_back(make_pair(0, make_pair(pos_begin, t)));

    int r_end = pos_end.first;
    int c_end = pos_end.second;
    int time = t;

    while (!dq.empty()) {

        auto node = dq.front();
        dq.pop_front();

        auto pos_curr = node.second.first;
        time = node.second.second;

        if (pos_curr == pos_end)
            return time;

        time += 1;
        int r = pos_curr.first;
        int c = pos_curr.second;

        for (const auto & dir : D) {
            int dr = dir[0];
            int dc = dir[1];
            int rr = r + dr;
            int cc = c + dc;
            if (cc < 1 || cc > C - 1 - 1)
                continue ;
            if (rr < 0 || rr > R - 1)
                continue ;
            if (rr == 0 && a[rr][cc] != '.')
                continue ;
            if (rr == R - 1 && a[rr][cc] != '.')
                continue ;
            if (a[rr][ Modulo(cc - 1 + time, (C - 2)) + 1] == '<')
                continue ;
            if (a[rr][ Modulo(cc - 1 - time, (C - 2)) + 1] == '>')
                continue ;
            if (a[ Modulo(rr - 1 + time, (R - 2)) + 1][cc] == '^')
                continue ;
            if (a[ Modulo(rr - 1 - time, (R - 2)) + 1][cc] == 'v')
                continue ;

            auto state = make_pair(make_pair(rr, cc), time);

            if (seen.find(state) == seen.end())
            {
                seen.insert(state);
                dq.push_back({
                    time + abs(rr - r_end) + abs(cc - c_end),
                    state
                });
            }
        }
    }
    return time;
}

