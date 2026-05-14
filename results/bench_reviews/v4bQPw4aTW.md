Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes AdaBoN, a two-stage adaptive algorithm for Best-of-N alignment that allocates inference compute across prompts in a batch. The method first uses a small exploration budget to estimate each prompt's reward distribution via Gaussian KDE, then greedily allocates the remaining budget based on estimated marginal gains. Evaluated across 12 LM-RM pairs, 3 datasets, and 50 batches per configuration, AdaBoN consistently outperforms uniform allocation (BWR 0.54–0.62) and competes with 20–27% larger uniform budgets.

## Strengths

- **Consistent empirical outperformance of uniform allocation across broad experimental scope**: Table 2b shows BWR > 0.50 for 76–100% of batches across all 12 LM-RM pairs on AlpacaEval, with median BWRs reaching 0.62 (Table 1). Results are replicated on HH-RLHF and PKU-SafeRLHF datasets (Appendix H). This breadth of evaluation (4 LMs × 3 RMs × 3 datasets × 50 batches = 12 LM-RM pairs) is more extensive than prior work (Damani et al., 2024).

- **Competitive against substantially larger inference budgets**: Table 2a reports median EST of 150–153 for B=120, meaning AdaBoN's adaptive allocation with budget B matches uniform allocation with ~25% more budget. Figure 2b shows some batches achieving EST ≥ 160 (33% larger budget).

- **Simple, practical, model-agnostic design with latency benefits**: AdaBoN requires no auxiliary training (unlike Damani et al., 2024), works with any LM-RM combination out of the box, and needs only two serial calls to the base LM (one for exploration, one for final allocation), enabling parallelization.

- **New evaluation metrics tailored to reward model semantics**: BWR and EST are well-motivated for settings where RM scores are only meaningful comparatively. The tie-breaking conventions (1/2 for BWR, full weight for EST) are sensible and properly calibrated so that uniform against itself yields 0.50.

- **Theoretical grounding for greedy allocation**: Proposition 3.1 establishes concavity and monotonicity of the expected max function, ensuring greedy allocation is optimal on the true value vectors (Federgreen & Groenevelt, 1986).

## Weaknesses

### Fatal
None.

### Major

- **Absence of any adaptive baseline comparison**: The paper compares AdaBoN only to uniform allocation. Without comparisons to even simple adaptive heuristics (e.g., allocate remaining budget proportionally to observed maximum reward during exploration, or proportional to estimated variance), the experiments demonstrate only that *being adaptive helps*, not that *AdaBoN's specific mechanism* (KDE estimation + greedy allocation) is an effective way to be adaptive. The paper argues against comparing with Damani et al. (2024) for practical reasons (computational cost of training 216K MLPs), which is reasonable, but it does not include any lightweight heuristic baseline. This significantly limits what the experimental results can claim. (Section 4.2–4.3)

### Minor

- **Closed-loop evaluation (same RM for allocation and evaluation)**: The reward model used to guide allocation is also used to compute BWR and EST. While the comparison against uniform allocation is fair (both use the same RM), the results do not assess whether AdaBoN improves *true alignment quality* as judged by a different RM or human evaluators. The paper implicitly acknowledges this via its choice to use comparative metrics, but the limitation is worth stating explicitly.

- **Hyperparameter tuning at least partially on the evaluation data**: The paper states that the exploration budget \(d\) is chosen by evaluating across \(d \in \{0.60B, 0.7B, 0.75B, 0.80B\}\) on the same 50 batches used for reporting results (Appendix G.1). While the paper is transparent about this and shows that \(d=0.75B\) works nearly as well as the tuned optimum, and only 4 discrete values are considered, the reported BWRs may be mildly optimistic. A held-out validation split would be more rigorous.

- **Limited range of exploration budget values tested**: The tuning range \(d \in \{0.60B, 0.7B, 0.75B, 0.80B\}\) is narrow and does not include small values like \(0.1B\) or \(0.25B\) that would test whether KDE can work with far fewer samples. Since the paper claims reward distributions are "smooth and easy to learn" (Section 3.1), a sensitivity study with much smaller \(d\) would strengthen this claim.

- **Performance varies noticeably across LM-RM pairs**: The Qwen-Armo pair achieves only 0.54 median BWR with only 78% of batches above 0.50 (Tables 1, 2b). The paper's explanation (left-skewed distributions, Appendix G.1) is post-hoc and not experimentally validated. This suggests the method is not uniformly robust across all LM-RM combinations.

### Trivial
None.

## Nice-to-Haves

