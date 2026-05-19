- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 6, 5, 6, 5
Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper introduces DataMan, a data management tool for pre-training LLMs. The key contribution is a methodology for deriving 13 quality criteria (plus an Overall Score) by prompting GPT-4-turbo to analyze perplexity anomalies (top 2% / bottom 2%) in text — a "reverse thinking" approach. These criteria are used for pointwise quality rating of pre-training documents. The authors fine-tune a Qwen2-1.5B model on 356K GPT-4-annotated documents to create DataMan (80% average accuracy against GPT-4 labels), then use it to annotate the SlimPajama corpus and select a 30B-token subset for training 1.3B LLMs. Results show ICL improvements of 0.4%–4.3% over the best prior baseline (Qurating's Educational value) and instruction-following win rates up to 78.5%.

## Strengths

- **Novel data-driven derivation of quality criteria via reverse thinking from PPL anomalies.** Instead of relying on human intuition (as in prior work like Qurating), the paper prompts GPT-4-turbo to analyze the top 2% and bottom 2% of perplexity texts and iteratively derives 13 quality criteria plus an Overall Score (Section 3.2). This is a systematic departure from heuristic-based approaches and is grounded in the LLM's own learning dynamics.

- **Theoretical and practical justification for pointwise rating with O(N) complexity.** The paper derives a bound connecting pointwise rating loss to NDCG (Equations 2–4, Section 3.4) and computes the computational cost as O(N) vs. O(N²) for pairwise methods. This makes the pointwise choice principled and scalable for corpus-level data selection.

- **Consistent empirical gains across multiple evaluation axes.** Models trained on DataMan-sampled data outperform the strongest prior baseline (Educational value τ=2.0) by 0.4%–4.3% in ICL and achieve instruction-following win rates of 78.5% vs. 34.2%–57% for baselines (Figure 2). The "Overall Score l=5" model surpasses uniform sampling with 50% more data, directly validating the effectiveness of DataMan's quality ranking.

- **Domain-specific continued pre-training validates mixing capability.** Using DataMan's domain identification to select high-rated data in medical, law, and finance domains for continued pre-training yields significant ICL improvements in the corresponding target domains (Table 2), demonstrating generalizability beyond a single training setting.

- **Lightweight and practical annotation model.** The DataMan model (fine-tuned Qwen2-1.5B) achieves ~80% average test accuracy across all quality criteria (81.6% for Overall Score, 86% for domain recognition), demonstrating that a small model can faithfully replicate GPT-4-turbo's quality judgments at scale.

## Weaknesses

### Fatal
None.

### Major

- **No variance or statistical significance reported for any experimental result; claims of "significantly surpasses" are unsupported.** All downstream LLM training runs appear to be single-seed, single-run. No confidence intervals, standard deviations, or statistical tests are reported anywhere. The paper uses language like "significantly surpasses models trained on uniform sampling with 50% more data" (abstract, line 14; Section 5.3, line 175–177) without any evidence that the observed differences are beyond what random seed variation could produce. For 1.3B-parameter models trained on 30B tokens, seed effects on data shuffling and initialization could plausibly produce variation of similar magnitude to the reported 0.4%–4.3% gains. This weakens the evidential basis for the paper's strongest claims.

- **The 95% human agreement claim is not supported by the presented evidence.** The validation (Section 3.3, line 76) uses "two groups of ten documents" (20 documents per criterion) with "a clear quality gap" between groups — i.e., only unambiguous, clear-cut cases. Selecting only easy cases artificially inflates agreement rates. The real agreement on the actual data distribution (where most ratings are 3–5 and differences are subtle) is not measured. Moreover, the paper's headline metric for DataMan itself is ~80% accuracy against GPT-4-turbo labels (not human labels). The gap between 95% (human–GPT-4 on 20 easy cases per criterion) and 80% (DataMan–GPT-4 on the full test set) underscores that the 95% figure is not representative of actual deployment performance. Yet it is used prominently in the abstract (line 10), introduction (line 32), and conclusion (line 219) as a headline claim.

### Minor

- **The Qurating criteria mix baseline is mentioned but not properly benchmarked or explained.** The paper states that a "criteria mix" of Qurating's four criteria "did not perform well" (Section 5.3, line 169–170), and speculates this is "possibly due to a lack of complementarity among the Qurating's criteria." However, the actual numbers for this baseline are not reported in the main table (Table 1 is garbled in extraction; no textual reference to its quantitative performance is given), and no analysis is provided to explain why mixing all four criteria underperforms the single best one. Since Wettig et al. (2024) found that a mixture can outperform individual criteria in some settings, this omission weakens the claim of surpassing SOTA, as the comparison may be against a cherry-picked variant of the prior method.

- **No ablation of the 13 individual quality criteria.** The paper derives 13 criteria plus an Overall Score, but provides no experiment showing that each criterion contributes to downstream performance (e.g., removing one criterion at a time or using random subsets). Without this, it is unclear whether the criteria set as a whole is driving the gains or whether a much smaller set would suffice. While full ablation would be expensive, the paper could provide partial evidence (e.g., showing which criteria correlate most with downstream gains).

- **The pointwise vs. pairwise argument relies on a single case study of 7 documents.** Section 3.4 (line 83) uses a case study with the top-7 documents from Wettig et al. (2024) to argue that pointwise ratings are sufficient. A more systematic comparison — e.g., showing that pointwise and pairwise rankings correlate highly on a larger random sample — would strengthen what is otherwise a thin empirical justification for a key methodological choice.

### Trivial
None.

## Nice-to-Haves

- The sampling formula in Section 4 (line 113–117) could be clearer about how multiple criteria are jointly used for top-k selection when running the multi-criteria stratified sampling (vs. the Overall Score variant which uses uniform sampling by fixed rating).
- Including a simple perplexity-based baseline with a moderate threshold (rather than only lowest/highest extremes) would address potential concerns about baseline selection.

## Removed Points

These points are flagged for removal; treat them with caution:

- **"No comparison against D4, DoReMi, or other recent data selection methods"** (Harsh Critic) — Removed: scope creep. The paper already compares against the most relevant prior work (Qurating, DSIR, Perplexity Filtering). Asking for additional orthogonal methods is beyond the paper's stated scope.
- **"Perplexity filtering baseline seems designed to make filtering look bad"** (Harsh Critic) — Removed: speculative attribution of intent. Lowest/highest PPL filtering is a standard baseline used in prior work.
- **"DSIR with Wikipedia/Book is a weak version of that method"** (Harsh Critic) — Removed: subjective opinion; DSIR with Wikipedia/Book is a standard published baseline from the DSIR paper.
- **"The NDCG bound (Eq. 2–4) is a known result and does not add novel insight" / "The O(N) vs O(N²) argument is correct but obvious"** (Harsh Critic) — Removed: subjective dismissals of the theoretical contribution. Making the connection explicit and applying it to this setting is a valid contribution.
- **"The data selection algorithm is underspecified"** (Harsh Critic) — Partially addressed by the paper (Section 4 provides the formula and explains both the multi-criteria stratified and Overall Score variants). The remaining ambiguity is a nice-to-have clarification, not a weakness.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — Removed as insufficiently specific.

## Novel Insights

None beyond the paper's own contributions. The reviews surface several valid concerns about experimental rigor but do not identify any novel scientific insight about the method itself that the paper's authors missed.

## Suggestions

1. **Report multi-run results for a subset of configurations.** Running 3 seeds for at least the key comparisons (Overall Score l=5 vs. Uniform, Educational value τ=2.0) would dramatically strengthen the paper's central claims. Report means and standard deviations.

2. **Scale back the "95% agreement" claim or provide a proper human validation study.** Either (a) replace the headline 95% figure with the actual measured agreement on the 20-document-per-criterion sample, clearly noting the selection bias toward clear-cut cases, or (b) run a human validation on a larger, more representative sample (e.g., 100+ documents randomly sampled from the actual distribution).

3. **Report the Qurating criteria mix numbers in the main table and provide an analysis of why it underperforms.** If the mix truly underperforms educational value alone in this setting, explain why (e.g., different training budget, different base corpus, different mixing ratio). This is critical for the SOTA claim.

4. **Tone down causal language.** Phrases like "significantly surpasses" should be replaced with "outperforms in this experimental setup" unless statistical significance testing is provided.
