Now I have all the context I need. Let me produce the final consolidated review.

---

## Summary

This paper investigates whether translating English benchmarks into Arabic can conceal data contamination signals. The authors fine-tune four open-weight LLMs on Arabic-translated test splits of MMLU, XQuAD, and MLQA at varying proportions (0%, 10%, 50%, 100%), evaluate on the original English benchmarks, and probe memorization via an adapted TS-Guessing method with choice-reordering. They find that while MMLU accuracy rises monotonically with contamination, extractive QA scores (XQuAD/MLQA) are non-monotonic and TS-Guessing scores remain generally low. The paper concludes that translation masks but does not eliminate contamination, and proposes a Translation-Aware Contamination Detection (TACD) framework as a forward-looking blueprint.

## Strengths

1. **First systematic study of translation as a contamination masking mechanism.** While prior contamination work focuses overwhelmingly on English-only settings, this paper empirically demonstrates that when benchmarks are translated into Arabic, evaluation metrics can behave differently from expected same-language contamination patterns. The finding that translation ≠ decontamination (i.e., models still benefit from translated contaminated data even though surface-form detectors may miss it) is a genuinely novel observation. *Evidence: Section 4.1 (Table 2: MMLU monotonic gains vs. non-monotonic XQuAD/MLQA), Section 4.2 (near-flat TS-Guessing across p).*

2. **Extension of TS-Guessing with choice-reordering for multiple-choice QA.** The paper adapts the TS-Guessing memorization probe by randomly shuffling answer choices before masking one option, then checking whether the model reproduces the pre-shuffle index (IDR metric). This is a concrete methodological adaptation that isolates index-based memorization from content-based reasoning, and it can be reused in future multilingual contamination studies. *Evidence: Section 3.3, Figure 1, IDR definition in Section 3.4.*

3. **Multi-model, multi-dataset experimental scope.** The design spans four diverse open-weight models (LLaMA-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) and three benchmarks (MMLU, XQuAD, MLQA) at four contamination levels with controlled fine-tuning (LoRA, identical hyperparameters). This breadth is a strength — the observed patterns are unlikely to be model- or dataset-specific artifacts. *Evidence: Section 3.1, Table 2.*

4. **Non-monotonic extractive QA trends reveal dataset-specific contamination dynamics.** The "peak-at-10%" pattern in MLQA for several models (Gemma, LLaMA, Qwen) followed by decline at higher contamination is a nuanced finding that goes beyond a simple monotonic memorization story. It suggests that contamination can hurt cross-lingual generalization even when closed-book accuracy rises. *Evidence: Section 4.1 discussion of MLQA behavior.*

## Weaknesses

### Fatal
None.

### Major

1. **Missing English contamination control condition — the central claim is not directly supported.** The paper claims translation "conceals" or "masks" contamination signals, but it never runs a control condition where models are fine-tuned on *English* test data at the same proportions (0%, 10%, 50%, 100%) and compared on the same metrics. Without this control, several alternative explanations cannot be ruled out: (a) the non-monotonic XQuAD/MLQA patterns might arise from overfitting or dataset-specific quirks regardless of language; (b) the low TS-Guessing scores might reflect probe insensitivity to *any* fine-tuning-based contamination, not specifically to translation. The paper explicitly states "In typical same-language settings, increasing p would be expected to induce noticeable shifts" (Section 4.2), but this is stated as fact rather than demonstrated. This comparison is the single most important experiment needed to substantiate the paper's core narrative, and its absence makes the "masking" conclusion an interpretation rather than a demonstrated finding. *Evidence: Section 3.1 describes only four conditions (p=0%, 10%, 50%, 100% of Arabic-translated data); there is no English-only contamination arm.*

2. **The TS-Guessing results are equally consistent with probe insensitivity as with translation masking.** Table 3 shows that TS-Guessing scores are consistently low across nearly all models, contamination levels, and datasets. For XQuAD, EM scores range from 0.000 to 0.103 with most near zero. For MMLU, RL-F1 values are mostly below 0.06. The paper attributes this to translation "concealing" contamination, but an equally plausible explanation is that TS-Guessing (even choice-reordered) is simply not sensitive enough to detect this form of contamination, regardless of language. Without an English-contamination TS-Guessing baseline, the paper cannot distinguish between "translation masks detection" and "the detection method does not work for fine-tuning-based contamination." *Evidence: Table 3(a) and 3(b): near-zero EM and RL-F1 across all conditions.*

### Minor

1. **Inconsistent characterization of results across sections.** Section 4.2 states "Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks," but this contradicts Section 4.1 which documents clear monotonic MMLU gains (e.g., Mistral: 0.577→0.690, LLaMA: 0.332→0.431) and the TS-Guessing IDR values in Table 3a show substantial variation (LLaMA IDR: 0.287, 0.643, 0.410). The claim of "approximately equal performance" overstates the stability of the results. *Evidence: Table 2 (monotonic MMLU gains), Table 3a (variable IDR).*

2. **No analysis linking Arabic capability to contamination benefit.** The abstract claims "models with stronger Arabic capabilities benefit more" from contaminated data, but no quantitative analysis is provided — no correlation between pre-existing Arabic QA performance and contamination gain, no comparison across model sizes or Arabic proficiency. This claim is stated but not evidenced. *Evidence: The claim appears in the Abstract and Introduction but no systematic analysis is present in the results section.*

3. **Limited diversity of contamination language and method.** Only one language (Arabic) and one contamination modality (fine-tuning on test-set translations) are studied. The paper's broader conclusions about "multilingual contamination" and "dangerous blind spots in evaluation practices" would be substantially stronger with at least one additional language (e.g., French, Chinese, or a truly low-resource language) or a different contamination scenario (e.g., including translated data in a pre-training corpus). *Evidence: Section 3.1 uses Arabic only.*

