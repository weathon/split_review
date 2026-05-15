Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper studies the problem of steering pretrained Masked Diffusion Models (MDMs) to generate samples that optimize a downstream reward. The authors formulate steering as sampling from a Bayesian posterior proportional to the product of the pre-trained MDM prior and a reward distribution. They introduce Discrete Denoising Posterior Prediction (DDPP), a framework that learns to approximate this posterior by matching denoising posteriors at various masking levels. Three variants are proposed: DDPP-IS (Monte Carlo estimation of the partition function), DDPP-LB (learned lower-bound), and DDPP-KL (reverse-KL with discrete gradients). Experiments span synthetic grids, MNIST/CelebA images, protein sequence design (with wet-lab validation), and text generation.

## Strengths

- **Principled problem formulation.** The paper casts reward-based steering of MDMs as Bayesian posterior sampling (Eq. 1), which is a clean and theoretically grounded framing. This connects MDM fine-tuning to the same inference foundation used in RLHF for autoregressive models, making the contribution conceptually well-motivated.

- **DDPP-IS and DDPP-LB are genuinely simulation-free and off-policy.** These two variants require neither full trajectory simulation nor on-policy sampling. They operate by matching endpoint denoising posteriors at individual masking levels using the pre-trained model's own denoiser, which is a genuine practical advantage for scaling to large MDMs. Table 1 usefully summarizes this distinction.

- **Three complementary variants cover different trade-offs.** DDPP-IS (high-cost, low-bias partition function estimate), DDPP-LB (amortized, cheaper), and DDPP-KL (differentiable reward, bypasses partition function) offer a spectrum of engineering choices. Proposition 1 grounds DDPP-LB as a lower bound on the importance-sampling estimate.

- **Broad empirical evaluation across four domains.** The paper tests DDPP on synthetic data, images (binarized MNIST, CelebA 64×64), protein sequences (with wet-lab validation), and text (toxicity and sentiment steering). This breadth demonstrates the framework's versatility.

- **Wet-lab validation, however modest, is commendable.** The paper goes beyond in-silico metrics by expressing and purifying DDPP-designed proteins, with 4 of 6 constructs showing detectable expression (Figure 2). The authors are transparent about lower yields and insoluble accumulation.

- **Clear computational comparison (Table 1).** The table comparing DDPP variants to baselines along axes of trajectory simulation, reward differentiability, and amortization is helpful for practitioners.

## Weaknesses

### Fatal

None.

### Major

None that are truly fatal to the contribution. The following issues are substantive but addressable.

### Minor

1. **The "simulation-free" claim in the abstract is too broad.** The abstract states that "all three" DDPP objectives are "simulation-free." However, Section 3.3 explicitly states that DDPP-KL requires on-policy sampling: "clean data needed to compute L^KL is drawn purely on-policy by simulating the fine-tuning model x0 ∼ q_t,θ(x0)" (line 163). This requires running the full reverse process of the fine-tuned MDM, which is not simulation-free in the same sense as DDPP-IS/LB. The paper is transparent about this within Section 3.3, but the blanket statement in the abstract is misleading. The authors should either qualify the claim or note that DDPP-KL is the exception.

2. **No analysis of the approximation error between trajectory-level and single-step objectives.** The paper derives a trajectory-level posterior predictive objective (Eqs. 7–8) and then simplifies to a single-step endpoint matching loss (Eq. 11), noting only that this incurs a "discretization error" (line 135). No analysis or bound on this error is provided, and no experiments compare the trajectory-level vs. single-step variants to quantify the empirical impact. While such simplifications are common, the paper's theoretical framing would be strengthened by discussing when the approximation is valid (e.g., under small step sizes or large T).

3. **Missing standard RLHF-style baselines for MDMs.** The baselines include Best-of-N, RTB (GFlowNet), and SVDD (inference-time guidance). Absent are simpler alternatives such as REINFORCE with a baseline applied to MDMs, or weighted supervised fine-tuning on reward-filtered samples. The paper positions DDPP as addressing the lack of "scalable and rigorous" methods for steering MDMs, but does not show that a straightforward REINFORCE adaptation (which is arguably simpler) performs worse. Including at least one such baseline would isolate the benefit of the posterior-matching formulation.

4. **Missing standard deviations for some metrics.** Table 2 reports "mean over 3 runs" without visible standard deviations. Table 4 similarly reports averages without error bars. This makes it difficult to assess whether observed performance differences (e.g., between DDPP variants on MNIST BPD) are statistically reliable. (Notably, Table 3 does include standard deviations, confirming this is not a formatting artifact.)

