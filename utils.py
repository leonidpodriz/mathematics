import numpy as np
from typing import TypeVar, Set, Callable, Tuple

T = TypeVar("T")


def get_binary_relation(set_1: Set[T], set_2: Set[T], relation_condition: Callable[[T, T], bool]) -> Set[Tuple[T, T]]:
    """
    Get binary relation of two sets

    :param set_1: First set
    :param set_2: Second set
    :param relation_condition: Predicate function to test relation
    :return: New set from binary relation of two sets
    """
    return set(
        (i1, i2)
        for i1 in set_1
        for i2 in set_2
        if relation_condition(i1, i2)
    )


def get_cartesian_product(set_1: Set[T], set_2: Set[T]) -> Set[Tuple[T, T]]:
    """
    Get Cartesian product of two sets. Function uses `get_binary_relation` with always true predicate


    :param set_1: First set
    :param set_2: Second set
    :return: New set of Cartesian product
    """
    return get_binary_relation(set_1, set_2, lambda _, __: True)


def get_image(binary_relation: Set[Tuple[T, T]], value: T) -> Set[T]:
    """
    Getting image from binary relation by specific value

    :param binary_relation: Binary relation
    :param value: value to get image
    :return: Set of image
    """
    return set(
        bri[1]
        for bri
        in binary_relation
        if bri[0] == value
    )


def get_prototype(binary_relation: Set[Tuple[T, T]], value: T) -> Set[T]:
    """
    Getting prototype from binary relation by specific value

    :param binary_relation: Binary relation
    :param value: value to get prototype
    :return: Set of prototype
    """
    return set(
        bri[0]
        for bri
        in binary_relation
        if bri[1] == value
    )


def get_definition_area_for_binary_relation(binary_relation: Set[Tuple[T, T]]) -> Set[T]:
    """
    Getting definition area of binary relation. Just gets first item of every tuple

    :param binary_relation: Binary relation
    :return: Set of definition area
    """
    return set(bi[0] for bi in binary_relation)


def get_value_area_for_binary_relation(binary_relation: Set[Tuple[T, T]]) -> Set[T]:
    """
    Getting value area of binary relation. Just gets second item of every tuple

    :param binary_relation: Binary relation
    :return: Set of value area
    """
    return set(bi[1] for bi in binary_relation)


def get_matrix(binary_relation: Set[Tuple[T, T]]) -> np.array:
    """
    Getting matrix from binary relation

    :param binary_relation: Binary relation
    :return: Matrix (numpy two-dimensional array)
    """
    rows_count = max(get_definition_area_for_binary_relation(binary_relation))
    columns_count = max(get_value_area_for_binary_relation(binary_relation))
    matrix = np.zeros((rows_count, columns_count), dtype=int)

    for ri, ci in binary_relation:
        matrix[ri - 1][ci - 1] = 1

    return matrix


def get_inverse_relationship(binary_relation: Set[Tuple[T, T]]) -> Set[Tuple[T, T]]:
    """
    Getting inverse relationship from binary relation

    :param binary_relation: Binary relation
    :return: Set of inverted relationship
    """
    return set((i2, i1) for i1, i2 in binary_relation)


def get_composition(binary_relation_1: Set[Tuple[T, T]], binary_relation_2: Set[Tuple[T, T]]) -> Set[Tuple[T, T]]:
    """
    Getting composition (A * B) of two binary expressions

    :param binary_relation_1: First binary expression
    :param binary_relation_2: Second binary expression
    :return: Set of composited relations
    """
    return set(
        (br1i[0], br2i[1])
        for br1i in binary_relation_1
        for br2i in binary_relation_2
        if br1i[1] == br2i[0]
    )
