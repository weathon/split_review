## Summary

GoalRank proposes a generator-only large ranking framework for recommender systems, motivated by the empirically observed saturation of Multi-Generator-Evaluator (MG-E) paradigms. The paper offers two contributions: (1) a theoretical proof that for any finite k-mixture G-E system, a sufficiently large single generator always achieves strictly smaller KL approximation error to the optimal policy, with error decreasing as the generator scales (scaling law); and (2) a group-relative optimization principle that uses a biased reward model to construct a reference policy, enabling practical training via cross-entropy minimization. GoalRank is validated on public benchmarks (ML-1M, Amazon-Book), two industrial datasets, and a large-scale A/B test on a platform with 500M+ daily users.

---

## Strengths

- **Credible industrial validation**: The online A/B test on a platform with hundreds of millions of daily users over 14 days is a strong, rare form of evidence. GoalRank consistently improves App Stay Time (+0.149%), Effective Views (+1.212%), and user engagement metrics vs. a production MG-E baseline with tens of generators and hundreds of candidate lists.
- **Clear empirical motivation for the research question**: Figure 1(d) demonstrates the performance saturation of scaling generators in MG-E, directly motivating the design choice to move to a single larger generator.
- **Compelling scaling laws**: Figure 3 shows that GoalRank's performance rises nearly monotonically from 1M to 0.1B parameters on the Industry-0.1B dataset, while all baselines (DNN, RankMixer, PIER, MG-E) plateau—providing empirical support for the theoretical claims.
- **Sensible group-relative normalization**: Equation 4 normalizes rewards by group mean and standard deviation before constructing the reference policy, mirroring the robustness mechanism in GRPO-style objectives. The ablation in Table 3 confirms graceful degradation under synthetic reward noise, supporting the design's practical robustness.
- **Fair experimental protocol**: All baselines share the same reward model as GoalRank (explicitly stated), and model embedding dimension is fixed at 128 for all methods in the main table, removing obvious confounds.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Theory–practice gap in the optimization objective**: Theorem 1 shows the *existence* of a generator-only model with strictly smaller KL($\pi^* \| \pi$) error (forward KL), but the practical training objective (Equation 5) minimizes KL($\pi^{\text{ref}} \| \pi_\theta$) (reverse KL, i.e., cross-entropy supervised by the reference policy). These two divergences have different minimizers and different properties (mode-seeking vs. mean-seeking). The paper does not formally connect the theoretical guarantee to the proposed loss, leaving a meaningful gap between the existence proof and the optimization principle.

2. **Vague "evidence upper bound" derivation**: The abstract and introduction repeatedly claim that the group-relative objective is derived from an "evidence upper bound of the one-stage optimization objective," but no such derivation is presented in the main text. This is treated as a key conceptual step, yet Equations 1–5 trace from the entropy-regularized oracle objective to the practical loss with only informal arguments (the bias condition in Equation 3 is presented as sufficient but not proven to hold under any studied construction).

3. **Large offline gains raise reproducibility concerns**: GoalRank improves H@6 by +17% on ML-1M and +25% on the Industry dataset over the strongest baselines. These are unusually large margins. The reward model is trained on "real user feedback data" (details removed to appendix), and the exact relationship between this training data and the test-set ground truth is unclear. Any overlap between the reward model's training distribution and the evaluation ground truth would create an inadvertent data-leakage advantage that baselines do not share—since baselines use the reward model only at inference while GoalRank uses it during training.

4. **Group construction is not truly generator-only at training time**: GoalRank requires an "auxiliary set of ranking policies M (including heuristic methods and lightweight neural models)" to construct diverse list groups with sufficient reward gaps (Section 3.3). This means GoalRank depends on multiple auxiliary models during training, undermining the "generator-only" framing and making deployment reproducibility dependent on the quality and availability of these auxiliary policies.

### Minor

1. **Connection to RLHF / GRPO literature is underexplored**: The group-relative normalization in Equation 4 is structurally identical to the advantage normalization in Group Relative Policy Optimization (GRPO), and the overall reward-to-policy pipeline closely mirrors offline preference alignment (DPO, RAFT). The paper would benefit from explicitly situating its optimization principle within this established line of work, both to credit prior art and to make clear what is genuinely novel in the adaptation to list-wise ranking.

2. **Scaling study uses only one dataset**: The scaling law experiment (Figure 3) is conducted exclusively on the proprietary Industry-0.1B dataset. Validation on the public Amazon-Book dataset (which has high baseline performance in Table 1) would strengthen the generality of the scaling claims.

3. **Group size ablation interpretation**: Table 2 shows degraded performance for large groups (|B| = 50–100). The explanation ("weakens the reward gaps, amplifying reward model bias") is plausible but not verified. An analysis of the reward gap distribution as a function of group size would make the claim more concrete.

### Trivial

- The paper uses "evidence upper bound" without defining what the "evidence" refers to in an information-theoretic or variational sense; this terminology is borrowed from variational inference but applied informally.

---

## Nice-to-Haves

- A head-to-head comparison of GoalRank vs. DPO- or GRPO-style baselines adapted for list-wise ranking would help isolate what is novel in the group-relative construction.
- Reporting per-dataset scaling curves (not only Industry-0.1B) would strengthen the universality of the scaling law claim.
- An analysis of inference latency vs. MG-E would clarify the efficiency advantage of the single-generator design.

---

## Novel Insights

The most genuinely novel aspect is the marriage of group-relative reward normalization (from the RLHF/LLM literature) with the permutation-space ranking problem. The intuition that normalizing rewards at the group level cancels absolute bias while preserving relative ordering—and that this weaker signal is sufficient to construct a useful reference policy—is a clean and transferable insight. The formal connection between the Boltzmann optimal policy (Equation 2) and the practical cross-entropy objective (Equation 5), even if not rigorously bridged in the main text, provides a useful conceptual scaffold for future work in reward-conditioned sequence ranking.

---

## Suggestions

- Formalize or remove the "evidence upper bound" claim: either provide the derivation in the main text or restate the contribution as an intuitive motivation rather than a formal result.
- Explicitly address the KL direction mismatch (forward KL in Theorem 1 vs. reverse KL in training loss), either by restating the theorem with the reverse KL or by adding a bridging lemma.
- Clarify the reward model data split: explicitly confirm that reward model training data and test-set interaction data do not overlap, or report results under strict hold-out conditions.
- Add a standalone GoalRank (without auxiliary policies) variant to the ablation to quantify the contribution of the auxiliary policy group construction.

---

## Score and Decision

GoalRank presents a practically compelling contribution: the generator-only reframing of recommendation ranking, supported by a credible theoretical motivation, a sensible group-relative objective, and compelling empirical evidence including a production A/B test at massive scale. The major weaknesses—the theory-practice gap, the underspecified evidence-bound derivation, and the training-time reliance on auxiliary models—are real but do not invalidate the core empirical claims. The online results in particular provide independent, real-world validation of the approach's effectiveness.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>