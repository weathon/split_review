Now I have sufficient calibration context. Let me write the final consolidated review.

## Summary

This paper develops a theoretical framework for data curation in high-dimensional binary classification, deriving exact scaling laws for test error under label-agnostic and label-aware pruning oracles. The theory reveals a sharp phase transition: aggressive pruning ("keep hard") is optimal when the data generator is strong, while keeping all data (or preferring easy examples) is optimal when the generator is weak. The authors validate the theory with synthetic experiments, ImageNet experiments, and use the framework to interpret recent LLM reasoning results (LIMO, s1) and model collapse mitigation.

## Strengths

1. **Exact analytical test error formula under curation (Theorem 1, Eqns 9–11).** The paper provides a closed-form expression for the limiting test error that depends only on four scalar constants derived from the pruning rule. This gives a mathematically precise foundation that goes beyond heuristic analyses in prior work.

2. **Characterization of the optimal pruning strategy with a sharp phase transition (Theorem 2).** The paper proves that when the generator is strong (ρ→1) and the pruner is excellent (ρ\_*→1), "keep hard" is optimal; when the generator is poor (ρ<1) but the pruner is excellent, "keep easy" is optimal. This provides the first rigorous condition for when "less is more" versus "more is more" applies, which is the paper's central theoretical insight.

3. **Strong synthetic validation (Figure 1).** The match between theoretical predictions and empirical simulations across four regimes (varying generator quality and data size) is clear and supports the theory directly. The four quadrants cleanly illustrate the conditions under which pruning helps or hurts.

4. **Extension to label-aware curation (Theorem 3).** The framework is extended to the practically relevant setting where the oracle also verifies label correctness, covering the mechanism used in methods like LIMO and s1. This makes the theory directly applicable to current curation pipelines.

## Weaknesses

### Major

1. **Overclaiming on LLM reasoning explanation.** The abstract and introduction state that the paper "provides a principled explanation" and "rigorous justification" for the success of LIMO/s1. However, the theory is derived for binary classification with Gaussian features, linear teacher, squared loss, and an asymptotic high-dimensional limit — settings far removed from autoregressive LLM training with cross-entropy loss. The connection in Section 4.2 is purely analogical: the paper does not compute or measure ρ, ρ\_*, or ρ\_g in any LLM, nor does it test the predicted phase transition on any LLM reasoning task. The LLM discussion is a plausible qualitative interpretation, not a validated prediction. The paper would benefit from clearly separating the theoretically established results from the speculative interpretation, and framing the LLM connection as a suggestive qualitative connection rather than a "resolution" or "explanation."

2. **Theorem 2 relies on strong limiting assumptions that are not fully discussed.** The optimal strategy result is proven for ϕ→0 (data-rich limit) and λ→0 (unregularized limit), with ρ\_*→1. The paper then uses finite ϕ, λ, and ρ\_* in experiments without discussing how the results extrapolate away from these limits. The synthetic experiments do vary n (and thus ϕ), but the theoretical guarantee does not extend to the finite-ϕ, finite-λ regime used in practice. This gap between the limiting regime of Theorem 2 and the finite-resource experiments should be explicitly discussed.

### Minor

3. **ImageNet validation is indirect.** The ImageNet experiments (Figure 2) use training set size as a proxy for generator strength, and the theoretical quantities ρ, ρ\_*, ρ\_g are not measured. The results are consistent with the theory, but the mechanism could be confounded by other factors (e.g., covariate shift, representation quality, model confidence). The paper does not attempt to isolate label shift in the ImageNet experiments. While the synthetic experiments (Figure 1) directly validate the theory, the ImageNet experiments are only suggestive of the qualitative pattern.

4. **Model collapse experiment does not clearly map onto the theoretical framework.** Figure 3 uses the same model as both generator and pruner, which collapses the distinction between these entities that the theory parameterizes separately. The paper states "We use a pre-trained model as both the generator (w\_g) and pruner (w\_o)" but does not explain how the experimental setting maps to the theoretical parameters (ρ, ρ\_*, ρ\_g). The caption mentions "hard valid examples" without clarifying what "valid" means in this context. The experiment is interesting but the connection to the theory is not fully explicated.

5. **Sketch of proof is too brief.** The proof sketch for Theorem 1 (lines 154–155) mentions Stieltjes transforms and Marchenko-Pastur laws but does not connect them to the final expression. Given that the full proof is deferred to the appendix (which is stripped from the review copy), the main text would benefit from a more informative high-level description of how the constants p, γ, β, β̃ control the test error.

### Trivial

- The "keep easy" strategy for a weak generator: under label-agnostic pruning, examples with large |x^T w\_o| are retained. The paper could briefly discuss edge cases where the oracle is misaligned with the true labels and easy examples become misleading, but this is a minor omission.

## Nice-to-Haves

