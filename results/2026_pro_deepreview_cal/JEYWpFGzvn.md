Now I have a clear picture. Let me assemble the final review.

**Bracket**: InfoTok sits clearly above ElasticTok (6.00) and below LARP (7.50). The closest comparator is "On the Role of Discrete Tokenization" (7.00), which has more rigorous theory but less comprehensive empirical method contribution. InfoTok's empirical results are strong but its theoretical claims have issues, so I settle on **6.5**.

---

## Summary
InfoTok proposes an adaptive video tokenizer that dynamically allocates tokens based on per-video information complexity. It uses an ELBO-based router to determine token lengths and a transformer-based compressor to select which tokens to keep. Empirical results show InfoTok significantly outperforms the prior adaptive method ElasticTok — achieving ~2× better reconstruction quality at matched compression rates, while requiring 11× fewer network evaluations at inference time.

## Strengths
- **Strong empirical gains over ElasticTok**: Table 1 and Figure 4 show InfoTok achieves substantially better PSNR (+1–2 dB), LPIPS (−25–40%), and FVD (−40–60%) at matched BPP levels. At comparable reconstruction quality, InfoTok supports ~2.3× higher compression rates than ElasticTok.
- **Efficient single-pass inference**: Figure 4g demonstrates InfoTok needs only 1 extra decoder pass to determine token allocation, versus 11 forward evaluations for ElasticTok's binary search. This makes adaptive tokenization practically deployable.
- **ELBO-based router validated against optimal search**: Table 2 shows InfoTok's ELBO-guided token allocation achieves reconstruction quality extremely close to an exhaustive search-based optimal strategy (e.g., PSNR 29.86 vs 29.92), confirming the router effectively approximates ideal per-video budgets without brute-force search.
- **Compressor design validated by ablation**: Table 3 (Left) shows that ELBO-based token selection outperforms right-to-left and spatially-dispersed masking strategies. Table 3 (Right) further demonstrates the full InfoTok mechanism (ELBO router + compressor) generalizes across both Cosmos 3D-CNN and ViT backbones.
- **Well-motivated problem framing**: The paper uses Shannon's source coding theorem (Theorem 2.1) and a suboptimality proof for uniform routers (Theorem 2.2) to clearly articulate why content-dependent tokenization is necessary, providing a principled narrative for adaptive tokenization.

## Weaknesses

### Major
- **Theorem 3.1 (near-optimality guarantee) has a log-base consistency issue**: The bound states $\mathbb{E}[N_x] \leq H_C(\mathbb{D}) + \beta - \mathbb{E}[-\log p(\mathbf{x})]$, where $H_C(\mathbb{D}) = \mathbb{E}[-\log_C p(\mathbf{x})]$ is base-$C$ entropy. If $\log$ (unsubscripted) denotes the natural logarithm — as is standard in the VAE/ELBO literature the paper draws from — then the term $\mathbb{E}[-\log p(\mathbf{x})]$ is in nats while $H_C(\mathbb{D})$ is in base-$C$ units. With $\mathbb{E}[N_x] = \beta$ by construction, the inequality reduces to requiring $0 \leq H_C(\mathbb{D}) - \mathbb{E}[-\ln p(\mathbf{x})]$, which is negative for any $C > e$ and non-degenerate distribution. If instead all logs are base-$C$, the bound collapses to $\beta \leq \beta$ (trivial). Either way, the claimed "near-optimal compression guarantee" is not properly established by the presented theorem. This is significant because the paper repeatedly frames the router as "principled" and "information-theoretically optimal" based on this guarantee; the empirical method does not collapse without it, but the theoretical contribution is overstated.

### Minor
- **Per-token ELBO computation is not described**: Section 3.2 states the compressor preserves "the top $N_x$ tokens according to their corresponding per-token log-likelihood, which is also approximated via the ELBO values" and that this "does not incur extra network evaluation since the log-likelihood term has been computed in the router." However, the router computes only a *single global* reconstruction error (one extra decoder pass). How per-token importance scores are derived from this global quantity is never explained. While a plausible mapping exists (pixel-level reconstruction errors can be aggregated to token regions via spatial correspondence in the 3D-CNN encoder), the current text leaves a core algorithmic step unspecified. This matters for reproducibility.
- **ElasticTok comparison alignment is underspecified**: Section 4.1 states "Since ElasticTok's adaptiveness is governed by a loss threshold rather than an average compression rate, we align our methods with their settings." The procedure for mapping ElasticTok's loss thresholds to specific BPP values is not described. While the same-backbone ablation in Table 3 (Right) partially mitigates concerns about backbone mismatch, the head-to-head Table 1 comparison procedure remains opaque.
- **No standard deviations or confidence intervals reported**: All metric values in Tables 1–3 and Figure 4 are reported as point estimates. Without variance information, it is difficult to assess whether small differences (e.g., InfoTok 0.81 vs Cosmos-DV 1.00, PSNR 30.08 vs 30.01) are meaningful or within noise.
- **KL term proportionality claim is unverified**: Section 3.1 states that using only the reconstruction error (without the KL term) in the router is sufficient because "the KL term is approximately proportional to the reconstruction error." No empirical evidence or analysis is provided to support this shortcut.

