Now I have a thorough understanding of the paper and can construct the consolidated review.

## Summary

SwitchLoss proposes switching between three loss functions (MSE, JSD, STD_loss) during neural network training for imbalanced regression. The method runs multiple exploration cycles (100 for SwitchLoss, 32 for SwitchLossR), each with a randomized loss-switching schedule, and selects the best-performing model. The restricted variant SwitchLossR fixes MSE at every other switch. Evaluated on 22 datasets (standard, high-dimensional synthetic, image) across 4 architectures plus ResNet.

## Strengths

**1. Novel approach to imbalanced regression through loss-function switching.** Replacing a static loss with random switching among MSE, JSD, and STD_loss during training is genuinely different from existing resampling (SMOGN) and cost-sensitive (DenseLoss) methods. The approach is clearly described in Section 3.3 and Procedure 1, with the loss set defined in Equation 4.

**2. Evidence across diverse datasets and multiple architectures.** The method is tested on 15 standard tabular datasets, 5 synthetic high-dimensional datasets, and 2 image datasets (AgeDB, IMDB-WIKI), using 4 different feedforward architectures plus deep ResNet. Table 1 shows SwitchLoss variants winning the most datasets across architectures, and Table 2 shows per-region (many/medium/few-shot) RMSE improvements on the image datasets — a stronger signal than overall error alone.

**3. Concrete quantification of the core claim.** Figure 2 shows SwitchLoss achieving ~50% lower validation error than MSE (Figure 1) on the Accel dataset with the same number of epochs. Red dots mark switching epochs, directly connecting the loss-switching mechanism to the observed performance gain (discussed in Section 5).

**4. SwitchLossR provides a practical computational trade-off.** The restricted variant reduces the search space from 3^#switches to 2^(#switches/2) schemes (Section 3.3.1) while remaining competitive — winning nearly half of standard datasets (Table 1 discussion in Section 5) and outperforming SMOGN and MSE on image datasets (Table 2).

**5. Evaluation on high-dimensional settings where SMOGN is known to struggle.** The paper tests on 5 high-dimensional synthetic datasets where SMOTE-based methods introduce bias (Blagus & Lusa, 2013, cited in Section 5). SwitchLoss wins 75% of these cases (Section 5), suggesting it addresses a known weakness of resampling methods.

## Weaknesses

### Fatal
None.

### Major

**1. Missing critical baselines and overclaimed scope.** The paper claims SwitchLoss "surpasses prevailing state-of-the-art techniques dedicated to imbalanced regression" (abstract) and "outperforms other existing techniques" (conclusion), but compares only against MSE and SMOGN. DenseLoss (Steininger et al., 2021), which the paper itself cites as a "promising approach" (Section 2), is never evaluated. Weighted MSE and other simple cost-sensitive adaptations are also absent. The results may be genuine, but the claim of surpassing "state-of-the-art" cannot be supported without comparing against the methods the paper positions as the main competitors.

**2. Unfair computational comparison.** SwitchLoss runs 100 (or 132 combined) full training cycles and picks the best model; SMOGN and MSE each run one. The paper acknowledges this (Section 5: "speed of execution... follows a time complexity of O(e)") but does not control for it — e.g., by giving baselines multiple random restarts or tuning. Without controlling for compute budget, it is unclear whether the improvement comes from the switching mechanism or simply from the 100× larger search over random initializations/schedules.

**3. No statistical rigor in results.** Table 1 reports only a coarse "winner-per-dataset" count, discarding the magnitude of improvements. No confidence intervals, standard deviations, or repeated runs are reported for any experiment. Table 2 reports single RMSE values without variance. Given the random exploration stage, it is essential to know whether the reported advantages are statistically significant or within the noise of random seed variation.

**4. Underspecified implementation of key loss functions.** The paper defines JSD (Equation 2) in the abstract as a divergence between probability distributions, but never specifies how it is estimated from mini-batches during training — no mention of histogram binning, kernel density estimation, or any procedure to convert continuous predictions into distributions. Similarly, STD_loss (Equation 3) is the absolute difference between batch-level standard deviations of predictions and targets, which is highly sensitive to batch size and could be zero even with poor individual predictions. These are not hyperparameter details; they are core design choices needed to understand and reproduce the method.

**5. Mismatch between "two-stage" framing and actual algorithm.** Section 3.1 and the Conclusion describe a nested two-stage process where the first stage explores schemes and "the second stage, traditional training, then optimizes the neural network's parameters using the selected scheme." However, Procedure 1 does not implement a separate second stage — it returns the best model found during the exploration cycles. The actual algorithm is random search over switching schedules with model selection, not the sequential exploration-then-training procedure described in the text. This framing is misleading about what the method does.

### Minor

**1. No justification for the choice of loss functions.** Section 3.3 provides intuition (MSE for fit, JSD for distribution matching, STD for spread) but no theoretical or empirical evidence that these three are the right functions to combine, or that the specific set is better than alternatives (e.g., weighted L1, quantile loss, asymmetric loss).

