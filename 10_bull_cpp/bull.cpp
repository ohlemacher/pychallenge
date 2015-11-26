
/*
 * solution 10: bull
 */

#include <iostream>
#include <sstream>
#include <vector>
#include <regex>
#include <cassert>

#include "bull.h"

using namespace std;

/*
 *
 */
string Bull::lookAndSay(string seed) {
    string seq = seed;

    vector<string> say;
    char lastFirst('x');

    for (int j(0); j<seq.length(); j++) {
        char first(seq[j]);

        // Skip repeats of lastFirst
        if (first == lastFirst) {
            continue;
        }

        string rest(seq.substr(j));
        // Build a new regex searching for one or more 'first' chars.
        stringstream ssPattern;
        ssPattern <<
            "^(" <<
            first <<
            "+)";
        regex pat(ssPattern.str());

        // Search greedily for first char(s)
        smatch matches;
        if (regex_search(rest, matches, pat)) {
            string thisMatch = matches.str(1);
            if (0) {
                cout << "match: "
                    << ssPattern.str() << ": "
                    << first << ": "
                    << rest << ": "
                    << thisMatch
                    << endl;
            }
            // Add the matching length to say.
            stringstream sslen;
            sslen << thisMatch.length();
            say.push_back(sslen.str());
            // Add the matching single char to say
            stringstream ssThisMatch;
            ssThisMatch << thisMatch.c_str()[0];
            say.push_back(ssThisMatch.str());
            // Save the new lastFirst
            lastFirst = thisMatch.c_str()[0];
        } else {
            cerr << "Error: no match: "
                << ssPattern.str() << ": "
                << first << ": "
                << rest << ": "
                << endl;
            assert(0);
        }
    }
    string out;
    for (auto iter(say.begin()); iter!=say.end(); iter++) {
        out += *iter;
    }
    return out;
}

int Bull::lenAfterNIters(int iterations) {
    string seed("1");
    for (int i(0); i<iterations; i++) {
        seed = lookAndSay(seed);
    }
    return seed.length();
}

int main(int argc, char** argv) {
    int iterations(30);

    Bull bull;
    int lenAfterN(bull.lenAfterNIters(iterations));

    cout << "length after "
        << iterations
        << " iterations: "
        << lenAfterN
        << endl;

    return 0;
}

