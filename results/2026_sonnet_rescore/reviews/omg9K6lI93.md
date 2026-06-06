Now let me write the final consolidated review based on my reading of the paper.

---

## Summary
This paper investigates whether translating English benchmarks (MMLU, XQuAD, MLQA) into Arabic can mask data contamination while still allowing models to benefit from memorized benchmark content. The authors fine-tune four open-weight LLMs under varying proportions of Arabic-translated benchmark data using LoRA/PEFT, extend the TS-Guessing contamination probe with a choice-reordering mechanism, and propose a Translation-Aware Contamination Detection (TACD) framework as a forward-looking blueprint.

---

## Strengths

- **TS-Guessing extended with choice-reordering (Section 3.3, Figure 1, Table 3a):** The MCQ protocol shuffles answer options then masks one choice, measuring whether the model recalls the pre-shuffle answer-letter index. This is a concrete methodological contribution to contamination probing; the IDR results for LLaMA (0.287–0.643, substantially above the 0.25 chance baseline) demonstrate that Arabic-translated contamination does leave detectable memorization traces in some models, directly supporting the paper's thesis that translation masks but does not eliminate contamination.

- **Controlled multi-model experiment across contamination levels (Section 3.1, Table 2):** Four open-weight models are fine-tuned under identical LoRA/PEFT hyperparameters across four contamination buckets, enabling fair cross-model comparisons. MMLU accuracy rises monotonically with contamination for all four models (Mistral: 0.577→0.690; LLaMA: 0.332→0.431; Gemma: 0.220→0.284; Qwen: 0.553→0.581), providing concrete evidence that contamination effects persist through translation.

---

## Weaknesses

### Fatal
None.

### Major

- **No clean uncontaminated baseline — the p=0 condition is already contaminated.** The training formula in Section 3.1 is $\mathcal{D}_{\text{train}}^d(p) = \mathcal{D}_{\text{EN}}^d \cup \mathcal{D}_{\text{AR}}^d(p)$. The paper confirms $\mathcal{D}_{\text{EN}}^d$ for MMLU consists of "English test items formatted as MCQ," and this English benchmark split is present in *every* training condition, including p=0. The p=0 condition is not an uncontaminated reference; it is the English-contaminated condition. The experiment therefore does not test "does Arabic translation conceal contamination versus a clean model?" but rather "does adding Arabic-translated benchmark data on top of universally English-contaminated training produce additional or different effects?" These are fundamentally different questions. A truly uncontaminated baseline (no benchmark data in any language) is needed to support the paper's framing of Arabic translation as a "mask," and without it, the contamination effects attributed to translation cannot be cleanly separated from those attributable to the ever-present English contamination.

- **Contradictory interpretive claims between Sections 4.1 and 4.2.** Section 4.1 correctly characterizes MMLU trends as "a generally monotonic increase as contamination rises from 0%→100%" and attributes this to "contamination-driven memorization." Section 4.2, examining p ∈ {10, 50, 100}%, then claims "the models exhibit approximately equal performance on all evaluated benchmarks" and describes a "near-flat trend" as evidence of masking. These are contradictory readings of the same tables. Looking at Table 2, Mistral MMLU goes from 0.580 (10%) to 0.690 (50%)—a 19% relative increase—and LLaMA goes from 0.381 to 0.431. These are not flat. By restricting the "near-flat" claim to p={10,50,100} and not comparing against the p=0 baseline, Section 4.2 mischaracterizes the data while Section 4.1 reads it correctly.

- **Cross-lingual transfer confound for XQuAD and MLQA results.** XQuAD and MLQA are designed as parallel cross-lingual benchmarks: the Arabic and English splits share the same underlying passages. Training on the Arabic split of XQuAD and evaluating on the English split naturally produces performance gains through well-documented cross-lingual transfer—independent of any contamination dynamic. The paper does not acknowledge or control for this. The XQuAD gains (Gemma: 0.364→0.606; LLaMA: 0.364→0.569) may be partially or largely attributable to cross-lingual transfer rather than contamination-mediated memorization. The MMLU results (same-language, closed-book MCQ) are more defensible as a contamination probe and should carry more weight than XQuAD/MLQA in supporting the paper's conclusions.

- **"Stronger Arabic capabilities" claim in the abstract is unsupported.** The abstract states models "still benefit from exposure to contaminated data, particularly those with stronger Arabic capabilities." No measurement of Arabic language proficiency is reported anywhere in the paper. No ranking or comparison of models by Arabic proficiency is provided. The claim is treated as a given interpretation when explaining model differences (Gemma/LLaMA gaining on XQuAD, Mistral declining), but without an actual Arabic proficiency measure, this remains a hypothesis not a finding.

### Minor

- **TS-Guessing near-zero EM for XQuAD/MLQA may indicate method failure rather than masking.** Table 3b shows XQuAD EM values of 0.001, 0.005, 0.008 for LLaMA across contamination levels. These are essentially zero. The paper interprets this as masking. However, the masked-token TS-Guessing method as applied to extractive QA (masking a question word, asking the model to recover it from context) may simply not be a sensitive contamination probe—the method's floor on genuinely uncontaminated data is not established. Without a positive-control validation (a setting where contamination is known and the method should fire), the near-zero results are uninterpretable.

