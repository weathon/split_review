---

## Summary
Gen2Seg proposes finetuning generative models (Stable Diffusion and MAE encoder+decoder) for category-agnostic instance segmentation using an instance coloring loss on a narrow synthetic dataset (indoor furnishings and cars from Hypersim + Virtual Kitti 2). The core empirical finding is that generative pretraining encodes cross-category grouping priors that survive narrow finetuning: the resulting models generalize zero-shot to unseen object types (people, animals, art, x-rays, fine structures), approaching or surpassing heavily-supervised SAM on several benchmarks. The MAE result is particularly striking, as it achieves this without internet-scale pretraining.

---

## Strengths

- **Strong quantitative zero-shot generalization to diverse unseen domains (Table 1).** SD achieves 51.4 vs. SAM's 16.8 mIoU on iShape, and competitive performance on DRAM (48.2 vs. 50.2), EgoHOS (40.0 vs. 56.4), and PIDRay (30.9 vs. 44.2) — all without seeing masks for these categories. MAE-H reaches competitive performance on large-object benchmarks.

- **MAE results provide the cleanest evidence for the central thesis (Table 1).** MAE is pretrained only on unlabeled ImageNet-1K, so its cross-domain generalization (to art, x-rays, fine structures) cannot be attributed to internet-scale data breadth. This isolates the reconstruction-based generative objective as the plausible source of the grouping prior. MAE-H achieves 50.0/23.2/3.5 vs. SAM's 57.0/59.5/56.9 on COCO_exc, with strong iShape and EgoHOS results.

- **Robustness to drastic reductions in finetuning diversity is a compelling supporting result (Table 2).** Using only 10 Hypersim classes yields nearly identical performance to the full 33+ class set (e.g., SD iShape 53.6 vs. 51.4). Even ClevrTex (simple 3D shapes) still yields meaningful transfer. This rules out dataset-specific factors and implicates the pretraining.

- **Superior edge quality attributed to generative prior (Figure 6 / Table 6).** SD achieves Edge AP of 93.4 vs. SAM's 79.0 on BSDS500. Crucially, SD (COCO) — finetuned on coarse polygonal masks — still attains 89.7 vs. SAM's 79.0, strongly suggesting that fine boundary precision comes from the generative prior rather than training data quality.

---

## Weaknesses

### Fatal
None.

### Major

- **DINO-B baseline has an architectural asymmetry that weakens the causal argument.** Section 4.2 describes DINO-B as attaching DINO features to a *frozen* VAE decoder via a simple up-conv, finetuned end-to-end (up-conv only). In contrast, MAE-B/H finetune the full encoder+decoder jointly from a generatively pretrained initialization. These are not equivalent conditions: DINO is being asked to steer a frozen generative decoder through a small bridge module. A fairer comparison would either (a) give DINO a randomly-initialized decoder trained from scratch on the same data, or (b) fully finetune DINO + VAE decoder jointly. As configured, poor DINO-B performance could reflect the frozen decoder bottleneck rather than discriminative pretraining *per se*, making the attribution to "generative vs. discriminative pretraining" inconclusive for this baseline. This is the paper's most significant gap in causal evidence.

- **For SD, the causal attribution to "generative mechanism" vs. "data breadth" is unresolved.** SD is pretrained on LAION-5B (~2B+ images) covering virtually all visual categories appearing in the evaluation sets (art, x-rays, animal images, hands, etc.). The observed generalization for SD could plausibly stem from rich multi-domain representations acquired during pretraining, not from a learned grouping mechanism per se. The paper identifies the MAE results as the cleaner evidence (correctly), but still makes global claims about generative pretraining. Adding explicit discussion of this confound — and framing SD more carefully as "scale + generative pretraining" — would strengthen the paper's causal argument.

### Minor

- **Threshold for binary mask extraction is not specified in the main text (Section 3.2).** The method describes normalizing the similarity map and "threshold the merged similarity map to produce the binary mask," but the threshold value and how it was chosen is not stated. If it was tuned against any of the five evaluation datasets, the zero-shot framing could be compromised. Even if the details are in the appendix, a brief note in the main text about whether the threshold is dataset-agnostic would address this concern.

- **Edge detection evaluation at recall ≤ 20% is non-standard and the justification is deferred entirely to the appendix.** Without the appendix, readers cannot assess whether this choice favors the proposed model. The main text should include a one-sentence rationale (e.g., that the method produces sparse, high-quality edge predictions and is being compared on precision-dominant regime), as the choice to compare at this specific threshold meaningfully affects the interpretation of the results.

### Trivial
None.

---

## Nice-to-Haves

- **Ablating pretrained vs. randomly initialized MAE** would directly isolate what generative pretraining contributes vs. "any pretraining." A randomly initialized MAE+decoder trained from scratch on Hypersim+VK2 is a missing control that would be highly informative for the core thesis.
- **Table 2 analysis deserves deeper treatment:** the paper notes that as few as 5 object classes still gives meaningful transfer. Identifying performance floors (is there a regime where generalization collapses?) would be one of the paper's most striking contributions if fleshed out.
- **The object-part compositionality observation (Fig. 3)** is suggestive and interesting; a brief quantitative check on a part-labelled subset would give it more weight.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Introduction's human-cognition analogy is unfalsifiable."** This is a motivating analogy, not a falsifiable scientific claim. Removing motivational framing is a style nitpick outside the scope of evaluation.

