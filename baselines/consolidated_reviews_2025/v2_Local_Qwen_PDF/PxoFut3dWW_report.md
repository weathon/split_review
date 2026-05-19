## Summary
# Final Review Report

## Summary

This paper introduces Wanda (Pruning by Weights and activations), a simple yet effective post-training pruning method for Large Language Models (LLMs). Motivated by the observation of emergent large-magnitude features in LLMs, Wanda proposes a novel pruning metric that combines weight magnitudes with input activation norms ($S_{ij} = |W_{ij}| \cdot \|X_j\|_2$). Additionally, it introduces a per-output comparison group for weight selection, which is shown to be crucial for effective LLM pruning. Unlike prior methods such as SparseGPT, Wanda requires no weight updates or retraining, operates in a single forward pass, and achieves competitive performance on LLaMA and LLaMA-2 models across zero-shot tasks and language modeling benchmarks. The method is significantly faster and more robust to calibration data size than second-order approaches.

## Strengths
1. **Simple and Intuitive Methodology:** Wanda proposes a highly intuitive pruning metric that incorporates input activation norms alongside weight magnitudes. The motivating example clearly illustrates why magnitude pruning fails in the presence of emergent large-magnitude features, making the method easy to understand and implement.
2. **High Computational Efficiency:** By avoiding second-order Hessian computations and weight updates, Wanda achieves a significant speedup in pruning time compared to SparseGPT (e.g., 300x faster on LLaMA-65B). This makes it highly practical for rapid experimentation and deployment.
3. **Strong Empirical Performance:** Wanda demonstrates competitive performance against the state-of-the-art SparseGPT on unstructured 50% sparsity across multiple LLaMA and LLaMA-2 model sizes, without requiring any weight updates or retraining.
4. **Robustness to Calibration Data:** The method shows remarkable stability even with very few calibration samples (e.g., as low as 1 sample), which is a significant practical advantage over methods that rely on precise Hessian estimation.
5. **Comprehensive Ablation Studies:** The paper provides thorough ablation experiments on pruning configurations (comparison groups) and calibration sample sizes, offering valuable insights into the design choices and their impact on performance.

## Weaknesses
1. **Limited Theoretical Justification for Per-Output Grouping:** While the per-output comparison group is empirically shown to be superior for LLMs, the paper lacks a deep theoretical explanation for why this grouping works better than layer-wise or global comparisons. The observation that it does not hold for image classifiers is noted but not explained, leaving a gap in understanding the underlying mechanism.
2. **Minor Performance Gap on Structured Sparsity for Small Models:** Wanda occasionally underperforms SparseGPT on structured sparsity (e.g., 2:4) for smaller models (7B). While the gap is marginal, it suggests that weight updates may still offer benefits in highly constrained settings, which is not fully discussed.
3. **Reproducibility Details for Fine-Tuning:** The fine-tuning experiments report time budgets ("12 hours", "3 days") but do not specify the number of training steps or epochs. Wall-clock time is hardware-dependent and less reproducible; reporting steps would improve clarity.
4. **Calibration Context Length Not Explicitly Stated:** The experimental setup mentions using 128 calibration sequences but does not explicitly state the context length (sequence length) used. This detail is important for reproducibility as it affects activation norm estimation.
5. **Typographical Errors:** There are minor typos in the manuscript, such as "Large Languages Models" in the abstract and "corrsponding" in the Figure 1 caption, which should be corrected for professionalism.

## Key Issues
1. **Theoretical Grounding of Activation Norm Proxy:** The method relies on the assumption that the $\ell_2$ norm of activations across calibration tokens serves as a stable proxy for expected activation magnitudes during inference. While empirically valid, explicitly stating and justifying this assumption would strengthen the theoretical foundation of the metric.
2. **Lack of Explanation for Modality-Specific Grouping Behavior:** The finding that per-output grouping is superior for LLMs but not for image classifiers is intriguing. Without a hypothesis explaining this discrepancy (e.g., differences in activation sparsity or outlier feature prevalence), the generalizability of the per-output strategy remains unclear.
3. **Trade-off Acknowledgment for Structured Sparsity:** The paper emphasizes Wanda's competitiveness but could more explicitly acknowledge the marginal performance gap on structured sparsity for smaller models. Discussing this trade-off would provide a more balanced view of when weight updates might still be justified.

