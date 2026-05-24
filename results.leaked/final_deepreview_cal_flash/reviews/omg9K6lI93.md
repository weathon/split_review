Now I have a thorough understanding of the paper and the calibration anchors. Let me write my final consolidated review.

## Summary of Calibration

**Round 1 — Bracketing:**
- Low band (< 3.5): Anchors averaged 2.0–3.0 (e.g., "Llamas (mostly) think in English", 3.00; "Industrial Benchmarking of LLMs", 3.00)
- Middle band (3.5–7.5): Anchors ranged 4.25–6.75 (e.g., "Evading Data Contamination Detection", 4.25; "How much can we Forget", 6.75)
- High band (> 7.5): Anchors ranged 7.75–8.00 (e.g., "Training on the Test Task", 8.00; "Cheating Automatic LLM Benchmarks", 7.75)

**Initial bracket:** The paper has a fatal design flaw but an interesting question. It is clearly below the strong papers in the high band. It is also below the methodologically sound middle-band papers like "How much can we Forget" (6.75). The most comparable middle-band anchor is "Evading Data Contamination Detection" (4.25), which studies a similar topic (evading contamination detection) but has a cleaner experimental design. I place the initial bracket at **2.5–4.5**.

**Round 2 — Narrowing within bracket (2.5–4.5):**
- "Evading Data Contamination Detection" (4.25): Similar topic (evading contamination detection via rephrasing). Cleaner experimental design. Criticized for lack of depth. Our paper has a more interesting question but a more severe design flaw. → Our paper is weaker.
- "Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts" (4.25): Methodologically sounder approach to contamination measurement. → Our paper is weaker.
- "All Languages Matter: On the Multilingual Safety of LLMs" (3.50): Multilingual evaluation paper with methodological concerns and a rejected decision. Comparable overall quality. → Our paper is slightly weaker due to the fatal baseline flaw.
- "LLM Detectors Still Fall Short" (3.80): Thorough, well-scoped paper about LLM detection. → Our paper is comparable or slightly weaker.

After Round 2, the paper sits near the **lower end** of the bracket, closer to 3.0 than to 4.25. The fatal design flaw (training on the English test set in ALL conditions) is more severe than the weaknesses in any of the 3.5–4.25 anchors.

**Final score: 3.0 / Decision: Reject**

Now let me write the review.

Let me go through the rules carefully:

1. **Issue 1 (Baseline fatally contaminated)**: This is verified from the paper itself. D_EN includes "English test items formatted as MCQ" for MMLU. ALL conditions include the English test set. The paper claims "0% contamination" for p=0 but it's actually 100% contaminated with the English test set. This is a genuine fatal flaw. KEEP.

2. **Issue 2 (Prose contradicts data)**: Verified. Section 4.2 says "approximately equal performance" and "near-flat trend" across p∈{10,50,100}, but Table 2 shows Mistral MMLU jumping from 0.580 to 0.690 (19% relative increase). KEEP as major.

3. **Issue 3 (Missing p=0 for TS-Guessing)**: Verified. Table 3 only has p∈{10,50,100}. Without p=0, can't tell if probe works. KEEP as major.

4. **Issue 4 (TS-Guessing vs performance tension)**: Verified. Near-zero TS-Guessing scores vs large performance gains. Never addressed in paper. KEEP as major.

5. **Issue 5 (Scope mismatch)**: The paper discusses pre-training contamination in the lit review but tests fine-tuning. However, the paper is clear about its experimental paradigm (fine-tuning). This is a framing issue but not fatal. I'll soften this: it's a minor weakness about framing, not a fatal flaw. WEAKEN to minor.

Now let me also evaluate the Strength Finder's claims:

Strength 1: "Identifies that translation masks contamination signals while preserving memorization." - This is undermined by the baseline issue. But the MMLU increases are still real. I'll keep it but weaken.

Strength 2: "Extends TS-Guessing with choice-reordering" - This is a genuine methodological contribution. KEEP.

Strength 3: "Demonstrates the effect across multiple architectures" - Valid. KEEP.

Supporting strength 1 (TACD framework) - The TACD is described as a "blueprint" without implementation. This is more of a future direction than a contribution. I'll move it to minor strength or nice-to-have.

