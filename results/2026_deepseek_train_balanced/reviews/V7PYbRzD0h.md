## Summary

This paper introduces Chain-of-Jailbreak (CoJ), a multi-turn attack that decomposes a single malicious query into a sequence of seemingly harmless sub-queries executed through iterative editing operations (delete-then-insert, insert-then-delete, change-then-change-back). The authors construct CoJ-Bench (150 seed queries, 776 test sequences across 9 safety scenarios) and evaluate on GPT-4V, GPT-4o, Gemini 1.5, and Gemini 1.5 Pro, reporting 27–62% jailbreak success rates. A secondary contribution, Think-Twice Prompting, is proposed as a defense.

## Strengths

- **CoJ demonstrates a large and meaningful empirical gap over single-turn prompt attacks.** On 50 randomly selected seed queries, CoJ achieves 60–86% jailbreak success across all four models, while the best single-prompt baseline (refusal suppression) reaches only 14% on GPT-4V and ≤12% on the others (Table, lines 282–298). This large gap provides concrete evidence that multi-turn editing exploits a qualitatively different vulnerability than existing single-prompt jailbreak paradigms.

- **Systematic analysis of which factors drive attack success.** The paper decomposes results by edit operation (Insert-then-Delete most effective at 49% avg, with an explanation that it operates on benign tokens like "not" rather than sensitive keywords — lines 352–354), edit element (word-level 51% avg vs. char-level 39% and image-level 39% — Table, lines 357–372), editing steps (longer chains improve success — Figure, lines 378–384), and safety scenario (animal abuse 58% vs. child abuse 32% — Figure, lines 301–306). This granularity provides actionable insight into specific safeguard failure modes.

- **Dual human + automatic evaluation with consistent trends.** Both human annotation (three annotators, majority voting) and GPT-4-based automatic evaluation show similar trends across models (line 257), and the absolute JSR values are consistent (e.g., GPT-4o: 62.3% human vs. 64.6% auto — Table, lines 241–252). This methodological triangulation strengthens confidence in the reported results.

- **Evaluation on real, widely-deployed commercial services with default settings.** Experiments are conducted on GPT-4V, GPT-4o, Gemini 1.5, and Gemini 1.5 Pro via their official websites with default configurations (line 227), directly demonstrating practical threats to production systems.

## Weaknesses

### Fatal
None.

### Major

- **The headline comparative claim is not supported by the baselines selected.** The paper claims CoJ "significantly outperforms other jailbreaking methods" (abstract, line 9), but the experimental comparison (Table, lines 282–298) is limited to five single-prompt attack variants (instruction ignore, refusal suppression, etc.). The paper itself cites Deng et al. (2023) "Divide-and-Conquer" and Yang et al. (2023) "SneakyPrompt" in Related Work (line 444) — both are multi-step attack methods that decompose malicious intents — yet neither is included as an experimental baseline. Deng et al.'s method is the most directly comparable: it also decomposes an unethical drawing intent into multiple benign descriptions. Without this comparison, the paper cannot support the claim that CoJ outperforms *other jailbreak methods* generally; it only shows that CoJ outperforms trivial single-prompt methods. The conclusion may be correct, but the evidence as presented does not establish it. This is the most significant weakness in the paper.

- **The defense evaluation is too thin to support the claims made for it.** Think-Twice Prompting is tested on only 40 test cases (line 412) — cases selected because they "can successfully jailbreak all the models." The defense achieves 93–100% defense success on this sample (Table, lines 419–433). However: (1) the sample is very small; (2) the defense is tested only against CoJ attacks, so generalization to other attack types is unknown; (3) there is no evaluation of over-refusal rates on benign queries — a defense that blocks 97% of CoJ attacks but also blocks 30% of legitimate requests is not practically usable, and the paper provides no data on this. The paper presents the defense as a contribution (line 10: "can successfully defend over 95% of CoJ attack"; line 481: "effective prompting-based defense strategy"), but the evidence is insufficient to support these claims.