5. **The metric for the CelebA experiment is class-conditional BPD, but interpretation is ambiguous.** The paper reports that DDPP obtains BPD "within the range of the base model" while RTB achieves better BPD. Since class-conditional BPD on a restricted class (blond hair) mixes likelihood fidelity with the degree of class specialization, it is unclear whether BPD improvements reflect better overall generation or simply concentration on the target subclass. Unconditional BPD on the full test set would be more informative.

6. **Quantitative metrics are missing from the grid experiment.** Figure 1 shows that all DDPP variants produce samples in the lower half of the grid, but no quantitative metric (e.g., MMD, log-likelihood of the target) is reported. Since the true posterior is known in this synthetic setting, reporting quantitative convergence would strengthen validation of the theoretical claims.

### Trivial

- The notation is quite dense, particularly the mixing of trajectory indices and time steps (Section 3). Some steps in the derivation (e.g., Eq. 7→Eq. 8) would benefit from a high-level walkthrough.

## Nice-to-Haves

- **Computational cost analysis.** Reporting wall-clock time, number of reward evaluations, and number of denoiser calls for each DDPP variant vs. baselines would help practitioners choose among methods.
- **Ablation on M (number of importance samples) for DDPP-IS**, showing the reward/computation trade-off.
- **A study of the trajectory-level vs. single-step objective** on a small problem (e.g., the 128×128 grid) to empirically measure the discretization error.
- **Generated protein structure overlays** (predicted vs. target) for the miniaturization task to qualitatively assess the structural preservation.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"MNIST BPD anomaly" (criticism 3 from harsh reviewer):** The reviewer claims that DDPP-KL achieving better class-conditional BPD (78.52) than the pre-trained model (80.71) on even-digit generation is anomalous. This criticism misunderstands the metric: these are *class-conditional* metrics computed on the target class (even digits). A model fine-tuned to specialize on even digits will naturally have better class-conditional BPD than the pre-trained model which spreads mass over all ten digits. This is expected behavior, not an anomaly.

2. **"Missing appendix/proofs" components of criticism 2:** The reviewer criticizes proofs being "deferred to Appendix C, not available." Per policy, appendix sections are stripped by the PDF parser; they exist in the original submission. This criticism is removed.

3. **"Typos/formatting/style nitpicks":** Various formatting-related observations from the reviewer are parser artifacts, not author errors. Removed per policy.

4. **Strength from Strength Finder (generic):** "Consistent empirical outperformance across domains" is retained only in weakened form — DDPP outperforms on most metrics but SVDD wins on log-reward for MNIST and RTB is competitive on CelebA BPD. The original strength claim was slightly overbroad.

## Novel Insights

The most novel observation emerging from the reviews — beyond the paper's own contributions — is the **tension between the "simulation-free" framing and the on-policy nature of DDPP-KL**. The paper's clean theoretical narrative (Bayesian posterior sampling → detailed balance → simulation-free matching) applies cleanly to DDPP-IS and DDPP-LB but breaks for DDPP-KL, which reverts to on-policy simulation with discrete gradient estimation. This creates an implicit hierarchy: DDPP-IS/LB are principled but require partition function estimation, while DDPP-KL bypasses this but loses the simulation-free property and requires differentiable rewards. A future paper could unify these by analyzing when the single-step endpoint approximation is provably close to the trajectory-level objective, closing the theoretical gap the current paper leaves open. Additionally, the wet-lab results — while modest — suggest that the bottleneck for protein DDPP may be soluble expression yield rather than sequence quality, pointing toward multi-objective rewards that combine structural and expressibility terms.

## Suggestions

1. **Qualify the "simulation-free" claim** in the abstract to reflect that DDPP-KL requires on-policy sampling. For example: "two of our three objectives (DDPP-IS, DDPP-LB) are simulation-free."
2. **Add standard RLHF baselines** — at minimum a REINFORCE-with-baseline adaptation for MDMs and perhaps a weighted SFT baseline — to empirically justify why the posterior-matching formulation is preferable.
3. **Report standard deviations** for Tables 2 and 4, or explain if they are missing due to space constraints (appendix is acceptable).
4. **Add a synthetic-grid experiment comparing trajectory-level vs. single-step objectives**, ideally with a quantitative metric and an analysis of the discretization error as a function of step size γ.
5. **Quantity the computational overhead** of DDPP-IS (number of M samples, wall-clock time) vs. DDPP-LB to help practitioners navigate the cost-accuracy trade-off.
6. **Report unconditional BPD on the full CelebA test set** alongside class-conditional metrics to disentangle likelihood preservation from class specialization.

## Score and Decision

The paper presents a principled framework for steering MDMs with three well-motivated variants, strong synthetic and protein-domain experiments, and meaningful wet-lab validation. The main weaknesses are presentation overclaims (simulation-free), missing baselines, and incomplete analysis of the trajectory-level to single-step approximation. These are addressable and do not invalidate the core contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>