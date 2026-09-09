from enum import Enum


class ExperimentCondition(str, Enum):
    """Controlled conditions used by Experiment 01."""

    A_ONLY = "A_ONLY"
    AB_NO_COMM = "AB_NO_COMM"
    AB_COMM = "AB_COMM"
