Now I have all the information needed. Let me synthesize the review.

---

## Summary

This paper presents a comprehensive empirical study of rule-based and model-based verifiers in reinforcement learning for mathematical reasoning. The authors first show that rule-based verifiers suffer from significant false-negative rates (recall as low as 78%) that worsen as policy models become stronger. They then investigate model-based verifiers, finding that while they improve recall in static evaluation, generative verifiers are highly vulnerable to reward hacking during RL training — a fine-tuned verifier (R1-Distill-Verifier-1.5B) leads to training reward divergence and eventual collapse. A systematic probing study with 13 distinct attack patterns reveals that all generative verifiers, regardless of fine-tuning, are easily fooled, while discriminative verifiers (xVerify) remain robust. A hybrid verifier (rule-based first, model-based for edge cases) yields a consistent +2.3 point improvement in RL training.

## Strengths

- **Recall degradation with stronger policy models (Figure 2) is a compelling and actionable finding.** As generation models become more capable, rule-based verifiers struggle increasingly to recognize correct answers — an insight with direct practical implications for the RLVR community.

- **The systematic probing study (Section 6) is the paper's strongest contribution.** Constructing 13 distinct hacking patterns and evaluating attack success rates across a broad set of verifiers provides concrete, mechanistic evidence that generative verifiers are fundamentally brittle. The finding that discriminative verifiers (xVerify) are robust while all generative verifiers are vulnerable makes a clear, actionable distinction that the field should internalize.

- **Clear separation of static evaluation accuracy from dynamic RL robustness.** The paper demonstrates that a verifier with higher static recall (R1-Distill-Verifier-1.5B: 0.62 vs. 0.49 for its base) can perform worse in RL due to reward hacking. This is a non-obvious insight that challenges the natural assumption that better static accuracy translates to better RL training.

- **Well-constructed evaluation infrastructure.** The 8,000-example dataset annotated by GPT-4o with Cohen's κ = 0.933 against human judgments provides a trustworthy foundation. The use of GPT-4o as an oracle reward signal during RL training is a practical and well-justified design choice.

- **Cross-domain generalization (Appendix J).** The findings are replicated on WebInstruct-Verified (general science), showing that the verifier challenges are not confined to math, with rule-based recall dropping below 0.6 and reward hacking persisting.

## Weaknesses

### Fatal

None.

### Major

None. The core empirical findings are well-supported by the evidence presented.

### Minor

- **The causal link between fine-tuning and hacking susceptibility is overstated relative to the evidence.** The paper claims that "verifiers trained on labeled classification data ... are more susceptible to hacking" (Section 5.2). However, the evidence is mixed: R1-Distill-Verifier-1.5B (fine-tuned, generative) hacks in RL, but general-verifier (also fine-tuned, also generative) does not. Meanwhile, the probing study (Section 6) shows that *all* generative verifiers — including untuned ones — are vulnerable. The probing study further shows R1-Distill-Verifier-1.5B's vulnerability increases over its base model for some attack types (adversarial prefixes: 21.7 → 35), which does support some effect of fine-tuning. But the core generalization conflates two separable effects: (a) generative architecture is inherently vulnerable and (b) fine-tuning can amplify certain vulnerabilities. The paper would be stronger by clearly separating these two claims and acknowledging that the RL evidence for (b) rests on a single comparison.

- **The RL improvement from the hybrid verifier is attributed entirely to higher recall without controlling for other confounds.** Switching from a purely rule-based to a hybrid verifier changes more than recall — it alters the reward distribution, possible biases, and response formatting incentives. A control experiment (e.g., relaxing rule-based matching to achieve similar recall without changing verifier type) would strengthen the causal attribution. This does not undermine the practical value of the hybrid verifier finding, but the paper overstates the mechanism.

### Trivial

- **The abstract's recall claim could mislead readers unfamiliar with the hybrid design.** "Improving the recall rate from 84% to 92% on the Skywork-OR1 dataset" (abstract, line 69-70) refers to the *hybrid system's* recall, not the model-based verifier's standalone recall. The body of the paper clarifies this (Section 3.3 explicitly states the evaluation is on the FN subset), but the abstract is ambiguous. A brief qualifier in the abstract would prevent misinterpretation.

- The paper would benefit from a more explicit discussion of why general-verifier does not exhibit reward hacking in RL despite being fine-tuned and generative, given the probing results show it has high attack success rates (e.g., 22.1 on adversarial prefixes).

## Nice-to-Haves

- **RL experiment with xVerify (discriminative verifier).** Since the probing study shows discriminative verifiers are far more robust, running one in RL would test whether probing robustness translates to training stability.

- **Recall-only ablation.** An experiment where the rule-based verifier's matching rules are relaxed to achieve similar recall as the hybrid system would isolate the effect of recall from other properties of model-based verification. This would strengthen the paper's mechanistic claims but is not essential for its main contributions.

- **Analysis of why generative verifiers are specifically vulnerable.** The paper mentions CoT faithfulness briefly; a deeper investigation of how attack patterns corrupt reasoning traces would enrich the probing study's contribution.

## Removed Points

These points are flagged to be removed. Treat with caution.

