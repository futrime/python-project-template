"""Main module"""

import asyncio

from number_adder import NumberAdder


async def main() -> None:
    """Main function"""

    number_adder = NumberAdder()
    print(number_adder.add(1, 2))
    print(number_adder.add_many([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    asyncio.run(main())
