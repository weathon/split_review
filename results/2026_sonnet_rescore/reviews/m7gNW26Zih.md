## Summary
The paper presents a language-based audio retrieval system built on a dual-encoder contrastive learning framework, combining (i) soft-label distillation from an ensemble of pretrained audio-text models, (ii) LLM-driven caption augmentation (back-translation and LLM-based caption mixing), and (iii) a cluster-guided auxiliary classification head. The system was submitted to DCASE 2024 Task 8 and is evaluated solely on the CLOTHO dataset, reaching mAP@16 46.6 for the best single model and 48.8 with a weighted ensemble on the development test split.

---

## Strengths

- **Soft-label distillation produces large, consistent gains across all audio backbones.** Table 2 (SID 1 → SID 2) shows mAP@16 improving from 42.08 → 46.62 (PaSST), 40.41 → 45.35 (EAT), and 38.12 → 43.89 (BEATs), uniformly supporting the claim that soft targets address non-binary correspondences better than hard binary supervision. This is the paper's clearest and most credible finding.

- **Systematic ablation across three audio backbones and five system configurations.** Tables 1 and 2 together allow clear attribution of contributions to distillation, augmentation, and clustering independently, with three backbone models tested, providing a broader picture than single-model ablations.

- **Weighted ensemble provides a substantial and consistent improvement.** The E1–E4 ensembles in Table 2 achieve mAP@16 48.78–48.83, compared to the best single model's 46.62, demonstrating the practical value of ensembling heterogeneous system configurations.

---

## Weaknesses

### Fatal
None.

### Major

- **The conclusion directly misrepresents the ablation results.** Section 5 states that clustering "contributed to additional performance gains," but Table 2 contradicts this on the primary metric for the strongest backbone: PaSST mAP@16 peaks at SID 2 (46.62), then decreases at SID 3 (46.41), SID 4 (46.39), and SID 5 (46.50). EAT shows a modest uptick from SID 2 → SID 3 (45.35 → 46.05) but then falls back at SID 4 and 5. The abstract does acknowledge "mixed gains across backbones," making the unqualified conclusion statement a clear overstatement of the evidence. This is not a speculative gap—Table 2 is in the paper and the numbers are plain.

- **No comparison to any external published system.** The results section consists entirely of ablations among the authors' own system variants. CLOTHO is a well-studied benchmark with multiple published systems, yet the reader is given no anchor to assess whether mAP@16 46.6 or 48.8 is competitive, average, or below state-of-the-art. For a research contribution at a top venue, this is a critical omission. Without at minimum a comparison to the Primus et al. 2024 system (from which the distillation loss was directly adopted), the contribution cannot be contextualized.

- **Large unexplained development-to-evaluation performance drop.** Section 4 reports mAP@16 48.83 on the development test split, then states the final evaluation result is mAP@16 = 0.421 (42.1 on the same scale) — a roughly 6–7 point drop with no discussion whatsoever. Given that all hyperparameters, including the ensemble weights from grid search (Table 3), were tuned on the development split, this gap raises serious concerns about overfitting to the development test set. The paper ignores this entirely.

- **The novel component (cluster-guided classification) does not reliably improve the primary metric.** As documented in Table 2, the cluster guidance in SID 4 and SID 5 fails to improve over SID 3 for any backbone on mAP@16. The distillation and augmentation components are credited to Primus et al. 2024 and Wu et al. 2024 respectively. Given that the only original architectural element does not deliver consistent improvements, the paper's contribution relative to prior work is narrow.

### Minor

- **The abstract's claim that techniques improve robustness "under high correspondence ambiguity" is not operationalized.** The phrase "ablations indicate consistent improvements under high correspondence ambiguity" appears in the abstract but is never defined, measured, or linked to a specific subset of the evaluation. No analysis of high-ambiguity instances vs. low-ambiguity instances is presented anywhere in the paper, making this a speculative framing presented as a supported finding.

- **Hyperparameter choices for the cluster component (λ₂ = 0.05, number of clusters) are stated but not ablated.** Section 2.3 fixes λ₂ = 0.05 and Section 3.4 describes two cluster sources without any justification or sensitivity analysis. Given that clustering is framed as a novel contribution, even a small ablation on these values would be appropriate.

### Trivial

