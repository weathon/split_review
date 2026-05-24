Now I have strong calibration. Let me write the consolidated review.

## Summary
This paper trains a stable sparse autoencoder on DINOv2 to extract a 32,000-concept dictionary, then analyzes how downstream tasks (classification, segmentation, depth estimation) recruit these concepts, revealing functional specialization. It documents geometric departures from the sparse, near-orthogonal ideal of the Linear Representation Hypothesis (higher coherence, sharp spectral decay, dense positional signals), and proposes the Minkowski Representation Hypothesis (MRH)—that token embeddings are Minkowski sums of convex polytopes from each attention head—supported by theoretical propositions and preliminary empirical tests. The concept dictionary and interactive demo constitute a substantial resource for the interpretability community.

## Strengths

- **Large-scale concept extraction with a stable SAE on DINOv2.** The paper presents a 32,000-atom dictionary trained with a convex-hull-constrained (RA-SAE) that achieves R² > 88% reconstruction, and the accompanying interactive demo (to be released) sets a new scale for concept-based interpretability in vision models. The stability properties of RA-SAE are a genuine methodological improvement over naive SAEs.

- **Quantitative characterization of departures from the Linear Representation Hypothesis.** The dictionary coherence analysis (heavier-tailed inner products vs. random and Grassmannian baselines, Figure 4 bottom), sharp singular-value decay of D, and low Hoyer scores are properly benchmarked and provide concrete evidence that DINOv2's representation deviates from a purely sparse, near-orthogonal picture. This is the paper's best-supported finding and directly motivates the search for alternative geometric accounts.

- **Interesting qualitative discoveries of task-specific concept families.** The identification of "Elsewhere" concepts for classification (off-object activations that disappear under causal masking), border concepts for segmentation, and three families of monocular depth cues (projective, shadow, frequency) via controlled perturbations are genuinely intriguing and open new directions for vision interpretability research. The perturbation-based depth cue analysis (Figure 3) is methodologically creative.

- **Positional encoding analysis clarifies token geometry.** The careful analysis showing that (a) the positional subspace compresses to a 2D sheet in later layers, (b) positional directions appear only in intermediate PCA components, and (c) projecting tokens orthogonal to the positional subspace leaves PCA structure intact (Figure 25) convincingly demonstrates that the smooth token geometry is not merely a positional artifact.

## Weaknesses

### Major

- **The Minkowski Representation Hypothesis is overclaimed relative to the evidence provided.** The abstract states that "Multi-head attention directly implements this construction," but Proposition 1 only shows that attention *can* produce Minkowski-sum structure—it does not establish that the trained network *actually* factors its representations into semantically meaningful polytopes. The empirical tests (geodesic interpolation, Archetypal Analysis, Gram block structure) are all applied to final token embeddings, not to per-head outputs; they are consistent with MRH but also with other compositional geometries (e.g., sparse coding with non-negative weights). Moreover, condition (ii) of Definition 1 requires |S| << m (only a few tiles active), yet in the multi-head construction m = H (typically 12 or 16) and all heads contribute, violating the claimed sparsity condition without additional mechanisms that are not studied. The paper would be better served by framing MRH as a "theoretically possible and partially consistent" hypothesis rather than a demonstrated property.

- **Contradictory characterizations of code Gram structure.** Section 4 states that the Gram matrix ZᵀZ "has a spectrum that decays smoothly, with no gaps or dominant modes, providing little evidence for modular low-rank structure." Section 6 then claims that "the Grams of the codes … observe clear block structure … suggesting tiles effect." These statements appear to describe the same object and directly contradict one another. The paper does not clarify whether the two analyses use different code representations (e.g., SAE codes vs. AA codes), different normalization, or different matrix orderings. This unresolved inconsistency undermines the reliability of the MRH evidence and must be addressed.

- **Key task-specific findings rely on qualitative evidence without aggregate quantification.** The "Elsewhere" concept's causal role is supported by causal masking of a single example (rabbit). The claim that "all the concepts among the top-50 consistently localize along object contours" for segmentation is backed only by qualitative examples. The depth cue cluster labeling via UMAP is manual and subjective. Given that the paper makes strong functional claims (learned negation, dedicated boundary-detection subspaces), aggregate quantitative support is needed—e.g., fraction of ImageNet classes with an Elsewhere concept, Dice overlap between top concept activation maps and ground-truth boundaries on ADE20K, or inter-rater reliability for depth cue classification. Until provided, these findings are intriguing anecdotes rather than validated discoveries.

### Minor

- **Selection bias in the task-specific intra-group similarity analysis.** The paper isolates the top-100 most task-aligned concepts and shows they have higher intra-group similarity than random subsets. This mechanically follows from extreme-value selection (top-100 of 32,000 will regress toward higher similarity regardless of geometry). The analysis should compare against random subsets matched on firing frequency, norm, or other statistics to confirm that the effect is not a statistical artifact.

- **Incomplete baseline for dictionary coherence.** The paper compares D's coherence to random and Grassmannian baselines but does not compare to the coherence of the original activation space A itself. Showing that D's coherence exceeds that of A would strengthen the argument that the departure from orthogonality is due to learned structure rather than inherited data anisotropy.

- **SAE reconstruction fidelity not broken down by token type.** The paper reports R² > 88% overall but does not analyze reconstruction fidelity per token type (CLS vs. patch vs. register) or per image region. Since the dictionary is used for all downstream analysis, understanding whether certain tokens are systematically harder to reconstruct would inform the reliability of concept attributions.

- **Statistical significance absent from geometric comparisons.** The coherence, singular-value decay, and Hoyer-score plots are presented without error bars or confidence intervals. Variance over multiple random baseline draws would help assess how systematic the reported departures are.

