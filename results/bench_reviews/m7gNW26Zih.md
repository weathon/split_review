## Summary

This paper presents a system for language-based audio retrieval on the CLOTHO dataset that combines (1) soft-label distillation from a pretrained teacher ensemble (adopted from Primus et al., 2024), (2) LLM-driven caption augmentation via GPT-4o, and (3) a novel cluster-guided auxiliary classification task using BERTopic-derived pseudo-labels. The best single model reaches 46.6 mAP@16, and a weighted ensemble of system variants attains 48.8 mAP@16 on the development test split. The paper acknowledges that cluster guidance yields mixed gains across backbones but claims ablations show consistent improvements under high correspondence ambiguity.

## Strengths

- **Soft-label distillation delivers substantial, consistent gains.** Across all three audio backbones (PaSST, EAT, BEATs), adding distillation (SID 1 → SID 2) improves mAP@16 by 4–6 points: PaSST 42.08 → 46.62, EAT 40.41 → 45.35, BEATs 38.12 → 43.89 (Table 2). This is the strongest empirical result in the paper.

- **The LLM augmentation pipeline is concretely described.** The combination of back-translation and LLM-mix (mixing two audio signals and using GPT-4o to merge captions, generating 50,000 synthetic pairs) is explained with sufficient detail for others to adapt the recipe, even if GPT-4o itself is closed. Augmentation adds modest but measurable gains (e.g., EAT SID 2 → SID 3: mAP@16 45.35 → 46.05).

- **Three diverse audio backbones are evaluated.** Testing PaSST (supervised AudioSet pretraining), EAT, and BEATs (both self-supervised) provides a reasonable assessment of method generality across architectures.

## Weaknesses

### Fatal

None.

### Major

- **No comparison to any external baseline.** The paper reports only its own system variants. Numbers like mAP@16 46.6 (single model) and 48.8 (ensemble) cannot be contextualized without comparison to published CLOTHO results — from DCASE 2024 Task 8 entries, Primus et al. (2024), or prior dual-encoder baselines. The reader cannot judge whether these represent meaningful progress over the state of the art.

- **Claimed ablations and subset analyses are absent from the paper.** The abstract states "ablations indicate consistent improvements under high correspondence ambiguity" (line 17) and the contributions list promises "thorough ablations on topic granularity and teacher softness" (lines 37–38). Yet the paper contains only one results table (Table 2) with no ablation study, no analysis of different cluster granularities, no teacher-softness sweep, and no subset evaluation on ambiguous cases. These are claimed as contributions but not supported by presented evidence.

- **Cluster guidance — the paper's one novel component — does not deliver consistent gains.** For PaSST, adding cluster supervision (SID 4/5) to the best distillation+augmentation configuration (SID 3) yields mAP@16 of 46.39/46.50 vs. 46.41 — effectively flat, and below the best non-cluster configuration (SID 2: 46.62). For EAT, cluster guidance reduces performance (SID 3: 46.05 → SID 4: 45.34). For BEATs, SID 5 drops below even SID 2. The paper itself acknowledges "mixed gains" in the abstract, but then overclaims by asserting consistent improvements under ambiguity without evidence.

- **Potential data leakage from clustering.** Section 2.3 states clustering was performed "on all captions in the CLOTHO dataset" (line 170). It is never clarified whether this includes test-set captions. If test captions were used to derive cluster pseudo-labels that then supervised the audio encoder during re-finetuning, the reported retrieval numbers would be invalid.

### Minor

- **Teacher ensemble composition is unspecified.** The paper states soft labels come from "averaging similarities from three audio models" (line 380) but never names which models, their training data, or whether they were frozen during student training. This matters for both reproducibility and fairness (could the teachers have been exposed to test-relevant data?).

- **No statistical validation.** All results are single-point estimates. While this is common in large-scale retrieval benchmarks, coupled with the grid-searched ensemble weights on a single validation split, there is a non-trivial risk of overfitting to this particular split.

- **Reliance on closed GPT-4o for augmentation** limits full reproducibility by others without API access. The paper acknowledges this limitation (line 430) but does not provide open alternatives.

### Trivial

- Table 2 has garbled column headers ("Multiple annotation / Single annotation" with duplicate mAP@10 columns) making interpretation needlessly difficult.

## Nice-to-Haves

