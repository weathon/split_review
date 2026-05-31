Now I have all the information I need. Let me construct the final review.

## Summary

This paper proposes GOT-D, a data selection method for a two-stage fine-tuning pipeline: first "pre-fine-tune" an LLM on selected unlabeled data (drawn from a candidate set approximating the pre-training distribution), then fine-tune on the target task. The key idea is to select samples using the gradient of the Optimal Transport (OT) distance between the candidate set and the target training data, prioritizing samples whose increased presence would most rapidly reduce the OT distance. This differs from prior "distribution matching" approaches that select samples to match the target distribution directly, ignoring the pre-training distribution. Experiments are conducted on toxicity reduction (GPT-2), domain adaptation (8 domain-specific NLU tasks), and GLUE benchmark.

## Strengths

1. **Well-motivated theoretical framework.** Lemma 1 formalizes the "effective data distribution" insight — that light fine-tuning of a pre-trained model produces a model reflecting a weighted combination of fine-tuning and pre-training data. Theorem 1 builds on this to justify selecting samples via the gradient of OT distance between candidate and target sets, rather than naive distribution matching. This provides a principled alternative to methods like DSIR that ignore the pre-training distribution.

2. **Clear problem framing distinguishing pre-fine-tuning from continued pre-training.** Section 2 explicitly defines the low-data regime constraint (N(D_U) ≪ N(D_P)), contrasting with prior work (Xie et al. 2023, Gururangan et al. 2020) that used orders of magnitude more unlabeled data. This reframes data selection for a realistic budget-constrained setting.

3. **Computational efficiency by design.** The method derives selection gradients from the dual solution of a single OT problem (via the calibration method of Just et al. 2023), avoiding iterative optimization or per-sample gradient backpropagation through the model. This is a genuine algorithmic advantage over methods that require model re-training.

## Weaknesses

### Fatal

None.

### Major

