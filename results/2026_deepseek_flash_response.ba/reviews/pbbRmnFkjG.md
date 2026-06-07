Now I have sufficient calibration information. Let me compile the final review.

**Initial bracket (Round 1):** The paper sits between 4.5 and 6.5. It's clearly stronger than "What do vision transformers learn?" (4.75, Reject) and "Towards scientific discovery with dictionary learning" (5.60, Reject) but weaker than "Vision Transformers Need Registers" (8.00, Accept) and "Sparse autoencoders reveal selective remapping" (6.50, Accept).

**Narrowing (Round 2):** Comparing against the accepted 6.00 "A Simple Interpretable Transformer" and the accepted 6.50 "SAE remapping" papers: our paper has stronger empirical breadth (3 tasks, geometric diagnostics) but a problematic overclaim in MRH that those papers don't have. The 6.50 paper was accepted despite similar SAE-methodology limitations because it had a cleaner narrative without speculative framing. Our paper is most comparable to the 5.67 "Local vs distributed" paper (Reject) which was also hurt by framing issues. Score: **5.5**.

Let me write the final review.

## Summary of calibrations used

**Round 1 anchors:**
1. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/wZiH43e5Ah.md` (3.00, weak) - concept-based interpretability; our paper is substantially stronger
2. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/fmWVPbRGC4.md` (5.67, middle) - "Local vs distributed representations"; similar framing issues, rejected
3. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2dnO3LLiJ1.md` (8.00, strong) - "Vision Transformers Need Registers"; our paper is substantially weaker

**Round 2 anchors:**
4. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/imT03YXlG2.md` (6.50, Accept) - SAE for CLIP; our paper has similar methodology but weaker framing
5. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/4aJg9e4nvF.md` (4.75, Reject) - ViT visualization; our paper is stronger empirically
6. `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/bkdWThqE6q.md` (6.00, Accept) - Interpretable Transformer; comparable paper with cleaner scope

Now writing the final review:## Summary

This paper trains a stable sparse autoencoder on DINOv2-B to extract a 32,000-concept dictionary—one of the largest such interpretability resources for a vision foundation model. Using this dictionary, it studies how downstream tasks (classification, segmentation, depth estimation) recruit functionally specialized concept subsets, discovering "Elsewhere" concepts (object-dependent off-object signals) for classification, border concept subspaces for segmentation, and three monocular depth cue families for depth estimation. It then characterizes the statistics and geometry of these concepts, finding departures from a purely sparse near-orthogonal coding view. These findings motivate the Minkowski Representation Hypothesis (MRH): token activations lie in Minkowski sums of convex polytopes corresponding to attention heads, with concepts expressed as landmarks/regions rather than linear directions.

## Strengths

- **Large-scale concept dictionary with stable reconstruction.** The paper trains a stable SAE on DINOv2-B producing 32,000 concept atoms with R² > 88% reconstruction fidelity (Section 2), providing an unprecedented-scale resource for analyzing DINOv2's internal representations. The SAE's convex-hull constraint on dictionary atoms is a principled methodological choice addressing reproducibility concerns in prior SAE work.

- **Empirical discovery of functionally specialized concept subsets.** The paper identifies three striking patterns: (1) "Elsewhere" concepts in classification that fire off-object but depend on the object's presence (Section 3, Figure 2); (2) border concepts forming coherent low-dimensional subspaces for segmentation (Figure 2, right; Figure 10); (3) three distinct monocular depth cue families (projective geometry, shadow-based, frequency transitions) for depth estimation (Section 3, Figure 3). These go beyond prior DINO interpretability work in granularity and specificity.

- **Quantitative diagnostics with principled baselines.** Section 4 provides concrete measurements against rigorous baselines: DD^T inner-product distribution compared to random and Grassmannian frames (using the TAAP algorithm), SVD spectrum analysis, Hoyer scores, and co-activation Gram analysis (Figure 4). The finding that the dictionary is more coherent than a Grassmannian optimum and that task-aligned subsets form low-dimensional subspaces is well-supported.

- **Clean demonstration that token geometry is not reducible to position.** Section 5 shows via linear decoders and PCA that per-image token embeddings exhibit smooth, semantically aligned structure that persists after projecting out the positional subspace (Figure 25), ruling out a trivial positional explanation.

## Weaknesses

### Major

1. **MRH is overclaimed relative to its empirical support.** Proposition 1 shows multi-head attention constructively realizes MRH—each head outputs a convex combination and the sum is a Minkowski sum. The paper acknowledges this is "elementary" (line 161). The consequence is that criterion (i) of Definition 1 is guaranteed by the architecture for attention outputs, not an empirical discovery about DINOv2's representations. The three empirical tests supporting MRH (k-NN geodesics, Archetypal Analysis comparison, block structure in code Gram matrices) are described in a single paragraph and entirely deferred to the appendix (Figure 26), with no methodological detail in the main text. For a paper whose title, abstract, and central framing elevate MRH to a co-equal contribution, this level of support is insufficient. The paper would be stronger if MRH were presented as a speculative conceptual observation rather than a major theoretical contribution.

2. **Observed departures from LRH may be confounded with SAE inductive biases.** The SAE uses specific design choices (BatchTopK with k=8, non-negativity, dictionary atoms constrained to the convex hull of activations). These jointly determine what dictionaries can be learned, and the paper does not ablate these choices. The comparison baselines (random, Grassmannian) are mathematically idealized—a Grassmannian frame is the optimal packing for a sparse overcomplete dictionary, so deviation from it under an L2 reconstruction loss with k=8 is unsurprising. Without ablations over k (e.g., k=4, k=16) or SAE variants, it is unclear whether observed geometric patterns reflect DINOv2's intrinsic representation geometry or the specific SAE's solution manifold.

3. **Non-identifiability (Proposition 2) has implications for the paper's own concept dictionary that are not addressed.** The paper proves that Minkowski decompositions are non-unique from final activations alone. This implies that many equally valid factorizations of DINOv2's activations exist, yet the paper's entire analysis in Sections 3 and 4 depends on a particular factorization (the SAE's learned dictionary). The paper acknowledges this and suggests exploiting intermediate signals for future work, but does not discuss what makes the SAE's specific factorization informative rather than merely one of infinitely many. This is a self-referential concern that weakens the claim to have extracted "the" concepts DINOv2 uses.

### Minor

4. **Causal interpretation of "Elsewhere" concepts is partially overstated in the main text.** The main text describes Elsewhere concepts as "indicating a conditional negation" (line 79), but the causal masking evidence is mentioned only in the Figure 2 caption ("evidence suggestive of a causal effect realizing conditional negation (another interpretation being distributed off-object evidence)"). The distinction between correlational and causal evidence should be clearer in the main text, with the alternative interpretation acknowledged in-line.

5. **R² > 88% reconstruction fidelity is reported without variance across runs or data subsamples.** For an interpretability tool whose utility depends on faithful reconstruction, some measure of stability (e.g., variance across seeds or train/test splits) would strengthen confidence.

### Trivial

6. Several empirical observations that would strengthen the in-line argument are deferred to figures in the appendix (Figure 11 for task-specific subspace analysis; Figure 26 for MRH evidence). This makes quantitative support hard to evaluate from the main text alone.

## Nice-to-Haves

- A controlled comparison to LRH representations (e.g., generating activations from a known LRH model and checking whether the same diagnostics produce false positives for "departures") would substantially strengthen the argument that observed patterns are specific to DINOv2.
- Direct comparison of Archetypal Analysis (MRH-like) and SAE (LRH-like) on held-out reconstruction or interpretability would bridge the two halves of the paper more concretely.
- Stating a clear falsification condition for MRH—what empirical observation would show MRH is wrong?—would strengthen it as a scientific hypothesis.

## Removed Points

- **Criticism that MRH "is not a testable hypothesis" in full** — Weakened and retained in modified form. The critic's stronger claim that MRH is "definitional" is partially accurate for criterion (i), but criteria (ii) and (iii) of Definition 1 are empirically testable. The paper does attempt preliminary evidence for them (however insufficiently). The fully vacuous framing was removed.
- **Criticism about the non-identifiability being "structural" and "undermining the entire concept-extraction enterprise"** — Weakened to a minor point because the paper explicitly acknowledges this limitation. Presenting a known limitation of one's approach is intellectual honesty, not a flaw. The critic's framing overstates the damage.
- **Pure formatting/style nitpicks** (title wordplay criticism, generic presentation comments) — Removed per instructions.
- **Criticisms about missing related works** — Removed per instructions (cannot be confirmed from external sources).
- **Criticism about missing appendix details / proofs** — Removed per instructions (parser strips appendix sections from all papers).
- **Stand-alone criticism about missing confidence intervals** — Removed per soft rules: single-run evaluation is standard for large-scale SAE training, though the R² variance point is retained as trivial.
- **Strength Finder claims about "addressing an important problem" or generic writing quality** — Removed as generic/superficial.

## Novel Insights

The harsh critic's observation that MRH is architecturally guaranteed for attention outputs (criterion (i) of Definition 1) is a genuinely insightful critique that goes beyond what the paper acknowledges—it suggests MRH is not a testable hypothesis about DINOv2 specifically, but a description of the transformer architecture that holds for any model. Combined with the non-identifiability result (Proposition 2), this creates a tension: if MRH is both architecturally guaranteed and non-identifiable from activations alone, its value as a framework for interpreting DINOv2's specific learned representations becomes unclear. The paper would benefit from engaging with this tension directly.

## Suggestions

1. Reframe the paper around the empirical findings (Sections 3-5) as the primary contribution, with MRH demoted to a speculative conceptual observation or discussion point. This would eliminate the mismatch between the strength of the evidence and the prominence of the theoretical claim.
2. Add SAE ablations (varying k, varying sparsity targets) to demonstrate robustness of the observed geometric patterns against the specific SAE architecture.
3. Move the MRH empirical evidence (Figure 26 analysis) into the main text with sufficient methodological detail, or acknowledge that this evidence is too preliminary to constitute a central contribution.
4. Address the non-identifiability self-reference directly: if many factorizations are equally valid, what makes the SAE's specific factorization informative, and how should the community interpret dictionaries learned from activations alone?
5. Clarify in the main text that the Elsewhere concept interpretation is predominantly correlational, with suggestive (not definitive) causal evidence.

## Score and Decision

**Comparison anchors used for calibration:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| wZiH43e5Ah.md (Conceptualize Any Network) | 3.00 | R1 | Weaker: narrower scope, fewer findings |
| fmWVPbRGC4.md (Local vs distributed) | 5.67 | R1 | Similar: both have framing issues that hurt an otherwise reasonable submission |
| 2dnO3LLiJ1.md (ViTs Need Registers) | 8.00 | R1 | Stronger: cleaner narrative, fully-supported claims, more impactful |
| imT03YXlG2.md (SAE remapping CLIP) | 6.50 | R2 | Comparable methodology but cleaner framing; our paper has broader empirical scope |
| 4aJg9e4nvF.md (What do ViTs learn?) | 4.75 | R2 | Weaker: shallower analysis, less novel findings |
| bkdWThqE6q.md (Interpretable Transformer) | 6.00 | R2 | Comparable: similar strengths/weaknesses balance but cleaner scope |

**Round 1 bracket:** The paper sits between 4.5 and 6.5 — clearly above the weakest anchors but below the strong ones.

**Round 2 narrowing:** Compared to the accepted 6.50 SAE-remapping paper, our paper has broader empirical contributions but a more problematic theoretical overclaim. Compared to the rejected 5.67 "Local vs distributed" paper, our paper has stronger empirical findings but similar framing issues. The MRH overclaim is the primary factor preventing a higher score.

**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>