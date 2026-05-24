Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 bracket**: 5.0 – 7.5
**Round 2 narrowing**: Read anchors at 6.0 (CNS-Bench), 7.5 (Facing the Elephant), 5.25 (DiST). The paper is clearly stronger than CNS-Bench (6.0) and DiST (5.25) — broader benchmark, includes a method contribution, more thorough analysis. It is weaker than "Facing the Elephant" (7.5) — that paper had crisper experiments and tighter conclusions. This places the paper around **6.5**.

Now writing the review.

---

## Summary

This paper introduces LR0.FM, a comprehensive benchmark evaluating 10 vision-language foundation models (across 66 backbones) on zero-shot classification at low resolutions down to 16×16. It proposes the Weighted Aggregated Robustness (WAR) metric to fix issues with existing γ/SAR metrics, and LR-TK0 — lightweight trainable tokens added at every frozen transformer block that recover degraded features at low resolution via self-supervised distillation on synthetic diffusion-generated images. The benchmark analysis yields several insights (larger models help, early layers degrade most, dataset quality matters more than quantity), and LR-TK0 shows consistent improvements (~3% parameters, 4–10 WAR-16 gains) across EVA, MetaCLIP, and OpenCLIP families.

## Strengths

- **Comprehensive low-resolution benchmark.** The paper evaluates 10 models across 66 backbones and 15 datasets (Table 1), significantly expanding on prior work that typically covered 4–11 backbones. Figure 1 provides the first systematic view of zero-shot accuracy degradation across resolution levels for this breadth of models.

- **Novel WAR metric with measurable improvements.** WAR addresses two real flaws in existing γ and SAR metrics — inflated robustness near random chance and dataset imbalance in averaging. The improved Γᵈₙ formulation (Equation 1) zeros out scores near random baselines, and the weighted aggregation raises Spearman correlation for EuroSAT from 0.26 to 0.49 and ImageNet-A from 0.56 to 0.68 (Figure 5 left).

- **Effective and lightweight method (LR-TK0).** Adding ~3% parameters as learnable tokens at every block consistently improves SAR and WAR at 16×16 and 32×32 across three distinct model families (EVA, MetaCLIP, OpenCLIP) while maintaining performance at native resolutions (Table 2). The multi-scale training on synthetic diffusion images with random captions avoids exposure to target datasets, and the ablation study (Tables 5–6, Figures 13–15) validates key design choices: freezing is critical, multi-scale buckets help, and earlier token insertion yields larger gains.

- **Layer-wise degradation insight directly motivates method design.** The analysis in Figure 7 (right) shows that initial layers are more disrupted at low resolution than deeper layers. This finding is validated by the token-position ablation (Figure 15) and directly informed the design of adding LR tokens at every block rather than only later layers — a clean example of analysis driving design.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparisons to parameter-efficient fine-tuning methods.** The method is compared against SR methods (Table 3) and against fine-tuning the last four blocks (Table 5). Neither is an adequate baseline for the claim that LR tokens provide a *special* advantage beyond being a generic learnable addition to a frozen model. The paper should include comparisons to lightweight PEFT methods (e.g., LoRA, adapters, prefix tuning) of similar parameter count, trained on the same synthetic data or a small LR external dataset. Without these baselines, the reader cannot tell whether the gains come from the specific token architecture or simply from adding any small set of trainable parameters to the frozen model. Table 4 mentions applying LR-TK0 to visual prompt tuning, but this is a different framing (applying LR-TK0 to VPT, not comparing against VPT as a baseline).

- **WAR metric construction has unresolved gaps.** (a) The dataset weights wᵈ₁₆ are optimized only at 16×16 and then applied to all other resolutions (32×32, 64×64, 128×128) without validation that these weights produce reasonable correlations at those resolutions — datasets that behave anomalously at 16×16 may not be the ones needing re-weighting at higher resolutions. (b) The choice of the 0.95 multiplier in Equation 2 and the specific subset of datasets in the objective is described as "empirically found" with details deferred to the (stripped) appendix, making the construction appear ad hoc as presented. (c) Hyperparameter α=200 is stated as a "middle" value but no sensitivity analysis is shown for how much the final rankings change with different α values.

### Minor

- **Some analytic conclusions are drawn from confounded comparisons.** The claim that "pre-training dataset quality is more important than its size" rests primarily on the DataComp-1B vs. LAION-2B comparison (Figure 6 left), but other models with larger datasets (SigLIP‑10B, M²‑Encoder‑6B) also differ in architecture, training recipe, and text encoder — dataset size is not the controlled variable. Similarly, the fine-tuning claim (Figure 6 right) compares ALBEF/BLIP variants that are architecturally different from CLIP-style models. The paper's hedging language ("suggests") partially mitigates this, but the conclusions are presented with more certainty than the evidence strictly supports.

