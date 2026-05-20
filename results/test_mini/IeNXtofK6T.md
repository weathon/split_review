Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper revisits the idea of using an off-the-shelf LLM (via prompting, no fine-tuning) to detect and remove prompt injections in LLM agents — a defense that prior work had dismissed as ineffective. The key finding is that with modern LLMs (GPT-4o, GPT-4.1, Qwen3-32B) and a carefully designed system prompt, this simple approach achieves remarkably low false positive and false negative rates on three benchmarks (sub-1% FPR/FNR on AgentDojo), substantially outperforms prior prompting-based and several specialized defenses, and preserves agent utility by removing rather than discarding injected content. The paper includes informative ablations on model size, reasoning capability, and prompting strategies.

## Strengths

1. **Striking detection accuracy on established benchmarks.** Table 1 shows PromptArmor with GPT-4o achieves 0.07% FPR and 0.23% FNR on AgentDojo, and below 5% on Open Prompt Injection and TensorTrust. This directly supports the paper's central claim — that prior negative results were artifacts of weaker LLMs, not of the prompting approach itself. These numbers are genuinely impressive and practically meaningful.

2. **End-to-end defense effectiveness with utility preservation.** Table 2 shows PromptArmor-GPT-4.1 reduces ASR from 54.53% (no defense) to 0.00% while maintaining UA of 72.02% — the highest UA among all defenses with ASR below 1%. The removal-based design (versus discarding inputs) is meaningfully better for utility than alternatives like Tool Filter (18.80% UA).

3. **Clean ablation isolating model capacity from reasoning.** The Qwen3 experiment (Figure 3) across 0.6B, 8B, and 32B models in both reasoning and non-reasoning modes is well-designed and informative. It cleanly shows that 32B models achieve near-perfect detection regardless of reasoning mode, while 0.6B models cannot resolve the security-utility trade-off regardless of reasoning. This disentangles two confounded factors in prior work.

4. **Data contamination sanity check.** Section 4.5 conducts a memorization test (Carlini et al., 2021; Staab et al., 2023) and finds an average prefix-suffix similarity of 0.34, with only 3.5% of samples exceeding the 0.6 threshold — ruling out the concern that the guardrail LLM's performance is due to benchmark memorization.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline comparison is confounded by model capacity.** PromptArmor's best results use GPT-4o/4.1 (massive proprietary models), while the detection baselines (Deberta, Llama Prompt Guard 2, DataSentinel) use models orders of magnitude smaller (e.g., Mistral-7B, Deberta-v3). The paper acknowledges this for DataSentinel (line 266: "the released version uses Mistral-7B... which has limited reasoning ability"), but this acknowledgment does not resolve the confound. The conclusion that the *prompting approach* drives the improvement is not fully separable from the fact that the approach uses a much larger model. The Qwen3-32B experiment partially addresses this by showing prompting at a moderate scale works well, but a direct comparison — e.g., fine-tuning a similarly sized model for the same detection task vs. prompting it — is missing. The paper's core claim ("should be a standard baseline") is not undermined, but the comparative framing against existing defenses overstates what the evidence supports.

