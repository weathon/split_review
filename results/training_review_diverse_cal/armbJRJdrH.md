Now I have a thorough understanding. Let me produce the final consolidated review.

## Summary

This paper proposes rRCM (Robust Representation Consistency Model), a two-stage training framework for certified robustness. Stage 1 pre-trains a ViT encoder via instance discrimination that aligns representations of noisy views of the same image at different noise levels (framed as "points on the same PF ODE trajectory"). Stage 2 fine-tunes the encoder with a supervised objective combining cross-entropy, prediction consistency between two noisy views at the same noise level, and entropy regularization. The key claim is that this enables one-step denoising-then-classification — replacing the two-model (diffusion purifier + separate classifier) pipeline of prior diffusion-based methods with a single forward pass — yielding large certified accuracy gains (up to 11.6% at larger radii on ImageNet) with 85× average inference speedup over diffusion-based approaches.

## Strengths

1. **Strong certified accuracy with dramatic inference speedup**: On ImageNet, rRCM-B-Deep achieves 72.1% certified accuracy at radius 0.5 vs. 63.8% for DDS (Table 1), while reducing per-sample inference time from 52+ minutes (DensePure) to 53 seconds (rRCM-B). The gains are consistent across all evaluated radii and both ImageNet and CIFAR-10. This directly demonstrates the claimed efficiency-performance improvement.

2. **Novel one-step denoising-then-classification architecture**: The paper reframes the two-stage diffusion-based pipeline (separate denoiser + classifier) into a single model that performs both functions in one forward pass. This is a genuine architectural contribution that drives the latency improvement and simplifies deployment.

3. **Demonstrated scalability**: Increasing model capacity (rRCM-S → rRCM-B → rRCM-B-Deep) and training batch size both yield monotonic improvements in certified accuracy (Figures 3, 4), with performance not yet plateauing — a desirable property for large-scale datasets like ImageNet.

4. **Thorough experimental comparison**: Tables 1 and 2 include 10+ baselines spanning classical randomized smoothing (SmoothAdv, MACER, Boosting), diffusion-based methods (DDS, DensePure, DiffSmooth), and different evaluation budgets (10K/100K smoothing noises). The paper also reimplements baselines under controlled settings (same ViT backbone) for fairness.

5. **Honest reporting of limitations**: The paper acknowledges where it is outperformed (Boosting at r=0.75 on CIFAR-10), discloses the approximation used for PF ODE trajectory construction, and discusses the fundamental limitation that stochastic forward trajectories may diverge from PF ODE trajectories at high noise levels (Section 3.3).

## Weaknesses

### Fatal
None.

### Major

1. **Missing quantitative ablation for the core novelty — the pre-training stage**: The paper claims that its pre-training "significantly differs from previous methods" and states that it "conduct[s] further experiments and compare[s] the effectiveness of our method with MoCov3" (Section 3.3). However, Figure 5 is a conceptual illustration, not a quantitative comparison. No numerical results are provided comparing (a) training from scratch with only the fine-tuning objective, (b) pre-training with MoCov3 augmentations then fine-tuning, and (c) the proposed pre-training then fine-tuning. Without this ablation, it is not possible to isolate whether the performance gains come from the specific noise-level-based positive pair construction or simply from the contrastive pre-training + fine-tuning recipe. The paper notes (line 133) that training from scratch was "challenging" but offers no quantitative evidence. This gap directly undermines the substantiation of what the paper presents as its primary contribution (the structured noise schedule exploitation via contrastive denoising).

### Minor

2. **PF ODE framing is inflated relative to implementation**: The paper motivates its pre-training by appealing to the deterministic PF ODE and its non-crossing trajectory property (Section 3.1). However, the actual positive pair construction (Section 3.3) uses the approximation x_{t_{n-1}} = x_{t_n} + (t_{n-1} - t_n)ϵ — equivalent to the forward SDE step — not the true PF ODE step which requires the unknown score function ∇log p_t. While the paper does acknowledge this approximation (line 111) and cites Song et al. (2023), the PF ODE framing creates an expectation of theoretical grounding that the actual procedure does not deliver. The positive pairs trivially share the same clean image by construction, so the non-crossing trajectory argument is unnecessary to justify representation similarity. Reframing the contribution more precisely as "contrastive learning with noise-level-aware positive pairs" would be more accurate.

3. **Missing architecture and optimization details for reproducibility**: The paper states models "follow the Vision Transformer (ViT) architecture" but does not specify depth, width, patch size, or the exact configuration differences among rRCM-S, rRCM-B, and rRCM-B-Deep. Pre-training hyperparameters (learning rate, optimizer type, weight decay, learning rate schedule, warmup steps) are not reported; the paper only references EDM and MoCo-v3 implementations without specifying which settings are adopted verbatim and which differ.

4. **Scalability figures lack numerical values**: Figures 3 and 4 show certified accuracy vs. model size and batch size, but the text does not report the specific numerical values. Given these are central to the scalability claim, listing key numbers (e.g., certified accuracy at each radius for each model variant) would strengthen the presentation.

