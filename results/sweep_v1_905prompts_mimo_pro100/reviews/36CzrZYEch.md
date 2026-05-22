Good. Now I have all the information needed. Let me compose the final review.

## Summary

This paper introduces IRIS (Intrinsic Reward Image Synthesis), which uses negative self-certainty (NSC)—the negative KL divergence between a uniform distribution and the model's token distribution—as an intrinsic reward for RL-based alignment of autoregressive text-to-image models. The central empirical observation is that maximizing self-certainty improves language reasoning but degrades image quality, while minimizing it produces richer images. IRIS is applied to Janus-Pro models and compared against T2I-R1 (which uses external reward models) on three benchmarks.

## Strengths

- **Novel counter-intuitive finding with quantitative support.** Figure 2 provides direct evidence that RL alignment with external rewards *decreases* self-certainty on image tokens (orange line descending from ~20.2 to ~19.0) while *increasing* it on text tokens in math reasoning (blue line ascending from ~31.5 to ~36.5). This establishes the core claim that self-certainty exhibits modality-dependent behavior, which is a genuinely surprising and well-documented empirical observation that contrasts with prior work on self-certainty in LLMs.

- **Comprehensive ablation study isolating each design choice.** Figures 5–9 systematically validate four independent design decisions—with vs. without semantic CoTs, minimize vs. maximize image self-certainty, minimize vs. maximize text self-certainty, forward vs. backward KL, and RL vs. direct optimization. Each ablation is evaluated consistently, and the results coherently support the proposed NSC formulation. The finding that direct NSC optimization (without RL) causes model collapse (Fig. 9) is particularly important and well-demonstrated.

- **Competitive performance on 1B model without any external supervision.** On Janus-Pro-1B, IRIS achieves 0.72 on GenEval vs. T2I-R1's 0.75, 0.3793 on T2I-CompBench vs. 0.3820, and 0.37 on WISE vs. 0.38—all using zero human labels or domain-specific verifiers (Table 1a–c). These small gaps are notable given that T2I-R1 uses four specialized reward models (HPSv2, DINO, GIT, ORM).

- **Fine-grained category analysis revealing complementary strengths.** The paper shows IRIS outperforms T2I-R1 on biology, physics, and chemistry categories in WISE, while T2I-R1 excels on counting, color attribution, and spatio-temporal tasks. The explanation—that T2I-R1's external rewards encode human aesthetics and spatial relations but lack natural science knowledge—is well-supported by Table 1c and demonstrates genuine understanding of why intrinsic rewards can be preferable for general capability.

- **Careful experimental practice.** The identification and correction of the chat template inconsistency in T2I-R1's implementation (Sec. 4.1) shows careful experimental rigor and improves reproducibility.

## Weaknesses

### Fatal
None.

### Major

- **Consistent underperformance on 7B model undermines the headline claim.** On Janus-Pro-7B, IRIS underperforms T2I-R1 on every benchmark: GenEval 0.77 vs. 0.78, WISE 0.48 vs. 0.50, and CompBench 0.3916 vs. 0.3992 with consistent deficits across sub-scores (Table 1a–c). The abstract's claim of "competitive with or superior to external rewards" is accurate for 1B but misleading for the 7B setting, which is the more practically relevant scale. The paper attributes the gap to "the stronger capability of larger base models" (line 128), but this explanation is offered without further analysis—it essentially concedes that the approach's advantage diminishes where practitioners care most. The 7B training dynamics are also not shown (only 1B curves appear in Fig. 3), making it impossible to assess whether IRIS peaks early, converges to a lower point, or exhibits other failure behaviors at scale.

- **Unexplained mechanism connecting NSC to image quality.** Minimizing KL(U || π) pushes the model's output distribution toward uniform over the vocabulary—which by itself would produce noise, not quality images. The paper does not analyze what prevents mode collapse into noise beyond GRPO's relative advantage estimation, which is what actually selects among high-uncertainty outputs for quality. This means GRPO's ranking mechanism is the actual quality signal, with NSC serving as a diversity promoter, but the paper does not acknowledge or analyze this separation of roles. No quantitative analysis of the trained model's output distribution (e.g., entropy, spread, codebook utilization) is provided to validate the claimed mechanism.

### Minor

- **Single model family limits generalizability claims.** IRIS is demonstrated only on Janus-Pro (1B and 7B). The paper's discussion section acknowledges that T2I architectures are diverse (diffusion models, masked modeling, MAE-style) and that applying IRIS to them is future work (Sec. 4.4). The claim that IRIS is "agnostic to the model architecture" (line 48) is aspirational, not demonstrated.

- **Best-checkpoint selection introduces selection bias.** Table 1 reports "the best result of different methods among the checkpoints from 100 step to 800 step" (line 148). From Fig. 3, IRIS appears to peak earlier than T2I-R1 on some curves, meaning best-checkpoint selection may favor IRIS's early advantage while obscuring convergence behavior. Reporting mean±std across checkpoints or the final checkpoint alongside the best would strengthen the results.

