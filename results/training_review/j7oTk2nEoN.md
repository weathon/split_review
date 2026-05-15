Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper introduces two gray-box fine-tuning frameworks — DarkGray-box Input/Output Adapters (DGA) and LightGray-box Adapters (LGA) — that adapt foundation models for downstream tasks while keeping the backbone's architecture and weights hidden and frozen. DGA modifies only the input (via learned convolutional layers and extra/shift text tokens) and output (linear projection) of the backbone; LGA additionally injects learnable tokens into intermediate transformer layers. Experiments on text-image retrieval (COCO, Flickr30K, Stanford-Cars), text-video retrieval (MSR-VTT, VATEX), image classification (ImageNet), and sketch retrieval (Sketchy) across CLIP, BLIP, and DINOv2 backbones show that DGA achieves performance within ~1–2 points of LoRA while using ~0.4% of parameters and keeping the backbone sealed.

## Strengths

- **Novel and effective gray-box paradigm that achieves competitive performance without weight access**: DGA achieves Recall@1 within 0.38 points of LoRA on COCO (Table 2) and within 1 point on MSR-VTT (Table 5) despite having no access to model weights or architecture. This directly validates the core claim that strong adaptation is possible with a sealed backbone.

- **Broad evaluation across diverse tasks, domains, and backbones**: The paper tests 4+ retrieval/classification tasks (text-image, text-video, sketch-to-image, classification) with 3 backbones (CLIP, BLIP, DINOv2) spanning natural images, sketches, cars, and video frames (Tables 2–7). This range demonstrates the generality of the framework.

- **Systematic ablation study isolating adapter contributions**: Table 8 disentangles the impact of input vs. output adapters and text vs. visual modalities individually and in combination, providing clear evidence that joint optimization of all adapters yields the best results. The analysis of shift vs. extra tokens provides concrete design insights.

- **Extreme parameter efficiency with practical deployment advantages**: DGA uses ~0.4% of total model parameters (Section 3.1), requires no per-architecture engineering, preserves the original inference pipeline, and avoids multiple model copies — directly addressing the stated goals of storage efficiency and deployment simplicity.

- **Non-obvious advantage on low-data domain-specific tasks**: On Stanford-Cars (197 classes, limited samples), DGA and LGA outperform both LoRA and full fine-tuning across all Precision@K metrics (Table 4), suggesting that input-space adaptation can be more effective than weight modification when data is scarce.

## Weaknesses

### Fatal
None. The paper's core claim — that competitive fine-tuning is possible without exposing backbone weights — is supported by the empirical results. The weaknesses below are serious but addressable.

### Major

1. **Baseline comparisons lack sufficient documentation to be fully trustworthy.** The paper reports no hyperparameter details for any baseline: LoRA rank, alpha, and target modules are not specified; learning rate, batch size, number of epochs, and optimizer settings are absent for all methods including DGA. No error bars, variance estimates, or significance tests are reported for any experiment. This is especially problematic when DGA outperforms white-box methods on datasets like Stanford-Cars (Table 4) — while the paper's explanation (low sample count favors input-space adaptation) is plausible, the lack of evidence that baselines were well-tuned leaves the fairness of comparisons in question. This problem cuts across nearly every table and weakens confidence in the headline numbers.

2. **The paper's security/privacy motivation is prominently featured but never empirically validated.** The introduction and framing emphasize protecting proprietary rights, privacy, and preventing model theft as core motivations. However, no experiment tests whether gradients from DGA can leak backbone information, whether the approach resists known gradient-inversion attacks (e.g., Zhu et al. 2019; Zhao et al. 2020, which the paper does not cite), or whether DGA is meaningfully more secure than alternatives in practice. The paper does acknowledge this gap (Section 2: "it is not yet practical or feasible to recover an arbitrary model's architecture and weights based solely on input gradients... leaving this exploration for future research"), but given how centrally the security motivation features in the paper's framing, the absence of any validation — even a simple adversarial reconstruction attempt — is a significant omission.

### Minor

3. **The central ablation study (Table 8) uses CLIP while main retrieval results use BLIP.** Adapter behavior (e.g., interaction between visual and textual branches, effectiveness of shift vs. extra tokens) likely depends on the backbone architecture and pre-training. Running the ablation on CLIP does not invalidate it, but it weakens the evidential connection to the main experimental setup, which predominantly uses BLIP. The paper should either run the ablation on the primary backbone or explain why CLIP was chosen and why the conclusions are expected to transfer.

