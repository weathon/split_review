Now I have all the information I need. Let me write the final review.

---

## Summary

This paper proposes UniMoD, a task-aware token pruning method for unified multimodal transformers that handle both generation and understanding tasks. Through empirical analysis of attention patterns, layer importance, and token redundancy (ARank), the authors show that token redundancy varies significantly across tasks and layers. Building on these findings, UniMoD introduces separate routers for generation and understanding tasks, with ARank-based layer selection to determine which layers to convert to Mixture-of-Depths (MoD) blocks. Applied to Show-o and Emu3, UniMoD reduces training FLOPs by 15% and 40% respectively while maintaining or improving performance on multimodal understanding and generation benchmarks.

## Strengths

- **Thorough empirical analysis motivating the design**: The paper provides a multi-faceted analysis of unified transformers (Section 3), examining attention weight distributions across four models (Fig. 2), layer importance via inference-time layer skipping (Table 1), token redundancy via ARank across layers and tasks (Fig. 3), and task interactions via competitive token pruning (Fig. 4, Observation 5). This analysis yields five concrete observations that directly motivate the task-aware design, making the method feel principled rather than ad-hoc.

- **Task-aware routing is a genuine innovation for unified transformers**: The core idea — using separate routers for generation and understanding tasks because different modeling approaches (diffusion vs. autoregressive) create different redundancy patterns — is well-justified and effective. The ablation study (Table 5) cleanly demonstrates that both the task-aware router and the layer switch module are essential: removing either causes significant degradation, particularly in generation (GenEval drops from 0.61 to 0.50 without task-aware routing, and to 0.15 in Basic MoD).

- **Demonstrated across architecturally distinct models**: The method works on Show-o (discrete diffusion for generation + autoregressive for understanding) and Emu3 (fully autoregressive for both), covering the two main paradigms of unified transformers. For Emu3, the FLOPs reduction reaches 40% with maintained or improved benchmark scores (Table 3), and the method also extends to pure diffusion models like DiT and PixArt (Appendix A.5).

- **Clear performance-efficiency trade-off**: UniMoD matches or exceeds the full-computation baseline on most benchmarks while using fewer FLOPs. On Show-o, it achieves 1093.7 MME (+37.7 vs. baseline), 73.6 DSG (+1.4), and 0.61 GenEval (-0.01) at 15% FLOPs reduction. The baselines (Early-Exit, Interleaved Layer) at comparable FLOPs show catastrophic degradation on generation (GenEval 0.29 and 0.26 vs. 0.62 baseline), underscoring that UniMoD's design is non-trivial.

## Weaknesses

### Fatal

None.

### Major

- **FLOPs reduction does not translate proportionally to wall-clock speedup for Show-o (Table 4)**: For Show-o, a 10–20% TFLOPs reduction yields only a 2–4% decrease in iteration time (1.30→1.27 s/iter for T2I, 1.30→1.25 for MMU). The paper points to Appendix A.2 for discussion of this gap but the main text does not address it. Router overhead, gather/scatter operations from sparse token selection, and suboptimal kernel implementations likely consume much of the theoretical savings. While Emu3 shows a more meaningful 21% speedup (3.56→2.80 s/iter), the paper's efficiency narrative would be stronger with profiling data and a candid discussion of when real speedups materialize. The claim of practical training efficiency is partially supported but not fully substantiated for the smaller model.

### Minor

- **Training scope is ambiguous**: Section 5.1 states "The model is finetuned on 8 H100 GPUs" (referring to Emu3), and the datasets used (Cambrian for MMU, LLaVA-v1.5-mix-665K) are typical for supervised fine-tuning or continued training. The paper's motivation emphasizes the cost of training unified transformers broadly, yet the experiments demonstrate the method in what appears to be a fine-tuning or continued-training regime rather than pre-training from scratch. The method itself is general and could apply to any training stage, but the paper should explicitly clarify the training scope and ideally demonstrate savings during a pre-training or continued pre-training stage to align evidence with motivation.

- **Static ARank-based layer selection**: Layer selection and pruning ratios are determined from ARank measured on 50 samples at a single snapshot, then kept fixed throughout training. The paper does not examine whether ARank values drift as model weights evolve, nor whether the selected layers remain optimal over the course of training. This is a limitation shared with γ-MoD and does not invalidate the results, but it is a methodological gap worth acknowledging.

- **Ablation study reports only one generation metric**: Table 5 reports GenEval for all ablation variants but omits DSG and CLIP score, which are reported for the main results (Table 3). Including the full generation metric suite for ablations would give a more complete picture of how each component contributes to generation quality.

### Trivial

- **No standard deviations or confidence intervals** are reported for benchmark results. Given modest performance differences on some benchmarks (e.g., GQA: 56.3 vs. 54.5), statistical significance is unclear, though single-run evaluation is the norm in this subfield.

## Nice-to-Haves

