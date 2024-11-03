import time

from sugar import sugar

from track import track


@track()
def train(
    epochs: int,
    batch_size: int,
    learning_rate: float,
    momentum: float,
) -> None:
    for epoch in range(1, epochs + 1):
        time.sleep(0.001)
        fields = [
            f"Epoch {epoch}/{epochs}",
            f"Batch Size: {batch_size}",
            f"Learning Rate: {learning_rate:.4g}",
            f"Momentum: {momentum: .4g}",
            f"Loss: {1.0 / epoch:.4g}",
        ]
        print(" - ".join([f"{field: <12}" for field in fields]))


if __name__ == "__main__":
    sugar(train).run()
