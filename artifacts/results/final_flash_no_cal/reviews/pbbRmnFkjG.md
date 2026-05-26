Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper presents a large-scale interpretability study of DINOv2 using a 32,000-atom concept dictionary learned via a stable sparse autoencoder (RA-SAE). The study has three main parts: (1) analyzing how downstream tasks (classification, segmentation, depth estimation) recruit different concept subsets, revealing novel patterns such as "Elsewhere" concepts for classification and three families of monocular depth cues; (2) documenting how the learned dictionary's geometry departs from the near-orthogonal ideal of the Linear Representation Hypothesis (LRH) — higher coherence, sharper spectral decay, task-aligned anisotropy; (3) proposing the Minkowski Representation Hypothesis (MRH), where token embeddings are Minkowski sums of convex polytopes, formalizing a connection to multi-head attention. The paper is ambitious, clearly written, and tackles an important question about how vision transformers organize their internal representations.

## Strengths

1. **Largest-scale concept dictionary for a vision foundation model.** The paper extracts a 32,000-atom dictionary from DINOv2 with reconstruction fidelity R² > 88%, claimed as the largest interpretability demonstration for a vision foundation model to date (Abstract; Section 2). This scale enables both the downstream task analysis and the geometric study.

2. **Discovery of "Elsewhere" concepts implementing a form of conditional negation.** The paper identifies concepts that fire broadly across tokens but are suppressed on the object itself, and vanish when the object is causally removed via masking (Figure 2, Section 3). This reveals a learned negation pattern not previously documented in concept-based vision interpretability — prior work typically assumes concepts fire on the features they represent.

3. **Systematic identification of three distinct monocular cue families underlying DINO's depth estimation.** Using controlled perturbations (median blur, edge-preserving smoothing, high-pass filtering), the paper reveals three functional clusters: projective geometry cues, shadow-based cues, and local frequency transitions (Figure 3, Section 3). This decomposes DINO's emergent 3D understanding into interpretable primitives.

4. **Quantitative documentation that the dictionary departs from the near-orthogonal LRH ideal.** The paper shows pairwise atom coherence is higher than both random and Grassmannian baselines, the singular value spectrum decays sharply, and task-recruited concepts form low-dimensional subspaces (Figure 4, Section 4). These findings challenge a purely sparse-coding view with proper statistical baselines.

5. **Section 5 (The Shape of an Image) provides SAE-independent evidence for structured token geometry.** Per-image PCA maps reveal smooth, semantically aligned structure that cannot be explained by position alone. The positional encoding compression analysis (evolving from high-rank to a smooth 2D sheet across layers) is robust, well-visualized, and methodologically independent of the SAE framework (Figures 5–6, Section 5).

6. **Formal connection between multi-head attention and Minkowski sums (Proposition 1).** Proving that each attention head outputs a convex combination of its values and the sum across heads is a Minkowski sum provides a mechanistic basis for MRH grounded in the transformer architecture (Section 6). The non-identifiability result (Proposition 2) is an honest characterization that has implications for interpretability practice.

7. **Bounded steering prediction derived from MRH.** The paper derives a testable implication — linear steering in a landmark-based geometry should saturate — which connects to observed plateaus in SAE-style steering and motivates structure-aware probes (Section 6, Implications).

## Weaknesses

### Fatal

None.

### Major

1. **The LRH critique rests on a single SAE variant, limiting its generality.** The paper operationalizes LRH exclusively through the RA-SAE (with non-negativity, convex-hull-bounded atoms, and BatchTopK sparsity) and then finds the resulting dictionary departs from near-orthogonality. No comparisons are made with alternative SAE formulations (standard TopK, Gated SAE, JumpReLU SAE) or with purely geometric analyses of the *raw* DINOv2 activations (e.g., CKA, MDS, spectral analysis of original activations). Without showing that the same departures appear across multiple factorization methods, the critique of LRH remains potentially method-dependent. Section 5 (PCA on raw activations) provides some independent evidence, but it does not directly speak to the near-orthogonal feature-packing claim. The paper acknowledges this gap only indirectly. (Section 2, Section 4)

