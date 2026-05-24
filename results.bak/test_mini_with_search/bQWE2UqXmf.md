Now I have enough information. Let me compose the final review.

**Round 1 bracket**: Between 4.5 and 6.5. The weak anchors (1.5–3.0) are rejected papers with fatal flaws; the closest topical papers (D&R, Learn-to-Distance, HLD) all sit at 5.0–5.5 and were accepted as posters. The 8+ anchors are unrelated topics.

**Round 2 narrowing**: Pulled additional anchors in [4.5, 6.0] and [5.0, 7.0]. The most directly comparable papers are:
- **D&R (5.50)**: Recovery-based detection, also uses LLM rewriting. Reports AUROC with error bars. Has theoretical grounding (posterior concentration). Criticized for limited adversarial testing. Raidar has broader domain coverage (6 vs 4 datasets) and tests adaptive attacks, but lacks AUROC/error bars and has a confusing equivariance section. **Raidar is slightly weaker than D&R → anchors Raidar ≈ 5.0.**
- **Learn-to-Distance (5.50)**: Rewrite-based detection with geometric theory. Criticized for unrealistic assumptions and fairness of comparison. Raidar is cleaner but less theoretically grounded. **Raidar ≈ 5.0.**
- **TASTE (5.00)**: Adversarial training for multilingual detection. Criticized for metric choice and missing code. Raidar has a more novel core insight. **Raidar slightly stronger than TASTE → anchors Raidar ≈ 5.0.**

Final score: **5.0** — a paper with a genuinely novel insight and broad experiments, but with evaluation gaps and a confusing methodological point that prevent it from reaching the level of the stronger poster papers.

---

## Summary

This paper introduces Raidar, a method for detecting AI-generated text by prompting an LLM to rewrite the input and measuring the Levenshtein editing distance between the original and rewritten versions. The key insight is that LLMs modify AI-generated text less than human-written text because they perceive it as high-quality. The method operates on discrete symbolic output (no log-probabilities required), making it compatible with black-box LLMs. Experiments across six domains (News, Creative Writing, Student Essays, Code, Yelp Reviews, ArXiv Abstracts) show large F1 gains over Ghostbuster and DetectGPT — up to 29 points on Code — and demonstrate robustness across different source models, rewriting models, and adaptive attack prompts.

## Strengths

- **Simple, novel, and well-motivated core insight.** The observation that LLMs modify AI-generated text less during rewriting is intuitive and grounded in the auto-regressive training objective. This is a genuinely new detection signal that differs fundamentally from log-probability-based methods (DetectGPT, Ghostbuster) and watermarking.

- **Large and consistent empirical gains.** Tables 1–2 show Raidar (Invariance) exceeding Ghostbuster by 8–29 points in-domain and up to 32 points out-of-domain across all six datasets. The improvements are not confined to one domain — every dataset shows gains in at least one Raidar variant.

- **Black-box compatibility is a real practical advantage.** Raidar requires only discrete token output (Levenshtein distance), unlike DetectGPT (needs log-probabilities) and Ghostbuster (needs probability features). This makes it directly usable with GPT-3.5-turbo, GPT-4, and other API-only models.

- **Strong cross-model generalization.** Table 4 shows that a single rewriting model (GPT-3.5-turbo) detects text from five different generators (Ada, Text-Davinci-002, GPT-3.5, GPT-4, LLaMA 2) with F1 scores above 80 on most in-distribution tasks, including 96.88 on Ada code and 98.46 on LLaMA 2 code.

- **Effective on short inputs.** Figure 5 shows 74 F1 on Yelp with inputs as short as ~10 words, a regime where many competing methods (GPTZero, Ghostbuster) are documented to struggle.

- **Robustness to adversarial rephrasing under multi-prompt training.** Table 3 shows that training on two rewriting prompts and testing on a third unseen evasive prompt yields F1 scores of 86–93 on Code and ArXiv, demonstrating that the method can be adapted to resist paraphrasing attacks.

## Weaknesses

### Fatal
None.

### Major

