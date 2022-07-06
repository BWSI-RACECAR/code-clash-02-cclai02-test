class Solution:
    def two_numbers(self, ary, target):
        # type ary: list
        # type target: int
        # return type: list or bool

        for x in ary:
            other_num = target - x
            if other_num in ary:
                return [ary.index(x), ary.index(other_num)]
        return False

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])
    target = int(input())

    print(array)
    print(target)

    tc1 = Solution()
    print(tc1.two_numbers(array, target))

if __name__ == "__main__":
    main()
