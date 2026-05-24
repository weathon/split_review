Now I have everything I need. Let me write the consolidated review.

## Summary

This paper introduces OmniSep, a unified framework for sound separation that handles queries from text, image, audio, and multi-modal composed queries. It proposes three key components: (1) **Query-Mixup**, a training strategy that blends query features from different modalities to enable unified multi-modal training; (2) **negative queries** with proportional weighting for suppressing unwanted sounds at test time; and (3) **Query-Aug**, a retrieval-augmented method that maps unrestricted natural language descriptions to in-domain class labels for handling out-of-domain text queries. Experiments on MUSIC and VGGSOUND-CLEAN+ demonstrate strong performance across text-, image-, and audio-queried sound separation tasks.

## Strengths

1. **First unified model across all query modalities + composed queries.** The paper presents a single architecture that handles text, image, audio, and combined multi-modal queries — something no prior method achieves. Table 1 shows OmniSep outperforms prior specialist methods across TQSS, IQSS, and AQSS simultaneously (e.g., on VGGSOUND-CLEAN+, OmniSep achieves 6.70/6.69/7.12 Mean SDR vs. best per-column baselines of 6.26/5.46/5.34). This breadth of capability is a genuine contribution.

2. **Query-Mixup is well-motivated and empirically validated.** The ablation in Table 2 directly isolates the effect of Query-Mixup: comparing #4 (text+image+audio joint training without mixup, AVG SDR 6.45) vs. #5 (with mixup, AVG SDR 6.70). The 0.25 dB gain comes with error bars, and the key insight — that mixup enables strong IQSS performance (6.69 vs. 3.53 for text-only) without sacrificing TQSS (6.70 in both #1 and #5) — is cleanly demonstrated. The UMAP visualization (Figure 3) provides mechanistic support by showing mixed embeddings lie between modality clusters.

3. **Negative query with proportional weighting is practically robust.** Figure 2 systematically compares the proposed proportional weighting (Eq. 4) against naive subtraction across 6 task–dataset combinations. The proposed method consistently dominates, and critically, its SDR varies by at most 0.45 across α ∈ [0, 2], while naive subtraction fluctuates by >2 SDR on some settings. This robustness makes the method usable without per-task hyperparameter tuning.

4. **Query-Aug effectively bridges the domain gap for unrestricted text.** Table 3 shows OmniSep+Query-Aug achieves 6.32 Mean SDR on unrestricted descriptions, only 0.38 below the in-domain label baseline (6.70), while CLIPSEP-Text collapses from 5.49 to 3.53 under the same shift. The retrieval-augmented approach is a practical solution to a real limitation of existing text-queried separation models.

## Weaknesses

### Fatal
None.

### Major

1. **The SOTA claim is confounded by the backbone choice.** The main comparison (Table 1) pits OmniSep (using frozen **ImageBind**) against baselines using CLIP (CLIPSEP variants) or BERT (BERTSep). ImageBind is a more recent, more powerful multi-modal encoder, so the reported 0.4–4.3 dB SDR gains cannot be cleanly attributed to the proposed framework components. The Table 2 ablation does control for backbone (all entries use ImageBind), which validates Query-Mixup within the same backbone — but the headline SOTA comparisons remain confounded. The paper should either retrain OmniSep with CLIP features or augment CLIPSEP baselines with ImageBind. This does not invalidate the paper, but it undercuts the strongest claim ("state-of-the-art") as currently presented.

2. **The selection of α=0.5 for negative queries is not justified.** The paper states "All +NQ results are outcomes when α=0.5" but does not explain how this value was chosen — whether from a held-out validation set or from inspecting test-set performance. The robustness analysis (Figure 2) somewhat mitigates this, showing the proposed method is stable across α values. However, without a clear selection protocol, the comparisons in Table 1 (where +NQ shows gains of 0.10–1.60 dB) lack full evidential rigor. The paper should clarify the selection procedure or cross-validate α.

3. **The "open-vocabulary" framing is overstated.** Query-Aug retrieves the most similar in-domain class label from a predefined set and uses that label's query as a proxy. The model never handles truly novel sound concepts; it is bounded by the training label set. The evaluation (Table 3) tests only GPT-rewrites of the *same class labels* — this tests paraphrasing robustness, not open-vocabulary generalization to genuinely out-of-domain categories (e.g., abstract sounds like "pop music," which the Limitations section acknowledges but does not evaluate). This framing should be recalibrated (e.g., "retrieval-augmented closed-vocabulary" or "expanded-vocabulary").

### Minor

1. **No comparison against key contemporary methods cited in the paper itself.** The paper cites GASS (pons2024gass) and MixIT (wisdom2020unsupervised) in the related work but does not include them in main results. Given that the field is moving quickly and the paper claims state-of-the-art, comparing against these directly related methods would strengthen the evaluation.

