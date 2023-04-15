from gradient import Gradient
import random

def print_color_block(colorRGB):
    # print a strip of █ characters of the given color, which should be and (R, G, B) tuple with values ranging from 0 to 255
    print(f'\033[38;2;{colorRGB[0]};{colorRGB[1]};{colorRGB[2]}m█\033[0m', end="")


def print_strip(g: Gradient, length):
    # print to the console a strip of `length` characters coloured by the gradient
    for i in range(length):
        print_color_block(tuple(map(lambda x: int(x), g.get(i / length))))
    print()


def example(length):
    colorA = (0, 0, 255)
    colorB = (255, 0, 255)

    gradients = [
        # one tenth A->B and 9 thenths B->A
        Gradient([colorA, colorB, colorA], [1, 9]),
        # 50/50 gradient, with B right in the middle
        Gradient([colorA, colorB, colorA], [1, 1]),
        # similar to the first one, with the lengths inverted
        Gradient([colorA, colorB, colorA], [9, 1]),
    ]

    print("Blue -> Pink -> Blue with different separations")
    for g in gradients:
        print_strip(g, length)


def example_random(length):
    # Print a strip with a random a amount of colors separated by a random distance
    cant = random.randint(2, 6)
    g = Gradient(
        [tuple(random.random() * 255 for i in range(3)) for j in range(cant)],
        [random.random() for k in range(cant - 1)]
    )

    print_strip(g, length)


if __name__ == '__main__':
    print()
    example(length=80)
    
    print()
    print("10 Strips with a random amount of random colors:")
    for i in range(10):
        example_random(length=80)
        # print_strip(Gradient([(0, 0, 0), (0, 0, 0)], [1]), 80) # Just black
