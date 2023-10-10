from spire_wrapper import api

import asyncio

async def main():
    spireObj = api.Spire()
    data = await spireObj.coverage.getCoverages()
    print(data)

asyncio.run(main())