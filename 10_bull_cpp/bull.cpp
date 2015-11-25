
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <regex>
#include "bull.h"

using namespace std;

Bull::Bull() {
    cout << "Bull" << endl;
}

Bull::~Bull() {
}

string Bull::lookAndSay(int seed) {
    // Read the seed into a string
    stringstream ss;
    ss << seed;
    string seq = ss.str();

    vector<char> say;
    char lastFirst('x');

    for (int j(0); j<seq.length(); j++) {
        char first(seq[0]);
        if (first == lastFirst) {
            continue;
        }
        string rest(seq.substr(j));

        stringstream pat_ss;
        pat_ss <<
            "" <<
            "1" <<
            "";
        regex pat (".*"); //pat_ss.str());
        smatch matches;
        if (regex_search(rest, matches, pat)) {
            cout << "match: "
                << pat_ss.str() << ": "
                << first << ": "
                << rest
                << endl;
        } else {
            cerr << "no match: "
                << pat_ss.str() << ": "
                << first << ": "
                << rest << ": "
                << endl;
        }
    }
    return "done";
}

int main(int argc, char** argv) {
    cout << "10:  Bull" << endl;
    Bull bull;
    bull.lookAndSay(1112111);

    //string s0 = "abcdef";
    //string s1 = s0.substr(2);
    //cout << s1 << endl;
    return 0;
}
