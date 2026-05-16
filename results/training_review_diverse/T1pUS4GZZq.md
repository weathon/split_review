Now I have all the information I need. Let me compile my final review.

---

## Summary

This paper investigates whether modern recurrent architectures (xLSTM, Mamba) can serve as effective backbones for Large Action Models (LAMs) in place of Transformers, motivated by the need for fast inference in robotics. The authors introduce LRAM (Large Recurrent Action Model) with an xLSTM core and evaluate it against a Decision-Transformer baseline across 432 tasks from 6 domains at 4 model scales (16M–206M parameters), finding that the recurrent architectures match or exceed Transformer performance while offering substantial inference speed advantages, especially at long context lengths.

## Strengths

- **Large-scale, systematic empirical evaluation across diverse domains.** The paper evaluates 4 architecture variants at 4 model sizes across 432 tasks spanning image-based and state-based environments, discrete and continuous actions — a thorough evaluation scope that provides broad evidence for the paper's claims.

- **Clear inference speed advantage demonstrated empirically.** The latency and throughput measurements (Section 4.4) show xLSTM maintaining constant latency independent of context length, while the Transformer runs out of memory at ≥6400 timesteps. This advantage is theoretically expected but empirically confirmed, and directly relevant to the stated robotics motivation.

- **Competitive or favorable performance across model scales.** In the scaling comparison (Figure 2), both xLSTM and Mamba match or exceed the Transformer baseline on normalized scores at all four model sizes. Per-domain results (Figure 3) show xLSTM outperforming on 3 of 6 domains and matching on the remaining 3.

- **Careful architectural design choices validated by ablations.** Removing actions from the sequence representation to prevent shortcut learning (shown to help "across backbones," line 327) and using a shared action head with discretized continuous actions are thoughtful design decisions with empirical support.

- **Honest and well-scoped limitations section.** The paper explicitly acknowledges the lack of real-robot experiments, the offline-only fine-tuning setup, and the limited grid-world ICL evaluation, which strengthens credibility.

## Weaknesses

### Fatal
None.

### Major
- **No variance or confidence intervals on any evaluation result.** The scaling curves (Figure 2b) and per-domain results (Figure 3) are presented as single trajectories without error bars, confidence intervals, or statistical significance tests. For an empirical study whose central claim is that one architecture "compares favorably" to another, the absence of any variance measure is a significant gap — the observed differences could be within noise. This is the single most impactful weakness in the paper.

- **Inference speed comparison uses asymmetric optimization levels.** The paper uses custom xLSTM kernels while relying on standard PyTorch FlashAttention with KV-caching for the Transformer. Both backbones use `torch.compile`, but the paper acknowledges the kernel asymmetry (line 360) without fully controlling for it. While the theoretical advantage is real, the exact empirical speedup numbers likely overstate the practical gap — a Transformer implementation with equal engineering investment (e.g., vLLM, TensorRT-LLM) could yield different relative latencies.

- **In-context learning experiment lacks a Transformer baseline.** The Dark-Room ICL experiment (Section 4.3) compares only xLSTM variants and Mamba, omitting the original Transformer-based Algorithm Distillation. The claim that xLSTM [7:1] "attains the highest overall scores" is meaningful only among the architectures tested, and a DT baseline is needed to support the paper's broader narrative about recurrent architectures being advantageous for ICL in LAMs.

### Minor
- **Inference speed measured only on Atari Freeway, not a robotics environment.** Despite the paper's title and motivation emphasizing robotics, the latency/throughput experiments use a 2D Atari game. While the theoretical advantage carries over, testing on a robotics simulation (e.g., DMControl at high control frequencies) would strengthen the motivation–evidence link.

- **Fine-tuning experiment is xLSTM-only.** The fine-tuning comparison (Section 4.3) compares only pretrained xLSTM vs. xLSTM trained from scratch, with no Transformer fine-tuning baseline. This tells us that xLSTM benefits from pretraining, but not whether recurrent backbones are differentially advantageous for fine-tuning.

