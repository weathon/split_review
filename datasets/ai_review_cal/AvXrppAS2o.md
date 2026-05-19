- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 1, 5, 3
Now I have all the information I need to produce the final consolidated review. Let me compose it.

## Summary

The paper proposes a shared representation learning framework that jointly optimizes causal structure learning (as an auxiliary task) and outcome prediction, aiming to improve generalization for medical prediction tasks. It builds on the CausalGAE graph autoencoder architecture by adding a task-specific prediction head g₃ alongside the reconstruction decoder g₂, with a hyperparameter κ balancing the reconstruction and supervised losses. The paper reports experiments on synthetic data, UCI classification datasets, and a heart attack survival analysis case study.

## Strengths

- **Clear motivation and well-identified research gap**: The paper correctly identifies the tension between relying purely on causal parents for prediction (as CASTLE does) and the need to leverage non-causal associations for generalization in evolving clinical environments. The framing of "best of both worlds" is appropriate and the limitations identified in CASTLE (scalability, treating reconstructed target as final output) are genuine.

- **Architecturally sound design**: The use of a shared encoder g₁ with task-specific decoders (g₂ for reconstruction, g₃ for prediction) is a natural and clean way to combine causal structure learning with outcome prediction. The adoption of the CausalGAE framework rather than CASTLE's per-variable feedforward networks is a genuine scalability improvement.

- **Temporal case study design**: The cross-year evaluation in the Worcester heart attack study (Scenario 2, training on 1997/1999 and testing on 2001) is a compelling evaluation design that directly tests the paper's claim about generalizing to evolving clinical conditions.

## Weaknesses

### Fatal

1. **The documented hyperparameter setting κ=0 invalidates all experimental results.** 

   The paper explicitly states in the experimental setup (line 103): "The loss hyperparameter κ is set to 0." Looking at the training objective in Equation (7):

   \[
   \min_{\mathbf{W},\Theta_1,\Theta_2,\Theta_3} \frac{(1-\kappa)}{2n}\sum\|X-\hat{X}\|^2 + \lambda\|\mathbf{W}\|_1 + \frac{\kappa}{n}\sum\|Y-\hat{Y}\|^2
   \]

   When κ=0, the supervised prediction loss term vanishes entirely. The objective reduces to:
   
   \[
   \min_{\mathbf{W},\Theta_1,\Theta_2,\Theta_3} \frac{1}{2n}\sum\|X-\hat{X}\|^2 + \lambda\|\mathbf{W}\|_1
   \]

   This is **mathematically identical** to the CausalGAE objective (Equation 3). The prediction head g₃ receives zero gradient, so its parameters Θ₃ are never updated from initialization. Any prediction from g₃ would be random. If instead the paper uses the reconstruction output (Ẑ) for prediction (as suggested by line 123: "We infer the reconstructed target from the trained model"), then the model is effectively CausalGAE.

   Yet the paper claims across Tables 1, 2, 5, and 6 that its model substantially outperforms CausalGAE and other baselines. These results cannot have been produced by the method as documented. Every reported experimental finding — on synthetic data, real-world classification, causal discovery, and the survival analysis case study — is rendered uninterpretable. This is not a minor documentation slip; it is a contradiction between the method's core claim (joint learning) and its stated execution (κ=0 removes the joint learning entirely).

   This weakness alone makes the paper unacceptable in its current form. If the authors can clarify that κ was actually set to a non-zero value (and report what it was for each experiment), the method may be salvageable, but the present manuscript does not support its own claims.

### Major

2. **Ablation study is underspecified and internally inconsistent.** 

   Table 3 reports results for "Without reconstruction" and "Without outcome prediction" ablations. The paper does not explain what these ablations actually remove from the architecture or loss. If "Without outcome prediction" corresponds to setting κ=0 (which is the same as the documented full-model setting), it should produce identical results to the full model — yet the critic reports discrepancies between the ablation and CausalGAE results that suggest different experimental conditions. Without specifying whether the DAG constraint, the shared encoder, or the g₃ head are retained in each ablation, the ablation study cannot be interpreted as evidence for the benefit of joint learning.

