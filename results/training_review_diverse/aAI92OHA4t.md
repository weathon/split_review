Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces "soft checksums" for detecting out-of-distribution (OOD) predictions in regression surrogate models, particularly for scientific ML applications. The method adds a single check node to the neural network's output layer and trains the model to output a checksum function of its own predictions. Violation of this checksum — computed in a single forward pass with negligible overhead — serves as a signal that the input may be OOD and the prediction untrustworthy. Experiments on an 87-dimensional atomic physics surrogate (NLTE calculations) show FNR99 values as low as 1.64% with a sinusoid checksum.

## Strengths

- **Novel conceptual connection between checksums and OOD detection.** The paper draws a clean analogy between error-detecting checksums in communication and OOD detection in regression, translating a mature idea into a new domain. The method requires only one additional output node and one forward pass, making it lightweight compared to ensembles or Bayesian methods (Section 3.1, lines 55–56, 112–116).

- **Quantitative evidence of ID/OOD separation.** Table 1 reports FNR99 values across four loss configurations, with the best configuration (including L_OOD, excluding L_ID) achieving 4.76% (linear checksum) and 1.64% (sinusoid checksum). This demonstrates that the checksum error can separate ID from OOD predictions with reasonably low false-negative rates at a 99% true-negative threshold.

- **Loss design with OOD exposure improves detection.** The paper shows that adding L_OOD (a reward term for high checksum error on OOD data) consistently improves FNR99 compared to the baseline prediction + checksum loss alone — from 8.93% to 4.76% for linear, and from 3.84% to 1.64% for sinusoid (Table 1). This validates the use of outlier-exposure-style training for regression OOD detection.

- **Demonstrated correlation between checksum error and prediction error on OOD data.** Figure 2 shows a positively correlated relationship, suggesting the checksum error may serve as a continuous proxy for prediction error, not just a binary OOD flag. This adds utility beyond simple detection.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to any baseline or existing OOD detection method.** Table 1 and Figure 2 report results only for variants of the checksum loss itself. There is no comparison to any existing method — not a simple baseline (e.g., distance to nearest training point in latent space, prediction variance), nor a standard approach (e.g., MC dropout, deep ensembles, anchor-based methods that the paper cites in §2). Without baselines, the reader cannot assess whether FNR99 values of 1.64%–8.93% are strong or weak. The paper itself acknowledges this gap (line 266: "we must also conduct benchmark comparisons to establish the relative effectiveness"), but this admission does not remedy the absence. For a paper presenting a new method, the lack of any comparative evaluation is a central evidentiary gap that prevents acceptance as a validated contribution.

### Minor

- **Ambiguous separation between OOD training samples and OOD evaluation set.** The paper states that for L_OOD training it "sample[s] a subset of D_OOD with values between 20% to 25% outside of the hypercube" (line 203), while the OOD evaluation set is described as being split from the same D_OOD by a dividing line in the density-temperature plane (lines 187, 195–198). It is not explicitly stated whether the OOD evaluation set excludes the points used during training. If there is overlap, the FNR99 results for conditions including L_OOD would be artificially optimistic and potentially invalid. This ambiguity must be clarified.

- **Single dataset limits evidence scope.** Results are demonstrated on one physics dataset (NLTE atomic physics surrogates) with one OOD split (density-temperature dividing line). While the paper acknowledges this limitation (lines 265–280), for a method described as "general-purpose" (abstract, line 56), evidence on additional datasets or different OOD constructions would substantially strengthen the case. The paper also notes that hypercube-based OOD sampling "misses potential OOD regions within the hypercube" (line 278), but does not test detection of such interpolation gaps.

- **Quantitative correlation between checksum error and prediction error is missing.** Figure 2 qualitatively shows correlation, but no Pearson or Spearman coefficient is reported. This would strengthen the claim that checksum error serves as a continuous proxy for prediction error (§5, line 218).

- **Hyperparameter sensitivity is not explored.** The paper reports hyperparameters (λ_ID = λ_OOD = 0.01, w = 0.0001) from a "limited parameter sweep" (line 200) but does not show how FNR99 varies with these values. Without this, it is unclear whether the method is robust or brittle to these choices.