- **IDR metric may partially conflate memorization with positional bias.** The IDR measures whether the model predicts the *pre-shuffle* answer letter after reordering. If some models have a systematic positional preference (e.g., tendency to output "A"), this could inflate IDR without reflecting genuine memorization. The paper does not analyze whether IDR values above chance differ from what would be expected from known model positional tendencies.

### Trivial
None beyond parser artifacts in the extracted text (not author problems).

---

## Nice-to-Haves

- An ablation with an Arabic-only contamination condition ($\mathcal{D}_{\text{AR}}^d$ only, no English data), alongside a non-benchmark Arabic fine-tuning control (e.g., Arabic Wikipedia), would enable clean triangulation of the translation-mediated contamination effect distinct from direct English contamination and generic cross-lingual transfer.
- Reporting model performance on Arabic evaluation benchmarks (e.g., ArabiQ, Arabic MMLU) would substantiate the claim about Arabic capability as a moderating variable, turning an unsupported interpretive claim into an evidenced finding.
- A positive-control validation of the TS-Guessing method in a setting where contamination is known to be present and fully English would establish the method's sensitivity before applying it to the ambiguous translated setting.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic's framing of the baseline issue as "structural/fatal" requiring complete experimental redesign:** While the baseline issue is serious (correctly retained as Major), the harsh critic's claim that it makes the *entire empirical contribution* worthless is too strong. The IDR results (above-chance recall for LLaMA in Table 3a) remain meaningful evidence of memorization persistence through translation, and the monotonic MMLU gains in Table 2 are real data. Demoted to Major.

- **Strength Finder's claim about "rigorous experimental design" as a strength:** Given that the baseline is already contaminated (Major weakness) and the XQuAD/MLQA results conflate transfer with contamination (another Major weakness), calling the experimental design "rigorous" is contradicted by verified weaknesses. Removed per filtering discipline.

- **Strength Finder's claim about TACD as a "forward-looking solution" strength:** TACD is explicitly offered by the authors themselves as "a forward-looking blueprint rather than a complete implementation" (Section 5.3). It is unvalidated and unimplemented. Not a strength in the usual sense; it is an agenda section. Removed.

---

## Novel Insights

The TS-Guessing IDR results in Table 3a offer a moderately novel finding: memorization signals from Arabic-translated contamination are not uniformly masked—some models (LLaMA at 50%: IDR 0.643) exhibit strong pre-shuffle recall above chance, while others (Mistral: IDR ≈ 0.000; Gemma at 100%: IDR 0.005) appear nearly undetectable. This model-level variance in IDR could reflect differences in how models internalize label positions versus semantic content during fine-tuning, suggesting that contamination via translation interacts with model architecture or training regime in non-trivial ways. However, the paper does not analyze this variation systematically, leaving it as an unexplained empirical pattern rather than a grounded finding.

---

## Suggestions

1. Add a clean control condition ($p=\emptyset$, no benchmark data in any language) as the true uncontaminated baseline, which is the necessary anchor for all contamination claims.
2. Add an Arabic-only condition ($\mathcal{D}_{\text{AR}}^d$ only, no English benchmark data) to isolate the pure translation-contamination effect.
3. Revise Section 4.2 to accurately describe the data: MMLU shows monotonic increases (as correctly stated in 4.1), and the "near-flat" framing is inconsistent with Mistral's 0.580→0.690 jump and LLaMA's 0.381→0.431 increase within the 10–100% range.
4. For XQuAD/MLQA, explicitly model and test the cross-lingual transfer alternative hypothesis—ideally by comparing against a non-benchmark Arabic fine-tuning condition or citing literature on expected cross-lingual transfer gains for these model families.
5. Measure Arabic language proficiency directly (e.g., on an Arabic-language benchmark) to ground the "stronger Arabic capabilities" moderator claim in evidence.

---

## Assessment on Key Axes

**Originality:** Moderate. The core question (does multilingual translation mask contamination?) is underexplored and genuinely interesting. The choice-reordering extension of TS-Guessing is novel but modest. The TACD framework is an agenda item rather than a contribution.

**Importance of research question:** High. Multilingual contamination is a real blind spot in current evaluation practice, and the concern raised here has broad implications for multilingual LLM benchmarking.

**Claims well-supported:** Weak. The paper's primary claim—that Arabic translation masks contamination while effects persist—is partially supported by the IDR results and MMLU trends, but is seriously undermined by the absence of a clean baseline and the contradiction between Sections 4.1 and 4.2. The Arabic-capability moderator claim is unsupported.

**Soundness of experiments:** Weak-to-moderate. The multi-model, multi-contamination-level design is sensible, but the training formula ensures no condition is truly uncontaminated, and the XQuAD/MLQA results conflate cross-lingual transfer with contamination effects.

**Clarity of writing:** Moderate. The literature review is thorough but lengthy relative to its payoff. The internal contradiction between 4.1 and 4.2 suggests the discussion was not carefully integrated.

**Value to research community:** Moderate. The work points at a real problem and the IDR methodology is a useful probe. As currently written, however, the experimental design does not cleanly test the stated hypothesis, and the conclusions should be treated as preliminary findings rather than established evidence.

---

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>