// Literal translation of elves' program to bad C++ for speed.
using namespace std;
#include <iostream>
#include <set>

int main(void) {
	set<int> seen;
	unsigned int r1=0, r2=0, r3=0, r4=0;
	unsigned int prev;
i5:	r1 = 0;
i6:	r4 = r1 | 65536;
i7:	r1 = 12772194;
i8:	r3 = r4 & 255;
i9:	r1 += r3;
i10:	r1 &= 16777215;
i11:	r1 *= 65899;
i12:	r1 &= 16777215;
i13:	r3 = (256 > r4);
i14:	if (r3) goto i16;
i15:	goto i17;
i16:	goto i28;
i17:	r3 = 0;
i18:	r2 = r3 + 1;
i19:	r2 *= 256;
i20:	r2 = (r2 > r4);
i21:	if (r2) goto i23;
i22:	goto i24;
i23:	goto i26;
i24:	r3++;
i25:	goto i18;
i26:	r4 = r3;
i27:	goto i8;
i28:	if (seen.count(r1) > 0) {
		cout << prev << endl;
		return 0;
	}
	prev = r1;
	seen.insert(r1);
	r3 = 0;
i29:	;
i30:	goto i6;
}
