Now I have a good calibration picture. Let me synthesize the final review.

**Round-1 bracket:** The paper clearly sits above SUN (4.0) and Deep Unlearning (5.25) but I need to place it relative to stronger papers. Initial bracket: **5.5 – 7.5**.

**Round-2 narrowing:** Jogging the Memory (6.75) investigates relearning attacks — directly relevant to irreversibility claims. MoRE is a method paper with strong empirical results but overclaims on irreversibility. Decoupling the Class Label (5.75) is a similarly-scoped unlearning paper. MoRE lands **between 5.75 and 6.75** — stronger than Decoupling, but not as airtight as Jogging, because MoRE's central irreversibility claim against fine-tuning is unevaluated.

Final score: **6.0**.

---

## Summary

MoRE proposes a training-free post-hoc layer for feature-level machine unlearning. It introduces three ideas: (i) prototype-orthogonal (PO) projection to decorrelate forget and remain prototypes before erasure, preventing utility degradation; (ii) remapping forget prototypes to remain prototypes via a mixture of experts to scatter forget features and make them indistinguishable at the feature level; and (iii) efficient activation-mean prototypes for scalability. The method is evaluated on class-wise and instance-wise unlearning across CIFAR-10/100, Tiny-ImageNet, and ImageNet, plus a concept-unlearning task on Stable Diffusion, using both standard accuracy metrics and Knowledge Retention (KR) to measure resistance to linear-probe recovery.

## Strengths

- **PO projection effectively preserves remain utility during erasure.** Table 3 shows that without PO projection, erasure leaves 14.38% residual forget accuracy and degrades remain utility; with PO, forget accuracy drops to 0% while remain accuracy is preserved. Figure 6 corroborates this by showing remain prototype autocorrelations stay near 1.0 after unlearning.

- **Strong resistance to linear-probe recovery (KR evaluation).** Table 1 shows that under KR, MoRE suppresses forget accuracy to near random-guessing levels (e.g., 10.79% on CIFAR-10, 0.07% on CIFAR-100, 0.50% on Tiny-ImageNet), dramatically outperforming all baselines including ESC, ESC-T, and even the retrain-from-scratch model, which recovers substantially (e.g., 72.62% on CIFAR-10 KR).

- **Computationally efficient and scalable.** Figure 5 demonstrates MoRE completes unlearning in under 10 seconds with under 200 MB GPU memory on CIFAR-10/100, using only a single forward pass and lightweight linear algebra.

- **Generalization to diffusion models without architecture-specific adaptation.** Table 2 and Figure 4 show MoRE applied out-of-the-box to cross-attention layers of Stable Diffusion achieves the best LPIPS_d tradeoff (0.25–0.26), qualitatively removing Van Gogh's style while preserving prompt composition.

- **Robust to hyperparameter choices.** Sensitivity analyses (Figure 7, Tables 5–6) confirm stable performance across numbers of experts, remapping targets, and router designs.

## Weaknesses

### Fatal

None.

### Major

- **Irreversibility claim against fine-tuning is unevaluated.** The abstract and introduction state that MoRE "imped[es] recovery via fine-tuning" (line 13) and "significantly imped[es] the recovery of forgotten knowledge through fine-tuning or linear probing" (line 122–123). However, the only recovery attack evaluated is the KR metric, which trains a *linear probe* on frozen post-unlearning features. A linear probe is substantially weaker than unfreezing the full model and fine-tuning on forget data. Since MoRE leaves the original feature extractor weights untouched (it inserts a fixed linear transformation after the feature extractor), a fine-tuning attack could plausibly recover the forget class by retraining the feature extractor to route around the MoRE layer. Without this experiment, the headline claim of irreversibility against fine-tuning is unsupported. This is the paper's most significant evidential gap and directly affects the primary selling point.

### Minor

- **Post-hoc wrapper nature not discussed as a limitation.** MoRE applies a fixed, non-trainable layer after the feature extractor; the original model weights are never modified. Anyone with access to the original feature extractor (e.g., by stripping the MoRE layer) recovers the full, un-unlearned representation. The paper frames this as "feature-level unlearning" but never discusses the threat model: in what deployment scenarios is the MoRE layer inseparable from the model? This is a framing gap that should be acknowledged, though for black-box API deployments the approach remains practical.

- **Complement-space preservation may leave forget information accessible to non-linear probes.** Equation 4–5 explicitly preserves all feature information outside the prototype span via the \((\mathbf{I} - \mathbf{PD})\mathbf{z}\) term. The paper assumes this complement space contains no forget-class discriminative information but provides no evidence. A non-linear probe (e.g., a 2-layer MLP) trained on the unlearned features could potentially exploit residual forget information in the complement space. Evaluating this would strengthen the claim of feature-level completeness.

- **Modest quantitative advantage on diffusion model unlearning.** The LPIPS_d advantage (0.25–0.26) over RECE (0.23–0.25) and UCE (0.20–0.22) is real but small. The qualitative results are compelling but the quantitative edge is narrow; the paper's claim that MoRE "outperforms SOTA diffusion model unlearning methods" is somewhat strong given the margin.

### Trivial

- **"Mixture of Experts" naming.** The "experts" are fixed, non-learnable remapping matrices and the stochastic router is a random choice. While the paper acknowledges this (line 223–234), "Mixture of Remapping Experts" could give a misleading impression of learned, conditional computation. A more precise name would avoid confusion with standard MoE architectures.

