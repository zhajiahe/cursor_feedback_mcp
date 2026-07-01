#!/usr/bin/env python3
"""
測試輔助工具
============

提供測試中使用的通用工具，例如效能計時器。
"""

import time
from types import TracebackType


class PerformanceTimer:
    """簡單的效能計時上下文管理器

    用法::

        with PerformanceTimer() as timer:
            do_something()
        print(timer.duration)
    """

    def __init__(self) -> None:
        self.start_time: float = 0.0
        self.end_time: float = 0.0

    @property
    def duration(self) -> float:
        """已耗費的秒數（尚未結束時回傳當前累計時間）"""
        if self.end_time:
            return self.end_time - self.start_time
        if self.start_time:
            return time.perf_counter() - self.start_time
        return 0.0

    def __enter__(self) -> "PerformanceTimer":
        self.start_time = time.perf_counter()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.end_time = time.perf_counter()
