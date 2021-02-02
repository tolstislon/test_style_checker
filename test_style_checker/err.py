"""Text and error codes"""
from typing import Dict


ERROR: Dict[str, str] = {
    "MC100": "MC100: Invalid file name",
    "MC101": "MC101: Dublicate files names:\n{}\n{}",
    "MC102": "MC102: Bad test function name {}",
    "MC103": "MC103: No 'testcase' decorator or invalid value case id",
    "MC104": "MC104: Dublicate case id: {}",
    "MC105": "MC105: Invalid function"
}
