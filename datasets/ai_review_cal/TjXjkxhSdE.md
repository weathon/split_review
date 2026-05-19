- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6
Now I have all the information needed. Let me compose the consolidated review.

## Summary

This paper proposes SDS (Sparse-Dense-Sparse), a three-step pruning framework for LLMs: (1) initial one-shot pruning (SparseGPT/Wanda), (2) re-dense weight reconstruction with sparse regularization (L1+L2) to create a "pruning-friendly" weight distribution, and (3) a second pruning round with soft-mask weight adjustment. The core insight — supported by Table 1 — is that pruned models' lost knowledge is largely recoverable by reactivating pruned connections using only 128 calibration samples. Experiments on OPT (125M–2.7B) and LLaMA/LLaMA2-7B show consistent perplexity and accuracy improvements over the base pruning methods, especially for smaller models and aggressive sparsity levels.

## Strengths

- **Key empirical finding (Table 1)**: Applying 2:4 SparseGPT pruning to OPT-125M degrades perplexity from 27.66 to 60.43, but simply reactivating pruned connections with 128 C4 samples restores it to 27.94 — nearly matching the dense model. This finding, that pruning-induced loss is recoverable with minimal data, is the motivating insight prior one-shot methods (SparseGPT, Wanda) do not exploit.

- **Consistent improvements across all model×sparsity combinations**: In Table 3 (ppl_all), every single tested configuration shows perplexity improvement over the base method. At 2:4 sparsity, the average gain is ~7.5 points across models; individual gains reach 39.61 (OPT-350M, SDS-Wanda). Improvements hold for both SparseGPT and Wanda baselines and across structured (2:4, 4:8) and unstructured (50%) sparsity.

- **Thorough ablation study (Table 5/abl)**: 11 configurations systematically isolate the contribution of each component — skipping initial pruning, removing weight regularization, varying data type (DD/SD/KD), and using multiple vs. single data sources. The ablation clearly shows that only the full SDS with sparse data (SD) achieves the best perplexity (51.30) and highest average accuracy (49.61%), providing concrete evidence for each design choice.

- **Extension to non-uniform sparsity (Appendix)**: SDS applied on top of OWL (non-uniform sparsity) improves OPT-125M at 70% sparsity from 199.34→161.75 perplexity, showing the framework generalizes beyond uniform sparsity distributions and beyond its base methods.

## Weaknesses

### Fatal

None.

### Major

- **"State-of-the-art" claim is overbroad given the comparison scope.** The paper's experimental comparisons are entirely within-family: only SparseGPT and Wanda (the base pruning methods) serve as baselines. The Related Work cites DS∅T, SPP, and prune-and-tune as methods that "can improve the performance of pruned PLMs within limited complexity," but none are compared against. While these methods operate in a somewhat different setting (fine-tuning with additional data vs. SDS's calibration-only approach), the conclusion's unqualified "state-of-the-art pruning results" (line 363) is not supported by the experiments presented. The paper should either (a) add comparisons to these methods under a controlled setting (e.g., using only the same 128 C4 samples), or (b) explicitly scope claims to "outperforms the base one-shot pruning methods SparseGPT and Wanda."

- **Computational cost of the re-dense step is under-characterized.** SDS requires 200 epochs of layer-wise reconstruction per layer — "more than two hours on eight GPUs" for a 7B model (acknowledged in Limitations). However: (a) no wall-time or GPU-hour breakdown is provided for smaller models that constitute most experiments; (b) the paper compares this cost to "training a language model," but the relevant practical baseline is the one-shot pruning methods (SparseGPT/Wanda run in minutes on a single GPU); (c) no ablation explores whether lighter reconstruction (fewer epochs, smaller learning rate) could achieve comparable gains, leaving the cost-benefit tradeoff unclear.

### Minor

- **The claim that magnitude-based second pruning achieves "results similar to" SparseGPT/Wanda's Hessian-based metrics (line 151) is asserted without direct evidence.** The ablation study shows SDS works well, but does not isolate whether using the original SparseGPT/Wanda salience metric for the second pruning step would yield better results. This claim should either be backed by a dedicated comparison or softened.

- **No CPU speedup measurements for 2:4 or 4:8 structured sparsity.** The paper repeatedly highlights 2:4/4:8 configurations for "real-world computational acceleration on specialized hardware" (line 195), yet the CPU speedup evaluation (Table 6) only tests 50% unstructured pruning. Speedup numbers for the structured patterns that are a primary focus are absent.

