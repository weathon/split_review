## Summary

This paper identifies "dimensional collapse" in domain-similarity-based file selection for LLM pre-training—where methods like DSIR and QuRating produce features concentrated in a low-dimensional subspace, boosting domain-related tasks but harming general performance. To address this, the authors propose DiSF (Diversified File Selection), which greedily selects text files to minimize the Frobenius norm of the feature covariance matrix, encouraging more uniform eigenvalues and thus greater diversity. The method is evaluated on TinyLlama (120M–1.1B parameters) across nine Harness tasks, showing that selecting just 1.5% of SlimPajama files (~9B tokens) outperforms full-data pre-training at a 50B token budget.

## Strengths

- **Concrete diagnosis of dimensional collapse in domain-targeted selection.** The paper provides more than aggregate performance numbers: t-SNE visualizations (Figure 2a–c) show that DSIR and QuRating-W selected features form a "long narrow band," and the eigenvalue dominance score (Figure 3) quantifies the collapse. The trade-off is documented at the task level (Table 2, blue-highlighted cells show domain methods improving ARC-c/OBQA but degrading PIQA/HellaSwag). This goes beyond prior work that only reported aggregate scores.

- **DiSF outperforms full-data pre-training with dramatically less data across multiple scales.** With 1.5% of SlimPajama files (~9B tokens), DiSF surpasses full-data pre-training at 50B budget across all three model sizes (120M, 560M, 1.1B) on average commonsense reasoning (Table 2, Figures 5–6). The advantage is consistent across model architectures (TinyLlama, Pythia, OPT—Table 4) and grows with model scale (improvement over DSIR rising from 2.8% at 120M to 3.4% at 1.1B). This finding is the paper's strongest empirical contribution.

- **Comprehensive ablations demonstrating robustness.** The paper ablates selection budgets (1%–100%, Figure 8), model architectures (Table 4), feature extractors (Contriever, CLIP, GPT-2—Table 5), and selection scales (batch sizes, Figure 7). DiSF consistently outperforms baselines across all settings, showing the method does not rely on a narrow configuration. The batch-size ablation (Figure 7) is particularly informative as it addresses a practical concern about computational cost.

## Weaknesses

### Major

- **The batched greedy algorithm breaks the link to the theoretical guarantee.** Section 3.2 frames the selection as γ-weakly submodular optimization and discusses a $(1-e^{-\gamma})$ approximation guarantee for the classical greedy algorithm on the full set. However, the actual implementation (Algorithm 1, Section 3.1) divides the corpus into independent batches of size b=1024, runs greedy selection within each batch separately, and concatenates results. The paper acknowledges this as a computational optimization ("perform the selection at the batch scale") but never addresses whether the batched variant retains any approximation guarantee. Since the guarantee from γ-weakly submodular maximization applies only to the full-set greedy algorithm, the theoretical contribution advertised in the introduction (item 2) does not actually cover what is implemented. This is a disconnect between claimed contribution and delivered content. The empirical ablation on batch size (Figure 7) helps somewhat, but a theoretical claim backed only by an empirical proxy is not a delivered theoretical contribution.

- **The causal mechanism linking eigenvalue uniformity to downstream performance is not established.** The paper's central narrative is that domain-similarity methods cause "dimensional collapse" (non-uniform eigenvalues in the feature covariance matrix), and that preventing this collapse via Frobenius norm minimization drives the performance gains. However, the evidence is entirely correlational: DiSF produces flatter eigenvalues and better average accuracy, but no experiment demonstrates that eigenvalue uniformity (rather than a correlated property) is the mechanism. The observed pattern—DSIR/QuRating-W improve reading comprehension (ARC-c, OBQA) while degrading physical-world tasks (PIQA, HellaSwag)—is equally consistent with a simpler explanation: the selected data is skewed toward Wikipedia/Books-style text and away from the physical-knowledge content PIQA requires. The paper's eigenvalue analysis does not disentangle geometric diversity from topical diversity. A causal demonstration (e.g., interpolating between collapsed and uniform feature sets while controlling for content distribution) is needed to substantiate the mechanism claim.