- **Inference cost not reported.** LR tokens increase parameter count by ~3% but are processed through every transformer block, so both FLOPs and latency scale with (original sequence length + #LR tokens) × #blocks. This cost should be quantified — currently the paper reports only parameter counts, not compute overhead.

- **Training hyperparameters partially reported.** Learning rate, batch size, optimizer, and GPU hours are missing for the LR-TK0 training. The 200 epochs for EVA vs. 10 epochs for MetaCLIP/OpenCLIP is noted but unexplained, which could affect reproducibility.

- **No statistical significance or error bars.** Key results (e.g., Table 2 at 16×16) are reported from single runs. Given the relatively small synthetic dataset (7K captions), variance across training runs could be non-negligible.

### Trivial

- The observation that "higher GFLOPs weakly impacts robustness" (Figure 5 right) is supported only by visual dot-size comparison; a formal correlation statistic or regression line would be more appropriate.
- The number of LR tokens per block is fixed at (#spatial tokens × (N+1)) and never ablated. Sensitivity to this hyperparameter would help understand the method's robustness.

## Nice-to-Haves

- A quantitative analysis of feature similarity (e.g., CKA) between LR and HR feature maps with and without LR tokens would directly test whether the tokens close the representational gap shown in Figure 7 (right).
- Validating that the WAR weights derived at 16×16 produce reasonable rankings at 32×32 and 64×64, or providing resolution-specific weights, would strengthen the metric's credibility.
- Comparing to a simple baseline that bicubic-upsamples the LR image and passes it through the frozen model (without SR) would clarify whether the Baseline row in Table 3 differs from Table 2 due to SR-specific preprocessing.

## Removed Points

These points were raised by the reviewers but are removed after cross-checking against the paper:

- **Data contamination risk from synthetic images** (Harsh Critic): Speculative. The paper uses PIXART-α to generate images from *random* Conceptual Captions captions — the teacher model has never seen these specific generated images. The paper explicitly argues against direct overlap. Removed as unsubstantiated speculation.
- **Eᴅ formulation fails when A_HR < A_rand** (Harsh Critic): The paper explicitly defines Eᴅ ∈ [0, 1] (Equation 1), scoping out this edge case. For the well-trained models under study, A_HR consistently exceeds random. Removed as a non-issue for this paper's scope.
- **Baseline discrepancy between Table 2 and Table 3** (Harsh Critic): The paper clearly states Table 3 uses "SR-specific pre-processing." The discrepancy is thus explained. Removed.
- **Missing related works** (general): Per policy, related work complaints are not included as the reviewer does not have access to external sources.
- **Formatting, typos, grammar nitpicks** (general): Excluded per policy as parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The key novel observation — that initial transformer layers are more disrupted than deeper layers under low resolution, directly motivating block-level token insertion — is articulated in the paper itself and validated through ablation.

## Suggestions

1. **Add PEFT baselines.** Compare LR-TK0 against LoRA (of comparable rank), adapter modules, or VPT-deep with similar parameter counts trained on the same synthetic data. This is the single most impactful addition — it would either validate that LR-TK0's architecture provides a specific advantage or show that generic PEFT methods suffice, either of which is informative.
2. **Validate WAR weights across resolutions.** Show that wᵈ₁₆ yields reasonable correlations at 32×32 and 64×64, or provide resolution-specific weight tables.
3. **Report inference cost.** Add a column reporting FLOPs and wall-clock time for the forward pass with and without LR tokens.
4. **Add a formal correlation statistic for the GFLOPs claim** in Figure 5.
5. **Report training hyperparameters and include error bars** (at least on the main Table 2 results).

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak (< 3.5): 7LZjuA4AB2 (3.00), gNoqEdT2wO (2.33), ZaudLwn0Hm (2.50), JEmNgjuQHU (2.00) — all substantially weaker than the paper under review.
- Middle (3.5–7.5): hLIlN0f4ix (5.00, ShareLock), ZuYvrjh2od (5.00), UHHOAe1uIS (5.25, TUBench), 1CeIRl147S (4.33) — the paper is clearly stronger than these.
- Strong (> 7.5): 2dnO3LLiJ1 (8.00, Registers), gzqrANCF4g (8.00) — the paper is substantially weaker than these.

**Round 2 (Narrowing):**
- 1STZCCI8mn (6.00, CNS-Bench) — similar benchmarking paper. The paper under review is stronger: more comprehensive benchmark (10 models vs. a few) plus a method contribution.
- bJx4iOIOxn (7.50, Facing the Elephant) — strong empirical analysis paper. The paper under review is weaker: the Elephant paper had cleaner experiments and tighter conclusions.
- Yr4RgiZ7P5 (5.25, DiST) — benchmark + method paper, but narrower scope. The paper under review is clearly stronger.
- yAcLwJu9qs (5.50, VCR) — robustness benchmark paper. The paper under review is stronger.

**Final position**: The paper sits between the 6.0 (CNS-Bench) anchor and the 7.5 (Facing the Elephant) anchor, closer to the lower end due to the significant missing-baselines gap and the WAR metric's unresolved construction issues. The paper is definitively stronger than CNS-Bench, TUBench, DiST, and ShareLock. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>