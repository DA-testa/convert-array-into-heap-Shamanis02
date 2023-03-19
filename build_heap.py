def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    n = len(data)
    min_index = i
    left_child = 2 * i + 1
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, swaps)

def main():
    fileorno = input()
    if "I" in fileorno or "i" in fileorno:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in fileorno or "f" in fileorno:
        file = input()
        if "a" not in file:
            with open("test/" + file, 'r')as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
