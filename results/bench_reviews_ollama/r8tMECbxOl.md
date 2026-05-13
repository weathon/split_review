## Summary
The paper proposes TDTransformer, a transformer-based tabular classifier with type-specific embedding pipelines (categorical via BERT-tokenizer text embeddings, numerical via piecewise-linear encoding adapted from Gorishniy et al. 2022, binary via Hadamard with column-name embeddings), alignment layers to a common space, a column-type-aware (CTA) positional encoding that is applied only to the categorical sub-sequence, and a contrastive pre-train / supervised fine-tune pipeline. Reported average gains over baselines are 1.67% (binary) and 3.62% (multiclass) across an OpenML benchmark.

## Strengths
- The architectural decomposition into type-specific embedding pipelines with alignment layers (Sec. 3.1) is cleanly motivated by the CLIP analogy and is a reasonable response to column heterogeneity.
- The CTA positional encoding insight — that PE should be applied only to the token-wise categorical sub-sequence and not to column-wise numerical/binary embeddings (Sec. 3.2) — is a sensible design, and Table 4 plus the t-SNE plots in Fig. 4 give it some empirical support, with a 5.45% multiclass accuracy drop when PE is omitted entirely.
- Adapting PLE to use label-free quantile bins and rescaling the codomain to [-1, 1] to align with LayerNorm-normalized embeddings (Sec. 3.1, Table 1) is a small but pragmatic refinement of Gorishniy et al. 2022.

## Weaknesses

### Fatal
None.

### Major
- **Title/framing is not supported by the method.** The paper is titled "Language Models Are Good Tabular Learners" and concludes by advocating "a rethink of the power of language models in the tabular data domain" (Sec. 5), but no pre-trained LM is used. The model is a 12-layer gated transformer trained from scratch per task; only the BERT *tokenizer* is reused (Sec. 4.1 Experimental details). The central rhetorical claim of the paper is not what is actually demonstrated.
- **Baseline set omits the most directly relevant comparisons.** Tables 2–3 compare against XGBoost, CatBoost, SubTab, Scarf, and SwitchTab. The paper itself cites FT-Transformer (Gorishniy 2021), the PLE-based model (Gorishniy 2022), TabTransformer (Huang 2020), TabLLM, and TabLLaMA in related work, yet none appear as baselines. Without Gorishniy 2022 in particular — whose PLE this paper directly adapts — gains cannot be attributed to TDTransformer rather than to PLE itself.
- **Ablations do not isolate the listed contributions.** The contribution list claims three things: type-specific embeddings + alignment layers, PLE adaptation, and CTA positional encoding + type-aware corruption. Only positional encoding (Table 4), batch size (Tables 5–6), and SSCL vs SCL (Fig. 3) are ablated. There is no PLE-off ablation, no alignment-layer ablation, no type-aware-corruption ablation, and no no-pre-training ablation. The contributions are therefore not individually supported.
- **No variance/significance reporting despite repeated use of "significantly."** Headline gains are 1.67% (binary) and 3.62% (multiclass). With no seeds, no error bars, and no paired tests across datasets, "significantly improves the state-of-the-art" (abstract) is not substantiated.

### Minor
- **Dataset count is internally inconsistent.** Abstract and Sec. 4.2 reference "76 datasets" while Sec. 4.1 ("Datasets") states "56 real-world tabular classification datasets." This should be reconciled.
- **CTA-PE claim overstates Table 4.** Sec. 4.3 notes positional encoding and CTA-PE have "similar performance" overall, with the gap meaningful primarily in multiclass; the abstract/contribution framing of CTA-PE as a clear booster is stronger than the evidence.
- **Semantics confounder.** Sec. 4.2 explains losses to XGBoost by "lack of semantics in column names." This implies wins elsewhere may partly stem from column-name semantics rather than the architectural changes, which is never controlled for (e.g., by anonymizing column names).
- **SSCL > SCL justification is shaky.** The cited vision results (Chen 2020; He 2020) concern transfer to new downstream tasks, not in-domain fine-tuning; the analogy is loose.
- **Pre-training protocol under-specified.** Whether pre-training is per-dataset or joint, what data feeds SCL labels, and whether self-supervised baselines (Scarf, SwitchTab) received comparable pre-training compute are not stated in Sec. 4.

