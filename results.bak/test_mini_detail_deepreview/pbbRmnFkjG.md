Now I have a comprehensive picture of the paper and the calibration landscape. Let me write the final consolidated review.

**Calibration Summary:**

**Round 1 — Bracketing:**
- Low band (<3.5): Papers at 1.67–3.40 — mostly SAE papers with fundamental flaws or minimal contributions. The current paper is clearly far above these.
- Middle band (3.5–7.5): Anchors at 4.40 (SDXL SAE), 4.67 (SAE theory), 4.80 (LLM SAE), 6.50 (CLIP SAE). The current paper is stronger than the 4.40–4.80 papers and comparable to the 6.50 CLIP SAE paper, which it exceeds in novelty of findings.
- High band (>7.5): Anchors at 8.0–8.20 — papers with clean, well-supported contributions. The current paper's MRH evidence is too preliminary to place it in this band.

**Round 2 — Narrowing:**
- The LLM geometry paper (6.75) is the closest topical match (representation geometry, polytopes). That paper has stronger mathematical rigor but narrower scope (unembedding layer only, WordNet). The current paper has broader empirical scope but weaker support for its central theoretical claim. Comparable overall.
- The Interpretable Transformer paper (6.00) has a clean method but limited novelty. The current paper has more ambition and empirical depth.
- The ViT visual exploration paper (4.75) applies existing methods with limited novelty. The current paper is clearly stronger.

**Final bracket**: The paper sits between 5.5 and 6.5, and I anchor it at **6.0** — a solid Accept that recognizes genuine empirical contributions while being honest about the preliminary nature of the MRH evidence.

---

## Summary

This paper trains a stable sparse autoencoder (RA-SAE) on DINOv2-B activations to produce a 32,000-concept dictionary — the largest such interpretability resource for a vision foundation model. Using this dictionary, the paper (1) analyzes how three downstream tasks (classification, segmentation, depth estimation) recruit different concept subspaces, discovering "Elsewhere" concepts, border-specific detectors, and three families of monocular depth cues; (2) characterizes the geometry and statistics of the concept space, finding departures from the near-orthogonal ideal of the Linear Representation Hypothesis; and (3) proposes the Minkowski Representation Hypothesis (MRH) as a formal alternative where token embeddings lie in Minkowski sums of convex polytopes from attention heads. The MRH is grounded in the architecture of multi-head attention (Proposition 1) and supported by preliminary empirical signals.

## Strengths

1. **Large-scale, stable SAE dictionary as a community resource.** The paper operationalizes the LRH at an unprecedented scale for vision: 32,000 atoms with R² > 88% reconstruction fidelity, trained with a convex-hull constraint that guarantees in-distribution atoms. The interactive demo (to be released upon acceptance) will enable the community to explore DINOv2's internal concepts directly — a valuable contribution regardless of theoretical framing.

