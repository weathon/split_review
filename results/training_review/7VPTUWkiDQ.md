Here is the consolidated review, verified against the paper content.

---

## Summary

This paper formalizes compositional generalization for object-centric representations as an identifiability problem. It proves that autoencoders with **additive decoders** (where slot-wise renders sum without interaction) and a **compositional consistency regularizer** (which encourages the encoder to invert the decoder on novel slot combinations) achieve provable slot identifiability on the full latent space—including out-of-distribution (OOD) combinations of slots. The theory is validated on a synthetic Spriteworld dataset with two non-occluding objects, and the assumptions are ablated in Slot Attention.

## Strengths

- **Formal bridge between identifiability theory and compositional generalization.** The paper provides a rigorous definition of compositional generalization as OOD slot identifiability (Definition 2.4), grounding a previously vague conjecture in the object-centric learning literature. This is a genuine theoretical contribution.

- **Coherent theoretical chain.** The paper proves three logically connected results: (1) slot identifiability on a convex slot-supported subset (Theorem 3.1, extending Brady et al. 2023); (2) decoder OOD generalization via additivity (Theorem 3.2); and (3) full compositional generalization when both additivity and compositional consistency are satisfied (Theorem 4.1). The chain from identifiability → decoder generalization → encoder generalization is well-structured.

- **Compositional consistency regularizer (Definition 4.2).** The idea of enforcing encoder-side OOD generalization by re-shuffling inferred slots and minimizing reconstruction on the resulting OOD images is simple, principled, and directly grounded in the theoretical framework. This is a novel loss that prior work on identifiability for compositional generalization did not address.

- **Proof that additive decoders suffice for decoder-side OOD generalization (Theorem 3.2).** This result shows that the slot-wise rendering functions learned in-distribution transfer to novel slot combinations without degradation, which connects cleanly to common design patterns in object-centric models even though the softmax normalization used in practice violates additivity.

- **Empirical demonstration that standard Slot Attention fails OOD and why.** The ablation in Table 1 systematically isolates the roles of additivity, consistency regularization, and deterministic inference, showing incremental improvements. Figure 5's heatmaps visually confirm that each component addresses a distinct failure mode (decoder vs. encoder).

## Weaknesses

### Fatal
None.

### Major

- **Empirical validation is confined to a single synthetic dataset with two non-occluding objects.** The Spriteworld data excludes occlusion (explicitly, to satisfy compositionality), uses only two objects, and has a simple diagonal-strip slot-supported subset. The paper's central claim—that these theoretical conditions enable compositional generalization—is only demonstrated in a near-minimal setting. The paper acknowledges this in the Discussion ("experiments with a broader set of architectures on more datasets are required") but the gap between the theory's ambitions and the experiments' scope is significant. Without results on datasets with ≥3 objects, occlusion (e.g., CLEVR, ObjectsRoom), or more complex latent structure, the practical relevance of the framework remains unsubstantiated.

- **The theoretical assumptions (compositionality, additivity) are violated in nearly any realistic multi-object scene.** Compositionality requires each pixel to depend locally on at most one slot; additivity requires slot-wise renders to sum without interaction. Occlusion boundaries, shadows, reflections, perspective effects, and transparent/reflective objects all break these assumptions. The paper acknowledges this (Section 6: "they do not allow slots to interact during rendering and thus cannot adequately model general multi-object scenes"), but the fact remains that the theory covers a regime far removed from the settings that motivate object-centric learning. The title "Provable Compositional Generalization" is accurate under the stated assumptions, but readers may infer broader practical guarantees than the theory supports.

- **The Slot Attention experiments require a deterministic encoder modification whose necessity is not fully analyzed.** The paper shows that making inference deterministic (replacing random slot initialization with fixed initialization) improves OOD performance (Table 1, rows 3→4), and notes that stochastic operations make the consistency loss challenging (Section 4). However, the theoretical framework (Theorem 4.1) does not invoke determinism. Whether this modification is fundamentally required, or merely a practical workaround, is left unclear. The paper's main empirical demonstration on a popular architecture thus relies on a change that is not justified by the theory.

### Minor