Supporting strength 2 (controlled fine-tuning) - This is a standard setup. Not a strength per se. I'll drop this.

Let me also check for any other rules:
- REMOVE any criticism that questions the existence of cited models/tools: None of the criticisms do this.
- REMOVE factual errors or misunderstandings: Let me check each.
  - Issue 1: The critic says "fine-tuned on the exact benchmark it is later evaluated on." The paper says D_EN is "English test items." This is correct. KEEP.
  - Issue 5: The critic says the paper doesn't generalize to pre-training. But the paper's experiments are about fine-tuning. The paper IS clear about this. I'll WEAKEN this.
- REMOVE formatting/style nitpicks: None in the criticisms.
- REMOVE reproducibility nitpicks: None in the criticisms.
- REMOVE strawman weaknesses: Issue 5 could be seen as demanding the paper address something outside its scope. The paper clearly says "we fine-tune" in the abstract. But the lit review does discuss pre-training contamination extensively, so the critic's point about framing mismatch has some merit. I'll WEAKEN it but not REMOVE.

Let me now write the final review.

Actually wait, I need to check one more thing. Is the harsh critic right that D_EN is the TEST set and not the training set? Let me check.

For MMLU: "English test items formatted as MCQ" - these are items from the MMLU test set.
For XQuAD/MLQA: "English QA" - these are the English side of the parallel XQuAD/MLQA datasets.

For MMLU, the standard benchmark has a test split. If D_EN is the English test items, then training on them and evaluating on them is indeed contaminating the evaluation.

For XQuAD/MLQA, these are cross-lingual QA datasets with parallel English-Arabic data. The "English QA" might be the English questions with the Arabic answers, or the English portion of the dataset. If these are the evaluation examples, then it's the same issue.

So yes, the critic is correct. The paper trains on the evaluation data.

Actually wait - for XQuAD and MLQA, these datasets have training/validation/test splits. Let me check if D_EN refers to the training split or test split. The paper says "English QA" without specifying test/train. But the paper evaluates "on the English splits" of XQuAD/MLQA. Given the context of contamination study, it's likely the test split.

But actually, for XQuAD and MLQA, the "Arabic split" mentioned is the Arabic portion of these datasets (which are parallel English-Arabic datasets). The "English QA" is likely the English portion. These datasets were primarily designed for cross-lingual QA evaluation. If the paper is using the entire XQuAD/MLQA dataset (both English and Arabic portions) for training and evaluation, that's the same issue.

Let me not get too deep into this. The key point is verified: D_EN is the English test items/QA from the evaluation benchmarks, and ALL training conditions include them. This is a fatal design flaw for a contamination study.

OK, I'm confident in my assessment now. Let me write the review.Now I'll write the final consolidated review.

## Summary

The paper investigates whether translating benchmarks into Arabic conceals data contamination signals, by fine-tuning LLMs on mixtures of English and Arabic-translated benchmark data and evaluating on the original English benchmarks. The core finding is that MMLU accuracy increases monotonically with the proportion of Arabic-translated contamination (e.g., Mistral: 0.577→0.690, LLaMA: 0.332→0.431), while standard contamination probes (TS-Guessing) mostly fail to detect this — suggesting translation creates a blind spot. The paper also extends TS-Guessing with a choice-reordering strategy and proposes a Translation-Aware Contamination Detection (TACD) framework.

## Strengths

1. **TS-Guessing extension with choice-reordering (IDR)**. The paper introduces an Index-Recall Rate (IDR) metric for multiple-choice tasks that measures whether a model's prediction matches the pre-shuffle answer letter after reordering (Section 3.3–3.4, Figure 1). For LLaMA-3.2-1B at 50% Arabic contamination, IDR reaches 0.643 on MMLU (Table 3a), far above the 0.25 random baseline. This is a genuine methodological contribution that enables probing index-level memorization even when surface forms differ.

2. **Multi-model, multi-dataset evaluation**. The controlled fine-tuning experiments cover four open-weight models (Mistral-7B, LLaMA-3.2-1B, Gemma-3-1B, Qwen3-1.7B) and two task formats (MCQ in MMLU, extractive QA in XQuAD/MLQA). The consistent MMLU gains across all models (Table 2) suggest the phenomenon is not a single-model artifact.

