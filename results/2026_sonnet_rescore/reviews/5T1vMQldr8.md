## Summary

SPOT (Subgoal-based Preference Optimization Through Attention Weight) is an offline preference-based RL method that augments the Preference Transformer (PT) reward model with a CVAE-generated subgoal shaping signal. High-attention states from preferred trajectories are filtered using a dual-criteria mechanism (attention weight + reward threshold), forming a subgoal set; a CVAE learns to generate contextually appropriate subgoals conditioned on the current state-action; and a cosine-similarity reward bonus toward the predicted subgoal is added to the PT reward during offline RL training. The method claims to mitigate reward model extrapolation error by "constraining policy learning within the training distribution."

---

## Strengths

- **Highest average performance across 10 diverse tasks (78.82) with reduced variance**: Table 1 confirms that SPOT achieves the top average score (78.82 vs. 77.25 Oracle, 74.76 PT, 73.61 MR) while simultaneously reducing average standard deviation from 13.80 (PT) to 7.76 — both improvements are concrete and cross-benchmark.
- **Top-K% ablation validates attention-based subgoal filtering (Table 2)**: On hopper-medium-expert, using top-10% attention subgoals yields 99.37 vs. 55.24 for the bottom-10% group, with substantially lower variance. This hierarchy directly supports the dual-criteria filtering design choice.
- **Cosine-similarity shaping outperforms alternative shaping methods for positive weights (Table 3)**: On hopper-m, cosine similarity at λ=1.0 achieves 97.36 ± 10.26, outperforming potential-based (77.95) and negative distance (86.03), providing a concrete empirical justification for the shaping design.
- **Demonstrated query efficiency improvement over PT (Table 4)**: On hopper-medium-expert with only 30 queries, SPOT scores 85.09 ± 8.54 vs. PT's 68.06 ± 4.92, a +17-point gap under data-scarce conditions, which is practically useful.

---

## Weaknesses

### Fatal
None.

### Major

- **Theoretical framing overstates and mischaracterizes the mechanism.** The abstract, Section 4 intro, and Section 4.2.1 repeatedly claim SPOT "constrains learning within the training distribution" and that "the CVAE framework ensures that generated subgoals remain within the training distribution" via the KL divergence term. However, the mechanism is reward shaping — a cosine-similarity bonus toward a CVAE-predicted subgoal (Eq. 13). This does not constrain which states the policy visits; it provides a soft incentive. More importantly, Section 4.1.3 states: "This is achieved via the KL divergence term in the objective function, which regularizes the latent space to prevent the decoder from generating out-of-distribution subgoals." This KL regularization operates during *training* of the CVAE. At *inference time*, the CVAE is conditioned on OOD state-action pairs from the batch dataset, for which no distributional guarantee exists. The paper does not address why the CVAE generalizes reliably to these OOD inputs. This framing issue is not merely semantic — it drives the main interpretive claim of the paper and is unsupported as written.

- **Missing key ablation: attention-guided vs. random subgoals.** The paper compares PT, different reward shaping methods (Table 3), and different attention percentiles (Table 2), but there is no ablation comparing SPOT against "PT + cosine-similarity reward shaping using random (non-attention-selected) subgoals." Without this control, it is not possible to determine whether the empirical gains arise from the preference-aligned, attention-guided subgoal identification mechanism — which is the paper's core novel claim — or from any reward shaping on top of PT. Cosine similarity on raw state vectors is geometrically crude, and a random subgoal would still produce a positive shaping signal in many cases. This missing control significantly weakens the attribution of improvement to the proposed mechanism.

- **Extrapolation error analysis is partially confounded (Figure 2b).** The paper measures extrapolation error as a function of cosine similarity between the current state and the predicted subgoal (lines 249–277). However, this is precisely the quantity that SPOT's reward shaping optimizes (Eq. 11–13). SPOT's policy is therefore biased toward visiting states with high cosine similarity to predicted subgoals, meaning the comparison in Figure 2b partly reflects a sampling difference: PT's policy visits the full OOD region, while SPOT's policy is steered toward the high-similarity subregion that already has lower baseline error. The paper presents Figure 2b as demonstrating that "SPOT consistently outperforms the Preference Transformer (PT) baseline, showing substantially lower extrapolation errors across all distance ranges," but this result is consistent with the alternative explanation that reward shaping concentrates the policy in the favorable region rather than genuinely improving reward model quality across all OOD states. A cleaner design — e.g., evaluating reward model prediction error on a fixed held-out OOD set independent of the x-axis metric — would be needed to support the causal claim.

### Minor

- **Task-level performance is inconsistent, and "consistent superiority" is overstated.** From Table 1: `lift-mh` (SPOT 65.17 vs. MR 95.62, Oracle 81.62 — SPOT is below even Oracle and is worse than its own backbone PT at 68.46); `drawer-open` (SPOT 66.80 vs. MR 86.6 and IPL 87.64); `hop-m-r` (SPOT 85.08 vs. DTR 94.18). On `lift-mh`, SPOT is outperformed by 5 of 7 baselines. The paper attributes this to task difficulty, but no mechanism-based explanation is provided. The highest average score is legitimate, but the claim "consistent efficacy across different levels of demonstration quality" (Section 5.1) does not align with the manipulation task results.

