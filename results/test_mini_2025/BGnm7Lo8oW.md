Now I have sufficient calibration context. Let me write the consolidated review.

## Summary

This paper investigates reward function design for self-improving Chain-of-Thought (CoT) reasoning on unstructured text — a challenging setting where accuracy-based rewards are unavailable. The authors identify desirable criteria for reward functions, empirically analyze how different functions affect *what* reasoning is rewarded and *where* reasoning is placed (on FineWeb text and curated QA), and propose Reasoning Advantage (RA), which combines clipping, an empty-CoT baseline, and normalization. They introduce MMLU-FREE-FORM as an intermediate benchmark bridging curated QA and unstructured text, and show that RA is the only reward function tested that enables self-improvement on it, with zero-shot transfer gains of ~7% on GSM8K. An exploratory experiment on OpenWebMath fails; the authors diagnose insufficient CoT diversity as the bottleneck. The paper is a method+analysis contribution that does not solve the full problem but provides useful diagnostics and a demonstrably better reward function for a stepping-stone setting.

## Strengths

1. **Novel disaggregated analysis of reward function behavior.** Section 5.1's *what*/*where* experiments are the first systematic dissection of how different reward functions handle the twin challenges of identifying good reasoning and placing it at useful locations. Table 2 quantifies the gap: RA achieves 66.3% accuracy on *what* classification vs. 44.6% for standard loss, and 77.0 AUC on *where* selection vs. 39.4 for standard loss. This decomposition is a genuine analytical contribution that clarifies *why* loss-based rewards fail on unstructured text.

2. **Demonstration that RA uniquely enables self-improvement on free-form QA.** On MMLU-FREE-FORM (Section 5.2, Figure 2), RA is the only reward function that produces sustained improvement on both the in-domain test set and zero-shot transfer to GSM8K (nearly 7% improvement), while standard loss, delta loss, and random selection plateau quickly. The transfer result is particularly strong evidence of genuine reasoning gains rather than surface-level pattern matching.

3. **MMLU-FREE-FORM as an intermediate benchmark.** The adaptation of MMLU by stripping multiple-choice options creates a useful testbed that preserves many challenges of unstructured text (free-form answers, verification difficulty, multiple valid phrasings) while offering higher density of reasoning opportunities. The paper commits to releasing it, and the benchmark fills a real gap between curated QA and full pretraining-scale data.

