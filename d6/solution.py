def check_candidate(candidate):
    return len(set(candidate)) == len(candidate)

def find_marker(signal, length):
    signalLength = len(signal)
    assert(signalLength >= length)

    index = 0
    candidate = signal[index:index + length]
    while check_candidate(candidate) == False or index > signalLength - length:
        index += 1
        candidate = signal[index:index + length]

    return candidate, index + length

def main():
    signals = []
    with open('input.txt', 'r') as file:
        signals = map(lambda line: line.strip('\n'), file.readlines())

    for signal in signals:
        packet_marker, count = find_marker(signal, 4)
        print(f"{count} characters need to be processed before the start-of-packet marker `{packet_marker}` is found.")

        msg_marker, count = find_marker(signal, 14)
        print(f"{count} characters need to be processed before the start-of-message marker `{msg_marker}` is found.")

if __name__ == '__main__':
    main()
