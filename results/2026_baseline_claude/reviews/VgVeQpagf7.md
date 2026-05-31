## Summary

The paper introduces SPS (Summarize-Privatize-Synthesize) and SPS+, algorithms for generating a differentially private synthetic version of a sensitive dataset by adapting the D3S dataset distillation framework. Rather than privatizing a model (as in DP-SGD), SPS privatizes low-dimensional intermediate activation statistics extracted by a public pretrained model via a single application of the Gaussian mechanism. Two enhancements—multistage clipping and grouped pseudo-classes—yield SPS+, which claims to be the first generation-based approach to match or exceed DP-SGD on image classification, achieving 96.2%/76.6% on CIFAR-10/100 at ε=1 with ensemble models versus DP-SGD's 94.8%/70.3%.

---

## Strengths

- **First generation-based method to reach parity with DP-SGD on image classification.** Prior best was 89.1% (Private Evolution) on CIFAR-10 at ε=10, while SPS+ singles achieve 95.1–95.5% at ε=1 (and ensembles reach 96.2%). This is a concrete, verifiable milestone for the private ML community.
- **Elegant privacy design with reduced dimensionality.** The key insight—collecting and privatizing only the low-dimensional layer-level statistics (~10⁵) rather than full gradients (~10⁷)—directly improves the signal-to-noise ratio of the privatized quantity. The single-shot Gaussian mechanism (rather than iterative composition like DP-SGD) makes the accounting clean and tight.
- **Well-motivated, novel algorithmic contributions.** The noise redistribution between global and class-specific statistics (Section 3.2.4), multistage clipping that re-centers on previous estimates, and grouped pseudo-classes are each independently motivated and empirically validated. The insight that GPC improves optimization via covariance inversion dynamics (but not direct mean estimation) is non-trivial.
- **Practical flexibility demonstrated concretely.** The post-processing property allows SPS synthetic data to be freely reused: federated learning (asynchronous, no gradient sharing), class-incremental continual learning, and ensembling are all evaluated experimentally and compared to relevant baselines (FedLAP-DP, FedDM).
- **Fair comparison setup.** Both SPS+ and the DP-SGD baseline (De et al., 2022) use the same public pretrained WRN-22-8 on ImageNet as the starting point, making the accuracy comparison meaningful.

---

## Weaknesses

### Fatal
None identified.

### Major

- **Single-model SPS+ vs. DP-SGD disparity on CIFAR-100 at moderate ε.** The abstract claim that SPS+ "outperforms" DP-SGD uses ensemble numbers. For single models at ε=4, SPS+ (WRN34-10) achieves 77.2% vs. DP-SGD's 79.2%; it only surpasses DP-SGD via ensembling. This nuance is buried in Table 1 and warrants more prominent discussion: the single-model advantage holds at ε=1 for CIFAR-100 (71.9% vs. 70.3%, marginally), but SPS+ clearly needs ensembling to dominate at moderate privacy budgets. Ensembling is a legitimate structural advantage, but the headline claim should be stated with greater precision.

- **Computational overhead is acknowledged but not quantified in the main body.** The paper notes that "the cost of generating these images is relatively heavy" and defers to an appendix section (F.1), which was stripped. Image synthesis via optimization over the KL objective is inherently expensive; the community needs to understand the compute cost relative to DP-SGD fine-tuning in the main text to properly evaluate the trade-off.

### Minor

- **CAMELYON17 comparison uses different ε values.** SPS achieves 92.6% at ε=8, while DP-SGD baseline is 90.5% at ε=10. A smaller ε should be strictly harder, so this is a favorable comparison for SPS; an ε-matched comparison or an SPS result at ε=10 would be cleaner.
- **Grouped pseudo-classes mechanism lacks detailed intuition.** The claim that GPC "only works due to dynamics of optimizing the loss function, specifically the Σ inversion in the KL divergence, and the eigenvalue clipping of Σ" is stated but not derived or empirically isolated. An ablation showing that GPC fails for direct mean estimation (as claimed) and why the covariance inversion is the key driver would strengthen this.
- **No comparison of DP-SGD on WRN-34-10.** The paper argues that DP-SGD with a larger model incurs higher privacy cost, which is true—but a number from De et al. or a controlled comparison would quantify how much performance improvement is gated behind the model-size advantage of SPS.

### Trivial

- Figure caption duplication (text appears to be parsed twice for Figures 1 and 2).

---

## Nice-to-Haves

- An ablation that shows the gain from each component: public pretraining, noise redistribution, MC, and GPC in isolation would help readers understand their relative importance.
- A brief theoretical analysis of utility (bias/variance trade-off under noise) to complement the empirical ablations.
- Extension to ViT-family backbones or a discussion of how SPS would behave without BatchNorm-like layers.

---

## Novel Insights

The paper's most genuinely novel insight is that the information bottleneck imposed by low-dimensional activation statistics is a feature rather than a limitation when operating under differential privacy: it allows a single-shot, low-sensitivity privatization step rather than iterative composition over high-dimensional gradient updates. The grouped pseudo-class technique further reveals an interesting asymmetry—grouping classes introduces covariance coupling that improves optimization dynamics even when group memberships are random, a phenomenon that doesn't arise in direct mean estimation and hints at a broader principle connecting aggregation structure to DP-compatible optimization. The multistage clipping adaptation from mean estimation to full statistic matching is a concrete and reusable pattern.

---

## Suggestions

- Report single-model vs. ensemble comparisons explicitly side by side in the abstract and Section 5.1 narrative to avoid overstating the headline result.
- Add a compute-cost table (wall-clock time, GPU hours) for dataset synthesis vs. DP-SGD fine-tuning in the main paper.
- Provide an ablation isolating MC and GPC contributions to disentangle their individual effects, particularly on CIFAR-100 at ε=1.
- Include an ε=10 or ε=8 number for DP-SGD on CAMELYON17 at the same ε as SPS to make Table 2 directly comparable.

---

## Score and Decision

The paper presents a genuine and important empirical milestone: a generation-based private learning method that for the first time matches DP-SGD on image classification. The technical contributions are non-trivial and the practical use-cases (federated learning, continual learning, ensembling) are experimentally validated. The main weaknesses—headline precision around ensembling, missing compute cost in the main body, and underexplained GPC mechanism—are real but do not undermine the core result. This is a solid above-average contribution to the differentially private ML literature.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>