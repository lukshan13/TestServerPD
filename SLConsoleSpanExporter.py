#Author : Lukshan Sharvaswaran
#Implements ConsoleSpanExporter
## Exports json in a single line

from opentelemetry.sdk.trace.export import ConsoleSpanExporter
import typing
from typing import Optional
from os import linesep
import sys
import json

from opentelemetry.sdk.trace import ReadableSpan, Span, SpanProcessor
from opentelemetry.util._once import Once


class SLConsoleSpanExporter(ConsoleSpanExporter):
    
    def __init__(
        self,
        service_name: Optional[str] = None,
        out: typing.IO = sys.stdout,
        formatter: typing.Callable[
            [ReadableSpan], str
        ] = lambda span: json.dumps(json.loads(span.to_json()))
        + linesep,
    ):
        self.out = out
        self.formatter = formatter
        self.service_name = service_name