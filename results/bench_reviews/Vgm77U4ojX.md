## Summary

This paper introduces SigmaDock, a fragment-based SE(3) diffusion model for molecular docking that decomposes ligands into rigid-body fragments via a novel fragmentation scheme (FR3D) with soft triangulation constraints, then defines a diffusion process over SE(3)^m. The key contributions are: (1) a theoretical justification that fragment-based product-space diffusion avoids the entangled non-product measures of torsional models; (2) FR3D merging and triangulation constraints that reduce degrees of freedom while preserving geometric priors; and (3) an SO(3)-equivariant architecture adapted for fragment reasoning. Empirically, SigmaDock achieves 79.9% Top-1 success rate (RMSD<2Å & PB-valid) on PoseBusters, dramatically outperforming prior deep learning methods (12.7–32.8%) and surpassing classical physics-based docking — the first deep learning method to do so on this benchmark under fair training conditions.

## Strengths

- **State-of-the-art docking accuracy on PoseBusters**: SigmaDock achieves 79.9% Top-1 (RMSD<2Å & PB-valid) on PoseBusters using the intended train-test split (PDBBind v2020 only), compared to 12.7–32.8% for prior deep learning methods, and surpasses classical docking (Vina 59.0%, Glide 72.0%). This is the first deep learning method to exceed classical approaches under this rigorous benchmark (Figure 4, Table 1).

- **Novel fragmentation with triangulation constraints (FR3D)**: The paper introduces an irreducible fragmentation scheme that reduces fragments from k+1 to roughly 2/3(k+1), combined with soft triangulation distance conditioning that fixes bond angles while leaving dihedrals free. Ablations confirm triangulation is the single most important component (12.8% PB-valid drop when removed, Table 1).

- **Clean, fair evaluation protocol**: Trained on PDBBind v2020 only (no additional data that could cause leakage), evaluated with no energy minimization post-processing, and results include PB-validity checks. The deliberate choice to avoid commonly used but unfair evaluation practices makes the reported gains credible.

- **Strong generalization to unseen proteins and diagnostic failure analysis**: Performance remains high across low sequence-similarity splits (72% Top-1 PB-valid for [0,30) similarity), and degradation in the presence of co-factors (58.8% for natural ligands vs 83.0% for none, Table 2) confirms the model learns physical principles rather than memorizing training instances.

- **Computational efficiency without separate confidence models**: SigmaDock achieves 0.57s/mol per seed inference with a simple Vinardo energy + physico-chemical heuristic for ranking, requiring no separately trained confidence model or energy minimization — a practical advantage over methods like DiffDock (72s/mol with confidence model) and AF3 (~16 min/mol).

- **Theoretical guarantees**: Theorem 1 formally proves that torsional models induce entangled non-product measures while rigid fragments yield factorized product measures. Theorem 2 proves invariance to local coordinate orientation and stochastic SO(3)-equivariance of the sampling kernel (Appendix H.1).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No direct quantitative comparison to Uni-Mol Docking v2 and other recent deep learning methods reporting PoseBusters results.** The paper mentions Uni-Mol Docking v2 in Appendix J.2 and explains that it relies on energy minimization post-processing, which the authors deliberately avoid. However, the central claim of being "the first deep learning approach to surpass classical physics-based docking" would be strengthened by either reporting those methods' numbers alongside SigmaDock (with and without the same post-processing) or providing a more detailed justification that the comparison is impossible. As it stands, the claim is incompletely supported against the full set of comparable methods.

- **Headline results lack uncertainty quantification.** The core Top-1 percentages (e.g., 79.9% on PB) are reported as point estimates without confidence intervals, error bars, or variance across training runs. Given that the model uses 40 random seeds and a stochastic conformer generator, these numbers are random variables. The ablation table also lacks uncertainty estimates. While this is common practice in the field, it makes it impossible to assess whether the reported gains over baselines are statistically significant, especially when baseline variances are of similar magnitude.

- **The theoretical motivation (product-space over torsion-space) does not cleanly align with the ablation hierarchy.** Theorem 1 argues that the product-space formulation is the key advantage over torsional models, but ablations show the largest empirical driver is triangulation conditioning (12.8% drop when removed, Config A), while removing fragment merging causes a smaller drop (6.2%, Config C). This suggests the main practical benefit comes from geometric conditioning rather than the product-space formulation per se. The narrative would benefit from more careful attribution of which component drives which aspect of performance.

