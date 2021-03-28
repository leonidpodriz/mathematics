import numpy as np
from typing import TypeVar, Set, Callable, Tuple

T = TypeVar("T")


def get_binary_relation(set_1: Set[T], set_2: Set[T], relation_condition: Callable[[T, T], bool]) -> Set[Tuple[T, T]]:
    return set(
        (i1, i2)
        for i1 in set_1
        for i2 in set_2
        if relation_condition(i1, i2)
    )


def get_cartesian_product(set_1: Set[T], set_2: Set[T]):
    return get_binary_relation(set_1, set_2, lambda _, __: True)


def get_image(binary_relation: Set[Tuple[T, T]], value: T) -> Set[T]:
    return set(
        bri[1]
        for bri
        in binary_relation
        if bri[0] == value
    )


def get_prototype(binary_relation: Set[Tuple[T, T]], value: T) -> Set[T]:
    return set(
        bri[0]
        for bri
        in binary_relation
        if bri[1] == value
    )


def get_definition_area_for_binary_relation(binary_relation: Set[Tuple[T, T]]) -> Set[T]:
    return set(bi[0] for bi in binary_relation)


def get_value_area_for_binary_relation(binary_relation: Set[Tuple[T, T]]) -> Set[T]:
    return set(bi[1] for bi in binary_relation)


def get_matrix(binary_relation: Set[Tuple[T, T]], remove_zeros: bool = True) -> np.array:
    rows_count = max(get_definition_area_for_binary_relation(binary_relation))
    columns_count = max(get_value_area_for_binary_relation(binary_relation))
    matrix = np.zeros((rows_count, columns_count), dtype=int)

    for ri, ci in binary_relation:
        matrix[ri - 1][ci - 1] = 1

    return matrix


def get_inverse_relationship(binary_relation: Set[Tuple[T, T]]) -> Set[Tuple[T, T]]:
    return set((i2, i1) for i1, i2 in binary_relation)


def get_composition(binary_relation_1: Set[Tuple[T, T]], binary_relation_2: Set[Tuple[T, T]]) -> Set[Tuple[T, T]]:
    return set(
        (br1i[0], br2i[1])
        for br1i in binary_relation_1
        for br2i in binary_relation_2
        if br1i[1] == br2i[0]
    )