4. **LGA is insufficiently distinguished from prior prefix/prompt tuning work.** The paper acknowledges LGA is inspired by MaPLe and Prefix-Tuning (Section 2), but the description "enhancing adaptability by injecting learnable tokens into each transformer layer" is functionally identical to those methods. The claimed difference — independent vectors per layer with no shared MLP — is not empirically shown to matter, and it is unclear what LGA contributes beyond applying known techniques to the gray-box setting. The novelty of LGA relative to existing work is not crisply articulated.

5. **No training details provided for reproducibility.** Beyond hyperparameter specifics (point 1), the paper does not report any training configuration: learning rate schedules, batch sizes, number of epochs, optimizer choice, compute hardware, or runtime. This makes independent reproduction difficult.

### Trivial
- Table numbers in the ablation text reference "Table 14" (textual token analysis) whose content is missing from the extracted text due to parser truncation; this exists in the original submission.

## Nice-to-Haves

- A security evaluation: even a simple experiment testing whether a third party could infer backbone properties (architecture family, embedding dimension) from gradients would substantially strengthen the paper's motivation.
- Head-to-head comparison with Visual Prompt Tuning (Jia et al., 2022) and input-space prompting methods to better isolate the contribution of DGA's visual adapter.
- Per-dataset LoRA hyperparameter grids confirming baseline configurations were reasonably tuned.

## Removed Points

- **Criticism about missing Visual Prompt Tuning (Jia et al., 2022) in related work**: Removed per rule — the reviewer cannot verify existence of this citation as a known gap from external knowledge.
- **Criticism about Table 14 content being absent**: Removed per rule — parser strips appendix content; it exists in the original submission.
- **Criticism about "cannot be independently verified" / reproducibility concerns rooted in doubting the existence of cited references**: Not applicable; no reviewer explicitly raised this.
- **Claim that Stanford-Cars outperformance "cannot be trusted" specifically** (rather than the general baseline tuning concern): Softened. The paper offers a reasoned explanation for the result (low-data regime favors input-space adaptation), and the more general concern about baseline tuning documentation subsumes this.

## Novel Insights

The reviews collectively surface an interesting tension: DGA's strongest results come on the tasks where one would least expect them (outperforming LoRA on Stanford-Cars, being nearly tied on COCO), while its weakest results align with the intuition that distant-domain tasks (sketch) require weight modification. This suggests that the optimal setting for gray-box adaptation may be tasks where the backbone already has reasonable representations and what's needed is lightweight task-specific "steering" of the input representation, rather than tasks requiring deep representational changes. The paper does not fully exploit this insight — e.g., by characterizing when input-space adaptation is beneficial vs. when it hits a ceiling — but the data pattern is there.

## Suggestions

1. **Add a training details appendix** specifying hyperparameters for all methods (LoRA rank/alpha/target modules, learning rate, batch size, epochs, optimizer) across all datasets, plus error bars or at least 3-run means for key comparisons.
2. **Run the ablation study (Table 8) on the primary BLIP backbone** used in the main experiments, or provide a clear rationale for why CLIP-based ablation conclusions transfer.
3. **Add a brief security discussion or simple experiment**: Even testing whether a held-out attacker can recover the backbone's embedding dimension or architecture family from DGA gradients would go a long way toward grounding the paper's motivational claims.
4. **Sharpen the articulation of LGA's novelty** relative to MaPLe/Prefix-Tuning. If the contribution is the specific design choice (independent vectors, no shared MLP) and its application to retrieval tasks, say this explicitly and ablate the design choice.

## Score and Decision

The paper presents a genuinely useful idea (gray-box fine-tuning with sealed backbone) with broad empirical support across multiple tasks and backbones. The results are promising and the parameter efficiency is compelling. The main weaknesses — undocumented baseline tuning, unvalidated security motivation, and a mismatched ablation backbone — are real but not fatal; they erode confidence in some specific comparisons but do not invalidate the core contribution. The paper would benefit substantially from addressing these concerns but already contains a solid empirical contribution.

**Score: 6.0** — A methodologically sound paper with a clear contribution, held back by documentation gaps in the experimental setup and a motivational claim that outruns the evidence. With a thorough baseline documentation appendix and a consistent ablation design, this could be a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>