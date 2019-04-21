#!/usr/bin/env python3


def main():
    _ = int(input())
    cards = list(map(int, input().split()))
    cards.sort(reverse=True)
    alice_cards = cards[0::2]
    bob_cards = cards[1::2]
    print(sum(alice_cards) - sum(bob_cards))


if __name__ == '__main__':
    main()