## Actionable Suggestions
1. **Clarify Theoretical Assumptions:** Add a brief statement in the Method section explaining that the $\ell_2$ norm of activations is assumed to be a stable proxy for expected inference-time magnitudes due to statistical consistency across similar corpora.
2. **Hypothesize Modality Differences:** In the Comparison Group paragraph, include a hypothesis for why per-output grouping benefits LLMs but not vision models (e.g., LLMs have more pronounced emergent large-magnitude features and sparser activation distributions).
3. **Report Training Steps for Fine-Tuning:** Replace or supplement wall-clock time budgets ("12 hours", "3 days") with the number of training steps or epochs to improve reproducibility.
4. **Specify Calibration Context Length:** Explicitly state the context length (e.g., 2048 tokens) used for the 128 calibration sequences in the Experimental Setup section.
5. **Acknowledge Structured Sparsity Trade-offs:** Add a sentence in the Language Modeling discussion acknowledging that SparseGPT occasionally edges out Wanda on structured sparsity for smaller models, highlighting where weight updates may still offer marginal gains.
6. **Correct Typos:** Fix "Large Languages Models" to "Large Language Models" in the abstract and "corrsponding" to "corresponding" in the Figure 1 caption.

## Storyline Options + Writing Outlines
### Abstract Outline
- **S1 (Problem & Domain):** Large Language Models (LLMs) are natural candidates for network pruning, yet existing methods require costly retraining or computationally intensive second-order weight reconstruction.
- **S2 (Prior Gap):** Magnitude pruning, a standard baseline, fails dramatically on LLMs due to emergent large-magnitude features that distort weight importance rankings.
- **S3 (Proposed Method):** We introduce Wanda (Pruning by Weights and activations), a straightforward approach that prunes weights based on the product of their magnitudes and corresponding input activation norms, evaluated on a per-output basis.
- **S4 (Key Result):** Evaluated on LLaMA and LLaMA-2, Wanda significantly outperforms magnitude pruning and competes favorably with SparseGPT without requiring any weight updates or retraining.
- **S5 (Implication):** Wanda offers a highly efficient, single-forward-pass solution for inducing sparsity in pretrained LLMs, enabling rapid deployment and experimentation.