- A simple adaptive heuristic baseline (e.g., allocate remaining budget proportionally to observed max reward during exploration) would substantially strengthen the paper's claims about AdaBoN's specific design choices.
- A hold-out validation procedure for the exploration budget \(d\) would address the mild data-leakage concern.
- Evaluation with a different reward model at test time (RM used for allocation ≠ RM used for evaluation) would test for reward-model overfitting.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The two-prompt Bernoulli example is cherry-picked"**: The example is explicitly presented as a simple illustrative case to motivate why adaptivity helps. It is not meant to correspond to the real-valued setting. This is a strawman criticism.
- **"Proposition 3.1 is a simple known fact... not a theoretical contribution"**: The paper does not claim Proposition 3.1 as a major theoretical contribution; it is stated to justify the greedy algorithm's optimality on true vectors. Its simplicity does not weaken the paper.
- **"No confidence intervals for the median BWR"**: The paper provides Q1/Q3 quartiles, which are appropriate for non-parametric reporting of distributions across 50 batches. This is sufficient for the claims made.
- **"The exploration budget 75% undermines efficiency claims"**: The paper tunes \(d\) and finds \(d=0.75B\) works best across settings. The BWRs, while modest (0.54–0.62), still show consistent win rates. The critic's characterization that this "undermines" the claim is overstated; it is a limitation worth noting but not fatal.
- **"Lack of goodness-of-fit tests for reward distributions"**: The paper shows histograms (Figure 1), compares KDE against Gaussian and Skew-Normal fits (Appendix K.3, Table 16), and finds KDE works best. This is adequate evidence for an empirical systems paper.

## Novel Insights

The most interesting observation from these reviews is a structural pattern in the adaptive compute allocation literature: multiple papers (AdaBoN, the bandit learning approach of 0mNnINd2z5, and the optimal stopping paper fZJvPuadUT) all share the same fundamental weakness—they compare only against uniform allocation and not against other simple adaptive strategies. This suggests the community lacks established, standardized baselines for adaptive test-time compute allocation, making it difficult to judge whether any specific adaptive mechanism provides marginal value beyond "just being adaptive." For AdaBoN specifically, the paper's real contribution may be less about the algorithmic novelty (two-stage explore-then-allocate is a natural idea) and more about the empirical demonstration of its effectiveness across 12 LM-RM pairs—a level of breadth that prior work on this problem lacks.

## Suggestions

1. **Add a simple adaptive baseline**: After the exploration stage, allocate remaining budget proportionally to each prompt's observed max reward (or to the estimated distribution's tail heaviness). If AdaBoN outperforms this, the KDE+greedy machinery is justified. If not, the paper's contribution is merely demonstrating that adaptivity helps, which is already known.
2. **Perform a full sensitivity study on \(d\)**: Test \(d/B \in \{0.1, 0.25, 0.5, 0.75, 0.9\}\) to characterize the exploration-exploitation tradeoff and verify that the claim "reward distributions are easy to learn" holds with smaller budgets.
3. **Hold out a validation set for hyperparameter selection**: Reserve some batches from each dataset for tuning \(d\) and report results on the remainder.
4. **Consider a cross-RM evaluation**: Use one RM for allocation and a different RM (or human preference data) for evaluation to assess robustness to reward model misspecification.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| /home/wg25r/review_agent/human_reviews_2026/EZn2TmBBfF.md | 6.00 | Stronger paper: provides both theory and comprehensive empirical validation for BoN reward hacking mitigation. AdaBoN has broader empirical scope but weaker theoretical contribution. |
| /home/wg25r/review_agent/human_reviews_2026/0mNnINd2z5.md | 4.00 | Similar quality: both address adaptive compute allocation and share the weakness of missing adaptive baselines. That paper was accepted as Poster. AdaBoN has broader experiments (12 LM-RM pairs vs bandit paper's focused scope) but weaker theory. |
| /home/wg25r/review_agent/human_reviews_2026/fZJvPuadUT.md | 4.00 | Similar weaknesses (missing adaptive baselines), rejected. AdaBoN has more thorough experiments across more LM-RM pairs and datasets. |
| /home/wg25r/review_agent/human_reviews_2026/ztGHhyicWs.md | 3.50 | Weaker paper: training-free difficulty proxies paper, rejected for incremental contribution. AdaBoN has broader empirical evaluation and clearer practical contribution. |
| /home/wg25r/review_agent/human_reviews_2026/Zb3yuOZVDN.md | 2.00 | Much weaker: Withdrawn paper with significant quality issues. AdaBoN is substantially stronger. |
| /home/wg25r/review_agent/human_reviews_2026/ZNWpUfwisS.md | 0.67 | Incomplete manuscript, withdrawn. AdaBoN is not comparable to this. |

### Assessment

The paper addresses a well-motivated practical problem, proposes a simple and sensible method, and evaluates it with unusual breadth across LM-RM pairs and datasets. The main weakness—lack of any adaptive baseline comparison—is genuine and limits what the results can claim. However, the paper's contribution (demonstrating that a simple KDE-based two-stage allocation consistently beats uniform across 12 LM-RM pairs) is still valuable, particularly given the practical constraints (no auxiliary training, low latency). The paper falls short of a strong acceptance but has clear merit. Relative to the calibration anchors, it sits between the accepted bandit paper (4.00) and the stronger reward-hacking paper (6.00).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>