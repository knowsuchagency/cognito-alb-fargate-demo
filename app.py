#!/usr/bin/env python3
"""Entrypoint to the cognito alb fargate demo CDK app"""

from aws_cdk import core

from infrastructure.configuration import get_config
from infrastructure.demo_stack import DemoStack


def main():
    """Wrapper for the CDK app"""
    app = core.App()

    config = get_config()

    DemoStack(
        app,
        "cognito-alb-fargate-demo",
        config=config,
        env={
            "account": config.aws_account,
            "region": "us-east-2",
        },
    )

    app.synth()


if __name__ == "__main__":
    main()
