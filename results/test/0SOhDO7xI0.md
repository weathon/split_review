Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes DeepDRK, a deep learning-based knockoff generation pipeline for FDR-controlled feature selection. The method combines (1) multi-swapper adversarial training with a Knockoff Transformer to enforce the swap property, (2) a sliced Wasserstein correlation (SWC) regularization loss to reduce reconstructability between $X$ and $\tilde{X}$, and (3) a post-training dependency regularized perturbation (DRP) that mixes the trained knockoff with a row-permuted copy of $X$ to further boost power. Extensive experiments on synthetic, semi-synthetic, and real-world data (including RNA-seq and metabolomics) show DeepDRK consistently controls FDR near or below the nominal threshold while maintaining competitive power, particularly in the challenging small-sample ($n=200$, $p=100$) regime where baseline methods either exceed FDR substantially or collapse to near-zero power.

## Strengths

1. **Novel multi-swapper adversarial framework.** The paper introduces a multi-swapper formulation (§3.1) with $K$ neural-network swappers, a REx term to stabilize SWD across swappers, and a cosine-similarity regularizer to prevent mode collapse. This extends the single-swapper attack of DDLK [Sudarshan et al., 2020] and is motivated by the observation that a single swapper cannot guarantee the swap property for all $B \subset [p]$. The ablation studies (referenced as Appendix materials) support the contribution of each component.

2. **Consistent FDR control across diverse regimes.** DeepDRK maintains FDR at or below the nominal 0.1 threshold across synthetic data with varying $\beta$ scales (Figure 4), Gaussian mixtures with $\rho_{\text{base}}$ up to 0.8 (Figure 3), copula-based non-Gaussian distributions (Figure 2), and semi-synthetic RNA/IBD data (Figures 6-7). This stands in contrast to baselines (DDLK, Deep Knockoff, KnockoffGAN, sRMMD) that frequently exceed FDR or sacrifice power in the same settings.

3. **Theoretical and empirical justification for DRP.** The paper provides Lemma 1 and Proposition 1 showing the DRP's impact on the swap property vanishes asymptotically ($\alpha_n \lesssim n^{-1/2}$). The motivation for DRP—the observed competition between the swap loss and dependency regularization loss during training (§3.2)—offers a plausible explanation for why post-training perturbation outperforms direct joint minimization of the competing terms.

4. **Diagnostic analysis via knockoff statistics distribution.** Figure 5 provides mechanistic insight into why DeepDRK outperforms baselines: its null $w_j$ values are centered near zero while nonnull values remain large and positive, whereas baseline methods exhibit a positive shift in null statistics that degrades FDR threshold selection. This diagnostic goes beyond aggregate FDR/power numbers.

5. **Rigorous evaluation on non-Gaussian and small-sample data.** The paper evaluates on copula-based distributions (Clayton, Joe) with non-Gaussian marginals (§4.1) and on $n=200, p=100$ settings where baselines fail (e.g., Table 1: DeepDRK FDR mean 0.116 vs. DDLK 0.772). This demonstrates practical utility for biological/medical datasets, which are often small and non-Gaussian.

6. **Real-data case study with literature validation.** The IBD case study (§4.3) shows DeepDRK identifies 19/23 selected metabolites as literature-supported, a higher absolute count than most baselines. While qualitative, this demonstrates the method's practical applicability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Swapper mechanism is not fully specified.** The paper defines the swap loss using the notation $(X, \tilde{X}_\theta)_{S_{\omega_i}}$ (Eq. 3-4), and states that $K$ neural-network swappers $\{S_{\omega_i}\}_{i=1}^K$ "test whether the generated knockoffs satisfy the swap property" (line 88), but does not explain *how* a swapper produces the swapped tuple. What are the swapper's inputs and outputs? Does it output a probabilistic mask over features, a hard binary selection, or a direct permutation of the concatenated matrix? While the general paradigm follows DDLK's single-swapper attack, the paper's contribution is the *multi*-swapper design, and the mechanism by which each swapper produces a different adversarial environment should be clarified. This does not invalidate the results—the experiments demonstrate the method works—but it hampers reproducibility and makes it difficult for readers to assess or extend the approach. *Addressable in revision: a few sentences describing the swapper network's input/output/architecture would suffice.*

