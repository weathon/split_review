Now I have all the information needed. Let me compose the final review.

---

## Summary

This paper identifies a structural limitation of HiResCAM explanations: since softmax is invariant to a uniform shift of all logits, HiResCAMs (which decompose logits, not probabilities) admit an arbitrary additive matrix \(M\) across all class maps without changing predictions. The authors propose ContrastiveCAMs — pairwise class-difference maps that are provably invariant to this shift — and use them to formulate Core-Focused Cross-Entropy (CFCE), a training loss that penalizes reliance on non-core (spurious) image regions while remaining classification-calibrated. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC demonstrate that CFCE-trained models dramatically increase reliance on core regions (e.g., accuracy drops from ~90% to ~34% when core regions are ablated, vs. >67% retention for standard CE) and achieve high alignment between attention maps and ground-truth object masks.

## Strengths

- **Genuinely novel theoretical insight**: The proof that HiResCAM explanations are not uniquely determined — any uniform shift by a matrix \(M\) across all class maps leaves softmax predictions unchanged (Theorem 3.2) — is a crisp, well-articulated observation that cleanly motivates the contrastive reformulation. This is not a trivial rephrasing of softmax shift-invariance; the extension from scalar \(a\) to matrix \(M\) is specific to the spatial structure of CAMs.

- **Clean derivation from theory to method**: ContrastiveCAMs (Definitions 3.3, 3.4) are shown to be \(M\)-invariant (Theorem 3.5), and Proposition 4.2 elegantly rewrites cross-entropy in terms of ContrastiveCAMs, revealing exactly how core and non-core regions contribute to the loss. This directly motivates CFCE (Definition 4.5) as a principled modification.

- **Compelling core-ablation evidence**: The Hard-ImageNet results (Table 2) are the strongest piece of evidence. When core regions are ablated via Gray Mask, BBOX, or Tile, CFCE-trained accuracy drops to 34–45% while standard CE-trained models retain >67% — demonstrating that CFCE genuinely forces the model to rely on target-relevant regions. This result does not depend on any CAM-based metric and stands on its own.

- **Practical with approximate masks**: Oxford-IIIT Pets experiments (Section 5.2) show that CFCE with SAM-generated masks or bounding-box supervision achieves competitive IoU (83–85%), demonstrating the method does not require pixel-perfect annotations.

- **Downstream value demonstrated**: The segmentation transfer results (PASCAL VOC, Section 5.3) show that CFCE-trained backbones outperform CE-trained ones when fine-tuned or trained end-to-end for segmentation, confirming that the improved feature alignment transfers to related tasks.

## Weaknesses

### Fatal

None.

### Major

- **ContrastiveCAM IoU computation is undefined**: The paper reports ContrastiveCAM IoU values of 89–93% (Table 2) and 82–85% (PASCAL VOC), but never specifies how continuous ContrastiveCAM maps are binarized to compute intersection-over-union against binary core masks. Is a threshold applied? At what percentile or absolute value? Is it dataset-specific? Without this information, the IoU numbers — prominently featured as evidence of alignment — cannot be interpreted or reproduced. The core-ablation results (accuracy under masking) independently support the method's effectiveness, so this does not invalidate the central claim, but it is a significant reporting gap that must be addressed.

### Minor

- **HiResCAM limitation framing is somewhat overstated**: The paper states that HiResCAMs "may be misleading" and "fail to guarantee a faithful interpretation" due to the \(M\)-shift ambiguity. The mathematical observation is correct, but for any fixed trained network, the computed HiResCAM is a faithful decomposition of the logits that network actually produces. The ambiguity means that different networks with different internal logit representations can produce the same softmax output — which is the right motivation for ContrastiveCAM, but doesn't mean HiResCAM is unreliable for a given network. Reframing this as a contrastive-motivation rather than a deficiency would strengthen the paper.

- **Table 1 core/non-core contributions lack precise definition**: It is unclear whether the reported values are sums, means, or sums of absolute values of ContrastiveCAM activations within masked regions. The caption says "average contributions" but the computation is not specified.

- **Architectural modifications ("w/ Arch") described only in appendix**: The paper notes that modifications (bias-free classifier, etc.) are detailed in Appendix C. Since the appendix was not available for review, readers cannot assess whether the reported IoU degradation for "CE w/ Arch" vs. standard CE (e.g., 78.37% → 39.07% on Oxford-IIIT Pets validation) is expected or surprising, or what specific changes were made. A one-paragraph summary in the main text would help.

- **Theorem 4.6 proof unavailable for verification**: The consistency/calibration proof is deferred to Appendix A. While this is standard in conference submissions, including a proof sketch in the main text would increase confidence in the theoretical contribution.

- **KL regularization hyperparameters (\(\lambda_1, \lambda_2, \lambda_3\)) not ablated**: The regularized variant (CFCE + KL) improves IoU substantially on some datasets, but sensitivity to these hyperparameters is not discussed, making it unclear how dataset-dependent the tuning is.

### Trivial

- CFBCE (Core-Focused Binary Cross-Entropy) appears in the PASCAL VOC table without definition in the main text; its generalization from Equation 15 to the multilabel case is only described in Appendix B.

## Nice-to-Haves

