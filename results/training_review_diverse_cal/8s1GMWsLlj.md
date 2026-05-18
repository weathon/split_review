Now I have a thorough understanding of the paper and can verify each review claim against the actual text. Let me construct the final consolidated review.

---

## Summary

This paper investigates why iterative pruning methods (LRR, WR) outperform pruning-at-initialization (PaI) methods. The authors challenge the prevailing attribution to mask learning or regularization effects, and instead argue that repeated cyclic training is the primary driver. They show that applying cyclic training to PaI methods substantially boosts their performance, often matching or exceeding LRR at low sparsity. At high sparsity, they identify that parameter-mask coupling (not mask quality alone) is the critical missing ingredient. Based on this insight, they propose SCULPT-ing — cyclic training of a sparse mask followed by single-shot magnitude pruning — which achieves LRR-competitive performance with fewer training epochs and lower memory footprint on larger networks.

## Strengths

1. **Disentangling the driver of iterative pruning performance.** The paper systematically isolates cyclic training from mask learning through controlled experiments. Figure 2 (referenced) shows that cyclic training of a dense network matches the LRR performance peak without any pruning. Figure 5 further shows that an LRR mask with random initialization performs no better than a random mask after cyclic training — cleanly isolating that the mask structure itself is not the source of LRR's advantage at high sparsity. This is a genuine conceptual contribution.

2. **Identifying parameter-mask coupling as the high-sparsity gap.** The discovery that coupling between initialization and mask is necessary for high-sparsity performance, and that even parameter signs from a short warmup are sufficient to achieve this coupling (Figure 8a), is the paper's most novel insight. The ablation experiments comparing LRR mask + random init vs. LRR mask + warmup init (Figure 5) provide controlled evidence that directly supports this claim.

3. **SCULPT-ing is a practical method that delivers on its promise.** On ResNet50 for both CIFAR100 and ImageNet, SCULPT-ing matches or outperforms LRR while using roughly half the training epochs (450 vs. 900 at 90% sparsity) and training a sparse network throughout (reducing memory footprint). The method is simple, clearly motivated by the analysis, and the empirical results across multiple datasets and architectures support its effectiveness.

4. **Principled mechanism analysis.** The linear mode connectivity analysis (Figures 3, 6) and Hessian eigenvalue analysis provide complementary evidence for *why* cyclic training helps — showing that it jumps between local optima and converges to flatter minima. This goes beyond simply observing that cyclic training works and provides some mechanistic understanding.

5. **Broad empirical scope.** Results are shown on CIFAR10, CIFAR100, and ImageNet with ResNet20, ResNet18, and ResNet50 architectures, giving reasonable confidence that the findings are not dataset- or architecture-specific artifacts.

## Weaknesses

### Fatal

None.

### Major

1. **No error bars or uncertainty quantification for any result.** Every accuracy curve is presented as a single run. This is the most significant empirical weakness. The paper makes comparative claims — e.g., that cyclic PaI "outperform[s] LRR at low sparsity," that SCULPT-ing "matches LRR performance" on CIFAR100, and that certain differences between masks are "no better" than random. Without multiple seeds or confidence intervals, the reader cannot assess whether these differences are reproducible or within noise. This is particularly problematic for CIFAR10 and CIFAR100 experiments where multi-seed evaluation is the norm in the pruning literature. While the trends across sparsity levels appear consistent, the specific comparative claims need uncertainty quantification to be convincing.

2. **Unspecified procedure for choosing the number of training cycles.** The paper states: "We choose the number of training cycles in SCULPT-ing to maximally boost performance of the sparse mask" (Section 6) and "We only need to train the sparse network for enough number of cycles such that the generalization performance peaks" (Section 4). No concrete procedure is given — e.g., whether this is based on validation or test performance, whether a fixed rule (like "train until plateau with patience 2") is used, or whether the number is tuned per sparsity level. Since LRR's number of cycles is algorithmically determined by the pruning schedule (one cycle per iteration), while SCULPT-ing's cycles appear to be selected to maximize performance, the comparison is potentially asymmetric. The paper should state a reproducibility-ready rule and report the number of cycles used for each experiment.

### Minor

3. **Epoch-count comparison as proxy for computational cost is incomplete.** The paper counts epochs to argue SCULPT-ing is cheaper than LRR (450 vs. 900 epochs for ResNet50 on ImageNet). This is meaningful as a first-order comparison, but it does not account for the per-epoch cost difference: LRR trains dense networks in early iterations while SCULPT-ing trains sparse networks throughout. In standard deep learning frameworks without sparse kernel support, a sparse network is often not proportionally faster per epoch. The paper's claim about "computational and memory resources" would be strengthened by actual timing or FLOPs measurements. The memory footprint advantage is clearly valid regardless.

