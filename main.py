import argparse
from enum import Enum
from pkg.preprocess import preprocess
from pkg.train import train
from pkg.synthesis import synthesis


class Module(Enum):
    Text2Mel = 0
    SuperRes = 1

    def __str__(self):
        return self.name


class Action(Enum):
    preprocess = 0
    train = 1
    synthesis = 2

    def __str__(self):
        return self.name


def str_to_enum(the_enum, s):
    try:
        return the_enum[s]
    except Exception:
        raise ValueError()


def main():
    parser = argparse.ArgumentParser(description="optional actions")
    parser.add_argument("--action", type=lambda x: str_to_enum(Action, x), choices=list(Action))
    parser.add_argument("--module", type=lambda x: str_to_enum(Module, x), choices=list(Module))
    parser.add_argument("--load", type=int, default=0)
    args = parser.parse_args()
    if args.action is None:
        parser.print_help()
        return
    if args.action == Action.preprocess:
        preprocess()
    elif args.action == Action.train:
        if args.module is None:
            parser.print_help()
        else:
            train(args.module, args.load)
    elif args.action == Action.synthesis:
        texts = []
        with open("sentences.txt", "r") as f:
            for line in f:
                line = line.strip()
                if len(line):
                    texts.append(line)
        if len(texts):
            synthesis(texts)
    else:
        raise ValueError()


if __name__ == "__main__":
    main()
