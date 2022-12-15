from typing import List
import location


@db_session
def get_locations() -> List[location.Location]:
    pass


@app.get("/")
async def root():
    pass