5. **Entropy regularization hyperparameter not ablated**: The entropy term coefficient η₂=0.5 is fixed across all experiments without discussion of sensitivity. Since entropy minimization encourages confident predictions (which directly affects the certified radius calculation), some analysis of the impact of this choice would be helpful.

6. **"First to exploit structured noise schedule" is somewhat overstated**: Prior work on diffusion-based randomized smoothing (DDS, DensePure, DiffSmooth) uses noise schedules during inference-time purification. The novelty is in using the noise schedule during *classifier training* — a meaningful distinction — but the claim as phrased could be read as broader than warranted.

### Trivial

- The term "consistency loss" for the first term in Eq. 7 could cause confusion with consistency models (Song et al., 2023), since the objective is an infoNCE loss rather than enforcing the same-output property of generative consistency models. The paper itself notes the contrastive nature.
- The evaluation uses standard noise levels (σ ∈ {0.25, 0.5, 1.0}); evaluating at an intermediate level (e.g., σ=0.75) would add completeness but is not necessary given the three points already span the relevant range.

## Nice-to-Haves

- A quantitative ablation comparing "fine-tune from scratch," "fine-tune from MoCov3 pre-training," and "fine-tune from rRCM pre-training" under identical conditions.
- Reporting throughput (images/second) in addition to total certification latency to enable cleaner cross-method comparisons.
- A brief analysis of the sensitivity of certified accuracy to η₂.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Latency numbers are "not credible" (from Harsh Critic)**: The reviewer claims the paper reports 0.35 seconds for rRCM-B with 10,000 smoothing noises, implying 35 µs per forward pass. The number "0.35" does not appear in the paper text. The paper states rRCM-B takes 53 seconds per sample (Table 1). 53 seconds / 10,000 passes = 5.3 ms per forward pass, which is physically plausible for a batched ViT-B on an A800 GPU. The reviewer's specific calculation (35 µs) cannot be verified against the paper text and appears to be a misreading of the table. The 85× speedup claim is relative to DensePure (52+ minutes), not to 0.35 seconds. *Removed because the criticism is factually unverifiable from the paper and contradicts the text's stated numbers.*

2. **Criticism that DDS latency implies unrealistic per-pass time**: The reviewer claims DDS at 2.5 seconds for 10,000 passes implies 250 µs per pass, calling this "optimistic." Whether or not this is optimistic, it is a statement about a *baseline* (DDS, a prior method), not about the paper's own method. Per the rules, "weaknesses about unfair comparison with other methods [should be removed] if the asymmetry favors the baseline." The paper is not responsible for the plausibility of its baselines' reported latencies. *Removed as it does not reflect on the paper's own claims.*

3. **Criticism that the PF ODE claim means "the same positive pair construction is available without any diffusion model machinery"**: This is technically true but misses the point — the diffusion model machinery provides the *motivation* for the specific positive pair construction (same-noise-direction, two-noise-level). The paper's contribution is the combination of this construction with the training framework, not a claim that the construction is impossible without diffusion models. *Downgraded to Minor (Point 2 above) — the framing is inflated but the paper acknowledges the approximation.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension: the paper's strongest selling point (dramatic certified accuracy gains at low inference cost) is well-supported, but the weakest link (the novelty of the pre-training relative to standard contrastive learning) is unablated. This gap between empirical strength and conceptual framing is the core issue.

## Suggestions

1. **Add the missing ablation**: Compare (a) fine-tune from scratch (random init), (b) fine-tune from MoCov3 pre-training on ImageNet, and (c) fine-tune from rRCM pre-training, using identical fine-tuning stages. Report certified accuracy at each radius for all three. This single experiment would substantially strengthen the paper.

2. **Reframe the PF ODE motivation**: Acknowledge directly that the positive pair construction approximates the PF ODE step using Tweedie's formula / the forward-path shortcut, and that this approximation is adopted from consistency models (Song et al., 2023). Emphasize that the PF ODE serves as *motivation* for aligning representations along the noise level axis, rather than claiming the training follows exact PF ODE trajectories.

3. **Report architecture details and key hyperparameters**: Specify ViT depth/width/patch size for each model variant, and report learning rate, optimizer, weight decay, and schedule for pre-training and fine-tuning stages.

## Score and Decision

The paper presents a well-executed combination of ideas that yields strong empirical results on certified robustness — consistently beating both classical and diffusion-based methods on ImageNet and CIFAR-10 while dramatically reducing inference cost. The one-step denoising-then-classification architecture is a genuine contribution. However, the paper's central claim about exploiting the structured noise schedule via the specific pre-training strategy is not adequately ablated against simpler alternatives (e.g., MoCov3 pre-training, training from scratch), making it difficult to assess what drives the gains. The PF ODE framing is also somewhat overclaimed relative to the approximation actually used. These are addressable weaknesses — they do not invalidate the results but they do temper the novelty claim. The paper merits acceptance contingent on adding the key ablation and honestly reframing the contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>