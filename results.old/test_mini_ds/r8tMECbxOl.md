Now I have verified all claims against the paper. Let me write the consolidated review.

---

## Summary

This paper proposes TDTransformer, a transformer architecture for tabular classification that uses distinct embedding processes for categorical, numerical, and binary columns, with alignment layers to project embeddings into a shared space. It adapts piecewise linear encoding (PLE) for numerical values and introduces column-type-aware (CTA) positional encoding. The model is pre-trained with contrastive learning and fine-tuned on downstream tasks. Experiments on an OpenML benchmark (stated as both 56 and 76 datasets) show average accuracy improvements over XGBoost of ~1.67% (binary) and ~3.62% (multiclass).

## Strengths

- **Column-type-specific embeddings with alignment layers**: Section 3.1 defines separate embedding processes for categorical, numerical, and binary columns, each with a dedicated linear alignment layer (ϕ^cat, ϕ^num, ϕ^bin). This design directly addresses the heterogeneity challenge in tabular data and is inspired by multimodal alignment (CLIP), which is a novel adaptation for tabular transformers.

- **Adapted piecewise linear encoding for numerical values**: Table 1 and the surrounding text show that TDTransformer's PLE differs from the original (Gorishniy et al., 2022) in using quantile-based bins (requiring no labels), outputting [-1,1] for compatibility with layer normalization, and mapping a scalar to a single embedding rather than a sequence. This is a reasonable inductive bias for numerical reasoning.

- **Empirical evaluation on a substantial benchmark**: Tables 2 and 3 report results across many OpenML datasets. TDTransformer with CTA achieves average accuracy 74.37% (binary) and 75.44% (multiclass), outperforming XGBoost (72.91%, 73.61%) and the included deep-learning baselines. Figure 2 visualizes per-dataset comparisons across individual datasets.

- **SSCL vs SCL comparison**: Figure 3 provides an empirical comparison of self-supervised vs. supervised contrastive pre-training losses, showing SSCL yields better downstream performance.

## Weaknesses

### Major

- **Dataset count inconsistency (56 vs. 76)**: The abstract and Tables 2-3 refer to "76 real-world tabular classification datasets" while Section 4.1 states "We use 56 real-world tabular classification datasets." This is a sizable inconsistency (~35% difference) that makes the experimental scope unclear. The reader cannot determine whether the method was evaluated on 56 or 76 datasets, nor whether the reported averages would differ depending on which number is correct. This undermines trust in the experimental reporting and must be resolved.

- **Missing comparisons to the most directly relevant tabular transformers**: The paper claims to advance transformer-based architectures for tabular data, but the baselines (XGBoost, CatBoost, SubTab, Scarf, SwitchTab) do not include FT-Transformer (Gorishniy et al., 2021), TabTransformer (Huang et al., 2020), or SAINT. The absence of FT-Transformer is especially problematic because the paper's PLE adaptation is derived from Gorishniy et al. (2022), which was evaluated in the context of FT-Transformer. Without these comparisons, the paper cannot substantiate its claim of advancing the state of the art among transformer-based tabular methods.

- **No error bars, variance, or significance testing**: Tables 2-3 report only point estimates without standard deviations or confidence intervals. Given the modest average gains over XGBoost (1.67% binary, 3.62% multiclass) and the observation that XGBoost wins on several individual datasets (Figure 2), it is impossible to determine whether the aggregate improvements are statistically significant. Standard practice in this area requires reporting variance and, ideally, paired significance tests (e.g., Wilcoxon signed-rank).

### Minor

- **Misleading "language model" framing**: The title claims "Language Models Are Good Tabular Learners," but the method does not use a pre-trained language model. It uses a BERT tokenizer for categorical column names/values and trains a gated transformer (from TransTab) from scratch with no language modeling objective, no pre-trained LM weights, and no transfer from natural language. The contribution is a specialized tabular transformer, which is defensible without the inflated label.

- **Pre-training data source ambiguity**: The paper describes a pre-train/fine-tune pipeline but does not specify whether pre-training is performed on the training split of each dataset or on the full dataset (which could cause test-set leakage through the contrastive objective). This must be clarified.

- **No ablation of the core architectural choices**: The current ablations (pre-training loss, positional encoding, batch size) do not isolate the claims made in the contributions. A proper ablation would compare: PLE vs. scalar embedding vs. learned embedding for numerical columns; Hadamard product vs. addition for combining column name and value embeddings; presence vs. absence of alignment layers; column-type-specific embedding vs. a single shared embedding process.

- **Pre-training corruption mechanism underspecified**: The paper mentions "corruption parameter 0.5" and that "random permutation only occurs within the same type of column," but does not specify what the parameter controls (e.g., fraction of rows corrupted, fraction of cells within a row, or something else), making the pre-training procedure non-reproducible.

