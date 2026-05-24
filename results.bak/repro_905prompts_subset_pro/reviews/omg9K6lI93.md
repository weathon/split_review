Now I have enough to calibrate properly. Let me synthesize the final review.

**Calibration Summary:**
- Round 1 bracket: 4.0–6.0
- Round 2 narrowed: The paper is comparable to vl8VpW2niQ (5.40, memorization in ICL — novel angle, interesting findings, but significant methodological limitations) and rAylWUIKtu (4.25, benchmark inflation — overclaimed, limited scope). Our paper has a more novel cross-lingual angle and broader experiments than rAylWUIKtu, but a more serious internal contradiction than vl8VpW2niQ.
- **Final score: 4.5** — between rAylWUIKtu (4.25) and vl8VpW2niQ (5.40), closer to the lower end due to the internal contradiction.

Now let me write the review.

---

## Summary

This paper investigates whether translating benchmarks into Arabic can conceal data contamination while models still benefit from memorized content. The authors fine-tune four open-weight LLMs on varying proportions of Arabic-translated test sets (MMLU, XQuAD, MLQA) alongside English data, then evaluate on the original English benchmarks. They extend the TS-Guessing method with a choice-reordering strategy to detect memorized answer-index patterns. The paper also sketches a Translation-Aware Contamination Detection (TACD) framework as a forward-looking proposal. The core claims are that translation masks contamination signals while models still benefit, and that current English-only detection pipelines have a dangerous blind spot.

## Strengths

- **Novel cross-lingual angle on a well-studied problem.** Investigating whether translation into a low-resource language can serve as a contamination vector is a genuinely underexplored question. While contamination detection is heavily studied, the multilingual dimension is almost entirely absent from prior work, and the paper identifies a real blind spot in current evaluation practices.

- **Broad model and benchmark coverage.** The experiments span four instruction-tuned models across different families and scales (LLaMA-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) and three benchmarks (MMLU, XQuAD, MLQA) under identical fine-tuning protocols. This strengthens the generalizability of the empirical observations beyond any single architecture.

- **Non-monotonic behavior in extractive QA is genuinely informative.** The "peak-at-10%" pattern observed in MLQA for several models (Gemma: 0.474→0.494→0.411→0.471; Qwen: 0.162→0.409→0.157→0.153) followed by degradation at higher contamination levels is a non-obvious result. This suggests that small amounts of cross-lingual leakage can aid surface-form familiarity while heavier contamination overfits to distributional quirks — a nuanced dynamic that standard contamination checks would miss.

- **TS-Guessing with choice-reordering is a sensible methodological extension.** Shuffling answer choices before probing, then measuring index-recall rate (IDR) as the fraction of predictions echoing the pre-shuffle letter, provides a more targeted memorization signal than accuracy alone. The method is clearly described and the metric is well-defined.

## Weaknesses

### Fatal

None. No single weakness completely invalidates the paper's core observation that Arabic-contaminated fine-tuning can boost English benchmark performance. That empirical finding stands regardless of interpretive issues.

### Major

- **Internal contradiction between Sections 4.1 and 4.2.** Section 4.1 (line 193) correctly reports that "MMLU exhibits a generally monotonic increase as contamination rises from 0% → 100%." However, Section 4.2 (line 205) then claims that "the models exhibit approximately equal performance on all evaluated benchmarks" and describes a "near-flat trend." These statements are mutually contradictory. Table 2 shows MMLU increases of +0.113 (Mistral), +0.064 (Gemma), +0.099 (LLaMA), and +0.028 (Qwen) from 0% to 100% contamination. XQuAD and MLQA also show substantial non-monotonic swings (e.g., Mistral XQuAD collapses from 0.455 to 0.114). The "near-flat" narrative is directly contradicted by the paper's own data, and this claim underpins the central interpretation that translation "masks" contamination by compressing performance differences. This misalignment between reported data and interpretive claims undermines a key part of the paper's argument.

- **The "masking" claim relies on a missing comparison.** The paper argues that Arabic translation conceals contamination signals in a way that same-language contamination would not. However, there is no English-contamination control condition — i.e., fine-tuning on the same proportions of the original English test set — against which the magnitude and detectability of performance shifts could be compared. Without this baseline, the claim that translation specifically *masks* contamination (as opposed to contamination simply existing in another language) is asserted rather than demonstrated. The performance gains from Arabic fine-tuning are consistent with contamination being present; what is missing is evidence that these gains are harder to detect than they would be in an English-contamination setting.

### Minor

- **TACD framework is unevaluated.** Section 5 explicitly presents TACD as "a forward-looking blueprint rather than a complete implementation." While proposing directions is legitimate, the abstract states "we propose a Translation-Aware Contamination Detection framework," which sets an expectation of at least a minimal evaluation. The paper would be stronger if repositioned to acknowledge that TACD is a conceptual proposal rather than a validated contribution.

- **IDR patterns are unusual and not adequately explained.** The TS-Guessing probe yields puzzling results: Gemma's IDR drops from 0.350 at 10% contamination to 0.005 at 100%, while Mistral's IDR stays at 0.000 across all contamination levels. These patterns are not discussed in the paper. The lack of analysis leaves the reader uncertain about what the probe is actually measuring in this cross-lingual setting, weakening the contamination-detection narrative.