**2. SwitchLossR design rationale is unsubstantiated.** Section 3.3.1 states "we observed that employing a fixed MSE loss for every other switch... yielded comparable results" but provides no data or analysis to support this claim. The observation is presented as an empirical finding without supporting evidence.

**3. No ablation on the number of exploration cycles.** The paper uses 100 cycles for SwitchLoss and 32 for SwitchLossR without showing how performance varies with this parameter. Section 5 acknowledges "a more exhaustive exploration stage" could help but provides no analysis of diminishing returns.

**4. Under-explored failure modes.** Section 5 notes that "for less skewed distributions, the regular mean-squared error more frequently outperforms SwitchLoss" but does not analyze this systematically or provide diagnostic criteria.

### Trivial
- Procedure 1 refers to "test data set" for validation (line 69), which is terminologically confusing given the paper later distinguishes validation and test sets.
- Tables are embedded as images, making individual values hard to extract.

## Nice-to-Haves
- **Single-run adaptive switching**: The paper's thesis would be stronger if switching were triggered by a principled criterion (e.g., validation plateau, gradient alignment) rather than random pre-determined schedules, to demonstrate that switching itself (not schedule search) drives improvement.
- **Compute-controlled comparison**: Running baselines with 100 random restarts (matching SwitchLoss's budget) would clarify whether the advantage is from switching or from more trials.
- **Ablation of each loss function**: Does JSD alone help? STD alone? Or is the combination synergistic?
- **Error bars on the 22-dataset evaluation** would substantially strengthen the evidence.

## Removed Points

* **"The method does not do what the paper claims — switching happens across runs, not within a single training trajectory"**: This is factually incorrect. Procedure 1 clearly shows loss functions switching at switch epochs *within* each training run (inner loop). Each exploration cycle performs a full training with dynamic mid-training switching. The critic's stronger point about the framing mismatch is kept (Major weakness #5).
* **"Reproducibility: No code... learning rate, optimizer, batch size... not reported"**: Per the removal rules, undisclosed hyperparameters and missing code are nitpicks about reproducibility that should be removed. However, the underspecified JSD computation is kept because it is a core design choice, not a trivial hyperparameter.
* **Missing related work / "omits discussion of cost-sensitive loss functions"**: The paper does discuss DenseLoss (a cost-sensitive method). The critic asks for weighted L1/L2 and quantile loss, which are standard regression tools rather than specific imbalanced regression methods with known citations. Per the "do not mention missing related works" rule, this is removed.
* **"Table 2 is garbled"**: Parser artifact from embedded image; not present in original submission.
* **"The conclusion overstates the evidence"**: While the conclusion's claims are stronger than the evidence warrants (covered by Major #1 about missing baselines), as a standalone criticism it is a rephrasing of other weaknesses.
* **"Figure 2 is a single example, not systematic"**: Kept implicitly in Major #3 (no statistical rigor) rather than as a separate bullet.

## Novel Insights

The harsh critic's framing of SwitchLoss as "random search over loss schedules" is an overly reductive characterization. The actual contribution is more nuanced: the paper shows that *within a single training run*, switching among loss functions with different properties (pointwise accuracy from MSE, distributional alignment from JSD, spread matching from STD) can help escape poor local minima that a static loss gets stuck in — and that this benefit compounds when multiple random schedules are tried. The critic's alternative framing elides the key observation that switching happens *during* training (not just across runs) and that Figure 2 provides direct evidence of instability leading to a better minimum. However, the critic correctly identifies that the evaluation is not yet rigorous enough to support the strong claims made.

## Suggestions

1. **Add DenseLoss and at least one weighted loss baseline** to the evaluation. Without this, the "state-of-the-art" claim is unsupported.
2. **Report results with error bars** (standard deviations over multiple random seeds) for all experiments. Provide a table with mean RMSE ± std rather than only winner counts.
3. **Control for compute**: Run baselines with the same number of random restarts as SwitchLoss exploration cycles, or plot performance as a function of computational budget.
4. **Specify JSD computation precisely**: describe how continuous predictions are converted to distributions per batch (e.g., histogram with fixed binning, kernel density estimate).
5. **Align the paper's framing with the actual algorithm**: either implement a true two-stage procedure (explore schedules, then retrain with the best one) or clearly describe the current approach as random search with model selection.
6. **Add an ablation** showing performance vs. number of exploration cycles to justify the chosen values and demonstrate diminishing returns.

## Score and Decision

**Originality**: The loss-switching approach is genuinely novel for imbalanced regression.  
**Importance of research question**: Imbalanced regression is an important and under-studied problem.  
**Claims support**: Claims significantly outstrip the evidence — missing baselines, no statistical rigor, unfair compute comparison.  
**Soundness of experiments**: The experimental design has several methodological gaps (no error bars, single baselines, underspecified loss computation).  
**Clarity of writing**: Generally clear, but the "two-stage" framing is misleading relative to the actual algorithm.  
**Value to community**: The core idea is interesting and could inspire follow-up work, but in its current form the evidence is insufficient to establish reliability.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>