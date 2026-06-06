## Summary

SIGMADOCK is a fragment-based SE(3) Riemannian diffusion model for molecular docking. The key innovation is the FR3D fragmentation scheme that decomposes ligands into rigid-body fragments, enabling diffusion over SE(3)^m with a factorized product-measure structure (Theorem 1), bypassing the entangled Cartesian dynamics of torsional models. Evaluated on the PoseBusters benchmark under the proper train-test split, SIGMADOCK achieves 79.9% Top-1 PB-valid success rate — the first deep learning method to surpass classical physics-based docking on this benchmark — versus 38.0% for DiffDock and ~58% for the best prior DL methods.

---

## Strengths

- **State-of-the-art PoseBusters accuracy, verified by ablation**: SIGMADOCK achieves 79.9% PB-valid Top-1 on the 308-complex PoseBusters set (Figure 4, left) — nearly 22 pp above the next best DL method (G2G/Vibe2 at 58.1%) and substantially above all classical methods (PDBBind at 15.9%). Ablations in Table 1 confirm that each major component (triangulation conditioning −12.8 pp, fragment merging −6.2 pp, PL interactions −3.6 pp) contributes measurably, making the headline number credible.

- **No post-hoc minimization**: SIGMADOCK's default configuration (I*) reaches 79.9% PB-valid without energy minimization of generated poses — a meaningful departure from prior DL docking workflows that artificially boost PB validity through force-field refinement. Table 1 (Config. E shows +9.1 pp when removing PB Scoring after energy scoring) confirms the method's intrinsic chemical plausibility.

- **Theoretically grounded fragment-space formulation (Theorem 1 + Lemma 1)**: The paper formally demonstrates that disjoint rigid fragments induce a factorized Haar product measure on SE(3)^m, while torsional models produce entangled non-product measures. Lemma 1 further shows that triangulation conditioning constrains bond angles/lengths while preserving dihedral freedom — giving the architecture principled inductive biases from structural chemistry, not just empirical heuristics.

- **Oracle conformer bound (Ablation G)**: Sampling from the ground-truth bound conformer distribution M_b yields 85.4% PB-valid (Table 1, Config. G), providing a clear upper bound and a concrete 5.5 pp actionable target for future binding-aware conformer sampling improvements.

---

## Weaknesses

### Fatal
None.

### Major

- **Figure 4 right panel is inconsistent with Table 4, undermining the generalization claim.** Figure 4 right shows Top-1 values of ~51%, ~53%, ~53% across the three sequence-similarity bins [0,30), [30,95), [95,100]. Table 4 reports PB-valid values of 72%, 79%, 87% for the same bins. The ~20+ percentage point gap cannot be attributed to a simple metric label discrepancy — neither the RMSD-only column nor the PB-valid column in Table 1 produces values near 51–53% for any reported configuration. The paper provides no explanation for which metric, configuration, or evaluation protocol Figure 4 right corresponds to. Since "consistent generalisation to unseen proteins" is one of the paper's core selling points (stated explicitly in the abstract), this unresolved discrepancy directly undermines that claim and must be resolved before publication.

- **Table 4's per-bin SIGMADOCK–AF3 comparison conflates different hard-example populations.** In Table 4, the [0,30) sequence-similarity bin contains 109 complexes for SIGMADOCK but only 38 for AF3. This is because sequence similarity is measured against each method's respective training data: SIGMADOCK was trained on PDBBind(v2020) (~19k entries), while AF3 was trained on a vastly larger corpus; consequently, far fewer PB test structures are truly "novel" for AF3. The result is that the two methods' low-similarity bins contain different protein complexes in different proportions, making direct row-by-row comparison invalid. SIGMADOCK's 72% in a bin of 109 hard complexes and AF3's 87% in a bin of 38 (likely different, perhaps harder) complexes are not directly comparable. The paper should clarify this confound explicitly rather than presenting the rows as symmetric comparisons.

