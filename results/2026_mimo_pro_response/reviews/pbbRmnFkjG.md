Good. Now I have enough calibration. Let me write the final review.

## Summary

This paper trains a stable sparse autoencoder (32k concepts, k=8, R² > 88%) on DINOv2-B and uses the resulting dictionary for three studies: (1) task-specific concept recruitment analysis revealing functional specialization across classification (Elsewhere concepts), segmentation (border concepts), and depth estimation (monocular cue families); (2) systematic geometric diagnostics showing departures from idealized near-orthogonal sparse coding; and (3) the Minkowski Representation Hypothesis (MRH), framing token representations as Minkowski sums of convex polytopes defined by archetypal landmarks.

## Strengths

- **Novel and well-executed task-specific concept recruitment analysis**: The paper identifies functionally specialized concept subsets — "Elsewhere" concepts for classification that fire off-object but vanish when the object is removed via causal masking (line 79), border concepts for segmentation with consistent spatial footprints along contours (line 81), and three monocular depth cue families (projective geometry, shadow-based, frequency transitions) isolated via controlled perturbations (lines 83–93, Figure 3). The quantitative confirmation that task-aligned concepts form low-dimensional subspaces with faster eigenspectrum decay than random subsets (Figure 11) is compelling.

- **Clean methodological design for depth cue isolation**: The controlled perturbation experiment (median blurring, edge-preserving smoothing, high-pass filtering) isolating three functional depth cue clusters is methodologically sound and connects DINOv2's internal representations to visual neuroscience principles.

- **Systematic geometric diagnostics with appropriate baselines**: Four quantitative diagnostics — coherence vs. random/Grassmannian baselines (using TAAP algorithm), singular-value decay, Hoyer scores, and co-activation vs. geometric affinity correlation (Figure 13 showing weak correlation) — collectively establish that purely sparse near-orthogonal feature packing is insufficient. The comparison to multiple baselines (random, Grassmannian, shuffled) strengthens the analysis.

- **Thorough elimination of positional confound**: The paper trains linear decoders at each layer (Figure 6), shows position appears only among intermediate PCs (3–5), and demonstrates that projecting out the positional subspace leaves PCA organization largely unchanged (Figure 25). This is a careful and convincing elimination of an alternative explanation for smooth token geometry.

- **Honest and transparent positioning**: The paper is transparent about MRH being a "working hypothesis" with "preliminary evidence" (lines 35, 177), and Proposition 2 on non-identifiability (line 167) is an honest limitation acknowledged proactively.

## Weaknesses

### Fatal
None

### Major

- **MRH Proposition 1 is near-trivially true of any transformer**: The central theoretical claim (Proposition 1, lines 155–159) states that multi-head attention produces Minkowski sums because each head computes convex combinations of its value vectors and outputs are summed. The paper acknowledges this is "elementary" (line 161). While mathematically correct, this follows directly from the definition of attention — any transformer output trivially satisfies this property regardless of how internal representations are actually organized. The key question — whether the specific polytopes, tiles, and archetypes identified by MRH have empirical content beyond this architectural tautology — remains unanswered. The paper does not demonstrate that MRH makes predictions specific to Minkowski sums that are not also predicted by generic low-dimensional manifold descriptions.

- **MRH empirical tests are not discriminative**: The three empirical tests (line 163) — piecewise-linear geodesics staying near data support, Archetypal Analysis matching SAE at ~10 archetypes, and block structure in code Grams — are each consistent with MRH but do not uniquely support it. Geodesics staying near data is expected for any curved manifold; AA matching SAE could reflect low image dimensionality (independently established in Section 5); block structure in Grams could reflect spatial/semantic correlation rather than MRH "tiles." The gap between proposing a competing hypothesis to LRH and the evidence offered is significant.

- **Unresolved tension between R² > 88% under LRH and claimed LRH departures**: The SAE operationalizing LRH achieves R² > 88% reconstruction (line 57), which the paper presents as validation. Yet Section 4 claims significant departures from LRH based on coherence, spectral decay, and anisotropy diagnostics. If LRH were seriously wrong, the SAE should not reconstruct so well. The paper does not adequately resolve this tension — the departures may reflect that LRH is approximately correct with structured residuals, rather than evidence for a fundamentally different geometry. This weakens the motivation for proposing MRH as a competing hypothesis.

### Minor

- **Elsewhere concept causal language exceeds evidence**: The abstract states Elsewhere concepts "implement object negation" (line 9), while the body hedges to "evidence suggestive of a causal effect realizing conditional negation (another interpretation being distributed off-object evidence)" (line 51). The causal masking experiment (concept vanishes when object is removed) is suggestive but does not distinguish negation from distributed off-object evidence that correlates with object presence. The abstract and introduction should match the body's caution.

- **Sparsity parameter k=8 not ablated**: The choice of k=8 active codes per token (line 57) is stated to be consistent with prior work but is not ablated. Since sparsity level affects concept count, reconstruction quality, and geometric structure, an ablation would strengthen confidence in downstream findings.

### Trivial
None

## Nice-to-Haves
- Quantifying downstream task performance (classification accuracy, segmentation mIoU, depth RMSE) as a function of SAE reconstruction quality to confirm R² > 88% retains task-relevant information.
- Analyzing whether DINOv2's native self-supervised heads (DINO, iBOT) recruit similar concept subsets to the supervised probes.
- Checking robustness across DINOv2-L or DINOv2-g to assess scale dependence.