- **The "soft sparse mask" mechanism in Eq. (4) is underspecified.** The mask is "dynamically selected by |W^{sparse-2nd}_ℓ| in each iteration," but the number of iterations, the exact selection criterion (e.g., what fraction of weights are selected?), and the stopping condition are not specified in the implementation details.

- **The improvements are concentrated in smaller models.** At 50% sparsity, gains for LLaMA-7B are 0.04 (SparseGPT baseline) and 0.07 (Wanda baseline) perplexity points — orders of magnitude smaller than the 2.62–8.81 point gains on OPT-125M/350M. The paper reports the "1.8 point average improvement" at 50% sparsity, but this average is heavily weighted by the small OPT models. This pattern is honestly presented but should be explicitly discussed as a limitation of the method's applicability.

### Trivial

- **Notation ambiguity in Eq. (3).** The argmin variable is written as W^{sparse}_ℓ, but W^{sparse}_ℓ was introduced two lines earlier as a *fixed* input (the result of initial pruning). The optimization variable should use a distinct symbol (e.g., W_ℓ).

- **The S_DS / S_D_S / SD_S notation in Table 2 is confusing and hard to parse.** A simpler scheme (e.g., Step1/Step2/Step3 or S1/D/S2) would improve readability.

## Nice-to-Haves

- **Zero-shot accuracy with multiple runs or variance estimates.** Perplexity is deterministic given calibration data, but zero-shot accuracy can vary. Reporting multi-run statistics would strengthen the reliability of the accuracy claims. (This is not standard practice in the pruning literature, so it is not a weakness, but it would be a nice addition.)

- **Per-layer analysis of where the re-dense step is most effective.** The paper could examine whether pruning-friendliness improves uniformly across layers or is concentrated in early/late layers, providing deeper insight into the mechanism.

## Removed Points

These points were flagged by reviewers but are removed from the main assessment with justification:

- **Comparison to DS∅T/SPP as experimental baselines**: Retained as a Major weakness regarding the SOTA claim, but the fact that these methods use task-specific fine-tuning (vs. SDS's calibration-only setting) means they are not fully apples-to-apples comparisons. The primary issue is claim-scoping, not a missing experiment.

- **"Re-dense model is not truly dense"**: The paper's Figure 1 shows a three-peaked distribution and the term "re-dense" refers to reactivating pruned connections, not achieving 100% nonzero weights. The distribution analysis in the Appendix supports the qualitative claims. The exact fraction of nonzero weights is not required.

- **Performance gap from dense model should be discussed more**: The paper reports dense baselines in all tables and the comparison against initial pruning (the relevant baseline) is clearly presented.

- **Second pruning degrades relative to re-dense model**: This is expected behavior (pruning a model makes it worse than its unpruned version). The paper correctly compares the final model against the *initial pruning*, which is the right experimental question.

- **Post-hoc explanation for SD-data vs KD-data choice**: The ablation study empirically demonstrates which data type works best. The explanation is reasonable and supported by the data; theoretical depth is not required.

- **Missing error bars for zero-shot accuracy**: Not standard practice in the pruning literature (SparseGPT, Wanda also do not report them); moved to Nice-to-Haves.

## Novel Insights

The most interesting observation is the asymmetric benefit profile of SDS: the method is most impactful precisely where one-shot pruning struggles most — small models and high sparsity levels (2:4, 4:8) — while large models (7B+) see only marginal gains. This suggests that one-shot pruning methods already operate near-optimally for overparameterized models, but leave substantial room for improvement in the weight distribution of smaller, more thoroughly trained models. The ablation study's finding that sparse data (SD) works best within the full SDS framework while KD-aware data (KD) works best for the simpler SD_S variant is a non-obvious result about how data difficulty interacts with the optimization pipeline.

## Suggestions

1. **Scope claims precisely**: Replace "state-of-the-art pruning results" with "outperforms the base one-shot pruning methods SparseGPT and Wanda" unless comparisons to DS∅T/SPP are added.

2. **Add lightweight ablation of the re-dense step**: Show how perplexity improvement varies with the number of reconstruction epochs. If 50 or 100 epochs achieves most of the gain, this would substantially improve the cost-benefit profile.

3. **Report GPU-hours for all model sizes**: Give a concrete cost table so practitioners can evaluate whether the improvement justifies the overhead.

4. **Clarify the soft sparse mask in Eq. (4)**: Specify the number of iterations, selection rate, and whether the mask is updated via gradient descent or by a hard threshold.

5. **Fix notation in Eq. (3)**: Use a distinct symbol for the optimization variable (e.g., W_ℓ) to avoid confusion with the fixed sparse weights.

6. **Simplify Table 2 notation**: Consider "S1 / D / S2" or "Init. Prune / Re-dense / Second Prune."
