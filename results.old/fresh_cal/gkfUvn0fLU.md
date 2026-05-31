Now I have thoroughly read the paper and verified the claims. Let me produce the consolidated review.

## Summary

This paper studies reward model overoptimization in composite (multi-component) reward models for RLHF. It introduces "proxy points" — thresholds beyond which further optimizing a component RM degrades ground-truth evaluation performance — and shows that correlation between component RMs shifts these points. The core contribution is a constrained RL framework (CMDP with Lagrangian relaxation) that uses these proxy points as constraints, dynamically learning RM weightings via Lagrange multipliers to stay within useful ranges. The paper also proposes a gradient-free (Nelder-Mead) method to identify proxy points in a single training run, saving computation.

## Strengths

1. **Novel application of constrained RL to composite-RM overoptimization.** The paper casts RLHF with composite RMs as a constrained MDP (CMDP) where per-RM constraints at proxy points prevent overoptimization. This formulation naturally yields dynamic RM weightings via Lagrange multipliers, directly addressing the difficulty of tuning fixed RM weights. The five formulations enumerated in Table 1 provide a clear taxonomy for future work.

2. **Empirical demonstration that constrained methods outperform fixed-weight PPO.** Figures 3 and 4 show that μ-PPO and ξ-PPO achieve higher evaluation scores than PPO tuned with optimal fixed weights, and ξ-PPO remains stable under extended training while PPO degrades. The comparison is made fair by expending equal budget (10 runs) for hyperparameter selection in both approaches.

3. **Analysis of correlation effects on proxy points.** Section 3 demonstrates that correlation between component RMs shifts the joint proxy point away from independent estimates (Figure 2, referenced as `fig:correlated`), and the paper validates that correlation-aware thresholds outperform independent ones (Figure 5 right panel, labeled `fig:proxy-pt_performance`). This is a concrete finding for practitioners using composite RMs.

4. **Practical stability improvements.** The paper documents specific modifications — sigmoid-bounded Lagrange multipliers, low-momentum SGD updates, and replacing early value estimates with Monte-Carlo returns — that stabilize primal-dual optimization in this setting (Section 4, "Practical Improvements"). These are valuable for anyone applying constrained RL to LLM alignment.

5. **Gradient-free single-run threshold identification.** NM-PPO uses Nelder-Mead optimization to identify proxy points during a single training run (~256K steps), achieving comparable performance to methods requiring ~1.28M steps across multiple runs (Figure 5 left panel, labeled `fig:nm`).

## Weaknesses

### Fatal
None.

### Major

- **The evaluation (ground-truth) metric is not named.** The paper consistently refers to "evaluation score" and "ground-truth performance" (lines 71–72, 76, 79) and states it "uses held out metrics as the ground truth for convenience of iteration [citing Gao et al. 2022]." Following Gao et al.'s methodology is fine, but the specific metric is never stated. Is it a separate held-out RM of a particular architecture? A different functional combination of METEOR and intent? A deterministic rubric? Without knowing what the "evaluation score" on every figure's y-axis actually measures, a reader cannot (a) interpret the absolute magnitudes, (b) replicate the experiments, or (c) assess whether the overoptimization phenomenon is truly between a proxy and a *distinct* gold standard. This does *not* invalidate the relative comparisons between methods (since the same evaluation metric is used for all), but it is a significant clarity and reproducibility gap.

### Minor

- **Limited experimental scope.** The paper studies one dataset (DailyDialog), one base model (GPT-2), and two component RMs (METEOR and intent). While the authors acknowledge this in the discussion (line 198: "further testing of our methods is necessary on more domains and with composite RMs with more components"), the abstract's claim of "the first study on overoptimization in composite RMs" would be better scoped as a case study of a specific two-RM composite. Generalizing to larger models (e.g., LLaMA), more RMs (3–4 components), or diverse tasks would strengthen the contribution.

- **Role of adaptive weighting vs. constraint enforcement not isolated.** The constrained methods (μ-PPO, ξ-PPO) learn RM weightings dynamically via Lagrange multipliers, while the PPO baseline uses fixed weights. The improvement in Figure 3 could partly stem from adaptive weighting rather than constraint enforcement *per se*. An ablation that uses Lagrangian relaxation with intentionally loose thresholds (so constraints are never active) would help disentangle these factors. The paper acknowledges this attribution ambiguity (line 162: "We conjecture that the strong performance... is due to the beneficial effects of jointly optimizing the policy and Lagrange multipliers") but does not run the control.

- **NM-PPO computation details under-specified.** The paper reports NM-PPO uses 256K training steps (one run) vs. 1.28M steps (10 × 128K for ξ-PPO), but does not quantify the number of evaluation metric queries required during NM-PPO's simplex search, nor the wall-clock cost of those queries (which may involve expensive gold-standard evaluation). The "feasible region is relatively small" caveat (line 191) also suggests the strong NM-PPO results may depend on a favorable initial simplex placement, which the paper notes but does not further analyze.

- **Statistical detail could be stronger.** The long-training comparison (Figure 3 right) uses only 3 seeds, and the confidence band overlap between methods is non-negligible. Reporting effect sizes or bootstrapped significance would clarify whether the performance differences are robust.

### Trivial

- Figure numbering in the caption text references `fig:correlated` and `fig:proxy-pts` but the actual figure files are embedded by filename rather than explicit insertion points, making it somewhat difficult to map text references to figures.

