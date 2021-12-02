"""
    Cryptographic handshake
      - Transforms a subject number to an encrypted number
      - Perform the following steps a number of times called the loop size
        1. Set the value to itself multiplied by the subject number
        2. Set the value to the remainder after dividing by 20201227
    The card uses the same loop size
    The door always uses a different loop size

    Card -> 7 -> CPK
    Door -> 7 -> DPK

    The card transforms the subject number of the door's public key
"""


def get_loop_count(public_key, subject, value=1):
    loop_count = 0
    while value != public_key:
        value = value * subject
        value = value % 20201227
        loop_count += 1
    return loop_count


def apply_operation(subject, vals, value=1):
    for _ in range(vals):
        value = value * subject
        value = value % 20201227
    return value


if __name__ == "__main__":
    card_PK = 14012298
    door_PK = 74241

    card_loop_size = get_loop_count(card_PK, 7)
    door_loop_size = get_loop_count(door_PK, 7)

    encrypt_1 = apply_operation(door_PK, card_loop_size)
    encrypt_2 = apply_operation(card_PK, door_loop_size)
    assert encrypt_1 == encrypt_2
