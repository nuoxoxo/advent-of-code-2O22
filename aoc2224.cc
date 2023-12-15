#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <set>
#include <tuple>

using namespace std;

const vector<vector<int>> D = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}, {0, 0}};

int Modulo(int a, int b) {
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
    // seen.insert({pos_begin, time});

    deque<pair<int, pair<pair<int, int>, int>>> dq;
    dq.push_back(make_pair(0, make_pair(pos_begin, t)));
    // dq.push_back({0, {pos_begin, time}});

    int r_end = pos_end.first;
    int c_end = pos_end.second;
    int time = t;

    while (!dq.empty()) {

        auto node = dq.front();
        dq.pop_front();
        auto pos_curr = node.second.first;
        time = node.second.second;

        if (pos_curr == pos_end) {
            return time;
        }

        time += 1;
        int r = pos_curr.first;
        int c = pos_curr.second;

        cout << "(pre dir) \n";
        for (const auto  dir : D) {
            int dr = dir[0];
            int dc = dir[1];
            int rr = r + dr;
            int cc = c + dc;
            cout << rr << ' ' << cc << endl;
            cout << "dir:" << dir[0] << ' ' << dir[1] << endl;
            cout << "checking modulo 1: " << cc - 1 + time << ' ' << C - 2 + 1 << endl;
           
            /*
            if ((cc - 1 + time) % (C - 2) + 1 > C) {
                cout
                << rr << ' '
                << cc << ' ' 
                << a[rr][cc] << ' '
                << (cc - 1 + time) % (C - 2) + 1 << ' ' 
                << (rr - 1 + time) % (R - 2) + 1
                << endl;
            }
            cout << "checking modulo 2: " << rr - 1 + time << ' ' << R - 2 + 1 << endl;
            if ((rr - 1 + time) % (R - 2) + 1 > R) {
                cout
                << rr << ' '
                << cc << ' ' 
                << a[rr][cc] << ' '
                << (cc - 1 + time) % (C - 2) + 1 << ' ' 
                << (rr - 1 + time) % (R - 2) + 1
                << endl;
            }
            */
            if (cc < 1 || cc > C - 1 - 1) {
                cout << "here 1\n";
                continue ;
            }
            if (rr < 0 || rr > R - 1) {
                cout << "here 2\n";
                continue;
            }

            if (rr == 0 && a[rr][cc] != '.') {
                cout << "here 3\n";
                continue;
            }
            if (rr == R - 1 && a[rr][cc] != '.') {
                cout << "here 4\n";
                continue;
            }

            if (a[rr][ Modulo(cc - 1 + time, (C - 2) + 1)] == '<') {
            //if (a[rr][(cc - 1 + time) % (C - 2) + 1] == '<') {
                cout << "here 5\n";
                continue;
            }
            if (a[rr][ Modulo(cc - 1 - time, (C - 2) + 1)] == '>') {
            // if (a[rr][(cc - 1 - time) % (C - 2) + 1] == '>') {
                cout << "here 6\n";
                continue;
            }

            if (a[ Modulo(rr - 1 + time, (R - 2) + 1)][cc] == '^') {
            // if (a[(rr - 1 + time) % (R - 2) + 1][cc] == '^') {
                cout << "here 7\n";
                continue;
            }
            if (a[ Modulo(rr - 1 - time, (R - 2) + 1)][cc] == 'v') {
            // if (a[(rr - 1 - time) % (R - 2) + 1][cc] == 'v') {
                cout << "here 8\n";
                continue;
            }
            cout << "(mid)\n";
            auto state = make_pair(make_pair(rr, cc), time);
            if (seen.find(state) == seen.end()) {
                seen.insert(state);
                dq.push_back({
                    time + abs(rr - r_end) + abs(cc - c_end),
                    state
                });
            }
            cout << "(bottom) \n";
        }
    }

    return time;
}

int main() {
    int fd = 0; // 1
    vector<string> a;
    string line;
    while (cin >> line) {
        a.push_back(line);
        cout
        << line << ' '
        << line.length() << ' '
        << line[0] << ' '
        << (int)line[line.length() - 1]
        << endl;
    }

    int R = (int)a.size(), C = (int) a[0].length();
    pair<int, int> pos_begin = {0, 1};
    pair<int, int> pos_end = {R - 1, C - 2};

    cout << R <<  ' ' << C << endl;

    int res = BFS(a, pos_begin, pos_end, 0);
    int res2 = BFS(a, pos_end, pos_begin, res);
    res2 = BFS(a, pos_begin, pos_end, res2);
    cout << "Star 1: " << res << endl;
    cout << "Star 2: " << res2 << endl;

    return 0;
}

