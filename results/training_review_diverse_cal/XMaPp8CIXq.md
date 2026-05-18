Now I have full information to write the consolidated review. Let me compose it carefully.

## Summary

The paper proposes Guided Stochastic Exploration (GSE), a dynamic sparse training method that is always-sparse — it never materializes dense weights or dense gradients. At each grow/prune step, GSE samples a subset of inactive connections (size proportional to the active set), computes their gradients, and grows the ones with largest gradient magnitude. This combines the efficiency of random exploration (SET) with the guidance of gradient-based selection (RigL), while avoiding RigL's periodic dense gradient computation. Experiments on CIFAR-10/100 and ImageNet across ResNet, VGG, and ViT show GSE achieves accuracy competitive with or better than RigL and other DST methods, with a theoretical FLOPs advantage that grows with sparsity.

## Strengths

1. **GSE achieves higher accuracy than prior sparse-training methods at high sparsities.**  
   Table 1 shows GSE outperforming RigL, SET, Top-KAST, and all before-training methods at 98% sparsity across ResNet-56 and VGG-16 on CIFAR-10/100. At 98%, GSE outperforms before-training methods by 4.7% on average (Section 4.3). ImageNet results (Table 2) confirm the trend.

2. **The algorithm is designed to be truly always-sparse.**  
   Section 3 explicitly describes that "at no point is the dense model materialized" — the subset S ⊆ (W \ A) is sampled without enumerating all inactive connections, gradients are computed only for S (O(n) connections), and the top-k are selected in O(n) time via introspective selection. This design eliminates the O(n²) dense gradient computation that RigL requires every T steps.

3. **GSE has linear time complexity with respect to model width for the prune/grow step.**  
   The Erdős–Rényi initialization ensures |A| = O(n) per layer (Section 3.2). Subset sampling via the alias method runs in O(n) time, and introspective selection finds top-k gradients in O(n). This is quantified in the FLOPs comparison (Figure 4): at 99% sparsity GSE uses 11.8% fewer FLOPs than RigL, with the advantage growing dramatically at higher sparsities.

4. **Systematic investigation of subset-size and sampling distributions validates the design choices.**  
   Section 4.2 presents a thorough ablation across γ ∈ {0.25, 0.5, 1, 1.5, 2} and three distributions (uniform, GraBo, GraEst), showing that γ=1 with uniform sampling matches or exceeds RigL's accuracy. This grounds the method's hyperparameter choice in empirical evidence.

5. **Comprehensive, controlled evaluation against a wide range of baselines.**  
   Tables 1 and 2 compare GSE against nine baselines (Lottery, Gradual, SNIP, GraSP, SynFlow, SET, RigL, Top-KAST, DSR, SNFS) across three architectures, two dataset families, and three sparsity levels — all under the same optimizer settings (Section 4.1). The model scaling experiments (Section 4.5) further demonstrate that wider sparse CNNs improve accuracy for a fixed active-connection budget.

## Weaknesses

### Fatal
None.

### Major
None. No identified weakness invalidates the paper's core claims about GSE's accuracy or algorithmic properties.

### Minor

1. **γ hyperparameter shift between CIFAR and ImageNet is unexplained.**  
   Section 4.3 (CIFAR) uses γ=1, and Section 4.2 provides a systematic ablation justifying this choice. Section 4.4 (ImageNet) switches to γ=2 without any justification or sensitivity analysis. If the optimal γ varies with dataset or model scale, the paper should say so and provide guidance. If γ=2 was needed to match RigL on ImageNet, this weakens the generality of the γ=1 recommendation and raises the question of whether γ needs per-dataset tuning.

2. **The complexity comparison with RigL could be more precise about the overall picture.**  
   The paper states GSE "improves the training time complexity of RigL from O(n²) to O(n)" (Section 1). This is technically correct for the prune/grow step (RigL computes a dense O(n²) gradient every T steps; GSE computes O(n) gradients). However, the dominant cost in both methods is the sparse forward/backward pass at each training step, which is O(n) for both. The improvement is in a term amortized over T steps. The paper should clarify this to avoid giving the impression that overall training time is reduced from quadratic to linear — it is linear in n for both methods, and GSE removes a constant-factor overhead.

3. **Subset gradient computation could be described more explicitly to aid reproducibility.**  
   The paper says "their gradient magnitude is computed" (Section 3.2) for the sampled subset S, and notes that activations h and gradients δ are available from the forward/backward pass. For fully-connected layers, computing |h_i·δ_j| for each (i,j) pair in S is straightforward. For convolutional layers, the index arithmetic is more involved. While the mechanism is derivable, a more explicit description of how individual connection gradients are obtained from the available h and δ tensors — especially for convolutions — would strengthen reproducibility. Algorithm 1 provides pseudocode, but the text could be more concrete about this step.

