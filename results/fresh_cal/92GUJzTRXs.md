Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

This paper proposes ConDS (Context Distribution Shift), a method that modifies the distribution of a noisy ICL candidate set by augmenting samples that receive positive LLM feedback (computed on validation queries) and subsampling. The goal is to increase the probability of retrieving clean (informative) samples and decrease that of noisy (misleading) samples for test queries. ConDS can be combined with both off-the-shelf and fine-tuned retrievers. Experiments on 9 classification datasets under label noise show average improvements of 8.12% over the best baseline.

## Strengths

- **ConDS drastically increases the percentage of test queries with entirely clean retrieved ICL sets.** Figure 4 shows that on SST-2, 50.25% of test queries have 100% clean selected samples under ConDS, versus 0% for BM25, KNN, and PromptPG. This directly supports the claim that ConDS reduces the impact of noisy samples on retrieved sets.

- **ConDS delivers consistent accuracy gains across multiple tasks, retrievers, and noise settings.** Table 1 reports a 17.07% improvement over zero-shot and 8.12% over the best baseline on average across 9 datasets. Table 2 shows ConDS improves all 5 base retrievers (KNN, BM25, DPP, PromptPG, Random) by 1.26%–9.77%. Figure 5a shows consistent gains across noise ratios 0.1–0.6.

- **ConDS increases robustness to candidate set size variation.** Figure 5b shows PromptPG+ConDS has an accuracy difference of only 6.14% across candidate sizes 50–500, compared to 12.3% for PromptPG alone.

- **The method is conceptually simple and retriever-agnostic.** The distribution-shift mechanism operates on the candidate set itself rather than requiring a new retriever architecture, making it applicable to both off-the-shelf and fine-tuned retrievers.

## Weaknesses

### Fatal

- **The reward signal used to identify "informative" samples is computed against validation labels that are themselves noisy, creating a fundamental contradiction.** The paper's experimental setup (Section 4.1) injects noise (p=0.6) into the ICL Database *before* splitting 10% as C^{valid} (lines 130–132). Figure 1 explicitly states "we split the noisy candidate set." Yet Section 3.1 calls y_i^{valid} the "ground truth" (line 72) and uses EVAL(ŷ_i^{valid}, y_i^{valid}) as the reward signal. With 60% of validation labels being wrong, a correct LLM prediction is *penalized* 60% of the time, while an incorrect LLM prediction that happens to match the noisy label is *rewarded*. The paper itself acknowledges "noisy samples in the validation dataset" (line 157) but never addresses how the reward signal remains reliable under this condition. If the validation labels are indeed noisy (as the experimental description implies), the core feedback loop of ConDS is training on an unreliable or even anti-correlated reward signal, which would invalidate the claimed mechanism. The authors must clarify whether the validation set has clean labels (and if so, revise the ambiguous wording) or explain how ConDS functions despite a fundamentally corrupted reward signal.

### Major

- **The comparison protocol does not control for augmentation, conflating the effect of distribution shift with the effect of having more (and more copies of) samples.** ConDS augments informative samples up to α=1000 times before subsampling and retrieving from the modified set. Baselines retrieve from the *original* candidate set. The reported improvements (e.g., 8.12%) could partially or entirely reflect the fact that ConDS benefits from many augmented copies of clean samples rather than from the distribution-shift policy itself. A proper control would either (a) give baselines the same augmented candidate set (or an equivalently enlarged one via random duplication) or (b) compare against methods that also operate on the same modified set. Without this control, the contribution of the selective augmentation policy versus brute-force oversampling cannot be isolated.

- **The central claim of reducing noisy-sample impact "from almost all test queries to only a small percentage" is not supported by the reported evidence.** Figure 4 shows that ConDS raises the percentage of queries with 100% clean selected samples to 50.25% on SST-2. This means **49.75% of test queries still have at least one noisy sample** in their ICL set. The paper itself notes that "even a small percentage of noisy samples... has a chance to mislead the query answer" (line 157). A proportion of nearly 50% is not a "small percentage," and calling it such overstates the method's efficacy. The paper should characterize what fraction of queries remain vulnerable more precisely.

