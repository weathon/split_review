Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes PPE (Polyak Parameter Ensemble), a method that constructs a parameter ensemble for KGE models by maintaining a running weighted average of model parameters at each epoch interval. The authors argue that this approach alleviates gradient noise circling around a minimum at virtually no additional computational cost. They evaluate PPE on link prediction (7+2 datasets, 3 KGE models), multi-hop reasoning (UMLS), and image classification (CIFAR-10), reporting consistent improvements over the final-checkpoint baseline.

## Strengths

1. **Consistent improvements across multiple KGE datasets and models**: Tables 4–6 and 8 report that PPE outperforms the final-checkpoint baseline across all tested link prediction datasets (FB15K-237, YAGO3-10, NELL-995 variants, UMLS, KINSHIP, Mutagenesis, Carcinogenesis) and all three KGE models (DistMult, ComplEx, QMult). This breadth of evaluation lends credibility to the claim that epoch-interval averaging benefits KGE training.

2. **Truly minimal computational overhead**: The method requires only maintaining a running weighted average of parameters (one additional scalar multiply per parameter per epoch), with no extra gradient computations, no extended training time, and no test-time memory increase over a single model. The paper reports no observed runtime overhead. This is a genuine practical advantage over prediction-level ensembles.

3. **Empirical analysis of the role of embedding dimension**: Table 8 systematically varies d from 2 to 256 on UMLS and KINSHIP, showing that PPE benefits increase with parameter count and only dissipate at very low dimensions (d ≤ 4). This characterization is informative and helps define the regime where the method is most useful.

4. **Theoretical intuition via gradient attenuation**: Section 3 sketches how uniform-weight PPE reduces the effective contribution of later-epoch gradients by a factor proportional to the epoch index, providing a useful conceptual explanation for why averaging over epochs may stabilize training around a minimum.

## Weaknesses

### Fatal


None.

### Major

1. **Missing comparison against established parameter-averaging methods (SWA, standard Polyak averaging)**: The paper compares PPE only against the final checkpoint of the same model without any averaging. The paper's own uniform-weight PPE is acknowledged to be "applying the Polyak averaging technique at each epoch interval" (Section 1). Stochastic Weight Averaging (SWA; Izmailov et al., 2018) is cited in a list in the related work but is never discussed or used as a baseline, despite being a well-known parameter-averaging method that also aims to improve generalization through epoch-level averaging. Without comparisons to SWA or even a simple exponential moving average of parameters, the reader cannot tell whether the reported improvements come from *any* form of parameter averaging (already known) or from the *specific weighting scheme* (the supposed novelty). This is the single most important experimental gap.

2. **Ambiguity in the experimental setup (j=200 vs. N∈{200,250})**: The paper fixes the averaging start epoch at j=200 (Section 4.1) while training for N ∈ {200, 250} epochs. For any dataset where N=200, the averaging window j+1:N is empty, meaning PPE reduces to the final checkpoint and should produce identical results to the baseline. The paper does not specify which datasets use N=200 vs. N=250, nor does it discuss how results on N=200 datasets can show improvements. This is a potential contradiction that undermines confidence in the experimental reporting. The authors must clarify this.

### Minor

3. **Exponential growth claim is under-supported**: The paper's title asserts that "Exponential Parameter Growth Leads to Better Generalization," but the exponential weighting scheme is only tested with λ = 1.0 (uniform) and λ = 1.1. No systematic ablation (e.g., λ ∈ {1.05, 1.2, 2.0}) or theoretical argument isolates the benefit of exponential vs. uniform weighting. The observed advantage of λ=1.1 over λ=1.0 is marginal and inconsistent (the paper notes it wins 81/96 scores but loses 6/96 — and the losses are not discussed). This is insufficient to support the title's strong causal claim.

4. **No statistical significance or variance reporting**: The reported improvements are small in several cases (e.g., DistMult MRR on FB15K-237: 0.337 → 0.340). No confidence intervals, standard deviations, or significance tests are provided for any of the main results. The 10-fold cross-validation results on Mutagenesis and Carcinogenesis (Table 6) report only means without variance, even though small-dataset variance is expected to be high. Without this information, the reader cannot assess whether the observed differences are statistically meaningful or within training noise.

5. **CIFAR-10 experiment is essentially non-reproducible**: Figure 1 shows accuracy curves for CIFAR-10, but no model architecture, optimizer, learning rate schedule, data augmentation, number of epochs, or numerical test accuracy is provided. There is no baseline (non-PPE) comparison in the figure. This experiment cannot be evaluated or reproduced.