3. **The core empirical finding is real and interesting**. Adding Arabic-translated test data to the training set does boost English MMLU accuracy in a largely monotonic fashion (Table 2). This shows that cross-lingual semantic equivalents can provide a performance benefit that standard n-gram/exact-match contamination checks would miss. The underlying research question — whether translation masks contamination signals — is timely and practically important.

## Weaknesses

### Fatal

1. **The p=0 ("0% contamination") baseline is itself fully contaminated with the English test set.** The training set for every condition is defined as `D_train^d(p) = D_EN^d ∪ D_AR^d(p)`, where `D_EN^d` is explicitly described as "English test items formatted as MCQ" for MMLU and "English QA" for XQuAD/MLQA (Section 3.1). This means even the EN-only (p=0) condition includes the full English test set in the training data. The paper therefore cannot study whether translation "conceals" contamination relative to a clean baseline — it can only study the marginal effect of adding Arabic-translated copies on top of already-present English test data. The framing throughout the paper (generalization vs. memorization, "0% contamination" as a clean condition, translation "masking" contamination effects) is fundamentally incompatible with a design where every model has already been fine-tuned on the exact evaluation examples. This single issue undermines the paper's central claim and cannot be fixed without redesigning the experimental setup (adding a proper clean baseline and an English-contamination-only condition).

### Major

2. **The prose analysis in Section 4.2 directly contradicts Table 2.** The text states that "across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and describes a "near-flat trend" as evidence that translation masks contamination. Table 2 tells a different story: Mistral MMLU rises from 0.580 (p=10) to 0.690 (p=50) — a 19% relative increase. Similar increases are visible for LLaMA (0.381→0.431) and Gemma (0.244→0.284). Whether one interprets these as "near-flat" or substantial depends on the yardstick, but the text's characterization is misleading at best and actively contradicts the data that the paper's central argument rests on. This is not a minor rhetorical slip — it suggests the qualitative analysis is not calibrated to the empirical record.

3. **No TS-Guessing baseline at p=0 (Table 3).** The TS-Guessing results are reported only for p ∈ {10, 50, 100}%. Without a p=0 baseline, there is no evidence that the probe would detect contamination in the English-only setting. The paper's claim that translation "conceals" contamination requires showing that detection works in a same-language setting but fails in the cross-lingual setting. Table 3 cannot support this comparison because the p=0 English-only condition was never probed. (Note: the p=0 condition is not a true "clean" baseline either — see point 1 — but at minimum it would establish whether TS-Guessing produces non-zero signals when only English test data is in training.)

4. **Unexplained tension between large performance gains and near-zero TS-Guessing scores.** The paper's narrative requires that the MMLU gains in Table 2 are driven by contamination-driven memorization. However, the TS-Guessing probe designed to detect this memorization produces essentially zero values across most model × condition combinations (e.g., Mistral IDR = 0.000 for p=10 and p=50; Qwen3 XQuAD EM = 0.000 for p=10 and p=50). The paper never addresses this tension — it simply asserts the contamination narrative. If contamination drives the score gains, the probe should reflect it; if the probe fails, the paper cannot attribute the gains to memorization without additional analysis. The single exception (LLaMA at p=50, IDR=0.643) is not sufficient to resolve the tension.

### Minor

5. **Scope mismatch between framing and experiment.** The introduction and literature review (Sections 1–2) frame contamination in terms of pre-training dynamics (e.g., "benchmark data appears in the training corpus" via CommonCrawl leakage). The experiments, however, study explicit fine-tuning on the test set — a radically different and more extreme contamination regime. The paper acknowledges this implicitly but never discusses whether its findings would transfer to the pre-training setting that motivates the work. This limits the generality of the conclusions.

6. **The TACD framework (Section 5) is a sketch, not a contribution.** The paper describes TACD at a conceptual level with no implementation, no evaluation against existing detectors, and no empirical validation. While it is reasonable to include as future work, it is not a strength of the current paper.

### Trivial

None.

## Nice-to-Haves

- A truly clean baseline (no benchmark data in training at all) would allow the paper to separate contamination effects from general training benefits.
- A direct comparison of TS-Guessing recall on English-contaminated vs. Arabic-contaminated models would directly test the "translation masks contamination" hypothesis.
- Reporting results on held-out non-contaminated benchmarks would help distinguish contamination-driven gains from genuine capability improvements.

