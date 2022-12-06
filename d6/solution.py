def check_candidate(candidate):
    return len(set(candidate)) == len(candidate)

def find_marker(signal, length):
    signalLength = len(signal)
    assert(signalLength >= length)

    for i in range(signalLength - length):
        candidate = signal[i:i + length]
        if check_candidate(candidate):
            return candidate, i + length

    raise ValueError(f"Signal does not contain marker of length {length}.")

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
