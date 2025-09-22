#!/usr/bin/env python3
"""Command line interface for python-poc."""

import argparse
import sys

from python_poc import __version__, calculate, greet


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Python POC CLI")
    parser.add_argument(
        "--version", action="version", version=f"python-poc {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Greet command
    greet_parser = subparsers.add_parser("greet", help="Generate a greeting")
    greet_parser.add_argument("name", help="Name to greet")

    # Calculate command
    calc_parser = subparsers.add_parser("calc", help="Perform calculations")
    calc_parser.add_argument("a", type=float, help="First number")
    calc_parser.add_argument("b", type=float, help="Second number")
    calc_parser.add_argument(
        "--op",
        choices=["add", "subtract", "multiply", "divide"],
        default="add",
        help="Operation to perform",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    try:
        if args.command == "greet":
            result = greet(args.name)
            print(result)
        elif args.command == "calc":
            calc_result = calculate(args.a, args.b, args.op)
            print(f"{args.a} {args.op} {args.b} = {calc_result}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
