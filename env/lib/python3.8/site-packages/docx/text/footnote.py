from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from ..enum.style import WD_STYLE_TYPE
from .parfmt import ParagraphFormat
from .run import Run
from .paragraph import Paragraph
from ..shared import Parented

from datetime import datetime
import re

class Footnote(Parented):

    def __init__(self, fn, parent):
        super(Footnote, self).__init__(parent)
        self._fn = self._element = fn

    @property
    def paragraph(self):
        return Paragraph(self._fn.p, self)
    

    @property
    def text(self):
        return self.paragraph.text
