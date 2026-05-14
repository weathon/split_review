Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper studies why naive output alignment (as used in methods like ARB-X) fails for 1-bit post-training quantization of LLMs, identifying three specific failure modes: non-monotonic block-level loss, error accumulation across layers, and attention distortion. It then proposes a selective block-level quantization strategy that (1) uses the full-precision input (Output Error) rather than the quantized input as the alignment target, (2) restricts output alignment to only the final FC layer of each block, and (3) introduces an Attention Matrix Preservation (AMP) heuristic to protect token similarity structure. Experiments are reported on OPT (1.3B-30B), LLaMA-2 (7B, 13B), and LLaMA-3 (8B) across perplexity and zero-shot QA benchmarks.

## Strengths

- **Systematic diagnosis of why output alignment fails in 1-bit LLM quantization (Section 3):** The paper provides empirical evidence for three specific failure modes: (i) layer-wise output matching does not guarantee block-level loss reduction (Figure 1), (ii) quantization error accumulates across layers, causing the alignment target to drift from the true full-precision output (Figure 2, upper), and (iii) naive output matching distorts token similarity matrices and thus attention patterns (Figure 2, lower). These insights are valuable to the community and constitute a genuine contribution independent of the proposed method.

- **Practical design with no inference overhead:** The method derives closed-form updates for the binary matrix and scaling factors (Appendix B), and the AMP mechanism adds no new parameters or runtime cost at inference. The quantization overhead analysis (Appendix D, Table 6) shows the method is within acceptable range (e.g., 73 min for LLaMA-2-7B vs. 54 min for ARB-RC).

- **Component-level ablations:** The paper separately isolates the contribution of the Output Error objective (Table 4, ~0.7 PPL improvement), the AMP mask (Table 3, critical for LLaMA models), and the selective layer choice (Table 5, Appendix). This helps verify that each design choice contributes positively.

- **Broad experimental scope:** The evaluation covers three model families (OPT, LLaMA-2, LLaMA-3) across multiple scales and multiple perplexity/QA benchmarks, which is commendable if the baseline numbers are reliable.

## Weaknesses

### Fatal
- None.

### Major

- **Baseline perplexity numbers raise serious concerns about experimental reliability.** The tables are severely garbled by the parser, but the paper states that all baselines were run using C4 with sequence length 2048 (line 1012–1013) rather than their original calibration protocols. This is a defensible choice for fairness, but several reported values (e.g., ARB-X on LLaMA-2-7B PTB showing 5243.01; the paper itself acknowledges on line 565–566 that "the large perplexity indicates that the metric cannot provide a meaningful evaluation") are far enough from expected ranges to demand explanation. The paper does not present a side-by-side comparison of published numbers vs. their re-implemented numbers, nor does it clarify whether official implementations were used for baselines beyond ARB-RC (line 514 states "The ARB-RC results...were obtained by running the original ARB-RC implementation" but no similar statement is made for BiLLM, PB-LLM, or ARB-X). Because the claimed improvements hinge on outperforming these baselines, the experimental foundation is weakened until these numbers are verified.

- **The AMP mechanism is an ad-hoc heuristic without principled optimization.** The AMP mask is defined as the sign of the gradient of an attention-similarity objective (Eq. 10), then used as a binary switch to either accept or reject the closed-form candidate (Eq. 11). This is not derived from any joint optimization of the two objectives (output-error minimization and attention-similarity maximization), and there is no analysis of convergence or when this strategy might fail. While the ablation (Table 3) shows that AMP improves perplexity—especially for LLaMA models—the mechanism remains empirically motivated and lacks theoretical grounding, making its generalizability uncertain.

### Minor

- **Selective layer choice is insufficiently justified.** The paper restricts output alignment to only the "last fully connected layer of each block" (Section 4.2) based on the observation in Section 3.1 that some layers benefit from output alignment and others do not. The ablation in Table 5 (Appendix) tests one layer at a time and finds the final FC works best, but it never evaluates the combined effect of aligning multiple layers (e.g., Q/K/V + final FC, or all layers). Without this, the reader cannot tell whether the gain comes from the selective strategy itself or simply from choosing a single well-performing layer.

- **The closed-form solutions are only locally optimal.** The derivations (Eqs. 5–8) assume the Gram matrix Ŝ = X̂^T X̂ is fixed. Since X̂ changes as previous layers are quantized, the closed-form solutions are optimal for the current iteration but not globally. The paper does not discuss this approximation or quantify its impact.

- **No statistical significance or variance reported.** Single-run results are reported without confidence intervals or multiple seeds, which is common in large-scale LLM PTQ papers but limits confidence in the precise numerical advantages claimed.

