- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 5, 3, 3, 5
Now I have all the information I need. Let me write the consolidated final review.

## Summary

The paper proposes Q-flow, a neural-ODE-based method for learning a continuous invertible transport map between two arbitrary distributions from finite samples. The training objective combines a KL divergence term (estimated via a trained classifier network) with a Wasserstein-2 regularization to approximate the dynamic optimal transport (Benamou–Brenier) formulation. The authors also develop a separate "rationet" for density ratio estimation using the learned trajectory, and evaluate on DRE benchmarks, standard OT evaluation suites (Gaussian mixtures, CelebA64), and image-to-image translation.

## Strengths

- **Consistent improvement over strong baselines on OT benchmarks.** On the Gaussian mixture benchmarks (all four dimensions 32–256), Q-flow achieves lower $\mathcal{L}^2$-UVP than OTCFM, MMv1, MMv2, and W2. On the CelebA64 benchmark, Q-flow achieves the best $\mathcal{L}^2$-UVP and $\cos$ across all three checkpoints, including beating NOT (Korotin et al., 2023), the current state-of-the-art neural OT method. These tables provide direct evidence that the learned flow better approximates the true optimal transport map than existing methods.

- **State-of-the-art DRE with both accuracy and computational efficiency.** On the MNIST energy-based modeling task (Table 2, labeled `tab:bpd`), Q-flow achieves the lowest bits-per-dimension across all three choices of $Q$ (RQ-NSF: 1.05 vs 1.09 for DREinf; Copula: 1.14 vs 1.21; Gaussian: 1.31 vs 1.33), while converging in ~8 hours on one A100 GPU versus ~33 hours for DREinf (Section 5.1.3). The 2D Gaussian mixture DRE (Figure 2) also shows Q-flow achieving MAE 2.38 versus 3.22 for DREinf and 3.05 for TRE.

- **Better FID than NOT and GAN baselines on image-to-image translation.** Q-flow achieves lower FID than NOT, CycleGAN, and DiscoGAN on both handbag→shoes (12.97 vs 13.77 for NOT) and CelebA male→female (10.71 vs 13.23 for NOT), demonstrating practical benefit of the dynamic OT flow on a real perception task.

- **Methodological novelty: end-to-end OT refinement without pre-computed mini-batch couplings.** Unlike OTCFM (Tong et al., 2023), which requires pre-computing OT couplings on mini-batches, Q-flow directly minimizes the Benamou–Brenier transport cost from finite samples via an alternating refinement procedure (Algorithm 1). The classifier-based KL estimation avoids the need for an analytical terminal density, which is the key enabler for handling arbitrary $Q$.

## Weaknesses

### Major

