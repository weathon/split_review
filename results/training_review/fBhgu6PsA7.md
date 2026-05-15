Now I have enough information. Let me write the final consolidated review.

## Summary

This paper proposes MoFO (Momentum-Filtered Optimizer), a fine-tuning algorithm that mitigates forgetting in LLMs by selectively updating only the parameters with the largest momentum magnitudes within each parameter block at each iteration. The key idea is that by keeping parameters closer to the pre-trained initialization (via block coordinate descent with momentum-based selection), MoFO reduces forgetting of pre-training knowledge while achieving fine-tuning performance comparable to full-parameter training. The paper provides a convergence analysis for a GD-based simplification, a toy example for intuition, and experimental results on instruction fine-tuning (Llama-2-7B on MetaMathQA, Code-Alpaca) and continual fine-tuning (TinyLlama-1.1B on TRACE benchmark).

## Strengths

- **Well-motivated, simple method with clear intuition**: The connection between parameter movement distance and forgetting is empirically grounded (Adam vs. Lion comparison on Pythia-160m, Figure 1/Table 1), and the BCD-with-momentum-selection idea is natural and easy to implement atop any Adam-based pipeline.

- **Consistent forgetting mitigation across multiple benchmarks**: Tables 2 and 3 show that MoFO reduces average accuracy drops on general capabilities (MMLU, Commonsense, HumanEval, GSM8K) compared to Full FT, HFT, and L1/L2 regularization. On MetaMathQA, MoFO achieves an average improvement of +0.4% over the pre-trained model, while Full FT drops by -5.6%. On Code-Alpaca, MoFO shows the smallest average degradation (-1.1%) among all methods.

- **Replay-free and regularization-free design, orthogonal to existing methods**: MoFO does not require access to pre-training data (unlike replay methods) and does not modify the loss function (unlike regularization methods). The TRACE experiments (Table 4) demonstrate that MoFO can be combined with Replay (+1.5 OP) and GEM (+0.9 OP), showing complementarity with existing continual learning techniques.

- **Informative ablation on update fraction**: Figure 3 systematically maps the trade-off — update fractions below 20% preserve general capabilities while fractions above 40% match Full FT's task accuracy — providing clear practical guidance.

- **Head-to-head selection strategy comparison**: Table 5 directly compares MoFO (momentum-based), Gradient-filtered BCD, and Randomized BCD at the same 10% update fraction, showing that momentum-based selection outperforms both alternatives (45.4 vs. 40.2 vs. 35.0 on GSM8K).

## Weaknesses

### Fatal
None.

### Major

- **Convergence analysis applies to a different algorithm than the one used in practice**. Theorem 1 proves convergence (at rate O(T^{-1/2})) for a GD-based variant using *gradient* magnitude filtering, while the actual MoFO algorithm uses *momentum* magnitude filtering within the Adam optimizer. The paper acknowledges this gap (lines 241-242) but then states the result "provides theoretical support for the strong performance of MoFO in fine-tuning tasks." This overstates what is established: the theory supports a GD variant with gradient filtering, not the actual Adam-with-momentum-filtering method evaluated in experiments. The gap between the analyzed algorithm and the deployed algorithm is substantial enough that the theoretical result cannot be cited as evidence for MoFO's empirical success.

### Minor

- **Baseline regularization hyperparameters are not validated**. The L2 (λ₂=1e-3) and L1 (λ₁=1e-6) regularization hyperparameters are stated as fixed values without any tuning, sensitivity analysis, or validation-set selection. While the paper's core claims about MoFO vs. Full FT and HFT hold regardless, the comparison against regularization methods is weakened: the claim that "modifying the original loss function may impair the model's performance on the fine-tuning task" (line 24) is presented as a general finding but is only demonstrated for one specific (possibly strong) regularization strength. The gap on GSM8K (MoFO 47.7 vs. L2 44.5) could narrow with a better-tuned λ.

- **No experimental comparison with LoRA**. LoRA is discussed in Related Work (line 585: "forgets less but learns less") but never compared experimentally. Since LoRA is the most widely used PEFT method and also mitigates forgetting by freezing most parameters, an empirical comparison — even at comparable parameter-update budgets — would substantially strengthen the paper's claims about MoFO's relative effectiveness. As it stands, the paper's performance relative to the dominant PEFT paradigm is unquantified.

