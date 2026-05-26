Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper introduces Weight-Activation Subspace Iteration (WASI), a method that jointly compresses both weight matrices and activation tensors of transformers into low-rank subspaces during fine-tuning. WASI leverages the observation that weight subspaces remain stable across training iterations, using a one-time truncated SVD followed by lightweight subspace iteration, along with activation compression via a redesigned ASI. Experiments on ViT, SwinT, and TinyLlama show that WASI preserves accuracy while reducing memory (up to 62× for MLP linear layers) and computation (up to 2× FLOPs), with a 1.4× speedup on a Raspberry Pi 5.

## Strengths

- **Joint weight-activation compression under a unified low-rank framework.** WASI is the first method to simultaneously compress both weight matrices and activation tensors during transformer fine-tuning via subspace iteration (Sec. 3.3). This directly addresses the two main memory bottlenecks in backpropagation (weight storage and activation map caching), which prior work addressed separately.

- **Concrete on-device speedup validated on real hardware.** On a Raspberry Pi 5, WASI achieves ≈1.4× faster training and inference than vanilla training for ViT on CIFAR‑10 at ε=0.9 (Fig. 8). This is a practical demonstration on actual edge hardware, not just simulated metrics.

- **Large empirical savings while maintaining accuracy.** At ε=0.9, WASI matches vanilla accuracy across five image classification datasets using SwinT while cutting memory by up to 62× and FLOPs by up to 1.5× (Fig. 6). For TinyLlama on BoolQ, activation memory drops by 953×, weight memory by 30×, and training FLOPs by 13× with no accuracy loss (Fig. 7).

- **Theoretical grounding of resource trade-offs.** Section 3.4 provides closed-form expressions for memory compression and speedup ratios, offering predictive understanding of when WASI is most beneficial (Fig. 2).

## Weaknesses

### Fatal
None.

### Major

- **Headline resource-savings claims (62×, 2×) are stated in the Abstract and Conclusion without the MLP-only qualification.** The experimental setup (Sec. 4.1) clearly states that measurements focus on "linear layers within multi-perceptron blocks" and that attention-layer results are deferred to Appendix B.3. However, the Abstract and Conclusion advertise "memory usage by up to 62×" and "FLOPs by up to 2×" without this caveat. A reader who skips Sec. 4.1 would reasonably assume these are total-model numbers. In a transformer, attention linear projections (QKV, output), embeddings, and normalization also consume significant memory and compute. The paper should prominently qualify these numbers as MLP-layer-only in the Abstract, or report total-model savings. This is a framing problem, not a numerical fraud — the paper is transparent in the experimental section — but it needs correction.

- **LoRA, the de facto standard for resource-constrained fine-tuning, is not included as an experimental baseline.** The paper discusses LoRA in the related work (Sec. 2) and argues that it overlooks activation memory and does not compress the architecture for inference. While this argument has merit, LoRA is the most natural comparison point for any method claiming to enable on-device transformer fine-tuning. WASI is compared against SVD-LLM (which uses LoRA adapters but is a different paradigm), ASI (same group), and vanilla training. Without a direct comparison to standard LoRA (or LoRA+/AdaLoRA) on the same tasks and resource metrics, a practitioner cannot judge whether WASI offers a practical advantage over the approach they would most likely use today. The paper's positioning as an "on-device learning" method makes this omission significant.

### Minor

- **Validation of the weight-subspace stability assumption is thin.** The core premise — that weight subspaces remain stable across fine-tuning iterations — is supported by only one piece of evidence: Fig. 3a, which shows singular values of a single layer (W₆) of ViT on Pets. Stability should be demonstrated for multiple layers, across models (SwinT, TinyLlama), and across datasets. While the overall success of WASI (Figs. 5–7) indirectly supports the assumption, the paper would be stronger with direct evidence of stability in more settings, including a quantitative metric (e.g., subspace cosine similarity between consecutive iterations).