- A negative control for cluster guidance (e.g., random cluster labels) would establish whether the auxiliary task provides signal beyond a regularization effect.
- Sensitivity analysis on the number of clusters and the auxiliary loss weight λ₂.
- Subset evaluation isolating captions with high correspondence ambiguity to substantiate the abstract's central claim.
- Replacement of GPT-4o with an open-source LLM for fully reproducible augmentation.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

**From Harsh Critic — removed:**
- *"This alone invalidates the paper's main empirical claim"* — while the lack of external baselines is a real weakness, absolute numbers can be contextualized against published leaderboards; this framing is excessive.
- *"The improvement of SID 2 over SID 1 could reflect random variation"* — the 4–6 point mAP@16 gap across all three backbones is too large and consistent to attribute to random variation, even without error bars.
- *"Training details are underspecified: warmup strategy and stopping criteria are absent"* — the paper provides batch sizes, learning rate schedules with range (2e-5 to 1e-7), epoch counts, and optimizer; this is sufficient for the field's standard. Moved from weakness to removed.
- *"The distillation loss is a direct re-implementation of Primus et al.'s approach"* — this is not a weakness; the paper explicitly cites and credits Primus et al. (2024) for the distillation method (line 111–112).

**From Strength Finder — removed:**
- *"Rigorous ablations on topic granularity and teacher softness... show the method consistently helps under high correspondence ambiguity"* — these ablations do not appear anywhere in the paper. This claimed strength is fabricated.
- *"Reproducible LLM-based augmentation"* — GPT-4o is closed; the paper itself acknowledges this as a limitation. Not reproducible in the full sense.
- *"Detailed, reproducible training protocol"* — overstated given missing teacher model details.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface observations about the work that the authors had not already made or acknowledged (e.g., the paper already admits mixed cluster-guidance gains).

## Suggestions

- Add comparisons to published CLOTHO results (DCASE 2024 Task 8 entries, Primus et al. 2024, Koepke et al. 2022) to allow readers to contextualize the reported numbers.
- Either present the claimed ablations on topic granularity, teacher softness, and high-ambiguity subsets — or remove these claims from the abstract and contributions list.
- Clarify whether clustering was confined strictly to the training split. If test captions were included, re-run with training-only clustering and report corrected numbers.
- Specify the three teacher models used for distillation (architecture, pretraining data, frozen/updated status).
- Add a negative control using random cluster assignments to isolate whether the cluster auxiliary task contributes any signal.

---

**Anchor comparisons used for calibration:**

| Path | Paper | Avg Score | Comparison |
|------|-------|-----------|------------|
| `cFhcd4WGjO.md` | DART: Dual-Level Optimal Transport for Audio-Text Retrieval | 5.50 (Accept) | DART has stronger theoretical contribution, SOTA results, generalizes to image-text. Current paper is clearly below. |
| `KxxR7emO5K.md` | OmniCVR: Omni-Composed Video Retrieval Benchmark | 5.00 (Accept) | Strong benchmark contribution. Current paper is below. |
| `LXTf8GUg8f.md` | SPEAR: Unified SSL for Speech and Audio | 5.00 (Reject) | Genuine architectural novelty. Current paper is below. |
| `Me4AON8160.md` | Multimodal Dataset Distillation via Phased Teacher Models | 4.50 (Accept) | Novel phased distillation framework. Current paper is below. |
| `3q3LnQ63Az.md` | Fine-grained Audio Captioning with Multimodal Fusion | 4.50 (Withdrawn) | Similar LLM-pipeline pattern with limited novelty. Current paper is comparable. |
| `0wwcANeTjd.md` | Variable-Length Audio Fingerprinting | 4.00 (Reject) | Novel method but split reviews. Current paper is comparable. |
| `2YSqaj725G.md` | Revisiting Audio-Language Pretraining | 3.50 (Reject) | Thorough empirical study but no new method. Current paper has more novelty (cluster guidance is genuinely new) but weaker evaluation. Slightly above. |
| `kylhUNRXyt.md` | Speech-CLAP | 2.50 (Reject) | Unfair baselines, circular evaluation. Current paper is clearly above. |

The paper has real empirical contributions (distillation delivers large, consistent gains across backbones; ensemble results are strong), but the one novel method (cluster guidance) does not deliver, the evaluation lacks external context, and claimed ablations are absent. It sits between the clearly rejected papers (2.50–3.50) and the accepted papers (4.50–5.50).

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>