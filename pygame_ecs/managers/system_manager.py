from pygame_ecs.systems.base_system import BaseSystem


class SystemManager:
    def __init__(self) -> None:
        self.systems: list[BaseSystem] = []

    def add_system(self, system: BaseSystem):
        self.systems.append(system)

    def remove_system(self, system: BaseSystem):
        self.systems.remove(system)
