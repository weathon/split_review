- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 5, 5, 5
Now I have a thorough understanding of the paper and both reviews. Let me synthesize the final consolidated review.

## Summary
The paper proposes **TAMO**, a framework that treats tables as an independent modality for LLMs by encoding them via a permutation-invariant hypergraph neural network. The structural features are injected as learnable soft prompt tokens into a frozen LLM. The paper also introduces **StructQA**, a benchmark for table structure understanding. Experiments across five datasets (HiTab, WikiTQ, WikiSQL, FeTaQA, StructQA) show consistent improvements over pure-text baselines, with the frozen LLM setting achieving an average relative gain of 42.65%.

## Strengths

1. **Novel hypergraph-as-modality design with permutation invariance.** Section 2.2 formalizes table structure as a hypergraph where leaf cells are nodes and hierarchical containers (rows/columns/headers) are hyperedges. The encoder uses multiset functions (Equations 1–3, parameterized via Set Transformer) that are permutation-invariant by construction. This is a principled departure from serialization-based methods that lose structural information.

2. **Consistent large improvements across five benchmarks.** Table 2 shows TAMO outperforms pure-text baselines in every setting (frozen LLM, LoRA, SFT) on HiTab, WikiTQ, WikiSQL, FeTaQA, and StructQA. The multi-dataset evidence demonstrates generalizability beyond a single task.

3. **StructQA as a diagnostic benchmark.** Section 3.1 introduces the first open-source benchmark targeting table structure understanding, with 5 task types and 7,500 QA pairs. The probing experiment (Figure 2) reveals that even GPT-4's answer consistency drops below 40% under row/column permutation, quantitatively validating the motivation that current LLMs lack structural understanding.

4. **Quantified robustness to permutation.** On StructQA under random row/column shuffling (Figures 2 and 6), TAMO maintains substantially higher answer consistency than pure-text baselines, directly demonstrating that the hypergraph encoding preserves the permutation invariance property that serialization loses.

5. **Efficiency and scalability.** Figure 7 shows TAMO (frozen LLM) runs faster per epoch than LoRA, and TAMO+LoRA adds only ~10% overhead. Table 3 shows TAMO improves both TableLlama (+26.99%) and Mistral-7B (+9.98%) on WikiTQ, confirming generalizability across backbones.

6. **Attention interpretability.** Figure 5 provides interpretable evidence that the injected [table structure token] shifts the LLM's attention toward the correct answer cell, demonstrating that the structural features actually guide reasoning rather than just adding parameters.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The 42.65% average relative gain requires clarification on computation methodology.** The paper claims "an average improvement of +42.65% over inputting pure text modality on the frozen LLM setting" (abstract and Section 3.3) and "a maximum improvement of +86.06% on the HiTab dataset." The paper does not specify which baseline (Inference Only or Prompt Tuning) is used as the denominator, how the average across datasets is computed, or whether relative gain is averaged across datasets or computed from aggregate numbers. Since the reviewer's approximate calculation (~68.5% using Prompt Tuning baseline values) does not match the stated 42.65%, the authors should explicitly state the formula and baseline definition to resolve the inconsistency. (*Verifiable from the paper: the claim appears in the abstract and Section 3.3, but no formula or baseline specification is given.*)

2. **Missing hyperparameter details for prompt tuning baselines.** The Prompt Tuning baseline is the main trained competitor in the frozen LLM setting, but the paper does not report the number of soft prompt tokens, learning rate, training epochs, or whether early stopping was used. Without this information, it is difficult to assess whether the comparison is maximally favorable to the baseline. (*Verifiable from the paper: Section 3.2 describes the Prompt Tuning baseline but no implementation details are given.*)

3. **No variance or significance estimates.** All main results (Table 2, Table 3) are reported as point estimates without standard deviations, confidence intervals, or significance tests. While single-run evaluation on large benchmarks is common in this field, the absence of any variance information makes it harder to assess the reliability of the reported gains. (*Verifiable from the paper: Table 2 and Table 3 list only point values.*)

4. **Hypergraph construction for hierarchical tables needs a concrete example.** The paper defines leaf cells as nodes and branch cells as hyperedges, but does not give a worked example showing how multi-level headers map to hyperedges (e.g., whether a header spanning multiple columns is a single hyperedge or multiple, and how nested headers are handled). Figure 3 shows a flat table, not a hierarchical one. While the principle is clear enough for reproducibility, a specific example would significantly improve clarity. (*Verifiable from the paper: Section 2.2 lines 56–68 describe the construction but Figure 3 illustrates only a flat table.*)

### Trivial
- The phrase "This work is the first to input table structures into LLMs" (Figure 1 caption) could be moderated to acknowledge parallel or prior work more precisely, though the claim of first to treat tables as a *separate modality* with a dedicated encoder appears defensible given the cited literature.

## Nice-to-Haves
- **Ablation on the hypergraph structure** — comparing against a simpler graph (pairwise edges) or flat attention over cells would isolate the benefit of set-based hyperedges and directly validate the "set-based hierarchy" motivation.
- **Number of structure tokens analysis** — Section 3.8 shows 2+ tokens work similarly. A finer-grained study (e.g., values between 1 and 5) could reveal the optimal configuration.
- **Failure analysis** — a broader analysis of when TAMO fails (e.g., very large tables, cell-value-dominated vs. structure-dominated queries) would strengthen the claims.

## Removed Points
- **Permutation invariance criticism** (Critical Issue #1 from the harsh critic): REMOVED. The criticism claims the hypergraph representation is not permutation-invariant because "hyperedges are re-wired" when rows are swapped. This is factually incorrect. The hypergraph structure changes isomorphically under permutation, but the encoder processes all information through multiset functions (Set Transformer, Eqs. 1–3) that are permutation-invariant by construction, and the final mean pooling is also permutation-invariant. Tracing through the computation confirms that node-level and table-level representations are identical before and after permutation. The empirical robustness results (Figures 2, 6) further validate this.

- **StructQA fairness (inference-only comparison)**: REMOVED. The paper presents inference-only as a reference baseline; the fair comparison is Prompt Tuning (also trained). This is standard practice in the field.

- **TableLlama prompt tuning suspicion**: REMOVED. The paper explicitly addresses this at lines 192–193: "The minimal gap (0.0016 acc.) between the base and prompt tuning on TableLlama indicates that the supervised fine-tuned LLMs already possess a strong capability to follow tabular format instructions. Consequently, prompt tuning has a limited effect."

- **Data contamination concern about StructQA using WikiTQ tables**: REMOVED. The paper acknowledges this and notes StructQA mitigates contamination "to a certain extent" because the task format (cell location, column lookup, etc.) is new and different from the original WikiTQ QA pairs.

- **MLP compresses to one token bottleneck**: MOVED to Nice-to-Haves. Section 3.8 already investigates token count and shows 2+ tokens perform similarly.

- **Missing related works**: REMOVED per policy (no external sources to verify).

- **Formatting nitpicks, typos, missing appendix content**: REMOVED per policy (parser artifacts).

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Clarify the 42.65% computation** — explicitly state which baseline is used (Prompt Tuning), the formula for relative gain (per-dataset then averaged, or aggregate), and optionally recompute with the clarified methodology to confirm the number.
2. **Report prompt tuning hyperparameters** — number of soft tokens, learning rate, epochs, and whether early stopping was used.
3. **Add variance estimates** — even a single paragraph stating that standard deviations over 3 seeds were below a certain threshold would substantially strengthen the evaluation.
4. **Include a concrete hierarchical table example** — show how a table with multi-level headers (like those in HiTab) maps to hypergraph nodes and hyperedges.
