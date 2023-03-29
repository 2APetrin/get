def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


print(decimal2binary(1023))