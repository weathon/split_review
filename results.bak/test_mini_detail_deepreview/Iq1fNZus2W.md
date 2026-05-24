Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

## Summary

The paper identifies computational redundancy in multi-condition Diffusion Transformers (DiTs) that use the "concatenate-and-attend" strategy, and proposes PKA (Patch-wise and Keyword-Aware Attention), which decomposes full attention into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one attention at aligned positions, reducing O(N²) to O(N)) and Keyword-Scoped Attention (KSA) for subject-driven conditions (pruning query-key interactions to keyword-activated regions). An early-timestep sampling strategy for fine-tuning is also introduced. The method demonstrates meaningful efficiency gains — roughly 2× inference speedup over the efficient competitor OminiControl2 and up to 10× over the full-attention baseline — while being built on a well-motivated observation of attention sparsity.

## Strengths

- **Empirical grounding in attention pattern analysis (Figures 2–3):** The paper analyzes attention in existing multi-condition DiTs and shows concretely that spatial-condition attention is concentrated on the diagonal while subject-condition attention is sparse and localized. This directly motivates the two proposed modules and is not an assumed property.

- **PAA reduces complexity from O(N²) to O(N) with demonstrated efficiency gain:** Position-Aligned Attention (Section 3.2.1, Eq. 2) replaces full self-attention between noisy image and spatial condition tokens with one-to-one attention at aligned positions. The ablation (Figure 9) shows PAA achieves 13.63s latency and 237MB VRAM vs. 15.38s and 308MB without PAA, with visually comparable outputs.

- **KSA provides a tunable quality-efficiency tradeoff via mask threshold:** Keyword-Scoped Attention (Section 3.2.2, Figure 10) computes a binary mask from keyword-to-image attention and uses it to restrict attention to relevant regions. The ablation shows that at ε=0.4, KSA reduces latency from 16.99s to 15.26s and VRAM from 368MB to 242MB while maintaining subject fidelity.

- **Condition Cache is a practical engineering contribution:** Because condition tokens only self-attend within their own type, their Key and Value projections are computed once at the first denoising step and cached thereafter (Figure 4a), eliminating redundant recomputation across the entire denoising trajectory without quality degradation.

- **Perturbation analysis grounds the early-timestep sampling motivation:** Figure 5 provides a quantitative experiment showing that perturbing early (high-noise) timesteps reduces SSIM more than perturbing late timesteps, supporting the insight that visual conditions exert strongest influence early in the denoising process.

## Weaknesses

### Major

- **Quality comparison against baselines is uncontrolled for fine-tuning.** Section 4.1 states that the authors' method fine-tunes FLUX.1 via LoRA on Subject200K. It does not state that OminiControl2 or UniCombine were comparably fine-tuned on the same data. If the baselines were used off-the-shelf while the proposed method was fine-tuned on the evaluation distribution, the quality metrics in Table 1 (FID, SSIM, CLIP-I, DINOv2) predominantly reflect the fine-tuning advantage, not the architectural benefit of PKA. The paper's abstract and conclusion prominently claim PKA "maintains or improves generative quality" — this claim is unsubstantiated without controlled training conditions. The efficiency comparisons (Figures 7–8) are less affected, but the quality claim is central to the paper's messaging.

### Minor

- **Headline speedup number is inflated against a strawman baseline.** The "up to 10× inference speedup" (abstract, conclusion) is measured against UniCombine, which the paper itself characterizes as a full-attention baseline. Against the efficient competitor OminiControl2, the speedup at 16 conditions is roughly 2× (Figure 7). While 2× is still meaningful, leading with the 10× number without qualifying the comparison baseline is misleading. The paper does clarify this in Section 4.2.1 ("compared to the full-attention mechanism in UniCombine"), but the abstract and conclusion lack this qualification.

- **KSA mask reuse protocol is underspecified.** Section 3.2.2 states that a binary mask is generated at timestep t and reused at timestep t+1, invoking "temporal consistency." It does not specify whether the mask is recomputed at every even timestep, cached for multiple subsequent steps, or updated with some schedule. The efficiency analysis in Figure 10 aggregates over all steps without reporting the mask computation overhead. This ambiguity affects both reproducibility and interpretation of the reported savings.

- **Early-timestep sampling lacks quantitative validation.** Figure 11 shows only visual examples comparing different μ and δ settings. No quantitative metric (FID, subject consistency score, or convergence speed in terms of loss) is provided to support the claim that the shifted Logit-Normal distribution accelerates convergence or improves control fidelity. The single visual example is insufficient evidence.

- **Specific μ and δ values used in main experiments are not reported.** Section 3.3 states "μ > 0, δ > 1" but never gives the exact values used for the main results in Table 1 and Figures 7–8. Figure 11 shows μ=0.5, δ=1.5 for the ablation, but it is unclear whether the same values were used in the main experiments.

### Trivial

- Efficiency numbers (Figures 7–10) are reported without error bars or variance estimates. Quality metrics in Table 1 lack confidence intervals. Given the small fine-tuning budget (20K iterations on a subset), some stochasticity across runs is expected.

