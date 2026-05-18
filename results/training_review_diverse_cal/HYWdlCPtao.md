Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes CEMS (Curvature Enhanced Manifold Sampling), a data augmentation method for regression that extends prior first-order manifold sampling (FOMA) by incorporating second-order (curvature) information. CEMS samples synthetic points from a second-order Taylor approximation of the data manifold, using CAML for curvature estimation and practical batch-level optimizations to keep computational costs manageable. The method is evaluated on 9 in-distribution and out-of-distribution regression benchmarks, where it consistently ranks among the top 2 methods.

## Strengths

1. **Principled algorithmic extension from first-order to second-order manifold sampling.** CEMS explicitly extends FOMA's first-order tangent-space approach by incorporating curvature (Hessian) information via a second-order Taylor expansion of the embedding map *g*. This is a clear, well-motivated advance: the paper shows (Section 4, Fig. 1) that first-order methods deviate from the manifold near high-curvature regions, and Theorem 4.1 (even though a cited result) provides a formal justification for why the cubic error decay of second-order sampling can better preserve manifold structure locally.

2. **Consistently strong empirical performance across all 9 benchmarks.** In Tables 1 and 2, CEMS achieves either the best or second-best result on every single in-distribution and out-of-distribution task. On 5 of 9 tasks it is the best method; on the remaining 4 it is within a very small margin of the best. The relative improvement on SkillCraft Worst (8% over the second-best) is particularly noteworthy. This consistency is a genuine strength — the method does not have any "failure" datasets.

3. **Practical batch-level efficiency with explicit complexity and memory analysis.** The paper devises a batch-wise procedure (Alg. 2, Section 4) that reuses neighborhoods and SVD across points, reducing SVD calls from per-point to per-batch. The complexity analysis (Section 4) and the ablation study (Table 3) confirm that this batch-wise scheme achieves nearly identical accuracy while being substantially faster. The memory analysis using economy-size SVD is a practical consideration often overlooked in curvature-based methods.

4. **Clear relation to FOMA as a special case.** Section 4 explicitly shows that FOMA can be interpreted as a special case of CEMS (by replacing the Taylor-expansion sampling with simple scaling of normal components), which cleanly delineates what is new.

## Weaknesses

### Fatal
None.

### Major
None. No verified weakness invalidates the core claims of the paper.

### Minor

1. **Error in the complexity-analysis justification (Section 4).** The paper writes: "Using the manifold hypothesis, we assume that $d\ll D$ therefore $d\in\mathcal{O}(D^{2})$" (line 102). This is not a valid inference. If $d\ll D$, then $d=o(D)$, which does **not** imply $d\in\mathcal{O}(D^{2})$ in any meaningful sense — the stated relationship is vacuously true but doesn't follow from the premise. The intended reasoning (likely that the least-squares term $O(b^{2}d^{2})$ becomes $O(b^{2}D)$ when $d$ scales as $O(\sqrt{D})$) needs to be restated correctly. While the **final** complexity claim $O(b^{2}D)$ is plausibly correct under standard manifold assumptions, the argument given to reach it is logically broken and needs fixing.

2. **Overstated theoretical novelty.** The paper claims to "provide the fundamental theory" (abstract) and "foundational theory and practice" (contribution 1) for manifold sampling. However, Theorem 4.1 (Section 4.1) — the only formal theoretical result — is a standard Taylor-series error bound explicitly cited from Fowkes et al. (2013). It is a textbook result applied to motivate the method, not a novel theoretical contribution. The paper should honestly frame itself as an algorithmic/practical contribution, which is where its real value lies.

3. **No sensitivity analysis for key hyperparameters.** CEMS depends on the neighborhood size $k$, the sampling variance $\sigma$, and the estimated intrinsic dimension $d$. None of these are ablated in the main experiments. The paper notes that $d$ is estimated via a robust estimator (Facco et al., 2017) but does not report the estimated values per dataset or test sensitivity to this choice. Similarly, the values of $k$ and $\sigma$ are not analyzed. A reader cannot assess how robust the method is to these choices. (The only ablation provided — Table 3 — compares per-point vs. per-neighborhood basis computation, which is about efficiency, not hyperparameter sensitivity.)

