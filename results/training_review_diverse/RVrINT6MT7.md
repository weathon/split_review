Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me compile the final review.

## Summary

This theoretical paper derives mathematical conditions under which offline reactivation (sampling of task-like neural states during quiescence) emerges in noisy recurrent neural networks optimized to track smoothly varying stimuli from change-based sensory input. The authors show that greedily optimal dynamics decompose into an integration term and a denoising term (Langevin sampling of the state distribution), and validate the prediction that quiescent distributions match active distributions through numerical experiments on spatial navigation and head direction estimation tasks.

## Strengths

- **Rigorous mathematical derivation connecting optimal tracking to Langevin sampling in quiescence**: The paper derives an upper bound on the loss (Eq. 9) that separates into signal tracking and noise compensation terms, solves for greedy optimal dynamics (Eq. 19), and shows that under quiescence (zero velocity input, doubled noise) these dynamics reduce to Langevin sampling of the active state distribution \(p(\mathbf{r})\) (Section 2.4). This provides a clear set of conditions under which the stationary distribution of quiescent neural activity exactly matches the active distribution, giving a principled theoretical foundation for emergent reactivation.

- **Quantitative validation of distributional matching via KL divergence**: The Monte Carlo KL divergence metric (Fig. 2e) shows that quiescent decoded outputs have a divergence from the active distribution close to zero (0.05 nats for unbiased training), far lower than comparisons to uniform (1.65 nats), random (2.55 nats), or cross-distribution (biased vs. unbiased, 0.47 nats) baselines. This quantitatively establishes that quiescent activity statistically recapitulates the active experience distribution, not just a generic attractor.

- **Demonstration that noisy training is necessary for stable, space-tiling quiescent exploration**: Networks trained without noise produce quiescent trajectories with low total variance (Fig. 2f), and adding noise during quiescence to noiselessly-trained networks yields erratic, non-smooth trajectories (Suppl. Fig. C.3e-f, C.4a-b). In contrast, networks trained with noise produce smooth, variable quiescent trajectories that tile the task manifold, confirming the functional role of learned denoising dynamics in generating proper reactivation.

- **Generality across two ethologically relevant tasks and architectures**: Reactivation is reproduced in both 2D spatial position estimation (path integration, Fig. 1) and 1D head direction estimation (angular velocity integration, Fig. 3), and results hold for continuous-time GRUs (Suppl. Fig. C.2), demonstrating the phenomenon is not specific to a single task or architecture.

- **Correspondence of biased behavioral sampling to quiescent distributions**: When the agent's training trajectories are biased to a ring-shaped region (Fig. 2a), the quiescent decoded outputs concentrate on the same ring (Fig. 2b), and KDEs are closely aligned (Fig. 2c-d). This confirms that reactivation reflects the statistics of actual experience rather than being an artifact of uniform exploration.

- **Clear connection to neuroscience circuits and explicit framing relative to prior work**: The paper ties the spatial task to grid-cell models in entorhinal cortex and the head direction task to anterodorsal thalamus—both circuits where reactivation is empirically observed. It also distinguishes its emergent-reactivation hypothesis from generative-modeling alternatives, noting a testable difference: the former predicts matching stationary distributions, while generative models predict matching transition statistics as well.

## Weaknesses

### Fatal
None.

### Major

- **The mechanism predicted by theory is not verified in trained networks**: The derivation assumes the network implements the greedy optimal dynamics (computing the score function \(\nabla_{\mathbf{r}}\log p(\mathbf{r})\) and using \(\mathbf{D}^\dagger df/d\mathbf{s}\)). However, the numerical experiments use standard RNNs trained with gradient descent on MSE, not networks constructed to follow the derived equations. There is no analysis of learned weights, no comparison of the actual update rule to the predicted form, no drift-field analysis, and no perturbation experiments to show trained networks implement the proposed decomposition. The observation that quiescent distributions match active distributions is consistent with the theory but also with simpler explanations (e.g., diffusion on a learned attractor manifold). The paper validates the *prediction* but not the *mechanism*, leaving a significant gap between the theoretical and empirical contributions.

- **The "sufficient conditions" framing exceeds what the derivation supports**: The title and abstract assert sufficient conditions for reactivation, but the derivation proceeds through a series of approximations: a decomposition of \(\phi\) into \(\Delta\mathbf{r}_1 + \Delta\mathbf{r}_2\) (assumed, not derived), Taylor expansion, triangle inequality, Cauchy-Schwarz, and Jensen to produce an upper bound, followed by separate greedy optimization of each term. The result is a "heuristic solution" (Section 2.3) that is then treated as the basis for the main conclusion. While the mathematical derivation within its stated assumptions is sound, the claim of "sufficient conditions" would be more accurate if qualified as "conditions under which reactivation is expected given the greedy heuristic and idealized approximations." The paper acknowledges greediness but the framing in the title and abstract does not reflect this caveat.

### Minor

- **Head direction results are qualitative only**: Unlike the spatial navigation task, no quantitative measure of distribution overlap (e.g., KL divergence) is provided for the head direction task (Fig. 3). The distributions are described as "closely corresponding" based on visual inspection alone, which is weaker evidence than the spatial navigation analysis.

- **KL divergence results lack error bars or significance tests**: Figure 2e reports KL divergence values averaged over 5 networks without confidence intervals, making it difficult to assess the variability or statistical significance of the reported differences. While error bars are shown in other panels (Fig. 1b-c), their absence for the central quantitative metric weakens the claim.

