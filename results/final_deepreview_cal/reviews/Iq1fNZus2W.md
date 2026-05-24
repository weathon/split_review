## Summary

This paper introduces Patch-wise and Keyword-Aware Attention (PKA), a mechanism that replaces the expensive full-attention "concatenate-and-attend" paradigm in multi-condition Diffusion Transformers with two lightweight modules: Position-Aligned Attention (PAA) for spatial conditions and Keyword-Scoped Attention (KSA) for subject conditions. The attention decomposition is motivated by a principled analysis showing that attention in multi-condition DiTs is highly redundant — diagonal-concentrated for spatial layouts and keyword-localized for subject conditions. Complemented by a condition KV-cache and an early-timestep sampling strategy, PKA achieves up to 10× inference speedup and 5.12× reduction in attention VRAM while claiming maintained or improved generative quality compared to OminiControl2 and UniCombine.

## Strengths

- **Principled attention-redundancy analysis motivates the design**: Figures 2 and 3 convincingly show that spatial-condition attention concentrates along the diagonal and subject-driven attention localizes around keyword-relevant regions. This directly motivates PAA's one-to-one alignment and KSA's mask-scoped attention, making the architectural choices well-grounded rather than arbitrary.

- **Substantial and well-demonstrated efficiency gains**: Figures 7 and 8 provide clear, quantitative evidence — up to 10× inference speedup and 5.12× attention VRAM reduction versus full attention, with graceful scaling across 1–16 conditions. The efficiency results are the strongest empirical contribution and are presented transparently.

- **Thorough and informative ablation studies**: Figure 9 shows PAA outperforms sliding-window alternatives in both latency (13.63s vs. 14.00s best SWA) and VRAM (237MB vs. 276MB). Figure 10 demonstrates KSA's robust, tunable efficiency–fidelity trade-off across ε thresholds, with the quality degrading gracefully even at aggressive settings. The condition KV-cache design (Figure 4a) is a clever additional efficiency contribution.

- **Well-scoped related work and clear positioning**: The paper correctly situates itself against both UNet-based control methods (ControlNet, IP-Adapter) and DiT-based multi-condition frameworks (OminiControl, UniCombine, PixelPonder), and clearly articulates the distinction between its approach (structural priors to eliminate redundancy) and existing efficiency methods (token pruning, layer caching).

## Weaknesses

### Major

- **Ambiguous baseline training protocol undermines quality comparison**: The paper states "To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA…" (line 290–291), but never specifies whether OminiControl2 and UniCombine were also fine-tuned on the same curated Subject200K subset with equivalent LoRA configuration, iteration budget, and optimizer. If the baselines were evaluated using publicly released weights without dataset-specific adaptation, the reported quality differences in Table 1 could partly reflect domain mismatch rather than methodological superiority. This ambiguity affects the credibility of the core claim that PKA "maintains or improves generative quality" over state-of-the-art baselines and must be resolved for the quality comparison to be trusted.

### Minor

- **Early-timestep sampling contribution lacks quantitative validation**: Figure 11 provides only a single qualitative sequence (one condition image, three μ/δ settings, five iteration snapshots). There are no FID/SSIM curves across different μ,δ configurations, no statistical evaluation over the test set, and no numerical comparison to standard sampling. As a result, the claimed benefits of faster convergence and improved control fidelity remain anecdotal. This is notable because the early-timestep strategy is listed as a core contribution, yet its evidentiary support is the weakest part of the paper.

- **Perturbation experiment methodology is insufficiently described**: Figure 5 shows that perturbing visual conditions in early (high‑t) steps degrades SSIM more than late perturbations, justifying the early-timestep focus. However, the paper does not specify what the perturbation actually is (e.g., zeroing condition tokens, adding noise to features, removing attention paths), nor how SSIM is computed in this context (against what reference). The reader cannot fully assess the validity of the conclusion without these details.

- **No discussion of limitations or failure cases**: The paper lacks any explicit limitations section. Key assumptions — that PAA requires the spatial condition to be tokenized at the same grid resolution as the noisy image, and that KSA depends on a well-defined subject keyword in the prompt — are not acknowledged. The method's behavior when no distinct keyword exists (e.g., abstract prompts, multiple subjects) is unexplored. This makes the method's scope less transparent than it should be.

### Trivial

- The qualitative comparison in Section 4.2.2 describes UniCombine's outputs as having a "muted or desaturated color palette" — this observation, while potentially valid, is not supported by any quantitative color-distribution metric and reads as subjective.

## Nice-to-Haves

- Including PixelPonder (cited in related work, line 73) as an additional efficiency baseline in Figures 7–8 would broaden the context for the claimed speedup.
- Adding quantitative learning curves (FID vs. iterations for different μ,δ) for the early-timestep sampling would substantially strengthen that contribution.
- A brief acknowledgment of when KSA's keyword assumption holds and when it may not (e.g., prompts with implicit subjects) would make the method's scope more honest.

## Removed Points

*These points were flagged by reviewers but are not retained as valid weaknesses:*

