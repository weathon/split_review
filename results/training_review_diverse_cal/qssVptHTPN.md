Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper proposes "locality alignment," a post-training stage for ViTs that uses a masked reconstruction procedure called MaskEmbed to improve patch-level semantic encoding. The key idea is that pre-trained ViTs (CLIP, SigLIP) trained with image-level supervision fail to encode local semantics, and that this can be fixed via self-supervised fine-tuning using the pre-trained model's own masked outputs as targets — requiring <1% of pre-training compute. The authors evaluate on a patch-level probing benchmark (showing consistent improvements across many backbones) and in vision-language models (showing gains on spatial reasoning benchmarks like RefCOCO, TallyQA, VSR).

## Strengths

1. **Well-motivated and timely problem.** The paper identifies a genuine gap — VLMs struggle with spatial reasoning, and part of the problem may be that their vision backbones (CLIP, SigLIP) are trained with image-level supervision and lack local semantic encoding. The solution (self-supervised fine-tuning without new annotations) is practical and efficient.

2. **Clean vision-centric validation.** The probing benchmark (Section 4) is well-designed: frozen backbone, patch-level multi-label classification, separate global/local metrics. Results consistently show MaskEmbed improves local feature extraction across many backbones (IN1k classifiers, CLIP, SigLIP, OpenCLIP, DFN, EVA02, MoCo v3), with especially strong gains for the large high-resolution models used in VLMs (CLIP ViT-L @336px, SigLIP SO400M @384px). The ablation study (Section 4.2) systematically investigates reconstruction target, mask distribution, augmentations, decoder size, and training data.

3. **Controlled VLM comparisons within a shared framework.** Using the Prismatic library with fixed LM (Llama-2 7B) and two data mixtures, the paper compares VLMs with and without locality alignment for both CLIP and SigLIP backbones. Improvements are shown on spatial benchmarks (RefCOCO, OCID-Ref, TallyQA, VSR, AI2D) without degrading holistic benchmarks like VQAv2 — across four separate comparisons (Figure 5).

4. **Efficiency is demonstrated.** MaskEmbed trains for 5 epochs on IN21k with batch size 1024, which the paper correctly states is <1% of CLIP/SigLIP pre-training cost. The decoder-as-adapter adds negligible overhead.

