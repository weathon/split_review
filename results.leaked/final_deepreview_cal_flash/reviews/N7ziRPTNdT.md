Now let me compile the final review.

## Summary

This paper investigates whether generative (decoder-based) or non-generative (encoder-only) approaches are better suited for compositional generalization — a key component of data-efficient visual perception. The authors formalize the required inductive biases for both approaches via function classes $\mathcal{F}_{\text{int}}$ (generators) and $\mathcal{G}_{\text{int}}$ (inverses), prove that constraining an encoder to $\mathcal{G}_{\text{int}}$ is infeasible when $d_x \gg d_z$ because the constraints depend on unknown out-of-domain geometry (Theorem 3.2), while constraining a decoder to $\mathcal{F}_{\text{int}}$ is straightforward and coordinate-aligned. Empirically, they show on photorealistic PUG datasets that non-generative methods fail at compositional generalization unless backed by massive pretraining, while generative methods (structured autoencoder + search + replay) consistently improve OOD performance without additional data.

## Strengths

1. **Theorem 3.2 — a sharp theoretical asymmetry result.** The proof that inverse generators $g \in \mathcal{G}_{\text{int}}$ can have arbitrary derivatives when $d_x \geq d_z^3$ (the realistic image regime) formally demonstrates why constraining encoders to guarantee compositional generalization is fundamentally harder than constraining decoders. The contrast with $\mathcal{F}_{\text{int}}$, where constraints are global and coordinate-aligned (Eq. 3.1), rigorously proves an asymmetry that has been speculated about but not previously formalized. This is the paper's strongest contribution.

2. **Principled formalization linking identifiability to compositional generalization.** Section 2 builds on prior work to define exactly when OOD identifiability holds for both approaches (Eq. 2.5–2.7). This framing cleanly reduces the practical question to whether a model class can be feasibly constrained to $\mathcal{F}_{\text{int}}$ or $\mathcal{G}_{\text{int}}$, providing a unified theoretical language that supports both the theoretical analysis and the experimental design.

3. **Consistent empirical gains from generative replay and search.** Figure 6 shows that across six very different base encoders — from scratch-trained ViT-S to massive models like SigLIP2 — generative methods using replay and/or search improve OOD accuracy on every model on both PUG-Background and PUG-Texture. The gains are often large (e.g., from ~30% to ~80% for the from-scratch model on PUG-Background), demonstrating practical value that goes beyond the theoretical impossibility result.

4. **Empirical confirmation of the $n=0$ special case.** Figure 5C shows that all non-generative methods achieve near-perfect OOD accuracy on PUG-Object, where concepts do not interact. This matches the theoretical prediction that $\mathcal{G}_{\text{int}}$ is more structured when $n=0$, and serves as a positive control validating the experimental framework.

## Weaknesses

### Fatal

None.

### Major

1. **Title and framing overstate what the evidence supports.** The title asserts "Generation is Required for Data-Efficient Perception." The paper's own experiments show that non-generative methods *can* achieve OOD generalization: SigLIP2 reaches ~80% on PUG-Background, and *all* non-generative models achieve near-perfect performance on PUG-Object. The paper's nuanced claim is that *guaranteeing* compositional generalization via encoder constraints is infeasible (Theorem 3.2), not that non-generative methods can never succeed. The paper acknowledges this internally (e.g., "OOD accuracy improves with encoders leveraging larger-scale pretraining"), but the title and abstract's absolutist framing invites a reader to reject the paper for overclaiming. This is a structural misalignment between the narrative and the evidence. The paper would be stronger with a title like "Generation Provides a Principled Pathway to Data-Efficient Compositional Generalization" or similar, and corresponding adjustments throughout.

### Minor

2. **Experiments test unconstrained encoders, not the theory's central mechanism.** Theorem 3.2 predicts that *attempting to constrain* an encoder to $\mathcal{G}_{\text{int}}$ is infeasible because the constraints are manifold-dependent. The experiments test *unconstrained* encoders — a setting consistent with the theory but not a direct test of its mechanistic claim. A more targeted experiment would attempt to regularize an encoder toward the manifold-dependent structure of $\mathcal{G}_{\text{int}}$ (Eq. 3.4) on ID data and show that this regularization fails to transfer OOD. The current experiments demonstrate practical consequences of the theory, which is valuable, but they leave a gap between the theory's specific prediction and the evidence.

