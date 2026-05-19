- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper provides a theoretical framework for compositional generalization in object-centric representation learning. It proves that autoencoders with additive decoders and a compositional consistency regularizer can provably generalize to unseen combinations of known objects. The theory is validated on synthetic multi-object data, and an ablation study on Slot Attention demonstrates the practical relevance of each theoretical assumption.

## Strengths

- **Unified theoretical framework for compositional generalization**: The paper jointly addresses identifiability and out-of-distribution generalization, which prior work treated separately. Theorem 3 shows that combining an additive decoder, compositional consistency regularization, and compositional/irreducible assumptions on the generator yields provable compositional generalization (slot identifiability on the full latent space). This goes beyond earlier results that considered only identifiability or only generalization in isolation.

- **Novel compositional consistency regularizer**: Definition 4 introduces a loss \(\mathcal{L}_{\text{cons}}\) that trains the encoder to invert the decoder on out-of-distribution slot combinations. The paper shows both theoretically (Theorem 3) and empirically (Table 1, Figure 3) that this regularizer is necessary for encoder generalization — without it, OOD slot identifiability drops from 0.94 to 0.83 in the Slot Attention ablation. This provides a concrete, implementable method that prior works did not propose.

- **Extension of slot identifiability to restricted training supports**: Theorem 1 generalizes the identifiability result of Brady et al. (2023) from the full latent space to convex, slot-supported subsets. This is essential for the compositional generalization setting, where the training distribution covers only a subset of slot combinations. The proof shows that compositionality on the whole space can be relaxed while still guaranteeing slot identifiability in-distribution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Convexity assumption is introduced without justification**: Theorem 1 and Theorem 3 require \(\mathcal{Z}_{\text{rest}}\) to be *convex*, yet the paper never discusses why this geometric condition is needed, whether it holds for typical multi-object datasets (beyond the diagonal strip used in experiments), or what happens when it is violated. The proof likely relies on convexity for connectivity or path-lifting arguments, but this is left implicit. Clarifying this would help readers assess the scope of the theoretical result.

- **R² identifiability metric does not directly measure diffeomorphism**: Definition 3 (slot identifiability) requires a *diffeomorphic* relationship between ground-truth and inferred slots, but the experiments measure this via nonlinear regression R². A high R² from an MLP regressor may not guarantee diffeomorphism (e.g., the mapping could be injective but not smooth, or could only generalize on the support of training data). The paper does not discuss this gap. This does not invalidate the results — R² is the standard metric in this literature — but acknowledging the mismatch would strengthen the presentation.

- **Caveat about compositionality being implicitly learned is underdeveloped**: The paper states (Section 4) that the compositionality regularizer from Brady et al. is not explicitly optimized because inductive biases in object-centric models seem to minimize it implicitly. However, the theoretical guarantees of Theorem 3 require compositionality. The paper measures compositional contrast on the *training set* but does not verify it holds OOD, so it is possible the decoder is not compositional on OOD points, meaning the guarantees may not apply. A brief caveat or discussion of this risk is needed.

- **Slot Attention ablation has limited scope**: Table 1 reports results for a single configuration (two objects, two slots, specific hyperparameters). The paper does not analyze sensitivity to the number of slots, latent dimensionality, batch size (which affects the diversity of slot combinations used in \(\mathcal{L}_{\text{cons}}\)), or whether the conclusions hold for more than two objects. As a theory paper with synthetic experiments this is understandable, but the generality of the ablation findings is unclear.

### Trivial
None.

## Nice-to-Haves

- Provide a concrete example of a compositional generator that can be represented by an additive decoder in the main text (the discussion is currently relegated to the appendix).
- Directly test whether the encoder inverts the decoder OOD on a grid of interpolated slot combinations (not just via reconstruction R²) to visualize the "encoder failure" the paper diagnoses.
- Discuss whether the convexity assumption can be relaxed to a weaker condition such as connectedness or path-connectedness, and whether the experimental diagonal strip could be replaced with a non-convex support.
- Analyze why stochastic encoders hurt compositional consistency training (e.g., does Hungarian matching become inconsistent across forward passes?) and propose a more principled solution beyond deterministic inference.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No discussion of slot permutation invariance during training"** (Harsh Critic, Missing Parts §1): The paper explicitly discusses slot permutation and uses the Hungarian algorithm both for the consistency loss (line 269) and for evaluation (line 292). This criticism is factually wrong.

- **"The paper does not report results for models that do not use the additive decoder"** (Harsh Critic, Missing Parts §2): Table 1 row 1 (Add.=✗, \(\mathcal{L}_{\text{cons}}\)=✗, Det.=✗) reports exactly this baseline. The criticism is factually wrong.

- **"Missing analysis of failure cases"** (Harsh Critic, Missing Parts §3): This requests experiments beyond the stated scope of the paper. The paper transparently scopes itself as a first theoretical result on synthetic data and acknowledges extensions in the Discussion. This is not a weakness of the work as presented.

- **"Section 3.3 reformulation of IZ is only valid if the encoder's slot functions are surjective"** (Harsh Critic, Section-by-Section §5): The paper shows the equivalence mathematically (lines 251–258) and uses it to construct a sampling strategy that covers \(\mathcal{IZ}\) by construction from ID data. The concern is overly pedantic given the empirical validation.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives overlap substantially; the only genuinely novel observation not already present in the paper is the suggestion to directly test whether the learned encoder inverts the decoder OOD via an identity-check on interpolated slot combinations, rather than only through reconstruction R². This is a useful experimental design suggestion but not a new insight about the paper itself.

## Suggestions

- Add a paragraph in Section 3 (or in the discussion of Theorem 1) explaining why convexity is required for the proof and whether it can be relaxed, even if only to say "we leave this relaxation to future work."
- In the metrics paragraph (Section 6), add a brief note that R² approximates the required diffeomorphic relationship and is standard in the literature, but is not a perfect measure of diffeomorphism.
- In Section 4, explicitly state: "If the decoder is not compositional on OOD points, the theoretical guarantees of Theorem 3 may not hold, and our experiments only verify compositionality in-distribution."
- Clarify whether the Slot Attention ablation results are representative across different random seeds, slot counts, and latent dimensionalities, even if only in a brief sentence.
- Add a concrete example (e.g., "separated object rendering with occlusion-free compositing via additive alpha compositing") in Section 3.1 to build intuition for additive decoders.