1. **Missing AUROC and confidence intervals — evaluation is incomplete by the standards of this field.** The detection literature (DetectGPT, Ghostbuster, Fast-DetectGPT, Binoculars, D&R, etc.) standardly reports AUROC and often includes confidence intervals or variance. Raidar reports only F1 scores in all main tables (Tables 1, 2, 3, 4, 5). F1 depends on a threshold choice that is not justified, and without AUROC the reader cannot assess performance across the full operating range. No error bars, significance tests, or variance estimates are given anywhere in the paper. This is especially needed given the magnitude of the reported gains (e.g., 95.38 vs 65.97 on Code), which would be more convincing with confidence bounds. The baselines (DetectGPT, Ghostbuster) are also reported as F1-only in the tables, so the *relative* comparison is internally consistent, but the paper cannot be positioned against, or independently verified against, the broader literature that reports AUROC. **Fix: add AUROC with bootstrapped confidence intervals, and specify the threshold selection procedure.**

2. **Equivariance measurement is mathematically confusing.** Section 3.1 defines equivariance using prompts $T$ and $T^{-1}$, where applying $T$, rewriting, then $T^{-1}$ should return to the original. However, the first example pair shows:
   - $T$: "Write this in the opposite meaning:"
   - $T^{-1}$: "Write this in the opposite meaning:"  
   These are identical prompts, not inverses. Applying the same prompt twice gives the opposite of the opposite (which in principle could return to the original if the LLM is consistent, but this is not explained or justified). The second pair (Expand/Concise) is a proper inverse. As presented, the measurement formula $L = D(F(T^{-1}, F(p, F(T, \x))), F(p, \x))$ assumes $T^{-1}$ undoes $T$, but the provided "opposite meaning" example does not satisfy this without additional reasoning about LLM behavior that the paper does not supply. This undermines the interpretation of the equivariance results in Tables 1–2. **Fix: either correct the prompts to be genuine inverses (e.g., "make this positive" / "make this negative") or provide a clear justification for why the same prompt serves as its own inverse in this context, or remove the problematic example.**

3. **Potential confound: text quality versus origin is not addressed.** The paper's central hypothesis is that LLMs modify AI-generated text less because they "perceive" it as high-quality (abstract: "LLMs often perceive AI-generated text as high-quality"). But high-quality human text (professional journalism, edited prose) could also be modified little. If the human-written texts in the evaluation are systematically less polished than the AI texts — which is plausible for Yelp reviews and student essays — the observed effect could partly reflect quality rather than origin. The paper does not include any control for text quality (e.g., matching on perplexity under a held-out LM, or readability scores). This limits the generality of the claim that the method detects *origin* rather than *fluency*. **Fix: include an experiment that matches human and AI texts on a quality metric to show the editing-distance gap persists, or explicitly acknowledge this limitation.**

### Minor

1. **The value of $K$ for uncertainty measurement is not specified.** Section 3.1 defines the uncertainty metric as $U = \sum_{i=1}^{K-1} \sum_{j=i}^{K} D(\x_i', \x_j')$, but the paper never states what $K$ was set to in any experiment. This affects reproducibility.

2. **Bag-of-words edit is mentioned but never used.** Section 3.2 describes bag-of-words edit distance as a measurement, but all reported results use only Levenshtein distance. It is unclear whether the bag-of-words feature was ever incorporated or tested.

3. **Classifier choice is inconsistently reported.** Table 1 does not specify which classifier was used. Table 2's caption says "We use logistic regression classifier for all ours," and Section 4 says "Logistic Regression or XGBoost." It should be stated per-table or clarified whether the classifier choice varied.

4. **The adaptive attack evaluation is thin relative to the robustness claims.** The abstract claims the method is "inherently robust on new content," and the conclusion states it is robust "when detecting text generated via prompts that aim to bypass our detection." However, Table 3 tests only two hand-crafted evasive prompts. A stronger adversary could optimize generation to maximize rewriting edits directly (e.g., via RL or supervised fine-tuning). The claim of inherent robustness is stronger than the evidence supports.

