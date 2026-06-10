## Summary

This paper addresses the "alignment tax" on small language models by proposing two methods—DCKD (Dual-Constrained Knowledge Distillation) and ADPA (Advantage-Guided Distillation for Preference Alignment)—that transfer preference alignment knowledge from larger, DPO-aligned teacher models to smaller student models. DCKD extends standard KD with an additional KL-divergence constraint on dispreferred responses, while ADPA uses the per-token log-probability ratio between a DPO teacher and a reference teacher as a distribution-level reward signal to guide student model training. Experiments on three student model sizes (500M–7B) compare against several baselines.

## Strengths

- **The core idea of using the DPO implicit reward ratio as a token-level distillation signal is simple and well-motivated.** Rather than applying DPO directly (which hurts small models) or relying on sparse sequence-level rewards, ADPA provides dense, token-level preference guidance from the teacher. This is a sensible approach to a genuine problem.

- **The ablation study (Table 2) cleanly isolates the contribution of each design choice.** Removing the DPO teacher from DCKD or the reference teacher from ADPA causes measurable performance drops (e.g., Danube3-0.5B MT-Bench 2.67 → 2.36, AlpacaEval WR 50.0% → 31.6% without the reference teacher), convincingly showing that both teacher models in ADPA are essential.

- **DCKD's dual KL constraint on both preferred and dispreferred responses is a concrete, non-trivial extension of standard KD** that the ablation confirms is beneficial. The hyperparameter analysis (α/γ sweep in Figure 5) shows the methods are reasonably robust to their scaling parameters, with clear over-optimization regimes identified (γ > 3).

- **The ADPA+ combination (DCKD initialization followed by ADPA) demonstrates synergistic improvement** over either method individually, suggesting the two approaches capture complementary aspects of preference knowledge.

## Weaknesses

### Major

- **The AlpacaEval evaluation replaces the standard GPT-4 reference with ADPA-trained student models, rendering the headline win rates uninterpretable as absolute quality measures.** The paper's claim that "existing distillation and preference alignment methods achieve a win rate below 50%, validating the strength of preference-based distillation" (Section 4.2) is essentially tautological: by construction, ADPA achieves 50% against itself, and any worse method scores below 50%. This setup communicates only relative ordering, not absolute quality. The MT-Bench results (which use standard GPT-4 evaluation) are valid, but the AlpacaEval results as presented cannot be compared against the published literature. Standard AlpacaEval against GPT-4 should be reported alongside these relative comparisons, even if the absolute numbers are low, so that readers have an interpretable anchor.

- **The sample complexity analysis in Section 4.4 is misleading and conflates pre-computed signals with learned ones.** The analysis claims ADPA achieves O(1) sample complexity for identifying the optimal action at a given state, compared to O(|A|) for token-level reward and O(|A|^(T−t)) for sequence-level reward. But ADPA's advantage function is derived directly from frozen teacher log-probability ratios — no exploration is needed because the signal is pre-computed. The token-level and sequence-level methods (PPO-based) must *learn* a reward model and then explore. If a perfect token-level reward were provided as an oracle, it would also have O(1) "sample complexity." Moreover, the claim that sequence-level PPO requires enumerating |A|^(T−t) trajectories is a strawman — PPO samples trajectories, it does not exhaustively enumerate them. This section should be either removed or replaced with an honest efficiency comparison (e.g., wall-clock time, number of forward passes, convergence epochs).

- **Baselines DPKD and PLAD are materially modified without justification or ablation.** The paper states: "for DPKD and PLAD, we use actual preference data as positive and negative samples, rather than pseudo pairs, to ensure fairness" (Section 4.2). Both methods' core design is to use the teacher's output as preferred and the student's own output as dispreferred — this on-policy contrastive signal is central to their mechanism. Replacing this with static ground-truth preference pairs changes the method in an unknown direction. Without a comparison between the modified and original versions, the results for these baselines cannot be taken as faithful representations of the published methods. The paper should report results for the original implementations and, if the modification is necessary for fairness, justify why it is neutral.

### Minor

