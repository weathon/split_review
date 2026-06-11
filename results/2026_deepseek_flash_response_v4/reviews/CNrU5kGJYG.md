## Summary

This paper proposes TrojanTO, the first post-training action-level backdoor attack designed specifically for Trajectory Optimization (TO) models in offline RL. Unlike prior RL backdoor attacks that rely on reward manipulation during training, TrojanTO directly modifies a pretrained TO model's weights with a small set of poisoned trajectories (0.3%), using trajectory filtering, batch poisoning, and alternating training to jointly optimize the trigger and model parameters. The method is evaluated across 6 D4RL environments and 3 TO architectures (DT, GDT, DC), achieving an average CP of 0.701.

## Strengths

- **First post-training backdoor attack targeting TO models, justified by a principled incompatibility argument**: The paper correctly identifies that prior RL backdoor attacks rely on reward manipulation during training, which is fundamentally incompatible with TO models because they minimize reconstruction loss rather than maximizing reward (Section 1, line 17). TrojanTO decouples the attack from training, making it feasible against large-scale TO models where retraining is prohibitive.

- **Systematic empirical decomposition reveals reward manipulation is ineffective while trigger design is critical**: Section 4 (Tables 1–3, Figure 1) separately investigates target action selection, trigger design, and reward manipulation. Figure 1 convincingly shows reward manipulation has negligible effect across DT, DC, and GDT models, while target action type changes ASR from 0.110 to 1.000 (Table 1) and trigger dimension choice changes ASR from 0.000 to 0.915 (Table 2). This challenges the dominant paradigm in RL backdoor literature that treats reward manipulation as the primary attack vector.

- **Reliable effectiveness across tasks and architectures with clean component ablation**: Table 4 shows TrojanTO achieves competitive CP (0.701 avg) across 6 environments and 3 TO model types, while baselines have catastrophic failures (e.g., IMC CP=0.013 on DT/Hopp, Baffle CP=0.000 on DT/Walk — Section 6.1). The ablation study (Table 5) cleanly isolates each component's contribution: AT is critical for ASR (dropping from 0.719 to 0.507 when removed), TF/BP for BTP (dropping from 0.914 to 0.850/0.836).

- **Persistent backdoor capability with bounded degradation**: Section 6.3 demonstrates that TrojanTO sustains target-action output for k=5,10,15 consecutive steps after trigger activation, maintaining CP values of 0.876–0.973 across environments. The finding that persistence is bounded by the model's context window (line 307) provides a concrete architectural insight about TO models.

## Weaknesses

### Major

- **Headline comparison to Baffle is misleading due to fundamentally different threat models**: The paper claims a "105.0% improvement" over Baffle (line 268) and repeatedly contrasts 0.3% vs 10% poisoning rates (abstract, Section 6.1). However, the paper itself categorizes Baffle as a *pre-training* data-poisoning attack that must survive from-scratch training (line 62), while TrojanTO is a *post-training* attack with direct weight modification. These are fundamentally different paradigms with different constraints. The 105% figure is an artifact of comparing a stronger attack paradigm against a weaker one, not a meaningful measure of TrojanTO's quality. The IMC comparison (another post-training method) is the appropriate baseline, where TrojanTO shows more modest but genuine gains (0.701 vs 0.551 CP). The abstract and Section 6.1 should recalibrate these claims — the paper does not need to remove the Baffle comparison entirely, but it should be framed as illustrating the limitations of pre-training attacks for the TO setting, not as a competitive superiority claim at different poisoning rates.

- **Data-access ambiguity in the threat model**: Section 3.3 states the adversary acts "without access to the original training dataset" (line 60), yet TrojanTO's trajectory filtering (Section 5.1) operates on trajectories from the dataset, and the 0.3% poisoning figure refers to trajectories drawn from this dataset. The paper never clarifies whether the adversary (a) collects new rollouts using the clean policy, (b) has access to a different but related dataset, or (c) actually has limited access to the original data (contradicting the threat model statement). This matters because it affects the realistic severity of the attack — collecting trajectories from a proprietary dataset may be infeasible in a supply-chain scenario.

### Minor

- **Main results (Table 4) report only point estimates without variance**: While Tables 6 and 7 include standard deviations, Table 4 — the central results table showing all environments, models, and baselines — reports only means over 3 seeds × 3 target actions. Without variance, the reader cannot assess whether TrojanTO's advantages on individual tasks (or the cases where baselines outperform, e.g., IMC CP=0.752 vs TrojanTO CP=0.559 on DC/Ant) are systematic or due to noise. Many standard deviations in Tables 6 and 7 are exactly 0.000, raising questions about rounding precision.

- **Defense evaluation in Section 6.5 is too thin**: The main text lists five defense methods and states only fine-tuning works, but provides no quantitative results or summary table. The paper says details are in Appendix B.1 (line 326), but the main text's claim that "the other tested methods proved largely ineffective" is unsupported on the page. A brief summary table with ASR/BTP/CP after each defense would strengthen the presentation.

- **Hyperparameter λ is not specified**: Equation (7) uses λ to balance backdoor and clean losses, with λ ∈ [0,1] mentioned in Equation (1), but the actual value used in experiments is never stated.

- **Source of the 0.3% poisoning rate is underspecified**: The paper says "0.3% of trajectories" but does not clarify whether this refers to the proportion of the original dataset, the filtered set F_τ, or something else.