### Minor

- **The augmentation parameter α=1000 is extreme and its sensitivity is not studied.** Each informative sample is duplicated 1,000 times. No ablation shows performance at lower α values (e.g., 2, 10, 100) to demonstrate that the distribution shift, not brute-force duplication, drives the gains. If the method collapses at small α, its contribution is questionable.

- **The subsampling upper limit N_upp is never defined**, nor is the subsampling strategy described (random? uniform? score-based?). This is critical to understanding how the augmented set is controlled and how the distribution shift actually operates.

- **No standard deviations or per-seed results are reported.** Table 1 states "average performance of three random seeds" but provides no measure of variance. Given the small candidate set (N=200) and high noise (p=0.6), results could be noisy, and the reader cannot assess significance.

- **The conclusion claims experiments on "generative tasks"** (line 184), but all 9 datasets listed in Section 4.1 are classification tasks. Either generative experiments exist in the (stripped) appendix or the claim is inaccurate. This discrepancy should be resolved.

- **Computational cost is not discussed.** Augmenting each informative sample 1,000 times over multiple epochs could be expensive, especially for fine-tuned retrievers. A runtime comparison with baselines is needed.

### Trivial

- None beyond the presentation issues addressed above.

## Nice-to-Haves

- An analysis of failure cases: what happens when validation queries themselves are mostly noisy and misguide the augmentation?
- Sensitivity analysis for the number of epochs.
- Experiments on larger LLMs (beyond GPT-Neo-2.7B) to test generality.

## Removed Points

The following points from the input reviews were removed with justification:

- **"The 'noise in ICL is largely overlooked' claim is inaccurate because prior work observed it."** The paper correctly distinguishes between *observing* the phenomenon (Kossen et al., Wei et al.) and *solving* it. The harsh critic's objection is based on a misreading.
- **"The problem formulation should specify whether input or label is noisy."** Context makes clear it is label noise. This is a minor clarity preference, not a weakness.
- **"Missing related works"** — I cannot verify the existence of missing citations; remove per rules.
- **"Missing appendix content / theoretical analysis"** — Remove per rules (appendix stripped by parser).
- **"The comparison with Cheng et al. should be more thorough."** The paper provides a valid explanation of why training-time noise injection doesn't apply to black-box LLMs. The criticism is unspecific.
- Several formatting/presentation nitpicks — removed per rules (parser artifacts, not author errors).
- **"The paper should be rejected" (from the harsh critic's overall assessment)** — incorporated into score judgment; not a standalone weakness.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely confirm the paper's strengths and surface a set of concerns (validation label ambiguity, comparison fairness, overclaimed statements) that are common critiques for papers presenting empirical methods with incomplete controls.

## Suggestions

1. **Clarify the validation set label status explicitly.** State whether the 10% validation split occurs before or after noise injection. If the validation labels are clean, clarify the experimental procedure; if they inherit the noise, explain how the reward signal remains valid (or acknowledge the limitation).
2. **Add a control experiment where baselines receive the same augmented candidate set** (or a randomly augmented set of the same size) to isolate the effect of the selective distribution-shift policy from brute-force oversampling.
3. **Replace the "small percentage" wording** with a precise characterization (e.g., "reduces the fraction of queries with any noisy samples from 100% to 49.75%").
4. **Provide standard deviations** for all reported results.
5. **Study sensitivity to α** across a wide range (e.g., 2, 10, 100, 1000) to show the method works without extreme augmentation.
6. **Define N_upp and the subsampling procedure.**

## Score and Decision

**Originality:** The idea of iteratively shifting the candidate set distribution for robust ICL is novel. **Importance:** The problem of label noise in ICL is practically relevant. **Claims support:** The central claims are partially supported, but the validation label ambiguity and lack of comparison controls weaken the evidence significantly. **Soundness:** The experimental design has serious gaps (no control for augmentation, no variance reporting, underspecified parameters). **Clarity:** Generally readable but contains a critical ambiguity about validation labels. **Value:** Potentially valuable if the core issues are resolved, but cannot be accepted in the current form.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>