2. **Genuinely novel task-specific findings.** The "Elsewhere" concept (off-object activations that depend on the object's presence, verified via causal masking) is a non-obvious discovery about how DINOv2 supports classification. The finding that segmentation top-50 concepts consistently localize to object boundaries and form a coherent low-dimensional subspace, and the identification of three distinct monocular depth cue families (projective, shadow-based, frequency transitions) via controlled perturbation experiments, are concrete interpretability results that stand on their own.

3. **Formal architectural grounding of MRH.** Proposition 1 is a clean theoretical result showing that multi-head attention *realizes* Minkowski-sum structure: each head outputs a convex combination of its values, and summing across heads yields exactly a Minkowski sum of convex polytopes. This connects an intuitive geometric picture (concepts as proximity to landmarks) to actual transformer computations.

4. **Clean positional analysis.** The demonstration that the positional subspace compresses to a 2D sheet in final layers, and that projecting orthogonally to it leaves PCA structure largely unchanged (Figure 25), convincingly separates positional from semantic content and supports the interpolative-geometry narrative.

## Weaknesses

### Major

1. **Domain mismatch in task-specific analysis is unaddressed.** The SAE dictionary is trained on ImageNet-1K activations but used to analyze concept recruitment for segmentation (ADE20K) and depth (NYU Depth). The paper does not report reconstruction fidelity on these out-of-distribution datasets, nor does it control for the possibility that the observed task-specific subsets reflect distribution shift (which concepts happen to activate on ADE20K/NYU-like images) rather than functional specialization for the task. This does not invalidate the findings — linear probes for these tasks are trained on the respective datasets and may adapt — but it weakens the claim that the observed concept subsets are truly task-specific rather than dataset-driven. The paper should report R² on ADE20K and NYU tokens, or acknowledge this as a caveat.

2. **Geometry analysis lacks quantitative precision.** The claim that the dictionary is "more coherent than random or Grassmannian baselines" relies on qualitative visual comparisons (Figure 4, density plots of DD^T inner products). No specific thresholds are reported (e.g., fraction of atom pairs with absolute cosine > 0.3, > 0.5), no error bars or confidence intervals are given, and the number of trials for the random baselines is unspecified. The singular value spectrum comparison is similarly impressionistic. A learned dictionary adapting to data will naturally be more coherent than a random set — the key question is whether the *degree* of departure from near-orthogonality is meaningful. Quantifying this would sharpen the argument that LRH is meaningfully violated.

3. **Empirical evidence for MRH is preliminary and does not discriminate against alternatives.** The three empirical tests (straight-line vs. k-NN geodesics, AA vs. SAE reconstruction, Gram block structure) are consistent with MRH but also with many other geometric accounts (e.g., low-rank subspace with local nonlinearities, or nonlinear manifold models). No direct test is performed — for instance, verifying that token embeddings actually lie in a Minkowski sum of explicit head polytopes, or that the convex-hull structure of per-head outputs is non-trivial. The paper is reasonably transparent about this ("preliminary empirical signals"), but MRH is given billing equal to the empirical contributions in the title and framing.

### Minor

4. **Co-activation/geometry correlation analysis has a potential confound.** The paper notes that the correlation between Z^T Z and DD^T is "roughly proportional to the trace of activation covariance" which "may be an intrinsic property of linear reconstructive methods" (footnote 1). This is a reasonable caveat but it undermines the claim that "concept co-occurrence only weakly shapes geometry" — the weak correlation could be an artifact of the measurement, not a genuine finding.

5. **Causal interpretation of the Elsewhere concept is over-claimed.** The paper states these concepts "implement conditional negation" but also acknowledges "another interpretation being distributed off-object evidence." The causal masking test (Petsiuk et al. 2018) shows correlation with object presence, not a causal implementational role. The language is appropriate in the figure caption but the main text ("implementing object negation") is stronger than the evidence supports.

### Trivial

6. The paper states the interactive demo "will be publicly released upon acceptance" but it is not available for reviewers to verify. This is acceptable for review but should be released promptly upon acceptance to support the claim of being "the largest interactive interpretability demo for a vision foundation model."

## Nice-to-Haves

- A direct test of whether per-head outputs actually lie in convex hulls of their value vectors (e.g., by extracting per-head attention-weighted values and checking convexity empirically) would substantially strengthen the MRH claim. The theory says it *can* realize MRH; showing that it *does* in practice would be more convincing.
- Human validation of the monocular depth cue clustering (e.g., via a labeling study) would strengthen the claim that these correspond to genuine perceptual cue families.
- Error bars or statistical tests on the geometry comparisons (coherence, spectral decay) would improve rigor.

## Removed Points

- **MRH as a "central contribution that is not supported"** (from harsh critic): The paper explicitly frames MRH as "a working hypothesis" with "preliminary empirical signals" (abstract, Sec. 7). While MRH is prominently featured, the paper is transparent about its preliminary nature. The critic's characterization overstates the gap between claim and evidence.
- **Reproducibility concerns about missing appendix content** (harsh critic section "Missing Parts and Places to Improve"): The parser strips appendices from all papers; these details exist in the original submission.
- **"No direct test is performed" for MRH** — softened from Fatal to Major because the paper acknowledges the preliminary nature of the evidence and the critic's specific "direct test" suggestions (per-head polytope verification) are properly scope for future work.
- **"The narrative arc from LRH to MRH is not well supported"** — this is more a framing preference than a verifiable weakness. The paper's three-part structure (LRH operationalization → departures → alternative proposal) is coherent; whether one is convinced by the transition is a judgment call, not a flaw in the paper.
- **"Data geometry analysis confound" about Z^T Z and DD^T** — The paper already acknowledges this potential confound in footnote 1.
- **Generic strengths from Strength Finder** (e.g., "addresses an important problem", "largest interpretability demo") — kept only where specifically evidenced.

## Novel Insights

None beyond the paper's own contributions. The novel synthesis is the observation that the empirical departures from LRH (task-clustered concepts, dense positional features, higher coherence) naturally motivate a geometric picture where tokens are sums of convex regions rather than points on a near-orthogonal frame. This synthesis, while preliminary, connects the dots between SAE-based interpretability and the architectural structure of attention in a way that has not been drawn before for vision transformers.

## Suggestions

1. Report SAE reconstruction fidelity (R²) on ADE20K and NYU Depth tokens to address the domain mismatch concern. If fidelity is acceptable, the task-specific analysis is strengthened; if not, the limitation should be discussed.
2. Add quantitative thresholds to the geometry analysis: e.g., the fraction of atom pairs with |cos θ| > 0.2/0.3/0.5, compared against baselines with error bars. Report the number of trials and how baselines are constructed.
3. Reframe MRH as a concluding outlook/future direction rather than a co-equal contribution with the empirical findings, OR add stronger empirical evidence (e.g., checking whether per-head outputs are indeed in the convex hull of that head's value vectors).

## Score and Decision

**Score bracket reasoning**: Round 1 bracketing placed the paper well above the low band (<3.5, papers with fatal flaws) and clearly below the top band (>7.5, papers with clean, complete contributions). Round 2 narrowing compared the paper against the LLM geometry paper (6.75) and the CLIP SAE paper (6.50) — both accepted papers with comparable scope-to-evidence balance. The current paper has more novel empirical findings than the CLIP SAE paper but a weaker central theoretical claim than the LLM geometry paper. On balance it is comparable to these anchors, placing it at **6.0**.

**Calibration anchors retrieved** (all rounds, listed with avg score):
- *Wxl0JMgDoU* (2.50) — Chess SAE, narrow scope, weak. Below current paper.
- *wZiH43e5Ah* (3.00) — Concept extraction, limited novelty. Below current paper.
- *89wVrywsIy* (3.40) — SAE circuit tracing, limited scope. Below current paper.
- *UbLvSPMvMA* (1.67) — Cosine loss for sparse binary, flawed. Well below current paper.
- *imT03YXlG2* (6.50) — CLIP SAE, concepts reused in adaptation. Comparable ambition, similar weaknesses (domain shift, limited novelty critique). Current paper has more novel task-specific findings.
- *Ch8s4FdUXS* (4.40) — SDXL SAE, too narrow scope. Below current paper.
- *ghH6YYDs15* (4.67) — SAE theory, no empirical contribution. Below current paper.
- *F76bwRSLeK* (4.80) — LLM SAE interpretability. Below current paper.
- *tcsZt9ZNKD* (8.20) — Scaling SAEs, clean scaling laws. Above current paper in rigor.
- *2dnO3LLiJ1* (8.00) — Vision Transformers Need Registers, clean contribution. Above.
- *I4e82CIDxv* (8.00) — Sparse Feature Circuits, clean methodology. Above.
- *5Ca9sSzuDp* (8.00) — CLIP decomposition, clean analysis. Above.
- *vogtAV1GGL* (5.75) — Concept representation theory. Below current paper (theory-only, no experiments).
- *bVTM2QKYuA* (6.75) — LLM representation geometry. Comparable, stronger theory but narrower scope.
- *BpyHIrpUOL* (6.00) — Polyhedron representation learning. Different topic, similar score tier.
- *DZxU0q2S11* (5.75) — Data geometry bounds. Below current paper.
- *4aJg9e4nvF* (4.75) — ViT visual exploration. Below current paper.
- *bkdWThqE6q* (6.00) — Interpretable transformer. Similar score, different contribution type.
- *bSq0XGS3kW* (5.00) — Object-centric transfer. Below current paper.
- *J9eKm7j6KD* (4.80) — Motion control vectors. Below current paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>