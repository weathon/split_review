- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 5, 8, 5, 6
Now I have a thorough understanding of the paper and can verify each claim. Let me construct the final review.

## Summary

The paper proposes GPS (Gumbel Prior Similarity), a set-to-set matching measure that models the distribution of KNN distances between two sets using Gumbel distributions. The method feeds KNN distances through a Gumbel log-likelihood (with fixed, grid-searched parameters) to produce a similarity score, and is applied to few-shot image classification and 3D point cloud completion. Empirically, GPS shows consistent improvements over CD, EMD, and variants (HyperCD, InfoCD) across multiple benchmarks and backbone networks, while maintaining linear complexity.

## Strengths

1. **Consistent empirical wins across multiple tasks and backbones.** The paper reports improvements over CD, EMD, and recent alternatives (InfoCD, HyperCD, DCD) on five few-shot classification datasets (Tables 4–6) and across seven backbone networks for point cloud completion (Tables 8–12). This breadth—spanning both classification and geometric completion—suggests the approach is broadly applicable rather than narrowly tuned.

2. **Linear complexity competitive with CD, far cheaper than EMD.** Figure 5(b) and the text in Section 4.1 show that GPS with 1 Gumbel and 1st NN only has running time comparable to CD, while EMD-based DeepEMD is substantially slower. This is a practical advantage for large-scale use.

3. **Ablation studies demonstrating robustness to hyperparameters.** Tables 1–3 and Table 7 systematically vary the number of Gumbel mixtures, number of NNs, and Gumbel parameters, showing that "the best results under different settings are close to each other" and that mixtures improve robustness. This addresses the concern that the method might be brittle to parameter choice.

4. **Generality across two distinct learning regimes.** The same GPS formulation handles both few-shot classification (where distances are not driven to zero, δ=0) and point cloud completion (where distances should approach zero, δ>0), with a clear analysis in Section 3.3 distinguishing the two cases (Figure 4).

## Weaknesses

### Fatal
None. The core contribution—a similarity measure formed by feeding KNN distances through a Gumbel-shaped nonlinearity—is a valid heuristic with empirical support. The theoretical framing is somewhat oversold, but the method itself is not invalid.

### Major

1. **No error bars or variance reporting anywhere in the paper.** All classification and completion tables report single point estimates with no standard deviations, confidence intervals, or mention of number of runs. Given that improvements are sometimes small (e.g., 0.2–1.5% in few-shot classification), it is impossible to assess whether these gains are statistically meaningful or within run-to-run variation. This is the most serious weakness because it undermines the reader's confidence in the main empirical claim.

2. **Baseline comparison protocol for point cloud completion is insufficiently specified.** For few-shot classification, the paper explicitly states (line 129): "we re-implement all pre-training, meta-training, validation and testing stages with different loss functions, and retrain the networks from scratch." For point cloud completion, the text says (line 141–142): "We compare our method using seven different existing backbone networks... by replacing the CD loss with our GPS wherever it occurs." It does not state whether all baselines (L1-CD, L2-CD, DCD, HyperCD, InfoCD) were retrained under identical protocols or whether published numbers are cited. If the latter, differences in training procedures (optimizer, schedule, epochs) could confound the comparison.

3. **The probabilistic derivation is dressed up but the actual method is a fixed nonlinearity.** The paper sets up a graphical model (Figure 3) and a Bayesian formulation (Eq. 3), but immediately simplifies by taking p(q) and p(P₁=P₂|q) as constants (line 78) and replacing the sum over latent Gumbel distributions with fixed, grid-searched mixture components (Eq. 4–5). The resulting "likelihood" is simply a sum of fixed-parameter Gumbel log-densities evaluated on transformed KNN distances. This is not an estimated probabilistic model—it is a nonlinear transformation with parameters selected by grid search. The paper's title and abstract claim a "probabilistic distributional similarity," which overstates what the method actually delivers. While this does not invalidate the empirical results, it mischaracterizes the contribution.

### Minor

