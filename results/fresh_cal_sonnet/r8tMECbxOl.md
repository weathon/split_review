**Round 1 bracket: 4–6** (the paper is clearly above the ~3 rejects but lacks the completeness of an 8+ paper; most comparable anchors in the 4–5 range are tabular-transformer rejects with similar issues).

Now narrowing within the bracket:Now I have enough information to write the final review. Let me synthesize everything.---

## Summary

TDTransformer is a transformer-based tabular classification framework that addresses two alleged bottlenecks: (1) data heterogeneity via column-type-specific embeddings with independent alignment layers for categorical, numerical, and binary columns, and (2) numerical representation via an adapted label-free piecewise linear encoding (PLE). A column-type-aware (CTA) positional encoding is also proposed, and the model is pre-trained with contrastive objectives before fine-tuning. Evaluation is conducted on 76 OpenML tabular datasets against tree-based methods and self-supervised transformer baselines.

---

## Strengths

- **Column-type-specific embeddings with alignment layers**: The paper explicitly designs separate embedding pathways for categorical (text tokenized), numerical (PLE-encoded), and binary (Hadamard-product of column-name embedding and binary value) columns, with independent linear alignment layers φ^cat, φ^num, φ^bin mapping to a common space (Eqs. 2, 5–7). This is a principled departure from serializing all features as text tokens and is directly motivated by the heterogeneity problem.

- **Label-free adapted PLE for numerical features**: The adaptation shifts the PLE codomain to [−1,1] (to align with layer normalization) and replaces decision-tree bins with quantile-based bins (Table 1), making PLE independent of labels. This is a reasonable engineering choice that removes a supervised dependency present in the original PLE formulation.

- **CTA positional encoding respects permutation invariance**: By applying positional encoding only to categorical (token-ordered) embeddings and not to numerical/binary (column-wise, permutation-invariant) embeddings (Eq. 10), the model avoids imposing a spurious ordering on features where none exists. The ablation in Table 4 shows a 5.45% accuracy drop when positional encoding is removed entirely in the multiclass setting, and t-SNE visualizations in Figure 4 confirm better class separation.

- **Large and stratified evaluation**: The benchmark covers 76 OpenML datasets with results broken down by column-type subsets (S∪S_num), class imbalance (positive ratio γ), dataset size (|D|≥2000), and number of classes (C≥4), providing more diagnostic resolution than a single aggregate metric. The claimed 3.38% accuracy gain on the difficult binary subset (0.2 < γ < 0.8) and 3.62% multiclass gain over the best baseline are reported in Tables 2–3.

- **Honest failure analysis**: Section 4.2 explicitly identifies a case where XGBoost outperforms TDTransformer—datasets with semantically empty column names (V1,…,V100) and categorical values (v1,v2,…)—and explains the mechanism (language model reliance on metadata). This kind of transparency strengthens the paper's credibility.

---

## Weaknesses

### Fatal
None.

### Major

- **TransTab (the backbone) is absent from the baseline comparison.** Section 3.3 states explicitly that "the backbone model…is constructed using the gated transformer proposed in (Wang & Sun, 2022)"—this is TransTab. Yet Tables 2, 3, and Figure 2 compare against XGBoost, CatBoost, SubTab, Scarf, and SwitchTab. Without TransTab as a baseline, the experiments cannot isolate how much performance gain comes from the new contributions (type-specific embeddings, adapted PLE, CTA encoding) versus the backbone itself. This is the most consequential gap: the paper argues these architectural additions are the key, but the only controlled comparison that would confirm this—TransTab alone versus TDTransformer—is absent.

- **FT-Transformer is cited but not used as a baseline.** Gorishniy et al. (2021) ("Revisiting Deep Learning Models for Tabular Data") is cited in the reference list. It is the canonical tabular transformer benchmark, handles both categorical and numerical features, and is the primary comparator in this line of work. The paper's claim to "significantly improve the state-of-the-art" over transformer-based approaches cannot be substantiated without it. SubTab, Scarf, and SwitchTab are self-supervised learning wrappers, not transformer architectures designed to compete with tree-based methods. The relevant prior art is missing.

