Now I have a thorough understanding of the paper. Let me construct the final review.

## Summary

The paper introduces TDTransformer, a transformer-based architecture for tabular classification that addresses two key challenges: (i) heterogeneity of tabular data (different column types), and (ii) numerical reasoning. The method uses distinct embedding processes per column type (categorical, numerical, binary) with alignment layers to map them to a shared space, adapts piecewise linear encoding (PLE) for numerical values without requiring labels, and proposes a column-type-aware (CTA) positional encoding that only applies positional information to categorical column embeddings. The paper evaluates on 56–76 OpenML datasets and reports improvements over XGBoost, CatBoost, and several deep tabular baselines.

## Strengths

- **Principled architectural response to data heterogeneity (Section 3.1)** – The separate embedding processes per column type (categorical tokenized as natural language sentences; numerical via PLE; binary via scalar multiplication), each with its own linear alignment layer ($\phi^\text{cat}$, $\phi^\text{num}$, $\phi^\text{bin}$), are a clean and well-motivated design. This differs from prior transformer-based tabular methods that tokenize all columns uniformly.

- **Label-free adaptation of PLE for numerical values (Equations 3–4, Table 1)** – The paper adapts PLE from Gorishniy et al. (2022) to use quantile-based bins derived from the value distribution (removing the dependency on labels), and sets the codomain to $[-1,1]$ to better match layer-normalized embeddings. This is a concrete contribution to numerical representation in transformers.

- **Column-type-aware positional encoding (CTA PE, Equation 10)** – The insight that categorical column embeddings (token-level, from variable-length sentence tokens) need positional information while numerical/binary column embeddings (column-level, one vector per column) benefit from permutation invariance is sound. The ablation in Table 4 verifies that removing all positional encoding significantly degrades multiclass accuracy (5.45% drop), while CTA PE provides a modest gain over standard PE in the multiclass setting.

- **Large-scale empirical evaluation** – The paper evaluates on a substantial number of OpenML datasets (56 stated in the body, 76 referenced elsewhere; see Weaknesses) covering both binary and multiclass classification, comparing against multiple baselines including tree-based methods (XGBoost, CatBoost) and deep learning methods (SubTab, Scarf, SwitchTab).

## Weaknesses

### Fatal
None.

### Major

- **Dataset count inconsistency (abstract: 76, body: 56, tables: "a subset of 76 tables")** – The abstract (line 4) claims evaluation on "76 real-world tabular classification datasets from the standard OpenML benchmark," while Section 4.1 (line 173) states "We use 56 real-world tabular classification datasets in the standard OpenML benchmark." Tables 2 and 3 refer to "a subset of 76 tables." This is not a trivial formatting artifact but a factual discrepancy between the abstract, the body text, and the table captions. Until resolved, a reader cannot determine the actual evaluation scale. This is the single most concrete issue in the paper because it directly affects trust in the reported results.

- **Missing key baselines: TabTransformer and FT-Transformer** – The paper cites both Huang et al. (2020, TabTransformer) and Gorishniy et al. (2021, FT-Transformer) in its references and uses the former as motivation for its positional encoding discussion. Yet neither is included as an experimental baseline. These are the most directly comparable methods for a paper proposing a new transformer architecture for tabular data. Without them, the claim of "significantly improves the state-of-the-art methods" (abstract) is not supported by the evidence presented. The gap is amplified by the fact that the paper also omits other standard tabular deep learning methods such as TabNet (which is at least mentioned in passing in related work sections of similar papers).

- **No variance or statistical significance reported** – All results in Tables 2–3 are single-point averages across datasets. No standard deviations, confidence intervals, or multiple-seed results are reported. Given that the reported gains are modest (1.67% accuracy on binary tasks, 3.62% on multiclass) and the method involves non-deterministic training (pre-training + fine-tuning with early stopping), it is impossible to assess whether these improvements are statistically reliable. This is a standard expectation for empirical ML papers.

- **Missing ablation: performance without pre-training** – The paper's pipeline includes self-supervised pre-training (SSCL) followed by supervised fine-tuning. The ablation study (Section 4.3) compares SSCL vs. SCL pre-training losses, but never compares against a "no pre-training" baseline (i.e., training the architecture from scratch with only supervised fine-tuning). This means the source of the reported gains is confounded: it could be driven by the novel architecture (embedding design, PLE, CTA PE) or by the contrastive pre-training. This is the single highest-leverage ablation that is absent.

### Minor

