## Summary

This paper challenges the conventional view that softmax's effectiveness in attention stems from producing probability distributions (non-negativity, row normalization, sparsity). It argues instead that softmax's key role is implicit regularization of the Frobenius norm of the attention matrix (Theorem 1: $\|\text{softmax}(A)\|_F \leq \sqrt{N}$). From this perspective, it derives scaled polynomial activations $\phi(x) = \frac{1}{\sqrt{N}}x^p$ intended to achieve the same $\mathcal{O}(\sqrt{N})$ norm bound, and evaluates them on image classification (Tiny-ImageNet, ImageNet-1k), object detection/segmentation (COCO), and NLP (LRA). The empirical results show that the scaled cubic activation $x^3/14$ is broadly competitive with softmax — winning on several ViT/Swin/XCiT architectures while losing on DeiT and some LRA tasks.

## Strengths

1. **Theorem 1 establishes a clean $\mathcal{O}(\sqrt{N})$ Frobenius-norm bound for softmax attention and its gradient.** Section 3.1 proves $\|\text{softmax}(A)\|_F \leq \sqrt{N}$ and $\|\nabla\text{softmax}(A)\|_F \leq 2\sqrt{N}$, directly linking the regularity of the attention matrix to sequence length $N$. While the bound itself is a simple consequence of row-stochasticity, the paper's use of it as a design principle for alternative activations is a worthwhile departure from prior Lipschitz-based analyses.

2. **Figure 1 empirically validates the $\sqrt{N}$ scaling law predicted by the theory.** The experiment trains ViT-Tiny on Tiny-ImageNet with the $x^3$ activation at four different sequence lengths (256, 64, 16, 8) while varying the scale factor. As sequence length decreases, the optimal scale decreases, confirming the $\mathcal{O}(1/\sqrt{N})$ relationship. This is the paper's cleanest theory-to-experiment validation.

3. **The scaled cubic activation demonstrates broad competitiveness with softmax across multiple architectures and tasks.** On ImageNet-1k (Table 2), $x^3/14$ matches or exceeds softmax on 5 of 8 architectures: ViT-Base (79.6 tie), ViT-Small (80.5 vs. 80.2), Swin-Base (83.2 vs. 83.0), Swin-Small (83.4 vs. 83.3), and XCiT-Small (82.1 vs. 81.2). COCO detection/segmentation results (Table 3) show near-identical performance to softmax, and the cubic activation wins on 2 of 5 LRA tasks. This breadth supports the paper's central claim that softmax's properties (non-negativity, normalization, sparsity) are not strictly necessary.

4. **Attention heatmaps (Figures 6–11) show that polynomial activations produce qualitatively different attention patterns — including negative values — yet achieve competitive performance.** This visually reinforces the argument that the conventional desiderata for attention weights can be violated without catastrophic failure.

## Weaknesses

### Major

1. **Theory and experiments operate on different mathematical objects (structural gap).** The theoretical analysis in Section 3.2 (Theorem 2, Corollaries 1–4) proves bounds on the Frobenius norm of *matrix powers* $(XQK^TX^T)^p$ — i.e., the attention-score matrix multiplied by itself $p$ times via matrix multiplication. The experiments, by contrast, use "polynomial activations" $\phi(x)=x^3$ and $\phi(x)=x$. In standard deep learning, an "activation function" applied to a matrix is understood element-wise: $[a_{ij}] \mapsto [a_{ij}^3]$. Element-wise cubing is mathematically distinct from the matrix cube $A^3 = A \times A \times A$; they produce different numerical values, different Frobenius norms, and different scaling behavior with $N$. The paper never clarifies which operation is used in the experiments and provides no argument bridging this gap. If the experiments use element-wise operations (the standard reading), **the theoretical guarantees in Section 3.2 do not apply to the experimental setup**, and the claimed link between the theory and the empirical design is unsupported. This does not invalidate the empirical results, but it severs the paper's primary intellectual thread connecting the theoretical framework to the experimental validations.

2. **The causal claim that Frobenius-norm regularization is *why* softmax works is asserted, not supported.** The abstract states "we theoretically show that its success lies in its ability to implicitly regularize the Frobenius norm of the attention matrix." The paper demonstrates a *correlation*: (a) softmax satisfies $\|\text{softmax}(A)\|_F \leq \sqrt{N}$, and (b) scaled polynomial activations that also have bounded Frobenius norm perform competitively. But no ablation directly tests whether the norm bound is causally responsible — e.g., by artificially modifying softmax's Frobenius norm (via scaling or clamping) and measuring the effect on performance, or by testing an activation with similar norm behavior but totally different semantics. The claim that regularization is "why softmax works" exceeds what the evidence supports.

### Minor

