I have thoroughly analyzed the paper and cross-checked every claim against the actual text. Let me now produce the consolidated review.

---

## Summary

NARCISSUS proposes an unsupervised anomaly detection method that exploits the empirical observation that models converge faster on normal data than on anomalous data during training. By combining a tailored early stopping scheme (VES) that identifies when the model has converged on normal data, with an ensemble method (RVES) that handles epistemic uncertainty, the paper shows that semi-supervised backbones can be converted to unsupervised operation while maintaining near-identical accuracy. The main evidence is Table 2, where NARCISSUS achieves F1 scores within 0.02 of semi-supervised baselines across 6 time-series datasets.

## Strengths

- **Convincing core empirical finding**: The observation that training on mixed normal+anomalous data yields convergence on normal data first (Figure 1) is well-motivated and supported by the ablation study, where bootstrapping (training to convergence without VES) produces highly unstable F1 scores ranging from 0.43 to 0.97 (Figure 3). This controlled experiment directly validates the paper's central design choice.

- **Broad backbone generality**: NARCISSUS is demonstrated across 7 different semi-supervised backbones (LSTM-NDT, OmniAnomaly, USAD, MTAD-GAT, GDN, TranAD, NPSR) without architectural modification, which credibly supports the model-agnostic claim for time series.

- **Strong empirical results on the primary (time series) benchmark**: Table 2 shows that across 6 time-series datasets and numerous backbone/model combinations, NARCISSUS (unsupervised) produces F1 scores within 0.02 of the fully supervised versions trained on clean normal data. In several cases (e.g., SMAP), NARCISSUS exceeds the semi-supervised baseline. This is the paper's main evidence and it is compelling.

- **Ablation cleanly isolates the contribution of each component**: The paper separately shows (i) that bootstrapping without VES is unstable (Figure 3, §5.4), and (ii) that removing RVES degrades performance (Table 7). This demonstrates that both components are necessary.

- **Honest limitation discussion**: Section 6 openly acknowledges the constraints of NARCISSUS (requires sparse anomalies, well-bounded data, sufficiently large datasets), which helps practitioners understand when the method will and will not work.

## Weaknesses

### Fatal

None.

### Major

- **RVES is underspecified for reproduction**: The paper does not specify the number of ensemble members, the aggregation rule for combining outputs ("take the joint set in the ensemble" is ambiguous between intersection vs. union), or the procedure for setting detection thresholds. Training dynamics (§5.2) and runtime are not compared to baselines to substantiate the "lightweight" claim. This makes the ensemble component difficult to reproduce and its claimed robustness unverifiable from the current description.

- **No sensitivity analysis for the critical hyperparameter η**: The VES algorithm's effectiveness depends on η (the percentile of validation subsets filtered out), which the paper calls "the upper bound of the portion of anomalous data." In an unsupervised setting, η is unknown. The paper says "empirically we can choose a large η to be safe" but provides no analysis of how performance varies with η across datasets. Without this, it is unclear whether the method requires dataset-specific tuning that would require labels to perform.

- **Image and graph experiments use a transductive (merged train+test) setup that limits comparability**: For the image and graph extensions (§5.3), the paper explicitly states it merges original training and test data. While this is acknowledged, it means NARCISSUS and bootstrapping are evaluated in-sample on data that includes test instances, while the semi-supervised baselines train only on the clean training set and are evaluated on held-out test data. The evaluation conditions differ, so the "comparable performance" claim for these domains is on weaker footing. The paper correctly flags this as a limitation but does not fully address the implications for generalization claims beyond time series.

### Minor

- **Theorem 4.2 restates the assumption rather than establishing a non-trivial guarantee**: The theorem shows that if $N_n \cdot \delta_n \gg N_a \cdot \delta_a$, then SGD updates are dominated by normal data. This is essentially a restatement of the conditioning assumption — it derives directly from the gradient bound and the sparsity condition. The paper does not verify empirically that this gradient-dominance condition actually holds for the models and datasets used in experiments, nor does it provide a tighter link between the assumed data characteristics (sparsity, boundedness) and the observed loss-separation behavior. The theoretical framing is therefore decorative rather than predictive. This does not invalidate the empirical results but means the theory does not carry independent weight.

- **VES algorithm's filtering rationale is not empirically validated**: The algorithm filters out high-loss validation subsets, assuming the remainder reflects normal data. While the intuition is consistent with the core insight, the paper does not analyze whether the filtering actually succeeds (e.g., what fraction of retained subsets are actually anomaly-free, or how this changes over training epochs). A simple validation of the filtering quality would strengthen confidence in the mechanism.

