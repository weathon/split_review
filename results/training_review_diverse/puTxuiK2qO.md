Now I have the full picture of the paper and can verify reviewer claims directly. Let me write the final consolidated review.

---

## Summary

AdaFisher proposes an adaptive second-order optimizer that replaces Adam's second-moment estimate with a diagonal block-Kronecker approximation of the Fisher Information Matrix (FIM). The method applies K-FAC's block-diagonal structure, extracts only the diagonals of the Kronecker factors, normalizes them via Min-Max scaling, and incorporates the result as a preconditioner in the Adam framework. Empirical results on CIFAR-10/100, ImageNet, TinyImageNet, WikiText-2, and PTB show consistent accuracy/perplexity improvements over Adam, AdaHessian, K-FAC, and Shampoo across CNNs and vision transformers.

## Strengths

- **Consistent and substantial accuracy improvements across architectures and datasets.** On CIFAR-10/100, AdaFisher achieves the highest accuracy among all compared optimizers across ResNet-18/50/101, DenseNet121, MobileNetV3, and transformer-based models (Tiny Swin, FocalNet, CCT-2/3×2). For example, on ResNet-101 CIFAR-100: AdaFisher 80.65% vs. next-best Shampoo 78.83% (Table 1). On ImageNet with batch size 256: AdaFisher 76.95% Top-1 vs. Shampoo 72.82% and K-FAC 70.96% (Table 2). These gains are consistent, not cherry-picked.

- **Demonstrated stability across learning rates and batch sizes.** The stability analysis (Figure 4) shows AdaFisher maintains high accuracy across a wide range of learning rates (0.0001–0.01) and batch sizes (64–1024), where competing optimizers degrade more significantly. This is a practical advantage that reduces hyperparameter tuning burden.

- **Novel diagonal block-Kronecker approximation with a clean integration into Adam.** The core idea—diagonalizing Kronecker factors of the FIM and plugging the result into Adam's second moment (replacing the EMA of squared gradients)—is conceptually clean. Table 1's summary of optimizers clarifies how AdaFisher differs from Adam, AdaHessian, K-FAC, and Shampoo. The method introduces only one additional hyperparameter over Adam.

- **Extension to normalization layers (BatchNorm, LayerNorm).** Proposition 2 derives Kronecker factors for normalization layers, extending the method's applicability to modern architectures including Transformers. The language modeling results on WikiText-2/PTB using a GPT-1-style model demonstrate this extension works.

- **Trajectory visualization and FIM histogram analysis.** The paper provides visualizations (loss landscape trajectories, FIM diagonal histograms) that offer qualitative insight into why AdaFisher converges to different regions of the loss landscape compared to Adam.

## Weaknesses

### Fatal

None.

### Major

- **Ablation studies are entirely missing.** Section 4.4 states "We further conduct extensive ablation studies on additional components of AdaFisher, including the convergence efficiency, our novel approximation of the FIM, the significance of EMA for Kronecker factors, the impact of the square root, the stability across learning rate schedulers and the updated computation of the FIM for normalization layers" — but **no ablation results appear in the paper**. This is the single most critical gap. Without ablations, it is impossible to verify that the diagonal Kronecker approximation (as opposed to the EMA scheme, the Min-Max normalization, the removal of the square root, or the damping term) drives the observed gains. A controlled comparison (full AdaFisher vs. variants without the diagonal approximation, without Min-Max normalization, with square root reintroduced, etc.) is essential to substantiate the paper's central claim.

- **Wall-Clock-Time (WCT) cutoff conflates convergence quality with speed.** The paper uses a WCT-based evaluation: AdaFisher trains for 200 epochs; other optimizers are terminated when AdaFisher finishes. For ImageNet, Adam is given 90 epochs because it "surprisingly matched AdaFisher's training duration." This protocol makes it impossible to separate the optimizer's intrinsic convergence properties from per-epoch computational differences. The paper does not report equal-epoch results, which are standard practice for optimizer evaluation. Given that second-order methods can have different per-epoch costs, the reported accuracy gaps could partially reflect epoch count differences rather than optimization quality. The authors should report results at equal epochs (e.g., 90 or 200 epochs for all optimizers) alongside the WCT results.

- **Evidence for diagonal dominance is limited to a qualitative demonstration on a single layer.** The core motivation for the diagonal approximation (Section 3.1) rests on a Gersgorin-disk and eigenvalue-perturbation analysis of the **37th convolutional layer of ResNet-18 at two training steps**. No quantitative metrics are reported (e.g., ratio of diagonal sum to total sum, Frobenius norm of off-diagonals vs. diagonals). No demonstration is provided for early layers, late layers, other architectures (e.g., Transformers), or different training stages. Given that the entire method hinges on this approximation being valid across layers and architectures, the empirical basis is thin. The paper would be substantially stronger with a systematic analysis across layers, architectures, and training stages.

### Minor

- **Min-Max normalization of Kronecker factors is introduced without justification.** Proposition 1 applies Min-Max normalization to the diagonals of \(\mathcal{H}_{D_i}\) and \(\mathcal{S}_{D_i}\) before taking the Kronecker product, rescaling each factor's entries to [0,1] based on batch statistics. The paper offers no explanation for why this normalization is necessary, what properties it preserves, or how it interacts with the EMA updates and the damping term \(\lambda\). This design choice is opaque and could affect reproducibility.

