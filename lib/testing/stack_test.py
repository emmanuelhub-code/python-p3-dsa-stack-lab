import pytest
from Stack import Stack

class TestStack:

    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        for index in range(len(expected)):
            assert expected[index] == stk.items[index]

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.push(0)
        assert stk.items[-1] == 0

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.pop()
        expected = [1, 2, 3, 4]
        for index in range(len(expected)):
            assert expected[index] == stk.items[index]

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        assert stk.size() == len(expected)

    def test_empty(self):
        '''Test Stack isEmpty() method'''
        stk = Stack()
        assert stk.isEmpty() is True
        stk.push(1)
        assert stk.isEmpty() is False

    def test_full(self):
        '''Test Stack full() method'''
        stk = Stack([1], 1)
        assert stk.full() is True
        assert stk.size() == 1
        assert stk.pop() == 1
        stk.push(1)

        # Expect OverflowError when pushing to a full stack
        with pytest.raises(OverflowError):
            stk.push(2)

    def test_search(self):
        '''Test Stack search() method'''
        stk = Stack([5, 6, 7, 8, 9, 10])
        # Top of stack is distance 0
        assert stk.search(10) == 0
        assert stk.search(9) == 1
        assert stk.search(5) == 5
        # Value not in stack
        assert stk.search(100) == -1
