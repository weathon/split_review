## Summary

This paper proposes Diffusion Actor-Critic (DAC), a method that reformulates KL-constrained policy iteration for offline RL as a diffusion noise regression problem. It derives that the optimal constrained policy's score function decomposes into the behavior policy's score plus a Q-gradient term, leading to a tractable noise regression objective with "soft Q-guidance" (scaling the Q-gradient by the noise level). The method directly represents the target policy as a diffusion model without requiring density estimation of either policy, and uses LCB of Q-ensembles for stable critic learning. Experiments on D4RL benchmarks show strong results on locomotion tasks and competitive performance on antmaze.

## Strengths

- **Principled theoretical derivation (Section 3.1, Eq. 8–14):** The paper provides a clean, self-contained derivation showing how the KL-constrained policy iteration solution connects to a diffusion noise regression objective. The connection between the Lagrangian solution (Eq. 8), the score function decomposition (Eq. 10–11), and the final tractable noise regression loss (Eq. 14) is well-motivated and correctly carried out. This is a genuine conceptual contribution that bridges the gap between policy-regularized RL and diffusion models without requiring explicit density estimation.

- **Soft Q-guidance mechanism with clear motivation (Eq. 14, Figure 1):** The insight that the Q-gradient should be scaled by the noise level √(1-ᾱₜ) is well-motivated by the derivation, and the 2D bandit example (Figure 1) provides concrete visual evidence that soft Q-guidance keeps actions within the behavior support while hard Q-guidance and denoised Q-guidance produce OOD actions. This is a distinct improvement over prior guidance approaches.

- **LCB value target with informative ablation (Table 2, Section 3.2):** The LCB approach for Q-ensemble targets is a clean alternative to the ensemble minimum, and the ablation (Table 2) convincingly shows that LCB prevents the catastrophic collapse seen with the minimum operator on halfcheetah tasks (e.g., halfcheetah-medium-expert: 99.1 with LCB vs. 43.2 with Min), while maintaining comparable performance on hopper tasks.

- **Strong empirical results on locomotion tasks (Table 1):** The paper achieves a locomotion-v2 total of 836.4, substantially ahead of the best prior method (DQL at 791.2). The improvements on medium datasets (halfcheetah-m: 59.1 vs. 51.1, hopper-m: 101.2 vs. 90.5, walker2d-m: 96.8 vs. 87.0) are large and consistent, and the paper reports its own results with standard deviations across seeds.

## Weaknesses

### Fatal
None.

### Major

- **The antmaze-large underperformance is not adequately explained or addressed.** On antmaze-large-play, DAC scores 50.3 vs. IDQL-A's 63.5 (a 21% relative gap); on antmaze-large-diverse, DAC scores 55.3 vs. 67.9 (19% gap). The paper's explanation — that prior methods "tune the rewards by subtracting a negative number" — is entirely speculative and unsupported by any controlled experiment (line 211–212). If this single preprocessing choice causes a 10+ point gap, the authors should either verify this by running DAC with the same preprocessing or provide a different explanation. As presented, this pattern suggests a systematic weakness in sparse-reward, long-horizon settings that the paper does not analyze or acknowledge as a limitation.

- **The comparison methodology for the central SOTA claim relies on numbers from published tables under unknown evaluation protocols.** The paper states it "report[s] the best results from their own paper or tables in the recent papers" (line 209) and reports its own results "after convergence" (line 213). This means baseline numbers were generated under potentially different protocols (number of seeds, evaluation episodes, early stopping vs. final performance), and no confidence intervals are provided for any baseline. While citing table numbers is standard practice, the paper's headline claim of "an average increase of over 5%" and the explicit "state-of-the-art baseline" framing (line 27) demand a more controlled comparison to be fully persuasive.

### Minor

- **The surrogate objective approximation (substituting π* with the behavior dataset D) is noted but its implications in the diffusion setting are not discussed.** The paper substitutes the expectation under π* with the behavior data D (line 122–124), following the standard approach in policy-regularized methods. However, unlike AWAC where the exp(Q/η) weight adapts the importance, here the noise predictor is trained on perturbations of behavior actions while the target noise e* is defined w.r.t. π*. The paper provides no analysis of this approximation error or conditions under which it is valid. This is a real evidential gap, though it does not invalidate the method given the empirical results.

- **The Q-function extension to R^d is mentioned but not constructed.** The paper says functions are "smoothly extend[ed]" to R^d (line 110) but provides no explicit construction. Since the denoising trajectory passes through points x_t that can be far from the action space A, and neural network Q-gradients at such points have no formal guarantees, the theoretical grounding of the guidance term at high noise levels is incomplete. The soft Q-guidance scaling partially mitigates this in practice, but the paper should acknowledge this gap directly.

