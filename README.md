# byte-frequency-distribution-processing-module
Cuckoo Sandbox Processing module - *bytes-frequence-distribution*

## Description
Cuckoo Sandbox is the leading open source automated malware analysis system. This module is installed directly into the processing modules directory of a Cuckoo instance. It accesses the file path of the task with 'category' as 'file' and creates a byte sequence distribution table. The output value for each byte is a percentage of the total file size. In addition, shannon entropy information is also provided to provide useful information for analysis. This module is designed and tested on Cuckoo version 2.0.7. To use the module, refer to the contents below.

## Dependiencies
*bytes-frequence-distribution* is self-contained. The module has no dependencies.

## Requirements
This module is for Cuckoo Sandbox 2.0.7 which can be obtained here:
- https://cuckoosandbox.org/
- https://cuckoo.readthedocs.io/en/latest/

## Usage
1. Add the information at `$your_cwd/conf/processing.py`.
```console
$ vim $your_cwd/conf/processing.conf
# ...
[bytes]
enabled = yes
```

2. Add the information at `$your_cuckoo_instance/cuckoo/common/config.py`.
```python
class Config(object):
    configuration = {
        # ...
        "processing": {
            # ...
            "bytes": {
                "enabled": Boolean(True),
            },
        },
    }
```

3. Copy the file to `$your_cuckoo_instance/cuckoo/processing/`.
    - `cuckoo/processing/bytes.py`

4. Copy the file to `$your_cuckoo_instance/tests/`.
    - `tests/test_processing_bfd.py`

5. Test
```console
$ pytest tests/test_processing_bfd.py
```

7. Analysis
```console
$ cuckoo
$ cuckoo submit [file]
```

8. Results
```console
$ cat $your_cwd/storage/analyses/[task_id]/reports/report.json
```