- **No explicit definition of the distance metric**. The paper reports that "the distance from the pre-trained model to the minimum reached by MoFO is approximately 20% of the distance to that reached by the Adam optimizer" (line 168) but never formally defines the distance metric. From context it is clearly Euclidean distance in parameter space, but a direct, reported L2 distance (or cosine similarity) between fine-tuned and pre-trained weights for the main Llama-2-7B experiments would better substantiate the central claim.

### Trivial

- The toy example in Section 4 uses only 2 parameters with a product-of-quadratics loss function, which is far removed from the high-dimensional, overparameterized setting of LLMs. It provides intuition but would benefit from a disclaimer that it is purely illustrative and does not constitute evidence.

- The distance comparison between Adam and Lion (Section 2.1) uses Lion as the contrasting optimizer, but Lion's known tendency to converge to sharper minima may exaggerate the distance gap relative to a more typical baseline. The core observation is still valid but could be strengthened with additional optimizer comparisons.

## Nice-to-Haves

- Reporting confidence intervals or standard deviations from multiple runs (even 2-3 seeds) would help assess whether the small advantages over HFT (e.g., MoFO 44.3 avg vs. HFT 43.8 on MetaMathQA) are statistically reliable. This is not standard practice for LLM fine-tuning at 7B scale, but it would strengthen the paper.

- Wall-clock time per iteration and total training time comparison between MoFO and Full FT, since full gradients must be computed before filtering.

- Quantitative parameter-space distance (L2 norm or cosine similarity) between fine-tuned and pre-trained weights for the Llama-2-7B experiments, not just the Pythia-160m loss landscape plots.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"Lion's known tendency to converge to sharper minima might exaggerate the distance difference"* — Removed because the Adam-vs-Lion comparison is purely motivational; the paper does not base its core claims on this example and the observation is presented as an illustration, not a formal experiment.

- *"The paper does not discuss whether the parts are of different sizes and whether top-α% within each part is fair"* — Removed because the paper explicitly partitions by natural network blocks (weight matrices, biases) to reduce computational complexity (line 128), which is a standard and reasonable design choice. Different block sizes are inherent to network architecture and the per-block top-α% is a natural proportional allocation.

- *"No confidence intervals or multiple runs"* — Moved to Nice-to-Haves. Single-run evaluation is the norm for 7B-scale LLM fine-tuning on standard benchmarks (GSM8K, MMLU, HumanEval). The lack of statistical significance reporting is worth noting but does not constitute a methodological gap given community standards.

- Strength Finder point #5 (toy example providing mechanistic insight) — Dropped because the verified weakness about the toy example being too simplistic conflicts with presenting it as a strength. The toy example is acknowledged in the Minor/Trivial sections above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's transparent acknowledgement of the theory-to-algorithm gap and its claim that the theory provides support, but this is a presentation/overclaiming issue rather than a novel observation about the method itself.

## Suggestions

1. Either strengthen the convergence analysis to cover the actual Adam-with-momentum-filtering algorithm, or explicitly reframe the existing theorem as "analysis of a related algorithm" and tone down the claim that it provides theoretical support for MoFO's performance.

2. Tune the regularization baselines (L1/L2 λ values) using a validation set, or at minimum report a sensitivity sweep to show that MoFO's advantage holds across a range of regularization strengths.

3. Add LoRA as a baseline at a comparable parameter-update budget (e.g., set LoRA rank so that the number of trainable parameters matches the effective update fraction used in MoFO). This single addition would substantially strengthen the experimental comparison.

4. Directly report the L2 distance (or cosine similarity) between pre-trained and fine-tuned parameters for the Llama-2-7B experiments to quantitatively substantiate the central "converges closer" claim.

## Score and Decision

MoFO is a simple, well-motivated, and practically useful method. The core idea — momentum-magnitude-based parameter selection within BCD for forgetting mitigation — is sound, and the experiments show a consistent and practically meaningful improvement over full fine-tuning and regularization baselines. The paper does not claim more than it delivers on the empirical side.

The main weaknesses are the theory-to-algorithm gap (the convergence proof supports a different variant) and the absence of a LoRA comparison. The baseline tuning concern is real but limited to the regularization comparison, which is not the paper's strongest experimental pillar (the comparisons with Full FT and HFT are unaffected). These issues are addressable in revision.

The paper makes a genuine contribution: a simple, scalable optimizer-level intervention that reduces forgetting without requiring pre-training data or modifying the loss function. The empirical evidence, while not exhaustive, is consistent and covers a reasonable range of settings (2 model sizes, 2 instruction-tuning datasets, 8-task continual learning benchmark).

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>