- **The AF3 comparison in Table 4 has a reported mismatch (80.2% vs. 84.4% in AF3's own reporting).** The paper footnotes this discrepancy but does not explain why the mismatch arises. While this is unlikely to affect the paper's core claims, a brief explanation would improve completeness.

### Trivial
None.

## Nice-to-Haves
- A direct empirical comparison of torsional diffusion vs. fragment diffusion under identical architectural conditions (same backbone, same data) would more directly support the theoretical claims in Section 2.2.2.
- A cross-docking experiment (even on a small subset) would strengthen the generalizability claims beyond re-docking.
- An analysis of how results depend on the quality of the initial RDKit conformer used for triangulation reference distances (e.g., ETKDGv3 vs. a more precise force field).

## Removed Points
These points were flagged for removal based on instructions; treat with caution:

- **Criticism that alignment procedure "essentially solves the docking problem"** — This misreads the paper. The alignment is used solely to verify that RDKit conformers can approximate bound poses, not as part of the docking procedure itself. The paper is explicit about this usage.
- **Criticism that the SDE formulation follows prior work** — This is an observation, not a weakness. The paper's novelty is in fragmentation and conditioning, not in the SDE mechanics (which are correctly attributed to Yim et al., 2023).
- **Strength Finder strength about "fragment-based SE(3) diffusion overcomes torsional model limitations"** — Kept as it is well-supported, but the strength finder's summary language has been integrated into the strengths section above.
- **Individual section notes about Section 2.2.1 alignment** — Already addressed by the paper's clear framing and the 5-try alignment protocol (Appendix D.3).
- **Generic strengths from Strength Finder that are redundant** — Merged into main strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the same assessment: the paper makes a genuine, well-executed contribution with clean experimental design, but could be strengthened by broader baseline comparison and uncertainty quantification. The most insightful observation across reviews is the tension between the theoretical framing (product-space as the key advantage) and the ablation evidence (triangulation as the main empirical driver) — this is a useful refinement point for the authors' narrative.

## Suggestions
1. Add a comparison table (possibly in appendix) with Uni-Mol Docking v2 and any other open-source deep learning methods reporting PoseBusters results, noting whether they use energy minimization. If possible, run SigmaDock with the same post-processing for an apples-to-apples comparison.
2. Provide confidence intervals for the main Top-1 results — at minimum, report standard deviation or bootstrapped confidence intervals across test points for the headline numbers.
3. Reframe the contribution narrative to more accurately reflect that triangulation constraints, not just the product-space formulation, are the primary empirical driver of performance gains.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison |
|---|---|---|
| Quotient-Space Diffusion (`3JPAkwSVc4`) | 7.50 (Oral) | Stronger theoretical novelty but comparable empirical rigor; SigmaDock has stronger practical impact and cleaner evaluation |
| Pallatom-Ligand (`uMD75SDTTA`) | 6.00 (Poster) | Similar applied-diffusion contribution; SigmaDock has better ablations and more convincing causal analysis of components |
| PoseX (`qqzxKudD4T`) | 5.00 (Poster) | Benchmark paper with less novelty; SigmaDock is substantially more novel |
| Bento (`kIxAQxUZHq`) | 5.00 (Reject) | Benchmark paper; SigmaDock has stronger methodological contribution |
| ProtoBind-Diff (`FrXTQED0Nt`) | 3.50 (Reject) | Marginal improvements over baselines; SigmaDock's results are dramatically better |
| Perturbed Flow Matching (`CEuzrRs613`) | 2.67 (Reject) | Much weaker empirical validation; SigmaDock is significantly stronger |
| RoSE (`yV2bsMVfal`) | 3.00 (Withdrawn) | Limited novelty; SigmaDock is more complete and better executed |
| SAIR (`qgk2F6jxH4`) | 5.50 (Poster) | Dataset paper; different contribution type |
| FragFM (`tr6vRn2aPg`) | 5.00 (Poster) | Fragment-based molecular generation; SigmaDock addresses a harder problem (docking) with stronger results |

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>