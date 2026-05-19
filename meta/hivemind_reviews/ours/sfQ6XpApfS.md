## Summary
PiCO proposes an unsupervised framework for LLM evaluation where models act as peer reviewers: they answer unlabeled questions, evaluate each other's responses, and a "consistency optimization" aligns learnable confidence weights $w$ with response scores $G$ to produce a ranking closer to human preferences. The paper introduces three alignment metrics (PEN, CIN, LIS) and evaluates on Chatbot Arena, MT-Bench, and AlpacaEval.

## Strengths
1. **Empirically outperforms both supervised and unsupervised baselines.** Table 1 shows PiCO achieving the best PEN, CIN, and LIS across all three datasets at multiple data volumes. Notably, it beats PRE (a supervised method) on CIN by a margin of 2.5–3.0 on the full Chatbot Arena set (12.0 vs 15.0), demonstrating that unsupervised consistency optimization can match or exceed methods that require human annotations.

2. **Ablation validates the consistency assumption from multiple angles.** Table 2 shows Forward Weight Voting (assigning higher weights to stronger LLMs) yields better PEN/CIN than Uniform or Backward voting. Critically, "Random Weight + Consistency Optimization" further improves over Forward Voting across all three datasets, directly supporting the paper's core hypothesis that optimizing consistency moves the ranking toward human preferences.

3. **Learned confidence weights demonstrably reduce evaluation bias.** Figure 3 shows the preference gap (PG) heatmap before and after applying learned weights $w$. The re-weighted PG values are visibly closer to zero across all three datasets, showing that consistency optimization mitigates inflated self-assessments (e.g., ChatGLM-6B's self-preference bias) without requiring human labels.

4. **Unsupervised elimination matches or exceeds supervised elimination.** Figure 4 shows PiCO's CIN improving as weak reviewers are removed, and this unsupervised elimination performs comparably or better than PRE's supervised elimination (which requires human-annotated qualification exams) across all three datasets.

## Weaknesses
### Fatal
None.

### Major

1. **Optimization procedure is underspecified, harming reproducibility.** The paper defines the objective as $\operatorname{argmax}_w \text{Consistency}(G, w)$ with Pearson correlation, and constrains $G_j = \sum \mathbf{1}\{A_i^j > A_i^k\} \cdot w^s$. However, it never describes how this optimization is actually performed. No algorithm, solver, stopping criterion, learning rate, initialization scheme, or convergence check is provided. The paper says "we only introduce this straightforward implementation" (line 148) without specifying what the implementation is. This is a structural gap: even though the problem (maximizing Pearson correlation between $w$ and $G$ where $G$ is linear in $w$) is well-defined and differentiable, a reader cannot reproduce the results without knowing the solver. Given that 4 random seeds are reported, some randomized iterative procedure was used, but its details are absent.

2. **The reported performance gains (0.1, 2.5, 0.92 on PEN, CIN, LIS) do not cleanly match Table 1.** The paper states these as concrete improvements "compared to the Runner-up" (line 249). Cross-checking Table 1: the PEN gain of ≈0.1 is a reasonable average across configurations; the CIN gain of 2.5 matches the best cases (Chatbot Arena 0.4, MT-Bench 1.0). However, the LIS gain of 0.92 does not correspond to any entry in Table 1 — the closest values are 1.0 (Chatbot Arena 1.0, PiCO=10.00 vs PRE=9.00) and 0.75 (several configurations). The paper appears to be picking best-case or approximate numbers without specifying which dataset/volume they come from, undermining precision in the central performance claim.

### Minor

1. **No statistical significance testing.** Results are reported as means over 4 seeds with confidence intervals, but significance tests are not performed. Many comparisons (especially on AlpacaEval, e.g., PiCO PEN 1.17±0.02 vs PRE 1.18±0.03) show overlapping variance, making the claimed "consistent outperformance" (line 249) not statistically well-supported.

2. **The 60% elimination threshold is unsubstantiated.** The paper states it removes reviewers "until 60% of models are eliminated" (line 156) without justifying this specific threshold. Figure 4 shows CIN improving monotonically with more elimination, but the stopping point is presented as a fixed design choice rather than a tuned or cross-validated parameter. A sweep at finer granularity would strengthen the claim.

3. **No sensitivity analysis for key hyperparameters.** The permutation entropy order $k=3$, the number of reviewers per battle pair (5), and the random pair construction seed are all fixed without any robustness checks. These choices could materially affect results (e.g., $k=3$ vs $k=5$ in PEN).

4. **Forward Weight Voting outperformed by consistency optimization lacks discussion.** Table 2 shows "Random Weight + Consistency Optimization" improving over Forward Weight Voting (which uses ground-truth ranking to assign $w=[1,0.9,\dots,0]$). The paper reports this but does not discuss why an unsupervised optimization surpasses a prior that directly uses the human ranking. This is not suspicious — the linear forward weighting is unlikely to be optimal — but the lack of discussion leaves the reader to wonder whether the optimization is finding genuinely better weights or overfitting to the evaluation metric.

5. **The consistency assumption validation does not directly test the assumption.** The ablation in Table 2 tests whether forward weighting (with ground-truth ranking) beats backward/uniform weighting, which is consistent with the assumption. However, the fact that consistency optimization finds different (and better) weights than the forward oracle actually places the assumption under some tension — if stronger models were strictly better evaluators capturing the ground truth perfectly, the forward weights should be optimal. The paper does not reconcile this.

### Trivial

- **Tie handling in answer-ranking data is mentioned but not operationalized.** The partial order $\{>, <, =\}$ is defined (line 137) and tie verdicts are possible in the prompt (line 171), but how ties are incorporated into $G_j$ computation is not specified.

- **No description of how $w$ is parameterized** (scalar per model? bounded? initialized?).

## Suggestions
1. **Specify the optimization algorithm.** Even brief pseudocode or a sentence (e.g., "we perform gradient ascent on Pearson correlation $\rho(w, G)$ with respect to $w$, using a learning rate of 0.01 and stopping when $\rho$ changes by less than $10^{-4}$") would resolve the main reproducibility concern.

2. **Fix the imprecise performance claims.** Replace "gains of 0.1, 2.5, and 0.92" with specific dataset-configuration references (e.g., "on Chatbot Arena at full data volume, PiCO achieves gains of 0.13 (PEN), 3.0 (CIN), and 1.0 (LIS) over the runner-up PRE").

3. **Report significance tests** (e.g., paired bootstrap across the 4 seeds) for the main comparisons, especially on AlpacaEval where variance overlaps substantially.

4. **Add a decomposition experiment** showing CIN for: (a) no optimization + no elimination, (b) optimization only + no elimination, (c) elimination only + uniform weights, (d) full PiCO. This would clarify which component drives performance.

5. **Justify or sweep the 60% elimination threshold** with a finer-grained analysis.

6. **Discuss why Consistency Optimization beats Forward Weight Voting** — the paper should explain that forward weights are a simple linear heuristic and the optimization finds superior non-linear weights, which is evidence the weight space is richer than a rank-linear assignment.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
