Now I have a clear picture. Let me compile the final review.

---

## Summary

This paper investigates whether compositional generalization—the ability to handle unseen combinations of visual concepts—requires a generative (decoder-based) approach or can be achieved with non-generative (encoder-only) methods. Building on recent identifiability results (Brady et al., 2025), the authors prove that constraining an encoder to the inverse generator class $\mathcal{G}_{\text{int}}$ is infeasible in practice because the necessary constraints depend on the unknown geometry of the OOD data manifold (Theorem 3.2). In contrast, constraining a decoder to $\mathcal{F}_{\text{int}}$ is straightforward via architecture or regularization. The paper then demonstrates on the photorealistic PUG datasets that generative inversion (gradient-based search and replay) substantially improves OOD accuracy over non-generative methods, especially when large-scale pretraining is unavailable.

## Strengths

- **Theoretical asymmetry result (Theorem 3.2).** The paper proves that for $d_x \geq d_z^3$, the Jacobian and Hessian of an inverse generator $g \in \mathcal{G}_{\text{int}}$ can be made arbitrary at any point—meaning no local derivative constraint can distinguish an encoder that identifies the true inverse only in-domain from one that fails OOD. Combined with Lemma 3.1 and the manifold-dependent constraint in Eq. (3.4), this provides a rigorous, principled argument for why encoder constraints are infeasible while decoder constraints are straightforward. This is the paper's central theoretical contribution and is convincingly presented.

- **Clean empirical demonstration.** On PUG-Background and PUG-Texture (Fig. 6), applying generative replay and gradient-based search to the same autoencoder consistently improves OOD slot-classification accuracy across all base encoders, from ViT-S trained from scratch (~40% → ~75% on PUG-Background) to large pretrained models. The experimental design is well-controlled: the same autoencoder is used for both non-generative and generative evaluation, isolating the effect of generative inversion without confounders.

- **Well-structured formalization.** Section 2 clearly lays out the problem: perception as inverse problem (Eq. 2.1), the distinction between generative and non-generative approaches (Eqs. 2.2–2.3), and the OOD identifiability conditions (Eqs. 2.5–2.6). This mathematical setup underpins the theory and makes the paper self-contained.

- **Thoughtful dataset design.** The three PUG splits (Background, Texture, Object) systematically vary concept-interaction degree, from $n=0$ (non-interacting objects) to higher-order interactions. Figure 5 shows that near-perfect OOD accuracy occurs only in the no-interaction setting, corroborating the theoretical prediction that encoder constraints are data-dependent and hard to enforce when interactions are present.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Gap between theory and decoder implementation.** The theory states that constraining a decoder to $\mathcal{F}_{\text{int}}$ is "straightforward" via architecture or regularization (Sec. 3). The experiments use a regularized cross-attention Transformer (from Brady et al., 2025) as an *approximation* to $\mathcal{F}_{\text{int}}$. The paper does not measure how closely this approximation satisfies the theoretical constraints (e.g., the block-diagonal Hessian condition in Eq. 3.1) on the learned models. A brief analysis—or at minimum an ablation showing that removing the regularization eliminates the OOD gains—would tighten the link between theory and practice. The paper does report results with unstructured decoders in §C (appendix, stripped), but this connection deserves more attention in the main text.

- **Limited scope of empirical validation.** The experiments are confined to the PUG datasets, which, while photorealistic, involve controlled compositions of a small set of concepts (animals, backgrounds, textures). The authors acknowledge this limitation (Sec. 7), and the paper is framed as a principled investigation rather than a large-scale benchmark. However, the claim that generative methods are "required for data-efficient perception" would be strengthened by evidence on more diverse data, even at smaller scale.

### Trivial

- **Computational cost of search not discussed in main text.** The gradient-based search procedure (Sec. 4.1) is a distinctive feature of the generative approach. The main text defers all implementation details (number of gradient steps, learning rates, stopping criteria) to the appendix. Stating the typical computational overhead per sample during inference—even a ballpark figure—would help readers assess practicality.

- **Fig. 6 labeling for PUG-Texture.** The paper correctly states that "replay cannot be applied" on PUG-Texture, but the figure still shows "with replay" bars. A note in the caption clarifying that "with replay" on PUG-Texture corresponds to the ID-only encoder would prevent momentary confusion.

## Nice-to-Haves

- A more intuitive preamble to Lemma 3.1 and Theorem 3.2, explaining *why* the high ambient dimension "destroys" the favorable structure of $\mathcal{G}_{\text{int}}$ before the formal statements, would make the theoretical contribution more accessible to a broader audience.

