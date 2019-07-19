#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `py_test` package."""


import unittest
from click.testing import CliRunner

from py_test import py_test
from py_test import cli


class TestPy_test(unittest.TestCase):
    """Tests for `py_test` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'py_test.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
