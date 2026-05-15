Here is my consolidated final review.

---

## Summary

This paper proposes DyNet, a family of all-in-one image restoration networks built on a weight-sharing mechanism that reuses a single transformer block's weights across multiple sequential blocks at each encoder-decoder level. By varying the reuse frequency, the same checkpoint yields both a large variant (DyNet-L) and a lightweight variant (DyNet-S) that can be switched at deployment time without reloading weights. The authors introduce a dynamic pre-training strategy that trains both variants concurrently in a single session (claimed 50% GPU-hour savings), and curate Million-IRD, a 2M-image pre-training dataset filtered from LAION-HR. The combined system achieves 32.74 dB average PSNR in the all-in-one setting (0.68 dB above PromptIR) while using 57% fewer parameters.

## Strengths

1. **Weight-sharing enables flexible deployment from a single checkpoint.** The core idea — reusing transformer block weights at each encoder-decoder level with configurable reuse frequency — is clean and practical. Differing only in depth, DyNet-L and DyNet-S share the same underlying weights, so a user can switch between them at inference time without separate checkpoints. This is not supported by prior all-in-one methods (e.g., PromptIR, AirNet) and has genuine practical value for resource-constrained deployment.

2. **Architecture-only improvements are real and non-trivial.** Table 4(a) shows that DyNet-L *without* pre-training achieves 32.33 dB average PSNR vs. PromptIR's 32.06 dB, while using only 16M parameters vs. PromptIR's 37M (a 57% reduction). This 0.27 dB gain with dramatically fewer parameters is meaningful and derives from the architectural choices (weight-sharing + skip-connection prompts), not from large-scale data.

3. **Million-IRD is a potentially valuable community resource.** The curation of 2M high-resolution, quality-filtered images from 100M LAION-HR samples (reduced to ~8M 512² patches post-processing) fills a genuine gap in the IR pre-training landscape, where existing datasets offer at most a few thousand images. If released, this could benefit future IR research even beyond this paper.

4. **Dynamic pre-training is an elegant solution to training multiple variants.** Training DyNet-L and DyNet-S jointly by randomly alternating between them in each iteration is a natural consequence of the shared-weight design. The approach eliminates redundant computation compared to training two models independently.

5. **Consistent gains across all-in-one and single-task settings.** The paper reports improvements across dehazing (+0.76 dB SOTS), deraining (+2.32 dB Rain100L), and denoising in both all-in-one and single-task settings. The GWA plug-in for non-gray real-world haze is a simple but effective practical extension (Figure 6).

## Weaknesses

### Fatal
None.

### Major

1. **Main comparison conflates pre-training with architecture innovation.** The headline result (Table 1, Abstract) compares DyNet-L/S *with* Million-IRD pre-training against PromptIR *without* any pre-training. From Table 4, pre-training contributes 0.41 dB of DyNet-L's 0.68 dB gain (i.e., ~60%). The architecture alone contributes 0.27 dB. While the paper includes Table 4(a) showing the architecture-only comparison, the central claim "DyNet-S boosts performance by 0.43 dB" (Abstract, Figure 1 caption) attributes the full gain to the system without clarifying how much comes from pre-training vs. architecture. A controlled comparison where PromptIR is also pre-trained on Million-IRD under the same protocol is the missing experiment needed to substantiate a claim of architectural superiority.

2. **The effect of placing prompt blocks at skip connections is not isolated from the weight-sharing mechanism.** The paper touts placing prompts at skip connections (vs. the decoder side in PromptIR) as a "fundamental correction" (Section 3.1). However, Table 4(a) compares the full DyNet design (weight-sharing + skip-connection prompts) against PromptIR (no weight-sharing + decoder-side prompts). There is no ablation that keeps weight-sharing fixed and varies only the prompt placement. The performance difference in Table 4(a) could be driven primarily by the weight-sharing or the different number of effective transformer blocks, not by the prompt location. The claimed "correction" is therefore not experimentally isolated.

3. **No ablation validating that joint training does not degrade performance.** The dynamic pre-training strategy trains DyNet-L and DyNet-S jointly by randomly alternating between them. The paper claims "50% reduction in GPU hours" (compared to training two variants separately), but provides no experiment comparing the performance of jointly-trained variants against the same variants trained independently on Million-IRD. If joint training degrades either variant, the savings come at a cost that the paper does not quantify.

### Minor

1. **Missing controlled experiments weaken several claims.** (a) The 50% GPU-hour claim is mathematically valid when comparing joint training vs. separate training of both variants, but the paper does not specify the baseline it is compared against. (b) The impact of reuse frequency on the accuracy-efficiency trade-off (e.g., [2,2,2,2] vs. [4,6,6,8] vs. [8,8,8,8]) is not explored beyond the two predefined variants. (c) The dataset filtering thresholds (T_NIQE, T_BRISQUE, T_NIMA) are described as "empirically defined" but no values are reported, harming reproducibility.

