Now I have all the information I need to produce the final review. Let me synthesize everything carefully.

---

## Summary

This paper studies the relationship between discrete-time and continuous-time training objectives for diffusion-based samplers (neural SDEs trained to sample from unnormalized densities). The authors prove that, in the limit of infinitesimal time steps, trajectory-level objectives (Trajectory Balance, VarGrad) and local objectives (Detailed Balance) used in discrete-time policy training converge to well-defined continuous-time objects — path-space measure divergences and the Fokker-Planck equation, respectively. Empirically, they show that training with **coarse nonuniform** time discretization (Random or Equidistant step placement) achieves comparable sampling quality to training with 100-step uniform discretization while being substantially cheaper, and also produces samplers more robust to the inference-time number of integration steps.

---

## Strengths

1. **Asymptotic equivalence proofs for global objectives (Prop. 3.2 & 3.3):** The paper rigorously shows that trajectory-level divergences (TB, VarGrad) defined for discrete-time policies converge to their continuous-time path-space counterparts as the mesh size goes to zero. This is a useful theoretical unification — it connects the GFlowNet/RL training losses used in practice to the continuous-time stochastic control perspective, which was previously only heuristic. The convergence of functionals with polynomial growth (Prop. 3.2) goes beyond trivial SDE approximation by explicitly addressing the Radon-Nikodym derivative expressions specific to diffusion sampler training.

2. **Local objective → PDE equivalence (Prop. 3.4 & 3.5):** Proposition 3.4 shows that the Detailed Balance discrepancy asymptotically enforces Nelson's identity and the Fokker-Planck equation, establishing a new link between a discrete-time RL loss and a continuous-time PDE characterization of time reversal. This is the most novel theoretical result — it provides a concrete condition under which DB training produces correct continuous-time reversals, and it generalizes to the Brownian bridge setting (Prop. 3.5) used in popular samplers.

3. **Empirical demonstration of coarse-discretization efficiency:** Figure 4 (right panel) plots runtime against ELBO gap, showing that nonuniform (Random) discretization achieves a strictly better trade-off than uniform discretization — comparable performance at substantially lower training time. The log-log scaling in Figure 4 (left) confirms near-linear scaling with trajectory length. The finding is clean and practically useful: training with ~10 nonuniform steps can match the quality of 100 uniform steps.

4. **Robustness to inference-time discretization (Figure 5):** Models trained with Random or Equidistant discretization produce smooth ELBO curves as the evaluation-step count varies, whereas Uniform-trained models exhibit periodic artifacts at multiples of the training step count. This is a practically important and previously unreported property — it shows that nonuniform training yields samplers less sensitive to the inference discretization choice.

---

## Weaknesses

### Fatal
None. The theoretical results are correct as stated; the empirical findings support the main claims. No errors invalidate the core contributions.

### Major

1. **Theory-experiment disconnect:** The theoretical results (Propositions 3.1–3.5) all concern the asymptotic limit as the maximum step size goes to zero — i.e., arbitrarily fine discretization. The experiments, by contrast, deliberately use **coarse** discretization (as few as 5–10 steps). The theory therefore does **not** explain, predict, or guide the choice of nonuniform schedules, and the experiments do not validate the theory (they operate in a regime the theory says nothing about). The paper acknowledges this gap by calling it a "hypothesis" (line 40), but the two contributions remain loosely coupled. The paper would be stronger if it either (a) provided a non-asymptotic or rate-based analysis that sheds light on the coarse-discretization regime, or (b) framed the theory and experiments as independent contributions with a clearer separation of scope.

2. **No error bars on the main evaluation figure (Fig. 3):** Figure 3, which is the central empirical result showing ELBO gap as a function of N_train, does not report variability. The caption makes no mention of error bars or multiple runs. Figure 4 (timing) does include "mean and std over 3 runs," but the primary quality metric relies on readers trusting that differences between discretization schemes are not due to noise. Without error bars, it is impossible to judge whether the advantage of Random over Uniform at small N_train is statistically significant. This is a straightforward omission that should be addressed.

### Minor

