Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper addresses the problem of implicit subpopulation imbalance — where class labels are balanced but hidden subpopulations within classes are imbalanced. The authors propose SHE (Scatter and HarmonizE), a method that discovers latent subpopulations by maximizing predictive information (via an optimal data partition objective), then combines per-subpopulation predictions using LogSumExp to achieve subpopulation-balanced predictions. The method is supported by information-theoretic motivation, theoretical analysis, and comprehensive experiments across multiple benchmarks.

## Strengths

1. **Novel and well-motivated method for an important problem**: The paper targets the under-explored setting of implicit subpopulation imbalance, which differs from standard class imbalance and spurious correlations. The motivating figures (Figures 1–2) and the information-theoretic framing via interaction information (Definition 3.1) provide a clear conceptual foundation for why discovering and rebalancing subpopulations can improve generalization.

2. **Clean theoretical insight for balanced prediction (Theorem 3.4)**: The paper proves that applying LogSumExp to per-subpopulation logits yields predictions that fit the subpopulation-balanced distribution, assuming each subpopulation model fits its conditional distribution. This is a simple, elegant result that cleanly justifies the HarmonizE component and requires no subpopulation annotations at test time.

3. **Consistent and non-trivial empirical gains across benchmarks**: Table 2 shows SHE outperforms the best baseline by 1.72% on COCO, 1.50%/1.35%/1.53% on CIFAR-100 (IR=100/50/20), and 1.42% on tieredImageNet, with standard deviations reported. These results are replicated across multiple datasets and imbalance ratios.

4. **Fine-grained improvement on minority subpopulations without harming majority ones**: Table 3 shows SHE improves the Few-split (minority subpopulations) by 4.42% over the best baseline on COCO while also achieving the best Many- and Medium-split accuracies. This demonstrates meaningful subpopulation-level rebalancing.

5. **Thorough ablation validating all components**: Figure 4 and Table 5 systematically isolate each design choice. K=1 degrades to ERM, removing the diversity term (β=0) still beats ERM but adding it helps, removing the entropy term reduces accuracy, and SHE outperforms model-based V and EIIL-style alternatives. These ablations confirm the necessity of each proposed component.

6. **Generalization to richer settings**: Table 4 shows SHE combined with LA handles co-existing class and subpopulation imbalance (1.19–1.80% gains), and SHE_{w/GDRO} achieves competitive worst-group accuracy on CelebA and Waterbirds without group annotations. Table 6 shows SHE remains effective when fine-tuned from CLIP/ALIGN/AltCLIP via LoRA.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between the theoretical analysis and the implementation**: This is the paper's most significant weakness. Theorem 3.3 provides a generalization bound for minimizing the empirical risk in Eq. (1) for a **fixed** data partition ν (a function mapping X×Y→S with hard indicator assignments). The implementation in Section 3.4 replaces ν with a per-sample soft assignment matrix V ∈ ℝ^{N×K}, which is optimized jointly with the network. The bound does not account for the complexity or optimization of V (or ν), and Eq. (2) uses soft probabilities v_{is} rather than the hard indicators 𝟙(ν(x_i,y_i)=s) analyzed in the theorem. The paper claims "it is theoretically demonstrated that our method converges to optimal data partition," but the convergence guarantee holds for fixed ν, not for the joint optimization over ν and f that is actually performed. This gap means the theoretical claims about optimal data partition are overstated relative to what the analysis actually supports. The LogSumExp result (Theorem 3.4) is not affected by this gap — it remains a clean and valuable insight. The empirical contributions are also unaffected, but readers should interpret the theoretical grounding as motivational rather than as a proof that the learned V corresponds to the optimal ν defined in Definition 3.1.

### Minor

1. **No principled guidance for choosing K (number of subpopulations)**: The paper sets K=4 for all experiments and provides ablation for K=1..6 on COCO (with similar trends referenced to the appendix for other datasets). However, there is no discussion of how a practitioner would select K in a real application where subpopulations are truly unknown, nor analysis of behavior when K is severely misspecified (e.g., K=2 when the true K=8). The method's sensitivity to under- or over-specifying K is only partially explored.

2. **No explicit limitations section**: The paper does not discuss its own limitations. Important considerations that would help readers — such as the potential for V to overfit (amplified by the N×K parameterization), the need to pre-specify K, the assumption of fixed K across all classes, and the fact that the multi-head strategy divides feature channels equally among K heads (reducing per-head capacity) — are not acknowledged. A brief limitations paragraph would substantially improve the paper's scholarly rigor.