- **Design of L_OOD as an inverse MSE (Eq. 6d) receives no discussion of gradient behavior.** The inverse form means gradients are largest when the checksum error is smallest (near zero), which could create training instability. The paper notes the ε term to avoid division by zero (line 159) but does not discuss whether this loss term caused practical stability issues, nor justify this design over simpler alternatives (e.g., a negative MSE term or margin-based loss).

### Trivial
None.

## Nice-to-Haves

- **Quantitative correlation coefficient** (Spearman's ρ) between checksum error and prediction error for Figure 2.
- **Sensitivity analysis** showing how FNR99 varies with λ_ID, λ_OOD, and sinusoid frequency w.
- **Testing on an additional dataset** or OOD construction (e.g., interpolation gaps inside the hypercube) to broaden evidence.
- **Testing a physical conserved quantity as a natural checksum** (mentioned as a possibility on lines 129–130 but not implemented).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing training details (architecture, optimizer, etc.)"** — The reviewer notes that model architecture, optimizer, learning rate, epochs, and random seeds are not reported. These details would ordinarily appear in an appendix, which the parser strips from all submissions. Per instructions, such criticisms about missing appendix content are removed.

- **"Single dataset and arbitrary OOD split limit generalizability" (as a fatal/major claim)** — While the single-dataset scope is a real limitation, the paper explicitly scopes itself to the physics surrogate domain and acknowledges the limitation. Moved from "major" to "minor" in the main review above.

- **"L_OOD gradient blowup" overstatement** — The harsh critic stated the loss "blows up" as checksum error approaches zero. In fact, the loss goes to λ_OOD/ε (a finite value), and the gradient is -λ_OOD/(x+ε)² (also finite at x=0). The concern is not about blowup but about potential stability with very small ε. This is already captured in the minor weakness above with corrected language.

- **"Missing related works"** — Per instructions, I cannot confirm the existence of missing related works, so this is removed.

- **"Reproducibility nitpicks about undisclosed hyperparameters"** — Hyperparameter details (λ_ID, λ_OOD, w, batch size) are reported (lines 202–204). Further granularity (e.g., complete training logs) is impractical for a submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the paper's main strengths and weaknesses clearly: the core idea is novel and well-motivated, but the experimental validation is incomplete without baselines. The finding that L_ID hurts performance (Table 1) is an interesting observation from the paper itself, but neither reviewer develops this into a deeper insight beyond what the authors already note about conflicting training targets.

## Suggestions

1. **Add baseline comparisons** — Even a single simple baseline (e.g., distance of latent embedding to nearest training point, or prediction variance from a tiny 3-model ensemble) would immediately contextualize the FNR99 values and transform the paper from a proposal into a validated method. This is the single highest-leverage improvement.

2. **Clarify the OOD training/evaluation split** — State explicitly whether the subset of D_OOD used for L_OOD training (20–25% outside the hypercube) overlaps with the OOD evaluation set. If disjoint, say so. If not, re-run experiments with disjoint sets.

3. **Report variance across multiple runs** — The current results appear to be from a single run (or at least no variance is reported). Showing that the best FNR99 is stable across different initializations would increase confidence.

4. **Add a quantitative correlation coefficient** to Figure 2 to support the claim that checksum error is a continuous proxy for prediction error.

## Score and Decision

**Originality:** High — the checksum framing for OOD detection in regression is genuinely novel.
**Importance of research question:** Medium-High — detecting unreliable predictions from surrogate models is practically important in scientific simulation.
**Claims well supported:** Low-Medium — the core claim (soft checksums can separate ID/OOD) is supported, but without baselines the effectiveness relative to alternatives is unknown.
**Soundness of experiments:** Low-Medium — one dataset, no baselines, ambiguous OOD split, no variance reporting.
**Clarity of writing:** Good — the method description and motivation are clear.
**Value to the research community:** Medium — an interesting idea that could be impactful with stronger validation.

The paper introduces a genuinely novel and elegant concept, but the experimental validation is insufficient for acceptance at a competitive venue. The lack of any baseline comparison is the central issue — without it, the reader cannot assess whether the reported FNR99 values represent a meaningful advance. The remaining issues (ambiguous OOD split, single dataset, missing variance) are addressable. I recommend rejection with a clear path to revision, as the core method is worth pursuing.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>