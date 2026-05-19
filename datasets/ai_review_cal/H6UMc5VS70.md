- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6
Now I have all the information needed. Let me produce the consolidated final review.

## Summary

This paper proposes FlipAttack, a black-box jailbreak attack that disguises harmful prompts by flipping their characters/words (four flipping modes) and then guides LLMs to reverse the flip and execute the harmful intent using a guidance module (four variants with CoT, role-playing, few-shot). The method requires only a single query to the victim LLM and achieves an average ASR of 81.80% across 8 LLMs (98.85% on GPT-4 Turbo, 98.08% on GPT-4o), outperforming the runner-up by 25.16 percentage points, while also achieving a 98.08% average bypass rate against 5 guard models.

## Strengths

- **High attack success rate with large improvement over baselines**: Table 1 shows FlipAttack achieves 81.80% average ASR across 8 LLMs, surpassing the runner-up (ReNeLLM, 56.64%) by 25.16 percentage points. This includes 98.85% on GPT-4 Turbo, 98.08% on GPT-4o, and 97.12% on Mixtral 8x22B.

- **Single-query efficiency with dramatically lower token cost**: Section 4.2 and Figure 4 demonstrate FlipAttack requires only 1 query to the victim LLM, while iterative methods like ReNeLLM consume 5,685 tokens per example. The bubble chart clearly shows FlipAttack in the optimal region (high ASR, low cost).

- **Stealthiness validated on multiple guard models**: Table 2 reports a 98.08% average bypass rate across 5 guard models (100% on OpenAI Moderation, 100% on LLaMA Guard 2 8B). Table 6 further shows flipped prompts have the highest perplexity (809.67) compared to other concealment methods (e.g., Caesar Cipher 258.10, ReNeLLM 15.56), supporting the claim that guard models are "unfamiliar" with flipped text.

- **Thorough ablation study confirming component contributions**: Figures 5–6 systematically ablate four flipping modes and four guidance module variants across all 8 LLMs. Key findings include: Vanilla alone achieves 98.08% on GPT-4 Turbo; CoT adds 16.92% on Claude 3.5 Sonnet; LangGPT boosts GPT-3.5 Turbo from 39.04% to 70.38%. This level of dissection gives strong empirical grounding to the design choices.

- **Empirical verification of flipping task feasibility**: Table 5 shows strong LLMs (GPT-4 Turbo, Claude 3.5 Sonnet) achieve >95% match rate on the flipping task, while weaker models improve substantially with few-shot (e.g., LLaMA 3.1 405B from 44.80% to 90.46%). This directly supports the claim that the flipping task is easy enough to be a practical attack mechanism.

## Weaknesses

### Fatal
None.

### Major

1. **Contribution 1 ("reveal LLMs' understanding mechanism") is substantially overclaimed.** The paper frames this as a key insight, but the supporting experiment (Table 3) merely shows that adding random noise to the left of a sentence produces higher perplexity than adding it to the right (avg. 815.93 vs. 477.09). This is a predictable consequence of autoregressive generation: left-side noise corrupts the conditioning context for every subsequent token. Calling this a "mechanism" discovery and comparing it to human reading ("like human beings," line 349) inflates what is a straightforward empirical observation. The attack itself does not depend on this being a deep insight, but including it as Contribution 1 weakens the paper's intellectual framing. **Impact**: The attack contribution is still strong, but the paper overstates its scientific contribution in this area.

2. **GPT-4 judge used for ASR on GPT-family targets, with no calibration.** The ASR evaluation uses GPT-4 as the judge (line 108, Table 1 caption). Five of the eight victim models belong to the same model family (GPT-3.5 Turbo, GPT-4 Turbo, GPT-4, GPT-4o, GPT-4o mini). GPT-based judges are known to exhibit leniency toward outputs from the same family. The paper provides no calibration — no human evaluation, no alternative judge (e.g., a non-GPT LLM or a rule-based system), and no correlation analysis. **Mitigating factor**: The results on non-GPT models (Claude 3.5 Sonnet 86.54%, Mixtral 8x22B 97.12%, LLaMA 3.1 405B 28.27%) provide strong independent support, so the core claim does not collapse. But the near-100% figures on GPT-4 Turbo (98.85%) and GPT-4o (98.08%) should be treated with caution until independently verified.

### Minor

3. **Defense strategy claims are stated without experimental support.** Section 3.3 ("Defense Strategy") asserts that SPD and PGF "are ineffective against FlipAttack" but provides no experimental setup, data, or analysis. Even in an attack-focused paper, making an unsupported claim about defense effectiveness weakens rigor. The section should either be removed or supported with even minimal evidence.