3. **PUG-Texture results partly conflate generation with generic optimization.** On PUG-Texture, replay cannot be applied, so the gains come entirely from gradient-based search — a generic optimization procedure that is not uniquely generative. The paper's main narrative attributes these gains to "generation" without adequately separating the decoder's structural bias from the added compute of search iterations. The unstructured decoder ablation in §C addresses this in principle, but it should appear in the main text, especially since the PUG-Texture results are a key part of the empirical case.

4. **Computational cost of search is not discussed.** The paper advocates search as a key mechanism but provides no analysis of how many gradient steps are required, the latency-accuracy tradeoff, or how this compares to an encoder forward pass. This is relevant to any practical recommendation, particularly given the "data-efficient" framing.

5. **No direct data scaling analysis.** The paper claims generative methods are more data-efficient, which follows from their OOD performance on a fixed 20k-image dataset. However, no data scaling curves (OOD accuracy vs. number of ID training images) are provided. A plot showing that generative methods achieve higher OOD accuracy with less data would cleanly substantiate the data-efficiency narrative.

### Trivial

6. **Error bars / variance not reported in main figures.** Figures 5 and 6 appear to show point estimates without confidence intervals or standard deviations. Reporting variance would help assess reliability, especially for smaller models.

7. **No failure case analysis.** The paper does not examine whether certain OOD combinations (e.g., a dark animal on a dark background) systematically cause failures, which could reveal boundaries of the $\mathcal{F}_{\text{int}}$ assumption on the PUG data.

## Nice-to-Haves

- A direct experimental test of the theory's mechanism: attempt to regularize an encoder toward the manifold-dependent structure of $\mathcal{G}_{\text{int}}$ (Eq. 3.4) on ID data and show this regularization fails to transfer OOD. This would close the gap between the theory's prediction and the empirical evidence.
- Data scaling curves (OOD accuracy vs. number of ID training images) to directly measure the data efficiency claim.
- Unstructured decoder ablation results brought into the main text, especially for PUG-Texture, to cleanly separate the decoder's structural bias from search as a generic optimizer.

## Removed Points

*These points were raised in the reviews but are not valid weaknesses in context of the paper as written.*

- **"Experiments are not a controlled test of the theory"** — The paper states upfront that its experimental goal is to "assess the extent to which non-generative methods can achieve compositional generalization in practice," not to directly verify Theorem 3.2's mechanism. The theory-experiment pairing is complementary, and the suggested targeted experiment is a nice-to-have, not a missing requirement.
- **"Search is a generic optimizer, not generative"** — Search operates by inverting the decoder, which is the generative model. Without the decoder, there is no meaningful search landscape. The unstructured decoder ablation (§C) already tests the importance of the decoder's structure.
- **"Contribution of decoder bias vs. search is not disentangled"** — The unstructured decoder ablation (§C) explicitly addresses this, and the paper references it. Moving it to the main text is a presentation suggestion, not a weakness.
- **Criticisms about missing appendix content or references** — The submission's appendix and references were stripped by the PDF parser; they exist in the original submission.

## Novel Insights

The reviews surface a subtlety that the paper only partially addresses: Theorem 3.2 is about the *infeasibility of constraining encoders* to $\mathcal{G}_{\text{int}}$, but the experiments test *unconstrained* encoders that do or do not succeed through optimization dynamics. This leaves two distinct claims on the table — (a) a guarantee-level claim (constraints are infeasible to enforce) and (b) an empirical observation (unconstrained methods often fail but sometimes succeed with scale). These are logically related but not identical. The paper would be strengthened by cleanly separating them: the theory shows why you cannot *guarantee* success by designing encoder inductive biases; the experiments show what happens when you rely on optimization to find a good inverse. The SigLIP2 result on PUG-Background is actually consistent with the theory — it doesn't contradict the impossibility of *guaranteeing* generalization via constraints — but the paper's framing treats it as a caveat rather than as a distinct regime that the theory actually predicts (scale can implicitly regularize toward the right inverse through optimization). A more precise framing would strengthen both the theory and the empirical story.

## Suggestions

1. **Revise the title and framing.** Change the title to something like "Generation Provides a Principled Pathway to Data-Efficient Compositional Generalization" and adjust the abstract and conclusion to match what the evidence actually shows. This is the single highest-leverage change and would substantially improve the paper's reception.

