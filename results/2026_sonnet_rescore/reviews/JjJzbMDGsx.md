## Summary
The paper introduces the **Language Confusion Gate (LCG)**, a lightweight plug-in MLP trained via norm-adjusted self-distillation that dynamically masks tokens of disallowed language families during decoding. The method requires no modification to the base LLM and reduces language confusion by an order of magnitude across four no-think and three thinking models, as demonstrated on FLORES-NO-LATIN, INCLUDE, and Humaneval-XL, while preserving task performance (BLEU, accuracy, Pass@k).

---

## Strengths

1. **Targeted motivation from confusion-point analysis**: The paper establishes empirically that the confusion token is top-1 56.74% of the time (making greedy decoding ineffective), while the correct-language token appears in the top-3 in 99.29% of cases at confusion points (Section 3.1). This directly and precisely motivates logit-level masking as the right intervention.

2. **Mechanistic insight into embedding norm bias**: Table 1 quantifies a significant norm imbalance across language families (e.g., Qwen3-8B CJ tokens occupy 10.74% of top-5% norms vs. 0.14% for Low-Res), and Figure 2 demonstrates that norm-adjusting logits eliminates CJ confusors from the top-10 list. This is a novel mechanistic contribution that directly motivates the norm-adjusted self-distillation strategy.

3. **Consistent, large-magnitude results across architectures**: LCG-adjusted reduces CJ confusion from 4.5% to 0.1% and Latin confusion from 12.1% to 2.0% for Qwen3-8B; from 1.0% to 0.0% CJ and 4.4% to 0.4% Latin for Qwen3-30B, all with BLEU scores stable or slightly improved (Table 3). Results hold across Qwen3, Llama3.1, Gemma3, and GPT-OSS architectures in both no-think and thinking modes (Tables 3–4).

4. **Norm-adjustment ablation demonstrates the value of the mechanistic insight**: LCG-adjusted consistently outperforms LCG-unadjusted (e.g., Llama3.1-8B Latin% from 5.7% → 2.9%, Qwen3-8B Latin% from 6.2% → 2.0%), confirming that the norm-bias discovery translates directly into a better training signal.

5. **Practical efficiency**: The gate adds only 0.4% overhead in a production benchmark (Section 6), intervenes on only 0.33–0.38% of tokens (Section 5.3), and is compatible with speculative decoding.

---

## Weaknesses

### Fatal
None.

### Major

- **ORPO baseline comparison is potentially unfair against LCG (in the other direction)**: The paper synthesizes its own ORPO dataset "similar to Lee et al. (2025)" rather than using that paper's exact setup. The observed capability degradation on INCLUDE (Qwen3-8B: 61.4 → 57.3, Llama3.1-8B: 46.1 → 43.2) is attributed to ORPO "sacrificing language understanding," but it could equally reflect a suboptimally tuned implementation. The paper provides no hyperparameter details for ORPO training. This does not invalidate LCG's results, but it means the advantage in head-to-head comparison cannot be fully credited — the conclusion "ORPO sacrifices capability" is suggestive but not established. The authors should either provide full ORPO tuning details or hedge this interpretation.

### Minor

- **Code-switching preservation analysis (86.7%) is methodologically opaque**: This figure (Section 5.3) is doing the most important work in the paper's "LCG preserves legitimate code-switching" claim. The paper does not specify how many examples were human-annotated, how many annotators were involved, what the inter-annotator agreement was, or how the sample was constructed from FLORES-WITH-LATIN. Given how much weight the paper places on this number, a minimal description of the annotation protocol is needed to make the claim verifiable.

- **Low-Res-to-Low-Res confusion is structurally unaddressed, with no empirical scoping**: Intervention Rule 1 states that Low-Res tokens are never masked, meaning LCG cannot prevent, e.g., Devanagari appearing in Thai output or Arabic appearing in Hebrew output. The paper acknowledges this in the conclusion ("the gate cannot resolve more nuanced confusion between languages that share the same script… or between two different low-resource languages"), but never quantifies what fraction of real-world confusion events fall outside the CJ and Latin categories that LCG actually targets. Given the paper's framing of LCG as a general solution "across 200+ languages," quantifying this scope gap—even approximately from a held-out confusion sample—would substantiate the claim.

- **No statistical significance reporting**: Some baseline confusion rates are very low (e.g., Gemma3-12B CJ at 0.2% before, 0.1% after), making it unclear whether reported reductions are within sampling noise. The intervention rate frequency analysis is only reported for FLORES-NO-LATIN, not for reasoning tasks where sequences are longer and more diverse.

### Trivial

