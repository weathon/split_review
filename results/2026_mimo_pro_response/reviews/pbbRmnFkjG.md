Now I have enough calibration data. Let me finalize the review.

**Calibration analysis:**

All anchors retrieved across rounds:

| Round | Path | Avg Score | Relevance |
|-------|------|-----------|-----------|
| 1 | nSDOkm0SKo | 1.00 | Financial market NN — not relevant |
| 1 | gwZ90hFSL2 | 1.00 | Humanoid robot NLP — not relevant |
| 1 | 5lUdTogEL3 | 1.00 | Person re-ID — not relevant |
| 1 | P49gSPmrvN | 1.00 | UMAP text analysis — not relevant |
| 1 | tcsZt9ZNKD | 1.75 | Scaling SAEs (actually 8.20 avg) — retrieval error |
| 1 | Wxl0JMgDoU | 2.50 | SAE on chess model — less depth than our paper |
| 1 | 89wVrywsIy | 3.40 | Hierarchical circuit tracing — narrower scope |
| 1 | wZiH43e5Ah | 3.00 | Concept extraction framework — narrower scope |
| 1 | Ch8s4FdUXS | 4.40 | SAE on SDXL Turbo — much narrower, rejected |
| 1 | ghH6YYDs15 | 4.67 | SAE inference theory — different focus |
| 1 | F76bwRSLeK | 4.80 | Original SAE paper for LMs — foundational but limited |
| 1 | J9eKm7j6KD | 4.80 | Control vectors for motion — different domain |
| 1 | imT03YXlG2 | 6.50 | SAE remapping visual concepts — similar scope, narrower |
| 1 | 9ca9eHNrdH | 7.00 | SAEs not canonical — novel techniques, clean message |
| 1 | XAjfjizaKs | 6.50 | Multi-layer SAEs — different focus |
| 1 | 1Njl73JKjB | 7.00 | Principled SAE evaluation — evaluation framework |
| 1 | I4e82CIDxv | 8.00 | Sparse feature circuits — clean, all 8s |
| 1 | 5Ca9sSzuDp | 8.00 | CLIP interpretation — clean decomposition, all 8s |
| 1 | 2dnO3LLiJ1 | 8.00 | ViT registers — foundational DINO work, all 8s |
| 1 | STUGfUz8ob | 7.60 | Abstract reasoning in transformers — different topic |
| 2 | vogtAV1GGL | 5.75 | Concept mechanisms — rejected, weaker empirics |
| 2 | bVTM2QKYuA | 6.75 | Representation geometry + polytopes in LLMs — very relevant |
| 2 | s1zO0YBEF8 | 6.50 | Concept learning dynamics — different focus |
| 2 | d63a4AM4hb | 7.00 | Non-linear features — related to LRH challenges |
| 2 | k9t8dQ30kU | 6.75 | Task structure and geometry — related but different |
| 2 | 4IRYGvyevW | 5.60 | Feature learning geometry — rejected, narrower |
| 2 | cmXWYolrlo | 7.50 | Geometric inductive biases — different focus |
| 2 | GjfIZan5jN | 7.33 | Interpretability and classifiability — related |
| 2 | 3i13Gev2hV | 8.00 | Hyperbolic vision-language — different domain |

**Round 1 bracket:** Between 6.0 and 7.5. The paper's empirical richness (Elsewhere concepts, depth cues, LRH diagnostics) places it above the 5.75-6.50 range, while the MRH overclaiming prevents it from reaching the 7.5-8.0 range where clean, well-supported contributions sit.

**Final calibration:** The most relevant anchor is bVTM2QKYuA (6.75, "Representation Geometry of Features and Hierarchy"), which also proposes polytope representations for concepts and validates them empirically. Our paper has richer empirical content across multiple dimensions (task recruitment, causal interventions, geometric diagnostics) but the theoretical contribution (MRH) is less rigorously validated. This suggests 6.5-7.0.

Given the strong empirical work balanced against the MRH overclaiming, I settle on **6.5**.

---

