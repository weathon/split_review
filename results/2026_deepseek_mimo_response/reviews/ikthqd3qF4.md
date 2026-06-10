Now I have all the calibration data I need. Let me write the final review.

## Summary
This paper derives observable lower bounds on precision and relative recall for unsupervised record linkage by exploiting a structural constraint that limits positive outcomes per individual (e.g., at most one first-lien mortgage origination). The key insight is that the rate of multiple originations within predicted clusters bounds the false positive rate. The authors demonstrate this framework with hierarchical agglomerative clustering on 65.5 million HMDA mortgage applications, identifying ~314K cross-applicants with an estimated precision lower bound of 92.3%.

## Strengths
- **Novel theoretical contribution — observable precision bounds from structural constraints (Theorem 1, Section 2.2):** The derivation that Pr[False] ≤ Pr[Mult]/p² depends only on observables (empirical origination rate and fraction of clusters with multiple originations) and requires no labeled data. The proof sketch is intuitive and the bound is clean. This is a genuinely clever insight with broad applicability.

- **Simulation convincingly validates bound tightness (Section 3, Figures 3a vs 4a):** The simulation with known ground-truth shows close correspondence between true precision (~95%) and the bound-based estimate (93.7%) at ε=0.06, demonstrating the bound is tight enough for practical model selection. The comparison between "with date" and "without date" covariates effectively demonstrates how the bound responds to covariate informativeness.

- **Domain- and method-agnostic framework (Sections 1-2):** The framework requires only three structural features and applies to any label-generating algorithm. The explicit connections to insurance, college admissions, and job offers demonstrate genuine breadth. Theorem 1 is stated for general predicted labels, enabling cross-model comparison and hyperparameter tuning.

- **Principled precision-recall trade-off optimization without labels (Corollaries 1-2, Figure 5):** The extension to recall bounds, weighted precision-recall scores, and Fβ-scores via observable quantities enables principled parameter selection. Figure 5's frontier with the "knee" point selection is a concrete demonstration of theory driving practical decisions.

- **Large-scale real-world application with policy relevance (Section 4):** The application to 65.5 million HMDA applications with 96 parameter combinations demonstrates scalability and produces concrete, policy-relevant outputs. The connections to fairness measurement (Elzayn et al., 2025), lending standards monitoring, and shopping behavior analysis ground the methodology in economically meaningful questions.

## Weaknesses

### Fatal
None.

### Major
- **Restriction to size-2 clusters undermines generality claim and discards signal (Footnote 4, line 186):** The paper drops all clusters with more than two applications, meaning individuals who file 3+ applications (potentially the most important cross-applicants) have their entire cluster discarded. The justification ("to keep the discussion as simple as possible") is insufficient given the cost. More importantly, for size-2 clusters, Theorem 1 becomes an exact equality under the assumption Pr[Mult|False] = p² (Remark 1, line 136), making Assumption 2 unnecessary for the results actually used. The paper presents Assumptions 1 and 2 and a general theory but only demonstrates the simplest special case. Showing that the general bound remains informative for clusters of size 3+ would substantially strengthen the generality claim.

- **92.3% precision consistently conflated with a point estimate rather than a lower bound:** The abstract states "92.3% precision" without qualification. The conclusion says "achieving an estimated precision of 92.3%." Section 4 states "estimate that 92.3% are true cross-applicants." Since this quantity is derived as a lower bound from the model's own outputs via Theorem 1 — with no external ground truth in the real application — it should consistently be qualified as "at least 92.3%." Additionally, no confidence intervals or bootstrap standard errors are provided for this estimate despite it relying on empirical estimates of p̂ and p̂_m.

### Minor
- **Notation inconsistency in Equations (1)-(2) (lines 142-146):** The text preceding Eq. (1) says "This yields a new lower bound on the precision of our algorithm," but Eq. (1) writes Pr[False] ≥ ..., which is a lower bound on the *false positive rate*, not on precision. The RHS actually equals the lower bound on precision (confirmed by the mathematical derivation: precision ≥ (1 - Pr[Mult]/p²)/(1 - Pr[Mult])). Similarly, Eq. (2) defines α̂(θ) with Pr[False] ≥ α̂(θ), but line 148 says α̂(θ) is "the lower bound on precision." The mathematical content is correct but the labeling will confuse readers.

- **No sensitivity analysis on partitioning variables (Section 4.1):** The 9 categorical partitioning variables determine which applications are candidates for clustering, yet there is no analysis of how robust the 92.3% bound is to excluding individual variables. This matters for practitioners choosing variables.

- **No discussion of structural constraint violations:** The framework assumes each individual originates at most one first-lien mortgage. If borrowers take out a first mortgage plus a second mortgage or HELOC, the foundational assumption Pr[Mult|¬False] = 0 breaks down. The paper should discuss sensitivity to such violations.

