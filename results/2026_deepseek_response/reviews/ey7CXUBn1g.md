Now I have sufficient calibration data. Let me compose the final review.

## Summary

AdaSVD proposes two innovations for SVD-based LLM compression: (1) **adaComp**, which alternately updates the truncated U and V matrices using Moore-Penrose pseudoinverse solutions to minimize reconstruction error on calibration data, and (2) **adaCR**, which assigns layer-specific compression ratios based on input-output cosine similarity. Experiments across LLaMA2-7B, OPT-6.7B, Vicuna-7B, and Mistral-7B show consistent improvements over SVD-LLM and other SVD baselines at 40-60% compression ratios on language modeling and commonsense reasoning benchmarks, with additional validation on LLaVA vision-language models and in combination with GPTQ quantization.

## Strengths

1. **Consistent and demonstrable improvements over SVD-LLM across multiple model families.** Table 1 shows AdaSVD reduces WikiText-2 perplexity from 16.11→14.76 (8.4% relative improvement) at 40% compression and from 89.90→50.33 (44% relative) at 60% on LLaMA2-7B. Table 2 confirms this advantage extends to OPT-6.7B, Vicuna-7B, and Mistral-7B at 60% compression, where AdaSVD is the only method maintaining reasonable perplexity while outperforming SVD-LLM consistently. The gap widens at higher compression ratios, which is where the method is claimed to matter most.

2. **Both proposed components (adaComp and adaCR) are individually validated through controlled ablations.** Table 3a shows adaComp alone (without adaCR) improves PPL from 15.47→14.76 at 40% and from 78.82→50.33 at 60%. Table 3b shows adaCR alone improves PPL from 27.33→25.58 at 50% and from 69.46→50.33 at 60%. Each component contributes meaningfully and independently.

3. **Orthogonality to weight quantization is demonstrated.** Table 4 shows AdaSVD+GPTQ-INT4 consistently beats SVD-LLM+GPTQ-INT4 at every compression ratio (e.g., 82.08 vs 119.46 at 60% on WikiText-2), confirming the benefits persist when combined with another compression technique.

4. **Generalization to vision-language models.** Figure 5 shows qualitative improvements in image captioning when AdaSVD is applied to the language backbone of LLaVA-7B at 40% compression, providing evidence of broader applicability beyond pure LLMs.

5. **The alternating pseudoinverse formulation demonstrably stabilizes MSE reduction.** Figure 3(a) shows the method converges smoothly while the naive approach (direct matrix inversion) produces erratic updates, establishing a clear practical motivation for the pseudoinverse formulation.

## Weaknesses

### Fatal
None.

### Major

1. **Practical quality of compressed models at the tested ratios is severely degraded, which limits the significance of the claimed contribution.** At 60% compression, AdaSVD achieves PPL 50.33 on WikiText-2 (original: 5.68) — roughly a 9× increase. Average commonsense reasoning accuracy drops from 68.85% to 36.87% at 60% and to 42.63% even at 40%. While AdaSVD outperforms the baselines (many of which are completely broken, with PPL in the thousands), the paper frames its results as "narrowing the performance gap between compressed and original models" without qualifying that the gap remains enormous. The paper claims to "push the performance boundary" but does not identify any operating point where the compressed model is practically usable. This issue applies broadly to SVD-based LLM compression at these ratios, but the paper does not adequately contextualize this limitation or demonstrate that its improvements translate to practically useful models.

2. **The alternating update procedure does not consistently benefit from more iterations, raising questions about whether it converges to a useful optimum.** Table 3c shows that **1 iteration of adaComp outperforms 3 and 15 iterations** at both 40% (14.76→15.84) and 50% (25.58→27.45) compression. Even at 60%, the best result is at 1 iteration (50.33 vs 64.12 at 3 iterations). The paper attributes this to "overfitting due to limited calibration data," but this explanation is not tested (e.g., by varying calibration set size). The fact that more alternating iterations never improve results on 7 of 9 comparisons in Table 3c suggests the benefit comes entirely from a single pseudoinverse update, not from the alternating procedure itself. A comparison against a simple gradient-descent baseline with a tuned learning rate is missing; without it, it is unclear whether the pseudoinverse formulation itself matters or whether any reasonable optimizer would suffice.

