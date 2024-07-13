#!/bin/bash

# Run tests with coverage
pytest --cov=app --cov-report=xml tests/
