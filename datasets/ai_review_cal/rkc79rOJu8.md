- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 3, 6
Here is my consolidated final review.

---

## Summary

This paper proposes BeST, a quantization-based metric for pre-trained source model selection in transfer learning. The key idea is to map source model softmax outputs onto a discrete grid via a quantization function, solve for the optimal classification policy analytically, and use the resulting validation accuracy at the optimal quantization level as a transferability score. The approach is novel in applying quantization (traditionally used for computational efficiency) to the task-similarity estimation problem. Experiments on MNIST and CIFAR-10 subsets show that BeST rankings correlate with ground-truth transfer accuracy, especially for high-performing source models, and that computing the metric is substantially faster than full neural network training.

---

## Strengths

- **Novel quantization approach enabling analytical tractability.** The paper introduces a principled method (Section 4.1–4.2) that maps continuous softmax outputs to a discrete grid, reducing what is normally a continuous optimization problem to a finite one. The optimal classification policy for a given quantization level can be solved analytically (Equation 3–4). This is a genuinely new use of quantization for transferability estimation.

- **Large computational savings demonstrated quantitatively.** Table 2 reports speedups of up to 57× over full neural network training (e.g., MNIST→MNIST at tl-frac=0.01: 0.75 CPU seconds vs. 42.71 CPU seconds). The advantage persists across all three TL setups and data sizes, confirming the time-efficiency claim with concrete numbers.

- **Strong ranking accuracy for high-performing source models.** Table 1 shows that for sources with >90% transfer accuracy (threshold=0.9), the mean deviation of predicted ranks from true ranks is less than 2 with as few as 100 samples and less than 1 with 500 samples. The small standard deviations indicate consistent performance across source-target pairs.

- **Validation across multiple TL setups, data regimes, and architectures.** The experiments span three TL setups (MNIST→MNIST, CIFAR10→CIFAR10, CIFAR10→MNIST), three data fractions (1%, 3%, 5%), and two custom model architectures (2-layer and 5-layer). Figure 7 shows that the metric maintains >60% correct-rank fraction across all conditions, supporting robustness claims within the tested scope.

- **Architecture indifference demonstrated.** The metric itself requires no knowledge of the custom model architecture. Figure 7 shows it performs substantially above random (>60% correct ranks) for both 2-layer and 5-layer custom models, confirming the metric is not architecture-dependent (even though ground-truth rankings differ by architecture, as expected).

---

## Weaknesses

### Fatal
None.

### Major

- **No comparison against existing transferability metrics.** The paper's Related Work (Section 2) explicitly lists LogME (You et al., 2021), GBC (Pándy et al., 2022), H-score (Bao et al., 2019), LEEP (Nguyen et al., 2020), and NCE (Tran et al., 2019). Yet the experiments compare BeST only to ground-truth transfer learning accuracy obtained by full training. Existing metrics also claim strong rank-correlation results on similar benchmarks, and several (LogME, GBC) are also fast to compute. Without baseline comparisons, the paper cannot establish that BeST advances the state of the art — the contribution is presented in a vacuum. This is the single most important gap. The time-savings comparison against full training (Table 2) is incomplete without showing whether BeST offers any advantage (or is at least competitive) over existing fast metrics in ranking accuracy, speed, or robustness.

### Minor

- **Non-standard rank evaluation metric limits comparability.** The paper defines a rank as "correct" if the true TL accuracy of the predicted source is within 3% of the true TL accuracy of the true rank-*i* source. This is a custom, lenient measure that does not appear in the transferability estimation literature. Standard rank correlation measures (Spearman's ρ, Kendall's τ) are absent, making it impossible to compare BeST's performance with published results from other methods. The paper does report mean rank deviation (Table 1), which is more informative, but this is a secondary metric.

- **Very limited target-class scope.** All primary experiments use binary target tasks (n=2). The one multiclass experiment (Section 5.2) uses a 4-class source → 3-class target. Realistic transfer learning often involves target tasks with 10 or more classes. While the paper acknowledges the computational scaling challenge (cost proportional to q^(m-1) for m-class sources), it does not demonstrate whether the metric works well for larger n, nor does it explore strategies (e.g., sampling, approximations) to address the scaling. The reader cannot assess whether BeST is useful in the settings where source selection is most needed.

