## Summary

This paper introduces Soft MoE, a fully-differentiable routing mechanism for Mixture-of-Experts Transformers that replaces discrete token-to-expert assignments with learned convex combinations of all input tokens. Soft mixing eliminates token dropping, expert imbalance, and throughput collapse at scale while preserving the FLOPs-parameter decoupling that makes MoEs attractive. Experiments on JFT-4B and ImageNet classification show that Soft MoE models Pareto-dominate dense ViTs and standard sparse MoEs (Tokens Choice, Experts Choice)—Soft MoE B/16 (3.7B params) matches ViT H/14 (669M params) at 5× fewer inference FLOPs and 5.7× faster wall-clock time.

## Strengths

- **Fully-differentiable routing eliminates discrete assignment pathologies.** The core algorithmic contribution (Equations 1–2, Section 2.1) replaces hard top-k assignments with convex combinations computed via paired column-wise and row-wise softmax operations. This makes the entire layer differentiable (lines 100–105) and inherently immune to token dropping and expert imbalance (lines 125–131), without requiring auxiliary load-balancing losses.

- **Throughput is empirically invariant to expert count, unlike sparse MoEs.** Figure 3 (lines 327–330) shows Soft MoE's training throughput remains approximately constant as experts increase from 8 to 4,096, while sparse MoEs suffer dramatic degradation beyond 1,000 experts. This follows directly from avoiding slow top-k/sort operations (lines 138–139) and the complexity analysis in Section 2.2.

- **Strict Pareto-dominance over dense ViTs and sparse MoEs across compute budgets.** The training Pareto frontiers (Figure 2, Section 3.2) show Soft MoE outperforms both dense ViTs and sparse MoEs at every training cost/performance point on JFT-4B and ImageNet 10-shot accuracy. Table 1 quantifies this: Soft MoE B/16 (3.7B params, 32 GFLOP/img) achieves 62.4% JFT p@1 and 82.9% INet 10-shot versus ViT H/14 (669M params, 334 GFLOP/img) at 59.7% and 83.3%, while being >5× faster at inference.

- **Clean ablations confirm learned mixing is the active ingredient.** Table 2 (lines 359–365) systematically ablates routing components (Identity, Uniform, Soft/Uniform, Uniform/Soft). Full Soft MoE (54.3% JFT p@1) outperforms every variant, and notably even the Identity routing (no mixing, 51.5%) outperforms ViT (48.3%)—showing parameter scaling helps—but learned mixing adds a further 2.8–3.0 percentage points on top.

- **Representations transfer to image-text contrastive learning.** Table 2 (lines 396–408) shows frozen Soft MoE vision encoders serve as better foundations for text towers than ViT encoders on ImageNet and CIFAR-100 zero-shot, demonstrating that soft routing does not sacrifice representation generality.

## Weaknesses

### Fatal

None.

### Major

None. The paper makes a well-supported contribution within its stated scope and is transparent about its limitations.

### Minor

- **"Sparse" label in the abstract is internally inconsistent.** The abstract (line 6) calls Soft MoE a "fully-differentiable *sparse* Transformer," but the paper later explicitly states "Soft MoEs are not technically sparse" (line 143) because every token fractionally activates all parameters through the convex combination. While the sparsity claim can be defended at the expert-MLP level (each expert processes only a subset of slots), the paper's own clarification makes the abstract wording misleading. This is fixable by softening the language to "softly-sparse" or similar.

- **The claim that Soft MoE addresses "ineffective finetuning" of MoEs (line 5) is not directly tested.** The finetuning results in Table 1 compare Soft MoE against dense ViT models, not against sparse MoEs. The paper shows that Soft MoE finetunes well in absolute terms, but whether it finetunes *better than* sparse MoEs—which is what the introduction implies—remains untested. This does not weaken the paper's main contributions, but it is an unsubstantiated bullet point in the motivation.

