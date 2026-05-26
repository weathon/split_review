Here is my consolidated review after thoroughly reading the paper and cross-validating every reviewer claim against the actual text.

---

## Summary

This paper investigates whether translating English LLM benchmarks into Arabic can act as a natural barrier against data contamination. The authors fine-tune four small open-weight models on varying proportions of Arabic-translated test data (MMLU, XQuAD, MLQA) combined with the original English test sets, then evaluate on the English benchmarks and apply a TS-Guessing memorization probe with choice reordering. They find that MMLU accuracy rises with contamination level and that TS-Guessing detects memorization signals even through translation. The paper also outlines an untested Translation-Aware Contamination Detection (TACD) framework. The research question—whether translation masks contamination—is important and underexplored, but the experimental design does not cleanly isolate the effect of contamination-through-translation from direct English contamination, and a key analytical claim in Section 4.2 is internally contradicted by the paper's own data.

---

## Strengths

**1. TS-Guessing with choice reordering provides a useful methodological extension.**
The paper extends TS-Guessing (Deng et al., 2024) by adding a choice-reordering step for MMLU and measuring the Index Recall Rate (IDR). Table 3 shows that IDR varies meaningfully across contamination levels (e.g., LLaMA-3.2-1B IDR jumps from 0.287 at 10% to 0.643 at 50%), providing a signal that standard accuracy metrics alone would miss. This is a concrete, reusable methodological contribution for future contamination audits.

**2. Controlled comparisons reveal task-dependent contamination dynamics.**
The comparison of MMLU (closed-book MCQ) versus XQuAD/MLQA (extractive QA) shows that contamination affects these tasks differently: MMLU rises monotonically with contamination across all models, while extractive QA performance is often non-monotonic (e.g., Gemma-3-1B-it MLQA peaks at 10% then declines). This nuanced finding—backed by Table 2—is a genuinely interesting observation that complicates the assumption that contamination uniformly inflates all metric types.

**3. The paper identifies a genuine gap in current contamination detection practices.**
The argument that English-centric contamination checks may miss contamination when benchmarks are translated (Section 4.2, Section 5) points to a real and underappreciated problem. The paper's framing of this blind spot is clear and well-motivated, even if the experimental evidence for its severity is incomplete.

---

## Weaknesses

### Fatal
None. The experimental design is flawed but not irredeemable; the paper still yields partial insights.

### Major

**1. The experimental design cannot isolate translation-mediated contamination from direct English contamination.**
The training condition for every model and every contamination level is defined as

$$\mathcal{D}_{\text{train}}^d(p) = \mathcal{D}_{\text{EN}}^d \cup \mathcal{D}_{\text{AR}}^d(p),$$

where $\mathcal{D}_{\text{EN}}^d$ *is the English test set itself* (Section 3.1, p. 4). The $p=0$ condition ("EN-only") is therefore already a model fine-tuned on the exact evaluation benchmark. Across all conditions, the model sees the English test items directly.

This means the paper never establishes a scenario where contamination is introduced *only through translation*. Every observed effect is a joint effect of direct English exposure plus Arabic-translated exposure. The core claim that "translation conceals traditional contamination signals, creating a dangerous blind spot" (Abstract, Introduction, Conclusion) requires showing that a model contaminated *solely* through translation would evade English-centric detection. The paper's design cannot deliver this evidence. The results can only speak to the *additional* effect of translated data on top of already-seen English test content.

**2. Section 4.2 makes an analytical claim that is directly contradicted by the paper's own data and by Section 4.1.**
Section 4.2 states: *"Across contamination levels $p \in \{10, 50, 100\}\%$, the models exhibit approximately equal performance on all evaluated benchmarks. This near-flat trend indicates that Arabic→English translation is effectively masking contamination effects."* (p. 6). This is factually inconsistent with Tables 2 and 3a:

- **MMLU (Table 2):** Mistral-7B moves 0.580→0.690→0.690 across $p=10,50,100\%$ (a relative increase of ~19%). LLaMA-3.2-1B moves 0.381→0.389→0.431. All four models show a monotonic MMLU increase across these levels, which Section 4.1 itself describes as *"a generally monotonic increase"* (p. 6).
- **XQuAD (Table 2):** Mistral-7B XQuAD collapses 0.455→0.272→0.114. Qwen3-1.7B XQuAD moves 0.429→0.510→0.564.
- **TS-Guessing IDR (Table 3a):** LLaMA IDR jumps 0.287→0.643→0.410; Gemma IDR drops 0.350→0.029→0.005.

