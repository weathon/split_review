- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper challenges the prevailing narrative that iterative pruning methods like Learning Rate Rewinding (LRR) succeed primarily due to better mask identification or implicit regularization. Through systematic experiments, the authors demonstrate that LRR's repeated cyclic training schedule—not superior mask finding—is the dominant driver of its performance. They show that cyclic training substantially boosts pruning-at-initialization (PaI) methods, making them competitive with LRR at low sparsity. For high sparsity, they identify parameter-mask coupling as the missing ingredient and propose SCULPT-ing, a procedure that cycles a sparse mask, performs one-shot magnitude pruning, and retrains, achieving LRR-comparable performance at reduced computational cost.

## Strengths

1. **Cleanly demonstrates that cyclic training, not mask quality, drives LRR's success.** Figure 2(a,b) shows dense networks trained with repeated cyclic schedules match or exceed LRR's peak performance, isolating optimization duration as the key factor. Section 4's linear mode connectivity analysis (Figure 3) provides mechanistic evidence that cyclic training jumps between local optima—a behavior absent in one-cycle schedules.

2. **Cyclic training elevates PaI to competitive levels across architectures.** Figure 4 shows that cyclic training boosts random, SNIP, and Synflow masks across three datasets (CIFAR10, CIFAR100, ImageNet), with low-sparsity cyclic PaI even surpassing LRR. This directly improves upon prior PaI methods that standard training could not make competitive.

3. **Identifies parameter-mask coupling as the critical missing ingredient at high sparsity via a clean ablation.** Figure 5 demonstrates that an LRR mask with random initialization performs no better than a random mask after cyclic training, while the same mask with a warmed-up (coupled) initialization recovers full LRR performance. This isolates coupling from mask structure, which existing work had conflated.

4. **SCULPT-ing achieves LRR-level performance at reduced computational cost on larger networks.** Figures 7 and 8 show SCULPT-ing matches or outperforms LRR on CIFAR100 ResNet18, ImageNet ResNet18, CIFAR100 ResNet50, and ImageNet ResNet50, while requiring fewer total epochs (e.g., 450 vs. 900 epochs for 90% sparsity on ImageNet ResNet50).

5. **Signs alone suffice for coupling.** Figure 8(a) shows that using only parameter signs from warmup (with random magnitudes) paired with an iteratively pruned mask and cyclic training matches LRR up to 90% sparsity—a sharp mechanistic insight into lottery ticket initializations.

## Weaknesses

### Fatal
None.

### Major

- **No error bars or multiple seeds reported.** Every accuracy curve in Figures 2, 4, 5, 7, 8, and 9 appears to come from single runs. The paper contains no statement about seeds, variance, or replication. Pruning methods, especially at high sparsity, can exhibit non-trivial variance across random seeds (initialization, data ordering). Without error bars, the reader cannot assess whether observed differences between methods (e.g., cyclic PaI vs. LRR, or SCULPT vs. LRR) are meaningful or within noise. This is the single most significant evidential weakness. The conclusions may well be correct, but the evidence as presented does not support them with the required statistical confidence. The paper should either add multi-seed experiments (even 3 seeds for key comparisons) or explicitly frame itself as a single-run exploratory study and temper comparative claims.

### Minor

- **The coupling mechanism in SCULPT-ing is not analyzed mechanistically for SCULPT specifically.** The paper claims that the one-shot magnitude pruning step "induces coupling" between mask and parameters, citing the general finding that magnitude pruning minimally changes the network function (MasonWilliams & Dahlqvist, 2024). However, the paper does not directly verify what changes in the optimization landscape after this pruning step. The linear mode connectivity analysis from Sections 4 and 5 (Figures 3, 6) is not revisited for SCULPT-ing. The claim remains plausible but descriptive rather than mechanistically supported. Showing that the pruned network is mode-connected with its retrained version would directly substantiate the coupling claim.

- **Fairness of low-sparsity LRR comparison not fully controlled.** The paper claims cyclic PaI outperforms LRR at low sparsity (Figure 4). However, LRR prunes 20% of remaining weights per iteration, so at low sparsity (e.g., 20-40%), LRR undergoes very few pruning-training cycles. The paper does not show whether giving LRR additional training cycles at these low sparsities would close the gap. If LRR's performance saturates early simply because it has fewer total cycles, the claim that cyclic PaI "outperforms" LRR at low sparsity may reflect a training-budget asymmetry rather than a fundamental advantage of PaI masks. This does not undermine the paper's core thesis about cyclic training being important, but it deserves clarification.

