Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes IDEAL, a method for selecting a small subset of unlabeled data to annotate for in-context learning. It constructs a directed k-NN graph from unlabeled embeddings, quantifies the influence of candidate subsets via an independent cascade diffusion model, and selects the subset with maximum influence using a greedy algorithm with a submodularity guarantee. Empirical results across 9 datasets (classification, multi-choice, dialogue, generation) show IDEAL outperforming the prior state-of-the-art Vote‑k in 17/18 settings while being 7.8× faster during subset selection.

## Strengths

1. **Principled, end-to-end unsupervised selection without an explicit diversity–representativeness trade-off.** By modeling selective annotation as influence maximization on a directed graph, IDEAL avoids the two-stage procedure of Vote‑k (diversity sampling followed by LLM-based confidence scoring) and eliminates the need for LLM inference during selection. The resulting pipeline is simpler and yields a 7.8× average speedup (Figure 2).

2. **Consistent and substantial empirical improvements over the prior state of the art.** IDEAL outperforms Vote‑k and random selection in 17 out of 18 evaluation scenarios across 9 datasets, under two annotation budgets (100 and 18), with multiple LLMs (GPT‑Neo 2.7B, GPT‑J 6B, GPT‑3.5‑Turbo), and across in-distribution and out-of-distribution settings (Tables 1, 3, 4; Figure 4). The gains are not marginal: e.g., SST‑5 with budget 100, IDEAL achieves 51.4% vs. Vote‑k's 46.6%.

3. **Empirical validation of the core assumption linking influence to ICL performance.** The paper samples 30 subsets, groups them by influence level, and shows that higher-influence subsets yield better average, median, and worst-case ICL accuracy on SST‑5 and MNLI (Figure 3). This bridges the gap between the theoretical influence objective and the practical task metric.

4. **Versatility demonstrated across multiple dimensions:** different LLMs, similarity-based vs. random prompt retrieval, and out-of-distribution transfer (SST‑2 → IMDb, BoolQ → BoolQ Contrast Set). IDEAL retains its advantage in all settings.

5. **Extensibility to automatic annotation (Auto‑IDEAL).** The influence diffusion process can bootstrap annotations from a small manually-labeled subset, achieving best performance in 4/5 classification datasets — sometimes surpassing fully manual IDEAL.

## Weaknesses

### Fatal

None.

### Major

None. The identified issues are addressable and do not invalidate the paper's core claims.

### Minor

1. **The key hyperparameter *k* (number of nearest successors for graph construction) is never stated.** The paper describes connecting each vertex to its *k* nearest successors (line 60) but never gives the value used in experiments. This directly controls graph sparsity and diffusion reach, and affects reproducibility. Although source code is provided, the paper itself should state *k* and ideally include a sensitivity analysis.

2. **The theoretical guarantee is for the influence metric, not task accuracy; the paper could be more precise about this scope.** Theorem 1 provides a standard \(1-(1-1/m)^m\) approximation bound for the influence function \(f_\mathcal{G}\), under a submodularity condition. The paper correctly discusses this as a bound on influence (Remark 3) and separately validates the influence–accuracy correlation empirically (Figure 3). However, the abstract and introduction use phrases like "enjoys theoretical support" in a way that some readers may interpret as a guarantee on ICL performance. Sharpening the framing — e.g., stating explicitly that the bound applies to the influence surrogate and the link to task accuracy is empirical — would eliminate this ambiguity. This is a framing issue, not a methodological error.

3. **Dataset pool sizes (*n* for each of the 9 datasets) are not reported.** The paper defines *n* as the number of unlabeled instances (line 50) and reports annotation budgets *m*, but never states the pool sizes. These are needed to interpret the time comparison (speedups depend on *n* and *m*) and to assess the difficulty of each selection problem. The datasets are standard (following Vote‑k), so the sizes can be looked up, but reporting them would improve reproducibility and analysis.

4. **No analysis of how the stochastic diffusion process interacts with greedy selection.** The influence function averages 10 diffusion runs (line 95), but the marginal gains used by the greedy algorithm inherit Monte Carlo noise. When several candidates have similar estimated gains, the selection order could be sensitive to this noise. A simple sensitivity check (repeating the full selection pipeline with different random seeds) would address this but is absent.

5. **No confidence intervals or per-run spread reported for main results.** Table 1 reports averages over only 3 random trials without variance or best/worst-case ranges. Given the small replication, the consistency of the pattern (17/18) is reassuring, but individual comparisons could be fragile. Reporting standard deviations or min/max across runs would strengthen reliability.

### Trivial

- The automatic annotation case study (Auto‑IDEAL) uses the LLM's own predictions to label additional data, inheriting prediction errors without analyzing propagation effects or label quality. Since this is presented as a preliminary case study (not a core claim), this is a minor oversight rather than a critical flaw.

## Nice-to-Haves

- A sensitivity analysis for the graph construction hyperparameter *k* (e.g., *k* ∈ {5, 10, 20, 50}) on one or two datasets.
- Graph statistics (average out-degree, diameter, number of strongly connected components) to characterize the constructed graphs across datasets.
- A brief discussion of the computational cost of the Sentence-BERT embedding computation and whether it is included in the reported time comparison (both methods need embeddings, so the relative advantage is fair either way, but clarifying would prevent confusion).

## Removed Points

- **Criticism about "cannot be independently verified" / "not yet released" implications**: None raised.
- **The critic's claim that the theory section "overstates its reach" as a central contribution**: This is partially kept (Minor #2) but downgraded from the critic's implied severity. The paper is actually fairly clear about what the theory covers (the influence function, not task accuracy), and the empirical correlation analysis bridges the gap. The remaining concern is a framing nuance.
- **The critic's concern about the 7.8× speedup lacking clarification on embedding time**: Both IDEAL and Vote‑k require embeddings (both use Sentence-BERT), so the cost is shared and the comparison is fair regardless. This is not a real weakness; moved to Nice-to-Haves as a clarification.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective that the paper itself does not already convey.

## Suggestions

1. **State the value of *k* used in all experiments** and include a sensitivity analysis (e.g., *k* ∈ {5, 10, 20, 50}) on at least one or two datasets.
2. **Report dataset pool sizes (*n*) for each of the 9 datasets** and include variance (standard deviation or min/max) for the 3‑run averages in Table 1.
3. **Reframe the theoretical contribution** to explicitly state: "The approximation bound applies to the influence function \(f_\mathcal{G}\). Because we empirically observe a positive correlation between \(f_\mathcal{G}\) and ICL accuracy (Figure 3), optimizing influence serves as a principled surrogate for task performance."
4. **Add a reproducibility section** listing: the value of *k*, random seeds used for the diffusion process, and pipeline-level seeds.
5. **Run a stability check** on the greedy selection by repeating the full pipeline with different random seeds for the diffusion and reporting how often the same subset is selected.

## Score and Decision

**Overall assessment**: The paper makes a credible empirical contribution: applying influence maximization to selective annotation for ICL is a well-motivated idea, and the results demonstrate consistent improvements over the prior state-of-the-art across a broad range of settings. The theoretical analysis applies standard submodular maximization theory — it is correctly used but not novel. The main weaknesses (unspecified *k*, missing pool sizes, no variance reporting, no sensitivity to stochasticity) are all addressable and do not undermine the core empirical findings. The paper is acceptably written and the 17/18 improvement pattern is strong evidence. I recommend acceptance with minor revisions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>