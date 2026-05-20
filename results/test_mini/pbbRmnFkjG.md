Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 bracket:** After reading the anchors, the paper clearly sits above the 3.3–4.0 band (weak SAE+ViT papers) and below 8.0 (unrelated top-tier papers). The plausible range is **4.5–6.5**.

**Round 2 narrowing:** Comparing against specific anchors:
- Sparse CLIP (5.0): similar ambition but DINOv2 paper is more comprehensive
- Lattice Representation Hypothesis (5.0): structurally similar but DINOv2 has more empirical work
- M-CBM (5.5): comparable quality, DINOv2 is more original but less clean
- On the Limits of SAEs (6.0): more rigorous but narrower scope
- Priors in Time (6.0): cleaner execution on a more focused question

The DINOv2 paper sits around **5.5** — it has genuine empirical contributions and interesting findings, but the dataset confound, thin evidence for key interpretations, and preliminary nature of MRH prevent it from reaching the 6+ tier of cleaner, more rigorous papers.

---

## Summary

This paper trains a stable sparse autoencoder (RA-SAE) on DINOv2-B to extract a 32,000-atom concept dictionary — the largest such interpretability resource for a vision foundation model. Using this dictionary, the authors (1) analyze how downstream tasks (classification, segmentation, depth estimation) recruit task-specific concept families, discovering "Elsewhere" negation concepts, border detectors, and monocular depth cue clusters; (2) characterize the geometry and statistics of the learned dictionary, documenting heavier-tailed pairwise similarities, sharp spectral decay, task-aligned anisotropy, and dense positional signals that go beyond a purely sparse near-orthogonal picture; and (3) propose the Minkowski Representation Hypothesis (MRH), where tokens behave as Minkowski sums of convex polytopes around archetypal landmarks, with a mechanistic link to multi-head attention.

## Strengths

1. **Large-scale, stable concept dictionary.** The RA-SAE with 32,000 atoms achieves R² > 88% reconstruction fidelity on DINOv2-B activations. This represents a substantial empirical resource for understanding what DINOv2 encodes, backed by systematic use of a stable SAE variant (Fel et al., 2025). The release of an interactive visualization is a practical contribution to the community.

