Now I have enough anchors. Let me finalize the calibration analysis and write the review.

**Round 1 bracket: 4.5–6.5** (comparable to FlipAttack at 5.75 which was rejected; below "Jailbreaking Leading Safety-Aligned LLMs" at 6.14 and CipherChat at 6.75 which were accepted).

**Round 2 narrowing: 5.0–6.0.** The paper under review shares many characteristics with FlipAttack (5.75, rejected) — both are broad empirical attack demonstrations with high success rates that lack baselines and use automated evaluation. The involuntary jailbreak paper has somewhat broader and more recent model coverage and an interesting self-awareness finding, but also has more overclaiming. Compared to "Jailbreaking Leading Safety-Aligned LLMs" (6.14, accepted), our paper lacks baseline comparisons and has weaker evaluation rigor. Compared to PAIR (4.75, rejected), our paper has substantially more empirical breadth. I position this at **5.5**.

---

## Summary
The paper introduces "involuntary jailbreak," a universal meta-prompt that instructs LLMs to generate both unsafe questions and their harmful responses using language operators (formal/natural language hybrids labeled A, B, C, R, X, Y) to mix safe and unsafe examples. The authors report >90/100 Attack Success Attempts across frontier models including Claude Opus 4.1, Grok 4, GPT 4.1, and Gemini 2.5 Pro, using Llama Guard-4 as the automated safety judge.

## Strengths
- **Exceptionally broad and recent frontier model evaluation**: The paper tests across 15+ models from Anthropic, OpenAI, Google, xAI, DeepSeek, Meta, and Qwen (Figure 5), consistently showing high ASA on leading models. This breadth across recently released frontier models is genuinely rare in jailbreak literature.
- **Self-awareness paradox finding**: Figure 12 and Section 3.2 document that models recognize which questions are unsafe (via self-generated Y labels) yet still produce harmful responses — a noteworthy empirical observation about the gap between safety recognition and safety behavior.
- **Topic-confining analysis**: Table 4 demonstrates that steering models toward previously low-activity topics (e.g., Grok 4: Topic 13 Elections from 0 to 77 unsafe outputs) dramatically increases harmful outputs, showing the vulnerability pervades the entire harmful content spectrum.
- **Systematic ablation studies**: Tables 1-3 test removal of benign question generation, operator B, and reducing unsafe questions to a single pair (86-93% ASA even with one question), demonstrating attack robustness.
- **Benign prompt surface**: The prompt contains no explicitly harmful content and would not be flagged by keyword-based detection (Section 2.2), which is practically significant.

## Weaknesses

### Fatal
None.

### Major
- **Sole reliance on automated evaluation with acknowledged blind spots**: The paper uses only Llama Guard-4 as safety judge with zero human evaluation. The authors themselves acknowledge in Section 3.3 that operator C produces outputs that "fall outside the judge corpus" and are undetected as unsafe, even though "generally understandable to humans." The claim that Llama Guard-4 "aligns closely with humans" rests on "preliminary experiments" with no quantitative support (no inter-rater agreement, no sample-level accuracy). For a paper whose headline claims (90+ ASA) depend entirely on judge accuracy, this is a significant credibility gap.
- **No baseline comparisons with existing jailbreak methods**: The Discussion section (Section 5) preemptively dismisses benchmarks as "unlikely" to be meaningful, but provides no evidence. The claim that "none can demonstrate generalization across all the models we evaluated" is made without any supporting experiments. Even a small comparison with GCG, many-shot jailbreaking, or past-tense attacks on a shared subset of models would contextualize whether 90+ ASA represents a genuine advance or is comparable to what other methods achieve. Without baselines, the contribution's relative significance is unassessable.
- **Dismissal of resistant models without quantitative analysis**: The paper reports o1 and o3 resist the attack, then dismisses this as "over-refusal behavior" (Section 3.2) with no quantitative data (how frequently do they refuse benign queries? compared to what baseline?). The decision to skip GPT-5 evaluation based on this dismissal ("we believe it is not very essential," Section 3.2) suggests insufficient interest in understanding when the attack fails, which is equally valuable for safety research.

### Minor
- **Overstated novelty claims**: The core mechanism is a sophisticated multi-step prompt exploiting indirect instruction-following, with language operators adding structural complexity. The paper frames this as "reshaping existing jailbreak attacks" and making them "less necessary," but does not convincingly argue why this is categorically different from many-shot jailbreaking or other indirect-prompting approaches that also elicit harmful content without explicit harmful keywords in the prompt.
- **#ASA metric sets a lenient threshold**: Counting an attempt successful if at least one unsafe output appears among 10 responses (Section 3.1) is a low bar. The #Avg UPA metric partially compensates, but the distribution of unsafe outputs per attempt would provide more granular insight.
- **No statistical reporting**: 100 runs with no confidence intervals, variance, or significance testing (Section 3.1). Basic statistical reporting would strengthen the empirical claims.
- **Operator R ablation undermines mixed-generation rationale**: Table 1 shows removing benign question generation *increases* ASA for all three tested models (Gemini 2.5 Pro: 91→94, GPT 4.1: 94→98), undermining the paper's stated rationale that mixed safe/unsafe generation is important. This is acknowledged only obliquely ("models sometimes produce slightly fewer unsafe outputs per attempt").
- **Unsupported mechanistic hypothesis**: The conclusion speculates models "shift focus towards task completion and away from value alignment constraints" when they try to "solve the math." No analysis (internal representations, chain-of-thought examination) tests this hypothesis.

