Now I have a clear calibration picture. Let me finalize the review.

**Round 1 bracket**: Based on the bracketing pass, IterRef clearly sits above SVDD (3.80) and DNO (5.50), is comparable to or stronger than Demon (6.20), and sits near IterComp (6.80). My initial bracket is **5.5–7.0**.

**Round 2 narrowing**: The Demon paper (6.20) has a similar problem setting (inference-time alignment without backprop) but narrower evaluation (only images, 22 prompts, limited baselines). IterRef is stronger — broader evaluation across language and image, multiple backbones, a principled MCMC framework, and a novel finding about late-stage refinement. DNO (5.50) has similar issues plus reward hacking concerns. IterComp (6.80) is a different problem (training-based) but comparable in quality.

IterRef is clearly above Demon (6.20) and below IterComp (6.80), placing it at approximately **6.5**.

---

## Summary
This paper introduces IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) transitions — noising-denoising steps — to iteratively refine intermediate states toward reward-aligned distributions. By designing the MTM balancing function to simplify importance weights to uniform and acceptance to a reward-difference comparison, IterRef achieves efficient iterative refinement with convergence guarantees. The method consistently outperforms baselines across language and image tasks, often achieving with 2–4T NFEs what baselines need 32T NFEs. The paper also identifies that late-stage refinement dominates in discrete diffusion, a finding that contrasts with continuous diffusion dynamics.

