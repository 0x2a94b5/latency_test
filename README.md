# Latency Test

## Abount
`latency_test` used as test and log local to server latency.

## Quickstart

### Configuration
Configure the `config.ini` file and add the corresponding parameters.
Examples:
```ini
[default]
local = home
hosts = google.com
port = 80
timeout = 5
log_level = info
log_name = latency_test
```

### Startup
```shell
python latency_test.py
```
