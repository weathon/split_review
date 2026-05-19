- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 6, 3
Now I have verified the paper's content against the reviewer claims. Let me compose the final review.

## Summary

This paper identifies and characterizes a "crosslingual knowledge barrier" in multilingual LLMs: models that perform competitively on explicit crosslingual tasks (machine translation, embedding alignment) systematically fail to transfer knowledge acquired in one language when answering questions in another language. The paper demonstrates the barrier across six LLMs on both general knowledge (MMLU) and domain-specific knowledge (Harry Potter Quiz), tests inference-time mitigations (prompt engineering, few-shot learning) and finds them insufficient, then proposes mixed-language fine-tuning on out-of-domain data (WikiText) as a simple and effective training-time mitigation. The contribution is primarily empirical: a clean experimental design that isolates crosslingual knowledge transfer from mere multilingual capability, plus a practical mitigation method.

## Strengths

- **Controlled evaluation isolates crosslingual knowledge transfer from multilingual capability.** The paper designs mixed-language MMLU variants (mixup translation, GT-option translation) that are novel compositions unlikely to appear in pretraining, and shows systematic accuracy drops across all six models (e.g., GPT-4 drops from 81.82 to 68.61 on mixup-translated MMLU). This goes beyond prior consistency metrics (Qi et al. 2023) by measuring transfer of knowledge learned only in one language. Evidence: Section 3.1, Table `mmlu_variants`, and the specific GPT-4 numbers cited at line 115.

- **Mixed-language fine-tuning on *out-of-domain* general corpora effectively reduces the barrier.** Fine-tuning on mixed-language WikiText-103 (a general corpus with no Harry Potter overlap) improves performance both on mixup MMLU and on the Harry Potter Quiz across languages, including English. The ablation with English-only fine-tuning confirms the mixed-language aspect is responsible. Evidence: Figure `HP-mixed-fted-general` (Fig. 5), Table `mmlu_ft_fewshot_mitigation` (Tab. 4), and the discussion at lines 203–207.

- **Thorough exploration and elimination of inference-time mitigations strengthens the case for training-time intervention.** The paper tests prompt engineering (alternative option IDs, multilingual awareness instructions) and several few-shot strategies (English, same-bias, translate-then-answer), finding none close the gap. Evidence: Table `mmlu_prompt_mitigate` (Tab. 3) showing no improvement and even drops from default prompting.

- **Systematic comparison across models, languages, and tasks.** Six models (open-source and proprietary), five languages (en, fr, de, es, it), two knowledge domains (general MMLU, domain-specific HP-Quiz), and multiple translation granularities (document, sentence, word-level) are evaluated, providing broad empirical coverage.

- **Pragmatic design of mixed-language fine-tuning with ablation on translation granularity.** The paper compares document-level, sentence-level, and word-level mixing, finding word-level works best in few-shot settings while sentence-level is more effective in zero-shot — providing actionable guidance.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims (existence of a crosslingual knowledge barrier, effectiveness of mixed-language fine-tuning as a mitigation) are well-supported by the evidence presented. The limitations that exist are addressable in future work and do not threaten the paper's main conclusions.

### Minor

- **The embedding experiment (Section 2.2) provides weaker evidence than the paper's framing suggests.** The comparison between mixed-language-translated text and random-token-replaced text shows the model distinguishes meaningful translations from random perturbations, but it does not directly test whether the model *aligns* English and non-English words that share meaning. A cleaner baseline would compare against replacing translated words with random *non-English* words from the same language (controlling for the fact that any non-English token may shift embeddings differently). The paper correctly positions this as supplementary evidence (the translation results independently establish crosslingual capability), but the claim that this experiment "implies the explicit crosslingual capabilities of multilingual LLMs" (line 72) slightly oversells what the specific comparison shows.

- **The mechanism by which mixed-language fine-tuning reduces the barrier is not investigated.** The paper speculates that "frequent language switches" help (line 203) but does not test this hypothesis — e.g., by ablating the switching frequency, comparing against fine-tuning on more non-English data without mixing, or analyzing post-fine-tuning embeddings to see if alignment improved. The paper honestly acknowledges this as a limitation ("One important question that is not answered..."), so this is a gap in depth rather than a flaw in the empirical claims.

- **The behavioral bias underlying the GT-option translation results could be more thoroughly characterized.** The paper attributes the sharp performance drop in GT-option translation to models avoiding non-English options (line 116). The controlled one-wrong-option experiment supports this, but the analysis does not test asymmetry (e.g., does a non-English correct option in an otherwise all-English set still hurt?) or vary the number of non-English options to probe the bias's nature. This is a reasonable observation that could be deepened but does not undermine the main findings.

### Trivial

- **No confidence intervals or variance estimates are reported for the main accuracy results** (Tables in Section 3). Given the large test sets (~14k MMLU samples), the standard errors are small, but reporting them would be standard practice and help readers assess the reliability of observed differences (e.g., between English and mixup-translated MMLU).

## Nice-to-Haves

- **Comparison with parallel-data fine-tuning.** The paper proposes mixed-language (non-parallel) fine-tuning as a method that avoids parallel corpora. A natural baseline would be fine-tuning on a small amount of parallel data (e.g., sentence pairs from WikiMatrix) to show whether the mixed-language approach offers a different trade-off. This would help situate the method relative to existing crosslingual training techniques.

- **Analysis of embeddings after mixed-language fine-tuning.** Performing the same embedding distance analysis (Section 2.2) on post-fine-tuning models could test whether alignment between original and translated sentences improves, directly connecting the mitigation to the earlier crosslingual capability measurement.

- **Systematic investigation of the bias symmetry in GT-option translation.** Varying the number of non-English options and testing both directions (non-English correct option in English context, and vice versa) would clarify whether the bias is against non-English options specifically or a more general pattern.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not report the amount of non-English data in the original pretraining corpora"** — The critic correctly notes this is unavoidable given proprietary datasets and is not presented as a flaw in the paper. Removed because the paper cannot report what it cannot know.

- **Generic framing from Harsh Critic's section-by-section notes** — Notes like "the motivation is clearly stated" are descriptive praise without specific evidence anchor. Removed as redundant with the Strengths section.

## Novel Insights

None beyond the paper's own contributions. The reviews faithfully describe the paper's contributions and limitations but do not surface insights about the crosslingual knowledge barrier or the mixed-language fine-tuning mechanism that the paper itself does not already provide.

## Suggestions

- Provide a cleaner baseline for the embedding experiment (random non-English word substitution instead of random token replacement) to more directly test crosslingual alignment, or re-frame the experiment's claim more cautiously as showing the model treats multilingual content differently from random noise.
- Explore the mechanism of mixed-language fine-tuning: compare against fine-tuning on more non-English data (without mixing) to isolate whether mixing, versus simply adding non-English data, drives the improvement.
- Report confidence intervals for the main accuracy results (MMLU variants) to help readers assess the reliability of observed differences.
- Test the behavioral bias systematically by varying the number/proportion of non-English options, to clarify whether the avoidance pattern is symmetric.
