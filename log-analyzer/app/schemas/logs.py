#Write pydantic schemas here to validate data format
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


#Add schema classes to validate incoming data
#Replace field and class names accordingly
class LogLevel(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
class LogSchema(BaseModel):
    id: int
    title: str
    level: LogLevel
    source: Optional[str] = "unknown"
    timestamp: Optional[datetime] = None