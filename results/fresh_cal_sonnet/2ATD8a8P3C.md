Now I have a thorough understanding of the paper. Let me do the calibration searches.Initial bracket: **4–6.5**. The paper is clearly above the weak anchors (2.5–3) given its theoretical contributions, but below the 7.0 "Conformal Risk Control" anchor given its experimental limitations and proof error. Let me narrow.Now let me read a couple of the most relevant anchors fully to sharpen the comparison.Now I have enough information to write the full review. Let me synthesize everything carefully.

---

## Summary

This paper proposes a general framework for conformal prediction on structured output spaces, where prediction sets are implicitly defined over a space of structured representations (e.g., nodes in a directed acyclic graph). The framework adapts the learn-then-test sequential search to handle non-monotone coverage, extends to PAC (training-conditional) coverage guarantees, and provides an integer programming formulation for DAG-structured prediction sets. Three empirical domains (MNIST digit numbers, hierarchical ImageNet, SQuAD year-QA) are used to validate that coverage guarantees hold.

---

## Strengths

- **First general framework for conformal prediction on structured label spaces.** Section 3 unifies and generalizes prior domain-specific work (Khakhar et al. on partial programs, Mohri et al. on QA) by providing a search over thresholds τ with a plug-in statistical test φ applicable to any structured label space. The related-work section explicitly places this as a first-of-its-kind generalization.

- **Genuine extension of learn-then-test to PAC coverage guarantees.** Theorem 2 and the φ_PAC statistical test provide a novel PAC (training-conditional) coverage guarantee in the structured setting. The paper correctly notes (Section 1, related work) that it is "the first to adapt these techniques to provide PAC guarantees" for structured prediction, and this claim is supported by the proof in Section 3.

- **Concrete and practically usable integer programming formulation.** Section 4 presents a well-specified integer program (Equations 7–12) that solves the DAG-structured optimization problem. The constraints encode coverage propagation through the DAG, and the formulation handles both hierarchical classification and interval-union prediction sets within a single framework.

- **Non-monotone coverage handled via sequential search.** The paper correctly identifies (Section 1) that coverage is not monotone in τ for structured sets and adapts the learn-then-test sequential search to this setting — a non-trivial algorithmic adjustment enabling broader applicability than traditional threshold-based conformal methods.

---

## Weaknesses

### Fatal
None.

### Major

- **Error in the stated justification of the PAC proof.** In the proof of Theorem 2, line 147 states: "the first inequality follows since the CDF of the Binomial(n,p) is monotonically decreasing in p and μ ≤ ε." However, line 132 of the same proof explicitly establishes that "since τ₀ is invalid, we have μ > ε." The stated reason "μ ≤ ε" directly contradicts the proof's own setup. The correct justification is: since μ > ε and the binomial CDF is monotonically decreasing in p, F(ℓ̂; n, μ) ≤ F(ℓ̂; n, ε) < δ. The final inequality F(ℓ̂; n, ε) < δ is correct and the theorem's conclusion is mathematically sound, but the stated justification as written contains a logical inversion that must be fixed.

- **No quantitative baseline comparison undermines the paper's core empirical claim.** The paper's stated contribution is that structured prediction sets produce *more interpretable* representations *while maintaining coverage*. However, experiments only confirm that coverage holds — something guaranteed by the theory regardless. No comparison against flat conformal prediction (e.g., APS/RAPS on fine-grained labels) is provided. The single qualitative example in Table 1 actually illustrates the difficulty of this claim: at m=4, ε=0.1, the structured set {[1997], [1979], [2007], [2015–2019]} covers 8 concrete years (1979, 1997, 2007, 2015–2019), while the standard conformal set {1979, 1997, 2007, 2016, 2017, 2019} covers only 6 years. The structured representation is more compact *syntactically* but covers *more* concrete labels. This tradeoff is precisely the paper's thesis and it is never framed, quantified, or compared systematically across any domain. Without this, the interpretability claim is asserted but not demonstrated.

### Minor

- **Text generation over-promised in the abstract.** The abstract motivates the framework with "complex structured outputs such as text generation," and the introduction similarly invokes text generation as a target application. However, text generation is never formalized within the framework or evaluated in experiments; it appears only as a future direction in the conclusion. The framing should be narrowed to match what the paper actually delivers.

