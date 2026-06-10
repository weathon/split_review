## Summary

This paper introduces MOST, a framework for finding $m$ diverse Pareto-optimal solutions when there are $n \gg m$ objectives. The core idea is to formulate objective-to-solution assignment as an optimal transport (OT) problem with marginal constraints that enforce coverage (every objective covered) and balance (no model dominates). The result is a bi-level alternating algorithm that interleaves OT matching with a reweighted MGDA step per solution. Experiments on federated learning ($n=30,206$ clients vs $m=5$ models), multi-task learning, and mixture-of-prompt learning for LLMs show consistent improvements over baselines.

## Strengths

- **Principled matching mechanism via OT with marginal constraints.** The two simplex constraints ($\Gamma\vec{1}_m = \alpha$, $\Gamma^\top\vec{1}_n = \beta$, Eq.~obj:ot) directly encode coverage and balance — properties that prior reference-vector approaches lack in the $n\gg m$ regime. This is a clean and well-motivated formulation.

- **Convergence guarantee for the bi-level alternating algorithm.** Theorem 1 establishes an $O(\nu/T)$ convergence rate for the non-convex case under full-batch gradients, which matches standard gradient descent despite the alternating structure. This provides a theoretical grounding that many MOO papers lack.

- **Consistent and sizable empirical gains across three distinct application domains.** MOST outperforms all baselines on federated learning (Table 1, e.g., 84.25% vs 83.09% on Syn(0.0,0.0)), multi-task learning (Table 2, e.g., 82.98% vs 80.74% on Office-10), and mixture-of-prompt learning (Table 3, e.g., 67.03% vs 62.69% on BoolQ), with margins exceeding reported standard deviations.

- **Negligible computational overhead.** Runtime of MOST is comparable to MGDA and Linearization (Table 4, e.g., 217.59s vs 219.86s on Syn(0.0)), and OT accounts for less than 1% of total training time (line 409).

- **Empirical evidence of specialization.** The analysis in Section 5 shows $\Gamma$ converges to ~75% sparsity, and the oracle loss (best solution per objective) decreases while average loss rises — directly supporting the claim that solutions specialize to complementary subsets of objectives.

- **Practical curriculum strategy.** The progressive relaxation of marginal constraints (Section 3.3) addresses the training collapse problem where one model dominates all objectives. The ablation confirms this improves performance.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The multi-task learning experiments do not test the paper's claimed $n\gg m$ regime.** Office-Caltech10 has $n=4$ objectives and $m=4$ solutions ($n=m$), and DomainNet has $n=6$, $m=4$ ($n > m$ but not $n\gg m$). These are settings where reference-vector methods (which the paper argues "do not generalize well" to many objectives) are designed to work. This does not invalidate the paper, since the FL experiments ($n=30$, $m=5$; $n=206$, $m=5$) and prompt learning ($n=128$, $m=3$) properly test the $n\gg m$ regime. But calling all three application domains supportive of the core claim is overstated when one of them does not match the motivating setting.

- **Hypervolume is mentioned as an evaluation metric but never reported.** Section 5.1 (line 261) states that hypervolume is used "to measure diversity." No hypervolume results appear anywhere in the paper. Since hypervolume is the standard metric for Pareto front quality in MOO, its absence weakens the claim that MOST "profiles the entire Pareto frontier." The existing evidence (accuracy, tail accuracy, KL divergence) is informative but incomplete without the accepted MOO metric.

- **Ablation results are described in prose without quantitative support.** Section 6.5 reports that the curriculum boosts performance by "over 2.00%" and that OT-generated weights outperform random weights, but no table or figure with ablation numbers, standard deviations, or statistical comparisons is provided. This makes it impossible for a reader to independently assess the magnitude or reliability of each component's contribution.

- **Mismatch between the theoretical diversity definition and the empirical diversity measure.** Definition 1 (line 176–178) defines solution diversity via cosine similarity between columns of $\Gamma$. However, the empirical diversity measure used in the FL experiments (Figure 3b, line 315) is the KL divergence between *predictions* of different solutions. The paper does not explain why the empirical measure is appropriate or how it relates to the formal definition, creating a disconnect between theory and evaluation.

- **Convergence theory covers an idealized version of the algorithm.** Theorem 1 assumes full-batch gradients, and the paper acknowledges this gap (line 209) without analyzing whether guarantees degrade under mini-batch stochastic gradients and $K>1$ steps. While this is common practice in learning theory papers, the gap means the theory serves as a qualitative sanity check rather than a tight characterization of the practical algorithm.

### Trivial

- The prompt learning application treats each training *instance* as a separate objective ($n=128$, $m=3$), which stretches the usual meaning of "objectives" (typically conflicting criteria like accuracy vs fairness). This is acknowledged by the authors but the framing is unusual.

## Nice-to-Haves

- Including personalized FL baselines (e.g., pFedMe, Smith et al.) would strengthen the FL comparisons, though the current baselines (FedAvg, FedProx, FedMGDA+) are already reasonable.
- Reporting statistical significance or confidence intervals for the main results would strengthen the quantitative claims.
- Clarifying which value of $m$ was used for the FEMNIST FL experiments (the paper only states $n=206$, not $m$).

## Removed Points

The following criticisms from the inputs were removed for the stated reasons:

1. **R($\Gamma$) differentiability concern** — The paper's use of subgradients for the $\max$ term in $R(\Gamma)$ is standard; there is no actual technical gap here.
2. **Proposition 1 is a known result** — The paper explicitly cites Brualdi (2006) for this property; it is not claimed as a novel contribution.
3. **Missing personalized FL baselines** — The chosen baselines are standard and reasonable; demanding additional baselines is scope creep.
4. **MOSTE extension not evaluated** — Results may appear in the appendix, which is stripped by the parser. Per instructions, absent appendix content should not be treated as missing.
5. **Strongly-convex convergence claim lacking formal theorem** — Formal statement may reside in the appendix.
6. **Model architecture details absent** — Not a meaningful weakness for this paper; architecture choices are conventional.
7. **Statistical significance not reported** — Standard in this community; nice-to-have but not a weakness.
8. **"Assignment dynamics on a single synthetic dataset with no details"** — The paper does provide details in Section 5 with Figure 2 and discusses the setup.
9. **"Stretches the framing" for prompt learning** — The paper acknowledges the unusual framing; it is a design choice, not an error.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's theoretical framing of diversity (cosine similarity of $\Gamma$ columns) and the empirical proxy used to measure it (KL divergence of solution predictions). The paper would benefit from either reconciling these or explicitly justifying why the empirical measure is appropriate. Additionally, the fact that OT accounts for <1% of runtime while providing the core matching mechanism is a practically valuable detail — it suggests the framework is deployable even at scale, where other OT-based methods often bottleneck.

## Suggestions

1. Replace or supplement the MTL experiments (Office-Caltech10, DomainNet) with a genuinely large-$n$ multi-task benchmark to directly test the $n\gg m$ regime.
2. Report hypervolume results for the FL and prompt-learning experiments, or remove the claim that hypervolume is used.
3. Provide a proper ablation table (mean and std) for each component: full MOST, MOST without $R(\Gamma)$, MOST with random weights instead of OT, MOST without curriculum.
4. Acknowledge the gap between Definition 1 (cosine similarity of $\Gamma$ columns) and the empirical diversity measure (KL divergence of predictions), or align them.
5. Clarify the value of $m$ used for the FEMNIST experiments.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>