- A comparison with one additional saliency-guided or attention-regularized training method beyond CORM/DFR would contextualize the benefit of the ContrastiveCAM-based formulation.
- Showing the distribution of the redundancy matrix \(M\) across images (beyond the single scalar \(\gamma\) per dataset) would give readers better intuition for when and how severely the HiResCAM ambiguity matters in practice.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Architectural modifications may drive apparent CFCE improvement"** — The harsh critic speculated that CFCE's gains might partially stem from architectural changes rather than the loss. This is contradicted by the data: CE w/ Arch (which uses the same architecture) achieves only 30.27% ContrastiveCAM IoU vs. 89.22% for CFCE. The architecture alone cannot explain the improvement. Removed as speculative and unsupported.

- **"GradCAM IoU vs. ContrastiveCAM IoU metric asymmetry"** — The paper does report ContrastiveCAM IoU for the CE w/ Arch baseline (30.27%), providing a fair within-metric comparison. The GradCAM IoU numbers serve only to compare with prior work (CORM, DFR) that reported GradCAM IoU. Removed as the paper already addresses this.

- **"No comparison with saliency-guided training methods beyond CORM/DFR"** — Moved to Nice-to-Haves; CORM and DFR are the most directly comparable methods from the core risk minimization literature.

- **Formatting/spelling/typo concerns** — All such concerns from the harsh critic are parser artifacts, not author errors. Removed per hard rules.

## Novel Insights

The key insight that elevates this paper beyond a standard method proposal is the formal connection between softmax shift-invariance and spatial explanation ambiguity. Prior work has noted that softmax only cares about logit differences, but extending this to show that a full spatial matrix \(M\) can be added to every class's HiResCAM without changing predictions is genuinely novel. More importantly, the paper demonstrates that this is not just a theoretical curiosity — the redundancy is quantitatively significant (\(\gamma\) up to 0.367, meaning the removable component's Frobenius norm is ~37% of the original explanation's norm). This bridges a gap between the formal properties of softmax-based classifiers and the practical reliability of gradient-based CAM explanations.

## Suggestions

- Define the ContrastiveCAM IoU computation explicitly: state the binarization method (threshold value or percentile), whether it uses \(\text{CAM}^{\text{Recon}}\) or aggregates pairwise maps, and include a sensitivity analysis to the binarization threshold.
- Add a brief summary of the "w/ Arch" modifications in the main text (Section 5), even if full details remain in Appendix C.
- Include a proof sketch of Theorem 4.6 in the main paper to make the theoretical contribution self-contained.
- Soften the framing of HiResCAM's limitation from "may be misleading" to "not uniquely determined at the probability level," which is both more precise and less likely to provoke pushback.

## Score and Decision

**Originality**: The HiResCAM \(M\)-shift observation and ContrastiveCAM formulation are genuinely novel. Connecting this to a training objective (CFCE) that enforces feature alignment is a creative and well-executed extension.

**Importance**: Feature alignment and shortcut learning are central concerns in robust ML. The method provides a principled way to incorporate core-region supervision into standard classification training.

**Claim support**: The core-ablation results strongly support the claim that CFCE forces reliance on target regions. The missing IoU binarization definition is an addressable gap that does not undermine the independently-compelling ablation evidence.

**Soundness**: The theoretical derivations (Theorems 3.2, 3.5, Proposition 4.2) are mathematically clean and well-motivated. The empirical design includes appropriate baselines (CE w/ Arch) and spans multiple datasets and task types.

**Clarity**: The paper is well-organized and the mathematical exposition is clear. Some implementation details are omitted or deferred to stripped appendices.

**Value to community**: The connection between post-hoc interpretability and training-time alignment is timely and the method is practical (works with coarse masks, transfers to downstream tasks).

### Calibration comparison

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| WYsLU5TEEo (Counterfactual GAN) | 2.50 | R1 | Much weaker — tangential method, limited evaluation |
| waIltEWDr8 (WASUP) | 3.00 | R1 | Weaker — less theoretical depth |
| BwQUo5RVun (Weakly supervised grounding) | 3.00 | R1 | Weaker — more limited scope |
| HXwrppoSPc (COMiX) | 3.25 | R1 | Weaker — less empirical validation |
| 6u6GjS0vKZ (Activation Hue Loss) | 4.25 | R1 | Weaker — modest improvements, less novelty |
| 3b8CgMO5ix (Model guidance→segmentation) | 5.50 | R1 | Weaker — poor presentation, limited contribution |
| bkdWThqE6q (INTR) | 6.00 | R1/R2 | Our paper is stronger — more theoretical depth, quantitative evaluation |
| 57NfyYxh5f (How to Probe) | 6.25 | R1/R2 | Our paper is stronger — more novel insight, method + theory, not just observation |
| GlAeL0I8LX (QPM) | 6.67 | R2 | Our paper is comparable — both have theoretical + empirical contributions |
| khuIvzxPRp (CLIP AFT) | 6.80 | R2 | Our paper is comparable/slightly stronger — more novel theoretical insight, stronger quantitative gains |
| GjfIZan5jN (IIS) | 7.33 | R2 | Comparable — IIS is more polished, our method is more actionable with stronger empirical gains |
| PBjCTeDL6o (UNI) | 8.00 | R1 | Stronger — more polished, comprehensive theoretical analysis |
| 25kAzqzTrz (FixMatch theory) | 8.00 | R1 | Stronger — deeper theoretical contribution |
| DJSZGGZYVi (REPA) | 9.00 | R1 | Much stronger — exceptional contribution |

Round-1 bracket: ~6.5–7.5. Round-2 narrowed to 6.67–7.33. The paper is stronger than QPM (6.67) and CLIP AFT (6.80) due to its genuinely novel theoretical insight and compelling ablation results, and comparable to IIS (7.33) though slightly less polished in reporting. **Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>