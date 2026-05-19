- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 6, 8
Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper systematically identifies three types of distribution shifts (element, force norm, connectivity) that cause performance degradation in MLFFs, then proposes two test-time refinement strategies — radius refinement (RR) to adjust the graph connectivity by matching Laplacian eigenvalues, and test-time training (TTT) using cheap physical priors to improve representations. Experiments on large foundation models (MACE-OFF, JMP, EquiformerV2, MACE-MP) demonstrate that even billion-parameter models degrade under these shifts, and the proposed methods mitigate them. The most impressive result is that a GemNet-T model with TTT can enable stable MD simulations of entirely unseen molecules where the same model without TTT fails catastrophically.

## Strengths

1. **Systematic diagnosis of three distinct distribution shift types with concrete evidence.** The paper defines clear criteria for feature, force norm, and connectivity shifts (§2.2), then shows that four large foundation models (MACE-OFF, MACE-MP, EquiformerV2, JMP) suffer 2–10× higher force MAE on out-of-distribution examples (Figure 2). This provides quantifiable evidence that the problem is real and widespread, not a narrow artifact of a single model.

2. **Test-time radius refinement is simple, cheap, and practically useful.** The method (§3.1) adjusts the test-time radius cutoff to align Laplacian eigenvalue distributions with the training distribution. It can be dropped into any existing radius-graph MLFF at negligible extra cost (only eigenvalue computations), and the paper notes it "virtually never deteriorates performance" since one can always revert to the training radius. This is a genuinely novel procedural contribution.

3. **TTT with cheap priors yields substantial empirical gains, including enabling simulations of unseen molecules.** The TTT method (§3.2) improves force errors on the SPICEv2 benchmark and — most compellingly — enables stable MD simulations of entirely unseen molecules (naphthalane, toluene) where the same model without TTT fails even at 5,000× smaller timesteps (§4.2, Figure 8). This establishes a clear and ambitious benchmark for MLFF generalization.

4. **Transparency about the distribution of improvements.** The paper acknowledges that improvements from both methods are right-skewed and shows results for the top 10% of molecules alongside aggregate numbers (Figures 5–7, line 171). This is honest reporting that lets readers calibrate their own expectations.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"Order of magnitude" claim in the abstract is imprecise without qualification.** The abstract claims the methods "can reduce force errors by an order of magnitude on out-of-distribution systems." The aggregate results (Table 1, embedded as an image) show roughly 2× improvement for GemNet-T+TTT and ~1.1× for MACE-OFF+RR. The 10× improvement appears on specific molecules (e.g., new elements — line 165: "sometimes by a factor of 10 for specific molecules"), which the "can" qualifier technically covers, but the abstract does not signal that this applies to a subpopulation rather than typical or average performance. Since the abstract is the most-read part, stating "can reduce" without bounding it risks misleading readers. A simple rephrasing ("can reduce force errors by up to an order of magnitude for the most challenging out-of-distribution molecules") would resolve this.

2. **The eigenvalue heuristic (55% target) for connectivity shifts lacks robustness analysis.** The paper (§3.1, line 101) picks the [0.9,1.1] interval and 55% target based on the observation that "for many molecular datasets (such as SPICE, MD17, and MD22)… this percentage is consistently around 55%." But no table or range is provided in the main text showing what this percentage actually is for each dataset, what happens when the training distribution itself has a different percentage, or how sensitive the method is to targeting 50% vs. 60%. Given that the radius refinement procedure directly hinges on this value, the reader needs more evidence that the 55% target is robust (or that performance degrades gracefully if it varies). The paper leaves a brief note that "investigation of other distance metrics" is future work, but the main claim would be stronger with a simple sensitivity test.