- **Harsh Critic Point 1 (inadequately supported fine-tuning claim):** Partially kept as a minor weakness (see above), but the claim that the evidence is wholly "inadequate" is too strong. The paper qualifies its claim with "some" and the probing study provides additional evidence (R1-Distill-Verifier-1.5B's vulnerability increases over its base model). The core observation — that fine-tuned verifiers can be more vulnerable despite better static accuracy — is valid and supported.

- **Harsh Critic Point 2 (biased subset evaluation):** The paper explicitly explains this design choice in Section 3.3 ("we focus here exclusively on the examples that rule-based verifiers classify as incorrect"). It also reports full-set metrics in Table 5 (Appendix F). The abstract phrasing is slightly ambiguous but the body resolves it. This is primarily a presentation issue.

- **Harsh Critic Point 3 (RL improvement conflated with recall):** Partially kept as a minor weakness for the overstatement of mechanism, but the core practical finding (hybrid verifier improves RL) does not require a mechanistic decomposition to be valuable. The confound is real but does not threaten the paper's contribution.

- **Strength Finder point about "rigorous static evaluation dataset construction with GPT-4o and human validation":** Kept as a strength (reworded). Valid and concrete.

- **Strength Finder point about "generalization of findings to general-science domain":** Kept as a strength. Valid.

- **All formatting/spelling/typo criticisms from Harsh Critic:** Removed per hard rules — these are parser artifacts, not author errors.

- **Harsh Critic "Missing Experiments" section (xVerify RL, recall-only ablation, replicate fine-tuning recipe):** Moved to Nice-to-Haves. These would strengthen the paper but are not necessary for its core claims.

- **Harsh Critic "Deeper Analysis Needed" about CoT faithfulness:** Moved to Nice-to-Haves. Interesting but outside the paper's stated scope.

## Novel Insights

The most genuinely novel insight emerging from this work is the **decoupling of static verification accuracy from RL robustness**. The paper shows that a verifier can simultaneously have higher static recall and worse RL outcomes due to reward hacking — and conversely, that a verifier (DS-R1-Distill-Qwen-1.5B) can be highly vulnerable in probing attacks yet safe in RL because the policy model is not strong enough to exploit it. This two-way asymmetry is not obvious and has real implications for how the field should evaluate verifiers: neither static accuracy nor probing vulnerability alone predicts RL behavior. A second insight is that the vulnerability of generative verifiers appears to stem from their CoT reasoning process, where adversarial prefixes and answer explanations disrupt the reasoning chain, while discriminative verifiers bypass this attack surface entirely.

## Suggestions

- Revise the claim about fine-tuning increasing hacking susceptibility to be more precise: the evidence supports that fine-tuning *can amplify* certain attack vulnerabilities (as shown in probing) but does not universally cause RL hacking (general-verifier counterexample). Frame this as a risk rather than a causal law.
- Add a sentence to the abstract clarifying that the "84% to 92%" recall improvement is for the hybrid system, not a standalone model-based verifier.
- Include a brief discussion of why general-verifier avoids reward hacking in RL despite its probing vulnerabilities, even if speculative. The current asymmetry is striking and readers will notice it.
- Consider adding the recall-only ablation (relaxed rule-based matching) as a control, or at minimum acknowledge this confound explicitly in the limitations.

---

## Score Calibration

Here are the anchor papers retrieved, with comparison notes:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| **VerifyBench** (JfsjGmuFxz) | 5.50 (Accept Poster) | Benchmark paper for reference-based reward systems. Similar topic relevance. Our paper has more diverse experiments (RL training, probing, cross-domain) and offers more actionable insights into verifier behavior. |
| **RLVR Implicitly Incentivizes** (jGbRWwIidy) | 5.33 (Accept Poster) | Empirical+theoretical analysis of RLVR. Similar paper type (analysis). Our paper has broader experimental scope and more clearly novel findings. |
| **HERO** (0CajQNVKyB) | 6.00 (Accept Poster) | Method paper with strong results, comprehensive ablations. Different contribution type but comparable execution quality. Our paper is comparably well-executed. |
| **The Invisible Leash** (qGhFl1SiPX) | 5.00 (Reject) | Analysis of RLVR limitations. Mixed reviews due to novelty concerns and confounded experiments. Our paper has cleaner experimental design and more actionable findings. |
| **Proof-Verifier** (FAe9Gts2Qd) | 4.50 (Reject) | Generative verifier for theorem proving. Weak RL validation, limited comparisons. Our paper's RL experiments are more thorough and the findings more conclusive. |
| **DeepScaleR** (I6GzDCne7U) | 4.00 (Reject) | Training recipe paper. Limited novelty and scale concerns. Our paper is substantially more comprehensive and novel. |
| **Curing Miracle Steps** (FGkknrhv09) | 3.00 (Withdrawn) | Methodology paper with missing baselines and confounded experiments. Our paper's experimental rigor is significantly higher. |

This paper is most comparable to the "RLVR Implicitly Incentivizes" (5.33) and "VerifyBench" (5.50) papers in topic and execution quality, but offers more comprehensive experiments and clearer practical takeaways. It is roughly at the level of HERO (6.00) in terms of experimental thoroughness and clarity. I recommend a score of **6.0** with an Accept (Poster) decision. The weaknesses (overstated fine-tuning claim, recall-only confound) are minor and addressable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>