Now I have enough to write my final consolidated review. Let me synthesize everything.

---

## Summary
AdaBoN proposes a two-stage adaptive allocation strategy for Best-of-N alignment that distributes an inference budget across a batch of prompts. The first stage uses a small exploration budget to estimate per-prompt reward distributions via Gaussian KDE; the second stage uses a greedy marginal-gain algorithm to allocate the remaining budget. Evaluated across 12 LM-RM pairs and 3 datasets with 50 batches each, AdaBoN consistently beats the uniform allocation (BWR > 0.50) and is competitive with uniform allocations using ~20–30% larger budgets.

## Strengths
- **Broad, consistent empirical validation.** AdaBoN is evaluated across 12 distinct LM-RM pairs, 3 datasets (AlpacaEval, HH-RLHF, PKU-SafeRLHF), and 50 batches of prompts per setting. Table 1 shows median BWR > 0.50 for every pair, with values reaching 0.59–0.62. Table 2b shows >75% of batches have BWR > 0.50 across all pairs. The consistency of improvement across this breadth of settings is a genuine strength.
- **Model-agnostic and training-free design.** AdaBoN requires no auxiliary model training, contrasting with Damani et al. (2024), which requires training an MLP per LM-RM pair and budget value. The method uses only black-box LM calls and a reward model, demonstrated successfully across 12 LM-RM pairs without retuning.
- **Competitive against larger budgets, with clean latency properties.** EST values (Table 2a) of 148–155 at B=120 mean AdaBoN matches uniform allocations using 23–29% larger budgets. The two-stage design requires only two parallel LM-call phases, avoiding sequential dependencies that would increase latency.
- **Clean theoretical grounding with practical simplification.** Proposition 3.1 proves concavity of the marginal-gain function for any distribution with finite first moment, justifying the greedy allocation step. The KDE choice is empirically justified (Appendix K.3 compares against Gaussian and Skew-Normal MLE).
- **Performance scales with batch size.** Figure 3 shows monotonic BWR increase as K grows from 3 to 20, with gains up to 0.15 for some LM-RM pairs, demonstrating that AdaBoN effectively exploits cross-prompt budget reallocation in larger batches.

## Weaknesses

### Fatal
None.

### Major
- **No comparisons with any adaptive baseline.** The evaluation compares AdaBoN exclusively against the uniform (non-adaptive) allocation. While the authors provide reasonable justification for not comparing with Damani et al. (2024) — no existing implementation, computationally prohibitive training requirements (216,000 MLPs) — this does not excuse the absence of simpler adaptive heuristics. Natural baselines sharing the same two-stage structure (e.g., allocate remaining budget inversely to the best exploration reward, or proportionally to the gap between best reward and mean) would isolate whether the KDE+greedy combination specifically drives the gains, or whether any reasonable adaptive policy would achieve similar results. The paper's core claim that the *specific method* is effective is therefore weaker than it could be.

### Minor
- **Concavity gap between theory and practice is acknowledged but not analyzed.** Proposition 3.1 guarantees concavity for true expected gains, but the algorithm operates on Monte Carlo estimates from a KDE. The paper notes this ("While the greedy procedure may not be optimal when run on the estimated vectors, it still serves as an efficient heuristic") but does not empirically assess how often concavity is violated in practice. An empirical study of concavity violation rates would strengthen the connection between theoretical motivation and practical performance.
- **Modest effect sizes.** BWR values of 0.55–0.62 and EST values indicating ~25% budget savings are consistent but modest. The practical significance — whether a 25% compute saving on Best-of-N alignment meaningfully changes deployment decisions — is not fully clear. The paper is transparent about these numbers, so this does not undermine the claims, but it limits the impact.
- **Exploration budget is high and not systematically justified.** The paper fixes d = 0.75B across all experiments, noting this is a "good initial guess" and showing in the appendix that tuning provides minimal improvement. However, 75% of the per-prompt budget spent on exploration is unusually high, and a sensitivity analysis across a wider range (e.g., 0.5B to 0.9B) in the main evaluation would better characterize the exploration-exploitation tradeoff.

