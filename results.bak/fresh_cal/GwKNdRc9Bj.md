Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper introduces ADLoss, a method for Preference-based Reinforcement Learning (PbRL) that uses the jointly learned policy to compute an action distance (expected number of steps between state-action pairs under the current policy) and incorporates it as an auxiliary prediction task for the reward model via metric multi-dimensional scaling. The key idea is to force the reward model's embedding space to preserve action distances, thereby providing structural information about state reachability and dynamics to improve reward learning. Experiments on six Meta-World continuous control tasks against state-of-the-art PbRL baselines (PEBBLE, SURF) and several adapted baselines show substantial and consistent improvements, with a small human-in-the-loop study providing additional validation.

## Strengths

1. **Novel and well-motivated contribution to PbRL**: The paper is the first to exploit the jointly learned policy's structure (action distances) as an auxiliary signal for reward learning in PbRL. This is a genuinely new direction — prior work focused on query sampling, data augmentation, or pre-training, not on extracting information from the policy being learned. The paper clearly distinguishes itself from related work on goal-conditioned RL (Hartikainen et al. 2019, Venkattaramanujam et al. 2019) by noting that its method requires no explicit goal proposals.

2. **Consistent and substantial empirical improvement across all six tasks**: Figure 2 shows ADLoss consistently and substantially outperforming PEBBLE and SURF across all Meta-World tasks. On five of six domains (Hammer, Door-Open, Button-Press, Drawer-Open, Window-Open), ADLoss reaches performance close to SAC trained on oracle rewards — a striking result given the weak binary feedback signal. Results are reported as mean ± std over 5 seeds, and the improvement is both large and consistent.

3. **Ablations isolate the action distance signal**: Figure 3 compares ADLoss against adapted baselines that share some characteristics — forward dynamics prediction (Rdynamics), bisimulation metrics (BISIM), and L2 embedding preservation (L2EmbeddingLoss) — and shows all are "clearly weaker" than action-distance-based training. This demonstrates that the benefit is specific to the action distance signal, not simply any auxiliary prediction task or dynamics awareness.

4. **Theoretical grounding for policy acceleration**: Propositions 4.4–4.5 show that for strong-reversible MDPs with absorbing states, action distance is a pessimistic heuristic, which (via Cheng et al. 2021) provides intuition for why the embedding-preserving auxiliary task accelerates policy learning. While the assumptions do not match the experimental domains exactly, the framing offers principled intuition rather than being a core claim, and the empirical results stand independently.

## Weaknesses

### Fatal
None.

### Major
None. The core empirical contribution is solid, and the identified issues are addressable without undermining the main claims.

### Minor

1. **Action distance is approximated by a single-trajectory step count, not the expectation it is defined as**. The paper defines action distance as an expectation over trajectories (Eqs. 5–6) but trains against the raw step count from a single trajectory (Section 4.4.1: "use the number of action steps taken in the trajectory from s_i to s_j as the ground truth distance d_y = |j−i|"). The paper provides Proposition 4.6 (proved in the stripped Appendix B.1) claiming that with balanced sampling and a perfect function approximator the estimate works, and the MSE loss over many pairs would indeed push the embedding toward the conditional expectation. However, the paper never empirically validates that the learned embedding distances actually correlate with *true* expected action distances (as opposed to the noisy single-trajectory proxy). A simple correlation analysis between embedding distances and ground-truth expected steps (e.g., estimated by Monte Carlo rollouts on a subset of states) would directly support the central claim that the embedding preserves action distances. Currently there is an evidence gap between the mechanism described and the optimization objective actually used.

2. **Theoretical propositions (4.4–4.5) assume strong-reversible MDPs with absorbing states, which do not apply to the Meta-World experimental domains**. The paper acknowledges this implicitly ("we provide intuitions," line 113, and "for strong-reversible MDPs," line 125) and notes that the auxiliary task "does accelerate policy learning as confirmed empirically." This is a reasonable qualification, but the propositions are presented as formal results (Definitions, Propositions, a Proof) in the main paper body, which may mislead readers into thinking the theory directly supports the experimental results. A clearer disclaimer — or moving the theoretical discussion to an appendix — would better align the narrative with the evidence.

3. **Hyperparameter λ_ad sensitivity is only ablated on one task (Button-Press)**. Figure 4 (center) shows performance varies strongly with λ_ad, with λ_ad=10 being best on Button-Press. The paper does not report whether this value transfers to the other five tasks, or whether λ_ad was tuned individually per task for the main results. Since the ablation acknowledges that "tuning this hyperparameter has the most impact on the performance" (Section 5.2), the reader cannot assess whether the headline results reflect a robustly good default or per-task tuning.

