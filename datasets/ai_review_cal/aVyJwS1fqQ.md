- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6
Now I have all the information needed. Let me verify the specific claims against the paper and produce the consolidated review.

**Key verification results:**
- The paper does NOT state the number of trials in the planning experiment (no "trial" match). The critic's "10 trials per task" is not in the paper.
- No variance/error bars reported (grep confirms zero matches for seed, variance, standard dev, error bar, confidence).
- Human evaluation: only mentions "user study" with no participant count or procedural details.
- VDM/LVDM adaptation: "encode the trajectory into an embedding" — no hyperparameter tuning reported.
- VLP mentioned in Related Work (line 30) but not compared.
- Scaling: described qualitatively, single curves shown.

Now I'll synthesize the review.

---

## Summary

This paper proposes Mani-WM, a diffusion-transformer-based world model that generates video of a robot arm executing an action trajectory given an initial frame (trajectory-to-video). The key technical contribution is a frame-level adaptive normalization (Frame-Ada) mechanism that conditions each generated frame on its corresponding individual action, enabling precise action–frame alignment. The model uses spatial-temporal attention for efficiency and a DiT backbone for high-quality generation. Experiments on four real-robot datasets (RT-1, Bridge, Language-Table, RoboNet) show that Mani-WM outperforms VDM, LVDM, iVideoGPT, and MaskViT on the primary metrics (Latent L2, PSNR), with human raters consistently preferring Mani-WM's outputs. Additional experiments demonstrate scaling behavior, flexible action controllability from diverse input sources, and a real-robot model-based planning demonstration.

## Strengths

1. **Frame-level conditioning (Frame-Ada) is clearly validated.** Table 1 shows that Mani-WM-Frame-Ada consistently outperforms the video-level variant (Mani-WM-Video-Ada) on Latent L2 loss and PSNR across all three primary datasets (RT-1, Bridge, Language-Table), directly supporting the paper's central architectural claim that frame-by-frame action conditioning is beneficial.

2. **Strong empirical scope across four real-robot datasets.** The evaluation spans datasets with different action spaces (2 DoF to 7 DoF), varied resolutions (up to 288×512), and both short (16-frame) and long (150+ frame autoregressive) trajectory settings — demonstrating generalization beyond a single domain.

3. **Human preference evaluation confirms metric alignment.** Figure 4 reports pairwise human preference judgments showing Mani-WM is preferred in ≥60% of comparisons against every baseline on every dataset. The paper shows that this human ranking correlates with Latent L2 loss and PSNR, justifying the choice of primary metrics.

4. **Scaling behavior is demonstrated.** Figure 5 shows monotonic improvement in Latent L2 loss and PSNR as model size increases from 33M to 679M parameters across all three datasets, indicating the architecture can benefit from additional compute.

5. **Flexible action controllability with out-of-distribution inputs.** Figure 6 shows Mani-WM accurately following trajectories from a keyboard (Language-Table), VR controller (RT-1, Bridge), and a learned policy — sources with distributions different from the training data — and the generated frames are compared against real-robot rollouts. This goes beyond standard test-set evaluation.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline comparison fairness is not fully established (Tables 1–3).** VDM and LVDM, originally designed for text-to-video, are adapted by "encod[ing] the trajectory into an embedding" — the same approach used for text conditioning in the original papers. The paper does not report whether any hyperparameter search (learning rate, training steps, trajectory encoding design) was performed for these baselines. On the three primary datasets (RT-1, Bridge, Language-Table), VDM and LVDM are the only baselines for the trajectory-to-video task; iVideoGPT and MaskViT are compared only on RoboNet in a different prediction regime (2 context → 10 frames). While the results consistently favor Mani-WM, the lack of evidence that baselines were given a fair tuning budget weakens the claim that Mani-WM "outperforms all the comparing baseline methods."

