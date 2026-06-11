Now I have all the data I need. Let me finalize the review with a calibrated score.

---

## Summary
VQ-Transplant proposes a framework that decouples VQ module development from full tokenizer retraining by substituting new VQ modules into frozen pretrained tokenizers and applying lightweight decoder adaptation (~5 epochs on ImageNet-1k). The paper also introduces MMD-VQ, a nonparametric quantization method using maximum mean discrepancy. The framework is evaluated across five VQ algorithms and four datasets, demonstrating that VQ-Transplant can achieve competitive reconstruction quality at substantially reduced computational cost.

## Strengths
- **Systematic validation of the two-stage framework across five VQ algorithms**: Tables 3 and 7 consistently show that (1) VQ substitution alone degrades reconstruction, (2) decoder adaptation recovers and improves it, confirming the decoder-mismatch hypothesis. This pattern holds for both multi-scale and fixed-scale VQ across all five methods (Vanilla, EMA, Online, Wasserstein, MMD).

- **Strong cross-dataset generalization**: Tables 8-10 demonstrate that the framework transfers to FFHQ, CelebA-HQ, and LSUN-Churches — datasets outside the pretrained model's OpenImages training distribution — achieving strong reconstruction (e.g., r-FID 1.21 on FFHQ for Wasserstein VQ with adapter, outperforming all listed baselines).

- **Practical value demonstrated via from-scratch comparison**: Table 6 shows that from-scratch training of MMD VAR for 25-35 GPU-hours yields r-FID of 1.26-1.40, while VQ-Transplant achieves 0.81-0.91 in 22 GPU-hours. This demonstrates that the transplant strategy is not merely faster but qualitatively more effective at limited compute budgets.

- **MMD-VQ is a well-motivated secondary contribution**: The theoretical motivation (nonparametric distribution matching via characteristic kernels, avoiding Gaussian assumptions of Wasserstein VQ) is clearly articulated in Section 4.2, even if the empirical gains over Wasserstein VQ are modest.

## Weaknesses

### Fatal
None.

### Major
- **Speedup claims in Table 1 conflate dataset size with method efficiency**: The 21.8× speedup compares VAR trained on OpenImages (16×A100, 60h = 960 GPU-hours) against VQ-Transplant on ImageNet-1k (2×A100, 22h = 44 GPU-hours). Since OpenImages is substantially larger than ImageNet-1k, the speedup numbers are not clean measures of the framework's efficiency advantage. The paper never reports what VAR would cost trained on ImageNet-1k. The from-scratch comparison in Table 6 partially addresses this, but the headline "21.8×" and "95% cost reduction" claims remain confounded. The paper's actual strength lies in the workflow argument (once a pretrained tokenizer exists, VQ iteration costs ~22 GPU-hours), which should be the headline rather than an apples-to-oranges speedup comparison.

- **The claim of outperforming VAR requires more careful discussion regarding codebook size**: The headline result of r-FID 0.81 (MMD VAR, K=8192) vs. VAR's 0.92 (K=4096) in Table 2 combines a codebook-size increase with the method change. At equal K=4096 with 5-epoch adaptation, MMD VAR achieves r-FID 0.91, essentially tied with VAR's 0.92. However, Table 5 shows that with 20-epoch adaptation at K=4096, MMD VAR reaches r-FID 0.79, genuinely outperforming VAR at equal codebook size. The paper should discuss these nuances explicitly, and ideally report VAR at K=8192 to isolate the method's contribution from the codebook size.

### Minor
- **No downstream generation evaluation**: The paper motivates VQ research through downstream generation tasks (Section 1), yet all evaluation is limited to reconstruction metrics. There is no experiment training a generative model on tokens from the transplanted tokenizer. While reconstruction evaluation is standard in the VQ tokenizer literature, demonstrating that transplanted tokens are usable for generation would strengthen the paper's stated motivation.

- **MMD VQ and Wasserstein VQ are nearly indistinguishable empirically**: Across Tables 3, 7, 8, 9, and 10, the two methods produce very similar results. The paper claims MMD VQ handles non-Gaussian features better (Section 4.2), but never demonstrates a setting where this gap meaningfully manifests. The theoretical motivation is sound, but the empirical contribution of MMD VQ over Wasserstein VQ is limited.

### Trivial
- The parallel quantization scheme for fixed-scale VQ (splitting 32-dim into two 16-dim sub-vectors) is described but its design choices are not motivated or ablated.

