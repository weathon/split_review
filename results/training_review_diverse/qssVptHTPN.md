Now I have all the information I need. Let me write the final consolidated review.

## Summary

The paper proposes locality alignment, a post-training stage for vision transformers (ViTs) that improves local semantic encoding via a self-supervised masked reconstruction procedure called MaskEmbed. The approach fine-tunes a pre-trained ViT to reconstruct masked views of its own embeddings using an expressive decoder, without requiring any labeled data. The authors demonstrate that locality alignment improves patch-level semantic segmentation probing across many backbones (CLIP, SigLIP, IN1k classifiers, MoCo v3, etc.) and that VLMs built with aligned backbones outperform those with standard backbones on spatial understanding benchmarks (RefCOCO, OCID-Ref, TallyQA, VSR, AI2D), using CLIP ViT-L @ 336px and SigLIP SO400M @ 384px with the Prismatic training recipe.

## Strengths

- **Clean probing experiments validate the core claim independently.** The vision-centric evaluation (Figure 3, Section 4.3) uses a controlled setup: the same frozen backbone with the same two-layer transformer probing head, testing only whether the backbone's patch-level features encode class content. Locality alignment improves local probing across a wide range of backbones (CLIP, SigLIP, IN1k classifiers, MoCo v3, EVA02, DFN, OpenCLIP). This directly and cleanly supports the paper's central technical contribution — the aligned backbone encodes better local semantics — without any confound from adapter choice.

- **Demonstrated VLM improvement across multiple benchmarks and two strong backbones.** The VLM experiments (Figure 4, Section 5.2) show consistent improvements on spatial understanding benchmarks for both CLIP ViT-L @ 336px and SigLIP SO400M @ 384px, across two data mixtures. The improvements span object localization (RefCOCO, OCID-Ref), counting (TallyQA), relational QA (VSR), and diagram understanding (AI2D), covering the main categories where VLMs are known to struggle.

- **Computationally efficient.** MaskEmbed requires less than 1% of CLIP/SigLIP pre-training compute (approximately 60k gradient steps with batch size 1024 on IN21k). The ablation study verifies that strong improvements can be obtained in as few as 5 epochs of IN21k training.

- **Thorough ablation study.** The paper systematically ablates reconstruction target ([CLS] vs. full embedding sequence), mask sampling strategy, data augmentations, decoder size, and training data (IN1k vs. IN21k). These ablations provide concrete guidance for practitioners and demonstrate that the design choices (expressive decoder, full sequence reconstruction, diverse training data) are all important.

- **Outperforms CLIPSelf in a controlled comparison.** Table 1 shows MaskEmbed (local 46.32) improving over the teacher (44.63) while CLIPSelf degrades it (36.16), demonstrating that the decoder-based reconstruction approach is superior to the crop-averaging approach of CLIPSelf for local feature extraction.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The VLM evaluation varies the adapter alongside the backbone.** The comparison is between "original backbone + MLP adapter" and "aligned backbone + MaskEmbed decoder (trained during alignment)." The paper acknowledges that using an MLP with the aligned backbone "slightly hurts performance" (line 205) and switches to the decoder. This does not invalidate the core claim because (a) the probing experiments already provide clean, independent evidence that locality alignment improves local features without changing the output head, and (b) the decoder was trained jointly with the aligned backbone during MaskEmbed — it is not a separable variable. However, the paper would be strengthened by showing that a decoder-like adapter trained from scratch on the *original* backbone (without backbone fine-tuning) does not produce the same VLM gains. As it stands, the VLM evidence is slightly less cleanly attributable to the backbone change alone.

- **No statistical characterization of VLM results.** The VLM results (Figure 4) appear to be based on single-run evaluations. Given the stochasticity in VLM training (data ordering, initialization), reporting results from 2-3 seeds (or at least a subset of key benchmarks) would help establish that the improvements are not noise. This is standard practice for the field and is a concrete way to strengthen the paper.

- **The CLIPSelf comparison (Table 1) uses only CLIP ViT-B/16.** While this is a reasonable starting point for a controlled comparison, the paper's strongest VLM claims involve CLIP ViT-L and SigLIP SO400M. Showing that MaskEmbed also outperforms CLIPSelf at those scales (or explaining why the comparison cannot be run at those scales) would strengthen the paper.

