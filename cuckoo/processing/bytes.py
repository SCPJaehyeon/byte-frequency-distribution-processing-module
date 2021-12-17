import os
import math
import logging
from cuckoo.common.abstracts import Processing
from cuckoo.common.objects import File
log = logging.getLogger(__name__)

class ByteFrequencyDistribution(Processing):
    """Get byte frequency distribution table & shannon entropy results."""

    def _get_byte_frequency_table(self, file_path):
        """Get byte frequency table dict.
        @param file_path: file path.
        @return: byte frequency table(over 0) dict or None.
        """
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
        except IOError as e:
            log.exception(e)
            return {}
        frequency_table = {}
        byte_arr = map(ord, data)
        filesize = len(byte_arr)
        for byte_idx in range(256):
            cnt = 0
            for byte in byte_arr:
                if byte == byte_idx:
                    cnt += 1
            if cnt > 0:
                frequency_table[str(format(byte_idx,'02X'))] = round((float(cnt) / filesize) * 100, 3)
        if not frequency_table:
             return {}
        return frequency_table

    def _get_shannon_entropy(self, bytefreq):
        """Calculate shannon entropy(min bits per byte-character).
        @param bytefreq: byte frequency list.
        @return: shannon entropy float.
        """
        ent = 0.0
        for freq in bytefreq:
            freq = freq / 100
            if freq > 0:
                ent = ent + freq * math.log(freq, 2)
        ent = -ent
        return round(ent, 3)

    def run(self):
        """Run byte frequency distribution analysis.
        @return: analysis results dict or None.
        """
        self.key = "bytefreqdist"
        if self.task["category"] == "file":
            if not os.path.exists(self.file_path):
                return {}
            f = File(self.file_path)
        else:
            return {}

        try:
            frequency_table = self._get_byte_frequency_table(f.file_path)
            if frequency_table:
                frequency_table["shannon_entropy"] = self._get_shannon_entropy(frequency_table.values())
            return frequency_table
        except Exception as e:
            log.exception(e)
            return {}

