Now I have all the evidence. Let me write the final consolidated review.

## Summary

This paper introduces selective pruning, a structured pruning method for LLMs that removes neurons based on their relative importance to a forget dataset versus a retain dataset. The method requires only a small representative sample of data and runs on a single GPU. The paper evaluates this approach across multiple model families (OPT, Galactica, Pythia, RoBERTa, ViT) on tasks including code removal, python removal, bird classification removal, toxicity reduction, and CIFAR-100 class unlearning. A secondary contribution is the finding that feed-forward neurons are substantially more specialized (separable) than attention neurons for most model families.

## Strengths

- **Selective pruning achieves effective capability removal across model families and sizes.** The method consistently produces asymmetric accuracy drops (forget >> retain) with all curves above the x=y line (Figure 1). For OPT-6.7B forgetting code while retaining Pile, an ~80% drop in code accuracy requires only a ~20% drop in Pile accuracy (Section 5.1). This pattern holds across OPT, Galactica, Pythia, RoBERTa, and ViT models.

- **Feed-forward neurons are substantially more specialized than attention neurons.** Table 1 reports that for OPT-1.3B, feed-forward pruning achieves a 59.6 max differential accuracy drop versus 28.4 for attention pruning; for Galactica-1.3B, 52.4 vs 41.7. Figure 4 confirms this across four model families. This finding about the locus of specialization is a genuine empirical contribution.

- **Systematic comparison of importance metrics provides actionable guidance.** The paper evaluates four metrics (freq, abs, rms, std) and identifies I_abs as the most reliably effective across feed-forward and attention layers (Section 5.2). This empirical grounding helps future practitioners select an appropriate metric without exhaustive search.

- **Competitive performance on toxicity removal and CIFAR-100 class unlearning.** On GPT2-Large toxicity removal, selective pruning reduces mean toxicity from 0.08 to 0.02 and toxic comment proportion from 3.5% to 0.3%, comparable to task arithmetic (Table 2). On CIFAR-100, SP achieves 0% forget accuracy with MIA success rate of 3.8%, competitive with retraining (3.2%) and better than several baselines (Table 3).

- **Compute- and data-efficient.** All experiments run on a single NVIDIA RTX 4090 (Section 5), and the method requires only a small dataset representative of the target task — in contrast to Hessian-based pruning methods whose cost scales with O(d_row · d_col³) for LLMs.

## Weaknesses

### Fatal
None.

### Major

- **No baselines on the primary LLM unlearning tasks.** The main evaluation (code vs pile, python vs code) contains no comparison to any existing unlearning method. Random pruning is mentioned as a baseline on line 153 ("As a baseline we also randomly pruned layers") but its results are never shown in any figure or table. Without knowing how selective pruning compares to even a trivial baseline, the reader cannot assess whether the observed asymmetric drops reflect genuine selectivity or merely random degradation. The paper positions itself as a baseline ("we provide our results as a baseline for others," line 331), but absent comparison data, there is no way to calibrate the results. Adding random pruning curves and at least one simple comparison method (e.g., gradient ascent on forget data, or fine-tuning on retain data) would significantly strengthen the paper.

### Minor

- **CIFAR-100 experiments are missing the base architecture.** Table 3 compares selective pruning to several unlearning methods on CIFAR-100 class removal, but the paper never states what model selective pruning is applied to. The ViT models listed in Section 4.1 (ViT-base-patch16-224, ViT-large-patch32-384) are described as fine-tuned on ImageNet-1k, not CIFAR-100. The architecture, training setup, and whether the other methods use the same base model are all unspecified, making the comparison harder to interpret than it should be.

- **No variance or statistical significance reported.** All experiments appear to be single runs. The smooth curves in the figures come from interpolation between pruning steps, not from multiple trials. While single-run LLM evaluation is not uncommon, the absence of any repeatability evidence (error bars, confidence intervals, or even a note about stability across seeds) weakens confidence in the quantitative claims.

- **Dataset sizes for importance computation are not reported.** The paper claims to be "data-efficient" but never states how many examples from each dataset were used to compute importance scores (lines 226–237 describe the datasets but not the subsample sizes used). A range of dataset sizes would help substantiate the data-efficiency claim and guide practitioners.

