- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 3, 5, 3, 5
Now I have a thorough understanding of the paper and all the claims. Let me construct the final consolidated review.

## Summary

This paper studies "reflection networks" — deep neural networks with absolute value activation, scalar weights beyond the first layer, constant width, and non-standard ℓ₁^L regularization — and shows that their training problem is equivalent to a convex Lasso problem. For 3-layer networks, the Lasso dictionary is given explicitly with feature functions interpretable as distances to reflection planes. For deeper networks (L>3), the paper states a theorem claiming Lasso equivalence and shows that the sublibrary of features contains reflections of increasing order (up to 2(L−3)). The paper also presents qualitative experiments on simulated and LLM-embedding data suggesting that trained networks exhibit kinks at reflected data points.

## Strengths

- **Explicit Lasso dictionary for 3-layer networks (Theorem 1)**. The paper provides a fully concrete dictionary construction for depth-3 reflection networks in arbitrary input dimension, including a reconstruction formula for the optimal network. This is a non-trivial extension of prior 1D and ReLU results.

- **Geometric interpretation of 3-layer features (Theorem 2 / geometricInterp)**. The features are interpretable as distances to reflection planes spanned by training data, expressed using wedge products and generalized cross products. This bridges complex algebraic dictionary elements to a clean geometric picture.

- **Multilevel symmetry result (Theorem 5 / absvalsublib)**. The paper proves that the sublibrary of deeper networks contains reflections of order up to 2(L−3), formally establishing that additional layers introduce higher-order reflections — a structural distinction from shallow networks. The sublibrary features (data feature biases) are defined constructively via a recursion.

- **Honest acknowledgement of limitations**. The paper acknowledges that the full dictionary for L>3 is future work (line 575), that exponential complexity in d is NP-hard to avoid (Lemma 2), and that the architecture and regularization are non-standard. This candor is valuable.

## Weaknesses

### Fatal

None.

### Major

- **The central claim of full Lasso equivalence for arbitrary depth (Theorem 4 / lemma:deep) is only partially delivered.** Theorem 4 states that reflection networks of *any* depth are equivalent to Lasso problems with finite, discrete dictionaries. However, the paper's own text (line 575) says: *"A full analysis of the entire dictionary for networks with more than 3 layers is an area for future work."* The explicit dictionary construction is given only for L=3; for L>3, the paper defines the *sublibrary* (a subset of features) and proves the reflection-order bound (Theorem 5), but the full dictionary — which features exist, how they are indexed, and how the Lasso selects among them — is not provided. This gap between the stated theorem and what is actually constructed is a significant weakness.

- **Experiments are purely qualitative and do not validate the claimed equivalence.** The experiments train standard networks with Adam, then visually inspect whether learned functions have kinks at reflected points. This is consistent with the theory but does not demonstrate that: (a) the trained network corresponds to any optimal Lasso solution, (b) the specific reflection features predicted by the Lasso dictionary are the ones selected, or (c) the Lasso leads to different/better solutions than standard training. The LLM embedding experiments show plots projected onto one dimension with no quantitative metrics, no error bars, no baselines (e.g., linear classifier or shallow network accuracy), and no comparison between Lasso-predicted and empirically observed kink locations. The simulated-data experiment (2D with all second coordinates zero, effectively 1D) uses a Lasso pre-initialization for only 1 of 100 neurons, making the significance of the resulting reflection patterns unclear.

- **The architecture studied is far more restricted than the paper's broad framing suggests.** The "reflection network" (Eq. 4) constrains all weights beyond the first layer to scalars, keeps the number of neurons constant across layers, uses absolute value activation, and employs a non-standard ℓ₁^L regularization. The abstract states *"training deep neural networks (DNNs) with absolute value activation and arbitrary input dimension can be formulated as equivalent convex Lasso problems"* — this omission of the scalar-weight and constant-width restrictions overstates the scope. While the paper does introduce the reflection network as a special case in the main text (line 32), the abstract and introduction repeatedly use unqualified "deep networks" language that practitioners will reasonably interpret as applying to standard architectures.

### Minor

- **The 3-layer dictionary is exponential in d (O((Nd)^d)), severely limiting practical applicability.** The paper acknowledges this and suggests subsampling or polishing as remedies, but subsampling breaks the exact equivalence and optimality guarantees. This means the Lasso formulation cannot be tractably used for even moderate input dimensions, which undercuts the practical significance of the convexification.

