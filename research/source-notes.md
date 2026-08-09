# Source Notes

## Unicode and Language Scope

Unicode Myanmar script data can represent multiple languages. This project targets Standard Burmese writing first and must not infer Burmese correctness from character-sequence validity alone.

## Segmentation and Spacing

Burmese spacing is commonly phrase-oriented rather than a simple space-between-every-word system. Rules that blindly insert spaces between every token are unsafe.

## Normalization Boundary

Encoding normalization and language correction are separate responsibilities. The normalizer may report or transform encoding issues; the grammar checker handles Burmese language usage only after normalization status is known.

## Humanizer Evidence Boundary

The repository currently has stronger published evidence for encoding, segmentation, normalization, and general Burmese NLP evaluation than for Burmese-specific AI-writing markers. Humanizer patterns must therefore be labeled as empirical heuristics until native-reviewed evidence is collected.

## Benchmark Limitation

General Burmese NLP benchmarks are useful for model quality context, but they are not direct gold standards for social-media humanization. This project requires a task-specific native-reviewed evaluation set.