## Removed Points

- **Strength Finder's "controlled fine-tuning to isolate causation" (supporting strength 2).** Using fixed hyperparameters across conditions is standard practice, not a distinctive strength. The absence of a clean baseline (point 1 above) also undercuts any claim of causal isolation.

- **Strength Finder's "TACD framework provides a structured blueprint."** The TACD description is purely conceptual with no implementation or evaluation. It reads as future work, not a current contribution.

- **Harsh Critic's Issue 5 (study doesn't generalize to pre-training).** The paper is transparent about its fine-tuning paradigm. The pre-training discussion in the literature review provides context, not a claim that the experiments directly test pre-training. This is a framing issue, not a fatal flaw.

- **Harsh Critic's "results contradict TS-Guessing" framing (part of Issue 4).** There is a tension, but the critic overstates it: IDR=0.643 for LLaMA at p=50 is a non-trivial signal, and the probe is designed for index-level memorization, not all forms of contamination. The tension is real but not an outright contradiction.

- **Any formatting/style nitpicks, typo complaints, or missing appendix issues.** These are parser artifacts or not substantive.

## Novel Insights

None beyond the paper's own contributions. The core observations — that Arabic-translated benchmark data boosts English MMLU accuracy and that standard probes (TS-Guessing) often fail to detect cross-lingual contamination — are useful but fatally undermined by the confounded experimental design.

## Suggestions

The paper asks a genuinely interesting question, but answering it requires a clean experimental design:

1. Add a **true clean baseline** where the model is fine-tuned on non-benchmark data only.
2. Add a **same-language contamination condition** (English test data in training, English probe) alongside the cross-lingual condition (Arabic translations, English probe) to directly test whether translation degrades detection.
3. Run **TS-Guessing on the p=0 (English-only) condition** to establish whether the probe works at all in this fine-tuning paradigm.
4. Address the **tension between Table 2 gains and Table 3 near-zero scores** explicitly — either by demonstrating that the gains come from a mechanism other than index-level memorization, or by adding a more sensitive probe.

---

## Score and Decision

**Round 1 — Bracketing (3 queries parallel):**
- Low band (< 3.5): Anchors returned included "Llamas (mostly) think in English" (3.00, Reject), "Industrial Benchmarking of LLMs" (3.00, Reject), "Exploring and Benchmarking Planning Capabilities" (2.00, Reject).
- Middle band (3.5–7.5): Anchors included "Evading Data Contamination Detection" (4.25, Reject), "How much can we Forget about Data Contamination" (6.75, Reject), "To the Cutoff... and Beyond" (6.75, Accept), "Crosslingual Capabilities and Knowledge Barriers" (5.67, Reject).
- High band (> 7.5): Anchors included "Training on the Test Task" (8.00, Accept), "Cheating Automatic LLM Benchmarks" (7.75, Accept), "Context-Parametric Inversion" (8.00, Accept).

**Initial bracket:** 2.5 – 4.5. The paper's fatal design flaw places it well below the methodologically sound middle-band papers (6.0–7.0). The most relevant comparison is "Evading Data Contamination Detection" (4.25), which studies evasion of contamination detection — a similar theme but with a cleaner design.

**Round 2 — Narrowing within bracket (2.5–4.5):**
- "Evading Data Contamination Detection" (4.25, Reject): Similar topic (evading detection via rephrasing). Cleaner experimental design. Our paper has a more interesting multilingual angle but a more severe design flaw. → Our paper is weaker.
- "Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts" (4.25, Reject): Methodologically sounder. → Our paper is weaker.
- "All Languages Matter: On Multilingual Safety" (3.50, Reject): Multilingual evaluation paper with methodological concerns. Comparable overall quality. → Our paper is slightly weaker due to the fatal baseline flaw.
- "LLM Detectors Still Fall Short" (3.80, Reject): Well-scoped, rigorous. → Our paper is comparable or slightly weaker.

**Final score determination:** The paper sits near the lower end of the bracket. The fatal design flaw (training on the English test set in ALL conditions) is more severe than the weaknesses in the 3.5–4.25 anchors. The central claim about translation "masking" contamination is unsupported by the experimental design. The paper has an interesting question and some methodological value (IDR metric), but the core empirical contribution is invalidated.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>