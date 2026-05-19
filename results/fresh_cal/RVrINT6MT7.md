Now I have thoroughly read and analyzed the paper. Let me compose the final consolidated review.

---

## Summary

This paper derives sufficient mathematical conditions under which noisy recurrent neural networks, optimized for state estimation from change-based sensory inputs, naturally exhibit offline reactivation — revisiting the same distribution of neural states during quiescence as during active behavior. The key theoretical result (Section 2.4) shows that optimal greedy denoising dynamics during active processing become Langevin sampling of the active state distribution when inputs are absent and noise variance is increased. This is validated through numerical experiments on spatial position estimation and head direction estimation tasks, with quantitative distributional comparisons (KL divergence, explained variance, KDE overlap).

## Strengths

- **Rigorous mathematical derivation of sufficient conditions for distributional reactivation**: Section 2.4 derives that under stated assumptions (noisy continuous-time dynamics, change-based inputs, near-optimal tracking), quiescent dynamics become Langevin sampling of the active state distribution \(p(\mathbf{r})\). This provides a formal foundation that prior emergent models of reactivation lacked, as the paper correctly notes most previous approaches "lack rigorous mathematical justification."

- **Quantitative validation across two ethologically relevant tasks with multiple measures**: Figure 2e reports KL divergence values between active and quiescent decoded output distributions (unbiased, biased, and baseline comparisons). Figures 1c and 3a-d show overlapping explained variance curves and similar projected neural trajectories for both spatial position and head direction tasks. The use of KDE comparisons, PC projections, and decoded trajectory visualizations provides converging evidence.