- **Embedding evidence is asserted without presentation.** Section 4.3 references an "embedding figure" showing high cosine similarity between Arabic→English translations and English originals, but no figure number is given and the evidence is not presented in a way the reader can evaluate. The claim that translation "compresses observed performance differences" through semantic preservation is therefore unsubstantiated in the text as presented.

### Trivial

- The paper uses "test items" to describe D_EN^d (line 136), which could be misread as implying that the English test set itself is included in training. The actual setup (English training data + Arabic translations of test items) should be clarified with more precise terminology.

## Nice-to-Haves

- An English-contamination control condition would transform this from an exploratory study into a definitive demonstration of translation-specific masking.
- Implementing even a basic version of TACD on the existing data (e.g., checking TS-Guessing across one additional language pair) would strengthen the framework claim.
- Quantitative measures of effect size or statistical tests comparing performance across contamination levels would replace the problematic "near-flat" description with rigorous evidence.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "TS-Guessing probe is not valid for cross-lingual contamination because the model never sees English letter assignments."** REMOVED — The critic assumes Arabic translations do not preserve the A/B/C/D choice structure, but this is not established. If the Arabic MMLU translations retain the same letter-labeling convention (A, B, C, D map to the same answer positions), then the model could learn letter-index mappings from Arabic fine-tuning. The probe's validity depends on dataset construction details not discussed in the paper, making this a question rather than a demonstrated flaw.

- **Harsh Critic: "The artificial contamination set-up limits applicability" and "does not resemble how contamination appears in practice."** MOVED to scope consideration — The paper uses direct fine-tuning on test sets, which is an extreme but controlled form of contamination. This is a legitimate experimental design choice for studying mechanisms, not an inherent flaw. The concern about ecological validity is noted but does not invalidate the controlled experiment.

- **Strength Finder: "Empirical demonstration that translation masks but does not eliminate contamination" (as a core strength).** WEAKENED — The "does not eliminate" part is supported by performance gains. The "masks" part is the paper's interpretation and, as discussed in Major Weaknesses, relies on a contested "near-flat" narrative and a missing English-contamination control.

- **Harsh Critic: "The probe would need to target semantic recall rather than letter-position recall."** REMOVED — This is a design suggestion, not a flaw. The letter-position probe is a deliberate choice that can detect a specific form of memorization; semantic recall probes would measure something different.

## Novel Insights

None beyond the paper's own contributions. The observation that non-monotonic patterns in extractive QA (peak at low contamination, degradation at high) constitute a fragility signal not captured by standard linear contamination checks is the most interesting empirical finding, but it is already presented by the authors.

## Suggestions

- Resolve the Section 4.1/4.2 contradiction by either removing the "near-flat" claim or replacing it with a quantitative argument that acknowledges the observed increases while arguing they are smaller than would be expected under same-language contamination. The latter would require the English-contamination control.
- If adding an English control is infeasible, reframe the contribution more modestly: the paper demonstrates that cross-lingual contamination *exists and produces measurable effects*, without making comparative claims about whether it is harder to detect.
- Either implement a minimal version of TACD or move it to a Discussion/Future Work section and remove "we propose a framework" from the abstract.
- Present the embedding evidence explicitly with a figure number and quantitative cosine similarity values, or remove the claim from Section 4.3.

## Score and Decision

This paper investigates a genuinely interesting and underexplored question — whether translating benchmarks can serve as a contamination vector while evading English-only detection. The multi-model, multi-benchmark experiments are a strength, and the non-monotonic extractive QA patterns are a genuinely novel finding. However, the paper is undermined by a direct internal contradiction between its data description and its interpretive claims: the "near-flat trend" narrative in Section 4.2 is falsified by the monotonic MMLU increases and large QA swings reported in Table 2 and correctly described in Section 4.1. This is not a minor wording issue — it is the paper claiming something its own evidence contradicts. Combined with an unevaluated detection framework and a missing English-contamination control for the central comparative claim, the paper falls short of supporting its strongest conclusions. The core empirical finding (cross-lingual contamination boosts English performance) is valid and worth reporting, but the paper overreaches in its interpretation.

**Anchor comparison:**
- Nk1MegaPuG (4.25, Round 1/2): Evading contamination detection — overclaimed, unclear methodology. Our paper is stronger with clearer experiments.
- rAylWUIKtu (4.25, Round 2): Benchmark inflation retro-holdouts — limited scope, overclaimed. Our paper has broader experiments but similar overclaiming issues.
- vl8VpW2niQ (5.40, Round 2): Memorization in ICL — novel angle, interesting findings, but single model and methodological concerns. Our paper is comparable but slightly weaker due to the internal contradiction.
- m2NVG4Htxs (6.75, Round 1): Longitudinal contamination — well-executed, clear methodology. Our paper falls meaningfully short of this standard.
- Nsms7NeU2x (6.75, Round 1): Forgetting contamination — thorough theory + experiments. Our paper is clearly weaker.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>