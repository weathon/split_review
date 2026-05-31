Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes GOOD-AT, a graph adversarial defense framework that re-frames attack-induced structural perturbations as out-of-distribution (OOD) samples. Instead of relying on handcrafted properties (e.g., feature similarity, spectral low-rankness) that adaptive attacks can exploit, GOOD-AT trains an ensemble of binary MLP detectors on PGD-generated adversarial edges (positive/OOD) and original edges (negative/in-distribution), then removes detected OOD edges during inference. The paper also provides a theoretical argument for why traditional adversarial training on graph structures produces incorrect (feature, structure)-label mappings, identifies a hypothesized trade-off between attack effectiveness and defensibility, and evaluates robustness across ~25,000 perturbed graphs using the adversarial unit test from Mujkanovic et al. (2022).

## Strengths

- **Theoretical analysis of adversarial training failure for graph structures (Section 4)**: The paper formally argues that traditional adversarial training with structural perturbations can cause GNNs to learn incorrect mappings, because node ground-truth labels may change under perturbation while the model is encouraged to predict the original label. This provides a specific, graph-motivated explanation for why standard adversarial training underperforms on graphs, going beyond the empirical observations in prior work (Xu et al., 2019; Mujkanovic et al., 2022).

- **OOD-detection-based adversarial training paradigm that avoids handcrafted properties**: The core idea — treating adversarial edges as OOD samples and training neural-network-based detectors to identify them — is a conceptually clean departure from property-based defenses (Jaccard-GCN, GNNGuard, ProGNN, SVD-GCN, etc.). Rather than defining a fixed similarity metric or spectral filter that adaptive attacks can circumvent, the approach learns a decision boundary directly from adversarial examples, which is well-motivated by the adaptive-attack vulnerability documented in Mujkanovic et al. (2022).

- **Extensive adaptive robustness evaluation using the adversarial unit test**: The paper evaluates on 7 adaptive attack types from Mujkanovic et al. (2022) over ~25,000 perturbed graphs (Figure 3). GOOD-AT consistently outperforms all seven property-based baselines (RGCN, Jaccard-GCN, GNNGuard, ProGNN, SVD-GCN, GRAND, Soft-Median-GDC) on evasion attacks, with RAUC values close to the theoretical upper bound on Cora (0.61) and low standard deviation across data splits.

- **Transferability analysis across adaptive attacks (Figure 4)**: The paper systematically evaluates how each adaptive attack transfers across defenses. GOOD-AT is the most robust model on 6 out of 7 adaptive attacks, demonstrating that its robustness does not rely on a narrow, easily-circumventable property.

## Weaknesses

### Fatal
None.

### Major

- **Detector performance is never directly evaluated, leaving the core mechanism unvalidated**: The paper reports only end-to-end classification accuracy (Table 1) and RAUC (Figure 3), which confound two factors: (i) does the detector accurately distinguish adversarial edges from clean edges? and (ii) does removing the detected edges help classification? Without direct detection metrics (precision, recall, AUC, false-positive rate, or ROC curves), the results are ambiguous — the observed robustness could stem from the GCN being resilient to the specific pattern of removals rather than from accurate detection. The ablation on the number of detectors (Table 1) measures final accuracy, not detection quality, so it does not resolve this. This is the single most important evidential gap, as the paper's entire contribution rests on the OOD detector's effectiveness.

- **No adversarial training baseline is included in the experiments**: The paper's Section 4 motivates GOOD-AT by arguing that adversarial training for graph structures "can result in the model learning erroneous (feature, structure)-label mapping," and this failure is central to the paper's framing. However, the experimental comparison (Section 7.1) includes only property-based defenses — no adversarial training method of any kind appears as a baseline. While the paper cites prior work (Xu et al., 2019; Mujkanovic et al., 2022) showing that adversarial training underperforms on graphs, the motivating argument would be substantially strengthened by an empirical comparison that directly demonstrates this failure under the same attack and dataset conditions used for the main evaluation.

- **The claimed trade-off between attack effectiveness and defensibility is not empirically validated**: Hypothesis 1 (Section 6) is presented as a core contribution ("for the first time, propose the existence of a trade-off"). However, the supporting evidence is limited to a qualitative observation that adaptive attacks against GOOD-AT also reduce attack effectiveness on vanilla GCN. No systematic experiment is provided — e.g., varying attack budgets while measuring both accuracy drop (effectiveness) and detector AUC (defensibility) to show a monotonic or quantitative relationship. The paper acknowledges this in Limitations (Section 8: "we do not rigorously prove Hypothesis 1 theoretically"), but continues to list it as a contribution, creating a gap between the claim and the evidence.

- **Poisoning defense evaluation is incomplete given acknowledged vulnerabilities**: The paper states that the self-training poisoning defense "can be bypassed by some simple adaptive designs" (Section 5, line 117), yet the poisoning evaluation (Figure 3) uses the unit test from Mujkanovic et al. (2022), which does not include adaptive attacks against self-training. The paper acknowledges this implicitly ("existing poisoning attacks must incorporate adaptive attacks against the self-training strategy," line 169), but the results showing RAUC "close to the upper bound" are presented as evidence of robustness without the corresponding adaptive evaluation that the paper itself says is necessary. This conflates robustness against the tested (non-adaptive) attacks with overall robustness.

### Minor

- **Threshold \( t \) for detector decision not specified**: The decision function \(\Gamma\) depends on a threshold \( t \) (line 80), but the paper never states how this threshold is chosen, whether it is tuned per dataset, or what value(s) are used. This detail is needed to reproduce the method.

