Now I have a thorough understanding of the paper and can verify all reviewer claims. Let me construct the consolidated review.

## Summary

This paper proposes FlipAttack, a jailbreak attack against black-box LLMs that disguises harmful prompts by reversing (flipping) their text at the character or word level, then instructs the LLM to reverse them back and execute the harmful behavior. The attack achieves state-of-the-art results: 81.80% average ASR across 8 LLMs (25.16% above the runner-up), 98.08% average bypass rate against 5 guard models, and requires only a single query. The paper also provides empirical evidence that LLMs process text left-to-right and that left-side noise degrades understanding more than right-side noise.

## Strengths

1. **Record-high attack success rate on state-of-the-art LLMs**: FlipAttack achieves an average ASR of 81.80% across 8 LLMs, outperforming the runner-up by 25.16% (Table 1). It attains 98.85% on GPT-4 Turbo, 98.08% on GPT-4o, and 86.54% on Claude 3.5 Sonnet — the latter being 65+ points higher than any other black-box method on that model. These results are empirically verified and clearly presented.

2. **Nearly perfect bypass of guard models with direct empirical evidence**: FlipAttack achieves a 98.08% average bypass rate across 5 guard models, including 100% on OpenAI's Moderation and LLaMA Guard 2 8B (Table 2). Unlike the perplexity analysis (which has framing issues), this is direct, unmediated evidence of stealth that doesn't rely on proxy metrics.

3. **Single-query attack with minimal cost**: The attack requires only 1 query, whereas iterative methods like ReNeLLM and PAIR incur high token costs (e.g., 5,685 tokens per example for ReNeLLM). Figure 4 confirms FlipAttack occupies the lowest-cost region while achieving the highest ASR. This practical efficiency is a genuine strength.

4. **Comprehensive ablation studies validating design choices**: Ablations on four flipping modes (Figure 6) and four guidance variants (Figure 7) across 8 LLMs are thorough and informative. The ablation reveals that the simplest variant ("Vanilla") already achieves very high ASR on strong models (98.08% on GPT-4 Turbo), while more complex guidance components benefit weaker models. This is explicitly acknowledged by the paper (line 338), not hidden.

5. **Simplicity and elegance of the core idea**: The attack constructs flipped text using only the original prompt's own content, without external noise, ciphers, or complex transformations. The flipping task is shown to be easy for strong LLMs (e.g., 99.54% match rate for Claude 3.5 Sonnet, Table 5). The method's simplicity is a virtue, not a weakness.

## Weaknesses

### Fatal

None.

### Major

1. **Overclaimed mechanism story that doesn't match the actual attack design.** The paper builds a narrative around "left-side noise" — claiming that LLMs read left-to-right and that left-side noise degrades understanding more than right-side noise — and presents this as motivating the flipping attack. However, the four flipping modes (word-order reversal, character-within-word reversal, full character reversal, and the deliberately misleading mode IV) are symmetric global transformations, not an asymmetric left-noise injection. The left-vs-right noise experiment (Table 3, adding random strings to either end of a sentence) is a different operation and doesn't directly explain why *flipping* works. The paper's central theoretical claim — "revealing LLMs' understanding mechanism" (Contribution 1) — is overstated: what the evidence robustly shows is that text reversal bypasses safety alignment, not that left-side noise specifically is the key mechanism. The attack would work (or fail) the same regardless of the left/right directionality claim. This framing disconnect weakens the paper's intellectual contribution, though the empirical findings remain strong if reframed honestly as "text reversal + unflip instruction."

2. **The Fool Model Mode (IV) is presented but not explained.** Mode IV flips characters but instructs the LLM to reverse word order — a deliberate mismatch between the transformation and the correction instruction. The paper's ablation (Figure 6) shows results for this mode, and the text (line 292) notes CoT can help with it. However, the paper provides no mechanistic explanation for *why* this variant works or why it fools the model differently than Mode III with correct instructions. The "left-side noise" framework cannot account for it (since the correction instruction is wrong), and the paper offers no alternative theory. This is a missed opportunity to probe what the LLM is actually doing.

### Minor

