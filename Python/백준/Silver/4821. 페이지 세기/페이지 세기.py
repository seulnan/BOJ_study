import sys

while True:
    total_page = int(sys.stdin.readline())

    if total_page == 0:
        break

    print_page_count = [0] * (total_page + 1)
    print_range_list = sys.stdin.readline().rstrip().split(',')

    for print_range in print_range_list:

        if '-' in print_range:
            low, high = map(int, print_range.split('-'))

            for i in range(low, high + 1):

                if i <= total_page:
                    print_page_count[i] += 1

            continue

        page = int(print_range)

        if page <= total_page:
            print_page_count[page] += 1

    print(sum([1 if 1 <= i else 0 for i in print_page_count]))