2. **Novel qualitative findings about task-specific concept usage.** The identification of "Elsewhere" concepts (off-object activation that depends on the object's presence), border concepts for segmentation, and three families of monocular depth cues (projective, shadow-based, frequency-transition) are genuine observations that could inform future work on vision model interpretability. The controlled perturbation methodology for isolating depth cues (Figure 3) is well-conceived and principled.

3. **Rich geometric characterization of the dictionary.** The analysis in Section 4 documents several nontrivial properties: heavier-tailed pairwise similarities than Grassmannian baselines, sharply decaying singular-value spectrum, antipodal pairs forming signed axes, and low Hoyer scores confirming distributed (non-neuron-aligned) atoms. These observations are carefully grounded in comparisons to appropriate baselines (random, Grassmannian, shuffled).

4. **Theoretical link between attention and Minkowski geometry.** Proposition 1 provides a clean formal demonstration that multi-head attention outputs are Minkowski sums of convex hulls of per-head value sets. While nearly tautological in retrospect, this connection is mathematically precise and provides a mechanistic grounding for thinking about token embeddings as lying in sums of convex regions rather than unbounded linear subspaces.

## Weaknesses

### Major

1. **Cross-task quantitative comparisons are confounded by dataset distribution.** The task analysis uses *different datasets* for each task: classification on ImageNet-1K (object-centric, single-object images), segmentation on ADE20K (scenes with multiple objects), and depth on NYUv2 (indoor scenes). The quantitative comparisons in Figure 11 (dictionary span, intra-task similarity, eigenvalue spectra) therefore conflate task differences with dataset differences. For example, the narrower concept set for depth could simply reflect that indoor scenes are a more restricted visual domain. The paper does not acknowledge this confound, making the central quantitative claim that "classification recruits a broad set while segmentation and depth use more compact subsets" uninterpretable as a statement about tasks per se. This does not invalidate the per-task *qualitative* findings (Elsewhere, border, depth cues), but it substantially weakens the paper's quantitative backbone.

2. **The Minkowski Representation Hypothesis is presented as a core contribution but is not adequately supported.** The MRH receives prominent billing in the abstract and contributions, yet the evidence is thin. Proposition 1 is mathematically correct but nearly tautological (attention outputs convex combinations; summation across heads yields Minkowski sums) — it does not predict the specific form of the representation (e.g., that a *small* number of archetypes suffice) without additional assumptions. The empirical evidence (Figure 26) is preliminary: the geodesic comparison is qualitative, the archetypal analysis comparison is circular given the SAE's own sparsity constraint (k=8), and the Gram matrix block structure is presented without quantification or baseline comparison. The paper's own framing as a "working hypothesis" partially tempers this, but the gap between the MRH's prominence and its evidential basis remains substantial.

### Minor

3. **The "Elsewhere" concept interpretation rests on thin evidence.** The paper interprets a single concept's behavior across a few classes (rabbit, fox, cat) as evidence of "conditional negation" / "object negation." The observation — a concept that fires off-object but disappears when the object is causally masked — is equally consistent with the concept encoding "background texture" or "out-of-focus region" that happens to correlate with object presence. The paper acknowledges alternative interpretations ("another interpretation being distributed off-object evidence") but the core claim in the abstract and contributions ("classification exploits 'Elsewhere' concepts that implement 'object negation'") significantly overstates what a single example pattern can establish. A systematic analysis across many classes with controlled causal experiments (e.g., inpainting vs. adding distractors) would be needed to support this reading.

4. **Departures from the Linear Representation Hypothesis are somewhat overstated relative to the evidence.** The paper documents heavier-tailed pairwise similarities and sharp spectral decay, and interprets these as "challenging a purely sparse, near-orthogonal 'feature packing' account." However, the LRH as articulated in prior work (Elhage et al., Park et al.) does not require strict near-orthogonality in the dictionary basis — it requires that the representation space has *capacity* for many features, which can coexist with clustering or anisotropy. The heavier tails (Figure 4A) involve a small number of atom pairs with higher similarity; the overall distribution is still centered near zero. The task-aligned clusters are induced by probing, and the paper does not show they are intrinsic to the dictionary rather than artifacts of the probing method. These are interesting observations about the learned dictionary's structure, but they do not cleanly contradict LRH.

5. **SAE quality characterization is incomplete.** The paper reports R² > 88% reconstruction fidelity but does not specify whether this is on a held-out test set, how it varies across inputs, or whether the SAE generalizes to out-of-distribution images. Common SAE quality metrics — fraction of dead atoms, monosemanticity, coverage of the activation space — are not reported. While the paper references Fel et al. (2025) for stability, an independent characterization of this specific SAE would strengthen confidence in the downstream analyses.

### Trivial

6. The SAE uses non-negative codes (Z ≥ 0), but the discussion of antipodal signed axes (Section 4) refers to semantic oppositions that would correspond to signed directions. The relationship between the non-negativity constraint and signed semantic axes is not clearly addressed.

7. The depth cue perturbation methodology (median blur, high-pass filtering, edge-preserving smoothing) is described in a single sentence. Additional detail on how these perturbations were designed, validated, and calibrated would improve reproducibility.

## Nice-to-Haves

- Controlling for the dataset confound in task comparisons (e.g., using multi-annotation datasets where the same images support multiple tasks, or at minimum acknowledging and discussing the confound explicitly).
- A more systematic analysis of Elsewhere concepts: across how many classes do they appear, how consistent are the patterns, and can the "conditional negation" interpretation be validated with controlled inpainting vs. distractor experiments?
- Quantitative evaluation of the MRH's block-structure prediction in the code Gram matrix, compared to a suitable null baseline.
- Restructuring the paper to foreground the empirical contributions (SAE dictionary, task-specific analysis, geometric statistics) and present MRH as a shorter discussion/outlook section, better matching the strength of evidence.

## Removed Points

- *Weakness about statistical significance/variance not being reported*: This is a generic criticism. Most interpretive analyses in this space do not report variance, and the paper makes primarily qualitative claims that do not require significance testing.
- *Weakness about missing comparison to other vision foundation models (CLIP, MAE)*: The paper is scoped as a DINOv2 study. Demanding cross-architecture comparison is scope creep.
- *Weakness about no steering experiments being performed*: The paper discusses implications of MRH for steering but does not claim to perform steering experiments. Not a missing experiment but a speculation about implications — removing per instructions.
- *Weakness about figures being too dense*: Purely a formatting sentiment; not affecting technical evaluation.
- *Strength about "non-identifiability result"*: Proposition 2 is well-known in convex geometry (Minkowski sums admit many decompositions). The practical implications for interpretability are noted but the result itself is standard, not novel.
- *Several generic strengths from Strength Finder*: Claims about "important problem" or "addressed important question" — these are generic and apply to most papers. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The "Elsewhere" concept pattern and the connection between attention and Minkowski sums (Proposition 1) are the most novel observations, but both are documented within the paper itself.

## Suggestions

1. **Address the dataset confound** by (a) acknowledging it explicitly, (b) performing a control analysis on a subset of images where multiple task annotations exist (e.g., ImageNet images with segmentation labels or depth maps), and (c) softening or removing the quantitative cross-task comparisons in Figure 11 if the confound cannot be controlled.

2. **Either strengthen the Elsewhere evidence or dial back the claim.** Add systematic measurements across classes, validate the "conditional negation" interpretation with controlled inpainting vs. distractor experiments, or reframe the finding as a qualitative observation (e.g., "we observe a recurring pattern of off-object activation...") rather than a definitive mechanism.

3. **Restructure the MRH presentation.** Given the preliminary evidence, MRH would be more appropriately placed as a shorter discussion/outlook section rather than a main contribution. This would better match the strength of evidence and reduce the perception of overclaiming.

4. **Report basic SAE quality metrics** — fraction of dead atoms, reconstruction held-out R², coverage — to allow readers to assess the reliability of the dictionary.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| tWe5owhOyU (SALVE) | 2.00 | R1 | Much weaker — simpler SAE application, poor evaluation |
| Vk7IDXKgX3 (Lang Models Explain Visual Features) | 3.33 | R1 | Weaker — marginal novelty, unclear methodology |
| BXzUi2QZ7z (Tracing Concept Circuits) | 4.00 | R1 | Weaker — novelty criticized, less comprehensive analysis |
| rxiWsoM6Cx (Sparsity Reveals Strangers) | 4.00 | R1 | Weaker — narrower scope (OOD detection only), less depth |
| DjefrO8TJr (Sparse CLIP) | 5.00 | R1 | **Comparable** — clean execution but narrower scope; DINOv2 paper is more ambitious with more qualitative depth |
| C7M6F0OJ1l (Hierarchical Semantics in SAEs) | 4.40 | R1 | Weaker — proposed architecture has limited validation |
| 5K1FG92m5s (Lattice Representation Hypothesis) | 5.00 | R2 | **Comparable** — structurally similar (proposes new representation hypothesis); lattice paper is more rigorous on theory, DINOv2 paper has more extensive empirical work |
| gdEWoxhb70 (M-CBM) | 5.50 | R1 | **Slightly weaker** — cleaner pipeline but incremental combination of SAE+CBM; DINOv2 paper is more original |
| DSOTgzeH3w (Limits of SAEs) | 6.00 | R2 | **Stronger** — rigorous theoretical contribution with well-controlled experiments; DINOv2 paper is broader but less rigorous |
| 4J2e3nWiC8 (Priors in Time) | 6.00 | R2 | **Stronger** — focused, well-executed with clear novel architecture and clean empirical demonstration |
| NHP2Y8IVMU (Interpretable Visual Prompt Tuning) | 5.50 | R2 | **Comparable** — clean method paper with good evaluation; DINOv2 paper has more exploratory depth |

**Round 1 bracket:** 4.5–6.5 (above the weak SAE+ViT papers at 3.3–4.0, below the unrelated top-tier 8.0 papers).

**Round 2 narrowing:** The paper lands between the 5.0 band (Sparse CLIP, Lattice Hypothesis) and the 6.0 band (Limits of SAEs, Priors in Time). It is more original and comprehensive than the 5.0 papers but less rigorous and focused than the 6.0 papers. The dataset confound and overstated Elsewhere/MRH claims prevent it from reaching the cleaner 6.0 level.

**Final score: 5.5** — A paper with genuine empirical contributions (large-scale SAE resource, interesting qualitative findings) but held back by a significant dataset confound in the quantitative comparisons, thin support for key interpretations, and a new hypothesis whose prominence exceeds its evidential basis. With revisions addressing the confound and recalibrating the claims, the empirical core could be a solid contribution.

<score>5.5</score>
<decision>Accept</decision>