2. **The real-robot planning experiment has an insufficient comparison baseline (Table 4).** The only comparison is against random trajectory selection. This does not rule out the possibility that even a simple open-loop policy or a non-planning method could achieve comparable or better results. The paper also does not specify how candidate trajectories are generated, the number of trials per task (no "trial" count is given in the paper), or report confidence intervals. The claim that Mani-WM "enables" model-based planning success is not adequately separated from the possibility that any reasonable cost function would outperform random selection. A comparison against a model-free policy or an ablation without Mani-WM's visual predictions would be needed to support the applied claim.

### Minor

1. **No variance or uncertainty reporting for any quantitative result.** Tables 1–3 and Figure 5 report only single-point estimates with no standard deviations, confidence intervals, or seed-averaged results. Generative models, especially diffusion models, exhibit run-to-run variability, and without error bars the reliability of small numerical margins (e.g., differences in the hundredths on Latent L2 loss) cannot be assessed.

2. **Human evaluation lacks procedural details.** The paper reports that "we perform a user study" and shows preference rates (Figure 4), but provides no information on the number of participants, number of pairwise comparisons per method and dataset, inter-annotator agreement, or whether participants had any specialized expertise. This limits the interpretability of the human evaluation results.

3. **Inference speed is mentioned only qualitatively.** The Limitations section states that "inference speed is not real-time" but provides no quantitative throughput numbers (e.g., seconds per frame or per sequence) to contextualize this limitation or allow comparison with future work.

### Trivial
- None.

## Nice-to-Haves

- **Initial frame conditioning ablation.** The paper does not evaluate the alternative of adding noise to the initial frame and predicting it jointly with the other frames. An ablation confirming the necessity of keeping the initial frame clean would strengthen the design justification.
- **VLP comparison or discussion.** VLP (Du et al., 2024) is cited in Related Work as a planning-oriented video world model but is never compared or discussed in the context of why it was excluded (e.g., it may require language prompts rather than action trajectories). A brief explanation would help readers situate the contribution.
- **Inference compute comparison.** A table comparing inference time between Mani-WM and the U-Net baselines (VDM, LVDM) would be useful for practitioners.

## Removed Points

These points were raised but removed after cross-checking against the paper:

- **"Ten trials per task" in planning experiment.** This number is never stated in the paper; the critic appears to have assumed it. The broader concern (insufficient statistical power) is retained in Major weakness #2.
- **"The strongest results are on datasets with no direct competitor for the precise task."** This is misleading: VDM and LVDM are compared on all three primary datasets. The concern about fair tuning is retained; the framing about "no competitor" is removed.
- **"VDM fails to generate realistic videos despite consuming more computation" is treated as a criticism.** This is the paper's own reported result, not a weakness.
- **Formatting nitpicks and missing appendix references.** These are parser artifacts, not author errors.
- **Generic "related work" gap claims.** The only specific related-work mention the reviewer could anchor (VLP) is moved to Nice-to-Haves.

## Novel Insights

The reviews do not produce genuinely novel observations beyond the paper's own contributions. The key tension they surface — that a technically well-architected method (Frame-Ada in a DiT) is coupled with an evaluation whose rigor does not match the strength of the claims — is essentially the paper's own gap between its reported experiments and its headline assertions. No review insight challenges the validity of the method itself or reveals an unanticipated application.

## Suggestions

1. **Tune baselines fairly and report the procedure.** For VDM and LVDM, perform (and report) a hyperparameter search for trajectory conditioning — at minimum over learning rate and training steps. If results are robust, this closes the primary concern. If not, consider replacing or augmenting these baselines with better-adapted methods (e.g., iVideoGPT adapted to all datasets, or VLP if feasible).

2. **Add variance reporting.** Report means and standard deviations over at least 3 seeds for all quantitative metrics in Tables 1–3 and Figure 5. State the number of trials for the planning experiment and report confidence intervals or bootstrap estimates.

3. **Strengthen the planning baseline.** Compare against at least one non-trivial alternative: (a) a simple open-loop policy that maps the goal image directly to actions, or (b) an ablation that removes the visual prediction component from Mani-WM (e.g., using only action information). This would separate the value of video prediction from the value of having any cost function at all.

4. **Report human evaluation details.** Include number of participants, number of comparisons per method, and agreement/consistency metrics.