1. **Internal inconsistency in the Tiny-ImageNet scale reporting.** Line 221 states "Results in table ... show $\frac{1}{8}x^3$ outperforming softmax," but the table header (line 234) reads $\frac{x^{3}}{16}$ and the caption (line 240) says "the right scale of $\frac{1}{8}$." The paper simultaneously prints $1/8$ in the text, $1/16$ in the table, and $1/8$ in the caption. This is confusing and suggests careless writing. More generally, the process for selecting the "best" scale is not described — how many scales were searched, over what range, on which validation split?

2. **No conclusion, discussion of limitations, or synthesis of results.** The paper ends abruptly after the LRA table. There is no reflection on what the mixed results collectively imply (e.g., why the cubic activation underperforms on DeiT architectures but wins on Swin, or why it loses on 3 of 5 LRA tasks). Given the paper's stated goal of "critically examining softmax attention" and "uncovering deeper insights," the absence of a synthesized discussion is a structural omission.

3. **No statistical significance measures.** None of the tables report error bars, confidence intervals, or standard deviations across runs. Several comparisons show margins below 1% (e.g., 79.6 vs. 79.6 on ViT-Base, 83.0 vs. 83.2 on Swin-Base). Without variance estimates, it is impossible to assess whether the reported differences are meaningful or within noise.

4. **The LRA experiments reuse a fixed scale $1/14$ without justification for varying sequence lengths.** The LRA tasks (e.g., ListOps up to ~2,000 tokens, Pathfinder with different lengths) have sequence lengths that differ from ImageNet's $N=196$. The theory prescribes a scale of $1/\sqrt{N}$, but the paper does not report per-task sequence lengths or justify why a single scale works across tasks.

5. **The theoretical analysis relies on i.i.d. Gaussian assumptions for $X$, $Q$, $K$ (Theorem 2).** During training, activations are not Gaussian (they are processed through layers with nonlinearities), and $Q$, $K$ are learned and correlated. The paper acknowledges the expectation framework but does not discuss how violations of this assumption might affect the practical validity of the bounds. This limits the practical applicability of the theoretical guarantees.

### Trivial

- The caption of Figure 4 (line 319) says "ViT-Tiny" but the surrounding text refers to ViT-Small, indicating a copy-paste error in the figure label.

## Nice-to-Haves

- **Comparison against at least one alternative activation from related work** (e.g., ReLU attention) would contextualize the results. The paper cites ReLU attention, Taylor softmax, and periodic alternatives but tests none, making it hard to assess whether the proposed polynomial activations offer any advantage over these existing approaches.
- **Ablation testing causality** (e.g., clamping or scaling softmax's Frobenius norm and measuring performance impact) would strengthen the central claim about Frobenius-norm regularization being the operative mechanism.

## Removed Points

These points were raised by reviewers but removed after filtering:

- *"The paper may not be reproducible because the code is not included"*: Removed per hard rule — code availability is not a criticism of the paper's content.
- *"Missing appendix proofs"*: Removed per hard rule — the parser strips appendices from all papers.
- *"The Frobenius norm bound is trivial (just from row-stochasticity)"*: Removed — while the bound is simple, the paper uses it as a design principle for deriving alternative activations, which goes beyond prior work. This is a matter of interpretation, not a concrete weakness.
- *"The paper should pursue SOTA results"*: Removed — the paper explicitly disclaims this goal.
- *"The λ(x) = x activation performs poorly, contradicting the claim"*: Weakened — the paper acknowledges this and focuses on the cubic activation as the primary alternative. The linear activation is included as a natural baseline from the theoretical framework.

## Novel Insights

The most interesting point to emerge from reviewing this paper is the tension between what the theory guarantees and what the experiments actually test. The paper proves bounds on matrix powers $(XQK^TX^T)^p$ but experiments with element-wise $x^p$. If the empirical results hold despite this gap, either (a) there is a hidden theoretical connection between these operations under the specific conditions of training, or (b) the scaling law $1/\sqrt{N}$ is more empirically robust than the specific mathematical form used to derive it. This suggests the real contribution may be the empirical finding that scaling matters, with the theory providing intuition rather than proof. The paper would be strengthened by acknowledging this directly.

## Suggestions

1. **Clarify the activation operation.** State explicitly whether $\phi(x) = x^p$ is applied element-wise or as a matrix power. If element-wise, either provide theoretical justification for why the matrix-power bounds carry over, or reframe the theory as providing intuition rather than direct guarantees. This is the single most important fix.

2. **Calibrate the causal claim.** Replace "its success lies in" with "we hypothesize that part of softmax's effectiveness may stem from" or add a direct ablation test.

3. **Add a conclusion that synthesizes the mixed results.** Discuss when polynomial activations help vs. hurt (e.g., why they work on Swin but not DeiT) and what this reveals about attention mechanisms.

4. **Resolve the $1/8$ vs. $1/16$ discrepancy** and describe the scale search procedure (number of candidates, range, validation criterion) for reproducibility.

5. **Report error bars or confidence intervals** for at least the main ImageNet-1k and LRA experiments.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>