"""Imports Prime File """
import prime

#test module

def test_generatre_prime_factors_string_value_error():
    """STEP1"""
    assert prime.find_prime("A string") == ValueError


def test_generatre_prime_factors_variable_equals_one():
    """STEP2"""
    assert prime.find_prime(1) == []


def test_generatre_prime_factors_variable_equals_two():
    """STEP3"""
    assert prime.find_prime(2) == [2]


def test_generatre_prime_factors_variable_equals_three():
    """STEP4"""
    assert prime.find_prime(3) == [3]

def test_generatre_prime_factors_variable_equals_four():
    """STEP5"""
    assert prime.find_prime(4) == [2, 2]

def test_generatre_prime_factors_variable_equals_six():
    """STEP6"""
    assert prime.find_prime(6) == [2, 3]

def test_generatre_prime_factors_variable_equals_eight():
    """STEP7"""
    assert prime.find_prime(8) == [2, 2, 2]

def test_generate_prime_factors_variable_equals_nine():
    """STEP8"""
    assert prime.find_prime(9) == [3, 3]
