Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper identifies a genuine problem: existing optimizers for LoRA fine-tuning lack transformation invariance, meaning the update to the low-rank weight matrix depends on the arbitrary parameterization of the two LoRA factors. The authors propose LoRA-RITE, which achieves transformation invariance through unmagnified gradients combined with one-sided matrix preconditioning on the rank-\(r\) side, keeping per-step complexity at \(\mathcal{O}(mr^2+nr^2+r^3)\) and memory \(\mathcal{O}(mr+nr)\). The method consistently outperforms Adam, LoRA+, ScaledAdam, Shampoo, and Lamb across Super-Natural Instructions and four LLM benchmarks (HellaSwag, ArcChallenge, GSM8K, OpenBookQA) on Gemma-2B, Gemma-7B, and mT5-XXL, with particularly large gains on GSM8K (e.g., 55.50% vs. Adam's 48.37% on Gemma-7B).

## Strengths

1. **Clear problem diagnosis with formal motivation.** Section 2 mathematically demonstrates that neither gradient descent nor Adam satisfies scalar scale invariance for LoRA (Eqs. 11–15, 20–25), and Section 3.1 proves that diagonal preconditioners cannot achieve full transformation invariance (Eq. 26). This provides a rigorous foundation justifying the need for matrix preconditioning — a diagnostic contribution that is independently useful.

2. **Novel and efficient algorithm design.** The core idea of using unmagnified gradients (Eq. 7) with one-sided matrix preconditioning on the rank-\(r\) side is novel and clean. The method provably achieves transformation invariance for the simplified update (Eq. 8, lines 259–266) while maintaining complexity comparable to first-order methods when \(r \ll m,n\). Table 5 confirms the practical overhead is only 5–8% over Adam.

3. **Consistent and substantial empirical gains across diverse settings.** The improvements are not isolated to one configuration. LoRA-RITE outperforms all baselines on every dataset, every model size (2B, 7B, XXL), and every rank tested (4 and 16). On Gemma-7B across four LLM benchmarks, average accuracy rises from 68.71% (Adam) to 76.91% — an 8.2% absolute gain. The pattern that Lamb (scalar-scale-invariant) is consistently second-best provides indirect evidence that stronger invariance properties matter.

4. **Theoretical convergence bound with an advantage under imbalance.** Theorem 4 derives a regret bound of \(\mathcal{O}(G D_A D_B T^{-1/2})\), which is tighter than the \(\mathcal{O}(G(D_A^2+D_B^2)T^{-1/2})\) bound of one-sided matrix Adagrad when \(D_A \neq D_B\) — a condition that Figure 1 confirms occurs in practice. While the analysis uses a simplified setting (no first moment, Adagrad-style sum of squares rather than EMA), this follows standard practice in the optimization literature.

## Weaknesses

### Fatal
None.

### Major

1. **The transformation-invariance claim for the full algorithm is asserted without complete proof.** The paper provides a clear algebraic demonstration of invariance for the update *without* accumulated first/second moments (Eq. 8, lines 259–266). However, when moments are incorporated with basis projection (\(\mathbf{P}_{\mathbf{A}_t}\)) and escaped mass (\(\rho_{\mathbf{A}_t}\)), Theorem 2 (line 336–339) simply asserts that "every unmagnified term is consistent" and concludes invariance without a step-by-step verification. The paper describes the mechanism (projection transforms accumulated moments to the new basis; escaped mass compensates for information loss), which is plausible and principled, but a full proof showing that \(\delta\mathbf{A}_1\mathbf{B}_1^\top = \delta\mathbf{A}_2\mathbf{B}_2^\top\) for the complete update with moments is not provided. Given that transformation invariance is the paper's central theoretical contribution, this gap is significant. The paper would be stronger with either a complete proof or an honest characterization of what weaker invariance property the practical algorithm satisfies.

2. **The convergence analysis is disconnected from the implemented algorithm.** The paper explicitly states it analyzes a simplified scenario "where the first moment is omitted and the second moment is a summation, similar to Adagrad" (line 362), while the actual LoRA-RITE uses EMA-style second moments and a first moment. Theorem 3 bounds a non-standard quantity \((\frac{1}{T}\sum_t \frac{1}{\eta}\nabla\boldsymbol{\theta}_t^\top(\boldsymbol{\theta}_t-\boldsymbol{\theta}_{t+1}))\) rather than standard regret. The stronger bound (Theorem 4, \(\mathcal{O}(G D_A D_B T^{-1/2})\)) requires Assumption 1, whose practical validity is not empirically verified. While this level of analysis is common in optimization papers, the gap means the theory does not convincingly explain the empirical success of the actual algorithm.

### Minor

1. **Results are reported without variance estimates.** All tables report single numbers without standard deviations, confidence intervals, or evidence from multiple seeds. LLM fine-tuning can exhibit non-trivial run-to-run variability. The consistent cross-benchmark pattern somewhat mitigates this concern, but basic error bars on a representative subset (e.g., one model on one benchmark with 3 seeds) would substantially increase confidence. This is a standard limitation for large-scale LLM fine-tuning experiments, but it should be acknowledged.

2. **The Limitations section discusses limitations of LoRA, not of LoRA-RITE.** Lines 578–579 describe inherent limitations of the LoRA method itself (reduced representational power, rank selection difficulty), but do not address limitations of the proposed optimizer — for example, the potential numerical sensitivity of QR decompositions, the additional hyperparameters introduced (\(\beta_1, \beta_2\), escaped-mass accumulation), or sensitivity to the escaped-mass heuristic. Acknowledging these would strengthen the paper.

### Trivial

- The phrasing "It is only \(r\) times slower than Adam" (line 341) is technically correct for the optimizer step alone but could mislead readers; the actual wall-clock overhead is only 5–8% because backpropagation dominates. The paper does provide the clarifying context immediately ("this overhead is negligible when comparing with the back-propagating time"), so this is a presentation polish issue rather than a real error.

## Nice-to-Haves

- An ablation study comparing LoRA-RITE with and without the escaped-mass correction (\(\rho_{\mathbf{A}_t}\)) would clarify whether this heuristic is necessary for the empirical gains.
- A few additional seeds (e.g., 3 runs on one representative benchmark like OpenBookQA with Gemma-2B) with mean and standard deviation would greatly improve credibility.
- A proof sketch or lemma-level argument for the invariance of the full algorithm (with moments, projection, and escaped mass) would resolve the main theoretical concern.
- An analysis of training dynamics (weight norm plots for both LoRA factors) under LoRA-RITE, analogous to Figure 1 shown for baselines, would directly demonstrate that the method balances updates across factors.

## Removed Points

These points from the reviewers were evaluated and removed with justification:

- **"The speed comparison should be explained; the text says 'it is only r times slower' without nuance."** The paper *does* include the clarifier: "since \(r\) is very small, this overhead is negligible when comparing with the back-propagating time" (line 341). The explanation is present, so this criticism is not accurate as stated.

- **"Missing comparison to Riemannian gradient descent."** The paper explicitly discusses RGD (lines 429–432), noting that it lacks momentum and adaptivity and performs worse than Adam in existing experiments. Including it as a baseline would add little information and is scope creep given the existing baseline set (Adam, LoRA+, ScaledAdam, Shampoo, Lamb).

- **"Missing results on more model families (Llama, GPT)."** This demands breadth beyond the paper's scope. The paper already evaluates on Gemma (2B, 7B) and mT5-XXL, covering both decoder-only and encoder-decoder architectures across two orders of magnitude in parameter count.

- **Generic strengths from Strength Finder:** Some claimed strengths (e.g., "addresses an important problem") are dropped as generic. The strengths listed above are the specific, evidence-backed ones.

## Novel Insights

The most interesting observation emerging from cross-referencing the reviews is that Lamb (scalar-scale-invariant) consistently ranks second-best behind LoRA-RITE (fully transformation-invariant), and the gap between them widens on harder tasks (GSM8K: LoRA-RITE 55.50% vs. Lamb 50.64% on Gemma-7B). This provides the first empirical evidence I am aware of that *full* matrix-transformation invariance confers benefits beyond scalar-scale invariance — a finding that helps disentangle which invariance properties matter in practice. The paper itself notes this relation (lines 518–519) but does not fully develop the point; it deserves more emphasis.

## Suggestions

1. Provide a complete proof or at least a detailed sketch showing that the update \(\delta\mathbf{A}_t\mathbf{B}_t^\top\) (Eq. 11, with moments, projection, and escaped mass) is identical for any equivalent pair \((\mathbf{A}_1,\mathbf{B}_1), (\mathbf{A}_2,\mathbf{B}_2)\). Alternatively, honestly characterize what invariance property the practical algorithm satisfies if the full property does not hold.

2. Add standard deviations for at least one representative setting (e.g., OpenBookQA, Gemma-2B, 3 seeds) to the main results.

3. Include an ablation of the escaped-mass mechanism and report default hyperparameter values with a sensitivity analysis.

4. Move the Limitations section to discuss LoRA-RITE's own limitations (e.g., reliance on QR decomposition, untested escaped-mass heuristic, extra hyperparameters).

## Score and Decision

The paper makes a genuine contribution: the problem is well-motivated, the algorithm is novel and principled, and the empirical results are consistently strong across a diverse evaluation suite. The two major weaknesses — the incomplete invariance proof for the full algorithm and the gap between the convergence theory and the implemented method — are real but not fatal; they reflect a level of theoretical rigor that falls short of the paper's ambitions rather than invalidating the core contribution. The empirical evidence is the strongest pillar, and it stands even if the theory is only partial. With revisions addressing the invariance proof, basic error bars, and the escaped-mass ablation, this would be a strong paper.

**Score:** 6.5

**Decision:** Accept

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>