- **The R² slot identifiability metric, while standard in the field (Locatello et al. 2020, Brady et al. 2023), measures continuous latent-space alignment rather than the discrete object-discovery/binding problem that motivates object-centric learning.** High R² indicates that each inferred slot encodes a diffeomorphic transformation of a ground-truth slot, but the experiments do not verify that slots correspond to the same object identity across images in a semantically meaningful way (e.g., that slot 1 always encodes the circle). Since the Hungarian algorithm matches slots globally before computing R², the metric is more forgiving than true binding consistency.

- **The scatter plot (Figure 4, left) supporting the paper's central theoretical prediction has limited sampling in the critical low-loss region.** The paper claims that "OOD slot identifiability is maximized exactly when both losses are minimized," but only a handful of points occupy the region where both ℒ_rec and ℒ_cons are near zero. While the qualitative trend is visible, the claim is somewhat stronger than the data density supports.

- **The compositional consistency loss relies on a non-differentiable Hungarian matching step** (Section 4, paragraph 3). The paper does not analyze whether this introduces training instabilities or degenerate solutions (e.g., slot collapse), nor does it ablate the matching mechanism.

- **Warm-up phase for the consistency loss is not discussed.** The paper trains only on ℒ_rec for 100 epochs before introducing ℒ_cons, presumably because shuffled slots yield implausible images early in training. This design choice is sensible but is not analyzed or justified in the text.

### Trivial
None.

## Nice-to-Haves

- An experiment comparing the proposed approach with a concurrent related method (Lachapelle et al. 2023) that also studies additivity for compositional generalization would help situate the contribution.
- Visualizing the slot functions **D**_k (intermediate images before summation) for the additive decoder would provide a standard diagnostic verifying that each slot genuinely learns object-wise rendering.
- A failure analysis showing which OOD slot combinations are hardest (e.g., slots with overlapping x-positions) would deepen the empirical understanding.

## Removed Points

These points are flagged as removed because they are factually incorrect, misunderstand the paper, or are parser artifacts. Treat them with caution.

1. **"The ablation in Section 5.2 does not include any comparison to an unmodified Slot Attention baseline."** — Factually wrong. Row 1 of Table 1 (Add: ✗, L_cons: ✗, Det: ✗) IS the standard Slot Attention: non-additive softmax-mask decoder, no consistency loss, stochastic inference (random initialization). The critic mistakenly thought Det: ✗ was a non-standard modification, but it is the standard behavior.

2. **"The paper does not mention that the Spriteworld dataset uses non-occluding objects."** — False. The paper explicitly states (Section 5, Data paragraph): "To ensure that the generator satisfies compositionality, we exclude images with occluding objects."

3. **"The slot identifiability metric conflates continuous slot space alignment with actual object discovery... the Hungarian algorithm hides this problem."** — This misunderstands the metric. The R² measure fits regressors across the entire dataset; if slots permuted arbitrarily across images, the regression mapping would be inconsistent and R² would be low. High R² with global Hungarian matching DOES imply consistent slot-to-object correspondence.

4. **Various formatting/style criticisms and claims about missing appendices/proofs** — The appendix content exists in the original submission; the parser strips those sections.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the work that the paper itself does not already articulate.

## Suggestions

1. **Expand the experimental validation** to at least one dataset with 3–5 objects and occluding relationships (e.g., CLEVR6 or ObjectsRoom). Even if the assumptions are violated, demonstrating graceful degradation would substantially strengthen the claim of practical relevance.

2. **Add a standard Slot Attention baseline** (softmax masks, stochastic inference, no modifications) to Table 1, and clarify that Row 1 is already this baseline (the current caption could be misread).

3. **Analyze the necessity of deterministic inference** more thoroughly — either theoretically (why does stochasticity break the consistency loss gradient?) or empirically (compare consistency loss gradients with vs. without deterministic initialization).

4. **Discuss the warm-up phase** (100 epochs of reconstruction-only training) and its role in making the consistency loss tractable.

## Score and Decision

This paper makes a genuine theoretical contribution: it formalizes compositional generalization as OOD slot identifiability, proves sufficient conditions (additive decoder + compositional consistency), and proposes a principled regularizer. The theory is sound, well-structured, and clearly presented. The weaknesses are real but do not invalidate the core contribution — the experimental limitations are acknowledged by the authors, and the theoretical assumptions are stated transparently. The paper is appropriate for a venue that values theoretical foundations in representation learning, where the main contribution is the framework and formal results rather than empirical breadth.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**