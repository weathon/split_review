Now I have verified all claims against the paper. Let me write the final consolidated review.

---

## Summary

This paper proposes "chat vector"—the weight difference between LLaMA2-chat and LLaMA2—added to a continually pre-trained (CP) model in a target language, as a computationally cheaper alternative to the full CP→SFT→RLHF pipeline for non-English LLMs. Experiments across Traditional Chinese, Korean, and Simplified Chinese evaluate instruction following, toxicity, and safety. The core idea is simple and practically motivated, and the paper documents both promising results and notable limitations.

## Strengths

- **Simple, efficient method for transferring chat/alignment capabilities.** The chat vector approach replaces the expensive CP→SFT→RLHF pipeline with CP followed by a single vector addition. This efficiency gain is clearly motivated (Section 3.2, Figure 1), and the empirical results (Tables 1–3) show that the chat vector consistently improves instruction following, reduces toxicity, and enhances safety relative to CP-only and CP→FT baselines, across three target languages.

- **Multi-aspect evaluation across three dimensions and three languages.** The paper evaluates instruction following (Vicuna benchmark, GPT-4 scoring), toxicity (Real Toxicity Prompts, Perspective API), and safety (Safety Prompts) for Traditional Chinese, Korean, and Simplified Chinese models. The results in Tables 1–3 are broadly consistent: chat-vector-augmented models outperform their non-chat counterparts across most settings.

- **Honest documentation of limitations, including the language-fidelity issue.** Section 5.5 transparently reports that the full-magnitude chat vector can cause English responses when applied to Chinese-LLaMA (which has stronger English capabilities), and that a half-magnitude scaling partially mitigates this. This candor is a strength, even though the issue itself is a weakness.

- **Useful negative result about LLaMA2-chat forgetting after CP.** Section 5.1 (observation 4) shows that taking LLaMA2-chat and continually pre-training it on Chinese causes loss of chat capabilities. This empirically validates that the chat vector's design—adding the vector *after* CP to a non-chat base—avoids this washout. This is arguably the strongest empirical finding.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed contribution contradicted by empirical results (target-language fidelity).** The paper lists as a contribution (line 23): "We find that the resultant model responds precisely in the target language." However, Section 5.5 (Table 4) shows that applying the chat vector at full magnitude to Chinese-LLaMA produces a "high proportion of English responses" on both Vicuna and Safety Prompts. The half-magnitude workaround (coefficient 0.5) mitigates this for the FT+chat-vector pipeline but degrades capability for the CP+chat-vector pipeline (lines 209-210). No principled method is given for choosing the coefficient, and it is applied differently across models without justification. This does not invalidate the core idea (the method works for the authors' own Traditional Chinese CP model and for Korean LLaMA), but it means one of the four stated contributions is not supported by the evidence, and the practical recommendation for practitioners is incomplete.

2. **No comparison against any model that underwent RLHF in the target language.** The paper frames chat vector as an efficient alternative to full RLHF, and the main advantage is efficiency. However, none of the baselines include a model that actually underwent RLHF in the target language. The reader consequently cannot calibrate how much capability is sacrificed by skipping RLHF. Without this comparison, the "efficiency vs. capability" tradeoff is unquantified, and the central claim that the method is "competitive" (in any absolute sense) is unsupported. Including even a small-scale RLHF baseline trained on the same CP base would substantially strengthen the paper.

3. **Heavy evaluation reliance on GPT-4 creates a compounding bias.** The evaluation chain uses GPT-4 in three overlapping roles: (a) to translate the Vicuna and Real Toxicity Prompts benchmarks into Chinese/Korean (lines 113-116), (b) to provide gold-standard answers (treated as 10-point ground truth, line 124), and (c) to score model responses via GPT-4-as-judge (line 124). This creates a closed loop where GPT-4-centric response styles are implicitly rewarded. Since LLaMA2-chat (from which the chat vector derives) was trained partly on GPT-4-generated data, models augmented with the chat vector may benefit from this circularity in ways that are hard to disentangle. While GPT-4-as-judge is standard practice, the triple role of GPT-4 in this particular setup goes beyond what is typical and weakens the independence of the quantitative results.

### Minor

1. **Multi-turn dialogue evaluation rests on a single case study (Figure 2).** No quantitative evaluation of multi-turn conversation is provided. A single anecdote in Figure 2 does not constitute sufficient evidence for the claim that "integrating chat vectors empowers models with multi-turn conversation abilities."

