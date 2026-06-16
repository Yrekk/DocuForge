from enum import StrEnum


class AppMode(StrEnum):
    NONE = "none"
    OFFLINE = "offline"
    PROMPT = "prompt"
    APPLICATION = "application"


class FormKeyPrefix(StrEnum):
    OFFLINE = "offline_field"
    PROMPT = "prompt_field"
    APPLICATION = "application_field"


APP_MODES = [
    {
        "label": "Choisir un mode",
        "value": AppMode.NONE,
    },
    {
        "label": "Génération documentaire offline",
        "value": AppMode.OFFLINE,
    },
    {
        "label": "Génération de prompt",
        "value": AppMode.PROMPT,
    },
    {
    "label": "Assistant candidature offline",
    "value": AppMode.APPLICATION,
},
]