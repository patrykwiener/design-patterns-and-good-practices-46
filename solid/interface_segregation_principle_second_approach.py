from abc import ABC, abstractmethod


class OfflineProductActionsInterface(ABC):
    @abstractmethod
    def find_in_outlet(self):
        pass


class OnlineProductActionsInterface(ABC):
    @abstractmethod
    def try_for_seven_days(self):
        pass


class ReviewableProductActionsInterface(ABC):
    @abstractmethod
    def show_reviews(self):
        pass


class ProductActionsInterface(
    OfflineProductActionsInterface,
    OnlineProductActionsInterface,
    ReviewableProductActionsInterface,
    ABC,
):
    pass


class ComputerActionsUI(OfflineProductActionsInterface, ReviewableProductActionsInterface):
    def find_in_outlet(self):
        pass

    def show_reviews(self):
        pass


class SoftwareActionsUI(OnlineProductActionsInterface, ReviewableProductActionsInterface):
    def try_for_seven_days(self):
        pass

    def show_reviews(self):
        pass
