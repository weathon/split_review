- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 8, 6
Now I have a thorough understanding of the paper and can verify each claim against the source text. Let me produce the consolidated review.

## Summary

This paper proposes Physics-Informed Weakly Supervised Learning (PIWSL) for training machine-learned interatomic potentials (MLIPs). Two novel loss functions are introduced: PITC (Taylor-expansion consistency) enforces consistency between predicted energy and forces on perturbed configurations via a first-order Taylor expansion, and PISC (spatial consistency) enforces path-independence of energy predictions using the concept of conservative forces. Experiments on ANI-1x and TiO₂ across five MLIP architectures (SchNet, PaiNN, SpinConv, eSCN, Equiformer v2) show consistent error reductions, often by a factor of two, particularly in data-scarce regimes. The method also enables accurate force prediction when training without reference force labels, addressing a realistic scenario for expensive ab initio methods like CCSD(T)/CBS.

## Strengths

- **Consistent and substantial error reduction across architectures and datasets.** On ANI-1x with 1000 samples, PIWSL reduces PaiNN energy RMSE from 56.62 to 24.53 kcal/mol and force RMSE from 12.96 to 11.43 kcal/mol/Å (Table 1). On TiO₂ with 1000 samples, eSCN energy RMSE drops from 3.31 to 1.40 kcal/mol and force RMSE from 0.46 to 0.21 kcal/mol/Å (Table 2). Gains hold across five architectures and two primary datasets.

- **Enables accurate force prediction without any reference force labels.** When training with only energy labels (the realistic scenario for CCSD(T)/CBS), PIWSL improves force RMSE by factors of 2–3.5 (Table 3). For PaiNN with gradient-force (GF), force RMSE falls from 83.36 to 24.02 kcal/mol/Å; for Equiformer GF, from 35.70 to 21.83 kcal/mol/Å.

- **Outperforms the prior Taylor-expansion-based weak-label approach.** PITC achieves lower energy and force RMSE than the WL method (Cooper et al., 2020) on both PaiNN and Equiformer, with and without reference forces (Table 5). The WL method actually degrades PaiNN energy (81.86 kcal/mol) while PITC improves it (30.94 kcal/mol) over the baseline (56.62 kcal/mol).

- **Ablation study cleanly isolates each component's contribution.** Table 4 shows PITC accounts for the majority of improvement (PaiNN energy 24.60 vs. baseline 56.62). PISC alone does not improve accuracy but stabilizes training when combined with PITC, reducing Equiformer energy variance from ±26.48 (PITC only) to ±0.50 (PITC+PISC).

- **Qualitative analysis demonstrates improved physical consistency.** On the aspirin C–H bond stretch (Figure 2c,d), PIWSL-trained models yield potential energy curves closer to the reference, and the direction from original to perturbed structures aligns with the negative force gradient, whereas baseline predictions often point in the opposite direction.

- **Validation on multiple datasets and architectures confirms generality.** Results span heterogeneous molecules (ANI-1x), bulk materials (TiO₂), with additional benchmarks on rMD17 and LMNTO referenced in the supplementary material, covering both gradient-force and force-branch models.

## Weaknesses

### Fatal
None.

### Major
- **The NoisyNode comparison lacks sufficient detail on hyperparameter configuration.** NoisyNode is presented as a primary competitor, but the paper does not report whether hyperparameters (noise magnitude, loss weighting) were optimized per architecture. For SchNet, NoisyNode outperforms both baseline and PIWSL, while for PaiNN, eSCN, and Equiformer it produces drastically worse results (e.g., PaiNN energy RMSE 464.55 vs. baseline 168.01 on ANI-1x with 100 samples). The explanation that NoisyNode does not "incorporate the proper response of energy to perturbations" is plausible, but without evidence of fair tuning the reader cannot fully assess whether PIWSL is genuinely superior or NoisyNode was simply poorly configured for these models. The paper's main claim (improvement over the standard supervised baseline) is unaffected, but the secondary claim about NoisyNode is weakened.

