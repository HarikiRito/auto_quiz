import time
import asyncio

from api.seach import google_search_get


def is_prime(x):
    return not any(x // i == x / i for i in range(x - 1, 1, -1))


async def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x - 1, 0, -1):
        if is_prime(y):
            print('→ Highest prime below %d is %d' % (x, y))
            return y
        await asyncio.sleep(0.01)
    return None


async def main():
    t0 = time.time()
    await asyncio.wait([
        google_search_get('WOW', 'a'),
        google_search_get('WOW', 'b'),
        google_search_get('WOW', 'c'),
    ])
    t1 = time.time()
    print('Took %.2f ms' % (1000 * (t1 - t0)))


a = asyncio.run(main())
print(a)
