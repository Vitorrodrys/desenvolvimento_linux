from consumer import Consumer
from producer import Producer
from stock import Stock


def main():
    stock = Stock()
    producers = [Producer(stock, id_producer) for id_producer in range(1, 4)]
    consumers = [Consumer(id_consumer, stock) for id_consumer in range(1, 4)]


if __name__ == "__main__":
    main()
