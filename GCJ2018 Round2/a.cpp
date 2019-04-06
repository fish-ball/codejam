#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main() {
    int C;
    cin >> C;
    for (int c = 1; c <= C; ++c) {
        printf("Case #%d: ", c);
        int N;
        cin >> N;
        vector<int> A(N);
        for (int i = 0; i < N; ++i) cin >> A[i];
        // Only fail case
        if (!A[0] || !A[N-1]) {
            printf("IMPOSSIBLE\n");
            continue;
        }

        int result = 0;
        int l = 0;
        vector<pair<int, int>> V(0);
        for (int i = 0; i < N; ++i) {
            if (A[i]) {
                V.push_back(make_pair(i, l));
                result = max(result, max(abs(i-l), abs(l+A[i]-i-1)));
                l += A[i];
            }
        }
        printf("%d\n", result+1);

        for (int k = 0; k < result; ++k) {
            string s(N, '.');
            for (int i = 0; i < V.size(); ++i) {
                int left = V[i].second;
                int middle = V[i].first;
                int right = V[i].second + A[middle] - 1;
                if (left + k < middle) s[left+k] = '\\';
                if (right - k > middle) s[right-k] = '/';
            }
            puts(s.c_str());
        }
        puts(string(N, '.').c_str());
    }
}
