Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper proposes F²SA-p, a family of fully first-order methods for stochastic bilevel optimization that exploit p-th order smoothness in the lower-level variable to achieve improved SFO complexity. The key insight is that the prior F²SA method implicitly uses a forward-difference approximation of the hypergradient; the authors generalize this to p-th order central differences, yielding a systematic algorithmic family with complexity bounds of Õ(p ε^{-4-2/p}). A matching Ω(ε^{-4}) lower bound via a clean separable construction shows near-optimality in the highly-smooth regime.

## Strengths

- **Novel finite-difference reinterpretation of F²SA.** The paper shows that the hypergradient estimator in Kwon et al. (2023) is exactly a forward finite difference applied to a penalty function (Eq. 9), then extends the idea to arbitrary p-th order central differences (Lemma 3.1). This connection is elegant and directly motivates the entire F²SA-p family.

- **Provable acceleration from high-order smoothness.** Theorem 3.1 proves an SFO complexity of Õ(p ε^{-4-2/p}) for p-th order smooth bilevel problems, strictly improving on the prior Õ(ε^{-6}) bound. The result approaches the Õ(ε^{-4}) lower bound when p is large enough (Remark 3.4), matching the best-known complexity of HVP-based methods under stronger assumptions.

- **Tight lower bound with a clean, separable construction.** Theorem 4.1 establishes an Ω(ε^{-4}) lower bound that holds for any p by using a fully separable bilevel instance (f(x,y) = f_U(x), g(x,y) = μy²/2). This avoids flaws in prior lower bound constructions (e.g., violating smoothness assumptions) and shows F²SA-p is near-optimal in the highly-smooth regime.

- **Tighter Lipschitz analysis of the penalty function.** Lemma 3.2 generalizes existing Lipschitz-continuity results to any p and, for p=2, improves the constant from Õ(κ⁶) to Õ(κ⁵) (Remark 3.2). This tighter estimate is of independent interest.

- **Thorough comparison to related assumptions.** Section 2.2 carefully distinguishes the paper's setting from those requiring stochastic Hessians, mean-squared smoothness, or joint high-order smoothness — making the contribution's scope and novelty explicit.

- **Practical demonstration on a real dataset.** The experiments on learn-to-regularize with logistic regression (20 Newsgroup, Figure 1) show that F²SA-p with p>1 converges faster and achieves better test accuracy than F²SA and several HVP-based baselines, confirming that the higher-order methods are practically viable.

## Weaknesses

### Fatal
None.

### Major

- **Experiments claim to verify the theory but do not.** Section 5 states the experiments are conducted "to verify our theory," yet they only report test loss/accuracy versus outer-loop iterations with fixed inner-loop steps (K=10). There is no measurement of SFO cost, no variation of ε to test the predicted Õ(ε^{-4-2/p}) scaling, and no comparison of empirical convergence rates across different p against the theoretical predictions. The experiment merely demonstrates that the algorithm runs and achieves reasonable accuracy on one dataset — this is an illustrative demonstration, not a verification of the complexity theory. This disconnect between the claimed purpose and the actual content of the experiments weakens the paper's empirical credibility. The theoretical contributions remain unaffected, but the experimental section is misleading as written.

### Minor

- **No investigation of SFO-normalized convergence.** The paper does not report convergence of the hypergradient norm (or a proxy) as a function of total SFO calls. Without this, the reader cannot assess whether the theoretical Õ(ε^{-4-2/p}) rates are reflected in practice or whether higher p actually reduces the SFO cost to reach a given accuracy. Including such curves would substantiate the core theoretical claim.

- **The normalized gradient step is used without empirical justification.** Algorithm 1 uses a normalized gradient step (x_{t+1} = x_t − η_x Φ_t/‖Φ_t‖) to simplify the analysis (Remark 3.1). The authors conjecture that standard gradient steps would also work, but no experimental ablation comparing normalized versus standard steps is provided. Since the normalized step is a non-standard design choice, even a brief experimental comparison would help.

### Trivial

- The "w/o Reg" baseline (line 740–741) is briefly described as "the training result of SGD without tuning any regularization." Given that this is a bilevel optimization paper, the role of this baseline in the context of bilevel evaluation could be better motivated — it is unclear what comparison the reader should draw from it beyond a sanity check that tuning regularization helps.

## Nice-to-Haves

- A plot comparing the finite-difference error ‖Φ_t − ∇φ(x_t)‖ against ν for different p on a problem with known closed-form hypergradient would directly validate Lemma 3.2 and the estimator design.
- An experiment on a problem where smoothness is only guaranteed up to a specific order (e.g., a piecewise-polynomial construction) to test whether higher p indeed yields faster convergence under matching smoothness, and whether it breaks when smoothness is insufficient.
- Testing whether the normalized gradient step degrades practical performance compared to standard (unnormalized) steps.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh critic: "The proof of Lemma 3.2 relies on a high-dimensional Faà di Bruno formula that is not sketched in the main text; its correctness cannot be assessed without the appendix."** REMOVED per hard rules — complaints about material deferred to the appendix are parser artifacts; the full proof exists in the original submission's appendix, and the critic concedes "the approach appears plausible."

