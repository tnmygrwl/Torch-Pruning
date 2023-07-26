from contextlib import contextmanager
import logging
import os, sys
from termcolor import colored
import copy
import numpy as np
import torch

def flatten_dict(dic):
    flattned = {}
    def _flatten(prefix, d):
        for k, v in d.items():
            if isinstance(v, dict):
                if prefix is None:
                    _flatten( k, v )
                else:
                    _flatten(f'{prefix}/{k}', v)
            else:
                if prefix is None:
                    flattned[k] = v
                else:
                    flattned[f'{prefix}/{k}'] = v

    _flatten(None, dic)
    return flattned

class _ColorfulFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super(_ColorfulFormatter, self).__init__(*args, **kwargs)

    def formatMessage(self, record):
        log = super(_ColorfulFormatter, self).formatMessage(record)

        if record.levelno == logging.WARNING:
            prefix = colored("WARNING", "yellow", attrs=["blink"])
        elif record.levelno in [logging.ERROR, logging.CRITICAL]:
            prefix = colored("ERROR", "red", attrs=["blink", "underline"])
        else:
            return log

        return f"{prefix} {log}"
