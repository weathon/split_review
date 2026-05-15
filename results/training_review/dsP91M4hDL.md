Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes TC-MoE, which expands the MoE expert space by multiplying each original expert with the ternary set {-1, 0, 1}, creating E¹ (original), E⁰ (zero output, no compute), and E⁻¹ (negated output) variants without adding expert parameters. The authors introduce a custom load balancing loss tailored to the expanded space and a reward loss that gives E⁰ experts a synthetic gradient to enable a flexible efficiency-effectiveness trade-off. Experiments at the 100M-to-400M-parameter scale show consistent improvements of ~1% over Top-K baselines while reducing activated expert count by up to 9%.

## Strengths

- **Novel, parameter-free expert-space expansion**: The core idea is clean and well-motivated. Multiplying each expert by {-1, 0, 1} creates three expert variants without adding FLOPs to the expert FFNs themselves. The only extra cost is a modest increase in router parameters — a genuinely different direction from prior work that modifies routing schemes rather than the expert space.

- **Consistent empirical gains across multiple settings**: TC-MoE shows improvement across all tested configurations (tiny, base, fine-grained base; RedPajama and FineWeb datasets), with average accuracy gains of 0.83%–1.18% over Top-K. Efficiency gains are also consistent (9% fewer activated experts, 6.5% FLOPs reduction on RedPajama base). The gains hold under varying activation budgets (Figure 3), outperforming Random drop and Top-P baselines.

- **Well-motivated load balancing loss**: The redesigned auxiliary loss correctly accounts for the unique properties of the expanded space — excluding cost-free E⁰ experts from balancing, and balancing Eⁱ¹ and Eⁱ⁻¹ together since they share parameters and reside on the same device under expert parallelism. Figure 7 demonstrates near-perfect per-expert workload equalization on training data.

- **Ablation validates each ternary component**: Table 3 shows that {-1, 1} improves accuracy by 0.29%, {0, 1} improves accuracy by 0.52% while reducing K by 0.19, and the full set achieves the best combined result. This cleanly isolates the contribution of each expert type.

## Weaknesses

### Fatal
None.

### Major

- **Missing Expert Choice Routing baseline (Zhou et al., 2022)**: Expert Choice is the most prominent dynamic routing method that also allows flexible token-to-expert assignment. The paper cites it as prior work in Section 2 and claims its approach is "unlike previous studies... that focus on modifying the routing scheme." Yet Expert Choice is never evaluated as a baseline. The paper's dynamic routing comparisons (Figure 3) include only two baselines (Top-P and Random drop), neither of which is the strongest representative of this family. This gap weakens the claim that TC-MoE "consistently achieves superior performance under different activation budgets" (line 213) against dynamic routing methods.

- **No statistical significance or variance reporting**: All results come from single runs with no standard deviations, confidence intervals, or seed sweeps. The reported improvements (0.83%–1.18%) are modest, and it is impossible to determine whether these are genuine gains or within noise. This is particularly concerning because training large MoE models from scratch involves stochasticity from data ordering, initialization, and the router learning dynamics. The paper would be substantially strengthened by reporting statistics across at least 3 seeds, even if only for the main comparison (Table 1).

- **Reward loss mechanism is empirically unvalidated**: The reward loss (α₂) is presented as the mechanism for a "flexible trade-off between efficiency and effectiveness" (Section 3.4). However, the paper never shows a sensitivity study varying α₂, never reports what α₂ value was used in the main experiments, and does not explain how the "different activation budgets" in Figure 3 are achieved for TC-MoE (whether by varying α₂ or by some other mechanism). Without this, the central claimed capability — controllable efficiency-effectiveness trade-off — is asserted but not demonstrated. The ablation in Table 3 does not vary α₂ either.

### Minor

- **The "40%" flipped-sign claim is not quantified in TC-MoE results**: The introduction states that "approximately 40% of the experts with low gate values have positive contributions when their output signs are flipped" (line 26), motivating the E⁻¹ design. However, the paper never measures how often TC-MoE actually uses E⁻¹ versus E¹, nor what fraction of E⁻¹ activations are beneficial. Figures 4–5 show distributional shifts visually but provide no quantitative metric (e.g., "% of activations with negative contribution before/after"). The numerical evidence for the claimed mechanism is absent.

