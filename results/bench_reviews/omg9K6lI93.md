Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper investigates whether translating evaluation benchmarks into Arabic can mask data contamination in LLMs. The authors fine-tune four open-weight models on mixtures of English and Arabic-translated benchmark data (MMLU, XQuAD, MLQA) at varying contamination levels and evaluate on the original English benchmarks. They extend the TS-Guessing memorization probe with a choice-reordering strategy for multiple-choice questions. The paper claims that Arabic translation masks contamination signals (making them harder to detect via surface-form methods) while contaminated knowledge continues to inflate performance, and proposes a Translation-Aware Contamination Detection (TACD) framework as a forward-looking solution.

## Strengths

- **Underexplored research question.** Investigating contamination dynamics across language barriers — specifically whether translation into a low-resource language can conceal memorization — addresses a genuine gap in the contamination literature, which has focused almost exclusively on English.
- **TS-Guessing extension with choice reordering is a creative diagnostic.** The index-recall rate (IDR) metric for MCQ tasks — checking whether a model reproduces the pre-shuffle answer letter after options are randomly reordered — provides a conceptually clean, surface-form-independent probe of index-level memorization (Table 3a).
- **Cross-model, multi-benchmark experimental scope.** The study covers four model families (Mistral, Gemma, LLaMA, Qwen) across three benchmarks (MMLU, XQuAD, MLQA), revealing task-dependent contamination dynamics: monotonic MMLU accuracy gains contrast with erratic, model-specific patterns on extractive QA, which is a genuinely interesting observation.

## Weaknesses

### Fatal
*None.*

### Major

- **Self-contradictory claim about performance flatness.** Section 4.2 states that "across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and interprets this as evidence that translation masks contamination. Table 2 directly contradicts this for MMLU: Mistral rises from 0.580→0.690, LLaMA from 0.381→0.431, Qwen from 0.560→0.581, and Gemma from 0.244→0.284. These are not "approximately equal." The paper acknowledges monotonic MMLU gains in Section 4.1 but then makes a contradictory interpretive claim in Section 4.2. This undermines the paper's central narrative about translation masking.

- **No same-language contamination condition.** The paper's headline claim — that Arabic translation specifically *masks* contamination signals compared to what would be observed with direct English contamination — cannot be evaluated without a condition where models are contaminated with English test data at comparable levels. Without this comparison, the paper can only show that Arabic-translated contamination produces some performance effects, not that translation uniquely *conceals* those effects relative to same-language leakage. This is a critical missing baseline for the paper's core argument.

- **Ambiguous specification of training data.** Section 3.1 defines D_EN^d as "the English split" with the parenthetical "MMLU: English test items formatted as MCQ; XQuAD/MLQA: English QA." The phrase "test items" creates genuine ambiguity about whether the English evaluation data is included in training. While the reasonable baseline scores (e.g., Mistral MMLU 0.577 at p=0) suggest this is not the case and that D_EN^d likely refers to English training data, the description is so unclear that it invites exactly the kind of misinterpretation that could undermine confidence in the entire experimental design. The paper must unambiguously specify which data splits are used for training vs. evaluation.

### Minor

- **Missing TS-Guessing baseline at p=0.** The TS-Guessing results (Table 3) are reported only for p ∈ {10, 50, 100}%. Without a p=0 (clean) baseline, the IDR and ROUGE-L values cannot be properly contextualized. While IDR values like 0.643 for LLaMA at 50% contamination are well above the chance rate of 0.25, the 0.287 at 10% is only marginally above chance, and a clean baseline would clarify whether these signals genuinely reflect contamination-driven memorization or baseline model behavior.

- **Embedding similarity analysis is mentioned but not presented.** Section 4.3 references an "embedding figure" showing that Arabic→English translations remain close to English originals in representation space with "high cosine similarity," but no figure, quantitative results, or layer-wise analysis appear in the paper. This leaves a key piece of the paper's mechanistic argument (that translation preserves semantic content sufficient for memorization transfer) entirely unsupported.

### Trivial

- **TS-Guessing implementation details for IDR are underspecified.** For MMLU, the paper does not specify whether the model is prompted to output a single letter or free text, nor how the model's generated output is mapped to the predicted letter ℓ̂_i for IDR computation.

## Nice-to-Haves

