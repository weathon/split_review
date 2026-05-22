Now I have sufficient calibration material. Let me produce the final consolidated review.

## Summary

This paper proposes MoRE (Mixture of Remapping Experts), a training-free framework for feature-level machine unlearning. It introduces three innovations: (i) prototype-orthogonal (PO) projection that decorrelates forget and remain prototypes via the pseudoinverse before erasure, (ii) remapping forget prototypes to multiple remain prototypes via a mixture-of-experts architecture to break feature separability, and (iii) activation-mean prototypes enabling O(Nd) time and O(dk) memory complexity. Experiments across CIFAR-10/100, Tiny-ImageNet, ImageNet (classification) and Stable Diffusion v1.4 (concept erasure) show MoRE achieves strong forget-set accuracy reduction while preserving remain-set utility, often surpassing training-based baselines at a fraction of the compute cost.

## Strengths

1. **Novel prototype-orthogonal projection for utility preservation**. The paper identifies that forget and remain prototypes are highly correlated (cosine similarities ~0.5–0.77; Fig. 3) and that naive subspace erasure (ESC) degrades remain prototypes from 1.0 to 0.52 autocorrelation. Using the pseudoinverse (Eq. 2) to project features into a space where prototypes form an orthogonal basis is a principled solution. Table 3 shows that without PO, remap drives forget accuracy to zero but hurts remain utility; with PO, remain accuracy stays at 99.94% (CIFAR-10). The complement-space skip connection (Eq. 4) ensures the transformation remains full-rank.

2. **Remapping with multiple experts demonstrably disrupts feature-level recoverability**. Under the KR evaluation (linear probe on frozen features, Table 1), MoRE achieves HM_f of 0.07 (CIFAR-100) and 0.50 (Tiny-ImageNet), whereas the next-best baseline ESC-T gives 96.07 and 95.47—an orders-of-magnitude reduction. This empirically shows that forget features are not merely erased but scattered to the point where even a tuned linear probe cannot separate them, a significant advance over prior work.