### Trivial
- Figure references in the main text (e.g., Figure 11, Figure 26) point to appendix figures not visible in the main submission, making it hard to follow the argument without flipping to the appendix.

## Nice-to-Haves
- **Head-level empirical tests of MRH.** Directly analyzing whether per-head outputs are convex combinations of a small number of value vectors (e.g., via Archetypal Analysis on per-head outputs) would constitute stronger evidence for MRH than token-level tests that are consistent with many geometries.
- **Ablation of the convex-hull constraint.** Comparing the RA-SAE dictionary to an unconstrained SAE (even at smaller scale) would clarify whether the observed geometric properties (heavier tails, sharp spectral decay) are intrinsic to DINOv2's representation or artifacts of the RA-SAE constraint.
- **Limitations section.** The paper lacks a dedicated limitations section. Given the preliminary and speculative nature of MRH in particular, an honest discussion of what is not yet established would strengthen the paper.

## Removed Points
These points were flagged for removal; treat them with caution:
- Criticisms about the interactive demo not being publicly available yet ("no link or preview of the demo is provided beyond a mention of future release") — removed per hard rules: "REMOVE any criticism that questions the existence, release status, or availability of any model, tool, benchmark, dataset, or reference cited in the paper."
- The claim that missing related works is a weakness — removed per hard rules: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."
- Suggestions that proofs or appendices are missing — removed per hard rules about parser-stripped sections.
- Strength Finder claims that the MRH empirical tests "provide initial empirical support, linking interpretable geometry to architectural structure" — this strength conflicts with verified weaknesses showing the MRH evidence is thin and the Gram matrix evidence is contradictory; per rules, "when a strength and weakness disagree, the weakness wins."
- Strength Finder claim that the paper provides "systematic quantification of task-specific concept recruitment" — overstated given the selection bias issue and qualitative nature of core findings.
- The harsh critic's point about "Proposition 2 is a known property" — this is a generic criticism that applies to many theoretical contributions; Proposition 2's value is in applying the known property to representation analysis, not in proving a new mathematical result.

## Novel Insights
The most novel observation emerging from the review process is that the paper contains two papers of different quality: (a) a well-executed empirical phenomenology of DINOv2's concept dictionary (task-specific subspaces, geometric statistics, positional analysis), and (b) a speculative theoretical proposal (MRH) that is much less supported. The link between (a) and (b) is the weakest part of the paper. The empirical evidence for departures from LRH is genuinely valuable and stands on its own—it would motivate alternative geometric accounts even without the specific MRH framing. The MRH, as presented, is a thought-provoking hypothesis whose strongest support is the theoretical Proposition 1 (attention can realize it) rather than the empirical tests, which are too generic to distinguish MRH from competing compositional geometries.

## Suggestions
1. **Resolve the Gram matrix inconsistency** by explicitly clarifying which code representations are used in each analysis (Section 4 vs. Section 6) and what the different diagnostics reveal. If the two analyses refer to different objects (SAE codes vs. AA codes), say so directly.
2. **Tone down the MRH framing.** Replace "directly implements" with "can realize" or "is consistent with." Acknowledge that the empirical evidence for MRH is preliminary and that alternative geometries (sparse coding with non-negative weights, for instance) are also consistent with the data.
3. **Add quantitative support for Elsewhere and border concepts.** Report aggregate statistics: percentage of ImageNet classes with a top-activated Elsewhere concept, Dice overlap between top-50 border concept activations and ground-truth boundaries on ADE20K.
4. **Add a matched-baseline for task-specific similarity.** Compare top-100 task-aligned concepts against random subsets matched on firing frequency and norm to control for selection artifacts.
5. **Add a dedicated limitations section** discussing what MRH does and does not establish, and what further experiments would be needed to confirm it.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Wxl0JMgDoU (SAE chess) | 2.50 | R1 bracketing (weak) | Much weaker — thin contribution, no concept analysis |
| 89wVrywsIy (Hierarchical tracing) | 3.40 | R1 bracketing (weak) | Weaker — narrower scope, less empirical depth |
| UbLvSPMvMA (Cosine loss SAE) | 1.67 | R1 bracketing (weak) | Much weaker — purely methodological, no model analysis |
| imT03YXlG2 (CLIP SAE remapping) | 6.50 | R1 bracketing (middle) | Stronger — cleaner experiments, better supported claims |
| ghH6YYDs15 (Compute optimal SAE) | 4.67 | R1 bracketing (middle) | Weaker — theoretical, less empirical breadth |
| 1Njl73JKjB (Principled SAE eval) | 7.00 | R1 bracketing (middle) | Stronger — rigorous evaluation framework |
| bVTM2QKYuA (Representation Geometry LLM) | 6.75 | R2 narrowing | Stronger — tighter theory-empirical link, clearer claims |
| k9t8dQ30kU (Task structure & nonlinearity) | 6.75 | R2 narrowing | Stronger — well-focused, clean experiments |
| bkdWThqE6q (Interpretable Transformer) | 6.00 | R2 narrowing | Comparable in quality but less ambitious scope |
| 5iENGLEJKG (INViTE) | 5.25 | R2 narrowing | Similar — interesting findings but qualitative weaknesses |

**Round 1 bracket:** 4.5–6.5 (above the rejected 1.67–3.4 range, below the 6.5–7.0 clean accept range)

**Round 2 narrowing:** The paper sits above INViTE (5.25) due to broader scope and stronger geometric analysis, but below the 6.0–6.75 anchors due to the overclaimed MRH, unresolved Gram inconsistency, and qualitative nature of key findings. The paper is not as polished as the 6.0 anchors but has more ambitious scope and interesting discoveries.

**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>