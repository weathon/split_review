## Summary

This paper proposes ARPO (Agentic Reinforced Policy Optimization), an RL algorithm for training multi-turn LLM-based agents. The core idea is an entropy-based adaptive rollout mechanism that selectively spawns branch samples at high-entropy tool-call steps, combined with an advantage attribution scheme for the resulting branched trajectories. Evaluated across 13 benchmarks spanning mathematical reasoning, knowledge-intensive reasoning, and deep search, ARPO consistently outperforms trajectory-level RL baselines (GRPO, DAPO, REINFORCE++) while claiming to use only half the tool-call budget.

## Strengths

- **Well-motivated empirical observation driving the method**: The pilot experiments in Section 2 (Figures 1-2) systematically quantify token entropy spikes after tool-call feedback across multiple agent types (search engine and Python interpreter), providing three concrete observations (Ob.1–Ob.3) that directly motivate the branching mechanism. This grounding in empirical observation rather than pure intuition is a strength.

- **Consistent improvements across 13 benchmarks and multiple model families**: Table 1 shows ARPO outperforms GRPO, DAPO, and REINFORCE++ on both Llama3.1-8B and Qwen2.5-7B across 10 reasoning tasks (average ~4% gain). Table 2 shows gains on deep search benchmarks with Qwen3-8B and Qwen3-14B (e.g., GAIA Avg: 43.7 vs. 36.9 for Qwen3-14B). The cross-architecture consistency is notable.

- **Efficiency claim with partial evidence**: Figure 7a demonstrates ARPO uses ~250–300 tool API calls per step versus GRPO's ~400–450, and the paper reports this is achieved with only 1k RL training samples for DeepSearch tasks. While the efficiency claim has gaps (see weaknesses), the tool-call savings themselves are clearly demonstrated.

- **Rollout diversity analysis**: The PCA+DBSCAN clustering analysis (Figure 7b) provides quantitative evidence that ARPO produces more distinct behavioral clusters (54 vs. 48) from trajectories, moving beyond purely qualitative diversity arguments.

- **Soft advantage estimation justification**: The paper presents both hard and soft advantage variants with experimental comparison (Figure 5), showing soft advantage yields more stable reward curves. This is a well-supported design choice rather than an arbitrary one.

## Weaknesses

### Fatal

None

### Major

- **Theoretical section overclaims novelty**: Section 3.3 presents a "Generalized Policy Gradient Theorem" (Equation 6) as one of four key contributions (bullet 3 in the introduction). However, formulating policy gradients over temporally extended actions (macro-actions/options) is well-established in hierarchical RL, rooted in the options framework (Sutton, Precup, Singh 1999) which the paper itself cites. The paper even acknowledges this: "This generalization encompasses the traditional Policy Gradient Theorem (Sutton et al., 1999)... as a specific instance of our broader GPG framework." Restating known results with Transformer-specific notation and claiming them as a novel theorem is an overclaim that accounts for a significant portion of the stated contributions.

- **Tool-call efficiency claims lack total compute accounting**: The paper repeatedly emphasizes ARPO achieves better performance with "only half the tool-call budget" (abstract, Section 5.2, Figure 7a). However, ARPO branches at high-entropy steps, generating Z partial paths per branch, each requiring LLM forward passes and generation steps. The paper's footnote 1 dismisses "the minor overhead from token-level entropy calculations," but the real cost is additional LLM inference for branched paths. Since ARPO produces M total trajectories (N global + M−N partial), matching GRPO's total trajectory count, total LLM compute may not decrease. Figure 7a measures only tool API calls, not total FLOPs, wall-clock time, or LLM inference cost. This undermines the paper's central practical efficiency argument.

- **Missing key ablation in main text: entropy-based branching vs. random branching**: Without comparing entropy-guided branching against branching at randomly selected tool-call steps, it is unclear whether improvements stem from the entropy signal specifically or simply from having more diverse rollouts via any branching strategy. The paper references "More ablation and scaling analyses can be found in the Appendix A.2" but the main text does not present this critical comparison. This is the single most important experiment for validating ARPO's core thesis, and it should be featured prominently rather than deferred.

### Minor

- **No variance or confidence intervals reported**: All results in Tables 1 and 2 are single-run numbers. Given the sensitivity of RL training to random seeds, and that several gains are modest (~2–4%), reporting variance is important for assessing reliability. At least one additional run with different seeds would substantially strengthen the claims.

- **Pass@K analysis only shown for ARPO, not baselines**: Figure 6 presents Pass@1/3/5 scaling only for ARPO-trained models (Qwen3-8B and Qwen3-14B). Without GRPO baselines shown at Pass@3/5, we cannot determine whether the scaling behavior is unique to ARPO or a property of multi-sample evaluation in general.

- **Multi-tool reward bonus (r_M) creates a narrative tension**: Equation 5 gives a reward bonus (r_M = 0.1) for using both search and Python tools. The paper states "We follow Tool-Star (Dong et al., 2025)" suggesting this is applied consistently across methods. However, this directly incentivizes the multi-tool behavior that ARPO claims to discover organically through entropy-based exploration, weakening the narrative that ARPO naturally discovers better tool-use strategies. If the bonus is applied to all baselines, it should be explicitly stated for transparency.