- **Table 4 caption mislabeling**: Table 4 is titled "Effectiveness of LCG Intervention on 'No-Think' Models measured on Humaneval-XL," but the table evaluates thinking models (Qwen3-8B-Thinking, Qwen3-30B-Thinking, GPT-OSS). This is a copy-paste error.

---

## Nice-to-Haves

- An empirical breakdown of what fraction of confusion events across the evaluated languages fall into CJ%, Latin%, and Low-Res-to-Low-Res categories would let readers understand whether LCG addresses 90% or 50% of real-world confusion.
- A code-switching type breakdown (technical terms, proper nouns, code snippets) of the 86.7% figure would sharpen the code-switching preservation claim.
- A complementary ablation showing that the gate trained *without* norm adjustment more frequently fires incorrectly (masking tokens it should allow) would strengthen the mechanistic narrative beyond just showing that LCG-adjusted achieves lower confusion rates.
- Reporting intervention frequency on reasoning tasks (Humaneval-XL) in addition to FLORES-NO-LATIN.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Commercial models not in Table 3"**: The paper clearly explains that commercial models are shown in Table 2 as motivational context only, noting "we are not sure if a similar intervention mechanism like LCG has been applied to any commercial models." This is correctly scoped. Not a weakness.

- **"Token classification conservatism (ambiguous BPE tokens → Symbols)"**: The paper explicitly discusses this in Section 4.1 and notes the classification methodology in Appendix A. This is addressed in the paper; flagging it as a reproducibility concern adds nothing without a concrete example of failure.

- **"Training details not reported (optimizer, LR, MLP hidden dim)"**: The paper defers to the appendix, which has been stripped by the parser. Per evaluation rules, weaknesses about appendix absence are removed.

- **"200+ language coverage not validated in evaluation"**: This would be a nice-to-have but is scope creep — the paper explicitly targets CJ and Latin confusion, which it validates on 5–8 languages. Requesting evaluation of all 200+ languages is unreasonable for a venue paper.

- **"Figure 2 caption doesn't communicate that norm adjustment shifts from CJ to Latin rather than Hebrew"**: The paper text explicitly states: "Norm bias can account for a subset of such errors but cannot fully explain language confusion." The paper correctly frames Figure 2 as a partial diagnostic, not a solution. This is a presentation nitpick.

---

## Novel Insights

The most technically novel element of this paper is the output token embedding norm decomposition in Section 3.2: by decomposing `logit_i = ||h|| · ||e_i|| · cos_sim(h, e_i)` and showing that the norm term `||e_i||` creates a systemic high-resource language bias (Table 1), the paper provides a mechanistic explanation for *why* confusion arises that goes beyond prior behavioral descriptions. The immediate translation of this insight into a debiasing signal (norm-adjusted self-distillation) for training a plug-in gate — rather than using it directly as a rule — is an elegant design choice that correctly handles cases where norm adjustment alone is insufficient (e.g., English-Chinese confusion where both have high norms). This mechanistic-to-training pipeline is the paper's most distinctive intellectual contribution.

---

## Suggestions

1. **Add full annotation protocol for the 86.7% figure**: Number of examples, annotators, IAA metric, and sampling procedure. Even 3–4 sentences would suffice.
2. **Report ORPO hyperparameters (or hedge the interpretation)**: Provide the dataset size, training steps, learning rate, and reference checkpoint, or explicitly note the comparison is against a best-effort re-implementation and may not reflect ORPO's ceiling.
3. **Quantify scope empirically**: Report, from a held-out confusion sample, what fraction falls into CJ%, Latin%, and Low-Res-to-Low-Res. This closes the gap between the "general solution" framing and the evaluated coverage.
4. **Fix Table 4 caption** to read "Thinking Models."

---

## Score and Decision

**Originality**: The norm-bias decomposition and norm-adjusted self-distillation are genuinely novel; the plug-in MLP design concept is familiar but the specific instantiation is new. **Importance**: Language confusion in LLMs is a real, widespread problem (shown even in GPT-5 and Qwen3-235B), and a practical, training-free solution has clear deployment value. **Claims supported**: Core confusion-reduction claims are strongly supported across four architectures and two task types; the code-switching preservation claim is partially supported but with insufficient methodological transparency. **Soundness**: Experimental design is generally sound with a minor gap in the ORPO comparison. **Clarity**: Well-organized, clearly written; the mechanistic analysis is easy to follow. **Community value**: High — open-sourced datasets, practical deployment numbers, results on widely used models.

The weaknesses are real but bounded: the ORPO comparison caveat, the opaque 86.7% annotation methodology, and the Low-Res scope gap are all fixable without new experiments. None threaten the core contribution.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>