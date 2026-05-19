- Decision: Reject
- Avg Score: 4.00
- Scores: 1, 3, 5, 8, 3
Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

---

## Summary

This paper proposes CBF-LLM, a framework that applies control barrier functions (CBF) from control engineering to LLM alignment. The core idea is to add a lightweight "safety filter" between the LLM's token predictor and the token selector: the filter zeros out token probabilities that would cause a learned "language-constraint function" (L-CF) to decrease too rapidly (violating a discrete-time CBF inequality), then renormalizes. The method is learning-free (no LLM fine-tuning) and add-on. An experiment using Llama 3 with a RoBERTa sentiment classifier on a single positive-sentiment steering task is presented.

## Strengths

- **Novel cross-domain framework**: The paper formalizes text generation as a discrete-time dynamical system and adapts the CBF formalism (Equations 6-7, Algorithm 1) to the token-generation setting. This explicit translation from control theory to NLP is a novel and principled way to think about alignment as a safety-filter problem.

- **Learning-free, add-on design**: CBF-LLM requires no modification of the underlying LLM's parameters; it operates solely on the output probability distribution (Section 3). This makes it broadly applicable across LLMs without per-model training, as acknowledged in the contributions (lines 65-68).

- **Adjustable strictness (α parameter)**: The hyperparameter α ∈ [0,1] controls how aggressively the filter intervenes, from "only block already-negative text" (α=1, equivalent to Blacklist) to "require monotonic improvement" (α=0). The paper demonstrates empirically that different α values produce different intervention counts (Table 1: 137.90 for α=0.8 vs 161.59 for α=0.3), offering practical flexibility.

- **Working implementation with off-the-shelf models**: The method is concretely implemented using Llama 3 8B and a pre-trained RoBERTa sentiment model (Section 4.1), with no additional training. This makes the approach replicable and illustrates feasibility.

## Weaknesses

### Fatal

None. The core method is coherent and the implementation works as described for the tested setting. No issues that fully invalidate the paper's claims.

### Major

1. **No comparison with any existing controlled generation / alignment method.**  
   The paper compares only against a trivial Blacklist filter (which is itself a special case of CBF with α=1, as noted at line 410) and a NoControl baseline. A substantial body of work on guided/controlled text generation exists — PPLM, GeDi, DExperts, FUDGE, and others — many of which also use an external classifier to steer generation on the exact tasks the paper discusses (sentiment, toxicity, etc.). Without any comparison, the paper cannot demonstrate whether CBF-LLM offers any practical advantage over prior approaches in alignment effectiveness, output quality, or computational cost. This is the most significant weakness: the contribution of the paper (a new alignment framework) must be evaluated relative to existing approaches, not just against a degenerate special case of itself.

2. **Evaluation scope is far too narrow to support generalization.**  
   The experiment uses a single task (positive sentiment steering), a single initial prompt (line 418), a single LLM (Llama 3), a single L-CF model (RoBERTa sentiment classifier), a short generation length (30 tokens), and only 100 samples (line 422). The paper claims alignment "ability" and "effectiveness" broadly (lines 6, 384, 565), but the evidence is confined to one narrow corner of one task. At minimum, multiple alignment goals (toxicity, bias, style, factuality), multiple prompts, and multiple LLMs would be needed before such claims can be supported.

3. **No evaluation of output quality beyond the L-CF value and disallowed-token counts.**  
   The paper measures only (a) whether the L-CF value stays positive and (b) how many tokens were disallowed per generation. It reports no fluency metrics (e.g., perplexity from a held-out LM), diversity metrics (e.g., distinct n-grams, self-BLEU), coherence measures, or human ratings. In controlled generation, suppressing tokens to stay within a safe region is easy; the harder question is whether the resulting text remains natural and fluent. Table 1 shows CBF(α=0.8) disallows 137.90 tokens vs the Blacklist's 209.79, but without quality metrics, it is unclear whether the CBF filter achieves this by making better decisions or by being more permissive in ways that degrade output. The qualitative examples (Section 4.2) look plausible, but systematic evaluation is absent.

### Minor

