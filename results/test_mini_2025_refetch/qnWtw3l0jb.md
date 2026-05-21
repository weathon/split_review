Now I have solid calibration data. Let me synthesize the final review.

**Bracket analysis:**
- Round 1 bracketing: This paper clearly sits above the weak band (avg <3.5) and within the middle-to-strong range. Narrowest plausible bracket: 5.5–8.0.
- Round 2 narrowing: Comparing to closely related papers — π2vec (5.25, successor features for policy evaluation), DVFB (6.67, FB for zero-shot RL), Proto Successor Measure (6.75 avg but rejected), RoboFlamingo (6.50, VLM for IL), and Imitation Learning from Observation with ADS (6.50) — the current paper is stronger than all of these in terms of experimental thoroughness (21 tasks, 4 domains, 20 seeds), theoretical grounding, and breadth of contribution (5+ IL principles from a single model). The most comparable paper, DVFB (FB representations for zero-shot RL, avg 6.67, accepted poster), is slightly less comprehensive. The current paper is stronger.
- Final score: 7.0 — a strong accept. This is above π2vec (5.25), above RoboFlamingo (6.50), above ADS (6.50), and above DVFB (6.67), reflecting the paper's more thorough evaluation and broader contribution.

Now I'll write the consolidated review.

Let me also think carefully about what to move to "Removed Points":

1. **Harsh critic's "Coverage of pre-training data is not analyzed"** — This is a genuine methodological gap. The paper relies on RND exploration data but doesn't check if expert states are covered. The paper acknowledges this indirectly in App. G. This is a legitimate minor weakness. **Keep as Minor.**

2. **Harsh critic's "Stationary imitation performance..."** — Valid point about slight overclaiming in the abstract. The abstract says "matches, and often surpasses" but for stationary-only methods the best FB-IL is 68.9 vs TDIL 70.0. **Keep as Minor.**

3. **Harsh critic's "Error bars in main figure"** — The paper defers variance to Appendix E.3. This is standard. However, the paper could add a note. **Demote to Trivial.**

4. **Harsh critic's "Comparison to a stronger stationary offline baseline" with significance test** — Nice-to-have suggestion. **Move to Nice-to-Haves.**

5. **Harsh critic's "Discussion of FB's rank-d approximation"** — The paper acknowledges this. Nice-to-have. **Move to Nice-to-Haves.**

6. **Harsh critic's "Pre-training compute cost"** — Nice-to-have. **Move to Nice-to-Haves.**

7. **Strength Finder's generic strengths** — All strengths are concrete and specific. Keep all.

Now let me write the review.## Summary

This paper introduces FB-IL, a family of imitation learning methods built on a pretrained Forward-Backward (FB) successor-measure model — a "behavior foundation model" (BFM).  The core contribution is showing that a single FB model, pretrained on task-agnostic unsupervised interactions, can implement at least five distinct IL principles (behavioral cloning, reward-based, feature matching, Bellman residual minimization, and goal-based imitation) using only a few expert demonstrations at test time, with no need to solve a new reinforcement learning problem.  Experiments across 21 tasks in 4 domains (DeepMind Control Suite) demonstrate that FB-IL matches the performance of state-of-the-art offline IL algorithms while producing imitation policies in seconds rather than hours — a speedup of roughly three orders of magnitude — and outperforms alternative BFM approaches (DIAYN, MaskDP, Goal-GPT, Goal-TD3).

## Strengths

- **Dramatic test-time speedup with competitive accuracy.**  Figure 2 shows offline IL baselines require 3–13 hours per task, while FB-IL methods produce policies in <5 seconds to 4 minutes.  This speedup is achieved while matching or exceeding SOTA offline IL performance: ER_FB (68.9%), BC_FB (68.2%), BBELL_FB (68.5%) versus the best stationary offline baseline TDIL (70.0%), with the goal-based variant Goal_FB reaching 78.6%.  The per-domain breakdown in Figure 3 confirms this pattern across all four environments.

