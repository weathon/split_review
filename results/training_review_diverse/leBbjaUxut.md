Now I have thoroughly read and analyzed the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes the Multi-Scale Diffusion Transformer (MDiT), which reintroduces explicit multi-scale inductive biases into diffusion transformers through a shallow U-Net-like structure with aggregate blocks and heterogeneous transformer stages. The paper also provides an explainability analysis (partial-head RoPE probes and MLP classification probes) showing that DiTs inherently behave as semantic autoencoders with distinct encode-decode phases, and introduces a variance matching regularization term to improve image contrast when training with Min-SNR. The core empirical result is a 3–4× convergence speedup from the architecture alone and up to 12.5× reduction in training FLOPs versus DiT-XL at comparable FID.

## Strengths

- **Novel insight that DiTs function as semantic autoencoders, validated through two complementary tools.** The partial-head RoPE analysis (Fig. 5b–c) and MLP classification probes (Fig. 5e) independently show that isotropic DiTs transition from position-focused to semantic-focused processing and back, mirroring an encode-decode structure. This is the first systematic demonstration of this depth-wise functional characterization in diffusion transformers, going beyond the isotropic black-box treatment in prior DiT work (Peebles & Xie, 2022; Crowson et al., 2024).

- **Significant and well-quantified training speedup.** MDiT achieves a 3× speedup on FFHQ-256, 4× on ImageNet-256 B-scale, and 3.47× on ImageNet-256 L-scale over the DiT baseline under identical hyperparameters (Fig. 6). MDiT-L matches DiT-XL while requiring 12.5× fewer training FLOPs and 11.6× fewer images (Table 4). These savings are substantial and clearly documented.

- **Architectural contributions are ablated systematically.** The paper isolates the effects of LLaMA blocks, cross-attention, RoPE, and the multi-scale architecture (Table 2), identifying the multi-scale design as the largest single contributor. The correlation between probe accuracy and both FID (−0.76) and D-FID (−0.90) (Fig. 7c) provides a principled basis for architectural configuration choices.

- **Variance matching regularization addresses a real failure mode.** Min-SNR training can produce washed-out outputs, and the proposed per-channel variance matching term (Fig. 8) visibly improves contrast and vibrancy at moderate λ<sub>VAR</sub>. The gradient analysis in Figure 4 provides a mechanistic explanation for why this regularization complements MSE loss.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "accelerating convergence" claim for variance matching is not supported by the presented evidence.** The abstract and contributions state that variance matching "further accelerat[es] convergence by 3% on ImageNet-256," but the only evidence (Fig. 8a) is a single FID comparison at 300k training steps over different λ<sub>VAR</sub> values. This is a quality comparison at a fixed checkpoint, not a convergence-rate comparison. A 3% FID improvement at a fixed step could reflect faster convergence, better final quality, or both — one cannot distinguish without FID-vs-training-steps curves for multiple λ<sub>VAR</sub> values. The paper should either provide convergence curves or rephrase the claim (e.g., "improving FID by 3%").

- **The title and framing overclaim the causal role of explainability.** The title states "Explainability Leads to Faster Training," and the abstract claims the architecture "leverages this understanding" from XAI. However, the MDiT architecture (Section 3) is introduced before the explainability analysis (Section 4), and the multi-scale design appears motivated by standard inductive-bias reasoning about image structure rather than by the probe results. The XAI analysis is used to optimize the {M,N,K,L} configuration (Section 5.3), which is a genuine and interesting use, but the overall framing implies a causal arrow (XAI → architecture) that the paper does not clearly establish. The contributions remain solid if reframed as "explainability helps understand and optimize" rather than "explainability leads to."

- **The abstract and conclusion present "7× training speedup" without sufficient context.** The paper's contribution list states "accelerating convergence by 3.47× on ImageNet-256" (which is accurate for the L-scale architecture comparison), while the abstract adds "culminating in a 7× training speedup." The 7× figure is substantiated in Section 5.5, where MDiT-XL without Min-SNR matches DiT-XL at 1M steps — a valid architecture-only comparison. However, because most experiments in the paper use Min-SNR and the abstract mentions Min-SNR as part of the approach, the 7× figure can appear to compound architectural and algorithmic gains. The paper body clarifies this (line 208: "Omitting Min-SNR and variance matching to better isolate architectural performance"), but the abstract and conclusion lack this nuance. The 7× claim is defensible but would benefit from explicit qualification in the abstract.