- **Ablations use the competing paradigm's reward models as evaluation metrics.** The ablation studies (Sec. 4.3) evaluate IRIS variants using HPSv2, DINO, GIT, and ORM—the same four models used to train T2I-R1. While the paper correctly notes these are not used in IRIS's training objective, they are not neutral metrics: they define quality for the competing paradigm. Using these to optimize IRIS's design choices (forward vs. backward KL, with vs. without CoT, etc.) steers IRIS toward the external-reward paradigm rather than independently validating the intrinsic-reward approach.

- **No quantitative diversity analysis or human evaluation.** The paper claims NSC produces "richer" images but provides no diversity metrics (e.g., LPIPS between samples from the same prompt, FID). All evaluation is through automatic benchmarks. Given that the motivation centers on the subjectivity of image quality, even a small-scale human evaluation would substantially strengthen the central claim.

### Trivial

None.

## Nice-to-Haves

- Analyze what NSC actually changes in the output distribution of trained models (entropy, codebook utilization statistics) compared to the base model and T2I-R1, to validate the mechanism claim.
- Report 7B training curves to understand why the approach underperforms at scale.
- Provide failure case analysis showing where IRIS degrades relative to the base model or T2I-R1.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"T2I-R1 numbers are authors' re-runs, not published numbers"** — The paper explicitly identifies and justifies the recalculation due to a chat template bug. This is careful experimental practice, not a weakness.
- **"Section 4.4 is too brief"** — While a longer discussion would be welcome, this is a presentation preference, not a substantive flaw.
- **"Emergence of CoTs is unexplained"** — The paper does observe this and connects it to the NSC text-token objective. The harsh critic's concern about confounding is speculative.
- **"Circular evaluation in ablations"** — Already addressed above as a minor weakness; the paper explicitly acknowledges these metrics are not used in IRIS training.
- **"Uniform distribution is assumed without discussion of alternatives"** — This is consistent with prior work (Zhao et al., 2025b) and the ablation validates forward KL over backward KL.

## Novel Insights

The paper's genuinely novel observation is that self-certainty has opposing effects across modalities: maximizing it helps language reasoning but hurts image generation, while minimizing it improves T2I quality. This contrasts sharply with prior work (Zhao et al., 2025b; Zhang et al., 2025a) that uniformly recommends maximizing self-certainty. The fine-grained category analysis in Table 1c is also insightful, showing that intrinsic rewards excel on knowledge-intensive categories where external reward models lack domain coverage, while external rewards retain advantages on aesthetics and spatial reasoning—suggesting that intrinsic and external rewards capture complementary aspects of image quality.

## Suggestions

- Add an explicit analysis of what prevents NSC optimization from producing pure noise: analyze the output distribution statistics of IRIS-trained models (codebook usage, per-token entropy) compared to base and T2I-R1 models.
- Provide 7B training dynamics curves and investigate why the approach's advantage diminishes at scale—e.g., is it because larger models already have sufficient output diversity?
- Add a small human evaluation study to validate the claim that NSC-generated images are "better aligned with human preferences."
- Reframe the contribution more honestly: the 1B results are genuinely competitive, but the 7B results are not, and the paper should acknowledge this asymmetry more prominently rather than burying it in a parenthetical.

## Score Calibration

**Round 1 bracketing anchors:**
- Weak band (avg < 3.5): "Data Extrapolation for T2I" (3.4), "Knowledge Enhanced Image Captioning" (3.0), "Innate-Values-driven RL" (2.5)
- Middle band (3.5–7.5): "Mitigating Object Hallucination" (5.0), "Scaling Autoregressive T2I" (5.75), "Adding Conditional Control with RL" (6.5), "TTA with CLIP Reward" (6.67), "IterComp" (6.8), "CCA for Guidance-Free" (7.0)
- Strong band (> 7.5): "Transfusion" (7.6), "Interpreting CLIP" (8.0), "SANA" (8.5)

**Initial bracket: 5.5–7.0.** The paper is clearly above the weak reject papers and below the strong accept papers.

**Round 2 narrowing anchors:**
- "Mitigating Object Hallucination" (5.0): Uses RL without human feedback but single-model, single-task, weaker ablations. IRIS is clearly better.
- "Adding Conditional Control with RL" (6.5): Novel RL approach, limited experiments, single model family. IRIS is comparable in quality.
- "CCA for Guidance-Free" (7.0): Theoretically grounded, tested on multiple AR models, solves a fundamental problem. IRIS is somewhat less rigorous in its mechanism explanation and has weaker 7B results.

**Final score: 6.0.** The paper offers a genuinely novel and well-documented empirical finding (modality-dependent self-certainty behavior), comprehensive ablation studies, and competitive 1B results without any external supervision. However, the consistent 7B underperformance, unexplained mechanism, single-model evaluation, and overstated claims hold it back from a higher score. It sits above the 5.0 reject (which had weaker experiments and less novelty) but below the 6.5–7.0 accepts (which had cleaner theoretical grounding or broader evaluation).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>