- **Attack budget for generating OOD training samples not reported**: The paper uses PGD to generate adversarial edges for detector training but does not specify the perturbation budget \(\Delta\) used during this training phase. If the budget is fixed (e.g., 10%), the detector may generalize poorly to attacks with larger budgets; if variable, that should be described.

- **Clean accuracy after defense processing is not reported**: The upper bound \(\text{RAUC}_{\text{max}}\) is computed using GCN's clean accuracy on the original graph. If GOOD-AT's edge-removal process also removes benign edges during inference on clean graphs, its effective clean accuracy (and thus its true upper bound) could be lower. Reporting the defense's clean accuracy after processing would clarify whether the RAUC comparisons are affected.

- **Adaptive attack formulations are described only at a high level**: Section 6 describes two adaptive evasion strategies (generating undetectable perturbations, and incorporating detector output as a regularization term) but provides no precise mathematical formulation. This limits reproducibility of the adaptive evaluation.

- **No ablation of the edge embedding design**: The edge representation (Eq. 4) concatenates node representations with raw features. No ablation compares this against alternatives (e.g., Hadamard product, difference, or attention-based aggregation), making it unclear whether the design choice materially affects performance.

### Trivia
- The inductive classification and generality experiments (Section 7.3) are each described in a single sentence without quantitative tables or figures, making them unverifiable from the text alone.
- Standard deviations are reported across 5 splits, but no significance tests (e.g., paired t-tests comparing GOOD-AT against the second-best method) are provided.

## Nice-to-Haves

- A discussion of computational cost would be helpful, since training \( K \) detectors each requires a separate PGD attack run on the clean graph.
- If the self-training poisoning defense is retained in the main evaluation, including adaptive attacks specifically designed against it would make the poisoning results more meaningful.
- Reproducibility would benefit from specifying exact configuration files for the unit test (hyperparameters, splits, seeds) in the provided GitHub repository.

## Removed Points

These points were flagged by reviewers but are removed per filtering rules:

- **"Upper bound comparison is misleading" framed as major claim**: The RAUC_max is defined identically for all methods (clean GCN accuracy vs. MLP). While the concern about defense-induced clean accuracy drop is valid (kept as Minor), the critic's framing that this "may overstate performance" is softened — RAUC_max is a shared reference bound, and all methods are evaluated on the same scale.

- **"Self-training poisoning defense contradiction" (harsh critic's point #3)**: The paper is internally consistent — it states that the self-training strategy can be bypassed by adaptive attacks, and then shows that existing (non-adaptive) poisoning attacks in the unit test are ineffective against it. The paper also explicitly notes "This indicates that existing poisoning attacks must incorporate adaptive attacks against the self-training strategy." This is an acknowledgment, not a contradiction. The substantive concern (incomplete evaluation) is retained in Major weaknesses above.

- **"Section-by-section: No ablation of edge embedding"**: Retained in Minor weaknesses, not removed.

- **"Section-by-section: Section 7.3 brevity"**: Retained in Trivial.

- **"Code and reproducibility" (harsh critic)**: The critic's speculation about what "should include" in the repository is not a verifiable weakness from the paper content.

- **"Strength: Trade-off identification" from Strength Finder**: The identification of the trade-off is a genuine conceptual observation; however, since the paper does not validate it, the strength is qualified by the retained Major weakness about insufficient validation.

- **"Statistical rigor: confidence intervals/significance tests"**: Standard deviations across 5 splits are reported, which is standard practice. Calling for significance tests beyond this is a nice-to-have.

- **"Pure formatting/style nitpicks" and "typos/grammar"**: Not present in the original submission (parser artifacts only).

## Novel Insights

The reviews surface a core tension that the paper does not fully resolve: the method replaces property-based detection with learned OOD detection to overcome adaptive attacks, but evaluates the detector's success only through the proxy of end-to-end classification accuracy. This leaves open the question of whether the detector genuinely generalizes to unseen attack distributions or whether the GNN's own robustness to edge deletion is inflating the results. Additionally, the poisoning side reveals an asymmetry — the paper correctly identifies that self-training has simple adaptive bypasses, but then evaluates it under non-adaptive attacks, creating a mismatch that mirrors the very problem the paper diagnoses in prior work. The trade-off observation, while speculative, is intriguing and could motivate future work on attack-detection co-design, but the paper would benefit from separating the (well-supported) evasion defense contribution from the (speculative) trade-off claim in its presentation.

## Suggestions

1. **Directly evaluate the OOD detector**: Report detection AUC, precision/recall, and the fraction of removed edges that are truly adversarial vs. clean. This would validate the core mechanism and could be done without changing the experimental setup.
2. **Include at least one adversarial training baseline** (e.g., GCN trained with PGD-generated adversarial graphs on the same budget) to empirically ground the motivating claim about adversarial training failure.
3. **Systematically study the trade-off**: For several attack methods, vary the budget and measure both accuracy drop (effectiveness) and detector AUC (defensibility). A plot of this relationship would turn the qualitative observation into a supported claim.
4. **Clarify or remove the poisoning defense results**: Either design adaptive attacks against the self-training defense and include them, or reframe the poisoning discussion as an OOD analysis without claiming empirical robustness.
5. **Report clean accuracy after GOOD-AT's edge removal** to establish a method-specific upper bound and demonstrate that the defense does not degrade performance on clean graphs.
6. **Specify the threshold \( t \)** and the attack budget used for generating OOD training samples, as both are necessary for reproducibility.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>