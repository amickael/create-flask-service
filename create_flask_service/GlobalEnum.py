from enum import Enum


class GlobalEnum(Enum):
    TEMPLATE_DIR = "template"
    PLACEHOLDER = "{{ %SERVICE_NAME% }}"