4. **Human study is a pilot study lacking statistical rigor**. The study reports only raw feedback count ratios (e.g., 336/593 for window-open) without standard deviations, number of subjects, inter-subject variability, or any statistical test. This provides suggestive evidence consistent with the oracle experiments but does not meet the usual standards for a human evaluation claim. The conclusion "consistently required fewer feedbacks" is not adequately supported.

### Trivial

1. **No analysis of computational cost**. Computing the auxiliary loss requires iterating over all O(L²) state pairs within recent trajectories. For L=50 and k=5 trajectories, this is ~6250 pairs per gradient step. Reporting wall-clock time relative to PEBBLE would help practitioners assess the trade-off.

2. **The metric MDS discussion (Section 3.2) introduces the f(·) generalization but the actual loss (Eq. 7) uses f(x)=x without comment.** A brief remark that the loss is a specific case of mMDS would be cleaner.

## Nice-to-Haves

- An empirical validation (even in the appendix) showing that the learned embedding distances correlate with expected action distances (estimated via Monte Carlo rollouts) would close the action-distance-approximation gap.
- A sensitivity analysis of λ_ad across 2–3 diverse tasks (e.g., one where ADLoss works very well like Hammer, and one where gains are more modest) to demonstrate robustness to hyperparameter choice.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper does not report standard deviations for adapted baselines (Figure 3)"** (Harsh Critic). REMOVED — the paper explicitly states (line 189): "The result plots show the mean (solid line) and standard deviation (shaded region) over five random seeds," which applies to all result plots including Figure 3.
- **"PEBBLE implementation may be under-tuned"** (Harsh Critic). REMOVED — a speculative concern about baseline implementation quality without evidence of misimplementation. The paper uses standard PEBBLE as the backbone algorithm.
- **"No baseline using goal-conditioned heuristics"** (Harsh Critic). REMOVED — the paper clearly distinguishes its approach from goal-conditioned methods (Hartikainen et al. 2019, Venkattaramanujam et al. 2019) and explains why they are not directly comparable (they require explicit goal proposals, which the proposed method does not).
- **"BISIM baseline described in Appendix F.3 which we cannot see"** (Harsh Critic). REMOVED — the parser strips appendix content from all papers; this exists in the original submission.
- **"Missing related works"** — REMOVED per instructions: do not mention missing related works.
- **Various formatting/typo nitpicks** — REMOVED per instructions (parser artifacts, not author errors).
- **Strength Finder's generic strengths about "importance of the problem"** — REMOVED as generic/superficial.
- **Strength Finder's claim about "robustness" from ablation on one task** — WEAKENED: the λ_ad ablation is only on one task, so the robustness claim is not fully supported.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the action-distance-to-embedding mapping is trained on single-trajectory step counts rather than true expectations is the most insightful cross-cutting observation, but it primarily sharpens a limitation the paper partially acknowledges rather than revealing something entirely new.

## Suggestions

1. **Acknowledge the action distance approximation explicitly**: State that the training target is a single-sample estimate of the expected action distance, explain why the MSE loss over many pairs drives the embedding toward the conditional expectation (this is standard regression logic), and provide a correlation analysis between embedding distances and Monte-Carlo-estimated expected steps to validate the mechanism.

2. **Reframe the theoretical section**: Either move Propositions 4.4–4.5 to an appendix with a note that they apply to a restricted MDP class, or add an explicit statement in the main text that the experiments do not satisfy the strong-reversibility assumption, and the theory is provided as intuition-building rather than a formal justification of the empirical results.

3. **Report λ_ad values used across tasks and/or add sensitivity analysis on 2–3 tasks**: Clarify whether the same λ_ad=10 was used for all tasks in the main experiments or whether per-task tuning was performed. If the latter, disclose the tuned values.

4. **Strengthen the human study**: Report the number of participants, provide per-subject feedback counts (or at least standard deviations), and include a basic statistical comparison (e.g., a paired test) to support the claim of reduced feedback requirements.

## Score and Decision

**Summary assessment**: This paper makes a novel, simple, and effective contribution to PbRL. The empirical evidence across six continuous control domains is strong, with consistent large-margin improvements over PEBBLE and SURF, reaching near-oracle SAC performance on most tasks. The adapted baselines convincingly isolate the action distance signal as the source of improvement. The identified weaknesses (the single-trajectory approximation of action distance, the theory–experiment mismatch in MDP assumptions, limited λ_ad sensitivity analysis, and the pilot-level human study) are all addressable and do not undermine the core contribution. This is a solid paper that will be of interest to the PbRL community.

**Score**: 7.5 (Accept)

**Decision**: Accept

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>