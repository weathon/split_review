I have thoroughly reviewed the paper and all reviewer claims. Let me now produce the final consolidated review.

---

## Summary

This paper introduces Set-MI, a method that improves membership inference in language models by aggregating membership predictions over sets of documents that share a common attribute (e.g., creation date, license type, language) and are therefore expected to share training membership status. The key contribution is reformulating MI from individual-document prediction to set-level prediction, which reduces variance and yields a consistent average gain of 0.14 AUROC over four prior Individual-MI methods across five newly constructed benchmarks (Wikipedia, Arxiv, Language, License, Instructions). The paper also provides systematic ablations of model size, deduplication, document length, and set size, and demonstrates robustness to violations of the set assumption.

## Strengths

1. **Novel set-based reformulation of membership inference.** The insight that documents sharing natural attributes (creation date, license, language, dataset source) are likely to share training-membership status is genuinely new and well-motivated. The idea is simple yet effective — averaging individual MI scores over such sets yields an average AUROC gain of 0.14 across five benchmarks (Table 2), a substantial improvement over the Individual-MI baselines that barely exceed random (0.5–0.6 AUROC). This reframing opens a new direction for MI research.

2. **Construction of the first set-based MI benchmarks spanning five diverse domains.** The paper creates evaluation benchmarks for Wikipedia, Arxiv, Language, License, and Instructions, each leveraging natural metadata (creation date, language, license type, dataset source) to form sets satisfying the set assumption (Section 4, Table 1). These benchmarks enable standardized evaluation of set-level membership inference in realistic, multi-domain scenarios and are likely to be reused by the community.

3. **Systematic ablation of factors affecting Set-MI performance.** The paper isolates the effects of target model size (70M to 12B), training data deduplication, document length (16 to 2,048 tokens), and set size (1 to 100 documents). Key findings — larger models and unduplicated data yield larger gains from aggregation, and even sets of only 3 documents provide significant improvement (Figures 3–4) — give practical guidance for applying Set-MI.

4. **Robustness analysis under noisy set assumptions.** Section 6 explicitly tests violations of the set assumption by injecting noise into member and/or non-member sets, and shows that all three aggregation methods (MAX, MIN, FULL) still outperform Individual-MI across noise ratios from 0.0 to 0.9. The analysis also provides practical guidance on which aggregation to choose based on noise type, which strengthens the paper's practical utility.

## Weaknesses

### Major

- **The Wikipedia and Arxiv benchmarks rely on creation-date proxies without direct verification of actual membership in the training corpus.** The paper labels ground-truth membership based on whether a document's creation date precedes the Pile's data-collection cutoff (2020-03-01 for Wikipedia, 2020-08-01 for Arxiv), rather than directly verifying that each document appears in the Pile. The Pile undergoes filtering, deduplication, and snapshotting, so some pre-cutoff documents could be absent. While the paper's robustness analysis (§6) uses a clean version with 13-gram overlap verification and shows Set-MI is robust to noise, the main experimental results (Table 2) rest on unvalidated proxy labels. This does not threaten the relative comparison between Set-MI and Individual-MI (since both use the same labels), but it means the absolute AUROC values reported for these two benchmarks may not reflect true membership inference performance. The authors should verify membership by exact overlap (which they demonstrate capability for in §6) for at least a representative sample, or clearly quantify how many documents from their sampled sets are actually missing from the Pile.

### Minor

- **The Language benchmark uses documents from Redpajama but Bloom-7B (trained on ROOTS) as the target model, introducing potential source mismatch.** Membership is determined at the language level (whether the language was used in Bloom's training), but the specific Wikipedia articles and versions from Redpajama may not perfectly coincide with those in the ROOTS corpus. While the set-level aggregation and the paper's noise robustness analysis mitigate this concern, the benchmark's labels are a proxy that could introduce unknown noise. Re-running using documents actually drawn from ROOTS, or providing evidence of substantial overlap, would strengthen this benchmark.

- **The reported correlation of 0.824 (p=0.0002) between Individual-MI and Set-MI performance (§5.1) lacks a specified sample size.** The paper does not state how many data points this correlation is computed over. While it could be computed across all 20+ entries in Table 2 (which would make the p-value reliable), the paper should explicitly report the sample size and the conditions over which the correlation is computed to allow readers to assess its statistical validity.

- **The document length analysis (§5.4) is presented as a figure without explanation of why Set-MI benefits more from longer sequences than Individual-MI.** A brief explanation (e.g., variance reduction from more tokens, or that longer sequences provide stronger memorization signals) would improve the discussion.

### Trivial

- The main results (Table 2) lack confidence intervals or error bars. Given the stochasticity in subsampling documents and token sequences, reporting means over multiple runs would improve reliability.

## Nice-to-Haves

- **Practical guidance for discovering sets in the wild.** The paper acknowledges that metadata availability is an assumption but does not discuss how a practitioner would identify candidate sets without ground-truth knowledge. A brief "how to use Set-MI in practice" paragraph with concrete examples (e.g., using public timestamps, license metadata, or dataset provenance) would increase the paper's impact.

- **A control baseline that aggregates Individual-MI scores at the set level without the set assumption** (e.g., randomly partitioning documents into pseudo-sets and averaging). This would isolate whether the benefit comes from the set assumption itself or simply from any form of aggregation.

- **Explanation of the document length effect** (moved from Minor, as this is a presentation gap rather than a flaw in results).

## Removed Points

- **Criticism about "the evaluation relies on the assumption that sets are perfectly known and clean"** — The paper explicitly acknowledges this limitation in the conclusion ("Our work makes an assumption that the metadata about the dataset of interest is available...leave relaxing this assumption for future work"). This is a proper scoping decision, not an oversight. Moved to Nice-to-Haves.

- **Claim that the correlation is "likely only 5–6 data points"** — The actual sample size is not stated but Table 2 contains at least 20 entries (5 benchmarks × 4 methods), making the critic's specific count speculative. The general concern about reporting sample size is kept as a Minor weakness.

- **Request for "larger-scale verification" framed as a fatal flaw** — The paper already has overlap-verified labels in §6; the critic's demand adds marginal value. The underlying concern about main-experiment proxy labels is kept as Major, but the framing as a fatal issue is removed.

## Novel Insights

None beyond the paper's own contributions. The key insight — that documents sharing natural metadata attributes tend to share membership status and can be exploited via simple aggregation — is the paper's own conceptual contribution.

## Suggestions

1. For the camera-ready version, verify membership for at least a representative subsample of documents in the Wikipedia and Arxiv benchmarks using exact 13-gram overlap (as done in §6). Even verifying 100 documents per benchmark would substantially increase confidence in the main results.
2. Report the sample size and conditions over which the Individual-MI / Set-MI correlation is computed.
3. Add a brief discussion of the document length effect — e.g., whether the benefit comes from variance reduction, stronger memorization signals in longer sequences, or both.
4. Add error bars or confidence intervals to Table 2, computed over multiple random subsamples of documents and token sequences.

## Score and Decision

The paper makes a solid, well-motivated contribution. The core idea (set-level aggregation for MI) is novel, clearly presented, and convincingly demonstrated across multiple benchmarks and ablations. The main limitation — that two of the five benchmarks use proxy labels — is partially addressed by the robustness analysis with verified labels. The weaknesses are addressable and do not undermine the central contribution. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>