4. **Fool Model Mode (IV) is underspecified and its success mechanism is unclear.** The description (line 169) states: input "bmob a dliub ot woH" and ask the LLM to "flip word order." The paper never explains how this recovers the original prompt. The ablation (Figure 5) shows it largely fails without CoT but achieves moderate success with CoT on some models (~40% on Claude 3.5 Sonnet). The paper does not analyze how CoT turns an apparently incoherent instruction into a working attack. This mode exists in the paper but lacks a clear mechanism analysis.

### Trivial

5. **"Like human beings" anthropomorphism without evidence.** The paper claims LLMs "read and understand sentences from left to right like human beings" (line 349). No human experiments are conducted to support this comparison. The phrasing is unnecessary and detracts from the otherwise rigorous empirical presentation.

## Nice-to-Haves

- **Analyze the Physical Harm category failure.** The paper notes 69.55% ASR on physical harm (line 266) is substantially lower than other categories but does not analyze why. A brief analysis of whether flipping obscures safety-critical terms would strengthen the discussion.

- **Report variance or confidence intervals for main results.** Table 1 reports point estimates without variance. Given 16 methods × 8 models, some results may lie within noise. Adding confidence intervals would increase confidence in the reported gaps.

- **Clarify "1 query" for Variant D.** The paper correctly states 1 query to the victim LLM, but Variant D (few-shot) includes multiple example prompts within that single query, and the few-shot construction uses the harmful prompt itself, which could be detected. A brief clarification would prevent reader confusion.

## Removed Points

*These points were flagged by reviewers but are removed from the main evaluation after cross-checking against the paper.*

- **Criticism about "before noising, LLMs can easily understand 'bomb'" conflating character-level vs semantic-level confusion.** The paper's phrasing is about guard models recognizing harmful words, which is factually correct. This is a non-issue.
- **Criticism that "Why does FlipAttack Work?" is a summary, not an analysis.** This section explicitly references experimental evidence in Section 5.3; it is a framing section, not meant to be a standalone analysis.
- **Criticism about missing standard deviations in Table 1.** Single-run evaluation on large jailbreak benchmarks is standard in this subfield; requesting confidence intervals is a generic critique that does not follow the field's norms.
- **Criticism that "1 query" claim is overstated for Variant D.** The paper says 1 query to the victim LLM, which is correct. The adversary's own construction cost is irrelevant to the query-efficiency claim.
- **Criticism about deterministic prefix/suffix matching detection.** This is a speculative defense not tested by the reviewer; the paper's guard model bypass results already address detectability in practice.

## Novel Insights

The key insight that emerges from reading the reviewer inputs together is that the paper's strongest contribution is also its simplest: the finding that character-level and word-level flipping — the most trivial possible obfuscation — outperforms complex cipher-based (SelfCipher), coding-based (CodeChameleon), and iterative optimization (ReNeLLM) approaches. This suggests that LLM safety alignment is surprisingly brittle to input transformations they have simply never seen during training (flipped text has near-zero representation in training data, as the paper notes). The inversion is so easy for the LLM to reverse that the safety mechanisms simply do not engage. This tells us something about the generalization boundaries of RLHF-based alignment: it generalizes poorly to even simple distribution shifts in input format. The paper's own "understanding pattern" framing obscures this more interesting point; the real story is about out-of-distribution brittleness of safety training, not left-to-right comprehension.

## Suggestions

1. **Reframe Contribution 1 honestly.** Drop the "reveal understanding mechanism" language. Replace it with: "We empirically verify that autoregressive LLMs are more sensitive to left-side than right-side perturbations — a property we exploit for attack design." This is defensible and avoids overclaiming.

2. **Calibrate the GPT-4 judge.** Run a human evaluation on a random 100-example subset, or use an independent non-GPT judge (e.g., Mixtral-based evaluation or keyword+LLM hybrid) to verify ASR on GPT-family targets. Report the correlation between judges.

3. **Either remove or support the defense section.** The two-sentence claim about SPD and PGF being ineffective adds nothing. Either delete the subsection entirely, or provide minimal experimental evidence (e.g., "FlipAttack achieved X% ASR under SPD/PGF").

4. **Explain Mode IV's mechanism or remove it.** A concrete example showing the complete chain from flipped input → LLM processing → recovered original → harmful output would clarify whether this mode has a coherent recovery path.
