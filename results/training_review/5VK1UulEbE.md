Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes FredNormer, a plug-and-play frequency-domain normalization module for non-stationary time series forecasting. It first provides a theoretical analysis showing that time-domain normalization uniformly scales all non-zero frequencies without changing their relative proportions, motivating a frequency-aware approach. FredNormer then uses a Coefficient-of-Variation-based stability metric (computed over the training set) to identify stable frequency components, followed by a learnable linear weighting layer that adjusts DFT coefficients before transforming back to the time domain. Experiments on seven datasets with DLinear, PatchTST, and iTransformer backbones show consistent improvements over unnormalized baselines and competitive results against RevIN and SAN.

## Strengths

- **Consistent and sizable empirical improvements across diverse backbones and datasets.** On the highly non-stationary ETTm2 dataset, FredNormer reduces the averaged MSE from 0.420 to 0.280 (33.3%) for PatchTST and from 0.633 to 0.283 (55.3%) for iTransformer (Table 1). Improvements are consistent across all seven datasets tested.

- **Plug-and-play design with demonstrated compatibility.** FredNormer is a model-agnostic input transformation that can be combined with existing normalization methods (e.g., SAN in the "Ours*" condition) to further improve results, as shown in Table 2. It operates solely on the input and requires no architectural changes to backbones.

- **Well-motivated frequency-domain framing.** The observation that time-domain normalization treats all frequency components uniformly is correctly formalized (Lemma 1), and the CV-based stability metric provides a natural, dimensionless way to quantify which frequencies carry consistent signal across training samples. The visualization in Figure 4 supports that the metric assigns higher weights to consistently reproducible components even when their amplitude is low.

- **Efficiency advantage over SAN.** Running time comparison (Figure 5) shows FredNormer is consistently faster than SAN across datasets and forecasting horizons, which is relevant given that SAN is positioned as the SOTA normalization baseline.

- **Ablation against alternative frequency selection strategies.** The ablation study (Table 4) shows the proposed stability metric outperforms both low-pass filtering and random frequency selection (from FEDformer) on all tested settings, confirming that the stability criterion adds value beyond naive filtering.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison: PatchTST results against RevIN and SAN are not reported.** The paper states that three backbones (DLinear, PatchTST, iTransformer) were used to evaluate all three normalization modules (FredNormer, RevIN, SAN), but Table 2 — the primary comparison table against existing normalization methods — only includes DLinear and iTransformer. PatchTST results against RevIN and SAN are absent from the paper. Since PatchTST is one of the two primary backbones in Table 1 and the paper emphasizes "model-agnostic" generality, this omission significantly weakens the claim of comprehensive evaluation. PatchTST is only shown in the "Ours vs. no normalization" comparison (Table 1).

- **The 1D differencing applied before DFT is neither ablated nor evaluated.** Algorithm 2 and Section 3 state that a 1D-difference operation is applied to the input sample before the DFT. The paper's only justification is "to smooth the data" (line 294). There is no ablation study that removes or replaces this operation, no analysis of how much of the improvement stems from differencing vs. the stability weighting, and no clarification of whether the differencing is also applied to the inputs of RevIN/SAN baselines. If differencing is unique to FredNormer, its contribution to the reported gains is unknown. This is a genuine methodological gap that affects interpretability of all results.

### Minor

- **The theoretical analysis is straightforward and does not justify the method's superiority.** Lemma 1 (normalization uniformly scales non-zero frequencies) and Theorem 1 (the proportion of a frequency subset's energy to the total is unchanged) follow directly from the linearity of the Fourier transform. This is a correct observation but falls short of a "theoretical analysis" that explains *why* the method works or provides design guidance. The paper also overstates the implication: uniform scaling does not prevent a model from learning frequency-specific weights downstream, as the model's ability to distinguish components depends on the learned representation, not on whether input frequencies were scaled uniformly. The theory is best understood as motivation, not as a proof of necessity.

- **The claim that the weighting layer introduces "sample-specific variation" is overstated.** The weighting coefficients \((\mathbf{S} \times \mathbf{W}_r + \mathbf{B}_r)\) depend on the pre-computed dataset-level stability metric \(S\) and learned parameters \((\mathbf{W}_r, \mathbf{B}_r)\) that are shared across all samples. Every sample's DFT coefficients are multiplied by the *same* weight vector. The only per-sample variation is that each sample has different DFT coefficients — the weighting itself is static. This is more accurately described as a static frequency filter learned from dataset-level statistics, not an operation that introduces sample-specific variation.

- **Method notation contains unresolved ambiguities.** The stability metric \(S\) is defined as \(\mathbb{R}^{K \times C}\) (line 276), but the linear projection in Eq. (8) multiplies \(\mathbf{S} \in \mathbb{R}^{K \times C}\) by \(\mathbf{W}_r \in \mathbb{R}^{K \times 1}\) using "\(\times\)" — standard matrix multiplication is dimensionally incompatible here (inner dimensions \(C\) and \(K\) do not match). The intended operation (likely a broadcast or per-frequency projection) is not clearly specified. Algorithm 2's pseudocode (lines 237-241) similarly uses "linear_r(S)" inside a per-frequency loop, which is ambiguous about how \(S\)'s channel dimension is handled.