- The attention sparsity analysis (Figures 2–3) is qualitative only — no quantitative measurement (e.g., fraction of attention scores below a threshold) is provided to substantiate the "significant portion is redundant" claim.

## Nice-to-Haves

- A quantitative analysis of mask temporal stability for KSA (e.g., IoU between masks at adjacent timesteps) would clarify whether one-step reuse is sufficient or whether longer caching is feasible.
- Ablation of the PAA window size (currently fixed to one-to-one) would strengthen the design justification.
- A discussion of failure modes — scenarios where PAA's strict spatial alignment or KSA's keyword-based masking might lose non-local or global condition information — would improve completeness.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No citation for UniCombine in references"** — removed per hard rule: the reference list is truncated by PDF parsing; the original submission contains the full bibliography.
- **"Condition cache is standard practice, not a contribution"** — while the caching mechanism itself is standard, its application in this architecture (enabled by condition-only self-attention) is a valid contribution.
- **"Qualitative comparison differences are subtle; our method shows over-saturation"** — subjective visual judgment; not a verifiable weakness.
- **"FID values are high (52–80)"** — high FID is expected for fine-grained multi-condition tasks and is consistent across all methods; not a weakness specific to this paper.
- **"No limitations section"** — a useful suggestion but not a weakness in the paper's technical content; moved to nice-to-have.
- **"No sensitivity analysis for hyperparameters"** — ε is ablated; PAA window size is fixed by design choice; μ, δ are shown in Figure 11. Partial coverage exists.
- **"ε selection lacks principled method"** — the paper uses ε=0.2 as default and provides an ablation from 0.2–0.8 showing graceful degradation. This is standard practice; the criticism is overwrought.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Control for fine-tuning in the quality comparison:** Either fine-tune OminiControl2 and UniCombine on the same Subject200K subset under identical LoRA conditions and re-report Table 1, or clearly qualify that the quality comparison is against off-the-shelf models and present the efficiency results as the primary contribution.

2. **Specify the KSA mask protocol precisely:** State the exact schedule of mask computation (e.g., recomputed every step, every k steps, or only at step t for step t+1). If the mask is computed every step despite the "reuse" language, clarify that the efficiency gain comes from reducing KV interactions, not from mask caching.

3. **Report the specific μ and δ values used in the main experiments** and add a quantitative evaluation of early-timestep sampling (e.g., FID vs. training iterations for different sampling distributions).

4. **Reframe the headline efficiency claims** to foreground the 2× gain over OminiControl2 and clearly qualify the 10× figure as "against the full-attention baseline UniCombine."

5. **Add confidence intervals or per-run variance** for efficiency numbers and quality metrics, given the limited training budget.

## Score and Decision

**Round 1 bracket (wide search):** The paper's topic (efficient attention for multi-condition DiT control) retrieved anchors spanning ~3.0 to ~8.5. Low-band papers (3.0–3.4) had fundamental flaws in evaluation or unclear contributions; the current paper is clearly stronger. The high-band paper SANA (8.5) and Würstchen (8.0) are from a different tier — they propose holistic architectural innovations with large-scale validation. The most relevant middle-band anchors were UniCon (7.00, Accept), LinFusion (6.25, Reject), ViCo (5.50, Reject), and "Towards Enhanced Controllability" (3.75, Reject). My initial bracket: **4.5–6.5**.

**Round 2 (narrowing within bracket):** I retrieved anchors inside (4.5,6.0): ViCo (5.50), Compositional VQ Sampling (5.25), Controlled Denoising (4.60); and inside (6.0,7.5): Ctrl-Adapter (7.00), UniCon (7.00), and an RL-based method (6.50). Comparing directly:

*The current paper vs. UniCon (7.00):* UniCon has a clearer experimental setup, fewer evaluation ambiguities, and cleaner framing. The current paper's quality comparison issue and underspecified mask reuse make it notably weaker. **The current paper is below UniCon.**

*The current paper vs. ViCo (5.50):* ViCo has a weaker motivation and less novel method. The current paper has stronger grounding (attention analysis), a clearer problem framing, and more concrete efficiency measurements. **The current paper is above ViCo.**

*The current paper vs. LinFusion (6.25):* Both papers propose efficient alternatives to standard attention in diffusion models and have meaningful but incomplete evaluations. The current paper's evaluation gaps (the quality comparison issue especially) are somewhat more salient. **The current paper is slightly below LinFusion.**

*The current paper vs. Compositional VQ Sampling (5.25):* Both have evaluation concerns, but the current paper's motivation is stronger and the efficiency gains are more directly demonstrated. **The current paper is above this anchor.**

Synthesizing: the paper has genuine contributions (well-motivated design, meaningful ~2× speedup over efficient competitor, clean ablations) but is weakened by an uncontrolled quality comparison that undermines one of its headline claims and several underspecified details. This places it between ViCo (5.50) and LinFusion (6.25), closer to the former. **Final score: 5.5.** Decision: Reject — the evaluation gaps (particularly the uncontrolled quality comparison) are significant enough that the paper's claims are not adequately supported in its current form. However, these issues are addressable with additional experiments and clearer writing, and the core method is sensible.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>