2. **Add a targeted experiment that directly tests the theory's mechanism.** Attempt to regularize an encoder toward the manifold-dependent structure of $\mathcal{G}_{\text{int}}$ (Eq. 3.4) on ID data and measure whether this transfers to OOD. If the regularization fails to transfer, it directly validates Theorem 3.2's central claim.

3. **Bring the unstructured decoder ablation into the main text.** Show that search on a structured decoder outperforms search on an unstructured decoder for PUG-Texture, cleanly separating the contribution of the decoder's inductive bias from generic optimization.

4. **Add data scaling analysis and computational cost discussion.** Report OOD accuracy vs. number of ID training images for generative and non-generative methods. Also report the number of gradient steps required for search and the resulting latency.

---

**Calibration report for score 6.5:**

All anchors retrieved across rounds:

| Anchor path | Avg score | Round | Comparison to this paper |
|---|---|---|---|
| Eg32tDGgF5 (Do Generative Models Learn Rare Factors) | 3.00 | 1 (weak) | Much weaker — limited empirical study, no theoretical contribution comparable to Theorem 3.2 |
| ZbOSRZ0JXH (Beyond Finite Data) | 3.00 | 1 (weak) | Much weaker — no theoretical grounding, different framing |
| hv8l922Ad7 (Correcting Flaws in Disentanglement Metrics) | 3.40 | 1 (weak) | Much weaker — narrower scope, no theory of compositional generalization |
| EHmjRIA4l2 (Compositional World Models) | 3.00 | 1 (weak) | Much weaker — no formal theory |
| 7VPTUWkiDQ (Provable Compositional Generalization for OCL) | 7.33 | 2 (mid) | Better — cleaner framing, same level of theory, but on synthetic data; this paper has more realistic experiments but worse framing |
| Hxm0hOxph2 (On Provable Length and Compositional Generalization) | 5.25 | 2 (mid) | Worse — narrower scope (seq-to-seq), weaker empirical validation |
| s1zO0YBEF8 (Dynamics of Concept Learning) | 6.50 | 2 (mid) | Comparable — both have theory + experiments; that paper's SIM abstraction was criticized, this paper's experiments are more realistic but have framing issues |
| H98CVcX1eh (Discovering modular solutions) | 6.50 | 2 (mid) | Comparable — similar level of theory and experiments; that paper had clarity issues, this paper has framing issues |
| 7oT1X8xjIk (Identifiability of Nonlinear Rep Learning) | 5.80 | 2 (mid) | Slightly worse — theory-focused without the same experimental validation of practical implications |
| hKMPz3wkPV (Towards a formal theory of compositionality) | 6.75 | 2 (mid) | Comparable-definitional paper with substantial technical concerns raised; this paper has cleaner contributions but framing issues |
| bSq0X3GSkW (Transfer of Object-Centric RL) | 5.00 | 2 (mid) | Worse — empirical only, no theory |
| 7QGyDi9VsO (Next state prediction) | 5.00 | 2 (mid) | Worse — narrower scope, no theoretical guarantees |
| 9Xt5TgM7Us (Seeing the part) | 4.75 | 2 (mid) | Worse — no theory of compositional generalization |
| STUGfUz8ob (When can transformers reason with abstract symbols) | 7.60 | 3 (strong) | Better — cleaner proofs, more comprehensive experiments, no framing issues |
| 25kAzqzTrz (Why FixMatch Generalizes Better) | 8.00 | 3 (strong) | Better — rigorous theoretical analysis, well-designed experiments, no overclaiming |
| P7KIGdgW8S (Hölder Stability of GNNs) | 8.00 | 3 (strong) | Better — complete theoretical treatment, no framing mismatch |
| 3i13Gev2hV (Compositional Entailment Learning) | 8.00 | 3 (strong) | Better — well-scoped claims, comprehensive experiments |

**Round 1 bracket:** 5.5 – 7.0 (between clearly weak anchors at ~3.0 and clearly strong anchors at ~8.0).

**Narrowing:** The paper is weaker than the 7.33 anchor (Provable Compositional Generalization) mainly due to the framing overclaim, even though the experiments are more realistic. It is comparable to or slightly above the 6.50 anchors (Dynamics of Concept Learning, Discovering modular solutions), which had their own significant weaknesses (SIM abstraction concerns, clarity issues). The paper's strongest anchor comparison is against its direct predecessor at 7.33 — the current paper has a novel theoretical extension to the harder inverse case and more realistic experiments, but the framing overclaim pulls it down relative to that cleanly-framed prior work.

**Final score: 6.5**

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>