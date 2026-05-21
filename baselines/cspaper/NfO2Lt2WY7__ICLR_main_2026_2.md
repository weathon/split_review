---
job_id: baac0645-7684-4935-983e-b760666b0840
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: NfO2Lt2WY7.pdf
paper: Are Complicated Loss Functions Necessary for Teaching LLMs to Reason?
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on reinforcement learning for LLM post-training and empirical analysis of policy optimization objectives for reasoning.

## Minimum Quality
Pass ✅. The paper contains the required scientific components, including abstract, introduction, related work, methodological formulation, experiments, quantitative/qualitative results, and conclusion. While there are notable issues in novelty, clarity, and evidential strength, these do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies whether the main ingredients of GRPO are all necessary for improving reasoning in LLM post-training. The authors ablate GRPO into several variants, identify negative feedback and group-relative advantage estimation as important ingredients, and propose RGRA, a simplified REINFORCE-style objective that removes PPO-style clipping and policy-ratio terms while keeping group-relative advantages and KL regularization. Experiments on small Qwen and Llama instruction-tuned models trained on 1,800 GSM8K examples evaluate training dynamics, math benchmarks in English and Chinese, and a small qualitative reasoning example.

## Strengths
The paper asks a useful and timely question. A large amount of current RL-for-LLM practice inherits fairly complicated objectives, and it is valuable to test whether some of those components are actually doing useful work versus just adding implementation baggage.

I appreciated the paper’s attempt to isolate specific components of GRPO rather than only introducing yet another variant. The decomposition into positive-only advantages, RGRA without PPO-style constraints, and direct-reward REINFORCE is conceptually clean and easy to follow at a high level.

The empirical setup spans multiple model families and sizes, not just one checkpoint. Testing on Qwen2.5-0.5B, Qwen2.5-1.5B, and Llama3.2-1B gives at least some evidence that the observed trends are not entirely model-specific.

The benchmark coverage is broader than a single test set. Tables 1, 2, and 3 include English math, Chinese math, and STEM evaluations. In particular, Tables 1 and 2 show a fairly consistent pattern that RGRA is competitive with or slightly better than GRPO on the two Qwen models, which is the central empirical observation of the paper.

The training-dynamics plots in Figure 1 are useful. Even though the paper over-interprets them in places, the figure does support one important qualitative claim, namely that positive-only variants and RAFT can produce shortened responses or collapse in the smallest model. In Figure 1(a)-(b), the Qwen2.5-0.5B curves clearly separate the stable GRPO/RGRA trajectories from the collapsing positive-only / RAFT regimes, and this is a more informative presentation than reporting only final benchmark scores.

The qualitative example in Figure 2 does help communicate what the authors mean by “emergent reasoning behaviors.” It is a simple example, but the contrast between direct-answer behavior in Figure 2(a) and the explicit step-by-step derivation in Figure 2(b) is intuitive for readers.

The paper is easy to reproduce at a coarse level. The training set source, reward design, group size, maximum generation length, and main hyperparameters are stated in the main paper, and there is a reproducibility statement with code availability.

## Weaknesses
1. **The claimed methodological contribution is quite narrow, and the paper oversells it.**  
   The proposed method, RGRA in Equation (2) on Page 5, is very close to a standard REINFORCE-style policy-gradient update with a group-normalized reward baseline and a KL penalty. That is a reasonable variant to test, but the paper often presents the findings in much broader language, for example in the abstract and conclusion, suggesting that “PPO-style constraints are unnecessary” for teaching LLMs to reason. The actual evidence is much narrower: small models, one training dataset, one reward design, and short training runs. This matters because the paper’s headline claim is substantially broader than the demonstrated regime. A more defensible framing would be “in this small-scale RLVR setting, removing clipping did not hurt and sometimes helped.”

