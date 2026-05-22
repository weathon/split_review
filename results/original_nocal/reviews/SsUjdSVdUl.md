Now I have thoroughly verified the paper content against all reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper proposes Critique-RL, a two-stage reinforcement learning approach for training critiquing language models without relying on stronger supervisors. The key insight is that indirect reward signals from actor refinement alone (used by prior work) fail to optimize critics' discriminability — the ability to judge whether a response is correct. Stage I optimizes discriminability via a direct rule-based reward comparing the critic's judgment against an oracle answer verifier; Stage II optimizes helpfulness (refinement quality) while preserving discriminability via a KL regularization term to the Stage-I policy. Experiments on math reasoning tasks (MATH, GSM8K, AQuA; OOD on SVAMP, TheoremQA) with Qwen2.5-3B/7B show consistent gains over SFT, STaR, Retroformer, and CTRL baselines, with ablations confirming both stages contribute.

## Strengths

1. **Clear problem diagnosis and principled decomposition.** The paper systematically identifies, via carefully visualized training dynamics (Figure 3), that indirect rewards alone produce either conservative or aggressive critics whose discriminability stagnates or collapses. This is a concrete, verifiable failure analysis. The two-stage solution directly addresses this: Stage I isolates and optimizes discriminability; Stage II optimizes helpfulness while anchoring to the discriminable policy. The ablation study (Table 3) cleanly confirms that removing either stage degrades performance, providing strong internal validity for the decomposition.

2. **Consistent and substantial empirical gains.** On Qwen2.5-7B, Critique-RL achieves 58.40% on MATH vs. 53.86% (CTRL) and 52.34% (Retroformer); similar margins hold across GSM8K, AQuA, and both model sizes (Table 1). The discriminability (Acc@Dis) improvements are particularly large — e.g., 85.20% vs. 71.42% on MATH for 7B — confirming the Stage I objective is working as intended. The gains are also demonstrated under oracle-verifier isolation (Figure 5), separating the contribution of discriminability from helpfulness.

3. **Strong out-of-domain generalization.** Models trained on MATH+GSM8K+AQuA transfer to unseen tasks (SVAMP, TheoremQA) with clear gains over all baselines (Table 4). For Qwen2.5-7B on SVAMP, Critique-RL achieves 89.7% vs. 85.1% (CTRL) and 84.0% (Retroformer), showing that the learned critiquing ability is not dataset-specific.

4. **Iterative improvement and stability.** Table 2 shows that a second iteration of two-stage training yields further monotonic gains (MATH Acc@Refine: 48.6 → 51.0; Acc@Dis: 82.8 → 86.5), suggesting the method does not saturate quickly and is stable under repeated application.

## Weaknesses

### Fatal

None.

### Major

1. **Baselines use different RL algorithms, confounding the comparison.** Critique-RL uses RLOO as its base algorithm, while Retroformer uses PPO and CTRL uses GRPO (as stated in §5.1). The paper does not equalize the RL algorithm across methods — no ablation where Retroformer/CTRL are re-implemented with RLOO, nor where Critique-RL is run with PPO/GRPO. This means some portion of the reported advantage over these baselines could stem from RLOO being more effective for this setting rather than from the two-stage mechanism itself.  
   *Mitigation:* The ablation study (Table 3) does control for algorithm internally — all ablations share the same underlying RL method and demonstrate that the two-stage decomposition itself matters (e.g., "w/o Stage I" drops MATH Acc@Refine from 48.6 to 47.6; "w/o Stage II" to 45.9). So the core claim about two-stage > single-stage is well-supported. However, the headline comparisons against Retroformer/CTRL remain confounded, and the paper should either add an algorithm-controlled comparison or explicitly acknowledge this limitation.

### Minor

2. **Discrimination reward parsing accuracy is not analyzed.** The Stage I reward $r_{\text{dis}}$ relies on $f(x,y,c)$ extracting a Boolean judgment from free-form critique text. The paper provides one clean example (Figure 2) but does not report how often the critic produces a parseable judgment, the extraction success rate, or the accuracy of the parser. If parsing failures are frequent, the Stage I reward would be noisy, and the reported discriminability gains may depend on the parser quality rather than the RL optimization. Adding a simple parse-success rate and robustness analysis would significantly strengthen this component.

