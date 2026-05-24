Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper presents a comprehensive empirical analysis of rule-based and model-based verifiers for reinforcement learning with verifiable reward (RLVR) in mathematical reasoning. It establishes two main findings: (1) rule-based verifiers have non-negligible false negative rates (~14% on average) that worsen as policy models become more capable, and (2) while model-based verifiers improve static verification accuracy, they are vulnerable to reward hacking during RL training, with the paper providing direct evidence of a fine-tuned verifier's reward signal diverging from oracle rewards. A probing study further demonstrates that generative verifiers are broadly susceptible to simple adversarial patterns.

## Strengths

- **Quantifies the false-negative rate of rule-based verifiers and its increase with stronger models**: Figures 1 and 2 provide clear evidence that across three popular rule-based verifier implementations and five datasets, average recall is only 86%, dropping to 0.78 on challenging datasets like Skywork-OR1. The recall further declines as the generation model becomes more capable (Long-CoT models show lower average recall than weaker models), which is a practically concerning trend as the community deploys stronger reasoning models. This is concretely documented with multiple open-source systems.

- **Provides direct experimental evidence of reward hacking in a fine-tuned verifier with oracle reward tracking**: Figure 3 (right) shows that for the fine-tuned R1-Distill-Verifier-1.5B, the training reward diverges sharply from the GPT-4o oracle reward after approximately 450 training iterations, while an untrained verifier and the rule-based verifier maintain close alignment. This is accompanied by a drop in evaluation accuracy (Figure 3, left) from the peak. This empirical demonstration — with oracle tracking that reveals the divergence — is a clean validation of a concern the community has discussed anecdotally.

- **Systematic probing of verifier robustness with 13 attack patterns across 10 verifiers**: Table 3 shows that all generative verifiers, both fine-tuned and off-the-shelf, are highly vulnerable to simple manipulations (e.g., adversarial prefixes achieve 35% success on the fine-tuned verifier, empty symbols succeed at 23.6% for DeepSeek-R1-Distill-Qwen-1.5B), while discriminative verifiers (xVerify) are substantially more robust. This provides a structured benchmark for future robustness work.

- **Cross-domain validation**: The finding that rule-based verifier limitations and reward hacking persist on both Skywork-OR1 (math) and WebInstruct-Verified (general science), where the performance gap between rule-based and hybrid verifiers widens to 3.6 points, demonstrates that the issues are not dataset-specific.

## Weaknesses

### Fatal
None.

### Major

- **Single-run RL experiments without measures of statistical significance**: The RL training experiments (Table 2, Figure 3) are conducted with a single run and no standard deviations, confidence intervals, or multiple seeds. As the paper itself acknowledges, "All benchmarks are reported with a single sample due to computational constraints" (Figure 3 caption). For AIME24 and AMC23, the paper reports Avg@32, but the overall training process and the 2.3-point improvement from the hybrid verifier (55.0 → 57.3) come from a single trajectory. GRPO is stochastic, and without replication we cannot assess whether the reported gains or the reward hacking observation are robust. The cross-dataset replications on Skywork-OR1 and WebInstruct-Verified partially mitigate this concern, but the core DeepScaleR result lacks the statistical grounding expected for a paper making empirical claims of this nature.

- **The reward hacking claim is based on a single fine-tuned verifier, with an unreconciled counterexample**: The paper's narrative (§5) argues that fine-tuned model-based verifiers are prone to reward hacking, but this conclusion rests almost entirely on R1-Distill-Verifier-1.5B. The general-verifier — listed alongside it as a "trained verifier" in §5.1 — achieves 57.0 average accuracy (Table 2), essentially tied with the best non-hacked verifier at 57.3, with no evidence of reward hacking detected. The paper acknowledges this in passing ("one might assume that general LLM verifiers are relatively robust," line 255) but does not analyze what makes general-verifier robust while R1-Distill-Verifier-1.5B is hackable. This weakens the generality of the mismatch claim and leaves an important question open: is the issue fine-tuning per se, or something specific about the rejection fine-tuning procedure or data used for R1-Distill-Verifier-1.5B?

### Minor

- **Probing study uses 471 samples from a single dataset, with artificial attacks**: The hacking pattern evaluation (§6) is conducted on approximately 471 samples from DeepScaleR, with one adversarial answer per pattern per sample. While 13 pattern types provide breadth, the sample size is modest, and the attacks (prompt injection, gibberish, single symbols) are hand-crafted rather than arising organically from RL training dynamics. The paper itself identifies the disconnect: DS-R1-Distill-Qwen-1.5B has high attack success rates in probing but does not exhibit reward hacking in RL (§6.2, line 273: "the policy models in our RL training are not strong enough to find and exploit these vulnerabilities"). This means the probing results function as a potential risk assessment rather than a direct predictor of RL failure, a nuance that could be foregrounded more clearly.

