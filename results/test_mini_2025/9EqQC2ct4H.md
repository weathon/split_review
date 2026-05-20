Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

**Round-1 bracket: 5.0 – 7.5** (based on broad comparison with weak anchors ~3 and strong anchors ~8)

**Round-2 narrowing:** The paper is clearly stronger than the Journey-TRAK paper (avg 5.75, rejected) and the CHG Shapley paper (avg 4.67, rejected). It is comparable to the D-TRAK paper (avg 6.0, accepted poster) — perhaps slightly stronger in contribution novelty but with a different set of fixable gaps. It is weaker than the Influence Functions paper (avg 8.0, oral) which had more thorough theoretical development. Final score: **6.0**.

---

## Summary

This paper introduces the problem of attributing *global* properties of diffusion models (image quality, demographic diversity, aesthetic quality) to *data contributors* (groups of data from the same source) rather than to individual training points — a formulation not addressed by prior local/datum-level attribution methods. The authors propose estimating Shapley values for contributors by approximating the expensive retraining on each data subset via sparsified fine-tuning (magnitude pruning + rapid fine-tuning), and evaluate across three diverse settings: DDPM on CIFAR-20, LDM on CelebA-HQ, and SD LoRA on ArtBench.

## Strengths

1. **First formulation of global contributor attribution for diffusion models.** The paper formalizes a new problem (Definition 1, Section 2.2) that targets attributing global properties (Inception Score, diversity entropy, aesthetic score) to data contributors rather than individual data points, filling a gap left by prior local-attribution methods (D-TRAK, Journey-TRAK). The motivation — compensating data labelers or artists — is timely and clearly articulated.

2. **Sparsified fine-tuning makes Shapley estimation practical.** The paper achieves 5.3× to 18.6× speedups over full retraining across the three settings (Table 2), with pruning reducing parameters by 45–74%. Figure 2 further demonstrates that sparsified-FT Shapley achieves *higher* LDS than either standard fine-tuning or full retraining under the *same* computational budget, showing that the pruning step provides a genuine efficiency-accuracy advantage rather than a simple speed-quality trade-off.

3. **Consistent state-of-the-art LDS across three diverse model/dataset/property combinations.** In Table 1, sparsified-FT Shapley achieves 61.48% (CIFAR-20), 26.34% (CelebA-HQ), and 61.44% (ArtBench), outperforming all 15 baselines including D-TRAK (10.90%, −27.23%, 11.30%) and LOO (30.66%, −1.22%, 3.74%). The advantage holds across subset sizes α = 0.25, 0.5, 0.75 (Appendix F).

4. **Counterfactual validation confirms causal impact of identified contributors.** In Figure 3, removing the top 40% of contributors identified by sparsified-FT Shapley changes the Inception Score by −23.23% (CIFAR-20) and demographic diversity by −7.83% (CelebA-HQ), whereas the best baselines achieve −17.30% and −6.64% respectively. This evaluation does not rely on the additive assumption of LDS, providing complementary evidence.

5. **Theoretical convergence bounds for the approximation.** Propositions 1 and 2 (Section 3.2) prove that as fine-tuning steps increase, the expected error in the global property and in the resulting Shapley values is bounded (under convexity and lottery-ticket assumptions). While the assumptions are idealized, the analysis connects the approach to known results in pruning and fine-tuning theory.

## Weaknesses

### Fatal
None.

### Major
1. **No direct validation of the core approximation (Equation 6).** The paper never directly compares $\mathcal{F}(\tilde{\theta}_{S,k}^*)$ (sparsified fine-tuned) against $\mathcal{F}(\theta_S^*)$ (fully retrained from scratch) for any subset $S$. The LDS metric tests the *end-to-end* Shapley values against true retrained model properties, and the counterfactual analysis provides complementary validation, so the results are not unmoored. However, a direct head-to-head comparison — even on a small-scale proxy (e.g., CIFAR-10 with fewer contributors where full retraining is feasible) — would isolate the approximation error and verify that pruning+fine-tuning does not introduce systematic bias that artifactually benefits Shapley's additive structure. Without this, the central methodological claim of Equation (6) rests on indirect evidence.

2. **Number of Shapley sampling subsets M is not reported.** The paper uses KernelSHAP (Equation 5) with $M$ sampled subsets but never states what $M$ is for any experiment. Given that $n$ ranges from 20 to 258 contributors, the number of subsets needed for stable Shapley estimates is nontrivial. Without $M$, (a) the results are not reproducible, and (b) it is impossible to assess the variance of the Shapley estimates or to interpret the computational trade-offs in Figure 2. The paper should report $M$ and ideally show LDS sensitivity to $M$.

### Minor
3. **LDS evaluation structurally advantages Shapley over baselines.** The LDS metric measures how well an additive linear model (sum of contributor scores over a subset) predicts the true model property. The Shapley value's efficiency axiom guarantees that this linear model is *optimal* for the Shapley value — it is an axiomatic property, not an empirical finding. In contrast, baseline methods (TRAK, influence functions, similarity-based) were not designed to yield additive contributor scores for global properties, so their lower LDS is partly structural. The paper partly mitigates this through the counterfactual evaluation (Figure 3), which does not rely on additivity. Still, the paper would benefit from a non-additive evaluation (e.g., leave-one-out rank correlation between per-contributor method scores and true leave-one-out retraining effects) to disentangle attribution quality from the structural advantage of additivity.

4. **Figure 2 lacks confidence intervals.** The paper reports LDS with 95% CIs for Table 1 (across three random initializations of held-out subsets), but Figure 2 (LDS vs. computational budget) shows only trend lines without error bars. Since LDS varies with the randomly sampled evaluation subsets, this quantification should be included.

