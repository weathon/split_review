Now I have a thorough calibration picture. Let me finalize.

**Calibration Analysis:**

**Round 1 bracket:** 6.0–7.5

**Round 2 anchors:**
- DDPP/Steering MDMs (6.25, Accept) — most directly comparable: same problem domain, different approach. IterRef has broader experiments and clearer methodology.
- CARDS (5.75, Reject) — cascade reward sampling for LLM alignment. Weaker than IterRef in scope and results.
- Learning How Hard to Think (6.50, Accept) — adaptive test-time compute, different domain but similar theme.
- SDDS (6.00, Accept) — discrete diffusion samplers, narrower scope.

**Narrowing:** IterRef is clearly above CARDS (5.75, Reject) and SDDS (6.00, Accept). It is comparable to or slightly stronger than DDPP (6.25, Accept) due to broader empirical validation. It sits just below the convergence paper (7.00) which had a stronger theoretical core. But IterRef combines both theory AND strong empirical results across 3 models, 2 modalities, 5 reward functions — which is a broader contribution than the 7.0 theoretical paper.

**Final score: 7.0**

---

## Summary
This paper introduces IterRef, a test-time scaling method for discrete diffusion that applies Multiple-Try Metropolis (MTM) with a noising-denoising transition kernel to iteratively refine intermediate states toward reward-aligned distributions. The method is evaluated across three model backbones (MDLM, LLaDA-8B, MaskGIT), two modalities (text and image), and five reward functions, demonstrating consistent improvements over BoN, SoP, SVDD, and FK Steering baselines, with particularly striking efficiency gains at low NFE budgets.

## Strengths
- **Principled theoretical foundation with convergence guarantee**: The paper derives a specific transition kernel K and balancing function λ (Eq. 2) yielding uniform importance weights and a clean reward-difference acceptance rate (Eq. 3). Proposition 1 proves convergence to p*(x_t), grounding the method in established MCMC theory rather than heuristics.
- **Dramatic efficiency gains at low compute, consistently across backbones**: On MDLM, IterRef at 2T NFEs surpasses all baselines at 32T NFEs on Sentiment, CoLA, and Perplexity (§4.2, Figure 2a). On Toxicity with LLaDA, 4T NFEs matches FK at 32T — an 8× speedup. These results hold across both MDLM and LLaDA-8B backbones and four reward functions.
- **Cross-modality generalization**: Table 1 shows IterRef outperforms all baselines at every compute budget on MaskGIT with CLIPScore (e.g., 33.7 vs. 32.1 next-best at NFE=2; 35.8 vs. 34.8 at NFE=16).
- **Compelling ablation on iterations vs. particles (Table 3)**: At fixed compute on LLaDA, k=8/N=4 yields toxicity 54.0 while k=1/N=32 yields 3.3 — directly supporting the central hypothesis that iterative refinement is fundamentally more effective than increasing particle count.
- **Novel empirical insight on step importance in discrete diffusion**: Table 2 reveals later denoising steps (0.1T) consistently outperform earlier steps (0.9T), contrasting with continuous diffusion where early steps dominate (Choi et al., 2022). This advances understanding of discrete diffusion dynamics.
- **Practical cost optimizations preserving theoretical properties**: The specific balancing function (Eq. 2) eliminates backward resampling, and pool reuse on rejection avoids redundant candidate generation — both maintaining MTM's theoretical guarantees (§3.3).

## Weaknesses

### Fatal
None

### Major
- **No diversity or quality analysis alongside reward scores**: Every experimental result reports reward scores alone. The Ethics Statement explicitly acknowledges "reward over-optimization" (line 317), yet no metrics such as distinct-1/2, self-BLEU (for text) or FID/LPIPS (for images) accompany the reward curves. Without this, the headline claims (2× Toxicity improvement, 8× faster) could reflect reward gaming rather than genuinely better outputs. The qualitative examples (Figures 3, 5b) provide some reassurance but are cherry-picked. This is the paper's most significant gap.

- **Missing comparison with DSearch and DTS**: The Related Works section (§5, line 307) explicitly discusses DSearch (Li et al., 2025) and DTS (Jain et al., 2025) as recent competitive methods for reward-guided generation in discrete diffusion — one reframing the problem as search with dynamic beam width, the other using MCTS-based value backup. Both are discussed as relevant contemporaries but absent from experiments. Their inclusion would either validate IterRef's advantage over a stronger baseline set or provide a more nuanced picture.

- **Proposition 1's reversibility assumption is unvalidated**: Proposition 1 (line 146) requires that "q and p_θ form a reversible Markov kernel," which is not a standard property of trained discrete diffusion models. The paper provides no empirical validation of this assumption (e.g., measuring detailed balance violation) or discussion of when it might break down. The abstract (line 9) claims "proving convergence to the reward-aligned distribution" without qualification, while the contribution bullet (line 35) hedges with "under certain assumptions" — an inconsistency that overstates what is established.