### Trivial

None.

## Nice-to-Haves

- Report per-target-action-type results in the main paper (rather than averaged over three types), since Section 4.1 shows target action choice significantly affects ASR.
- Include pairwise ablation (e.g., w/o TF and w/o BP together) to test interaction effects between components.
- State the computational cost (GPU-minutes/hours) of the post-training attack to support the practicality claim.
- Test robustness to other perturbation types (e.g., adversarial noise, sensor noise models).

## Removed Points

These points from the input reviews were identified as questionable or noise and are provided for awareness:

- **Harsh Critic: "first systematic study" scope precision** — The paper's claim is reasonable given its focus on TO models and post-training attacks; the critic's suggestion to re-scope is a wording preference, not a substantive flaw.
- **Harsh Critic: trigger dimension physical interpretation** — State dimensions in D4RL are abstract and typically without semantic labels; asking what dimensions (1,2,3) "represent" is not standard for this setting.
- **Harsh Critic: pairwise ablation** — Moved to Nice-to-Haves as an enhancement, not a flaw.
- **Harsh Critic: other perturbation types (adversarial noise)** — Scope creep beyond the paper's stated evaluation scope.
- **Strength Finder: "105% improvement over Baffle" framing** — The 105% figure depends on the unfair comparison discussed above; the underlying empirical result is retained in Strengths but the inflated framing is removed.

## Novel Insights

The most interesting finding from this paper is that reward manipulation — the dominant paradigm in the RL backdoor literature — is nearly irrelevant for TO models, while trigger design (dimensions and values) is what drives attack success. This is a concrete finding grounded in the architectural difference between TO models (which minimize reconstruction loss) and traditional RL agents (which maximize reward). The persistent backdoor finding (bounded by context window length) provides a crisp architectural insight: attack persistence is fundamentally limited by the model's finite context window, not by the attack design. This suggests that as TO models adopt longer context windows, the persistence threat window grows correspondingly.

## Suggestions

1. **Reframe the Baffle comparison**: Present it as illustrating the limitations of pre-training attacks for the TO setting rather than as a head-to-head superiority claim. Let the IMC comparison carry the main quantitative argument of TrojanTO's advantage within the post-training paradigm.

2. **Resolve the data-access contradiction**: Explicitly state whether the adversary needs access to original training data, collects new rollouts using the clean policy, or has partial access. This is critical for assessing the attack's realistic threat level.

3. **Add variance to Table 4**: Include standard deviations (or at least min-max ranges) for the main results table so the reader can distinguish signal from noise.

4. **Include a defense summary table in the main text**: Even a brief one with ASR/BTP/CP after each defense method would substantiate the claim that only fine-tuning is effective.

5. **Specify λ and clarify the 0.3% computation**: State the actual λ value used and whether 0.3% refers to the original dataset or the filtered set.

---

## Calibration Anchors

All anchors retrieved across all calibration rounds:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| em0gAL8fbK (Multi-Vehicle Backdoor) | 4.00 | R1 | TrojanTO is stronger — more environments, lower poisoning rate, better ablation |
| P895PSh41Z (RAORL) | 4.50 | R1 | Offline RL robustness; different topic |
| X2x2DuGIbx (Certified Defense) | 6.75 | R1/R2 | TrojanTO is weaker — lacks theoretical guarantees |
| 5hAMmCU0bK (Robust Offline RL) | 7.00 | R1/R2 | TrojanTO is weaker — purely empirical with no theory |
| AKAlVyunxA (SHINE) | 5.75 | R1/R2 | Comparable — SHINE has theory, TrojanTO has broader empirical eval for its domain |
| rp5vfyp5Np (BATTLE) | 4.25 | R1 | TrojanTO is stronger — more comprehensive evaluation |
| UhW2wA1pRV (Robust DRL Behavior) | 5.50 | R2 | Comparable — both have solid empirical eval but notable gaps |
| HZnnHDrBXD (Tree-based Attack) | 5.75 | R2 | TrojanTO has stronger empirical eval; Tree-based has theory |
| vRyp2dhEQp (Efficient Backdoor) | 5.75 | R2 | Comparable — both have solid contributions but methodological concerns |
| S1Bv3068Xt (BALD) | 6.25 | R2 | TrojanTO is weaker — BALD has broader scope, multiple attack types, real LLM eval |
| 46xYl55hdc (Single-agent Poisoning) | 7.00 | R2 | TrojanTO is weaker — theoretical contribution |
| F5dhGCdyYh (Illusory Attacks) | 7.33 | R2 | TrojanTO is weaker |
| QyVLJ7EnAC (Model-Free Robust Offline RL) | 6.40 | R2 | TrojanTO is weaker |
| 5e0yWSNGIc (Certified Training RL) | 5.33 | R2 | Comparable |
| ZtOnddFVT3 (Self-Alignment Offline Safe RL) | 4.67 | R2 | TrojanTO is stronger |

**Bracket (Round 1):** 4.0–6.5  
**Narrowing (Round 2):** The paper is clearly stronger than the 4.00 anchor but comparable to the 5.75 anchors (SHINE, Efficient Backdoor, Action-Manipulation). The misleading Baffle comparison and data-access ambiguity prevent it from reaching the 5.75-6.25 range of the strongest comparable papers. **Final score: 5.0.**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>