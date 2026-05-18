## Summary

PnP-Flow integrates Flow Matching models into the Plug-and-Play (PnP) framework for image restoration. The key idea is to define a time-dependent denoiser \(D_t = \mathrm{Id} + (1-t)v^\theta_t\) from a pre-trained flow-matching velocity field, and then use it within a Forward-Backward Splitting algorithm augmented with an interpolation step that projects iterates onto flow trajectories. The method avoids backpropagation through ODEs and trace computations, making it memory-efficient (0.10 GB peak GPU memory). The paper evaluates on denoising, deblurring, super-resolution, and inpainting across CelebA and AFHQ-Cat, showing the method ranks first or second in most task–metric combinations.

## Strengths

- **Principled denoiser design via conditional expectation.** The paper derives \(D_t(x) = x + (1-t)v^\theta_t(x) = \mathbb{E}[X_1 \mid X_t = x]\) under the optimal velocity field (Eq.~\eqref{helper}–(211)), establishing a direct theoretical link between flow matching and denoising that goes beyond black-box PnP denoisers. Proposition~1 further characterizes when the denoising loss is zero (straight-line flows).

- **Consistent first-or-second ranking across tasks.** In Tables~1–2, PnP-Flow ranks first or second in 9 of 10 metric/task combinations on CelebA and all on AFHQ-Cat, while every baseline (PnP-Diff, PnP-GS, OT-ODE, D-Flow, Flow-Priors) drops sharply on at least one task (e.g., D-Flow falls to 26.42 PSNR on denoising vs. 32.45 for PnP-Flow). This cross-task stability directly supports the method's claimed generality.

- **Dramatically lower memory usage with competitive runtime.** Table~3 shows PnP-Flow uses 0.10 GB GPU peak memory on CelebA deblurring versus 0.65 GB (OT-ODE), 2.96 GB (Flow-Priors), and 5.91 GB (D-Flow), while maintaining reasonable runtime (3.40s). This efficiency stems from avoiding ODE backpropagation and trace computations.

- **Versatility beyond Gaussian latent distributions.** Section~5.3 explicitly notes that unlike OT-ODE, Flow-Priors, and diffusion-based methods, PnP-Flow works with any latent distribution (e.g., Dirichlet for categorical data), extending its potential applicability to domains like molecular data.

## Weaknesses

### Fatal
None.

### Major

1. **Interpolation step is a heuristic, not a principled "reprojection."** The algorithm generates \(\tilde{z}_n = (1-t_n)\varepsilon + t_n z_n\) with \(\varepsilon \sim P_0\) independent of \(z_n\), and frames this as "reprojection onto flow trajectories" (lines~10,~66,~232,~247). However, the flow path \(X_t = (1-t)X_0 + tX_1\) requires \((X_0,X_1) \sim \pi\) (a coupled pair). The paper acknowledges the issue (line~249: "note that while \(\varepsilon\) is sampled from \(P_0\), it is not necessarily coupled to \(z \sim P_1\) via \(\pi\)") but provides no argument — theoretical or empirical — for why this linear combination with *independent* noise nevertheless moves the iterate onto the support of \(X_t\) in a useful sense. The algorithm may still work well empirically, but the paper's framing as "reprojection" overstates the principle, and the core mechanism lacks justification. This is a methodological gap that the paper does not address.

2. **Claims of "consistently outperforming" are overstated.** The abstract (line~12) claims "demonstrating superior results" and the contributions (line~68) claim "our method consistently outperforms state-of-the-art ... methods." Table~2 (AFHQ-Cat) shows this is false: PnP-Flow loses to PnP-GS on denoising (31.65 vs. 32.34) and to PnP-Diff on deblurring (27.62 vs. 27.97). The more measured statement in Section~5 (line~343) — "consistently ranks first or second" — is accurate and should replace the stronger phrasings.

3. **Ablation studies are entirely absent.** The paper does not analyze the effect of: (a) the number of time steps \(N\) (is 100 necessary, or could 20 suffice?); (b) the exponent \(\alpha\) in the learning rate schedule \((1-t)^\alpha\); (c) the number of Monte Carlo averaging samples (1 vs. 5 vs. 10); or (d) the interpolation step itself (what happens if \(D_t\) is applied directly to \(z_n\) without interpolation?). These are not optional — they are necessary to attribute performance to specific design choices and to understand the method's sensitivity.

### Minor

1. **No uncertainty quantification.** All PSNR/SSIM results in Tables~1–2 are point estimates without standard deviations, confidence intervals, or significance tests. Given that margins are often small (<0.5 dB), the reader cannot assess whether reported improvements are statistically meaningful. Reporting std. devs over the 100 test images would substantially strengthen the credibility of the quantitative claims.

2. **Convergence guarantee (Proposition~2) does not match the deployed algorithm.** The proposition assumes an infinite-time regime with \(\sum_n (1-t_n) < \infty\) and \(\gamma_n = 1-t_n\), but experiments use a finite uniform schedule \(t_n = n/N\) with \(N=100\) and \(\gamma_n = (1-t_n)^\alpha\) (where \(\alpha\) may differ from 1). The boundedness condition on the iterates is also assumed rather than verified. As a result, the theory does not directly certify the algorithm's behavior in the setting where it is actually evaluated.