2. **The Minkowski Representation Hypothesis is presented as a central contribution but has insufficient empirical support relative to that billing.** The paper is appropriately careful in calling MRH a "working hypothesis" with "preliminary empirical signals," yet it is presented as one of the three main contributions alongside the dictionary and the task analyses. The supporting evidence has notable gaps:
   - **Proposition 1** shows that multi-head attention *can* realize MRH — this is a formal connection, not evidence that DINOv2 *does* organize its representations this way. The mechanism (convex combinations summing to a Minkowski sum) is a property of any ViT, so it doesn't distinguish MRH from other accounts.
   - **The empirical diagnostics** (geodesic vs. straight-line interpolation; Archetypal Analysis matching SAE reconstruction; block structure in Gram matrices; Figure 26) are consistent with MRH but also consistent with other explanations. In particular, Archetypal Analysis matching SAE reconstruction on a per-image basis is an apples-to-oranges comparison (AA is per-image, SAE is global), and block structure in Gram matrices is expected from any k-sparse non-negative code set.
   - **No distinguishing experimental test is provided.** The paper outlines implications (steering saturation, landmark-based proximity) but does not evaluate any of them against LRH-based alternatives. Without a test that could distinguish MRH from LRH, the hypothesis remains a speculative reframing rather than a validated account. (Section 6)

3. **The task-specific analyses, while qualitatively insightful, lack causal validation for the interpretability claims.** The Elsewhere concept analysis includes causal masking (concept vanishes when object is removed), which is a positive step. However, the depth cue analysis identifies concepts whose activation changes under specific perturbations, but does not show that ablating these concepts causally impairs depth estimation performance. Without such validation, these remain interesting correlations within the SAE model rather than confirmed properties of DINOv2's internal reasoning mechanisms. The paper's framing ("discovering what DINO sees") overstates the evidence level for these findings. (Section 3)

### Minor

1. **The non-identifiability result (Proposition 2) is presented as a contribution but primarily underscores a limitation.** While honestly acknowledging that Minkowski decomposition from final activations is ill-posed is valuable, the paper does not fully grapple with how this underdetermination affects the empirical tractability of MRH as an explanatory framework. If the decomposition cannot be uniquely recovered, how should researchers confirm or falsify MRH from observable data?

2. **Proposition 1's status as a "hypothesis" versus an architectural observation is blurred.** The multi-head attention → Minkowski sum connection is a mathematical consequence of the architecture, not an empirical discovery. The MRH as a *representational hypothesis* (that concepts are landmarks/regions) is logically separate from this mechanism. The paper would benefit from more clearly distinguishing the mechanistic claim (attention enables this geometry) from the empirical claim (DINOv2's representations actually exhibit this geometry).

3. **The depth cue perturbation analysis is somewhat circular in structure:** perturbations are designed to isolate specific cue types, concepts whose activations change are then identified as encoding those cue types, and the clusters are visualized via UMAP. The analysis recovers the perturbation design. This is a reasonable starting point, but the paper frames it as "discovering" the cue families rather than validating that the perturbations isolate what they claim to isolate.

4. **Several key analyses are deferred to appendices.** The Elsewhere concept proof via causal masking, the depth cue perturbation details, and the full MRH theoretical statements are all in appendices that, while present in the original submission, are not available in the main text. The main paper's empirical core (Figures 4, 5, 6) is solid, but the qualitative task analyses (Figures 2, 3) are hard to fully evaluate without the appendix content.

### Trivial

None.

## Nice-to-Haves

