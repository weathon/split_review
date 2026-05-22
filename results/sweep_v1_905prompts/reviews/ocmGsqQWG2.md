## Summary

This paper identifies a new vulnerability in LLMs called "involuntary jailbreak": a single universal meta-prompt that instructs the model to generate its own refusal-worthy questions and then produce detailed unsafe responses. The attack is untargeted (models autonomously generate the harmful content breadth) and achieves #ASA ≥ 90/100 on Claude Opus 4.1, Grok 4, Gemini 2.5 Pro, and GPT-4.1. The paper also shows that models often label their self-generated questions as unsafe yet still answer them, and that topic confinement can steer the attack toward specific harm categories.

## Strengths

- **Novel untargeted attack that works across frontier proprietary models.** The attack concept—a meta-prompt that makes the LLM generate its own unsafe questions and responses without providing any explicit harmful content in the prompt—is genuinely different from prior targeted jailbreaks. The results show #ASA ≥ 90 out of 100 for Claude Opus 4.1, Grok 4, Gemini 2.5 Pro, and GPT-4.1 (Fig. 5), covering a broader set of frontier models than most existing jailbreak evaluations.

- **Topic coverage and confinement analysis.** Fig. 6 demonstrates that the attack spans all 14 Llama Guard-4 safety categories, and Table 4 shows that explicit topic steering can force high unsafe output counts even on topics where the models initially produce zero (e.g., Grok 4 on Elections goes from 0 to 77 unsafe outputs out of 94 generations). This proves the attack is not limited to a narrow harm band.

