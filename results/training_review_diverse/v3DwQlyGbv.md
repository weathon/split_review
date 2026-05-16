Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the final consolidated review.

## Summary

This paper presents Paramanu-Ganita, a 208M-parameter decoder-only language model pretrained from scratch on 31.5B tokens of curated mathematical text/code with a domain-specific BPE tokenizer, then instruction fine-tuned on MetaMathQA. The authors argue that domain-specific pretraining from scratch is far more cost-effective than continual pretraining of large LLMs, supporting this with a claimed 135× reduction in training cost (170 vs. 23,000 A100 hours) while achieving competitive results on GSM8K (39.4%), MATH, and other math reasoning benchmarks versus models 35×+ larger.

## Strengths

- **Dramatically improved training efficiency is well-documented**: Paramanu-Ganita's total training cost of 170 A100 hours (Section 7.1, Section 10) vs. LLEMMA 7B's 23,000 A100 hours (Section 1) represents a genuine 135× reduction. This concrete cost comparison directly supports RQ2 and is a legitimate contribution regardless of evaluation fairness issues.

- **Novel domain-specific tokenizer and curated pretraining corpus**: The paper develops a merged math/code BPE tokenizer (size 17,357) with special tokens for math and code (Section 5), and constructs a mixed corpus from AutoMathText, MathPile, AlgebraStack, CoT-templatized Q&A, and in-house lecture notes (Section 4, Table 1). The careful data curation and tokenizer design are concrete, reproducible contributions.

- **Effective use of μP hyperparameter transfer**: The authors tune hyperparameters on a 15M model and transfer to 208M using maximal update parameterization (Section 7.1, Section 3.3), a practical and systematic approach that avoids expensive large-scale tuning.

- **Comprehensive multi-level evaluation across non-contaminated benchmarks**: The zero-shot evaluation on LogiQA, MMLU-math subsets, AGIEVAL-AQuA-RAT (GRE/GMAT), and AGIEVAL-SAT-Math (Table 3) demonstrates robust reasoning across difficulty levels. These results are not affected by the data contamination issue affecting GSM8K/MATH.

- **Explicit quantification of environmental sustainability**: Total training time (170 A100 hours) is concretely contrasted with LLEMMA's 23,000 hours (Section 1), making the environmental claim verifiable rather than vague.

## Weaknesses

### Fatal
None. The paper's core approach (training a small math model from scratch with domain-specific data/tokenizer) remains valid, even if the headline comparisons are confounded.

### Major

- **Data contamination from instruction fine-tuning on MetaMathQA invalidates the headline GSM8K and MATH comparisons against models not similarly fine-tuned.** MetaMathQA (Yu et al., 2024) is constructed by bootstrapping from the **training splits** of GSM8K and MATH. Paramanu-Ganita is instruction fine-tuned on MetaMathQA (Section 7.2) and then evaluated on the **test splits** of the same benchmarks. Meanwhile, the headline comparisons the paper emphasizes — outperforming LLEMMA 7B by 3% on GSM8K (Section 9), PaLM 62B by 5.94% on MATH, etc. — are against models evaluated **zero-shot or few-shot without any fine-tuning on GSM8K/MATH training data**. This conflates model capability with task-specific fine-tuning. The claim "our model outperforms LLEMMA 7B despite being 35× smaller" is structurally misleading because LLEMMA 7B was not given the same opportunity to learn from the evaluation benchmarks' training distribution. (The paper does include MetaMath and WizardMath in Table 2 — models that *were* fine-tuned on the same data — but their scores are not discussed in the body text, and they likely show Paramanu-Ganita underperforming significantly, which undermines the paper's rhetoric.) To salvage this, the authors should either (a) compare against models also fine-tuned on GSM8K/MATH training data, or (b) report the zero-shot pretrained-only performance against zero-shot LLM baselines.

- **The paper reports "the best score across our model checkpoints" for Paramanu-Ganita (Table 3 caption, line 152), while baseline scores are single values quoted from published papers.** Selecting the best checkpoint over multiple evaluations inflates results relative to baselines that report a single run. This is a form of evaluation asymmetry that should be disclosed and justified (e.g., by also reporting the final checkpoint score or the mean/std across checkpoints).

### Minor

- **No absolute accuracy is reported for MATH in the text.** The abstract and Section 9 give only percentage-point differences ("outperformed the various models by 6-8% points") for MATH, never the model's own absolute score. The GSM8K absolute score (39.4%) is given in the introduction, but MATH's is absent from all running text. The tables are garbled by the parser, so the numbers cannot be verified from the extracted paper. This omission makes it impossible to compare with future work.

- **Evaluation protocol for Table 3 (multiple-choice benchmarks) is underspecified.** The paper states "Zero-shot evaluation of Paramanu-Ganita 208M and LLMs" (Table 3 caption) and "using lm-eval-harness at zero-shot greedy decoding setting" (line 154). However, it is unclear whether the comparison LLMs' scores were also obtained via zero-shot lm-eval-harness evaluation or are quoted from published papers — many of which (e.g., LLaMA-2's MMLU scores) are standardly reported at 5-shot. If the scores are from published few-shot results, the zero-shot comparison is invalid. If re-evaluated, the paper must state this explicitly.