2. **The Query-Aug result (#11 surpasses #6) lacks explanatory analysis.** OmniSep+Query-Aug achieves 6.32 Mean SDR on unrestricted descriptions, surpassing the in-domain labeled baseline CLIPSEP-Text at 5.49. This is a striking result that merits deeper investigation: what fraction of descriptions are mapped to the correct class? Does Query-Aug sometimes select a *better* query than the original class label? Without this analysis, the reader cannot assess whether the reported number reflects a genuine advantage or a quirk of the retrieval mapping.

3. **The ablation does not test composed queries without Query-Mixup.** The paper claims that Query-Mixup "forms the basis of composed-query and negative query capabilities" (Section 5.4). However, no experiment trains OmniSep without Query-Mixup (alternating modality batches, as in CLIPSEP) and evaluates on composed queries. This causal claim is supported only by the UMAP visualization and by the fact that #5 handles composed queries while #4 does not — but #4 is never evaluated on composed queries in the tables. This would be a straightforward and informative missing ablation.

### Trivial
None.

## Nice-to-Haves
- Add an ablation replacing ImageBind with CLIP (or vice versa for baselines) to directly isolate framework gains from backbone effects.
- Include a table showing what fraction of GPT-rewritten descriptions are mapped to their "correct" class via Query-Aug.
- Report composed-query performance for a model trained without Query-Mixup to directly test the claimed causal link.

## Removed Points

These points were identified by the reviewers but removed after verification against the paper. Treat them with caution if encountered elsewhere.

1. **"The ablation does not include error bars or standard deviations."** — Factually wrong. Table 2 (lines 205–209) clearly shows every entry has ± standard deviation values (e.g., "6.70±0.66", "6.33±0.68"). This criticism was based on misreading the table.

2. **"Missing related works"** — Removed per instruction: I cannot independently verify the existence of works not cited by the paper. The paper's related work section covers CLIPSEP, i-Query, AudioSEP, MixIT, GASS, and others appropriately.

3. **"Parser-stripped appendix contents"** — Any criticism about missing details in the appendix (e.g., query set construction details) is not actionable since the appendix was stripped by the parser. The original submission contains these details.

4. **"Formatting/style nitpicks"** — Removed as parser artifacts, not author errors.

5. **"The UMAP visualization is geometrically trivial"** — While not surprising, the visualization is useful exposition and does not harm the paper.

6. **"#5 achieves the same TQSS as #1, suggesting Query-Mixup doesn't help TQSS"** — This is not a weakness; it is a desired property. Query-Mixup matches the text-only specialist while enabling strong IQSS/AQSS, demonstrating it resolves the training-objective instability without sacrificing single-modal performance.

## Novel Insights

The most interesting tension in the reviews concerns the backbone confound issue. This paper's reliance on ImageBind (vs. baselines' CLIP) mirrors a pattern seen in the FlowBind review, where frozen pre-trained backbones obscure the true contribution of the proposed framework. In both cases, the actual methodological novelty is real but the headline comparisons are weakened. For OmniSep specifically, the within-backbone ablation (Table 2) successfully isolates the proposed components, but the authors chose to lead with a between-backbone SOTA claim. A cleaner separation — "here is what the framework adds, same backbone" vs. "here is what ImageBind enables" — would strengthen the contribution narrative considerably.

## Suggestions

1. Re-run the main comparison (Table 1) with OmniSep trained using CLIP instead of ImageBind, or equivalently, augment the CLIPSEP baselines with ImageBind. This directly addresses the backbone confound and would make the SOTA claim bulletproof.

2. Clarify how α=0.5 was selected for the negative query results — specify whether it was chosen on a held-out validation set, and if so, report the validation performance. Alternatively, since Figure 2 shows the method is robust across α, report results for a range (e.g., α ∈ {0.3, 0.5, 0.7}) to demonstrate the conclusion is not sensitive to the specific value.

3. Replace "open-vocabulary" with a more precise term such as "retrieval-augmented vocabulary expansion" and include a small experiment with genuinely out-of-domain queries (e.g., abstract sounds not in VGGSOUND's label set) with an analysis of retrieval failures to set realistic expectations.

4. Add an experiment where a model is trained without Query-Mixup (alternating modality batches, as in CLIPSEP) and evaluated on composed queries. This would directly test the causal claim that Query-Mixup enables composed-query capabilities.

5. Add an analysis of Query-Aug retrieval accuracy — what fraction of GPT-rewrites are mapped to the correct class label? This would help explain why OmniSep+Query-Aug (#11) outperforms the in-domain baseline (#6).

## Score and Decision

Round 1 bracket: I placed this paper between 4.0 and 6.5 based on initial calibration against weak anchors (scores 2.0–3.0), mid anchors (MARS-Sep 5.50, AlignSep 4.80, CodecSep 4.00), and strong anchors (8.0 from different domains).

Round 2 narrowing: I retrieved anchors in [4.5, 6.5] and [5.0, 7.0]. The most relevant comparisons are:

| Anchor | Avg Score | Round | Comparison to OmniSep |
|--------|-----------|-------|----------------------|
| MARS-Sep | 5.50 (Accept) | R1/R2 | Directly comparable: both do multi-modal sound separation. MARS-Sep has more novel method (RL), OmniSep has broader task coverage. Similar evaluation scope limitations. OmniSep is slightly weaker due to backbone confound issue. |
| AlignSep | 4.80 (Accept) | R1/R2 | Focuses on video-queried separation only. Had overclaiming issues similar to OmniSep's "open-vocabulary." OmniSep's broader task scope makes it marginally stronger. |
| CodecSep | 4.00 (Reject) | R1 | Efficiency-focused with novelty concerns. OmniSep is clearly stronger. |
| FlowBind | 6.00 (Accept) | R2 | Similar frozen-backbone confound issue but more novel framework and stronger efficiency. OmniSep is weaker. |
| OmniCVR | 5.00 (Accept) | R2 | Benchmark paper with mixed reviews. OmniSep as a methods paper is comparable in quality. |
| UALM | 6.00 (Accept) | R2 | Broad audio language model unification. Different scope; higher novelty and stronger evaluation. OmniSep is weaker. |

I place OmniSep between AlignSep (4.80) and MARS-Sep (5.50) — closer to MARS-Sep given the broader task coverage and cleaner ablations, but pulled slightly down by the unresolved backbone confound. The paper has real contributions that would be publishable with revisions, but the SOTA claim needs stronger isolation from the backbone choice.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>