1. **Sign inconsistency between Equation (8) and Algorithm 1.**  
   Equation (8) (line 311) uses the condition `h(Concat(x,t)) - h(x) ≤ -α h(x)` to keep a token's probability, while Algorithm 1 (line 349) correctly uses `h(x⁺) - h(x) ≥ -α h(x)`, consistent with the discrete-time CBF constraint (Equation 4). These are opposite inequalities. The algorithm implements the correct filter; Equation (8) has a sign error that should be corrected. This does not affect the experimental results (which use the algorithm) but is a formal inconsistency that would confuse readers.

2. **Top-k heuristic is not discussed in terms of its effect on the safety guarantee.**  
   The paper mentions that top-k sampling is used for efficiency (line 328) and the algorithm only evaluates the top-k tokens (Algorithm 1, lines 347-357). However, the paper earlier states that the CBF filter "guarantees that the generated text x always satisfies that x∈𝒮" (line 319). With top-k truncation, only a subset of tokens is checked, so this formal guarantee no longer strictly holds. The paper does not acknowledge this gap or discuss its practical implications.

3. **No discussion of L-CF reliability on incomplete/partial sentences.**  
   The filter evaluates `h(Concat(x, t))` for each candidate token *before* the token is appended — i.e., it judges the sentiment of an incomplete sentence. The RoBERTa sentiment model was likely trained on complete sentences, and its behavior on partial or syntactically incomplete text could be unreliable. The paper does not discuss this potential brittleness.

4. **No discussion of limitations or failure modes.**  
   There is no section or paragraph discussing cases where the L-CF might be inaccurate, where the filter might over-suppress and degrade generation, or where the CBF constraint might be too restrictive to allow coherent text. Adding such a discussion would strengthen the paper.

### Trivial

None beyond what is already listed as minor.

## Nice-to-Haves

- **Comparison with at least two existing guided generation methods** (e.g., a logit-addition method and a sampling-time classifier method) on the same task, ideally with the same LLM and L-CF. This is the most impactful single addition for establishing the method's value.
- **Automatic quality metrics** such as perplexity, distinct-n-grams, and self-BLEU for all conditions.
- **Experiments on at least one additional alignment goal** (e.g., toxicity reduction or style control) and with additional initial prompts.
- **Ablation study on the top-k parameter** to show how it affects both safety and text quality.
- **Confidence intervals or variance** for the disallowed-token counts in Table 1.

## Removed Points

These points were raised by a reviewer but are removed or downgraded per the filtering guidelines:

- *"The CBF(0.3) case has more disallowed tokens than CBF(0.8), which is reasonable but the paper does not discuss the trade-off in depth."* — Removed. The paper does discuss the role of α in determining strictness (lines 321-326), and the trade-off is implicitly demonstrated by the differing counts.
- *"The attractor analysis could be condensed or removed."* — Removed. This is a subjective presentation preference, not a substantive weakness.
- *"The paper does not report standard deviation or per-generation breakdown for disallowed tokens."* — Demoted to Nice-to-Have. The table reports averages, and while variance would be informative, single-run average reporting is conventional for this type of exploratory demonstration.
- *"The paper is missing a comparison with prior work."* — Kept as Major Weakness #1 above (this is a substantive, concrete criticism).
- Strength Finder's claim that the paper "verifies the safety guarantee stated in Theorem 1" is overstated — the paper states no Theorem specific to CBF-LLM, only the standard CBF theorem in preliminaries. The relevant strength (empirically maintaining positive L-CF values) is kept but rephrased accurately.

## Novel Insights

None beyond the paper's own contributions. The cross-domain analogy (CBF → LLM alignment) and the attractor distribution analysis are the paper's original offerings; the reviews do not surface additional insights not already present in the paper.

## Suggestions

1. **Add comparisons to existing controlled generation methods** (PPLM, GeDi, DExperts, or even a simple logit-addition baseline) on the same task. Without this, the paper cannot demonstrate that CBF-LLM improves upon the state of the art.
2. **Expand the evaluation** to include at least one additional alignment task (e.g., toxicity reduction), additional initial prompts, and possibly a second LLM. Report quality metrics (perplexity, diversity) alongside the intervention count.
3. **Fix the sign error** in Equation (8) to match Algorithm 1.
4. **Add a limitations section** that discusses: (a) the effect of top-k heuristic on the safety guarantee, (b) scenarios where the L-CF might be unreliable (e.g., on incomplete sentences), and (c) potential failure modes where the filter could degrade text quality.
5. **Report variance/confidence intervals** for the disallowed-token counts in Table 1.