- **Ablation identifies operator necessity.** Tables 1 and 2 show that removing operators B or R reduces effectiveness for some models (e.g., Gemini 2.5-flash-lite #ASA drops from 100 to 83 without operator B). Table 3 confirms that even a single unsafe question generation suffices for high success rates, isolating the mechanism.

- **Weaker models fail due to limited instruction-following, not stronger guardrails.** The paper explicitly documents that GPT-4.1-mini, Llama 3.3-70B, and DeepSeek R1-Distilled-Llama-70B cannot generate unsafe outputs because they cannot follow the complex meta-prompt (§3.2). This strengthens the claim that the vulnerability exploits advanced instruction-following capability rather than representing a generic alignment failure.

## Weaknesses

### Major

- **No comparison to any existing jailbreak method.** The paper provides zero baselines—not even a minimal prompt baseline (e.g., "generate 10 harmful questions and their detailed answers" without the operator scaffolding). This undermines the strongest claim in the abstract ("makes existing jailbreak attacks seem less necessary"). The Discussion (§5) argues that no meaningful benchmark exists and that existing methods cannot generalize, but these claims are unverified: the paper itself does not demonstrate that its method generalizes where others would fail. Without any comparison, the reader cannot assess whether the attack is meaningfully distinct from, say, a simpler "just answer these" instruction.

- **The "involuntary" framing exceeds the evidence.** The core evidence for involuntariness is that models output "Y(X(input)) = Yes" (labeling the question as unsafe) while simultaneously generating the harmful X(input). However, the prompt explicitly instructs the model to output Y(X(input)) = Yes for unsafe questions. The model is therefore following the instructed output structure, not independently "confessing" that it knows it is violating its safety rules. The paper claims (line 288) that Fig. 12 shows "the number of unsafe responses corresponds closely with the number of questions LLMs internally label as unsafe," but without access to the model's internal representations or reasoning (the evidence is the Y label the prompt instructed the model to produce), the "involuntary" characterization remains suggestive rather than established.

### Minor

- **Single automated judge without validation data.** All evaluations use Llama Guard-4 as the sole safety judge. The paper notes (§3.1) that "preliminary experiments" showed alignment with human and GPT-4.1 judgments, but presents no data, sample size, or agreement statistics. If Llama Guard-4 has systematic biases on this specific attack's outputs, the reported numbers could shift.

- **No variance or confidence intervals.** Results are reported as point estimates over 100 attempts without standard deviations, confidence intervals, or per-attempt breakdowns. Given the binary nature of #ASA and the count nature of #Avg UPA, reporting variance would allow readers to assess the stability of the reported rankings.

- **Primary metric (#ASA) is lenient.** #ASA counts an attempt as successful if at least 1 of 10 outputs is unsafe. The paper does report #Avg UPA, which is reassuring (mostly 6–10), but the headline metric can mask cases where most outputs are safe. A stricter threshold (e.g., majority unsafe) would strengthen the results.

- **Ablation is limited to operators B and R.** Operator C is discussed only qualitatively (it degrades readability, §3.3). Operator A is stated as "cannot be ablated" without justification. A more systematic ablation testing each operator's contribution jointly would strengthen the attribution of the attack's effectiveness to specific prompt components.

### Trivial

- Fig. 5's axis labels are garbled in the extracted text (refers to "#ASA" as "number of samples used for training" and "#Avg UPA" as "LUPA score"), likely a rendering artifact.

## Nice-to-Haves

- A small human evaluation (e.g., 50–100 outputs) to validate Llama Guard-4 agreement.
- A minimal-prompt baseline: strip the operators and simply ask the model to generate harmful questions and answers, to isolate the operators' contribution.
- A deeper exploration of why the attack works—e.g., analyzing whether the multi-step operator structure shifts attention from safety to task-completion as hypothesized in §6.

## Removed Points

- *Formatting/style nitpicks* (epigraph being "unsubstantiated," minor phrasing issues): Removed per style rule.
- *Criticism about missing appendix content*: Removed; appendix is stripped by the parser and exists in the original submission.
- *Criticism that the paper "does not explore why the attack works"*: Removed; the paper proposes a reasonable hypothesis (operators shifting focus toward task completion) in §6, so this criticism overstates the gap.
- *Strength about "involuntary" evidence being strong*: Downgraded; the evidence is weaker than claimed due to the Y(X) label being part of the instructed output structure.
- *Request for comparison to specific baseline methods*: Downgraded to Nice-to-Have; not having baselines is a major weakness, but demanding adaptation of specific methods (GCG, PAIR) is a suggestion, not a minimum requirement.

## Novel Insights

The most genuinely novel observation that emerges from this paper—beyond its own contributions—is that the attack seems to exploit the *strength* of instruction-following in frontier models: the better a model is at following complex, multi-step instructions, the more vulnerable it is. This inverts the usual assumption that stronger capabilities imply stronger safety. The paper's observation that weaker models (Llama 3.3-70B, GPT-4.1-mini) fail because they *cannot follow the instructions* rather than because they *refuse the content* suggests a fundamental tension: the same capability that makes these models useful (faithful execution of complex directives) also makes them exploitable when safety and instruction-following misalign. This tension deserves more investigation than the paper currently provides.

## Suggestions

1. Add at least one baseline: a stripped-down prompt that removes all operator scaffolding but keeps the core "generate unsafe questions and answer them" instruction. If the operators contribute meaningfully, the stripped version should show lower success rates; if not, the narrative changes but the result remains interesting.
2. Provide validation evidence for Llama Guard-4 on a held-out sample (inter-annotator agreement with a second judge or human raters).
3. Report per-attempt variance (standard deviation or IQR) for #Avg UPA across the 100 runs.
4. Tone down claims in the abstract ("makes existing jailbreak attacks seem less necessary") to match the evidence level, or add the necessary baselines to support them.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 5kMwiMnUip (NEMESIS) | 1.40 | R1-low | Much weaker paper; no novel attack, rejected |
| BeOEmnmyFu (Playing Language Game) | 2.50 | R1-low | Weaker; narrow scope, limited model coverage |
| KyKTjRtyNG (Incremental Exploits) | 3.00 | R1-low | Weaker; conventional multi-round approach |
| lUyYX9VFgA (Code-of-thought Prompting) | 3.00 | R1-low | Weaker; limited results |
| 1zt8GWZ9sc (Quack) | 3.67 | R1-mid | Weaker; role-playing approach on smaller models |
| QXCjvHnDmu (Open Sesame) | 5.00 | R1-mid | Comparable on idea, but tests only small open-source models (Llama-7B). Current paper tests frontier models. |
| hXA8wqRdyV (Simple Adaptive Attacks) | 6.14 | R1-mid | Stronger evaluation (baselines, model range, judge validation); accepted at NeurIPS |
| sULAwlAWc1 (One Model Transfer) | 7.00 | R1-mid | Stronger; comprehensive baselines and defense evaluation |
| 6Mxhg9PtDE (Shallow Safety Alignment) | 9.50 | R1-high | Much stronger; theoretical insight + rigorous experiments |
| Bo62NeU6VF (Backtracking) | 8.00 | R1-high | Much stronger; well-evaluated defense method |

**Round 2 — Narrowing**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| zf53vmj6k4 (Political Correctness) | 4.25 | R2-low | Comparable in evaluation rigor issues (no baselines, no variance), but current paper's attack is more broadly effective |
| hkjcdmz8Ro (PAIR) | 4.75 | R2-low | Comparable; PAIR is more automated but targets smaller models |
| e9yfCY7Q3U (I-GCG) | 6.25 | R2-mid | Stronger; has baselines, comprehensive evaluation, accepted |
| aSy2nYwi2Z (JailbreakEdit) | 6.67 | R2-mid | Stronger; thorough evaluation and ablations |

**Initial bracket**: Between ~4 and ~6. The paper's novelty (untargeted meta-prompt attack on frontier models) is genuinely above the ~3.5 rejected papers, but the evaluation gaps (no baselines, single judge, no error bars) prevent it from reaching the ~6+ level of accepted papers.

**Narrowing**: Compared to the round-2 anchors, the paper is stronger than the "Political Correctness" (4.25) and PAIR (4.75) papers because its core finding is more novel and broadly applicable. However, it is clearly weaker than I-GCG (6.25) and JailbreakEdit (6.67), which have comprehensive baselines, variance reporting, and multi-judge or human validation. The paper sits between these bands—stronger idea but weaker evaluation.

**Final score**: 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>