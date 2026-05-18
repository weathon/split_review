Now I have a thorough understanding of the paper. Let me synthesize my findings.

---

## Summary

This paper proposes MI-MAE, a masked autoencoder training method that adds two mutual-information-based losses to the standard MAE reconstruction loss: an InfoNCE loss to maximize mutual information between latent features from different orthogonal masks, and a CLUB-based loss to minimize mutual information between the latent features and the encoder input. The authors frame these losses through a custom application of the information bottleneck (IB) principle to MAEs. The paper claims a single quantitative result (83.9% ImageNet-1K accuracy at 400 epochs vs. 83.4% for 1600-epoch MAE) but the experiments section is truncated in the parsed text, removing all tables and comparison details.

---

## Strengths

1. **Novel framing of MAE through the information bottleneck principle**: The paper attempts to provide a principled information-theoretic perspective on why MAEs work, connecting the encoder's latent space to the IB notions of relevant and irrelevant information (Definition 1, Eq. 3, Section 4.1). While the execution has significant gaps, the lens itself is a sensible direction that goes beyond existing implicit contrastive-learning analogies.

2. **The method translates IB conditions into concrete, implementable losses**: The paper connects the conditions in Corollary 4 to two practical loss functions — InfoNCE for MI maximization (Eq. 7) and CLUB for MI minimization (Eq. 10) — that can be plugged into an existing MAE training pipeline (Section 4.2). This makes the approach easy to implement and ablate.

3. **Claims a non-trivial empirical result**: The abstract states that 400-epoch MI-MAE achieves 83.9% accuracy on ImageNet-1K, surpassing 1600-epoch MAE by 0.5%, and mentions improvements on detection and segmentation. If verified in the full (non-truncated) submission, this would demonstrate a meaningful efficiency gain.

---

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical derivation is not rigorous enough to justify the method.** Several critical steps are missing or opaque:
   - **Definition 1** defines information distortion as $D_I = I(X·(1-m); X·m | \widehat{X·m})$, but the justification for why this specific conditional mutual information corresponds to the IB notion of "distortion" is absent. The connection is merely asserted.
   - **Eq. 3 (the IB Lagrangian)** is presented as a direct application of Tishby & Zaslavsky (2015) without clarifying how the MAE-specific variables ($\widetilde{X·(1-m)}$, $D_{IB}$) map onto the standard IB formulation.
   - **Theorem 2** states an upper bound involving $O(K_x|Y|/\sqrt{n_x})$ but is presented without proof, derivation, or clear connection to standard learning-theoretic quantities. The bound's dependence on $|Y|$ (the "ground truth" set) and the role of the bias $r$ are not explained.
   - **Corollary 4** is central to justifying the contrastive loss, yet its derivation is completely opaque. The three conditions for maximizing $I(\hat{z}_k; z_k)$ are stated without proof, and the leap from these conditions to the InfoNCE loss (line 114) is a single sentence. InfoNCE maximizes a *lower bound* on MI, while Corollary 4 involves MI directly — this gap is not addressed.
   - **Line 140** asserts that optimizing $\mathcal{L}_{\text{min.mi}}$ "also satisfies the third condition in Corollary 4" without any justification.
   
   Collectively, these gaps mean the theory does not convincingly derive the proposed losses. The losses may be effective, but the IB framing is at best a loose motivation, not a derivation.

2. **Novelty is incremental and positioning relative to prior work is insufficient.** The two loss components — InfoNCE and CLUB — are standard tools in the literature. Applying them to MAE with multiple orthogonal masks is a straightforward combination. The paper mentions U-MAE (Zhang et al., 2022) and other contrastive-MAE connections but does not clearly articulate what MI-MAE adds beyond what these methods already accomplish. The paper states that prior methods "only perform on par with the original MAE" (line 46), but since comparisons to U-MAE, CIM, or other contrastive MAE variants are not present in the (truncated) experiments section, this claim is unsubstantiated.

### Minor

1. **The "mutually orthogonal masks" concept is underspecified.** The paper explains that masks are non-overlapping and partition the image into $N$ inputs plus a residual $X_0$ (lines 103-104), but it does not describe *how* these masks are generated algorithmically (e.g., random non-overlapping partition? fixed grid? adaptive?). The generation mechanism could affect the results.

2. **The computational efficiency claim needs clarification.** The paper reduces training epochs to one-quarter because four masks are used per image (line 155), implying comparable total compute. This logic is sound at the level of total encoder forward passes (4 masks × epochs/4 = 1 mask × epochs), but the paper does not state this explicitly or provide FLOPs/wall-time comparisons. A reader could reasonably be confused. A brief analysis would resolve this.