## Strengths
- **Principled MTM formalization with elegant simplification**: The paper designs the balancing function λ (Eq. 2) such that importance weights reduce to uniform (w_n = N^{-1}) and the acceptance ratio simplifies to a reward-difference comparison (β = min(1, exp((r(x_t') - r(x_t))/α))). This eliminates the backward resampling step entirely, nearly halving per-iteration cost while preserving the MTM convergence guarantee (Proposition 1). The derivation from the general MTM framework to this simple acceptance rule is clean and well-motivated.
- **Consistent and large-margin empirical gains**: Figure 2 shows IterRef outperforming FK, SVDD, SoP, and BoN across four language tasks and two model backbones at all compute budgets. IterRef with 2T NFEs surpasses all baselines at 32T NFEs on Sentiment, CoLA, and Perplexity with MDLM. Cross-modal validation in Table 1 (MaskGIT + CLIPScore) further confirms consistent gains — IterRef achieves 35.8 CLIPScore at NFE=16 vs. the next-best baseline at 34.8.
- **Novel finding on late-stage refinement dominance**: Table 2 reveals that applying IterRef at later denoising stages (0.1T, 0.3T) consistently outperforms early-stage application (0.7T, 0.9T) across all four tasks. For CoLA, late-stage-only (0.1T, score 87.0) even beats evenly-spread refinement (83.0). This directly contrasts with the continuous-diffusion literature where early stages dominate content formation, providing genuinely new insight into discrete diffusion dynamics.
- **Iteration count k dominates particle count N**: Table 3 demonstrates that with fixed total budget k×N=32, k=8, N=4 achieves substantially better performance (Toxicity 54.0, CoLA 85.3) than k=1, N=32 (Toxicity 3.3, CoLA 8.7). This confirms that iterative refinement — not simply drawing more candidates — is the mechanism driving alignment, directly supporting the paper's core claim.

## Weaknesses

### Fatal
None.

### Major
- **Reversibility assumption in Proposition 1 is strong and undiscussed**: Proposition 1 assumes that q and p_θ form a reversible Markov kernel. For absorbing-state discrete diffusion, the forward noising process q is not obviously reversible, and the learned p_θ is not constrained to satisfy reversibility. The paper presents the convergence guarantee prominently as a contribution (Section 1, contribution #3) but does not discuss whether this assumption holds in practice or to what extent the empirical results rely on it. If the assumption is violated, the theoretical guarantee does not apply to the algorithm as actually deployed. The proof is deferred to Appendix D.4 (stripped from the submission), so the reader cannot verify whether relaxed forms of reversibility would suffice. This weakens the claimed theoretical contribution but does not undermine the empirical results.
- **No variance or uncertainty reporting**: All results report only means across 3 seeds with 15 prompts per task for language. No standard deviations, confidence intervals, or statistical tests are reported. Given the small prompt set, the reliability of the observed gains is difficult to assess — a few outlier prompts could substantially shift the means. This is particularly relevant for strong claims like "8× faster scaling" which depend on precise NFE-to-performance mappings.

### Minor
- **NFE metric conflates generative and reward model costs**: The paper uses NFE treating reward-model and generative-model calls on equal footing. Section 3.3 acknowledges this and notes that for LLaDA-8B, generative-model calls dominate, while for MDLM they are comparable. The paper mentions wall-clock time analysis in Appendix C.4, but this is stripped. This doesn't invalidate the comparisons but makes precise cost accounting harder to verify from the main text alone.
- **Limited prompt diversity for language tasks**: Only 15 prompts from Han et al. (2022) are used for the main language experiments. While the image experiments use 50k generations, the language results may not generalize broadly across prompt distributions.
- **Methods from related work not compared**: DSearch, DTS, and PG-DLM are discussed in related work (Section 5) but not included as baselines. Including at least one would strengthen the state-of-the-art claim, though the four baselines used are well-chosen and represent the main approaches in this space.

### Trivial
- **Equation 3 typo**: The acceptance ratio is written as `β = min(1, exp((r(x_t') - r(x_t)/α)))` with misplaced parentheses. It should read `β = min(1, exp((r(x_t') - r(x_t))/α))`.

## Nice-to-Haves
- Discussion of whether the reversibility assumption in Proposition 1 is realistic for absorbing-state discrete diffusion, or whether a relaxed convergence result could be stated without it.
- Error bars or confidence intervals on the main results to support claims of significant improvement.
- A more detailed breakdown of computational cost separating generative-model NFEs from reward-model NFEs in the main figures.

## Removed Points
These points are flagged to be removed, treat them with caution.
- The Harsh Critic input was truncated ("Now let me re-read the experimental details more carefully, focusing on the comparison between the method's theoretical and") and contained no completed criticisms to evaluate. No points were removed from the Harsh Critic.
- Strength Finder framing about "this paper addressed an important problem" — removed as generic and non-specific. The problem importance is clear from context and needs no separate strength listing.

## Novel Insights
The finding that late-stage refinement dominates in discrete diffusion (Table 2) is genuinely novel and contrasts with established continuous-diffusion wisdom where early stages drive content formation. If this finding generalizes, it suggests fundamentally different dynamics between continuous and discrete diffusion that could inform future algorithm design beyond just test-time scaling. This is the kind of result that could spark follow-up work on understanding why discrete diffusion trajectories behave differently.

## Suggestions
- Add a brief discussion of whether the reversibility assumption in Proposition 1 is plausible for absorbing-state discrete diffusion models, or clarify whether the convergence result should be viewed primarily as conceptual motivation rather than a practical guarantee.
- Report standard deviations or confidence intervals alongside means in the main results to help readers assess the reliability of the observed gains.
- Consider adding one of DSearch, DTS, or PG-DLM as a baseline if computational resources permit, as they represent more recent approaches in the same problem space.

## Anchor Calibration

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| SVDD (2fgzf8u5fP) | 3.80 | R1 | IterRef is clearly stronger — cleaner theory, broader evaluation, more consistent results |
| DNO (x1uv2gdjKV) | 5.50 | R1 | IterRef is stronger — broader evaluation across modalities, more principled MCMC framing, novel late-stage finding |
| C-Code (MBDH5zyxHM) | 4.60 | R2 | IterRef is stronger — more principled approach with theoretical guarantees and multi-modal evaluation |
| Demon (tfemquulED) | 6.20 | R2 | IterRef is comparable but stronger — broader evaluation (language + image, multiple backbones) and a novel insight about refinement dynamics |
| IterComp (4w99NAikOE) | 6.80 | R1 | IterRef is slightly weaker — IterComp has more comprehensive evaluation and fewer theoretical concerns, though different problem setting |
| SEDD (71mqtQdKB9) | 6.60 | R2 | Different subfield (training discrete diffusion models vs test-time scaling), but comparable quality tier |
| MDM Scaling (WNvvwK0tut) | 6.50 | R2 | Different subfield (scaling laws for MDMs), comparable quality tier |

**Bracket**: 5.5–7.0 (Round 1) → narrowed to 6.0–6.8 (Round 2). IterRef sits above Demon (6.20) due to broader evaluation and a novel finding, and slightly below IterComp (6.80) due to the reversibility assumption concern and lack of error bars. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>