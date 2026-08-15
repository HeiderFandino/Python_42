import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = [
        "alice",
        "bob",
        "charlie",
        "dylan",
    ]
    actions: list[str] = [
        "move",
        "grab",
        "use",
        "swing",
        "run",
        "climb",
        "release",
        "eat",
        "sleep",
        "swim",
    ]

    while True:
        selected_player = random.choice(players)
        selected_action = random.choice(actions)

        event: tuple[str, str] = (
            selected_player,
            selected_action,
        )
        yield event


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        selected_event = random.choice(events)
        events.remove(selected_event)
        yield selected_event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        event = next(event_generator)
        print(
            f"Event {i}: Player {event[0]} "
            f"did action {event[1]}"
        )

    second_event_generator = gen_event()
    ten_events_list: list[tuple[str, str]] = []

    for _ in range(10):
        event = next(second_event_generator)
        ten_events_list += [event]

    print(f"Built list of 10 events: {ten_events_list}")

    for consumed_event in consume_event(ten_events_list):
        print(f"Got event from list: {consumed_event}")
        print(f"Remains in list: {ten_events_list}")
