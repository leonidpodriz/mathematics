from utils import get_binary_relation, get_matrix, get_definition_area_for_binary_relation, \
    get_value_area_for_binary_relation, get_inverse_relationship, get_composition, get_cartesian_product, get_image, \
    get_prototype

A = {5, 8, 9, 12, 13, 16, 18, 19, 20}
q = get_binary_relation(A, A, lambda a1, a2: abs(a1 - a2) % 4 == 0)
matrix = get_matrix(q)

D = get_definition_area_for_binary_relation(q)
E = get_value_area_for_binary_relation(q)

qm1 = get_inverse_relationship(q)
q_qm1_composition = get_composition(q, qm1)
qm1_q_composition = get_composition(qm1, q)

cartesian_product = get_cartesian_product(
    get_value_area_for_binary_relation((get_composition(qm1, q))),
    get_definition_area_for_binary_relation(get_composition(q, qm1)),
)

q_image_5 = get_image(q, 5)
qm1_prototype_16 = get_prototype(qm1, 16)

print(" REPORT ".center(80, "="))
print(f"A = {A}")
print(f"q = {{ (a, b): a is A, b is A, |a - b| mod 4 = 0 }} = {q}")
print(f"Matrix view of q: \n{matrix}")
print(f"D(q) = {D}")
print(f"E(q) = {E}")
print(f"q^-1 = {qm1}")
print(f"(Composition) q * q^-1 = {q_qm1_composition}")
print(f"(Composition) q^-1 * q = {qm1_q_composition}")
print(f"Cartesian product: D(q^-1 * q) x E(q * q^-1) = {cartesian_product}")
print(f"Image q(5): {cartesian_product}")
print(f"Prototype q^-1(16): {cartesian_product}")
