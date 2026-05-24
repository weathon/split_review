## Summary

This paper proposes S-ViLM, a video-language pre-training framework that adds two fine-grained modeling objectives — intra-clip temporal grouping (via a cut-and-paste operation with foreground/background assignment) and inter-clip spatial grounding (via learnable group tokens aligned to noun phrases) — on top of a standard global contrastive loss. The model is evaluated on four downstream tasks (text-video retrieval, VQA, action recognition, temporal action localization) and achieves strong results, often with less pre-training data than competitors.

## Strengths

1. **Clean, well-motivated architectural design.** The two proposed components are individually simple and well-motivated: cut-and-paste creates synthetic scene changes to enable temporal grouping supervision, and learnable group tokens (borrowed from GroupViT) avoid off-the-shelf object detectors for spatial grounding. Both are integrated naturally into a dual-encoder framework.

2. **Ablation study cleanly isolates each component's contribution.** Table 6 shows that adding either spatial grounding (Scenario 2) or temporal grouping (Scenario 3) individually improves over the contrastive-only baseline across all five evaluation metrics, and the full model (Scenario 4) achieves the best scores. This is the strongest evidence that the proposed components are independently and jointly beneficial.

3. **Strong empirical results with less pre-training data.** In zero-shot text-video retrieval on MSR-VTT (Table 1), S-ViLM achieves R@1 of 28.6 using only 3.3M pairs (VideoCC+ActivityNet), surpassing methods trained on 5.5M–120M pairs. Similarly, linear probing on UCF101 (94.8%) beats MMV (91.8%) which additionally uses audio as a modality. These results demonstrate that the fine-grained objectives yield efficient representations.

4. **The temporal grouping visualization (Figure 2, left) is compelling.** The similarity matrices clearly show that the temporal-aware model produces features that are more discriminative across different scenes compared to the baseline — direct evidence that the temporal grouping loss achieves its intended effect.

## Weaknesses

### Fatal

None.

### Major

1. **The TAL evaluation uses a different model pre-trained on a much larger dataset.** Section 4.3.4 explicitly states "the model is pre-trained on HowTo100M only" for TAL, while the other three tasks use VideoCC+ActivityNet (3.3M pairs). HowTo100M contains ≈100M clips — roughly 30× more data. This means the paper does not actually evaluate a single pre-trained model on four tasks. The abstract and introduction present results as if they come from a unified model ("S-ViLM surpasses...on four representative downstream tasks"). The paper is transparent about this in the main text, but the framing is misleading, and the TAL results in Table 4 are not directly comparable to the main model used elsewhere. The ablation in Table 5 partially addresses this by showing VideoCC-only TAL results (50.5 mAP@0.5, 34.2 Avg), but these are not compared against the baselines in Table 4, and they are lower than several competitors (e.g., TSP: 51.3, 35.8; BSP: 50.9, 34.8).

2. **The spatial grounding mechanism lacks quantitative evaluation.** The claim that the inter-clip spatial grounding module "aligns group tokens with noun tokens" to capture "region-object correspondences" is supported only by a single attention-map visualization (Figure 2, right) and the ablation improvements in Table 6. While the ablation shows that adding L_g helps performance, it does not discriminate between (a) the module genuinely learning region-object correspondences and (b) it simply serving as auxiliary regularization that incidentally improves global features. Without a quantitative grounding metric (e.g., recall@k on grounded noun phrases, or performance on a region-video retrieval benchmark), the core claim about "region-object alignment" remains partially unverified.

### Minor

3. **Overclaiming in the abstract and contributions.** (a) The claim "outperforms SOTA by 3% in R@1 in zero-shot video-text retrieval" — the actual margin is 28.6 vs. MCQ's 26.0 = 2.6 absolute points. (b) The claim "5% in accuracy in action recognition on UCF101" — no single comparison in Table 3 cleanly yields 5%. The largest gain is over MCQ fine-tuning (96.5 vs. 92.3 = 4.2 points). (c) The claim that S-ViLM "consistently exceeds other self-supervised competitors" in TAL (Section 4.3.4) is inaccurate — TSP achieves higher mAP@0.75 (37.1 vs. 36.4) and higher Avg mAP (35.8 vs. 35.6) in Table 4.

4. **The ablation baseline (Scenario 1) already uses cut-and-paste.** The contrastive loss in Eq. (7) operates on blended video \(\tilde{v}_i\), meaning the "contrastive only" baseline already benefits from the synthetic scene-change data augmentation. This means the reported gains from adding L_t (temporal grouping) are incremental relative to a baseline that already has modified temporal structure. An ablation without cut-and-paste entirely would more cleanly isolate the effect of the temporal grouping component.

5. **VQA gains are modest despite the "substantial" framing.** The improvements over ALPRO are +1.4% on MSRVTT-QA and +0.5% on MSVD-QA. While positive, these are not "substantial" and the paper's language should reflect this more accurately.

### Trivial