3. **No sensitivity analysis or justification for the critical hyperparameter κ.** 

   The paper describes κ as "a hyperparameter that can be tuned depending on the dataset" (line 86) but provides no guidance on how it should be chosen, no sensitivity analysis over a range of κ values, and no report of what κ was used (beyond "κ is set to 0," which contradicts the results). For any method that balances reconstruction and supervised losses, the value of κ directly determines the model's behavior. Its absence from the experimental analysis makes the method non-reproducible.

### Minor

4. **Causal discovery improvements over CausalGAE are small and lack proper uncertainty quantification.** 

   Table 2 reports TPR improvements (e.g., 0.714→0.821, 0.857→0.893) without confidence intervals or results averaged over multiple random DAG seeds. The standard deviations come from cross-validation data splits, not from the graph generation process, so they do not capture uncertainty in the causal discovery evaluation.

5. **Interpretability claims are not validated.** 

   The causal graphs in Figure 2 are presented as evidence of interpretability, but they are not validated against any ground truth or expert medical knowledge. They remain purely anecdotal.

### Trivial

6. **Duplicate word**: "like like" on line 101.
7. **Duplicate phrase**: "datasets into into" on line 164.

## Nice-to-Haves

- A hyperparameter sensitivity analysis for κ (and ideally for λ and the DAG penalty parameters) would strengthen the paper even if the κ=0 confusion is resolved.
- The paper could discuss limitations — e.g., scenarios where the shared representation might hurt prediction (when the causal structure is misspecified), or the computational challenges inherited from the DAG constraint.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **CASTLE AUC=0.50 "suspicious"** (Harsh Critic): The reviewer speculates that CASTLE's AUC of 0.50 on the survival analysis case study suggests implementation issues. AUC=0.50 is a valid outcome for a model that fails to generalize on difficult data; there is no evidence of a bug. **Removed: speculation not grounded in the paper.**

- **Missing comparison with newer methods** (Harsh Critic): The reviewer states "given the paper's publication date (2026), there are likely newer approaches combining causality and prediction that should be discussed." This is speculative — the reviewer does not name specific missing baselines and the paper already compares against CASTLE, CausalGAE, MLP, L2+ES, and ES. **Removed: speculative, not based on paper content.**

- **No discussion of DAG constraint enforcement during joint optimization** (Harsh Critic): The paper references Ng et al. (2019) for the DAG constraint mechanics (line 103: "default threshold and loss hyperparameters as in (Ng et al., 2019)"), which is standard practice. The joint loss with both terms does not change how the DAG constraint is enforced. **Removed: standard reference suffices; the critic demands unnecessary detail.**

- **Strength Finder generic/superficial strengths**: Several claimed strengths (e.g., "strong performance on challenging real-world classification", "robust causal discovery") are undermined by the fatal κ=0 issue. Since the fatal weakness invalidates all experimental results, these claimed strengths cannot be retained as valid. They are noted above under "Strengths" only as descriptions of what the paper *claims*, with the understanding that the fatal weakness renders them unsubstantiated.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface a single, clear central finding: the paper's core claim (joint learning of causal structure and outcome prediction) is directly contradicted by its own documented experimental setup (κ=0 eliminates the outcome prediction loss). This is not an area of debate between reviewers — the harsh critic identified it correctly, and the strength finder's positive observations are all contingent on experimental results that the paper's own text makes impossible to reproduce.

## Suggestions

1. **Resolve the κ documentation issue as the absolute top priority.** Report exactly what κ value(s) were used for every experiment, justify the choice, and provide a sensitivity analysis across a range of κ values. If κ was not actually zero, correct the paper text. If κ was zero, acknowledge that all experiments need to be re-run with non-zero κ to support the paper's claims.

2. **Specify the ablation study precisely.** For each ablation, state what loss terms are kept/removed, what architectural components are retained, and whether the DAG constraint is enforced. Ensure that the ablation baselines are directly comparable (same data splits, seeds, random initializations) to the full model and to each other.

3. **Average causal discovery results over multiple random DAGs** and report standard deviations or confidence intervals that reflect uncertainty in both data sampling and graph generation.
