import copy


def get_string_from_file(file):
    with open(file) as file:
        string = file.read()
    return string

class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

def encode(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    original_char_count = copy.deepcopy(char_count)

    orphan_node_list = []
    for key in char_count:
        orphan_node_list.append(Node(key, None, None))

    while len(char_count) != 1:
        sorted_char_count = sorted(char_count.items(), key=lambda x: x[1])
        char_count[sorted_char_count[0][0] + sorted_char_count[1][0]] = sorted_char_count[0][1] + sorted_char_count[1][1]
        char_count.pop(sorted_char_count[0][0])
        char_count.pop(sorted_char_count[1][0])

        curr_node = Node(name=sorted_char_count[0][0] + sorted_char_count[1][0])

        tobepopped = []
        for i in range(len(orphan_node_list)):
            if sorted_char_count[0][0] == orphan_node_list[i].name:
                if curr_node.left is None:
                    curr_node.left = orphan_node_list[i]
                    tobepopped.append(i)
                else:
                    curr_node.right = orphan_node_list[i]
                    tobepopped.append(i)
            elif sorted_char_count[1][0] == orphan_node_list[i].name:
                if curr_node.left is None:
                    curr_node.left = orphan_node_list[i]
                    tobepopped.append(i)
                else:
                    curr_node.right = orphan_node_list[i]
                    tobepopped.append(i)

        orphan_node_list.pop(tobepopped[1])
        orphan_node_list.pop(tobepopped[0])
        orphan_node_list.append(curr_node)

    root = orphan_node_list[0]
    return root

def total_bits(root, string):
    bits_per_char = {}
    for char in set(string):
        bits_per_char[char] = 0
        curr_node = root
        while len(curr_node.name) > 1:
            if char in curr_node.left.name:
                curr_node = curr_node.left
                bits_per_char[char] += 1
            else:
                curr_node = curr_node.right
                bits_per_char[char] += 1

    total_bits = 0
    for char in string:
        total_bits += bits_per_char[char]

    return total_bits

def main():
    file_name = input("Enter the name of the file: ")
    string = get_string_from_file(file_name)
    print(f'Number of bits to encode {file_name}: {total_bits(encode(string), string)}')

if __name__ == "__main__":
    main()