- **Overclaim in the abstract.** The statement that "LRAM compares favorably to Transformers in terms of performance and speed" oversimplifies the evidence: the performance advantage is modest (3/6 domains, no error bars) and the speed advantage, while real, is measured under asymmetric optimization conditions. The conclusion section's more cautious language ("attractive alternatives") is better calibrated to the evidence.

### Trivial
None.

## Nice-to-Haves
- Include a DT baseline in the ICL (Dark-Room) experiment to enable direct comparison.
- Test inference speed on a robotics simulation (e.g., DMControl) to strengthen the robotics motivation.
- Provide per-task breakdowns for the largest model to show where architecture differences arise.
- Test the removal-of-actions ablation on DT as well to verify the effect is backbone-independent.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Parameter mismatch between xLSTM and DT:** The harsh reviewer claimed the architecture comparison is confounded by parameter mismatch. However, the paper explicitly states that models are compared at matched parameter counts (16M, 48M, 108M, 206M) and the latency comparison uses "the same number of layer blocks and parameters" (line 353). The only mention of parameter mismatch is for Mamba (line 271), which the paper honestly caveats. *Reason: Factually incorrect about the xLSTM vs. DT comparison.*

- **Ablation on removing actions not compared across backbones:** The reviewer claimed this ablation was only done for one backbone. The paper states "We found that removing actions from the context results in better performance **across backbones**" (line 327). *Reason: Factually incorrect.*

- **Normalization scheme undefined:** The reviewer claimed the normalization scheme is unspecified. The paper clearly states "For Meta-World, DMControl, Mimicgen, Composuite, and Procgen we use data-normalized scores, as suggested by [Levine:20]" and "For Atari, we report human-normalized scores." *Reason: The paper adequately specifies the normalization scheme following standard practice.*

- **"Post-hoc" criticism of the removing-actions justification:** The reviewer characterized the shortcut-learning explanation as "post-hoc." This is standard empirical practice — observing an effect and proposing an explanation. *Reason: Unreasonable methodological nitpick.*

- **UMAP analysis is qualitative:** The reviewer criticized the UMAP analysis as "not directly linked to performance." This is true of all UMAP analyses; they are an interpretability tool, not a performance metric. The paper does not overclaim. *Reason: Unreasonable expectation for an interpretability visualization.*

- **Dataset is "a compilation of existing sources":** The reviewer dismissed the dataset contribution. Compiling and standardizing 894M transitions from diverse sources into a unified evaluation benchmark is a standard and valid contribution for an empirical paper. *Reason: Misclassification of the paper's contribution type.*

- **Reproducibility concerns about missing architecture details:** The reviewer claimed architecture details are not given. These details are standard for the appendix, which the parser strips from all papers. *Reason: Parser artifact — appendix exists in original submission.*

## Novel Insights
The paper's key novel insight is that modern recurrent architectures (xLSTM, Mamba) can serve as effective backbones for large action models, achieving competitive performance with Transformers while offering the practical advantage of constant-memory, linear-time inference. The finding that removing actions from the sequence representation improves performance on robotics domains (while not affecting discrete control) is a practically useful architectural insight. The observation that xLSTM's sLSTM blocks may provide state-tracking benefits for in-context RL (due to non-diagonalized recurrent matrices) is conceptually interesting, though the current evidence is preliminary.

## Suggestions
- Add error bars, confidence intervals, or bootstrapped means to all evaluation figures. This is the single most impactful improvement — without it, the central performance comparison is not properly quantified.
- For the inference comparison, either (a) match the optimization level (e.g., implement both in a common framework) or (b) frame the empirical numbers more cautiously, separating the algorithmic complexity advantage from implementation-specific speedups.
- Include a Transformer baseline in the ICL experiment to make the comparison complete.
- Test inference latency on a continuous-control robotics environment (e.g., DMControl) to directly support the robotics motivation in the title.

## Score and Decision

The paper addresses a timely and practically motivated question with a large-scale empirical evaluation across 432 tasks. The inference speed advantage is convincingly demonstrated, and the performance results are promising. However, the lack of any statistical variance reporting is a significant gap for an empirical study making comparative claims, and the asymmetric optimization in the inference comparison weakens the quantitative speedup claims. The contributions are real but the experimental rigor has room for improvement.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>