Now I will write the final consolidated review.

## Summary

AdaSVD proposes two complementary techniques for SVD-based LLM compression: **adaComp**, which post-truncation alternately updates the U and Vᵀ matrices using a Moore-Penrose pseudoinverse formulation to compensate for truncation error, and **adaCR**, an input-output cosine similarity heuristic that assigns per-layer compression ratios. The paper reports consistent perplexity improvements over SVD-LLM and other baselines across multiple LLMs (LLaMA2-7B, OPT-6.7B, Vicuna-7B, Mistral-7B) and compression ratios (40–80%).

## Strengths

1. **Moore-Penrose pseudoinverse update (MPPU) for stable optimization.** Figure 3(a) shows the proposed SVD-based pseudoinverse update produces a smooth, monotonic MSE decrease over 25 update steps, while the naive closed-form inverse fluctuates wildly. This is a concrete technical improvement over the direct inverse formulation (Eq. 6–7) and directly enables the reported error reduction.

2. **Consistent and sizable gains at high compression ratios.** Table 1 shows AdaSVD reduces WikiText-2 perplexity from SVD-LLM's 89.90 to 50.33 at 60% compression on LLaMA2-7B (44% relative improvement), and from 16.11 to 14.76 at 40%. These improvements hold across all three language modeling datasets and five commonsense reasoning benchmarks, and across compression ratios from 40% to 80%.

3. **Orthogonality to quantization is empirically validated.** Table 4 shows AdaSVD+GPTQ-INT4 consistently outperforms SVD-LLM+GPTQ-INT4 at every compression ratio from 40% to 80%, demonstrating that adaComp's benefits are not redundant with quantization but stack additively.

4. **Clean ablation design.** Table 3(a–b) cleanly isolates the contributions of adaComp and adaCR. The controlled comparison shows that both components contribute substantially and independently — e.g., at 60% compression, AdaSVD without adaComp scores 78.82 (already beating SVD-LLM's 89.90), while adding adaCR brings it to 50.33.

5. **Empirical characterization of inter-layer importance diversity.** Figure 4 systematically measures normalized layer importance across 8 LLMs, showing that the first layer consistently has the highest importance and that LLaMA models exhibit a bowl-shaped importance curve, providing direct motivation for the adaCR design.

## Weaknesses

### Major

1. **V-update derivation (Eq. 13) has a dimension inconsistency and discards calibration data.** The paper's alternating optimization claims to minimize L_SVD = ||U_k^σ (V_k^σ)ᵀ X − W X||²_F. The U update (Eq. 6, 8–10) properly incorporates the calibration data X through the least-squares formulation. However, Eq. 7 and Eq. 13 give the V update as V_k^σ = ((U_k^σ)ᵀ U_k^σ)⁻¹ (U_k^σ)ᵀ W = ((U_k^σ)†)ᵀ W — an expression with **no dependence on X** and a **dimension mismatch** (U_k^σ is m×k, giving ((U_k^σ)†)ᵀ as m×k, which cannot multiply W (m×n) to yield the expected n×k output). This asymmetry between the U and V updates is neither acknowledged nor explained. While the method empirically works, the mathematical presentation is incorrect or incomplete as written, undermining confidence in the correctness of the claimed alternating optimization procedure.

2. **Baseline perplexity numbers for prior methods show extreme values at moderate compression ratios that are not discussed.** At 40% compression, SVD-LLM achieves PTB perplexity of 719 (vs. original 8.35) and at 50% reaches 1,772 on PTB and 129 on C4. While the paper notes that FWSVD and ASVD "fail on these LLMs with compression ratios under 60%," and the authors state they used official GitHub repositories, the SVD-LLM numbers at PTB are orders of magnitude worse than the original model in ways that are not compared against SVD-LLM's own published results. The paper would be stronger if it acknowledged whether these baseline reproductions are consistent with published numbers and explained any discrepancies. (Note: SVD-LLM's WikiText-2 numbers at 40% — 16.11 — are within reasonable range for compressed LLMs; the concern is concentrated on PTB and C4.)