- **Title overstates the scope** – The title "Language Models Are Good Tabular Learners" suggests the paper adapts a pre-trained large language model to tabular data. In fact, the method uses a BERT tokenizer but trains a gated transformer from scratch on tabular data. This is a fine contribution, but the title will mislead readers expecting an LLM-adaptation paper (like TabLLM or TableLLaMA, both cited in related work).

- **Missing ablation: PLE vs. standard numerical tokenization** – The paper motivates PLE as beneficial for numerical reasoning but never ablates within the TDTransformer framework: what happens if numerical values are tokenized as words (standard method) instead of using PLE? The reader cannot isolate the benefit of PLE from the other architectural changes.

- **Positional encoding discussion cites Huang et al. (2020) in a way that conflicts with the paper's own findings** – The paper states (line 118) that "table columns have the permutation invariance property that prevents positional encodings from improving performance (Huang et al., 2020)," yet the paper's own Table 4 shows that *removing* positional encoding causes a 5.45% accuracy drop in multiclass classification — directly contradicting the cited claim. The paper's finding is more interesting than the framing suggests (it means the paper's architecture differs from TabTransformer in a meaningful way), but the text should acknowledge this discrepancy rather than presenting Huang et al. as unqualified motivation.

- **Training details are sparse** – The experimental details (line 230) provide the optimizer (Adam), hidden dimension, depth, batch size, early stopping patience, and max epochs, but do not specify the learning rate, warmup steps, or learning rate schedule. These are needed for reproducibility.

### Trivial

- **Typo:** "epxeriments" (line 230) should be "experiments."

## Nice-to-Haves

- A comparison of computational cost (training time and inference throughput) vs. XGBoost and other deep baselines would aid practical adoption.
- An analysis of sensitivity to column ordering and scalability to very wide tables would strengthen the paper.

## Removed Points

These points were raised by a reviewer but are removed after verification against the paper:

- **"The notation uses $\circ \mathcal{M}$ but does not define the mask properly"** — Removed. Line 88 explicitly states "$\mathcal{M}$ is the attention mask to exclude padding token embeddings." The mask is defined; the notation may be terse but it is not undefined.
- **"No limitations section"** — Removed. This is a formatting preference, not a substantive weakness. The paper does discuss a known failure case (lack of semantics in column names, lines 242–243).
- **"No code release"** — Removed per the Hard Rules: reproducibility concerns about the existence of code/repositories that could be released in a camera-ready version are not valid weaknesses for a submission.
- **"Related work reads as a list"** — Removed as a pure style critique that does not affect the scientific content.
- **"Strawman" criticisms about the paper's scope** — The request for a "no pre-training" ablation is kept (it is a substantive empirical gap), but the broader complaint that the paper "does not explicitly distinguish itself from TabTransformer or FT-Transformer" is removed since the method section does clearly describe the architectural differences (separate embeddings per column type, PLE, alignment layers).

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface an additional perspective that the paper's authors missed.

## Suggestions

1. **Resolve the 56 vs. 76 dataset count discrepancy immediately.** Clarify whether the evaluation is on 56 datasets (with 76 being a different count for tables or splits) and ensure the abstract, body, and table captions are consistent.
2. **Add TabTransformer and FT-Transformer as baselines** under the same data splits and training protocol. If computational constraints prevent this, state the reason clearly and adjust the strength of the SOTA claim.
3. **Report results with variance** (mean and std over at least 3–5 random seeds).
4. **Add a "no pre-training" ablation** (train the architecture from scratch with only supervised fine-tuning) to disentangle the contribution of the architecture from the contribution of contrastive pre-training.
5. **Add a PLE vs. standard tokenization ablation** within the TDTransformer framework to isolate the benefit of PLE for numerical values.
6. **Tone down the title** to reflect that the method is a custom transformer trained from scratch, not a pre-trained language model being adapted.
7. **Specify the learning rate, warmup schedule, and any learning rate decay** in the experimental details.

## Score and Decision

The paper proposes a well-motivated architecture with several sensible design choices. However, the evaluation is significantly weakened by: (i) the dataset count inconsistency, (ii) the absence of the most directly comparable transformer-based tabular baselines (TabTransformer, FT-Transformer), (iii) the complete lack of variance or significance reporting, and (iv) a missing key ablation (no pre-training). These issues prevent the evidence from supporting the strong claims made. The contribution may be salvageable with major revisions, but as presented the paper does not meet the bar for acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>