- **Asymmetric main-text experimental coverage.** The paper advertises three evaluation domains (MNIST, ImageNet, SQuAD) but the main text (Section 5, Results) discusses only SQuAD. MNIST and ImageNet results appear only in appendix figures without main-text discussion. For a paper that centers these three domains in its abstract and contributions, readers cannot evaluate those results from the main paper alone.

- **Small SQuAD dataset limits statistical weight.** The SQuAD subset contains 262 examples total (131 calibration / 131 test), and the underlying model achieves only ~33.2% accuracy on year extraction. The reported standard deviations across 5 seeds carry limited statistical weight at this scale. The large prediction set sizes may reflect poor model calibration rather than structural properties of the method.

- **No guidance on choosing m in practice.** The hyperparameter m significantly affects both prediction set structure and size (as demonstrated in Figures 3–4) but no principled guidance is given for how to select it. Since m cannot be tuned on the test set, this is a real practical question the paper leaves entirely open.

### Trivial

- **Candidate threshold set T is unspecified.** Section 3 introduces a "finite set of candidate thresholds T ⊆ ℝ" and assumes it is ordered, but never specifies how T is constructed in practice. Standard conformal prediction derives thresholds from calibration scores; clarifying this would improve reproducibility.

- **Computational cost of the integer program is unaddressed.** For large DAGs (e.g., the ImageNet WordNet hierarchy has thousands of nodes), solving an IP at inference time for every input may be slow. A brief empirical report of wall-clock time would clarify whether this is a practical constraint.

---

## Nice-to-Haves

- A direct size comparison between structured and flat conformal prediction across at least one domain (e.g., mean concrete label count for standard flat conformal vs. |leaves(ỹ)| for the structured predictor, all as a function of ε at matched coverage) would make the interpretability tradeoff visible and quantifiable.
- A secondary analysis showing how the benefit of structured prediction sets depends on the alignment between the DAG structure and the model's posterior (e.g., well-organized hierarchy vs. a random DAG) would sharpen understanding of when the method is most valuable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The marginal guarantee proof is a single sentence deferring to learn-then-test."** (Harsh Critic) — The proof of Theorem 1 correctly cites the learn-then-test paper. This is standard academic practice for a result that follows directly from prior work. Not a flaw.

- **Computational cost of IP framed as a Major flaw** (Harsh Critic) — Demoted to Trivial; no evidence is given that the IP is slow in practice on the paper's actual experimental domains. This is speculative about large DAGs, not a demonstrated problem.

- **"The algorithm's threshold set T is a reproducibility concern"** (Harsh Critic) — Demoted to Trivial. The standard practice in conformal prediction of using calibration scores as thresholds is well-understood; this is a minor clarification, not a substantial gap.

- **Demanding confidence intervals for the scale of experiments** — Standard deviations across 5 seeds are reported, which is reasonable for empirical CP papers of this scale. Requesting formal CIs would be above the field's norms here. Retained only as an acknowledgment that statistical weight is limited (Minor weakness above) rather than demanding more formal statistical machinery.

- **Strength Finder strength: "Empirical validation demonstrates coverage guarantees are satisfied"** — Weakened: the paper satisfies a guarantee already implied by the theory. This is only a strength to the extent it validates the implementation. Not an independent scientific contribution; partially folded into the coverage confirmation note.

---

## Novel Insights

The paper's key insight — that the learn-then-test framework's sequential search is the right primitive for handling non-monotone coverage in structured label spaces, and that this same mechanism can be adapted to yield PAC guarantees — is a clean and useful observation. The integer programming formulation for DAG-structured sets is notable for its generality: the same IP handles both hierarchical classification (fixed DAG per dataset) and interval-union prediction (input-varying DAG), which is non-obvious. The qualitative example in Table 1 inadvertently surfaces a genuine tension: structured representations can be syntactically more compact while covering *more* concrete labels, which is the right framing for interpreting the method's value but one the paper itself does not develop. Making this tradeoff explicit would be the single most impactful addition to the paper.

---

## Suggestions

