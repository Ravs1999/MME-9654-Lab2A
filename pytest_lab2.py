# SPDX-FileCopyrightText: 2021-2022 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

import pytest
from pytest_embedded import Dut


@pytest.mark.esp32
@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.esp32c3
@pytest.mark.esp32c6
@pytest.mark.esp32h2
@pytest.mark.generic
def test_lab2(dut: Dut) -> None:
    dut.expect_exact('lab2: Create RMT TX channel')
    dut.expect_exact('lab2: Install led strip encoder')
    dut.expect_exact('lab2: Enable RMT TX channel')
    dut.expect_exact('lab2: Start LED rainbow chase')