### Minor
- **The first-order Taylor approximation is not empirically validated at the perturbation magnitudes used during training.** The paper states that the maximum perturbation length is "at most 30% of the original bond length" (~0.33 Å for C–H). The qualitative validation in Figure 2 uses a perturbation of only 0.01 Å. The paper does not report the ratio of the second-order term to the first-order term at training perturbation scales, nor does it show how performance varies with perturbation magnitude. While the method works empirically, making this an incomplete justification rather than a fatal flaw, the "physics-informed" framing would benefit from a stronger quantitative link between the approximation and the actual perturbation sizes used.

- **The robustness claim (contribution iv) rests on thin evidence.** The paper states that PIWSL "mitigates sensitivity issues associated with limited sizes of available data sets," but the only supporting evidence is a single qualitative example (aspirin C–H bond stretch, Figure 2c,d). The paper explicitly scopes out MD stability simulations, which is reasonable, but the claim still warrants more than one qualitative curve. A quantitative measure of prediction variance under random perturbations across the test set would substantiate the claim more convincingly.

- **The adversarial perturbation direction definition ($L_{\text{dist}}$) is imprecise.** Equation (7) defines $\mathbf{g} = \nabla_{\mathbf{r}} L_{\text{dist}}(\mathbf{y}^{\text{pred}}, \mathbf{y}^{\text{ref}})$, but $L_{\text{dist}}$ is described only as "a distance measure function" without specifying whether it is the standard supervised loss or a separate function. Clarification is needed, particularly since computing $\nabla_{\mathbf{r}}$ of the standard loss could involve expensive second derivatives (Hessian) for gradient-force models.

- **The paper does not discuss computational overhead of the additional forward/backward passes.** PIWSL requires evaluating the MLIP on perturbed configurations, which approximately doubles the per-step computation. A brief statement of training time relative to baseline would help practitioners assess the cost-benefit trade-off.

### Trivial
- The claim that error reduction is "often between 10% and more than 50%" is accurate for most models but should be qualified for SchNet, where PIWSL produces essentially no change (31.49 vs. 31.50 kcal/mol for 1000 samples, Table 1).
- Table 1 and Table 2 are inconsistent on footnote annotations: Table 2 has a footnote (a) about larger batch size for SchNet, but Table 1 has no parallel annotation.

## Nice-to-Haves
- A sensitivity study of the loss coefficients $C_{\text{PITC}}$ and $C_{\text{PISC}}$, or at minimum a justification of the chosen values.
- The curl-reduction analysis for force-branch models (currently relegated to the supplementary material in Section sec:force-rot-experiment) deserves at least a brief mention of the main quantitative result in the main text, as it is a unique benefit of the method.

## Removed Points
- *Criticism about PISC alone not improving accuracy / weak support for stabilization claim.* — The paper's evidence (Equiformer: PITC-only variance ±26.48 → PITC+PISC ±0.50) actually supports the stabilization claim well. This criticism misreads the data.
- *Criticism that the paper should discuss the PITC/PISC consistency being non-trivial for force-branch models.* — The paper already states this clearly (Section 5.1: "Unless otherwise mentioned and except for SchNet, forces are directly predicted and not computed through the negative gradient of the energy").
- *Criticism about the adversarial vs. random perturbation discrepancy not being discussed.* — The paper states "the results might depend on the employed model" (Section 5.5), which is a reasonable acknowledgement of the discrepancy.
- *Strength Finder strengths about the problem being important.* — These are generic; only specific, evidenced strengths are retained.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Provide the actual perturbation magnitudes ($\epsilon$ values) used in training in the main text, and empirically validate the first-order approximation by either (a) computing the ratio of the second-to-first order terms for a representative system or (b) showing how performance varies with perturbation magnitude.
2. Add a brief statement on whether NoisyNode hyperparameters were tuned per architecture, or otherwise reframe the comparison as informative-but-not-definitive.
3. Add a quantitative robustness metric (e.g., variance of predicted energies/forces under random test-set perturbations) to substantiate the sensitivity-mitigation claim.
4. Clarify the definition of $L_{\text{dist}}$ in Equation (7) and explain how the gradient is computed efficiently.
5. Include a brief note on training-time overhead relative to the baseline.