- **No error bars, standard deviations, or multiple-seed results are reported anywhere.** Every MT-Bench and AlpacaEval number appears to come from a single run. Given the models are small enough (500M–7B) that multiple training runs are feasible, the reader cannot assess whether the reported advantages (e.g., "10.8% improvement over DPO") are reliable or within noise. This is standard practice at top venues and should be addressed.

- **The MDP / advantage-function formalism in Section 3.3 is decorative, not operational.** The Q-function in Eq. (101) accumulates a sum of per-token log-ratios, but the advantage function in Eq. (109) discards this cumulative component and uses only the per-token term β log(π_dpo/π_ref). There is no Bellman equation, no learned value function, and no bootstrapping — none of the machinery that the RL/MDP framing suggests. The method is better described as per-token distillation of the DPO implicit reward ratio, which is a reasonable idea that does not require the MDP apparatus. The formalism could be simplified without loss of clarity.

- **The ADPA+ variant receives more total training than either DCKD or ADPA alone** (DCKD initialization + ADPA training). No control experiment trains ADPA for the same total number of steps without DCKD initialization, making it unclear whether the improvement comes from the initialization or simply from additional training time.

### Trivial

- Figure 1 reports MT-Bench improvement deltas (e.g., "+0.76 for Danube2-1.8B ADPA") but does not state the starting and ending raw scores, making the claim difficult to cross-reference with the main results table.

- The paper switches between "PLaD" and "PLAD" inconsistently across the text.

## Nice-to-Haves

- Report standard AlpacaEval win rates against GPT-4 alongside the ADPA-relative ones. This would require only an additional evaluation pass and would make the results interpretable against the existing literature.
- Compare ADPA against an equally simple baseline: standard KD from the DPO teacher onto preferred responses only, plus separate KD from the reference model onto dispreferred responses only. This would isolate whether the advantage function's contrastive signal is genuinely better than independent distillations.
- Run key experiments with 3 random seeds and report means/standard deviations.

## Removed Points

These points were flagged in the reviews but removed for the following reasons:

- *"Three-orders-of-magnitude drop in learning rate (2e-5 vs 5e-7)"* — Factually overstated: 2e-5/5e-7 = 40, approximately 1.6 orders of magnitude. Different training phases commonly use different learning rates. Removed.
- *"Best α/γ values not stated"* — The paper discusses optimal values in Section 4.4 (α=0.2, γ=1.5). The critic missed this. Removed.
- *"Results not broken down by preference dataset"* — The paper states "Table 4.1 presents the comparative results across both preference datasets." Removed.
- *"LLaMA-2-7B results receive almost no discussion"* — The results are present in the table; papers commonly focus discussion on the most interesting/novel model sizes. Removed.
- *Strength Finder strength about sample complexity* — Directly conflicts with a verified weakness about the analysis being misleading. Removed.
- *Missing related works / reproducibility concerns about cited entities* — Per instructions, these are removed.
- *Formatting/style nitpicks* — These are parser artifacts, not author errors. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the AlpacaEval evaluation**: Report standard AlpacaEval win rates against GPT-4 for at least one model pair, even if the numbers are low. This gives readers an absolute anchor. The relative (ADPA-as-reference) comparison can be retained as a secondary metric, but the paper should not frame it as "validating" the method's strength.

2. **Remove or rewrite the sample complexity analysis**: Either delete Section 4.4's complexity claims entirely, or reframe them as a discussion of the practical efficiency advantage of using pre-computed teacher signals versus online RL — with operational metrics (wall-clock time, GPU hours, convergence steps) rather than asymptotic complexity claims that compare apples to oranges.

3. **Address the baseline modification**: Report the original DPKD/PLAD implementations alongside the modified versions, or justify with an ablation showing the modification is neutral. Alternatively, include additional unmodified baselines.

4. **Report variance**: Run 3 seeds for at least the main comparison on one model pair and report means ± std.

5. **Simplify the MDP formalism**: Acknowledge that the "advantage function" reduces to the per-token DPO log-ratio and that no RL bootstrapping is used. The core method is strong enough to stand without the decorative RL framing.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>