I've now verified all claims against the paper. Let me write the final consolidated review.

## Summary

This paper proposes DyNet, a family of encoder-decoder networks for all-in-one image restoration (denoising, deraining, dehazing). The core idea is a weight-sharing mechanism—a single transformer block's weights are reused across subsequent blocks at each encoder-decoder level—enabling a single checkpoint to serve both bulky and lightweight variants by varying only the reuse frequency. The paper also introduces a dynamic pre-training strategy that trains both variants concurrently in one session, and a large-scale pre-training dataset (Million-IRD, ~2M images). DyNet-L achieves 32.74 dB average PSNR across tasks (Table 1), +0.68 dB over PromptIR, while DyNet-S uses 56.75% fewer parameters and 31.34% fewer GFlops.

## Strengths

- **Weight-sharing mechanism delivers substantial efficiency gains with maintained or improved accuracy.** Even *without* pre-training (Table 5a), DyNet-L (32.33 dB) slightly exceeds PromptIR (32.06 dB) while using 56.75% fewer parameters (16M vs 37M). DyNet-S (32.09 dB) matches PromptIR with 56.75% fewer parameters and 31.34% fewer GFlops. This cleanly shows the architecture's core value: parameter efficiency without sacrificing performance.

- **Million-IRD pre-training demonstrably boosts performance.** Table 5 quantifies the contribution: pre-training on Million-IRD adds +0.41 dB for DyNet-L (32.33→32.74) and +0.40 dB for DyNet-S (32.09→32.49). The dataset is a tangible resource contribution to the community, with 2M high-quality images filtered via NIQE, BRISQUE, and NIMA metrics.

- **State-of-the-art all-in-one results on multiple tasks.** Table 1 shows DyNet-L achieves 38.69 dB on Rain100L deraining (+2.32 dB over PromptIR) and 31.34 dB on SOTS dehazing (+0.76 dB), with competitive denoising results. The visual comparisons (Figs. 3–5) support these quantitative gains.

- **Ablation studies separate architecture from pre-training contributions.** Table 5 explicitly partitions results into (a) without pre-training and (b) with pre-training, allowing the reader to assess each contribution independently. This design partially addresses concerns about confounded comparisons.

## Weaknesses

### Fatal
None.

### Major

- **The 50% GPU-hour savings claim for dynamic pre-training is asserted without any empirical validation.** The paper repeats this claim in the abstract, introduction, method section (line 137), experiments (line 379), and conclusion (line 390), but reports zero GPU-hour measurements or wall-clock times. No ablation compares models pre-trained jointly (the proposed method) against models pre-trained separately for the same number of effective updates per variant. Since the random activation scheme could mean each variant receives only half the effective training updates, the reader cannot assess whether the claimed savings come at a quality cost. This is a central paper contribution left completely unsubstantiated.

- **The headline performance gap (0.43–0.68 dB over PromptIR) conflates architecture + pre-training + dataset effects, and the architecture itself is not fully isolated from PromptIR's.** The ablation in Table 5(a) *partially* disentangles these (architecture-only DyNet-L achieves +0.27 dB over PromptIR), but the paper never compares PromptIR pre-trained on Million-IRD against DyNet pre-trained on Million-IRD. Without this comparison, it is impossible to know how much of the final advantage comes from the architectural innovations (weight sharing, skip-connection prompting) versus simply having access to large-scale pre-training data that PromptIR did not use. Additionally, DyNet differs from PromptIR in multiple ways simultaneously (weight sharing, depth configuration, prompt placement); no ablation isolates the specific effect of moving prompts from decoder to skip connections while keeping everything else identical.

- **The dynamic pre-training strategy's design is presented without analysis of key choices.** The pre-training corrupts 80% of each input patch (50% augmentation + 30% masking, line 195). The paper does not ablate the masking ratio, augmentation strategy, or the effect of the aggressive 80% corruption rate on downstream fine-tuning quality. These are non-trivial design decisions that could significantly affect results.

### Minor

- **The notation for weight reuse (Sec. 3.1) could be clearer.** The equations and description leave ambiguity about whether the reuse frequency \(f\) at each level counts the initial block plus \(f-1\) reused blocks (as the equations imply) or something else. The paper also does not explicitly state total block counts per variant or how the reuse frequencies map to both encoder and decoder separately versus jointly.