4. **"Fully-differentiable" claim is technically inaccurate.** The paper describes CEMS as "fully-differentiable" (contributions, line 20; conclusion). However, the pipeline includes a $k$-nearest-neighbors step (Algorithm 1, step 1), which is a discrete, non-differentiable operation. The paper cites Ionescu et al. (2015) for differentiable SVD, but this does not make the kNN selection differentiable, and the method does not actually exploit differentiability to learn hyperparameters via gradients. This claim should be removed or qualified.

### Trivial

1. **Abstract overstates "superior" performance.** The abstract claims CEMS "is superior in in-distribution and out-of-distribution tasks," but on Electricity (Table 1) and RCF (Table 2), FOMA achieves lower error. The contribution list (line 21) more accurately says "competitive or even surpasses," which is the right characterization. The abstract should be toned down to match.

2. **Sine example (Figure 1) is qualitative only.** The toy example visually illustrates the advantage of second-order sampling but provides no quantitative measure (e.g., mean distance of sampled points to the true manifold). A quantitative comparison would strengthen the qualitative claim.

## Nice-to-Haves

- **Wall-clock timing comparisons.** The paper claims "mild computational overhead" but reports only asymptotic complexity. Per-epoch runtime comparisons against FOMA and other baselines would substantiate this claim.
- **Statistical significance tests.** Results are reported as averages over 3 seeds (with standard deviations in Appendix H). Simple paired tests (e.g., corrected t-tests across seeds) would help readers judge whether the observed differences are meaningful.
- **Comparison with a simple additive Gaussian noise baseline.** Adding Gaussian noise to inputs or outputs is a trivial domain-independent baseline for regression DA. Comparing against it would contextualize the benefit of manifold-based geometry.
- **Report estimated intrinsic dimensions** used for each dataset and test sensitivity to $k$ (neighborhood size) and $\sigma$ (sampling variance) over a reasonable range.

## Removed Points

- **"Marginal and inconsistent empirical gains" claim**: REMOVED. This mischaracterizes the results. CEMS is consistently top-2 on all 9 datasets — that is remarkably consistent. The paper's own characterization ("competitive or surpasses") is accurate. The abstract's "superior" is slightly overstated but the overall empirical pattern is a strength, not a weakness.
- **Missing Eq. 2 / Eq. 9 in main text**: REMOVED. These equations are in the appendix, which was stripped by the parser. The main text gives a textual description sufficient for following the method.
- **Strength about "differentiable pipeline" from Strength Finder**: REMOVED because it conflicts with the verified weakness that kNN is non-differentiable. Per rules, the weakness wins.
- **Criticism that method "relies on CAML"**: REMOVED. The paper explicitly cites and builds on CAML (Li, 2018). Building on prior work is standard practice, not a weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Fix the complexity analysis in Section 4: replace the incorrect inference "$d\ll D$ therefore $d\in\mathcal{O}(D^{2})$" with the correct reasoning. If the intended point is that $d^{2} = O(D)$ (so the least-squares term becomes $O(b^{2}D)$), state it explicitly. If the point is simply that $d\ll D$ makes $d$ small enough that the $O(b^{2}d^{2})$ term is negligible compared to $O(b^{2}D)$, state that instead.
2. Remove or qualify the "fully-differentiable" claim. Either acknowledge the kNN step is discrete, or restrict the claim to the differentiable components (SVD, least-squares, sampling).
3. Tone down the abstract to match the empirical evidence ("competitive with and often surpassing SOTA" rather than "superior").
4. Add a brief sensitivity study for $k$ and $\sigma$ on at least one representative dataset to demonstrate robustness.

## Score and Decision

The paper makes a clear algorithmic contribution (extending first-order manifold sampling to second-order with curvature), supports it with consistently strong empirical results across 9 benchmarks, and provides practical efficiency optimizations. The weaknesses are all addressable: one logical error in the complexity justification, overclaimed framing (theory novelty, "fully-differentiable," abstract's "superior"), and missing sensitivity analysis. None threaten the core contribution. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>