- **Several experimental details omitted.** The experimental setup (Section 3) does not specify: optimizer (SGD vs. Adam), momentum, weight decay, batch size, data augmentation, number of epochs per cycle for CIFAR-10 and CIFAR-100 (only ImageNet's 90 epochs is stated), or the exact cyclic learning rate schedule parameters. The signs experiment (Figure 8a) describes using "random weight magnitudes" without specifying the distribution or scale. These are standard details required for reproducibility.

- **Abstract slightly overclaims.** The abstract states SCULPT-ing "matches the performance of state-of-the-art iterative pruning methods in the high sparsity regime," but on CIFAR-10 with ResNet-20, SCULPT-ing cannot match LRR (acknowledged in Section 6). The broader results on ImageNet and CIFAR100 do support the claim, but the abstract would benefit from a qualifier (e.g., "on larger networks").

### Trivial

- The word "describle" appears instead of "describe" in Section 3 (line 49). This is a parser artifact from PDF extraction and does not reflect the original submission quality.

## Nice-to-Haves

- **Demonstrate SCULPT-ing's coupling with linear mode connectivity.** Revisiting the analysis from Figures 3 and 6 for SCULPT-ing (comparing the pre-prune network to the retrained network) would directly support the coupling claim.
- **Include comparisons with dynamic mask methods** such as AC/DC (Peste et al., 2021) or RiGL (Evci et al., 2020) that also train sparse networks longer but update masks dynamically.
- **Provide wall-clock time or FLOP measurements** to complement the epoch-count comparison. Sparse operations may not be efficiently accelerated on standard hardware, so actual cost savings depend on implementation.
- **Explore SCULPT-ing's failure on small networks** more systematically (e.g., test on wider ResNet-20 or deeper small architectures) to substantiate the "small parameter size" conjecture.
- **Perform SCULPT-ing starting from the target sparsity** to make the "sparse training from scratch" framing cleaner, or explain why this does not work.

## Removed Points

- *Coupling mechanism point about the paper not showing what constitutes "coupling" in terms of the optimization landscape.* This is a restatement of the retained minor weakness about lack of mechanistic analysis for SCULPT-ing; merged into the single Minor point above rather than kept as a separate weakness.
- *Criticism about missing appendix, missing proofs in appendix, or absent references.* These are known to be parser-stripped content that exists in the original submission. Removed per hard rules.
- *Code availability suggestion.* Not a weakness; moved to implicit nice-to-have.
- *"The low-sparsity outperforming LRR claim needs scrutiny" framing as a Critical Issue.* Redundant with the retained Minor weakness; demoted from Critical Issue to Minor because the concern is about training-budget asymmetry, not a methodological error. The paper's core claim about cyclic training's importance remains unaffected.
- *Strength Finder's generic statements* (not present in the provided Strength Finder output; all listed strengths are concrete and evidence-backed, so none were removed).

## Novel Insights

None beyond the paper's own contributions. The reviews primarily validate the paper's framing and add a demand for statistical rigor, which is a standard methodological requirement rather than a novel observation.

## Suggestions

1. **Add multi-seed experiments with error bars to the key comparative figures** (Figures 4, 5, 7, 8). Even 3 seeds with mean ± std for the main comparisons (cyclic PaI vs. LRR, SCULPT vs. LRR) would substantially strengthen confidence in the results. If this is infeasible, clearly state that results are from single runs and temper comparative language.
2. **Provide complete experimental specifications** in the setup section: optimizer, momentum, weight decay, batch size, data augmentation, per-dataset epoch counts per cycle, and the exact cyclic learning rate schedule (e.g., cosine annealing with warm restarts, schedule parameters).
3. **Describe the random magnitude initialization** in the signs experiment (Figure 8a) precisely—distribution, scale, and any normalization used.
4. **Address the LRR low-sparsity comparison** by either showing that LRR with extra cycles at low sparsity does not improve further, or clarifying the asymmetry.
5. **Revisit linear mode connectivity for SCULPT-ing** to directly demonstrate that the pruning step places the network in a mode-connected basin with the retrained solution.
