Now I have all the information needed to write the consolidated review.

## Summary

This paper introduces M2rc-Eval, a repository-level code completion benchmark spanning 18 programming languages with two types of fine-grained annotations (bucket-level based on AST depth and semantic-level with 11 categories), along with a companion instruction corpus M2rc-Instruct. The benchmark is substantially broader in language coverage than existing alternatives (RepoBench: 2, CrossCodeEval: 4, R²C²-Bench: 4). The authors demonstrate that fine-tuning on M2rc-Instruct yields large and consistent improvements across three code LLMs, and the fine-grained annotations reveal meaningful performance variations across different completion scenarios.

## Strengths

- **Massively multilingual coverage (18 languages).** Table 1 directly shows that M2rc-Eval covers 18 languages vs. 2–4 for prior repository-level benchmarks. This is a clear and significant step forward in scope, addressing a genuine gap where existing benchmarks cannot evaluate general code intelligence across languages.

- **Fine-grained annotations enable diagnostic analysis.** Two orthogonal annotation axes (bucket-level via AST depth, semantic-level with 11 categories) are introduced and shown to reveal meaningful disparities — e.g., StarCoder-7B's EM varies from ~55% at deep AST nodes to ~10% at shallow nodes, and performance differs sharply across semantic categories like "Identifier and Scope" vs. "Special Language Structure." No prior repository-level benchmark provides this granularity.

- **Consistent, large improvements from M2rc-Instruct.** Across all three base models, fine-tuning on the instruction corpus yields large average EM gains: DeepSeekCoder-6.7B rises from 22.6% → 46.8%, StarCoder-7B from 21.0% → 44.5%, and Code Llama-7B from 19.4% → 41.9% (Table 3). The improvement is uniform across all 18 languages, not concentrated in a few.

- **Cross-lingual transfer insight.** The ablation fine-tuning StarCoder-7B on Python-only data (50k) achieves 39.2% EM on the full multilingual validation set, approaching the 44.4% EM from fine-tuning on all 18 languages (Table 6). This provides empirical evidence that instruction-following capability learned in one language can transfer to others.

- **Rigorous quality control pipeline.** Multiple explicit filters are applied, including ensuring test repositories are absent from the training set and discarding cases exactly predictable by a smaller model without cross-file context (§3.2).

## Weaknesses

### Fatal
None.

### Major

- **The retrieval baseline is weak and the claim that "cross file context is highly effective" (line 330) is not well supported by the +Retrieval results.** Across all three models in Table 3, the +Retrieval setting (Jaccard similarity on line-level segments) shows only modest EM gains (1–3 percentage points) while Edit Similarity consistently *drops*: Code Llama-7B ES 50.3→46.1, StarCoder-7B ES 52.0→50.0, DeepSeekCoder-6.7B ES 54.7→51.7. The Jaccard-based retrieval is a rudimentary baseline that introduces noisy context. This does not undermine the benchmark's core contribution (language coverage, annotations, instruction corpus), but the paper's framing of the retrieval results is misleading, and the benchmark's utility as a retrieval-augmented completion testbed has not been demonstrated with a reasonable retrieval method. At minimum, the paper should reframe or add a stronger retrieval baseline (e.g., BM25).

- **The large fine-tuning gains warrant stronger decontamination analysis.** The absolute improvements of 20–25 pp EM from fine-tuning are striking. While the paper ensures repositories in the benchmark are absent from the training set (§3.2, filter a), both datasets are drawn from the same source (The-Stack-v2-dedup), and file-level or snippet-level overlaps across different repositories remain possible. The paper does not report any n-gram overlap statistics or near-deduplication analysis between InStruct and the M2rc-Eval test set. The cross-lingual transfer result (Python-only → 39.2% on all languages) partially mitigates this concern by showing the effect is not limited to the trained language, but the concern should still be addressed with quantitative overlap statistics.

### Minor

- **The semantic-level annotations are not validated.** The paper defines a mapping from Tree-sitter syntax labels to 11 semantic categories (§3.4), but provides no evaluation of this mapping's quality — no manual spot-check, no inter-annotator agreement study, not even a small random sample verification. Given that the mapping is language-specific and covers 18 languages, errors are plausible. The semantic-level analyses (e.g., Fig. 6) could partially reflect annotation noise rather than genuine model capabilities. A small manual validation (e.g., 50–100 samples per language) would substantially increase confidence.

