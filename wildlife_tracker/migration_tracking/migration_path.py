from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self,
                path_id: int,
                species: str,
                start_location: Habitat,
                destination: Habitat,
                duration: Optional[int] = None) -> None:
        pass

    