- **The paper's central claim—that type-specific embeddings are the key driver—has no direct ablation.** Section 4.3 ablates SSCL vs. SCL pre-training, positional encoding variants (none / standard / CTA), and batch size. Nowhere does the paper compare TDTransformer to a version where all columns are handled uniformly (e.g., all serialized as text tokens, as in the approach TDTransformer is meant to improve upon). Without this, the central architectural hypothesis is not verified by internal evidence.

- **Dataset count is factually inconsistent.** The abstract states "76 real-world tabular classification datasets." Section 4.1 reads: "We use 56 real-world tabular classification datasets in the standard OpenML benchmark." Table 2's caption and Table 3's caption both say "we select a subset of 76 tables for detailed comparison." This is unreconciled. It is unclear whether 56 or 76 datasets constitute the actual benchmark, and the discrepancy affects the reliability of reported averages.

### Minor

- **Contrastive pre-training contribution is not isolated.** Section 4.3 compares SSCL vs. SCL but neither is compared to a fine-tuning-from-scratch baseline (no pre-training). Since contrastive pre-training is listed as a contribution, the evidence that it helps at all—rather than being neutral—is absent.

- **Binary embedding zeroes out column identity when value = 0.** From Eq. 7, E^bin = E^bin_col ∘ (x · 1^T_d); when x_i = 0, the entire representation for that binary column becomes the zero vector. For columns where the "false" state is semantically meaningful, the model loses the column identity entirely. This design choice is not acknowledged or discussed.

### Trivial

- **Spectral bias motivation is loosely connected to tabular heterogeneity.** The paper cites spectral bias (Rahaman et al., 2019; Xu et al., 2019) as motivation for why transformers fail on heterogeneous tabular data (Section 1), but spectral bias describes training dynamics (preference for low-frequency components) rather than an architectural inductive bias for heterogeneous feature types. The link is suggestive but underdeveloped as a theoretical foundation.

---

## Nice-to-Haves

- **Stratify results by semantic richness of column names.** The paper acknowledges in Section 4.2 that TDTransformer's advantage partially depends on semantic column names and values. A systematic analysis of performance across the full benchmark stratified by this property would clarify the real scope of the contribution—and inform the community about when LLM-backbone tabular models are likely to help.

- **Analyze whether TDTransformer's edge partially reflects additional information.** When comparing TDTransformer to XGBoost or other tree-based methods, the model uses rich natural language metadata (column names, cell strings) that GBDTs ignore. The discussion in Section 4.2 touches on this but does not frame it as a methodological note: the comparison is partly "same task" and partly "more information." Acknowledging this explicitly would sharpen what the contribution actually demonstrates.

- **CTA gain over standard positional encoding.** Table 4 and the surrounding text note that "Positional encoding and CTA positional encoding have similar performance" while the drop from removing encoding entirely is 5.45%. The paper should clarify how much of the narrative benefit of CTA encoding is statistical vs. architectural—the main gain appears to be from using any positional encoding at all.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "comparison with SubTab/Scarf/SwitchTab is unfair."** The critic frames the self-supervised baselines as unfair comparators because they are "not purpose-built tabular transformer architectures." This is partly valid (the better framing is "incomplete," not "unfair") — but critically, a weak basket of baselines does not unfairly advantage the author's method; it merely leaves the comparison incomplete. Removed as an independent weakness (merged into the FT-Transformer baseline criticism above).

- **Harsh critic: "TransTab uses one-hot for categorical columns, losing semantic information."** The paper actually mentions this in the Discussion (Section 5): "Some baseline methods with transformer-based architectures use one-hot encoded representation for categorical columns, which inherently loses semantic information." The paper is not wrong here; the statement is a fair self-description of why TransTab and similar methods underperform. Removed as misdirected criticism.

- **Strength finder: "TDTransformer achieves a 3.38% accuracy gain… directly supporting the claim."** This strength is substantially undermined by the missing TransTab and FT-Transformer baselines — the gain is measured against suboptimal baselines. Demoted from standalone strength; the evaluation breadth is retained as a strength but the claimed magnitude of gain should not be taken at face value without the key comparisons.

