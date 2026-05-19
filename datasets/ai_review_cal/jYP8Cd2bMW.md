- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6
Now I have all the evidence needed. Let me write the consolidated review.

## Summary

This paper proposes FedMAP, a personalized federated learning framework that uses Maximum A Posteriori (MAP) estimation with a Gaussian prior to regularize local model training, formulated as a bi-level optimization problem. The global model (a Gaussian mean) acts as a prior, and local models are trained by minimizing negative log-posterior (data loss + squared-distance regularization). The server aggregates local parameters via a weighted average where weights are computed as likelihood × prior density. Experiments on a synthetic dataset (10 clients, three non-IID types) and Office-31 (3 clients, one per domain) show accuracy gains over FedAvg, FedProx, and FedBN, especially for clients with imbalanced or limited data.

---

## Strengths

1. **Principled bi-level formulation for PFL.** The paper formalizes FL as a bi-level optimization problem (Eq. 7), where the lower level solves MAP estimation locally and the upper level estimates the global prior from local models. This provides a cleaner theoretical framing than heuristic regularizers and explicitly couples the two stages (Section 2.3).

2. **Consistent accuracy gains, especially for disadvantaged clients.** On the synthetic label-skew benchmark, FedMAP achieves 80.39% average accuracy vs. 75.20% for individual training and 63.05% for the next-best baseline FedBN (Table 1). Clients 8–10 with severe label imbalance improve by 13–15% over individual training, which is a practically meaningful margin.

3. **Evaluated across three distinct non-IID types.** The synthetic experiments separately test feature distribution skew, quantity skew, and label distribution skew (Section 4.1, Figure 1), allowing targeted analysis of where FedMAP helps most. Per-client accuracy is reported rather than just averages.

4. **Integration with Flower framework.** FedMAP is implemented within the open-source Flower FL framework (Section 4, "Setup"), facilitating adoption and reproducibility.

---

## Weaknesses

### Fatal

None.

### Major

1. **Mismatch between the theoretical derivation and the aggregation weighting scheme (Section 2.3 vs. Algorithm 2).** The derivation of the global model update from the upper-level objective (Eq. 6, lines 128–133) minimizes  
   \[
   -\frac{1}{q}\sum_{k=1}^q \mathbb{P}(Z_k|\theta_k)\log\rho_\gamma(\theta_k).
   \]  
   For a Gaussian prior \(\rho_\gamma(\theta)\propto e^{-\|\theta-\gamma\|^2/(2\sigma^2)}\), this yields the closed-form solution  
   \[
   \gamma^* = \frac{\sum_k \mathbb{P}(Z_k|\theta_k)\,\theta_k}{\sum_k \mathbb{P}(Z_k|\theta_k)},
   \]  
   i.e., weights should be **only** \(\mathbb{P}(Z_k|\theta_k)\). The algorithm, however, uses \(\omega_k^{(t)} = \mathbb{P}(Z_k|\theta_k^{(t+1)}) \times \rho_{\gamma^{(t)}}(\theta_k^{(t+1)})\) (Algorithm 2, line 226) and aggregates with these weights (Eq. 10). The extra factor \(\rho_\gamma(\theta_k)\) does **not** follow from Eq. (6) under any standard interpretation. The paper claims "In view of (prior MLE) and the specific form of \(\rho_\gamma(\theta)\) …, the aggregation is performed as a weighted average … where the weights are \(\omega_k^{(t)}\)" (lines 231–236), but this claim is not supported by the derivation. This inconsistency must be resolved: either change the algorithm to match the derivation, or derive a modified objective that justifies the product weighting. Without this fix, the claimed theoretical grounding is partially invalidated. **(Verifiable directly from Eqs. 128–133, 164–166, and Algorithm 2 line 224–227.)**

2. **Baselines perform suspiciously poorly, suggesting inadequate tuning.** On the synthetic label-skew benchmark, FedAvg and FedProx achieve only 50–57% accuracy while individual training reaches 57–88% and FedMAP reaches 66–89% (Table 1). On Office-31, FedProx scores 40.22% on Webcam vs. 68.98% for individual training and 86.04% for FedMAP (Table 2). Such extreme underperformance of standard FL methods relative to individual training is atypical and raises serious concerns that baseline hyperparameters (e.g., the proximal term \(\mu\) for FedProx, learning rate schedules, number of local epochs) were not properly tuned. The paper provides no tuning details for baselines. **(Verifiable from Tables 1 and 2; no tuning grid or sensitivity analysis is reported in Section 4.)**

3. **No comparison to Bayesian PFL baselines.** Despite framing FedMAP as a Bayesian method and citing pFedBayes, FedPop, and β-Predictive Bayes in the related work (Section 1, "Bayesian approach in FL"), none of these are included in the experiments. Since the paper's novelty claim centers on the Bayesian bi-level formulation, comparing against the closest Bayesian PFL competitors is essential to establish advantage. **(Verifiable gap: Section 4 baselines include only FedAvg, FedProx, FedBN, and Individual.)**

