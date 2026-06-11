Now I have all the data needed. Let me finalize the review.

**Round 2 anchors compared:**
- DyDiT (5.50, Accepted): PKA is clearly stronger — 10× speedup vs 1.73×, cleaner motivation, more principled modular design.
- LinFusion (6.25, Rejected): Comparable. PKA has cleaner motivation and more dramatic efficiency scaling; LinFusion has broader applicability. Both have some experimental gaps. PKA slightly below due to F1 mischaracterization.
- PT-DiT (6.40, Accepted): Comparable contribution level. PKA's type-specific decomposition is more novel; PT-DiT has broader task coverage. PKA slightly below due to quality-claim issues.
- LEGO Bricks (6.67, Accepted): PKA's efficiency results are stronger but LEGO has cleaner presentation and properly scoped claims. PKA below.

**Final score: 6.0** — genuinely strong efficiency contribution held back by quality-comparison overclaiming.

---

## Summary
This paper proposes Patch-wise and Keyword-Aware Attention (PKA), a decomposed attention mechanism for efficient multi-condition control in Diffusion Transformers. PKA replaces the quadratic-cost full attention with two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one attention at aligned patch positions) and Keyword-Scoped Attention (KSA) for subject conditions (attention confined to keyword-relevant regions via a temporally-reused binary mask). Complemented by condition KV-caching and an early-timestep sampling strategy, PKA achieves up to 10× inference speedup and 5.12× VRAM reduction for the attention module while scaling near-constantly with condition count.

## Strengths

- **Attention pattern analysis motivates the design (Figures 2, 3):** The paper opens with a diagnostic analysis showing that spatial-condition attention concentrates along the diagonal and subject-condition attention localizes to keyword-relevant regions. This empirical finding directly justifies why full O(N²) attention is wasteful and motivates the two-module decomposition. The attention heatmaps are specific and interpretable.

- **PAA provides clean O(N) complexity with validated efficiency (Eq. 2, Figure 9):** Position-Aligned Attention computes attention exclusively between noisy image and spatial condition tokens at matching spatial coordinates, reducing complexity from O(N²) to O(N). The ablation (Figure 9) confirms PAA outperforms sliding window attention variants in both latency (13.63s vs. 14.00s best SWA) and VRAM (237MB vs. 276MB) while maintaining visual fidelity.

- **KSA provides tunable efficiency-quality control (Eqs. 3-4, Figure 10):** Keyword-Scoped Attention uses a lightweight attention map between image queries and 1-2 keyword tokens to generate a binary mask, then reuses this mask across timesteps to confine subject-condition attention to salient regions. The threshold ε provides an explicit control knob; Figure 10 shows graceful degradation rather than brittle collapse across ε ∈ {0.2, 0.4, 0.6, 0.8}.

- **Condition KV-caching amplifies per-step savings (Section 3.2, Figure 4a):** By restricting condition tokens to self-attend only within their own groups, the Key and Value projections become independent of the noisy image and can be cached after the first denoising step. This systems-level contribution multiplies the per-step savings of PAA/KSA across the full denoising trajectory.

- **Efficiency scales near-constantly with condition count while baselines grow quadratically (Figures 7, 8):** At 16 conditions, PKA achieves 10× inference speedup and 5.12× VRAM reduction vs. UniCombine's full attention, with PKA's time and memory remaining nearly flat as conditions increase from 1 to 16. This is the paper's headline result and directly validates the core claim that the attention bottleneck is eliminated.

- **Perturbation experiment provides principled motivation for early-timestep sampling (Figure 5):** Rather than presenting the shifted logit-normal distribution as an ad-hoc trick, the paper shows that perturbing visual conditions at early (high-t) steps drops SSIM steeply while late-step perturbations barely affect it. This empirical justification distinguishes the approach from arbitrary training heuristics.

## Weaknesses

### Fatal
None.

### Major

- **Baseline training parity is unspecified, undermining quality comparison (Table 1):** The paper fine-tunes FLUX.1 with LoRA for 20K iterations, but never states whether OminiControl2 and UniCombine were retrained under identical conditions (same base model, dataset subset, training budget, LoRA configuration). If the baselines were not retrained, the quality metrics in Table 1 do not constitute a controlled comparison. This does not affect the efficiency claims (which are architecture-inherent), but it undermines the paper's statement that PKA *improves* quality rather than trading it off.

- **Subject-Canny F1 gap is substantial and mischaracterized (Table 1):** PKA achieves an F1 score of 0.414 versus 0.551 for UniCombine on the Subject-Canny task — a 25% relative drop. The paper describes this as "a narrow margin," which is inaccurate. The paper does not address why restricting spatial attention to aligned positions produces a controllability regression on edge-guided tasks, which is precisely the kind of trade-off the method's design would predict. This should be confronted rather than dismissed.

### Minor

