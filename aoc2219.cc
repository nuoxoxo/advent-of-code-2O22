#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <tuple>
#include <deque>

using namespace std;
using State = tuple<int,int,int,int,int,int,int,int,int>;
//                   tt,ore,cly,obs,geo,rates

template <typename ... Params>
void print(const Params &... args)
{ sizeof...(args) ^ 0 ? ((cout << args << ' '), ..., (cout << '\n')) : (cout << '\n'); }

int BFS(int minutes,int oo,int cc,int oco,int occ,int gco,int gcc){
    int best = 0;
    State state = {minutes, 0,0,0,0, 1,0,0,0};
    deque<State> Q = {state};
    set<State> SEEN;
    while (!Q.empty()){
        State state = Q.front();
        Q.pop_front();
        auto [tt,ore,clay,obs,geo,ro,rc,robs,rg] = state;
        best = max(best,geo);
        if (!tt)
            continue ;
        int oremax = max({oo,cc,oco,gco});
        if (ro >= oremax) ro = oremax;
        if (rc >= occ) rc = occ;
        if (robs >= gcc) robs = gcc;
        int ORE = oremax * tt - ro * (tt - 1);
        int CLAY = occ * tt - rc * (tt - 1);
        int OBS = gcc * tt - robs * (tt - 1);
        ore = min(ore, ORE);
        clay = min(clay, CLAY);
        obs = min(obs, OBS);
        state = {tt,ore,clay,obs,geo,ro,rc,robs,rg};
        if (SEEN.find(state) != SEEN.end())
            continue ;
        SEEN.insert(state);
        Q.push_back({tt-1,ore + ro,clay + rc,obs + robs,geo + rg,ro,rc,robs,rg});
        if (ore >= oo)
            Q.push_back({tt-1,ore-oo+ro,clay+rc,obs+robs,geo+rg,ro+1,rc,robs,rg});
        if (ore >= cc)
            Q.push_back({tt-1,ore-cc+ro,clay+rc,obs+robs,geo+rg,ro,rc+1,robs,rg});
        if (ore >= oco && clay >= occ)
            Q.push_back({tt-1,ore-oco+ro,clay-occ+rc,obs+robs,geo+rg,ro,rc,robs+1,rg});
        if (ore >= gco && obs >= gcc)
            Q.push_back({tt-1,ore-gco+ro,clay+rc,obs-gcc+robs,geo+rg,ro,rc,robs,rg+1});
    }
    return best;
}

int main(){
    string line;
    int p1 = 0;
    int minutes = 0;
    int p2 = 1;
    int i = -1;
    vector<string> lines;
    while (getline(cin, line)){
        lines.push_back(line);
    }
    int N = lines.size();
    bool testing = (N == 2);
    while (++i < N){
        vector<int> n;
        int integer;
        stringstream ss(lines[i]);
        string temp;
        while (ss >> temp)
            if (stringstream(temp) >> integer)
                n.push_back(integer);
        int id,oo,cc,oco,occ,gco,gcc;
        id = n[0];
        oo = n[1];
        cc = n[2];
        oco = n[3];
        occ = n[4];
        gco = n[5];
        gcc = n[6];
        if ((testing && i == 1) || (!testing && i < 3)){
            p2 *= BFS(32,oo,cc,oco,occ,gco,gcc);
            print("p2/", p1);
        }
        p1 += id * BFS(24,oo,cc,oco,occ,gco,gcc);
        print(i,"p1/",p1,"\tp2/",p2);
    }
    print("part 1:",p1);
    print("part 2:",p2);
}