- **The simulated-data experiment is contrived.** The data lies in ℝ² but all second coordinates are zero, making it effectively 1D. The Lasso is solved on the 1D projection, then one neuron is pre-initialized from that solution. The finding that kinks appear at reflected points is not surprising given this setup, and with 99 randomly initialized neurons, it is unclear whether the reflection pattern is robust.

- **No classification accuracy reported for LLM experiments.** The paper trains networks to classify IMDB reviews but reports only visual projections, not accuracy. Without knowing whether these networks perform well, the significance of the observed reflection patterns is unclear — they could be features of a poorly performing model.

- **Novelty relative to prior work is somewhat incremental.** The 1DNN work already handled absolute value activation and arbitrary depth for 1D data with reflection features. Pilanci & Ergen (2023) already handled arbitrary dimension for shallow ReLU networks with geometric algebra features. The current contribution extends both to absolute value + high dimensions + depth ≥3, which is a natural synthesis. The key novelty is the multilevel symmetry result (Theorem 5), but this is only stated for the sublibrary, not the full dictionary.

### Trivial

None of note.

## Nice-to-Haves

- Provide the explicit dictionary construction for L=4 as a concrete illustration of the pattern for deeper networks, even if the general case is deferred.
- Add quantitative validation: pick a small dataset (d=2, N small), solve the exact Lasso, reconstruct the network, and compare the resulting function to a gradient-descent-trained network. Measure how well the Lasso predicts kink locations.
- Report accuracy or regression error for the LLM experiments to establish that the reflection-bearing networks are actually performing well on the task.
- Clarify the relationship between the volume formula (Eq. 5) and the distance-to-planes interpretation (Eq. 7) — they appear as separate results without explicit derivation of one from the other.

## Removed Points

These points from the reviews were removed with brief justification:

- *"Proofs deferred to appendix cannot be evaluated"* — Removed per policy: the parser strips appendices from all papers; proofs exist in the original submission.
- *"Geometric algebra background goes mostly unused"* — Removed as factually inaccurate: wedge products, the Hodge star, and generalized cross products are directly used in Theorem 2 and throughout the dictionary construction.
- *"Missing related works"* — Removed per policy: we cannot verify what the paper does/does not cite.
- *Pure formatting/presentation nitpicks* — Removed as parser artifacts or style preferences.
- *"Overclaims novelty: prior work already did X"* — Softened to Minor (above) rather than the critic's stronger framing; the paper does extend both 1DNN (to arbitrary dimension) and Pilanci2023 (to absolute value and deeper layers), which constitutes genuine novelty even if incremental.
- *"Theorem 4 is stated without proof sketch"* — Partially removed the appendix-deferred claim; kept the substantive point (line 575 admits the full dictionary for L>3 is future work) in Major weaknesses.
- *"The dictionary definition in Theorem 1 is extremely complex"* — This is subjective; the paper provides a precise mathematical definition, and complexity is inherent to the problem.

## Novel Insights

The harsh critic's observation that the paper's core theoretical result (Theorem 4) is presented without explicit construction for L>3, combined with the paper's own admission that the full dictionary is future work, reveals an important structural issue: the paper claims to prove a general equivalence but delivers the constructive part only for L=3. The strength finder's focus on the sublibrary and the reflection-order theorem (absvalsublib) provides a more precise characterization of what is actually shown for deeper networks — namely, that a subset of features (the sublibrary) has a known structure, but the full dictionary remains unspecified. The tension between these two perspectives is the paper's central unresolved issue.

## Suggestions

1. **Restrict the scope of the central claim.** Either provide the explicit dictionary for L>3 (even just for L=4 as a proof of concept) or honestly reframe Theorem 4 as a partial result: the equivalence is fully constructive for L=3, and for L>3 a sublibrary is characterized but the full dictionary is deferred. The abstract and introduction should say "reflection networks" not "deep neural networks" without qualification.
2. **Add quantitative experimental validation.** Pick a small (N small, d=2) dataset, construct the exact Lasso dictionary, solve it, reconstruct the network, and compare its predictions to both the Lasso solution and a gradient-descent-trained network. This would validate the claimed equivalence directly rather than relying on visual pattern-matching.
3. **Report classification accuracy** for the LLM experiments and compare to baselines (linear classifier, shallow network) to show the reflection features are associated with good performance.
4. **Run the simulated experiment** with genuinely 2D data (not all-second-coordinate-zero), with multiple random seeds, and without the Lasso pre-initialization to see whether reflection patterns emerge from standard training alone.