3. **Overclaiming in the abstract and conclusion:** The abstract claims "greatly improved sample efficiency." For the 25GMM and Funnel tasks (Fig. 3), the improvements from nonuniform over uniform at low N_train are modest (e.g., ELBO gap improving from roughly −0.5 to −0.3). The "greatly improved" characterization is accurate for Manywell and LGCP but overstated as a blanket statement. Similarly, the conclusion speculates that the benefits "are especially beneficial in very high-dimensional problems" — the highest dimension tested is 1600, which is moderate for this literature. These claims should be calibrated to the actual results.

4. **"Near-state-of-the-art" claim (line 357) references an appendix table:** The paper states that combining nonuniform training with off-policy local search yields "near-state-of-the-art results" (Table 2, in appendix). While the appendix presumably contains these comparisons, the main text does not provide any external calibration. A brief summary of the comparison numbers in the main text would substantiate this claim.

### Trivial
None.

---

## Nice-to-Haves

- **A principled method for choosing the discretization schedule:** The paper tests Random and Equidistant placement but provides no guidance on how to choose or optimize the schedule. Even a heuristic explanation (e.g., uniform coarse discretization overweights nearly-deterministic early steps) would strengthen the paper.
- **Non-asymptotic rates for a simplified case:** Providing even a one-dimensional toy analysis showing how discretization error scales with step size for the Radon-Nikodym derivative would elevate the theory from purely asymptotic to practically relevant.
- **Quantitative comparison to non-diffusion-based samplers** (e.g., HMC, normalizing flows) for the same tasks, if available in the literature, to give meaning to "competitive performance."

---

## Removed Points

These points were flagged by the reviewers but are removed for the reasons stated:

- *"The theoretical results are expected from standard SDE theory"* — The paper explicitly acknowledges this (the results "extend classical results on SDE approximations... to objectives for diffusion-based samplers"). The contribution is in the application to the specific Radon-Nikodym derivative expressions used in diffusion sampler training, not in deriving new SDE convergence results. This is a framing observation, not a weakness.
- *"The paper only compares within-family (PIS, TB, DB) and not to other neural samplers"* — The paper's contribution is about the effect of discretization choice on training objectives. Comparing against methods that use entirely different training frameworks (normalizing flows, MCMC) would be a separate study. The controlled comparison across objectives and discretizations is appropriate for the claims made.
- *"PIS is described as on-policy only but combined with off-policy local search"* — Table 1 describes the fundamental properties of the objective itself, not whether external exploration strategies can be combined with it. There is no contradiction.
- *"Missing comparison against fine uniform with the same step count"* — This comparison is already present (the paper compares coarse nonuniform vs. coarse uniform at the same N_train).
- *"The GFlowNet framing is forced"* — The paper explicitly notes that discrete-time policies correspond to GFlowNets, but the results apply more broadly. This is a framing choice, not an error.
- *"The conclusion overclaims about very high-dimensional problems"* — This is a forward-looking statement ("We expect"), not a claim of having demonstrated it, and 1600 dimensions is non-trivial for sampling.
- *All formatting/style nitpicks and reproducibility concerns about undisclosed hyperparameters or missing appendix content* — These are artifacts of the PDF extraction or standard for the field.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface a novel perspective on the paper that the authors themselves do not articulate.

---

## Suggestions

1. **Add error bars or confidence intervals to Figure 3** (ELBO gap vs. N_train). This is the most important single improvement — without it, the reader cannot assess whether the reported differences are meaningful.
2. **Explicitly acknowledge the scope of the improvements** in the abstract and conclusion: large for Manywell and LGCP, more modest for 25GMM and Funnel. Calibrate "greatly improved" to the actual results.
3. **Discuss the theory-experiment gap openly.** A paragraph in Section 3 or 4 explaining that the asymptotic theory validates the objectives' meaning but does not directly predict coarse-discretization behavior, and that the empirical findings are complementary, would improve coherence.
4. **Briefly summarize the "near-state-of-the-art" comparison from Table 2** in the main text (e.g., "on LGCP, our method achieves an ELBO gap of X vs. the previous best of Y"), so the claim does not rely solely on the appendix.

---

## Score and Decision

This is a solid paper with a clear, well-executed theoretical contribution (unifying discrete and continuous training objectives for diffusion samplers) and a practical empirical finding (coarse nonuniform discretization accelerates training). The main weaknesses are the theory-experiment disconnect and the absence of error bars on the primary evaluation figure. Neither is fatal, but both should be addressed. The paper is above the acceptance threshold for a good venue.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>