- A more systematic scan of n and ρ in the synthetic experiments would strengthen the empirical validation beyond the four quadrants shown in Figure 1.
- The LLM discussion could be strengthened by suggesting concrete ways to estimate ρ for an LLM on different problem difficulties, even if the estimation is approximate.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing appendix, missing proofs, missing reproducibility details (hyperparameters, architectures)."** The appendix was stripped by the parser; these details exist in the original submission. Per hard rules, these criticisms are removed.
- **"Error bars not visible in Figures 2 and 3."** The figure captions mention error bars; visibility issues are likely PDF extraction artifacts. Per hard rules, formatting artifacts are removed.
- **"Comprehensive set of validations in Appendix B not provided."** The appendix was stripped by the parser. Per hard rules, this criticism is removed.
- **"The paper does not discuss cases where easy examples are misleading."** This is a generic one-size-fits-all concern, not a specific problem identified in the paper. Removed.
- **Strength: "Reconciliation of contradictory LLM reasoning results."** This strength conflicts with the verified weakness about overclaiming. The paper's LLM discussion is interpretive and not validated, so this strength is overstated. Removed pending toned-down framing.
- **Strength: "Theoretical demonstration that curation prevents model collapse."** The experiment doesn't cleanly map to the theoretical framework (the same model is used as generator and pruner), weakening this claim as a strength of the theory itself. Removed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one observation that the paper itself does not fully articulate: the theory predicts that the *same* generator can be "strong" or "weak" depending on the slice of the test distribution (Section 4.2 makes this point for LLM reasoning but only implicitly). This suggests that the optimal pruning strategy is not just a function of the generator's global quality but of the match between the generator's competence and the target task's difficulty distribution — a more nuanced insight than the binary "strong vs. weak" framing. The paper could develop this point more explicitly.

## Suggestions

1. **Tone down the LLM claims.** Replace phrases like "provides a rigorous justification" and "principled explanation" with "offers a qualitative interpretation that is consistent with" or "suggests a mechanism for." The current framing overstates what the evidence supports.
2. **Discuss the gap between Theorem 2's limiting regime and the finite-resource experiments.** Explicitly state that Theorem 2 is proven for ϕ→0, λ→0, ρ\_*→1, and discuss how the results are expected to (and are observed to) extrapolate to finite settings.
3. **Clarify the model collapse experiment's mapping to the theory.** Explain how using the same model as generator and pruner corresponds to specific values of ρ\_g and ρ\_*, or discuss why the experiment should be seen as a qualitative demonstration rather than a direct test of the theory.
4. **Define "valid" in the model collapse experiment caption.** The caption of Figure 3 mentions "hard valid examples" without defining what validity means in this context.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Maximizing the Potential of Synthetic Data | I9Dsq0cVo9.md | 5.50 | 1,2 | Very similar methodology (RMT, binary classification, pruning). The paper under review is stronger: it derives optimal strategies (Theorem 2), has broader validation (ImageNet, model collapse), and connects to more timely phenomena (LIMO/s1). However, it also has more overclaiming issues. |
| Disentangling Roles of Representation and Selection in Data Pruning | EOPLy80bBm.md | 3.00 | 1 | Much weaker empirical paper without significant theoretical contribution. The paper under review is clearly stronger. |
| Generalization Error of Spectral Algorithms | 3SJE1WLB4M.md | 8.00 | 1 | Purely theoretical paper with tight results and clean execution. The paper under review is less clean theoretically but has more practical implications. |
| An Effective Theory of Bias Amplification | VoI4d6uhdr.md | 7.00 | 2 | Similar structure (theory + experiments for a practical phenomenon). Cleaner execution with less overclaiming. The paper under review is slightly weaker on empirical tightness. |
| High-dimensional Analysis of Knowledge Distillation | 1xzqz73hvL.md | 7.00 | 2 | Similar structure with theory and validation. Cleaner connection between theory and experiments. The paper under review has a wider gap between theory and experiments. |
| Analyzing Neural Scaling Laws in Two-Layer Networks | wFD16gwpze.md | 7.33 | 2 | More focused theoretical contribution with good validation. The paper under review addresses a broader question but with less precision. |

**Round 1 bracket:** 5.5 – 7.5. The paper is clearly stronger than the 3.0–5.5 papers (data pruning without theory) and weaker than the 8.0 papers (tight theoretical results with minimal overclaiming).

**Round 2 narrowing:** Compared to the 5.5 synthetic data paper (accepted poster), the paper under review has stronger theoretical contributions (optimal strategy characterization, not just performance analysis) and broader validation. Compared to the 7.0 papers (bias amplification, knowledge distillation), the paper under review has more overclaiming issues and a larger gap between theory and the practical claims. The paper sits between these bands.

**Final score:** This paper makes a genuine theoretical contribution with clean synthetic validation and suggestive real-world experiments. However, the overclaiming about LLM reasoning and the gaps between the limiting theory and the finite-resource experiments prevent it from reaching the 7+ range. The paper is clearly above the 5.5 level of the closest comparable work but below the cleanly-executed 7.0 papers.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>