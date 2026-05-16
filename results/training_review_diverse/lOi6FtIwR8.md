Here is my final consolidated review:

---

## Summary

This paper introduces ProFS (Projection Filter for Subspaces), a tuning-free weight-editing method that reduces LLM toxicity by identifying a low-dimensional toxic subspace in MLP layers via SVD on centered embedding differences and projecting model weights out of that subspace. The authors ground the method in factor analysis theory, position it as a sample-efficient, noise-robust alternative to DPO, and provide theoretical/empirical evidence that ProFS can be interpreted as a denoised single-step approximation of DPO gradients.

---

## Strengths

- **Robustness to labeling noise is cleanly demonstrated.** Figure 2 shows ProFS is nearly unaffected even when 50% of preference labels are flipped, while DPO degrades sharply. This is a concrete practical advantage for real-world alignment with noisy annotations, and the evidence is clear.

- **The method works with very small datasets.** ProFS achieves meaningful toxicity reduction with as few as 5–50 datapoints (Table 1, Section 6), which is a genuine practical contribution regardless of how DPO would fare at comparable data sizes.

- **Principled theoretical framing via factor analysis.** The decomposition of sentence embeddings into toxic, context, and corpus-mean components (Equation 2), and the argument that SVD on centered embedding differences recovers the toxic subspace, gives the editing procedure a non-heuristic justification that goes beyond prior editing work.

- **Both theoretical and empirical connections to DPO.** The derivation showing that a single DPO gradient step operates on embedding differences in a manner analogous to ProFS (Section 5), combined with the empirical correlation of 60–80% variance explained (Figure 4), provides a genuine bridge between the editing and tuning paradigms.

- **Centering ablation cleanly isolates the mechanism.** Table 5 shows that including the corpus mean direction in the edit catastrophically increases perplexity, which directly supports the design choice and validates the factor model's separation of the mean component.

- **Generalization beyond toxicity is demonstrated.** On HH-Golden (multi-preference dataset), ProFS achieves a higher GPT-4o-mini-judged win rate than DPO when both use 500 datapoints (Table 4), showing the approach is not limited to toxicity.

- **Layer-wise analysis validates the L₀ hyperparameter choice.** Figure 3 systematically shows that editing only higher layers preserves perplexity while maximizing toxicity reduction, consistent with prior findings about hierarchical encoding in transformers.

---

## Weaknesses

### Major

- **The sample-efficiency claim is not adequately supported by controlled comparison.** The paper states that ProFS requires "orders of magnitude less data" than DPO (Abstract, line 61, line 247), but the evidence rests on comparing ProFS at 500 datapoints to DPO at 2,000 datapoints (Table 1). DPO is never evaluated at lower data sizes (e.g., 50, 100, 500). Without testing DPO at multiple data quantities, the reader cannot distinguish between the hypothesis that DPO fundamentally needs more data and the alternative that DPO at 500 would be comparable. ProFS's ability to work with 5–50 datapoints is a real strength, but the *comparative* "orders of magnitude" claim requires equal-data experiments. This is the single most significant weakness in the paper's evidence for its headline contribution.

### Minor

- **Capability evaluation for GPT-2 (the primary model) is limited to perplexity on WikiText-2.** Perplexity is a coarse measure that can remain low while generation quality degrades. The paper does evaluate larger models on seven zero-shot tasks (Section 6, following wei2024assessing), which is appropriate for those models, but the GPT-2 experiments—which form the bulk of the empirical work—lack any downstream-task validation (e.g., LAMBADA, BLiMP, or even a human evaluation of generation quality).

- **The factor model assumes the context component is identical for toxic/non-toxic sentence pairs** (Equation 2: both share the term $\tilde{\mathbf{B}} \tilde{\mathbf{f}}_i$). This is a strong assumption that is stated (line 186) but not validated. If the context components differ systematically (e.g., because the toxic and non-toxic sentences from PPLM generation are not semantically parallel), then the difference matrix $\mathbf{T}_\ell$ captures not only the toxic subspace but also context mismatches. A synthetic experiment or residual analysis would strengthen the theoretical framing.

- **The selection of $k$ is not justified.** The paper uses $k=2$ for GPT-2 and $k=10$ for all other models (line 225) without reporting an ablation over $k$ (e.g., singular value decay curve, or toxicity vs. perplexity trade-off as $k$ varies). The paper does ablate $L_0$ (Figure 3) but not $k$, which is equally important for understanding the method's sensitivity.

- **Sentence embedding computation is underspecified.** The paper states "We compute the sentence embeddings of $x_i^+, x_i^-$" (line 141) but does not specify how—are these obtained by averaging over token embeddings, taking the last token, or some other aggregation? This is needed for exact reproducibility.

