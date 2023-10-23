import argparse
import typing
import statistics

import wfdb

from utils import error_estimates


class CommandArgument(typing.Protocol):
    args: str


def parse_arguments(arg_parser: argparse.ArgumentParser) -> None:
    arg_parser.add_argument(
        dest='args',
        type=str,
    )
    arg_parser.set_defaults(command=exec_command)


def exec_command(args: CommandArgument) -> None:
    annotation = wfdb.rdann(args.args, 'atr')
    # Determination of R moments in the ECG. n
    sample_R = (annotation.sample/annotation.fs)[1:-1]
    # Determination of R-R intervals in the ECG.
    intervals_R_R = [sample_R[i] - sample_R[i - 1] for i in range(1, len(sample_R))]
    mean_intervals_R_R = statistics.mean(intervals_R_R)
    statistical_error = error_estimates.root_mean_square_uncertainty(intervals_R_R)
    absolute_error = error_estimates.absolute_error(statistical_error, 1/annotation.fs)
    relative_error = absolute_error/mean_intervals_R_R
    print(f'{60/mean_intervals_R_R:.3f}\u00B1{(60/mean_intervals_R_R)*relative_error:.3f} Cardiac contractions rate')