- **The training format of InStruct is underspecified.** The paper states "we just use the ground-truth to supervise the tuning process" (§3.1) but does not describe the prompt template, the infilling marker format, or how the instruction is structured. Without this, the fine-tuning setup cannot be reproduced. Providing a concrete example of the training input format is necessary for reproducibility.

- **Filter (d) uses exact match as threshold, which is extremely strict.** The quality control filter discarding test cases "exactly predicted by DeepSeekCoder-1.3B without cross file contexts" uses exact match, meaning only cases the small model gets perfectly right are removed. The paper does not report how many cases were removed by each filter, making it hard to assess the filter's impact.

### Trivial
None.

## Nice-to-Haves

- The CodeBLEU analysis (§4.5) and semantic-level analyses would benefit from being extended to more models (beyond StarCoder-7B) to show generalizability.
- The cross-lingual transfer analysis could be expanded: does Python-only fine-tuning transfer equally to structurally similar languages (e.g., JavaScript) vs. dissimilar ones (e.g., Haskell), or is the transfer uniform?
- Reporting how many test cases were removed by each quality filter would help readers assess the filtering pipeline's strictness.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper does not release the benchmark or the instruction corpus (no link, no statement about future release)."** — Removed per hard rule: criticisms about release status/availability of cited artifacts are not valid grounds for evaluation. The paper describes the construction methodology, which is the relevant contribution at the review stage.

2. **"The analysis on different model sizes... it would be more informative to also show StarCoder-7B after fine-tuning with the same amount of data (50k per language) to compare absolute gains across model sizes."** — Removed as factually incorrect. The paper already shows this comparison in Table 4: both StarCoder-3B (41.7 EM) and StarCoder-7B (44.4 EM) are fine-tuned on the same InStruct dataset.

3. **Formatting/parsing artifact observations** — Removed per hard rule: these are parser artifacts, not author errors.

4. **"Missing appendix" or "missing proofs in appendix"** — Not applicable; the reviewer did not raise this.

## Novel Insights

Beyond the paper's own contributions, the cross-lingual transfer finding is the most interesting synthetic insight from the reviews: the Python-only fine-tuning ablation achieving 39.2% EM (within ~5 points of the full 18-language 44.4% EM) suggests that a large component of the InStruct gain is instruction-following format learning rather than language-specific knowledge acquisition. This is consistent with the data contamination concern (if it were contamination, Python-only would not transfer to Haskell) but also means the absolute scores after fine-tuning may reflect format compliance rather than deep repository-level understanding. The paper's own interpretation aligns with this, but the reviews surface the tension more sharply than the paper does.

## Suggestions

1. **Address the retrieval framing.** Either reframe the +Retrieval results as a naive baseline showing that simple Jaccard retrieval is harmful (and discuss why), or add a stronger retrieval method (BM25 or RepoCoder-style retrieval) to demonstrate the benchmark's value for retrieval-augmented completion.
2. **Report n-gram overlap statistics** between InStruct and the M2rc-Eval test set to rule out data contamination as the primary driver of the fine-tuning gains.
3. **Validate the semantic annotation mapping** with a small manual spot-check (e.g., 50 samples per language), or at minimum document the mapping rules for all 18 languages.
4. **Provide the prompt template** used for InStruct training examples so others can reproduce the fine-tuning setup.
5. **Clarify the bucket ordering** explicitly (bucket 1 = shallowest, closest to root; bucket 10 = deepest, closest to leaves) in the caption or text.

## Score and Decision

This paper makes a solid contribution — its benchmark's 18-language coverage is a clear step beyond prior work, the fine-grained annotations are novel and useful for diagnostic analysis, and the instruction corpus demonstrates consistent gains. The weaknesses are real but fixable: the retrieval claim is overstated, decontamination could be stronger, and the annotations lack validation. None of these undermine the core contributions (the benchmark scale, the annotation methodology, and the instruction corpus itself). With the suggested revisions, this would be a strong contribution to the community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>