Now let me write the consolidated final review.

## Summary

The paper extracts a 32,000-atom concept dictionary from DINOv2 using a stable sparse autoencoder (RA-SAE), then analyzes how downstream tasks (classification, segmentation, depth estimation) recruit these concepts, revealing functional specialization including "Elsewhere" concepts (implementing learned negation), border detectors, and three monocular depth cue families. The geometric analysis of the dictionary finds higher coherence and sharper spectral decay than Grassmannian/random baselines, challenging a purely sparse near-orthogonal view. Motivated by these departures, the paper proposes the Minkowski Representation Hypothesis (MRH), in which tokens behave as Minkowski sums of headwise convex polytopes around archetypal landmarks, and shows that multi-head attention naturally realizes this structure.

## Strengths

- **Largest-scale concept extraction for a vision foundation model.** The paper trains a stable SAE on DINOv2 to produce a 32,000-atom concept dictionary with R² > 88% reconstruction fidelity (Section 2). This scale directly enables the downstream and geometric analyses and, as released, could be a substantial community resource.

- **Task-specific functional specialization with quantitative controls.** The paper shows that classification, segmentation, and depth estimation recruit distinct, low-dimensional concept subspaces, with intra-task concepts more aligned than random subsets and eigenspectra decaying faster than baselines (Figure 11). The identification of specific interpretable families — "Elsewhere" concepts for classification with causal evidence via object removal (Figure 2, left), boundary detectors for segmentation forming a tight cluster in embedding space (Figure 2, right; Figure 10), and three monocular cue families for depth (projective, shadow, frequency; Figure 3) — goes beyond task-agnostic concept lists.

- **Empirical challenge to the sparse, near-orthogonal view of LRH.** The paper provides multiple geometric diagnostics on the learned dictionary: atom-pair coherence is higher than random and Grassmannian baselines (Figure 4, bottom left; Section 4), the singular-value spectrum decays sharply (Figure 4, bottom middle), and the correlation between co-activation and geometric affinity is weak (Figure 13). These findings are concretely benchmarked against Grassmannian frames via the TAAP algorithm (Appendix F) and shuffled baselines (Appendix E).

- **MRH with mechanistic derivation.** Proposition 1 formally establishes that multi-head attention realizes MRH through headwise convex combinations and Minkowski sums — a direct architectural grounding for the geometric hypothesis. The paper also derives a non-identifiability result (Proposition 2) that honestly characterizes the limits of interpreting MRH from final activations alone.

- **Causal isolation of "Elsewhere" concepts.** Classification concepts that activate off-object yet depend causally on the object's presence are identified and perturbed via causal masking (Figure 2, left; Section 3). This provides evidence for a learned negation mechanism going beyond correlational attribution.

- **Positional subspace analysis ruling out a trivial explanation.** The paper trains linear decoders to predict token coordinates, documents how the positional subspace compresses to two dimensions in final layers, and then projects tokens orthogonally to this subspace, finding that the smooth PCA structure "remains largely unchanged" (Section 5, Figure 25). This cleanly rules out positional encoding as the sole driver of the observed interpolative token geometry.

## Weaknesses

### Fatal
None.

### Major

- **The convex-hull constraint on the SAE dictionary may confound the geometric claims used to motivate departure from LRH.** The stable SAE constrains each dictionary atom to lie in the convex hull of real activations (Section 2, D = SC with S row-stochastic, conv(A) approximated by 128k k-means centroids). This constraint forces atoms to be interior to the data distribution rather than spanning the full space, which can itself increase atom-atom coherence and induce spectral decay. The paper compares only against random and Grassmannian baselines — neither controls for the convex-hull constraint. The correct control is an otherwise identical SAE that omits this constraint, to determine whether the reported higher coherence, sharp spectral decay, and antipodal pair structure are properties of DINOv2's representational geometry or artifacts of the RA-SAE's parametrization. Without this ablation, the strength of the challenge to LRH (Section 4) is unclear, which in turn weakens the motivation for MRH (though MRH itself has independent support from the positional analysis and Proposition 1).

- **Several central task-specific findings lack quantitative validation.** The paper makes strong claims that are supported only by qualitative examples or informal observation: (i) "Across many ImageNet classes, the top concepts for classification include … an 'Elsewhere' concept" — no number, fraction, or distribution is reported; (ii) "all the concepts among the top-50 consistently localize along object contours" for segmentation — no metric quantifies this (e.g., average distance to ground-truth boundaries); (iii) the three depth cue families are identified via UMAP clustering of perturbation responses, but no verification confirms the clusters correspond to distinct depth cues rather than statistical artifacts of the perturbations. The "intra-task concepts are significantly more aligned" claim (Section 3) similarly lacks a reported statistical test. These are the paper's main empirical results about what DINOv2 encodes, and they need rigorous quantitative backing to be fully convincing.

### Minor