- **Convergence theory is too generic to be informative.** Proposition 1 (convex) merely states the scheme "converges" and the "rate is bounded"—this carries no content. Proposition 2 (non-convex) derives an \(O(\log T / \sqrt{T})\) bound by referencing Chen et al. (2018) for "generalized Adam-type methods," without constructing a Lyapunov function specific to AdaFisher or showing how the diagonal Kronecker approximation affects the bound. The theoretical section does not distinguish AdaFisher from any other Adam-family optimizer and is presented as a contribution that it does not substantively make.

- **Language modeling baselines raise tuning concerns.** On WikiText-2, AdaFisherW achieves 152.72 PPL while AdaHessian (407.69) and Shampoo (1727.75) perform dramatically worse. Shampoo's failure to converge and the statement that K-FAC "was unable to train effectively" (line 286) suggest possible suboptimal hyperparameter selection or implementation issues. The paper should report tuning details for baselines or include additional well-tuned second-order baselines.

- **Ambiguous indexing in the EMA update (Algorithm 1).** Lines 3–4 of Algorithm 1 use \(i\) to denote both the layer index (1 to \(L\)) and a time index within the EMA update (e.g., \(\mathcal{H}_{D_{i}} \leftarrow \gamma_1 \mathcal{H}_{D_{i-1}} + (1 - \gamma_2)\mathcal{H}_{D_{i}}\)). It is unclear whether \(\mathcal{H}_{D_{i-1}}\) refers to the previous layer's factor or the same layer's factor from the previous time step. This needs disambiguation for reproducibility.

- **Normalization layer derivation (Proposition 2) lacks validation.** The proposed formula for Kronecker factors of BatchNorm/LayerNorm (averaging over batch and spatial dimensions then forming a rank-1 matrix) is a very crude approximation. The paper does not validate this formula against the true FIM block for normalization layers, nor does it compare to the standard K-FAC treatment of these layers. This component is presented as a contribution (C2) but is unverified.

### Trivial

None.

## Nice-to-Haves

- Equal-epoch comparisons alongside WCT results to disentangle convergence quality from throughput.
- A systematic quantitative analysis of diagonal dominance across layers (early, middle, late), architectures (CNNs + Transformers), and training stages.
- Controlled ablation isolating each design choice: diagonal approximation, Min-Max normalization, square-root removal, EMA decay rates.
- A cleaner derivation or alternative treatment of normalization-layer Kronecker factors, with empirical validation.

## Removed Points

- **"Error bar overlap" claim (harsh critic):** The reviewer claimed standard deviations overlap for some results (e.g., ResNet18 CIFAR10: AdaFisher 96.25±0.17 vs. K-FAC 95.17±0.16). These intervals do **not** overlap. The claim is factually incorrect and is removed.
- **Criticism about missing appendix / code in appendix:** Per instructions, the appendix is stripped by the parser; the original submission likely contains it. Removed.
- **Missing related work:** Per instructions, external verification of missing related work is not possible. Removed.
- **Generic critique that first-order methods "require extensive hyperparameter tuning" is too broad:** This is a framing argument, not a structural weakness. Removed as editorial opinion rather than verifiable flaw.
- **Strength Finder claim about "theoretical convergence guarantee":** The harsh critic correctly identifies that the convergence analysis is derivative and generic. This strength conflicts with a verified weakness (the theory is too shallow to be a genuine contribution). Moved here.

## Novel Insights

None beyond the paper's own contributions. The review process reveals that the paper presents a plausible, empirically promising approach whose core claim (that diagonalized Kronecker factors yield a practical second-order optimizer) cannot be fully verified due to missing ablations and a confounded experimental protocol. The diagonal-dominance motivation, while intuitive, lacks the quantitative rigor needed to support the method's central approximation. The normalization-layer derivation and Min-Max normalization are presented without sufficient justification or validation.

## Suggestions

1. **Add ablation studies as the highest priority.** On a representative task (e.g., ResNet-50 on CIFAR-100), compare: (a) full AdaFisher, (b) no diagonal approximation (use full K-FAC factors with EMA), (c) no Min-Max normalization, (d) with square root reintroduced, (e) with Adam-style second-moment EMA instead of the paper's EMA scheme. This is the only way to verify what drives the gains.
2. **Add equal-epoch comparisons** for all experiments. Report the accuracy at, e.g., 90 and 200 epochs for all optimizers, and present the WCT results as supplementary.
3. **Provide quantitative diagonal dominance metrics** across multiple layers, architectures, and training stages. Report the ratio \(\sum |\text{diag}| / \sum |\text{all entries}|\) or the off-diagonal-to-diagonal Frobenius norm ratio.
4. **Justify or remove the Min-Max normalization**, or provide an ablation comparing performance with and without it.
5. **Clarify the EMA indexing** in Algorithm 1 and equations, and cleanly separate layer indices from time indices.
6. **Either strengthen the convergence theory** (prove a property specific to the diagonal Kronecker approximation) **or remove the theoretical claims** and present the convergence analysis as a straightforward adaptation of existing results.

## Score and Decision

The paper proposes a sensible and promising idea, and the empirical results are consistently positive across a diverse set of tasks and architectures. However, the combination of (a) entirely missing ablation studies that are essential to verifying the core methodological claim, (b) a confounded experimental protocol (WCT cutoff without equal-epoch results), and (c) limited evidence for the diagonal-dominance motivation means the contribution is not convincingly demonstrated in its current form. The core issues are addressable with additional experiments and analysis, but the paper as submitted does not meet the bar for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>