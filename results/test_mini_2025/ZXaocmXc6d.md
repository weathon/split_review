## Summary

This paper derives exact closed-form solutions for the gradient flow dynamics of two-layer linear networks under "λ-balanced" initializations, where the relative scale between layers is controlled by a single parameter λ. The solutions capture the evolution of the network function, weight correlations, representational similarity, and NTK across the full spectrum from the rich regime (λ ≈ 0, sigmoidal learning curves) to the lazy regime (|λ| → ∞, exponential learning). The analysis reveals a novel "semi-structured lazy" regime where one layer remains task-agnostic while the other retains structured representations, and demonstrates applications to reversal learning, transfer learning, and fine-tuning. The theoretical results are validated by numerical simulations.

## Strengths

1. **Exact closed-form solutions for gradient flow under λ-balanced initialization (Theorem 4.3).** The paper provides explicit, time-dependent expressions for the network function, weight correlation structure, and NTK (Equations 13–15). This strictly relaxes the zero-balanced assumption of prior work (Fukumizu 1998, Braun et al. 2022), moving from a single point in initialization space to a continuum parameterized by λ. The solutions are validated by numerical simulations across multiple λ values (Figure 2).

2. **Discovery and precise characterization of a "semi-structured lazy" regime.** The paper demonstrates that for large |λ|, one layer's representations become task-agnostic (identity-like) while the other remains structured and task-specific (Section 5, Theorem C.4). This is qualitatively distinct from the standard unstructured lazy regime (where both representations are static) and from the rich regime (where both are task-aligned), and is supported by Theorem C.3 and the explicit singular value splitting in Equation 18.

3. **Analytical demonstration that non-zero λ guarantees success in reversal learning.** The paper proves that reversal learning consistently succeeds when λ ≠ 0 because the initialization avoids the saddle point that traps zero-balanced networks (Section 6, "Reversal learning"; Appendix D.2). This is a concrete theoretical prediction not available from prior balanced-initialization analyses.

4. **Clean derivation of the sigmoidal-to-exponential transition in singular value dynamics (Theorem 5.1, Equation 17).** The limiting expressions as λ → 0 (sigmoidal) and λ → ±∞ (exponential) are explicit and quantified with matching simulations (Figure 3), providing a precise analytical handle on the rich-to-lazy transition.

5. **Architecture-dependent interplay between λ and NTK evolution.** The analysis of funnel, square, and inverted-funnel architectures (Figure 5, Theorem C.6) shows that the sign of λ determines which architecture enters the lazy regime, and identifies a "delayed rich" phase. This rigorously confirms and extends the rank argument from Kunin et al. (2024) to the multi-output setting.

## Weaknesses

### Fatal

None.

### Major

1. **Scope mismatch between title/abstract and actual analysis.** The title advertises "deep linear networks" and the abstract describes "wide and deep neural networks," but the exact results are derived exclusively for **two-layer** linear networks with hidden dimension N_h = min(N_i, N_o) (Assumption A3: the narrowest possible width that can represent the task). The paper does not provide exact solutions for deeper architectures or for networks where N_h > min(N_i, N_o). Connections to wide networks (LeCun initialization, infinite-width limit) are discussed heuristically (Figure 1C, Appendix A.3) but are not part of the main theoretical derivation. The paper acknowledges this in Section 7 ("extension of this initialization to deep networks" is left for future work), but the title and first-page framing do not reflect these limits. A more accurate title would specify "Two-Layer Linear Networks."

2. **The λ-balanced initialization condition is highly structured and not straightforward to realize in finite networks.** The condition W₂ᵀW₂(0) − W₁W₁(0)ᵀ = λI is a very specific constraint. The paper argues (Figure 1C, Appendix A.3) that LeCun initialization in the infinite-width limit approximates this condition, but practitioners cannot straightforwardly set a desired λ in a finite-width network. This does not invalidate the theoretical contribution, but it means the quantitative predictions are tied to an initialization scheme that is not directly achievable in practice outside the infinite-width limit. The paper is transparent about this being a theoretical framework, but the gap between the solvable model and practical realizability is larger than the framing suggests.

### Minor

3. **Singularity at λ = 0 in the main theorem (Theorem 4.3) is not addressed in the main text.** The expressions in Equation 15 contain terms like (e^{λ_⊥ t/τ} − I)/λ_⊥. When λ = 0, λ_⊥ = 0 and this term is formally undefined (0/0). The theorem as presented in the main text does not note that the solution should be interpreted via continuity or a limiting procedure. The appendix presumably handles this, but the main text should explicitly flag this for readers.

4. **Applications are illustrative rather than deep.** The continual learning result is unsurprising (catastrophic forgetting persists regardless of λ), the reversal learning result is a clean theoretical point but only demonstrated in linear networks, and the transfer learning and fine-tuning observations are connected to practice (e.g., LoRA) only in passing (Section 6). The evidence consists of qualitative demonstrations in Appendix D rather than quantitative benchmarks. This limits the impact of the applications section.

5. **The comparison to standard lazy dynamics from Gaussian initialization (Figure 4D) is somewhat apples-to-oranges.** The paper contrasts the λ-balanced framework with large Gaussian initialization to highlight the novelty of the "semi-structured lazy" regime. While this illustrates a genuine difference, the comparison involves different initialization schemes with different properties, making it less controlled than the within-framework comparisons.

### Trivial

