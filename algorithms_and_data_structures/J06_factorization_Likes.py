"""Exercise 1: Likes!
Implement the system of displaying the number of "likes" known from Facebook.
Explanation: The likes function should take a string list of names as input
people who "like" a given post / photo, and output a properly formatted text.

Finally, the algorithm should work as follows:

likes([])  ## => "nobody likes it"
likes(["Peter"])  ## => "Peter likes it!"
likes(["Peter", "Anna"])  ## => "Peter and Anna like it"
likes(["Peter", "Anna", "Mark"])  ## => "Peter, Anna and Mark like it"
likes(["Peter", "Anna", "Mark", "Ola"])  ## => "Peter, Anna and 2 other people like it"
"""

from typing import List


def likes(names: List[str]) -> str:
    n_of_likes = len(names)
    if n_of_likes == 0:
        return "nobody likes it"
    if n_of_likes == 1:
        return f"{names[0]} likes it!"
    if n_of_likes == 2:
        return f"{names[0]} and {names[1]} like it!"
    if n_of_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like it!"
    return f"{names[0]}, {names[1]}, {names[2]} and {n_of_likes - 2} other people like it!"


if __name__ == "__main__":
    list_of_likes = [[], ["Peter"], ["Peter", "Anna"], ["Peter", "Anna", "Mark"],
                     ["Peter", "Anna", "Mark", "Ola"], ["Peter", "Anna", "Mark", "Ola", "Frank"]]

    for likes_list in list_of_likes:
        print(f"{likes_list} -> '{likes(likes_list)}'")
