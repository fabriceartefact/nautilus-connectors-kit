# GNU Lesser General Public License v3.0 only
# Copyright (C) 2020 Artefact
# licence-information@artefact.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
from tenacity import (
    retry as _retry,
    wait_exponential,
    before_sleep_log,
    before_log,
    stop_after_attempt,
)
import config
import logging


def retry(fn):
    return _retry(
        wait=wait_exponential(multiplier=1, min=4, max=10),
        stop=stop_after_attempt(5),
        reraise=True,
        before=before_log(config.logger, logging.INFO),
        before_sleep=before_sleep_log(config.logger, logging.INFO),
    )(fn)