## Removed Points
These points are flagged to be removed, treat them with caution:
No weaknesses were removed — all identified issues are grounded in specific paper content.

## Novel Insights
The most genuinely novel contribution is the systematic task-specific concept recruitment analysis. The "Elsewhere" concept discovery — concepts that fire off-object but causally depend on object presence, challenging standard attribution maps — is a non-trivial finding with practical implications for interpretability tools. The depth cue family isolation via controlled perturbations (median blurring, edge-preserving smoothing, high-pass filtering) provides interpretable, neuroscience-aligned explanations for how DINO performs depth estimation without 3D supervision. The geometric observation that task-aligned concepts form low-dimensional subspaces with faster eigenspectrum decay (Figure 11) and that co-activation and geometric affinity correlate only weakly (Figure 13) provide useful negative evidence against pure sparse coding.

## Suggestions
- Tone down MRH positioning: frame it as a refinement of LRH rather than a competing hypothesis, since the evidence shows LRH is approximately correct with structured deviations. This is more honest about what the data show.
- Sharpen MRH's empirical content by identifying observable consequences specific to Minkowski sums not shared by generic low-dimensional manifolds (e.g., computing faces of per-image activation polytopes and showing alignment with archetypes).
- Add an ablation on sparsity parameter k to strengthen the empirical foundation.
- Resolve the R² > 88% vs. LRH departures tension explicitly in the discussion.

## Evaluation

**Originality**: The task-specific concept recruitment analysis and Elsewhere concept discovery are genuinely novel contributions to vision transformer interpretability. The MRH proposal is intellectually stimulating but theoretically underdeveloped. Moderate-to-high originality.

**Importance**: Understanding how vision transformers organize representations internally is an important research question. The empirical findings are valuable to the interpretability community. Moderately important.

**Claims well-supported**: The empirical interpretability claims (Sections 3–5) are well-supported with multiple quantitative diagnostics and appropriate baselines. The MRH claims (Section 6) are explicitly positioned as preliminary, but the evidence is not discriminative. Strong for empirical sections, weak for MRH.

**Soundness of experiments**: Generally sound — controlled perturbations, multiple baselines (Grassmannian, random, shuffled via TAAP), quantitative diagnostics. SAE setup is well-specified. Good.

**Clarity of writing**: Well-written with clear section structure and honest positioning. Some tension between abstract/intro causal language and body hedging on Elsewhere concepts. Good.

**Value to community**: The 32k concept dictionary and interactive visualization would be valuable resources. The task-specific recruitment analysis provides actionable insights for interpretability tool design. Good value.

---

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Scaling/evaluating SAEs | tcsZt9ZNKD.md | 1.75 | 1 | Much weaker — different scale of contribution |
| Chess SAE adaptivity | Wxl0JMgDoU.md | 2.50 | 1 | Much weaker — narrow domain, limited insights |
| Hierarchical circuit tracing | 89wVrywsIy.md | 3.40 | 1 | Weaker — less rigorous, limited validation |
| CAN concept extraction | wZiH43e5Ah.md | 3.00 | 1 | Weaker — generic framework, less novel findings |
| SDXL Turbo SAE | Ch8s4FdUXS.md | 4.40 | 2 | Weaker — limited scope, less novel insights |
| Compute-optimal SAE | ghH6YYDs15.md | 4.67 | 2 | Weaker — theoretical focus, less empirical novelty |
| Concept mechanisms | vogtAV1GGL.md | 5.75 | 2 | Weaker — less rigorous, less comprehensive analysis |
| Simple interpretable transformer | bkdWThqE6q.md | 6.00 | 2 | Comparable but narrower scope |
| PatchSAE (CLIP) | imT03YXlG2.md | 6.50 | 1/2 | Comparable — my paper has stronger empirical analysis |
| Representation geometry | bVTM2QKYuA.md | 6.75 | 2 | Comparable — my paper has broader empirics but weaker theory |
| RSVC visual concepts | ih3BJmIZbC.md | 6.80 | 2 | Similar level — my paper has stronger novel findings |
| Not All Features Linear | d63a4AM4hb.md | 7.00 | 2 | Slightly stronger — more rigorous theory + causal interventions |
| SAE canonical units | 9ca9eHNrdH.md | 7.00 | 1 | Slightly stronger — cleaner conceptual contribution |
| Sparse feature circuits | I4e82CIDxv.md | 8.00 | 1 | Stronger — more decisive practical contribution |
| CLIP text decomposition | 5Ca9sSzuDp.md | 8.00 | 1 | Stronger — cleaner methodology + clear insights |
| Vision Transformers Registers | 2dnO3LLiJ1.md | 8.00 | 1 | Stronger — foundational contribution with broad impact |

**Round-1 bracket**: Between 5.0 and 7.5 (clearly above weak anchors, below strong anchors).

**Round-2 narrowing**: The paper is clearly above PatchSAE (6.50) in empirical novelty and breadth, comparable to Representation Geometry (6.75) in overall contribution, but below Not All Features Linear (7.00) due to weaker theoretical formalization. The paper sits at approximately 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>