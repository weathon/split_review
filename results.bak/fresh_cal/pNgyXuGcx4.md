Now I have a clear picture of the paper and all the claims. Let me compose the final consolidated review.

---

## Summary

This paper investigates whether FP8 training of LLMs is robust enough to be cost-effective compared to mixed-precision BF16. It reports a surprising finding—even standard BF16 training has ~10% loss-divergence rate on nanoGPT at only 5% of training—and proposes a loss landscape sharpness metric adapted for autoregressive LLMs (operating on the last-token logit). Through MS-AMP O1 experiments on GPT-2 and bit-simulation experiments (clamping mantissa bits of BF16) on Llama models up to 7B, the paper argues that reduced-precision training narrows the stable hyperparameter space and that current FP8 methods are not yet robust enough to be cost-effective.

## Strengths

- **Surprising empirical finding about BF16 training instability.** Figure 1 and Section 1 show that 18 out of 188 BF16 nanoGPT runs (≈10%) diverge at only 5% of training under identical hyperparameters, while 70 TF32 runs show zero divergence. This is a concrete, reproducible result that challenges the community's implicit trust in BF16 as a stable default. The paper is right to foreground this.

- **New loss landscape sharpness metric adapted for autoregressive LLMs.** Section 3.1 defines a sharpness measure (Equation 2) operating on the last-token logit rather than input embeddings, solving the computational bottleneck of prior methods (Keskar et al., 2017) for decoder-only Transformers. The metric requires only one forward pass per measurement and is clearly specified, making it easy to adopt.

- **Precise ablation identifying the numerical bottleneck from exponent reduction.** Section 4.2 shows that E7M7 (one exponent bit removed) prevents training entirely, and the inner/outer-range ablation isolates the cause to the inability to represent large values rather than a loss of precision. This is a more specific diagnosis than simply noting that fewer exponent bits hurt.

- **Learning-rate robustness test reveals latent instability.** Figure 9 compares E8M5 vs BF16 at default and 10× learning rates using 18 seeds per condition. E8M5 shows notably more frequent loss spikes at the higher LR even though no run diverges, demonstrating that mantissa reduction narrows the stable hyperparameter region *before* overt failure.

## Weaknesses

### Fatal
None.

### Major

1. **Claims about "FP8 training" outpace the evidence, which only covers MS-AMP O1.** The abstract states that "currently available methods for FP8 training are not robust enough," and the Discussion refers to "existing mechanisms to stabilize FP8 training." However, the experiments only use MS-AMP at its O1 optimization level (Section 2.4: "we use only the most basic optimization scheme"). Higher levels (O2, O3) and other FP8 frameworks (e.g., TransformerEngine) are described in the paper but never tested. The paper's reasoning—that testing the "least invasive" level is conservative—is valid for what it shows, but the broad language about "FP8 training" in the abstract and conclusion extends well beyond the single-library, single-level evidence. This undermines the paper's strongest-pitch claim.

2. **The sharpness metric is claimed to "predict" divergence but is only shown to correlate with it.** The paper's contribution list (Section 1) says the metric "can predict when training divergence will occur." The evidence is: (a) qualitative plots (Figures 7, 8) where sharpness rises before a few selected divergences; (b) Table 1 showing E8M5 sharpness increasing at 5K steps before loss divergence is visible. There is no precision/recall analysis, no comparison against baselines (gradient norm, loss variance), no held-out set of runs to test predictive utility, and no demonstration of a usable threshold. The paper itself acknowledges "no exact sharpness threshold exists" (Figure 7 caption) and "the exact threshold may differ depending on the configurations" (Section 4.3). The gap between the claimed capability and the presented evidence is significant.

### Minor

1. **The bit-simulation experiments study mantissa reduction under an 8-bit exponent, which differs substantially from real FP8.** The paper clamps mantissa bits of BF16 (E8M3, E8M4, E8M5), keeping the 8-bit exponent of BF16. Real FP8 uses E5M2/E4M3 formats with 4–5 exponent bits, narrower exponent range, hardware-specific scaling, and different accumulation behavior. The paper acknowledges that removing *exponent* bits (E7M7) prevents training, yet the entire program of "bit reduction" thereafter studies mantissa reduction—a different axis from what FP8 constrains. The experiments are valid as a scientific study of mantissa-precision effects, but their connection to the paper's practical claims about FP8 viability is indirect and needs to be argued more carefully.

2. **Computational cost of the sharpness metric is not reported.** Section 3.1 states that the forward pass "need only be performed once for each measurement," but the L-BFGS-B optimization on a ~32,000-dimensional space (vocabulary size) requires many iterations of the loss function (cross-entropy from logits). No runtime or FLOP comparison to baselines is provided, making it hard to assess whether the metric is practical for online monitoring during training.

3. **The mantissa clamping mechanism is underspecified.** The paper describes clamping bits but does not state whether values are rounded or truncated, or how denormals are handled. This is a reproducibility gap.

### Trivial

None.

## Nice-to-Haves

