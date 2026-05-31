## Summary

FedBARRE proposes a federated learning framework that combines a Randomized Ensemble Classifier (REC) with optimized data perturbations to defend against gradient inversion attacks while preserving model utility. The paper claims three risk measures, proves convexity of the REC adversarial risk, and introduces a two-tiered training algorithm with dynamic classifier selection. Experiments on MNIST, FMNIST, CIFAR-10, and CIFAR-100 report improved accuracy and reconstruction-based privacy metrics compared to DP-based baselines.

## Strengths

- Addresses a genuinely important problem: the privacy-utility trade-off in federated learning under gradient leakage attacks.
- The idea of using an ensemble of classifiers with data perturbations is a reasonable high-level approach to improve robustness.
- Experiments cover four datasets and multiple baselines, showing some favorable numerical results.

## Weaknesses

### Fatal

1. **Contradictory and unfounded privacy claims.**  
   - The paper claims in the conclusion to provide “provable privacy guarantees” and a “rigorous privacy-utility frontier.”  
   - Yet Section 3.4 explicitly states that the convexity property “does not constitute a formal privacy guarantee.”  
   - No formal privacy accounting (e.g., DP budget, Rényi DP) is provided for any method—including the baselines. The “privacy budget” used in experiments (ε = 0.7) is never defined or computed for FedBARRE; it appears only in a single experiment where it is assumed a priori.  
   - The paper lacks any rigorous privacy analysis. The claim of “provable privacy guarantees” is false and misrepresents the contribution.

2. **Flawed evaluation of privacy protection.**  
   - Privacy is measured only by reconstruction quality metrics (MSE, PSNR, SSIM) under a single attack (DLG). These metrics do not quantify actual information leakage (e.g., membership inference, attribute inference).  
   - The comparison with DP baselines is not fair: the baseline methods (DP-GAS, DP-LAP, PPFA, Noise-Add) are not standard FL-DP methods (e.g., DP-SGD, DP-FedAvg) and their privacy parameters (ε, δ, noise scale) are never reported.  
   - Without controlling the privacy budget across methods, the reported “better privacy” may simply reflect stronger distortion rather than superior privacy-utility trade-off.  
   - FedBARRE’s perturbation is *optimized to minimize loss* (inner minimization), which is a highly unusual choice for privacy. The resulting distortions are data-dependent and could leak information themselves; no analysis is provided.

### Major

3. **Theoretical contribution is trivial or incorrectly framed.**  
   - The paper proves convexity of the ensemble objective *in the perturbation δ* (not in model parameters) and linearity in α. This is a straightforward property when the constituent losses are convex in δ, but for neural networks the loss is not convex in inputs. The authors provide no argument that the loss is convex in δ for the models used (LeNet, ResNet).  
   - The “REC adversarial risk” is not a standard adversarial risk (which is a min-max objective). It is a benign inner-minimization that does not correspond to any known threat model. Its convexity is a weak theoretical anchor.  
   - The three risk measures (standard, privacy-utility, REC privacy-utility) are near-identical reformulations with no novel insight.

4. **Experimental setup is insufficient for a method paper.**  
   - Only 4 clients, 30 rounds, and simple architectures (LeNet, ResNet-18) are used.  
   - The algorithm selects the best of M classifiers per round based on validation loss—this is essentially model selection, not a true ensemble. Gradients from only the selected classifier are uploaded to the server, raising questions about whether the ensemble structure is actually exploited.  
   - No ablation isolates the effect of the REC from the perturbation mechanism.  
   - The warm-up period (rounds 1–8 without defense) and attack only at rounds 9–11 is unrealistic and does not test sustained defense.

5. **Key implementation details are missing or inconsistent.**  
   - The algorithm (Algorithms 1 and 2) uses PGD to *minimize* the perturbation loss, which is confusing and likely leads to perturbations that make the data *easier* to classify, undermining the stated privacy goal.  
   - The “ensemble weights α” introduced and theoretically optimized are never used in the algorithm; model selection (argmin over validation loss) replaces them.  
   - The “dynamic classifier selection strategy” is simply picking the model with lowest validation loss—a standard routine that does not deserve a new name.

### Minor

- The paper states “provable privacy guarantees” in the abstract and conclusion but later walks it back—this inconsistency undermines credibility.
- Figure 2 (reconstruction images) shows FedBARRE yielding *clearer* images than FedAvg in some cases (e.g., MNIST digits in row 3 are sharp and recognizable, contradicting the privacy argument). The paper does not explain this.
- The privacy-utility plots (Figure 4) use a single privacy budget axis “P” that is never defined; it appears to be a proxy for perturbation strength, not a formal privacy metric.

### Trivial

- Typos and formatting issues are present but I do not list them per instructions.

## Nice-to-Haves

- A formal differential privacy analysis of the perturbation mechanism, or at least an empirical privacy leakage evaluation (membership inference, attribute inference).
- Ablation study separating the effect of ensemble size from perturbation strength.
- Comparison with standard DP-FedAvg under equal privacy budgets (ε, δ).

## Novel Insights

None beyond the paper’s own contributions. The claimed insights (convexity of REC risk, privacy-utility optimization) are either trivial or unsupported.

## Suggestions

- Remove all “provable privacy guarantees” claims unless a formal DP bound is derived and verified.
- Redesign the perturbation objective: for privacy, the inner loop should *maximize* loss (adversarial perturbation) or be an independent random draw; minimizing loss is counterintuitive.
- Compare with standard DP methods (DP-SGD, DP-FedAvg) under the same formal privacy budget.
- Provide privacy leakage metrics that go beyond reconstruction quality (e.g., membership inference AUC, attribute inference success rate).
- Clarify the role of the ensemble: if only the best model’s gradient is shared, the ensemble is not used in inference or aggregation—this should be justified.

## Score and Decision

The paper has a fatal flaw: it claims provable privacy guarantees while providing no formal privacy analysis and using a flawed evaluation that does not control privacy budget. The theoretical contribution is weak, the experimental setup is insufficient, and the algorithm’s design choices are questionable. The paper in its current form does not bring sufficient value to the community.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>