1. **Fix the PAC proof justification:** Replace "μ ≤ ε" with the correct direction: "Since μ > ε (as τ₀ is invalid) and the binomial CDF is monotonically decreasing in p, F(ℓ̂; n, μ) ≤ F(ℓ̂; n, ε)."
2. **Add at least one quantitative baseline comparison:** Plot mean leaf-count under the structured predictor vs. mean prediction set size under a standard flat conformal predictor (APS or RAPS) at matched coverage, for ImageNet or SQuAD. This is the single experiment that would most directly support the paper's interpretability thesis.
3. **Move MNIST and ImageNet results to the main text** or add a paragraph discussing them; the current main-text-only treatment of SQuAD leaves the other two domains invisible to reviewers.
4. **Narrow the abstract's scope** to remove the text-generation framing that the paper does not instantiate or evaluate.
5. **Discuss selection strategy for m:** even a sentence acknowledging that m is fixed by the user prior to calibration, with a note that smaller m trades interpretability for potentially larger concrete sets, would be helpful.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `v8RDgaEtE2.md` (Regression CP under Bias) | 2.50 | R1 (low) | Rejected; much weaker contribution (asymmetric adjustments only) |
| `7HdtLgsvys.md` (Tube Loss) | 2.50 | R1 (low) | Rejected; narrow loss function proposal, no CP theory |
| `ZBL26FX0FT.md` (Socrates Loss) | 3.00 | R1 (low) | Rejected; incremental loss function, no structural novelty |
| `MNGMpHxi1I.md` (Info-theoretic Predictive Uncertainty) | 3.00 | R1 (low) | Rejected; similar domain, narrower contribution |
| `33XGfHLtZg.md` (Conformal Risk Control) | 7.00 | R1 (mid) | Accepted; much broader impact, multiple extensions, tighter guarantees |
| `RcNzwKrjTo.md` (CP with Trust Scores) | 5.00 | R1 (mid) | Rejected; single variant, no structured setting |
| `Dtxc7mlKRg.md` (Class-Conditional CP for Imbalanced Data) | 4.60 | R1 (mid) | Rejected; narrower contribution (single setting), similar experimental limitations |
| `loDppyW7e2.md` (Multi-Dimensional CP) | 5.60 | R1 (mid) | Accepted; comparable scope but stronger experimental validation |
| `uUkpYafkVl.md` (CP for Deep Classifiers via Truncating) | 4.75 | R2 | Rejected; narrower (single new score function), comparable experimental depth |
| `PRKFRRzOEq8.md` (CP with Noisy Labels) | 5.40 | R2 | Rejected; comparable breadth but stronger baseline comparisons |
| `4vPVBh3fhz.md` (PAC Prediction Sets Under Label Shift) | 6.40 | R2 (read) | Accepted; PAC guarantees in a specific setting with 5 datasets and multiple baselines |
| `pzUhfQ74c5.md` (Conformal Language Modeling) | 6.25 | R2 | Accepted; more targeted application with stronger empirical section |
| `56jIlazr6a.md` (Unified Uncertainty Estimation) | 5.25 | R2 | Rejected; broader ambition but weaker execution |
| `libLqoInAd.md` (Dempster-Shafer + CP) | 5.25 | R2 | Rejected; combination of DS theory and CP, comparable experimental depth |

**Round 1 bracket:** 4.5–6.5. Clearly above the 2.5–3.0 rejected anchors (genuine theoretical contribution, general framework), clearly below the 7.0 Conformal Risk Control (weaker experiments, proof error).

**Round 2 narrowing:** The most topically comparable accepted papers are "PAC Prediction Sets Under Label Shift" (6.4) and "Conformal Language Modeling" (6.25). Both have 5+ datasets, explicit baseline comparisons, and no proof errors. The paper under review has a *broader* theoretical scope (general framework vs. one specific extension) but substantially weaker experimental execution — no baselines, proof error in justification, and a qualitative example that cuts against the stated claim. This places the paper below these anchors. "Multi-Dimensional CP" (5.6, accepted) has comparable scope with stronger experiments. "CP with Noisy Labels" (5.4, rejected) and "Unified Uncertainty Estimation" (5.25, rejected) are comparably executed. The paper is between these: above 5.0 based on the genuine generality of its framework and two-pronged contribution (marginal + PAC), but below 5.6 given the proof error and absence of any quantitative comparison to standard conformal baselines.

**Final score: 5.0** — the paper is at the borderline. The framework is sound and the contributions are real, but the experiments do not support the paper's central empirical thesis and the proof contains an explicit contradiction. With quantitative baseline comparisons and a corrected proof, this would be a solid acceptance at ~6.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>