Now I have a thorough understanding of the paper and can verify each claim. Let me compose the final consolidated review.

---

## Summary

This paper proposes LaTable, a diffusion-based generative model designed to be trained across heterogeneous tabular datasets. The key architectural innovations are: (1) an encoder-only transformer without positional encodings to handle variable-length inputs and achieve column-order equivariance, (2) pretrained LLM embeddings for dataset descriptions, column names, and categorical values to leverage semantic similarities across tables, and (3) a mixed-type diffusion framework that handles both numerical and categorical variables. The model is trained jointly on 78 curated datasets from OpenML. Experiments show that LaTable significantly outperforms single-dataset baselines (TVAE, CTGAN, TabDDPM, ARF) on in-distribution generation and, when finetuned on a few samples, generates better out-of-distribution data than baselines trained from scratch. The paper also honestly documents LaTable's poor zero-shot performance and discusses the data quality challenges ahead.

## Strengths

- **Cross-dataset training with column-order equivariance**: The architecture directly satisfies desiderata D1 and D4 — no positional encodings plus separate feature-name embeddings enable variable-length, permutation-invariant generation. This is a principled design that distinguishes LaTable from all single-dataset baselines (Sec. 3.3.1, 3.3.2).

- **Significant in-distribution gains over single-dataset baselines**: Table 1 shows LaTable achieves density 0.865 (vs. 0.700 for next-best ARF), coverage 0.900 (vs. 0.832), and downstream AUC 0.874 (vs. 0.853). The gains are especially pronounced on small datasets (Fig. 1), providing concrete evidence that cross-dataset training transfers generation capabilities.

- **Few-shot OOD generation outperforms baselines trained from scratch**: Figure 2 shows finetuned LaTable attains density near 1.0 (on par with real data) and coverage exceeding both real data and all baselines with tens of samples. This directly validates the claim that pretraining enables sample-efficient adaptation to unseen datasets.

- **Honest diagnostic of zero-shot limitations with actionable insight**: Section 5 explicitly identifies that poor zero-shot performance stems from OOD features not covered in pretraining, and demonstrates that naive scaling to larger metadatasets (WikiTables, 100k+ tables) does not improve zero-shot generation. This negative result is valuable for the community, pointing toward data quality and curation rather than scale alone.

- **Principled handling of categorical variables using LLM embeddings**: Categories are embedded as "[column name] is [category]" strings via a frozen LLM encoder, with an attention-like probability mapping (Eq. 3) supporting variable-size category sets. This avoids learning per-category embeddings from scratch and leverages semantic similarities across tables (Sec. 3.3.2).

