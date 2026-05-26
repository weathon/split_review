Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper presents a real-time pipeline integrating streaming latent-space construction (including a novel streaming jPCA), an adaptive nonparametric stimulus-response model via kernel regression with a time-dependent kernel, and constrained optimization to design high-dimensional stimulation patterns that drive latent neural dynamics along chosen directions. The method is demonstrated on synthetic data and on two real neural recording modalities (calcium imaging, mouse; electrophysiology, nonhuman primate) with **simulated** stimulation effects, and achieves end-to-end runtimes under 100 ms, making it potentially suitable for future closed-loop experiments.

## Strengths

- **Real-time optimization produces stimulations aligned with desired latent directions.** The designed stimuli yield significantly smaller angles between the observed perturbation and the target latent direction compared to random single-neuron, random multi-neuron, and shuffled baselines (Fig. 4a). This directly demonstrates the core claim—that the optimization can select high-dimensional stimulation patterns to affect low-dimensional latent dynamics.

- **Nonparametric stimulus-response model adapts to non-stationarities.** The kernel regression estimator with a time-dependent kernel recovers from a 180° flip and a continuous rotation of the ground-truth mapping within ~15 s, while a non-adaptive baseline suffers sustained error (Fig. 2e). This shows the method can track changes in neural responsiveness over time.

- **End-to-end computation runs faster than real time.** The full pipeline (latent update, dynamics prediction, S-R model update, optimization) completes in under 100 ms per timepoint with averages below 10 ms (Section 3), which is a necessary condition for closed-loop *in vivo* use.

- **Validation across two neural recording modalities.** The approach is tested on both calcium imaging data (15 Hz, 592 neurons) and intracortical electrophysiology data (30 Hz, 130 units), showing consistent improvement over the blind baseline (Section 4.1, Figs. 3). This cross-modality evidence supports the method's general applicability.

- **Novel streaming sjPCA converges to offline jPCA solutions.** The streaming jPCA formulation (Eq. 2) with Orthogonal Procrustes stabilization achieves the same rotational plane structure as offline jPCA, with error dropping to near zero within seconds (Fig. 1a). While not integrated into the stimulation experiments, this is a standalone algorithmic contribution.

- **Optimization handles realistic experimental constraints.** The objective (Eq. 8) enforces non‑negativity and an L₁-based sparsity penalty, and correctly identifies infeasible target directions (e.g., "Negative" yields high predicted angles in Fig. 4b). These constraints mirror common limitations in optogenetic and electrical microstimulation setups.

## Weaknesses

### Fatal
None.

### Major

1. **The central claim of enabling adaptive stimulation experiments is not supported by real stimulation validation.** Every experiment on real neural data uses a **simulated** stimulation model—an autoregressive function ($a_t = 0.8 a_{t-1} + u_t$) added to the recorded traces. The stimulus–response mapping $S$ that the algorithm learns is therefore determined by a hand-crafted, deterministic simulation rule, not by actual optogenetic or electrical stimulation of the recorded neurons. The abstract and introduction frame the method as enabling "the next generation of experiments capable of designing and testing stimulations of latent neural dynamics in real time," but this claim cannot be supported by experiments that sidestep the core difficulty the method is supposed to solve: the unknown, noisy, and state-dependent nature of real neural responses to stimulation. The Discussion acknowledges offline execution as a limitation but does not adequately emphasize that the **stimulation itself** is simulated. A method paper aiming at real experimental impact should at minimum validate on a dataset with actual delivered stimuli (even open-loop), or clearly reframe the contribution as a simulation/design tool with appropriately hedged claims.

2. **The optimization is compared only to random baselines and a blind model, with no comparison to existing adaptive stimulation approaches.** The paper compares its designed stimuli only to random single-neuron, random multi-neuron, shuffled, and blind (stimulation-agnostic) baselines. Prior work on adaptive stimulation—Bayesian optimization (Minai et al., 2024), active learning (Wagenmaker et al., 2024), and input-output dynamical modeling (Yang et al., 2021)—is cited in the Introduction but never used as a comparator. The claim that the optimization "outperforms random methods" is a minimal bar; any method that leverages information about the latent target should beat random sampling. Without comparison to at least a simple non-random baseline (e.g., stimulating neurons with the highest loadings on the desired latent direction, or a linear approximation of $S$), it is unclear whether the complex kernel-regression pipeline and constrained optimization provide meaningful advantages over simpler alternatives.

