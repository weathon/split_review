Now I have everything I need. Let me write the final consolidated review.

## Summary

This paper derives observable lower bounds on precision and relative recall for unsupervised anonymous record linkage by exploiting a structural constraint (e.g., an individual can originate at most one first-lien mortgage). The bounds depend only on the origination rate and the fraction of clusters with multiple originations, requiring no ground-truth labels. The method is demonstrated on 65.5M HMDA mortgage records using agglomerative clustering, achieving an estimated 92.3% precision at the preferred specification. The paper is a methodological contribution with an empirical illustration.

## Strengths

- **Derivation of an observable precision bound (Theorem 1).** Section 2.2 proves that precision is at least \(1 - \Pr[\text{Mult}]/p^2\) using only the rate of clusters with multiple originations and the overall origination probability. This bound requires no ground-truth labels and is the paper's central theoretical contribution. The bound is novel — to my knowledge, the first work to derive such observable bounds for unsupervised record linkage — and its reliance on a widely applicable structural constraint (at-most-one positive outcome per individual) makes it domain-agnostic.

- **Compelling simulation validation.** In Section 3.1, the bound closely matches true precision across tuning parameters. For the "with date" specification at \(\varepsilon=0.06\), the bound gives 93.7% while true precision is ~95%, demonstrating the bound is both valid and practically tight (Figures 3a vs. 4a).

- **Large-scale real-world application.** The method is demonstrated on 65.5M HMDA applications (Section 4). The preferred specification identifies 314,344 cross-applicant clusters at an estimated 92.3% precision. This shows the method works at scale on real data and connects to important applications in fair lending and mortgage market analysis.

- **Domain- and method-agnostic framework.** The bounds apply to any label-generating algorithm, not just the clustering instantiation used here. Section 1 lists four other domains (secured loans, insurance, college admissions, job applications) where the same structural constraint holds, making the framework broadly applicable.

## Weaknesses

### Fatal

None.

### Major

- **Equation (1)–(2) inconsistency between the algebraic expression and its interpretation.** The text states: "This yields a new lower bound on the precision of our algorithm" and then writes  
  \(\Pr[\text{False}] \geq \frac{1 - \Pr[\text{Mult}]/p^2}{1 - \Pr[\text{Mult}]}\) (Equation 1).  
  If \(\Pr[\text{False}]\) on the left is the false positive rate (as defined earlier in the paper), then precision = \(1 - \Pr[\text{False}]\), so the inequality gives precision \(\leq 1 -\) RHS — an **upper** bound on precision, not a lower bound. Yet the empirical estimator \(\hat{\alpha}(\theta)\) is correctly treated as a lower bound on precision throughout the simulation (Figure 4) and application (Figure 5), and the simulation confirms it functions as a lower bound. The equation as written is inconsistent with its interpretation and with the empirical usage. This is a presentation error that must be corrected — the left side of (1) and (2) should likely read "Precision" rather than \(\Pr[\text{False}]\). The underlying math is sound (as shown by the simulation), but the formalism is wrong, and a careful reader cannot determine which quantity is being bounded from the equations alone.

- **No comparison to alternative methods in the HMDA application.** The paper's contribution is the bounds themselves, which are method-agnostic. However, the empirical illustration would be far more convincing if it showed that the bound correctly ranks different clustering choices or a simple alternative (e.g., a single-linkage baseline or a naive distance threshold). Without any baseline, the 92.3% figure is informative but the reader cannot assess whether this represents good performance or is merely an artifact of the specific algorithm.

### Minor

- **Restriction to size-2 clusters is not quantified.** Footnote 4 states that all clusters with more than two applications are dropped, but the paper does not report how many such clusters exist in the data or how this affects the generalizability of the empirical findings. The theoretical bounds are stated generally, but only size-2 clusters are tested, leaving unclear whether and how the bounds extend to larger clusters.

- **No robustness checks on Assumptions 1 and 2.** Assumption 1 (independence across borrowers) and Assumption 2 (monotone origination probability) are stated and used to derive the bound, but the paper provides no sensitivity analysis or stress tests. The simulation uses the same structural constraint as the bound, so it verifies the math rather than testing robustness to assumption violations. A discussion of the direction and magnitude of bias under plausible violations (e.g., correlated origination due to local economic shocks) would strengthen the paper.

