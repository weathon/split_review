Now I have all the information needed. Let me synthesize the consolidated review.

## Summary

This paper introduces *spreading OOD detection*, a new benchmark task for node-level OOD detection on graphs where OOD nodes propagate via epidemic models (SI/SIS), modeling real-world phenomena like virus spread more accurately than the conventional random-selection setup. The paper also contributes the Spreading COVID-19 dataset (symptom-based features on a social-network graph) and proposes EDBD, an energy-based detector that uses energy similarity and consistency matrices to control aggregation and prevent harmful mixing of ID and OOD energies. Experiments across seven datasets show EDBD outperforms eight baselines on both spreading OOD detection and conventional label leave-out.

## Strengths

1. **Well-motivated and novel task formulation.** The paper identifies a genuine limitation in prior node-level OOD evaluation — random OOD selection ignores interactions — and formalizes a natural alternative where OOD spreads via epidemic models (SI/SIS). Section 1 motivates this with concrete real-world examples (viruses, computer worms, contaminants), and Section 3 provides a clear formalization (Eqs. 1–2). This is the paper's primary contribution and is cleanly scoped.

2. **Creation of a dedicated real-world benchmark, Spreading COVID-19.** The dataset provides 23-dimensional symptom-based features for ID classes (normal, allergies, cold, flu) and OOD (COVID-19), with infection spread simulated on the LastFM Asia social graph. The feature design is documented in Appendix A with symptom probabilities sourced from medical references. The dataset is publicly released under CC BY 4.0, filling a gap in node-level OOD resources.

3. **Consistent empirical superiority across tasks.** EDBD outperforms eight baselines across both spreading OOD detection (Tables 2, 3) and conventional label leave-out (Table 1) on all seven datasets, with standard deviations reported over 10 runs. The ablation study (Table 4) confirms that both the energy similarity matrix (S) and energy consistency matrix (C) contribute meaningfully to performance. The method also generalizes beyond the proposed task — it improves over prior methods on the standard label leave-out setup, which the paper does not require to be true.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Synthetic Bernoulli OOD features on Cora/LastFM Asia limit the reach of the realism claims.** The paper uses Bernoulli(0.1) features for OOD nodes on Cora and LastFM Asia (Section 5.1). While the paper's primary realism claim concerns the *spreading mechanism* (rather than feature realism), and the COVID-19 dataset separately addresses feature realism, the paper's language ("realistic settings," "curate realistic benchmarks") is broad enough that a reader could reasonably expect both mechanism *and* features to be realistic on all datasets. The paper would benefit from explicitly distinguishing that the Cora/LastFM Asia experiments demonstrate the method under *synthetic* spreading conditions, while the COVID-19 dataset validates the real-world applicability. This does not undermine the core contribution (the spreading formulation is independently valuable) but is a presentation issue that overreaches slightly.

2. **EDBD's design choices are not compared to alternatives.** The similarity function (Section 4.3) — an inverse-distance formula involving global min/max of energies and absolute difference — and the consistency measure (Section 4.4) — standard deviation with a linear transform C = I − βΣ — are both plausible but not compared against reasonable alternatives (e.g., Gaussian RBF similarity, entropy-based consistency, or median absolute deviation). The ablation shows that removing each component hurts, but does not show that *this specific formulation* is preferable to other plausible ones. For a benchmark paper where the method is a secondary contribution (a baseline), this is not fatal, but a brief comparison of 2–3 alternatives would strengthen the paper.

3. **The ablation study's claim that the "no S, no C" variant corresponds to GNNSAFE is imprecise.** The paper states (Section 5.4): "The first rows of the tables in Table 4, where both S and C, correspond to the performance of GNNSAFE." When S is excluded (uniform edge weights) and C is excluded (C = I by setting β = 0), the EDBD recurrence becomes E^(k) = (1−α)E^(k−1) + α·A_row-norm·E^(k−1). GNNSAFE (Wu et al., 2023) uses a different recurrence: E^(k) = (1−β)E^(0) + β·A_row-norm·E^(k−1), with E^(0) as a persistent base. These are not equivalent. The ablation's conclusion that both S and C contribute is unaffected, but the claim of equivalence to GNNSAFE should be corrected or qualified.

