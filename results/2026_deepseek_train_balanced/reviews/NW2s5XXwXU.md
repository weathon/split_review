## Summary

This paper tackles long-tailed generation with diffusion models. It proposes T2H (noisy Tail to clean Head) and H2T (noisy Head to clean Tail) strategies that, during training, replace the denoising target for a sample with one from another class selected via a similarity-based Gaussian kernel over a batch. A Batch Re-sample strategy ensures balanced class representation in the reference batch. The method outperforms prior long-tail generation methods (CBGAN, gSR-GAN, CBDM) on CIFAR10LT, CIFAR100LT, and TinyImageNet200LT, and shows improved robustness to extended training schedules.

## Strengths

- **Consistent and often substantial improvement across multiple datasets**: T2H improves over CBDM by 0.38 FID on CIFAR10LT (imb=0.01), 1.29 on CIFAR10LT (imb=0.001), 2.43 on CIFAR100LT, and 8.54 on TinyImageNet200LT (Tables 2, 3 in text and embedded figures). The pattern holds across four different dataset configurations, not a single lucky run.

- **Identifies and empirically validates the optimal transfer window**: The paper shows that the transfer probability transitions from ~0 to ~1 across diffusion steps 500–800 (Figure 7), and that restricting transfers to this range yields the best FID scores. This grounds the design choice in the known "high variance" semantic-formation period (Xu et al., 2023) rather than relying on a heuristic.

- **Demonstrates training-time robustness**: Figure 6 shows that while CBDM's FID degrades substantially over long training (~800k steps), the proposed method maintains stable performance, directly supporting the claim that data-driven references avoid the bias accumulation that model-prediction-based augmentation suffers from.

- **Proposition 3.1 provides a non-trivial bound connecting transition strength to both label frequencies and sample similarity**: The bound $\mathbb{E}[\dots] \le \frac{B}{2} (q(y^H) q(y^T))^\beta \exp(-\|x_0^H - x_0^T\|_2^2 / 8\sigma_t^2)$ formally shows that effective head-to-tail transfer depends on both the label product and the L2 similarity, motivating the batch re-sampling strategy in a principled way.

## Weaknesses

### Fatal
None.

### Major

- **No variance estimates or multiple-seed runs for any reported result**: All reported FID scores are single values. On CIFAR10LT (imb=0.01), the improvement over CBDM is only 0.38 FID — a margin that could fall within run-to-run noise for diffusion model training. The consistent pattern across datasets partially mitigates this concern, but for the headline claim on the primary benchmark, the absence of error bars substantially weakens the quantitative evidence. This is especially consequential because the method itself adds stochasticity at the batch construction and per-sample selection levels (the multinomial draw in Eq. 8).

### Minor

- **The selection kernel uses pixel-space L2 distance at noise levels where this distance may lose semantic content**: The selection probability $p_{sel}(z) \propto \exp(-\|x_0^{(z)} - x_t\|_2^2 / 2\sigma_t^2)$ measures pixel-space distance between noisy $x_t$ and clean references. At large $t$, $x_t$ is heavily corrupted and this distance is dominated by noise, making selection effectively random. The paper partially addresses this through the cutting-time analysis (Figure 7), identifying the 500–800 step optimal range and showing that restricting transfers to this window avoids the problem. However, the paper does not discuss whether the $x_t$-to-other-class-$x_0$ comparisons at moderate noise levels reliably select semantically appropriate head-class targets, or whether semantically distant head-tail class pairs could receive inappropriate transfers.

- **No per-class or per-tail evaluation**: The paper claims to improve "diversity of tail classes" but only reports aggregate FID. For conditional generation, 50k/L images are generated per class, yet no per-class FID, Intra-FID for tail categories, or other class-conditional metric is shown. The central claim about tail-class improvement would be substantially stronger with per-class breakdowns.

- **Proposition 3.1 is motivational rather than providing actionable guarantees**: The bound characterizes how transition strength depends on label frequencies and sample similarity, motivating the batch re-sampling strategy. However, it does not provide convergence guarantees, bias bounds, or any formal property of the algorithm's output distribution. The proposition is reasonable as motivation but the paper's abstract describes it as "statistical analysis to validate this methodology," which overstates its role.

- **The core claim about CBDM's bias is supported only through aggregate comparisons, not a controlled ablation**: The paper repeatedly argues that CBDM's model-prediction-based references introduce bias, and that data-driven references avoid this. While the overall FID comparisons (Tables 2, 3) and robustness curves (Figure 6) are consistent with this claim, there is no ablation that isolates only the reference source (data vs. model prediction) while holding everything else fixed. Such an experiment would directly validate the central motivation.

### Trivial
None.

## Nice-to-Haves

- **A controlled ablation isolating the reference source (data vs. model prediction)**: The paper's central motivation — that data-driven references avoid bias from model predictions — would be much more directly evidenced by an experiment where only the reference source is swapped while keeping all other training conditions identical. This would complement the already-convincing overall comparisons.

- **Per-class FID or Intra-FID for tail classes**: This would directly substantiate the claim about tail-class diversity improvement, which aggregate FID can only indirectly support.

- **Downstream classifier evaluation on generated tail-class samples**: This is a common auxiliary evaluation in long-tail generation work and would further strengthen the paper's claims about the practical utility of the generated data.

- **Discussion of failure modes or cases where head-to-tail transfer could be harmful** (e.g., when head and tail classes are semantically distant, the L2-based selection may propose inappropriate targets).

## Removed Points

- "No IS values discussed in text" — The tables are embedded images; the parser cannot render them. This is a presentation artifact, not an author error.
- "Broken equations in the CBDM connection section (line 138)" — Parser artifact. The original paper does not have broken equations.
- "Missing training details / batch size K not specified" — The paper states it "strictly follows CBDM's implementation," which is standard practice for a follow-up method.
- "Critique of CBDM as relying on model prediction is never demonstrated quantitatively" — It IS demonstrated through the overall comparison results (Tables 2, 3) and the robustness experiment (Figure 6). The evidence is indirect (aggregate comparison rather than a single-variable ablation) but present. Moved to minor weakness as a request for a cleaner ablation.
- "Only image generation is evaluated — could show downstream classifier performance" — This is scope creep; the paper's contribution is to image generation, and it evaluates using standard generation metrics.
- "The soft weighted averaging version is never implemented in main experiments" — Figure 5 explicitly evaluates the soft version (β sweep) and validates that the hard gating version is approximately equivalent. This is incorrect as stated.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface any perspective on the paper's approach, positioning, or implications that the authors had not already articulated.

## Suggestions

- Run the main experiments with at least 3 random seeds and report mean ± std for FID. This is the single highest-leverage improvement: if the 0.38 FID gap on CIFAR10LT holds with tight error bars, the headline claim is credible; if it falls within noise, the paper needs to reframe its claims around the larger-margin datasets (where improvements are 1.29–8.54 FID).
- Add per-class FID or Intra-FID for tail classes to directly evidence the diversity improvement claim.
- Include a discussion of when the L2-based selection mechanism might select inappropriate targets (e.g., when head and tail classes are semantically unrelated), and whether the cutting-time strategy fully mitigates this.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>