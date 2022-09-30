from typing import Union

from ingester.tables import Parking, session, Base, engine


def get_user_category(code: int) -> str:
    if code == 1:
        return "hourly"
    if code == 2:
        return "user_card"
    if code == 99:
        return "any"
    return "unknown"


def ingest(data: list[dict[str, Union[str, int]]]) -> None:
    """Ingest data."""
    Base.metadata.create_all(engine)

    print("starting ingestion")
    for i, row in enumerate(data):
        d = row["fields"]
        record = Parking(
            public_equipment_id=d["idobj"],
            parking_name=d["appellation"],
            hour=d["horodatage"],
            user_category=get_user_category(d["code_type_usager"]),
            occupancy=d["occupation_nb_vehicules"],
        )
        session.add(record)
        session.commit()

        if i % 100 == 0:
            print(f"added {i} records")