- **Thorough multi-metric evaluation**: The paper uses downstream AUC, density, coverage, precision, and recall, providing a multi-faceted view of generation quality beyond a single metric (Table 1, Figs. 1–2).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No comparison to language-model–based tabular generators (GReaT, Tabula, Realtabformer).** The paper discusses LM-based approaches in the related work (Sec. 2) and argues they have disadvantages (autoregressive tokenization of numbers, poor modeling of continuous distributions, expense). Yet the experimental evaluation only compares against non-LM baselines (TVAE, CTGAN, TabDDPM, ARF). While these LM methods are also single-dataset approaches (the paper's core claim is about cross-dataset training, not beating LMs per se), including at least one LM baseline would make the evaluation more complete and directly support the claim that LaTable's design choices are beneficial. The absence is a gap, though not a fatal one — the paper already shows strong results against competitive non-LM single-dataset baselines.

- **Zero-shot performance is discussed qualitatively but not quantified.** The paper (Sec. 4.2, Sec. 5) states that "the zero-shot performances of LaTable does not match the baselines" and that zero-shot is "significantly worse," but there is no explicit table, figure panel, or numeric entry showing the magnitude of the gap. The OOD figures (Figs. 2–3) plot performance as a function of training samples starting from some small number, not from zero. Because zero-shot capability is a central challenge for foundation models and the paper builds its discussion around this limitation, the reader needs to see the actual gap (e.g., density 0.3 vs. 0.6, or similar) to assess how far the approach is from usable zero-shot generation.

- **No ablation isolating the benefit of cross-dataset training.** The paper attributes LaTable's strong performance on small datasets to transfer across tables (Fig. 1 and surrounding text). This is plausible, but there is no experiment comparing LaTable trained jointly on all datasets versus a version trained on each dataset individually (or on a subset). Such an ablation would directly quantify the benefit of multi-dataset training and rule out alternative explanations (e.g., that gains come from LLM embeddings or other architectural choices rather than cross-dataset training).

- **Limited OOD evaluation (5 datasets) and no downstream AUC for OOD.** The OOD experiments are conducted on only 5 datasets, and the evaluation reports only density and coverage — unlike the in-distribution setting where downstream AUC (XGBoost) is also reported. Per-dataset results and downstream performance for OOD would strengthen the claim that finetuned LaTable produces practically useful synthetic data. The paper acknowledges the small OOD evaluation set but does not discuss variability across the 5 datasets.

- **Model size and computational cost not reported.** The paper does not state the number of parameters in LaTable, training time, or inference cost relative to baselines. For a method that argues efficiency advantages over LM-based approaches, some data on this (even approximate) would be useful for practitioners.

### Trivial

None.

## Nice-to-Haves

- Add one or two LM-based baselines (e.g., GReaT or Tabula) to the in-distribution comparison, especially since the paper motivates LaTable as circumventing LM limitations.
- Provide a zero-shot column or explicit data point in the OOD figures (or a separate table) to quantify the zero-shot gap.
- Run an ablation training LaTable on each dataset individually (or on a random subset of datasets) to isolate the cross-dataset transfer benefit.
- Report per-dataset results or individual curves for the 5 OOD datasets to show variability.
- Add downstream AUC evaluation for the OOD setting on the subset of classification datasets.
- Report approximate model size and training/inference cost.

## Removed Points

- **"No comparison to LM-based baselines is a structural gap that prevents the paper from making its central empirical case"**: Downgraded from the harsh critic's implied fatal/major severity. The paper's central claim is about cross-dataset training enabling better generation; the LM-based methods are single-dataset methods in the same class as the baselines already included. Their absence is a gap but does not undermine the paper's core empirical argument, which is already well-supported against the included baselines.
- **"The main OOD figure begins at a small number of samples, not at zero"**: This is an observation about figure axis choices, not a factual error or weakness. The paper does discuss zero-shot separately in text. The real issue is that zero-shot is not quantified, which is kept above.
- **"Missing ablation" framed as critical oversight**: Kept as minor weakness. An ablation would strengthen the paper but the evidence from Figure 1 (better performance on small datasets) already provides indirect support for the transfer claim.
- **Strength Finder's generic framing filtered**: No changes needed — all strengths are well-grounded with specific citations to the paper.

## Novel Insights

The review reveals an interesting tension in the paper's evidence structure: LaTable's strongest empirical results (in-distribution on 78 datasets, few-shot OOD on 5 datasets) support what the model *can* do when trained or finetuned, while its weakest result (zero-shot) is the one the paper foregrounds as a limitation. This is actually an honest and scientifically valuable framing — most papers would bury poor zero-shot performance. The reviewers agree on this point: the honest diagnostic of zero-shot limitations is a genuine strength, not a weakness. At the same time, the missing LM baseline comparison creates a motivational gap: the paper criticizes LM-based approaches at length but never tests whether they perform better or worse, leaving the critique untested. The most constructive path forward would be to either add one LM baseline or explicitly acknowledge that LM comparison is left for future work and adjust the related work framing accordingly.

## Suggestions

1. Add at least one LM-based baseline (e.g., GReaT or Tabula) to the in-distribution experiments, or explicitly state that LM-based methods are excluded because they are single-dataset methods and the paper focuses on cross-dataset training.
2. Add a table row or figure panel showing zero-shot density/coverage for LaTable and baselines, even if the numbers are low — the field needs this baseline.
3. Run a single-dataset variant of LaTable as an ablation to quantify the benefit of multi-dataset training.
4. Report per-dataset results or variability for the 5 OOD datasets to help readers assess whether averaged trends are driven by outliers.
5. Include OOD downstream AUC (even on a subset) for alignment with the in-distribution evaluation.

## Score and Decision

The paper is a solid, well-motivated contribution. It introduces the first diffusion model that can be trained across heterogeneous tabular datasets with a principled architecture, and demonstrates strong empirical results against competitive baselines. The weaknesses are addressable (adding a baseline or two, quantifying zero-shot, running an ablation) and do not threaten the core claims. The paper's honest handling of its zero-shot limitations adds scientific value. On originality, importance, support for claims, and clarity, the paper scores well.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>