Now let me produce the final consolidated review.

## Summary

This paper proposes Trajectory Entropy Exploration (TEE), a multi-agent exploration method that addresses the homogeneity problem caused by parameter sharing in MARL. TEE uses contrastive learning with learnable identity representations to construct a trajectory representation space, then applies a particle-based (k-NN) entropy estimator to maximize the entropy of different agents' trajectory distributions, generating intrinsic rewards that encourage diverse exploration. The method is integrated with QMIX via a separate intrinsic utility network. Experiments across Pac-Men, SMAC (6 scenarios), and SMACv2 (3 scenarios) show TEE consistently outperforming QMIX, QTRAN, MAVEN, EOI, SCDS, PMIC, LIPO, and FoX.

## Strengths

- **Formally articulates a concrete limitation of mutual-information-based exploration.** Section 3 analytically shows that the variational reward $r_{MI}(\tau,i)=\log q_\theta(i\mid\tau)-\log p(i)$ assigns $r_{\text{new}} = -\infty$ (limit argument) to novel trajectories while $r_{\text{known}} = \log|A|$ to familiar ones. This provides a clear, formal motivation for moving beyond MI-based diversity methods.

- **Learnable identity representations (not fixed one-hot vectors) for contrastive learning.** The paper introduces trainable identity vectors $d^a \in \mathbb{R}^\mathbb{H}$ as anchor variables in the InfoNCE loss (Equation 1), rather than using fixed agent IDs. The ablation study (Figure 6a) confirms that replacing these with one-hot vectors or vanilla contrastive learning causes significant performance drops, validating the design.

- **Modified entropy estimator empirically validated for multi-agent stability.** The paper adapts the standard k-th-nearest-neighbor entropy estimator to average over all $k$ neighbors (Equation 5), adding a numerical stability constant $d$. The ablation directly validates this choice: the k-th-neighbor variant "damages performance and introduces significant variance" while the averaging variant works reliably.

- **Consistent empirical superiority across standard and exploration-focused benchmarks.** TEE outperforms all baselines across six SMAC scenarios (including super-hard ones) and all three SMACv2 scenarios (designed specifically to test exploration under stochastic conditions). The SMACv2 visitation heatmaps (Figure 5) provide direct visual evidence that TEE agents explore substantially more of the state space than baselines.

- **Well-targeted ablation study.** Section 4.3 systematically ablates six components (autoregressive model, fixed encoder, identity prediction, fixed agent identity, vanilla contrastive learning, and neighbor selection strategy), providing clear disambiguating evidence about which design choices matter and why. The T-SNE visualizations in Figure 7 further support the qualitative claims.

## Weaknesses

### Major

- **Mathematical imprecision in the entropy estimator (Equations 3–6).** The k-NN entropy estimator's hypersphere volume formula (Equation 3) uses $|A|$ (the number of agents) as the dimension in the exponent and gamma function argument: $\mathrm{v}_a^k = \|c_t^a - (c_t^a)^{(k)}\|^{|A|} \cdot \pi^{|A|/2} / \Gamma(|A|/2+1)$. However, the trajectory representations $c_t^a$ live in $\mathbb{R}^\mathbb{H}$ (as implied by $d^a \in \mathbb{R}^\mathbb{H}$ and the dot product in the contrastive loss), and the standard k-NN entropy estimator requires the *actual data dimension* in the volume formula. The paper never states that $\mathbb{H} = |A|$, nor does it specify the value of $\mathbb{H}$. This same error propagates into Equations 4–6 and the intrinsic reward (Equation 6).  

  **Why this is major but not fatal:** The practical effect is that distances are raised to the $|A|$-th power rather than the $\mathbb{H}$-th power, which scales the entropy estimate by a constant factor $|A|/\mathbb{H}$ and can be partially absorbed by the reward weight $\beta$. It does not change which trajectories are nearest neighbors or invert the relative ordering of trajectory "sparsity." The method's empirical success demonstrates it works as a diversity-promoting signal regardless. However, the paper's central claim — that it is *maximizing trajectory entropy* in a principled way — is undermined by this imprecision. The authors must either (a) clarify that $\mathbb{H}$ is intentionally set to $|A|$ and justify this design choice, or (b) correct the exponent to $\mathbb{H}$ and verify that results are not sensitive to this correction.

### Minor

- **Non-standard form of the k-NN estimator used without theoretical justification.** The paper replaces the standard form (log of distance to the k-th NN) with an average over $k$ neighbors followed by a log (Equation 5). While the paper provides empirical motivation (instability of the standard form) and ablation validation, it offers no discussion of how this modification affects the bias, variance, or asymptotic properties of the entropy estimate. Since the intrinsic reward is the core mechanism, a brief analysis (even empirical, on synthetic data) would strengthen the paper.

- **No ablation isolating entropy maximization from contrastive representation learning alone.** The ablation study tests variants that damage representation quality, but does not include a variant that uses contrastive learning (with identity representations) *without* the entropy intrinsic reward — e.g., replacing it with a simpler diversity bonus or no bonus at all. This makes it difficult to determine how much of TEE's gain comes from entropy maximization vs. the representation learning itself, which is a critical question given that the contrastive objective already separates agent representations.

