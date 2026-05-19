- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

LaTable introduces a tabular diffusion model designed for cross-dataset training — a novel direction in tabular generative modeling. The architecture combines a transformer without positional encodings (for column-order equivariance), frozen LLM embeddings for feature names, descriptions, and categories, and a mixed-type diffusion framework handling both numerical and categorical variables. Experiments on 78 OpenML datasets show LaTable outperforms single-dataset baselines (ARF, CTGAN, TVAE, TabDDPM) on in-distribution generation, and demonstrates strong few-shot out-of-distribution performance through finetuning. The paper also honestly discusses poor zero-shot performance as a limitation and explores data-quality challenges.

## Strengths

1. **Column-order equivariance via transformer without positional encodings** (Section 3.3.1, line 62): The paper removes positional encodings and instead feeds feature-name embeddings to break symmetry, satisfying desideratum D4. This is a clean, principled architectural choice that differentiates LaTable from recurrent or causally-masked approaches.

2. **Pretrained LLM embeddings for categories with similarity-based decoding** (Section 3.3.3, Eq. 3): Uses a frozen LLM (UAE-Large-V1) to encode category names, then predicts probabilities via an attention-like similarity layer. This avoids learning separate embeddings per category, preserves semantic relationships across datasets (e.g., "gender"/"sex"), and is scalable to many categories — a practical solution for cross-dataset training.

3. **Strong in-distribution generation results across multiple baselines** (Table 1): LaTable achieves downstream AUC of 0.874, density 0.865, coverage 0.900, and precision 0.866 — outperforming ARF, CTGAN, TVAE, and TabDDPM. The gains are most pronounced on smaller datasets (Figure 2), consistent with the cross-dataset transfer claim.

4. **Compelling few-shot out-of-distribution results** (Section 4.2, Figure 3): When finetuned on OOD datasets with few samples, LaTable achieves density near 1.0 and significantly higher coverage than all baselines, including real training data. This provides direct evidence that cross-dataset pretraining yields useful priors for new tables.

5. **Honest framing of zero-shot limitations** (Sections 4–5): The paper explicitly acknowledges that zero-shot performance is poor, investigates reasons (feature/distribution shift between training and OOD sets, WikiTables domain mismatch), and frames this as a challenge for future work rather than overclaiming. This scientific candor is a strength.

6. **Practical engineering choices**: Encodings are cached to disk (line 79), avoiding LLM inference during training. The chosen LLM encoder is lightweight (1.34 GB). These decisions make cross-dataset training feasible.

## Weaknesses

### Fatal

None.

### Major

1. **Missing ablation isolates cross-dataset benefit.** The paper's central thesis is that training across datasets transfers to individual tasks. Yet there is no comparison between LaTable trained on all data and LaTable trained *from scratch on each individual dataset* (i.e., without cross-dataset training). Without this ablation, the observed gains could stem from the transformer architecture, the diffusion framework, the LLM embeddings, or the combined training — not necessarily from cross-dataset transfer per se. Figure 2 (improvement on small datasets) is suggestive but correlational. This is the single biggest gap in the experimental validation. (Lines 118–140, Figure 2.)

2. **TabDDPM baseline performance is suspiciously low.** TabDDPM achieves downstream AUC of 0.757 and density of 0.414 (Table 1), which is far below what one would expect from a recent diffusion-based tabular generator. The paper acknowledges this ("despite hyperparameter tuning attempts, TabDDPM performed poorly for small datasets," line 140) but offers no further analysis or controlled experiment to validate that the gap is genuine. Since LaTable also outperforms ARF, CTGAN, and TVAE, the comparison is not wholly undermined, but the TabDDPM numbers raise questions about whether the experimental setup systematically disadvantages certain baselines, which erodes confidence in the absolute ranking.

### Minor

1. **Statistical reporting could be strengthened.** Table 1 reports means and standard deviations over 5 random seeds aggregated across 78 heterogeneous datasets. This conflates seed-level noise with cross-dataset variability. While Figure 2 does show per-dataset scatter plots, the aggregate table lacks paired statistical tests (e.g., Wilcoxon signed-rank, win/loss counts) that would directly substantiate the claim that LaTable "significantly outperforms" baselines across datasets. (Table 1, lines 121–140.)

2. **Implementation details are incomplete.** The paper omits several parameters needed for reproducibility: transformer size (number of layers, heads, hidden dimension \(d_h\)), number of diffusion steps, learning rate, batch size, training time, and hardware. These details affect both reproducibility and the interpretation of the "scaling up" discussion. (Section 3.)

3. **OOD selection criteria are not stated.** The paper splits 83 datasets into 78 in-distribution and 5 out-of-distribution (line 116) without specifying what makes the 5 datasets "out-of-distribution" — feature overlap? label shift? domain? Without this, the reader cannot assess whether the zero-shot test is meaningful or trivial.

### Trivial

None.

## Nice-to-Haves

- **LM-based baselines** (GReaT, Tabula) would strengthen the generation quality comparison, even though they train on single datasets. The paper explains why they are not directly comparable (single-dataset training), but including them would address a natural reader question.
- **A qualitative analysis** of what LaTable learns from cross-dataset training (e.g., t-SNE of feature embeddings or nearest-feighbor analysis in embedding space) would make the transfer mechanism more concrete.
- **Per-dataset win/loss counts** and a paired sign test for the in-distribution results would turn a suggestive table into a rigorous one.

## Removed Points

These points were removed from the harsh critic's review; treat them with caution:

- **"Zero-shot analysis is speculation dressed as finding"** — The paper explicitly frames this section as exploratory ("Let us explore possible directions for future research," line 184) and discusses it as a limitation. The critic's characterization is overstated given the paper's own cautious framing. Removed.
- **"LM-based baselines are a notable omission"** — The paper explains that LM-based approaches (GReaT, Tabula) train/finetune on single datasets only (line 40) and are thus addressing a different setting. The criticism is scope-creep. Moved to Nice-to-Haves.
- **"Missing related works"** — Per the review guidelines, missing related works are not raised without external verification. Removed.
- **"Qualitative analysis missing"** — This is a nice-to-have, not a weakness. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface that the cross-dataset ablation gap and the TabDDPM baseline issue are the two most consequential weaknesses, and that the paper's few-shot OOD results are its strongest evidence for transfer.

## Suggestions

1. **Add the from-scratch ablation** — Train LaTable on each single dataset individually (no cross-dataset training) and compare to the cross-dataset trained version. This directly measures the transfer benefit and would be the cleanest validation of the paper's core claim.
2. **Run a small controlled experiment** on 10–15 datasets to compare properly tuned TabDDPM against LaTable, to verify the gap is real and not an artifact of hyperparameter selection or evaluation mismatch.
3. **Add paired statistical tests** (Wilcoxon signed-rank or win/loss counts) to Table 1 to support the claim that LaTable "significantly outperforms" baselines across datasets.
4. **Complete the reproducibility checklist** by specifying transformer size, diffusion steps, learning rate, batch size, and compute hardware.
5. **Define OOD explicitly** — state what distinguishes the 5 OOD datasets from the 78 in-distribution ones (e.g., feature overlap, dataset domain, column type distribution).