1. **Missing specification of the feature representation used for OT computation on text.** The paper states that L1-norm is used as the cost function (line 117) and references entropy-regularized OT solvers, but never specifies what feature space the OT distance is computed over. For text data, the pairwise cost C(z,z') requires a vector representation of each sample — are these bag-of-words vectors, SBERT embeddings, logits from the LLM, or something else? Without this, the method cannot be reproduced from the paper alone. While the code is open-sourced (line 4), a core algorithmic contribution should specify this in the text. (Note: this is a major gap in description, but the source code mitigates the reproducibility concern.)

2. **Empirical gains on domain adaptation and GLUE are small and within reported variance.** On domain adaptation (150K budget, Table 2), GOT-D averages 83.83±1.13 vs DAPT 83.11±1.54 vs DSIR 82.98±0.28 — overlapping error bars on every baseline. On GLUE with full data (Table 4 Upper), the average is 83.43 vs DSIR 83.25 and TAPT/c 83.18 — a 0.18% margin. On GLUE with 5K data (Table 4 Lower), 78.43 vs DSIR 78.15 and TAPT/c 78.32. None of these margins survive within the reported standard deviations, and no statistical significance tests are provided. The paper's claim of "consistently surpassing" other methods is overstated relative to the strength of evidence on these benchmarks.

3. **No variance reported for the toxicity experiments.** Table 1 reports only point estimates for both GOT-D variants and baselines across all toxicity metrics. Given the stochasticity of nucleus sampling (25 generations per prompt) and model fine-tuning, these results need variance estimates (over seeds or data splits) to assess reliability. The toxicity results are the paper's strongest empirical showing, but the lack of variance undermines confidence.

4. **Candidate set (D_S) not specified for GLUE and toxicity experiments.** For domain adaptation, D_S is implicitly the combined domain data. For GLUE (Section 4.4) and toxicity (Section 4.2), the paper never states what constitutes the candidate pool. For GLUE, is it the "all domains" corpus? The Pile? A subset of Wikipedia? For toxicity, the paper mentions a "pool of unlabeled data" (line 195) but does not describe it. Since the method's core assumption is that D_S ≈ D_P (pre-training distribution), the composition of D_S is critical for evaluating whether this assumption holds in each experiment.

### Minor

1. **Ambiguous notation in Theorem 1.** The expression "$D_U\cdot \partial\text{OT}(D_S, D_R)/\partial D_S$" uses a dot product between a set and a gradient vector that is not formally defined. The surrounding text makes the intended meaning (select samples with the most negative gradient values) clear enough, but the notation should be tightened.

2. **No random baseline in the GLUE table.** DSIR and TAPT/c are compared, but a random selection baseline is absent from Table 4 (though the commented-out code on line 308 suggests it was considered). For a paper making claims about selection quality, omitting a random baseline weakens the comparison.

3. **Scalability claim lacks empirical backing.** The paper states selection completes "within a few minutes for millions of samples on a single GPU" (line 62) but provides no runtime table or wall-clock measurements. This is a claimed advantage over prior work and should be quantified.

4. **The "18% gain for RTE" framing is ambiguous.** The text (line 340) reports "∼ 18% gains for RTE." This appears to be an absolute improvement of about 18 percentage points over the vanilla BERT baseline (59.56 → 77.97), not a relative improvement over competing methods. The phrasing could mislead a casual reader.

### Trivial

None.

## Nice-to-Haves

- An ablation comparing gradient-based selection (largest negative gradient) against selecting from the opposite direction (largest positive gradient) or random selection from the top-k gradient magnitudes would more directly validate the theory.
- A plot showing how performance varies with selection budget (e.g., curves from 10K to 200K) would be more informative than the two discrete data points (50K, 150K).
- A runtime table showing wall-clock selection time for varying candidate set sizes would substantiate the scalability claim.

## Removed Points

*"DAPT was designed for much larger continued pre-training; restricting it to 150K may disadvantage it."* — The paper explicitly addresses this concern by using TAPT/c rather than DAPT for the 50K constrained setting (Section 4.3). For the 150K setting, the assertion that DAPT is disadvantaged is speculative — the original DAPT paper used varying amounts of domain data. The paper's choice is reasonable.

*"The 2.7B model result mentioned in the abstract is not present in the provided sections."* — The results for models up to 2.7B are referenced in the introduction (line 62–63) and may appear in the appendix (which is not included in this extract due to parsing). Per policy, missing appendix content is not a valid criticism.

*"Lemma 1 is stated without proof."* — This is standard practice in ML conference papers where page limits prevent full proofs. The lemma is used to motivate the approach, and its empirical consistency is acknowledged via a citation (Hernandez et al. 2021).

*Generic area-of-concern sweeping from the harsh critic about methodological rigor, fairness of comparison frameworks, and evidence strength* — These were filtered during the merging process as they lacked concrete anchors to specific sentences, equations, or tables in the paper.

*Strength Finder's generic strengths about "addressing an important problem"* — Removed as superficial. Only concrete, paper-specific strengths were retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Specify the exact feature representation and cost function used for OT computation on text samples. If this was in the appendix, bring it to the main paper.
2. Report standard deviations (or confidence intervals) for the toxicity experiments.
3. Add a random selection baseline to the GLUE table and report statistical significance tests (e.g., paired bootstrap or t-test over seeds) for the key head-to-head comparisons.
4. Explicitly state the candidate set composition for every experiment (GLUE and toxicity).
5. Include a small runtime table to substantiate the scalability claim.
6. Reframe the claims in the abstract and conclusion from "consistently surpasses" to more precise language reflecting the mixed strength of the evidence.

## Score and Decision

The paper proposes a well-motivated idea with a clean theoretical framing, and achieves unusually strong results on toxicity reduction. However, it suffers from several significant weaknesses: the OT implementation for text is underspecified (incomplete description of the method), the core empirical claims on domain adaptation and GLUE are supported by margins that fall within reported variance, and key experimental details (candidate set composition for half the experiments, variance for the strongest results) are omitted. The core idea has merit, but the paper in its current form does not provide a reproducible, convincingly validated method. Major revisions are needed.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>