### Minor
- **Overstated claim on iterations vs. particles**: The paper states "increasing iterations is more effective than simply generating more particles" (line 287), but Table 3 shows the peak at k=8/N=4, with k=16/N=2 actually underperforming (Toxic: 48.0 vs 54.0; CoLA: 75.3 vs 85.3). The more accurate statement is that there is an optimal balance favoring iterations.

- **Intermediate reward approximation quality unexplored**: The method relies on approximating r(x_t) by evaluating the reward on the model's prediction of x_0 from state x_t (line 117), but this approximation's reliability is only briefly mentioned and deserves more analysis, as it is central to the method's success.

- **Table 2 suspicious coincidence**: Both Toxic and Sentiment at 0.1T show exactly 37.6 (lines 238-239). Given these are different metrics on different scales, this may be a copy-paste error that should be verified.

### Trivial
- **Figure 1 caption characterization**: The caption states the noising process "incurs nearly zero cost" (line 27), but the transition kernel K requires a full denoising pass from timestep s back to t for each proposal, which is the dominant cost. The paper is transparent about this in §3.3, but the caption could mislead.

## Nice-to-Haves
- Report wall-clock times alongside NFE counts in the main text (acknowledged in §3.3 that aggregating NFE "may obscure meaningful differences"; wall-clock analysis deferred to Appendix C.4)
- Define the baselines (SLP, SR, SVTOD) used in the Figure 5 detoxification case study in the main text

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Eq. 3 rendering issue**: The harsh critic noted that Eq. 3 as rendered places α only on r(x_t) rather than the full difference. This is almost certainly a PDF parsing artifact — the intended expression is clearly (r(x_t') - r(x_t))/α. Not an author error.
- **"MTM imposes no constraints" misreading**: The critic claimed line 152 is misleading. However, the sentence refers to steps where IterRef is NOT applied — at those steps, any denoising method can be used. The context makes this clear.
- **Missing related works**: Per hard rules, cannot flag missing related works without external verification.

## Novel Insights
The paper provides a genuinely novel insight about discrete diffusion dynamics: unlike continuous diffusion where early denoising steps dominate content determination, Table 2 demonstrates that in discrete diffusion, later steps (0.1T) are far more impactful for reward-guided refinement. This finding has direct practical implications for how to allocate test-time compute in discrete diffusion. Additionally, the MTM-based noising-denoising refinement framework is a novel contribution to the test-time scaling toolkit — the specific combination of the transition kernel K and balancing function λ yielding uniform importance weights and reward-only acceptance (Eq. 2-3) is an elegant result that simplifies practical implementation while maintaining theoretical guarantees.

## Suggestions
- Add diversity metrics (distinct-1/distinct-2 for text, FID/LPIPS for images) alongside reward curves — if IterRef maintains diversity while improving reward, that dramatically strengthens the core claim
- Include DSearch and DTS baselines in Figures 2 and Table 1
- Add empirical validation of the reversibility assumption or soften the abstract's convergence claim
- Soften the k vs. N claim to reflect the actual optimal balance

## Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SVDD (2fgzf8u5fP) | 3.80 | 1 | Direct baseline, rejected with similar diversity concerns and unfair alpha settings. IterRef is much stronger. |
| CARDS (UAA2nWUtVl) | 5.75 | 2 | Cascade reward sampling for LLM alignment, rejected with limited experiments. IterRef is clearly stronger. |
| DreamTime (1bAUywYJTU) | 5.75 | 2 | Diffusion-guided 3D generation. Less relevant but similar tier. |
| Inference Scaling Laws (VNckp7JEHn) | 5.75 | 2 | LLM inference scaling study. Similar test-time scaling theme. |
| SDDS (peNgxpbdxB) | 6.00 | 1&2 | Discrete diffusion samplers. Narrower scope, accepted at 6.00. IterRef is broader. |
| DDPP (Ombm8S40zN) | 6.25 | 1&2 | Most comparable: steering MDMs via posterior prediction. Accepted at 6.25. IterRef has stronger empirical wins and clearer methodology. |
| Learning How Hard to Think (6qUUgw9bAZ) | 6.50 | 2 | Adaptive test-time compute allocation. Different domain, similar theme. |
| IterComp (4w99NAikOE) | 6.80 | 2 | Iterative feedback for T2I. Less directly relevant. |
| Convergence of Discrete Diffusion (pq1WUegkza) | 7.00 | 1 | Theoretical analysis of discrete diffusion. Stronger theory, weaker empirics than IterRef. |
| One Step Diffusion (OlzB6LnXcS) | 8.00 | 1 | Shortcut models for efficient diffusion. Stronger single contribution. |

**Round 1 bracket:** 6.0–7.5
**Round 2 narrowing:** IterRef sits above DDPP (6.25) given stronger empirical validation, comparable to the convergence paper (7.00) combining both theory and experiments. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>