- **Uniform class distribution assumption untested.** The derivation of the training accuracy formula (Equations 2–4) relies on the assumption that class labels are uniformly distributed (Section 3). Real-world limited-data settings are often imbalanced. The paper provides no experiments or analysis testing whether BeST remains robust when this assumption is violated. An explicit discussion or ablation would strengthen the paper.

- **Unimodality assumption for ternary search not fully validated.** Algorithm 1 uses ternary search, which relies on validation accuracy being unimodal in the quantization level q. The paper states this is supported by "simulations under various settings" but provides no figure, formal proof, or systematic analysis, particularly for the multiclass case where the behavior could differ from the binary case.

### Trivial
None.

---

## Nice-to-Haves

- Compare BeST against simple baselines such as random ranking or a label-overlap similarity heuristic to establish a lower bound.
- Study sensitivity to the 80/20 train/validation split ratio and different tolerance/max-steps settings.
- Report the distribution of optimal q* values across source-target pairs as supporting evidence for the search bounds.
- Include a brief discussion or simple experiment on non-uniform class distributions (even a synthetic perturbation) to assess robustness.

---

## Removed Points

These were flagged during review triage. Treat them with caution — they are mostly noise or scope-creep.

- *"Comparing to neural network training is a strawman because all metrics are fast."* The harsh critic argued this. **Reason for removal:** The paper compares against the straightforward baseline of training each candidate model — the default approach a practitioner would use. Showing that BeST is faster than training is a valid comparison; the missing comparison against *other metrics* is already listed as a Major weakness. The speed-vs-training claim is not a strawman.

- *"Architecture indifference is undermined because the 5-layer model gives better alignment."* **Reason for removal:** The critic's reasoning is flawed. The metric itself is architecture-agnostic (it does not use architecture information). The ground-truth rankings naturally differ by custom model capacity, and the metric correlates with both at >60%. The better alignment with 5-layer is expected since a more capable model can extract more signal; this does not invalidate architecture indifference.

- *"Only showing high-accuracy regime leaves possibility that metric catastrophically fails on low-performing sources."* **Reason for removal:** The paper explicitly scopes its goal to "reliable in identifying good pairs" (high-performing sources), and the threshold filter is transparent. The claim is about ranking within the top candidates, not about all sources. This is a scope-defined design choice, not a flaw.

- *"Time improvement drops from ~51× to ~5× for 4→3 class transfer, suggesting marginability when data is abundant."* **Reason for removal:** Even at 5× speedup the method is still faster. The paper acknowledges the non-linear scaling. This is an observed limitation, not a weakness that invalidates the contribution.

- Generic formatting/style nitpicks, speculation about missing appendix content, and comments about "at time of writing" status of cited works are all removed per hard rules.

---

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives are largely consistent: both recognize the novelty of the quantization approach and the strength of the computational savings, while both agree that the evaluation gap relative to existing metrics is the central weakness. The harsh critic's structural critique is correct on the missing baselines but overstates several secondary concerns (e.g., the "architecture indifference undermined" argument is not textually supported). The strength finder accurately identifies the paper's concrete evidence but is too generous about the evaluation completeness.

---

## Suggestions

1. **(Required for acceptance) Add baseline comparisons** against at least 2–3 established transferability metrics (LogME, GBC, and H-score are natural candidates since they also use source model embeddings + target data without requiring source data). Report Spearman ρ and Kendall τ for all methods on the same benchmarks. This is the single highest-leverage change.

2. **Report standard rank correlation measures** (Spearman ρ, Kendall τ) alongside or replacing the custom 3%-tolerance metric. This enables direct comparison with published results and is the community standard.

3. **Include one experiment with a larger target class count** (e.g., 5-class or 10-class target) to demonstrate scalability beyond toy regimes. If computational constraints prohibit this, state the limitation more prominently and discuss potential approximate solutions.

4. **Test robustness to non-uniform class distributions** by running at least one set of experiments where target classes are imbalanced (e.g., skewed 80/20 split) and report whether ranking accuracy degrades significantly.

5. **Provide empirical validation of the unimodality assumption** for ternary search, ideally with a figure showing validation accuracy vs. q for several source-target pairs across binary and multiclass settings.

---
