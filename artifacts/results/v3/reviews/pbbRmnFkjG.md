Now I have a thorough understanding of the paper and the calibration landscape. Let me compile my final review.

## Calibration Summary

**All anchors retrieved:**

**Round 1 - Topic low (<3.5):** tcsZt9ZNKD (1.75, SAE scaling), Wxl0JMgDoU (2.5, Chess SAE), 89wVrywsIy (3.4, Circuit analysis), wZiH43e5Ah (3.0, Concept extraction) — These papers fail at small scale, narrow scope, or weak execution; the current paper does not share those failures.

**Round 1 - Topic mid (3.5-7.5):** imT03YXlG2 (6.5, SAE for CLIP ViT — most comparable; similar methodology, cleaner narrative), Ch8s4FdUXS (4.4, SDXL Turbo — narrower scope, rejected), F76bwRSLeK (4.8, SAE interpretable features in LLMs — accepted but basic), 9ca9eHNrdH (7.0, SAEs non-canonical — strong negative result with clean experiments).

**Round 1 - Topic high (>7.5):** I4e82CIDxv (8.0, Sparse feature circuits), 5Ca9sSzuDp (8.0, CLIP decomposition), 2dnO3LLiJ1 (8.0, ViT registers), STUGfUz8ob (7.6, Transformers reasoning) — Significantly more polished, better-supported papers.

**Round 1 - Weakness queries:** l5ouuojPGe (3.0), z1yI8uoVU3 (3.0), LDu822E45Q (4.25), lAhQCHuANV (6.33), bWT6OBJ71x (4.4, insufficient evidence pattern), J7AwIJvR3d (3.75), fmWVPbRGC4 (5.67, local vs distributed representations), 4ndvumlZak (4.5), ghH6YYDs15 (4.67, SAE limitations), 5IZfo98rqr (3.5, SAE dark matter), k9t8dQ30kU (6.75, representation geometry).

**Round 2:** 1Njl73JKjB (7.0, Principled SAE evaluations), DZxU0q2S11 (5.75), 34SPQ6fbYM (4.5), OXfllUhjrJ (3.67), 8ohamFnX14 (5.2).

**Round 1 bracket:** 4.5–6.5. The paper is clearly above the low-band (<3.5) because of substantial scale and thoroughness, but below imT03YXlG2 (6.5) due to structural issues in the MRH framing.

**What low-band and weakness-anchored papers failed at:** limited scope, insufficient empirical support for central claims, missing experiments that discriminate hypotheses. The paper under review shares the "insufficient discriminating evidence for the central theoretical claim" pattern — the MRH is proposed with evidence that is consistent with it but does not rule out alternatives. However, unlike those weak anchors, the paper's empirical contributions (Sections 3–5) are substantial and would stand independently. The score must reflect both the strong empirical core and the structural weakness in the MRH argument.

**Final score: 5.5** — strong empirical contributions weighed against structural issues in the MRH framing and the unresolved SAE-MRH tension.

---

## Summary

This paper trains a stable sparse autoencoder on DINOv2-B activations, yielding a 32,000-atom concept dictionary — the largest such resource for a vision foundation model. Using this dictionary, the paper makes three contributions: (1) a task-specific analysis showing that classification, segmentation, and depth estimation recruit distinct low-dimensional concept subspaces ("Elsewhere" concepts for negation, border detectors, monocular depth cue families); (2) a detailed geometric and statistical characterization of the dictionary revealing departures from the Linear Representation Hypothesis (higher coherence than Grassmannian baselines, sharp spectral decay, antipodal pairs, low-dimensional token neighborhoods); and (3) the Minkowski Representation Hypothesis (MRH), a theoretical proposal that token embeddings are Minkowski sums of convex polytopes arising naturally from multi-head attention, supported by preliminary empirical evidence (geodesic paths, Archetypal Analysis reconstruction parity, block-structured code Gram matrices).

## Strengths

1. **Large-scale, stable concept dictionary for DINOv2.** Section 2 delivers a 32k-atom SAE with R² > 88% reconstruction fidelity and stability guarantees via convex-hull-constrained atoms. This is a valuable resource that will enable follow-up interpretability work on a widely used vision foundation model.

2. **Task-specific functional specialization (Section 3).** The analysis showing that classification, segmentation, and depth estimation recruit distinct, low-dimensional concept subspaces is novel and well-supported. The identification of "Elsewhere" concepts (off-object yet object-dependent), exclusive border detectors for segmentation, and three interpretable monocular depth cue families provides concrete, non-trivial insights into how DINOv2 organizes its representations for different downstream tasks. The quantitative spectral analysis (Figure 11) confirms that task-recruited concepts form coherent low-dimensional subspaces.

3. **Careful geometric characterization of departures from LRH (Section 4).** The systematic comparison against random and Grassmannian baselines for coherence, spectral decay, Hoyer scores, and co-activation geometry provides concrete empirical diagnostics that challenge a pure sparse-coding view. The discovery of antipodal pairs forming signed semantic axes and dense positional outliers is well-documented and thought-provoking.

4. **Theoretical grounding of MRH via multi-head attention (Proposition 1).** The derivation showing that multi-head attention naturally produces a Minkowski sum of head-wise convex sets is mathematically sound and provides an elegant architectural justification for the hypothesis. This connects the proposal to established mechanism in a non-trivial way.

