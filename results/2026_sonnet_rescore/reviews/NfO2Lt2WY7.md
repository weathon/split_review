## Summary
The paper conducts a systematic ablation study of Group Relative Policy Optimization (GRPO) to identify which components—group-relative advantage estimation, PPO-style clipping, and KL regularization—are necessary for effective post-training of LLMs on mathematical reasoning tasks. The authors find that (1) negative feedback is essential for training stability and performance, (2) advantage estimation is indispensable, and (3) PPO-style clipping is not required. Based on these findings, they propose REINFORCE with Group Relative Advantage (RGR/RGRA), a simplified variant that removes the PPO-style clipping and policy-ratio terms while retaining group-relative advantage estimation. Experiments across three model sizes (Qwen2.5-0.5B, 1.5B, and Llama3.2-1B) on nine benchmarks support the claim that RGR achieves comparable or slightly superior performance to GRPO.

---

## Strengths

- **Systematic ablation identifies essential GRPO components**: Figure 1 provides clear, consistent evidence across all three model families that positive-only advantages (GRPO-pos) and direct-reward REINFORCE suffer catastrophic reward and response-length collapse within the first 20–40 steps, while GRPO and RGR maintain stable training trajectories. This is a concrete, reproducible finding.

- **RGR broadly matches or surpasses GRPO across diverse benchmarks**: Tables 1–3 show RGR achieves the highest average Math-English score on all three models (e.g., Qwen2.5-0.5B: 26.5 vs. 25.6; Qwen2.5-1.5B: 38.3 vs. 37.3 for GRPO), wins 17/27 individual benchmark comparisons, and shows larger margins on STEM benchmarks (e.g., Gaokao2024-STEM: 41.2 vs. 32.6 for 1.5B). The count of 17/27 wins is verifiable from the tables.

- **Broad multilingual evaluation supports generalization**: The paper covers nine benchmarks spanning English math, Chinese math, and STEM domains. The Chinese math gains for Qwen2.5 models (e.g., 0.5B RGR avg 55.1 vs. GRPO 51.4; 1.5B RGR 69.3 vs. GRPO 65.7 in Table 2) suggest the simplification generalizes beyond English.

- **Emergent reasoning behavior observed only under stable advantage-based methods**: Figure 2 and the analysis on the Countdown dataset show that RAFT and GRPO-pos models produce direct answers without reasoning steps, while GRPO and RGR models produce explicit multi-step chains. This is a useful qualitative indicator beyond benchmark accuracy.

---

## Weaknesses

### Fatal
None.

### Major

- **Limited training duration conflates "clipping inactive" with "clipping unnecessary"**: Training runs only ~70 optimizer steps with LoRA (rank 128, ~10% of parameters) on 1,800 examples with a 512-token generation cap. After only 70 steps, neither GRPO nor RGR drifts far from the reference policy, which means the PPO clipping constraint is likely never meaningfully activated. The paper cannot distinguish the claim "clipping is unnecessary" from "clipping is inactive at this scale and duration." The paper itself acknowledges in the conclusion that larger models and longer training were out of scope due to hardware constraints—but this framing presents scale limits as future work rather than as a caveat on the current claims. A single ablation showing how far policy ratios actually diverge during RGR training (relative to the clipping boundary) would directly address this confound but is absent.

- **No statistical validation for competitive performance claims**: The core claim in the conclusion—that RGRA "surpasses GRPO on 17 over 27 tasks, establishing it as a competitive reinforcement learning objective"—is not supported by any variance estimates, confidence intervals, or significance tests. For English math benchmarks, the RGR-vs.-GRPO margin averages 0.9 points (0.5B), 1.0 point (1.5B), and 0.1 points (1B) per Table 1. Many individual comparisons flip direction: GRPO outperforms RGR on OlympiadBench (1.5B: 12.6 vs. 12.0) and Chinese math for Llama (30.1 vs. 26.6). Without variance reporting, "surpasses" is unsubstantiated—the honest characterization is "comparable," which is still a useful finding but a weaker contribution claim.

### Minor

- **Unexplained inconsistency between Figure 1 training dynamics and Table 1 evaluation results for REINFORCE**: Figure 1 caption states that REINFORCE on Qwen2.5-0.5B causes both reward and response length to collapse to near zero by step ~20, with the paper describing this as "degenerate outputs of minimal length." Yet Table 1 reports Qwen2.5-0.5B REINFORCE achieving 44.7 on GSM8K—higher than the 41.5 untrained baseline. A model producing near-zero-length outputs at evaluation time should not consistently outperform the baseline. The paper neither acknowledges this tension nor explains it (e.g., whether best-checkpoint vs. final-checkpoint evaluation was used, or whether the collapse is specific to on-policy generation during training rather than evaluation). This undermines confidence in how training trajectories relate to reported benchmark numbers.

- **RAFT's inclusion in an RL component ablation muddies the framing**: The three ablations described in Section 3.2 isolate individual GRPO components (positive-only advantages, removal of clipping, removal of advantage estimation). RAFT is a supervised fine-tuning method on selected responses—fundamentally a different algorithm class—yet it is analyzed alongside the RL variants as if it is a "simplified RL approach." The paper's conclusions about which RL components are necessary do not cleanly extend to explaining RAFT's behavior, and its inclusion raises a question (SFT vs. RL) that is somewhat separate from the paper's stated question (which GRPO components are necessary). A cleaner framing would separate the RL component ablation from the RAFT comparison.

### Trivial

- **Method naming is inconsistent across the paper**: The abstract and Table 1–3 use "RGR," while Section 3.2 and the objective notation use "RGR A," and the conclusion (Section 5) uses "RGRA" throughout. The reader must infer these are the same method.