6. **Notational error in the derivation**: Equation (5) uses the index "(2,2)" where "(1,1)" and "(1,2)" are clearly intended (the gradient terms η∇L are attributed to epoch 1, step 1 and epoch 1, step 2, but written as η_{(2,2)}). This reduces clarity in the theoretical motivation.

7. **Dynamic weight scheme described but never evaluated**: Section 3.1 describes a validation-loss-driven scheme for determining α, akin to early stopping. The paper acknowledges it was not tested (Section 4.1: "we did not dynamically determined α by tracking the validation loss"), but this is still a gap between the method description and the experiments.

### Trivial

- The abstract claims "11 benchmark datasets" but the paper evaluates on 10 (7 link prediction + 2 bio + CIFAR-10). Minor inflation.
- Some sentences contain self-references ("In B, we propose two techniques") that refer to sections stripped by the PDF parser.

## Nice-to-Haves

- A comparison against SWA and a simple step-level Polyak averaging baseline would significantly strengthen the paper.
- Reporting standard deviations across multiple training seeds for all main results.
- An ablation of the exponential growth rate λ (e.g., λ ∈ {1.0, 1.05, 1.1, 1.2, 2.0}).
- An ablation of the start epoch j to show sensitivity to this hyperparameter.
- Numerical results and implementation details for the CIFAR-10 experiment.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"SWA is not mentioned"** — Izmailov et al. (2018) is cited in the related work (line 36). Factually incorrect.
- **"ααα garbled equation"** — PDF parser encoding artifact; not present in the original submission.
- **"Cost-free claim is misleading/incorrect"** — The paper qualifies memory claims with "at testing time" and the compute overhead of a running average is genuinely negligible vs. training. The criticism overstates the issue.
- **"Tables embedded as images"** — PDF parser artifact.
- **"No code release" / "no random seeds"** — Reproducibility nitpicks to be removed per guidelines.
- **"Missing appendix content / missing proofs"** — Appendix sections are stripped by the PDF parser.
- **"Derivation is not a rigorous proof"** — The paper frames the derivation as intuition/conjecture, not as a formal proof. The criticism demands a standard not claimed.
- **"Early epochs (0 to j) receive zero weight contradicts explanation"** — Reviewer misread "starting from w_j"; the paper correctly describes that epochs before j have zero weight and averaging begins at j.
- **"11 vs 9 datasets"** — The actual count is 10 (not 11 or 9). Minor inflation, not a core issue. 
- **"Contribution is not novel"** — Overly harsh framing; the paper acknowledges its connection to Polyak averaging and the contribution is the application with exponential weighting to KGE. The real problem is lack of comparison, not lack of novelty.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface any observation about the method or results that goes beyond what the paper already states.

## Suggestions

1. **Add SWA and standard Polyak averaging as baselines** in the main KGE experiments (Tables 4–6). This is essential to demonstrate that the *exponential weighting scheme* (not just epoch-interval averaging) is what drives improvements.
2. **Clarify the j=200 / N ambiguity**: specify which datasets use 200 vs. 250 epochs, and for any dataset where N=200, explain how PPE with j=200 can differ from the baseline. If this reveals that some reported improvements are impossible, the results must be corrected.
3. **Report standard deviations or confidence intervals** for all main metrics, especially the 10-fold cross-validation results.
4. **Provide complete experimental details for CIFAR-10**: architecture, optimizer, schedule, epochs, and numerical test accuracy with and without PPE.
5. **Systematically ablate λ** over a wider range to support the title's claim about exponential growth.
6. **Fix the notational error in Equation (5)** where "(2,2)" should be "(1,1)" and "(1,2)".
7. **Reconsider the abstract's dataset count**: 10 datasets is still a solid evaluation; inflating to 11 is unnecessary.

## Score and Decision

The paper addresses a practical problem (building effective ensembles without the traditional overhead) and provides broad, consistent evidence that epoch-interval averaging benefits KGE models. However, the evaluation has two critical gaps that prevent acceptance: (1) the absence of comparison against existing parameter-averaging methods (SWA, Polyak) makes it impossible to isolate the contribution of the proposed weighting scheme, and (2) the j=200 / N ambiguity raises unresolved questions about the validity of some reported results. Together, these issues mean the paper's core claims are not adequately supported.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>