- **Harsh critic: "The statement that the method 'can be scaled to 32B sized large language model (LLM) training' (citing Pan et al., 2024) is not directly relevant to the theoretical contribution and is presented without further discussion."** REMOVED — this is not a weakness of the paper. The statement is a passing reference to prior work (F²SA, not this paper's method) and serves as motivation. It does not affect any technical claim.

- **Strength Finder: "This paper addressed an important problem" or similar generic claims.** REMOVED — these are superficial strengths that lack concrete evidence or specific citations.

## Novel Insights

The reviewers' observation that the finite-difference reinterpretation naturally suggests that the penalty parameter ν plays the role of the finite-difference step size is genuinely insightful. It connects two seemingly disparate literatures (penalty methods for bilevel optimization and numerical finite-difference schemes) and explains why F²SA-2 achieves the same per-iteration cost as F²SA while providing better error guarantees: the central difference estimator with α₀=0 means no extra lower-level problem needs to be solved. This insight — that "F²SA-2 benefits almost come for free" — is not just a theoretical artifact but has immediate practical implications for algorithm selection.

## Suggestions

- Revise the experimental section's framing. Instead of claiming to "verify our theory," present the experiments as a practical demonstration that F²SA-p is a viable algorithm family that outperforms baselines on a standard benchmark. If SFO-normalized convergence curves and hypergradient norm tracking are added, then the verification claim becomes supportable.
- Add an ablation comparing normalized versus standard (unnormalized) gradient steps in the outer loop, even on a small synthetic problem. This would address Remark 3.1 empirically and strengthen confidence in the algorithm design.
- Include a small experiment on a problem with controlled smoothness (e.g., a polynomial lower-level problem where p is exactly 2 or 3) to demonstrate that higher p actually accelerates convergence when the smoothness is present, and does not help (or hurts) when it is absent.

## Score and Decision

### Anchor comparison

| Anchor Path | Avg Score | Comparison to this paper |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/dJgb3ngAvT.md` | 5.00 (Accept) | Similar structure (new problem class/theory + algorithm + experiments). That paper introduced uniform convexity as a new tractable class; this paper introduces the finite-difference reinterpretation. Both have theory-heavy contributions with moderate experiments. This paper's theory is cleaner and includes a lower bound, but its experiments are weaker. Comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/HDqO1nHLmd.md` | 4.67 (Reject) | That paper only tightened condition-number dependencies for existing single-loop AID/ITD — an incremental improvement. This paper introduces a genuinely new framework (finite-difference reinterpretation) with broader implications and a matching lower bound. This paper is notably stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/GxKb08oD67.md` | 4.50 (Reject) | Both are fully first-order bilevel papers. That paper solved a new problem (CSBO) but with weak complexity (Õ(ε^{-8})). This paper achieves substantially better complexity (Õ(ε^{-4-2/p})) with a more elegant theoretical framework. This paper is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/RawXXTYZCw.md` | 3.33 (Reject) | That paper had serious correctness doubts and presentation problems. This paper's theory appears sound, well-structured, and the lower bound provides strong validation. This paper is much stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/hMxlumpguU.md` | 2.50 (Reject) | That paper lacked novelty (essentially recombining existing components), had weak experiments, and no stochastic analysis. This paper has clear novelty, solid theory, and works in the stochastic setting. This paper is far stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/a4LbWVcCmt.md` | 3.00 (Reject) | Not directly comparable (convex optimization with generalized smoothness). This paper is substantially stronger in contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/AlYT0ZD51A.md` | 4.50 (Reject) | Not directly comparable (NAG under relaxed assumptions). This paper's contribution scope is broader. |
| `/home/wg25r/review_agent/human_reviews_2026/wHzegHWXCf.md` | 4.00 (Reject) | Not directly comparable (Riemannian optimization). This paper is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/KirKWFPYJA.md` | 5.00 (Accept) | Not directly comparable (SGDM high-probability bounds). Both have solid theory; this paper's contribution is more novel. |
| `/home/wg25r/review_agent/human_reviews_2026/GeKMezBiA5.md` | 4.50 (Reject) | Similar domain (bilevel penalty methods). That paper had more serious concerns about contribution. This paper is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/JR1emTWT1D.md` | 3.00 (Reject) | Not directly comparable (trilevel). This paper is stronger. |

This paper sits closest to dJgb3ngAvT (5.00, Accept) — both make a clean theoretical contribution to bilevel optimization with a novel problem framing, and both have moderate experimental validation. The dJgb3ngAvT paper has somewhat better experiments (synthetic + data hyper-cleaning vs. one dataset here), but this paper has the advantage of including a matching lower bound. On balance, I judge these as comparable, with this paper having a slight edge in theoretical elegance. I assign **5.0**.

**Originality:** The finite-difference reinterpretation of penalty-based bilevel methods is genuinely novel and opens a new design space for fully first-order methods.

**Importance:** Closing the gap between fully first-order methods and HVP-based methods for stochastic bilevel optimization is an important open problem; the near-optimality result in the highly-smooth regime is a meaningful step.

**Claims supported:** The theoretical claims are well-supported by rigorous proofs. The experimental claims of theory verification are unsupported — the experiments are only a demonstration.

**Soundness:** The theoretical analysis appears sound. The experimental methodology is adequate for a demonstration but insufficient for verification.

**Clarity:** The paper is well-written, with clear motivation, careful assumption delineation, and accessible explanations of the key insights.

**Value to community:** The finite-difference perspective and the F²SA-p family provide a new lens for designing fully first-order bilevel methods, and the analysis tools (Lemma 3.2, the lower bound construction) are of independent interest.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>