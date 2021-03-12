def show_order(argv):
    if len(argv) == 0:
        start_order = 0
        stop_order = 0
    elif len(argv) == 1:
        start_order = int(argv[0])
        stop_order = 0
    elif len(argv) == 2:
        start_order = int(argv[0])
        stop_order = int(argv[1])
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if start_order == 0:
            all_order = [line.split('\n')[0] for line in f.readlines()]
            print(*(all_order[i] for i in range(len(all_order))), sep='\n')
        else:
            all_order = [line.split('\n')[0] for line in f.readlines()]
            if stop_order == 0:
                print(*(all_order[i] for i in range(start_order - 1, len(all_order))), sep='\n')
            else:
                print(*(all_order[i] for i in range(start_order - 1, stop_order)), sep='\n')


if __name__ == '__main__':
    import sys

    exit(show_order(sys.argv[1:]))
