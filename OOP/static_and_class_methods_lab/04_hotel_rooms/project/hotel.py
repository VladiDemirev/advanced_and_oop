from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int) -> "Hotel":
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        # room = [r for r in self.rooms if r.number == room_number][0]
        room = next((r for r in self.rooms if r.number == room_number), None)
        return room.take_room(people)

    def free_room(self, room_number: int) -> None:
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self) -> str:
        # self.guests = sum([r.guests for r in self.rooms])
        result = [f"Hotel {self.name} has {self.guests} total guests"]
        result.append(f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}")
        result.append(f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}")
        return "\n".join(result)
