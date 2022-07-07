class TrieNode:
    """
    The Trie Node class represents a single node object inside a Trie
    
    ...

    Attributes
    ----------
    prefix_bit : str
        Contains a bit representing an IP Address
    children: Dictionary
        Holds a BGP record mapped against a bit
    is_end_of_address: bool
        A boolean value to check if its the end of an address
    """
    def __init__(self, prefix_bit):
        self.prefix_bit = prefix_bit
        self.children = {}
        self.is_end_of_address = False


class Trie:
    """
    The Trie class represents the Trie object comprised of
    multiple TrieNode objects

    ...

    Attributes
    ----------
    root : TrieNode
        Pointer to the TrieNode

    Methods
    -------
    add(word=""):
        Adds a new TrieNode into the Trie
    does_prefix_exist(ip_bits):
        Checks if a given IP address exists in the trie
    """
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, prefix):
        """
        Adds a prefix bit entry into the Trie if one doesn't already exist

        Parameters:
            prefix (str): Bits representation of an IP Address
        Returns:
            None
        """
        curr_node = self.root
        for prefix_bit in prefix:
            if prefix_bit not in curr_node.children:
                curr_node.children[prefix_bit] = TrieNode(prefix_bit)
            curr_node = curr_node.children[prefix_bit]
        curr_node.is_end_of_address = True

    def does_prefix_exist(self, prefix):
        """
        Checks if a given IP address exists in the trie and returns the boolean value

        Parameters:
            prefix (str): Bits representation of an IP Address
        Returns:
            bool
        """
        if prefix == "":
            return True
        curr_node = self.root
        for prefix_bit in prefix:
            if prefix_bit not in curr_node.children:
                return False
            curr_node = curr_node.children[prefix_bit]
        return curr_node.is_end_of_address


trie = Trie()
addresses = ["11001100100001000010100010011011",
             "11111111100001000010100010011011",
             "11001100100001000010100010011011",
             "1100110011000010010010100010011011"]

for address in addresses:
    trie.add(address)

print(trie.does_prefix_exist("110011001000010000101000100110100"))  # False
print(trie.does_prefix_exist("11001100100001000010100010011011"))  # True