- **No analysis of the cold-start / representation calibration problem.** The paper argues TEE avoids the MI methods' problem of penalizing novel trajectories. However, since the representation space is learned online, novel trajectories may initially have poorly calibrated representations (collapsed together), yielding small distances and thus low intrinsic rewards — a related failure mode. The paper does not analyze this empirically (e.g., tracking how intrinsic rewards for newly visited states evolve over training).

- **The $r_{\text{new}} = -\infty$ argument is directionally correct but overstated.** The theoretical limit $q_\theta(i\mid\tau) \to 0$ giving $-\infty$ is mathematically valid but in practice a well-calibrated variational classifier would assign some small positive probability to any trajectory, yielding a large negative number rather than $-\infty$. The core insight (MI methods disincentivize novel trajectories) stands, but the framing exaggerates the contrast with TEE.

- **Hyperparameter sensitivity unexamined.** The method depends on $k$ (nearest neighbors), $\beta$ (intrinsic reward weight), and the representation dimension $\mathbb{H}$. None of these are ablated. The estimator's bias-variance tradeoff depends critically on $k$, and $\beta$ controls the balance between exploration and task reward.

- **Limited statistical rigor.** Results are reported over only 5 random seeds with no significance testing. In stochastic environments like SMACv2, wider confidence intervals limit the reliability of fine-grained comparisons between methods.

### Trivial

- The limitations section (Section 6) is very brief (two sentences) and does not mention the cold-start issue, hyperparameter sensitivity, or computational overhead.

- The paper states TEE "can be integrated with policy gradient methods" (line 130) but only evaluates with QMIX. An additional experiment would strengthen the generality claim.

## Nice-to-Haves

- An analysis comparing TEE's computational overhead (contrastive encoder + autoregressive model + per-agent k-NN per timestep) against baselines would help practitioners assess practicality.
- The contrastive loss uses only $|A|-1$ negatives per positive pair (since the denominator sums over all agents at the same timestep). In SMAC with 5–10 agents, this is quite limited. While the paper's goal is representation organization (not rich feature learning), a brief discussion of this design choice would be helpful.

## Removed Points

The following points from the inputs were removed per the filtering rules:

1. **"The relationship between contrastive learning and entropy maximization creates a conceptual tension... the 'entropy' being maximized is primarily a measure of agent identity separation"** — This is a speculative conceptual concern that is partially addressed by the ablation study (variants without identity representations or with vanilla contrastive learning degrade). The paper's representation space is explicitly designed to be identity-informed; calling this a "tension" rather than a design consequence is an area-of-concern framing without a concrete identified flaw in the paper's logic. Moved here as it leans on speculation rather than a specific verifiable error.

2. **"Limited negatives in contrastive loss"** — The paper's goal for the contrastive loss is to organize representations by agent identity (a simpler task than standard contrastive representation learning), so the limited number of negatives is not a demonstrated weakness. The critic's concern is speculative about representation quality rather than grounded in a concrete failure.

3. **"Only 5 random seeds" / "no statistical significance testing"** — 5 seeds with mean+std reporting is standard practice in MARL (QMIX, CDS, EOI, etc.). Singling out this paper for a field-standard practice without evidence that results would change with more seeds is a generic criticism.

4. **"Missing related works"** — Not allowed per hard rules; no way to verify existence of unmentioned works.

5. **All formatting, typo, and presentation-style nitpicks** — Stripped as parser artifacts per hard rules.

6. **Strength Finder's generic/delusional strengths** — Removed claims like "the paper addressed an important problem" as generic.

## Novel Insights

The most interesting synthetic observation from these reviews is the tension between the paper's claimed *principled* use of k-NN entropy estimation and the *ad hoc* modifications it makes to that estimator (averaging over all k neighbors, using $|A|$ as the dimension, adding a constant $d$). These modifications are empirically validated but lack theoretical grounding, which creates a gap between what the paper claims to be doing ("maximizing trajectory entropy") and what it actually does ("using a distance-based diversity reward in a learned representation space that empirically works well"). The resolution — acknowledging these as pragmatic engineering choices that approximate entropy maximization — would make the paper stronger. A deeper question is whether the core novelty (replacing MI with entropy) is really what drives the gains, or whether the combination of contrastive representation learning + any reasonable distance-based diversity bonus would achieve similar results. The ablation study doesn't fully answer this.

## Suggestions

1. **Fix or clarify the dimension in the entropy estimator.** Either explicitly state that $\mathbb{H} = |A|$ and discuss the implications, or correct the exponent in Equations 3–6 to use $\mathbb{H}$ and re-run experiments to confirm the results are not sensitive to this change.

2. **Add an ablation that removes the entropy reward but keeps contrastive learning.** This would isolate whether entropy maximization provides additional value beyond the representation learning itself.

3. **Analyze the cold-start behavior empirically.** Track how intrinsic reward magnitudes evolve for novel vs. familiar trajectory regions over the course of training.

4. **Discuss the modified k-NN estimator's properties.** At minimum, compare entropy estimates from the proposed averaged form against the standard form on a synthetic distribution to show bias/variance behavior.

5. **Ablate key hyperparameters $k$ and $\beta$** to show the method's sensitivity to choices the user must make.

## Score and Decision

**MY FINAL SCORE:** <score>7.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>