- **Inconsistency between the described activation rank-selection method and experiments.** Section 3.3 describes a redesigned ASI using "a dynamic-programming strategy that determines r_i by minimizing memory usage under a target pre-tuning perplexity." However, the experiments (Sec. 4.3) control compression via an explained-variance threshold ε for both WASI and ASI, with no mention of perplexity-based rank selection. The paper should clarify whether the dynamic-programming approach is used as a pre-processing step, whether ε overrides it, or whether the description and implementation diverge. As written, the methodological narrative is unclear.

- **No error bars or measures of variance for main results.** Figures 5–7 report single runs without confidence intervals. Given that accuracy differences between WASI and vanilla are often small (1–2%), statistical significance is unclear. This is a common issue in the literature but should be addressed.

- **The TinyLlama experiment uses aggressive compression (ε=0.1) and fine-tunes only the last 5 layers**, logging resource consumption only at those layers. While the results are impressive, this setting is not directly comparable to full-model fine-tuning and should be interpreted with caution. The paper acknowledges this ("due to limited resources") but could discuss potential limitations more explicitly.

- **No dedicated limitations section.** The paper does not discuss scenarios where WASI might underperform (e.g., tasks requiring full-rank weight updates, models with slow singular-value decay, or when subspace iteration convergence might be insufficient).

### Trivial
- The theoretical analysis in Sec. 3.4 assumes the same rank for weights and activations, but experiments use different ranks (controlled by ε). The paper acknowledges this simplification but could note its impact on the analysis more clearly.

## Nice-to-Haves
- Add a direct LoRA baseline to the main experiments. Even reporting results for LoRA on one setting (e.g., ViT / CIFAR‑10) would significantly strengthen the positioning.
- Expand the stability analysis (Fig. 3a) to cover multiple layers and models, with a quantitative metric such as subspace cosine similarity between epochs.
- Report total-model resource consumption (including attention layers, embeddings, normalization) in the main paper alongside the MLP-layer numbers, so readers can assess end-to-end savings.

## Removed Points

These points were flagged by reviewers but are excluded from the main review for the following reasons:

- **"SVD-LLM is a post‑training compression method, not a training‑time memory reducer"** — Removed. The paper notes that SVD-LLM is not a training-time method but uses it as a comparison for model compression during inference and for certain resource metrics. The authors acknowledge this difference and the comparison is still informative.
- **"WSI outperforms SVD by ≈35% — the description is unclear"** — Removed as a pure clarity nitpick. The paper explains this is for the same FLOPs budget; the comparison is interpretable.
- **"The Fig. 3b comparison may be trivial"** — Removed. The claim is specific (same-FLOPs comparison) and is a valid sanity check of subspace iteration efficiency.
- **"Reproducibility: main text should give enough detail"** — Removed. The paper references Appendix A.1 and A.2 for algorithm details, which is standard practice.
- **"Missing appendix content"** — Removed. The parser strips appendices; these exist in the original submission.
- **"Missing related works"** — Removed per instruction to not comment on missing related works.
- **Typo/formatting criticisms** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core narrative — joint subspace compression is promising — but do not surface a fundamentally new interpretation of the results.

## Suggestions

1. **Qualify all headline numbers in the Abstract and Conclusion** by stating that the reported 62× memory reduction applies to MLP linear layers. Better yet, report total-model savings or at least provide a rough estimate of how the savings translate to the full model.
2. **Add LoRA as an experimental baseline** in at least one primary setting (e.g., ViT on CIFAR‑10). Report the same resource metrics (training memory, FLOPs, inference efficiency) and accuracy.
3. **Reconcile the activation rank-selection description** in Sec. 3.3 with the experimental procedure. If the dynamic-programming/perplexity approach is not what is used in the main experiments, correct the text.
4. **Expand the stability validation (Fig. 3a)** to at least 3 layers per model and include a quantitative metric such as subspace cosine distance between consecutive iterations.

## Score and Decision

The paper presents a novel and practically valuable method for joint weight-activation compression during transformer fine-tuning, with real measured speedups on edge hardware. The core contribution is solid. The main weaknesses — unqualified headline claims and the missing LoRA baseline — are significant but addressable and do not invalidate the paper's central findings. I recommend acceptance with a request for the authors to address these issues in a revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>