- Profiling the router overhead (parameter count, FLOPs, memory) and characterizing the gather/scatter cost from sparse token selection would help readers understand the FLOPs-to-wall-clock gap and identify optimization opportunities.
- Demonstrating the method during pre-training or continued pre-training from an early checkpoint would strengthen the alignment between the paper's motivation and its experimental evidence.
- Including DSG and CLIP scores for all ablation variants in Table 5 would provide a more complete picture of generation quality across design choices.
- Verifying that ARank-based layer selection remains reasonable at the end of training (or periodically re-computing it) would address the static selection concern.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "The paper never explains this gap" (FLOPs vs wall-clock)** — The paper references Appendix A.2 for a discussion of this gap. The appendix was stripped by the parser but exists in the original submission. The substantive concern about the gap is retained above as a Major weakness, but the claim that the paper "never explains" it is inaccurate.

- **Harsh critic: "Section 3 connection between layer importance experiment and ARank is loose"** — The inference-time layer-skipping experiment (Table 1) and ARank analysis (Fig. 3) serve complementary purposes: the former establishes that layers have different importance, the latter quantifies token-level redundancy. Using both to motivate layer selection is reasonable, not a flaw.

- **Harsh critic: "Baselines (Early-Exit, Interleaved Layer) are extremely weak"** — These are intentionally simple sanity checks demonstrating that naive approaches fail. The ablation study (Table 5) provides more informative comparisons against Basic MoD and component-ablated variants.

- **Harsh critic: demand for full pre-training demonstration** — While clarifying the training scope is a valid request (retained as Minor), demanding full pre-training from scratch is scope creep. The method's contribution is the pruning strategy itself; the experiments demonstrate it works at the tested training stage.

- **Strength Finder: "Training cost analysis documents concrete speedups... (Tab. 4)"** — This characterization is overly generous for Show-o, where speedups are minimal (2–4%). The strength is retained above but qualified.

## Novel Insights

The paper's empirical finding that token redundancy patterns in unified transformers are task-dependent — and that this stems from the fundamentally different modeling approaches used for generation (diffusion/flow-matching) versus understanding (autoregressive) — is genuinely insightful. The competitive token pruning experiment (Figure 4) provides a clean demonstration that generation tokens dominate the routing decision when a single router is used, explaining why naive MoD fails on unified transformers. This task-competition dynamic is specific to unified models and was not identified in prior MoD work focused on single-task LLMs or MLLMs.

## Suggestions

- Add a paragraph in the main text (not just the appendix) discussing the gap between FLOPs reduction and measured training time for Show-o, including router overhead and potential optimization strategies. This would directly address the most significant concern about practical impact.
- Clarify in Section 5.1 whether the experiments constitute continued training of a pre-trained checkpoint or fine-tuning, and report the number of training steps and total FLOPs saved in absolute terms.
- Report DSG and CLIP score for all ablation variants in Table 5, and consider adding a short discussion of whether ARank values drift during training.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| PyramidDrop (5ncdKonxd4) | 3.00 | R1 | Weaker — narrower scope, less novelty |
| Balancing Token Efficiency (IqGVIU4rvM) | 2.50 | R1 | Weaker — different problem, less mature |
| A-MoD (jIAKjjEmWi) | 4.00 | R1 | Weaker — narrower evaluation, less novelty |
| ECoFLaP (iIT02bAKzv) | 5.50 | R1/R2 | Comparable — similar evaluation thoroughness, but UniMoD has stronger empirical motivation |
| SparseVLM (1xG3MN1RRW) | 5.20 | R2 | UniMoD is stronger — tackles training efficiency, has richer analysis |
| LLM-VTP (Acdd83rF1s) | 5.80 | R2 | Comparable in quality — UniMoD has broader model coverage |
| γ-MoD (q44uq3tc2D) | 6.67 | R1 | γ-MoD is stronger — more thorough evaluation, larger demonstrated speedups, first to introduce ARank for MoD |
| Transfusion (SI2hI0frk6) | 7.60 | R1 | Stronger — breakthrough contribution, more comprehensive |
| MoE++ (t7P5BUKcYv) | 8.00 | R1 | Stronger — more significant contribution |

**Round 1 bracket**: Between A-MoD (4.00) and γ-MoD (6.67), plausibly 4.5–6.5.

**Round 2 narrowing**: Compared against SparseVLM (5.20, weaker), ECoFLaP (5.50, comparable), and LLM-VTP (5.80, comparable). UniMoD has stronger empirical motivation and novelty than ECoFLaP, but the evaluation has gaps (modest practical speedup, training scope ambiguity) that place it below γ-MoD (6.67). The paper lands near ECoFLaP but slightly above due to stronger empirical analysis and more novel task-aware design.

**Final assessment**: The paper addresses a well-motivated problem with a principled, task-aware approach backed by thorough empirical analysis. The core method is sound and the ablation is clear. The main limitations are the modest practical speedup for the smaller model and ambiguity about training scope — both addressable. The paper makes a genuine contribution to efficient training of unified multimodal transformers.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>