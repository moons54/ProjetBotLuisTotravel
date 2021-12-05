#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot.with mdp"""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "039dc8b4-511a-45a2-b144-c8fb30795859")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "6bbb51e473e3469baddc39e0830e5af4")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://mybotluisoc-authoring.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "b6dc2b99-2c28-4b4f-87fe-4fa764ed78eb"
    )