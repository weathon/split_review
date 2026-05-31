## Summary

The paper proposes two new algorithms for aggregating multiple LLM outputs: **Optimal Weight (OW)**, which assigns inverse-sigmoid weights using each agent's accuracy and is proven Bayesian-optimal under conditional independence, and **Inverse Surprising Popularity (ISP)**, a counterfactual variant of the classic Surprisingly Popular rule that exploits second-order inter-agent correlations without requiring ground-truth labels. The authors prove that ISP provably outperforms majority voting (MV), which in turn outperforms SP, in expected advantage. Empirical validation spans simulations, UltraFeedback, MMLU, and the ARMMAN healthcare dataset.

---

## Strengths

- **Tight theoretical framework with novel results.** Theorem 1 establishes OW as the globally Bayesian-optimal aggregator (linear or nonlinear) under the symmetric prior induced by label-shuffling. Theorem 2 cleanly orders ISP ≥ MV ≥ SP in expected advantage with closed-form gaps, and Theorem 3 provides a finite-sample guarantee. These results are original in the LLM aggregation context and strengthen the information-aggregation literature in a new direction.

- **Novel and principled ISP algorithm.** ISP is a creative inversion of the SP rule: rather than conditioning on what others *actually* answered, it scores a label using what others would have answered had they reported *different* options. The motivation is carefully worked out (Equations 3–5), and the reason SP fails in the LLM setting (accurate agents leave less room for exploiting systematic underestimation) is convincingly explained.

- **Connection to Bradley-Terry and RLHF.** Corollary 1 connects the optimal weighting scheme (K=2) to the logit of the logistic function, providing an information-theoretic justification for the Bradley-Terry model used in RLHF post-training—a noteworthy conceptual bridge.

- **Practical closed-loop design.** Section 5.2 closes the gap between theory and practice: OW-L uses ERM on second-order empirical moments to recover agent accuracies without labels; OW-I bootstraps pseudo-labels from ISP predictions. Both variants are simple, scalable, and consistently outperform MV in the real-world experiments.

- **Comprehensive and consistent empirical evaluation.** Across 16 model ensembles, OW-L outperforms MV in 97.9% of cases; MV never achieves the best performance. t-test statistics (12.53, 23.39, 3.22) confirm the improvements are statistically significant. The ARMMAN healthcare case adds external validity beyond standard NLP benchmarks.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical claims are about expected advantage, not accuracy.** Theorem 2 ranks the methods by $\mathbb{E}[\text{Adv}_{X}(s^*)]$, not by $\Pr[\text{argmax}_{s} \text{Adv}_{X}(s) = s^*]$. Higher expected advantage for the true label does not in general imply higher probability of the argmax selecting it (e.g., the variance of the advantage could be large, or other labels could have high-variance advantages). The simulations validate accuracy-level ordering empirically, but a tighter theoretical statement—or at least an explicit acknowledgment of this gap—is needed. As written, the main theorem could be misread as guaranteeing accuracy improvement.

2. **Second-order information requires a large *shared* unlabeled dataset, limiting applicability.** ISP (and OW-L/OW-I) require all N LLMs to answer the same M questions, so that $\hat{P}(A_i|A_j)$ can be estimated. In deployment scenarios where questions arrive online or where one cannot afford to query all N models on a shared corpus, this assumption is restrictive. The paper does not analyze what M is required relative to the benefit from Theorem 3 for practical settings (e.g., the MMLU and UltraFeedback sizes used).

3. **Modest real-world gains with unclear signal separation.** The absolute accuracy gains over MV in Table 3 are 1.45% (UltraFeedback), 1.05% (MMLU), and 0.54% (ARMMAN). These are statistically significant but small in magnitude. Since OW-L and OW-I produce *identical* results in three of three settings (Table 3), there is no empirical differentiation between the two estimation approaches, which raises questions about whether the optimization in OW-L (Equation 7) is actually doing something distinct from OW-I's pseudo-labeling.

### Minor

1. **Label-shuffle assumption and LLM position bias.** The pre-processing step requires LLMs to be order-invariant in their predictions. This is acknowledged as an assumption (with a citation), but position bias remains an empirically documented phenomenon for many models used here (e.g., Llama-3.2-1B). The impact of residual order-dependence on the theoretical guarantees is not analyzed.

2. **No sample complexity bound for OW-L.** OW-L relies on ERM (Equation 7) to recover agent accuracies from second-order moments, but the paper provides no convergence or identifiability analysis for this step—unlike ISP, which has Theorem 3. It is left to empirical validation alone.

3. **The scale-dependent behavior of ISP is an implicit limitation.** Theorem 2 states that the ISP–MV advantage decays as $\Theta(1/K)$ while ISP–SP remains $\Theta(1)$, meaning ISP's edge over MV becomes negligible for large K. The experiments only go up to K=10; for open-ended generation tasks reframed as multiple-choice with many options, the benefit would be very small.

### Trivial

1. In Table 3, designating Single Best as a "clairvoyant oracle" is methodologically correct but creates a slightly confusing table structure, as a reader might compare directly with other rows.

---

## Nice-to-Haves

- A direct accuracy-level theorem (even under stronger conditions) bridging the expected-advantage result to classification error would strengthen the theoretical case.
- An ablation showing sensitivity to M (number of unlabeled questions) for estimating second-order information would help practitioners calibrate when ISP is worth using.
- Including a broader set of K values or open-ended tasks would stress-test the theory's prediction that ISP's benefit vanishes at large K.

---

## Novel Insights

The most genuinely novel insight beyond stated contributions is the clean characterization of *why* SP fails in the LLM setting relative to human crowds: LLMs do not systematically underestimate the popularity of correct answers in the way humans do, so the "corrective bias" that SP exploits is absent, and the cost of subtracting the predicted score exceeds the benefit. The ISP fix—replacing actual peer reports with counterfactual reports on all other labels—elegantly converts SP's exploitative logic into an amplifying logic compatible with LLM behavior. The asymptotic result (ISP advantage ∝ 1/K) also provides a theoretically grounded scope condition: ISP is most valuable for binary or few-choice tasks, which aligns precisely with the RLHF preference aggregation use-case.

---

## Suggestions

- Explicitly discuss the gap between expected-advantage ordering and accuracy ordering; add a corollary or remark clarifying conditions under which the former implies the latter.
- Provide an identifiability proof or necessary conditions for the ERM in Equation 7 to guarantee a unique solution for $\hat{x}_1, \dots, \hat{x}_N$.
- Report OW-L and OW-I separately for individual model ensemble pairs in the appendix to understand when the two methods diverge.
- Analyze sensitivity of all methods to violations of conditional independence (e.g., by introducing controlled correlation in simulations), since this is the paper's core assumption.

---

## Score and Decision

The paper presents a well-grounded theoretical framework with two novel algorithms, clean proofs, a rich connection to the information-aggregation literature, and consistent (if modest) empirical improvements across multiple real-world settings. The major concern—that Theorem 2 proves advantage ordering rather than accuracy ordering—is a non-trivial gap between the stated and proved claims. The practical utility also partly depends on having a large shared unlabeled corpus. Nevertheless, the contributions are genuine, the work is careful, and it advances understanding of how to go beyond majority voting in multi-agent LLM settings.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>