- **Early-timestep sampling evidence is qualitative only (Figure 11):** This is presented as a contribution, yet its evaluation consists of a single qualitative figure showing one example across three μ/δ settings at five iteration milestones. No quantitative ablation (FID, CLIP-I, F1, etc.) with and without early-timestep sampling at the end of training is provided. The perturbation analysis (Figure 5) establishes motivation but does not validate that the final trained model quality improves.

- **KSA keyword extraction mechanism is unspecified (Section 3.2.2):** The paper states that the keyword set K "typically contains just 1 to 2 tokens" but does not specify whether these are identified automatically (e.g., noun-phrase extraction) or require manual user specification. This is a practical detail that affects usability.

- **No KSA temporal consistency ablation:** The mask computed at timestep t is reused at t+1, relying on the assumption of temporal consistency in denoising. An ablation comparing mask reuse vs. recomputation would directly test this central assumption; none is provided.

- **Patch grid alignment constraint not discussed:** PAA only works when the spatial condition is tokenized identically to the noisy latent (same patch grid), which limits portability to other DiT architectures or condition encodings. This should be stated explicitly.

### Trivial
- Dataset curation criteria and train/test split details are underspecified (Section 4.1).

## Nice-to-Haves
- An explicit quality-efficiency trade-off characterization (sweep attention restriction degree and plot quality vs. compute) would strengthen the contribution beyond binary "ours vs. theirs" comparison.
- A limitations section discussing the patch grid requirement, reliance on keyword-identifiable subjects, and the fact that efficiency gains are most pronounced at high condition counts.
- Statistical treatment of results (variance across seeds/runs) for Table 1.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "The conclusion adds a forward-looking claim about video generation that is purely speculative."** Removed: this is a standard future-work mention common in conclusions, not a substantive weakness.
- **Harsh Critic: "PAA vs. SWA latency difference (13.63s vs. 14.00s) is modest."** Removed: the comparison actually favors PAA, which is simpler and faster; this is not a weakness.
- **Harsh Critic: "No limitations section."** Removed: this is a formatting observation, not a substantive weakness. The underlying concern about unstated limitations is kept as Minor weaknesses (patch grid constraint, keyword mechanism).
- **Strength Finder: "Quality metrics improve despite efficiency gains."** Weakened: the baseline training parity issue and F1 mischaracterization prevent this from being a clean strength. The efficiency results stand independently.
- **Harsh Critic: "No statistical treatment of results."** Moved to Nice-to-Haves: confidence intervals are not standard in this subfield for benchmark-scale evaluations.
- **Harsh Critic: "Condition cache is never ablated."** Removed: the KV-cache is an engineering consequence of the modular design, not a separate contribution claim requiring its own ablation. The efficiency gains include its effect and Figures 7-8 capture the combined benefit.

## Novel Insights
None beyond the paper's own contributions. The core insight — that different condition types exhibit different attention sparsity patterns that can be exploited through type-specific attention modules — is the paper's contribution.

## Suggestions
- Clarify baseline training conditions in Table 1: were OminiControl2 and UniCombine retrained on the same FLUX.1 base with the same dataset and budget? If not, acknowledge this and frame the quality comparison appropriately.
- Add a quantitative ablation for early-timestep sampling (final metrics with/without) or demote it from a contribution claim.
- Either confront the Subject-Canny F1 regression with an analysis of why it occurs (and when it matters), or acknowledge it as a known trade-off rather than a "narrow margin."
- Specify the keyword extraction mechanism for KSA.

## Calibration Anchors

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| Highlight Diffusion | 3.00 | R1 | Much weaker: training-free method, limited speedup, no multi-condition control |
| MDiT | 5.00 | R1 | Weaker: collection of architectural tweaks, less principled motivation, 7× training speedup vs PKA's 10× inference speedup |
| DyDiT | 5.50 | R2 | Weaker: 1.73× speedup vs PKA's 10×, more incremental contribution |
| LinFusion | 6.25 | R1 | Comparable: both address attention efficiency in diffusion; LinFusion broader applicability, PKA cleaner motivation; PKA slightly below due to quality-claim issues |
| PT-DiT / Qihoo-T2X | 6.40 | R1,R2 | Comparable: both reduce attention redundancy through structured sparsity; PT-DiT broader task coverage, PKA more novel decomposition; PKA slightly below due to overclaiming |
| LEGO Bricks | 6.67 | R2 | Slightly stronger: cleaner presentation, properly scoped claims, but PKA's efficiency results more dramatic |
| Würstchen | 8.00 | R1 | Much stronger: new architecture with state-of-the-art results, broader impact |
| Differential Transformer | 8.00 | R1 | Different domain (LLM), not directly comparable |

**Round 1 bracket:** 5.0–7.0. PKA is clearly above MDiT (5.00) and below the 8.0 strong band.

**Round 2 narrowing:** PKA sits between DyDiT (5.50) and PT-DiT (6.40), closer to the PT-DiT / LinFusion cluster. The efficiency contribution is genuinely strong (cleaner and more dramatic than most comparables), but the quality-comparison overclaiming and F1 mischaracterization pull it below PT-DiT (6.40) and LEGO (6.67). **Final score: 6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>