- **Unified framework for multiple IL principles from a single pretrained model.**  Section 4 derives concrete FB-based algorithms for BC (BC_FB), reward-based imitation (ER_FB, RER_FB), successor feature matching (FM_FB), Bellman residual minimization (BBELL_FB, FBLOSS_FB), and goal-based imitation (Goal_FB).  No other BFM method in the comparison (DIAYN, Goal-GPT, MaskDP, Goal-TD3) offers this breadth.  The derivations are clean and follow naturally from the FB properties established in Proposition 1.

- **Thorough and well-designed experimental protocol.**  The evaluation spans 21 tasks across 4 domains, uses 20 random seeds per algorithm-task pair, and averages over 10 independently pretrained FB models.  Ablations include warm-start analysis (App. E.2), distribution shift robustness (App. E.5), sensitivity to the number of expert demonstrations (App. E.4), and variance across FB pretraining seeds (App. E.3) — all of which support the main claims.

- **Demonstrated effectiveness on non-stationary, non-realizable expert behaviors.**  Section 5.3 shows that Goal_FB (49.53±4.06) matches Goal-TD3 (50.76±6.52) and significantly outperforms Goal-GPT (17.58±0.82) on yoga-pose waypoint imitation, using the same pretrained FB model without any task-specific fine-tuning.  This tests the method in a regime where stationary-policy assumptions are violated.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Slight overclaiming in the abstract for stationary tasks.**  The abstract states that FB-IL "matches, and often surpasses, the performance of SOTA offline IL algorithms."  For stationary (non-goal-based) methods, the best FB-IL methods (BC_FB 68.2%, ER_FB 68.9%, BBELL_FB 68.5%) are *slightly below* the best stationary offline baseline TDIL (70.0%) in the aggregated Figure 1. The "surpasses" claim is fully supported only by Goal_FB (78.6%), which the paper itself notes has "more restricted applicability" (Section 4.4).  The authors should qualify the abstract to clearly separate stationary and goal-based claims — e.g., "matches SOTA stationary offline IL and outperforms them on goal-based tasks" — to avoid overstatement.  (The paper's own Section 5.1 wording "on-par or better" is appropriate.)

2. **No analysis of how well the pretraining data covers expert-visited states.**  The FB model is pretrained on RND exploration data, and FB-IL's success depends on whether successor measures of expert states lie within the learned representation.  The paper notes in Appendix G that offline baselines improve when the unsupervised dataset includes expert samples, suggesting coverage matters.  Yet there is no quantitative metric (e.g., density ratio, reconstruction error, or state-support overlap) comparing expert state coverage against the RND dataset.  While this does not invalidate any result, it would help practitioners understand when the approach might fail (e.g., tasks requiring states far from the exploration distribution).

3. **Missing error visualization in the main aggregate figure (Figure 1).**  The paper reports variance in Appendix E.3 but Figure 1 shows only point estimates without error bars or confidence bands.  For a headline claim of "matching or surpassing SOTA," the main figure should at minimum include a caption statement that variance is deferred to the appendix (it does not) or display error bars for the aggregated bars.  None of the paper's other claims depend on whether individual differences are significant, so this is a presentation issue rather than an evidential one.

### Trivial

- The main aggregate bar chart (Figure 1) and Figure 2 are presented as raw LaTeX tables with image references that appear broken in the extracted text.  These are parser artifacts, not author issues, but the production version should ensure clear figure rendering.

## Nice-to-Haves

- A statistical significance test (e.g., bootstrap) comparing the best stationary FB-IL methods against TDIL would clarify whether the ~1-point gap is meaningful; if not significant, it would strengthen the "on-par" claim.
- Reporting the GPU-hours required for FB pretraining would contextualize the test-time speedup tradeoff, particularly for practitioners evaluating total compute cost.
- An empirical illustration of how the rank-d approximation degrades imitation quality on specific tasks (e.g., by analyzing eigenvalue decay of the B-embedding or comparing FB's successor measure reconstruction error against expert trajectories) would illuminate the theoretical limitation acknowledged in the conclusion.

## Removed Points

- **Strength Finder's strength about "robustness under distribution shift"** — This is valid and supported by App. E.5.  Retained in Strengths.
- **Go through sweeping / speculative weaknesses from Harsh Critic:** The following were removed or demoted because they are either standard practice, addressed in the paper, or outside scope:
  - The request for significance testing between FB-IL and TDIL was moved to Nice-to-Haves (demoted from Minor) because the ~1-point gap does not threaten any core claim and significance testing is not standard for aggregate bar charts across 21 tasks.
  - The comment about FB's rank-d approximation lacking empirical illustration was moved to Nice-to-Haves (demoted from Minor) because the paper acknowledges this theoretical limitation explicitly in the conclusion and further analysis is beyond scope.
  - The missing pre-training compute cost was moved to Nice-to-Haves (demoted from Minor). The paper's core claim is about test-time speed; pretraining cost is orthogonal.
  - The coverage analysis criticism was retained as Minor (see Weaknesses #2) after verifying from the paper that no such analysis exists — it is a genuine gap, though not fatal.

## Novel Insights

None beyond the paper's own contributions.  Both the Harsh Critic and Strength Finder reviews faithfully reflect the paper's content without introducing new analytical perspectives.  The key observation that unifies both reviews is that the paper's main idea (applying FB successor measures to IL) is well-executed but the headline claims in the abstract slightly outpace the stationary-task evidence, and the dependency on pretraining coverage is unexamined.

## Suggestions

1. In the abstract and conclusion, clearly separate the stationary and goal-based claims.  For example: "FB-IL matches the performance of SOTA offline IL on stationary tasks, and the goal-based variant (Goal_FB) surpasses all baselines on tasks where goal-based imitation is applicable."
2. Add a brief analysis (in the appendix if not the main text) quantifying how well the RND exploration data covers the state support of the expert trajectories used across the 21 tasks — even a simple density-ratio visualization across domains would address the largest unanswered methodological question.
3. Include explicit error bars or confidence bands in the aggregated Figure 1, or at minimum add a caption note that variance is reported in Appendix E.3.

## Score and Decision

**Calibration anchors:**
| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| π2vec: Policy Representation with Successor Features | o5Bqa4o5Mi.md | 5.25 | R1/R2 | Uses successor features for policy evaluation; current paper is broader, more thorough, and more strongly supported. Current paper is stronger. |
| DVFB: Zero-Shot RL via Dual-Value FB | 0QnKnt411O.md | 6.67 | R2 | Also uses FB representations for zero-shot problems; similar evaluation scope but fewer tasks (12 vs 21). Current paper is comparably strong, slightly more comprehensive. |
| RoboFlamingo: VLM-based Robot Imitation | lFYj0oibGR.md | 6.50 | R1/R2 | Imitation via foundation models; strong empirical results but less theoretical depth. Current paper is at least comparable. |
| Proto Successor Measure | s9SVlWOcLt.md | 6.75 | R2 | Related successor-measure work but rejected due to limited experiments (2 environments). Current paper's evaluation is far more extensive. |
| Imitation Learning from Observation with ADS | pPJTQYOpNI.md | 6.50 | R2 | Simple but effective IL contribution; 9 tasks. Current paper is more original and comprehensive. |
| Video In-context Learning | wkbx7BRAsM.md | 7.00 | R2 | Zero-shot video imitation; different domain but similar quality tier. Current paper is comparably strong. |
| Unsupervised RL (weak band) | Various | 2.0–3.33 | R1 | Clearly below current paper's quality. |

**Round 1 bracket:** 5.5–8.0. **Round 2 narrowing:** Above π2vec (5.25), above ADS (6.50), comparable to or stronger than DVFB (6.67) and RoboFlamingo (6.50). The paper's experimental thoroughness and breadth of contributions place it above the average poster-level paper.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>