I have thoroughly verified all claims against the paper. Let me now produce the consolidated review.

## Summary

This paper studies whether translating benchmark test data (MMLU, XQuAD, MLQA) into Arabic before fine-tuning conceals data contamination signals. The authors fine-tune four open-weight LLMs on varying proportions of Arabic-translated test sets (0%, 10%, 50%, 100%) and evaluate on the original English benchmarks. They extend TS-Guessing with a choice-reordering strategy to probe memorization. The core finding is that translation does not eliminate contamination—models show measurable performance gains (particularly on MMLU) and some memorization signals persist—but the paper's framing around "masking" of contamination signals is undermined by internal inconsistencies in how the results are presented.

## Strengths

1. **Well-motivated research question with a controlled experimental design.** The paper addresses an underexplored angle of contamination—whether translation into a lower-resource language (Arabic) alters contamination dynamics. The factorial design (4 models × 3 datasets × 4 contamination levels = 48 combinations) is systematic, and the use of consistent PEFT settings across conditions supports fair comparison.

2. **Novel extension of TS-Guessing with choice-reordering for MCQ benchmarks (Section 3.3, Figure 1).** The idea of shuffling answer choices and masking an incorrect answer, then measuring index-recall rate (IDR) as a contamination signal, is methodologically sound and fills a gap: standard next-token probability probes do not directly test whether a model memorized answer *positions* rather than content. The IDR of 0.643 for LLaMA-3.2-1B at 50% contamination (Table 3a) provides concrete evidence that position-level memorization persists through translation.

3. **Non-monotonic contamination patterns in extractive QA are empirically documented.** The "peak-at-10%" pattern in MLQA across multiple models (e.g., Gemma: 0.474 → 0.494 → 0.411 → 0.471; LLaMA: 0.443 → 0.520 → 0.437 → 0.456) is a nuanced finding that goes beyond simple monotonic trends. This suggests small amounts of cross-lingual overlap can aid extraction while heavier exposure harms it—an observation with practical implications for understanding how contamination interacts with task type.

4. **The core empirical result—that translation does not eliminate contamination—is supported by the MMLU data.** Table 2 shows clear monotonic increases for MMLU across all four models (e.g., Mistral-7B: 0.577 → 0.690; LLaMA-3.2-1B: 0.332 → 0.431). This directly demonstrates that benefits from Arabic-translated test data transfer to English evaluation, which is the paper's central empirical contribution.

## Weaknesses

### Fatal
None.

### Major

1. **§4.2 directly contradicts Table 2.** The paper states "Across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and describes a "near-flat trend." This is factually incorrect: Table 2 shows MMLU accuracy increasing by 5–20 percentage points across contamination levels for every model (e.g., Mistral: 0.580→0.690; LLaMA: 0.381→0.431). The text references "Tables 2 and 3a" together as showing broad stability, but Table 2's MMLU column clearly does not. This is an internal inconsistency between the paper's analysis in §4.2 and its own presented data. While §4.1 correctly describes the MMLU increase, §4.2 contradicts it, undermining the paper's coherence and forcing readers to distrust the analysis. (Verified: lines 205–224.)

2. **Missing embedding figure with no data.** Section 4.3 states "The embedding figure shows that Arabic→English translations remain close to their English originals in representation space, with high cosine similarity s = cos(e^{ar→en}, e^{en})." No such figure exists in the paper—there is only Figure 1. No cosine similarity values, no visualization, and no numerical results are provided. This claim about the representational mechanism behind the "masking" effect is therefore unsubstantiated. (Verified: line 228; grep for "Figure [2-9]" returns no matches.)

3. **No standard contamination detection methods are tested despite claims otherwise.** The paper claims translation "conceals traditional contamination signals" (abstract) and "evade[s] standard detection tools" (conclusion), yet never applies any existing detection method (Min-K% Prob, guided prompting, exact/near-exact match search) to the contaminated models. The only detection probe used is the authors' own TS-Guessing variant, which produces noisy and often near-chance results (Table 3). Without testing whether standard methods would or would not detect the contamination, the claim about "evading standard detection tools" is unsupported. (Verified: §2.3 discusses existing methods, but §3.3 and §4.2 only apply TS-Guessing.)