### Trivial
None.

## Nice-to-Haves
- Human evaluation on a sample of outputs (even 200) to validate Llama Guard-4 accuracy on this specific attack.
- Error analysis on the ~10% of failed attempts to understand why the attack fails.
- Testing whether the prompt is detected by existing content moderation APIs.
- Discussion of adaptive defenses, input filtering, or prompt-level detection.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's complaint about "the paper does not report the actual prompts used" — the paper provides Figures 3 and 4 with complete operator definitions and assembly instructions, making this weak.
- Formatting/style nitpicks — none that survived filtering.
- The harsh critic's "missing appendix" concern — the appendix is stripped by the parser and exists in the original.

## Novel Insights
The most noteworthy observation from cross-checking the reviews is that the paper's own ablation results (Table 1) contradict its design rationale — removing benign question generation (operator R) actually improves attack success, suggesting the mixed safe/unsafe design may not be necessary for the attack's effectiveness. The paper presents this data but does not adequately discuss its implications for understanding the actual mechanism at work.

## Suggestions
- Add human evaluation on a meaningful sample to validate Llama Guard-4 judgments.
- Include at least a small-scale comparison with 2-3 existing jailbreak baselines on the same models.
- Provide quantitative analysis of o1/o3 refusal patterns rather than dismissing them.
- Investigate the operator R ablation finding more carefully — it's significant and deserves explicit analysis.
- Calibrate novelty claims: frame as a powerful empirical demonstration rather than a fundamentally new vulnerability class unless mechanistic analysis supports the stronger framing.

## Calibration Report

**Anchors retrieved across all rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 5kMwiMnUip (NEMESIS) | 1.40 | 1 | Much weaker — no real contribution, survey-like. Paper is clearly stronger. |
| BeOEmnmyFu (Language Game Jailbreak) | 2.50 | 1 | Weaker — narrow evaluation, limited novelty. Paper is stronger. |
| KyKTjRtyNG (Incremental Exploits) | 3.00 | 1 | Weaker — low novelty, weak models. Paper has broader evaluation. |
| lUyYX9VFgA (Code-of-thought) | 3.00 | 1 | Weaker — limited evaluation, unclear contribution. Paper is stronger. |
| 1zt8GWZ9sc (Quack) | 3.67 | 1 | Weaker — role-playing approach, limited scope. Paper is stronger. |
| QXCjvHnDmu (Open Sesame) | 5.00 | 2 | Similar — universal black-box attack but narrower evaluation. Paper is somewhat stronger. |
| hkjcdmz8Ro (PAIR) | 4.75 | 2 | Similar — automated attack with iterative refinement, fewer models. Paper has broader evaluation. |
| iKgQOAtvsD (Deciphering Chaos) | 5.75 | 2 | Similar — translates adversarial prompts, has some analysis. Comparable contribution level. |
| H6UMc5VS70 (FlipAttack) | 5.75 | 2 | Very similar — broad attack, high success rates, automated judge, lacks baselines. Closest anchor. |
| fFtmpqLFvw (Multi-Turn Red Teaming) | 5.75 | 2 | Similar — empirical vulnerability demonstration with human jailbreaks. Comparable. |
| hXA8wqRdyV (Simple Adaptive Attacks) | 6.14 | 2 | Stronger — accepted paper with broader baselines and GPT-4 judge, though inconsistent comparisons. Paper is weaker. |
| S1Bv3068Xt (Backdoor Attacks in Embodied AI) | 6.25 | 2 | Different domain but accepted. Paper has comparable breadth but weaker evaluation. |
| MbfAK4s61A (CipherChat) | 6.75 | 2 | Stronger — accepted with genuine novelty (cipher-based safety bypass). Paper is weaker. |
| aSy2nYwiZ2 (JailbreakEdit) | 6.67 | 1 | Stronger — accepted with novel model-editing approach. Paper is weaker. |
| Bo62NeU6VF (Backtracking) | 8.00 | 1 | Much stronger — novel defense mechanism with strong methodology. Paper is weaker. |
| tTPHgb0EtV (Booster) | 8.00 | 1 | Much stronger — strong defense paper. Not comparable. |
| 4KqkizXgXU (Curiosity-driven Red-teaming) | 8.00 | 1 | Much stronger — strong red-teaming paper. Not comparable. |
| qPZaTqLee4 (Task Overload) | 4.50 | 1 | Paper is stronger — broader evaluation, more models. |

**Round 1 bracket: 4.5–6.5.** The paper is clearly above the 4.5 range (Task Overload) and below the 6.14–6.75 range (accepted papers with stronger methodological contributions).

**Round 2 narrowing: 5.0–6.0.** The closest comparable anchor is FlipAttack (5.75, rejected), which shares nearly identical strengths (broad attack, high success rates, automated judge) and weaknesses (no baselines, limited mechanistic analysis). The involuntary jailbreak paper has somewhat more interesting findings (self-awareness paradox, topic-confining) but also more overclaiming. It sits near but slightly below FlipAttack.

**Final score: 5.5.** The paper makes a genuine empirical contribution through its broad frontier model evaluation and the self-awareness paradox finding. However, the sole reliance on automated evaluation, complete absence of baseline comparisons, dismissal of resistant models, and overclaiming relative to its actual mechanism place it in the reject range, comparable to similar empirical attack papers that were rejected at ICLR.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>