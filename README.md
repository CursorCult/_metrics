# CursorCult Metrics (`_metrics`)

This repo defines **standard benchmark metrics** that `_benchmark_<RULE>` repos can reuse.

## Structure

Metrics are grouped by language:

```text
python/
  code_coverage.py
```

## Metric contract

A metric is a program/script that:

- reads an agreed-upon input artifact (e.g. a JSON report)
- prints **exactly one number** to stdout (with optional trailing newline)
- prints nothing else

That single number is the metric value (higher-is-better unless the metric says otherwise).

## Standard Artifacts

Benchmarks should emit the following files into their `artifacts/` directory to use these metrics:

### Python Coverage (`code_coverage.py`)
- **Input**: `coverage.json`
- **Format**: Standard JSON output from `coverage json`.
- **Usage**: `python3 python/code_coverage.py <path/to/coverage.json>`

## License

Unlicense / public domain. See `LICENSE`.