3. **Key experimental details are absent from the main text.** (a) The number of TTT gradient steps per test molecule is not reported — only "taking gradient steps" (§3.2) is mentioned, and the MD17 experiment (§4.2) doesn't state whether one update or many are performed. (b) The specific 10 candidate radii searched over for RR (§3.1, line 156) are not described (e.g., range, step size relative to the training cutoff). (c) While the paper notes priors are computationally cheap, it does not report the actual cost of TTT (GNN forward/backward passes per molecule), which matters for practitioners deciding whether to use it. These omissions reduce reproducibility and practical utility.

### Trivial
None.

## Nice-to-Haves

- **Sensitivity analysis on the OOD threshold.** The paper defines out-of-distribution as >1 standard deviation from the training mean (line 32). Testing alternative thresholds (0.5σ, 2σ) would show the trend is robust.
- **Ablation against simpler TTT baselines.** The paper could compare TTT against fine-tuning the full model (not just the representation) on the prior labels at test time, to justify the separation into frozen/fine-tuned components.
- **Plot of total energy over time for unstable MD17 simulations.** The paper states even 5,000× smaller timesteps don't stabilize the baseline model (§4.2). Showing energy blowup explicitly would make the failure mode concrete.
- **Failure-mode analysis for TTT.** A scatter plot of prior error vs. TTT improvement would help practitioners understand when the method provides little benefit.

## Removed Points

*These points are flagged to be removed from the main review; treat them with caution.*

1. **"TTT dependence on prior/pre-training is understated"** — The paper explicitly states in §3.2 (line 137): "We reiterate that TTT with a prior will not work on a model that has only been trained on reference calculations." This limitation is clearly stated, so the criticism is based on a misreading.

2. **"Confounded comparison between GemNet-T+TTT and MACE-OFF"** — The paper presents both baselines (GemNet-T without TTT, MACE-OFF, MACE-OFF+RR) alongside the TTT result, and the narrative (line 169) simply notes that "TTT with the GemNet-T model performs better than MACE-OFF" — a factual statement about the aggregate numbers. The paper does not claim this is an apples-to-apples architecture comparison.

3. **"How 'new out-of-distribution region' is detected"** — The paper clarifies: "when a new out-of-distribution region is encountered (i.e., when testing is done on a new system)" (§3.2, line 135). This is sufficiently clear.

4. **"The 55% eigenvalue heuristic's motivation is thin"** — The paper provides the motivation: it corresponds to "the mean training Laplacian eigenvalue ± half the standard deviation" (line 101) and is observed consistently across several molecular datasets. The criticism about missing dataset-specific numbers is valid (kept as Minor #2), but the motivation is not "thin."

5. **Criticisms about missing appendix sections or details deferred to the appendix** — The parser strips these sections; they exist in the original submission.

6. **Generic "evaluation lacks rigor" or "could the metric be measuring a proxy" style criticisms** — These are speculative and lack concrete anchors in the paper.

## Novel Insights

The most novel insight from the review process is the observation that the two proposed methods operate at fundamentally different levels of generality: radius refinement is a zero-cost heuristic that can be applied to any existing pre-trained MLFF with no retraining, while TTT offers larger gains but requires the model to have been specifically pre-trained with a prior (and uses a shared representation between prior and main task heads). The reviewers did not identify any fundamental flaw that invalidates this core trade-off, but the lack of even a rough characterization of TTT's computational overhead (seconds per molecule? dominated by GNN or prior?) weakens the practical message. The paper's own strongest evidence — the MD17 experiment where TTT enables stable simulations of completely unseen molecules — is genuinely impressive and sets a useful benchmark for the field.

## Suggestions

1. **Calibrate the abstract claim** to say "up to an order of magnitude" or "by an order of magnitude for the most challenging molecules" to match the aggregate numbers.
2. **Add a small table** showing the 55% eigenvalue percentage range across datasets (SPICE, MD17, MD22) and a brief robustness test (e.g., targeting 50% and 60% instead).
3. **Report the number of TTT gradient steps, learning rate, and per-molecule computational cost** in the main experiments section (§4).
4. **List the 10 candidate radii** used in the RR search and their relationship to the training cutoff.
