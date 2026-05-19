- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 8, 6
Now I have all the information I need. Here is my consolidated final review.

---

## Summary

This paper proposes two algorithms (UCB-C and UCB-D) for constrained Bayesian optimization, addressing both the coupled (all functions evaluated together) and decoupled (functions evaluated independently) settings. The key contributions are: (1) a penalty-free regret definition that avoids manual tuning of a penalty parameter; (2) a principled adaptive rule for selecting which function to query (objective vs. constraint) that is connected to uncertainty sampling in active learning; (3) a claimed sublinear cumulative regret guarantee for the decoupled setting (Theorem 3.3); and (4) an estimator with a convergence guarantee (Lemma 3.5). The empirical evaluation on three synthetic and three real-world problems (gas compressor, CNN tuning, quantum chip design) shows competitive or superior query-efficiency against EIC, ADMMBO, and the state-of-the-art CMES-IBO.

## Strengths

1. **First algorithm with a claimed provable regret guarantee for decoupled constrained BO** — Theorem 3.3 (Sec. 3.2) provides a sublinear cumulative regret bound for the decoupled setting, a problem that prior theoretical works (Lu and Paulson 2022, Xu et al. 2023) only addressed in the coupled setting. The bound is stated as \(R_T \leq \sqrt{|\mathcal{F}| T \beta_T \max_h C_h \gamma_{h,T}}\).

2. **Novel penalty-free regret definition** — Equation (3) in Sec. 2 defines instantaneous regret as \(\max_{h\in\mathcal{F}} r_h(\mathbf{x}_t)\), avoiding the penalty parameter that required manual tuning in Lu and Paulson (2022). The paper also shows that sublinear regret under this definition implies sublinear regret under the sum definition and vice versa (Remark 2.1).

3. **Function query selection grounded in active learning** — Sec. 3.3 shows that the adaptive function-query rule in Algorithm 1 coincides with the uncertainty sampling criterion \(h_t = \arg\max_{h\in\mathcal{F}} u_{r_h,t-1}(\mathbf{x}_t)\), establishing a principled connection to active learning that goes beyond prior ad-hoc alternatives (ADMMBO's deterministic alternation, PESC's complex lookahead).

4. **Self-tuning horizontal exploration** — Sec. 3.2 introduces a relaxation parameter \(\nu_t\) that is tied to the vertical exploration bonus via \(\nu_t = 2\beta_t^{1/2}\sigma_{f,t-1}(\mathbf{x}_t)\), automatically balancing queries of constraints vs. the objective without manual scheduling. The intuitive justification (if \(\nu_t\) is too large, querying the objective reduces it; if too small, the objective regret is already small) is clearly stated.

5. **Strong empirical validation** — The experiments span 3 synthetic problems (with 0, 1, and 2 active constraints, allowing visual inspection of query allocation) and 3 real-world problems (Gas compressor with 4-d and 1 constraint, CNN tuning with 5-d and 10 constraints, quantum chip design with 11-d and 2 constraints). Figs. 2g–i and 3a–c show UCB-D consistently achieving lower instantaneous regret against number of queries compared to EIC, ADMMBO, and CMES-IBO.

6. **Estimator with theoretical convergence guarantee** — Lemma 3.5 (Sec. 3.4) bounds the instantaneous regret at the estimator by \(|\mathcal{F}|\sqrt{|\mathcal{F}|\beta_t \max_h C_h \gamma_{h,t}/t}\), ensuring convergence to the optimal solution as \(t\to\infty\).

## Weaknesses

### Fatal
None.

### Major

- **No proof sketch for the decoupled regret bound in the main text.** The paper states Theorem 3.3 (the central theoretical claim) and defers the entire proof to Appendix C, but provides zero intuition in the main text about how the standard GP-UCB information-gain argument is extended to handle functions that are not queried at every iteration. This is a significant expository gap: readers cannot assess even the plausibility of the bound without consulting the appendix, and the paper's headline contribution ("provable performance guarantee") rests on this proof. While the proof exists in the original submission (the appendix was stripped by the parser), the main text should include at least a paragraph sketching how the regret contributions of unqueried functions are controlled.

### Minor

- **The decision threshold \(2\beta^{1/2}\sigma_f\) is justified intuitively but not ablated.** The algorithm switches between querying the objective and a constraint based on comparing \(\max_c(\lambda_c - l_{c,t-1})\) to \(2\beta_t^{1/2}\sigma_{f,t-1}(\mathbf{x}_t)\). While the paper explains the self-tuning intuition clearly, no ablation study is provided to demonstrate that this specific choice (rather than, e.g., a fixed threshold or purely heuristic comparison) matters for performance.