4. **No statistical significance or variance reported.** All results in Tables 2 and 3 are single numbers with no standard errors, confidence intervals, or significance tests. Given the small number of models (4) and the noisy TS-Guessing results, it is impossible to assess whether observed differences (e.g., Qwen MMLU: 0.553→0.581) are meaningful or within noise. This is a standard expectation for empirical papers in this area and was noted in multiple calibration anchors (e.g., "Evading Data Contamination Detection" at 4.25 also had this critique).

### Minor

1. **TS-Guessing results are predominantly near-chance.** Table 3a shows MMLU IDR is near 0 for Mistral at all levels, near 0 for Gemma at 50% and 100%, and non-monotonic for LLaMA (0.287→0.643→0.410). Table 3b shows XQuAD TS-Guessing EM is near 0 for all models. While the LLaMA 50% IDR of 0.643 is notable (above random chance of 0.25), the overall picture is that the TS-Guessing probe detects contamination in only a small fraction of conditions. The paper's narrative treats these results as evidence of "masking," but they are equally consistent with the probe simply being insensitive.

2. **TACD is a conceptual outline only.** The paper describes TACD as a "forward-looking blueprint rather than a complete implementation" (§5.3). No experiments, validation, or even worked examples are provided. As a contribution, this is too preliminary to carry weight.

3. **The p=0 baseline is already contaminated with English test data.** The training mix D_train^d(p) = D_EN^d ∪ D_AR^d(p) means even at p=0, the model is fine-tuned on the English test set. Performance gains from adding Arabic translations could reflect cross-lingual transfer rather than contamination *per se*. The TS-Guessing probe partially addresses this (by testing position-level memorization), but the accuracy results alone cannot separate these mechanisms.

### Trivial

None.

## Nice-to-Haves

- Testing at least one standard detection method (e.g., Min-K% Prob) on the contaminated models would directly support or refute the claim that translation "evades standard detection tools."
- An English-only contamination control (fine-tuning on English paraphrases of the test set at equivalent rates) would help isolate whether translation specifically masks contamination more than paraphrase does.
- Reporting whether IDR values are above a well-defined random baseline (e.g., 0.25 for 4-choice MMLU) with statistical testing would strengthen the TS-Guessing analysis.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The central empirical claim is contradicted by the paper's own data" (harsh critic's point 1 in its strong form).** The critic argued this is a structural/fatal flaw. While §4.2's "near-flat" claim is indeed wrong for MMLU, the paper's broader finding (that translation does not eliminate contamination—models still benefit) is actually *supported* by the MMLU increases in Table 2. The problem is confined to the poor writing/analysis in §4.2, not the empirical core of the paper. Demoted from Fatal to Major (above).