- A same-language (English) contamination condition at matched contamination levels to directly test whether translation specifically *masks* contamination relative to direct English leakage.
- Confidence intervals or per-run variance for accuracy and TS-Guessing metrics — the paper reports point estimates and discusses trends (peaks, monotonic increases) without any indication of statistical reliability.
- Pre-fine-tuning Arabic capability measurements for all models to substantiate the claim that "models with stronger Arabic capabilities" benefit more from Arabic-translated contamination.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim that the experimental design trains on evaluation data (fatal design flaw):** This interpretation reads "English test items formatted as MCQ" literally as evaluation test items. However, the baseline MMLU scores (e.g., Mistral 0.577 at p=0) are in the normal range for these models, not inflated as they would be if trained directly on the evaluation set. The phrase likely describes the format of MMLU items (all are MCQ test-style items), not the data split. The ambiguity is a real issue (kept as a major weakness above), but the claim that the design is fatally and irrecoverably flawed is not supported by the evidence. **Removed.**

- **Harsh Critic claim that the literature review is "disproportionately long" and "not tightly connected":** This is a subjective presentation critique, not a substantive weakness. The review provides useful context on contamination types and detection methods. **Removed.**

- **Harsh Critic claim about "no comparison against a same-language contamination condition" already covered in weaknesses above; the claim that TACD "does not constitute a substantive contribution":** The paper is explicit that TACD is a "blueprint, not a complete implementation" — this is a scoping choice, not a flaw. The TACD section provides a reasonable forward-looking framework. **Weakened to Nice-to-Have suggestion about same-language comparison.**

- **Strength Finder claim that the paper "demonstrates that translation does not eliminate contamination":** This overstates the evidence. The paper shows MMLU gains with Arabic-translated contamination, which supports the claim, but without a same-language comparison and with the self-contradictory "flatness" claim, the strength is qualified. **Retained with caveats.**

## Novel Insights

The most genuinely novel observation from this work is the task-dependent asymmetry in how contamination transfers across languages: closed-book MCQ (MMLU) shows reliable, monotonic gains from Arabic-translated contamination, while extractive QA (XQuAD, MLQA) exhibits erratic, model-specific, and sometimes catastrophic patterns (e.g., Mistral XQuAD collapsing from 0.455 to 0.114). This suggests that translation-mediated contamination does not uniformly inflate all benchmark types and that memorization of surface options may help multiple-choice tasks while harming the fine-grained semantic alignment needed for span extraction. This task-type interaction merits further investigation beyond what the paper provides.

## Suggestions

- **Clarify data splits unambiguously.** Explicitly state which MMLU/XQuAD/MLQA splits (train, validation, test) are used in D_EN^d and D_AR^d. This is essential for readers to trust the experimental design.
- **Resolve the self-contradiction between Sections 4.1 and 4.2.** Either revise the "approximately equal performance" claim to accurately reflect the MMLU trends, or provide a quantitative justification for calling the observed differences "approximately equal."
- **Add a p=0 TS-Guessing baseline.** Even if only for one model, this would anchor the IDR and ROUGE-L values and dramatically improve interpretability.
- **Present the embedding similarity analysis** with actual figures, cosine similarity values, and layer-wise comparisons, or remove the reference to it.

---

### Anchor Comparison

- **GFDSGlEks2** (avg 4.67, Reject) — Contamination + post-training study. More rigorous experimental design, clearer baselines, error bars. Our paper has a more novel angle (translation) but is weaker in execution.
- **WFGxFzFDmQ** (avg 5.00, Reject) — Watermarking for contamination detection. Novel method with theoretical guarantees, much more substantive contribution. Our paper falls short of this standard.
- **YlpaaYxx4t** (avg 5.33, Accept Poster) — CoDeC detection method. Clean idea, strong empirical results, well-executed. Clearly superior to our paper.
- **WERLf030OU** (avg 3.00, Reject) — LogProber. Limited scope, thin experiments. Our paper has broader experiments and a more interesting thesis.
- **x4vwdjckZ6** (avg 4.00, Reject) — SLM contamination sensitivity. Systematic across 23 models, clear methodology. Comparable contribution level; our paper has a more novel question but weaker execution.
- **vkTl53bXMs** (avg 2.00, Reject) — PEARL. Fundamentally flawed methodology, all scores of 2. Our paper is clearly stronger.

**Calibration:** This paper sits between WERLf030OU (3.0) and GFDSGlEks2 (4.67). It is more ambitious and interesting than LogProber but lacks the rigor of the post-training contamination study. The self-contradictory claims and missing baselines prevent it from reaching the 4.5+ range but it is not fundamentally broken. A score of 4.0 reflects a paper with a genuinely interesting research direction and a creative probe (TS-Guessing + IDR) that is undermined by presentation issues, ambiguous methodology, and an overclaimed central argument.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>