- **Query efficiency analysis is narrowly scoped.** Table 4 compares SPOT only against PT, across only 2 environments. IPL and other reward-free approaches like CPL are natural comparisons for low-query regimes since they avoid reward model training entirely; the relevant question is whether SPOT's CVAE shaping outperforms methods that sidestep the query bottleneck altogether.

### Trivial

- **Table 3 bolding is ambiguous**: The bold formatting in Table 3 highlights the "cosine similarity" method row, but at λ=−1.0 for walker2d, cosine similarity scores 0.69±1.60 (near zero), which is clearly not a strong result, yet is bold. The convention for Table 3 differs from Table 1 and is not explained in the caption.

---

## Nice-to-Haves

- A controlled ablation using randomly selected subgoals (instead of attention-guided ones) with the same cosine similarity shaping would cleanly establish whether the attention mechanism specifically drives the gain, vs. any shaping signal.
- Restructuring the extrapolation error experiment using a fixed held-out OOD transition set — with measurement of reward prediction error independent of the cosine-similarity axis — would substantially strengthen the mechanistic claim.
- Extension of the query efficiency comparison to reward-model-free baselines (e.g., IPL) would better contextualize the practical benefit.
- Ablating the dual-criteria filter (attention-only, reward-only, and combined) would strengthen Section 5.2.1's interpretation.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Harsh Critic: "IPL/CPL overlook rich information" is inaccurate** — this is factually correct as a minor framing criticism but is too peripheral to change the evaluation; removed as a standalone point.
- **Harsh Critic: SPOT loses on `can-ph` to Oracle (73.25 vs. 63.82)** — comparing to Oracle is not a fair criticism since Oracle uses ground-truth rewards and is expected to outperform all learned-reward methods; removed per the rule against inflating weaknesses with asymmetric baseline comparisons.
- **Strength Finder: "Forward-looking subgoals" from qualitative Figure 3** — a single 2-panel qualitative example in a simple locomotion task provides weak evidence; it is illustrative but does not constitute a genuine strength. Removed.
- **Harsh Critic: Motivation of dual-criteria filtering is underdeveloped** — the paper provides the motivation ("high-attention states in marginally preferred trajectories may correspond to relatively bad states") and supports it empirically in Table 2; the framing is reasonable enough; removed.

---

## Novel Insights

The paper's most genuinely novel element is the combination of dual-criteria filtering (attention weight + reward threshold) over PT's attention mechanism to extract preference-aligned subgoals, followed by CVAE-based generative modeling to produce context-conditioned subgoals for unlabeled transitions. The empirical finding that top-10% attention subgoals yield nearly twice the performance of bottom-10% subgoals (Table 2) is a concrete validation that PT's attention weights carry meaningful subgoal information beyond what is typically exploited. The finding that cosine-similarity shaping robustly outperforms potential-based and Euclidean-distance shaping for this task setting (Table 3) also contributes a practical design insight to the reward shaping literature for offline PbRL. These are incremental but concrete additions.

---

## Suggestions

1. **Add a random-subgoal control condition**: Run PT + cosine-similarity shaping with randomly selected states as subgoals (not from the attention mechanism) to isolate the attention-based subgoal identification as the source of improvement.
2. **Redesign the extrapolation error experiment**: Use a fixed held-out OOD transition set not visited by either policy; measure absolute reward prediction error on this set for both PT and SPOT; use task step index or state-space distance from the training distribution (not cosine-to-subgoal) as the x-axis.
3. **Soften the theoretical framing**: Replace "constrains learning within the training distribution" with more accurate language such as "provides auxiliary reward guidance toward preference-aligned regions of the state space," which is what the mechanism actually does and avoids the unsupported distributional constraint claim.
4. **Ablate dual-criteria components**: Add rows for attention-only filtering and reward-only filtering in Table 2 to determine whether both criteria are jointly necessary.
5. **Extend query efficiency to include reward-free baselines**: Compare SPOT at low query counts against IPL (which doesn't use a reward model) to establish the practical scope of the query efficiency advantage.

---

## Score and Decision

**Originality**: The combination of attention-based subgoal extraction + CVAE + cosine reward shaping for offline PbRL is novel as a system, though each component is individually known. Incremental but well-motivated. (3/5)

**Importance**: Extrapolation error in offline PbRL is a real and practically significant problem. The multi-benchmark evaluation covers relevant settings. (4/5)

**Claims supported**: The average-performance claim is supported; the "consistent superiority" and "constrains learning within the training distribution" claims are not. The extrapolation error analysis is confounded. Key ablation is absent. (2/5)

**Soundness**: The experimental setup is reasonable; results are reproducible over 5 seeds; ablations exist but miss the most critical control. Theoretical justifications are imprecise/overstated. (3/5)

**Clarity**: The methodology section is clearly written and the architecture diagram is helpful; however, the mechanism description ("constrains learning") is misleading relative to what the equations actually implement. (3/5)

**Community value**: Highest average on a broad benchmark suite, reduced variance, improved query efficiency — these are meaningful contributions. Missing ablations limit how much can be safely adopted from this work. (3/5)

The paper demonstrates real empirical gains and proposes a concrete, novel mechanism for offline PbRL. However, the theoretical framing substantially overclaims, the primary diagnostic experiment (Figure 2b) is confounded with the optimization objective, and the most important ablation (random vs. attention subgoals) is missing. These issues collectively prevent confident attribution of the improvement to the claimed mechanism, which is the scientific core of the contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>