4. **Honest treatment of failure on OpenWebMath.** Section 6 openly reports that the RA+offline-RL pipeline fails on real unstructured text, diagnoses the bottleneck as insufficient CoT diversity (only 0.01% of generated CoTs pass RA's threshold), and suggests concrete directions (Quality-Diversity methods, online RL). This transparency is valuable for a community still figuring out the scope of the problem.

5. **Well-motivated reward function design principles.** The criteria identified in Section 4 (no external intelligence, rewards good over random reasoning, robust to multiple answers and answer perplexity, fast and parallelizable) are clearly articulated, and the paper systematically evaluates all relevant loss-based variants against them.

## Weaknesses

### Fatal

None.

### Major

1. **Positive self-improvement results are confined to a single synthetic setting.** The only successful self-improvement experiment uses MMLU-FREE-FORM — a dataset the paper explicitly constructs to make the problem easier (dense reasoning opportunities, known format, limited domain). The *what*/*where* analyses (Section 5.1) use real text from FineWeb but evaluate static reward-score quality, not actual self-improvement. The only full self-improvement attempt on real unstructured text (OpenWebMath, Section 6) fails. This creates a genuine gap between the paper's broader framing ("reward functions for self-improving general-purpose reasoning") and what is actually demonstrated. The paper is transparent about this, but readers should evaluate it as a stepping-stone contribution toward the grand challenge, not a solution to it.

2. **The OpenWebMath failure diagnosis is undersupported.** Section 6.1 attributes the failure to "lack of diversity in generated CoTs" based on a single statistic (0.01% of CoTs above the RA threshold) and anecdotal examples of conservative CoTs. No diversity metrics (embedding distances, n-gram overlap, number of distinct reasoning strategies) are provided, and alternative explanations are not systematically explored (e.g., the RA threshold being inappropriate for OpenWebMath's distribution, distribution collapse inherent in offline RL regardless of diversity, document-specific sensitivities of the empty-CoT baseline). Since the paper's main message for future work ("investigate methods for generating a more diverse set of CoTs") is directly derived from this diagnosis, stronger evidence is needed to ensure the recommendation is well-founded.

### Minor

3. **No theoretical analysis of *why* RA works.** The paper motivates RA's components (clipping, empty-CoT baseline, normalization) empirically but offers no analytical argument for why clipping bounds the influence of outlier tokens or why normalization by the empty-CoT baseline filters trivial locations. A simple theoretical justification (e.g., showing that clipping ensures the per-token loss contribution is bounded, or that the baseline subtracts the "background" predictability of the suffix) would significantly strengthen the contribution.

4. **The *what*/*where* experiments use only one model (Mistral-7B-Instruct) for computing rewards, and CoTs are generated by GPT-4o.** Using the same model for generation and evaluation would more closely match the self-improvement loop. Additionally, the "random" CoT baseline (random word strings) is an easy negative; while the paper correctly notes that the key finding is loss's inability to separate incorrect from random CoTs, a syntactically plausible but semantically wrong baseline would be a stronger test.

5. **The empty-CoT baseline's behavior on long documents is not discussed.** Running the model with no CoT on a long prefix-suffix pair may not be a well-defined operation — the model was finetuned on sequences *with* CoT tokens, and the base model's ability to predict long suffixes with zero context is undocumented. This assumption merits discussion.

### Trivial

None.

## Nice-to-Haves

- A scatter plot or trade-off curve showing *what* accuracy vs. *where* AUC for all reward function variants (including the non-normalized RA that does slightly better on *what* but worse on *where*) would give a fuller picture of the design space.
- Varying the temperature or prompt for CoT generation in the OpenWebMath experiment and measuring whether diversity increases (and whether more CoTs pass the RA threshold) would directly test the diversity-bottleneck hypothesis.
- Comparing RA with a softmax-normalized variant (instead of division by baseline) would help isolate whether normalization's benefit is from the specific form or simply from relative scaling.

## Removed Points

- **Criticism: "MMLU-FREE-FORM results may reflect format learning rather than reasoning improvement."** REMOVED. All experimental conditions receive the same initial finetuning to learn the [THOUGHT] format and use the same format during training. RA passes *fewer* training CoTs (1000 steps) than other conditions yet produces *better* generalization, which is inconsistent with a format-learning explanation. Moreover, the zero-shot transfer to GSM8K (a different dataset with a different task distribution) cannot be explained by format learning alone. The paper's control for this confound is adequate.
- **Criticism: "Main table lacks confidence intervals."** REMOVED. Table 2 explicitly states "See Appendix B.1 for full results and confidence bounds." The appendix is removed by the PDF parser, not omitted by the authors.
- **Criticism about missing related work, typos, formatting, unresolved hyperparameters.** REMOVED per policy: these are either parser artifacts, out-of-scope checks, or apply to every conference submission.

## Novel Insights

The harsh critic correctly notes that the paper's strongest result (RA on MMLU-FREE-FORM) operates in a setting that is "synthetic" relative to the ultimate goal of unstructured text. This is not a novel observation given the paper's own framing. However, one insight that emerges from reading the reviews together is that the paper's *what*/*where* decomposition may be more valuable than the specific RA recipe: the analysis framework provides a vocabulary for diagnosing reward function failures that could outlast RA itself. Future methods might improve on RA, but the *what*/*where* lens for understanding reward behavior is likely to remain useful.

## Suggestions

1. Strengthen the OpenWebMath failure analysis with quantitative diversity metrics (embedding diversity, n-gram overlap, number of distinct reasoning patterns per location). Vary temperature and prompting strategy to test whether diversity is indeed the bottleneck.
2. Add a brief theoretical justification for RA's components — even a few lines showing that clipping bounds per-token influence and that the empty-CoT baseline subtracts "background" predictability would significantly strengthen the paper.
3. Where possible, use the same model for CoT generation and reward evaluation in the *what*/*where* experiments to better match the self-improvement loop.
4. Tone down claims about "general-purpose reasoning" to match what is empirically demonstrated. The introduction and conclusion could more precisely scope the contribution to analysis + intermediate-benchmark demonstration.

## Score and Decision

**Calibration Report**

Round 1 (bracketing):
- Low band (<3.5): pXIbcRPxWR.md (2.50), aYYZBPoSHb.md (3.40), 9LAqIWi3QG.md (3.00), 79tJB1eTmb.md (3.00) — all rejected/withdrawn. Our paper clearly exceeds this band.
- Middle band (3.5–7.5): RFqeoVfLHa.md (6.50, Poster), 2ea5TNVR0c.md (6.50, Poster), LIW88mwqgv.md (5.00, Withdrawn/Reject), A6Y7AqlzLW.md (7.14, Spotlight).
- High band (>7.5): CjwERcAU7w.md (8.00, Oral), rfdblE10qm.md (8.00, Oral), mMPMHWOdOy.md (8.00, Oral), bNt7oajl2a.md (8.00, Oral). Our paper clearly below this band.

Round 1 bracket: **5.0–6.5**.

Round 2 (narrowing):
- LBJ (5.00, Reject) — Iter-CoT: surface-level incremental method, limited novelty. Our paper is substantially more insightful.
- cPgh4gWZlz.md (6.00, Poster) — Chain-of-Knowledge: clean framework, thorough experiments, moderate novelty concerns. Similar quality to our paper — both are solid analysis+method papers with clear contributions.
- w6nlcS8Kkn.md (6.67, Poster) — To CoT or not to CoT?: broad meta-analysis over 100 papers, 20 datasets, 14 models. Stronger empirical breadth than our paper.
- RFqeoVfLHa.md (6.50, Poster) — Self-Improvement Reversal: comprehensive experiments on diverse tasks, clear findings. Slightly stronger empirical breadth than our paper.

Our paper falls between the 5.0 (rejected) anchors and the 6.5 (poster) anchors. It is clearly above Iter-CoT (5.0) and comparable to Chain-of-Knowledge (6.0), but below the breadth of the "To CoT" paper (6.67) and "Self-Improvement Reversal" (6.50). The main reason is that the only successful self-improvement experiment is on a synthetic dataset, and the OpenWebMath diagnosis lacks rigor. However, the *what*/*where* analysis framework and the honest failure analysis provide real value that distinguishes the paper from weaker entries.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>