2. **The empirical evidence is too limited to support general claims about GRPO, PPO-style clipping, or reasoning.**  
   All training uses only 1,800 GSM8K training instances, as stated in Section 3.1 on Page 4. The model scales are 0.5B, 1B, and 1.5B, all LoRA-finetuned, with a very simple binary-ish reward made of correctness plus a small format bonus. This is a useful pilot study, but it is far from enough to conclude that clipping and policy ratios are broadly unnecessary in RL post-training for reasoning. In fact, the smallest-scale setting is exactly where some simplifications may look benign because the optimization horizon, policy drift, and distribution shift are limited. The paper repeatedly generalizes beyond what is justified.

3. **The comparisons are single-number comparisons with no variance estimates, significance tests, or multi-seed robustness.**  
   Tables 1, 2, and 3 report one accuracy number per condition, with no standard deviation, confidence interval, or indication of how many seeds were run. This is a major omission for a paper whose main contribution is a relative comparison between closely related objectives. For example, in Table 1, Qwen2.5-1.5-it improves from 37.3 (GRPO) to 38.3 (RGRA) on the English-math average, and in Table 3, from 45.7 to 50.7 on STEM average. Some of these gaps may be real, but without seed variability, one cannot tell which differences are robust and which are noise. This especially matters because the paper counts wins such as “17 out of 27 tasks” in Section 4, but many per-task differences are tiny and may not survive repeated runs.

4. **Important details of the optimization setup are underspecified, which makes the mathematical and algorithmic comparison less clean than it appears.**  
   Equation (1) on Page 4 gives the GRPO objective, and Equation (2) on Page 5 gives the RGRA gradient, but the paper is vague about several implementation details that materially affect interpretation:
   - How many optimization epochs or gradient updates are performed per sampled batch for GRPO versus RGRA?
   - Is GRPO truly on-policy with one update per rollout batch, or are there repeated minibatch updates over the same sampled trajectories?
   - How exactly is the KL term computed at token level in practice, especially for variable-length generations?
   - What happens when $\mathrm{std}(r_1,\ldots,r_G)=0$ in the group-relative advantage definition on Page 4? This case seems very plausible under sparse rewards. Is there an $\epsilon$ added to the denominator?
   
   These are not cosmetic details. If the number of reuse steps differs, then removing the policy ratio is not merely “removing clipping”; it also changes whether the estimator is correcting for off-policy reuse. Likewise, if zero-standard-deviation groups occur frequently, the stated advantage in Equation (1) is numerically ill-defined without an explicit stabilization constant.

5. **The math and notation are sloppy in ways that matter for understanding the method.**  
   Several equations and symbols are inconsistent or underexplained:
   - In the PPO expression on Page 3, the indexing mixes $o_t$ and $o_{i,<t}$, even though there is no instance index $i$ in that equation.
   - In Equation (1) on Page 4, the advantage is written as $\hat A_{i,t}$, but the formula depends only on trajectory-level reward $r_i$, so the time index $t$ is misleading unless the same scalar is broadcast to all tokens. If that is the intent, it should be stated explicitly.
   - In the GRPO-pos definition on Page 5, the expectation is written over $\pi_{\theta_{\text{off}}}$, but this symbol is not introduced anywhere else in the main paper. Elsewhere, the paper uses $\pi_{\theta_{\text{old}}}$. This is not a harmless typo, because off-policy versus old-policy sampling is conceptually important here.
   - Equation (2) defines a gradient rather than an objective, but the surrounding discussion still speaks of “the following gradient” without carefully separating objective and estimator. If the central message is simplification and transparency, the presentation should be more precise, not less.
   
   These issues reduce confidence that the compared objectives were specified and reasoned about rigorously.

6. **The evidence for “negative feedback is indispensable” is weaker than the paper claims.**  
   The paper compares GRPO-pos and RAFT against GRPO/RGRA and interprets worse performance as proof that negative feedback is essential. But the paper changes several things at once across methods. RAFT is not simply “no negative feedback”; it is a different training paradigm based on selecting top responses and doing cross-entropy training. GRPO-pos still retains clipping and KL, but also zeroes out all non-positive advantages, which changes both the signal and the effective sample size of policy updates. Therefore, the conclusion should be more local: these two particular positive-only training regimes under this setup underperform. That is weaker than the categorical statement in the abstract and conclusion.

