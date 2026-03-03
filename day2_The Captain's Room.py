K = int(input())
rooms = list(map(int, input().split()))

unique_rooms = set(rooms)

captain_room = (sum(unique_rooms) * K - sum(rooms)) // (K - 1)

print(captain_room)