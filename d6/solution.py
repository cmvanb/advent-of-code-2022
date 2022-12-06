def check_candidate(candidate):
    assert(len(candidate) == 4)

    unique = list(set(candidate))
    return len(unique) == 4

def find_marker(signal):
    assert(len(signal) >= 4)

    index = 0
    candidate = signal[index:index + 4]
    while check_candidate(candidate) == False:
        index += 1
        candidate = signal[index:index + 4]

    return candidate, index + 4

def main():
    signals = []
    with open('input.txt', 'r') as file:
        signals = map(lambda line: line.strip('\n'), file.readlines())

    for signal in signals:
        marker, count = find_marker(signal)
        print(f"{count} characters need to be processed before the marker `{marker}` is found.")

if __name__ == '__main__':
    main()