## Weaknesses

### Major

1. **Insufficient discriminating evidence for the MRH as a central claim.** The paper presents MRH as a headline contribution ("we advance a different view... we call this the Minkowski Representation Hypothesis"), but the empirical tests in Section 6.3 — geodesic paths, Archetypal Analysis reconstruction parity, and block-structured Gram matrices — are necessary conditions consistent with MRH but also with alternative geometric models (a single non-factorial convex hull, a smooth low-dimensional manifold, or a poor SAE fit that AA happens to match). The paper's own most distinguishing prediction (archetypal steering saturates while directional steering extrapolates, stated in Implications) is not tested. The paper would be considerably stronger if it either (a) provided a critical experiment that could discriminate MRH from alternatives, or (b) positioned the MRH more explicitly as a speculative framework rather than a central contribution, making the disconnect between the framing and the evidence less acute.

2. **Unresolved tension between SAE methodology and MRH geometry.** The paper's empirical backbone is a sparse autoencoder whose design instantiates the Linear Representation Hypothesis (features as sparse, near-orthogonal directions). The paper then uses this SAE to motivate the MRH, which posits a fundamentally different geometry (Minkowski sums of convex polytopes). The paper never explains what the 32,000 SAE atoms *correspond to* under the MRH — are they vertices of polytopes? random cross-sections? noise artifacts? This creates an internal contradiction: the primary analytical tool assumes the framework the paper rejects, and the reader is left uncertain whether the SAE-based empirical findings (Sections 3–5) should be reinterpreted in light of MRH or treated as independent of it. The paper needs to either build a bridge between the SAE output and the MRH framework, or explicitly decouple the SAE analysis as a probe of LRH failure modes from the separate MRH proposal.

### Minor

3. **Qualitative findings presented with limited methodological transparency.** The "Elsewhere" concept causal claim (conditional negation) rests on a causal masking experiment referenced only in the Figure 2 caption and deferred to Appendix D. The monocular depth cue taxonomy (Section 3) is described as derived from visual inspection of UMAP projections of perturbation responses. While these observations are genuinely interesting and the paper uses appropriately hedged language ("suggest", "may support"), presenting them as *findings* rather than *hypotheses* without quantitative validation (e.g., cluster purity metrics on perturbation responses, human evaluation of depth cue assignments) weakens the empirical credibility of otherwise compelling qualitative results.

4. **The non-identifiability result (Proposition 2) undermines earlier interpretability claims without being reconciled.** Proposition 2 correctly notes that Minkowski decomposition is non-unique from final activations. This is a theoretically important caveat, but it also implies that the SAE factorization in Sections 2–4 (which operates on final activations) is one arbitrary factorization among many. The paper does not address this tension — if decomposition is non-identifiable, what guarantees that the 32k-concept dictionary captures "real" rather than arbitrary structure? This should be explicitly discussed.

### Trivial

5. Several figure references (e.g., Fig. 26) point to content in the appendices that was not available in the reviewed version; confirm that these figures are included in the camera-ready submission.

## Nice-to-Haves

- Conduct the steering experiment comparing MRH-archetypal (moving toward landmarks within convex hull) and LRH-directional (adding unbounded feature directions) steering. This is the paper's own stated discriminating test and would dramatically strengthen the MRH proposal.
- Validate the depth cue taxonomy quantitatively by clustering concept response patterns to the perturbation suite and reporting cluster purity or silhouette scores.
- Test whether SAE atoms lie on the boundary of the activation convex hull (predicted if they correspond to polytope vertices under MRH) or in the interior.

## Novel Insights

The paper's most novel contribution is the synthesis of large-scale SAE-based interpretability with a geometrically grounded theoretical framework. The observation that multi-head attention mechanically produces Minkowski sums of convex sets (Proposition 1) is a genuinely new connection between transformer architecture and representation geometry. The empirical finding that task-recruited concepts form cleanly separated, low-dimensional subspaces with specific functional signatures (Elsewhere, border, depth cues) is a significant step beyond generic "features are interpretable" claims common in SAE papers. The geometric diagnostics in Section 4 (departures from Grassmannian baselines, weak co-activation/geometry coupling) provide reusable methodology for future interpretability work.

## Suggestions

1. **Restructure the paper to resolve the SAE-MRH tension.** Either (a) add a section explicitly explaining what SAE atoms correspond to under MRH (e.g., as overcomplete cross-sections of polytope boundaries) and validating this empirically, or (b) clearly separate the paper into two independent contributions: an empirical study of DINOv2's representations using SAEs (Sections 2–5), and a separate theoretical proposal (Section 6) that is presented as speculative rather than a conclusion of the empirical work.

2. **Add the steering experiment** as a critical test distinguishing MRH from LRH. This is the paper's own most compelling prediction.

3. **Strengthen the qualitative findings** with minimal quantitative validation — cluster purity for the depth cue taxonomy, a brief description of the causal masking experiment in the main text.

4. **Discuss the non-identifiability caveat explicitly** in the context of the SAE dictionary, not just as a theoretical observation about MRH.

## Score and Decision

**MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>**