- **Inconsistent AF3 statistics cited across sections.** The main text (Section 3.2) claims "we achieve AF3-level performance (Top-1 of 84%: see Extended Data Fig. 4e in Abramson et al.)", while Table 4 uses "Extended Data 4c" and reports AF3 at 80.2% overall. These are different extended data panels from the same AF3 paper and report different numbers, but neither the metric difference nor the subset distinction is explained. A reader cannot reconcile why SIGMADOCK (79.9%) is said to match AF3 (84%) in the text while Table 4 shows 79.9% vs. 80.2%.

### Minor

- **Energy scoring is the single largest ablation contributor, yet its design is undercharacterized.** Removing the pseudo-binding energy heuristic (Config. D) drops PB-valid from 79.9% to 66.1% — a 13.8 pp reduction, larger than any individual architectural ablation. The paper describes this as a "simple and cheap heuristic" involving pseudo-binding energy, bond angles, bond lengths, and internal energy. Given its outsized contribution, a brief analysis of which energy terms matter most, or a comparison against a learned confidence model, would substantially strengthen the methodological narrative. As written, the energy scoring's dominant role is easy to miss and its relationship to classical force-field evaluation deserves explicit framing.

- **Theorem 1's superiority claim is not isolatedly tested empirically.** Theorem 1 proves a factorization property (fragment SE(3) diffusion yields product Haar measures) and the inability of torsional models to do so. However, the only empirical evidence that this factorization *helps learning* is the comparison against DiffDock, which differs in architecture (EquiformerV2 backbone, virtual nodes), training data processing, and confidence model design. An ablation swapping only the diffusion parametrization (torsional vs. fragment) within the same SIGMADOCK architecture would be far more diagnostic. Without this, the 79.9% could plausibly be attributed to the architecture rather than the fragmentation.

### Trivial
None beyond the formatting artifacts inherent in PDF parsing.

---

## Nice-to-Haves

- **Confidence interval reporting**: With 308 PB complexes and 40 seeds, binomial standard error on Top-1 is roughly ±2–3% at 95% CI. Reporting uncertainty across multiple training runs would allow readers to judge whether the ±3–6 pp differences between ablation configurations in Table 1 are statistically meaningful.

- **FR3D reduction distribution**: The paper states m ≈ 2/3 m̂ empirically but does not report the distribution of fragmentation reductions. For highly flexible or nearly rigid ligands, the distribution matters for understanding the method's behavior at extremes.

- **Brief characterization of G2G and Vibe2**: These are the closest-performing baselines (58.1%), but their architectural class, confidence model usage, and training details are not described in the main text. A one-sentence characterization would help readers assess the 21.8 pp gap.

- **Actionable binding-aware conformer sampling**: The 5.5 pp gap between oracle (Ablation G: 85.4%) and default (79.9%) is a tractable target. Explicitly framing this as a next-step research direction in the Discussion would increase the paper's forward value.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic Point 1 (task-difficulty framing of AF3 comparison)**: The critic argues SIGMADOCK's holo-receptor input makes the task "substantially easier" than AF3's sequence-to-complex prediction, rendering the AF3 comparison "structurally misleading." This is partially true in principle, but the paper explicitly acknowledges "we cannot directly compare SIGMADOCK to co-folding methods" and provides Table 4 as a supplementary reference point, not the primary comparison. Furthermore, the easier-input argument cuts both ways: using a holo receptor is standard practice for re-docking evaluation, and SIGMADOCK's core claim is about re-docking, not sequence-to-structure prediction. The framing concern is real (and captured under the retained minor issue about inconsistent AF3 statistics) but the full "structurally misleading" characterization is overstated given the paper's explicit caveats.

- **Harsh critic's introduction critique about DiffDock's score-estimation space**: The critic claims "the score is estimated in torsion space, not Cartesian space" for DiffDock, calling the paper's inverse-problem framing incorrect. This is a subtle technical debate and does not definitively invalidate the paper's argument about entangled Cartesian-space distributions induced by torsional updates — which is what Theorem 1 addresses. Removed as a fringe technical dispute that does not rise to a verifiable paper error.