3. **Exceptional computational efficiency**. Fig. 5 shows MoRE completes unlearning in ~10 seconds and <200 MB GPU memory on CIFAR-10/100, while training-based methods take orders of magnitude longer. The memory complexity is constant with respect to dataset size (unlike ESC's O(N_f d) SVD). This practical scalability is a genuine contribution for real-world deployment.

4. **Thorough ablation validates all components**. Table 3 systematically ablates PO, erasing, remapping, and MoRE across both standard and KR settings. Sensitivity analysis on target remapping class (Table 5), number of experts (Fig. 7), and router variants (Table 6) shows stable performance and robustness, lending credibility to the design.

## Weaknesses

### Fatal

None. The core claims are supported by evidence, even if some claims are somewhat over-scoped.

### Major

1. **The claim of "irreversibility" is not tested against the threat model the paper itself invokes — full fine-tuning.** The abstract states MoRE "impedes recovery via fine-tuning" and the introduction frames reversibility as a core motivation. However, the only evidence for irreversibility is the KR metric, which trains a *linear probe on frozen features* (Table 1, "KR setting: lr=0.1"). A linear probe is a weaker adversary than full-model fine-tuning on forget data. The paper conducts no experiment where the unlearned model is fine-tuned (fully or partially) on the forget set and then tested for recovery of forget accuracy. Without this experiment, the central claim is overstated relative to the evidence. This is a gap that should be addressed by either (a) running the standard full fine-tuning recovery attack, or (b) tempering the language from "irreversible" to "strongly impedes linear probing based recovery."

2. **The KR metric produces anomalous results that the paper does not explain.** In the KR setting (Table 1), MoRE achieves remain test accuracy (D_rt) of 99.94% on CIFAR-10, far exceeding the original model's D_rt of 91.07%. Similarly on Tiny-ImageNet KR, MoRE gets D_rt=98.03 vs. the original's 90.10. This is counterintuitive — MoRE is applied on top of the original model's features, so its D_rt should not exceed the original's. The paper does not explain why a linear probe trained on MoRE's post-unlearning features would dramatically outperform the original classifier. This suggests either the KR evaluation protocol differs from standard accuracy in ways not described in the main text (the details are in the stripped appendix), or the metric is measuring something other than what it claims. Either way, the anomaly needs explicit clarification.

### Minor

1. **Diffusion model results are competitive but claims of superiority are overstated.** Table 2 shows MoRE achieves the best LPIPS_d tradeoff (0.25 for Van Gogh, 0.26 for Kelly McKernan), but on the primary forgetting metric LPIPS_f (0.33 for both), it is outperformed by UCE (0.25) and ESD (0.40 for Van Gogh). The paper states "outperforms SOTA diffusion model unlearning methods both quantitatively and qualitatively" — this is too strong given that on the direct forgetting measure (LPIPS_f), several baselines beat MoRE. The qualitative results (Fig. 4) are referenced but not assessable without seeing the images. The claim should be scoped to "achieves the best overall tradeoff."

2. **The choice of stochastic router over conditional router is under-motivated.** The paper states stochastic routing is the default because it "requires no training" (Section 3.3), yet Table 6 shows the trained variant MoRE-P-T-B achieves higher HM on CIFAR-10 (91.79 vs. 85.24) and comparable on CIFAR-100 (82.48 vs. 82.37). The conditional router improves performance without adding much cost (training a small router is cheap relative to the model). The paper should either adopt the conditional router by default or provide a clearer justification for preferring the stochastic variant beyond "no training required."

3. **The t-SNE visualization (Fig. 1) is used as qualitative evidence for the irreversibility claim, but t-SNE can create artificial clusters even from random data.** The paper's quantitative results (KR metric, HM_f) are the real evidence, so this is minor, but the claim that Fig. 1 demonstrates irreversibility should be supported with quantitative cluster metrics (e.g., silhouette score of forget vs. remain features after remapping).

### Trivial

- Table 5 and Table 6 have slightly confusing layouts due to column naming (D_f, D_r, D_f again), making them hard to parse. A cleaner column labeling and consistent subscript convention would help.
- The X-axis labels in Fig. 7 appear garbled (values like 0.2–0.8 instead of integers), likely a parsing artifact, but the authors should ensure the final PDF renders correctly.

## Nice-to-Haves

- A full fine-tuning recovery experiment (fine-tune the unlearned model on forget data for a few epochs, then measure forget accuracy) would directly validate the irreversibility claim.
- Quantitative cluster metrics (silhouette score, intra/inter-class distances) to replace or supplement the t-SNE visualization in Fig. 1.
- An explanation for why MoRE's KR remain accuracy exceeds the original model's, with controlled experiments to rule out metric artifacts.
- Ablation of the complement-space projection term (\( \mathbf{I} - \mathbf{PD} \)) to show how much information is retained versus discarded.

## Removed Points

These points are flagged to be removed — treat them with caution. They were omitted because they are speculative, nitpicky, or based on parser artifacts:

- **"The method is a simple linear transformation that conceals rather than removes information"** — This is speculative scope creep. The paper's claim is about impeding recovery via *fine-tuning/probing*, not cryptographic obfuscation. Any unlearning method could theoretically be inverted by an adversary with full knowledge and access; this is not specific to MoRE and its absence is not a weakness of the paper.
- **"Missing standard deviations in Table 1"** — The parsed table is from a PDF extract; the original paper likely has them. The reviewer's reading of blank ± entries is a parser artifact.
- **"Retrain D_r=99.98 for Tiny-ImageNet is suspicious"** — This is training accuracy, not test accuracy. The original model achieves 96.45% training accuracy on Tiny-ImageNet; a retrain on remain-only data could plausibly be higher. This is not a meaningful concern.
- **"Figure 7 X-axis shows 0.2–0.8 instead of integers"** — Explicitly identified by the reviewer as a parsing error, not the paper's flaw.
- **"Exact is not formally defined"** — The paper uses "exact" to mean that forget features are *exactly* removed from the feature representation (demonstrated through D_f=0.00), which is clear enough.
- **"MIA for random data forgetting is worse than retrain"** — MoRE's MIA (79.31) is higher than retrain (74.64), meaning it is less private on this metric. However, many other baselines (Prototype: 87.73, SCRUB: 86.41) are also higher than retrain, and MoRE outperforms ESC (73.43) and ESC-T (76.74). This is not a distinctive weakness.
- **"Conclusion is hyperbolic"** — Minor stylistic critique. The conclusion's aspirational language is typical for conference papers.
- **"Full mutual orthogonality discards remain-remain correlations"** — The paper acknowledges this in footnote 1 and justifies it by noting selective enforcement is mathematically complex. This is a reasonable design tradeoff, not a flaw.
- **"Applied out of the box to diffusion models undermines the claim"** — The paper presents this as a positive (demonstrating generality), not a weakness. The results are honestly reported and the paper explicitly notes this limitation.

## Novel Insights

None beyond the paper's own contributions. The harsh reviewer's framing that "irreversibility is untested" and the strength finder's emphasis on the HM_f gap (0.07 vs. 96.07) together highlight that the paper's core claim is simultaneously its strongest and most contested point: the *distance* between MoRE and baselines on the KR metric is enormous and genuinely impressive, but the claim of "irreversibility" requires moving from *linear probing on frozen features* to *full fine-tuning on forget data* to be fully convincing. This tension — impressive proxy evidence vs. insufficiently tested strong claim — is the key issue the authors should address.

## Suggestions

1. **Add a full fine-tuning recovery experiment.** Take the unlearned model, fine-tune it (all layers or the classifier head + last few feature layers) on the forget data for several epochs, then measure forget accuracy. If MoRE resists this, the irreversibility claim is genuinely validated. If recoverable, temper the language to "strongly impedes linear-probe based recovery."
2. **Explain the anomalously high KR D_rt values.** Run a controlled experiment: compute D_rt for the original model using the same linear-probe-on-frozen-features protocol used in the KR setting. If the gap persists, explain why MoRE's post-unlearning features are more linearly separable for remain classes. If the gap disappears under the standard protocol, adjust the numbers.
3. **Re-scope the diffusion model claims.** Replace "outperforms SOTA" with "achieves the best LPIPS_d tradeoff among training-free methods" to accurately reflect Table 2.
4. **Consider adopting the conditional router as default** (or reporting both), since MoRE-P-T-B outperforms the stochastic router on CIFAR-10.
5. **Add silhouette scores** for forget vs. remain features after each unlearning method to quantitatively substantiate the t-SNE visualizations.

## Score and Decision

**Calibration anchors** (all from deepreview_13k_calibration):

| Path | Avg Score | Comparison to MoRE |
|------|-----------|-------------------|
| `PUOesbrlw4.md` (Deep Unlearning) | 5.25 | Similar training-free SVD-based class unlearning, but MoRE is more sophisticated (PO + remapping + MoE) and has stronger empirical results across more settings |
| `p7mgNvOD9Q.md` (SUN) | 4.00 | Another training-free subspace method with simpler approach and weaker results; MoRE is clearly stronger |
| `OHOmpkGiYK.md` (Decoupling) | 5.75 | Scope expansion with GA-based method; MoRE has a cleaner, more efficient method and comparable experimental depth |
| `uDjuCpQH5N.md` (Do Unlearning Methods Remove) | 5.50 | Evaluation-focused, no new method; MoRE has a stronger method contribution |
| `Q1MHvGmhyT.md` (A Closer Look at MU for LLMs) | 6.00 | Analysis + method paper; MoRE has a more novel method but the LLM paper has stronger analytical depth |
| `51WraMid8K.md` (Probabilistic Perspective) | 8.00 | Fundamental evaluation framework with theoretical guarantees; MoRE is a method paper with less foundational impact |
| `BJfIDS5LsS.md` (MASIMU) | 2.50 | Poorly executed; MoRE is far stronger in every dimension |
| `CIN2VRxPKU.md` (Evaluating Deep Unlearning) | 5.33 | Evaluation-focused; MoRE has a method contribution and cleaner empirical story |

MoRE sits above the 4.0–5.5 papers (SUN, CodeUnlearn, MASIMU, Deep Unlearning) and is competitive with the 5.75–6.0 papers (Decoupling, A Closer Look). Its method contribution is stronger than most, but the overclaiming on "irreversibility" without full fine-tuning evidence and unexplained KR anomalies hold it back from the higher band. A score of **6.0** places it at the accept/reject boundary, where the paper could be accepted with revisions addressing the major weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>