2. **DRP perturbation weight $\alpha_n$ is not reported for the experiments.** The paper defines $\alpha_n$ as a preset perturbation weight satisfying $\alpha_n \lesssim n^{-1/2}$ asymptotically (Proposition 1), but does not state what $\alpha$ values were actually used for the finite-sample experiments ($n=200$, $n=2000$), how it was chosen, or whether a sensitivity analysis was performed. Since $\alpha$ directly controls the trade-off between reduced reconstructability and swap property degradation at finite samples, its omission is a reproducibility gap. *Addressable in revision: report the values and describe selection procedure.*

3. **The claimed loss competition is asserted without direct empirical evidence.** Section 3.2 states that $\mathcal{L}_\text{SL}$ dominates and $\mathcal{L}_\text{DRL}$ increases after a short decreasing period, and claims to be "the first to observe this phenomenon in all deep-learning based knockoff generation models." However, no training curves or loss trajectories are shown in the main paper to support this claim or illustrate the phenomenon. A single training curve (e.g., $\mathcal{L}_\text{SL}$ and $\mathcal{L}_\text{DRL}$ over epochs) would make the motivation for the post-training DRP more concrete and credible.

4. **Asymptotic justification does not fully resolve the finite-sample concern.** The DRP guarantee (Proposition 1) is asymptotic ($n \to \infty$), yet the paper's main advantage is claimed precisely in the small-$n$ regime ($n=200$). The statement that $\alpha_n \lesssim n^{-1/2}$ provides a rate, but no finite-sample analysis or practical guidance is given for how to set $\alpha$ at $n=200$ given the asymptotic condition. The authors could address this by reporting the actual $\alpha$ used and showing that the SWD degradation is empirically negligible at the sample sizes tested.

### Trivial

- The REx and $\mathcal{L}_\text{swapper}$ regularization rely on cosine similarity between swapper weight vectors, which presumes all swappers share the same architecture. While this is standard and the rationale (preventing mode collapse) is stated, the paper could briefly justify why weight-space orthogonality is expected to produce functionally diverse swappers.

## Nice-to-Haves

- Training curve plots showing $\mathcal{L}_\text{SL}$ and $\mathcal{L}_\text{DRL}$ over epochs to empirically illustrate the claimed loss competition.
- Sensitivity analysis for the DRP hyperparameter $\alpha$ (e.g., FDR/power as a function of $\alpha$) to demonstrate robustness.
- Discussion of how the number of swappers $K$ affects performance.

## Removed Points

- *"The ablation studies are relegated to the appendix... the reader cannot verify"* — This is standard practice; ablation studies belong in the appendix for space reasons. The main text references them.
- *"The paper never defines what a swapper is" (as a fatal/gap)* — Downgraded from fatal to minor. The concept follows DDLK's established paradigm and the paper's contribution is in the multi-swapper setup, not the swapper definition itself. The notation $(X, \tilde{X}_\theta)_{S_{\omega_i}}$ conveys the intended operation. However, more detail would improve clarity, hence Minor #1.
- *"Cosine similarity on raw weights is peculiar / rationale unclear"* — The paper does explain the rationale (prevent mode collapse, Eq. 5). The criticism is a matter of design taste, not a factual error. Moved to Trivial.
- *"This is a fundamental gap in the description of the method... cannot be accepted"* — Overstated. The method is implementable given the loss definitions and the DDLK paradigm; the missing details are clarity issues, not conceptual gaps.

## Novel Insights

The reviews surface an interesting tension in the paper: the central theoretical justification (DRP's asymptotic guarantee that $\alpha_n \lesssim n^{-1/2}$ preserves the swap property as $n\to\infty$) is somewhat at odds with the paper's strongest empirical claim (excellent performance at $n=200$). This tension is not uncommon in deep knockoff papers and is worth flagging as an area for future work: a finite-sample analysis or tighter bound could strengthen the theoretical foundation. On the strength side, the paper's diagnostic analysis (Figure 5 on knockoff statistics centering) provides a clear mechanistic explanation for *why* DeepDRK outperforms baselines, which is a level of analysis often absent from knockoff papers that report only aggregate FDR/power numbers.

## Suggestions

1. Add a paragraph describing the swapper mechanism: input representation, output format, and how the swapped tuple $(X, \tilde{X}_\theta)_{S_{\omega_i}}$ is produced from the network's output.
2. Report the DRP weight $\alpha$ values used for each experimental configuration (n=200, n=2000) and describe the selection procedure.
3. Include a training curve figure showing $\mathcal{L}_\text{SL}$ and $\mathcal{L}_\text{DRL}$ over training epochs for at least one synthetic dataset.
4. Add a brief justification for why cosine similarity in weight space is expected to produce functionally diverse swappers, or consider a functional diversity measure.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>