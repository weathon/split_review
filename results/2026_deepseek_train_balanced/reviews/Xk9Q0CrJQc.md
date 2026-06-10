## Summary

This paper identifies and characterizes three types of distribution shifts (element type, force-norm magnitude, and graph connectivity) that degrade the performance of machine learning force fields (MLFFs), even for large foundation models. To mitigate these shifts, the authors propose two test-time refinement strategies: (1) test-time radius refinement (RR), which adjusts the radius cutoff of test graphs to match the training Laplacian eigenvalue distribution and can be applied to any existing radius-graph MLFF; and (2) test-time training (TTT), which uses a cheap physical prior to update representation parameters at test time, requiring a custom pre-training procedure. Experiments on SPICE→SPICEv2 and MD17 benchmarks show that both methods can reduce out-of-distribution errors.

## Strengths

- **Systematic, empirically-grounded taxonomy of three orthogonal distribution shifts in MLFFs.** The paper identifies and formalizes feature shifts (new elements), label/force-norm shifts, and connectivity/graph-structure shifts as distinct failure modes. The diagnostic evaluation of four large foundation models (MACE-OFF, MACE-MP, EquiformerV2, JMP) in Figure 2 concretely shows 2–10× larger force MAE on out-of-distribution systems despite their massive scale. This goes beyond prior work that typically studies generalization in an aggregated way.

- **Test-time radius refinement (RR) is a simple, practical, post-hoc fix for connectivity shifts.** The method adjusts the test-time radius cutoff to match the training Laplacian eigenvalue distribution (Section 3.1). It can be applied to *any* existing radius-graph MLFF (including MACE-OFF and JMP) with minimal CPU cost, virtually never deteriorates performance, and effectively mitigates connectivity distribution shifts (Figure 6, Table 1). This combination of universal applicability, zero retraining cost, and clear scope is the paper's cleanest contribution.

- **TTT enables stable MD simulations under extreme distribution shifts.** In Section 4.2, a GemNet-dT model trained on only 3 molecules (aspirin, benzene, uracil) produces stable, quantitatively accurate simulations of unseen naphthalene and toluene only when TTT is applied. Without TTT, simulations remain unstable even after reducing the timestep by a factor of 5,000 (Figure 8). This demonstrates a genuine capability that standard supervised training alone does not provide.

- **Principled adaptation of test-time training from computer vision to MLFFs using cheap physical priors.** The paper correctly identifies that naive TTT fails for MLFFs and develops a pre-training/freeze/fine-tune or joint-training strategy that forces the main task head to rely on features learned from the prior (Section 3.2). The use of sGDML as a prior that evaluates thousands of structures per second on CPU makes the approach practical.

- **Established reproducible benchmarks for MLFF generalization.** The SPICE→SPICEv2 distribution shift benchmark (10k new molecules) and the extreme MD17 benchmark (3 training molecules → unseen molecules) are clearly defined and publicly reproducible protocols that fill a gap in standardized generalization evaluation for MLFFs.

## Weaknesses

### Fatal
None.

### Major

- **The "order of magnitude" improvement claim in the abstract is misleading given the right-skewed distribution of improvements.** The abstract states that "test-time refinement strategies can reduce force errors by an order of magnitude on out-of-distribution systems." However, the paper itself reports that improvements are "right-skewed, meaning many molecules show small improvements while some see large gains" (§4.1). The 10× improvements appear to be driven by specific molecules in the tail of the distribution. The paper does not report the *median* or *mean* improvement across all OOD molecules, only aggregate metrics (Table 1) and top-10% highlights (Figures 5b, 6b, 7b). The claim that "more than 8,000/10,000 molecules have errors below 25 meV/Å" is given without the corresponding baseline — how many were below that threshold *without* refinement? Without distributional statistics, a practitioner cannot know whether the typical molecule sees a 2× improvement, a 10% improvement, or no improvement at all.

- **Missing standard supervised learning baseline for GemNet-T.** The paper compares GemNet-T (pre-trained on sGDML prior, frozen, fine-tuned on DFT) vs. GemNet-T + TTT, which *does* isolate the effect of the TTT step. However, there is no comparison to a GemNet-T model trained via standard supervised learning (no prior pre-training, no TTT). This makes it impossible to assess how much improvement comes from the multi-task pre-training itself versus the TTT updates. It also leaves unclear whether the prior pre-training alone (without TTT) outperforms standard training. Adding this baseline would cleanly separate the regularization benefit of pre-training from the test-time adaptation benefit of TTT.

### Minor

- **TTT cannot be applied to the foundation models whose failures motivate the paper, and this limitation is relegated to a single sentence.** The paper's central motivation (Section 2, Figures 2a–2d) is that large foundation models suffer from distribution shifts. Yet TTT "will not work on a model that has only been trained on reference calculations" (§3.2, line 137) — i.e., it cannot be applied to MACE-OFF, MACE-MP, EquiformerV2, or JMP because they were not pre-trained with a cheap prior head. Only RR can be applied post-hoc to these models, and RR addresses only connectivity shifts (not force-norm or element shifts that Figures 5 and 7 also show are critical). The scope limitation should be stated more prominently in the abstract and introduction, not deferred to a note in §3.2.

