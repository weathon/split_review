Here is the final consolidated review.

---

## Summary

This paper proposes Conformal Language Modeling, a method for producing prediction sets from generative LMs with rigorous distribution-free coverage guarantees. The key innovation is calibrating a *sampling* algorithm (a stopping rule, quality filter, and diversity filter) rather than enumerating the intractable output space, using the Learn-Then-Test (LTT) framework. The method also extends to component-level guarantees for identifying correct subparts of long generations.

## Strengths

1. **Principled calibration of sampling-based stopping rules for LMs (Section 4, Theorem 1, Lemma 1).** The paper addresses a fundamental limitation of standard conformal prediction — requiring enumeration of the output space — by treating hyperparameters λ = (λ₁, λ₂, λ₃) as parameters of a *sampling algorithm*. Theorem 1 proves via LTT that the resulting procedure satisfies Eq. (4)'s coverage guarantee, and Lemma 1 provides valid p-values via binomial tail bounds. This is a genuinely novel direction.

2. **Component-level conformal selection with formal guarantees (Section 3.4, Proposition 2).** The paper extends guarantees to individual subcomponents of long generations. Proposition 2 proves that the component-coverage guarantee (controlling false positives) holds simultaneously with the set-level guarantee via a union bound (with probability ≥ 1−2δ). This addresses the practically important setting where LM outputs mix correct and incorrect statements.

3. **Empirical validation across three diverse tasks and model families (Figure 3, Section 6).** The experiments cover radiology report generation (ViT+GPT2), news summarization (T5-XL), and open-domain QA (LLaMA-13B few-shot) — substantially different output structures and model architectures. The likelihood-based scoring functions (Max, Sum) achieve valid coverage (loss never exceeds the diagonal) while producing more efficient sets than the First-K baseline. For QA, the AUC of expected set size for Max and Sum is "less than half the AUC of First-K" (line 317).

## Weaknesses

### Fatal
None.

### Major

1. **Admission function gap: the guarantee is about automated metrics, not factual correctness.** The paper's abstract and introduction use terminology like "correctness," "hallucinations," and "trustworthy predictions" (Section 1, line 16), tacitly inviting readers to equate "admissible by the admission function" with "factually correct." However, the admission functions are automated metrics: ROUGE-L ≥ 0.35 for summarization, CheXbert label matching for radiology, exact string match for QA. The guarantee is that the set contains a response scoring above a threshold on an automated metric against a human-written reference — not that it is correct in any direct sense. For instance, in the radiology setting, the guarantee is only as good as CheXbert's label extraction accuracy and the reference's completeness. The paper does not directly acknowledge this gap or validate that the admission functions correlate with human judgments of correctness.

2. **No ablation isolating the contribution of the three λ components.** The method has three hyperparameters controlling diversity (λ₁), quality (λ₂), and stopping (λ₃). There is no ablation that isolates each component's contribution to efficiency gains. What does the method achieve with the stopping rule alone (λ₃ only) but no rejection (λ₁, λ₂ disabled)? Or with rejection but no stopping rule? Without such ablations, it is unclear which component drives the reported gains, and whether the rejection rules sometimes harm coverage or efficiency. This is the single most important missing experiment.

3. **Component selection results lack quantitative specificity in the main text.** The component-level results are described in a single paragraph (Section 6, lines 320–321) with no numerical values — not even the AUC values reported for the main method. The paragraph states that modeling components independently "produces better (larger) sets" than Random, but "better" is not quantified with any numbers. No table of false positive rates or average selected-component counts appears in the main text. Readers cannot evaluate this claimed contribution based solely on what is in the main body.

### Minor

1. **Reuse of calibration data for secondary λ selection creates mild optimism bias.** The paper uses D_cal to both identify Λ_valid (via LTT) and select among Λ_valid configurations by minimizing set size + excess samples (Eq. 4). While the coverage guarantee is preserved (it holds for any λ ∈ Λ_valid), the efficiency numbers (set size, excess samples) for the selected λ are computed on the same data used to choose λ. This likely biases reported efficiency metrics optimistically. The paper acknowledges this ("reusing D_cal," line 173) but does not quantify its impact.

2. **Admission thresholds are chosen by vague "manual validation."** The summarization ROUGE-L threshold (0.35) and component thresholds (0.4) are "picked through manual validation" (line 230) with no detail on the validation procedure, held-out data, or selection criterion. These thresholds directly determine what "coverage" means.

3. **Component selection guarantee is about precision, not recall.** Proposition 2 guarantees control of the false positive rate among selected components — it ensures that selected components are likely correct, but does not guarantee that most correct components are selected. The abstract's phrasing ("identify subsets of individual components... that are each independently correct") could mislead readers about what is actually proven. The formal treatment (Eq. 5, line 206) is correct, but the exposition would benefit from stating this precision-versus-recall distinction explicitly.

### Trivial
- The Bernoulli process toy example (Section 4.2) is acknowledged by the authors as unrealistic ("of course, in reality we do not know p"), and is intended only for intuition. Including it or omitting it has no bearing on the paper's contribution.

## Nice-to-Haves
- A comprehensive table collecting AUC values and standard deviations for all (task × method × metric) combinations, rather than relying solely on visual estimation from plots.
- A discussion of the computational cost of calibration: grid size κ, number of LM API calls required, and how this scales with the grid dimension.
- A small-scale human evaluation validating that the admission functions correlate with human judgments of correctness.
- An analysis of when Λ_valid is empty and what ε values become unachievable given k_max = 20.

## Removed Points
These points were surfaced by reviewers but are removed as non-actionable, inaccurate, or outside scope:
- **"Pareto Testing is cited rather than explained"** — Standard practice; the paper builds on existing work and describes the high-level idea. Removed.
- **"ROUGE-L threshold of 0.35 seems low"** — Design choice, not a paper flaw. Removed.
- **"ROUGE-L for both admission and similarity creates a confound"** — Speculative concern about a reasonable design choice; the two functions serve different roles. Removed.
- **"No variance/confidence intervals for AUC"** — Standard deviations are shown in the loss/size/samples curves as shaded regions. Removed.
- **"Max variant missing from scoring functions text"** — This is a PDF parsing artifact (the itemize environment is garbled in extraction). The original submission defines it. Removed.
- **"The results section is only one page"** — Too general; the underlying specific points (missing numbers, no ablations) are kept above. Removed.
- **Generic strengths about "important problem"** — Removed as superficial; the strengths kept above are concrete and grounded in the paper's specific contributions.

## Novel Insights
None beyond the paper's own contributions. The key insight — calibrating the *sampling process* itself rather than enumerating the output space — is the paper's core contribution, and it is well-articulated.

## Suggestions
1. **Add ablations** isolating the three λ components (stopping only, stopping + quality, stopping + diversity, all three) to show which design choices drive efficiency gains.
2. **Report quantitative component results** in the main text: at minimum a table with false positive rates and average selected-component counts for each method.
3. **Provide a comprehensive results table** with AUC values and standard deviations for all task × method × metric combinations.
4. **Acknowledge the admission function gap explicitly** and discuss its implications for interpreting the guarantees (e.g., the guarantee inherits the limitations of the automated metric).
5. **Use a separate validation split** for the secondary λ selection (Eq. 4) to avoid optimism bias, or quantify the bias with a third hold-out set.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>