- **Algorithm 1 has inconsistent variable naming.** In the pseudocode (lines 130–131), $I_{r,n}$ (subscript "r" suggesting "retain") is labeled as computed on $D_f$ (forget data), and $I_{f,n}$ (subscript "f" suggesting "forget") on $D_r$ (retain data). The computation $S_n = I_{f,n} / (I_{r,n} + \epsilon)$ is then ambiguous: depending on whether the reader follows the variable names or the comments, the computed score could be the inverse of the intended scoring function. Since the results demonstrate the method works, this is a presentation bug rather than a substantive error, but it needs correction.

- **MCU comparison is uninformative.** The paper compares its LLM results to MCU results from Nguyen et al. (retain drop 1.5%, forget drop 3%) on a medical data classification task (line 256). This is a fundamentally different setting (classification vs. language modeling, different model architecture) and provides little context for interpreting the LLM results.

- **Base perplexity discrepancy and prompt difference not explained.** For GPT2-Large, the quoted base perplexity is 16.4 but the authors' replication gives 18.0 (Table 2). For LLaMA 2, a different (undisclosed) prompt was used because the base model was less toxic (line 410). These inconsistencies limit cross-paper comparability and should be discussed.

### Trivial

- A stray sentence fragment appears at line 87: "KL-divergence is computationally expensive to calculate.}" inside the definition environment, seemingly an editing remnant.
- SVD is mentioned as "considered" (lines 190–191) but never used in experiments, creating momentary confusion about whether it is part of the method.

## Nice-to-Haves

- Runtime and GPU memory measurements for models up to 6.7B parameters would substantiate the claimed efficiency advantage.
- Additional task pairs with varying conceptual distance (e.g., math vs poetry, English vs French) would deepen the separability analysis.
- A discussion of potential failure cases (what happens when retain and forget datasets are very similar) would be valuable, though the python/code pair partially addresses this.

## Removed Points

These points were flagged by reviewers but removed or downgraded after verification against the paper:

- **"Overclaiming generality"** — The paper's claims of "task-agnostic" and applicability to "other potentially harmful skills" are appropriately scoped; the paper tests on three task pairs plus toxicity and CIFAR-100, and acknowledges limitations. This is a reasonable claim for a method paper, not a weakness.
- **"Max-diff metric conflates importance metric and pruning object"** — The figure's purpose is precisely to compare both dimensions simultaneously. The finding that Pythia attention matches feed-forward (46.6 vs 46.2) is a nuance the paper discusses (lines 391–393), not a flaw.
- **"The comparison to task arithmetic is questionable"** — The authors are transparent about the perplexity difference (labeling it "replicated"), and the comparison framework is standard.
- **"Absence of Appendix/Proofs"** — Parser artifact; appendices exist in the original submission.
- **Formatting/style nitpicks and typo complaints** — Parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the reviews surface no genuinely novel insight that the paper itself does not already articulate. The most interesting observation from cross-referencing the reviews is that the community appears divided on how to evaluate unlearning methods for LLMs — some expect comparisons to established unlearning baselines even on new tasks, while others accept self-contained evidence of asymmetric capability drops. This tension is not resolved here but points to a broader need for standardized LLM unlearning benchmarks.

## Suggestions

1. **Add random pruning curves to Figures 1 and 4**, and at least one simple baseline (e.g., gradient ascent on forget data or fine-tuning on retain data) on the code/pile task. This is the single highest-leverage addition.
2. **Specify the architecture used for CIFAR-100 experiments** in Table 3 and clarify whether the compared methods share the same base model.
3. **Report the number of examples used for importance computation** and ideally show sensitivity to this hyperparameter.
4. **Fix the variable naming in Algorithm 1** so that $I_{f,n}$ consistently refers to Importance on $D_f$ and $I_{r,n}$ to Importance on $D_r$.
5. **Clarify or remove the stray KL-divergence sentence** at line 87 and the dangling SVD discussion at lines 190–191.
6. **Add a brief discussion of the perplexity discrepancy** between quoted and replicated GPT2-Large baselines.

## Score and Decision

The paper introduces a plausible and intuitive method with clear internal evidence of effectiveness (asymmetric accuracy drops supported by multiple model families and tasks). The finding about feed-forward neuron specialization is a genuine empirical contribution. However, the lack of baselines on the primary LLM tasks is a significant gap — without knowing how selective pruning compares to random pruning or a simple alternative, the central claim of "effective unlearning" is incompletely supported. The other issues (CIFAR-100 architecture, variance reporting, dataset sizes) are individually minor but collectively erode thoroughness. The paper is on the right track and its core ideas are sound, but it needs a major revision that adds baselines and fills the reporting gaps before it can be accepted.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>