### Minor

3. **Runtime and memory overhead of adaComp are not reported.** The paper never states how long the compensation step takes or how much additional GPU memory it consumes. For a compression method targeting resource-constrained deployment, the computational cost of the compression procedure itself is directly relevant. This gap is noted by multiple prior SVD compression papers at similar venues (e.g., ASVD, MoE-SVD) as a recurring weakness in the field.

4. **The adaptive compression ratio may not exactly preserve the total parameter count.** Equation (19) sets each layer's retention ratio proportional to its normalized importance, with mean normalization ensuring the average ratio equals the target. However, since layers differ in size, importance-larger-layer correlations could cause the actual total parameter count to deviate from the target. The paper does not verify that total parameters match the baseline uniform-ratio setting — a minor fairness gap in the comparison.

5. **Methodological novelty is modest.** The pseudoinverse solution to a least-squares problem is a standard numerical technique (Section 3.1, Equations 8–13), and its application to post-SVD compensation is a straightforward engineering adaptation. The stack-of-batch strategy (Equations 14–15) is simple data averaging. The adaCR importance metric (cosine similarity between input and output) is a simple heuristic. While the combination is sensible and well-validated, the individual components do not represent new algorithmic ideas.

### Trivial

- The paper states it evaluates at 70% and 80% compression ratios with results deferred to supplementary; these results are not present in the main text due to page limits.

## Nice-to-Haves

- A comparison against a simple gradient-descent baseline with a tuned learning rate in Figure 3(a) would clarify whether the pseudoinverse formulation is genuinely beneficial or whether standard optimization would suffice.
- An investigation into the "overfitting" explanation for why more iterations hurt — a calibration data size sweep would clarify this directly.
- Actual total parameter counts achieved by adaCR vs. target to verify fair comparison.

## Removed Points

These points were flagged by reviewers but are removed from the main review with justification:

- **"Catastrophic perplexity invalidates the entire evaluation"** — Overstated. The paper compares against SOTA SVD-based methods under identical conditions and shows consistent improvements. The perplexities are high because these are aggressive compression ratios across all SVD methods, not because of a flaw specific to AdaSVD. The paper never claims the compressed model matches the original; it claims to "narrow the performance gap" relative to prior SVD methods, which it demonstrably does. This criticism would apply equally to the entire subfield (ASVD, SVD-LLM, etc.) and is not a reason to dismiss this paper's specific contribution.

- **"adaCR may artifactually favor specific layers by under-compressing important layers"** — The mean normalization in Equation (18) ensures the average compression ratio equals the target (trr). The concern about total parameter count mismatch is kept as Minor weakness #4, but the artifact concern is addressed by the paper's math.

- **"Figure 1 values (~1.1–1.2) cannot be correct"** — The figure plots perplexity on a log10 scale, so values of ~1.1–1.2 correspond to PPL of ~12–16, consistent with Table 1. The critic misinterpreted the log-scaled axis.

- **"Missing comparison to non-SVD methods (GPTQ, AWQ)"** — The paper's scope is SVD-based compression; it explicitly states this scope. A GPTQ integration experiment is already provided (Table 4). Demanding standalone comparison to quantization methods is scope creep.

- **"Missing appendix content (70-80% results)"** — Per hard rules, the parser strips appendices; these exist in the original submission.

- **"Missing related works"** — Cannot be verified without external sources.

- **Formatting, typo, and presentation nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report the compression ratio at which AdaSVD achieves practically usable quality (e.g., PPL within 20% of original) and position the contribution around extending this usable compression range rather than comparing degrees of degradation.
2. Add runtime and peak-memory measurements for the adaComp procedure to address a standard expectation for compression papers.
3. Include a gradient-descent baseline (with tuned learning rate) in the comparison of Figure 3(a) to establish whether the pseudoinverse formulation genuinely matters.
4. Report actual total parameter counts achieved by adaCR vs. the target ratio to verify fair comparison.
5. Investigate why 1 iteration is optimal at lower compression ratios — a calibration data size sweep would distinguish overfitting from other explanations.

