#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot.with mdp"""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "52d93e78-62f5-4064-ad97-09f6dffd0316")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "nolss2d4320wslec4azej2mqruuhk8zlwstcoluj")
    LUIS_APP_ID = os.environ.get("LuisAppId", "bf5b04b9-91bc-41d4-926e-ca898e4e540d")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "51b95514a327424594da58bfb0319d30")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://westeurope.api.cognitive.microsoft.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "b6dc2b99-2c28-4b4f-87fe-4fa764ed78eb"
    )


