from __future__ import annotations

import time

from huffman import HuffmanTree
from utils import *
from typing import Union,List


def build_huffman_tree(freq_dict: dict[int, int]) -> HuffmanTree:
    """ Return the Huffman tree corresponding to the frequency dictionary
    <freq_dict>.

    Precondition: freq_dict is not empty.

    >>> freq = {2: 6, 3: 4}
    >>> t = build_huffman_tree(freq)
    >>> result = HuffmanTree(None, HuffmanTree(3), HuffmanTree(2))
    >>> t == result
    True
    >>> freq = {2: 6, 3: 4, 7: 5}
    >>> t = build_huffman_tree(freq)
    >>> result = HuffmanTree(None, HuffmanTree(2), \
                             HuffmanTree(None, HuffmanTree(3), HuffmanTree(7)))
    >>> t == result
    True
    >>> import random
    >>> symbol = random.randint(0,255)
    >>> freq = {symbol: 6}
    >>> t = build_huffman_tree(freq)
    >>> any_valid_byte_other_than_symbol = (symbol + 1) % 256
    >>> dummy_tree = HuffmanTree(any_valid_byte_other_than_symbol)
    >>> result = HuffmanTree(None, HuffmanTree(symbol), dummy_tree)
    >>> t.left == result.left or t.right == result.left
    True
    """
    lst = [[key, freq_dict[key]] for key in freq_dict]
    return helper([[key, freq_dict[key]] for key in freq_dict])

def helper(freq_list) -> HuffmanTree:
    if len(freq_list) == 1:
        symbol = freq_list[0][0]
        return HuffmanTree(None, HuffmanTree(symbol), HuffmanTree((symbol + 1) % 256))
          
    elif len(freq_list) == 2:
        #print(freq_list)
        frequencies = [freq_list[0][1], freq_list[1][1]]
        keys = [freq_list[0][0], freq_list[1][0]]
        smallest = frequencies.index(min(frequencies))
        if smallest == 0:
            return HuffmanTree(None, HuffmanTree(keys[0]), HuffmanTree(keys[1]))
        return HuffmanTree(None, HuffmanTree(keys[1]), HuffmanTree(keys[0]))
    
    else:
        
        smallest = [-1,-1]
        second_smallest = [-1,-1]
        for pair in freq_list:
            if pair[1] < second_smallest[1] or second_smallest[1] == -1:
                if pair[1] < smallest[1] or smallest[1] == -1:
                    smallest, second_smallest = pair, smallest
                else:
                    second_smallest = pair
        tree = HuffmanTree(None, HuffmanTree(smallest[0]), HuffmanTree(second_smallest[0]))
        freq_list.remove(smallest)
        freq_list.remove(second_smallest)
        freq_list.append([tree, smallest[1] + second_smallest[1]])
        #print(freq_list)
        return helper(freq_list)

def get_codes(tree: HuffmanTree) -> dict[int, str]:
    """ Return a dictionary which maps symbols from the Huffman tree <tree>
    to codes.

    >>> tree = HuffmanTree(None, HuffmanTree(3), HuffmanTree(2))
    >>> d = get_codes(tree)
    >>> print(d)
    >>> d == {3: "0", 2: "1"}
    True
    """
    return code_helper(tree,'')


def code_helper(tree: HuffmanTree, code: str):
    """
    return code for thing and such
    """
    if tree.is_leaf():
        #print([tree.symbol, code])
        return [tree.symbol, code]
    else:
        codes = []
        if not tree.left is None:
            print("1")
            codes.append(code_helper(tree.left, code + "0"))
        if not tree.right is None:
            codes.append(code_helper(tree.right, code + "1"))
        return codes

freq = {'A':5,'B':1,'C':6,'D':3}
t = build_huffman_tree(freq)
print(get_codes(t))
#result = HuffmanTree(None, HuffmanTree(2), HuffmanTree(None, HuffmanTree(3), HuffmanTree(7)))
#print(t == result," ", t.left," ", t.right)
#print(t)