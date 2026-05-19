- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 5, 3, 3
Now I have enough information to construct the synthesized review. Let me assemble it.

## Summary

The paper proposes a non-parametric autoencoder that models text datasets as being generated from underlying code programs with a dataset-level function library. The method uses in-context learning and code interpretation (Chain of Code) to infer latent symbolic representations without parameter updates. The authors evaluate the induced latent space on Super-NaturalInstructions tasks, measuring autoencoding recovery, correctness/domain-relevance of generated samples, diversity, and utility for downstream training.

## Strengths

- **Principled variational framework for code as a latent representation.** The paper derives a clean variational objective (Eq. 1) that formalizes the problem as non-parametric posterior inference over a shared function library and per-instance code programs. This grounding goes beyond prior autoencoding approaches that use continuous or unstructured latent spaces.

- **Demonstrated correctness advantage on algorithmic tasks (Table 2).** On algorithmic SNI tasks, the code latent space with induced demonstrations achieves substantially higher correctness by human eval (68.5%) compared to the CoT latent baseline (47.3%) and the interpolation baseline without a latent space (12.3%). GPT-4o-mini judgments show the same pattern (84.2% vs. 69.8% vs. 37.3%). This directly supports the central claim that code as a latent representation benefits compositional/algorithmic tasks.

- **Autoencoding recovery improved by variational optimization (Table 1).** Conditioning on the induced demonstration set increases autoencoding recovery (e.g., 26.1% → 38.9% for Llama3.1 8B with 12 exemplars) compared to using only domain-general seed demonstrations, validating that the iterative optimization procedure improves latent representations.

- **Interpretable and modular latent space.** The latent space decomposes into a shared function library and per-instance code programs (Figure 2), enabling direct inspection, conditional sampling by composing library functions, and execution via deterministic and neural interpreters — a clear advantage over black-box representations like CoT or continuous vectors.

- **Human evaluation validates automatic metrics.** The paper includes a human evaluation on a subset of generations (Table 2) to calibrate GPT-4o-mini judgments, adding rigor to the reported correctness and domain-relevance numbers.

- **Systematic evaluation across task categories.** The analysis separates algorithmic and non-algorithmic tasks, providing a nuanced picture of where code as latent representation excels (algorithmic) and where it is comparable to text-based latents (non-algorithmic).

## Weaknesses

### Fatal
None.

### Major

- **Negative downstream training result (Table 3) is acknowledged but not analyzed or explained.** The paper reports that the interpolation (no-latent) baseline produces better synthetic training data than the proposed method for downstream model training, sometimes even outperforming gold data. This is a significant finding that the paper simply states and moves past without any analysis. The discrepancy between Table 2 (where latent methods appear better on quality metrics) and Table 3 (where they underperform on downstream utility) is a critical puzzle that the paper must confront. Possible hypotheses include: the latent method produces less diverse data (hinted in Table 2's diversity column), or its outputs are correct but unrepresentative of the task distribution. The paper's conclusion (Section 9) omits any mention of this limitation, undermining coherence between claims and evidence.

### Minor

- **Key method details are underspecified for reproducibility.** The rejection-sampling procedure (Section 2) lacks several concrete details: (a) how the log-ratio for accepting/rejecting candidate programs is computed; (b) how many iterations the optimization runs; (c) the acceptance threshold for the rejection criterion (ROUGE-L/BLEU thresholds on line 107 appear related to validation but their role in the rejection step is unclear); (d) how convergence is determined. While the overall approach is clear, these missing details would make independent reimplementation difficult.

- **Chain-of-thought latent baseline is insufficiently described.** The paper claims (Section 4, line 94) that the CoT baseline is "as described in Section 4," but Section 4 only describes the code-based implementation. Line 142 provides a brief description ("a non-symbolic latent space composed of z_i as textual descriptions"), but the prior, decoder, and how the autoencoder objective is adapted for textual reasoning chains are not specified. This makes it difficult to assess whether the comparison is fair.

- **No error bars, confidence intervals, or significance tests reported for any table.** Given that values in Table 3 vary widely (e.g., 23.4 vs 54.1 for interpolation on IN tasks), variance reporting is essential to assess the reliability of the comparisons.

- **Ablation on the compile-success prior is absent.** The prior p(z_i|z_ℓ) = 𝟙(compiles(z)) is used as a hard constraint, but its effect is not isolated. How much does the syntactic validity check matter compared to selecting programs via ICL without it?

### Trivial

- **"Non-parametric" usage is potentially confusing.** The method relies on a large parametric LLM; the term is used to indicate "no gradient updates" rather than the statistical sense of a non-parametric model. Clarifying this would avoid misunderstanding.

## Nice-to-Haves

- An upper-bound comparison against directly using a strong LLM (e.g., Llama3.1 70B or GPT-4) as a data generator would strengthen claims.
- A failure analysis discussing when the latent induction procedure fails (e.g., tasks where no good program can be induced) would add depth.

## Removed Points

These points from the inputs were removed with justification:

1. *"The paper's main claim is contradicted by its own key experiment (Table 3)"* — REMOVED. This conflates downstream training performance with the paper's core claim about correctness/domain-relevance of generated text (Table 2). The paper's primary evidence for its central claim is Table 2, not Table 3. Table 3 tests a different hypothesis (utility for downstream training). The lack of explanation is a valid major weakness (moved above), but calling it a contradiction of the core claim overstates the relationship.

2. *"The prior p(z_i|z_ℓ) — described only as 'a compiler that rewards syntactically valid programs' — how is it incorporated?"* — REMOVED. The prior is clearly specified on line 60 as p(z_i|z_ℓ) = 𝟙(compiles(z)). This sub-point is factually incorrect.

3. *"The paper does not report correctness for interpolation in Table 2"* — REMOVED. Table 2 clearly includes interpolation results for correctness. The text (line 144) discusses the pattern.

4. All points about missing appendix, supplementary, or formatting artifacts — REMOVED per rule (these are parser issues, not author errors).

5. *"The framing overpromises relative to the evidence"* (general claim without specific anchor) — REMOVED per filtering discipline. The specific claim this references is addressed elsewhere (the Table 3 analysis).

6. *"The KL derivation appears mathematically sound but the leap from intractable combinatorial search to rejection-sampling heuristic is enormous and unbridged"* — Partially absorbed into the underspecification weakness above. The framing as "enormous and unbridged" is overly dramatic for what is a standard LLM-in-the-loop optimization approach.

7. *Strength Finder's generic strengths* — Strengths like "This paper addressed an important problem" without specific content are dropped. The core strengths listed above are the specific, evidence-grounded ones.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface concerns about the gap between generation quality and downstream utility, but this is a pattern recognized in the synthetic data literature rather than a novel observation specific to this paper.

## Suggestions

1. Add an analysis section explicitly confronting and explaining the negative downstream result from Table 3. Test hypotheses about diversity, task-coverage, or distribution mismatch between latent-generated and gold data.
2. Fill in the missing method details: number of optimization iterations, acceptance thresholds for the rejection sampler, convergence criteria, and the exact computation of the log-ratio used for scoring.
3. Provide a full specification of the CoT latent baseline: what constitutes its prior, encoder, and decoder?
4. Add error bars (e.g., across multiple runs or bootstrap resampling) to all three tables.
5. Add an ablation isolating the effect of the compile-success prior.
6. Revise the conclusion to accurately reflect the mixed results, acknowledging where the method underperforms baselines and why.
