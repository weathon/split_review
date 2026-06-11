Now I have a clear calibration picture. Let me finalize the review.

**Bracket from Round 1:** 4.0–6.5

**Narrowing from Round 2:** The paper sits between F76bwRSLeK (4.80, foundational SAE paper, accepted but with significant limitations) and bVTM2QKYuA (6.75, rigorous polytope-based geometric hypothesis with strong formalization and validation). The current paper has more empirical breadth than F76bwRSLeK but the MRH component is substantially weaker than bVTM2QKYuA's theoretical contribution. The paper lands at approximately **5.0** — solid empirical work undermined by an overclaimed and under-supported headline contribution.

---

## Summary
This paper trains a stable sparse autoencoder (RA-SAE) on DINOv2-B to extract a 32,000-concept dictionary, then analyzes which concepts are recruited by classification, segmentation, and depth estimation. It characterizes the statistical and geometric properties of the concept dictionary, finding departures from the Linear Representation Hypothesis (LRH), and proposes the Minkowski Representation Hypothesis (MRH) — the view that token embeddings lie in Minkowski sums of convex polytopes spanned by archetypal landmarks, a geometry naturally realized by multi-head attention.

## Strengths
- **Scale and specificity of the SAE operationalization**: The paper extracts a 32,000-concept dictionary from DINOv2-B with explicit parameterization (D = SC with S row-stochastic over 128,000 k-means centroids, k=8 active codes per token), achieving R² > 88% reconstruction fidelity (Section 2, line 57). This is a concrete, well-specified artifact enabling the downstream analyses.
- **Causal perturbation evidence for "Elsewhere" concepts**: Section 3 (lines 79-80, Figure 2) demonstrates that classification-recruited "Elsewhere" concepts fire off-object yet disappear when the object is removed via causal masking (Petsiuk et al., 2018). This provides causal — not merely correlational — evidence for a conditional mechanism.
- **Controlled-perturbation methodology for depth cues**: Section 3 (lines 83-93, Figure 3) uses targeted image-space perturbations (median blurring, edge-preserving smoothing, high-pass filtering) to isolate specific monocular depth cues and maps concept activation changes via UMAP, revealing three interpretable families (projective, shadow-based, frequency transitions). This perturbation-to-concept mapping is methodologically sound and the paper's most original empirical contribution.
- **Per-image PCA analysis ruling out pure positional explanation**: Section 5 (lines 119-135, Figures 5-6, 25) shows that per-image token PCA reveals smooth, semantically aligned structure that persists after orthogonal projection onto the positional subspace, and that positional decoders collapse to 2D in late layers. This provides direct evidence that token geometry encodes more than spatial location.
- **Systematic comparison against Grassmannian baselines**: Section 4 (Figure 4) compares the learned dictionary D against both random and Grassmannian frame baselines for coherence, spectral decay, and Hoyer sparsity. Finding heavier-tailed inner products and sharper singular value decay than baselines provides quantitative grounding for claims about departure from LRH.
- **Triangulation across task-level, statistical, and geometric evidence**: The paper builds its case through task-specialization patterns (Section 3), dictionary-level statistics (Section 4), and token-level geometry (Section 5). The convergence across these independent lenses strengthens the overall characterization.

## Weaknesses

### Fatal
None.

### Major
- **MRH empirical evidence is thin and does not distinguish the hypothesis from alternatives**: The Minkowski Representation Hypothesis occupies the title, abstract framing, and Section 6, yet the empirical support is confined to a single composite figure (Figure 26) described in approximately three sentences (lines 163-164): k-NN geodesics, Archetypal Analysis comparison, and block structure in code Grams. None of these tests are quantified, benchmarked against alternative geometric models, or subjected to statistical rigor. All three would be consistent with many geometric models beyond MRH (e.g., any curved manifold would show geodesic advantage, any low-rank model would show Archetypal Analysis matching SAE, any clustered representation would show block structure). The paper acknowledges MRH is a "working hypothesis," which is honest, but the evidence presented does not rise to the level expected for a paper's headline contribution.
- **Logical gap between empirical observations and the MRH proposal**: Sections 4 and 5 observe departures from LRH (higher coherence, anisotropic spectra, smooth token manifolds) and Section 6 proposes MRH, but the paper does not articulate why MRH is the *right* alternative rather than merely *one possible* alternative. Higher-than-Grassmannian coherence, anisotropic spectra, and smooth per-image token manifolds are compatible with many geometric models (union of subspaces, product manifolds, simple low-rank structure with noise). The paper acknowledges this gap implicitly (line 141: "This view is motivated by our observations above") but never fills it.
- **Proposition 1 is a restatement of attention mechanics, not a discovery**: The proof that multi-head attention realizes MRH (Section 6, lines 155-159) essentially observes that softmax produces convex combinations and head outputs are summed — basic properties of the attention mechanism. The non-trivial question is whether the model actually *learns* to use this capacity, not whether the architecture *can* realize it. The paper presents this as a theoretical result but it adds no new insight.