- **The denoising solution assumes access to the score function of the marginal activity distribution**: The optimal \(\Delta\mathbf{r}_1^* = \sigma^2 \nabla_{\mathbf{r}} \log p(\mathbf{r}) \Delta t\) requires the network to compute the gradient of log-probability of its own activity distribution. This is a non-trivial computation whose biological or mechanistic implementation is not discussed. The paper cites this as a "well-known solution" from denoising theory, but in the context of a neural circuit, the implicit computation is substantial.

### Trivial
None.

## Nice-to-Haves

- A quantitative distribution-overlap metric (KL divergence or similar) for the head direction task would strengthen the claim of generality to the same evidentiary standard as the spatial task.
- Reporting decoding error (position/head direction) for trained networks would confirm the "near-optimal" performance assumed by the theory — note that Fig. 1b does report training loss and decoding error, so this concern is partly addressed, but final converged values could be stated explicitly in the main text.
- A discussion or simple analysis of what the score function of \(p(\mathbf{r})\) would look like in a trained network, or how it could be approximated by biologically plausible circuits, would strengthen the connection to neural implementation.

## Removed Points

These points were raised by reviewers but are not valid weaknesses upon verification against the paper:

- **"Task performance not reported"**: Incorrect. Fig. 1b shows place cell tuning MSE and position decoding spatial distance error as functions of training. Task performance metrics are present.
- **"No comparison to simpler predictors"**: Incorrect. The paper compares quiescent distributions to uniform, random network, and cross-distribution baselines (Fig. 2e), which serve as proper controls.
- **"Noise doubling is critical and biologically unmotivated; undermines theoretical guarantee"**: The paper explicitly states (Section 2.4, line 137) that the factor of 2 "is necessary only to produce sampling from the exact same distribution" and that "different noise variances will result in sampling from similar steady-state distributions with different temperature parameters." It also notes that empirical results "hold whether or not we increase the variance of noise during quiescence" (Section 4). The paper is fully transparent about this assumption and its role.
- **"Continuous attractor models already understood diffusion produces replay; the claim they lack rigorous justification is inaccurate"**: The paper's claim is that *emergent* (non-generative) modeling approaches lack rigorous mathematical justification for **why reactivation emerges from task optimization** — not that attractor dynamics are themselves unstudied. The Discussion (line 192) explicitly cites Burak & Fiete (2009) and Khona & Fiete (2022) as attractor models and positions the current work as *complementing* these studies by providing a mathematical justification derived from optimal task performance. The critic's reading conflates two different claims.
- **Missing related works**: Hard rule — cannot be confirmed without external sources.
- **Formatting, style, and typographical nitpicks**: Hard rule — parser artifacts, not author errors.

## Novel Insights

The reviews surface a genuine tension in how to evaluate this paper. The harsh critic points out a real and significant gap: the paper validates the *prediction* (matching distributions) but not the *mechanism* (whether trained networks actually implement the derived score-based denoising dynamics). This is not a fatal flaw for a theoretical paper with supporting experiments — many such papers in neuroscience make predictions based on idealized reasoning and validate them at the phenomenological level — but it is a genuine limitation that the paper could address with additional analyses. The most insightful observation is that the paper's claim of "sufficient conditions" is somewhat outsized relative to the heuristic nature of the derivation; the contribution is better described as a plausible mathematical account of how reactivation *could* arise from task optimization, rather than a definitive theorem. The strengths identified by the positive assessment — particularly the KL divergence quantification and the biased-training experiment — are genuine and well-supported. The net assessment depends on whether one weighs the theoretical framing against the mechanistic gap: the theoretical derivation is sound within its assumptions, but the link to trained networks is phenomenological rather than mechanistic.

## Suggestions

1. **Bridge the mechanism gap**: Analyze the learned weights or dynamics of trained networks to check whether they approximate the derived form. For example, compute the drift field of the RNN dynamics and compare the component orthogonal to the output mapping to the predicted score-function-based denoising term. Alternatively, ablate the putative denoising component (e.g., by clamping the update in the direction orthogonal to the integration term) and show the predicted effect on quiescent activity.

2. **Qualify the framing**: Adjust the title and abstract to reflect that the conditions are "plausible sufficient conditions under idealized approximations" or "conditions under which reactivation is expected to emerge" rather than simply "sufficient conditions." This would make the contribution more defensible and more honest about the heuristic nature of parts of the derivation.

3. **Add quantitative metrics for head direction**: Provide KL divergence or angular histogram overlap measures for the head direction task to match the evidentiary standard of the spatial navigation analysis.

4. **Report error bars for the central KL divergence result**: Add confidence intervals or error bars to Fig. 2e to communicate variability across the 5 trained networks and strengthen the statistical claim.

## Score and Decision

This paper makes a genuine theoretical contribution by showing that optimal noisy tracking naturally produces Langevin sampling dynamics in quiescence — a clean mathematical result that connects task optimization to reactivation phenomena. The derivation is sound within its stated assumptions and the experimental validation is partially successful, with quantitative KL divergence evidence for the spatial task and qualitative evidence for head direction. However, the paper has two significant limitations that prevent a recommendation for acceptance: (1) the central claim of "sufficient conditions" is somewhat stronger than the heuristic derivation warrants, and (2) there is a substantial gap between the theory and the trained networks — the predicted mechanism is not verified, only the phenomenological prediction. These are addressable with additional analysis, but in the current form the paper overclaims relative to its evidence. The paper would need either tighter theoretical framing or mechanistic validation of the proposed dynamics to be acceptable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>