- **The MD17 extreme generalization experiment (§4.2) evaluates only 2 test molecules (naphthalene and toluene).** While the simulation stability results are visually compelling, the tiny test set limits generalizability. Are these results representative of other unseen molecules? A broader evaluation (e.g., other MD17/MD22 molecules) would substantially strengthen the evidence.

- **The connectivity heuristic (55% of Laplacian eigenvalues in [0.9, 1.1]) lacks theoretical justification and robustness analysis.** The paper states this percentage is "consistently around 55%" for several datasets, but no justification is given for why 55% is the right target or why the interval [0.9, 1.1] was chosen. A sensitivity analysis varying the interval bounds would strengthen the heuristic.

- **No quantitative force MAE numbers are reported for the MD17 simulation experiment (§4.2).** The results are presented only as a qualitative figure (Figure 8) showing interatomic distance distributions. Quantitative metrics (e.g., force MAE before/after TTT for the test molecules, bond-length RMSE over trajectories) would substantially strengthen the evidence.

- **RR and TTT are never applied to a common architecture for comparison.** RR is evaluated on MACE-OFF (and JMP), while TTT is evaluated on GemNet-T. Even though the paper does not claim a head-to-head comparison, applying RR to GemNet-T (or TTT to a small MACE model retrained from scratch) would help practitioners assess which method to use in which scenario.

### Trivial

- Typo in Equation 5: $\hat{\mathbf{F}}_{\mathrm{i}}^{1}$ should be $\hat{\mathbf{F}}_{\mathrm{i}}^{P}$ (superscript "1" instead of "P").

## Nice-to-Haves

- Report distributional statistics (median, interquartile range) for improvements rather than only top-10% highlights.
- Add the standard supervised GemNet-T baseline (no prior pre-training) to cleanly separate pre-training effects from TTT effects.
- Provide the count of molecules below 25 meV/Å *before* refinement, alongside the "more than 8,000/10,000" figure after refinement.
- Include a sensitivity analysis of the connectivity heuristic (varying the [0.9, 1.1] interval bounds).
- Add quantitative force MAE and trajectory stability metrics for the MD17 simulation experiment.
- Evaluate TTT with a simpler prior (e.g., Lennard-Jones, GFN2-xTB) to demonstrate robustness to prior choice.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No reported comparison to a GemNet-T model trained with the same pre-training procedure but without the TTT step"** — Factually incorrect. The paper compares "GemNet-T" (pre-trained + fine-tuned, no TTT) against "GemNet-T + TTT" in Figures 5–7 and references Tables 2–3. This is the exact ablation the critic claims is missing. The valid residual concern (no standard supervised baseline) is retained in Major weaknesses.

- **"Apples to oranges comparison (MACE-OFF+RR vs. GemNet-T+TTT)"** — The paper does not claim a head-to-head comparison of RR vs. TTT. These methods are presented for different scenarios: RR is a post-hoc fix applicable to any existing model; TTT requires custom training. The paper states this distinction clearly. Criticizing the lack of a common-architecture comparison is a reasonable suggestion (moved to Nice-to-Haves), but framing it as an "apples to oranges" flaw misreads the paper's structure.

- **"RR changes graph connectivity — no guarantee the resulting graph is physically meaningful"** — Speculative concern. The paper notes performance "virtually never deteriorates" because one can always revert to the training cutoff (line 103). No evidence of physically meaningless graphs is presented, and no experiment demonstrating such a failure is cited. This is a hypothetical risk, not a verified weakness.

- **"MACE-MP evaluated on its training set"** — The paper explicitly acknowledges this limitation: "This model does not have a clear validation set, as it was trained on all of the data" and "The performance deterioration would be more severe with a held-out test set" (line 67). The criticism merely restates something the authors already disclose.

- **"Missing comparison of TTT to fine-tuning on small DFT data or ensembles"** — Scope creep. The paper proposes specific test-time methods that *do not use ab initio labels*; comparing against methods that require new DFT labels is outside the stated scope.

- **"sGDML prior requires training on DFT data"** — The paper acknowledges this and mentions Lennard-Jones and semi-empirical potentials as alternatives that require no DFT training (line 137). The paper explicitly states the prior choice is flexible.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper that the authors do not already state or imply in their own discussion of limitations (right-skewed improvements, TTT's scope restriction, pre-training vs. TTT entanglement). The key synthesis from the reviews is that the abstract's "order of magnitude" framing is not well-calibrated with the paper's own honest reporting of right-skewed improvements — a rhetorical gap rather than a scientific insight.

## Suggestions

1. Qualify the "order of magnitude" claim in the abstract to reflect that improvements are right-skewed and largest gains occur in a fraction of molecules; report median/mean improvement across all molecules.
2. Add a "GemNet-T (standard supervised)" baseline — a model trained from scratch on DFT labels with no prior pre-training — to separate pre-training effects from TTT effects.
3. Report the baseline count (before refinement) alongside "more than 8,000/10,000 molecules have errors below 25 meV/Å" so readers can assess the absolute improvement.
4. Move the TTT scope limitation ("will not work on models trained only on reference calculations") from a footnote in §3.2 into the abstract and introduction.
5. Add quantitative force MAE and stability metrics for the MD17 simulation experiment.
6. Apply RR to the GemNet-T model and report results, enabling a cleaner comparison of the two methods on a common architecture.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>