2. **Korean experiments are presented only in aggregate in Table 1, with limited detail.** The Korean experiments use 7B models (vs. 13B for Chinese) with different fine-tuning data sources, and the only reported results are in the aggregated Table 1. No separate language-specific analysis, toxicity results, or safety evaluation for Korean is provided. This weakens the cross-lingual generality claim.

3. **No systematic investigation of the scaling coefficient.** The paper acknowledges (line 186) that "the method to obtain the optimal coefficient of the chat vector requires further research" and that magnitude "could severely affect the performance." However, only two values (1.0 and 0.5) are tested, on only one model (Chinese-LLaMA), without showing the tradeoff curve or analyzing why the coefficient interacts differently with CP vs. CP+FT models. This is a gap that limits the practical applicability of the method.

4. **No analysis of what the chat vector encodes mechanistically.** A simple ablation—e.g., applying the chat vector to only the first half, last half, or specific layer groups—could clarify which components (attention, feed-forward, embeddings) carry the chat capability. Such analysis would strengthen the paper's contribution to understanding weight-space arithmetic.

### Trivial
- None.

## Nice-to-Haves

- A comparison against at least one small-scale RLHF baseline (e.g., training a reward model and running PPO on the same CP model for a limited budget) to calibrate the capability-efficiency tradeoff.
- Reporting the scaling coefficient sweep (e.g., 0.25, 0.5, 0.75, 1.0) for at least one model to show the language-fidelity vs. capability tradeoff systematically.
- Layer-wise ablation of the chat vector to understand which layers carry the instruction-following and safety signals.

## Removed Points

These points from the reviewers are excluded or downgraded per the verification rules:

- **"No release of models or code"** (Harsh Critic's Missing Parts): Removed per the rule against questioning availability of cited entities, and because not all practical-method papers must release code to be evaluable. The paper's value can be assessed on its content.
- **"Fine-tuning dataset described only briefly"** (Harsh Critic's Missing Parts): Removed as scope creep—the paper is about the chat vector method, not the dataset itself. The dataset description (Section 4.1) is adequate for the paper's purpose.
- **"Cannot be independently verified" / reproducibility concerns rooted in doubting entity existence**: No such claims appear in the reviewer inputs.

## Novel Insights

None beyond the paper's own contributions. The harsh critic correctly identifies that the most interesting finding is actually the negative result about LLaMA2-chat forgetting after CP (Section 5.1, observation 4), which the paper itself identifies but does not foreground as a major contribution. The fact that directly continuing to train a chat model on new-language data washes out its alignment is arguably more robustly demonstrated than the positive results about the chat vector itself.

## Suggestions

1. **Resolve the contribution contradiction.** Either remove or qualify the claim that the model "responds precisely in the target language" (lines 16 and 23) to explicitly note the English-generation failure mode observed for Chinese-LLaMA, and document the conditions under which the method succeeds vs. falters.
2. **Add at least one RLHF-in-target-language comparison.** Even a limited PPO run on the CP base would provide crucial calibration for interpreting the efficiency-vs.-capability tradeoff.
3. **Run a scaling-coefficient sweep** (0.25, 0.5, 0.75, 1.0) for at least one model family, reporting both language-purity and task-performance metrics, to give practitioners actionable guidance.
4. **Reduce evaluation circularity** by using a non-GPT-4 evaluator (e.g., human evaluation on a subset, or a different LLM judge) for the Vicuna benchmark, and explicitly discuss the potential GPT-4 bias in the evaluation.

## Score and Decision

The paper proposes a simple and appealing idea with some genuine empirical support. The main results (chat vector improving instruction following, reducing toxicity, and enhancing safety across three languages) are broadly convincing. However, the paper suffers from three significant issues: (1) a stated contribution about target-language precision that is directly contradicted by the paper's own Section 5.5; (2) the absence of any RLHF baseline in the target language, which prevents calibration of the efficiency-vs.-capability tradeoff that is the paper's main value proposition; and (3) an evaluation pipeline that relies on GPT-4 in three overlapping roles (translator, gold answer, judge), creating a compounding bias. These issues collectively weaken the paper's case to a degree that, in its current form, the evidence does not fully substantiate the claimed contributions. The paper would benefit substantially from addressing the language-fidelity contradiction, adding even a limited RLHF baseline, and reducing evaluation circularity.

**Score**: The paper has a genuinely novel and practical idea, but the gap between claimed contributions and empirical support is too large for acceptance. The overclaim on target-language fidelity and the missing RLHF calibration are not fatal individually, but together they mean the paper's core claims are not convincingly demonstrated.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>