## Nice-to-Haves

- A control method with adaptive weights but no meaningful constraints (e.g., Lagrangian relaxation with very loose thresholds) to isolate the role of constraint enforcement from adaptive weighting.
- Quantification of evaluation query costs (number of calls, wall-clock time) for NM-PPO vs. ξ-PPO.
- Experiments with 3–4 RMs on a small-scale task to strengthen generality claims.
- Comparison against reward-model ensembling baselines (e.g., taking the minimum of multiple RMs) or simple early stopping.

## Removed Points

1. **PPO comparison not fair (reviewer's claim):** The reviewer claimed asymmetry favoring constrained methods, but the paper uses 10 initial runs for *both* PPO (to tune fixed weights) and constrained methods (to find proxy points), making the comparison budget-fair. The claim that "the constrained methods learn their weightings dynamically, while PPO uses fixed weights" is correct as a description, but it's a feature of the proposed method, not an unfair comparison — the paper compares fixed-weight PPO (standard practice) against a method that demonstrably improves upon it. Moved because the comparison is properly controlled.

2. **"The evaluation metric not being defined is a structural flaw" (severity overstatement):** The harsh critic called this "structural" and claimed it makes experiments "uninterpretable." While the metric should be named, the relative comparisons between methods on the same evaluation metric remain interpretable. The critic's speculation that overoptimization may not be occurring (if the evaluation metric is closely related to the training RMs) is unfounded — the paper explicitly says it uses separate "held out metrics" following Gao et al. 2022, and the proxy-point curves in Figure 1 (proxy-pts) clearly show non-monotonic behavior consistent with overoptimization. Demoted from the reviewer's implied score-collapsing severity to Major.

3. **Missing pseudocode (appendix stripped):** The reviewer mentioned pseudocode is "referenced but missing." The paper references `alg:cPPO`. Appendix content is stripped by the parsing pipeline and existed in the original submission. Removed per instructions.

4. **Hyperparameter disclosure concerns:** The reviewer flagged nondisclosure of exact weightings, KL coefficient schedules, learning rates, etc. The paper does provide the key methods details (PPO, sigmoid bounding, low momentum, MC returns); comprehensive hyperparameter tables are standard for appendix content. Removed per instructions (appendix-stripping issue and typical evaluation practice).

5. **Criticism about "ground-truth access" requirement:** The reviewer noted the paper acknowledges needing ground-truth access as a limitation; this is already in the paper's own discussion section. Not a novel weakness.

6. **Several generic strength-finder strengths removed:** General claims about importance of the problem, or that the paper "addressed an important problem" are removed as unspecific. Only concrete, evidenced strengths retained.

## Novel Insights

The harsh critic's framing of the evaluation-metric-as-unidentified issue is the most salient cross-cutting observation that goes beyond the paper's own self-critique. The paper takes the evaluation metric as a given (following Gao et al. 2022's methodology) and focuses on the constrained optimization machinery, but the fact that the specific gold-standard metric is never named makes it harder for readers to assess whether the overoptimization phenomenon studied is meaningful (i.e., a true proxy-vs-gold-standard gap) or whether the "evaluation score" is simply a different function of the same RMs — in which case the contribution would be about multi-objective optimization rather than overoptimization. The critic also correctly identifies that the paper's interesting results (adaptive weighting improving performance) are not fully disentangled from constraint enforcement, suggesting an ablation the paper itself does not perform. No other genuinely novel observation emerged beyond the paper's own contributions and acknowledged limitations.

## Suggestions

1. **Name the evaluation metric explicitly** and justify why it is a meaningful gold standard. If possible, describe its architecture, training data, and relationship to the component RMs.
2. **Add an ablation** comparing ξ-PPO against Lagrangian relaxation with very loose thresholds (constraints never active) to separate the effects of adaptive weighting from constraint enforcement.
3. **Report the number of evaluation queries** used during NM-PPO and include wall-clock time if available.
4. **Expand to at least one additional setting** (e.g., a different dataset or 3–4 RMs) to broaden the empirical support, or adjust the abstract/intro claims to clearly scope the contribution as a case study.
5. **Report confidence intervals or bootstrapped p-values** for the main comparisons in Figure 3, particularly the long-training regime where only 3 seeds were used.

## Score and Decision

**Originality:** 7/10 — Constrained RL formulations for RLHF exist, but applying them to prevent overoptimization of composite RMs with proxy-point constraints is novel. The correlation analysis of proxy points is also new.

**Importance of research question:** 8/10 — Overoptimization is a central problem in alignment, and composite RMs are increasingly used in practice.

**Claims supported:** 6/10 — The main claims are supported but weakened by the undefined evaluation metric and the lack of an ablation isolating constraint enforcement from adaptive weighting.

**Soundness of experiments:** 6/10 — Reasonable methodology and fair comparison budgets, but the evaluation metric ambiguity, limited scope, and opaque NM-PPO cost reporting reduce soundness.

**Clarity of writing:** 7/10 — Well-structured and clearly argued, but the missing evaluation metric definition and some figure-mapping issues hurt clarity.

**Value to research community:** 7/10 — The constrained RL framework and practical improvements are likely useful to practitioners working with composite RMs, even if the specific evaluation details need clarification.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>