### Trivial
- The term "prompt-adaptive" could be slightly misleading; the method adapts at the batch level (given K prompts simultaneously), not in a single-prompt online setting. The paper is clear about the batch setup, so this is a framing precision issue only.
- Figure captions contain minor mislabeling (Figure 2 references "Medical, Math, and ArXiv datasets" instead of reward model names; Figure 3 references different datasets and method names inconsistent with the paper's content), likely parser artifacts.

## Nice-to-Haves
- A measure of practical gain such as the fraction of oracle-optimal reward (using infinite-budget maximum) that AdaBoN achieves relative to uniform allocation would help readers assess whether the improvement is substantial in absolute terms.
- Analysis of how sampling temperature and decoding strategy affect reward distributions and consequently allocation performance would strengthen the robustness claims.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "Lack of comparisons with Damani et al."** — The paper explicitly addresses this (Section 4.2, final paragraph): no existing implementation, would require 216,000 MLPs to train, computationally prohibitive. This is a valid justification and should not be held against the paper.
- **Harsh Critic: "Uncertainty quantification missing across runs"** — The paper uses 100 runs and reports Q1/Q3 interquartile ranges alongside medians, which provides reasonable uncertainty quantification for this setting.
- **Harsh Critic: "No formal hypothesis tests"** — Formal hypothesis testing is not standard practice for large-scale LLM benchmark evaluations in this community.
- **Harsh Critic: "Temperature/decoding strategy not examined"** — The paper already evaluates across 12 LM-RM pairs and 3 datasets; this is scope creep.
- **Harsh Critic: "Bernoulli example over-emphasizes adaptivity benefit"** — The Bernoulli example in Section 2.3 is a pedagogical illustration, not a claim about real reward distributions. The paper explicitly notes real rewards are smooth (Section 3.1).
- **Harsh Critic: "KDE vs. empirical distribution ablation needed"** — The paper compares KDE against Gaussian and Skew-Normal MLE in the appendix (Table 16), which already addresses estimator choice.
- **Harsh Critic: "No analysis of whether BWR improvement stems from more KDE samples or greater prompt variance"** — This is a fine-grained analysis question, not a weakness of the current evaluation, which already demonstrates the core phenomenon.

## Novel Insights
The synthesis of reviewers reveals an interesting tension in the evaluation of adaptive inference methods: the uniform allocation is simultaneously the right baseline (it is minimax-optimal without knowledge of reward distributions) and an insufficient one (any reasonable adaptive method should beat it). The paper's evaluation demonstrates its method works, but the field would benefit from established intermediate adaptive baselines that calibrate how much of the gain is attributable to adaptivity itself versus the specific allocation algorithm. This is a gap not just for this paper but for the broader literature on adaptive test-time compute allocation.

## Suggestions
- Add at least one simple adaptive baseline (e.g., allocate remaining budget inversely proportional to the max reward observed during exploration, or proportional to the gap between max reward and mean). This would directly isolate the contribution of the KDE+greedy design.
- Include an empirical check on how often the estimated marginal-gain vectors violate concavity in practice, and whether the greedy procedure's performance degrades under those violations.
- Provide a sensitivity analysis for the exploration budget d across {0.5B, 0.6B, 0.75B, 0.9B} in the main results rather than deferring entirely to the appendix.

---

**Originality:** The method is a straightforward combination of KDE + greedy allocation applied to a new problem setting. The contribution lies more in the practical demonstration that this simple approach works well across diverse LM-RM pairs than in algorithmic novelty.

**Importance:** Adaptive allocation of inference compute is a timely and practically relevant problem as Best-of-N alignment becomes more widely used. The model-free, training-free nature of AdaBoN makes it immediately deployable.

**Claims supported:** The core claim that AdaBoN outperforms uniform allocation is well-supported across 12 LM-RM pairs. The claim that the method is competitive with ~25% larger budgets is supported. The claim that specific design choices (KDE, greedy) are necessary is not fully supported due to the lack of adaptive baselines.

**Soundness:** The experimental design is sound — appropriate metrics (BWR, EST), multiple batches, consistent methodology. The theoretical grounding (Proposition 3.1) is correct. The main gap is the absence of adaptive baselines.

**Clarity:** The paper is generally well-written, with clear notation (Section 2.1) and well-motivated design choices. The two-stage design is easy to understand and implement.

**Value to community:** AdaBoN offers a practical, training-free tool for more efficient Best-of-N alignment that can be adopted immediately. The BWR and EST metrics may also be useful for future work in this area. The main limitation is the modest effect size, which constrains the practical impact.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>