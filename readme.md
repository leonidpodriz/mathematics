# Mathematics

```text
==================================== REPORT ====================================
A = {5, 8, 9, 12, 13, 16, 18, 19, 20}
q = { (a, b): a is A, b is A, |a - b| mod 4 = 0 } = {(16, 20), (20, 8), (12, 16), (20, 20), (5, 13), (9, 5), (8, 12), (13, 5), (16, 16), (20, 16), (12, 12), (5, 9), (8, 8), (9, 13), (8, 20), (13, 13), (16, 12), (18, 18), (20, 12), (12, 8), (5, 5), (12, 20), (9, 9), (8, 16), (19, 19), (13, 9), (16, 8)}
Matrix view of q: 
[[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1]
 [0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1]
 [0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1]]
D(q) = {5, 8, 9, 12, 13, 16, 18, 19, 20}
E(q) = {5, 8, 9, 12, 13, 16, 18, 19, 20}
q^-1 = {(16, 20), (20, 8), (12, 16), (20, 20), (5, 13), (9, 5), (8, 12), (13, 5), (16, 16), (20, 16), (12, 12), (5, 9), (8, 8), (9, 13), (8, 20), (16, 12), (13, 13), (18, 18), (20, 12), (12, 8), (5, 5), (12, 20), (9, 9), (8, 16), (19, 19), (13, 9), (16, 8)}
(Composition) q * q^-1 = {(16, 20), (20, 8), (12, 16), (20, 20), (5, 13), (9, 5), (8, 12), (13, 5), (16, 16), (20, 16), (12, 12), (5, 9), (8, 8), (9, 13), (8, 20), (16, 12), (13, 13), (18, 18), (20, 12), (12, 8), (5, 5), (12, 20), (9, 9), (8, 16), (19, 19), (13, 9), (16, 8)}
(Composition) q^-1 * q = {(16, 20), (20, 8), (12, 16), (20, 20), (5, 13), (9, 5), (8, 12), (13, 5), (16, 16), (20, 16), (12, 12), (5, 9), (8, 8), (9, 13), (8, 20), (16, 12), (13, 13), (18, 18), (20, 12), (12, 8), (5, 5), (12, 20), (9, 9), (8, 16), (19, 19), (13, 9), (16, 8)}
Cartesian product: D(q^-1 * q) x E(q * q^-1) = {(16, 20), (20, 20), (8, 9), (19, 9), (9, 8), (5, 19), (8, 18), (19, 18), (13, 8), (16, 13), (18, 19), (12, 18), (5, 12), (9, 19), (13, 19), (18, 12), (5, 5), (12, 20), (9, 12), (13, 12), (16, 8), (18, 5), (20, 8), (12, 13), (9, 5), (5, 16), (13, 5), (16, 19), (18, 16), (20, 19), (5, 9), (5, 18), (9, 16), (8, 20), (19, 20), (13, 16), (16, 12), (18, 9), (18, 18), (20, 12), (12, 8), (9, 9), (8, 13), (19, 13), (13, 9), (16, 5), (13, 18), (20, 5), (12, 19), (5, 13), (16, 16), (20, 16), (12, 12), (8, 8), (19, 8), (16, 9), (20, 9), (12, 5), (20, 18), (5, 20), (19, 19), (8, 19), (9, 18), (18, 20), (12, 16), (8, 12), (19, 12), (9, 20), (13, 20), (20, 13), (18, 13), (12, 9), (8, 5), (19, 5), (9, 13), (13, 13), (16, 18), (5, 8), (8, 16), (19, 16), (18, 8)}
Image q(5): {(16, 20), (20, 20), (8, 9), (19, 9), (9, 8), (5, 19), (8, 18), (19, 18), (13, 8), (16, 13), (18, 19), (12, 18), (5, 12), (9, 19), (13, 19), (18, 12), (5, 5), (12, 20), (9, 12), (13, 12), (16, 8), (18, 5), (20, 8), (12, 13), (9, 5), (5, 16), (13, 5), (16, 19), (18, 16), (20, 19), (5, 9), (5, 18), (9, 16), (8, 20), (19, 20), (13, 16), (16, 12), (18, 9), (18, 18), (20, 12), (12, 8), (9, 9), (8, 13), (19, 13), (13, 9), (16, 5), (13, 18), (20, 5), (12, 19), (5, 13), (16, 16), (20, 16), (12, 12), (8, 8), (19, 8), (16, 9), (20, 9), (12, 5), (20, 18), (5, 20), (19, 19), (8, 19), (9, 18), (18, 20), (12, 16), (8, 12), (19, 12), (9, 20), (13, 20), (20, 13), (18, 13), (12, 9), (8, 5), (19, 5), (9, 13), (13, 13), (16, 18), (5, 8), (8, 16), (19, 16), (18, 8)}
Prototype q^-1(16): {(16, 20), (20, 20), (8, 9), (19, 9), (9, 8), (5, 19), (8, 18), (19, 18), (13, 8), (16, 13), (18, 19), (12, 18), (5, 12), (9, 19), (13, 19), (18, 12), (5, 5), (12, 20), (9, 12), (13, 12), (16, 8), (18, 5), (20, 8), (12, 13), (9, 5), (5, 16), (13, 5), (16, 19), (18, 16), (20, 19), (5, 9), (5, 18), (9, 16), (8, 20), (19, 20), (13, 16), (16, 12), (18, 9), (18, 18), (20, 12), (12, 8), (9, 9), (8, 13), (19, 13), (13, 9), (16, 5), (13, 18), (20, 5), (12, 19), (5, 13), (16, 16), (20, 16), (12, 12), (8, 8), (19, 8), (16, 9), (20, 9), (12, 5), (20, 18), (5, 20), (19, 19), (8, 19), (9, 18), (18, 20), (12, 16), (8, 12), (19, 12), (9, 20), (13, 20), (20, 13), (18, 13), (12, 9), (8, 5), (19, 5), (9, 13), (13, 13), (16, 18), (5, 8), (8, 16), (19, 16), (18, 8)}

```