- **Numerical stability of pseudoinverse not discussed.** The prototype matrix \(\mathbf{P}\) could be nearly rank-deficient when class prototypes are highly correlated (cosine similarities reach 0.77, as shown in Figure 3). While the paper wisely uses SVD-based pseudoinverse rather than normal equations to avoid squaring the condition number, no discussion of singular value thresholding or observed condition numbers is provided.

## Nice-to-Haves

- A fine-tuning attack experiment: unfreeze the full model (feature extractor + MoRE layer + classifier) and train on the forget set for a few epochs. This would directly address the "impeding recovery via fine-tuning" claim and, if successful, substantially elevate the contribution.

- A non-linear probe (2-layer MLP) on the unlearned features to test whether forget information leaks through the complement space. This would strengthen the "exact feature-level unlearning" claim.

- Explicit discussion of the threat model: when can an adversary strip the MoRE layer vs. when must they work with black-box access?

## Removed Points

*These points are flagged to be removed, treat them with caution:*

- **Harsh Critic, Issue 4 (Unconvincing retrain baseline):** The claim that retrain numbers are "anomalous" and inflate MoRE's advantage is not supported by the table data. On CIFAR-10 standard setting, Retrain HM = 99.57 exceeds MoRE's HM = 91.02; MoRE's advantage comes from irreversibility (KR), not from an underperforming retrain baseline. Additionally, the paper itself questions the gold-standard status of retraining (citing Thudi et al. 2022b, Goel et al. 2022). **Removed as factually incorrect.**

- **Harsh Critic, "Diffusion-model adaptation details too brief":** The criticism that the main paper lacks explanation of how MoRE is adapted to cross-attention layers likely targets content in the stripped appendix. Under the rules, missing appendix content cannot be flagged. **Removed.**

- **Harsh Critic, section-by-section notes about LR notation and optimizer details for KR:** These are reproducibility nitpicks about undisclosed hyperparameters. Under the rules, these are removed. **Removed.**

- **Strength Finder, "even after adversarial fine-tuning intended to recover forgotten knowledge":** The KR evaluation uses linear probing, not adversarial fine-tuning. This strength description is factually incorrect. **Removed from strengths, converted to the qualified version above.**

- **Strength Finder, generic framing strengths** (e.g., "the problem is important," "the question is interesting"): Removed as superficial and lacking concrete grounding.

## Novel Insights

The PO projection idea — using the pseudoinverse of the prototype matrix to create an orthogonal coordinate system where each prototype corresponds to an independent axis — is a clean and well-motivated solution to the prototype-correlation problem. The observation that ESC's erasure damages remain prototypes because forget and remain prototypes are highly correlated (Figure 3, cosine similarities up to 0.77) is empirically convincing and the PO solution is mathematically elegant. This general technique of decorrelating class prototypes before editing could be useful beyond unlearning, in any setting where one needs to surgically modify class-specific feature components.

## Suggestions

- Add a fine-tuning attack experiment (unfreeze full model, train on forget set) to substantiate the irreversibility claim, or recalibrate claims to "resistance to linear probing" if the method does not withstand fine-tuning.
- Add a non-linear probe experiment to rule out complement-space leakage.
- Discuss the threat model explicitly: under what access model is the MoRE wrapper sufficient, and when could it be stripped?
- Consider renaming to avoid implying learned MoE computation when the experts are fixed and the router is stochastic.

---

## Score and Decision

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison to MoRE |
|--------|------|-----------|-------|---------------------|
| Pseudo-Probability Unlearning | Xagys9QD3T | 3.00 | 1 | Clearly weaker — simpler method, less evaluation |
| MASIMU | BJfIDS5LsS | 2.50 | 1 | Clearly weaker |
| UGradSL | hwXUmwJAq5 | 3.00 | 1 | Clearly weaker |
| Auditing Data Controller | 85X9awoVtv | 2.50 | 1 | Different problem area |
| SUN | p7mgNvOD9Q | 4.00 | 1 | Weaker — simpler, no KR, no diffusion, less comprehensive |
| Deep Unlearning | pUOesbrlw4 | 5.25 | 1,2 | MoRE stronger — adds remapping, MoE, KR evaluation, diffusion exps |
| Forget Vectors | 7tpMhoPXrL | 4.80 | 1 | MoRE stronger — more comprehensive evaluation |
| Oblivious Unlearning | wAemQcyWqq | 5.67 | 1,2 | Different focus, MoRE more comprehensive |
| Decoupling Class Label | OHOmpkGiYK | 5.75 | 2 | MoRE stronger methodologically and empirically |
| Jogging the Memory | fMNRYBvcQN | 6.75 | 2 | Jogging more thorough on irreversibility investigation; MoRE has better method contributions |
| Sparse Representations | TLBPjECC5D | 5.25 | 2 | MoRE stronger |
| Project and Probe | f6CBQYxXvr | 7.00 | 2 | Different area, not directly comparable |

**Round-1 bracket:** 5.5 – 7.5.  
**Round-2 narrowing:** Between Deep Unlearning (5.25) and Jogging the Memory (6.75). MoRE brings stronger methodological contributions than Deep Unlearning but its central irreversibility claim is less thoroughly evaluated than Jogging's relearning analysis. The paper sits at **6.0** — a solid contribution with a significant evidential gap (no fine-tuning attack) that prevents the irreversibility claim from being fully substantiated.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>