- **DBSCAN clustering analysis parameters unspecified**: The rollout diversity analysis (Section 5.2, Figure 7b) uses DBSCAN with unspecified epsilon parameter. The cluster count difference (54 vs. 48) is modest. While the visual separation is suggestive, the analysis would be stronger with stated parameters and additional diversity metrics.

### Trivial

- The word "pioneeringly" in the first contribution bullet (Section 1) should not appear in a research paper.

## Nice-to-Haves

- An ablation varying the entropy threshold τ and monitored token count k would help practitioners understand when and how to apply ARPO.
- Reporting total training wall-clock time alongside tool-call counts would make the efficiency comparison more meaningful.
- Analysis of failure cases (when ARPO underperforms GRPO) would be more informative than additional benchmarks.
- A direct comparison of DeepSearch results separating the RL-trained models and workflow/non-RL methods into distinct evaluation contexts would improve clarity.

## Removed Points

These points are flagged to be removed per filtering rules; treat them with caution:

- **DeepSearch LLM-as-Judge bias concern**: The harsh critic raised concern that Qwen2.5-72B-instruct as judge could favor Qwen-family models. While plausible, this is a general concern about LLM-as-Judge evaluation that applies broadly in the field. The paper follows standard evaluation practices. Removed as a generic methodological concern rather than a paper-specific problem.
- **DeepSearch fairness with non-RL baselines**: The critic argued comparing ARPO to non-RL workflow methods and much larger models is misleading. However, Table 2 clearly separates these categories (gray text for larger models, distinct rows for different method types), and the core comparison is ARPO vs. GRPO within the same model family. Removed as the presentation is reasonably transparent.
- **Computational complexity claim (O(n log n) to O(n²))**: The harsh critic noted this claim conflate tool API calls with computational complexity. This is a valid nitpick but the footnote clarifies the scope. Demoted to trivial and removed.

## Novel Insights

The paper's genuinely novel contribution is the empirical observation that token entropy spikes reliably after tool-call feedback (Ob.1–Ob.3 in Section 2), and the corresponding design of an entropy-guided branching mechanism that converts this signal into targeted exploration. This bridges an interesting gap between entropy-based analysis of LLM reasoning (previously studied in single-turn settings) and multi-turn agentic RL. The insight that branching diversity should be concentrated at high-uncertainty decision points rather than uniformly distributed is valuable and, if validated against a random-branching baseline, could be a meaningful methodological contribution to the growing field of agentic RL.

## Suggestions

1. **Feature the entropy-vs-random branching ablation in the main text.** This is the single experiment that validates the core thesis. Present it with multiple seeds and error bars.
2. **Report total compute cost.** Replace or supplement Figure 7a with total LLM inference FLOPs or wall-clock training time. The tool-call count alone is insufficient to support the efficiency claim.
3. **Reframe Section 3.3.** Rather than presenting the macro-action policy gradient as a new theorem, position it as applying known hierarchical RL theory to validate ARPO's partial rollout approach. This is honest and still useful.
4. **Add variance reporting.** Even two runs per method would substantially increase confidence in the reported improvements.

## Calibration Report

**Round 1 (Bracketing):**
- Weak anchors (≤3.5): CollabUIAgents (3.00), LLMs Synergy (3.40), LLIT (2.33), LLaVA-Plus (3.25)
- Middle anchors (3.5–7.5): StepTool (5.50, Reject), JOSH/Sparse Rewards (4.75, Reject), MetaTool (5.00, Reject), REFUEL (6.50, Accept), AgentQuest (6.25, Accept), GPO (5.67, Accept), TPO (6.33, Accept), SynPO (6.60, Accept), COPO (7.33, Accept), TIS-DPO (7.00, Accept)
- Strong anchors (≥7.5): MaestroMotif (7.75, Accept), DeepLTL (8.00, Accept)

Initial bracket: **5.5–7.0**. ARPO is clearly stronger than StepTool (5.50) — it has a more novel mechanism (entropy-based branching vs. step-level reward shaping), broader evaluation (13 vs. ~4 benchmarks), and cross-model generalization. ARPO is comparable to REFUEL (6.50) in empirical breadth but has a weaker theoretical contribution and less rigorous theoretical grounding.

**Round 2 (Narrowing):**
- Lower bracket (4.0–6.5): StepTool (5.50), ToolComp (5.40), Algorithm Distillation (5.50), GPO (5.67)
- Upper bracket (6.0–8.0): TPO (6.33), SynPO (6.60), COPO (7.33), TIS-DPO (7.00)

ARPO is clearly above StepTool (5.50) and GPO (5.67). It's comparable to REFUEL (6.50) and TPO (6.33) — all have consistent but modest improvements, with some overclaiming. ARPO's broader empirical evaluation and unique mechanism push it slightly above these anchors, but the theoretical overclaiming and missing ablations pull it back from COPO (7.33) territory. Final score: **6.5**.

**Final score position:** 6.5, matching REFUEL. ARPO has stronger empirical breadth than StepTool (5.50) and comparable contributions to TPO/SynPO (6.33–6.60), but falls short of COPO (7.33) due to weaker theoretical grounding and missing critical ablations.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>