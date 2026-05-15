Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper develops a mathematical framework establishing sufficient conditions for "diffusive reactivation" in recurrent neural networks: under noisy continuous-time dynamics, near-optimal state estimation from change-based inputs, and a noise increase during quiescence, the quiescent dynamics become Langevin sampling of the active-state distribution. The authors validate on spatial position estimation and head direction estimation tasks, showing that decoded output distributions during quiescence approximately match those during active behavior, and that noisy training is needed for exploratory quiescent trajectories.

## Strengths

1. **Well-derived mathematical conditions linking optimal denoising to Langevin sampling.** The derivation from Eq. 7 through Eq. 14 is clear: the loss upper bound separates into a signal-tracking term (L_signal) and a denoising term (L_noise), and the greedily optimal denoising update Δr₁*(t) = σ²∇log p(r)Δt is the known minimum MSE estimator for additive Gaussian noise. The observation that this term, combined with the absence of input and doubled noise, yields Langevin sampling of p(r) is mathematically elegant and provides a non-generative explanation for distributional reactivation.

2. **Quantitative validation of distribution matching via KL divergence.** Fig. 2e reports KL divergence between active and quiescent decoded output distributions across multiple conditions (unbiased, biased, random networks, true uniform), with box plots over five networks. Biased quiescent outputs closely match biased active outputs (low KL), while cross-condition comparisons diverge — directly confirming the theory's central prediction that quiescent activity reflects the statistics of active experience, not some default attractor.

3. **Empirical evidence that noisy training is necessary for exploratory reactivation.** Networks trained without noise produce quiescent trajectories with low variance that fail to explore the task manifold; adding noise post-hoc to these networks produces erratic, non-smooth trajectories (Suppl. Fig. C.3–C.4). Only networks trained *with* noise produce smooth, exploratory quiescent trajectories (Fig. 2f). This is a non-trivial observation that supports the claim that learned denoising dynamics are key.

4. **Generalization across tasks, architectures, and behavioral policies.** Results hold for both 2D spatial navigation (path integration) and 1D head direction estimation (Fig. 1, 3), for both vanilla RNNs and GRUs (Suppl. Fig. C.2), and for both uniform and ring-biased behavioral policies (Fig. 2a–d). The biased-condition experiment is particularly strong: it shows that reactivation is experience-dependent, not just a fixed attractor.

5. **Clear articulation of how the theory can be experimentally dissociated from generative models.** The Discussion (Section 5, last paragraph) notes that generative models predict matching of moment-to-moment transition statistics, while the presented theory only predicts matching of the stationary distribution — offering a concrete experimental test.

## Weaknesses

### Fatal
None.

### Major

1. **The theory derives dynamics for an idealized system, but does not verify that trained RNNs implement those specific dynamics.** The derivation optimizes an upper bound (via triangle inequality) of a Taylor-expanded loss using a greedy, per-timestep heuristic. The resulting dynamics Δr*(t) = σ²∇log p(r)Δt + D†(df/ds)Δs require that (a) the network update decomposes into independent denoising and tracking functions, (b) the network state already satisfies r(t) ≈ D†f(s(t)), and (c) the denoising term uses ∇log p(r) — a global quantity. These are *assumptions* of the derivation, not consequences of training. The paper validates the predicted *outcome* (distribution matching) but never directly probes whether trained networks actually implement the predicted functional form of the dynamics (e.g., by regressing Δr against the score function and the input-driven term). Without this link, the paper establishes that the conditions are *sufficient* for reactivation in an idealized system, but not that task-optimized networks actually use this mechanism. This gap weakens the explanatory claim implied by the title and abstract.

2. **Noiseless-trained networks still exhibit distribution matching (Fig. 2e), undercutting the claim that noisy training is a necessary condition for the proposed mechanism.** The paper acknowledges this ("networks trained in the absence of noise still learned attractive task manifolds") and pivots to the exploration-variance argument (Fig. 2f). But this is an admission that the core distribution-matching phenomenon occurs even without the theoretical mechanism (noise-driven denoising dynamics). If distribution matching is also observed in noiseless networks, then the Langevin sampling account is not the unique or even primary explanation — there is a simpler attractor-based explanation. The paper does not sufficiently reconcile this.

3. **The acknowledged discrepancy that quiescent activity "does not tile space as uniformly" as active activity is not explained, yet the theory predicts exact distributional equivalence (p̃(r) = p(r)).** The paper notes this discrepancy (Section 4, Spatial Position Estimation) but offers no analysis of its cause — whether it is due to finite sampling time, discretization error, or a failure of the greedy heuristic. For the central claim of the paper, this discrepancy matters: the theory predicts exact match, the data show approximate match with systematic bias, and the reason is left unaddressed.

4. **Head direction results (Fig. 3) are presented qualitatively only.** Unlike the spatial task, no KL divergence or other distributional metric is reported for the head direction task. Given that the paper sets a quantitative standard (KL divergence) for the spatial task, the absence of a comparable metric for the head direction task weakens the claim of generality. The biased-motion experiment (Suppl. Fig. C.5) also shows only partial temporal structure with reversals — the language "demonstrate that... sequential reactivation dynamics" overstates what is shown.

### Minor