2. **Implementation details are incomplete.** The dynamic pre-training schedule is described only as "randomly switch" / "randomly alternate" — the exact probability of selecting DyNet-L vs. DyNet-S per iteration is not given. The learning rate is set to 1e-4 for 1M iterations with no mention of decay. The fine-tuning phase says "dynamic finetunning" is used but does not clarify whether both variants are fine-tuned jointly or separately after pre-training.

3. **Overstated originality framing.** The paper frames weight-sharing across sequential layers as a "novel" mechanism (Introduction), but parametric weight reuse across layers is a well-established technique (RNNs, weight-tied Transformers, recurrent convolutional networks). The novelty lies in its application to all-in-one IR with variable depth for flexible deployment — this narrower claim is accurate and sufficient; the broader framing inflates the contribution unnecessarily.

### Trivial
- The paper does not report statistical significance or confidence intervals for the benchmark results. (This is standard practice in this field and should be weakened accordingly — noted here as a nice-to-have, not a flaw.)

## Nice-to-Haves
- An ablation showing pre-trained PromptIR (on Million-IRD) vs. pre-trained DyNet would cleanly resolve the most serious criticism.
- Reporting the dataset threshold values and the fraction of LAION-HR images retained at each filtering stage would improve reproducibility.
- Visualizing failure cases or challenging scenarios (e.g., mixed severe degradations) would give a more balanced assessment than showing only successes.

## Removed Points

These points were raised in the input reviews but are excluded for the reasons noted:

- **"No mention of existing weight-sharing methods in IR related work"** — Removed per meta-reviewer instructions (cannot verify existence of unmentioned works from external sources).
- **"'CircArrowRight' not defined"** — This is a LaTeX rendering artifact; the symbol would render in the actual PDF.
- **"'dynamic finetunning' typo"** — Parser artifact, not present in the original submission.
- **"No confidence intervals reported"** — Single-run evaluation on standard benchmarks is the norm in this field; this is a field-standard practice, not a flaw.
- **"Cannot be independently verified"** (dataset/model existence) — Removed per hard rules: all cited entities are assumed to exist as of the current date.
- **Strength Finder's claim that dynamic pre-training "achieves 50% reduction" is an unqualified strength** — Weakened into the review above because the claim lacks validation that joint training does not hurt performance. The idea is good but the evidence is incomplete.
- **"Training DyNet-L alone would take the same GPU hours as joint session"** — This reasoning misunderstands the claim: the 50% savings is relative to training *both* variants separately, not relative to training just one.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's two contributions: the weight-sharing architecture and the large-scale pre-training. The reviews reveal that the architecture alone provides a modest 0.27 dB gain with massive parameter savings (57% fewer), while the pre-training adds a larger 0.41 dB. This suggests that the weight-sharing mechanism's primary benefit may be in efficiency and flexibility (the ability to switch variants), not in absolute accuracy — a point the paper could emphasize more. The dynamic pre-training idea is clever precisely because it exploits the weight-sharing to train both variants at once, but the reviews correctly note that the community would want to see whether joint training hurts either variant's ceiling before adopting the method.

## Suggestions

1. **Add a controlled experiment pre-training PromptIR on Million-IRD.** This is the single most impactful addition. If PromptIR also improves substantially, the paper's contribution shifts from "state-of-the-art performance" to "comparable or better performance with much higher efficiency," which is still a strong story.
2. **Add an ablation isolating prompt placement.** Keep weight-sharing and all other factors fixed; vary only whether prompts are at skip connections vs. decoder outputs.
3. **Add an ablation comparing joint vs. separate pre-training on Million-IRD.** Report the performance of DyNet-L and DyNet-S trained independently and jointly to validate that the 50% GPU-hour savings come without degradation.
4. **Report the dataset filtering thresholds** (exact T_NIQE, T_BRISQUE, T_NIMA values) and the retention rate at each step.
5. **Rephrase the headline claims** to clearly distinguish the contributions of the architecture and the pre-training, e.g., "The architecture itself yields 0.27 dB improvement with 57% fewer parameters; large-scale pre-training adds a further 0.41 dB."

## Score and Decision

**Originality:** 6/10 — Weight-sharing across layers is known, but its application to all-in-one IR with variable-depth deployment is novel.  
**Importance of research question:** 8/10 — Efficient all-in-one restoration is practically important.  
**Claims well supported:** 4/10 — The headline claim conflates pre-training and architecture; key ablations are missing.  
**Soundness of experiments:** 5/10 — Results are reproducible in principle, but missing controlled comparisons weaken attribution.  
**Clarity of writing:** 6/10 — Generally clear, though some claims are overstated and implementation details are sparse.  
**Value to community:** 7/10 — The weight-sharing design pattern and the Million-IRD dataset (if released) are useful contributions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>