---

## Nice-to-Haves

- Reporting the actual policy-ratio distributions during RGR training would directly diagnose whether clipping is inactive (ratios stay near 1.0) or genuinely irrelevant (ratios diverge but training remains stable). This single diagnostic would substantially strengthen the mechanistic argument.
- Running GRPO and RGR to convergence—even just on the existing 0.5B and 1.5B models with full SFT instead of LoRA—would test whether clipping eventually activates and matters over longer training horizons.
- Running each condition with at least 2–3 random seeds and reporting mean ± std would allow the 17/27 comparative claim to be stated with appropriate confidence.
- The relationship between RGR and Ahmadian et al. (2024), which argued that REINFORCE-style methods suffice for strong pretrained LLMs, deserves more explicit treatment. The novelty of RGR is specifically the combination with group-relative advantage estimation; stating this precisely would better position the contribution.
- Figure 2 reasoning trace analysis is on the Countdown dataset, but no quantitative evaluation (e.g., fraction of responses with reasoning traces) is provided. Even a small-scale count would be more convincing than one cherry-picked example.

---

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **GSM8K decontamination concern (Harsh Critic)**: The critic argues that evaluating on GSM8K test split after fine-tuning on GSM8K train split conflates train and test distribution. This is standard protocol—decontamination means the pretrained models weren't trained on it, and fine-tuning on a train split then evaluating on the test split is normal. **Removed: not a real methodological flaw.**

- **Code link blank placeholder (Harsh Critic)**: "The link to our code is ." The hard rules flag this as an anonymization artifact rather than an author error. **Removed per hard rules.**

- **512-token generation cap (Harsh Critic)**: The critic suggests this may create a reward-landscape artifact. However, the paper does not claim to study long-chain-of-thought behavior and the cap is disclosed. The comparisons are consistent across all methods under the same constraint. **Removed: not a substantive flaw given the paper's scope.**

- **Strength — "Emergent reasoning behaviors" as a major contribution (Strength Finder)**: The evidence is a single qualitative example from one Countdown problem (Figure 2). No quantitative measure of reasoning trace frequency is provided. The strength is real but the evidence for it is too thin to call it a core contribution. **Demoted to a qualitative observation rather than a core strength.**

- **Strength — "Comprehensive experimental setup supports reproducibility" (Strength Finder)**: The Appendix A description is stripped by the parser (per hard rules, the appendix exists), and the code link is an anonymization artifact. The setup is adequately described in Section 3.1. The claim about reproducibility is generic; **removed as insufficiently specific.**

---

## Novel Insights

The paper's most actionable insight is the demonstration that the group-relative advantage—not the PPO-style policy-ratio clipping—is the load-bearing component of GRPO for stability and reasoning emergence. This reframes the engineering challenge for researchers who want GRPO-like benefits without its complexity. The result that direct-reward REINFORCE (without group-relative normalization) fails even in the stronger 1.5B model, while RGR (REINFORCE with group-relative advantages) succeeds, is a clean empirical argument for the advantage-estimation mechanism rather than the clipping mechanism as responsible for GRPO's effectiveness. The convergence of this finding across three architecturally different models (Qwen2.5-0.5B, Qwen2.5-1.5B, Llama3.2-1B) increases its credibility within the stated experimental regime.

---

## Suggestions

1. **Add policy-ratio monitoring**: Log the distribution of $r_{i,t} = \pi_\theta / \pi_{\theta_\text{old}}$ during both GRPO and RGR training to show whether clipping is ever activated in GRPO. If ratios consistently stay in $(1-\epsilon, 1+\epsilon)$, this would prove the clipping constraint is inactive and make the "unnecessary" conclusion much more rigorous.
2. **Diagnose the REINFORCE collapse vs. benchmark accuracy inconsistency**: Clarify whether evaluation uses best-checkpoint or final-checkpoint; report per-step benchmark accuracy for REINFORCE to show whether the gain on GSM8K (44.7) is achieved before collapse or survives it.
3. **Report variance across multiple seeds** for at least the average benchmark scores to validate the 17/27 win-rate claim.
4. **Extend training duration** on existing small models to show whether RGR remains stable beyond 70 steps, which is the minimum needed to make the "clipping unnecessary" claim credible over non-trivial training lengths.

---

## Score and Decision

**Originality**: The core idea—removing PPO clipping from GRPO while retaining group-relative advantages—is incremental but provides clean empirical support for a widely held intuition that has lacked systematic ablation evidence. Score: 3/5.

**Importance of research question**: Understanding which components of GRPO are necessary is directly relevant to the community of practitioners deploying RL-based post-training at scale. Score: 3/5.

**Claims well supported**: The stability claims (Figure 1) are well supported. The "surpasses GRPO" claim is overstated given the small margins and absence of statistical tests, though "comparable to GRPO" is well supported. Score: 3/5.

**Soundness of experiments**: The ablation structure is coherent. The scale (70 steps, ≤1.5B, LoRA) limits the strength of the central conclusion; the REINFORCE inconsistency is unexplained. Score: 3/5.

**Clarity of writing**: The paper is generally clear, with well-defined objectives and organized results. The minor naming inconsistency (RGR vs. RGRA) is a blemish. Score: 4/5.

**Value to research community**: The practical takeaway—RGR achieves GRPO-level performance with a simpler objective—is useful even if the scale is limited. Score: 3/5.

Overall: The paper makes a real, specific, and experimentally grounded contribution. The main weaknesses are the limited experimental scale (which cannot fully rule out "inactive" vs. "unnecessary" clipping), the absence of statistical validation for competitive-performance claims, and one unexplained inconsistency. These are notable but do not invalidate the core finding. This is a borderline-to-weak accept.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>