## Summary
This paper trains a 32,000-concept stable sparse autoencoder (SAE) on DINOv2-B and uses it to study how downstream tasks recruit concepts, analyze the geometric and statistical structure of the concept dictionary, and propose the Minkowski Representation Hypothesis (MRH) — that tokens are sums of convex regions around archetypal landmarks rather than sparse combinations of near-orthogonal directions. The empirical analysis of task-specific concept utilization (Sections 3–5) is the paper's strongest contribution; the MRH framework (Section 6) is presented with formal definitions and propositions but supported only by preliminary empirical evidence deferred to appendices.

## Strengths
- **Causal discovery of "Elsewhere" concepts**: Classification-top concepts fire off-object yet vanish when the object is removed via causal masking (Petsiuk et al. 2018), demonstrating these implement learned negation ("the object exists elsewhere, but this token is not the object") rather than generic background detection (Section 3, Fig. 2 left). This is a genuinely surprising finding with a controlled causal test that goes beyond correlational concept analysis.
- **Monocular depth cue isolation via targeted perturbations**: Controlled perturbations — median blurring, edge-preserving smoothing, high-pass filtering — isolate three functionally distinct cue families (projective, shadow-based, frequency transitions), connecting internal representations to established visual neuroscience categories (Section 3, Fig. 3).
- **Systematic LRH departure diagnostics with proper baselines**: Multiple axes of comparison against random and Grassmannian baselines: heavier-tailed pairwise atom similarities (Fig. 4A), sharp singular-value spectrum decay (Fig. 4B), faster eigenspectrum decay in task-specific sub-dictionaries (Fig. 11 right), and low Hoyer scores confirming distributed atoms (Fig. 4C). Each departure is tested against specific baselines rather than asserted qualitatively.
- **Task-recruitment analysis revealing low-dimensional specialized subspaces**: Expressing linear probes in the concept basis shows intra-task concepts are significantly more aligned than random concepts and their sub-dictionary eigenvalue spectra decay much faster, indicating tasks recruit distinct low-dimensional regions (Section 3, Fig. 11).
- **Per-image PCA analysis distinguishing positional from semantic structure**: PCA projections reveal smooth, semantically aligned structure (Fig. 5); positional information compresses from high-rank to 2D across layers (Fig. 6); projecting tokens orthogonally to the positional subspace preserves PCA organization (Fig. 25), ruling out position as the sole explanation (Section 5).

## Weaknesses

### Fatal
None.

### Major
- **MRH is overclaimed relative to its evidential support**: The paper formalizes MRH with Definition 1, proves Propositions 1–2, derives practical implications for steering, and gives it top billing in the title, abstract, and paper structure. Yet the empirical support consists of three brief observations in a single appendix figure (Fig. 26, lines 163): geodesic interpolation staying near data support, archetypal analysis matching SAE reconstruction with ~10 archetypes, and "clear block structure" in Gram matrices. The paper itself acknowledges this is "preliminary" (lines 35, 177). These observations are consistent with many geometric structures (manifolds, simplicial complexes), not specifically polytope Minkowski sums, and the archetypal analysis comparison lacks detail on SAE baseline configuration. The abstract promises "testable predictions we outline" but the main text does not clearly deliver predictions that distinguish MRH from LRH. The gap between the formal apparatus and its evidential foundation is the paper's most significant structural weakness.

- **Proposition 1 restates known attention mechanics**: The observation that softmax attention computes convex combinations of value vectors and that multi-head attention sums across heads is well-established in the transformer literature. Writing the output as a Minkowski sum of projected head polytopes (lines 155–159) is mathematically correct but adds a name to a known construction without deriving novel testable predictions that distinguish MRH from alternative geometric accounts. The practical steering implications (stop at convergence, line 165) follow from the bounded nature of convex combinations regardless of whether MRH is the right framework.