- **The ablation on degradation combinations (Table 6) shows raw results without analysis.** The paper notes that "some degradations are more relevant" but does not analyze *why* certain task combinations help or hurt, limiting the table's interpretive value.

- **No confidence intervals, standard deviations, or per-image statistics are reported.** Given that some improvements are small (e.g., 0.09–0.11 dB in denoising), it is difficult to assess statistical significance.

### Trivial
- None that survive filtering.

## Nice-to-Haves

- A controlled experiment validating that pre-training on Million-IRD is superior to pre-training on the combined existing datasets (LSDIR + DIV2K + Flickr2K, ~90K images) would strengthen the dataset contribution.
- Reporting actual GPU hours for joint vs. separate pre-training, even as a rough estimate, would substantiate the efficiency claim.
- An ablation variant that removes weight sharing but keeps skip-connection prompting would isolate the specific effect of prompt placement.

## Removed Points

- **GWA comparison unfairness (Harsh Critic):** The critic claimed that the Gray-World Assumption pre-processing is applied only to DyNet and not to PromptIR in the real-world dehazing comparison. **This is factually incorrect.** The paper explicitly states (lines 261–262): "For a fair assessment, we also include results from GWA+PromptIR (PromptIR+)." The comparison includes PromptIR+.
- **"Essentially tied" framing for DyNet-L without pre-training:** The critic states that without pre-training DyNet variants are "essentially tied" with PromptIR. DyNet-S (32.09) is indeed close to PromptIR (32.06), but DyNet-L (32.33) shows a +0.27 dB advantage with the same GFlops and 56.75% fewer parameters—a real architectural contribution. The characterization conflates two different variants.
- **Reuse frequency as "notationally confusing" (detailed claim):** The equations in lines 103–106 make the mechanism clear (b=1 uses w^1, b=2:f reuse w^1). The mapping of reuse frequencies to encoder-decoder levels is explicitly stated (lines 118–119). This is a minor clarity preference, not a substantive weakness.
- **Strength: Dynamic pre-training cutting GPU hours by 50%:** Listed as a strength by the Strength Finder, but this claim lacks empirical support in the paper (as noted in Major weaknesses above). A claimed but unvalidated advantage cannot be listed as a confirmed strength.

## Novel Insights

The weight-sharing mechanism itself is the most interesting aspect of this work—it is genuinely unusual to see the same block weights reused across multiple sequential transformer blocks without a performance penalty. The paper shows that networks with shared weights can match or exceed the performance of unshared networks of similar depth, while using far fewer parameters. This suggests that transformer blocks in image restoration may be over-parameterized and that the inductive bias of repeated application of the same transformation may actually be beneficial. The ablation in Table 5(a) is the strongest evidence for this: DyNet-L (16M params, shared weights, 242 GFlops, 32.33 dB) vs PromptIR (37M params, unshared weights, 242 GFlops, 32.06 dB) shows that the shared-weight variant is both more parameter-efficient and slightly more accurate. The Million-IRD dataset, if released, would also be a practical contribution to the field.

## Suggestions

1. **Provide GPU-hour measurements.** Even approximate wall-clock times for joint vs. separate pre-training would turn the 50% claim into evidence. Without this, the dynamic pre-training contribution cannot be evaluated.
2. **Pre-train PromptIR on Million-IRD** using the same protocol. This is the single most important missing experiment: it would cleanly separate the architecture contribution from the data contribution.
3. **Add an ablation that isolates prompt placement.** Compare: (a) DyNet with skip-connection prompts (current), (b) DyNet with decoder-side prompts (PromptIR-style), while keeping weight sharing fixed. This would directly test the "fundamental correction" claim.
4. **Report standard deviations or per-image statistics** for the all-in-one results, especially for denoising where improvements are small (0.09–0.11 dB).

## Score and Decision

The paper presents a genuine architectural contribution (weight sharing for efficient all-in-one IR) and a useful dataset. However, two of its three claimed contributions suffer from significant evaluation gaps: the 50% GPU-hour savings claim is entirely unsupported, and the headline accuracy numbers conflate architecture, pre-training, and data effects in a way that the current experiments cannot fully disentangle. These are addressable in revision but materially weaken the paper as submitted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>