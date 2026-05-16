Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper proposes LMSP (Local Model Space Projection), a continual learning method that replaces the costly global SVD per layer (O(n³)) with a set of local low-rank decompositions defined by anchor points (O(n²)), reducing the computational complexity of orthogonal-projection-based CL. The method adapts ideas from local low-rank matrix approximation (LLORMA) to CL, integrates them into the CUBER framework's three-regime update rules, and provides theoretical convergence (O(1/K)) and backward-transfer guarantees. Experiments on four benchmarks report ACC and BWT, with LMSP achieving the best results among baselines.

---

## Strengths

- **Novel complexity reduction for subspace construction in orthogonal-projection CL.** The paper introduces local low-rank matrix approximation into continual learning, replacing the global SVD (O(n³)) with AltMin-based local decompositions (O(n²)). This is a principled approach to a real bottleneck in projection-based CL, and the theoretical complexity analysis (Section 4.1) is clearly articulated.

- **Theoretical convergence and backward-transfer guarantees.** Theorem 1 establishes O(1/K) convergence for both convex and non-convex settings under the local projection update; Theorem 2 proves conditions under which local projection achieves lower joint loss than global projection and enables backward transfer. Such formal analysis is relatively rare in the CL literature and adds substance beyond purely empirical contributions.

- **Consistent top performance across four benchmarks.** Table 1 shows LMSP achieving the highest ACC and BWT on Permuted MNIST, CIFAR-100 Split, 5-Datasets, and MiniImageNet, outperforming strong baselines including CUBER, TRGP, and GPM. This demonstrates that the reduced-complexity approximation does not sacrifice accuracy.

---

## Weaknesses

### Fatal
None.

### Major

- **No empirical validation of the central efficiency claim.** The paper's core thesis is computational efficiency — the title, abstract, introduction, and method all frame the contribution as reducing complexity from O(n³) to O(n²). Yet the experimental section (Section 5) reports only ACC and BWT. There are **no wall-clock times, no FLOP counts, no memory usage measurements, no per-task training time comparisons** with any baseline. A reader has no way to tell whether LMSP actually trains faster or uses less memory than CUBER, GPM, or a naive global SVD. The abstract states "Extensive experiments on several public datasets demonstrate the efficiency of our approach" — but the experiments do not measure efficiency at all. This evidential gap undermines the paper's primary thesis.

- **Incomplete method description affecting reproducibility.** Several key design details are omitted:
  - *Aggregation of multiple local subspaces.* The paper states that for a new task t, all m local model spaces are treated as m old tasks, giving tm candidates. But the update rules in Section 4.3 are written for a single local subspace q. When different local subspaces fall into different regimes (e.g., one Regime 1 and another Regime 3), it is never specified how these are combined — union of constraints? maximum? weighted combination? This is critical for implementing the method.
  - *Top-k selection.* The paper mentions finding "top-k correlated" old tasks but never specifies the value of k or the selection criterion.
  - *Key hyperparameter values.* The kernel bandwidth h, number of anchor points m, and rank r used in the main experiments (Table 1) are not reported. The ablation studies vary these parameters but the actual values for the main results are absent. The algorithm for AltMin and its rank per dataset are also not given.

### Minor

- **No error bars or statistical significance.** The reported gains over strong baselines are small (typically sub-1pp) and the method involves random sampling of anchor points, yet no standard deviations, confidence intervals, or multiple-seed results are provided. Without these, it is unclear whether the improvements are stable or within run-to-run noise. The claim that LMSP "outperforms other baseline methods" would be strengthened substantially by error bars.

- **No discussion of limitations or failure modes.** The paper introduces an approximation via local low-rank decomposition, but never discusses when this approximation might be harmful (e.g., for tasks with diffuse gradient structure where local low-rank assumptions break down) or how to diagnose such cases. A brief limitations paragraph would improve scientific rigor.

- **Source of baseline numbers unspecified.** The paper does not state whether baseline results in Table 1 were obtained by re-running the methods under controlled conditions or taken from prior publications. This affects reproducibility assessment.

### Trivial
None.

---

## Nice-to-Haves

- An ablation comparing LMSP with a single anchor point (effectively global SVD) vs. many anchor points would isolate the effect of local approximation from other design choices.
- A comparison with replay-based methods on computational cost (training time, memory) would provide useful context, though it is outside the paper's stated scope.
- Public code release would significantly aid reproducibility.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The proofs are relegated to the appendix (stripped), so in this version the theorems carry little force."* — The appendix was removed by the PDF parser; the proofs exist in the original submission. Removed per hard rule on missing-appendix complaints.
- *"Missing parentheses and garbled superscripts due to parsing"* — These are parser artifacts, not author errors. Removed per hard rule on formatting nitpicks.
- *"No details on model architectures, training hyperparameters"* — While these would be useful, the hard rule removes nitpicks about undisclosed hyperparameters as trivial implementation details.
- *"No comparison with replay-based methods on the efficiency front"* — This demands the paper address problems outside its stated scope (orthogonal-projection methods). Moved to Nice-to-Haves.
- *"The paper would benefit from a more self-contained argument or at least a sketch" (of the proof)* — This is an indirect request for content that exists in the appendix (now stripped). Removed per the missing-appendix rule.
- *"The reader is referred to Lee et al. (2013)... and to Lin et al. (2022a)... but the integration of the two is... inadequately explained"* — The paper does explain the integration through new local definitions (Definitions 3–5) and update rules in Sections 4.1–4.3. The specific missing-detail concerns are captured in the Major weaknesses above; the blanket claim of inadequate explanation is overly broad.

---

## Novel Insights

The reviews surface a crucial mismatch between the paper's framing and its evidence: the paper markets itself as an "efficient" CL method but evaluates only accuracy, not efficiency. This is a structural gap that no amount of theoretical complexity analysis can fill — empirical validation of runtime/memory is non-negotiable for a paper whose central claim is computational savings. Beyond this gap, the integration of local low-rank approximation into orthogonal-projection CL is genuinely novel, and the theoretical analysis provides a foundation that most CL papers lack. The missing method details (subspace aggregation, hyperparameter values) are fixable in a revision and do not threaten the core idea.

---

## Suggestions

1. **Add empirical efficiency measurements.** Report per-task and total training time, memory footprint of stored bases, and — for completeness — FLOPs or parameter counts for LMSP vs. CUBER, GPM, and TRGP. Without these, the central claim of the paper is unsubstantiated.
2. **Specify the missing method details.** Clarify how multiple local subspaces are aggregated across regimes, define the top-k selection criterion and k value, and report h, m, and r used in the main experiments.
3. **Add error bars.** Run each experiment with at least 3–5 random seeds (different anchor-point draws) and report mean ± std for both ACC and BWT.
4. **Add a limitations section** discussing when the local low-rank approximation may be inaccurate and how practitioners could detect this.
5. **State the source of baseline numbers** (re-run vs. cited from prior work) and, if re-run, describe the configuration.

---

## Score and Decision

The paper presents a novel and theoretically grounded idea for reducing the computational cost of orthogonal-projection continual learning. The accuracy results are strong across multiple benchmarks. However, the paper suffers from a major evidential gap: its central claim of "efficiency" is never empirically evaluated, and the method description is incomplete in ways that prevent reliable reproduction. These issues are fixable in a major revision but are too significant to overlook in the current form.

**Score:** 5.0 / 10

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>