3. **VLM evaluation is only qualitative.** Figure 5 presents four cherry-picked image captioning examples with color-coded correct/wrong spans. This is weak evidence for a general claim about VLM performance. Quantitative metrics (CIDEr, BLEU, or language perplexity on the VLM's language component) would be far more informative.

### Minor

4. **adaCR is a simple heuristic without comparison to alternatives.** The cosine-similarity-based importance metric is plausible but not theoretically grounded, and the paper does not benchmark it against alternative importance metrics (e.g., Fisher information as used by FWSVD, singular-value-based measures, or per-layer loss sensitivity). The ablation in Table 3b shows adaCR adds real value, but its effectiveness relative to other heuristics is unknown.

5. **No statistical significance or variance reporting.** All evaluations appear to be single-run with no confidence intervals or standard errors. Given stochasticity in calibration data sampling, variance reporting would strengthen the reliability of the comparisons, especially when margins are small (e.g., 25.58 vs. 27.19 at 50% on WikiText-2).

### Trivial

6. **Notation inconsistency for V_k^σ.** The paper uses V_k^σ in Eq. 2 as n×k (absorbing Σ^{½}), but in Eq. 7 and throughout Section 3.1 treats it as a k×n matrix without explicit transposition. This makes the derivation hard to follow and contributes to the dimension mismatch in Eq. 13.

## Removed Points

These points were raised by reviewers but are removed per the filtering rules:

- **"Original model has C4=45.30 and Mmlu=7.34 which are incorrect."** — This is likely a PDF-to-text parser column-alignment artifact; the same row shows WikiText-2=5.68 and PTB=8.35 which are correct for LLaMA2-7B. Removed as a formatting/parser artifact.
- **"The paper lacks inference latency/throughput measurements."** — This is outside the paper's stated scope (perplexity and accuracy comparison with prior SVD methods). The paper notes that SVD compression can accelerate inference; measuring speedup is a nice-to-have but not a required weakness.
- **"Missing 70%/80% results in the main paper."** — The paper explicitly states these are in the supplementary, which is standard practice given page limits.
- **Several generic criticism sweeps from the Harsh Critic (e.g., "the evaluation lacks rigor," "the comparisons may not be fair") without specific anchoring** — Removed as they are area-of-concern speculations, not concrete problems identified from the paper.
- **Criticism about "SVD-LLM achieves single-digit perplexities in its own paper"** — The 16.11 reported here is low-double-digit and within a reasonable range; the reviewer's claim about SVD-LLM's performance cannot be verified without access to that paper, and the rules prohibit doubting cited references.

## Nice-to-Haves

- Report inference speedup and actual memory reduction from SVD weight decomposition
- Include 70% and 80% compression results in the main paper (currently in supplementary)
- Benchmark adaCR against alternative importance metrics (Fisher information, singular-value-based measures)
- Compare stack-of-batch strategy against alternatives (e.g., gradient accumulation, larger GPU batches)

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective or synthesis that the paper's own framing misses.

## Suggestions

1. **Fix the V-update derivation.** Clarify the dimensions: state whether the variable being solved for is V_k^σ (n×k) or (V_k^σ)ᵀ (k×n), and derive the update rule with the calibration data X included. If the V update genuinely does not require X, explain why this is justified given that the U update does require it. If the implementation uses a different (correct) formula from what Eq. 13 writes, correct the equation.

2. **Address the baseline discrepancy.** Add a column or footnote comparing reproduced SVD-LLM perplexities against the numbers reported in the SVD-LLM paper (Wang et al., 2025) to demonstrate faithful reproduction, or explain any differences.

3. **Add quantitative VLM metrics** (CIDEr, BLEU, or language perplexity after compression) to complement the qualitative examples in Figure 5.

4. **Report variance** across multiple calibration-data samples, even if just 2–3 runs with standard deviation, especially for close comparisons.

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing) anchors:**
- `ZTvUT49JjL` — Matrix factorization theory (avg 3.40, reject) — unrelated topic, not comparable
- `0T8vCKa7yu` — Convex optimization quantization (avg 3.00, reject) — unrelated topic
- `HyPofygOCT` — ASVD: Activation-aware SVD for LLMs (avg 6.25, reject) — directly comparable SVD compression method. AdaSVD has better experimental breadth and comparable methodological novelty, but ASVD does not have a mathematical derivation error.
- `gp32jvUquq` — Basis Sharing: cross-layer SVD sharing (avg 6.50, accept) — stronger conceptual novelty, slightly cleaner evaluation.
- `3KEwJGYNzH` — AutoTrunc: SVD truncation selection (avg 4.00, reject) — AdaSVD is clearly stronger empirically.

**Round 2 (narrowing) anchors:**
- `ho7ZUS1z8A` — MoE-SVD (avg 5.00, reject) — AdaSVD has broader evaluation and better ablations; comparable in technical depth.
- `DLDuVbxORA` — OATS: sparse + low-rank compression (avg 6.25, accept) — comparable empirical quality; AdaSVD has cleaner method framing but the OATS paper has no mathematical errors.
- `DwiwOcK1B7` — DSF: Double Sparse Factorization (avg 6.33, accept) — stronger theoretical framework.

**Round 1 bracket:** 4 to 7. **Round 2 refined bracket:** 4.5 to 5.5.

**Comparative assessment:** AdaSVD is clearly stronger than MoE-SVD (5.0) — it has more datasets, cleaner ablations, and better writing. It is weaker than ASVD (6.25) because ASVD's primary weakness was novelty (being similar to SVD-LLM), whereas AdaSVD has a mathematical correctness issue in its core derivation that the authors must fix. The paper sits between these two anchors in quality: the experimental work is solid, but the derivation error in Eq. 13 is a real flaw that needs correction before the paper can be accepted.

**Score:** 5.0

**Decision:** Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>