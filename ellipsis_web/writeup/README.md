This challenge relies on exploiting a polyglot token attack in python-jwt 3.3.3, which was reported as a CVE from 2023.

More information can be found here:
- https://github.com/onhexgroup/Conferences/blob/main/Black%20Hat%20USA%202023%20slides/Tom%20Tervoort_Three%20New%20Attacks%20Against%20JSON%20Web%20Tokens.pdf
- https://github.com/davedoesdev/python-jwt/security/advisories/GHSA-5p8v-58qm-c7fp
- https://github.com/davedoesdev/python-jwt/commit/88ad9e67c53aa5f7c43ec4aa52ed34b7930068c9

See [solve.py](./solve.py) for an exploit script.

Flag: `DC256{1_g0od_JWT_l1brary_iS_pr0bably_en0ugh!}`