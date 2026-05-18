Now I have verified the key claims. Let me construct the final consolidated review.

## Summary

This paper proposes DreamMiss, a method to make denoising diffusion models (DDMs) for sequential recommendation robust to missing data. The core idea is a dual-side Thompson sampling (DTS) strategy that stochastically edits user interaction sequences during training by removing high-continuity items from high-stability sequences, creating uncertainty-aware guidance for the diffusion model. The method is evaluated on three real-world datasets (YooChoose, KuaiRec, Zhihu) and shows consistent improvements over strong baselines including DreamRec, PDRec, and DiffuASR.

## Strengths

- **Novel and well-motivated DTS-based editing strategy**: The idea of simulating missing data by preferentially removing items that least disrupt preference evolution—using continuity (local) and stability (global) scores—is creative and principled. The ablation study (Table 2) cleanly separates the contribution of each component: both "w/o L" and "w/o G" outperform "w/o GL" (random removal), and DreamMiss with both models outperforms alternatives using popularity, diversity, sequence length, or item position as probability metrics. This directly supports the claim that the DTS strategy preserves preference evolution better than heuristic alternatives.

- **Significant and consistent empirical gains**: On KuaiRec, DreamMiss outperforms DreamRec (the best generative DDM baseline) by 5.84% in HR@20 and 13.84% in NDCG@20. Across all three datasets, DreamMiss achieves the best results, with NDCG@20 improvements of at least 26.95% over missing-data-specific methods (IPS, DiffuASR, PDRec) on YooChoose. These gains are substantial and statistically credible given the reported standard deviations over five runs.

- **Robustness to varying missing data ratios**: Figure 3 shows DreamMiss maintains superior performance to PDRec and DreamRec on synthetic datasets with 10%, 20%, and 30% missing data, and its performance decline is smaller than baselines. This directly validates the method's resilience to uncertain missing data.

- **Comprehensive ablation study**: The eight-variant ablation (Table 2) systematically isolates the contributions of local and global probability models, and compares against four alternative metrics (popularity, diversity, sequence length, item position), providing strong evidence for the design choices.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical arguments in Section 3.3 are not valid as written and do not follow from the training procedure.** The consistency regularization analysis relies on Equation 17:  
  \(\|f_\theta(\mathbf{e}_N^{\tau_s},\hat{\mathbf{g}},\tau_s) - f_\theta(\mathbf{e}_N^{\tau_s},\tilde{\mathbf{g}},\tau_s)\|_2^2 \le 2(\|f_\theta(\mathbf{e}_N^{\tau_s},\hat{\mathbf{g}},\tau_s)-\mathbf{e}_N^0\|_2^2 + \|f_\theta(\mathbf{e}_N^{\tau_s},\tilde{\mathbf{g}},\tau_s)-\mathbf{e}_N^0\|_2^2)\).  
  This inequality holds for *any* three vectors (by the squared triangle inequality) — it is completely generic. The paper claims "minimizing the right-hand side... serves as an upper bound of the minimizer of the left-hand side, thus achieving consistency regularization." However, the training loss (Equation 12) only minimizes \(\|f_\theta(\mathbf{e}_N^{\tau_s},\tilde{\mathbf{g}},\tau_s)-\mathbf{e}_N^0\|_2^2\) (the term involving \(\tilde{\mathbf{g}}\), the edited-sequence guidance). The term \(\|f_\theta(\mathbf{e}_N^{\tau_s},\hat{\mathbf{g}},\tau_s)-\mathbf{e}_N^0\|_2^2\) (involving \(\hat{\mathbf{g}}\), the original observed sequence) is **never explicitly minimized** in the DreamMiss training objective. Therefore the claimed consistency regularization does not follow from the training procedure as described — the inequality is vacuous, and the argument provides no actual guarantee.

  Similarly, the extrapolation inequality (Equation 16) is stated without any derivation, definition of the constant \(C\), or articulation of the assumptions under which it would hold. The sentence "where \(C\) is the constant.3" suggests a garbled reference, not a rigorous claim.

  **Why this matters**: The paper presents Section 3.3 as a formal justification for why the method works. As written, these arguments do not support the paper's framing of principled theoretical grounding. This is a significant weakness **in the paper's presentation and claimed justification**, but it does not invalidate the empirical contribution — the method may still work well via a data-augmentation mechanism rather than a provable consistency-regularization one. The authors should either replace Section 3.3 with a clear intuitive explanation (verbal analogy to consistency regularization / data augmentation) or, if they wish to retain formal claims, derive them correctly.

- **The "Thompson sampling" formulation is underspecified.** The paper introduces probability models \(L(\mathrm{con}_n, p_n)\) and \(G(\mathrm{sta}_k, p_k)\) but never defines what random variable \(p_n\) or \(p_k\) represents, what distribution it follows, or how the sample \(\hat{p}\) is actually drawn from these models. Standard Thompson sampling draws a parameter from a posterior distribution, then acts greedily with respect to that draw. Here, the mechanism appears to be "compute a score, compare to a threshold, stochastically decide" — which is a Bernoulli trial, not TS in any recognizable sense. The paper should either (a) specify the actual sampling distribution (e.g., \(\hat{p}_n \sim \mathrm{Beta}(\alpha(\mathrm{con}_n), \beta)\) or similar), or (b) rename the mechanism to something more accurate (e.g., "score-based stochastic masking").