- **"Reported FID values are surprisingly high (52.99)"** — REMOVED. This reflects the dataset and task difficulty; all methods are evaluated identically, so relative comparisons remain valid. The absolute FID level is not a weakness.
- **"Missing baselines like PixelPonder" as a major flaw** — MOVED TO NICE-TO-HAVE. The paper already cites PixelPonder in related work and compares against the two most relevant DiT multi-condition frameworks (OminiControl2, UniCombine). Adding PixelPonder would strengthen but is not essential.
- **"Comparison fairness is a fatal structural flaw"** — DEMOTED to Major. The paper states "To ensure a fair comparison" which suggests intent to apply equal treatment; the weakness is ambiguity in description, not proven unfairness. This is addressable in rebuttal.
- **"The perturbation experiment is completely invalid"** — REMOVED as framed. The description is vague, which is a real issue (retained as Minor), but Figure 5's conclusion (early steps matter more) is independently plausible and the methodology can be clarified rather than discarded.
- **Strength Finder claim that early-timestep sampling is a core validated strength** — DOWNGRADED. Figure 11 is qualitative only and cannot support strong quantitative claims about convergence acceleration.
- **Generic formatting/style nitpicks** — REMOVED. These reflect parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The attention-redundancy analysis (Figures 2–3) is the most genuinely novel observation — decomposing multi-condition DiT attention into two distinct sparsity patterns (spatial-aligned diagonal and subject-driven keyword-localized) and designing specialized modules for each is a clean conceptual contribution that the paper executes well.

## Suggestions

- Explicitly state in the experimental setup whether OminiControl2 and UniCombine were fine-tuned on the same Subject200K subset with equivalent LoRA configuration and compute budget. If they were, add the training details; if not, add the fine-tuned comparison or clearly scope the quality claims.
- Add a quantitative ablation for the early-timestep sampling strategy: report test-set FID/SSIM for at least three (μ,δ) configurations versus standard Logit-N(0,1) sampling, ideally as learning curves over training iterations.
- Include a brief Limitations subsection (even 3–4 sentences) addressing the keyword-dependence of KSA and the spatial-alignment assumption of PAA.
- Clarify in the Figure 5 caption or accompanying text exactly what operation constitutes a "perturbation" and how SSIM is computed.

## Score and Decision

**Round 1 bracket**: Initial anchors placed the paper between 5.0 and 7.5 — above DyDiT (5.50) and ViCo (5.50), below SANA (8.50) and UniCon (7.00).

**Round 2 narrowing**: Compared against PT-DiT/Qihoo-T2X (6.40) and LEGO (6.67), the paper has comparable motivation quality and stronger efficiency numbers, but the comparison-fairness ambiguity and weaker early-timestep evidence pull it slightly below. Compared against UniCon (7.00), PKA is less polished and has a more significant outstanding concern. The paper lands at **6.0**.

**Anchor references across all rounds**:
| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| Jt1gGIumJo | 3.00 | R1 | PKA substantially stronger — principled analysis, real efficiency gains, proper baselines |
| vK8C37eHXM | 3.20 | R1 | Not comparable (diffusion+autoencoder, different problem) |
| rnTb9dm9zx | 3.00 | R1 | PKA stronger — better motivated, cleaner method |
| IqGVIU4rvM | 2.50 | R1 | Not comparable (tokenizer design for LLMs) |
| r2uhY4pXrb (ViCo) | 5.50 | R1 | PKA stronger — more novel decomposition, larger efficiency gains |
| taHwqSrbrb (DyDiT) | 5.50 | R1 | PKA stronger — better motivation, more dramatic efficiency results (10× vs 1.73×) |
| qmXedvwrT1 (LEGO) | 6.67 | R1,R2 | Comparable motivation quality; PKA slightly below due to comparison-fairness concern |
| iG7qH9Kdao | 5.00 | R1 | PKA stronger — more focused contribution, cleaner experiments |
| N8Oj1XhtYZ (SANA) | 8.50 | R1 | PKA clearly below — less polished, narrower scope, weaker evidence on some claims |
| gU58d5QeGv | 8.00 | R1 | PKA below — less comprehensive, smaller-scale |
| DJSZGGZYVi | 9.00 | R1 | Not directly comparable (training regularization for representations) |
| SI2hI0frk6 | 7.60 | R1 | PKA below — narrower scope, weaker evidence |
| cbv0sBIZh9 | 5.75 | R2 | PKA comparable — similar-quality contribution to a different problem |
| lTrrnNdkOX (PT-DiT) | 6.40 | R2 | PKA slightly below — similar motivation quality but comparison-fairness concern pulls it down |
| XMJBrvRDI8 | 6.25 | R2 | PKA comparable — different problem, similar evidence quality |
| gKui6QvvfK | 5.25 | R2 | PKA stronger — better experiments, clearer contribution |
| uJqKf24HGN (UniCon) | 7.00 | R2 | PKA below — less polished, outstanding comparison concern |
| 2o58Mbqkd2 | 7.33 | R2 | PKA below — less theoretically grounded |
| q5sOv4xQe4 (HART) | 6.80 | R2 | Not directly comparable (autoregressive, hybrid tokenizer) |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>