### Minor

3. **The sparsity constraint in Eq. (8) is incompletely specified.** The term $\|u\|_0^{\max}$ is not defined anywhere in the paper. The text says "we use an $L_1$ constraint on $u$ offset by $N$ to encourage a solution with the number of non-zero elements close to $n$," but the formula $\lambda_1(\|u\|_0^{\max} - \|u\|_1)$ with $[0,1]$ box constraints and a positive $\lambda_1$ encourages $\|u\|_1$ to be **large**, which pushes entries toward 1 — the opposite of sparsity. Whether the intended behavior is achieved and how many neurons are actually selected is not reported.

4. **sjPCA is presented as a contribution but is disconnected from the main validation.** The novel streaming jPCA is introduced in Section 2.1 and shown to converge in Fig. 1a, but the real-data stimulation experiments (Sections 4.1, 4.2) use proSVD for dimensionality reduction. The parallel latent-space selection (Fig. 1c) is illustrated but not employed in the stimulation pipeline. This makes the paper feel like a collection of loosely integrated components—the contribution of sjPCA to the stimulation task is never demonstrated.

5. **No ablation study.** The pipeline combines several components (streaming reduction, dynamics model, kernel regression with time kernel, optimization). It is never shown which parts are critical—e.g., does the time-dependent kernel matter? Would linear regression for $S$ suffice for the simulated effects? How much does the dynamical model choice affect results?

6. **No sensitivity analysis.** Hyperparameters (RBF length scales, delay $d$, sparsity penalty $\lambda_1$, dynamics model choice) are not analyzed, and it is unclear how robust the method is to misspecification.

7. **No statistical testing.** The comparative claims in Figs. 4 and 5 are presented as violin plots and scatter plots without hypothesis tests or confidence intervals. It is not quantified whether the designed stimuli are significantly better than the baselines.

### Trivial
None.

## Nice-to-Haves
- The exploration strategy for the stimulus-response mapping could be discussed—how many stimulus-response pairs are needed, and how to actively explore the space during a burn-in phase.
- The parallel latent-space selection could be demonstrated to improve stimulation targeting when the best-predictor space changes over time.

## Removed Points
These points are flagged to be removed from the main review; treat them with caution.

- **"Circular validation"** (Harsh Critic, Critical Issue 1). The claim that Fig. 4 uses the same simulation model for training and evaluation making it "circular" is overstated. The method learns $\hat{S}$ from sparse observations and evaluates against $s_{\text{obs}}$ from the actual system. This is standard simulation-based evaluation, not circular reasoning. The simulation being simple (autoregressive) does limit the strength of the validation—this is already captured in Major weakness 1.
- **Strength Finder generic strengths about problem importance** removed as per filtering rules (say nothing about the specific paper). None of the listed strengths were generic in this sense—all cited specific results—so none were removed for this reason.

## Novel Insights
Beyond the paper's own contributions, the reviews surface a tension that the paper does not fully address: the proposed pipeline is ambitious in scope (streaming + nonparametric modeling + constrained optimization), but the validation rests on simulated effects that strip away nearly all the biological complexity the method claims to handle. This gap between scope and validation is the paper's central weakness. A related observation: the paper simultaneously contributes several components (sjPCA, kernel regression S-R model, optimization) but does not demonstrate how they depend on each other, making the overall contribution difficult to evaluate as a unified system.

## Suggestions
1. **Reframe the claims** to match the validation. If real stimulation data cannot be obtained, the paper should be positioned as a simulation framework for *designing* stimulation protocols under known (or assumed) response mappings, with appropriately hedged language. Alternatively, obtain at least one dataset with real delivered stimuli (even open-loop) and show that $\hat{S}$ can be learned from actual neural responses.
2. **Add at least one non-random baseline** for the optimization: e.g., stimulate neurons with the highest absolute loading on the desired latent direction (an open-loop heuristic), or a linear approximation of $S$ compared to the kernel regression.
3. **Clarify the sparsity constraint**: define $\|u\|_0^{\max}$, explain how the L₁ offset achieves sparsity, and report the achieved number of non-zero stimulation targets.
4. **Integrate sjPCA into the stimulation experiments** or remove the claim that it is part of the adaptive stimulation pipeline.
5. **Add an ablation study** isolating the time-dependent kernel, the nonlinear S-R mapping, and the dynamical model choice.
6. **Add statistical testing** for the key comparisons in Figs. 4 and 5.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>