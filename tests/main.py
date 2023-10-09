from pathlib import Path
import sys
import os
sys.path.insert(0, os.path.join(Path(os.path.dirname(os.path.abspath(__file__))).parent.resolve()))

from src.spire_wrapper import api

import asyncio

async def main():
    spireObj = api.Spire()
    data = await spireObj.coverage.getCoverages()
    print(data)

asyncio.run(main())