### Minor

- **The generalization of the attack from text-slogan images to general images is insufficiently detailed.** The method is introduced entirely through text-slogan examples (lines 72–107), with edit operations derived from Levenshtein distance on strings. The extension to "Image-level" editing (Section 3.2, line 115) is described in only two sentences with two examples ("change the flowers into a weapon" and inserting a logo). The prompt used to instruct Mistral-Large-2 for automatic decomposition is not provided (line 171), so the reader cannot assess how the decomposition process handles non-text content. The paper reports per-element results (word 51%, image 39%, char 39%) but does not break down what fraction of the 776 test cases target text slogans vs. general images, making it difficult to assess the scope of the demonstrated vulnerability.

- **No inter-annotator agreement metric is reported for the human evaluation.** The paper employs three annotators with majority voting (lines 184–186) for subjective judgments across sensitive categories (child abuse, hate speech, etc.), but no Cohen's kappa or similar metric is reported to establish reliability.

- **No statistical variance or confidence intervals are reported for any result.** All jailbreak success rates are presented as point estimates without standard deviations, confidence intervals, or significance tests. Given the modest per-category sample sizes, this limits the reader's ability to assess the reliability of reported differences (e.g., between edit operations or models).

### Trivial

- The footnote dismissing Stable Diffusion and Midjourney because "their safeguards are too weak and do not need to jailbreak" (line 226) is asserted without demonstration. Including them would provide a useful upper-bound comparison.
- No limitations, failure-case analysis, or dual-use discussion is included despite the paper introducing an effective attack on commercial services.

## Nice-to-Haves

- Including Deng et al.'s Divide-and-Conquer and/or SneakyPrompt as comparative baselines would directly validate the paper's claimed novelty and make the contribution much stronger.
- Providing the full decomposition prompt used with Mistral-Large-2 would significantly improve reproducibility.
- A breakdown of results by text-slogan vs. general-image type would clarify the method's scope.

## Removed Points

The following points from the inputs were filtered:
- **Criticism about the defense being "obvious" or "essentially the obvious fix"** — this is a judgment about contribution novelty, not a specific weakness of the paper. The paper does not claim the defense is architecturally novel, only that it is effective. Removed as opinion-driven rather than evidence-based.
- **Strength about "novelty of exploiting multi-turn image editing for jailbreak"** — this is a positional claim rather than a concrete, evidence-grounded strength. It conflicts with the verified weakness about missing comparative baselines that would validate this novelty. Moved here.
- **Strength about Think-Twice Prompting providing "near-complete defense"** — this conflicts with the verified weakness about the defense evaluation being insufficiently scoped (N=40, no over-refusal test). Moved here.

## Novel Insights

The review process surfaces no genuinely novel insight beyond the paper's own contributions. The observation that Insert-then-Delete is the most effective operation because it edits benign tokens (e.g., "not") rather than sensitive keywords (Section 5.3) is a genuine insight already in the paper.

## Suggestions

1. **Add the most directly relevant multi-step baselines (Deng et al.'s Divide-and-Conquer, SneakyPrompt).** This is the single highest-leverage improvement — it would directly validate whether the multi-turn editing approach provides benefits over single-round decomposition of malicious intents.
2. **Provide the full decomposition prompt** used with Mistral-Large-2 for reproducibility.
3. **Expand the defense evaluation** to include over-refusal rates on benign queries and testing against at least one additional attack type. Alternatively, reframe the defense section as preliminary exploration rather than a claimed contribution.
4. **Report inter-annotator agreement** (Cohen's kappa or similar) for the human evaluation.
5. **Add confidence intervals or variance estimates** for the main results.
6. **Clarify the scope** by reporting what fraction of test cases involve text slogans vs. general images, and provide examples of image-level decomposition across different safety scenarios.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>