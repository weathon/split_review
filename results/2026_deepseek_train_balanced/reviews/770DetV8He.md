Now I have all the evidence I need. Here is my final synthesized review.

---

## Summary

This paper introduces the Markov Bridge Model, a generative framework that models the dependency between two intractable discrete distributions as a Markov process pinned at both endpoints, and applies it to single-step retrosynthesis (RetroBridge). The key innovation is replacing the noise→data paradigm of discrete diffusion with a product→reactants bridge process, eliminating the need for a tractable noise prior. On USPTO-50k, RetroBridge achieves competitive exact-match accuracy among template-free methods and outperforms both template-free and template-based methods on round-trip metrics.

## Strengths

**1. Round-trip results convincingly demonstrate practical value.** Table 2 shows RetroBridge achieving 85.1% top-1 round-trip coverage/accuracy, surpassing template-based methods GLN (82.5%) and LocalRetro (82.1%), and substantially ahead of other template-free methods. At k=5, RetroBridge reaches 97.1% coverage vs 94.7% for LocalRetro. Because round-trip evaluation captures the one-to-many nature of retrosynthesis (multiple valid reactant sets per product), this is the paper's strongest empirical evidence and a genuinely impressive result for a template-free method.

**2. Controlled ablation directly validates the Markov bridge formulation over diffusion.** Table 3 compares RetroBridge and DiGress using the same architecture and hyperparameters. RetroBridge-VLB (context) outperforms DiGress (context) at every k value (e.g., k=5: 79.44 vs 73.93; k=50: 86.31 vs 80.88). Critically, RetroBridge-VLB without product context still achieves 47.42 top-1 accuracy, while DiGress without context "does not manage to recover any reactants." This controlled comparison provides direct evidence that starting the process from the product molecule (bridge) is more natural than starting from noise and conditioning on the product (diffusion).

**3. Empirical justification of the variational lower bound over cross-entropy loss.** Table 3 shows RetroBridge-VLB (context) outperforming RetroBridge-CE (context) at all k>1 metrics (k=3: 73.04 vs 71.50; k=5: 79.44 vs 76.58; k=10: 83.74 vs 79.50). This provides empirical support for the theoretically motivated VLB objective over the simpler CE loss used in prior discrete diffusion work, beyond what the ablation's primary claim requires.

**4. Clean theoretical framing.** The Markov bridge formulation (Section 3.1) is a well-motivated adaptation of D3PM's discrete diffusion to the paired-data setting. The transition matrix modification — pinning the target distribution to the ground-truth reactants rather than a uniform/absorbing distribution — is simple but principled.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contribution is sound, the experiments are reasonably well-controlled, and no weakness invalidates the main claims.

### Minor

**1. Unconditional "state-of-the-art" claim in the abstract and conclusion is imprecise.** The abstract (line 9) and conclusion (line 318) state RetroBridge "achieves state-of-the-art results on standard evaluation benchmarks" without qualification. In exact-match accuracy (Table 1), RetroBridge is outperformed at k=1 by several template-free methods (DualTF$_{\text{aug}}$ 53.6, Graph2SMILES 52.9, Retroformer$_{\text{aug}}$ 52.9 vs RetroBridge 50.8) and at most k values by template-based methods. The paper's SOTA claim holds strongly for round-trip metrics (Table 2) and for exact-match k>1 among template-free methods — both defensible — but the unqualified phrasing in prominent positions misleads. The text in Section 4.2 (line 266) is appropriately qualified, but the abstract and conclusion are not. This is fixable with more precise wording.

**2. The comparison with DiGress supports the Markov bridge advantage but the claim of "superiority over diffusion models" (contribution #2, line 41) is somewhat stronger than a single comparison warrants.** The paper transparently calls it a "naïve adaptation" of DiGress (line 278) and uses matched architectures/hyperparameters, which is appropriate. However, diffusion-based conditional generation remains an active design space; a single comparison cannot rule out that a more carefully engineered conditional DiGress (e.g., different conditioning strategies, loss weighting, or architectural modifications) would close the gap. The paper would benefit from acknowledging this limitation explicitly in the contributions framing rather than presenting the result as conclusive.

**3. Key experimental parameter T (number of timesteps) is not reported in the main paper.** The parameter T directly affects the granularity of the bridge process and is required for reproducibility. It may appear in the appendix (which was stripped by the parser), but a core parameter like this belongs in the main text.

**4. No variance or statistical significance reporting.** All accuracy numbers in Tables 1–3 are single point estimates. Given the stochastic optimization and sampling (100 samples per product), reporting results over multiple seeds or providing bootstrap confidence intervals would substantially strengthen evidential quality.

**5. The 10 dummy nodes are used without any sensitivity analysis (line 147).** Different reactions involve different numbers of added atoms. A brief ablation varying this number (e.g., 5, 10, 15) would address an experimental gap and improve reproducibility.

### Trivial

- The confidence scoring mechanism in Section 3.3 (Eq. 14) is simply empirical frequency — counting how often each unique reactant set appears among M=100 samples — not a model-based likelihood or uncertainty measure. The paper frames this as "leveraging the probabilistic nature" of the model, which overstates what is essentially voting by sampling frequency. This does not harm the paper but should be presented more straightforwardly.

## Nice-to-Haves

- An analysis of *why* the bridge formulation helps (e.g., fraction of correct atoms retained at intermediate timesteps for bridge vs. diffusion) would sharpen the core methodological argument considerably.
- A failure-case analysis identifying reaction types or atom configurations where the bridge model systematically underperforms would strengthen the empirical contribution beyond aggregate metrics.

## Removed Points

These points are flagged to be removed — treat them with caution:

- Harsh critic's complaint about "one-shot graph transformer without a number" (reporting 0.0 vs textual statement). The paper's textual description ("does not manage to recover any of the reactants," line 285) is sufficient; adding a table row with 0.0 adds no information.
- Harsh critic's claim that confidence scoring is "presented as a contribution when it is not one." The paper's contributions list (lines 39–43) does not include confidence scoring as a separate contribution; it is presented as a practical feature of the approach, not a claimed novelty.
- Strength finder's claim that VLB "consistently outperforms CE at all k>1 metrics" — this is factually correct for k>1 and is retained as a strength; the caveat that CE beats VLB at k=1 (50.74 vs 48.92) is noted within the strength description so not removed.
- Strength finder's claim about confidence scores "correlating meaningfully with prediction quality" — kept as a trivial strength but noted to be limited (only 3 examples shown).

## Novel Insights

The most interesting observation that emerges from the combined reviews is that the paper's methodological contribution is strongest where the evaluation is most robust (round-trip, ablation vs DiGress) and weakest where the claims are most prominent (abstract, SOTA framing). The round-trip results are genuinely impressive and arguably more meaningful than exact-match accuracy for retrosynthesis, yet the paper leads with exact-match framing. The review process surfaces that the paper would be *stronger* if it re-centered its narrative around the round-trip advantage, where the evidence is unambiguous, rather than defending marginal exact-match comparisons at k=1.

## Suggestions

1. Qualify the "state-of-the-art" claim in the abstract and conclusion: e.g., "achieves state-of-the-art round-trip results and competitive exact-match accuracy among template-free methods."
2. Report T (number of timesteps) in the main text.
3. Add sensitivity analysis for the number of dummy nodes.
4. Add variance reporting across at least 3 random seeds for the main results.
5. Soften the claim about "superiority over diffusion models" to acknowledge the single-comparison basis.
6. Present the confidence scoring mechanism as empirical frequency rather than a likelihood-based uncertainty measure.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>