- **"The evaluation design cannot separate contamination from cross-lingual transfer" (harsh critic's point 2).** This criticism is valid as a design limitation but overstates the problem: (a) the TS-Guessing probe specifically tests memorization of position-level information, which is a contamination signal not explainable by transfer; (b) the MMLU format (closed-book MCQ) limits cross-lingual transfer as an explanation since the model must retrieve facts, not align spans. The confound is real but partial, and the paper (especially §4.1) acknowledges the complexity. Demoted from Major to Minor (above).

- **"TACD is not a contribution."** The paper itself frames TACD as a "blueprint," which is standard for position/conceptual contributions. An unimplemented framework is a weak contribution but not zero—it identifies a gap and a direction. Demoted from Major to Minor (above).

- **Strength finder point 6 about embedding cosine similarity.** This strength claimed "quantitative explanation of translation's masking effect" but there is no figure or data presented—it is an unsubstantiated statement. Removed entirely as it does not exist in the paper.

- **Strength finder point about "systematic experimental design."** This is retained (Strength 1 above) but the strength finder's framing as "48 model/dataset/contamination combinations yielding reliable comparisons" somewhat overstates things given the lack of variance reporting.

- **Accusations about "missing related works."** Removed per instructions—I cannot verify whether related works exist.

- **Formatting/style nitpicks.** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Rewrite §4.2 to align with Table 2.** The "near-flat" characterization is wrong for MMLU. The section should either (a) acknowledge the MMLU increases as evidence that contamination persists under translation, then separately discuss the TS-Guessing results (Table 3a) which show that *this particular detection probe* yields weak/noisy signals under translation, or (b) clarify that "near-flat" refers only to the TS-Guessing probe results, with a clear distinction from the evaluation accuracy trends.
2. **Include the embedding analysis or remove the reference.** If the cosine similarity analysis exists, include the figure/data. If not, remove the unsupported claim from §4.3.
3. **Test at least one established detection method** (Min-K% Prob or guided prompting) on the models to directly support the claim that translation "evades standard detection tools."
4. **Add variance estimates** (e.g., bootstrap confidence intervals or standard errors) to Tables 2 and 3.

## Score and Decision

**Calibration Report:**

All anchors retrieved across rounds:

| Anchor | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| fSbPwHjdDG (Llamas think in English) | 3.00 | 1 (bracketing, low) | Topically related (multilingual LLM behavior). Weaker than this paper. |
| zkNCWtw2fd (Synergistic IR) | 3.00 | 1 (bracketing, low) | Less relevant. Comparable weakness. |
| MyotJECv0D (MT Eval Metrics) | 2.50 | 1 (bracketing, low) | Not contamination-focused. Weaker. |
| OdoS6cH8MP (Textual Data Valuation) | 2.00 | 1 (bracketing, low) | Weak paper. |
| Nsms7NeU2x (How much can we Forget?) | 6.75 | 1 (bracketing, mid) | Significantly stronger—has theoretical framework and extensive experiments. |
| BCyAlMoyx5 (Crosslingual Capabilities) | 5.67 | 1 (bracketing, mid) | Stronger—cleaner crosslingual evaluation. |
| Nk1MegaPuG (Evading Contamination Detection) | 4.25 | 1 (bracketing, mid) | **Most comparable anchor.** Similar topic (evading detection), similar weaknesses (incomplete validation, weak experiments). Slightly better organized. |
| m2NVG4Htxs (To the Cutoff...) | 6.75 | 1 (bracketing, mid) | Significantly stronger—longitudinal analysis with statistical rigor. |
| jOmk0uS1hl (Training on Test Task) | 8.00 | 1 (bracketing, high) | Far stronger—well-executed with clear conclusions. |
| 1oijHJBRsT (Instruction Backtranslation) | 8.00 | 1 (bracketing, high) | Unrelated topic, high quality. |
| syThiTmWWm (Cheating Benchmarks) | 7.75 | 1 (bracketing, high) | Far stronger—clever experimental design. |
| vf5aUZT0Fz (DEPT) | 8.00 | 1 (bracketing, high) | Unrelated. |
| rAylWUIKtu (Benchmark Inflation) | 4.25 | 2 (narrowing, 3.0–5.0) | Similar quality—methodological paper with limited scope and validation gaps. |
| lwtaEhDx9x (Elephants Never Forget) | 4.75 | 2 (narrowing, 3.0–5.0) | Better execution—clearer presentation and more thorough testing. |
| hFQZmKFtlT (Rethinking Memorization) | 3.50 | 2 (narrowing, 3.0–5.0) | Weaker—small-scale synthetic experiments with limited findings. |

**Round-1 bracket:** 3.0–6.0 (the paper is clearly above the weakest contamination papers at 2.0–2.5 but well below the rigorous ones at 5.67–6.75).

**Narrowing:** In round 2, the paper aligns most closely with "Evading Data Contamination Detection" (4.25) and "Benchmark Inflation" (4.25) in terms of quality and issues. It is weaker than "Elephants Never Forget" (4.75) due to the internal inconsistency in §4.2 and the missing figure. It is stronger than "Rethinking Memorization" (3.50). Given the significant but fixable issues, the paper sits at **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>