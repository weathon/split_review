Now I have all the information needed to synthesize the final review. Let me carefully construct it.

## Summary

The paper proposes InstructDET, a data-centric pipeline that leverages foundation models (LLaVA, LLaMA) to automatically generate diverse, human-like referring expressions for object detection from images with bounding boxes. The resulting InDET dataset contains 3.6M instructions across 120.6K images, covering six categories of user intentions — far broader than existing REC datasets. The authors train a conventional DETR-based ROD model (DROD) on this data and evaluate it on both standard REC benchmarks and the InDET test set.

## Strengths

- **Novel data generation pipeline using foundation models.** The paper introduces a two-pipeline approach (global prompt via LLaMA text-only, local prompt via finetuned LLaVA with visual bbx input) to generate diverse referring expressions. This is a practical and well-motivated use of VLMs and LLMs for data augmentation in visual grounding, and the multi-object expression generation via semantic clustering and LLM summarization (G5–G6) is a genuinely new contribution beyond existing single-object REC datasets.

- **Large-scale, more diverse instruction dataset.** InDET comprises 3.6M instructions with 63k vocabulary, spanning all six guideline groups. The analysis (Fig. 3) convincingly shows that existing datasets concentrate on G1–G2, while InDET distributes across all groups, making it a useful resource for the community.

- **InDET training improves logic reasoning in existing models (Fig. 4).** When MDETR, Grounding-DINO, and UNINEXT are each trained with the same architecture but different datasets (RefCOCO, Flickr, or InDET), the InDET-trained variants consistently outperform on a 2k logic-reasoning test set. This is a fair, controlled experiment that isolates the value of the data, independent of model architecture — and it directly supports the paper's core thesis.

- **CLIP-based filtering with local enhancement score.** The paper designs a thoughtful filtering mechanism (Eq. 1) that uses a local enhancement score $S_e = S_l - S_g$ to reject hallucinated or globally-descriptive instructions, going beyond simple CLIP matching.

## Weaknesses

### Major

1. **The InDET test set comparison (Table 1) is an unfair comparison presented without sufficient caveat.** DROD was trained on InDET's training split; the baselines (MDETR, G-DINO, UNINEXT) were trained on entirely different data (RefCOCO, GoldG, CC, O365, etc.). The large gap (62.24 vs. 43.37 AP) is therefore primarily a data-distribution effect, not evidence that the DROD model architecture or training method is superior. The paper's language — "our DROD largely surpasses UNINEXT" and the abstract claim of "surpasses existing methods on both standard REC datasets and our InDET test set" — conflates this biased comparison with the fair one. The InDET test is useful as a sanity check that the model has learned the generated data, but it should not be presented as evidence of superiority over methods that have never seen InDET data.

2. **No human evaluation of generated instruction quality.** For a dataset paper whose primary contribution is 3.6M automatically generated instructions, the lack of human validation is a significant gap. The pipeline involves multiple stages (LLaVA description, LLaMA generation, CLIP filtering, synonymous rewriting) where hallucinations, object confusions, or nonsensical outputs can arise. The paper reports quantity, vocabulary size, and CLIP embedding diversity, but never validates whether even a small sample of instructions are factually grounded in the image, correctly describe the target object, or are naturally phrased. The CLIP filter rate and its precision/recall are also unreported. Without this, the reader cannot assess whether the dataset is clean or noisy — which matters because noisy data could inflate or harm performance in hard-to-predict ways.

3. **Gains on standard benchmarks are modest given the scale of additional data.** On RefCOCO/+/g (Table 2), DROD improves over UNINEXT by roughly 1–2 AP points on most splits (e.g., RefCOCO val: 88.92 vs. 87.64). Given that DROD is trained on InDET (3.6M instructions) in addition to O365 and CC — orders of magnitude more instruction data than UNINEXT's training set — these single-digit improvements suggest either that the benchmarks are near saturation or that the added diversity in InDET does not translate strongly to these standard distributions. The paper's framing ("surpasses existing methods with large margins" is implied) does not adequately acknowledge this.

### Minor

4. **The shuffled-expression experiment interpretation is ambiguous.** The paper claims that a larger performance drop on shuffled instructions indicates "better comprehension of instruction meaning." An equally plausible alternative is that a model with more exposure to natural syntactic patterns (DROD was trained on many more instructions) has overfit to those patterns, so breaking them causes a larger drop. Robust semantic comprehension could manifest as *less* disruption from word-order changes. The paper does not rule out this alternative, weakening the conclusion.