- **Cross-method validation for the LRH critique:** Running the same geometric diagnostics (coherence, spectral decay) on dictionaries learned by standard TopK, Gated, or JumpReLU SAEs would significantly strengthen the paper's challenge to LRH.
- **A distinguishing experimental test of MRH:** Measuring whether linear steering in DINOv2 saturates (as MRH predicts) vs. remains linear (as LRH predicts), or testing whether archetypal steering avoids saturation, would provide direct evidence for or against MRH.
- **Ablation studies for the depth cue concepts:** Showing that ablating the identified concept families impairs depth estimation accuracy would move the depth analysis from correlational to causal.
- **Inclusion of confidence intervals or error bars** on the geometric diagnostics (coherence, spectral decay) across multiple SAE training runs would strengthen the quantitative claims in Section 4.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"The central evidence against LRH is circular with respect to the tool used to test it… This is a non-sequitur."* — Overstated. The paper provides baselines (random, Grassmannian) and Section 5 is SAE-independent. The single-SAE limitation is real (retained as Major weakness #1), but calling it "circular" or a "non-sequitur" mischaracterizes the paper's logic: operationalizing LRH as a factorization and measuring whether the factorization matches LRH's geometric ideal is a valid approach. Removed due to factual inaccuracy in the severity framing.

- *"The paper offers no causal evidence that these SAE atoms are the mechanisms by which DINOv2 performs these tasks."* — Factually incorrect. The paper provides causal masking evidence for Elsewhere concepts (they vanish when the object is removed, Section 3, Figure 2). The depth analysis could benefit from stronger causal validation (retained as Minor weakness #3), but the blanket statement is wrong. Removed as factually incorrect.

- *"Proposition 1 is a trivially true property of the architecture, not a hypothesis about what concepts are or how they are organized."* — The formalization is a genuine contribution that links architectural mechanism to geometric structure. The hypothesis component (concepts as landmarks/regions) is separate from the mechanism, but the formal connection is non-trivial. Removed as it undervalues the contribution.

- *"Non-identifiability… further undermines the hypothesis's empirical tractability."* — The paper honestly acknowledges non-identifiability and draws constructive implications (need for intermediate signals). This is a feature, not a bug. Removed.

- *"The depth cue analysis is particularly circular: controlled perturbations are applied to isolate specific cue types, and then concepts whose activations change are identified as those cue types. This largely recovers the perturbation set."* — This is a valid observation about the analysis design (retained as Minor weakness #3) but the "circular" framing is too strong. The perturbation methodology is standard practice in feature attribution.

## Novel Insights

The most genuinely novel insight that emerges from synthesizing the reviews is a tension in the paper's architecture: the paper's strongest contribution (documenting departures from LRH via the SAE dictionary, Section 4) is partially undermined by its methodological dependence on that same SAE, while its most methodologically independent evidence (the token geometry in Section 5) is only loosely connected to the core LRH critique. The paper would be substantially strengthened by bridging these — e.g., showing that the geometric properties documented in Section 4 (coherence, spectral decay) can be detected through SAE-independent analyses of raw token geometry. Additionally, the Elsewhere concept finding (conditional negation) is a genuinely novel empirical observation that deserves more emphasis as a standalone discovery, independent of the MRH/LRH framing.

## Suggestions

1. **Run the same geometric diagnostics on alternative SAE formulations** (standard TopK, Gated SAE, JumpReLU SAE) and on spectral decompositions of the raw DINOv2 activations. If the departures from near-orthogonality are robust across methods, the critique of LRH becomes much more convincing. If they are method-specific, revise the claims accordingly.

2. **Provide a distinguishing experimental test of MRH vs. LRH.** The steering saturation prediction is ideal for this: measure whether linear steering in DINOv2 saturates or reverses at high strengths (consistent with MRH's bounded-landmark picture) and compare with predictions from the near-orthogonal LRH account. Alternatively, test whether archetypal steering (moving toward a learned landmark) avoids saturation.

3. **Add causal validation for the depth cue analysis** by ablating the top concepts in each identified family and measuring the drop in depth estimation accuracy. This would move the analysis from correlational to mechanistic.

4. **Restructure the paper to better reflect the evidence levels.** The MRH section is currently positioned as a co-equal contribution with the dictionary and task analyses, but the evidence for it is substantially weaker. Consider reframing Section 6 as "Towards Minkowski Geometry" with clear hedging, and elevating the Elsewhere/border/depth findings to standalone contribution status.

5. **Clarify the relationship between the SAE-based analyses and the PCA-based analyses in Section 5.** Currently these read as parallel threads; showing explicit connections (e.g., projecting SAE atoms into the PCA space of raw activations) would unify the paper's narrative.

## Score and Decision

This paper makes substantial contributions: the largest concept dictionary for a vision foundation model, novel empirical discoveries about task-specific concept recruitment, a well-documented challenge to the near-orthogonal LRH ideal, and a thought-provoking geometric hypothesis. The weaknesses are real but addressable — the single-SAE limitation weakens the LRH critique, the MRH evidence is preliminary relative to its billing, and the task analyses would benefit from causal validation. These do not invalidate the paper's contributions; they define the frontier for future work. The paper is clearly written, tackles an important question, and provides a rich foundation for follow-up research.

**Score: 7.5**

**Decision: Accept**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>