- **Data-size inconsistency across experiments is not explained.** In the toxicity experiments, DPO uses 2,000 datapoints while ProFS uses 500. In the HH-RLHF experiment (Table 4), both methods use 500. If DPO and ProFS are competitive at equal data (500) on HH-RLHF, why does DPO require 2,000 for toxicity? This is not inherently contradictory (toxicity may be a harder signal to learn), but the paper does not address the discrepancy, which could confuse readers about when the sample-efficiency claim applies.

### Trivial

- None.

---

## Nice-to-Haves

- Run DPO at multiple dataset sizes (25, 50, 200, 500, 2000) on the toxicity task and plot toxicity reduction vs. data size for both methods. This would directly substantiate (or qualify) the "orders of magnitude" claim.
- Add at least one downstream evaluation for GPT-2 (e.g., LAMBADA, StoryCloze) or a human evaluation of fluency/coherence of edited generations.
- Validate the shared-context assumption synthetically: construct data that obeys the factor model and verify that SVD recovers the correct subspace.
- Ablate over $k$ (e.g., 1, 2, 5, 10, 20) for GPT-2, showing toxicity vs. perplexity to justify the choice.
- Specify how sentence embeddings are aggregated (average pooling, last token, etc.).

---

## Removed Points

These points from the original reviews are flagged to be removed — treat them with caution:

- **"The bound (Equation 9) is stated without proof... relies on the appendix which is not available."** — Removed per hard rule: the parser strips appendix content; the bound and its proof exist in the original submission.
- **"The table (proj_to_vocab_censored) is not visible in the text."** — Removed per hard rule: this is a parser artifact; the table exists in the original submission via `\input`.
- **"Missing appendix" / "missing proofs in appendix"** — Removed per hard rule: parser strips appendix sections.
- **"The baseline (random matrix) should be drawn from the same distribution as the gradient"** — Removed as an overly specific technical nitpick that does not affect the paper's conclusions. The random matrix baseline (averaged over 10 draws) is a standard and reasonable null model.
- **"The claim that ProFS is the only method robust to label noise is expected because other methods were not designed for noise"** — Removed: the paper is making an empirical observation, not an unfair comparison. Reporting which methods are and are not noise-robust is standard scientific reporting.
- **Certain formatting/style nitpicks** (paragraph-level phrasing complaints) — Removed per hard rules on parser artifacts.

---

## Novel Insights

The reviews converge on a key structural observation: the paper's most exciting claim (sample efficiency via editing) and its most ambitious claim (editing as a denoised DPO) are in partial tension. The DPO-connection experiments (Section 8) show that ProFS's subspace explains 60–80% of DPO gradient variance, and that the correlation *increases* with sample size — which is consistent with the theory that DPO needs many samples to average noise. But if DPO at small sample sizes produces noisy gradients that ProFS "denoises," then the clean comparison would be ProFS vs. DPO at *the same small sample size*, not ProFS at 500 vs. DPO at 2000. The paper's strongest framing would be: "ProFS equals or exceeds DPO at any given data quantity, and degrades far more gracefully as data shrinks or noise increases." The current framing of "orders of magnitude less data" overreaches relative to the evidence, but the underlying phenomenon — that a direct subspace extraction method beats a gradient-based method in low-data, high-noise regimes — is well-supported by the ablation (5–50 samples) and noise robustness experiments. The contribution is real; the evidence just needs to be structured to match the claim.

---

## Suggestions

1. Add equal-data comparisons for DPO at 50, 200, and 500 samples on the toxicity task. This is the single most impactful addition — it would either validate the "orders of magnitude" claim or reveal its boundary conditions.
2. Add one downstream evaluation for GPT-2 (e.g., LAMBADA or a simple NLI task) to strengthen the capability preservation claim.
3. Add an ablation over $k$ (number of singular vectors) for GPT-2, showing the toxicity/perplexity trade-off curve and the singular value decay.
4. Specify how sentence embeddings are computed (pooling method) for reproducibility.
5. Briefly explain why DPO is used with 2000 samples in the toxicity experiment but 500 in the HH-RLHF experiment — even a single sentence clarifying that toxicity is a sparser/noisier signal would resolve the apparent inconsistency.

---

## Score and Decision

The paper introduces a well-motivated, interpretable editing method with genuine practical advantages (noise robustness, very-low-data operation) and provides a theoretically grounded connection to DPO that is novel. The core methodology is sound and the main empirical demonstrations hold. However, the central comparative claim ("orders of magnitude more sample efficient than DPO") is not adequately supported because DPO is only tested at one data size. This is a major but fixable weakness — it does not invalidate the paper's other contributions, but it does mean the paper's strongest advertised result requires additional evidence.

**Score:** 6.0 / 10

**Decision:** Accept — the paper's methodological contribution, noise-robustness demonstration, and theoretical framing are substantive enough to warrant publication, with the expectation that the sample-efficiency claim will be properly scoped or fully supported in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>