### Minor

1. **No statistical significance or variance reported.** All accuracy numbers in Tables 1 and 2 appear to come from a single run. Without standard deviations or multiple seeds, it is impossible to assess whether the reported gaps (e.g., 2–17% improvements on individual clients) are robust or within the noise of a single initialization. **(Verifiable: no mention of seeds, runs, or variance in Section 4.)**

2. **No sensitivity analysis of the prior variance \(\sigma^2\).** The hyperparameter \(\sigma^2\) directly controls the strength of the regularization term (Eq. 9: \(\frac{1}{2\sigma^2}\|\theta-\gamma\|^2\)) and is therefore central to the method's behavior. The paper does not study the effect of varying \(\sigma^2\) on accuracy, convergence, or stability. **(Verifiable: \(\sigma^2\) is defined in Eq. 8 but its value is never stated and no sweep is reported.)**

3. **Small-scale real-world evaluation.** The Office-31 experiment uses only 3 clients (one per domain). While this is a natural partition of the dataset, 3 clients is too few to demonstrate scalability or robustness to heterogeneity in realistic FL deployments. The synthetic experiments with 10 clients are more informative but are artificial. **(Verifiable: Section 4.1, "Office-31 dataset … three clients.")**

4. **The local-update notation is misleading.** Algorithm 2 uses "\(\theta_k^{(t+1)} \leftarrow \arg\min_{\theta}\ldots\)" inside a loop over epochs, implying the minimization is solved to optimality at each epoch. In practice only a few gradient steps are taken. This is a conventional shorthand but creates confusion given the paper's emphasis on exact MAP estimation. **(Verifiable: Algorithm 2, lines 223–225.)**

5. **Overstated claim about PFL being "underexplored."** The abstract states that PFL approaches are "currently underexplored." Given the substantial body of existing PFL work (including FedProx, pFedBayes, FedPop, and clustering/meta-learning methods cited in the paper itself), this characterization is inaccurate. **(Verifiable: abstract line 5; the paper's own related work section lists many PFL methods.)**

### Trivial

None.

---

## Nice-to-Haves

- An ablation where \(\sigma^2 \to \infty\) (no prior) on the same setup would isolate the effect of the prior term from other aspects of the algorithm.
- Discussion of the computational cost of computing \(\mathbb{P}(Z_k|\theta_k)\), which requires iterating over the full local dataset for each client at each round. This is a non-trivial overhead that should be acknowledged.
- Measuring communication rounds to convergence or total transmitted bits to substantiate the "reduced communication overhead" claim in the abstract.

---

## Removed Points

1. **Criticism that the paper does not discuss convergence guarantees.** The paper explicitly scopes out theoretical convergence analysis (conclusion: "future work"), and this is standard for empirical systems papers at this stage. Not a weakness; scope is clearly stated.

2. **Criticism about missing appendix details or reproducibility.** The parser strips appendix content from all papers; reproducibility details likely exist in the original submission. Per the hard rules, criticisms predicated on missing appendix/proofs are removed.

3. **Criticism that FedProx with proper tuning "should not" produce low accuracies.** The observation about suspicious baseline performance is kept (Major #2), but the specific assertion about what "should" happen with a "well-chosen" \(\mu\) is speculative and softened into a concrete concern about absent tuning evidence.

4. **Strength Finder's claim of "rigorous bi-level formulation"** is kept as a strength but weakened by the verified weighting inconsistency — a formulation cannot be called fully rigorous when the algorithm diverges from its derivation.

5. **Strength Finder's claim of "novel adaptive weighting"** is dropped from strengths because the weighting scheme conflicts with the paper's own derivation, making it unclear whether it is a principled contribution or an ad-hoc heuristic.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface one clear structural issue (theory–algorithm mismatch) but do not reveal new findings about the method beyond what the paper states.

---

## Suggestions

1. **Resolve the weighting inconsistency.** Either (a) change the aggregation weights to \(\omega_k = \mathbb{P}(Z_k|\theta_k)\) to match the derived closed-form solution from Eq. (6) and re-run experiments, or (b) modify the upper-level objective (Eq. 6) to include \(\rho_\gamma(\theta_k)\) in the loss so that the product weighting follows naturally, and re-derive.

2. **Tune baselines properly.** Report a grid search over FedProx's \(\mu\) (and other baseline hyperparameters) and include the best configuration. Report results over at least 3–5 random seeds with standard deviations.

3. **Add at least one Bayesian PFL baseline** (pFedBayes or FedPop) to the comparison, given the paper's Bayesian framing.

4. **Report a sensitivity analysis for \(\sigma^2\)** over at least one synthetic scenario to show how the prior strength affects convergence and final accuracy.

5. **Expand the real-world evaluation** to a partitioned benchmark (e.g., CIFAR-10/100 with label skew across 10–20 clients) to demonstrate scalability beyond 3 clients.

---