- **Overclaimed novelty: "We are the first to show that such an approach works" (Section 10).** Prior work on training small models from scratch on high-quality data (e.g., Phi-3, TinyStories, Sultan & Turney 2019) already demonstrated that small models can achieve strong performance on focused domains. The novelty lies in the math-specific focus, the tokenizer, and the cost quantification — not in being "first" to show that small domain models can work. This claim should be softened.

- **"Best score across checkpoints" selection without variance reporting.** For Table 3, reporting only the best checkpoint without confidence intervals or standard deviations makes it impossible to assess whether the reported improvements are statistically significant. Greedy decoding is deterministic per checkpoint, but different fine-tuning seeds or checkpoints could yield different results.

### Trivial

- The model architecture description appears twice verbatim (lines 15-16 and 17-20), a drafting error that should be cleaned up.

- MFU is reported as "40.392" (line 105) — typical precision for MFU is to one decimal place; the extra digits are unnecessary and suggest over-precision.

## Nice-to-Haves

- **Ablation on the specialized tokenizer**: Comparing tokenization efficiency (tokens per math expression) and downstream accuracy after pretraining with a standard BPE tokenizer vs. the merged math/code tokenizer would strengthen the claim that the tokenizer matters (Section 5).

- **Comparison with similarly sized models**: Adding comparisons with other small models (e.g., GPT-2 1.5B, OPT 350M, TinyLlama 1.1B) fine-tuned on MetaMathQA would isolate the effect of the pretraining data/tokenizer from the advantage of being small.

- **Zero-shot (pretrained-only) evaluation on GSM8K/MATH**: Reporting the model's performance before instruction fine-tuning would provide a fairer baseline against zero-shot LLM scores and help disentangle the effect of pretraining from instruction fine-tuning.

- **Perplexity on math-specific held-out text**: Reporting perplexity on held-out mathematical text (instead of only downstream accuracy) would directly measure the model's language modeling quality in the domain.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Duplicated sentences are a drafting error"** — Removed per hard rules on pure formatting/style nitpicks. (Kept in Trivial as a minor content issue, but the severity is negligible.)

- **"Missing raw scores for MMLU-math-college and AGIEVAL-SAT-Math"** — These are likely in the garbled tables (Table 3) which are parser artifacts. The MATH absolute score is genuinely missing from text, which I kept in Minor.

- **"No control for data overlap between fine-tuning and evaluation"** — This is subsumed under the data contamination Major weakness; keeping as a separate point would be redundant.

- **"Carbon footprint quantification"** — The paper's qualitative mention is sufficient for a first demonstration; a detailed calculation would be nice but is not a weakness.

- **"Missing comparison with similarly sized models"** — Moved to Nice-to-Haves. The paper's stated scope is comparing against much larger LLMs to test the "bigger means stronger" hypothesis.

- **Strength: "Competitive or superior results despite being 35× smaller"** — Removed because this conflicts with the verified data contamination weakness, per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewer insights collectively surface a genuine evaluation fairness problem (MetaMathQA data contamination) that the paper does not address. The observation that the paper selectively highlights comparisons against models not fine-tuned on GSM8K/MATH training data while silently including MetaMath/WizardMath (which likely outperform Paramanu-Ganita) in the table is an important structural criticism. However, this is a flaw in the paper's presentation, not a novel research insight.

## Suggestions

1. **Restructure the evaluation to be fair**: Either (a) report zero-shot pretrained-only results against zero-shot LLM baselines, or (b) foreground the comparison against models also fine-tuned on GSM8K/MATH training data (MetaMath, WizardMath, MAmmoTH). The latter would honestly show that a 208M model approaches (but does not surpass) 7B models after equivalent fine-tuning — still an impressive result given the 135× cost reduction.

2. **Report absolute accuracy for every benchmark in the text**, not only percentage-point differences.

3. **Clarify the evaluation protocol for Table 3**: State for each comparison model whether the score was obtained via zero-shot lm-eval-harness or quoted from published work, and if quoted, note the prompting setup used in the original paper.

4. **Disclose and justify the "best checkpoint" selection policy** and also report the score from the final training checkpoint or a mean across checkpoints.

5. **Add a discussion of the data overlap between MetaMathQA and the evaluation benchmarks**, and acknowledge this as a limitation of the current comparison.

6. **Tone down the "first to show" novelty claim** in Section 10 and focus on the specific contributions (math domain, tokenizer, cost quantification) that are genuinely novel.

## Score and Decision

The paper tackles a worthwhile question and has genuine contributions in terms of the pretraining pipeline, domain-specific tokenizer, and cost analysis. However, the central evaluation is significantly compromised by the data contamination issue: fine-tuning on MetaMathQA (derived from GSM8K/MATH training splits) while comparing against models evaluated zero-shot on the same benchmarks makes the headline claims structurally misleading. The paper also cherry-picks checkpoints and omits absolute MATH accuracy. These are fixable issues, but in the current form the evidence does not fairly support the claimed conclusions.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>