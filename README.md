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

## Python metrics

See `python/` for metric scripts and their expected inputs.

## License

Unlicense / public domain. See `LICENSE`.
