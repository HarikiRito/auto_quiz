import asyncio
from typing import List, Tuple, Coroutine

from text_extract.pil_utils import GoogleSearch


async def google_search_get(q: str, a: str) -> Tuple[int, int]:
    search_instance = GoogleSearch('{} - {}'.format(q, a))
    search_instance.search()
    results = search_instance.result
    total = results[0].number_of_results
    count_appear = 0
    descriptions = [result.description for result in results]  # type: List[str]
    for d in descriptions:
        if a.lower() in d.lower():
            count_appear += 1
    return total, count_appear


async def search_all(q: str, answers: List[str]):
    return await asyncio.wait([
        google_search_get(q, a) for a in answers
    ])


a = 'Vi công chúa Việt Nam nào sau dây có băng thac sĩ nuóc ngoài?'
b = ['Nguyen Phúc Nhu Lý', 'Nguyěn Phúc Phuong Dung', 'Nguyen Phúc Nhu Mai']

# r = asyncio.run(
#     search_all(a, b)
# )
#
# print(r)