### Trivial
- No wall-clock runtime or scalability analysis for the 65.5M application dataset.

## Nice-to-Haves
- Bootstrap confidence intervals for the empirical 92.3% precision bound would strengthen the empirical claim substantially.
- Demonstrating the general bound on clusters of size 3+ would recover lost signal and validate the full theory.
- Analysis of which distance components matter most among the 96 combinations would aid practitioners.

## Removed Points
These points are flagged to be removed, treat them with caution:
- No points were removed; all reviewer concerns were retained, demoted, or elevated as appropriate.

## Novel Insights
The paper's genuinely novel insight is that structural constraints limiting positive outcomes per individual create an observable signature (multi-origination rate in predicted clusters) that directly bounds the false positive rate — without any labeled data. This transforms an impossible evaluation problem into a tractable one by exploiting domain knowledge about the data-generating process. The tight correspondence between the bound and true precision in simulation (93.7% vs ~95%) validates this as a practical tool, not just a theoretical curiosity. This idea — that domain-specific structural constraints can substitute for labels in evaluation — is potentially applicable well beyond mortgage data.

## Suggestions
- Add bootstrap confidence intervals for the 92.3% empirical precision bound.
- Consistently qualify the 92.3% as "at least 92.3%" throughout the paper.
- Fix Eqs. (1)-(2) to correctly label the LHS as precision or flip the inequality for false positive rate.
- Demonstrate results on clusters of size 3+ or provide the empirical distribution of cluster sizes to quantify signal loss from the size-2 restriction.
- Add brief discussion of sensitivity when the "at most one origination" constraint is approximately violated.

---

## Calibration Report

**Anchors retrieved across all rounds:**

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | AAZ3vwyQ4X (Multimodal Structure Preservation) | 2.50 | Much weaker — general unsupervised learning, rejected for unclear contribution |
| 1 | yNyDvFQNEm (Network-Aware Embeddings) | 3.40 | Much weaker — rejected, unclear methodological contribution |
| 1 | oyFCgkkLUK (αMax-B-CUBED) | 4.75 | Weaker — small-scale experiments, unclear practical significance |
| 1 | f9RvYpXhFI (Fréchet bounds for PWS) | 5.50 | Most comparable in spirit; our paper has cleaner theory and 1000x larger application |
| 1 | HvkXPQhQvv (SSME) | 6.00 | Similar goal (evaluating without labels); our paper has cleaner theory, no labeled data needed |
| 1 | Q3Foe1fDjh (Expected Probabilistic Hierarchies) | 6.00 | Comparable theory quality; our paper has more impactful application |
| 1 | yF19SY1i8M (Robust NLP Evaluation) | 6.00 | Less comparable topic; similar contribution level |
| 1 | NO6Tv6QcDs (LLM-as-judge limits) | 6.50 | Comparable theoretical contribution; our paper has larger application |
| 1 | falBlwUsIH (OOD detection without labels) | 6.33 | Similar theory quality; our paper is more constructive |
| 1 | RvUVMjfp8i (SSL evaluation) | 8.00 | Stronger — more established framework with broader experimental validation |
| 1 | KbetDM33YG (Online GNN evaluation) | 8.00 | Stronger — different domain, more comprehensive |
| 1 | EUSkm2sVJ6 (Data Usage Inference) | 7.60 | Stronger — more polished, better uncertainty quantification |
| 2 | icTZCUbtD6 (Sample Hardness) | 6.20 | Comparable contribution level |
| 2 | sZGZJhaNSe (Aioli data mixing) | 6.25 | Comparable contribution level |
| 2 | F64wTvQBum (Domain certification) | 6.75 | Slightly stronger — cleaner presentation, no notation issues |
| 2 | W2dR6rypBQ (Explainable OR) | 6.75 | Slightly stronger — broader framework |

**Round 1 bracket:** 5.5–7.5. The paper is clearly better than the Fréchet bounds paper (5.50, reject) which is the most topically similar, and comparable to the OOD detection (6.33) and LLM-as-judge (6.50) papers that were accepted.

**Round 2 narrowing:** 6.0–7.0. The paper sits above the rejected 6.0 papers (cleaner theory, larger application) and comparable to the accepted 6.25–6.50 papers. The size-2 restriction and notation issues prevent it from reaching 6.75+.

**Final score justification:** The paper has a genuinely novel theoretical insight that is clean, well-validated in simulation, and demonstrated at scale in a real-world application with policy relevance. Its contribution is clearly above the rejected papers in the 5.5–6.0 range and on par with accepted borderline papers at 6.3–6.5. The size-2 cluster restriction is a notable limitation that prevents the general theory from being tested, but does not invalidate the contribution for the practical case where it is applied. Score: 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>