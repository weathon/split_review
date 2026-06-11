Now I have a solid calibration basis. Let me write the final review.

## Summary

This paper investigates whether translating English LLM benchmarks (MMLU, XQuAD, MLQA) into Arabic can mask data contamination from standard detection methods. It fine-tunes four open-weight models on mixtures of English and Arabic-translated test data at varying contamination levels (0%, 10%, 50%, 100%), evaluates on the original English benchmarks, and probes memorization via an extended TS-Guessing method with choice-reordering. The paper finds that models show MMLU accuracy gains with Arabic contamination (e.g., Mistral: 0.577→0.690) while the TS-Guessing probe yields largely flat/noisy scores. A Translation-Aware Contamination Detection (TACD) framework is proposed as a forward-looking blueprint.

## Strengths

1. **Joint finding (Table 2 + Table 3) is suggestive and worth exploring.** The observation that MMLU accuracy increases with Arabic contamination while TS-Guessing returns flat scores across contamination levels is a nontrivial pattern. If a same-language positive control were in place, this would provide evidence that translated contamination yields measurable performance gains that evade a standard probe.

2. **Novel empirical observation of "peak-at-10%" in MLQA.** Several models (Gemma, LLaMA, Qwen) show non-monotonic MLQA performance peaking at 10% contamination and then declining. This pattern is not predicted by standard same-language contamination studies and suggests translation-induced contamination dynamics that differ from English-only settings — a genuinely interesting finding.

3. **Methodological extension to TS-Guessing.** The choice-reordering strategy (shuffling answer options before masking and measuring index-recall rate IDR) is a sensible adaptation of Deng et al. (2024) that specifically targets position-based memorization that could survive translation. This is a concrete methodological contribution.

4. **Honest scoping of TACD.** The paper explicitly presents TACD as "a forward-looking blueprint rather than a complete implementation" and candidly discusses the resource demands and translation noise challenges. This forthrightness is welcome.

## Weaknesses

### Fatal
None.

### Major

1. **Internal contradiction between §4.1 and §4.2.** §4.1 documents that "MMLU exhibits a generally monotonic increase as contamination rises" and reports specific gains (Mistral: +11.3 points, LLaMA: +9.9 points). Yet §4.2 claims that "across contamination levels p ∈ {10,50,100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and that "scores remain broadly stable." These statements are in direct conflict for the MMLU data. Looking at just the 10%→100% range (the range §4.2 explicitly references), Mistral's MMLU goes from 0.580 to 0.690 — an 11-point gain that is not "broadly stable." This inconsistency undermines the paper's central narrative. The paper cannot simultaneously claim that translation produces measurable contamination-driven gains and that translation conceals those gains.

2. **Missing positive control for TS-Guessing.** The TS-Guessing probe returns very low scores across all conditions (XQuAD EM and ROUGE-L F1 are mostly <0.02; MMLU IDR is erratic and fluctuates wildly, e.g., Gemma goes 0.350 → 0.029 → 0.005 across contamination levels). Without a same-language (English→English) positive control demonstrating that TS-Guessing can detect memorization in these same models under the same conditions, the paper cannot distinguish between "translation masks contamination from the probe" and "the probe is simply too weak to detect memorization in these models." The erratic IDR values (e.g., Gemma swinging from 0.350 to 0.029 and back) suggest the probe may be producing noise. This gap critically weakens the paper's core claim.

3. **D_EN already includes English test items in every condition.** For MMLU, D_EN consists of "English test items formatted as MCQ" — meaning the p=0 baseline already includes the full English test set in training. The experiment compares "contaminated with English test items" against "contaminated with English + Arabic test items." The additive gains from Arabic are layered on top of already-memorized English content, making the already-artificial setup harder to interpret. The paper does not discuss this design choice or its implications.

4. **No statistical rigor.** No multiple seeds, confidence intervals, or significance tests are reported. Given the small model sizes (1B–7B) and LoRA fine-tuning, run-to-run variance could be non-trivial. The paper's comparative claims (monotonicity, flatness, non-monotonicity) depend on observed numerical differences but provide no indication of whether these differences are reliable.

### Minor

1. **Artificial experimental setup.** The paper deliberately fine-tunes on translated test-set items — a scenario far from realistic contamination pathways (incidental inclusion in web-scale pre-training data). While the paper frames this as a controlled study, the gap between this manufactured scenario and the claimed "blind spot in current evaluation practices" limits the strength of the conclusions. The paper would benefit from more clearly scoping the claims as a proof-of-concept demonstration of a mechanism, not evidence that realistic contamination is being missed.

2. **Source of MMLU Arabic translations unspecified.** The paper states "MMLU: Arabic translations of the test items" but does not specify who produced the translations, their quality, or their provenance. MMLU does not have a standard Arabic version; third-party translations vary. This affects both reproducibility and the ability to assess the contamination scenario's realism.

3. **Unsupported claim about Arabic capabilities.** The abstract claims that models "with stronger Arabic capabilities" benefit more from contamination, but the paper provides no analysis linking Arabic proficiency to contamination susceptibility — no correlation, no grouping, no controlled comparison. This claim should either be supported with evidence or removed.