1. **Perplexity-based stealth argument creates an internal inconsistency with the defense discussion.** The paper argues that high perplexity (809.67, Table 4) makes the flipped prompt "stealthy" because guard models are unfamiliar with it. At the same time, it proposes a Perplexity-based Guardrail Filter (PGF) as a defense and claims it is ineffective (line 197). If the perplexity is an order of magnitude above normal (~50 vs. ~810), a simple threshold-based filter should be trivially effective — yet the paper asserts otherwise without resolving this contradiction. The direct bypass-rate evidence (Table 2) is sufficient to demonstrate stealth; the perplexity framing and PGF discussion add confusion rather than support and should be reconciled or dropped.

2. **No dedicated analysis of why Claude 3.5 Sonnet is uniquely vulnerable.** The gap between FlipAttack (86.54% ASR) and the next-best black-box method on Claude (CodeChameleon at 20.77%) is the most striking single result in the paper — a 65+ point margin. The paper notes that Claude has the highest flipping-task match rate (99.54%, Table 5), which is relevant, but does not explicitly investigate why other methods fail so dramatically on Claude while FlipAttack succeeds. Given Claude's reputation for strong safety alignment, this deserves a targeted discussion.

3. **The guidance module's few-shot demonstrations split the original harmful prompt, partially undermining the stealth claim.** Variant D includes split harmful prompts (e.g., "bmob a" → "a bomb") as in-context examples. The paper acknowledges this risk (line 191), which is commendable, but does not evaluate whether using harmless filler demonstrations instead would maintain performance. This is a testable assumption, and the paper's conclusion that "developing a better splitting method is a promising future direction" sidesteps the question rather than addressing it.

### Trivial

None of substance; the paper is reasonably well-written.

## Nice-to-Haves

- Include a full example of an attack prompt (flipped text + guidance instruction) in the main text so readers can directly see what is sent to the API.
- The cost analysis (Figure 4) could report the total input token count for FlipAttack's full prompt (including guidance instructions), not just the flipped query.
- A comparison against simple text-reversal baselines (just flipping without the elaborate guidance module) on weaker models would strengthen the claim about the guidance module's necessity.

## Removed Points

- **Critic's claim that the iterative character-moving illustration "is not one of the four modes."** This is factually incorrect. The iterative process described on line 151 produces "bmob a si sihT" from "This is a bomb," which is exactly the output of Mode III (Flip Characters in Sentence). The iterative illustration is the conceptual motivation that directly maps to Mode III.
- **Critic's claim that the paper "over-claims the contribution of the multi-variant guidance module" because Vanilla already works on strong models.** The paper explicitly acknowledges this finding (line 338: "The variant Vanilla can already achieve a promising attack performance on some strong LLMs"). The guidance module variants are correctly framed as benefiting weaker models.
- **Critic's claim that the guidance module "undermines the claim of stealthiness."** The paper provides direct empirical evidence of stealth (98.08% guard model bypass rate, Table 2) that accounts for the full prompt (flipped text + guidance). The critic's concern about the guidance being detectable is contradicted by the actual bypass rates. The paper also acknowledges the risk of few-shot demonstrations.

## Novel Insights

None beyond the paper's own contributions. The reviews largely agree on the empirical strength and the framing weakness.

## Suggestions

1. Reframe the paper's narrative honestly: the core empirical finding is that text reversal (at word or character level) combined with an unflip instruction jailbreaks current LLMs with near-perfect success. Drop or substantially temper the "left-side noise mechanism" framing, which is a separate experiment that motivates but does not explain the attack.

2. Either reconcile the perplexity-based stealth argument with the PGF defense discussion, or remove the PGF section entirely. The direct guard-model bypass rates are sufficient evidence of stealth.

3. Add a brief discussion of why Claude 3.5 Sonnet is uniquely vulnerable to FlipAttack (drawing on the flipping-task match rate data and discussing Claude's potentially weaker rejection of non-canonical input forms).

4. Consider removing or clearly labeling the Fool Model Mode (IV) as an empirical curiosity that the current framework does not explain, rather than presenting it as a designed variant.

## Score and Decision

The paper makes a genuine empirical contribution: it demonstrates a simple, inexpensive, single-query attack that outperforms all existing methods on the most important closed-source LLMs by a wide margin and achieves near-perfect guard model bypass rates. The core weakness is a strained theoretical narrative that claims more than the evidence supports — the "left-side noise" mechanism does not coherently explain the flipping attack, and some of the paper's arguments (perplexity-based stealth, PGF defense) are internally inconsistent. These are fixable framing issues, not fatal empirical flaws. With a reframed narrative that honestly characterizes the attack as "text reversal + unflip instruction," the paper would be strong.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>