- **"Pocket Specified" vs. "Holo Specified" asymmetry as unfair comparison**: The harsh critic suggests the Figure 4 left grouping (DiffDock under "Holo Specified," SIGMADOCK under "Pocket Specified") may represent asymmetric input information favoring SIGMADOCK. Providing the pocket residues is an additional input that DiffDock does not receive. However, given this asymmetry *disfavors DiffDock (the baseline)* rather than the author's method, by the hard rules this criticism must be removed — unfair comparisons that favor the baseline and not the author's method are not a valid weakness.

- **Strength Finder #3 (generalization to unseen proteins)** as stated: This strength is undermined by the verified Figure 4 right vs. Table 4 inconsistency and is therefore not included in the Strengths section as stated.

- **Strength Finder's "AF3-level performance with 50× faster sampling"**: The speed claim (50×) is stated in the text and is reasonable. The "AF3-level performance" framing is retained as a major weakness to fix; the speed claim itself is kept as part of the data-efficiency strength but the full combined framing is removed as stated.

---

## Novel Insights

The most genuinely novel observation surfacing from this review — one not made explicit in the paper itself — is the structural confound in Table 4's per-bin analysis: because sequence similarity is measured against each method's *own* training corpus, SIGMADOCK's [0,30) bin of 109 complexes and AF3's [0,30) bin of 38 complexes are not the same complexes or even the same difficulty tier. This means the table, as currently presented, does not support the cross-method generalization narrative it is invoked to support. Resolving this — for example by measuring all bins against a common reference (e.g., PDB70 clustering) or by reporting the overlap between SIGMADOCK's and AF3's hard-example sets — would make the generalization comparison scientifically valid and would strengthen one of the paper's most interesting empirical claims.

---

## Suggestions

1. **Resolve Figure 4 right vs. Table 4 discrepancy**: Identify which metric/configuration Figure 4 right reports and label it explicitly. If it reports a different metric (e.g., RMSD-only Top-1), relabel the axis; if it shows a different configuration, state which one.

2. **Fix the AF3 statistics inconsistency**: Decide whether to use Extended Data Fig. 4c (80.2% overall) or 4e (84%) from Abramson et al., explain the difference (different metrics, subsets, or conditions), and use one consistently throughout the paper.

3. **Clarify Table 4's per-bin basis**: Add a footnote or methods paragraph explaining that sequence-similarity bins are measured against each method's own training data, so the row-by-row comparison is approximate and the populations differ. Optionally report SIGMADOCK's performance on AF3's 38 hard complexes (or vice versa) for a more direct comparison.

4. **Expand energy-scoring analysis**: Add even a brief (1-2 panel) supplementary analysis showing which energy terms drive the 13.8 pp contribution, or a comparison against a learned confidence head baseline, to sharpen the methodological narrative.

5. **Isolate fragmentation vs. architecture**: Even a small-scale ablation (e.g., on a random 50-complex subset) comparing torsional vs. fragment diffusion within the same EquiformerV2 architecture would directly validate Theorem 1's claimed learning advantage.

---

## Assessment Along Key Axes

**Originality**: High. Fragment-based SE(3)^m diffusion with a dedicated fragmentation algorithm (FR3D), triangulation soft constraints, and Newton-Euler equivariant scoring is a coherent and novel design not previously published.

**Importance of research question**: High. Molecular docking is a bottleneck in structure-based drug discovery; achieving chemically valid pose prediction without minimization is practically significant.

**Claims well supported**: Moderate-to-strong for the primary benchmark claim (79.9% PB-valid), with the ablation table providing solid support for individual contributions. Weakened by the Figure 4 right inconsistency and the confounded AF3 per-bin comparison.

**Soundness of experiments**: Mostly sound, with the verified Figure 4 inconsistency and AF3-statistics inconsistency as concrete issues requiring correction rather than structural flaws.

**Clarity of writing**: Good overall. The energy scoring contribution is the main place where the presentation underplays an important design choice.

**Value to the research community**: High. The first DL method to beat classical physics-based docking on a chemically rigorous benchmark, with open methodological contributions (fragmentation, diffusion design, equivariant scoring).

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>5</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>5</community_value>
</subscores>