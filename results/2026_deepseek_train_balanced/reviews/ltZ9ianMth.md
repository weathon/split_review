## Summary

This paper tackles robust time series forecasting with anomalies (TSFA) by bridging ideas from Learning with Noisy Labels (LNL). It defines three anomaly types (Constant, Missing, Gaussian), analyzes loss robustness (which losses are robust to target-side anomalies) and sample robustness (how anomaly position in the input affects predictions), and proposes RobustTSF — an algorithm combining L1-trend-filter-based sample selection with MAE loss. The key empirical finding is that anomalies near the label (at the "back" of the input window) cause much more degradation than those at the front or middle, motivating a position-weighted scoring scheme.

## Strengths

- **Well-designed controlled experiment revealing that anomaly position matters more than anomaly count (Table 1).** On both Electricity and Traffic datasets, across all three anomaly types and two anomaly rates, anomalies at the "back" position consistently cause substantially larger degradation (e.g., Const. η=0.2 on Traffic: back MAE 0.236 vs. front MAE 0.194) while front/middle positions barely differ from clean training. This finding is the paper's most novel empirical contribution and directly motivates the algorithm's design.

- **RobustTSF achieves consistent improvements across a wide range of settings.** In the main single-step results (Table 2), RobustTSF achieves best MAE/MSE in 26 out of 28 evaluation settings (two datasets × three anomaly types × two rates, plus clean). It also has the lowest Δ stability score (0.004 on Electricity, 0.003 on Traffic), indicating low variance between best and last epoch. This pattern holds for multi-step forecasting (Table 3) and subsequence anomalies (Table 4), where RobustTSF outperforms all baselines in every cell.

- **Ablation study validates the design choices.** Table 5 decomposes each component: MAE consistently beats MSE (Const η=0.3: 0.183 vs. 0.193), Dirac weighting slightly outperforms exponential, and trend-filter detection substantially beats prediction-based detection (Const η=0.3: 0.183 vs. 0.217). This provides evidence that the gains come from specific design choices rather than generic pipeline improvements.

- **Simple and computationally efficient algorithm.** The method avoids the detection-imputation-retraining loop, requiring only an L1 trend filtering solve and sample filtering before standard training. The authors explicitly note this efficiency advantage.

## Weaknesses

### Major

- **Theoretical claim in Proposition 1 is imprecisely stated and the connection to Theorem 1 is incomplete.** Theorem 1 proves that if ℓ(f(x), y) + ℓ(f(x), y^A) = C_x (constant w.r.t. f), then the noisy-risk minimizer equals the clean-risk minimizer. Proposition 1 then asserts "From Theorem 1, MAE is robust to Constant and Missing type anomalies." For MAE with a Constant anomaly (y^A = y + ε), the expression |f−y| + |f−y−ε| is constant w.r.t. f *only* when f is bounded between y and y+ε. Outside this interval, the sum varies linearly with f. The paper provides no justification that the forecaster's outputs are constrained to this interval, nor does it discuss this conditional nature. At best, MAE is *conditionally* robust to Constant/Missing anomalies under a boundedness assumption on f(x) that is neither stated nor proven. This gap does not invalidate the empirical results — MAE may still be approximately robust in practice — but the theoretical framing as a formal guarantee directly from Theorem 1 is overclaimed and needs correction. The paper should either scope the claim explicitly, add a boundedness condition, or present it as approximate robustness with a bound on the gap.

- **"Best epoch" reporting on the test set uses the test set for model selection (Section 6).** The paper states it "follows the evaluation protocol from a prominent benchmark method in LNL" which "records DNN performance on the clean test set at the end of each training epoch, and we report both the best and last epoch test set performances" (lines 287–288). Selecting the epoch with the lowest test error and reporting that value constitutes test-set leakage — the test set is being used to choose the model. The gaps between best and last epoch are material (e.g., Vanilla MAE on Electricity at η=0.3 Constant: best=0.206/0.086 vs last=0.245/0.109; Online on Traffic Missing η=0.3: best=0.233/0.127 vs last=0.285/0.177), showing that test-set-informed early stopping inflates reported numbers. RobustTSF's Δ scores are low (0.003–0.004), suggesting this issue is less severe for the proposed method, but the reporting convention makes it impossible to determine how much of the claimed advantage over baselines comes from the method versus from test-set-informed selection. The paper should report validation-set-based model selection with a single test-set evaluation.

### Minor

- **Anomaly scale parameters (ε for Constant/Missing, σ² for Gaussian) are never reported.** The paper says "the noise scale is within the range of (−∞, +∞)" (line 78) and "keeping the anomaly scale constant" (line 294), but the actual values used in experiments are never given. Without these, the experiments cannot be reproduced.

- **No error bars or confidence intervals.** Every result in the paper is a single run. Given stochasticity in neural network training and random anomaly generation, this is a notable omission for a paper making "SOTA" claims.