### Trivial
None.

## Nice-to-Haves

- Include an English contamination baseline to directly test whether translation reduces detectability relative to same-language contamination.
- Apply standard detection methods (Min-K% Prob, guided prompts) to both English- and Arabic-contaminated models and compare detection rates.
- Add a second language to test whether the observed patterns are specific to Arabic or generalize.
- Provide a quantitative analysis of the claimed relationship between Arabic capability and contamination benefit (e.g., correlate pre-existing Arabic performance with accuracy gains).

## Removed Points

- **"Experimental setup does not model realistic contamination"** — The paper is transparent about using fine-tuning on test-set translations as its paradigm; it does not claim to model web-scale pre-training contamination. The criticism overstates the mismatch between design and claim. However, the paper's broader language ("evade standard detection tools," "dangerous blind spot") does reach beyond what the design directly supports; this scope concern is adequately captured in the Major weaknesses above.
- **"Literature review disconnected from experiments"** — Generic criticism; many papers have broad related-work sections.
- **"TACD blueprint is unevaluated"** — The paper explicitly acknowledges this ("we offer TACD as a forward-looking blueprint rather than a complete implementation"). Not a valid weakness.
- **"Arabic is not low-resource"** — Subjective and not central to the paper's claims.
- **"TS-Guessing IDR may simply mean the model didn't see English indices"** — This is exactly what the probe is designed to test; not a flaw in the method.
- **"Choice-reordering not well justified for cross-lingual setting"** — The method is clearly described and its rationale (disentangling index recall from content reasoning) is sound.

## Novel Insights

The reviews surface one genuinely novel observation that goes beyond the paper's own contributions: the non-monotonic "peak-at-10%" pattern in MLQA is a specific failure mode where small amounts of translated contamination briefly improve span extraction, but heavier contamination degrades it. This suggests that contamination effects in cross-lingual settings are not simply monotonic memorization — they interact with the model's cross-lingual transfer ability in complex ways. The harsh critic noted this pattern but dismissed it as "noisy" and "model-specific," while the strength finder correctly recognized it as a nuanced finding that hints at dataset-specific contamination dynamics worthy of deeper investigation. Neither reviewer, however, frames this as a potential window into mechanistic differences between how MMLU (multiple-choice) and extractive QA respond to cross-lingual contamination — a direction that could motivate future work on probe design.

## Suggestions

1. **Run an English contamination baseline** — Fine-tune models on English test data at the same proportions (0%, 10%, 50%, 100%) and compare both evaluation scores and TS-Guessing results to the Arabic condition. This is the single most important addition; it would directly test whether translation specifically reduces detectability.
2. **Apply standard detection methods** — Run Min-K% Prob or a membership inference method on both English- and Arabic-contaminated models to quantify whether detection is harder in the Arabic condition.
3. **Tighten the language around "concealing" vs. "not detectably affecting"** — The paper should more precisely distinguish between "translation makes contamination harder to detect with these specific probes" (what the evidence supports) and "translation conceals contamination in general" (what the paper sometimes implies).
4. **Add quantitative analysis of Arabic capability and contamination gain** — If the claim about stronger Arabic models benefiting more is to be retained, provide a systematic analysis with correlation or regression.

## Score and Decision

**Calibration anchors (from retrieval):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|--------------------------|
| KS8mIvetg2 (Proving Test Set Contamination) | 7.50 / Accept | Much stronger: provable guarantees, rigorous statistical tests, thorough validation. This paper lacks comparable methodological rigor. |
| jOmk0uS1hl (Training on the Test Task) | 8.00 / Accept | Much stronger: clean experimental design, clear causal claims, extensive analysis. This paper's missing control condition would not pass their standards. |
| Nsms7NeU2x (How much can we Forget) | 6.75 / Reject | Stronger: combines theory with controlled experiments across scaling dimensions. This paper has less theoretical depth and a narrower experimental scope. |
| m2NVG4Htxs (To the Cutoff... and Beyond) | 6.75 / Accept | Stronger: natural experiment design with longitudinal analysis, statistically rigorous. This paper's conclusions are less well-supported. |
| Nk1MegaPuG (Evading Detection is too Easy) | 4.25 / Reject | Similar theme (evading/obscuring contamination detection), but this paper has more concrete experiments and a multi-model design. Marginally stronger than Nk1MegaPuG. |
| rAylWUIKtu (Benchmark Inflation) | 4.25 / Reject | Similar quality tier — interesting idea but experimental gaps weaken the central claims. Comparable overall quality. |

The paper identifies a genuinely novel problem and provides reasonable initial experiments, but the missing English contamination baseline is a significant gap that prevents the central claim from being adequately supported. The TS-Guessing results have plausible alternative explanations that are not ruled out, and the broader conclusions reach beyond what the experimental design can sustain. Compared to calibrated anchors, this paper sits notably below acceptance-quality work (e.g., KS8mIvetg2 at 7.50, jOmk0uS1hl at 8.00) and is more comparable to papers in the 4-5 range that identify interesting problems but have substantial experimental limitations.

**Originality:** 3/4 — novel question, first to study translation as a contamination masking mechanism.
**Quality of research question:** 3/4 — important and timely.
**Claims supported:** 2/4 — central claim lacks direct support due to missing control.
**Soundness of experiments:** 2/4 — reasonable breadth but missing crucial control, inconsistent result characterization.
**Clarity of writing:** 3/4 — well-structured and generally clear.
**Value to community:** 3/4 — the question is important and the initial data is useful, even if the conclusions are not fully established.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>