- **The comparison between SID 4 (finetuned model clusters) and SID 5 (BERTopic/e5-large-v2 clusters) is presented as two configurations but the results are nearly identical across all backbones**, with no principled discussion of why either source should be preferred. This conflates ablation with exploration without drawing any conclusions.

---

## Nice-to-Haves

- A targeted analysis of whether cluster-guided supervision improves retrieval *specifically on audio-caption pairs with high semantic overlap* across recordings would substantiate the paper's stated motivation more directly. CLOTHO's five captions per recording provide a natural basis for identifying high-ambiguity instances.
- An ablation on the number of clusters for the BERTopic variant would clarify the sensitivity of the cluster-guidance component.
- A comparison to the baseline Primus et al. 2024 system — from which distillation was directly adapted — would establish the incremental contribution of the augmentation and clustering components beyond that prior work.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: λ = 1.0 for distillation is not ablated.** While noting this lack of ablation is technically correct, this is a trivial design choice for a fixed hyperparameter inherited from prior work. Removed as a standalone weakness.

- **Harsh Critic: Section 2.2 is "entirely from Primus et al. 2024."** The paper explicitly credits the technique ("we adopted a distillation loss approach from...") and the equations are provided for completeness/reproducibility. Presenting prior work's equations to enable reproducibility is standard practice and is not a weakness. Removed.

- **Harsh Critic: Three-stage training pipeline overfitting risk in Section 3.4.** The concern about re-finetuning on CLOTHO for 20 epochs is valid but is subsumed within the "dev-to-eval gap" Major weakness above; raised separately it would double-count the same problem.

- **Harsh Critic: "This is a structural coherence problem, not an evidential one... it cannot be fixed by adding experiments."** The framing as Fatal/structural is too strong. The conclusion is inaccurately written, but the results themselves are reported honestly in Table 2. This is a Major claim accuracy problem, not a fatal design flaw. Demoted to Major accordingly.

- **Strength Finder: Systematic ablation as a strong selling point.** While the ablation is methodical, "systematic ablation" is somewhat generic as a strength and the ablations are limited to a single dataset. Kept but as a supporting observation rather than a headline strength.

---

## Novel Insights

None beyond the paper's own contributions. The paper's primary finding — that soft-label distillation from an ensemble of pretrained models produces large and consistent gains — is both well-known in the distillation literature and directly borrowed from Primus et al. 2024. The cluster-guidance idea is genuinely novel in this context, but the evidence for its utility is too mixed and insufficiently analyzed to constitute a solid new insight. The reviewers collectively surface that the contribution is essentially a competition system write-up with one undervalidated novel component.

---

## Suggestions

1. **Rewrite the conclusion** to accurately reflect Table 2: acknowledge that cluster guidance showed mixed and largely null effects on mAP@16, and that the major driver of improvement was soft-label distillation (SID 1→2).
2. **Add at least one external baseline** — ideally the Primus et al. 2024 system that provided the core distillation loss — so that the reported numbers can be situated within the literature.
3. **Analyze the 6–7 point development-to-evaluation drop** explicitly; discuss whether ensemble weight grid search on the development test split inflated development-set results and how this affects interpretation.
4. **Provide a targeted analysis of high-ambiguity pairs** to substantiate the claim that cluster guidance helps specifically in cases of non-binary correspondences — or remove that claim from the abstract.
5. **Ablate λ₂ and the number of clusters** to assess the robustness of the cluster-guidance component.

---

## Evaluation Along Key Axes

- **Originality:** Low. The main techniques (distillation, back-translation, LLM mix) are directly imported from prior work. The cluster-guided head is the only original element.
- **Importance of research question:** Moderate. Audio-text retrieval under non-binary correspondences is a relevant open problem.
- **Claims supported:** Poor. The conclusion overstates the clustering contribution against the evidence in Table 2; an abstract claim about high-ambiguity improvements is unsubstantiated.
- **Soundness of experiments:** Moderate. Ablations are systematic but conducted on a single dataset, with no external baselines and an unexplained dev-eval gap.
- **Clarity of writing:** Adequate but contains a significant inconsistency between Table 2 and the conclusion.
- **Value to the research community:** Limited in the current form; the distillation finding may be of modest interest, but the paper reads primarily as a competition system description.

---

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>1</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>2</community_value>
</subscores>