- **FLOPs reduction numbers overstate savings**: The paper reports "6.5% FLOPs reduction" but this appears to count only expert FFN computation. The router FLOPs increase from N×d to (2N+K)×d is acknowledged qualitatively ("this cost is negligible") but never quantified or factored into the reported FLOPs numbers. For N=8, K=2, this is a 125% increase in router FLOPs (from 8d to 18d). While likely small relative to expert compute, this should be accounted for or explicitly bounded.

- **Evaluation protocol underspecified**: The paper does not state whether the 9 benchmark evaluations are zero-shot or few-shot, nor the prompting protocol used. This makes direct reproduction difficult.

- **Router capacity confound in ablation**: The ablation (Table 3) varies the number of router outputs across conditions ({1}: 8 experts; {-1,1}: 16 experts; {0,1}: 10 experts; full set: 18 experts). Improved performance could partly come from increased router capacity rather than the ternary structure itself. A control condition with 18 outputs but only E¹ experts would isolate this.

- **Out-of-distribution load balance degradation**: Figure 7 shows near-perfect training distribution balance (~11.5% per expert pair) but notable degradation on ARC-Easy (range 8.5%–15.0%). The paper treats this as minor, but it indicates the load balancing loss does not fully generalize, which matters for deployment.

### Trivial
- The y-axis labels and scales for Figures 4 and 5 are not visible in the text, making the distributional plots harder to interpret.

## Nice-to-Haves

- A sensitivity plot of accuracy vs. average K as α₂ varies, directly showing the claimed trade-off curve.
- Quantify the frequency of E⁻¹ and E⁰ activations during inference (e.g., "X% of tokens activate at least one E⁻¹").
- Report results at larger scales (1B+ parameters) to test whether the ~1% improvement persists.
- For the zero-expert count, ablate K=1 vs. K=2 to justify the design choice.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The number of zero experts is set to K without justification"** — The paper **does** justify this choice (line 99: "as this is sufficient for the Top-K router to activate any number from 0 to K"). The reviewer's concern about whether fewer could suffice is a reasonable ablation question but the claim of "no justification" is inaccurate.
- **"Derivation concerns about gradient interference"** — The reviewer notes that adding a negative gradient to g_{E⁰} might indirectly affect other expert logits. This is a standard property of auxiliary losses in MoE (load balancing losses work the same way). Not a meaningful weakness.
- **Formatting/style nitpicks about figure aesthetics** — Removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper claims a fundamentally new paradigm (expert-space expansion rather than routing-scheme modification), but evaluating against routing-scheme baselines (Expert Choice, Top-P) is still necessary to establish practical value. The lack of α₂ ablation also highlights a recurring pattern in MoE papers — proposing auxiliary losses for efficiency trade-offs without characterizing the Pareto frontier they claim to enable. The router capacity confound in the ablation is a subtle but instructive methodological point: when expanding the expert set, one must control for the fact that a larger router weight matrix itself provides more representational capacity independent of the expert content.

## Suggestions

1. **Include Expert Choice Routing as a baseline.** This is the single most important addition to validate the claim of superiority over dynamic routing methods.
2. **Add variance estimates** — even 3 seeds for the main comparison (Table 1) would substantially increase confidence in the results.
3. **Show a sensitivity curve of accuracy vs. average K for varying α₂**, and compare this against the threshold-tuning curves of Top-P and Random drop. This is the minimal experiment to validate the reward loss.
4. **Add a router-capacity control** to the ablation (e.g., 18 E¹-only experts) to disentangle the effect of ternary content from larger router size.
5. **Report quantitative summary statistics** for Figures 4–5 (e.g., percentage of activations with negative contribution).

## Score and Decision

The core idea is clean, well-motivated, and likely useful. The paper provides initial evidence of consistent improvements. However, the absence of the most relevant dynamic routing baseline, the lack of any variance reporting, and the unvalidated reward loss mechanism leave the experimental support incomplete. These are fixable issues but as presented, the evidence does not fully substantiate the claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>