5. **LLaMA-based guideline assignment for G1–G6 is unvalidated.** The paper uses LLaMA with in-context learning to assign instructions to six groups, then uses per-group breakdowns (Table 1) to interpret model behavior. There is no reported accuracy or human agreement for this assignment. If misclassifications are systematic, the per-group analysis could be misleading (e.g., inflating G6 performance by including simpler instructions).

6. **No variance or confidence intervals reported.** Tables 1 and 2 report single runs without standard deviations or error bars. Many comparisons differ by fractions of a point; without variance estimates, statistical significance cannot be assessed.

### Trivial

7. **The "in-the-wild" scalability claim is forward-looking and unsupported.** The introduction states the method "can automatically expand training data by using in-the-wild images with object bbxs," but all experiments use only COCO, Flickr, and Objects365 images. This is a reasonable future direction but not a demonstrated capability.

## Nice-to-Haves

- Human evaluation of instruction quality on a sample of 200–500 instructions (correctness, naturalness, relevance to target object) would substantially increase confidence in the dataset.
- Retraining at least one baseline method (e.g., UNINEXT) on InDET's training data to enable a fair comparison on the InDET test set would cleanly separate the data contribution from unfair distributional advantages.
- An ablation study training the DROD model on a random subset of InDET of size comparable to existing REC datasets (e.g., ~100K instructions) would help separate the benefit of data *diversity* from the benefit of sheer data *scale*.

## Removed Points

- **"The central empirical claim is biased in the paper's favor" (Critic's Issue 1 fully)** — This is kept in Major Weakness #1 above, but the critic's framing as a "fatal" issue is downgraded. The paper's core contribution (the pipeline and dataset) is not invalidated; only the specific InDET test comparison and its framing are problematic. The standard benchmark results and Fig. 4 provide fair evidence.
- **"Model is architecturally standard"** — The paper openly states it uses a "conventional ROD model" and makes no architectural novelty claim. This is not a weakness for a data-centric paper.
- **"InDET results carry equal weight" framing** — The abstract mentions both evaluations; the critic's concern about conflation is noted but the paper does separate the two evaluations into different tables with different caveats (Table 2 specifies training data, Table 1 does not but context makes it clear). This is addressed by Weakness #1.
- **Strength Finder Strength 1 (InDET gains)** — Removed because it conflicts with verified Weakness #1 (unfair comparison).
- **Strength Finder Strength 2 (shuffle comprehension)** — Removed because it conflicts with verified Weakness #4 (ambiguous interpretation).
- **Strength Finder Strength 5 (in-the-wild scalability)** — Removed because the claim is not experimentally supported (Weakness #7).

## Novel Insights

None beyond the paper's own contributions. The core observation — that foundation models can be used to generate diverse referring expressions beyond existing REC datasets — is well-motivated, and the specific pipeline design (dual-pipeline generation + CLIP local-enhancement filtering + multi-object semantic clustering) is the paper's main methodological contribution.

## Suggestions

1. **Add a human evaluation study** of generated instruction quality on 200–500 samples, reporting correctness, hallucination rate, and naturalness. This is the single most impactful addition for establishing dataset credibility.
2. **Retrain at least one baseline on InDET** and report results on the InDET test set to enable a fair comparison. Alternatively, reframe Table 1 as "evaluating whether the model has learned the InDET distribution" rather than as a method comparison.
3. **Tone down claims** in the abstract and introduction about "largely surpassing" existing methods — qualify the scale and the nature of the comparison (standard benchmarks vs. InDET test).
4. **Report variance** across at least 3 runs for the main results.
5. **Abandon or reinterpret** the shuffle experiment, or add a control experiment where instructions are paraphrased (preserving meaning but changing syntax) rather than randomly shuffled.
6. **Validate the LLaMA-based guideline assignment** by reporting human agreement on a sample.

## Score and Decision

**Originality:** 6/10 — The data pipeline is novel, but the model architecture is standard and the overall approach (use foundation models for data generation) is timely rather than surprising.

**Importance:** 7/10 — Diversifying REC data is a real problem; the dataset and pipeline could be practically useful to the community.

**Claims support:** 4/10 — The strongest claimed result (InDET test) rests on an unfair comparison; the fair comparison shows modest gains. The shuffle experiment's interpretation is unsupported. No human evaluation validates dataset quality.

**Soundness:** 5/10 — The pipeline is well-designed and the logic-reasoning experiment (Fig. 4) is sound, but the central evidence for the method's value has significant gaps.

**Clarity:** 6/10 — The paper is generally readable but conflates evaluations and overstates results.

**Value:** 6/10 — The dataset and pipeline are potentially valuable, but the lack of quality validation limits immediate usefulness.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>