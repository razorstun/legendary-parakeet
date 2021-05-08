Generators

- Generator function allow us to write a function that can send back a value and then later resume to pickup where it left off
- allow us to generate a sequence of values over time
- the advantage is that instead of havinf to compute an entire series of values up front,
    the Generatorm computes one value waits until next value is called front
- next(generator object) to get next value
- iter(object) - to convert iteratable object into Generators