## Calibration Report

**Round 1 — Bracketing (3 bands):**

| Band | Anchor Path | Avg Score | Sim | Comparison |
|------|------------|-----------|-----|------------|
| Weak (< 3.5) | ZTvUT49JjL | 3.40 | 0.72 | Substantially weaker; implicit matrix factorization, not LLM compression |
| Weak (< 3.5) | GtlRN48XYA | 3.00 | 0.68 | Federated fine-tuning LoRA; less rigorous experiments |
| Weak (< 3.5) | 0T8vCKa7yu | 3.00 | 0.68 | LLM quantization with convex optimization; thin evaluation |
| Weak (< 3.5) | 04RLVxDvig | 3.00 | 0.68 | NanoMoE; parameter-efficient blocks; limited comparison |
| Middle (3.5–7.5) | FVgizbs3o2 | 3.75 | 0.77 | TensorGPT; tensor-train embedding compression; AdaSVD stronger |
| Middle (3.5–7.5) | ho7ZUS1z8A | 5.00 | 0.77 | MoE-SVD; MoE-specific SVD compression; AdaSVD more general + better ablations |
| Middle (3.5–7.5) | 3KEwJGYNzH | 4.00 | 0.76 | AutoTrunc; truncation position search; AdaSVD more comprehensive |
| Middle (3.5–7.5) | HyPofygOCT | 6.25 | 0.76 | ASVD; activation-aware SVD; broader influence but AdaSVD comparable on evaluation |
| Strong (> 7.5) | f4gF6AIHRy | 8.00 | 0.68 | Data selection for pre-training; different topic, much stronger paper |
| Strong (> 7.5) | TwJrTz9cRS | 8.00 | 0.67 | LoRA variant (HiRA); different topic, much stronger claims + evaluation |
| Strong (> 7.5) | vf5aUZT0Fz | 8.00 | 0.67 | Embedding decoupling for pre-training; different topic, much stronger |

**Initial bracket: 4.5–6.5** — Clearly above the weak-band papers and below high-band papers.

**Round 2 — Narrowing (4.5–6.5 and 6.0–8.0):**

| Anchor Path | Avg Score | Sim | Comparison |
|------------|-----------|-----|------------|
| FA3iYp1y6z (LRC) | 5.00 | 0.76 | Low-rank correction for quantized LLMs; AdaSVD has broader experiments but similar novelty concerns → AdaSVD slightly stronger |
| DM6Q45HWSk (EVA) | 4.75 | 0.74 | LoRA initialization via SVD; different task; AdaSVD more thoroughly evaluated |
| DwiwOcK1B7 (DSF) | 6.33 | 0.77 | Double sparse factorization; accepted; stronger novelty (ADMM formulation) |
| B9klVS7Ddk (LLM-KICK) | 6.75 | 0.76 | Compression evaluation benchmark; accepted; stronger novelty (benchmarking contribution) |
| gp32jvUquq (Basis Sharing) | 6.50 | 0.76 | Cross-layer SVD basis sharing; accepted; stronger novelty (parameter sharing idea) |
| xw29VvOMmU (LQ-LoRA) | 6.75 | 0.75 | Low-rank + quantized decomposition; accepted; stronger novelty + more impactful results |

**Final score determination:** AdaSVD sits between the 5.00-level papers (LRC, MoE-SVD) and the 6.25–6.75 papers (ASVD, DSF, Basis Sharing, LQ-LoRA). It has comparable evaluation breadth to ASVD (6.25) but weaker novelty — its core techniques are standard mathematical tools (pseudoinverse, cosine similarity, data averaging) applied to a specific problem, whereas ASVD introduced activation-aware weight transformation. It is stronger than MoE-SVD (5.00) and LRC (5.00) which had narrower evaluation and similar novelty concerns. The practical quality degradation at tested ratios is a real concern shared with all SVD-compression papers in this space. **Final score: 5.5**, reflecting solid incremental work with thorough evaluation but modest novelty, placing it below the ICLR acceptance threshold.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>