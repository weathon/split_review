## Summary

This paper introduces FB-CPR, which regularizes unsupervised zero-shot RL based on forward-backward (FB) representations with a distribution-matching objective against unlabeled motion-capture trajectories. The method uses the FB model's own trajectory embedding (ER_FB) to map unlabeled motion data into the same latent space as latent-conditioned policies, then trains a discriminator and critic to minimize the KL divergence between the policy-induced and dataset-induced joint distributions over (state, latent). On a 358-dim SMPL humanoid with realistic physics, FB-CPR achieves 73.4% of single-task specialist performance across reward, goal, and tracking tasks while outperforming ASE by >1.4×, all without any task-specific training or planning at inference time.

## Strengths

1. **Novel algorithmic combination.** The paper is the first to integrate FB zero-shot RL representations with conditional trajectory-level policy regularization. Using ER_FB to embed unlabeled trajectories into the same latent space as policies (rather than learning a separate encoder) is a clean design that ties representation learning and regularization together. This is technically novel and clearly described in Section 3.

2. **Strong empirical results on a challenging benchmark.** FB-CPR is evaluated on a high-dimensional humanoid (358-dim state, 69-dim action, realistic joint limits and torque constraints) with 29 hours of uncurated motion-capture data (AMASS). Across 45 reward tasks, 50 goal-reaching tasks, and 990 test motions, it achieves 73.4% of single-task specialist performance and outperforms ASE by >1.4× on every category — all zero-shot. The comparison includes TD3, Goal-GAIL, PHC, CALM, ASE, DIFFUSER, MPPI, and H-GAP, making this one of the most comprehensive evaluations of a humanoid BFM.

3. **Human evaluation confirms behavioral quality.** A study with 50 human evaluators shows FB-CPR matches TD3's task success rate while being judged as producing significantly more natural/"human-like" motions (Figure 3). This directly demonstrates that the motion-capture regularization yields qualitatively better behavior, not just higher scores — a dimension that raw reward metrics miss.

4. **Systematic ablation study.** Figure 4 ablates four key design choices: (i) latent-conditional vs. state-only discriminator, (ii) with vs. without the FB unsupervised term F^T z, (iii) online vs. offline training, and (iv) scaling with network capacity and dataset size. Each ablation cleanly isolates the contribution of the corresponding component.

5. **Honest discussion of limitations.** Section 5 candidly acknowledges failure modes (motions involving ground contact, unnatural movements during falling/standing), the reliance on expensive motion-capture data, the lack of perception/object interaction, and the absence of theoretical convergence guarantees. This contextualizes the contribution without overclaiming.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Non-stationarity from the self-embedding loop is acknowledged but not analyzed.** The discriminator and critic rely on ER_FB(τ) (which depends on the evolving backward embedding B) to embed dataset trajectories into the latent space. While the Discussion (end of Section 3) claims this "binds FB and policy training together, thus ensuring a more stable and consistent learning algorithm," no evidence or analysis of this stability is provided. The embeddings drift as B is updated, creating a moving target for both the discriminator and the critic. An analysis of the embedding drift over training, or a comparison against periodically recomputing embeddings with a frozen B, would strengthen the paper's claims about algorithmic stability.

2. **Human evaluation only compares against TD3, not against other motion-regularized methods.** The qualitative naturalness comparison shows FB-CPR beats TD3 — but TD3 is a pure reward optimizer with no motion prior, so this is expected. Showing FB-CPR is competitive with or surpasses ASE, CALM, or PHC on human-perceived naturalness would directly support the claim that FB-CPR's specific regularization yields superior behavioral quality over existing BFMs, not just over unregularized RL.

3. **The latent distribution ν is a three-component mixture whose proportions are not specified or ablated.** The paper states ν mixes (1) ER_FB trajectory embeddings, (2) B(s) goal embeddings, and (3) uniform samples, but gives no mixture weights (e.g., in Section 3, "Latent space distribution") and no ablation studying their effect. Since the mixture design is a deliberate algorithmic choice, the relative importance of each component is unclear.

4. **The offline ablation (FB-AW) uses a dataset collected by FB-CPR itself.** The paper's hypothesis is "Is online policy regularization necessary given a large diverse dataset?" To test this, FB-AW is trained on the replay buffer of the FB-CPR agent. While the paper acknowledges that "no dataset with our criterion exists," using FB-CPR's own data conflates two issues: offline optimization difficulty and dataset quality. An offline dataset with broader coverage (e.g., from random exploration or multiple unsupervised agents) would provide a cleaner test of whether online regularization per se is necessary. That said, the current setup is still informative — if offline learning fails even when given data from the same distribution the online agent sees, the case for online training is strengthened, not weakened.