- **Decomposition of the loss into signal and noise terms with closed-form optimal updates**: Equations 10–13 partition the upper-bound loss into \(\mathcal{L}_{\text{signal}}\) (tracking the target function's gradient) and \(\mathcal{L}_{\text{noise}}\) (score-function denoising). This mechanistic decomposition explains why reactivation emerges without an explicit generative objective, connecting to established results in denoising and score matching.

- **Demonstration that biased behavioral statistics during training produce corresponding biases in quiescent activity**: Figure 2a–d shows that a drift in the agent's motion policy during training (occupying a ring rather than uniform space) is faithfully reflected in quiescent decoded trajectories, quantified by elevated KL divergence for mismatched comparisons. This provides a testable prediction distinguishing this framework from hand-crafted attractor models.

- **Identification of the distinct role of noise during training**: The noiseless-training control (Fig. 2f, Suppl. Fig. C.3–C.4) shows that networks trained without noise exhibit lower exploration variance and that adding noise to untrained networks produces erratic trajectories, establishing that noise during training stabilizes quiescent dynamics.

## Weaknesses

### Fatal

None.

### Major

- **The paper conflates distributional reactivation (proven) with the temporally structured sequential replay that motivates much of the neuroscience discussion.** The introduction opens with hippocampal replay and sequential reactivation in prefrontal, sensory, and motor cortices — phenomena involving compressed temporal sequences with specific transition structures. The theoretical result (Section 2.4) proves that the *stationary distribution* of neural states during quiescence matches the active distribution: \(p(\mathbf{r}) = \tilde{p}(\mathbf{r})\). This is a claim about distributional equivalence, not temporal sequence structure. Langevin sampling generates trajectories whose transition structure is purely diffusive, not temporally correlated in the way true hippocampal replay is. The paper does acknowledge this in the Discussion (line 190: "Note that though we empirically observe reactivation that mimics the moment-to-moment transition structure... our theory does not yet explain how this phenomenon emerges") and introduces "diffusive reactivation" (line 18) to scope the contribution. However, the abstract, early framing, and title do not carry this qualification forward with sufficient prominence. A reader could reasonably infer the paper explains sequential replay, which it does not. This is fixable with honest reframing but, as written, creates a mismatch between motivation, claims, and results.

*Severity: This is a real scope-vs-framing gap. The paper's actual contribution (rigorous conditions for distributional reactivation) is valuable and well-supported; it simply needs to be presented more precisely from the abstract onward.*

- **The KL divergence results (Fig. 2e) are presented without error bars or statistical tests.** The paper states "unbiased quiescent outputs were almost as close to unbiased active outputs as a true uniform distribution" and "values are averaged over five networks," but does not report variability, confidence intervals, or statistical significance for any of the KL divergence comparisons. Given that this is the primary quantitative measure of distributional match — and that the paper uses it to draw conclusions about biased vs. unbiased conditions — the absence of uncertainty quantification weakens the evidential force. Error bars are provided for the explained variance curves (Fig. 1c), so the authors clearly have the capability; this should be extended to the KL divergence metrics.

### Minor

- **The derivation's upper bounds are applied without any assessment of their tightness.** The analysis proceeds through: (a) Taylor expansion to first order in \(\Delta t\), (b) triangle inequality, (c) Cauchy-Schwarz inequality, (d) Jensen's inequality, (e) greedy optimization ignoring temporal dependencies, and (f) the approximation \(\mathbf{r}(t) \approx \mathbf{D}^\dagger f(\mathbf{s}(t))\). Each step is individually reasonable, but the cumulative looseness of the final bound \(\mathcal{L}_{upper}\) relative to the original loss \(\mathcal{L}\) is never examined. The paper then treats the optimal dynamics derived from \(\mathcal{L}_{upper}\) as the "greedily optimal" dynamics for the original problem, but these are only guaranteed to minimize an upper bound. The numerical experiments showing that trained networks exhibit the predicted behavior provide indirect support, but the paper does not check whether the trained networks' internal updates actually contain a term proportional to \(\sigma^2 \nabla_{\mathbf{r}} \log p(\mathbf{r})\) — which would be a direct and informative verification. This is common practice in theoretical neuroscience papers (derive, then validate empirically), so it is not a fatal gap, but it leaves the mechanistic claim less directly supported than it could be.

- **The doubled-noise assumption is needed for exact distributional equivalence but is not well-motivated biologically.** The paper acknowledges (line 137) that "Different noise variances will result in sampling from similar steady-state distributions with different temperature parameters" and notes results hold without doubling (Suppl. Fig. C.1). However, the paper never quantifies how similar the distributions are at different noise levels. A sweep of noise variance values with associated distributional divergence (KL or other) would strengthen the claim that the factor-of-2 is a convenience rather than a requirement. Additionally, the biological plausibility question — are quiescent states genuinely noisier than waking states? — is not addressed. This is a methodological gap rather than a fatal flaw, but it reduces the precision of the claimed theoretical guarantee.

- **The GRU robustness discussion is brief and under-analyzed.** The paper notes (line 174) that "GRUs were more sensitive to increases in quiescent noise, and other architectures would require more hyperparameter tuning," but does not explore why or quantify the sensitivity. If the denoising-during-quiescence mechanism is architecture-dependent, this limits the generality of the sufficient conditions. A brief analysis of what architectural features drive the sensitivity would strengthen the claims.

### Trivial

- The explained variance curves in Figure 1c are described as "highly overlapping," but no quantitative measure of overlap (e.g., area between curves, number of PCs to reach 90% variance) is provided. A simple numeric comparison would make this claim more precise.
- Line 12 contains a typo ("offilne" should be "offline"). Line 123 contains garbled characters ("cahnay ntgraeis niend t hnee tstwaotre kv apriaabalbi") that appear to be PDF extraction artifacts.

## Nice-to-Haves

- **Direct verification of the predicted denoising dynamics in trained networks**: The theory predicts that during active processing, the network's update contains a term proportional to \(\sigma^2 \nabla_{\mathbf{r}} \log p(\mathbf{r})\). This could be tested by estimating the score function from the empirical distribution of network states and comparing it to the actual updates. This would bridge the gap between the derived optimal solution and what trained networks actually implement.
- **Quantification of the effect of noise scale on distributional match**: A sweep of quiescent noise variance values (from 0 to, say, 3\(\sigma\)) with associated KL divergence between active and quiescent distributions would address how critical the factor-of-2 assumption is.
- **Statistical testing for KL divergence comparisons**: Adding error bars or confidence intervals to Figure 2e, or reporting a permutation test for the null hypothesis that active and quiescent distributions are identical.

## Removed Points

The following points from the inputs were removed with justification:

- **"The noiseless training experiment reduces the force of the claim because reactivation occurs via other mechanisms"** — Removed. The paper identifies sufficient, not necessary, conditions. Sufficiency is not diminished by the existence of alternative mechanisms, and the critic themselves said "this is not a flaw."
- **"The derivation's approximations are a structural flaw"** — Downgraded to Minor. The paper validates empirically, which is the standard approach in theoretical neuroscience. The approximations are individually justified, and the empirical results support the conclusion.
- **"The paper cannot be independently verified because the appendix is missing"** — Removed per instructions. Appendix material exists in the original submission; the PDF extraction tool strips these sections.
- **Generic strengths about "addressing an important problem" or "interesting question"** — Removed from Strengths per instructions. Only strengths with specific, concrete evidence are retained.
- **"The paper should discuss connections to score-based generative models"** — Removed. This is a framing suggestion, not a weakness, and the paper already contextualizes its contribution relative to generative models in the Discussion.

## Novel Insights

The novel insight emerging from synthesizing the reviews is that the paper's core framing tension — between the broad "reactivation" terminology and the specific "distributional matching" result — actually points toward a potentially deeper contribution than either reviewer fully articulated. The paper's explicit dissociation in the Discussion (generative models predict transition statistics; this theory only predicts stationary distribution matching) suggests a concrete experimental test to distinguish these hypotheses, which is a stronger contribution than either review described individually. The fact that Langevin sampling of the active distribution during quiescence arises naturally from optimal denoising dynamics — without any explicit generative training objective — is a clean connection between normative theory (optimal state estimation) and emergent network behavior that has not been made in prior work.

## Suggestions

1. **Reframe the contribution more precisely from the abstract onward.** Explicitly state at the beginning that the paper provides sufficient conditions for *distributional* reactivation (stationary distribution matching) and that temporally structured sequential replay is observed empirically but not yet explained theoretically. The Discussion already does this; the abstract and introduction should follow suit.

2. **Add error bars or confidence intervals to the KL divergence results (Fig. 2e).** As the primary quantitative evidence for distributional matching, these need uncertainty quantification. Even simple standard deviation bars over the five network seeds would substantially strengthen the claim.

3. **Report a quantitative measure of the overlap between active and quiescent explained variance curves in Fig. 1c** (e.g., area between curves, or the number of PCs needed to reach 90% variance explained in each condition).

4. **Perform a noise-scale sensitivity analysis** for the quiescent noise variance, reporting distributional divergence (KL or other) as a function of the noise multiplier. This would address the doubled-noise concern directly.

5. **Consider verifying the presence of the score-function term** (\(\sigma^2 \nabla_{\mathbf{r}} \log p(\mathbf{r})\)) in the trained networks' internal dynamics during the active phase, as this would provide a direct mechanistic link between theory and simulation.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>