- **The largest Soft MoE underperforms on the most challenging retrieval benchmark.** In Table 2 (lines 407–408), Soft MoE H/14 (84.6% IN/0shot, 86.3% CIFAR100) achieves strong zero-shot gains over ViT H/14 (83.8%, 84.7%), yet on COCO retrieval it underperforms ViT H/14 (61.0 vs 62.7 for Img2Text, 44.8 vs 45.2 for Text2Img). The paper's explanation—"poor alignment between features learned on closed-vocabulary JFT and this open-vocabulary task" (line 385)—is reasonable but partial. The fact that the *largest* Soft MoE (most parameters) drops below the dense baseline on this task somewhat undercuts the general "preserve benefits for image-text alignment" narrative (line 34).

- **The ablation analysis undersells an interesting asymmetry.** From Table 2, the gap between Soft/Uniform (learned dispatch only, 53.6%) and full Soft MoE (54.3%) is only 0.7% on JFT p@1, while the gap between Uniform (no learned mixing, 51.8%) and Uniform/Soft (learned combine only, 52.6%) is 0.8%. This suggests that most of the benefit from learned mixing comes from the dispatch weights alone, and the learned combine weights add comparatively little. The paper incorrectly states "dispatch mixing appears slightly more important" (line 347) when the numbers actually show dispatch is substantially more important (learned dispatch alone: +1.8% over Uniform; learned combine alone: +0.8%). A more precise discussion would strengthen the paper.

### Trivial

- The softmax normalization asymmetry (column-wise for dispatch vs. row-wise for combine) is never explicitly justified. The paper presents it as self-evident, but this design choice (as opposed to using the same normalization direction for both) merits a brief explanation.

## Nice-to-Haves

- A brief experimental demonstration of what happens *without* L2 normalization (lines 163–172) would help practitioners understand when the fix is necessary.
- Quantifying the memory footprint (model weights + activations + optimizer states) for the largest configurations (e.g., Soft MoE H/14 with 54B parameters) would help practitioners assess realistic hardware requirements.
- Including a finetuning comparison against sparse MoEs would directly test the "ineffective finetuning" motivation.
- A main-text summary of the LAION-400M results (currently only in the appendix) would strengthen reproducibility confidence.

## Removed Points

*These points were raised by the reviewers but filtered out as non-substantive, scope-inappropriate, or not verifiable from the paper.*

- **"Method evaluated only on vision tasks"**: Scope. The paper is about vision experiments, honestly notes the autoregressive decoding limitation (§6), and does not claim otherwise. Scope creep to require language experiments.
- **"Comparison with sparse MoE baselines is conflated"**: The critic claims the comparison is unfair because Soft MoE was designed to avoid routing bottlenecks. This is the *point* of the paper—showing the design pays off empirically. The paper includes sparse MoEs at their best regime (k=1–2, reasonable expert counts) and Soft MoE still wins. Not a weakness.
- **"No statistical significance / variance reporting"**: Standard for large-scale single-run benchmarks in this regime; not a meaningful gap.
- **"LAION results only in one sentence"**: Standard to defer to appendix. The reviewer has no basis to claim this is inadequate.
- **"Text encoder not jointly trained"**: The paper uses a standard frozen-encoder evaluation protocol (LIT-style). Methodological standard, not a weakness.
- **"Missing memory footprint analysis"**: Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful observations (the dispatch/combine asymmetry in ablation results, the COCO underperformance of the largest model) but these are annotations on the paper's data, not synthetic insights.

## Suggestions

1. Revise the abstract to avoid calling Soft MoE "sparse" given the paper's own later clarification that the method is technically dense at the token level.
2. Either add finetuning comparisons against sparse MoEs or remove "ineffective finetuning" from the list of problems Soft MoE addresses (line 5).
3. Discuss the dispatch/combine asymmetry more precisely in the ablation section—the data show learned dispatch contributes ~2× the gain of learned combine.
4. Add a brief discussion or caveat about the COCO H/14 underperformance in the contrastive learning section beyond the current single-sentence explanation.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>