5. **The unsupervised term ablation lacks mechanistic analysis.** The ablation in Figure 4 (top right) shows that including the F^T z term improves performance, but the paper only says FB "is providing much more than just a motion encoder through ER_FB." A discussion of whether this term provides better exploration, sharper policy differentiation, or improved state coverage would make the analysis more informative.

6. **Table 1 uses per-task best-algorithm normalization.** The reported 73.4% normalizes each task's FB-CPR score against the best algorithm for that specific metric (which may be a single-task specialist like PHC for tracking success or TD3 for rewards). While the paper discloses this, it risks overstating relative performance against multi-task methods. Presenting absolute scores alongside normalized ones (which the appendix does) is recommended for the main text.

### Trivial

1. The claim in the abstract of "the first humanoid behavioral foundation model that can be prompted to solve a variety of whole-body tasks" is slightly overbroad given that ASE (Peng et al., 2022) is a published humanoid BFM with zero-shot capability. The paper does acknowledge ASE as the "closest BFM approach" and compares against it extensively, so this is a phrasing issue rather than a substantive error.

2. The KL-to-return conversion in Eq. 8 uses the discounted state distribution, while the discriminator (Eq. 9) is trained on undiscounted samples from the replay buffer. This is a standard approximation (shared with GAIL and related methods) and does not invalidate results, but it should be noted.

3. The computational cost comparison (12 seconds vs. 30 minutes for OracleMPPI) conflates amortized pre-training with inference. The paper reports 3M gradient steps and 30M environment steps for pre-training but does not give wall-clock training time or GPU hours, which would help assess total compute cost.

## Nice-to-Haves

- A per-motion-type breakdown of tracking success (e.g., walking vs. dancing vs. static motions) would clarify where FB-CPR's failures concentrate.
- Reporting absolute scores in Table 1 alongside normalized scores would improve transparency.
- An ablation of the mixture proportions in ν would help understand the contribution of each component.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the FB-AW dataset "inherits the behavioral biases of FB-CPR" making the ablation unfair.** The paper explicitly states "no dataset with our criterion exists" and uses the FB-CPR replay buffer — which, if anything, should favor the offline variant since it comes from the same distribution. The fact that offline learning still fails despite having access to good data from the agent itself actually *supports* the paper's claim about the difficulty of offline optimization. This criticism is factually reversed.
- **Criticism that the paper claims "first humanoid BFM" without acknowledging ASE.** The paper explicitly acknowledges ASE as "the closest BFM approach to ours," compares against ASE throughout, and qualifies the "first" claim by specifying the scope ("that can be prompted to solve... motion tracking, goal reaching, and reward optimization"). The criticism misreads the paper's positioning.
- **Demands for the human evaluation to include "a more informative comparison" against ASE or CALM.** This is a reasonable suggestion (moved to Minor) rather than a structural flaw, since comparison against TD3 — the strongest reward-optimization baseline — is a valid baseline for naturalness.
- **Pure presentation nits** (scaling experiment missing numerical values in figure caption, formatting/style comments).

## Novel Insights

The reviews surface one genuinely interesting tension: the paper claims the self-embedding design (using ER_FB to bind FB and policy training) "ensures a more stable and consistent learning algorithm," but the harsh critic's concern about non-stationarity is well-grounded — the backward embedding B drifts throughout training, which could create a moving target for the discriminator. The paper never resolves this tension. This is an empirically testable question: one could measure how much ER_FB(τ) changes for fixed trajectories as B is updated, or compare against a variant that recomputes embeddings periodically with a frozen B. A positive result (small drift / convergence) would strengthen the paper's methodological contribution; a negative result would point to a meaningful limitation.

## Suggestions

1. **Add a stability analysis of the self-embedding loop.** Measure the drift of ER_FB(τ) for held-out trajectories over the course of training, or compare the current online scheme against periodic re-embedding with a frozen backward encoder. This would address the most substantive methodological concern.
2. **Add a human evaluation comparing FB-CPR against at least one other motion-regularized BFM (ASE or CALM).** This would directly support the claim that FB-CPR's specific regularization yields superior behavioral quality, not just improvement over unregularized RL.
3. **Specify the mixture proportions for ν and ideally ablate them.** The three-component latent distribution is a deliberate design choice whose relative weighting is currently opaque.

## Score and Decision

This paper presents a novel, well-motivated algorithm and backs it with extensive experiments on a realistic and challenging humanoid benchmark. The main results — outperforming ASE by 1.4× and achieving 73.4% of single-task specialist performance across reward, goal, and tracking tasks — are credible and represent a clear advance for zero-shot humanoid BFMs. The identified weaknesses (unanalyzed non-stationarity, incomplete human evaluation, unablated latent distribution) are genuine but minor; none threaten the core claims. The paper makes a solid contribution.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>