import uuid


def generate_uuid():
    unique_id = uuid.uuid4()
    print(f"Generated UUID: {unique_id}")
    return str(unique_id)


def generate_multiple_uuids(count):
    print(f"Generating {count} UUIDs:")
    for i in range(count):
        print(f"  {i + 1}. {uuid.uuid4()}")