- **Ablation study is limited in scope.** Table 4 only tests three datasets (ETTh1, ETTm1, Weather) with two forecasting horizons and two backbones, comparing against only a low-pass filter and random frequency selection. Stronger baselines are not considered, such as: selecting frequencies by average amplitude (energy-based filtering), using the stability metric without the learnable projection, or using random but fixed (non-learned) weights. The ablation also excludes the datasets where the largest gains are reported (ETTm2, Traffic).

- **No statistical significance testing.** Many of the improvements over SAN in Table 2 are small (e.g., iTransformer+Ours 0.376 vs. iTransformer+SAN 0.392 on ETTh2). Without statistical tests or confidence intervals, it is unclear which gains are robust.

### Trivial
- The running time comparison (Figure 5) compares against SAN but not against RevIN, which is the simplest and fastest baseline. Since RevIN adds near-zero overhead, reporting its runtime would make the efficiency claim more complete.
- Algorithm 2 computes DFT per-sample inside the training loop, but the paper does not discuss whether this adds meaningful overhead during training (though the running time analysis partially addresses this).

## Nice-to-Haves
- An ablation study removing the 1D differencing to measure its contribution.
- PatchTST results against RevIN and SAN to complete the comparison.
- A comparison against frequency selection by average amplitude (energy-based) to further validate the stability metric's advantage.
- An analysis linking dataset-specific performance gains to frequency characteristics (e.g., distribution of stability values).

## Removed Points

These points have been removed or modified from the reviewer critiques, with brief justification:

1. **"The theoretical analysis is a non sequitur — uniform scaling does not prevent a model from learning frequency-specific weights downstream"** — Kept in modified form in Minor Weaknesses. The original harsh critique overstated this; the paper uses the theory as motivation, not a formal impossibility result. However, the analysis is indeed trivial and over-claimed, which is retained.

2. **"Improvement percentages are misleading because base MSEs are high"** — Removed. Reporting both absolute MSE and relative improvement is standard practice. The base MSEs (e.g., PatchTST 0.420 on ETTm2) are not unusually high for this dataset without normalization.

3. **"Fredformer distinction is unclear"** — Removed. The paper's characterization of existing frequency methods as "costly and architecture-specific" is a reasonable distinction. The paper is about normalization, not about frequency-domain model architectures.

4. **"Experiment details missing (hyperparameters, learning rate)"** — Removed as a nitpick. The paper states parameters are the same as in Table 1 and reports averaged results with standard deviations.

5. **"Ours* counts toward headline totals"** — Removed as a substantive criticism. Table 2 clearly separates "Ours" and "Ours*" columns, and the paper explicitly states "Ours* represents the results where both FredNormer and SAN are used." The transparency is adequate.

6. **"Low-pass filter is a weak ablation baseline"** — Weakened. The ablation does show FredNormer outperforming both low-pass and random selection consistently. The issue is more about limited scope (3 datasets vs. 7, missing stronger alternatives) than about the baseline being weak per se.

7. **From Strength Finder: "Comprehensive ablation"** — Moved here. The word "comprehensive" conflicts with the verified weakness about limited scope. The ablation is present but not comprehensive.

## Novel Insights

None beyond the paper's own contributions. The reviews raise legitimate concerns about evaluation completeness and presentation accuracy, but they do not uncover a surprising structural insight about the method or the problem that the paper itself misses.

## Suggestions

1. **Complete the missing experiments:** (a) Add PatchTST results against RevIN and SAN to Table 2 (or a supplementary table). (b) Add an ablation condition "FredNormer w/o 1D-differencing" to Table 4 to isolate the contribution of the differencing operation. (c) If differencing is essential, apply it consistently to baseline inputs for fairness, or explicitly acknowledge the asymmetry.

2. **Clarify the notation in Eq. (8) and Algorithm 2:** The shape mismatch between \(S \in \mathbb{R}^{K \times C}\) and \(\mathbf{W}_r \in \mathbb{R}^{K \times 1}\) should be resolved. If the operation is a per-frequency projection of the \(C\)-dimensional channel vector to a scalar weight, this should be explicitly described. If the channel dimension is handled by broadcasting, state this clearly.

3. **Tone down the "sample-specific variation" claim** or provide evidence that the weighting truly varies per sample beyond the trivial fact that each sample has different DFT coefficients.

4. **Reframe the theoretical contribution** as "motivating observation" rather than "theoretical analysis that proves a limitation," since the lemmas are basic consequences of DFT linearity and do not provide design guidance for the method.

5. **Expand the ablation study** to include (a) energy-based frequency selection, (b) stability metric without the learnable projection, and (c) testing on ETTm2/Traffic where the largest gains are claimed.

## Score and Decision

The paper addresses a legitimate problem — the insensitivity of time-domain normalization to frequency-specific structure — and proposes a simple, efficient, empirically effective solution. The core empirical results on DLinear and iTransformer are solid and consistent. However, the evaluation has notable gaps: the most important comparison (FredNormer vs. RevIN/SAN on PatchTST) is missing, the 1D differencing operation is not ablated, and several presentation claims are overstated. These issues are resolvable but prevent the paper from being fully convincing in its current form. The theoretical framing is modest, and the method description has unresolved ambiguities.

The paper makes a real contribution but requires substantial additional experimental validation to fully substantiate its claims. The missing PatchTST comparison and unevaluated differencing are not fatal — the method demonstrably works on the two backbones tested — but they are significant enough to affect confidence in the "fully model-agnostic" claim.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>