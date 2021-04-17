   # normal way to test code
   def average(l):
        if not l:
            return None
        return sum(l)/len(l)

    if __name__ == "__main__":
        l = [1, 2, 3, 4, 5]
        expected_result = 3.0
        result = average(l)

        if expected_result == result:
            print("test passed")
        else:
            print("test failed", "received:", result,
                  "Expected:", expected_result)

    code test with Assert


def Average(l):
    if not l:
        return None
    return sum(l)/len(l)


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    expected_result = 3.0
    result = Average(l)
    print(result)
    # if assert don't accepcted reselt its throw  AssertionError, other wise its return none
    assert expected_result == result, "average() produced incorrect result"