### Minor
- **No ablation on dictionary size or sparsity**: The choice of c=32,000 atoms and k=8 active codes is not justified or compared against alternatives (line 57). The geometric findings (LRH departures) might be sensitive to the overcompleteness ratio (32,000 for d=768). Reporting reconstruction fidelity and concept recovery as a function of dictionary size and sparsity would strengthen the claim that observed departures reflect genuine geometric properties rather than dictionary miscalibration.
- **Single-model scope**: All results are on DINOv2-B only (line 57). MRH is proposed as a general hypothesis about ViT representations but tested on one model. Testing on at least one additional model (e.g., DINOv2-L or a CLIP ViT) would help assess generality.
- **Alignment score methodology deferred entirely to appendix**: The alignment score connecting linear probes to the concept dictionary (Section 3, line 63) is entirely in Appendix C.1, making it hard to assess whether recruitment patterns could be artifacts of probe methodology.
- **"Simple feature packing" alternative not characterized**: The paper claims geometric effects "are hard to attribute to simple feature packing" (line 109) without showing what feature packing would look like in these diagnostics or how it would differ, making this an assertion rather than a demonstration.

### Trivial
None.

## Nice-to-Haves
- A systematic perturbation study for "Elsewhere" concepts — varying object size, position, identity, and background — would strengthen the "conditional negation" interpretation vs. "distributed off-object evidence."
- The non-identifiability result (Proposition 2, line 167) deserves more careful discussion: if decomposition requires intermediate signals (attention weights, per-head outputs), this limits MRH's practical utility for interpreting final-layer representations.
- A clearer distinction between "MRH as a mathematical description of attention" (trivially true) and "MRH as a hypothesis about representational geometry" (the actual claim) would sharpen the presentation.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Criticism about formatting, typos, or parser artifacts — these are not paper issues.
- Criticism about missing appendix content — the parser strips appendices; they exist in the original submission.
- General sweeps about evaluation rigor without concrete anchors from the harsh critic.
- Suggestions about missing related works — cannot verify external references exist.
- Strengths that are generic ("important topic", "well-motivated area") rather than specific to this paper's evidence.

## Novel Insights
The paper's most genuinely novel empirical finding is the "Elsewhere" concept phenomenon — the discovery that top classification concepts are off-object, conditionally-active detectors that implement learned negation (vanishing under causal masking), rather than being background features. This challenges standard attribution-based interpretability. The monocular depth cue isolation via targeted image perturbations is also a well-designed experiment that bridges internal representation analysis with visual neuroscience. These findings are valuable contributions regardless of whether MRH is ultimately validated.

## Suggestions
- Move MRH empirical evidence (Fig. 26) into the main paper with proper quantification: what dictionary size and sparsity does the AA comparison use? Report block structure in Gram matrices with a quantitative metric against shuffled baselines.
- Articulate at least one concrete, testable prediction that distinguishes MRH from LRH (e.g., under MRH, adding a concept vector should saturate at a polytope boundary; under LRH, it scales linearly).
- Ablate dictionary size (e.g., 8K, 16K, 32K, 64K) and sparsity (k=4, 8, 16) to show geometric findings are robust.
- Test on at least one additional model to assess MRH generality.

## Score and Decision

**Calibration anchors summary:**
- Round 1: imT03YXlG2 (6.50, SAE visual concepts — narrower scope), 9ca9eHNrdH (7.00, SAEs not canonical — cleaner contained contribution), 1Njl73JKjB (7.00, principled SAE eval — evaluation framework), 5Ca9sSzuDp (8.00, CLIP decomposition — clean all-8s paper), I4e82CIDxv (8.00, sparse feature circuits — clean all-8s paper)
- Round 2: bVTM2QKYuA (6.75, representation geometry + polytopes — most relevant anchor, similar polytope theory with cleaner validation), d63a4AM4hb (7.00, non-linear features — related LRH challenges), GjfIZan5jN (7.33, interpretability scoring — related but different)

**Round 1 bracket:** 6.0–7.5

**Final score reasoning:** The paper's empirical contributions (Elsewhere concepts, depth cue isolation, LRH diagnostics) are richer than the 6.50 anchors and comparable to the 6.75–7.00 anchors. However, the MRH overclaiming — formal definitions and propositions for a theoretical contribution supported by only preliminary appendix evidence — is a genuine structural weakness that prevents the paper from reaching the 7.5+ range where well-supported contributions sit. The score of 6.5 reflects strong empirical work with a theoretical contribution that needs strengthening.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>