Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper proves a first-order equivalence between activation steering vectors and influence-function-based re-weightings of training data, formalized through a primal–dual optimization framework. It introduces the Influence-Aligned Steering (IAS) vector, an alignment diagnostic γ (cosine of the smallest principal angle between Jacobian subspaces), spectral optimality results for steering directions, and generalization bounds for low-rank steering. The core theoretical insight — that steering and influence are projections of the same sensitivity tensor — is novel and potentially unifying.

## Strengths

**1. Novel theoretical unification of steering and influence (Theorem 4.2, Lemma 4.1).** The paper provides the first closed-form mapping between activation steering vectors and signed influence measures over training data. The derivation is clean: the chain-rule factorization (Lemma 4.1) and the primal–dual construction (Section 3) yield an explicit formula for ρ_s that is operational, not just conceptual. This is the paper's genuine contribution.

**2. Alignment diagnostic γ is practically useful (Theorem 5.1, Fig. 2).** Reducing the feasibility question to a single scalar — the smallest principal-angle cosine between two Jacobian subspaces — is elegant and computationally cheap (two small SVDs). The empirical finding that γ increases monotonically with layer depth (0.64→0.94 in GPT-2 Medium, Fig. 2) provides concrete guidance for practitioners: steer at later layers. The bound √(1−γ²) on the irreducible logit error is tight and actionable.

**3. Generalization guarantee for low-rank steering (Theorem 6.1).** The Rademacher-complexity bound √(2k/(dn)) gives theoretical grounds to trust that low-rank IAS corrections do not catastrophically increase generalization gap. For fixed α and k ≪ d, the excess risk vanishes as layer width and sample size grow, which is a non-trivial and useful result.

**4. No-free-lunch characterization (Theorem 6.2).** Converting small γ into a provable upper bound on steering fidelity justifies the rule "if γ < 0.5, skip steering and use weight-space editing instead." This impossibility result is clean and directly useful.

## Weaknesses

### Fatal
None.

### Major

**1. Unexplained slope of 1.5 in Fig. 1 contradicts the claimed quantitative equivalence.** The paper's central empirical claim is that the first-order logit shift from an influence update is matched by the IAS vector. Fig. 1 shows a fit slope of 1.50 — meaning the actual steering effect is 50% larger than predicted — yet the text merely says this is "consistent with the expected linear regime" (line 243). A slope of 1.5 vs. the predicted 1.0 is not addressed, error bars are absent, and no explanation (Jacobian estimation scaling, second-order amplification, pseudoinverse convention) is offered. While the high cosine (0.978) confirms direction preservation, the magnitude error undermines the quantitative claims of equivalence. This must be resolved for the paper's core experiment to be convincing.

**2. The spectral optimality experiment (Fig. 3) does not validate Theorem 5.3.** Theorem 5.3 claims that the top eigenvector of Σ maximizes expected first-order logit change under an ℓ₂ budget. The experiment on ResNet-50 compares the spectral radius of true labels against a null distribution from random labels, showing statistical significance (p=0.00498). This does not test the optimality claim: it does not measure the actual logit change achieved by the spectral steering direction, nor does it compare against alternative directions (random directions in activation space, CAA, PCA of activation differences, or any other baseline). The x-axis label ("Spectral radius of Xc^T diag(y) Xc") is never defined in the paper, further obscuring what is being plotted. The experiment is a statistical sanity check, not a validation of the theorem.

**3. No empirical validation of the claimed data-attribution workflow.** The paper promises repeatedly (Abstract, line 122, line 134, Corollary 1) that ρ_s "pinpoints the fewest training examples to relabel/remove/examine" and that practitioners can "identify the responsible training examples." Section 7 contains no data-attribution experiment, case study, or human evaluation. There is no comparison to existing data-attribution methods (TracIn, direct influence functions, GradDot, etc.) on any task. For a paper that presents this as a key practical contribution, the omission is major.

**4. Abstract and introduction overstate the scope of the equivalence.** The abstract states "any steering vector can be represented as an influence weighting over training data and vice versa" without the span-condition qualification introduced later in the paper (Theorem 4.2, line 112–118). At γ=0.6 (the low end of the observed range in Fig. 2), the residual bound √(1−γ²) allows up to 80% of the target logit change to be unreachable via steering. The paper does not measure this residual empirically anywhere, nor does it demonstrate the γ-based decision rule ("if γ < 0.5, skip steering") in practice. The unconditional phrasing in the abstract sets misleading expectations.

### Minor

**1. Eq. (2) has a missing pseudoinverse.** The expression Δh* = J_{h→y}^⊤ J_{θ→y} Δθ in Eq. (2) is inconsistent with Theorem 5.2's Δh* = J_{h→y}^† J_{θ→y} Δθ and with the dual derivation presented in the same sentence. The correct form should include the pseudoinverse factor (J_{h→y}J_{h→y}^⊤)^†. This typo in a core formula hurts readability.

**2. Influence function reliability is not discussed.** The entire duality depends on influence estimates I(z→x) involving the inverse Hessian (or its damped Gauss-Newton surrogate). The paper cites Basu et al. (2021, "Influence functions in deep learning are fragile") in the references but does not discuss this literature or address whether the influence vectors used in experiments are trustworthy. Acknowledging this limitation (and ideally validating in a tractable setting where influence functions are known to be accurate, such as logistic regression on fixed features) would substantially strengthen the paper.

