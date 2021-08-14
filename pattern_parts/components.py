from abc import ABC, abstractmethod
from typing import TypeVar
from patterns.simple_discord import SimpleMember
from patterns.pattern_error import *
from json import JSONEncoder, dumps
import inspect
from patterns.pattern_part import PatternPart

component = TypeVar("component", bound="Component")
Statement = TypeVar("Statement")


class ComponentEncoder(JSONEncoder):
    def default(self, o):
        return o.to_dict()


class Component(PatternPart):

    @abstractmethod
    def __init__(self):
        """
            Dummy constructor because otherwise my fucky auto-importing of components and operators in channels_file_managers won't work
        """
    @abstractmethod
    def user_applies(self, member: SimpleMember) -> bool:
        """
            Abstract method that gets called when a Statement wants to know if a user applies to a component
        """

    @abstractmethod
    def reverse(self) -> component:
        """
            Abstract method that returns the reverse of self
        """
    #@abstractmethod
    def optimize(self, super_component: component) -> component:
        """
            method that returns an optimized version of self
        """                       

    def simplify(self) -> component:
        """
            Returns a simplified version of self
        """
        return self

    @abstractmethod
    def from_string(self)
    """
        Parses self from string
    """