- **Empirical evidence for MRH is thin relative to its prominence.** The paper presents MRH as a core contribution (appearing in the title, abstract, and a dedicated section), but the empirical support consists of a straight-line vs. k-NN interpolation test, an Archetypal Analysis comparison with ~10 archetypes, and block-structure observations in Gram matrices (Section 6, Fig. 26). The paper is transparent about these being "preliminary empirical signals" and MRH being a "working hypothesis," but the gap between the strength of the hypothesis language and the thinness of the evidence remains somewhat disproportionate. Proposition 1 (attention realizes MRH) is a mathematical observation about how attention works — it establishes architectural plausibility, not that DINOv2 *actually* uses this structure in a way that creates meaningful archetypal geometry.

- **Internal tension between the SAE-based analysis and MRH is not resolved.** The paper constructs a 32,000-atom concept dictionary via SAE (treating atoms as directions interpretable via linear probes), then later proposes MRH in which concepts are regions/landmarks rather than directions. The paper acknowledges this once ("extracting concepts from single layers is insufficient" in Section 7) but does not reconcile the two views or discuss whether the SAE-based findings (task specialization, geometric statistics) would survive reinterpretation under MRH.

### Trivial

None.

## Nice-to-Haves

- **Ablation of sparsity hyperparameter k=8.** The paper does not justify why k=8 was chosen or show sensitivity to this choice. A sweep over k (e.g., 4, 8, 16, 32) would clarify robustness of the geometric findings.

- **Concrete testable prediction of MRH.** The paper outlines steering implications but does not test a clear, non-trivial prediction. For example: if tokens are Minkowski sums of head-specific convex sets, perturbing attention weights to move a token toward a head's archetype should produce monotonic changes in task outputs until saturation at the archetype (not extrapolating). A demonstration of this would substantially strengthen MRH as an empirical proposal.

## Removed Points

**These points are flagged to be removed; treat them with caution.**
- The reviewer's criticism that the paper lacks missing related work comparisons (e.g., DARC, Fel et al. 2023b) — removed per the rule against citing missing related works without external sources to verify.
- The reviewer's criticism about missing appendix content (Figure 26 and Appendix content) — removed per the rule that the parser strips appendix sections from all papers; they exist in the original submission.
- The reviewer's claim that the paper "does not benchmark against prior DINO interpretability efforts" — removed per the missing-related-works rule.
- Various formatting/style nitpicks and complaints about "missing details" that are addressed in the stripped appendix — removed per the appendix rule.
- The reviewer's claim that the non-identifiability result (Proposition 2) "undermines the paper's entire interpretability agenda" — the paper itself acknowledges this limitation and proposes using intermediate signals to address it; the criticism misreads the paper's self-aware treatment.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation emerging across the reviews is the tension between the two analytical frameworks deployed in the paper: the SAE-based linear factor model (directions as concepts) and the MRH convex-geometric model (landmarks and regions as concepts). The paper does not fully resolve this tension, but it surfaces a genuinely important question for interpretability: whether concept extraction should aim for sparse directions or landmark geometry, and how to choose between these paradigms. A second novel insight — not emphasized by the paper but implicit in its findings — is the hybrid sparse-dense regime in DINOv2: most concepts are sparse, but a few positional concepts are nearly universally active. This challenges the binary framing of sparse vs. dense representations and suggests a spectrum that existing theory (LRH, superposition) does not account for.

## Suggestions

1. **Ablate the convex-hull constraint:** Train a standard BatchTopK SAE (without the convex-hull constraint on D) on the same DINOv2 activations with the same sparsity. Recompute the geometric diagnostics (DDᵀ coherence histogram, singular-value spectrum, antipodal pair counts) and report whether the departures from LRH persist. If they do, the geometric claims are strongly supported; if not, they should be reframed as properties of RA-SAE dictionaries rather than DINOv2's concept space.

2. **Quantify the task-specific findings:** For segmentation, compute the average distance of top-k concept activation maps to ground-truth object boundaries over a sample of the ADE20k validation set. For classification, scan many ImageNet classes and report the fraction for which an "Elsewhere" concept appears in the top-10 task-aligned atoms. For depth, use synthetic images with known depth cues to verify that the three UMAP clusters correspond to distinct physical cues.

3. **Add statistical tests** where the paper uses informal "significance" language (intra-task alignment, coherence differences vs. baselines).

4. **Resolve or explicitly bracket the SAE–MRH tension.** Either discuss whether the SAE dictionary approximates the MRH archetype set, or clarify which analyses rely on the direction-based view and how they would change under MRH.

5. **Mitigate the MRH evidence gap** by testing one concrete prediction (e.g., steering saturation near landmarks) rather than relying on the three preliminary observations alone. Alternatively, reframe MRH more modestly as a speculative proposal with a clear research agenda.

## Score and Decision

This paper makes solid contributions: the largest stable concept dictionary for a vision foundation model, novel task-specific findings (Elsewhere concepts, border detectors, depth cue families), a credible geometric challenge to pure sparse-coding views, and a thought-provoking hypothesis (MRH) grounded in attention's convex-combination mechanism. However, the geometric challenge is weakened by the unablated convex-hull constraint, several task-specific findings lack the quantification needed to fully support their strong claims, and the MRH evidence is preliminary relative to its billing. These are addressable weaknesses that do not invalidate the core contributions. The paper provides genuine value to the community through its analyses, released dictionary, and conceptual framework.

**Overall assessment:** Solid paper with real contributions and addressable weaknesses.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>