2. **Adaptive attack evaluation is too narrow for the robustness claims made.** The paper tests only one adaptive method (AgentVigil, a fuzzing-based template generator). In the results text (line 313), the claim is properly qualified as "robustness against fuzzing-based adaptive attacks." However, the abstract (line 27) states the paper "demonstrate[s] that PromptArmor is robust against adaptive attacks specifically designed to circumvent it" — without qualification. An adaptive adversary could use many other strategies (e.g., gradient-based optimization to craft injections with low detection signal, prompt leaking to disable the guardrail, adversarial suffixes targeting the guardrail LLM's detection prompt). The current experiment does not support the broader claim of robustness against adaptive attacks in general.

### Minor

1. **The removal step is not directly evaluated.** The method's second step — fuzzy matching to extract and excise injected text — is only evaluated indirectly via end-to-end ASR and UA. A direct removal accuracy metric (e.g., what fraction of injection text is correctly removed, what fraction of benign content is erroneously excised) would strengthen the evidence that the method works as described. The paper describes the fuzzy matching mechanism (Section 3.1, lines 80-82) but provides no standalone evaluation of its correctness.

2. **"Computational efficiency" claim is overstated.** Section 3.2 claims computational efficiency as an advantage ("no need for extra costly data collection, model design, or training processes") and states that "even smaller LLMs can achieve effective detection performance." However, the 0.6B Qwen3 model has 62.57% FPR or 75.71% FNR depending on reasoning mode (Figure 3) — neither is "effective." The 8B model achieves reasonable FPR (0.14%) but high FNR (26.50%) without reasoning. Only the 32B model approaches GPT-4.1's performance. The paper should be more precise about what "smaller" means and what performance tradeoffs smaller models incur. Additionally, no cost or latency numbers are reported, which would help practitioners evaluate the practical tradeoff.

### Trivial
None.

## Nice-to-Haves

- **Cost and latency analysis.** Even rough estimates (cost per data sample for GPT-4o vs. Qwen3-32B, latency) would help users decide when PromptArmor is practical.
- **Failure case analysis.** With only 1-2 false positives on AgentDojo for GPT-4o, a qualitative analysis of these cases could inform future improvements.
- **Direct removal accuracy measurement.** Evaluating what fraction of injected text is correctly excised by the fuzzy matching step.
- **Broader adaptive threat model testing.** Beyond AgentVigil, testing against a small set of qualitatively different adaptive strategies (e.g., gradient-based optimization, adversarial suffix targeting the guardrail prompt).

## Removed Points

- **Criticism that "Adaptive attack evaluation is too narrow to support robustness claims"** — This is partially retained in Major Weakness 2 but the reviewer's framing as "fatal" or "structural" is removed. The paper does properly qualify "fuzzing-based adaptive attacks" in the results section. The mismatch with the broader abstract claim is noted.
- **Criticism about missing related works** — Not included per instructions; no external sources to confirm omissions.
- **Strawman points from Strength Finder** — Generic strengths about "importance of the problem" dropped. All retained strengths are specific and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The main finding — that prompting a modern off-the-shelf LLM works much better than prior work suggested — is the paper's contribution, and the reviewers did not surface a genuinely new insight that the paper itself missed.

## Suggestions

1. **Temper the abstract's robustness claim.** Replace "robust against adaptive attacks specifically designed to circumvent it" with a more precise description (e.g., "shows initial resistance to fuzzing-based adaptive attacks").
2. **Add a direct removal accuracy experiment.** Use benchmarks that provide ground-truth injection boundaries (AgentDojo does) to report both detection and removal metrics separately.
3. **Report cost and latency.** Even one sentence on approximate cost-per-query for each guardrail model would substantiate the "computational efficiency" claim.
4. **Add a discussion of the model capacity confound in the baseline comparison.** The paper already notes DataSentinel uses Mistral-7B; a more explicit discussion of how this limits the comparison would strengthen the paper's honesty and reproducibility.
5. **Consider adding one more open-source model family** (e.g., Llama-3-70B or DeepSeek-R1) to the Qwen3 ablation to strengthen the "model size, not just reasoning, drives performance" argument.

## Score and Decision

**Calibration details (all rounds):**

**Round 1 — Bracketing:**
- Weak anchors (< 3.5): orzX69D5UO (3.00, Cognitive Control Architecture), PKrYc2nyO4 (3.20, SAID), d1fVTnq3c8 (2.50, Bypassing Prompt Guards), M4He5YzG44 (3.33, LEG) — all rejected or withdrawn. PromptArmor is substantially stronger than these.
- Middle anchors (3.5–7.5): SelfGrader (4.00, Reject), DiffuGuard (5.20, Accept Poster), Adaptive Attacks on Trusted Monitors (5.50, Accept Poster), SENTINEL (4.50, Reject). PromptArmor is cleaner and more convincing than SelfGrader and SENTINEL, comparable to DiffuGuard and the Trusted Monitors paper.
- Strong anchors (> 7.5): Mostly unrelated oral papers on other topics (LLMs in multi-turn, multimodal reasoning, etc.). PromptArmor is not in this tier.

**Initial bracket:** 4.5 – 6.5

**Round 2 — Narrowing within bracket:**
- ChatInject (5.00, Accept Poster) — attack paper on AgentDojo; received 6,8,2,4. PromptArmor has a more focused, constructive contribution. Comparable quality.
- The Attacker Moves Second (6.00, Reject) — meta-evaluation of defenses; received 6,2,8,8. Much larger empirical scope but methodological in nature. PromptArmor is less ambitious but also cleaner.
- Building a Foundational Guardrail (6.50, Accept Poster) — guardrail via synthetic data, training, and benchmark; received 8,6,6,6. More engineering-heavy contribution. PromptArmor's contribution is simpler but the message is more direct and general.
- A Guardrail for Safety Preservation (6.40, Accept Poster) — fine-tuning guardrail. Different approach.

**Final score reasoning:** PromptArmor is clearly stronger than SelfGrader (4.00, Reject) and SENTINEL (4.50, Reject). It is comparable to ChatInject (5.00, Accept Poster) and DiffuGuard (5.20, Accept Poster), but weaker than the Foundational Guardrail paper (6.50, Accept Poster) and The Attacker Moves Second (6.00, Reject in its own venue but with very high scores). The paper makes a clear, useful empirical contribution with strong results. The weaknesses are real but fixable and do not invalidate the central finding. A score of 5.5 reflects that this is a solid paper worth accepting, with useful practical implications, but not an exceptional or breakthrough contribution.

**Score:** 5.5 — Solid empirical contribution with a clear practical message. The paper convincingly shows that prior negative results on prompting-based defenses no longer hold with modern LLMs. The evidence supports the main claim. The paper has some real weaknesses (confounded baseline comparison, narrow adaptive evaluation, missing removal accuracy and cost data) but none are fatal. The contribution is practically useful and the paper is well-positioned within the literature.

**Decision:** Accept

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>