4. **Efficiency claims in the main text are not clearly distinguished from experimental realization.**  
   Early sections state that "all forward passes use sparse weights" and "the operations are always sparse" (Section 3, Section 3.2). The Limitations section (4.7) later clarifies that accuracy experiments used mask simulation (standard practice in the field). While the paper is transparent, the unqualified language in earlier sections could mislead a casual reader into thinking the experiments used true sparse computation. A single sentence in Section 3 or at the start of Section 4 would resolve this. The FLOPs analysis (Section 4.6) is correctly presented as theoretical.

### Trivial

- **ViT scaling result is noted but not systematically investigated.**  
  Section 4.5 reports that ViT accuracy decreases with increasing width, offering a conjecture about data requirements. A brief ablation on training length or data augmentation could help determine whether this is fundamental to ViTs or specific to the training setup. The paper acknowledges the result, making this a minor presentation point.

## Nice-to-Haves

- **Wall-clock runtime comparison**: A single wall-clock time measurement (even with mask simulation) comparing GSE to RigL on a fixed problem would ground the FLOPs advantage in practice, though the paper's theoretical FLOPs analysis (following standard practice in Evci et al., 2020) is sufficient for validating the algorithmic claim.
- **Sensitivity analysis for γ on ImageNet-scale models**: A small sweep over γ (e.g., {0.5, 1, 2}) for ResNet-50 on ImageNet at 90% sparsity would address the γ=2 question directly.
- **Discussion of memory overhead**: The paper could briefly mention the O(n) memory cost of storing the subset indices and their gradient values, for completeness of the efficiency analysis.

## Removed Points

These points were raised by reviewers but are removed or substantially weakened after cross-checking against the paper:

1. **"Gradient computation is underspecified to the point of irreproducibility"** — Removed as overstatement. The paper describes that activations h and gradients δ are available from the forward/backward pass (Section 3.1, lines 68-74), and for any (i,j) pair the gradient is h_i·δ_j. The mechanism is standard and reproducible from the description. Algorithm 1 (provided as pseudocode) further covers the implementation. This is a clarity improvement at most (see Weakness #3 above), not a reproducibility blocker.

2. **"Efficiency claims are presented as practically realized despite mask simulation"** — Removed. The paper's FLOPs analysis (Section 4.6) is explicitly theoretical: "The FLOPs are obtained for ResNet-50 on ImageNet using the method described by Evci et al. (2020)." The Limitations section (4.7) openly acknowledges mask simulation. All DST papers in the field use this same standard practice. The paper's efficiency claims are about the algorithm's design and its theoretical complexity, not about wall-clock benchmarks.

3. **"Figure 4 is misleading by extending to brain-level sparsities"** — Removed. The paper clearly states this is "for illustration" (line 167) and the left plot separately shows practical sparsity levels. This is not misleading.

4. **"No standard deviations or confidence intervals reported"** — Removed. The paper states it "report[s] the mean and plot[s] the 95th percentile" (line 102). Error information is provided.

5. **"11.8% FLOPs reduction is modest"** — Removed. This is a data-point-level nitpick. The trend is that GSE's advantage grows with sparsity, which is the paper's actual claim. At 99% sparsity for the full model (including the O(n) forward/backward pass dominating), an 11.8% reduction in total FLOPs is non-trivial.

6. **Memory overhead of subset storage** — Moved to Nice-to-Haves. The subset S is bounded by γ|A| = O(n), comparable to the active set itself. This is not a meaningful gap.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an insight about the paper that the authors themselves do not already articulate. (The observation that GSE sits between SET's unbiased exploration and RigL's greedy selection is already in the paper.)

## Suggestions

- Add a brief justification for the γ=2 choice on ImageNet (e.g., ablation results or a note that γ=1 was not tested due to compute constraints, with the expectation that γ=1 would also work).
- Clarify in Section 3 or early in Section 4 that the accuracy experiments use mask simulation (standard practice) while the efficiency analysis is theoretical. A single sentence suffices.
- Make the complexity comparison more precise: state that the O(n²)→O(n) improvement is in the prune/grow step specifically, and that the dominant training cost remains the O(n) forward/backward pass for both methods.
- Provide a brief concrete example of how subset connection gradients are computed from h and δ for a fully-connected layer, to aid reproducibility.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>