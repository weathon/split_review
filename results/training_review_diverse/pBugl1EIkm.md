Here is the consolidated final review.

## Summary

This paper presents ReAgent, a defense against backdoor attacks on LLM-based agents. ReAgent uses a two-level consistency check — execution-level (thought–action consistency) and planning-level (instruction–reconstruction consistency) — to detect when a compromised agent is acting under a trigger. The core insight is that backdoor attacks create detectable inconsistencies among the user's instruction, the agent's planning, and its actions. Evaluated across three tasks (OS, DB, WebShop) and three backbone LLMs (GPT-3.5-Turbo, Mistral-7B, Llama3-8B), ReAgent reduces attack success rates from >90% to as low as 4%, while providing interpretable chain-of-thought explanations.

## Strengths

- **Novel two-level detection creates a principled evasiveness dilemma.** ReAgent checks both execution-level (thought–action) and planning-level (instruction–reconstruction) consistency. Section 4.1 argues that an action-only backdoor is caught at the execution level, while a thought-action backdoor is caught at the planning level. The ablation study (Figure 3) confirms this design: combining both levels reduces ASR further than either alone (e.g., from ~30% to ~4% in the DB thought-action attack). This dual-coverage approach is, to my knowledge, not present in any prior defense.

- **Large and consistent empirical reduction in attack success rate.** Table 2 shows ReAgent lowers ASR to as low as 4% on DB and OS tasks with GPT-3.5-Turbo, while all three baselines (Fine-pruning, Rephrasing, SelfCheckGPT) maintain ASRs >90%. The paper provides clear evidence that existing LLM backdoor defenses are ineffective against agent backdoors and that ReAgent substantially improves detection.

- **Chain-of-thought explanations improve detection accuracy and provide transparency.** Section 6.2 (Figure 4) demonstrates that including CoT explanations reduces FPR from 38% to 6% and ASR from 14% to 10%. Beyond accuracy, this feature enables users to understand and rectify false positives — a practical advantage over black-box detectors.

- **Evaluation across diverse tasks and backbone LLMs.** Experiments cover three representative environments (OS, DB, WebShop) and include both closed-source (GPT-3.5-Turbo) and open-source models (Mistral-7B, Llama3-8B) in Tables 2 and A.1. This breadth supports the claim of generalizability.

- **Empirical demonstration that common alternative defenses fail.** Section 6.1 shows fine-tuning with up to 3,000 clean samples still yields >90% ASR, and ONION fails because triggers (e.g., "update", ".txt") are innocuous words that do not affect perplexity. These negative results clarify why an agent-specific approach is needed.

- **Self-checking LLM approach outperforms fixed similarity metrics.** Figure 5 shows that BERTScore and STS yield AUCs near 0.5 (random) for distinguishing benign vs. backdoored cases, while ReAgent's LLM-based consistency check achieves high detection. This methodological choice is empirically validated.

## Weaknesses

### Fatal
None.

### Major

- **The defense relies on the compromised agent's own judgment for core detection, and this dependency is not adequately justified.** ReAgent's detection pipeline uses the same LLM that is under suspicion for both execution-level and planning-level consistency checks (Section 4.2). The paper assumes (Section 3.2) that "the agent is well-trained for the target task and can reason about its behavior within that task" and that the backdoor corrupts specific behavioral traces but leaves the model's self-checking capability intact. However, if an adversary controls the training data, they could train the model to appear consistent even when backdoored (e.g., produce innocuous reconstructed instructions from malicious thought trajectories). The paper provides no formal argument that this is impossible, tests no adaptive adversary who anticipates the defense, and offers only a brief assertion that the assumption is "realistic." This is a structural vulnerability in the threat model that readers evaluating security guarantees must weigh carefully.

- **The evaluation is limited to highly salient, clearly inconsistent backdoors, and the paper's own acknowledged failure mode is not tested.** All tested attacks (Table 1) use starkly malicious actions — `rm -rf`, forcing purchases of a specific brand — triggered by simple keywords. The paper's own limitation discussion (Section 6.4) identifies a case where the malicious action *aligns* with the user's instruction ("Purchase Adidas sneakers" from "Purchase sneakers") and concedes that ReAgent "struggles to identify" such backdoors. Despite this acknowledgment, no experiment tests this class of subtle backdoor. The results (e.g., "reduces ASR by up to 90%") therefore do not yet support the broader claim of defending "against a range of backdoor attacks" — the range tested is the range ReAgent was designed to catch.

### Minor

