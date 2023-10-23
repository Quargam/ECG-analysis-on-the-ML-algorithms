import statistics
import typing


def dispersion(sequence: typing.List[typing.Union[int, float]]) -> float:
    """Calculation of the dispersion from the sequence of numbers."""
    mean_sequence = statistics.mean(sequence)
    return statistics.mean(map(lambda x: (x - mean_sequence)**2, sequence))


def root_mean_square_uncertainty(sequence: typing.List[typing.Union[int, float]]) -> None:
    """Determine the statistical_error of the average value."""
    return (dispersion(sequence) / (len(sequence) - 1)) ** 0.5


def absolute_error(
    statistical_error: typing.Union[int, float],
    random_error: typing.Union[int, float],
    instrumental_error: typing.Optional[typing.Union[int, float]] = None,
) -> float:
    """Calculation of the absoluteerror."""
    instrumental_error = instrumental_error or random_error
    return (statistical_error ** 2 + random_error ** 2 + instrumental_error ** 2) ** 0.5