- **Compare against FP16 training as an intermediate baseline.** The paper motivates the study with FP16's known instability but never runs FP16 experiments. Including FP16 would contextualize whether FP8's instability is merely "worse than FP16" (incremental) or qualitatively different.
- **Investigate whether gradient scaling or loss scaling (standard FP16 stabilization techniques) could reduce FP8 instability.** The paper mentions gradient scaling for FP16 in the introduction but does not discuss its applicability to FP8.
- **Test whether the sharpness metric could be applied during training for early stopping**, which is the natural use case implied by "predicting divergence."
- **Follow up on the E8M5 7B model from Table 1** to see whether its rising sharpness actually leads to divergence later. The paper acknowledges the computational cost of longer runs but the claim about the metric's predictive power would be stronger with this follow-up.

## Removed Points

The following points from the inputs are excluded from the main review, with brief justifications:

- **"The cost argument is speculative and not tied to measured failure rates"** (Harsh Critic #4): The $100K figure is presented as a "rough approximation" (Section 1) to motivate the problem, not as a core empirical claim. It is an illustrative cost estimate, common in motivation sections, and does not threaten the paper's validity.
- **"Section 3.2 (MASKING) is essentially empty"**: The parser likely stripped this content; masking techniques are referenced later (Section 5 mentions "removing masking from the LM head"). Per the rules, parser-stripped content should not be critiqued.
- **"No comparison with FP16 training"**: This asks the paper to address a topic outside its stated scope (FP8 vs BF16). The paper mentions FP16 for motivation, not as a required baseline.
- **"No discussion of gradient scaling or loss scaling"**: The paper's scope is evaluating current methods, not proposing new stabilization techniques for FP8.
- **"The paper does not try higher optimization levels (O2, O3)" framed as the central/only issue**: This concern is captured in Weakness #1 (Major), where it is appropriately contextualized. The separate framing is redundant.
- **From Strength Finder: generic/deeply overstated strength about sharpness predicting divergence "across model sizes and mantissa widths"**: The qualitative evidence is real but does not demonstrate prediction. This is better captured as a qualified observation in the strengths list.
- **"the paper does not try... other FP8 frameworks (e.g., TransformerEngine)"**: This is part of the same issue captured in Weakness #1.

## Novel Insights

None beyond the paper's own contributions. The interaction of the two reviewer perspectives does surface one synthetic observation that neither captures individually: the paper's strongest contribution (the BF16 10% divergence finding) and its weakest argument (the broad FP8 cost-effectiveness claim) are in tension with each other. If even BF16—the community's standard—has a non-trivial failure rate, then the proper question is not "are FP8 methods robust enough?" but rather "how much *additional* failure risk does FP8 introduce?" The paper gestures at this framing in Section 1 but never quantifies the differential, leaving it unclear whether the gap between FP8 and BF16 is large enough to matter given BF16's own baseline failure rate. Reframing the evaluation around *differential* risk (FP8 failure rate − BF16 failure rate) would sharpen the paper's empirical contribution.

## Suggestions

- **Tighten the scope of the central claim.** Replace "currently available methods for FP8 training are not robust enough" with the more precise "MS-AMP O1 FP8 training on GPT-2 shows a persistent loss gap relative to BF16, suggesting cost-effectiveness requires scrutiny." The paper's concrete evidence supports the latter; the former invites justified skepticism.
- **Validate the sharpness metric as a predictor, not just a correlator.** Hold out a set of random seeds, compute sharpness at a fixed checkpoint, and test whether runs with above-threshold sharpness diverge more frequently. Report AUC or a simple confusion matrix. A single quantitative figure would transform the metric from an interesting observation into a practical tool.
- **Quantify the gap in Figure 6 numerically.** Report the final loss difference between MS-AMP O1 and BF16 (with and without LM-head exclusion) at 120K steps, ideally with variance across seeds. A small gap (e.g., 0.05 loss) has very different implications from a large gap.
- **Add a controlled failure-rate comparison.** Even for a small model (120M), run 20+ seeds for BF16 and 20+ for MS-AMP O1 under identical hyperparameters and report the fraction that diverge. This directly tests the robustness claim the paper cares about.
- **Acknowledge the "differential risk" framing.** Since BF16 itself has a ~10% divergence rate (at 5% of training), the practical question is whether FP8 adds material risk beyond this baseline. The paper would benefit from making this comparison explicit.

## Score and Decision

**Score:** 3.0

**Decision:** Accept

**Rationale:** The paper identifies a genuinely important and under-studied problem. The BF16 divergence finding (10% at 5% of training) is surprising and practically significant. The sharpness metric, while not yet rigorously validated as a predictor, is a principled adaptation of prior work to autoregressive LLMs and enables the paper's diagnostic analysis. The bit-reduction experiments and learning-rate robustness tests add convergent evidence. However, the paper overclaims—its broad language about "FP8 training not being robust enough" exceeds the evidence (MS-AMP O1 only), and the sharpness metric is presented as a "predictor" but only demonstrated as a correlator. These are addressable weaknesses; the core contributions are real.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Accept</decision>