### Trivial
- Figures 2 and 3 use dual axes that combine per-dataset scatter and averages; per-dataset numeric tables would be clearer.

## Nice-to-Haves
- Critical-difference diagrams or per-dataset win/loss tables across the full benchmark.
- A controlled "anonymized column names" experiment to test the semantics-leakage hypothesis the authors themselves raise.
- Adding at minimum FT-Transformer and Gorishniy 2022 to the baseline table.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *(From harsh critic) Missing comparisons against TabPFN, SAINT, NODE, TabR, TabLLM as related work omissions* — KEPT as a Major weakness only for the directly cited tabular-transformer methods (FT-Transformer, Gorishniy 2022, TabTransformer). The broader list strays into "missing related work" territory which we are instructed not to assert.
- *(From harsh critic) "No experiment shows quantile bins outperform tree bins, nor [-1,1] vs [0,1]"* — this is a fair nice-to-have but the paper does not claim quantile bins are superior; it claims they are *label-free* (Sec. 3.1), which is a different, defensible claim. Removed as a strawman.
- *(From strength finder) "Strong empirical improvement … TDTransformer consistently outperforms all compared methods"* — conflicts with the verified Major weakness about an incomplete baseline set; weakness wins.
- *(From strength finder) "Robustness on challenging data subsets"* — the subsets ($0.2<\gamma<0.8$, $|\mathcal{D}|<2000$) look post-hoc and lack significance testing; weakness wins.
- *(From strength finder) "Principled handling of column heterogeneity via type-specific embeddings and alignment layers"* — kept as a Strength; the strength-finder itself notes this is not ablated, but the design itself is concrete and specific.

## Novel Insights
None beyond the paper's own contributions. The PLE adaptation is incremental relative to Gorishniy et al. 2022, and the CTA-PE observation, while sensible, is a localized architectural tweak rather than a broader insight.

## Suggestions
- Either incorporate a pre-trained LM (the title's premise) or rename and reframe the paper around "type-aware tabular transformers."
- Add FT-Transformer and Gorishniy 2022 (PLE) as baselines; with the latter, the contribution of PLE itself versus the rest of TDTransformer can finally be isolated.
- Run per-component ablations (PLE off / alignment-layer off / type-aware corruption off / no pre-training) on at least a representative subset of the benchmark.
- Report mean ± std over ≥3 seeds and a paired test (e.g., Wilcoxon) across datasets; release per-dataset numbers.
- Resolve the 56 vs 76 dataset discrepancy in the text and list the OpenML IDs.
- Run an anonymized-column-names experiment to quantify how much of the gain depends on semantic column names.

## Axis-by-Axis Assessment
- **Originality:** Low-to-moderate. PLE is borrowed from Gorishniy 2022 with a minor codomain change; type-specific embedding pipelines and CTA-PE are reasonable but incremental.
- **Importance:** Moderate. Tabular deep learning is a well-motivated area, but the paper's framing around "language models" overpromises.
- **Claim support:** Weak. "SOTA" is asserted without comparing to the most relevant transformer baselines and without variance/significance.
- **Soundness of experiments:** Weak. Missing key baselines, missing component ablations, inconsistent dataset count, no seeds.
- **Clarity:** Adequate; the framework figure and equations are followable, though several typos and the dataset-count inconsistency hurt.
- **Value to community:** Limited in current form — the CTA-PE observation is the most useful takeaway.

## Score and Decision
The paper has substantive architectural ideas but the central "language models" framing is not what was tested, the baseline set excludes the most directly relevant transformer competitors, the listed contributions are not individually ablated, and the headline gains are reported without variance against an incomplete comparator set. These are not cosmetic and would require a substantial revision rather than rebuttal-fixable edits.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>