7. **The Figure 1 analysis is suggestive, but the paper over-interprets it and omits key axes needed for a fair stability claim.**  
   Figure 1 does show collapse-like behavior for RAFT and positive-only settings, especially in Qwen2.5-0.5B. However, the figure only reports average reward and average response length over training. Those are weak proxies for optimization stability. A shortened response can reflect collapse, but it can also reflect a model learning to answer tersely under the given reward. Conversely, long responses are not evidence of better reasoning. Moreover, the plots do not report KL divergence, entropy, gradient norms, or policy-ratio statistics, which are exactly the kinds of quantities one would want when making claims about the necessity of PPO-style constraints. In Figure 1(c)-(f), for the larger models, the differences are more mixed than the text suggests, especially because some curves remain reasonably stable even when final benchmark performance differs. The figure is useful, but not enough to sustain the paper’s mechanistic conclusions.

8. **The benchmark tables reveal a more mixed picture than the narrative suggests.**  
   The write-up emphasizes that RGRA “outperforms GRPO in most settings,” but Tables 1, 2, and 3 are not uniformly favorable. For Llama3.2-1.0-it, RGRA is basically tied with GRPO on English math in Table 1 (20.2 vs 20.1 average), worse on Chinese math in Table 2 (26.6 vs 30.1), and slightly worse on STEM in Table 3 (22.5 vs 24.9). Even within the Qwen models, the gains are sometimes modest or inconsistent across subsets, for example AMC23 in Table 1 where RGRA is not better than GRPO for Qwen2.5-1.5-it. So the empirical conclusion should be stated much more carefully: RGRA appears competitive and often strong on the two Qwen models, but the evidence is not uniformly positive across architectures.

9. **The qualitative reasoning analysis is too weak to support claims about “emergent reasoning behaviors.”**  
   Figure 2 on Page 9 shows one example from Countdown, with one direct-answer output and one chain-of-thought-like output. This is nowhere near enough to support the broader claims in Section 4 about the emergence of interpretable reasoning strategies. There is no dataset-level analysis, no rate of explicit reasoning traces, no success-conditioned analysis, no length-controlled comparison, and no evidence that the reasoning traces are causally tied to correctness rather than just stylistic verbosity. If the authors want to make claims about reasoning behavior rather than just benchmark accuracy, this section needs substantially more substance.

10. **The baseline space is incomplete for the exact claim being made.**  
    The paper positions itself as a simplification study of GRPO, but the baselines in the main experiments are mostly GRPO, positive-only GRPO, direct-reward REINFORCE, RAFT, and supervised fine-tuning. That is a reasonable starting point, but for a paper arguing that policy-ratio clipping is unnecessary, I expected at least a stronger ablation around the clipping mechanism itself: e.g., varying $\epsilon$, removing clipping while retaining ratios, or studying different numbers of policy updates per sampled batch. As written, the paper compares one particular clipped objective against one particular no-ratio/no-clipping objective, which makes it difficult to attribute the effect specifically to clipping rather than to several bundled implementation changes.

11. **The presentation has multiple signs of insufficient polishing.**  
    Beyond the notation issues above, there are many writing and citation problems in the main paper: typographical errors such as “prefernces” on Page 1, inconsistent citation formatting, duplicated or malformed references, and awkward prose in the references section. The “Models” paragraph on Page 4 has grammatical issues, and some benchmark names are inconsistently formatted. These do not invalidate the work, but they make the paper feel less mature than it should be for a main-track ICLR submission.