- **No discussion of infeasible problems.** The paper's analysis and the non-emptiness of \(O_t\) depend on the problem being feasible (line 125: "if the optimization problem is feasible"). There is no discussion of what happens when the constraints cannot be simultaneously satisfied — the algorithm could stall or behave arbitrarily in that case.

- **Inability to compare to PESC.** The paper excludes PESC (the main existing decoupled approach) from experiments, citing implementation challenges. This is understandable and the authors reference Takeno et al. (2022) as also noting this difficulty, but it leaves the empirical comparison without the most natural decoupled baseline.

- **Missing a simple ablation baseline for the decoupled setting.** A baseline that always queries the objective (and checks feasibility post-hoc) would help demonstrate the specific benefit of adaptive function selection. The current comparisons are all against algorithms designed for the coupled setting (EIC, CMES-IBO) or a weak decoupled baseline (ADMMBO with deterministic alternation).

- **Finite-domain assumption.** The theoretical analysis assumes a finite input domain \(\mathcal{X}\). The paper notes this is for simplicity (citing the discretization trick of Srinivas et al. 2010), but the real-world experiments (e.g., 11-d QChip) operate on continuous spaces where this assumption is a strong simplification.

### Trivial
None.

## Nice-to-Haves

- A 1–2 paragraph sketch of the decoupled regret proof strategy in the main text (even if informal), explaining how the regret from unqueried functions is accounted for.
- A simple ablation comparing UCB-D against "always query objective", "always query most-violated constraint", and random function selection on one synthetic problem to validate the adaptive rule.
- Statistical significance tests (beyond standard error bars) for the experimental comparisons.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **The harsh critic's central claim that the decoupled regret bound (Theorem 3.3) is invalid or has a structural proof gap.** This criticism asserts that the information-gain analysis cannot extend to unqueried functions. However, the paper explicitly states that the proof is in Appendix C, which was stripped by the parser. Since the weakness depends on speculation about content in the stripped appendix (not verifiable from the paper as written), it is removed per policy. The softened concern about missing proof sketch is retained as a Major weakness above.

2. **Reproducibility concerns about missing implementation details (GP hyperparameters, \(\beta_t\) schedule, initial data, baseline implementations).** The paper states these are in Appendix E. The appendix was stripped by the parser; they exist in the original submission.

3. **Criticisms about missing proofs or derivations in the appendix.** These sections are present in the original submission and were removed only by the PDF parser.

4. **Formatting nitpicks, typos, and presentation issues.** These are parser artifacts, not author errors.

5. **The claim that the paper should have compared to published PESC results.** The paper explains why PESC is excluded (citing Takeno et al. 2022 on the difficulty of maintaining a consistent configuration) — this is a reasonable methodological decision, not a weakness.

## Novel Insights

The harsh critic identifies a genuinely difficult technical question that the paper does not adequately address in the main text: how to bound the cumulative sum of posterior standard deviations for functions that are rarely queried. This is a nontrivial extension of the GP-UCB analysis framework. However, the critic's claim that this gap is "fatal" or "structural" cannot be verified without access to Appendix C. The novel insight from synthesizing the two reviews is that the paper's adaptive query rule (tying \(\nu_t\) to the vertical bonus) may itself be the key to controlling unqueried functions' regret — because when a function is not queried, its instantaneous regret is bounded indirectly through the objective's standard deviation (if in \(S_t\)) or the constraint's lower confidence bound (if in \(\mathcal{U}_t\)). This potential proof strategy is hinted at by the paper's design but never explicitly stated.

## Suggestions

1. **Add a proof sketch in the main text:** Even 1–2 paragraphs explaining how the decoupled regret bound is derived — especially how the contributions of functions that are not queried at each iteration are controlled — would significantly strengthen the paper. Without this, readers cannot assess the central theoretical claim without consulting the appendix.

2. **Include an ablation on the function-query rule:** Compare UCB-D against "always query objective," "always query most-violated constraint," and random function selection on at least one synthetic problem. This would directly validate that the adaptive rule (and the specific \(2\beta^{1/2}\sigma_f\) threshold) drives the observed performance gains.

3. **Add a brief discussion of the infeasible case:** Acknowledge what happens when no input satisfies all constraints, and suggest a practical fallback (e.g., relaxing constraints or minimizing violation).

4. **Consider adding a baseline that always queries the objective and checks feasibility post-hoc** to isolate the benefit of adaptive function selection.
