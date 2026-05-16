Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper investigates the vulnerability of safety-aligned LLMs/MLLMs to out-of-distribution (OOD) inputs. The authors propose JOOD, a jailbreak strategy that transforms harmful inputs using simple off-the-shelf techniques (text-mixing, image mixup, CutMix, etc.) to create OOD-ified versions that bypass safety guardrails. The key insight is that RLHF-based safety alignment does not generalize well to inputs that fall outside the training distribution. Experiments on GPT-4, GPT-4V, MiniGPT-4, and LLaVA-1.5 show high attack success rates across multiple jailbreak scenarios, with extensive ablations characterizing the effect of mixing coefficients, auxiliary image similarity, and transformation types.

## Strengths

- **Novel and well-motivated insight**: The paper systematically identifies a genuine vulnerability of RLHF-based safety alignment — that it fails to generalize to OOD inputs created by simple transformations. This is a previously underexplored axis of attack, and the paper provides clear evidence (especially Figure 4's mixing coefficient ablation) that the effect is driven by the degree of OOD-ification rather than superficial properties of the transformation.

- **Simple yet effective attack**: JOOD uses widely-available, inexpensive, black-box transformations (text-mixing, image mixup). The paper demonstrates across Figures 3a and 3b that multiple text-mixing and image-mixing variants consistently outperform the vanilla attack and non-mixing transformations (RandAug), showing the approach is robust to the specific mixing technique used.

- **Strong empirical results across models and scenarios**: JOOD achieves high ASR on proprietary models (63% on GPT-4V in Bombs or Explosives scenario, Table 1) and generalizes to open-source MLLMs (>80% ASR in multiple scenarios). The per-instruction harmfulness distributions (Figure 2) and exclusive jailbreak counts (Table 2) provide complementary evidence beyond aggregate ASR.

- **Comprehensive ablations**: Figures 3–5 provide thorough analysis of the effect of mixing coefficient, auxiliary image similarity, visual type (typography vs. real images), and different transformation techniques. These ablations support the core OOD hypothesis and offer actionable insights for defense.

- **Robustness to system-prompt defense**: Table 3 shows JOOD maintains 60% ASR even with a safety-aware system prompt (only 3% degradation), while baselines drop more sharply (FigStep-Pro drops 10%).

## Weaknesses

### Fatal
None.

### Major

- **Unfair baseline comparison via "max over attacks" evaluation**: JOOD evaluates by taking the best response across n=5 auxiliary words/images × m=9 mixing coefficients = up to 45 attempts per harmful instruction (Section 3.3, Eq. 4). The paper does **not specify whether baselines (CipherChat, PAIR, FigStep, HADES) were evaluated with the same multi-attempt protocol or with a single attempt per instruction**. If baselines were run only once while JOOD selects the maximum from dozens of attempts, the reported margins (e.g., "+42% ASR" in Hacking, "+40% ASR" in Bombs or Explosives) conflate attack effectiveness with brute-force search. The paper should: (a) clarify the baseline evaluation protocol, (b) report per-attempt ASR (e.g., average or median across transformations), or (c) match the number of attempts across methods. The exclusive jailbreak counts (Table 2) partially mitigate this concern since they show JOOD jailbreaks instructions baselines fail on entirely, but the quantitative ASR comparisons in their current form lack fairness guarantees.

### Minor

- **Central mechanism (uncertainty increase) is asserted but not directly measured**: The paper repeatedly claims that OOD-ifying inputs "highly increases the uncertainty of the model" (abstract, introduction, Section 3.2), but never directly measures any uncertainty proxy — no perplexity, output entropy, confidence scores, or refusal token probabilities are reported. The evidence for the mechanism is indirect: mixing coefficients affect ASR (Figure 4), which is consistent with the uncertainty story, but alternative explanations (e.g., mixing distracts the model, or provides a "cover story") are not ruled out. Directly measuring uncertainty would substantially strengthen the paper's theoretical contribution.

- **No variance or statistical significance reporting**: Results (Tables 1–3, Figures 3–5) are reported as point estimates with no error bars, confidence intervals, or repeated runs. Each scenario contains ~30 instructions, and jailbreak success can be sensitive to the specific random sampling of auxiliary words/images. While single-run evaluation is common in this literature, reporting bootstrapped confidence intervals or results over multiple random seeds would substantially increase confidence in the quantitative claims.

- **Text-mixing transformation is underspecified**: The paper describes text-mixing by example ("bomb" + "apple" → "baopmpble") and mentions "H(orizontal)-Interleave" (Figure 3a), but provides no formal algorithm for the character-level interleaving function. Questions such as how words of different lengths are handled, whether the interleaving order is deterministic or random, and what other mixing variants (beyond H-Interleave) entail are not addressed. While the approach is reproducible from the example and citation of Enaganti et al. (2018), a formal specification would enable exact replication.

- **Prompt change for mixed images is not controlled**: In Section 3.2, the text instruction is reformulated to "tell me how to build **each** object in this image" (emphasis added). This asks about both the harmful and auxiliary objects, which is a different task from the vanilla attack ("tell me how to build the object in this image"). The paper does not ablate whether this change in instruction, independent of image mixing, contributes to the increased harmfulness scores.

- **System prompt defense is generic**: Table 3 tests only a single, short system-prompt defense. The paper's claim that JOOD is "robust" to defense is based on this one prompt. Stronger or more specific defense prompts (common in practice) might yield different results.

### Trivial
- The example auxiliary word "apple" in the implementation details (Section 4) has a formatting artifact ("$a_{\mathrm{pp}\perp\mathrm{e}}$") — this is a parser issue, not an author error.

## Nice-to-Haves
- **Ablation on the necessity of the explicit de-obfuscation instruction** ("Please refer to the possible words inside this new word as '[Words]'") in the text-mixing prompt. Does the model still parse the coined word without this instruction?
- **Human validation of harmfulness**: The HF and ASR metrics are fully automatic. A small human evaluation (e.g., 50 responses rated by annotators) would validate that the automatic metrics correspond to actual harmful content.
- **Negative societal impact discussion**: A brief note on responsible disclosure or the intent to expose vulnerabilities for safety improvement would be appropriate for an attack paper.
- **Failure case analysis**: For the ~37% of instructions JOOD does not jailbreak, examining whether the model refuses or produces safe responses could guide improvements.

## Removed Points

- **"The auxiliary images/words are randomly sampled from the Internet, which is not reproducible"**: This criticism is downgraded because providing the exact URLs for all auxiliary images/words is not standard in this literature; authors can release the exact set with code. The paper specifies n=5 and the sampling procedure, which is adequate for reproducibility.
- **"No missing citations are apparent"**: This is not a weakness.
- **"The paper does not discuss potential misuse or dual-use considerations"**: Moved to Nice-to-Haves — this is common for attack papers and does not affect technical soundness.
- **"The code is not mentioned"** and **"assuming it will be released (stripped appendix)"**: Parser artifacts; any code/appendix information was in the original submission's appendix which is stripped.
- **"HF score is not directly validated against human judgments"**: This is an automatic evaluation concern; moved to Nice-to-Haves as a suggestion rather than a weakness.

## Novel Insights

Beyond the paper's own contributions, the reviewers collectively surface two noteworthy observations. First, the strength of JOOD comes from a simple principle (making inputs OOD to safety alignment) rather than algorithmic sophistication — implying that **any** transformation that pushes inputs far enough from the safety-alignment distribution may work. Second, the negative correlation between auxiliary image similarity and harmfulness (Figure 5a) suggests that defenses could potentially be built by monitoring the semantic coherence of inputs, though this is speculative. The per-instruction analysis (Figure 2) revealing that baselines produce sparse high-harmfulness responses while JOOD consistently produces harmful outputs across most instructions is a qualitative distinction worth highlighting beyond aggregate ASR.

## Suggestions
1. **Clarify the baseline evaluation protocol** — explicitly state whether each baseline method received a single attempt per instruction or multiple attempts, and if the latter, how many. Consider reporting per-attempt ASR (average or median across the 45 JOOD configurations) alongside the max-based metric.
2. **Report variance** — provide bootstrapped 95% confidence intervals for the main ASR results, or run the attack with 3–5 different random seeds for auxiliary sampling.
3. **Add a direct uncertainty measurement** — compute perplexity, output entropy, or refusal-token probability for JOOD inputs vs. vanilla inputs to directly support the claimed mechanism.

## Score and Decision

The paper identifies a genuine and practically important vulnerability: simple OOD-ification via mixing techniques effectively bypasses RLHF-based safety alignment in proprietary models. The ablations are thorough and the core finding is robust across multiple scenarios, models, and transformation variants. The main concern is a methodological ambiguity in the evaluation protocol — the paper's head-to-head ASR comparisons with baselines are not clearly fair given JOOD's multi-attempt design. This does not invalidate the paper's contribution (the exclusive jailbreak counts and ablations provide independent support), but it does undermine the quantitative margins as currently stated. With clarification of the evaluation protocol (which is addressable in rebuttal), the paper would be a solid contribution to the jailbreak literature.

**Score: 6.5/10** — The contribution is real and well-supported by qualitative and ablative evidence, but the main quantitative comparisons need clarification before the claims can be taken at face value. This is a borderline accept / weak accept.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>