4. **"Signs are sufficient for coupling" experiment is shown only on one small-scale setting.** Figure 8(a), which demonstrates that using only parameter signs (with random magnitudes) from warmup can match LRR performance, is limited to CIFAR10 with ResNet20. This is a mechanistic insight experiment and does not need to be replicated everywhere, but given that the coupling phenomenon is central to the paper's high-sparsity narrative, showing this on at least CIFAR100 would increase confidence that it generalizes.

5. **Hessian eigenvalue analysis and the dense/sparse discrepancy.** The paper shows that cyclic training leads to flatter minima (lower Hessian eigenvalues) for both dense and sparse networks, yet the performance boost is substantially larger for sparse networks (Figure 3c, and performance curves in Figure 4). The paper notes this discrepancy (dense networks "usually outperform pruned networks with our improved cyclic training schedule" in the abstract) but does not fully explain why the Hessian flatness measure alone cannot account for the differential benefit at higher sparsity. This is a minor gap in the mechanistic analysis.

### Trivial

6. **Experimental details are underspecified in the main text.** Section 3 ("Experimental Setup") states the datasets, architectures, and GPU type but omits the optimizer, learning rate values, weight decay, momentum, batch size, and data augmentation. These details are likely in the appendix (which the parser strips), but including at least the optimizer and learning rate schedule parameters in the main text would improve reproducibility.

## Nice-to-Haves

- **Code release.** Releasing code would aid reproducibility given the complexity of pruning experiments.
- **Comparison to dynamic sparse training methods** (e.g., RigL, SET, MEST). The paper explicitly focuses on fixed-mask PaI versus iterative pruning, so this is outside scope, but a brief discussion or single comparison would help contextualize SCULPT-ing in the broader sparse training landscape.
- **Explicit discussion of when SCULPT-ing is expected to fail.** The paper notes the ResNet20/CIFAR10 limitation and conjectures it is due to small parameter size. This hypothesis could be tested (e.g., scaling ResNet20's width), but leaving it as a conjecture is acceptable for a conference paper.

## Removed Points

- *"Title oversells 'training longer' thesis at expense of coupling insight"* — Presentation commentary, not a substantive weakness. Removed.
- *"Linear mode connectivity analysis is suggestive but not rigorous"* — The analysis is standard empirical evidence of its kind. The specific Hessian eigenvalue discrepancy observation is kept (Minor #5); the broader "not rigorous" characterization is removed as it misaligns with the standards for empirical analysis papers.
- *"Missing comparison to RigL/SET/MEST would strengthen the paper"* — Scope creep; the paper's focus is fixed-mask PaI vs iterative pruning. Moved to Nice-to-Haves.
- *"Paper should discuss limitations of SCULPT-ing more explicitly"* — The paper already discusses the ResNet20 limitation. Moved to Nice-to-Haves as a suggestion for deeper analysis.
- *"Code and data availability"* — Standard suggestion. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. (The reviews do not contribute novel observations beyond what the paper itself states.)

## Suggestions

1. **Add at least 3 seeds with means and standard deviations** for all main accuracy curves (Figures 4, 5, 7, 8). This is the single highest-leverage improvement. Without it, the comparative claims about outperforming/matching LRR are not fully convincing.

2. **Formalize the procedure for choosing the number of cycles.** State a clear rule (e.g., "train until validation accuracy does not improve for 2 consecutive cycles") and report the specific numbers used per experiment. Decouple this choice from test-set performance.

3. **Report actual training time or throughput** for at least the ResNet50/ImageNet comparison (SCULPT vs. LRR at 90% sparsity) to substantiate the computational savings claim.

4. **Include basic hyperparameter details** (optimizer, learning rate, weight decay, batch size) in the experimental setup section rather than deferring entirely to the appendix.

## Score and Decision

**Originality:** 7/10. The paper's main insights — that cyclic training (not mask learning) drives PaI improvement, and that parameter-mask coupling is the high-sparsity bottleneck — are novel and well-argued. The SCULPT-ing method is simple but effective.

**Importance of research question:** 8/10. Understanding why iterative pruning outperforms PaI is a central open question in the sparsity literature. The paper's findings have practical implications for efficient sparse training.

**Claims support:** 5/10. The claims are plausible and the evidence is directionally clear, but the lack of error bars and the unclear cycle selection procedure significantly weaken the support for comparative claims.

**Soundness of experiments:** 6/10. The experimental design is thoughtful (controlled ablations, coupling analysis, varied architectures). However, the missing uncertainty quantification and underspecified cycle selection are real gaps.

**Clarity of writing:** 7/10. The narrative is coherent and the progression from analysis to method is logical. Some details are deferred to the appendix.

**Value to community:** 7/10. The insights about cyclic training and coupling are likely to influence how researchers think about sparse training. SCULPT-ing is a practical method that others can build on.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>