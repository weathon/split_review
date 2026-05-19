- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3
I've thoroughly read and verified the paper content. Now I will produce the final authoritative review.

---

## Summary

This paper proposes AntifakePrompt, a deepfake detection method that formulates binary classification as a visual question answering (VQA) task and applies soft prompt tuning to a pretrained InstructBLIP model. By inserting a learnable pseudo-word embedding (4,864 parameters total) into the question prompt "Is this photo real?" and optimizing only the embedding, the method turns a generic VLM into an effective deepfake detector. Evaluated on 23 datasets (3 held-in, 20 held-out) covering text-to-image, inpainting, super-resolution, face swap, stylization, and adversarial attacks, AntifakePrompt achieves 91.81% average accuracy, substantially outperforming all non-VLM baselines while using far fewer parameters and training data.

---

## Strengths

1. **VQA + prompt tuning yields dramatic gains over pretrained VLM baselines.** Table 2 shows that pretrained InstructBLIP (36.53% average) is transformed into AntifakePrompt (91.81% average) — a 55-point improvement — directly validating the core claim that prompt-tuned VLMs are effective fake image detectors.

2. **Comprehensive evaluation across 23 datasets covering six generative categories.** The paper curates held-in and held-out test sets spanning text-to-image (SD2, SD3, SDXL, IF, DALL·E 2/3, Playground, SGXL, GLIDE, DiffusionDB), inpainting (LaMa, SD2IP), super-resolution (LIIF, SD2SR), stylization (ControlNet), face swap (DF, DFDC, FF++), and three attack scenarios (adversarial, backdoor, data poisoning). This goes well beyond prior work.

3. **Superior held-out accuracy with extreme parameter efficiency (4,864 parameters).** AntifakePrompt tunes only the embedding vectors of a single pseudo-word (768-dim for Q-Former, 4,096-dim for LLM), compared to 11M–23M parameters in baselines like DE-FAKE and Wang2020, while still outperforming them on most held-out datasets.

4. **Demonstrated data efficiency.** The ablation study (Table 1) shows that with only 15K training samples (a quarter of DE-FAKE's data), AntifakePrompt still outperforms DE-FAKE on most held-out sets; with 1.5K samples it surpasses Wang2020 on all fake datasets.

5. **Robustness to adversarial, backdoor, and data poisoning attacks.** AntifakePrompt achieves 87–89% accuracy on all three attack types (Table 2, last three rows), while the next-best VLM variant (LoRA-tuned InstructBLIP) drops to 39–51% on these sets, demonstrating genuine sensitivity to subtle manipulations.

6. **Systematic ablation studies identify optimal design choices.** The paper separately evaluates pseudo-word position (replace/prefix/postfix), tuning targets (Q-Former only / LLM only / both), and training set sizes, providing clear empirical evidence for the chosen configuration (Table 1).

---

## Weaknesses

### Fatal
None.

### Major

1. **Train/test split for COCO is not clearly documented.** The paper states that 90K COCO images are used for real-image training (line 137–138) and 3K Flickr30k images form a held-out real test set. However, Table 2 reports accuracies on COCO itself (as a held-in dataset) without specifying how many COCO test images there are or confirming they are disjoint from the 90K training images. The same question applies to the held-in fake sets (SD3, SD2IP). This is a documentation gap that makes it impossible for readers to verify complete separation. The paper should explicitly state the test-set sizes for COCO, SD3, and SD2IP and confirm no overlap with training.

2. **LaMa failure case is acknowledged but not analyzed.** On the LaMa inpainting dataset, AntifakePrompt achieves only 39.40% in its primary configuration — below random guessing (Table 2). Adding LaMa to the training set raises this to 55.80%, still far below the 90%+ on most other datasets. The paper notes this "relatively lower performance" (line 276) but offers no analysis of *why* LaMa is so challenging for a VLM-based detector. Since inpainting creates fundamentally different artifact patterns (seamless hole-filling) than full-image generation, understanding this blind spot is important for characterizing the method's generalization boundaries.

### Minor

3. **Abstract claims "average accuracy over unseen domains" but reported average includes held-in datasets.** The abstract states improvement "in average accuracy over unseen domains" but the "Average" row in Table 2 (91.81%) averages over all datasets including three held-in sets (COCO, SD3, SD2IP). The paper should report separate averages for held-in and held-out sets, or rephrase the claim to avoid implying the average is restricted to unseen domains.

4. **No analysis of *what* the prompt-tuned VLM learns.** The paper demonstrates that prompt tuning improves performance dramatically, but does not examine what visual features or artifacts the tuned pseudo-word captures. An analysis (e.g., attention visualization, feature-space probing) would strengthen the understanding of why the approach generalizes so well.

### Trivial
None.

---

## Nice-to-Haves

- A fully finetuned InstructBLIP baseline (not just LoRA) would provide a direct reference point for the efficiency-accuracy trade-off claimed by prompt tuning.
- Reporting results over multiple random seeds with standard deviations would increase confidence, especially for the ablation studies where differences are sometimes small.
- The ablation studies use SD2 while main experiments use SD3 (acknowledged explicitly at line 149). While explained, unifying this choice would avoid reader confusion.

---

## Removed Points

*These points were flagged by reviewers but removed after cross-checking against the paper:*

- **Missing related works on CLIP-based detection** — Removed per instructions (do not mention missing related works).
- **SD2/SD3 inconsistency in ablations** — Removed because the paper explicitly acknowledges this: "SD3 (SD2 for ablation studies)" (line 149). The reviewer noted this but it is already addressed.
- **Demand for full finetuning baseline** — Removed; this is a nice-to-have, not a core weakness. The paper's claim is about prompt tuning being efficient and effective, not about being strictly better than full finetuning in every setting.
- **Confidence intervals / standard deviations** — Removed; single-run evaluation on large-scale benchmarks is standard practice in this area.
- **Conclusion does not mention LaMa** — Removed; the conclusion is a high-level summary, and not every limitation must appear there.
- **"Missing appendix" and "proofs deferred to appendix"** — Removed; the parser strips these sections; they exist in the original submission.
- **Formatting/style nitpicks and parser artifacts** — Removed; these are not author errors.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths, and the cross-checking did not surface an angle — positive or negative — that the authors themselves do not already articulate or could not address with straightforward revisions.

---

## Suggestions

1. **Add a clear data split table.** State explicitly: "Training uses 90K COCO images (split X), 30K SD3 images, 30K SD2IP images. Testing on COCO uses K disjoint images from a held-out partition of COCO; testing on SD3 and SD2IP uses K disjoint images from those same sources." This resolves the main documentation gap.
2. **Report separate held-in and held-out averages** in Table 2 or as a note in the caption, so the "unseen domains" claim is auditable.
3. **Add a brief qualitative analysis of the LaMa failure.** For example, examine attention maps from the Q-Former on LaMa vs. other fake images, or test whether a small number of LaMa exemplars (not the full 30K) resolves the issue. Even a paragraph of analysis would strengthen the paper's understanding of its own limitations.
4. **Consider visualizing the learned pseudo-word embedding** (e.g., t-SNE of tuned vs. untuned embeddings) to shed light on what the prompt tuning modifies.

---