**3. IAS underperforms CAA on detoxification (Table 1) without discussion.** IAS has higher toxicity (0.0164 vs. 0.0150) and higher perplexity (13701 vs. 13291) than CAA. If the advantage of IAS is its traceability to training data, this trade-off is defensible, but the paper does not make this argument, nor does it demonstrate that the traceability is accurate. The choice of steering vector construction for this experiment (spectral direction vs. projected influence update) is not clearly specified.

**4. No error bars or confidence intervals in Table 1 or Fig. 1–2.** For a paper making quantitative claims about slopes, alignment values, and toxicity/perplexity scores, the absence of error bars or repeated-trial statistics makes it impossible to assess the reliability of the reported numbers.

### Trivial

- The x-axis label in Fig. 3 ("Spectral radius of Xc^T diag(y) Xc") is never defined in the paper.
- Theorem 6.2 (No-Free-Lunch) is a direct geometric consequence of principal angles and adds little beyond Theorem 5.1.

## Nice-to-Haves

- A linear-model or small-scale experiment (e.g., logistic regression on fixed features) where influence functions are exact, to validate the duality cleanly before moving to deep networks.
- A concrete example showing ρ_s applied to a real steering vector (e.g., anti-toxicity) with the top-weighted training examples and a human evaluation of their semantic relevance.
- Measuring the residual from Theorem 4.2 empirically: for a steering vector, compare the true logit shift to the best-possible influence-weighted sum and report the residual norm relative to √(1−γ²).
- Showing γ across layers for more models (e.g., a small vision model, Llama-7B) to demonstrate generality beyond GPT-2 Medium.

## Removed Points

*The following points raised by reviewers were excluded or downgraded:*

- **"The theory predicts slope 1.0 in Fig. 1" as framed by the harsh critic:** The critic treats slope ≠ 1 as automatically invalidating the core claim. I kept this as a Major weakness but downgraded it from a "fatal" framing — the high cosine (0.978) shows the linear relationship holds strongly in direction, which supports the qualitative equivalence. The issue is the unexplained magnitude error, not a collapse of the entire theory.
- **Criticism about missing proof details for Theorem 4.2 in the main text:** The appendix (where proofs would normally appear) was stripped by the parser. Per instructions, this is not the authors' fault.
- **Generic concerns about "influence function fragility" framed as fatal:** The paper does cite Basu et al. (2021) and uses damped Gauss-Newton surrogates. I kept a Minor weakness acknowledging the lack of discussion, but removed the framing as a critical methodological gap.
- **Strength Finder's claim that Fig. 1 "directly confirms the first-order approximation":** Since the slope is 1.5, not 1.0, calling this a strength is misleading. I removed this strength.
- **Strength Finder's claim that Fig. 3 validates spectral optimality:** The experiment does not test what the theorem claims (optimal steering direction). I removed this strength.
- **Generic praise about "addressing an important problem" from Strength Finder:** Dropped as superficial per instructions.

## Novel Insights

None beyond the paper's own contributions. The most interesting tension exposed by the reviews is that the paper's strongest point (geometric unification via primal–dual optimization) and its weakest point (empirical validation of that unification) are the same quantity: Fig. 1 shows near-perfect directional agreement but a 50% magnitude error, which the authors never explain. This discrepancy itself is a novel observation — the paper would benefit from investigating whether the slope ≠ 1 is a consistent artifact or reveals something about second-order effects in transformer architectures.

## Suggestions

1. **Explain the slope of 1.5 in Fig. 1.** Provide error bars, repeat the experiment at different α values and layers, and discuss whether the deviation from slope 1 is due to Jacobian estimation, pseudoinverse conventions, or genuine second-order effects. A plot of the residual as a function of α would confirm the O(α²) bound from Corollary 2.

2. **Properly validate Theorem 5.3.** Compare the logit change achieved by the spectral direction against random directions in activation space, CAA, PCA of activation differences, and a few other steering heuristics. Show that the spectral direction indeed achieves larger logit changes under the same ℓ₂ budget.

3. **Provide at least one data-attribution case study.** Select a steering vector (e.g., detoxification), compute ρ_s, and show the top-10 weighted training examples with a brief discussion of whether they are semantically related to the targeted behavior. Compare ρ_s scores against plain influence function scores on the same examples.

4. **Qualify the abstract's claims** to reflect the span-condition dependence and the residual bound √(1−γ²). The current phrasing ("any steering vector can be represented...") is technically misleading without the caveat.

5. **Add error bars or confidence intervals** to Table 1 and Fig. 1–2. Single-point estimates without variance are insufficient for quantitative claims.

## Score and Decision

The paper's core theoretical contribution — the primal–dual unification of steering and influence — is novel and well-executed. The γ diagnostic is a genuinely useful tool. However, the empirical validation has significant gaps: the central linearity experiment shows a 50% magnitude discrepancy that is not explained, the spectral optimality experiment does not test the claimed result, and the data-attribution workflow is promised but never demonstrated. These issues are addressable but require non-trivial additional experiments.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>