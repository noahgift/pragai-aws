#!/usr/bin/env python

"""
Command-line Tool for Working with PAWS library
"""
import sys

import click
import paws
from paws import s3

@click.version_option(paws.__version__)
@click.group()
def cli():
    """PAWS Tool"""

@cli.command("download")
@click.option("--bucket", help="Name of S3 Bucket")
@click.option("--key", help="Name of S3 Key")
@click.option("--filename", help="Name of file")
def download(bucket, key, filename):
    """Downloads an S3 file
    ./paws-cli.py download --bucket gdelt-open-data --key events/1979.csv --filename 1979.csv
    """

    if not bucket and not key and not filename:
        click.echo("--bucket and --key and --filename are required")
        sys.exit(1)
    click.echo("Downloading s3 file with: bucket-{bucket},key{key},filename{filename}".\
        format(bucket=bucket, key=key, filename=filename))
    res = s3.download(bucket, key,filename)
    click.echo(res)

if __name__ == "__main__":
    cli()