### Trivial
- None that are not parser artifacts.

## Nice-to-Haves

- A side-by-side comparison table showing published baseline perplexities vs. the numbers obtained in this paper would resolve the baseline reliability concern.
- An ablation comparing selective alignment (final FC only) against aligning all layers within the same framework would strengthen the design justification.
- A simple jointly-optimized alternative (e.g., adding λ·L_AMP as a regularizer to the output-error loss) would test whether the AMP heuristic is better than a standard multi-objective approach.

## Removed Points

- **Criticism that BiLLM results "inconsistent with published results" citing specific values (e.g., 16.79):** The tables in the parsed text are severely garbled by the parser, making it impossible to verify the exact mapping between numbers, methods, model sizes, and datasets. I cannot confirm or refute the specific numerical claims without a clean table. Further, the paper's decision to use a unified calibration setup (C4, seqlen 2048) for all methods is standard practice for fair comparison in the PTQ literature. This concern is noted as a major weakness above but framed more cautiously.

- **Criticism about missing appendix/proofs:** The parser strips appendix content from all papers; these exist in the original submission.

- **Criticism about novelty relative to ARB-X already applying output alignment:** The paper explicitly acknowledges ARB-X as an output-alignment method (Section 1, lines 70–82) and clearly identifies its limitations. The paper does not claim to be the first to use output alignment.

- **Strength Finder's generic claims** such as "this paper addresses an important problem" — these are dropped as superficial.

## Novel Insights

Beyond the paper's own contributions, the synthesis of reviews highlights an interesting tension: the paper's strongest contribution (Section 3's diagnosis of why output alignment fails) is largely independent of the proposed method, yet the paper's central claim of superiority depends entirely on baseline numbers that have not been verified against published results. This suggests the paper could be restructured—possibly as a purely analytical paper about the failure modes of output alignment in 1-bit PTQ—without relying on potentially unreliable comparative numbers. The AMP mechanism's dramatically different impact on LLaMA vs. OPT (ablation Table 3) is also a potentially important finding about architecture-specific quantization sensitivity that warrants deeper investigation.

## Suggestions

1. **Verify and report baseline numbers transparently.** Run BiLLM, PB-LLM, ARB-X under their original recommended calibration settings and present a side-by-side table with the numbers from this paper's unified setup, explaining any discrepancies. Clarify whether official implementations were used for each baseline.

2. **Strengthen the ablation for selective alignment.** Evaluate output alignment on all layers versus the proposed selective scheme (final FC only) within the same framework to justify the design choice conclusively.

3. **Address the local-optimality gap in the closed-form derivations.** At minimum, add a discussion of how the alternating optimization approximates the global objective and whether there is empirical evidence of convergence.

4. **Add a controlled experiment for the RMSNorm hypothesis.** The paper hypothesizes that AMP's stronger effect on LLaMA stems from RMSNorm vs. LayerNorm (Section 5.3). A controlled experiment swapping normalization types in a small model would substantiate this claim.

## Score and Decision

**Calibration anchors** (retrieved from human review corpus, all on similar topics):

| Anchor Path | Avg Score | Comparison to This Paper |
|---|---|---|
| `/home/.../Urt7MPg1u0.md` (1-bit training) | 4.00 | Similar topic; that paper has weaker analysis but comparable experimental concerns. This paper is slightly stronger analytically. |
| `/home/.../Ra5rXQvuFP.md` (DBellQuant) | 4.00 | Similar 1-bit PTQ topic; both have experimental reliability issues. This paper has stronger diagnostic analysis. |
| `/home/.../0mqsIlMtfm.md` (PTQTP) | 3.00 | Weaker analysis and more overclaimed novelty than this paper. |
| `/home/.../yBDBCpEzsO.md` (BTC-LLM) | 3.50 | Similar quality; this paper has clearer contributions and better analysis. |
| `/home/.../KWtOTMMvKU.md` (Compression order) | 5.50 | Stronger theoretical framework and more reliable experiments. This paper is weaker on both dimensions. |
| `/home/.../QpbtT95S95.md` (QAT scaling laws) | 6.00 | Much more thorough experimental methodology and clearer contribution. This paper falls short by comparison. |

This paper has a genuine analytical contribution in Section 3 that sets it apart from the weakest 1-bit PTQ papers (avg 3.0–4.0). However, the experimental foundation is weakened by unverified baseline numbers and the AMP mechanism is heuristic. It does not meet the standard of accepted papers (avg 5.5–6.0). Relative to the anchors, a score of 4.5 accurately reflects the paper's strengths in analysis and its weaknesses in experimental validation.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>