- **No runtime or inference speed measurements are provided**, despite listing inference speed as a motivation over prior methods (line 24: "reduced inference time and greater practicality"). The paper claims N_a=10 vs. 32–128 for other methods, but provides no wall-clock measurements or latency comparisons to substantiate the practicality claim.

- **The Q-gradient guidance ablation (Figure 2) is presented qualitatively without numerical values.** The paper states "soft Q-guidance achieves the highest performance in nearly all tasks" but does not report the actual scores or margins in text or a table, making it impossible for a reader to assess the magnitude of the effect.

- **The paper has no limitations section or discussion of failure modes**, despite the antmaze-large results and the acknowledged approximations. The conclusion (Section 6) is a single paragraph that only restates contributions.

### Trivial

- Theorems 1 and 2 are labeled as theorems but are relatively straightforward: Theorem 1 restates the standard DDPM/score-matching connection in the RL context, and Theorem 2 is an algebraic substitution. Calling these "theorems" is an over-claim; they would be more accurately described as observations or propositions.

- The ablation text (line 256) says the "variant of DAC without the LCB target also achieve[s] competitive performance" without reporting what "competitive" means numerically, which would help disambiguate the contribution of the LCB component vs. the diffusion actor formulation itself.

## Nice-to-Haves

- Re-implementing the most directly relevant baselines (DQL, IDQL, SfBC) under a shared evaluation protocol would substantially strengthen the SOTA claim.
- A controlled experiment on antmaze-large testing whether DAC benefits from the same reward preprocessing as IDQL-A would turn a speculative explanation into a genuine finding.
- A brief discussion of why the surrogate substitution (π*→D) is reasonable in the diffusion setting — perhaps noting that the soft Q-guidance term provides a form of implicit importance reweighting — would address a clear reader concern.
- Additional quantitative analysis of generated action quality (e.g., distance to nearest neighbor in the dataset) would complement the 2D bandit visualization.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about missing hyperparameter/architecture details in the main body.* The reviewer noted this as a weakness, but such details are almost always deferred to the appendix in main conference papers. The parser strips the appendix, making this criticism an artifact of the review format rather than a genuine paper deficiency.
- *"No analysis of diffusion model's sample quality" raised as a missing analysis.* The paper provides the 2D bandit example (Figure 1) as qualitative analysis. While more analysis could be informative, the existing visualization is sufficient for the paper's claims, and this request exceeds standard expectations for an RL method paper.
- *Strength about "Significant and consistent empirical improvements" was flagged as potentially conflicting with the comparison methodology weakness.* It is retained because the numbers in Table 1 are real and the improvements over the next-best reported numbers are large; the comparison concern is noted as a separate weakness rather than a contradiction.
- *Criticism that Theorem 2 is "calling it a theorem is misleading."* Retained as Trivial because the content is still correct — the labeling is a presentational over-claim, not a substantive error.
- *Criticism that the policy extraction step (Eq. 24) with N_a=10 may violate the KL constraint.* The reviewer raised this concern, but since the policy is trained to satisfy the constraint and N_a=10 is a small number of candidates, this concern is speculative and the paper provides no evidence of constraint violation. Demoted to removed.

## Novel Insights

The most striking pattern across the reviews is that the paper's theoretical derivation (Section 3.1) is widely recognized as its genuine contribution, but the empirical evaluation is seen as markedly weaker. This asymmetry — a clean theory paired with a loose comparison methodology — means the paper's overall contribution is greater than the empirical section alone would suggest, but weaker than the abstract's SOTA claim implies. The fact that the paper deliberately uses a harder evaluation protocol (performance after convergence rather than early stopping) and still achieves strong numbers on locomotion tasks is an under-appreciated strength that partially offsets the comparison concern.

## Suggestions

1. Add a limitations paragraph acknowledging: (i) the surrogate approximation and its potential impact, (ii) the lack of formal guarantees for Q-gradient evaluation at out-of-support points, (iii) the weaker antmaze-large performance and its possible causes.
2. Run a controlled ablation on antmaze-large with the same reward preprocessing used by IDQL-A, and report the results (or show concretely why it cannot be done).
3. Provide a table with numerical values for the Q-gradient guidance ablation (Figure 2) so readers can assess effect magnitudes and not just relative rankings.
4. Include wall-clock runtime measurements for inference (or at least a clear caveat that the N_a comparison is about samples evaluated, not actual speed).

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>