- **Harsh Critic: "Inter-instance separation loss is O(n·|Ω|) and may dominate training time."** The method successfully runs on dense Hypersim scenes with many small objects (the paper reports 3.7 million masks processed). If this were a practical bottleneck, the experiments would not have been feasible. The concern is speculative and not grounded in an observed failure.

- **Harsh Critic: "DINO-B failure explanation is post-hoc without experimental validation."** The paper explicitly frames this as a hypothesis: "We hypothesize this is because self-distillation... over-emphasize semantics via invariant representations." Presenting a working hypothesis alongside empirical results is standard practice; this is not a weakness.

- **Harsh Critic: "Object-part compositionality gets no quantitative treatment in main text."** The paper references "Table 7 for more examples and results." The table is in the appendix (stripped by the parser). Per review rules, missing appendix content should not be flagged.

- **Harsh Critic: "No automatic (unprompted) instance segmentation evaluation."** The paper explicitly scopes this out: "We intentionally opt not to train a separate mask decoder to showcase that our model's output features truly represent object instance shapes." This is a principled, clearly-stated methodological choice, not a gap.

- **Harsh Critic: "Hyperparameter values (λ_sep, λ_mean, bilateral filter) not reported in main text."** Appendix A.1 is referenced explicitly ("Additional details regarding models and datasets appear in Appendix A.1"). This is appendix-deferred implementation detail per the review rules.

- **Harsh Critic: "90% Hypersim sampling ratio not justified; may be tuned."** Minor implementation detail, likely in Appendix A.1.

- **Strength Finder: "Existing mask predictors finetuned from scratch fail to generalize (SimpleClick=2.4)"** — this is verifiably true and a real strength, but note that the DINO-B comparison (a separate strength claim) is partially tempered by the baseline design asymmetry discussed in Major weaknesses. The SimpleClick comparison (same backbone, same data, same prompting protocol) is clean and unambiguous and is retained.

---

## Novel Insights

The most genuinely novel observation in this work is the MAE result: a model pretrained on ImageNet-1K alone, with no text conditioning, no internet-scale data, and no exposure to animal or art imagery, generalizes to segment those domains after finetuning on synthetic furnishings and cars. This cannot be explained by data breadth and implicates the reconstruction-based generative objective specifically. Equally striking is Table 2's finding that even training on ClevrTex (simple geometric shapes) or just 5 object classes preserves meaningful zero-shot transfer — suggesting the generalization is not bottlenecked by object diversity in finetuning data. These two observations together constitute a genuine, falsifiable empirical finding about the nature of generative pretraining as a source of domain-general grouping priors.

---

## Suggestions

1. **Add a randomly-initialized MAE control.** A fresh MAE+decoder trained from scratch on Hypersim+VK2 (no generative pretraining) would cleanly isolate the pretraining contribution and directly refute the "any pretraining works" alternative.

2. **Fix the DINO-B comparison for the camera-ready.** Test fully finetuned DINO-B + randomly-initialized decoder trained from scratch, or DINO-B + fully finetuned VAE decoder. A fairer control would make the paper's causal claims much more robust.

3. **Acknowledge the SD confound explicitly.** Add a sentence in Section 4.3 or the Conclusion noting that the SD generalization results are potentially partially explained by LAION-5B data breadth, and that the MAE results provide the cleaner evidence for the generative-mechanism hypothesis.

4. **State the threshold selection procedure in the main text** (even one sentence: "a fixed threshold of X used uniformly across all datasets") to address the reproducibility concern without requiring the reader to locate an appendix.

5. **Reframe the DINO-B failure carefully.** Present the invariant/equivariant hypothesis with the explicit caveat that it is not validated by the current experimental design, and note the baseline asymmetry as a limitation. This demonstrates scientific honesty and does not diminish the paper's contribution.

---

## Assessment

**Originality:** High. The image-to-image instance coloring formulation is elegant, and the empirical discovery of category-agnostic grouping transfer from narrow generative finetuning is non-obvious and worth knowing.

**Importance:** High. Demonstrating that generative pretraining provides domain-general grouping priors opens a practical path to label-efficient instance segmentation and has implications across medical imaging, robotics, and beyond.

**Claims supported:** Mostly well-supported. The MAE results and the diversity-ablation (Table 2) are cleanly argued. The SD generalization claim has a data-breadth confound, and the DINO-B causal argument has a baseline asymmetry — both acknowledged by the paper to varying degrees but not fully resolved.

**Soundness of experiments:** Good. The evaluation protocol is appropriate (five diverse held-out domains, multiple baselines, ablation over training diversity), and the results are internally consistent. The DINO-B baseline design is the main gap.

**Clarity:** Good. The paper is well-organized and clearly written; key design choices (image-to-image framing, instance coloring loss, no mask decoder) are well-motivated.

**Value to community:** High. The findings are likely to influence both how the community thinks about generative pretraining and how it designs low-annotation segmentation systems.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>