5. **Rigorous comparison with CLIPSelf.** Table 1 shows that MaskEmbed outperforms CLIPSelf. Critically, the paper includes an ablation where MaskEmbed uses averaged features (mimicking CLIPSelf's decoder) with the same masking strategy, and shows this degrades performance — isolating the decoder as the key design difference, not the masking approach.

## Weaknesses

### Fatal
None.

### Major

1. **Adapter confound in VLM experiments (missing control: original backbone + decoder adapter).** The paper's VLM experiments compare (original backbone + MLP adapter) vs. (aligned backbone + MaskEmbed decoder as adapter). The paper acknowledges that the aligned backbone with an MLP adapter hurts performance (Section 5, line 205), and therefore adopts the decoder as the adapter for the aligned backbone. This means the treatment differs from the baseline in *two* ways: the backbone AND the adapter architecture. The missing control — original backbone + decoder adapter — is necessary to determine whether the VLM gains come from the improved backbone, the better adapter, or the combination. Without this control, the paper's core claim that "locality alignment improves VLMs" cannot be fully attributed to the backbone change. The probing experiments independently validate the backbone improvement, but the VLM evidence for the *mechanism* is substantially weakened.

2. **No statistical variance reported for VLM results.** The VLM results (Figure 5) are presented as single-point radar charts without error bars, confidence intervals, or indication of multiple runs. For benchmarks with small effect sizes, it is impossible to assess whether improvements are reliable or within run-to-run noise. This reduces confidence in the quantitative VLM claims.

### Minor

1. **The connection between probing and VLM performance is assumed, not tested.** The probing benchmark shows MaskEmbed improves patch-level classification with a frozen backbone. The VLM uses the same frozen backbone but a very different training objective (autoregressive language modeling). The paper does not empirically test whether improved probing scores *mediate* the VLM improvements — it is possible that fine-tuning on IN21k changes feature distributions in ways that incidentally help the decoder adapter without reflecting better local semantics. A targeted analysis (e.g., probing VLM internals on localization tasks after VLM training) would bridge this gap.

2. **No evaluation of zero-shot capabilities after alignment.** The paper acknowledges that MaskEmbed does not preserve CLIP's zero-shot classification abilities (line 167), and notes that training CLIP too long on IN1k can degrade performance (Section 4.2). However, the paper does not measure what other capabilities might be lost after alignment on IN21k (e.g., retrieval, open-vocabulary detection), which would help contextualize the VLM trade-offs.

3. **Compute cost lacks concrete numbers.** The paper states MaskEmbed costs <1% of pre-training compute but does not report actual GPU-hours or FLOPs for the runs. Given that efficiency is emphasized, concrete numbers would strengthen this claim.

### Trivial
None.

## Nice-to-Haves

- Run the missing control experiment: original backbone + decoder adapter as the VLM adapter. If this shows no improvement, the VLM gains cleanly attribute to the backbone. If it does improve, the authors could disentangle the backbone and adapter contributions.
- Report VLM results in a numbered table alongside the radar charts so readers can directly compare raw scores.
- Provide a brief analysis probing VLM attention or hidden states on localization tasks to ground the claimed mechanism.
- Report zero-shot classification/retrieval metrics for the aligned backbone to measure what is preserved.

## Removed Points

- **CLIPSelf comparison criticism ("the two objectives differ in more ways than just the decoder"):** The paper already addresses this. Table 1 includes a condition "MaskEmbed (avg)" that uses the same MaskEmbed objective and masking strategy but with averaged features instead of a transformer decoder. This directly controls for the objective, varying only the decoder architecture. The critic missed this ablation. The comparison is fair.

- **Criticism that the paper should test bounding-box regression probing:** This is beyond the paper's stated scope. The probing benchmark is designed to test patch-level semantic classification, which is directly relevant to VLMs. Asking for bounding-box regression is scope creep.

- **"The comparison over-attributes the difference to the decoder" (w.r.t. CLIPSelf):** Removed because the paper explicitly runs the controlled comparison with averaged features, showing the decoder is indeed the key differentiator.

## Novel Insights

The most interesting observation from this review is the asymmetry in evidence quality between the vision-only and VLM experiments. The probing benchmark is cleanly controlled (frozen backbone, classification head trained from scratch) and convincingly demonstrates that MaskEmbed improves local feature extraction. The VLM experiments, by contrast, change both the backbone and the adapter simultaneously, creating a confound that weakens the causal interpretation. This suggests a design principle for future work: when evaluating a backbone improvement in a downstream system (VLM, detection, etc.), isolate the backbone change before swapping other components. The paper's own admission that the aligned backbone with an MLP adapter "slightly hurts performance" (line 205) is revealing — it implies the aligned embeddings live in a different representational space that requires a different readout mechanism, which is an interesting finding in its own right but undermines the claim that the backbone itself is straightforwardly "better."

## Suggestions

1. **Run the critical missing control:** Train a VLM with the original (unaligned) backbone but using the MaskEmbed decoder (randomly initialized or separately trained on the original backbone) as the adapter. If this shows no improvement over the original+MLP baseline, then the VLM gains are attributable to the backbone change. If it does improve, the paper needs to separate backbone and adapter contributions.

2. **Report VLM results with variance.** At minimum, state whether the Prismatic recipe is deterministic and report results from 2-3 runs or bootstrapped metrics for the main comparisons.

3. **Add a mechanism check:** After VLM training, probe the VLM's patch-level representations on localization tasks to verify that the improved local encoding from the backbone is actually used by the LM, rather than ignored.

4. **Report what the aligned backbone loses.** Measure zero-shot classification/retrieval for the aligned backbone to clarify the capability trade-offs, which is important for practitioners deciding whether to adopt this method.

## Score and Decision

This paper tackles an important problem and provides a clean, efficient method. The probing experiments are thorough and convincing. However, the VLM experiments — which form the paper's headline contribution — have a significant confound: the treatment changes both the backbone and the adapter architecture relative to the baseline, so the VLM improvements cannot be cleanly attributed to locality alignment. This confound is fixable with additional experimentation, and the probing evidence independently supports the method's effectiveness for local feature extraction. The paper has genuine value, but in its current form the central VLM claim is not fully supported. I recommend **borderline reject** — the authors should address the confound before the work can be accepted.

**Originality:** Good — locality alignment as a post-training stage is a novel framing.

**Importance of question:** High — improving VLM spatial reasoning is a timely and important goal.

**Claims support:** Partially — probing claims are well-supported; VLM claims are confounded.

**Soundness:** Adequate for probing experiments; compromised for VLM experiments due to missing control.

**Clarity:** Well-written and well-structured.

**Value to community:** Moderate — the method is practical and efficient, but the core claim needs stronger evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>