### Trivial
- **The "2.3×" compression factor is approximate**: The paper cites this figure with "e.g." in the text, acknowledging it as an illustration rather than a precise measurement. Clarifying the exact operating point where this factor is computed would improve precision.

## Nice-to-Haves
- A plot of ELBO vs. $-\log p(\mathbf{x})$ for sample videos would strengthen the claim that ELBO is a reliable proxy for information complexity.
- Analysis of how consistent ELBO-based length assignments are across random restarts, or how sensitive reconstruction quality is to the $\beta$ calibration.
- Extension to video generation tasks, which the paper acknowledges as a limitation but would significantly strengthen the contribution.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Theorem 2.2 is in an artificially restricted setting"** — REMOVED. The theorem proves a specific and valid claim: uniform routers are suboptimal even with optimal training. The oracle assumption is a standard proof technique, not a flaw. The paper explicitly states it is analyzing the simplified inference stage.
- **Harsh Critic: "Missing implementation details (optimizer, epochs, hardware)"** — REMOVED per hard rules. These are standard appendix details; the paper references Appendix C, which is stripped in this format.
- **Harsh Critic: "The binary mask application point is unclear"** — REMOVED. Section 3.2 adequately describes the mask is computed in the adaptive compressor and applied to select tokens. The description is high-level but sufficient.
- **Strength Finder: "Rigorous theoretical motivation" and "near-optimal compression guarantee"** — QUALIFIED. The theoretical framing (Theorems 2.1, 2.2) is sound, but Theorem 3.1 has a log-base issue that weakens the optimality guarantee. The paper's empirical contributions remain strong independent of this theorem.
- **Harsh Critic: "Theorem 3.1 is mathematically incoherent — fatal error"** — DEMOTED to Major. The theorem has a genuine issue but this does not invalidate the empirical method; the router design (allocate tokens proportional to ELBO) is independently motivated and validated. The error weakens the theoretical contribution but does not make the paper unsalvageable.

## Novel Insights
The paper makes a concrete connection between variational inference (ELBO) and adaptive tokenization that goes beyond prior work. While ElasticTok used heuristic uniform masking, InfoTok shows that the ELBO — already computed during standard VAE training — can serve as a practical, zero-additional-cost signal for both (a) deciding how many tokens a video needs globally, and (b) selecting which specific tokens carry the most information locally. Table 2's demonstration that this simple ELBO-based allocation nearly matches an exhaustive search optimum is a genuinely striking result that suggests the VAE training objective already encodes rich information about per-sample complexity that prior adaptive methods were not exploiting.

## Suggestions
- **Fix Theorem 3.1**: Either use a consistent log base throughout (e.g., define all quantities in base-$C$ or all in nats with appropriate scaling) and verify the bound, or reframe the theorem as stating that $\mathbb{E}[N_x] = \beta$ when $\beta$ is set to approximate the entropy, rather than claiming a formal inequality. The empirical validation in Table 2 already strongly supports the router's effectiveness without a tight theoretical bound.
- **Describe per-token scoring**: Add 1–2 sentences explaining how per-token ELBO values are derived — e.g., by backprojecting pixel-level reconstruction errors through the decoder's spatial structure to assign responsibility to individual latent tokens. A diagram or equation would further clarify this.
- **Report variance**: Add standard deviations or confidence intervals to Table 1 and Figure 4. This is especially important when claiming that InfoTok "saves 20% tokens without influence on performance" (where PSNR differences are <0.2 dB).
- **Specify the ElasticTok alignment procedure**: Describe how ElasticTok's loss thresholds were mapped to the reported BPP values, and confirm whether the same backbone architecture was used for the ElasticTok rows in Table 1.

## Score and Decision

**Calibration anchors used across rounds:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| ElasticTok | tFV5GrWOGm | 6.00 | R1 | InfoTok directly improves on ElasticTok's method with better routing, efficiency, and results |
| BSQ-ViT | yGnsH3gQ6U | 5.75 | R1 | Different focus (quantization), InfoTok has comparably strong empirical validation |
| "How many tokens is an image worth?" | mb2ryuZ3wz | 5.75 | R2 | Adaptive image tokenization; InfoTok handles the harder video domain |
| "On the Role of Discrete Tokenization" | WNLAkjUm19 | 7.00 | R2 | Stronger theory but narrower empirical scope; InfoTok's theory is weaker but method contribution is broader |
| LARP | Wr3UuEx72f | 7.50 | R2 | More complete pipeline (reconstruction + generation), SOTA on video generation; InfoTok lacks generation experiments |

**Round 1 bracket**: 6.0–7.5. InfoTok is clearly above ElasticTok (6.00) and clearly below the 8.00 landmark papers.

**Round 2 narrowing**: InfoTok sits between ElasticTok (6.00) and "On the Role of Discrete Tokenization" (7.00). It outperforms ElasticTok on every axis (theory, efficiency, results), but its central theoretical claim (Theorem 3.1) has a verifiable notation issue, and the method description has gaps (per-token ELBO, comparison procedure) that LARP-level papers typically cover more rigorously. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>