12. **The conclusion overstates the scientific takeaway relative to the evidence.**  
    Section 5 says the work demonstrates that negative feedback is indispensable, advantage estimation is crucial, and PPO-style clipping is unnecessary. The first two may be plausible working hypotheses from these experiments, but the third is still too strong. The paper has shown that in this narrow setup, a simplified REINFORCE-style variant can match or beat GRPO. That is interesting. It has not shown that clipping is generally unnecessary for teaching LLMs to reason.

## Questions
1. In Equation (1) on Page 4, the group-relative advantage is defined as
   \[
   \hat{A}_{i,t}=\frac{r_i-\mathrm{mean}(r_1,\ldots,r_G)}{\mathrm{std}(r_1,\ldots,r_G)}.
   \]
   What is done when $\mathrm{std}(r_1,\ldots,r_G)=0$? Please state the exact stabilized form used in implementation, for example whether you use
   \[
   \hat{A}_{i}=\frac{r_i-\bar r}{\mathrm{std}(r)+\epsilon}
   \]
   and what value of $\epsilon$ is used. This is especially important under sparse correctness rewards.

2. For GRPO versus RGRA, how many optimization passes are performed per rollout batch? If GRPO reuses the same sampled data for multiple updates while RGRA does not, then removing policy ratios changes more than just clipping. Please provide the exact update schedule in the main rebuttal.

3. Did you run multiple random seeds for Tables 1, 2, and 3? If yes, please report mean and standard deviation. If not, can you at least provide seed sensitivity for the key comparisons GRPO vs RGRA on Qwen2.5-0.5B and Qwen2.5-1.5B? This would materially affect my confidence.

4. Can you provide a more direct clipping ablation, rather than only comparing full GRPO to RGRA? For example:
   - keep policy ratios but remove clipping,
   - vary $\epsilon$,
   - vary the number of updates per rollout batch.
   
   This would help isolate whether clipping itself is unnecessary, versus the broader change to a one-pass REINFORCE-style estimator.

5. The claim that negative feedback is indispensable currently rests on GRPO-pos and RAFT. Can you clarify whether you tested any softer forms of positive-focused training, such as downweighting rather than zeroing negative advantages? That would help determine whether the failure is due to removing negative feedback per se or due to making the effective gradient too sparse.

6. Figure 2 is illustrative but anecdotal. Can you provide dataset-level evidence for “emergent reasoning behaviors,” such as average number of reasoning tokens, percentage of outputs containing intermediate steps, or correctness conditioned on reasoning-trace presence? A broader analysis here would strengthen the reasoning-specific claims.

7. Since the Llama3.2-1.0-it results are notably less favorable to RGRA than the Qwen results in Tables 1 to 3, do you have any hypothesis for why the architecture family appears to matter? Even a short controlled discussion would improve the paper’s scientific value.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work studies post-training objectives on public math and STEM benchmarks using rule-based rewards, and I did not identify human-subjects, privacy, or safety issues that would require an ethics flag based on the provided text.

## Soundness Rating
2: fair. The core empirical observation is plausible and partially supported, but the technical specification is loose, the math/notation has several issues, and the evidence is not strong enough for the breadth of the claims.

## Presentation Rating
2: fair. The high-level story is understandable, but the paper has multiple notation inconsistencies, underexplained equations, overstrong claims, and noticeable writing/reference quality issues.

## Contribution Rating
2: fair. The question is worthwhile and the ablation is somewhat informative, but the methodological step from GRPO to RGRA is modest and the empirical evidence is too narrow to make this a strong contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper asks a good question and provides some useful evidence that a simpler GRPO-like objective can work well in a small-scale RLVR setting. However, the current version overclaims, under-specifies important algorithmic details, and does not provide sufficiently robust evidence, especially given the narrow scale and absence of variance estimates. I see this as promising but not yet ready at ICLR standard.

## Reviewer Confidence
4: confident. I am confident in the assessment and carefully checked the main equations, tables, and figures, though I would still welcome clarification from the authors on the exact optimization details and stability handling.