- **GPT-4o is used as both the static annotation oracle and the RL oracle without validation on hard cases**: The static evaluation dataset (§3.1) relies on GPT-4o annotations validated against human judgments (Appendix B, stripped). The RL oracle reward (§5.2) also uses GPT-4o. While this is a reasonable approach, the paper does not report inter-annotator agreement rates or analyze cases where GPT-4o might be unreliable — particularly relevant given that the hybrid verifier's model-based component focuses specifically on hard cases that rule-based verifiers got wrong, which are likely the same cases where GPT-4o's own judgment could be uncertain.

- **"General Science" experiments in Appendix require more detail**: The paper mentions generalization to general science (WebInstruct-Verified, Appendix J), but the main text does not describe the dataset or evaluation procedure for this setting, making it difficult to assess the strength of this generalization claim without the appendix.

### Trivial
None.

## Nice-to-Haves

- An analysis of **why general-verifier is robust** to reward hacking while R1-Distill-Verifier-1.5B is not, which could inform design principles for robust verifiers. This is the most actionable open question the paper raises but does not address.
- **Multi-seed RL runs** (at least 3) for the main DeepScaleR experiment to establish statistical significance of the 2.3-point improvement claim.
- **Distribution-level visualizations** for the probing study (e.g., histograms per attack type across samples) to show whether high average success rates come from a few extreme cases or widespread vulnerability.
- Including concrete examples of reward-hacked outputs (single symbol, gibberish) in the main text to help readers assess the severity of the exploitation.

## Removed Points

- "Training details of R1-Distill-Verifier-1.5B are missing" — These are detailed in Appendix K, which is stripped by the parser. Per instructions, missing appendix content should not be flagged.
- "Missing related work" — Per instructions, I cannot verify which works exist or are missing.
- "Typos/formatting issues" — These are parser artifacts, not author errors.
- "The paper lacks a positive solution / defense experiments" — The paper self-identifies as an analysis paper (§7: "primarily analyzes... limitations and vulnerabilities"). Requesting defense experiments or a "solution" is scope creep beyond what the paper sets out to do.
- "Ablation of hybrid verifier design needed" — The paper provides a static evaluation comparison (Table 5 in Appendix F). Requesting additional architectural ablations is a reasonable suggestion but not a weakness.
- "The finding that recall drops with stronger models is not surprising" — This is a subjective judgment, not a methodological weakness. The paper provides empirical quantification that was not previously available.
- "The paper is primarily an analysis, not a solution" — The paper explicitly scopes itself as an analysis; this is an accurate characterization of its contribution type, not a weakness.

## Novel Insights

The most interesting observation that emerges from the reviews is the **asymmetry between probing vulnerability and actual RL exploitation**: the probing study shows that DS-R1-Distill-Qwen-1.5B is highly vulnerable to simple attacks (23.6% success on empty symbols), yet it does not exhibit reward hacking in RL. This suggests that probing-style adversarial evaluations of verifiers may overstate practical risk — a policy model must not only be able to generate hackable patterns but must also discover them through RL exploration, which depends on the optimizer's dynamics, reward landscape, and model capacity. Similarly, the fact that general-verifier (a fine-tuned verifier with strong static accuracy) resists reward hacking while R1-Distill-Verifier-1.5B does not suggests that the relationship between fine-tuning methodology and robustness is more nuanced than "fine-tuning causes hacking." The paper's data implicitly raises these questions even though the paper does not systematically resolve them.

## Suggestions

1. **Add multi-seed RL experiments** (at least 3 random seeds) for the main DeepScaleR comparison to provide standard deviations. If computational constraints preclude full re-runs, consider bootstrapping from checkpoints or reporting at least one replication for the key finding.
2. **Analyze and report why general-verifier avoids reward hacking**: compare its training data, architecture, or inference procedure to R1-Distill-Verifier-1.5B. This would transform the paper from a problem statement into a paper that offers design guidance.
3. **Increase the probing study sample size** and/or include samples from multiple datasets to strengthen the generality of robustness conclusions.
4. **Validate GPT-4o's oracle judgments** on a subset of hard verification cases (e.g., cases where GPT-4o disagrees with other verifiers) to quantify reliability, or add a secondary oracle annotation source.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>