3. **PnP-Diff baseline uses a model trained on a different dataset (FFHQ)** while evaluation is on CelebA and AFHQ-Cat. The paper transparently acknowledges this (line~332: "we had no alternative"), but the mismatch makes the comparison unreliable — it is unclear how much of PnP-Diff's underperformance is due to method quality vs. domain shift. The paper would be stronger without this baseline (the other four baselines already provide a fair comparison) or with a same-dataset diffusion model.

4. **Computational cost comparison (Table~3) omits PnP-GS and PnP-Diff**, the two main PnP baselines, and only compares against other Flow Matching methods. Including PnP-GS and PnP-Diff would substantiate the efficiency claims more fully.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment where the interpolation step is omitted (direct application of \(D_t\) to \(z_n\)) would isolate the step's contribution.
- Including a comparison on FFHQ with a same-dataset PnP-Diff model would clean up the baseline issue.
- A brief discussion of why the independent noise interpolation might still be effective (e.g., relating it to the denoising properties of MMSE estimators) would fill the theoretical gap without requiring a full proof.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Figure PSNR inconsistency (Harsh Critic §5):** The critic claimed figure PSNRs are inconsistent with table averages (e.g., denoising row in Figure~2 shows 33.58 for PnP-GS vs. 33.55 for PnP-Flow, while Table~1 reports both as 32.45). This is a misunderstanding: figures show per-image PSNR for a single test example, while tables report averages over 100 images. No inconsistency exists. **Removed: factually incorrect.**

- **Time-dependent learning rate lacks analysis (Harsh Critic §3.2):** The critic asked for a theoretical analysis of why \(\gamma_t = (1-t)^\alpha\). The paper states this is selected via grid search on a validation set — standard practice in the field. **Removed: generic nitpick.**

- **BM3D missing baseline (Harsh Critic §5):** The paper focuses on learned methods, and the non-learned baseline omission is minor. **Removed: scope creep; does not harm the paper's core claim.**

- **Out-of-distribution analysis missing (Harsh Critic §5.3):** The critic requested evaluation on degradation types not seen during hyperparameter tuning. This goes beyond standard evaluation practice. **Removed: scope creep.**

- **"Does not rely on good initialization" framed as weakness (Harsh Critic §5.3):** The critic speculated this could be problematic for tasks with weak priors — purely conjectural with no evidence. **Removed: speculative.**

**Strength Finder filtered strengths:**
- **Convergence guarantee (Proposition~2):** The Strength Finder listed this as a strength, but the guarantee's conditions do not match the experimental setup (see Weakness Minor #2). The theoretical contribution is noted but is not a practical strength for the deployed method. **Demoted to supporting point with caveat.**
- **"Consistently outperforms" framing in Strength Finder #2:** Rephrased to "consistently ranks first or second" to match the paper's own more accurate language in Section~5.

## Novel Insights

The reviews surface an interesting tension: the paper has a theoretically grounded denoiser (\(D_t = \mathbb{E}[X_1 \mid X_t = x]\)) that is well-motivated, but the interpolation step that feeds into this denoiser relies on an unprincipled coupling (\(\varepsilon\) independent of \(z_n\)). This means the algorithm's strongest theoretical anchor (the denoiser as conditional expectation) is applied to inputs (\(\tilde{z}_n\)) whose distribution relative to \(X_t\) is not characterized. An alternative not explored in either the paper or the reviews would be to use the flow model itself to map \(z_n\) back to the path — e.g., solving the ODE backward from \(t=1\) to time \(t\) with \(z_n\) as initialization — but this would sacrifice the computational efficiency that is one of the paper's main selling points. This reveals a genuine design tradeoff at the heart of the method.

## Suggestions

1. **Soften the language in the abstract and contributions** to match the evidence: replace "consistently outperforms" / "superior results" with "competes favorably with" or "ranks first or second."
2. **Add ablation studies** for at least (a) the number of time steps \(N\) and (b) the exponent \(\alpha\), to demonstrate the method's robustness and help practitioners configure it.
3. **Report standard deviations** (over the 100 test images) for all PSNR/SSIM entries in Tables~1–2.
4. **Address the interpolation step gap** with either: a brief theoretical justification (e.g., showing that the expected squared distance between \(\tilde{z}_n\) and the support of \(X_t\) remains bounded), or a clear reframing of the step as a heuristic with empirical motivation.
5. **Either drop the PnP-Diff baseline** or retrain a diffusion model on the same datasets.
6. **Include PnP-GS and PnP-Diff in the computational cost table** to make the efficiency comparison complete.

## Score and Decision

The paper presents a novel and useful integration of Flow Matching into the PnP framework, with strong empirical results and remarkable memory efficiency. The weaknesses are real but addressable: the overstated claims can be corrected, ablation studies can be added, and the interpolation step's justification can be strengthened (or the language around it softened). The core contribution — a time-dependent denoiser derived from a flow-matching model that avoids ODE backpropagation — is sound and valuable to the community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>