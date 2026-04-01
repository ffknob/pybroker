from pybroker.ui.component import AbstractUIComponent, ComponentOptions, ComponentReturn


class BaseUIComponent(AbstractUIComponent[ComponentOptions, ComponentReturn]):
    def __init__(self):
        super().__init__()