None of these trends are "approximately equal" or "near-flat." The paper's primary analytical argument about "masking" is grounded in a description that its own evidence refutes. This undermines the central interpretive claim of Section 4.2 and, by extension, one of the paper's headline conclusions.

### Minor

**3. The TS-Guessing procedure for MMLU is underspecified.**
Section 3.3 describes: *"(i) randomly shuffle choices (A,B,C,D), then (ii) mask the text of one incorrect answer and prompt the model to fill the mask."* The IDR metric measures whether the model's *predicted letter/index* matches the pre-shuffle correct answer letter. However, if the prompt asks the model to fill a mask (a text-completion task), how is a letter prediction extracted? The paper does not specify the prompt format, the decoding strategy, or how the model's text output is mapped to an index prediction. This creates a reproducibility gap.

**4. The TACD framework is proposed but not implemented or evaluated.**
Section 5 outlines a "Translation-Aware Contamination Detection" framework, but the paper explicitly calls it *"a forward-looking blueprint rather than a complete implementation"* (p. 8) and provides no experimental validation. While a forward-looking discussion is acceptable, the paper presents TACD as a contribution in the abstract and introduction without any evaluation. The practical contribution is therefore speculative.

**5. No variance or confidence estimates are reported.**
Tables 2 and 3 present single-point estimates with no error bars, confidence intervals, or measures of variability. Given small model sizes (1B–7B parameters) and the substantial non-monotonic fluctuations in the data (e.g., Qwen3-1.7B MLQA: 0.409→0.157→0.153 across $p=10,50,100\%$), it is difficult to assess which differences reflect genuine effects versus noise.

**6. Models are limited to small scales (1B–7B) with limited Arabic proficiency analysis.**
The paper cites Li (2023) showing that larger models exploit contamination more effectively, yet only tests models at 1B–7B scale. The claim in the Abstract about *"models with stronger Arabic capabilities"* is not substantiated by any analysis of the models' pre-existing Arabic proficiency or how it correlates with the observed effects.

### Trivial
None.

---

## Nice-to-Haves

- A true non-contaminated baseline condition (e.g., fine-tuning on unrelated data or on Arabic-only data without the English test set) would allow the core research question to be answered.
- An ablation removing $\mathcal{D}_{\text{EN}}^d$ from the training data would separate direct English contamination effects from translation-mediated effects.
- Variance estimates (e.g., bootstrap confidence intervals or results across multiple random seeds) would substantially strengthen the quantitative claims, especially given the non-monotonic patterns.

---

## Removed Points

The following points from the reviewer inputs were removed per filtering rules:

1. **"Literature Review is disproportionately long"** (Harsh Critic, Section-by-Section). This is a subjective style judgment about section length, not a substantive weakness. The paper is about contamination, and a 2.5-page review of contamination literature is within scope.

2. **Strength 5 from Strength Finder** ("Proposal of TACD framework as a concrete, actionable direction"). This conflicts with verified weakness #4 (TACD is not evaluated). Per the rule that a verified weakness overrides a conflicting strength, this is removed.

---

## Novel Insights

The combination of the two reviewer inputs surfaces a tension not fully articulated by either alone: the paper's TS-Guessing results (Table 3) actually provide the strongest evidence for the paper's thesis, yet they are given less interpretive weight than the flawed "near-flat trend" argument in Section 4.2. The IDR results—especially the large swings (LLaMA IDR 0.287→0.643, Gemma IDR 0.350→0.005)—show that the Arabic contamination level *does* affect memorization signals in a way that accuracy metrics alone would not capture. This is the paper's real empirical contribution, and it is obscured by the unsupportable "approximately equal" framing. A reframed paper that focuses on IDR as a detection signal for cross-lingual contamination, drops the unsupported "near-flat" claim, and adds a control condition without the English test set would be considerably stronger.

---

## Suggestions

1. **Redesign the experiment** to include a $p=0$ condition that is a true non-contaminated baseline (no English test set seen). The central comparison should be between a model fine-tuned *only* on Arabic-translated test data and a model fine-tuned on unrelated data. This would directly test whether contamination through translation alone evades English-centric detection.

2. **Correct the internal inconsistency in Section 4.2.** Either revise the "approximately equal" / "near-flat" claim to honestly describe the observed variation, or provide a quantitative criterion for "flatness" (e.g., effect size thresholds) and apply it consistently.

3. **Specify the TS-Guessing prompt format and decoding procedure** in detail, including how the model's text output is mapped to the index prediction used by IDR.

4. **Add variance estimates.** Even a single additional random seed or bootstrap resample would help distinguish signal from noise in the non-monotonic trends.

---

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>