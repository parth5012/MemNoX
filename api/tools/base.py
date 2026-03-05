"""
Base Tool Class
===============

Yeh file mein kya kya hoga:
- Tool interface/abstract class
- Common tool methods
- Tool metadata (name, description, parameters)
- Error handling wrapper
- Tool execution logging
- Input validation
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseTool(ABC):
    """
    Base class for all tools
    """

    name: str = "base_tool"
    description: str = "Base tool description"

    @abstractmethod
    async def execute(self, **kwargs) -> Dict[str, Any]:
        """
        Tool execution logic - har tool ko implement karna padega
        """
        pass

    def validate_input(self, **kwargs) -> bool:
        """
        Input parameters validate karta hai
        """
        # TODO: Implement validation
        pass