- The "inter-clip" naming for the spatial grounding loss is slightly misleading since the loss operates on all pairs within a batch rather than on clips from different videos. "Cross-modal grounding" or "group-noun alignment" would be clearer.
- The claim about "9% improvement" in zero-shot R@10 (65.1 vs. MCQ's 56.4 = 8.7 absolute points; line 187) is roughly correct but should be stated as absolute points to avoid confusion with relative improvement.

## Nice-to-Haves

- A quantitative grounding evaluation (e.g., on ActivityNet-Entities or a region-video retrieval setup) to directly validate the region-object correspondence claim.
- Unify the pre-training data — or at minimum, directly compare the VideoCC-only TAL results against baselines in a single table.
- Add an ablation that removes cut-and-paste entirely from the baseline to measure its isolated effect.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Reviewer criticism about "inconsistent pre-training data across tasks undermines the claim of a unified model"** — Partially retained as Major Weakness 1. However, the harsh critic's framing that this is "misleading" and that the paper "should have been transparent" is softened because the paper *is* transparent about it in Section 4.3.4 (line 254-255). The retained issue is about *framing* in the abstract/introduction, not about hiding the fact.
- **Criticism that missing related works discussion is superficial** — Removed per instructions: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."
- **"Inference cost" and "limitations paragraph" suggestions** — Removed as nice-to-haves that ask the paper to address issues outside its stated scope or that are generic.
- **Strength Finder's generic strengths** (e.g., "S-ViLM introduces a novel framework," "the paper addresses an important problem") — Removed as generic/superficial. Only specific, evidence-backed strengths retained.
- **Criticism about "the spatial grounding evidence is only qualitative" being framed as "partially unverified" by the harsh critic** — Retained as Major Weakness 2, which is accurate.
- **Strength Finder's claim about "state-of-the-art results across four tasks despite substantially less data"** — Partially retained (Strength 3) but caveated: the TAL model uses HowTo100M (much larger than VideoCC), so the "less data" claim only holds for 3 of the 4 tasks.
- **Criticism about "the paper does not compare the same model across all four tasks"** — Merged into Major Weakness 1.

## Novel Insights

None beyond the paper's own contributions. The two reviewers largely agreed on the paper's strengths (clean method, strong ablations, competitive results) and converged on the same core concerns (TAL data split, lack of quantitative grounding evaluation, overclaiming). The harsh critic's detailed numerical verification of the claimed gains and the TSP comparison is genuinely useful and was not present in the strength finder's analysis.

## Suggestions

1. **Acknowledge the TAL pre-training split explicitly in the abstract and introduction.** A simple sentence like "For temporal action localization, we additionally pre-train on HowTo100M" would remove the misleading impression of a single model evaluated on four tasks.

2. **Add a quantitative grounding evaluation.** A small-scale experiment measuring grounding accuracy or region-recall on a dataset like ActivityNet-Entities (even just a few hundred examples) would significantly strengthen the claim that the spatial grounding module learns genuine region-object correspondences.

3. **Correct the imprecise numerical claims.** Replace "3%" with "2.6%" (or state as relative improvement), clarify what the "5%" on UCF101 refers to, and remove or qualify the "consistently exceeds" language for TAL.

4. **Add a "cut-and-paste-free" baseline to the ablation.** Running Scenario 1 without any cut-and-paste blending would clarify how much of the improvement comes from the data augmentation itself versus the temporal grouping loss.

5. **Directly compare the VideoCC-only TAL results against baselines in Table 4.** Even if the numbers are lower, the transparency would strengthen the paper's credibility.

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing):**
- Weak anchors (<3.5): VideoGPT+ (3.40), Emergent Corpus Pretraining (3.00), CookingCLIP (3.00), Realizing Video Summarization (2.50) — all withdrawn/rejected. S-ViLM is clearly stronger.
- Middle anchors (3.5–7.5): Grounded-VideoLLM (4.25), Enhancing Video Understanding (4.75), Retrieval-Based VLM (4.75), Understanding Long Videos (5.67), ViLMA (6.00), LanguageBind (6.50). S-ViLM sits comfortably in this band.
- Strong anchors (>7.5): Norton (8.00), Is ImageNet worth 1 video (7.60), Visual Data-Type Understanding (8.00), Compositional Entailment (8.00). S-ViLM is not at this level.

**Round 2 (Narrowing in 3.5–7.5):**
- Enhancing Video Understanding (4.75, reject) — weaker than S-ViLM; marginal improvements, unclear contributions
- ViLMA (6.00, accept poster) — comparable quality; clean benchmark contribution with some scope limitations
- LanguageBind (6.50, accept poster) — slightly stronger overall; large-scale dataset contribution, but has comparison fairness issues
- Vinoground (5.75, reject) — evaluation benchmark with some limitations that led to rejection

**Final bracket:** The paper is between 5.5 and 6.5. S-ViLM is stronger than the 4.75 rejected paper (more complete method, cleaner ablations, stronger results) and comparable to ViLMA (6.0). It sits slightly below LanguageBind (6.5) because LanguageBind's dataset contribution offsets methodology concerns, while S-ViLM's TAL data split issue is a meaningful transparency concern that prevents a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>