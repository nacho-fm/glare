# Glare Detection API
A REST API that processes car image metadata to determine if there is a possibility of direct glare in the associated image or not. We assume there is a possibility of direct glare if:

1. Azimuthal difference between sun and the direction of the car travel (and hence the direction of forward- facing camera) is less than 30 degrees AND
2. Altitude of the sun is less than 45 degrees.

In this part we assume that the weather condition does “not” affect the glare condition, in other words, assume the weather condition is always sunny.

## Prerequisites

Python 3.7+

## Installation

From the root of the repo:
> python3 -m venv .venv 
>
> . .venv/bin/activate
>
> pip install -r requirements.txt

## Running the Flask Server on Port 5000 (Debug Mode)

> python3 -m glare/server.py
 
## Unit tests

> python3 -m glare/tests/test_services.py

## OpenAPI v3 Spec

The OpenAPI spec provided by Swagger allows for a portable way of defining an API spec. Tooling like Connexion works with Flask to make API maintenance specification driven.

The openapi/detect_glare.yaml file is the system of record for this API.

You can test it out over here: <Insert nacho.fm swagger link!

## Calculating Solar Position
Uses the NREL SPA algorithm (https://midcdmz.nrel.gov/spa/) to calculate solar position.