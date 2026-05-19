- Decision: Reject
- Avg Score: 6.80
- Scores: 6, 6, 8, 8, 6
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper introduces PG-LDS-ID, a novel analytical covariance-based subspace identification algorithm for modeling Poisson processes while dissociating the dynamics shared with Gaussian processes. The method uses a two-stage approach: Stage 1 identifies shared dynamics between both observation streams using a novel cross-covariance moment conversion, and Stage 2 optionally learns residual dynamics unique to the Poisson stream. On simulated data and real NHP neural spiking/movement recordings, PG-LDS-ID shows improved decoding of continuous from discrete observations and better sample efficiency compared to the single-modality PLDSID baseline.

## Strengths

1. **Demonstrated lower-dimensional latent state identification.** In simulations with fixed shared (n₁=4) and residual (n₂=12) dimensions (Figure 1c–d), PG-LDS-ID achieves near-peak performance and accurate mode identification using only 4 latent states, whereas PLDSID requires approximately 16 dimensions. This directly demonstrates the benefit of explicitly modeling the shared subspace.

2. **Superior behavior decoding from neural data.** On the NHP dataset (Section 4.2), PG-LDS-ID achieves higher kinematic prediction correlation at all tested latent dimensions compared to PLDSID (Figure 2a), with statistical significance at n_x=14 (p<0.0005, Figure 2c). Neural self-prediction AUC is maintained at comparable levels (Figure 2b–c), confirming that the improved decoding does not come at the cost of degraded Poisson modeling.

3. **Substantially better sample efficiency.** Figure 1a shows PG-LDS-ID reaches ground-truth predictive performance with ~1e4 training samples, while PLDSID requires ~1e5 samples — an order of magnitude more data. This is a concrete practical advantage.

4. **Novel cross-covariance moment conversion enabling mixed-modality SSID.** Equation (7) provides the key expression relating Cov(z_f, r_p) to observable quantities Cov(z_f, y_p) and μ_y, enabling the construction of the mixed Hankel matrix H_zr (Equation 8). This is the technical core that allows covariance-based SSID to use both Poisson and Gaussian observations.

5. **Noise statistics enforcement via convex optimization.** Section 3.2.3 formulates a convex optimization (Equation 12) that imposes the R=0, S=0 constraints required by the Poisson observation model while ensuring positive semidefiniteness — a gap in prior PLDSID work (Buesing et al., 2012).

## Weaknesses

### Fatal
None.

### Major

1. **The two-stage design choice is not ablated against a joint-model baseline.** The paper compares PG-LDS-ID against PLDSID, which only sees Poisson observations. This shows that *using both modalities during training* helps, but it does not isolate whether the *explicit separation of shared and residual dynamics via the two-stage block structure* is responsible for the gains, versus simply co-training with both signals in a single joint latent space without block structure. The paper's central claim — that the two-stage prioritization drives the reported improvements — would be significantly strengthened by comparing against a variant that learns a single joint latent space (without the block structure) from both observation types and then extracts shared modes post hoc (e.g., via projection onto the subspace best predicting the Gaussian observations). This does not invalidate the method (the paper honestly addresses limitations), but it leaves an important unanswered question about what exactly causes the performance gain.

### Minor

1. **Cross-covariance formula (Equation 7) is presented without justification.** The expression Λ_{z_f r_p} = Cov(z_f, y_p) / μ_{y_p} follows from model assumptions (z and r jointly Gaussian, y Poisson with mean exp(r)), but the derivation is not sketched. A brief note using Stein's lemma or the log-normal moment property would prevent reader confusion and clarify why this identity is exact under the model, not approximate.

2. **The extension-to-other-GLMs claim lacks a concrete example.** Section 5 states the method can be extended to other link functions via the appropriate moment conversion, citing Buesing et al. (2012). While plausible, no concrete example (e.g., Bernoulli observations) or sketch of the required changes is given, making the claim less actionable for prospective users.

3. **Frequency of unstable/non-minimal models is not reported.** Section 4.3 honestly acknowledges that the method may produce unstable or non-minimal models, but the paper does not quantify how often this occurs in either simulations or real data, or how it was handled when it occurred. This would be useful practical information.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing PG-LDS-ID against a jointly-trained (non-block-structured) variant would directly test whether the two-stage prioritization is necessary for the reported gains.
- Reporting the empirical frequency of unstable or non-minimal models across simulation runs and real-data folds.
- On the real-data analysis, a per-session breakdown (rather than pooling across six sessions) could provide additional insight into session-to-session variability.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No comparison against existing multimodal dynamical models (Abbaspourazad et al., 2021; Kramer et al., 2022)"** — REMOVED: These methods do not perform dissociation of shared vs. residual dynamics, which is the paper's core contribution. The paper's baseline (PLDSID) is the relevant state-of-the-art for Poisson SSID. Demanding comparison against methods that solve a different problem exceeds the paper's stated scope.

2. **"Generalizability of horizon specification" (Strength Finder point)** — REMOVED: Supporting distinct horizon values for the two observation streams is a minor implementation detail, not a core strength of the paper.

3. **"Analysis across individual sessions"** — REMOVED: The paper already performs 5-fold cross-validation across six sessions with random channel subsets. The suggestion to show per-session results is a reasonable but speculative nice-to-have, not a concrete weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear methodological gap (lack of ablation for the two-stage design) but offer no fundamentally new analysis or connection that the authors themselves did not identify.

## Suggestions

1. **Add an ablation study** comparing PG-LDS-ID against a variant that learns a single joint latent space (no block structure, no second stage) from both observation types, then extracts shared modes post hoc (e.g., via canonical correlation or by projecting onto the subspace best predicting the Gaussian observations). This directly tests whether the two-stage prioritization is the source of the gains.

2. **Provide a brief derivation of Equation (7)** in Section 3.2.1, referencing that the identity holds exactly under jointly Gaussian z and r via the law of total covariance and the log-normal moment property.

3. **Quantify the frequency of unstable/non-minimal models** encountered in the 50 random simulation runs and in real-data cross-validation folds, and describe how these cases were handled.

4. **Give one concrete example of extending to another GLM family** (e.g., Bernoulli) in Section 5, or cite the specific derivation in Buesing et al. (2012) that would be adapted.
