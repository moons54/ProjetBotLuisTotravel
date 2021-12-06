#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot.with mdp"""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "52d93e78-62f5-4064-ad97-09f6dffd0316")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "+{6{_?r8>ps@f7R@sB%ESGS%XuXF2P)")
    LUIS_APP_ID = os.environ.get("LuisAppId", "bf5b04b9-91bc-41d4-926e-ca898e4e540d")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "51b95514a327424594da58bfb0319d30")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "2ba079d0-6495-476c-b009-536b5223fc5d"
    )