- **"Negligible compute overhead" of the decoder adapter is not quantified.** The paper states the decoder adds "negligible compute overhead" (line 205) but provides no parameter count, FLOPs, or latency comparison vs. the MLP adapter. A sentence with concrete numbers would be reassuring.

### Trivial

- **Macro-averaged recall for the probing benchmark is stated but not compared against alternatives like mean average precision.** The paper justifies the metric choice (accounts for class imbalance), which is reasonable, but a brief note confirming the same trends hold with mAP or mIoU would be helpful.

## Nice-to-Haves

- Run the comparison "original backbone + decoder trained as VLM adapter (from scratch)" to fully isolate the contribution of backbone fine-tuning in the VLM setting.
- Report multi-seed variation for a subset of key VLM benchmarks.
- Include a quantitative overhead analysis of the decoder adapter (parameter count, relative FLOPs).
- Extend the CLIPSelf comparison to larger backbones (ViT-L, SO400M) if feasible.
- Provide an analysis of what the aligned backbone learns differently, e.g., visualizing decoder cross-attention or probing spatial correspondence.

## Removed Points

- **"Fatal confound" framing of the VLM evaluation**: Removed because the decoder is integral to the MaskEmbed method (trained jointly with the aligned backbone), not a separate intervention. The probing experiments already provide clean, controlled evidence for the core claim without any adapter confound. The issue is real but minor, not fatal. Moved to Minor above.
- **"Speculative claim about information compression"**: The paper provides an intuitive explanation for why the decoder is needed ("information is compressed into a space that is difficult to use"), which is reasonable given the probing evidence. The critic's demand for probing/nearest-neighbor analysis is an enhancement suggestion, not a weakness. Removed.
- **IN21k data coverage concern**: The paper explicitly acknowledges this limitation and lists web-scale data as future work (line 96). Already addressed. Removed.
- **Mask sampling clarity**: The paper already describes the procedure clearly (lines 117-118) including formal notation in a footnote. This is a nitpick based on misreading. Removed.
- **Formatting/style nitpicks**: Parser artifacts, not author errors.

## Novel Insights

The most novel insight emerging across the reviews is that post-hoc locality alignment through masked embedding reconstruction can recover local semantics from globally-trained ViTs *without* sacrificing global understanding — and that the aligned embeddings live in a different representational space that requires an expressive decoder (vs. a simple MLP) to interface with downstream LMs. This suggests that the standard practice of plugging CLIP/SigLIP ViTs into VLMs via simple linear/MLP projections may leave useful spatial information on the table, not because the backbone lacks the information, but because the information is nonlinearly encoded and needs a learned projection specific to the aligned space. This observation — that representation "compression" during alignment creates an accessibility issue that must be addressed with a learned decoder — is an interesting practical finding that could inform future VLM architecture design.

## Suggestions

1. **Run the experiment: original backbone + decoder adapter (trained from scratch during VLM training).** This would directly address the main reviewer concern by showing whether the decoder architecture alone explains the VLM gains. If the decoder-only variant performs worse, the locality alignment claim is cleanly supported.

2. **Add a brief statistical note.** Report the range or standard deviation for at least 2-3 seeds on one key benchmark (e.g., RefCOCO with CLIP ViT-L) to demonstrate reproducibility.

3. **Quantify decoder overhead.** Add a sentence: "The decoder adds X million parameters (Y% of the MLP baseline) and increases inference latency by Z%."

4. **Acknowledge the adapter limitation clearly in the discussion.** Add a sentence noting that the aligned backbone's embeddings require the decoder adapter, and confirm via probing that the improvement is not an artifact of the decoder.

## Score and Decision

The paper makes a clear and useful contribution: a computationally efficient post-training method that improves local semantic encoding in ViTs, convincingly validated through well-designed probing experiments across many backbones, and translated to VLM improvements on spatial benchmarks. The VLM confound (differing adapters) is real but minor — it does not threaten the core claim because the probing experiments provide independent, controlled evidence. The paper would benefit from the missing baseline and multi-seed results, but these are addressable improvements, not fatal flaws.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>