### Introduction Outline
- **P1 (Big Picture & Cost):** LLMs have reshaped NLP but demand significant computational resources. While quantization has advanced rapidly, network pruning remains underexplored for LLMs.
- **P2 (The Pruning Gap):** Traditional pruning methods require retraining or iterative processes, which are prohibitive for billion-scale models. Even recent one-shot methods like SparseGPT demand heavy second-order computations.
- **P3 (Why Magnitude Pruning Fails):** Magnitude pruning fails on LLMs because it ignores input activations. Emergent large-magnitude features mean small weights can still have large impacts if connected to high-activation inputs.
- **P4 (Wanda's Solution):** Wanda addresses this by incorporating activation norms into the pruning metric and comparing weights on a per-output basis. This simple adjustment preserves critical connections while maintaining computational efficiency.
- **P5 (Evidence & Contributions):** We demonstrate that Wanda matches or exceeds SparseGPT on standard benchmarks without weight updates, runs 300x faster, and is robust to calibration data size. Our contributions include the novel metric, the per-output grouping insight, and comprehensive empirical validation.

## Priority Revision Plan
| Priority | Action | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Clarify theoretical assumption: $\ell_2$ norm as stable proxy for activation magnitudes. | Strengthens methodological grounding and justifies metric generalization. | Low |
| **P0** | Hypothesize modality-specific grouping behavior (LLMs vs. vision models). | Provides deeper insight into why per-output grouping works, improving narrative depth. | Low |
| **P1** | Report training steps/epochs for fine-tuning experiments. | Improves reproducibility and allows fair comparison across hardware setups. | Low |
| **P1** | Specify calibration context length in experimental setup. | Ensures exact reproducibility of activation norm estimation. | Low |
| **P2** | Acknowledge structured sparsity trade-offs for small models. | Enhances objectivity and balanced discussion of limitations. | Low |
| **P2** | Correct typos ("Languages", "corrsponding"). | Improves professionalism and readability. | Low |

**Revision Strategy Roadmap:**
```text
[Problem: Theoretical grounding & reproducibility gaps]
    -> [Action: Add assumption clarification & training steps]
    -> [Expected impact: Stronger validity & reproducibility]
[Problem: Narrative depth on modality differences]
    -> [Action: Add hypothesis for per-output grouping behavior]
    -> [Expected impact: Deeper insight & reader engagement]
[Problem: Minor typos & trade-off acknowledgment]
    -> [Action: Text corrections & balanced discussion]
    -> [Expected impact: Professionalism & objectivity]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Wanda outperforms magnitude pruning & competes with SparseGPT | LLaMA/LLaMA-2, 50% unstructured/structured | Zero-shot acc, WikiText PPL | Wanda matches/exceeds SparseGPT without weight updates | C1, C3 | Minor gap on 2:4 for 7B models |
| E2 | Pruning speed comparison | LLaMA 7B-65B, NVIDIA A6000 | Pruning time (seconds) | Wanda is ~300x faster than SparseGPT | C3 | None |
| E3 | Inference speedup for structured sparsity | LLaMA-65B, CUTLASS GEMM | Latency (ms) | ~1.6x speedup for linear layers | C3 | Simulation-based, not end-to-end |
| E4 | Fine-tuning recovery potential | LLaMA-7B, LoRA & Full FT | Zero-shot acc, PPL | FT mitigates most performance drop | C1 | Wall-clock time reported, not steps |
| E5 | Ablation on pruning configuration | LLaMA-7B, various groups/metrics | PPL | Per-output (output, 1) is optimal | C2 | Image classifier trend not explained |
| E6 | Robustness to calibration samples | LLaMA-7B, 1-256 samples | PPL | Wanda stable even with 1 sample | C3 | None |

### Research-Theme Gap Diagnosis
The core research value (efficient, effective pruning without weight updates) is well-supported. However, the theoretical justification for the per-output grouping and the activation norm proxy assumption lacks explicit articulation. Additionally, the modality-specific behavior of the comparison group remains unexplained.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| C2 (Per-output grouping) | LLMs have sparser/more outlier activations than vision models | Compare activation distributions (sparsity, outlier ratio) across LLaMA-7B and ConvNeXt-B | Same pruning metric | Activation stats | LLMs show higher outlier prevalence | Low | Theoretical insight |
| C1 (Metric robustness) | $\ell_2$ norm converges faster than Hessian inverse | Track metric stability vs. sample size for Wanda vs. SparseGPT | Same calibration sets | Metric variance | Wanda variance drops faster | Low | Justifies low-data robustness |

**Traceability:** E1/E2 support C1/C3; E5 supports C2; Proposed experiments address theoretical gaps in C1/C2.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 7.5/10

**Rationale:** The paper presents a simple, highly efficient, and empirically strong pruning method for LLMs. Wanda's ability to match or exceed SparseGPT without weight updates and with significantly lower computational cost is a major practical contribution. The method is intuitive, well-motivated by emergent large-magnitude features, and supported by comprehensive ablation studies. The score is slightly tempered by the lack of deep theoretical justification for the per-output grouping strategy and minor reproducibility details (e.g., training steps, context length). However, these are fixable and do not undermine the core validity or value of the work.

**Post-Revision Target:** [8.0, 9.0]/10

**Justification:** Addressing the theoretical grounding of the activation norm proxy, hypothesizing the modality-specific grouping behavior, and clarifying reproducibility details will significantly strengthen the paper's narrative depth and scientific rigor. These revisions are low-effort but high-impact, likely elevating the paper to a strong acceptance candidate.