## Nice-to-Haves
- Report the from-scratch training cost for VAR on ImageNet-1k specifically, to provide a clean efficiency comparison.
- Discuss when and why the framework shows reduced adaptability (e.g., LDM-16 results briefly mentioned but deferred to Appendix D), as this is material to the claimed generality.
- Include a minimal downstream generation experiment to close the gap between motivation and evidence.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **REMOVED: "The headline speedup comparison is invalid (Fatal)"** — While the dataset confound in Table 1 is a real concern (retained as Major), the harsh critic's framing as "fatal" is excessive. The paper also provides Table 6 as a same-dataset comparison, and the core workflow argument remains valid regardless of the exact multiplier.

- **REMOVED: "The from-scratch comparison is a straw man"** — The paper explicitly acknowledges the limitation ("this outcome is expected, as discrete tokenizers typically require hundreds of epochs..."). The comparison has clear practical value: at equal compute budgets, transplanting beats from-scratch training.

- **REMOVED: "The claim of outperforming VAR is entirely due to codebook size / confounded by unequal codebook sizes"** — At 5 epochs and K=4096, MMD VAR (0.91) matches VAR (0.92). But at 20 epochs and K=4096, MMD VAR-d achieves 0.79 (Table 5), clearly outperforming VAR at the same codebook size. The harsh critic overlooked the extended adaptation results. Retained a softened version of this as Major with proper nuance.

- **REMOVED: "No discussion of when the framework fails"** — The paper discusses reduced adaptability with LDM-16 (Section 5.1, last paragraph), with details deferred to Appendix D (stripped by the parser but present in the original).

- **REMOVED: "MMD VQ and Wasserstein VQ are indistinguishable — find a setting where MMD outperforms or acknowledge limited contribution"** — Softened to Minor since the theoretical motivation is valid and the empirical similarity is acknowledged by the paper.

- **REMOVED (from Strength Finder): "Convincing demonstration of massive computational savings... 21.8× speedup and 95% reduction"** — This strength directly conflicts with the verified Major weakness about the dataset confound. The savings are real but the specific multipliers are not cleanly measured.

- **REMOVED (from Strength Finder): "MMD-VQ offers a principled, nonparametric alternative" with "empirical results broadly support this"** — Retained a more tempered version. The empirical gains are marginal, so the strength claim is weakened.

## Novel Insights
The observation that VQ substitution into a frozen tokenizer creates a systematic decoder-quantization mismatch recoverable through lightweight decoder adaptation is genuinely novel. The consistent finding that distribution-aligned VQ methods (Wasserstein, MMD) minimize information loss during substitution provides actionable guidance for future VQ algorithm design within the transplant paradigm.

## Suggestions
- Reframe Table 1 to clearly separate "cost of original pretraining" from "cost of VQ iteration," making the workflow argument the headline rather than cross-dataset speedup comparisons.
- Add explicit discussion of the codebook-size effect with reference to the 20-epoch results in Table 5, which show genuine outperformance at equal K=4096.
- Consider adding a setting where MMD VQ meaningfully outperforms Wasserstein VQ, or explicitly acknowledge the empirical similarity.

## Score and Decision

### Calibration Anchors
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Alternating Optimized Stochastic VQ (4XHyThqt1C) | 3.50 | R1 | VQ-Transplant is clearly stronger — more extensive experiments, clearer contribution |
| Wasserstein VQ / Distribution Matching (nS2DBNydCC) | 4.75 | R1 | VQ-Transplant builds on this but adds a practical framework, broader experiments, and MMD extension; meaningfully stronger |
| Binary Spherical Quantization (yGnsH3gQ6U) | 5.75 | R1/R2 | BSQ has a more novel core quantization method and includes downstream generation; VQ-Transplant is slightly weaker |
| epsilon-VAE (8ROIRnKloJ) | 5.67 | R2 | Comparable quality; epsilon-VAE has more novelty in its decoder design |
| ImageFolder (QE1LFzXQPL) | 6.25 | R1 | ImageFolder is clearly stronger — more novel core idea, downstream generation evaluation |
| Rotation Trick for VQ (GMwRl2e9Y1) | 8.00 | R1 | Much stronger — more principled, more novel, cleaner evaluation |

**Bracket (Round 1)**: 4.5–6.5. VQ-Transplant sits between the Wasserstein VQ paper (4.75, which it extends) and ImageFolder (6.25, which is a stronger tokenizer contribution).

**Narrowing (Round 2)**: VQ-Transplant is comparable to but slightly below BSQ (5.75) and epsilon-VAE (5.67). It is clearly above the Wasserstein VQ paper (4.75). The headline claim issues (dataset confound, codebook size nuance) and lack of downstream generation prevent it from reaching the 6+ tier.

**Final score**: 5.5 — a borderline accept/reject paper with genuine practical value and extensive experiments, held back by confounded headline claims and missing downstream evaluation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>