3. **The experiments section is truncated in the parsed text**, cutting off after Algorithm 1 begins (line 160). While this is a parser artifact and the original submission likely contains the full experimental results (tables for classification, detection, segmentation, ablations), the parsed version available for review does not contain the evidence supporting the core empirical claims. This limits what can be evaluated.

### Trivial
- The overbrace notation $\overbrace{X\cdot(1-m)}^{}$ (lines 73, 79, 81, 84) and tilde notation $\widetilde{X\cdot(1-m)}$ (Eq. 3) are introduced without formal definition, making the theoretical section harder to follow than necessary.

---

## Nice-to-Haves
- An ablation study comparing: (a) MAE baseline, (b) MAE + InfoNCE only, (c) MAE + CLUB only, (d) full MI-MAE, to isolate the contribution of each loss term.
- A comparison against existing contrastive-MAE methods (U-MAE, CIM, etc.) to substantiate the claim that MI-MAE outperforms them.
- A brief analysis of how the number of masks $N$ and their overlap pattern affect performance and training cost.

---

## Removed Points

- **"References and appendix are absent"** (Harsh Critic, last bullet under Other Observations): The parser strips these; they exist in the original submission.
- **"The paper cannot be independently verified"** / **"not yet released"** type concerns: All cited models, datasets, and references are assumed to exist per the review instructions.
- **Criticism about "unclear what MI-MAE adds beyond prior methods" where the critic implies the paper does not cite U-MAE**: The paper *does* cite U-MAE (line 46) and positions itself relative to it. The concern about insufficient *differentiation* is kept in Major weakness #2, but the claim that the paper omits these works entirely is incorrect.
- **Pure formatting/style nitpicks** about the paper's presentation are removed.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension: the paper's main differentiator is an IB-based theoretical framing, but that framing has too many gaps to be persuasive. The practical method (InfoNCE + CLUB on multiple masks) is a modest engineering contribution that could stand on its own empirical merits, but those merits cannot be fully assessed from the truncated text.

---

## Suggestions

1. **Reframe the theoretical contribution.** Either tighten the derivation substantially — defining all notation, showing the steps from the IB Lagrangian to the bounds, and providing proofs or clear references — or acknowledge that the IB principle serves as a loose motivation rather than a rigorous derivation of the losses. The paper's value does not hinge on the theory being a formal derivation; admitting heuristic approximations would be intellectually honest and less confusing.
2. **Specify the mask generation algorithm.** Describe how multiple orthogonal masks are created for each image (e.g., random non-overlapping patch assignment? fixed partition?) and discuss the implications for representation learning.
3. **Provide compute-normalized comparisons.** Explicitly state that total encoder forward passes are comparable (4 masks × ¼ epochs = 1 mask × 1 epoch) and provide wall-clock time or FLOPs comparisons.
4. **Compare against relevant contrastive-MAE baselines** (U-MAE, CIM, etc.) in the experimental section, not just the original MAE, to substantiate the claimed advantage.
5. **Add separate ablations** for the two loss terms to show that each contributes meaningfully.

---

## Score and Decision

**Originality**: 5/10 — The IB framing is somewhat novel for MAEs, but the losses are standard and the combination is incremental.  
**Importance of research question**: 7/10 — Understanding and improving MAEs is an important topic.  
**Claims support**: 3/10 — The theoretical claims are not well supported; the empirical claims cannot be verified from the truncated parsed text.  
**Soundness**: 4/10 — The theoretical derivation has significant gaps; the experimental design choices (epoch adjustment for multiple masks) are reasonable but incompletely justified.  
**Clarity**: 4/10 — The notation in Section 4 is confusing and several key concepts are underspecified.  
**Value to community**: 5/10 — If the empirical results hold and the method is simple to implement, it could have practical value, but the theoretical framing does not provide deep new insight.

The paper attempts a principled information-theoretic analysis of masked autoencoders but falls short in execution: the theoretical derivation is not rigorous, the method is an incremental combination of existing losses, and the empirical validation is absent from the parsed submission text. The claimed empirical result (83.9% at 400 epochs) is interesting but cannot be evaluated from what is available. The paper would need substantial revisions — particularly a tightened or honestly-scoped theoretical section, complete empirical validation, and clearer differentiation from prior work — to be reconsidered.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>