Here is my consolidated review after cross-checking every claim against the paper.

---

## Summary

This paper identifies a specific cause of out-of-the-box performance degradation in video foundation models — text encoder overfitting to ASR transcripts during end-to-end fine-tuning — and proposes a simple remedy: partially freezing the text encoder (shallow layers frozen, deep layers tunable). Building on the TVTS framework with tube masking for scalability, the authors train a series of models up to ViT-H/14 (1B parameters) and achieve state-of-the-art zero-shot results across retrieval and action recognition benchmarks, with consistent gains over CLIP baselines, ImageBind, and InternVideo.

## Strengths

- **Pinpoints a concrete cause of video model degradation.** The paper's empirical analysis (Table 1) shows that end-to-end fine-tuning (M₂-FT) and fully frozen text encoders (M₂-FF) both underperform the CLIP baseline, while partial freezing (M₂-PF) recovers and surpasses it (0.340 vs. 0.295 MMS on DiDeMo). The L_tune ablation (Fig. 1b) systematically validates that neither fully frozen nor fully fine-tuned extremes work, establishing a clear U-shaped performance curve. This diagnosis — that distortion in the text encoder's supervision signal, not just visual overfitting, drives degradation — is a genuine insight.

- **Consistent SOTA out-of-the-box results across multiple benchmarks.** Ours-H/14 achieves 41.3% R@1 on MSR-VTT retrieval (+4.5 over ImageBind), 59.6% top-1 on K-400 zero-shot action recognition (+9.6 over CLIP, +9.6 over ImageBind), and 48.4% on SSV2-MC (+12.9 over CLIP-ViP). These gains are replicated across B/32, B/16, and H/14 scales, lending credibility to the core claim.

- **Practical scaling result.** Training a 1B-parameter model on 80 V100s in one week (70% tube masking, ViT-H/14) is a nontrivial engineering contribution that makes billion-scale video pre-training more accessible.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Missing core training hyperparameters.** The paper reports temperature (0.05), K=4 segments, T=12 frames, and masking ratios, but omits batch size, total training steps/epochs, learning rate, learning rate schedule, warmup, weight decay, and optimizer choice. These are standard reproducibility details, not trivial. Without them, readers cannot assess the training budget or reproduce the baselines (M₁-FT, M₂-FT, M₂-FF, M₂-PF) in Table 1 — which is especially problematic since the critic correctly notes that the gap between M₂-FF (0.187 MMS) and M₂-PF (0.340) could partly reflect optimization differences. *Fixable in a revision.*

2. **The "comparable" claim to DINOv2-g is overstated.** The paper states "comparable performance to DINOv2-g on linear K400 with 40% fewer parameters" (line 62). The actual numbers are Ours-H/14: 73.1% vs. DINOv2-g: 78.4% — a 5.3 absolute point gap. "Competitive given the parameter advantage" would be more accurate. The paper's overall contribution does not hinge on this comparison, but the framing should be corrected.

3. **Table 1 baselines are diagnostically useful but not fully controlled.** The critic's concern that M₂-FF and M₂-PF may have used different hyperparameters is valid — the paper does not state whether they were trained identically aside from the freezing strategy. This is partially redeemed by the systematic L_tune ablation (Fig. 1b) which varies only the number of frozen layers, but the paper should clarify whether Table 1 training conditions were held constant across rows. *Easy to address in rebuttal.*

4. **Number of text encoder layers ($L_T$) is not stated for each model variant.** The ablation on $L_\text{tune}$ (Fig. 1b) reports performance as a function of tunable layers, and the paper says "freeze the first three-quarters of layers" (line 196), but never gives the actual $L_T$ values for ViT-B/32, B/16, or H/14. A reader familiar with CLIP can infer 12 layers for B/32 and B/16, but the H/14 text encoder depth should be stated explicitly.

### Trivial

- The paper says "the magnitude of publicly accessible videos is much smaller than images, e.g., HowTo100M vs. LAION-5B" as a general motivation. This is not a claim about the paper's own data (which uses 6M+2.5M videos) and is fine as-is, but the phrasing could be tightened to avoid confusion.

## Nice-to-Haves

- **Confidence intervals or multiple-seed results.** The paper reports only point estimates for all main results. While single-run evaluation is standard in large-scale video pre-training papers (CLIP, CLIP-ViP, ImageBind, InternVideo all do the same), adding standard deviations from 2–3 seeds would strengthen evidential credibility, especially for the SSV2-MC gain (+12.9 over CLIP-ViP) which is the largest single improvement.

- **Direct measurement of text encoder generalization.** The paper's claim that partial freezing "preserves generalization" is supported indirectly (via downstream video task performance). A more direct analysis — e.g., measuring the frozen+tuned text encoder's zero-shot image classification accuracy on ImageNet or CIFAR-100 before and after video pre-training — would make the "degradation-free" claim more concrete.

- **Ablation of the "three-quarters" heuristic.** The paper freezes the first 3/4 of layers without justification for this specific ratio. Does the optimal fraction vary with model scale? A sweep of freeze ratios (e.g., 0%, 25%, 50%, 75%, 100%) would be informative.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Missing related works (VideoPrism)"** — Removed per hard rule: do not mention missing related works; I have no external sources to confirm whether VideoPrism existed at submission time or is relevant.
- **"HowTo100M vs LAION-5B framing overstates data limitation"** — Removed: this is a general illustrative example in the introduction, not a claim about the paper's own data regime. The paper accurately states its own data (6M+2.5M videos).
- **"Whether CLIP-ViP uses official checkpoint in Table 1"** — Removed: the table caption explicitly states "tests are done with the officially released ViT-B/32 models," so this is already addressed.
- **"Figure legibility / missing appendix / formatting nitpicks"** — Removed per hard rules: these are parser artifacts, not author errors.
- **"Missing discussion of shortcut learning"** — Removed: the paper already discusses shortcut learning (lines 239–241, 458) and addresses it with the stop-gradient trick.

## Novel Insights

The insight that text encoder overfitting — not just visual overfitting — drives out-of-the-box degradation in video models is the paper's most valuable conceptual contribution. The finding that partial freezing outperforms both extremes (fully frozen and fully fine-tuned) mirrors the "head tuning" phenomenon in transfer learning but is novel in the context of video-language pre-training where ASR transcripts create a domain gap from the original CLIP alt-text distribution. The ablation on $L_\text{tune}$ is clean evidence for this phenomenon. Otherwise, the paper's insights are well-captured by its own contributions.

## Suggestions

1. Add a dedicated implementation details subsection with: batch size, total training steps/epochs, optimizer (type, β₁, β₂, ϵ), learning rate (peak value, schedule, warmup steps), weight decay, and gradient clipping.
2. Correct the DINOv2-g framing: rephrase "comparable" to "competitive" or "close to" with explicit acknowledgment of the 5.3 pp gap.
3. State $L_T$ (total text encoder layers) explicitly for each model variant (B/32, B/16, H/14).
4. Clarify that the four Table 1 baselines (M₁-FT, M₂-FT, M₂-FF, M₂-PF) were trained under identical hyperparameters except for the freezing strategy; if they were not, note this limitation.

## Score and Decision

The paper makes a genuine, well-supported contribution to video representation learning. The core diagnosis (text encoder overfitting → degraded supervision → poor out-of-the-box features) is convincingly demonstrated, and the partial freezing remedy is simple yet effective. Weaknesses are limited to incomplete reproducibility documentation and one overstated comparison — none threaten the central claims. The paper deserves publication after addressing the training details and correcting the DINOv2 claim.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>