- **Ablation study does not report variance of NARCISSUS itself**: Figure 3 shows bootstrapping variance, and Table 7 shows the effect of removing RVES. But the paper does not report the run-to-run variance of the full NARCISSUS method (VES + RVES) across different random seeds. This would complete the picture of whether the ensemble actually stabilizes performance as claimed.

### Trivial

- The connection between Eq. 3 (the optimization problem) and the VES algorithm is mentioned only in passing ("constraint E[(E(f̃)-E(f))|U] < ε in Eq. 3 is met"). Making this link more explicit would help the reader see the formalism as more than decorative.

## Nice-to-Haves

- Provide the anomaly contamination ratio for each dataset, to help readers assess whether the sparsity condition is satisfied.
- Include a plot of ensemble performance vs. number of models to show convergence and justify the computational cost.
- Analyze filtering quality of VES: what fraction of retained validation subsets are actually anomaly-free?

## Removed Points

These points were raised by reviewers but are either factually incorrect, based on misreading, or do not survive cross-checking against the paper:

1. **"Evaluation protocol is not standard and likely inflates results — this issue alone is decisive"**: The reviewer conflates the image/graph experiments (where merge of train/test is explicitly stated in §5.3) with the time series experiments (where no such merging is stated, and the paper follows standard protocols from prior works). For the main time series results (Tables 1, 2), there is no indication that train and test are merged. The reviewer's claim that "all quantitative comparisons (Tables 1 and 2) are suspect" is not supported by the paper text — the merging is only done for the secondary image/graph experiments, and is explicitly stated there.

2. **"VES has a circular dependency"**: The reviewer argues that VES requires a reliable loss estimate before convergence to determine convergence. This misunderstands the algorithm: VES tracks *relative* losses across different validation subsets as training progresses. The losses are computed from the current model state at each epoch — no "pre-convergence" estimate is needed. The signal naturally emerges from the differential convergence rate the paper identifies (normal data losses decrease faster). VES never claims to identify anomalies upfront; it uses the evolving loss signal dynamically.

3. **"Self-supervised methods not considered is a weakness"**: The paper explicitly justifies this exclusion in §5.1: self-supervised methods would need NARCISSUS as a module, and since NARCISSUS already matches semi-supervised performance, the additional complexity is unnecessary. This is a reasonable scope decision.

4. **"Results tables not present in extracted text"**: This is a parser artifact, not a paper problem.

5. **"The optimization problem in Eq. 3 is decorative / not connected to the algorithm"**: The paper explicitly states that the VES stopping criterion ensures the constraint in Eq. 3 is met (line 149). The connection exists, though it could be elaborated.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a substantially novel framing, method, or connection that the paper itself does not already articulate.

## Suggestions

1. **Specify the time series evaluation protocol explicitly.** State clearly that for all time series experiments, standard train/test splits are used (training data = mixed normal+anomalous, test data = held-out), and that the semi-supervised baselines train on the clean normal portion of the training set only. This would preempt the evaluation-protocol concern entirely.

2. **Fully specify RVES:** State the number of ensemble members used in experiments, the aggregation rule (e.g., average anomaly scores? majority vote of detected anomalies? how is "joint set" computed?), and the threshold selection procedure. Report total training time vs. a single semi-supervised run to substantiate the "lightweight" claim.

3. **Provide η sensitivity analysis.** Show how performance varies with η (e.g., η ∈ {1%, 5%, 10%, 20%, 30%}) on at least 3 datasets, and give practical guidance for setting η without labels (e.g., using a held-out set, or setting η to a conservatively high value and showing robustness).

4. **Report NARCISSUS run-to-run variance.** Complement the bootstrapping variance plot (Figure 3) with the distribution of NARCISSUS F1 scores across multiple seeds, to directly demonstrate that the ensemble stabilizes performance.

5. **Strengthen the theory or downplay it.** If Theorem 4.2 is to remain, explicitly acknowledge that it assumes the gradient-dominance condition rather than deriving it from more primitive properties, and focus theoretical effort on connecting the data characteristics (sparsity, boundedness) more tightly to the observed loss dynamics. Alternatively, frame the theory as a formalization of intuition rather than a predictive guarantee.

6. **Validate VES filtering quality.** As a sanity check, report the precision of the filtering step: what fraction of the retained validation subsets are actually anomaly-free (using ground-truth labels) on a few datasets.

## Score and Decision

The paper presents a genuine and practically valuable insight — that early training dynamics can substitute for clean training data in anomaly detection — and supports it with reasonably strong empirical evidence on time-series benchmarks (7 backbones, 6 datasets). The main weaknesses (underspecified ensemble, missing hyperparameter sensitivity, limited domain generalization) are addressable and do not undermine the core time-series claim. The paper would benefit from clarifications and additional analysis but the central contribution is solid.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>