- **No statistical confidence information for any quantitative result.** All reported values (Table 2, Figures 3, 4, 5) are point estimates without confidence intervals, standard deviations, or replication details. Since ReAgent relies on stochastic LLM calls, the variance across runs could be substantial. The paper does not specify how many test samples were used, whether results are averaged over multiple runs, or the decoding strategy for LLM outputs. While this is common in some areas of LLM research, it limits the reader's ability to assess the robustness of the claimed gains.

- **The baseline comparison primarily shows that non-agent-specific defenses do nothing, which is a low bar.** Fine-pruning, Rephrasing, and SelfCheckGPT all achieve ASR >90% and near-0% FPR (Table 2), meaning they effectively never detect attacks and never flag benign cases. The paper acknowledges these baselines are not designed for agent backdoors (Section 5.1), but the central comparison table lacks even a simple random-detection baseline to contextualize FPR/ASR trade-offs. While showing that existing methods fail is informative, the "outperforming existing defenses by large margins" claim rests on defeating defenses that were not built for this setting.

- **The FPR of 38% without CoT (Figure 4) raises reliability concerns.** While CoT reduces FPR to 6%, the non-CoT variant has a very high false positive rate — meaning that without the explanation feature, nearly 40% of benign trajectories would be flagged as attacks. This suggests ReAgent without CoT is not reliable, and the dependency on CoT for acceptable FPR should be discussed more prominently.

- **The stoichiometric combination of detection levels is underspecified.** The ablation (Figure 3) evaluates "combining" both levels, but the paper does not clarify the logical rule (e.g., does the system flag if *either* level detects an inconsistency? Both? A weighted score?). The combined FPR is also not reported, which matters for practical deployment.

- **Only one poisoning rate (50%) is tested.** While this follows prior work (Wang et al., 2024b; Yang et al., 2024), testing lower, more realistic poisoning rates would strengthen the evaluation.

### Trivial
- The paper does not explicitly state the number of test samples used for each task/LLM combination.
- The text references Appendix B and C for implementation details (prompts, in-context examples) — these are not present in the parsed version but exist in the original submission.

## Nice-to-Haves
- **Test against backdoors that distort behavior subtly** (e.g., always choose the most expensive option when triggered, slightly alter numerical results) to address the limitation the paper itself identifies in Section 6.4.
- **Include a random-detection baseline** to calibrate FPR/ASR trade-offs.
- **Report computational overhead** (additional LLM calls per trajectory) compared to normal execution.
- **Discuss the assumption of thought-trajectory access** explicitly as a deployment constraint — some real-world agents (e.g., closed-source API agents) may not expose internal reasoning.
- **Test generalization to unseen trigger/task combinations** to assess whether ReAgent detects anomalies rather than memorized patterns.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Criticism about missing appendix content** (the harsh critic noted "deferred to Appendix B, which is missing from the parsed text"). Per policy: the parser strips appendix sections from all papers; they exist in the original submission. Removed.
- **Criticism that the baselines comparison is "not meaningful"** and equivalent to "doing nothing." The paper clearly acknowledges the baselines were designed for NLP settings, not agents. Showing that existing methods fail is informative — it motivates the need for ReAgent. The comparison is transparent about this limitation. Downgraded from the critic's characterization.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Address the self-checking threat model more rigorously. Either provide a formal argument about why the adversary cannot corrupt the consistency evaluation (e.g., architectural separation, input-output constraints), or modify ReAgent to use an independent verifier (separate trusted LLM, external constraints) for the consistency checks, at least as an ablation.
- Add experiments with subtle backdoors where the malicious action is not clearly inconsistent with the user's instruction (the "Purchase Adidas sneakers" type), and report ReAgent's detection performance.
- Report all key results (Table 2, Figures 3, 4) as mean ± std over multiple independent runs with different random seeds, or at minimum state the number of test samples and confirm whether results are stable across runs.
- Clarify the combination rule for execution-level and planning-level detection, and report the combined FPR.

## Score and Decision

This paper introduces a genuinely novel and well-motivated defense against an important and underexplored problem (backdoor attacks on LLM agents). The two-level inconsistency detection approach is clever, the evasiveness dilemma is a useful conceptual contribution, and the experimental results — on the attacks tested — are strong. However, two significant concerns prevent full acceptance: (1) the core detection pipeline relies on the compromised agent's own judgment without adequate justification that this cannot be subverted, and (2) the evaluation is confined to high-salience attacks that ReAgent was designed to catch, while the paper's own acknowledged failure mode (Section 6.4) is left untested. The paper represents solid early work in an important direction, but these gaps need to be addressed before the claims of robust defense are fully supported.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>