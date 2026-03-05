"""
API Request/Response Schemas
=============================

Yeh file mein kya kya hoga:
- IngestRequest: Document upload ke liye request model
- IngestResponse: Upload success/failure response
- QueryRequest: User question ke liye request model
- QueryResponse: AI answer + sources + metadata
- Document: Document metadata structure
- ChatMessage: Conversation history ke liye
- ToolCall: Agent tool execution tracking
- AgentState: LangGraph state definition
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime


# TODO: Add Pydantic models here