- **CTA positional encoding advantage is marginal**: Table 4 shows CTA and standard positional encoding produce nearly identical results for binary (84.01 vs 84.11) and are close for multiclass (80.00 vs 80.30). The paper overstates the advantage of CTA given this empirical similarity.

### Trivial

- Hyperparameters are sparse: No learning rate, dropout, number of attention heads, or feedforward dimensions are reported. For a new architecture, these details are needed for reproducibility.
- The paper does not discuss limitations beyond noting one failure case (large datasets with non-semantic column names).

## Nice-to-Haves

- An ablation comparing PLE against simpler alternatives (e.g., nn.Embedding over binned values or a linear projection of the scalar) would strengthen the claim that PLE specifically contributes to performance.
- Adding FT-Transformer as a baseline would be the single most impactful improvement, since PLE is adapted from that line of work.
- Reporting standard deviations or confidence intervals, ideally along with paired statistical significance tests against XGBoost per dataset.

## Removed Points

- **Claim that the attention mask M is never defined**: The paper explicitly states "Here, M is the attention mask to exclude padding token embeddings" (line 88 of the extracted text). The criticism is factually wrong.
- **Pre-training data leakage characterized as "structural" and results "uninterpretable"**: While the paper should clarify the pre-training data source, standard practice in tabular self-supervised learning is to pre-train on the training split only, and the paper does not suggest otherwise. The fatal framing is speculative and not warranted by evidence on the page; this point is downgraded to Minor above.
- **General concerns about reproducibility ("no code")**: Many papers at this stage do not release code. The important architectural parameters and hyperparameters are the real concern; these are captured in the Minor weaknesses.
- **Strength Finder strengths that are generic or conflict with evidence**: Several strengths (e.g., "empirical superiority on a large benchmark") are kept but their force is qualified by the missing baselines and lack of error bars. Strengths about "CTA producing better class separation" from t-SNE are retained but noted as qualitative.
- **Criticisms about missing appendix or appendix content**: The appendix is stripped by the parser; these criticisms cannot be verified and are removed.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface new observations about the method or results beyond what the paper itself claims.

## Suggestions

1. Resolve the 56 vs. 76 dataset count inconsistency and clearly state the correct number and what it refers to.
2. Add FT-Transformer (and ideally TabTransformer and SAINT) as baseline methods. This is essential for any paper claiming to advance transformer-based tabular learning.
3. Report standard deviations and perform paired statistical significance testing (e.g., Wilcoxon signed-rank) against XGBoost per dataset.
4. Add ablations of the core design choices: PLE vs. scalar embedding, Hadamard product vs. addition, alignment layers vs. shared embedding.
5. Clarify whether pre-training uses only the training split or the full data, and specify exactly what the corruption parameter controls.
6. Reframe the title and abstract to accurately describe the method as a tabular transformer rather than a language model.
7. Provide missing hyperparameters (learning rate, dropout, attention heads) in the main text.

---

**Round 1 Bracket**: Initial calibration placed the paper in the 3.0–8.0 range, with the most relevant anchors in the 4.0–7.0 band (tabular transformer methods evaluated on OpenML-style benchmarks).

**Round 2 Anchors examined**:
- **TabDPT** (avg 5.25, Reject): Stronger evaluation with confidence intervals and win-rate analysis; pre-trains on 123 datasets. This paper is weaker on evaluation rigor.
- **Token Transferability / TabToken** (avg 5.67, Reject): Cleaner evaluation with 10 datasets, clear ablations, but marginal improvements. This paper has more datasets but weaker evaluation methodology.
- **TabFlex** (avg 5.25, Reject): Thorough efficiency evaluation with 25 baselines. This paper is weaker in comparison breadth.
- **Attic** (avg 5.75, Reject): Strong empirical evaluation on 100+ benchmarks with comprehensive baselines. This paper is notably weaker in experimental design.
- **TP-BERTa** (avg 7.0, Accept): Uses actual pre-trained LM, 145 datasets, strong evaluation. This paper is significantly weaker.
- **UniTabE** (avg 6.33, Accept): Pre-trains on 13B samples, extensive baselines. This paper is significantly weaker.
- **TabKANet** (avg 3.0, Reject): Similar evaluation issues (missing baselines, no hyperparameter tuning for GBDTs) and comparable novelty concerns. This paper is slightly stronger due to more extensive dataset coverage and a more coherent design.

This paper is most comparable to the 4.0–5.0 range papers: it has a plausible architectural contribution but its evaluation has concrete, verifiable flaws (dataset count inconsistency, missing key baselines, no error bars) that prevent it from substantiating its core claims. It is weaker than TabDPT, Attic, and the Token Transferability paper in evaluation rigor, but somewhat stronger than TabKANet.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>