### Minor

- **The synthetic missing-data generation procedure for RQ3 (Figure 3) is underspecified.** The paper states that datasets with 10%, 20%, and 30% missing ratios are created but does not specify *how* items are removed. If removal is random, DreamMiss is tested on randomly missing data but trained on DTS-edited sequences — a meaningful but unstated robustness test. If removal follows some bias, the interpretation changes. This detail is essential for reproducibility and proper interpretation of the robustness results.

- **Key hyperparameter values are not reported.** The thresholds \(\lambda_1\) and \(\lambda_2\) (which control the proportion of removed items during DTS editing), the guidance strength \(w\) used in the main experiments, and the unconditional training probability \(\rho\) are not given numerical values in the paper. The paper states "due to space constraints" for the \(\lambda_1,\lambda_2\) sensitivity analysis. These values are necessary for reproducibility.

- **Calibration of ablation variants is not explained.** The ablation study compares DreamMiss against variants using "popularity," "diversity," "Seq-len," and "Item-pos" as probability metrics, but does not specify how these were converted into sampling probabilities or what thresholds were used. Without this detail, a reader cannot replicate or fully interpret these comparisons.

### Trivial
- Minor terminology concern: "oracel" (line 184) and "denosing" (line 184) appear to be typos.
- The Thompson sampling name, while imprecise, is internally consistent with the paper's own simplified definition in Section 2.2; this is more a clarity issue than a correctness issue.

## Nice-to-Haves
- A significance test (e.g., paired t-test across runs) would strengthen claims of superiority, though the reported standard deviations already suggest the gains are meaningful.
- A brief comparison of training time or inference cost against DreamRec would help practitioners understand the practical overhead of the DTS editing step.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Strength from Strength Finder: "Theoretical justification linking simulation to consistency regularization and extrapolation"** — REMOVED because it conflicts with the verified weakness that the theoretical arguments in Section 3.3 are invalid as written and do not follow from the training procedure. The inequalities are generic and the connection to the actual training loss is not established.
- **Criticism about "cannot be independently verified" or missing reproducibility** — REMOVED per hard rules: all cited models, benchmarks, and datasets are assumed to exist.
- **Criticism about missing related work** — REMOVED per hard rules: the reviewer does not have external sources to confirm the existence of missing references.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear disconnect between the paper's ambitious theoretical framing (Section 3.3) and what the training procedure actually does. This is worth noting because many readers might skip verifying the math and assume the theory is sound. The paper's actual strength lies in the empirical validation of the DTS editing strategy as a data-augmentation technique, which is a well-motivated heuristic even without the formal justification currently offered.

## Suggestions

1. **Fix or drop Section 3.3.** Replace the formal-but-invalid inequalities with a clear intuitive explanation: training on stochastically edited sequences acts as data augmentation, making the denoising network less sensitive to missing data in the guidance signal. Reference consistency regularization as an *analogy*, not a theorem. If formal claims are retained, they must derive from an argument that the training loss actually minimizes the relevant distances.

2. **Specify the sampling distribution for the DTS mechanism.** Clarify what \(\hat{p}_n \sim L(\mathrm{con}_n, p_n)\) actually means — what distribution is \(p_n\) drawn from, how does \(\mathrm{con}_n\) influence the sampling, and is the "probability model" updated across epochs (as in standard Thompson sampling) or recomputed from scratch each time?

3. **Report all critical hyperparameters** (\(\lambda_1, \lambda_2, w, \rho\)) used in the main experiments, either in a table or in the implementation details.

4. **Describe the synthetic data creation procedure for Figure 3** in one sentence (e.g., "Items were randomly removed from each sequence with probability equal to the target missing ratio").

## Score and Decision

**Originality**: Good — the DTS-based editing for DDM guidance is novel within the sequential recommendation literature.  
**Importance**: High — missing data is a practical problem for real-world recommenders.  
**Claims support**: Mixed — the empirical claims are well-supported, but the theoretical claims in Section 3.3 are not.  
**Soundness**: The experimental methodology is sound; the main results and ablations are convincing.  
**Clarity**: Generally clear on the method and experiments; unclear and misleading on the theoretical justification and the TS formulation.  
**Value to community**: Positive — the method is effective and the DTS strategy could be adapted by other researchers.

The paper has a genuine empirical contribution and the core method is well-evaluated. The main weakness is that the paper over-reaches with a theoretical section that does not withstand scrutiny. This is fixable in revision (by removing or rewriting Section 3.3) and does not undermine the empirical results. The missing experimental details (synthetic data procedure, hyperparameter values, TS specification) are also addressable. I recommend acceptance conditional on addressing these issues.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>