1. **The "random network" baseline is not clearly defined in the main text** — are these untrained, randomly initialized networks? How are their quiescent trajectories generated? This information may be in the supplement but the main text should be self-contained on this point.

2. **The noise-doubling assumption, while acknowledged as non-catastrophic to deviate from ("Different noise variances will result in sampling from similar steady-state distributions with different temperature parameters"), lacks biological motivation.** The paper applies doubled noise as a design choice in experiments, not as a prediction verified in trained networks. This weakens the claim that these are *emergent* sufficient conditions — one condition is manually set rather than emerged.

3. **No direct probing of whether trained networks' Δr(t) matches the predicted analytical form.** The paper could have compared the empirical Δr(t) in trained networks to the predicted σ²∇log p(r)Δt + D†(df/ds)Δs via regression, but does not. This is a natural experiment to bridge the gap between theory and mechanism.

### Trivial
None.

## Nice-to-Haves

- Report a distributional metric (e.g., KL divergence or autocorrelation) for the head direction task to match the quantitative standard of the spatial task.
- Probe whether the score function ∇log p(r) can be read out from the learned recurrent weights, to assess biological plausibility.
- Analyze why the quiescent distribution does not tile space as uniformly as the active distribution — is this a finite-time effect, discretization artifact, or consequence of the greedy heuristic?

## Removed Points

The following criticisms from the harsh reviewer were removed per policy:

1. **"The paper's definition of 'reactivation' is too weak and largely disconnected from the neuroscience phenomenon"** — The paper explicitly qualifies its contribution as *"a certain type of reactivation — diffusive reactivation"* (line 18), acknowledges that *"our theory does not yet explain how this phenomenon [temporal structure] emerges"* (line 190), and provides experimentally testable dissociations from generative models. The paper engages with real reactivation phenomena (Kenet et al., Peyrache et al., Gardner et al.) that include distributional matching, not just sequential replay. The criticism overstates what the paper claims.

2. **"The paper does not engage with Burak & Fiete 2009, Khona & Fiete 2022 in mathematical depth"** — The paper cites these works in the Discussion (line 192) and frames its contribution as complementary (*"our work complements these previous studies by providing a mathematical justification for the emergence of reactivation dynamics in terms of optimal task performance"*). The depth of engagement is a judgment call, not a factual error.

3. **"The KL divergence may not be sensitive enough to distinguish subtle differences"** — Speculative; no evidence is provided that the KL estimates are unreliable.

4. **"No amount of additional experiments can prove that a black-box trained network implements a particular functional form"** — This is an overly strong epistemological claim that prescribes what counts as valid evidence rather than identifying a concrete flaw.

5. **"The resulting distribution is not a fixed Gaussian mixture... The assumption that p(r(t)|s) ∼ N(D†f(s), σ²Δt) is plausible only if denoising has already been perfectly achieved, which is circular"** — The paper acknowledges this as an assumption (Section 2.2: *"we will assume that this optimization has been successful for previous timesteps"*). This is a standard approximation in greedy optimization analyses, not a hidden flaw.

## Novel Insights

The most valuable observation across the reviews is that the paper's theoretical contribution (linking optimal denoising under change-based integration to Langevin sampling) and its empirical contribution (showing distribution matching in trained RNNs) are not as tightly coupled as the paper implies. The derivation tells us what an *idealized* optimal network would do; the experiments tell us that trained *black-box* networks exhibit some of the predicted phenomena. But without directly verifying the dynamical mechanism, the paper cannot rule out alternative explanations (e.g., attractor dynamics learned independently of denoising). The KL divergence results for noiseless-trained networks further support the possibility of simpler explanations. Closing this explanatory gap — either by probing the internal dynamics or by ablating the score-function term — would transform an interesting but incomplete story into a compelling one.

## Suggestions

1. **Directly probe the dynamics** by regressing empirical Δr(t) from trained networks against the predicted terms (σ²∇log p(r)Δt and D†(df/ds)Δs). This would test whether trained networks actually implement the derived mechanism or arrive at distribution matching through other means.

2. **Report a quantitative metric for the head direction task** (e.g., circular KL divergence or autocorrelation decay) to match the standard set for the spatial task.

3. **Analyze the cause of the imperfect tiling** of quiescent trajectories — is it finite-time undersampling, a consequence of the greedy approximation, or something else? This would strengthen rather than weaken the paper.

4. **Soften the claim about noisy training being a "condition"** for the mechanism, given that noiseless-trained networks also exhibit distribution matching. The paper could more precisely state that noise is necessary for *exploratory* (high-variance) reactivation but not for distribution matching per se.

## Score and Decision

This paper makes a genuine conceptual contribution — linking optimal denoising in state estimation to offline Langevin sampling provides a new way to think about reactivation that is distinct from generative modeling. The mathematical derivation is clear, the experiments span two relevant tasks, and the biased-policy experiment is a strong test. However, the gap between the idealized theoretical derivation and the black-box trained networks is significant: the paper does not verify that trained networks implement the specific dynamics it derives, and the noiseless-trained result suggests the distribution matching may have a simpler explanation. These are addressable in revision but currently weaken the paper's central claim. I recommend acceptance conditional on addressing the mechanism gap and adding quantitative results for the head direction task.

**Score**: 6.0  
**Decision**: Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>