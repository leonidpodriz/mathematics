from pprint import pprint

from utils import get_binary_relation, get_matrix, get_definition_area_for_binary_relation, \
    get_value_area_for_binary_relation, get_inverse_relationship, get_composition, get_cartesian_product, get_image, \
    get_prototype

A = {5, 8, 9, 12, 13, 16, 18, 19, 20}
q = get_binary_relation(A, A, lambda a1, a2: abs(a1 - a2) % 4 == 0)

# pprint(q)
# pprint(get_definition_area_for_binary_relation(q))
# pprint(get_matrix(q))
# print(get_definition_area_for_binary_relation(q))
# print(get_value_area_for_binary_relation(q))
# print(get_inverse_relationship(q))
#
qm1 = get_inverse_relationship(q)
# pprint(get_composition(q, qm1))
# print(get_composition(qm1, q))
#
pprint(
    get_cartesian_product(
        get_value_area_for_binary_relation((get_composition(qm1, q))),
        get_definition_area_for_binary_relation(get_composition(q, qm1)),
    )
)
#
print(get_image(q, 5))
print(get_prototype(qm1, 16))