### Minor

- **No variance or confidence-interval reporting.** All results (Tables 2–5, Figures 5–8) are reported as point estimates with no standard errors, confidence intervals, or discussion of training seed variability. Given the known variance in LLM pre-training outcomes, this makes it difficult to assess whether DiSF's improvements are statistically reliable. Single-seed runs are common in LLM pre-training work due to computational constraints, so this is not a fatal omission, but it should be acknowledged as a limitation.

- **Incomparable sampling strategies in eigenvalue analysis.** Section 2.3 and Figure 3 compare eigenvalue dominance scores using the top-500 samples ranked by each method's criterion for DSIR and QuRating-W, but 500 random samples from D4's pruned set. Different sampling strategies (most prototypical vs. random) could influence the eigenvalue distributions independently of the methods' overall diversity properties. The paper should either use comparable sampling or acknowledge this confound.

- **The 1.5% selection budget is chosen post-hoc.** The paper states (line 220) that 1.5% was selected because "it achieves comparable performance compared to Full Data pre-training." This is a post-hoc choice that optimizes the central comparison around the result. The full ablation (Figure 8) is transparent about the trade-off and mitigates this concern, but the main results table (Table 2) features a budget determined by its outcome.

### Trivial

None.

## Nice-to-Haves

- An experiment that explicitly controls the eigenvalue spectrum (e.g., by interpolating between DSIR's selected set and DiSF's selected set) and shows that the eigenvalue dominance score predicts downstream performance monotonically would turn the correlational evidence into a causal demonstration.
- An ablation isolating why DiSF outperforms D4 (is it the Frobenius norm objective, the greedy procedure, or something else?) would clarify the specific contribution.
- A discussion of why performance declines after 3% selection ratio (Figure 8) would deepen understanding of the method's behavior.

## Removed Points

These points were flagged during review but are removed per the filtering rules. Treat them with caution.

- **Theoretical analysis is a "promissory note" with missing assumptions.** The critic noted that Assumptions 1 and 2 are not stated in the paper body and that the bound expression appears garbled. The assumptions were in the appendix (stripped by the PDF parser), and the garbled text is a parser artifact of the LaTeX expression $e^{-2\mu}\frac{e^{2\mu-\epsilon}-1}{e^{2\mu}-1}$, which is correctly rendered in the paper. Per instructions, weaknesses about missing appendix content and formatting artifacts are removed.

- **Efficiency claims compared against a "straw" baseline.** The critic argued that "Full Data pre-training" is not a meaningful comparison. However, this baseline—training on all SlimPajama files shuffled randomly until 50B tokens—is standard and appears alongside explicit Random baselines in Figure 8. The comparison is valid and contextualized.

- **Inconsistency between 2.1% and 2.8% improvement figures.** These refer to different comparisons (training budget increase vs. model scale increase) and are not contradictory. The critic misread the axes.

- **Typos ("flies" for "files").** These are likely PDF parsing artifacts; per instructions, formatting/typographical criticisms are removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the predictable tension between a method that works well empirically and the theoretical framing that only partially covers what is implemented.

## Suggestions

1. **Align the theoretical claims with what is actually implemented.** Either prove that the batched greedy variant retains a (possibly weaker) guarantee, or reframe the γ-weakly submodular analysis as a heuristic motivation and remove the approximation-guarantee claim for the practical algorithm. The current framing overpromises.

2. **Add a limitation paragraph** acknowledging that the causal link between eigenvalue uniformity and downstream performance is correlational and that the observed patterns are also consistent with content-distribution shifts.

3. **Report at least 2–3 seeds** for the main experiments (Table 2), or provide a clear justification for why single-seed runs are sufficient (e.g., citing prior work on the variance of TinyLlama pre-training).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>