- **No sensitivity analysis for the threshold τ = 0.3 (Equation final_loss).** A single threshold is applied across all anomaly types, rates, and datasets. The paper provides no analysis of what fraction of samples are retained under each condition or whether results are stable over a range of τ values. Without this, it is unclear whether the method is robust to its own hyperparameter choice or whether τ=0.3 is a lucky choice that happens to work for the specific experimental conditions.

- **Heavy-tailed anomaly claim is stated but not empirically tested.** The paper asserts RobustTSF "works well when anomalies follow other heavy-tailed distributions like student-t distribution and Generalized Pareto distribution" (line 395), but then only evaluates on Gaussian subsequence anomalies. The heavy-tailed claim is unsupported by evidence.

- **Evaluation is limited in scope.** Only two datasets (both from infrastructure/sensor domains), only one backbone architecture (LSTM), and no comparison with more recent robust forecasting methods beyond the three detection-imputation baselines cited. While the paper notes community norms, the limited scope weakens generalizability claims.

- **No discussion of limitations or failure cases.** The paper does not discuss when RobustTSF might fail (e.g., when anomalies are concentrated at the last time step of every window, causing all samples to be dropped; or when the L1 trend filter cannot distinguish signal from anomaly). Including this would strengthen the paper's scientific contribution.

### Trivial

- None.

## Nice-to-Haves

- A "no selection" condition (train with MAE on all samples without filtering) in the ablation table would isolate the contribution of the selection module from the loss choice.
- The runtime/efficiency advantage claimed in the paper could be quantified with wall-clock comparisons.
- The interesting position-sensitivity finding (Table 1) could be deepened with a more formal characterization (e.g., a function relating anomaly position to expected error).

## Removed Points

*These points were flagged by reviewers but removed after verification against the paper:*

- **Missing comparison with Yoon et al. (2022):** The paper distinguishes its anomaly setting from Yoon et al.'s adversarial-perturbation setting (line 42). Not a valid weakness.
- **Missing comparison with robust regression methods (Pensia et al., Kong et al.):** The paper explains these methods require linear models and matrix inverses, making them inapplicable to DNN forecasting (lines 45–46). Not a valid weakness.
- **"0.182/0/070" table entry likely a formatting artifact:** Consistent with parser errors described in the instructions. Removed.
- **"Sample Robustness section is entirely empirical":** The section is an empirical analysis of anomaly position effects, which is a legitimate form of analysis. Not a weakness.
- **Dirac weighting with K'=K-1 makes the algorithm too simple:** The paper is transparent about this design choice; simplicity is a stated goal. Not a weakness.
- **Criticism that MAE robustness is "not novel" (Theorem 2):** Theorem 2's extension of known LNL results to the forecasting regression setting is a legitimate adaptation, even if the core idea is not entirely new. Removed as the paper's contribution is the package (theory + sample analysis + algorithm), not the isolated theorem.
- **Generic "evaluation lacks rigor" / "claims outrun evidence":** These are summary conclusions rather than specific, anchorable weaknesses. The specific sub-claims are addressed individually above.

## Novel Insights

The harsh critic's observation about the gap between Theorem 1's condition and MAE's actual behavior for Constant anomalies is a genuinely insightful mathematical point that goes beyond the paper's own analysis. The paper presents Proposition 1 as a direct corollary of Theorem 1, but the conditionality of MAE's robustness (requiring f(x) to lie between y and y^A) is a subtle but important caveat that the authors appear to have missed. Separately, the strength finder's framing of Table 1 as the paper's "most novel empirical contribution" is insightful — the position-sensitivity finding is arguably more novel and better-supported than the theoretical analysis, and the paper would benefit from recentering its contribution around this empirical discovery rather than the overclaimed theoretical guarantee.

## Suggestions

1. **Correct the theoretical framing of Proposition 1.** Either add a boundedness assumption on the forecaster's output (e.g., f(x) ∈ [min(y, y^A), max(y, y^A)]), prove a bound on the gap when f falls outside this interval, or present MAE as approximately/conditionally robust. The empirical results do not depend on a strict theoretical guarantee, so a more honest framing would strengthen rather than weaken the paper.

2. **Replace best-epoch test reporting with validation-set-based model selection.** Hold out a validation set, select the stopping epoch based on validation performance, and report only a single test-set evaluation. The "last epoch" results partially mitigate the concern, but the standard in the field for evaluation rigor is clear.

3. **Report anomaly scale parameters** (ε for Constant/Missing, σ² for Gaussian) in the experimental setup, and add a sensitivity analysis for τ showing retained sample fractions and performance over a range of values.

4. **Add confidence intervals** via multiple random seeds (at least 3–5) to establish statistical reliability of the claimed improvements.

## Score and Decision

This paper has genuine empirical contributions — the position-sensitivity finding is well-designed and practically useful, the algorithm is simple and effective, and the results show consistent improvements. However, the core theoretical claim is imprecisely stated to the point of being misleading about what is actually proven, and the evaluation methodology (best-epoch test reporting, no error bars, missing anomaly scale specifications) falls short of the rigor expected at a top venue. The issues are fixable, but the paper in its current form overstates both its theoretical guarantees and the strength of its empirical evidence.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>