### Trivial
None.

## Nice-to-Haves
- Re-run the TS-Guessing probe on an English→English contamination condition as a positive control.
- Report results across multiple random seeds (≥3) with variance estimates.
- Disclose the provenance and quality assessment of the MMLU Arabic translations.
- Clarify and resolve the tension between the monotonic MMLU trends and the "flat trend" claim.

## Removed Points
Points from the Harsh Critic that were filtered during review construction:
1. **"The experimental design does not test the claim"** (Critical Issue 1) — Removed because the experiment does test the claim: it shows that when models are exposed to translated test data, (a) they benefit from it (Table 2) and (b) standard probes fail to detect it (Table 3). The critic's objection conflates "the scenario is artificial" with "the experiment doesn't test the hypothesis." However, the artificiality concern is retained as a Minor weakness (above).
2. **"TS-Guessing results are negative and weaken the argument"** — The core of this criticism (no positive control) is retained as Major weakness #2. The framing that results are "negative" and therefore weaken the argument is itself removed; the flat TS-Guessing scores are consistent with the paper's thesis. The problem is the missing calibration, not the direction of the results.
3. **"TACD is not evaluated"** — The paper explicitly calls it a "blueprint, not a complete implementation." This is transparently scoped, not a weakness. Removed.
4. **"Literature review is too long / has grammar errors"** — Style/subjective formatting and parser artifact complaints. Removed.
5. **Various formatting/style nitpicks** — Removed per filtering rules.

## Novel Insights
The most illuminating tension from the reviews is that the paper's headline evidence (performance up, probe flat) is both its strongest and weakest point. The pattern is genuinely suggestive, but without a same-language positive control for the probe, the paper cannot rule out the simpler explanation that TS-Guessing is simply uninformative at these model scales. This gives the paper an uncomfortable evidential structure: its central finding is simultaneously what makes it interesting and what makes it unverifiable from the presented data. The "peak-at-10%" MLQA finding is more robust and may be the paper's most durable empirical contribution, though it is secondary to the paper's main argument.

## Suggestions
1. Add a same-language (English→English) TS-Guessing positive control using the same models and conditions to establish probe sensitivity.
2. Resolve the §4.1 vs. §4.2 contradiction: either acknowledge that MMLU shows clear contamination-driven gains (and reframe "flat" to apply only to probe scores, not evaluation scores), or provide a more nuanced characterization.
3. Report variance across multiple fine-tuning seeds (at least 3).
4. Disclose the source and quality of the MMLU Arabic translations.
5. Either provide analysis supporting the "Arabic capabilities" claim or remove it from the abstract.
6. Discuss the design choice of including English test items in D_EN and its implications for interpreting the additive Arabic gain.

## Score and Decision

**Bracketing (Round 1):** I queried five score bands using the calibration corpus. The most topically similar papers to this one are in the 3–5 range: "Evading Data Contamination Detection for Language Models is (too) Easy" (avg 4.25), "Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts" (avg 4.25), "Elephants Never Forget: Testing Language Models for Memorization of Tabular Data" (avg 4.75), and "Predicting and analyzing memorization within fine-tuned LLMs" (avg 4.00). Higher-quality contamination papers like "How much can we Forget about Data Contamination?" (avg 6.75) and "To the Cutoff... and Beyond?" (avg 6.75) are clearly stronger — they have rigorous large-scale experiments, theoretical grounding, and tighter argumentation. The lowest band papers (scores 1–2) are fundamentally unserious or broken. **Initial bracket: 3.0–5.0.**

**Narrowing (Round 2):** I pulled additional anchors in (2.5, 4.5) and (4.5, 6.0). Reading the full reviews of the most similar anchors:
- "Evading Data Contamination Detection" (avg 4.25, scores 3,6,5,3): Closest in topic. Clearer methodology (EAL attack demonstrated to evade detection) but criticized for lack of technical depth and unclear threat model. Our paper has a comparable contribution level but adds an internal contradiction that the Evading paper does not have.
- "Elephants Never Forget" (avg 4.75, scores 5,8,3,3): Broader scope with multiple testing methods. Our paper is narrower and has more serious experimental design concerns.
- "Predicting and Analyzing Memorization" (avg 4.00, scores 5,3,5,3): Comparable quality — both have interesting ideas undermined by experimental limitations.

**Calibration judgment:** The paper under review is most comparable to the lower end of the mid-range contamination papers. It has a timely question, genuine empirical work, and an interesting finding (peak-at-10%), but is held back by an internal contradiction that undermines its narrative, a missing positive control that weakens its core claim, and experimental design choices that are not adequately discussed. Across all retrieved anchor comparisons, this paper sits below the 4.25–4.75 anchors but above the 1–2 range. The most appropriate comparison paper is "Evading Data Contamination Detection" (4.25), which our paper resembles in topic and ambition but falls short of in execution due to the internal inconsistency.

**Final score: 3.5. Decision: Reject.**

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>