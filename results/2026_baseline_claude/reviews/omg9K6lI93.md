## Summary
The paper investigates whether translating English benchmarks into Arabic (a lower-resource language) provides a natural barrier against data contamination or merely masks it. The authors fine-tune four open-weight LLMs on varying proportions (0–100%) of Arabic-translated benchmark data (MMLU, XQuAD, MLQA) and evaluate on the original English benchmarks. They extend the TS-Guessing method with a choice-reordering strategy and propose a Translation-Aware Contamination Detection (TACD) framework as a conceptual blueprint for multilingual contamination auditing.

---

## Strengths
- **Novel and practically relevant research question.** Investigating whether translation constitutes a contamination "blind spot" is timely and important. As multilingual training data and benchmarks proliferate, understanding cross-lingual contamination dynamics is a genuine open problem the community has not systematically studied.
- **Systematic contamination bucket design.** Controlling the proportion of Arabic-translated benchmark data (p ∈ {0, 10, 50, 100}%) across three datasets and four models is a clean, interpretable experimental design that isolates the variable of interest.
- **Modest methodological extension (TS-Guessing + choice-reordering).** Adding a choice-shuffle step before masking an incorrect answer is a useful augmentation to the existing TS-Guessing method; it specifically targets index-letter recall, which is a crisp contamination signal independent of content reasoning.

---

## Weaknesses

### Fatal
**No English-only contamination baseline, making the central masking claim unverifiable.** The paper's thesis is that "Arabic translation masks contamination signals." To establish masking, one must first demonstrate what unmasked contamination looks like in this setup — that is, fine-tuning on the *English* benchmark content at the same proportions and measuring the resulting performance and TS-Guessing signals. Without this comparison, there is no way to attribute observed differences (or the lack thereof) to the masking effect of translation. The paper never performs this control, so the "masking" interpretation is not causally grounded.

**The training always includes the English test data in all conditions.** The training set is defined as $\mathcal{D}_{\text{train}}^d(p) = \mathcal{D}_{\text{EN}}^d \cup \mathcal{D}_{\text{AR}}^d(p)$, meaning the English version of the benchmark is in every model's fine-tuning corpus, including the "zero Arabic" baseline ($p=0$). As a result, all four conditions already constitute contamination with the exact English evaluation data. The experiment therefore does not measure whether Arabic data masks contamination; it measures whether *additional* Arabic exposure amplifies already-existing English contamination. This is a fundamentally different and much narrower question than the one the paper claims to answer.

### Major
**TS-Guessing results are nearly flat and very low, which the paper interprets as confirmation of masking, but this is self-contradictory.** Mistral-7B shows IDR=0.000 at every contamination level (Table 3a). Qwen's IDR declines with more contamination. LLaMA shows non-monotonic IDR (0.287→0.643→0.410). These signals don't clearly separate contamination levels, which the authors attribute to translation masking. However, this interpretation requires demonstrating that TS-Guessing *would* fire under English contamination — which is again missing from the design. The near-zero IDR and RL-F1 values throughout are also consistent with TS-Guessing simply being ineffective at detecting cross-lingual leakage, a distinct and more parsimonious explanation.

**Non-monotonic XQuAD/MLQA results directly conflict with the contamination-benefit narrative.** For Mistral, XQuAD *collapses* from 0.455 to 0.114 as contamination increases; for Qwen, MLQA spikes at 10% then collapses to 0.15; Gemma's MLQA is non-monotonic. The paper explains these patterns post-hoc as "overfit to distributional quirks," "fragile transfer," and "dataset-specific leakage." These explanations are plausible but are not tested, and they introduce heterogeneous mechanisms that undermine the unified claim that "translation masks contamination while models still benefit." A model that degrades on extractive QA with more contamination is not simply a masked-but-benefiting case.

**MMLU gains are confounded with legitimate cross-lingual knowledge transfer.** The paper observes that MMLU accuracy rises monotonically as Arabic benchmark exposure increases, and attributes this to contamination. However, fine-tuning on Arabic QA covering the same subject matter (e.g., MMLU topics translated to Arabic) would naturally improve cross-lingual knowledge regardless of contamination. The paper does not test whether the same gains occur when training on topically matched but *non-overlapping* Arabic content, so the monotonic gain cannot be attributed specifically to memorization of benchmark answers rather than topic-level knowledge acquisition.

### Minor
**The TACD framework is entirely conceptual.** Section 5 presents TACD as the paper's prescriptive contribution, but the authors explicitly state it is "a forward-looking blueprint rather than a complete implementation." No quantitative analysis, prototype, or even simulated evaluation demonstrates TACD's effectiveness. The framework's components (cross-translation benchmarking, TS-Guessing across variants, back-translation consistency) are reasonable ideas but remain unvalidated.

**Embedding analysis referenced but unexplained in the main text.** Section 4.3 states "The embedding figure shows that Arabic→English translations remain close to their English originals in representation space," but the embedding analysis is presented without naming the figure or detailing the model, layer, or method used to compute the cosine similarity. The claim is central to explaining why translation preserves contamination, yet the evidence is left implicit.

### Trivial
- The literature review (Section 2) is very long and organized as a self-contained survey rather than a focused motivation for the gap addressed in this paper.

---

## Nice-to-Haves
- An English-only contamination condition (fine-tune only on English test items without any Arabic) at matching p levels, which would serve as the critical comparison to establish whether the cross-lingual case differs from direct English contamination.
- A topically-matched but non-overlapping Arabic control corpus (same subjects as MMLU but drawn from Arabic-language educational resources never included in MMLU) to disentangle knowledge transfer from memorization.
- A brief quantitative pilot of TACD — even on a single benchmark with two translation variants — to provide empirical support for the framework.
- Per-subject MMLU breakdown to verify whether score gains are uniform or concentrated in topics where the Arabic translated training items have direct lexical correspondence to the test items.

---

## Novel Insights
The paper points to a real and insufficiently explored concern: multilingual fine-tuning pipelines may inadvertently create evaluation shortcuts that bypass standard English-centric contamination detectors, since surface-form matching tools will miss cross-lingual semantic overlap. The choice-reordering augmentation to TS-Guessing is a sensible idea for separating index memorization from answer reasoning. However, the experiments as designed do not cleanly establish the proposed mechanism — translation masking that preserves benefit — primarily because all models are fine-tuned on English test data from the start and no English-only contamination baseline is provided. The observations (monotonic MMLU gains, heterogeneous QA behavior, low TS-Guessing signals) are interesting but do not unambiguously support the stated conclusions.

---

## Suggestions
1. Add an English-only contamination condition (train on $\mathcal{D}_{\text{EN}}^d$ only at matched proportions) to serve as the unmasked reference point.
2. Redefine the training sets so $p=0$ means no benchmark data at all (neither English nor Arabic), making the baseline truly contamination-free.
3. Include a non-overlapping Arabic control corpus to test cross-lingual knowledge transfer vs. memorization.
4. Provide a worked pilot of TACD on at least one benchmark/language pair with quantitative results.
5. Show TS-Guessing results stratified by subject domain in MMLU; if contamination is driving MMLU gains, the domains with highest gains should show elevated TS-Guessing signals.

---

## Score and Decision

The paper raises a genuinely important and underexplored question about multilingual contamination. However, the experimental design contains a fatal structural flaw (English test data present in all conditions) that makes the core "masking" claim unestablishable from the data. The lack of an English-only contamination baseline means the central causal comparison is absent. Non-monotonic results in QA tasks are explained post-hoc without additional tests, and the proposed TACD framework is unvalidated. These are not minor gaps but structural issues that prevent the paper's claims from being scientifically established in their current form.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>