3. **Framing of the distinction from spurious correlations could be clearer**: The paper describes subpopulation imbalance as distinct from spurious correlations (Table 1), then evaluates the method on spurious correlation datasets (CelebA, Waterbirds) where it performs well. While not contradictory (the method can address both problems), the claimed sharp distinction is somewhat artificial — many spurious correlation problems can be reframed as subpopulation imbalance problems where the spurious attribute defines the subpopulation. The paper would benefit from a more nuanced discussion of this relationship rather than emphasizing separation.

4. **Analysis of computational cost is absent**: The method learns a per-sample V of size N×K and trains K classifier heads. While the multi-head strategy does not increase total parameter count compared to a standard single-head network, the joint optimization of V and the network, plus the diversity regularization, adds computational overhead. Runtime and memory comparisons with baselines are not reported.

### Trivial
None.

## Nice-to-Haves

- A variant that learns ν as a function g(x,y) (e.g., a small network taking features and labels) rather than a per-instance matrix V would directly bridge the theory-implementation gap and provide better generalization to unseen data.
- A heuristic for selecting K (e.g., based on validation performance, NMI elbow, or a Bayesian nonparametric approach) would improve practical deployability.
- An analysis of convergence behavior or sensitivity to V initialization would strengthen the methodological exposition.

## Removed Points

- **"The problem formulation claims a sharp separation from spurious correlations but the experiments show overlap"** — The paper explicitly states it "shares the similar rebalancing spirit" and provides Table 1 to formally distinguish the concepts. The overlap is acknowledged and the experiments on spurious correlation datasets demonstrate broader applicability, which is a strength, not a contradiction. Keeping this criticism would be inconsistent with the paper's actual framing.

- **"Some spurious-correlation methods (EIIL, JTT) require a held-out validation set; the paper does not specify"** — Line 144 explicitly states "methods for spurious correlations that do not require subpopulation annotation on the training and validation set." The paper does address this.

- **Test set construction is unclear** — Lines 50–56 define the subpopulation-balanced test distribution, and lines 142–143 describe how each dataset's test set is constructed (ALT-protocol for COCO, balanced sampling from subclasses for CIFAR-100/tieredImageNet). The description is adequate.

- **"K multiplies the Rademacher complexity; for large K this bound degrades"** — This is describing a standard property of the bound, not identifying a weakness.

- **Formatting/style nitpicks and requests for missing appendix content** — These reflect parser artifacts and should not be held against the paper.

## Novel Insights

The reviews surface an important meta-point about a common pattern in ML papers: theoretical guarantees are derived for an idealized version of the algorithm (hard assignments via a fixed function ν), while the practical implementation uses a relaxed/learned version (soft assignments via per-instance parameters V). The harsh reviewer correctly identifies this as a gap, but it is a gap of degree rather than kind — many latent variable methods use similar two-stage reasoning (theory for fixed assignments, practice with learned assignments). The more novel observation is that the paper's own ablation (SHE vs. SHE_{model-based V}) shows the per-sample V outperforms a function-based approach, suggesting the extra flexibility of per-instance parameters is empirically beneficial for subpopulation discovery even though it complicates the theoretical picture. This tension between theoretical tractability and practical effectiveness is worth exploring explicitly in future work.

## Suggestions

1. **Acknowledge and address the theory-implementation gap explicitly.** Either (a) reformulate the theory to cover the per-sample V (e.g., adding a regularizer and deriving a uniform bound over ν), or (b) clearly state that the theoretical analysis applies to the idealized case of fixed ν and that the joint optimization of V is justified empirically, with the theory serving as motivation. This would align the paper's claims with its actual contributions.

2. **Add a limitations paragraph** discussing the K selection issue, the potential for V to overfit, the multi-head capacity trade-off, and the relationship to spurious correlations.

3. **Provide a brief practical guide for choosing K** — even a heuristic based on validation-set accuracy or NMI would significantly improve the paper's usefulness to practitioners.

4. **Report computational cost** (training time, memory) for SHE vs. baselines to help readers assess practical trade-offs.

## Score and Decision

The paper addresses a genuine gap in the literature with a novel, well-motivated method. The empirical validation is strong — consistent gains across multiple benchmarks, thorough ablations, and demonstrations under co-existing class/subpopulation imbalance, spurious correlations, and fine-tuning scenarios. Theorem 3.4 (LogSumExp for balanced predictions) is a clean theoretical contribution.

The paper's primary weakness is the gap between the theoretical analysis (which assumes a fixed hard partition ν) and the implementation (which learns a soft per-instance partition V). This overstates what the theory actually proves and is a significant limitation, but it does not invalidate the empirical contributions or the LogSumExp guarantee. The method works and the results are credible.

Overall, this is a solid paper with a clear contribution that is somewhat weakened by overstated theoretical claims. With proper revisions to align the claims with the analysis, it would be a stronger paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>