- A sketch of how the results extend from $n=1$ to $n>1$ (even if deferred to the appendix) would strengthen the generality claim.

## Removed Points

These points were flagged by the input reviews but are removed for the reasons given:

1. **"Implementation details (gradient steps, stopping criterion, learning rate) are deferred to the appendix."** — Moved to Trivial. The paper states these are in App. B; deferring details to the appendix is standard practice. A brief mention of computational cost is a reasonable suggestion but not a weakness.

2. **"The paper would benefit from more explicit discussion of how closely the regularized cross-attention decoder approximates $\mathcal{F}_{\text{int}}$."** — Moved to Minor, merged with the theory-practice gap point.

3. **"The exposition around Lemma 3.1 and Theorem 3.2 could benefit from a more intuitive explanation."** — Moved to Nice-to-Haves. This is a presentation preference, not a weakness.

4. **"Extension to higher n — providing at least a sketch would strengthen the generality of the claim."** — Moved to Nice-to-Haves. The paper explicitly states the results are presented for $n=1$ with extensions possible; this is a reasonable scope choice.

## Novel Insights

The paper's key insight—that the asymmetry between constraining a decoder to $\mathcal{F}_{\text{int}}$ and an encoder to $\mathcal{G}_{\text{int}}$ gives generative methods a principled advantage—is genuinely novel. Prior work in this line (Brady et al., 2025; Lachapelle et al., 2023) established that $\mathcal{F}_{\text{int}}$ enables OOD identifiability, but did not analyze the inverse class $\mathcal{G}_{\text{int}}$ or the practical feasibility of constraining encoders. The observation that the encoder constraints become manifold-dependent (Eq. 3.4) while decoder constraints remain axis-aligned (Eq. 3.1) provides a clean geometric intuition for why generation helps. The further point that the constraints for the encoder depend on $\mathcal{X}_{\text{OOD}}$, which is unobserved, makes the infeasibility claim concrete rather than merely a statement about difficulty.

## Suggestions

- Add a measurement (even approximate) of how well the regularized cross-attention decoder satisfies the $\mathcal{F}_{\text{int}}$ constraints on the trained models, e.g., the norm of off-block-diagonal Hessian entries. This would directly connect the theory to the empirical method.
- State the approximate inference cost for gradient-based search (e.g., number of iterations, wall-clock time per image vs. a forward pass) in the main text.
- Clarify in the Fig. 6 caption or main text that the "with replay" bars on PUG-Texture correspond to the baseline encoder-only setting, since replay is not applicable there.

## Score and Decision

**Calibration details:**

Round 1 anchors (bracketing pass):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hv8l922Ad7.md` — avg 3.40 (weak): compositional generalization + disentanglement metrics, rejected. This paper is substantially stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7VPTUWkiDQ.md` — avg 7.33 (middle-high): "Provable Compositional Generalization for Object-Centric Learning." Direct predecessor work; this paper extends it with the asymmetry analysis and more realistic experiments.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/s1zO0YBEF8.md` — avg 6.50 (middle): "Dynamics of Concept Learning and Compositional Generalization." Related topic, accepted; this paper is stronger theoretically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hrqNOxpItr.md` — avg 8.00 (high): "Cross-Entropy Is All You Need To Invert the Data Generating Process." Different focus, broader scope; this paper's contribution is narrower.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RuP17cJtZo.md` — avg 8.00 (high): "Generator Matching." Different domain.

Round 1 bracket: **[6.5, 8.0]**

Round 2 anchors (narrowing pass):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/cCl10IU836.md` — avg 7.00: "Interaction Asymmetry: A General Principle for Learning Composable Abstractions." Very closely related (appears to be the Brady et al. 2025 paper). This paper extends it with the novel asymmetry analysis and photorealistic experiments. The current paper is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7VPTUWkiDQ.md` — avg 7.33 (re-read): Closely related predecessor. Current paper extends with novel theory and better experiments.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Cy5v64DqEF.md` — avg 7.50: "Idempotence and Perceptual Image Compression." Different domain; comparable quality.

The paper sits clearly above the 7.00 and 7.33 anchors (both are predecessors that this work meaningfully extends with novel theory and photorealistic experiments). It is comparable in quality to the 7.50 anchor. It does not quite reach the 8.00 anchors, which either have broader applicability (hrqNOxpItr) or open entirely new modeling paradigms (RuP17cJtZo). The minor gaps (theory-practice link for the decoder approximation, dataset scope) prevent it from reaching the top tier.

**Final score: 7.5.** The paper makes a principled, well-supported contribution to an important debate. The theory is sound and novel, the experiments are clean, and the limitations are honestly acknowledged.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>