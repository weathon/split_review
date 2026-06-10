## Summary

This paper proposes PCME++, an improved probabilistic cross-modal embedding framework for image-text matching. The core contribution is a closed-form sampled distance (CSD) that replaces the expensive Monte Carlo approximation used by the prior PCME method, enabling faster computation and ANN compatibility. The paper further introduces two optimization techniques—pseudo-positives (PP) and mixed sample data augmentation (MSDA)—designed for the pairwise BCE objective. Experiments on COCO Caption and extended benchmarks show competitive results across ViT-B/32, ViT-B/16, and ViT-L/14 backbones, along with uncertainty analyses and a prompt-filtering application.

## Strengths

- **Closed-form sampled distance (CSD) is a clean, practical improvement over PCME.** Deriving the closed-form expectation $\mathbb{E}\|\mathbf{Z}_v-\mathbf{Z}_t\|_2^2 = \|\mu_v-\mu_t\|_2^2 + \|\sigma_v^2+\sigma_t^2\|_1$ eliminates Monte Carlo sampling during both training and inference, making the approach compatible with approximate nearest neighbor search (e.g., FAISS). The toy experiment (Figure 2) provides evidence that CSD better separates certain from uncertain samples compared to Wasserstein-2 distance, and Table 3 (tab:probdist_abl) confirms that CSD substantially outperforms WD (RSUM 534.5 vs. 121.1) as a training objective.

- **PCME++ consistently achieves the best results across all backbones on the primary benchmarks.** In Table 1, PCME++ outperforms or matches all deterministic (VSE∞, InfoNCE) and probabilistic (PCME) baselines on ECCV Caption mAP@R, CxC R@1, and COCO RSUM. The advantage is clearest at ViT-L/14 scale, where PCME++ reaches RSUM 554.7 vs. PCME 550.4, while deterministic methods degrade.

- **The uncertainty analysis provides interpretable insights.** The paper demonstrates (Figure 3) that learned variance $\|\sigma^2\|_1$ correlates inversely with retrieval accuracy—samples with higher uncertainty indeed have lower R@1 on the training distribution. This validates that the probabilistic framework captures genuine dataset ambiguity rather than producing arbitrary variance estimates.

## Weaknesses

### Major

**1. The ablation study does not support the claimed effectiveness of the individual optimization techniques.**

Table 2 (tab:loss_abl) is the critical diagnostic. The baseline model (CSD + BCE loss, no VIB/PP/MSDA) achieves RSUM 535.9. Adding VIB alone *reduces* RSUM to 534.5. Adding PP alone yields RSUM 536.0—essentially flat. Adding MSDA alone yields RSUM 535.5—a slight decrease. Adding VIB+PP together (without MSDA) gives RSUM 534.8, *worse* than the baseline. Only the full combination of all three components reaches 537.0.

The paper states (§4.3) that "all the proposed techniques effectively improve probabilistic ITM" without acknowledging or analyzing this pattern. This is not a pattern of individually effective components that combine additively—it is a pattern where components individually hurt or flatline, and only the specific three-way combination produces a gain. Without an explanation of why the interaction is synergistic (or whether the improvement is an artifact of hyperparameter tuning for the full configuration), the reader cannot evaluate whether PP and MSDA are genuine contributions or accidental interactions. This significantly undermines the paper's narrative that PP and MSDA are independently valuable optimization techniques.

**2. Performance gains over the strongest deterministic baselines are marginal at practical backbone sizes, and the larger-scale comparison relies on a poorly-tuned baseline.**

For ViT-B/32: PCME++ RSUM 537.0 vs. VSE∞ 536.5—a gain of +0.5 (0.09%).
For ViT-B/16: PCME++ RSUM 548.0 vs. VSE∞ 547.2—a gain of +0.8 (0.15%).

The paper reports three-run averages without standard deviations, so it is impossible to assess statistical significance. These margins are within typical run-to-run variation for this task.

The more dramatic story is at ViT-L/14, where VSE∞ drops from RSUM 547.2 (B/16) to 424.3 (L/14)—a catastrophic collapse—while PCME++ reaches 554.7. However, the paper states (§4.1) that "optimization hyperparameters for all experiments are fixed, such as learning rate, based on VSE∞ ViT-B/32 validation RSUM score." This means the deterministic baselines at ViT-L/14 were almost certainly using ill-suited hyperparameters. The paper attributes the collapse to a fundamental failure of deterministic methods under FNs, but the experimental design confounds architecture scaling with hyperparameter mismatch. A properly tuned VSE∞ at ViT-L/14 would likely perform far better. The only clean comparison at this scale is PCME (550.4) vs. PCME++ (554.7)—a +4.3 gain that is credible but more modest than the paper's framing suggests.

**3. The "zero-shot" classification experiment is not a valid zero-shot evaluation and is misleadingly presented.**