- **No uncertainty quantification.** The precision estimate of 92.3% is reported as a point estimate without confidence intervals. Given the massive dataset, even simple bootstrap standard errors would help assess reliability.

### Trivial

None.

## Nice-to-Haves

- A small hand-labeled validation sample (e.g., 500 clusters checked against external data) would directly validate the bound's calibration on real HMDA data, addressing the otherwise unverifiable real-world plausibility.
- A comparison to one or two alternative clustering methods (e.g., DBSCAN or a simpler distance threshold) would demonstrate that the bound can be used for principled model selection.
- A brief discussion situating the proposed evaluation framework relative to existing unsupervised evaluation practices (Fellegi-Sunter model, synthetic data evaluation, holdout-set methods) would help clarify the novelty.
- Confidence intervals on the precision estimate via bootstrapping would improve the statistical credibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Absence of comparison to existing record-linkage methods" (harsh critic Issue 2, framed as major).** The paper's contribution is the bounds themselves, not the clustering algorithm. The bounds are the evaluation framework, and the clustering algorithm is only an instantiation. While a baseline comparison would strengthen the empirical section, the paper's core claim — that the bounds are observable and useful — does not depend on such a comparison. The critic's demand for a full survey of Fellegi-Sunter and probabilistic linkage methods is scope creep; the paper is not a record-linkage paper but a methodological contribution about evaluation bounds. Moved to Nice-to-Haves.

- **"Lack of real-world validation of HMDA results" (harsh critic Issue 3).** The paper explicitly states that "additional diagnostics to validate that the clusters truly correspond to cross-applicants" are in the Appendix. The parser strips appendices from all papers; that content exists in the original submission. Per the review rules, criticisms about missing appendix content are not valid.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix equations (1)–(2)** by either changing the left side to "Precision" (i.e., replacing \(\Pr[\text{False}]\) with Precision) or adjusting the inequality and variable definitions to be internally consistent. Ensure the formalism matches the empirical usage throughout.
2. **Add at least one baseline method** to the HMDA demonstration — even a simple single-linkage or fixed-threshold approach — to show that the bound correctly identifies the better method. This would directly validate the claim that the bounds enable model comparison.
3. **Report the number of size>2 clusters dropped** in both the simulation and application, and discuss whether the method could be extended to larger clusters.
4. **Add a simulation stress test** that violates Assumption 1 (e.g., correlated origination) or Assumption 2 to characterize the direction and magnitude of bias in the bound.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| Fréchet bounds for PWS (f9RvYpXhFI) | 5.50 | R1 | Less clean bound derivation, weaker validation; this paper is stronger |
| αMax-B-CUBED (oyFCgkkLUK) | 4.75 | R1 | Much weaker experiments and presentation; this paper is clearly stronger |
| Constrained PDE learning (5KqveQdXiZ) | 5.25 | R1 | Different topic; comparable overall quality |
| SSME model evaluation (HvkXPQhQvv) | 6.00 | R2 | Broader experiments but weaker theory; this paper is comparable |
| Weak labelers as constraints (2BtFKEeMGo) | 6.50 | R2 | More comprehensive empirical evaluation; this paper is slightly weaker |
| Limits to scalable evaluation (NO6Tv6QcDs) | 6.50 | R2 | Different topic, strong theory; this paper is comparable in theoretical contribution |
| SSL generalization theory (RvUVMjfp8i) | 8.00 | R1 | Very different topic, much stronger empirical/theoretical package; this paper is notably weaker |

**Round-1 bracket:** [4.5, 7.0]  
**Round-2 narrowing:** The closest methodological anchor (Fréchet bounds, 5.50) is weaker; the closest quality anchor (SSME, 6.00) is comparable but with different weaknesses. This paper's theoretical contribution is stronger than SSME's, but the equation error and lack of baselines hold it back. I place it above the Fréchet bounds paper and at parity with SSME.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>