- **No ablation or verification that the end-to-end refinement improves OT quality over the initialization.** The paper's pipeline consists of (a) initialization via concatenated CNFs or interpolants, then (b) iterative refinement with the full OT objective. The paper claims this refinement converges toward the dynamic OT, but never shows that the output after refinement is closer to the true OT map than the initialization itself. An ablation comparing the initialization alone against the full refinement is necessary to attribute the method's success to the proposed training procedure rather than to the initialization scheme. Without this, the reader cannot assess whether the refinement step (which is the paper's core algorithmic contribution) actually helps. (Confirmed: no ablation study appears anywhere in the paper; grep for "ablat" returns no results.)

- **Missing a key baseline (NOT) from the Gaussian mixture OT benchmarks.** The Gaussian mixture table (labeled `table-hd-metrics`) compares Q-flow against OTCFM, MMv1, MMv2, and W2, but omits NOT (Korotin et al., 2023), which is a recent state-of-the-art neural OT method. NOT *is* included in the CelebA table and the image-translation table, so its absence from the Gaussian mixtures table is unexplained. Since NOT was published before this work and is directly relevant, its omission weakens the claim of "consistent improvement over popular baselines" for these experiments. The paper should either include NOT in this table or explicitly state why its results are unavailable for the Gaussian mixture setting.

### Minor

- **No error bars, confidence intervals, or multiple-run statistics.** None of the quantitative results (Tables 1–5, Figure 2 MAE) include standard deviations or are reported over multiple runs. Given the stochasticity in neural network training and ODE integration, this omission limits the reader's ability to assess the significance of the reported improvements. This is standard practice to expect for empirical machine learning papers.

- **No study of hyperparameter sensitivity.** The method has several hyperparameters ($\gamma$, time grid resolution $S$, number of outer iterations Tot, inner epochs $E$ and $E_{\rm in}$). The paper states $S$ is "usually 3-5" and that $E_{\rm in}$ inner-loop updates are "light" but provides no sensitivity analysis or guidance for how to set these values across different problems. This limits reproducibility for practitioners.

- **Potential class imbalance issue in the KL loss estimator.** Equation (2) (labeled `rnet_loss`) uses unweighted sums $1/N$ and $1/M$. When $N \neq M$, the population optimum of the classifier shifts from $\log(q/p_1)$. The paper does not discuss whether class imbalance affects the KL surrogate or whether they balance the batches in practice.

- **Double-dipping concern for the DRE rationet.** The rationet is trained on the same transported samples used to train the Q-flow. The paper does not discuss whether this shared use introduces overfitting or bias in the ratio estimates, which could inflate DRE performance relative to methods that do not use a trained transport trajectory.

- **No evaluation of the sensitivity of the $W_2$ regularization coarseness $S$.** The paper notes that $S=3\text{–}5$ works, but does not ablate this choice or show that results are stable across different grid resolutions for the $W_2$ term.

### Trivial

- **No explicit convergence criterion in Algorithm 1.** The algorithm runs for a fixed number of outer iterations (Tot) and inner epochs (E, E_in), which is standard practice, but the paper could benefit from a brief note on how these were selected.

## Nice-to-Haves

- **Direct transport cost reporting on real data.** For the image-to-image translation task, reporting transport cost (e.g., estimated $W_2$ distance or regularization loss on a test set) alongside FID would more directly support the claim that the flow achieves low-cost transport, though FID is the appropriate metric for the downstream application.
- **Discussion of failure cases.** The paper's Discussion section (Section 6) mentions open theoretical questions but does not discuss practical failure modes (e.g., disconnected support, classifier mode collapse). A brief limitations paragraph would strengthen the paper.
- **Wall-clock times for OT benchmark experiments.** The computational advantage is demonstrated for MNIST DRE (8h vs 33h), but no timing is provided for the OT benchmarks or image translation experiments, making it hard to assess scalability.

## Removed Points

These points were identified in the reviewer inputs but removed after cross-checking against the paper (see filtering rules in the meta-reviewer instructions):

- **Question about invertibility error being unreported.** The paper references "Table \ref{inv_err}" (line 297). This table is in the appendix, which the parser strips from all submissions. Rule: remove criticisms about missing appendix content.
- **Criticism that OT optimality on real data is unsupported because only FID is reported.** The OT benchmarks (Tables 1, 2) already validate OT quality on CelebA data. The image translation task is a downstream application where FID is the standard metric, and the paper's claimed contribution for this task is "comparable or better metrics" — not proving OT optimality through FID. This criticism overreaches.
- **Claim about "nearly identical performance as DREinf" on MI estimation being a weakness.** The paper's own text describes this as near-optimal performance; matching the best baseline on this task is not a weakness. The statement is factual, not a flaw.
- **Criticism about MNIST BPD improvements being "modest."** The improvements (1.05 vs 1.09, 1.14 vs 1.21, 1.31 vs 1.33) are consistent across all three settings, and the computational advantage (8h vs 33h) is significant. Calling them "modest" is subjective and ignores the efficiency gain.
- **Request for complete hyperparameter disclosure.** Individual hyperparameter values for each experiment are typical for supplementary material (which is stripped), not the main text. The paper appropriately describes the key configurations.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension between a well-executed experimental paper and gaps in evaluation completeness. The most notable insight from the review synthesis is that the paper's central algorithmic contribution (the iterative refinement toward dynamic OT) lacks an empirical test that isolates its effect — this is a common pattern in papers that propose a multi-stage pipeline, and the absence is more significant here because the initialization alone (concatenated CNFs or interpolants) could plausibly already produce reasonable transport between $P$ and $Q$.

## Suggestions

1. **Add an ablation study for the refinement step.** Compare: (a) initialization alone, (b) refinement without the $W_2$ regularization, (c) refinement without the reverse direction, (d) full refinement. Report $\mathcal{L}^2$-UVP and $\cos$ on the Gaussian mixture benchmarks for each variant. This single experiment would substantially strengthen the paper.
2. **Include NOT in the Gaussian mixture OT benchmark table**, or explain why it is not applicable.
3. **Add error bars** (at minimum over 3–5 seeds) to the main quantitative tables.
4. **Add a brief hyperparameter sensitivity analysis** for $\gamma$, $S$, and the outer/inner iteration counts, even if only on one setting.
5. **Comment on class balance** in the classifier-based KL loss estimation — specifically whether $N=M$ in all experiments and whether the loss weighting changes when they differ.