- **Probe analysis is limited to t=0 (unconditional, no-noise setting).** The paper acknowledges this limitation (line 131), but does not discuss whether the semantic autoencoding pattern persists across noisier timesteps. This reduces confidence that the observed encode-decode behavior is a stable property of diffusion dynamics rather than an artifact of the reconstruction regime. A discussion of this scope limitation would strengthen the analysis.

### Trivial
- The text in Section 5.2 states the multi-scale architecture contributes "−22%" while the accompanying Table 2 is rendered as an image. If the table reports a different marginal contribution (e.g., −37% relative to a different baseline), the text and table would need to be reconciled so the reader can verify which baseline −22% refers to.

## Nice-to-Haves
- FID-vs-training-step curves for multiple λ<sub>VAR</sub> values would cleanly separate the "better final quality" and "faster convergence" effects of variance matching.
- Probe accuracy across multiple noise levels (t>0) would strengthen the claim that the semantic autoencoding behavior is a general property of DiTs.
- An ablation of variance matching without Min-SNR would clarify whether the regularization corrects a Min-SNR-specific artifact or offers a more general benefit.
- Comparison with more recent efficient DiT variants (e.g., MaskDiT, SiT) in a table or appendix would further contextualize the speedup, though this is not required given the already-extensive comparison suite.

## Removed Points
- *"The comparison with DiT-XL uses the original DiT-XL epsilon training... but the MDiT-L row also benefits from Min-SNR — the fairer comparison would be MDiT-L vs. DiT-XL both with Min-SNR."* **Removed:** The paper already includes a DiT-XL (mSNR) row in Table 4, providing exactly this comparison. The criticism reflects a misreading of the table.
- *"The 7× figure is misleading because it compounds architectural and algorithmic improvements."* **Downgraded to Minor:** The paper body (Section 5.5, line 208) explicitly states that the MDiT-XL models achieving the 7× speedup were trained "Omitting Min-SNR and variance matching to better isolate architectural performance." The 7× claim *is* architecture-only in the body. The abstract lacks this context but the claim is substantiated.
- *"The −22% figure does not appear in the table and the surrounding discussion is inconsistent with the numbers the table actually shows."* **Moved to Trivial:** The −22% is stated in the text. Since Table 2 is an image and cannot be independently read from the text extraction, this potential discrepancy cannot be verified from the paper alone. The authors should clarify in revision which baseline the −22% is relative to.

## Novel Insights
The most interesting finding that goes beyond the paper's own contributions is the strong negative correlation between MLP probe accuracy at the semantic-encoding peak and D-FID (−0.90), which is substantially stronger than the correlation with standard FID (−0.76). This suggests that probe-based semantic fidelity could serve as a lightweight, training-free proxy for downstream image quality when comparing architectural variants — potentially more reliable than FID and much cheaper to compute. The paper touches on this (Fig. 7c) but does not fully develop it as a methodology for architecture search; future work could systematize this into a design principle.

## Suggestions
1. Provide FID-vs-training-steps curves for multiple λ<sub>VAR</sub> values to properly support (or retire) the "accelerating convergence" claim for variance matching. If the effect is quality-only, rename accordingly.
2. Rephrase the title and framing to reflect that explainability *informs and optimizes* the architecture rather than causally *leading to* it. The paper's actual contribution — using probes as an architectural optimization signal (Section 5.3) — is already a strong and novel use of XAI without needing a stronger causal story.
3. Qualify the "7× training speedup" in the abstract (e.g., "representing up to a 7× training speedup compared to DiT-XL when comparing architecture-only performance") to match the body's precise description.
4. Add a brief discussion of the t=0 scope limitation for the probe analysis, noting whether the semantic autoencoding pattern is expected to generalize to noisier timesteps.

## Score and Decision

**Overall assessment:** The paper makes a genuine architectural contribution (MDiT) with well-documented 3–4× convergence speedups and up to 12.5× FLOP reductions. The semantic autoencoder insight is novel and well-supported. The weaknesses are minor and addressable: one overclaim about variance matching (evidence is at a single checkpoint, not convergence curves), a framing issue with the XAI causality, and ambiguous presentation of the 7× figure in the abstract. None of these undermine the core architectural claims. The paper is a solid contribution worth accepting.

**Originality:** Good — the multi-scale heterogeneous design for DiTs is novel, as is the XAI framework showing the semantic autoencoding behavior.

**Quality:** Good — experiments are thorough, ablations are systematic, and the speedup claims are well-supported by the evidence.

**Clarity:** Adequate but could be improved — the speedup presentation in the abstract is misleading without context, and the ablation percentages need clarification.

**Significance:** Good — reducing DiT training cost by 3–12× is practically valuable, and the XAI framework offers a new tool for architectural design.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>