4. **The mapping from the paper's parameters (α,β) to the standard Gumbel parameters (μ,σ) is never defined.** Definition 1 gives the Gumbel PDF with location μ and scale σ. Equation (4)–(5) use p(d_min; α,β) without stating how α,β relate to μ,σ. The mode is given as δ = (α)^{-1/β} (line 94), but this is not connected to the standard mode μ of the Gumbel. A reader cannot derive the exact log-likelihood function implemented without guessing or inspecting the demo code. This is a reproducibility gap.

5. **The i.i.d. assumption required for Gumbel extreme-value theory is acknowledged as violated but weakly defended.** The paper correctly notes (line 104) that KNN distances are not i.i.d. and that the Gumbel "is hardly valid in our modeling," then appeals to empirical success similar to "bag-of-word model." This is an honest admission, but it means the theoretical motivation (extremal distributions for i.i.d. samples) does not actually apply. The method should be presented as a heuristic whose Gumbel form is justified by empirical fit (Figure 2(c)), not by extreme-value theory.

6. **Proposition 1 does not connect to the main method.** Proposition 1 analyzes f(x)=xe^{-x}. This function does not appear in the Gumbel PDF (Eq. 1), in the GPS definition, or in the gradient of the Gumbel log-likelihood (which involves e^{-y} where y=(x-μ)/σ). The claimed gradient analysis following the proposition is generic and does not depend on this proposition. The proposition is mathematically correct but adds no insight to the paper's central claims.

### Trivial
None beyond the presentation issues already captured above.

## Nice-to-Haves
- Adding a comparison against simple alternatives would strengthen the paper: e.g., using the sum of KNN distances directly (without Gumbel), or applying other fixed nonlinearities (exponential, sigmoid, -log(d_min) without Gumbel). This would isolate the value added by the Gumbel shape.
- Making the Gumbel parameters learnable (as the paper's own limitations section suggests for future work) would eliminate the grid-search overhead.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critic's claim that "GPS improvements over DeepEMD with Grid/Sampling are reported without numbers"** — REMOVED because it is factually wrong. Line 119–120 explicitly states: "our GPS in 1-shot 5-way can improve 1.2% over DeepEMD with Grid and 1.3% with Sampling."
- **Critic's claim that the simplification of p(q) and p(P₁=P₂|q) "is not stated or defended"** — REMOVED because line 78 explicitly states: "Note that here we take p(q) and p(P₁=P₂|q) as two constants with no prior knowledge." The modeling choice IS stated.
- **Critic's claim about the derivation being "unjustified"** — WEAKENED from the critic's framing. The paper transparently states the simplifying assumptions (constant priors, fixed Gumbel parameters). The weakness is that the resulting method does not match the "probabilistic" billing, not that the derivation is hidden.
- **Strength Finder's claim about Proposition 1 providing "gradient analysis showing that the loss automatically down-weights easy samples"** — This claim overstates the proposition's relevance. Proposition 1 analyzes f(x)=xe^{-x} which does not appear in the Gumbel PDF or GPS. The gradient behavior is independently true of the Gumbel log-likelihood but does not follow from Proposition 1. REMOVED the claimed grounding via Proposition 1.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Add error bars.** Re-run the main experiments (especially few-shot classification) multiple times with different random seeds and report means ± std. This is essential given the small margins reported.
2. **Clarify the baseline comparison protocol for point cloud completion.** State explicitly whether all baselines were retrained under identical conditions or whether published numbers are used. If the latter, discuss potential confounds.
3. **Explicitly state the mapping from (α,β) to (μ,σ).** Provide the exact formula for p(d_min; α,β) in terms of the Gumbel PDF parameters. This takes one equation and eliminates all ambiguity.
4. **Tone down the "probabilistic" framing.** The method is better described as a Gumbel-shaped similarity function with fixed parameters, rather than a full Bayesian model. The empirical fit of Gumbel to KNN distance histograms (Figure 2(c)) is a perfectly defensible motivation on its own.
5. **Compare against simpler baselines.** Adding ablations that substitute the Gumbel log-likelihood with other fixed nonlinearities (or the raw KNN distance sum) would demonstrate the specific value of the Gumbel shape.

---