6. **The discussion of the λ = 0 limit in the singular value dynamics (Equation 17) shows λ in the denominator of the exponential argument for the sigmoidal case (e^{2\tilde{s}_α t/λ}),** which would diverge as λ → 0. The limit is presumably taken carefully with s_α(0) scaling appropriately, but the expression as presented could confuse readers.

## Nice-to-Haves

- A brief intuitive explanation of why the singular value splitting occurs (Theorem 5.2) and how the sign of λ determines which layer becomes identity-like would significantly improve accessibility.
- A quantitative measure of how much structure remains in the "semi-structured lazy" regime as a function of λ (e.g., Frobenius distance between the representation and identity) would sharpen the characterization.
- A short section or table showing how to approximately achieve a given λ in finite networks (e.g., by scaling layer-specific initialization variances) would increase practical utility.

## Removed Points

These points were flagged for removal but are noted for completeness; treat them with caution:

- **Harsh critic's claim about "NTK definition in equation (5) using Kronecker products being non-standard":** The Kronecker product formulation of the NTK for two-layer networks is standard and the paper cites the appropriate references. This is not a weakness.
- **Harsh critic's suggestion to "explicitly separate exact results from heuristic extensions" and "define the scope precisely":** The paper already states Assumptions A1–A3 clearly and explicitly acknowledges in Section 7 that extensions are future work. The issue is with the title/framing, not with internal clarity.
- **Strength Finder's generic strength about "addressing an important problem":** This is generic and not specific to the paper's evidence. Removed.
- **Strength Finder's claim about "analytical results for representation robustness to parameter noise":** This is factually present in the paper and correctly identified; however, the robustness analysis is limited to equal input-output dimensions, which the paper acknowledges.
- **Strength Finder's claim that the paper "strictly relaxes the zero-balanced assumption of prior work":** This is true and is a genuine strength; it was retained in the Strengths section above.
- **Harsh critic's claim about "missing statistical analysis of simulations":** The paper provides visual comparisons between analytical and numerical results (Figures 2–3) that clearly demonstrate agreement; a summary statistic would be nice-to-have but is not a weakness.
- **Harsh critic's suggestion to "remove the continual learning section":** This is a subjective editorial preference, not a weakness of the scientific content.

## Novel Insights

The most interesting meta-observation across the reviews is the recurring tension between what the λ-balanced framework actually delivers (exact solutions for a very specific class of two-layer networks) and how broadly it is framed. The harsh critic correctly identifies this as overclaiming, but simultaneously praises the theoretical contribution as "meaningful." This suggests the paper's genuine insight—that a single scalar λ can continuously interpolate between rich and lazy dynamics, and that the sign of λ interacts with architecture to determine which layer becomes lazy—may be underestimated by readers who focus on the restrictive assumptions. The "semi-structured lazy" regime is the most novel conceptual contribution, bridging the gap between unstructured lazy regimes (both representations static) and fully rich regimes (both representations task-aligned), and the paper correctly identifies that this structure could be exploited for transfer learning even though the downstream experiments remain lightweight.

## Suggestions

1. Revise the title to accurately reflect the scope, e.g., "From Lazy to Rich: Exact Learning Dynamics in Two-Layer Linear Networks under λ-Balanced Initialization."
2. Add a brief note in the main text (alongside Theorem 4.3) that the λ = 0 expressions should be interpreted via continuity, e.g., "the terms (e^{λ_⊥ t/τ} − I)/λ_⊥ are to be interpreted as their limits as λ_⊥ → 0."
3. Strengthen the contribution statement by explicitly stating what new insights the exact solution provides beyond prior work (Kunin et al. 2024, Xu & Ziyin 2024) in a concrete comparison paragraph.

## Score and Decision

**Calibration procedure:**

*Round 1 (Bracketing):* Broad search for papers on exact learning dynamics in linear networks with rich/lazy regime analysis. Weak anchors (avg 2.33–3.00) had poor presentation and no experimental validation — the paper under review is clearly stronger. Strong anchors (avg 7.6–8.0) were top-conference acceptances (Oral, Spotlight) with broader impact or more novel conceptual frameworks — the paper under review is weaker than these. **Initial bracket: (3.5, 7.5).**

*Round 2 (Narrowing):* Searched inside the bracket for comparable papers. Retrieved anchors:
- "Grokking in Linear Estimators" (avg 5.50, poster) — accepted but controversial; the paper under review has cleaner theory and better validation → **paper is stronger than this anchor.**
- "Simplicity Bias and Optimization Threshold" (avg 5.50, reject) — rejected; the paper under review is clearly stronger.
- "Connecting NTK and NNGP" (avg 6.00, reject) — mixed reviews, strong math but unclear contribution; paper under review is comparable in rigor but better validated.
- "Analyzing Neural Scaling Laws" (avg 7.33, spotlight) — similar analytical framework for two-layer networks, well-received; paper under review has comparable rigor but narrower scope (only minimal width, no nonlinear extensions).
- "Critical Learning Periods Emerge Even in Deep Linear Networks" (avg 7.25, spotlight) — methodologically similar, studied deeper networks with a compelling neuroscience narrative; paper under review is narrower (two-layer only) with a less compelling narrative.
- "Learning Dynamics of Deep Matrix Factorization Beyond EOS" (avg 7.00, poster) — strong assumptions were criticized; paper under review is comparably rigorous.

The paper sits above the 5.5 anchors (clearer theory, better validation) but below the 7.25–7.33 anchors (narrower scope, scope mismatch in framing). **Final score calibrated to 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>