5. **Pruning ratios are reported but not justified.** The paper states the pruned parameter counts (e.g., 35.7M → 19.8M for CIFAR-20) but does not explain how these specific ratios were chosen, whether performance of the pruned+fine-tuned model on the full dataset was checked, or whether sensitivity to the pruning ratio was studied.

### Trivial
6. The asymptotic theoretical results (Propositions 1, 2) rely on convexity and Lipschitz-gradient assumptions that the authors acknowledge are unrealistic for diffusion models. This is honest but the space could be better spent on empirical analysis of convergence behavior.

## Nice-to-Haves
- A random attribution baseline to anchor the LDS scale.
- An ablation showing how LDS varies with the number of fine-tuning steps $k$.
- Reporting of absolute GPU hours in addition to speedup ratios, for practitioners estimating total cost.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **Criticism that "the paper never tests the approximation"** via direct $\mathcal{F}(\tilde{\theta}_{S,k}^*) - \mathcal{F}(\theta_S^*)$ comparison: *Partially retained as Major weakness 1.* The harsh critic's framing that the approximation is "unvalidated" is too strong — the LDS and counterfactual evaluations do test the end-to-end pipeline against true retrained models. However, a direct per-subset comparison is indeed missing, so this is retained as a Major weakness but in a softened form.

- **"The theory adds little and may mislead casual readers"** (Harsh Critic, Section 3.2 critique): Removed. The paper explicitly acknowledges the assumptions are unrealistic and states the results are asymptotic. This is a valid approach for providing theoretical intuition.

- **Criticism that baselines are "ad hoc" aggregations for the LDS comparison**: Removed as overlapping with Minor weakness 3, which reframes this more precisely as a structural advantage.

- **"CelebA-HQ LDS is notably lower — this should be explored"**: Removed. The paper already acknowledges this (Section 4.5: "despite achieving the best results for CelebA-HQ… the LDS performance… is relatively low") and the entropy-based diversity metric is inherently noisier. This is a dataset property, not a weakness of the method.

- **"ArtBench counterfactuals show very small absolute changes"**: Removed. The paper reports the numbers honestly and the relevant comparison is *relative* to baselines, where the method still outperforms others. The suggestion to add a random null baseline is a nice-to-have.

- **"Hyperparameters: fine-tuning steps, learning rate, optimizer, batch size — all need to be specified"**: Removed. Fine-tuning steps *are* reported (1,000/500/200) and the paper defers to Appendices C/D for other training details (which are stripped by the parser, not omitted by the authors).

- **Strength Finder's "Theoretical convergence bounds"**: Retained but noted as asymptotic with acknowledged assumptions. Not removed.

## Novel Insights

The harsh critic's observation that LDS structurally advantages Shapley values (via the efficiency axiom) over baselines that were not designed for additive global attribution is a genuinely insightful point that deserves attention. While the paper partially addresses this with counterfactual evaluation, the community should consider developing evaluation metrics for contributor attribution that are not biased toward methods with built-in additivity. The second insight — that a direct head-to-head comparison of the pruned approximation against full retraining at the subset level would clarify whether the approach works as intended — is also a constructive observation that future work in this area should adopt as standard practice.

## Suggestions
1. Add a small-scale experiment (e.g., CIFAR-10 with 10 classes) where full retraining on all subsets is feasible, and directly compare $\mathcal{F}(\tilde{\theta}_{S,k}^*)$ vs $\mathcal{F}(\theta_S^*)$ across multiple subsets to validate the approximation.
2. Report $M$ (the number of KernelSHAP samples) for all experiments, and add a sensitivity analysis showing LDS vs. $M$ for at least one dataset.
3. Add a non-additive evaluation: for each contributor, compute the true leave-one-out effect on the global property, and measure rank correlation with each method's per-contributor scores. This disentangles attribution quality from the additive assumption.
4. Include confidence intervals or error bars in Figure 2.
5. Add a random-attribution baseline to Table 1 for context.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/.../vKViCoKGcB.md (D-TRAK) | 6.00 | R1/R2 | Directly comparable topic (data attribution on DDPM/CelebA/ArtBench). D-TRAK had weaker contribution (heuristic modifications without explanation) but similar evaluation scope. This paper has a more novel contribution but similar-level fixable gaps. **Comparable, slightly stronger in contribution.** |
| /home/.../XXpH3D0TVP.md (Journey-TRAK) | 5.75 | R1/R2 | Similar topic (data attribution on diffusion models). Rejected mainly for poor presentation and approximations. This paper has better presentation, more thorough evaluation, and a more novel method. **Stronger.** |
| /home/.../esYrEndGsr.md (Influence Functions) | 8.00 | R1 | Superior theoretical framework and rigorous treatment, but limited to smaller-scale experiments (CIFAR-2/10). **Weaker in theoretical depth and evaluation scale.** |
| /home/.../uVMZgtw2pf.md (CHG Shapley) | 4.67 | R2 | Data valuation for supervised learning, not diffusion. Rejected for not showing substantial advantage over baselines. This paper is **substantially stronger.** |
| /home/.../X6tNkN6ate.md (Interpretable Diffusion) | 6.00 | R1/R2 | Different topic (information decomposition in diffusion). Comparable quality but not directly comparable in domain. |

This paper sits between the D-TRAK anchor (6.0) and the Influence Functions anchor (8.0), closer to D-TRAK. It has a more novel contribution than D-TRAK (new problem formulation + Shapley approach vs. heuristic modifications) but shares similar issues of incomplete validation. The weaknesses are real but fixable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>