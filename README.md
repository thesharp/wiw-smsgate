# wiw-smsgate [![Build Status](https://travis-ci.org/thesharp/wiw-smsgate.png?branch=master)](https://travis-ci.org/thesharp/wiw-smsgate)

## Overview

This is our in-house utility to send text messages (SMS) from Nagios using our own XML-RPC gateway. This project is here just because I was too lazy to setup an internal git repository. Obviously, this utility is only usable for us, sorry for that.

## Dependencies

- Python 2.6, 2.7

## Usage

    Usage: wiw-smsgate [options] <phone number> <message>

    Options:
      -h, --help     show this help message and exit
      -v, --verbose  verbose output
      -t, --test     test mode for nosetests

    <phone number> should be in a 7xxxxxxxxxx format