4. **No statistical significance testing.** With only 10 test episodes and sometimes narrow margins (e.g., Cora SI AUROC-T: EDBD 97.0±1.4 vs. Energy 96.2±1.2, Table 3), differences may not be significant. A paired bootstrap or Wilcoxon signed-rank test would strengthen the experimental conclusions.

5. **No hyperparameter sensitivity analysis.** The method has hyperparameters α, β, ε, and K that are tuned on validation sets, but no analysis of how performance varies with these choices is reported. A brief sensitivity study on at least one dataset would help establish robustness.

### Trivial

- Section 4.3 uses `sin` to denote similarity (likely a parser artifact for `sim`).

## Nice-to-Haves

- The paper could explicitly acknowledge that the Cora/LastFM Asia experiments use synthetic OOD features and clarify that the "realistic" claim primarily refers to the epidemic spreading dynamics, not the feature distribution.
- A comparison of 2–3 alternative similarity functions (e.g., Gaussian RBF) for the energy similarity matrix would strengthen confidence in the design choices.
- A short discussion of why a specific epidemic parameter range (γ=0.5, δ=0.1) was chosen (already partially addressed in Appendix A) and how results might vary under different parameters would be useful.

## Removed Points

- *"The paper does not cite any prior work that criticizes [random selection]."* — Removed per instruction: missing related works should not be mentioned.
- *"The similarity function uses global min and max, which makes it sensitive to outliers."* — Removed: this is a speculation about a potential issue without evidence that it actually causes problems in the experiments, and the global normalization is a standard design choice.
- *"The claim that previous approaches use 'unrealistic benchmarks' is overstated."* — Removed: this is a subjective opinion about framing; the paper's characterization is defensible within its own argument.
- *"The method's components are insufficiently justified."* — Downgraded to Minor (point 2): the criticism has merit but the method is a secondary contribution; the paper does provide a clear conceptual motivation (preventing energy mixing).
- *"Hyperparameter values not reported."* — Removed as a reproducibility nitpick per instructions; folded into the sensitivity analysis point (Minor, point 5).
- *"The LastFM Asia / High School Contact degree distribution comparison is weak."* — Removed: the paper acknowledges the limitations (Appendix A) and provides a reasoned justification based on Dunbar et al. (2015). The comparison serves as supporting evidence, not a central claim.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unanticipated synthesis that the paper itself does not already articulate.

## Suggestions

1. Clarify the scope of "realistic settings" by distinguishing between the Cora/LastFM Asia benchmarks (spreading mechanism realistic, features synthetic) and the COVID-19 dataset (both realistic). A one-sentence disclaimer in Section 5.1 would suffice.
2. Add a brief comparison of at least one alternative similarity function and one alternative consistency measure in an appendix, or acknowledge the absence as a limitation.
3. Correct the ablation claim about GNNSAFE correspondence — either directly compare against GNNSAFE's actual recurrence in the same setting, or rephrase to say the variant "uses only graph structure" without claiming equivalence to GNNSAFE.
4. Add paired significance tests (e.g., Wilcoxon signed-rank) for the main spreading OOD results where margins are small.
5. Include a sensitivity analysis of α, β, ε, and K for at least one dataset in an appendix.

## Score and Decision

This is primarily a benchmark/task-formulation paper, and its strongest contribution is the spreading OOD detection formulation plus the COVID-19 dataset. These contributions are well-motivated, clearly formalized, and fill a genuine gap. The method (EDBD) is a reasonable baseline that consistently outperforms prior approaches, and the ablation confirms its components matter. The weaknesses — synthetic features on non-COVID datasets, heuristic design choices without alternative comparisons, imprecise ablation claim, and missing significance/sensitivity analyses — are real but minor relative to the core contribution. None invalidate the paper's claims or significance. With modest revisions addressing the precision of the ablation claim and the scope of the realism claims, the paper would be a clean contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>