### Minor
- **SAE layer is not specified**: The paper applies the SAE to "DINOv2-B with 4 registers" (line 57) but never states which transformer layer's activations are factorized. DINOv2-B has 12 layers. While the dimensions (d=768, t=261) are consistent with the final layer output, the choice affects reproducibility and the generality of findings across layers.
- **Dictionary transfer across datasets is not validated**: The SAE dictionary is trained on 1.4M ImageNet-1K images and then used to analyze concept recruitment for segmentation (ADE20K) and depth estimation (NYU Depth v2). The paper provides no analysis of whether reconstruction fidelity degrades on these out-of-distribution datasets.
- **"Elsewhere" concept interpretation as "negation" is not uniquely supported**: The paper frames "Elsewhere" concepts as implementing "learned negation" (line 79), but the evidence — that these concepts fire off-object and disappear when the object is masked — is consistent with several mechanisms (figure-ground separation, contextual modulation, distributed off-object evidence). The paper acknowledges this ambiguity in Figure 2's caption but treats "negation" as the primary framing in the main text.

### Trivial
- **"per-head" in Section 3 likely means "per-task"**: Line 65 states "top 100 most task-aligned concepts per-head" in the context of task-specific concept analysis. Since the SAE dictionary analysis does not involve attention heads, this appears to be a wording error.

## Nice-to-Haves
- Quantitative values for key claims (cosine similarities, spectral decay rates, effect sizes) currently deferred to figures should appear in the main text.
- SAE stability analysis across seeds or hyperparameter choices would strengthen confidence in the reported findings.
- The depth cue perturbation experiment could be expanded into the centerpiece of the paper, as it is the most original empirical contribution.
- If MRH is kept as a contribution, develop quantitative tests that distinguish it from alternative geometric models (union of subspaces, product manifolds, etc.) rather than relying on three qualitative observations in one composite figure.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **(Harsh Critic) Alignment score definition missing from Appendix C.1**: The parser strips appendices from all papers; the definition exists in the original submission. Removed per hard rule about missing appendix.
- **(Harsh Critic) "Figure 11 is referenced extensively but quantitative values are not reported in the text"**: This is a presentation preference, not a methodological flaw. Demoted to Nice-to-Have.
- **(Harsh Critic) "The paper's LRH is a strawman"**: The paper operationalizes a specific, well-defined version of LRH (near-orthogonal Grassmannian frames) and finds departures. Whether this is the "right" version of LRH to target is a matter of framing, not a factual error. The paper's characterization is defensible.
- **(Harsh Critic) "Proposition 2 undercuts the practical utility"**: Proposition 2 is presented as a limitation that the paper acknowledges and discusses (lines 167-173: "exploiting intermediate signals... may render the factorization tractable"). The paper is honest about this limitation.
- **(Strength Finder) Proposition 1 as a core strength**: While mathematically correct, presenting the observation that attention computes convex combinations and sums them as a theoretical discovery is an overstatement. This observation is demoted from a strength; it is noted instead alongside the weakness about MRH evidence.
- **(Strength Finder) "Identification of antipodal pairs as signed semantic axes"**: This is a minor observation (one sentence in the paper, line 34 in the original numbering) rather than a significant contribution.

## Novel Insights
The depth cue perturbation methodology is the most genuinely novel empirical technique in the paper, providing a principled way to causally link input features to internal concept representations. The "Elsewhere" concept finding — that classification concepts fire off-object in a causally dependent manner — is surprising, though the paper's "negation" interpretation remains one of several plausible explanations.

## Suggestions
- Commit to either: (a) making the empirical characterization of DINOv2's concept geometry the central contribution (with MRH as a forward-looking discussion point), or (b) developing rigorous, quantitative tests that distinguish MRH from alternative geometric models. In its current form the paper spreads itself too thin across both goals and delivers neither with sufficient depth.
- Report reconstruction fidelity on ADE20K and NYU Depth v2 to validate dictionary transfer, or discuss the limitation candidly.
- Specify the SAE layer explicitly in the main text — this is a one-sentence fix that substantially improves reproducibility.
- Elevate the footnote about the correlation between Z^T Z and DD^T (currently line 123) to the main text — it is an insightful algebraic observation.

## Score and Decision

### Anchor comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Ch8s4FdUXS (SAEs for SDXL Turbo) | 4.40 | R1/R2 | Current paper has broader scope, more tasks, larger scale, and more quantitative comparison. Clearly stronger. |
| F76bwRSLeK (SAEs for LLMs, foundational) | 4.80 | R2 | Current paper extends SAE methodology to vision at larger scale with richer task analysis. Slightly stronger empirically, but the MRH overreach is a comparable weakness. |
| bVTM2QKYuA (Representation geometry, polytopes in LLMs) | 6.75 | R2 | Both propose geometric hypotheses involving polytopes. bVTM2QKYuA has rigorous formalization, clear theorems, and systematic validation on 900+ concepts. Current paper's MRH has trivial theoretical contribution and thin evidence. Clearly weaker. |
| imT03YXlG2 (SAEs for CLIP, concept adaptation) | 6.50 | R1 | Stronger paper: clearer contribution, more focused scope, better-validated findings. Current paper is more ambitious but less rigorous. |
| ugXGFCS6HK (Discriminating image representations) | 6.20 | R2 | Different topic area. Current paper is less rigorous but has broader empirical scope. |

**Round 1 bracket:** 4.0–6.5  
**Round 2 narrowing:** The paper is stronger than the 4.40–4.80 range but substantially weaker than the 6.50–6.75 range. The empirical contributions (Sections 3-5) are solid, but the headline MRH contribution is under-supported. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>