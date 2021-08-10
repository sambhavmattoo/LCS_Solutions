#include <iostream>
#include <string>
#include <sdsl/suffix_arrays.hpp>
#include <sdsl/lcp_bitcompressed.hpp>
#include <sdsl/memory_management.hpp>

using namespace sdsl;
using namespace std;

class LCS {
	public:
		int length;
		int example_index_x;
		LCS() {
			length = 0;
			example_index_x = 0;
		}
};

// Uses bit-compressed vectors. These provide the best result in terms of access time as compared to WT's and storage based off psi fn's. They are more costly on the memory however.
// One possible improvement to this basic solution could be to use lcp_byte if m + n < 255 but bit-compression is still better than DAC.
LCS LCS_SA_LCP(string X, string Y) {
	
	// Initialize the Answer container.
	LCS Ans;

	// Initialize the size of the strings.
	int m = X.size();
	int n = Y.size();

	// Create the concatenated string with sentinel letters.
	string concat_string = X + "#" + Y + "$";

	// Create bit-compressed CSA.
	csa_bitcompressed <> SA;
	construct_im(SA, concat_string, 1);

	// Create bit-compressed LCP Array.
	lcp_bitcompressed <> LCP;
	construct_im(LCP, concat_string, 1);
	
	// Calculate LCS length and position.
	for(int i = 4; i < SA.size(); i++) {
		if (SA[i] < m && SA[i - 1] > m || SA[i] > m && SA[i - 1] < m) {
			if(LCP[i] > Ans.length) {
				Ans.length = LCP[i];
				if (SA[i] < m && SA[i - 1] > m) {
					Ans.example_index_x = SA[i];
				}
				else {
					Ans.example_index_x = SA[i - 1];
				}
			}
		}
	}

	return Ans;
}

int main() {
	
	// Just some driver code to test correctness. Commented code is a memory management system that outputs the time and memory usage in form of raw html code that can be saved to view.
	string X = "AAAGATTTACACAAGAACACG", Y = "GAGAGAAAATCGAAAG";
	//memory_monitor::start();
	LCS Ans = LCS_SA_LCP(X, Y);
	//memory_monitor::stop();
	//memory_monitor::write_memory_log <HTML_FORMAT> (cout);
	cout << Ans.length << endl;
	cout << Ans.example_index_x << endl;

	return 0;
}