5. **Which prompts were used for the main results is not explicitly stated.** The paper lists several prompts for invariance (lines 216–220) and shows prompt-specific F1 scores in Figure 3 (bar charts), but does not state which specific prompt (or combination) was used to produce the main results in Tables 1 and 2. This should be clarified.

6. **No limitations section.** The paper would benefit from discussing: the possible quality confound, computational expense (API calls per detection), dependence on a capable rewriting LLM, and limited language coverage (English only).

### Trivial
None that rise above parser artifacts.

## Nice-to-Haves

- Reporting AUROC as the primary metric (or at minimum alongside F1) would bring the paper in line with field standards and strengthen the contribution.
- The quality confound experiment suggested in Major #3 would substantially strengthen the paper's central claim.
- A brief analysis of computational cost (approximate API calls per detection, token costs) would help readers assess practical deployability.
- Including a non-LLM baseline (e.g., fixed edit distance threshold without any ML classifier) as a sanity check for Table 5 would be informative.

## Removed Points

These points from the input reviews were considered but removed:
- **"DetectGPT uses OPT-2.7B which disadvantages it vs GPT-3.5-turbo"**: This is the standard implementation of DetectGPT (it was designed to use the same model for scoring and generation). The paper follows the standard setup. Not a genuine weakness.
- **"Missing watermarking comparison"**: The paper's scope is post-hoc detection, not watermarking. Comparing to watermarking would be outside stated scope.
- **"Figure 5 trend line is hand-drawn"**: Parser artifact; the original PDF likely has a proper regression line.
- **"Prompt ablations — how many prompts were tried"**: The paper shows 9+ prompts in Figure 3 and states they used manual prompts. This is sufficient transparency.
- **"Reproducibility details about hyperparameters and splits"**: These are standard minor omissions; the core method is simple and the Levenshtein-based features are deterministic given the prompts.

## Novel Insights

None beyond the paper's own contributions. The reviews identified evaluation gaps and a confusing methodological section but did not uncover a fundamentally new interpretation or connection that the paper itself missed.

## Suggestions

1. **Add AUROC with bootstrapped confidence intervals** to all main tables. This is the most impactful change for positioning the paper within the detection literature.
2. **Fix the equivariance prompt example.** Either use a genuine inverse pair (e.g., "make this positive" / "make this negative") or add an explanation for why the same "opposite meaning" prompt applied twice serves as an inverse in the LLM's behavior.
3. **Add a controlled experiment for the quality confound.** Match human and AI texts on perplexity under a held-out LM and show the editing-distance gap persists.
4. **State the value of $K$ for uncertainty** and clarify whether bag-of-words was used in any result.
5. **Temper the "inherently robust" claim** given the limited adaptive attack evaluation, or add stronger attacks.
6. **Add a limitations section** discussing quality confound, computational cost, and English-only evaluation.

## Score and Decision

**Round 1 bracket**: The paper sits between 4.5 and 6.5 based on comparison with anchors. The weak anchors (1.5–3.0) are rejected papers with fatal flaws. The closest topical papers — D&R (5.50, Accept Poster), Learn-to-Distance (5.50, Accept Poster), TASTE (5.00, Accept Poster) — all fall in this band.

**Round 2 narrowing**: Comparing Raidar directly to these anchors:
- vs. **D&R (5.50)**: Raidar has broader domain coverage (6 vs 4 datasets) and tests adaptive attacks, but lacks AUROC/error bars that D&R provides, and has the confusing equivariance issue. Raidar is slightly weaker.
- vs. **Learn-to-Distance (5.50)**: Raidar has a cleaner, more intuitive method and broader experiments, but lacks theoretical grounding and has evaluation gaps. Comparable or slightly weaker.
- vs. **TASTE (5.00)**: Raidar has a more novel core insight and broader experiments. Slightly stronger.

**Final score**: 5.0. The paper presents a genuinely novel and simple insight with broad experimental support, but is held back by (a) the absence of AUROC and confidence intervals, (b) a confusing equivariance definition, and (c) an unaddressed quality confound. These are fixable issues; with revisions this would be a solid contribution.

**Decision**: Accept (borderline, requiring moderate revisions).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>