- **Harsh critic: "Accuracy is misleading on imbalanced datasets."** The paper uses AUC for binary classification (appropriate) and segments results by positive ratio γ. This concern is partially addressed; removed as a standalone weakness.

---

## Novel Insights

The CTA positional encoding design decision—adding positional encoding only to categorical embeddings while leaving numerical and binary columns position-free—is a small but genuinely useful insight: it resolves the tension between the permutation-invariance of tabular features and the token-ordering assumed by standard transformers. The core finding that the model's advantage is substantially conditioned on semantic richness of column names (Section 4.2) is also a practically important observation that has implications for benchmarking tabular methods more broadly: evaluation on datasets with generic column names like V1,...,V100 may tell a very different story than evaluation on datasets with informative metadata.

---

## Suggestions

1. **Add TransTab as an explicit baseline** using the same 76-dataset OpenML benchmark. This single experiment would make the paper's claims about its architectural additions credible.
2. **Add FT-Transformer as a baseline.** Without it, the paper cannot claim improvement over the transformer state of the art for tabular data.
3. **Ablate type-specific embeddings.** Compare TDTransformer to a version that serializes all column types uniformly as text tokens. This directly tests the paper's central hypothesis.
4. **Resolve the 76 vs. 56 dataset count.** Clarify in one place how many datasets are used and reconcile the discrepancy across abstract, Section 4.1, and table captions.
5. **Add a no-pre-training baseline** to the ablation in Section 4.3 to validate the contrastive pre-training contribution.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `3qDhqj6qfu.md` (TabKANet) | 3.0 | R1 | Simpler method, narrower eval, basic benchmark — clearly weaker than TDTransformer |
| `ioOgrS0UKx.md` (PlicoTabTransformer) | 3.0 | R1 | Missing FT-Transformer baseline, limited eval — slightly weaker than TDTransformer |
| `0bjIoHD45G.md` (Closing the gap) | 4.2 | R1 | Similar problem framing, missing key baselines, non-standard metrics — comparable issues |
| `pE0UM18TQh.md` (Fine-tuned ICL) | 4.33 | R1/R2 | Limited novelty, adequate but not strong evaluation — roughly comparable |
| `wElgE9qBb5.md` (Mambular) | 4.25 | R1 | Reasonable breadth but limited ablation — comparable |
| `FDMlGhExFp.md` (TabDPT) | 5.25 | R2 | Larger scale, better ablation, but rejected for novelty; somewhat stronger than TDTransformer |
| `Dk1ybhMrJv.md` (Pretrained deep models) | 5.33 | R2 | Well-supported claims in a specific niche; more complete evaluation |
| `a06UO11IrQ.md` (Rethinking Pre-training) | 6.0 | R2 | More complete experimental design; stronger methodological justification |
| `rhgIgTSSxW.md` (TabR) | 5.75 | R2 | Accepted; demonstrates GBDT outperformance with rigorous ablation — clearly stronger |

**Round 1 bracket:** 4–6. The paper is clearly above the ~3 rejects but well below the 8+ accepted papers.

**Round 2 narrowing:** Within the 4–6 band, TDTransformer most closely resembles the 4.2–4.5 cluster ("Closing the gap," "Fine-tuned ICL," Mambular): reasonable contributions, evaluation on a reasonable benchmark, but missing the key controlled comparisons that would make the main claims defensible. The missing TransTab baseline is a more structurally significant gap than the issues in those papers (since it concerns the method's own backbone). The 76-dataset evaluation is broader than those papers, which pulls the score slightly upward. TDTransformer sits below TabDPT (5.25) and clearly below TabR (5.75, accepted): those papers have more complete experimental designs.

**Final score: 4.5** — above the 4.2 cluster due to the broader evaluation and honest failure analysis, but below 5.0 because the three simultaneous gaps (TransTab baseline, FT-Transformer baseline, type-specific embedding ablation) mean the paper's core claims cannot be assessed with the evidence provided.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>