Section 5.3 reports an ImageNet classification experiment where the "Best top-K for each class" strategy (41.82%) selects per-class prompt subsets using the *ImageNet validation set* to choose K individually for each class. The paper acknowledges this is "not a true ZS" in the text, but the table is titled "ImageNet Zero-shot" and the result is presented as a positive capability demonstration. Selecting optimal per-class K on the evaluation distribution means the comparison to a fixed single-prompt baseline (30.43%) is not a test of zero-shot ability—it is a test of how much supervised post-hoc selection on the target distribution can boost accuracy. Furthermore, with all 80 prompts, PCME++ (34.22%) underperforms the InfoNCE baseline (35.50%), and with a single prompt PCME++ achieves only 30.43%. This experiment should either be conducted in a genuinely zero-shot manner (fixed K chosen without validation set access) or clearly labeled as supervised prompt selection.

### Minor

- **The 33% speedup claim is unsubstantiated.** The paper claims (§3.2, line 64) that PCME++ is "empirically... 33% faster than PCME" but provides no wall-clock timing, throughput measurements, or training-time comparison in any table or figure. Given that computational efficiency is one of the two primary motivations for CSD (the other being ANN compatibility), the absence of any quantitative speed benchmark is a notable omission.

- **PP is sensitive to the noise level, with no guidance for unknown noise.** The PP weight α must be reduced from 0.1 (clean) to 0.01 (20% noise) to 0.0 (50% noise). The paper does not discuss how to set α in practice when the noise level is unknown, which limits the method's practicality.

- **The paper reports averages over three runs but never reports standard deviations or confidence intervals.** This makes it impossible to assess whether the small margins (e.g., +0.5 RSUM) are meaningful or noise.

- **The noisy correspondence results for PCME++ are absent from Table 3** (likely a parser artifact, as the LaTeX `\multirow{6}` header suggests a sixth row exists). If PCME++ results were indeed present in the original submission, this is a non-issue; if not, the paper's claim that "ours successfully handles the scenario" would be unsupported.

### Trivial

- The $\beta = 0$ notation on line 83 appears to be truncated or a formatting artifact ("$\beta = 0."). If VIB is used as claimed, $\beta$ must be positive; the value needs clarification.

## Nice-to-Haves

- **Wall-clock speed benchmarks** comparing PCME vs. PCME++ training and inference time on the same hardware would concretely demonstrate the efficiency advantage of CSD.
- **Analysis of the VIB × PP × MSDA interaction.** Understanding why the combination works when individual components do not would substantially strengthen the paper.
- **Statistical significance testing** (e.g., bootstrap or paired tests across runs) for the small RSUM differences.

## Removed Points

*These points were flagged by reviewers but removed during merging due to the filtering rules specified.*

- **"Missing PCME++ results in noisy correspondence table"**: The LaTeX source contains `\multirow{6}` headers implying 6 rows per noise ratio, but only 5 methods are visible in the extracted text. This is a parser artifact; the original submission likely included PCME++ results. Removed per the hard rule that parser artifacts are not author errors.
- **"CSD vs. Wasserstein theoretical justification overstated"**: The critic argued the analysis assumes fixed μ, but the paper provides a toy experiment as empirical support. This is a nuanced scientific point, not a clear weakness. Demoted to Removed Points.
- **"β=0 confusion"**: Likely a formatting/truncation artifact. Removed per hard rule about parser/formatting issues.
- **"MSDA 25% choice unexplained"**: A minor design choice that does not affect the core claim. Removed per soft filtering.
- **"HNM framing lacks evidence"**: The paper provides t-SNE visualization and references prior work. The critic's skepticism is reasonable but does not rise to a concrete weakness about the paper's results. Removed.

## Novel Insights

None beyond the paper's own contributions. The CSD closed-form distance is the primary novelty; most other observations (marginal gains, ablation interaction, baseline tuning issues) are straightforward consequences of reading the evidence presented.

## Suggestions

1. **Re-evaluate the ViT-L/14 deterministic baselines with properly tuned hyperparameters** for each backbone size. Report what a well-tuned VSE∞ or InfoNCE achieves at this scale. If the advantage of probabilistic methods persists, it becomes much more convincing.

2. **Either remove or restructure the zero-shot experiment.** Present it as supervised per-class prompt selection on ImageNet validation—which is interesting in its own right—rather than framing it as zero-shot capability.

3. **Provide wall-clock speed measurements** for the claimed 33% speedup, including both training iteration time and inference throughput.

4. **Add a discussion of the ablation interaction.** Even a brief hypothesis about why VIB+PP+MSDA works when the parts individually don't would help readers evaluate whether the improvement is reliable.

5. **Report standard deviations** for the three-run averages, at least for the key RSUM comparisons.

## Score and Decision

The paper has a genuine core contribution in the CSD closed-form distance, and the consistent top-line results across backbones are positive. However, the paper oversells its optimization techniques (PP, MSDA) in ways not supported by its own ablation evidence. The performance margins at practical backbone sizes are small, and the experimental comparison at ViT-L/14 is confounded by improper baseline tuning. The zero-shot experiment is methodologically questionable. A major revision that tones down unsupported claims and addresses the experimental gaps would produce a stronger paper. In its current form, the evidence does not fully substantiate the paper's claimed contributions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>