3. **Figure 1 (scaling plot) is confusingly labeled.** The table in the caption lists five data series including two entries labeled "w/o Critique-RL (3B)" — presumably one corresponds to @2k and the other to @3k sampling amounts (defined in the caption text), but the duplicate naming makes the figure hard to parse. The values are given only approximately (with ~), and the exact meaning of each baseline (e.g., "w/o Critique-RL" vs. "w/o Critique-RL (SFT)") is not specified in the main text. The central compute-efficiency claim relies on this figure; it should be cleanly legible.

4. **No variance or statistical significance reported.** All results come from a single run without standard deviations, confidence intervals, or significance tests. RL training can be noisy, and even 2–3% fluctuations could affect rankings on smaller datasets like AQuA. The paper should report results across multiple seeds or at minimum state that variance was negligible.

5. **Motivating analysis limited to one setting.** The failure-mode analysis in §4.1 is conducted only on GSM8K with Qwen2.5-3B. While the two-stage solution is then validated across more settings, the paper does not verify that the same conservative/aggressive failure patterns appear on other tasks or model sizes.

6. **KL regularization direction in Stage II is not justified.** Equation (9) uses $\text{KL}(\pi_\phi^{\text{Stage-I}} \mid\mid \pi_\phi^{\text{Stage-II}})$ (forward KL from Stage-I to Stage-II), whereas Stage I uses the more conventional $\text{KL}(\pi_\phi^{\text{SFT}} \mid\mid \pi_\phi^{\text{Stage-I}})$. The paper does not discuss this choice or compare it with the reverse direction. A brief explanation would clarify the design rationale.

### Trivial

7. The table in Figure 1's caption has the column "w/o Critique-RL (3B)" duplicated, likely corresponding to @2k and @3k variants, but this is not labeled in the table headers.

## Nice-to-Haves

- Including the summarization results (currently in Appendix G) in the main paper would strengthen the generality claim, as all main experiments are on math tasks.
- Studying the interaction between actor quality and critique effectiveness (e.g., using a weaker/stronger actor) would deepen the analysis of how the two-stage method depends on the actor's ability to follow feedback.
- A controlled RL algorithm comparison (Critique-RL with PPO/GRPO, or Retroformer/CTRL with RLOO) would eliminate the confound identified in Major weakness 1.

## Removed Points

The following points from the inputs are removed with justification:

- **"Without relying on stronger labeling or an oracle reward function during testing" is misleading (Harsh Critic):** The paper explicitly states "during testing" (line 104: "without relying on stronger labeling or an oracle reward function *during testing*"). The oracle verifier is only used for training rewards, which is standard practice. The claim is about not needing an oracle at test time, which is accurate. REMOVED — misunderstands the paper.

- **"@2k and @3k are never defined in the text" (Harsh Critic):** The caption of Figure 1 (line 42) states: "with @2k and @3k indicating sampling amounts that are 2 times and 3 times the x-axis value, respectively." These are defined. REMOVED — factually wrong.

- **Generic "evaluation lacks rigor" / area-of-concern sweeps:** Several speculative concerns from the Harsh Critic about whether "the metric could be measuring a proxy" or "confounders are controlled" without specific evidence from the paper. REMOVED — not grounded in specific statements in the paper.

- **Strength Finder's generic strengths that conflict with verified weaknesses:** "Compute-efficient test-time scaling" is partially retained (in Strengths) but the strength is tempered by the clarity issues in Figure 1. Other generic strengths were dropped per filtering instructions.

## Novel Insights

The most novel observation emerging from the reviews — beyond the paper's own contributions — is that the two-stage decomposition cleanly resolves what appears to be a fundamental tension in RL-based critique training: helpfulness optimizations (via indirect actor rewards) inherently degrade discriminability, while pure discriminability training (Stage I) does not yield helpful feedback. The paper shows this tradeoff empirically (Figure 3) and the ablation study (Table 3) confirms that the KL regularization back to Stage-I policy is what prevents discriminability collapse in Stage II. This suggests that for any system where a model must both judge correctness and provide formative feedback, explicit discrimination-phase pretraining followed by anchored helpfulness optimization may be a generally applicable recipe.

## Suggestions

1. Add a controlled comparison where all methods use the same RL algorithm (e.g., run Retroformer/CTRL-style rewards with RLOO, or Critique-RL with GRPO/PPO) to isolate the contribution of the two-stage design from algorithm choice.
2. Report parsing success rates for the discrimination reward $r_{\text{dis}}$ to confirm that parsing noise is not a confounding factor.
3. Run experiments with at least 3 random seeds and report means with std. dev. for the main results.
4. Clean up Figure 1: clearly label the two "3B" sampling-multiple baselines as "@2k" and "@3k" in both the figure legend and table, and report exact values rather than approximations.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>