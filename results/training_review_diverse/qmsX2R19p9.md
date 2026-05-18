Now I have all the information needed. Let me produce the final consolidated review.

## Summary

TNT proposes a multi-modal table-language framework that replaces naive text-based table serialization with structure-aware column embeddings. It uses a table encoder with bi-dimensional attention plus a three-stage training pipeline (contrastive pre-training, multi-task feature alignment, instruction tuning) to produce compact column-level representations that LLMs can consume directly. Evaluated on NL2SQL (SPIDER and variants), TNT achieves up to 14.4% higher execution accuracy over text-based baselines, especially when column names are non-semantic. The paper also shows the approach generalizes across three backbone LLMs and is compatible with standard prompting techniques.

## Strengths

- **Novel structure-aware table encoding with meaningful empirical gains**: TNT's bi-dimensional attention mechanism produces column embeddings that genuinely capture content-driven table semantics. The strongest evidence is Table 1, where TNT achieves up to 14.4% higher EX on schemas with anonymized column names—a concrete demonstration that the representation captures structure beyond surface-level schema parsing. Section 6.4 (Table 5) further shows that TNT with just one example value outperforms text-based serialization with many values, validating the token efficiency claim.

- **Well-designed and ablated three-stage training pipeline**: The paper introduces column-wise contrastive pre-training (Section 4.1) that learns column semantics from unlabeled tables, multi-task feature alignment using five diverse objectives (Section 4.2), and instruction tuning. Ablation results (Table 3) confirm each stage contributes meaningfully—removing any stage causes drops of up to 23.4%. Figure 5 further shows that pre-training prevents shortcut learning during alignment. This is a carefully constructed pipeline where each component's role is clearly motivated.

- **Generalizability across backbone LLMs and practical compatibility**: TNT consistently improves results across LLaMA3-8B, Mistral-7B, and CodeLlama-7B (Table 2), demonstrating the representation is not tied to a single LLM. Table 6 shows TNT integrates naturally with schema filtering, code correction, and self-consistency, approaching GPT-4 performance with an 8B model—a practically meaningful result.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation on a single task undersupports the paper's broader generality claims**: The paper's rhetoric—"bridge the semantic gap between Text and Table" (abstract), "general table understanding" (Section 3 Remark), "multi-modal perspective" (Section 5), and claims about "pioneering validation of the feasibility of integrating tabular and textual modalities" (Section 5)—consistently frames TNT as a broadly applicable table understanding framework. Yet every experimental result comes from NL2SQL on SPIDER-derived benchmarks. NL2SQL is a legitimate and challenging table understanding task, but it is one specific reasoning paradigm (text-to-SQL). The paper does not evaluate on structurally different tasks such as table-based fact verification (TabFact), table-to-text generation, or open-domain table QA. The paper states it "focuses on NL2SQL as a concrete example," but this caveat is buried (line 27) and the surrounding rhetoric is not commensurate with the evidence. To credibly claim general table understanding, at least one additional distinct table reasoning task is needed. This is a real gap between claim scope and evidence, not a demand for exhaustive evaluation.

### Minor

- **The column-embeddings-vs-soft-prompts ablation does not control for training regime**: The paper compares TNT's column embeddings against soft prompts with the same parameter count (Table 4) to argue the embeddings are not just learned tokens. However, the soft prompts were only trained during instruction tuning, while TNT's column embeddings benefit from the full three-stage pipeline (contrastive pre-training + multi-task alignment + instruction tuning). The more controlled experiment would pre-train the soft prompts on the same contrastive objective and alignment data, or train TNT's column embeddings through instruction tuning alone. As presented, the comparison conflates representation quality with training regime, weakening the argument that "column embeddings truly capture high-level abstractions" (line 246).

- **No decontamination analysis between pre-training data and evaluation benchmarks**: The 86k business tables used for pre-training are described only as "from various domains, including finance, education, and medicine" (line 93). There is no analysis of whether these tables share schema overlap with SPIDER databases. If the pre-training data includes tables with similar schemas or domains to SPIDER, the reported gains could partly reflect data similarity rather than generalizable table understanding. A simple decontamination analysis (e.g., measuring schema overlap, or showing that gains hold on truly unseen table distributions) would address this.

- **Missing standalone test-set results for TNT without auxiliary techniques**: Table 6 reports TNT combined with schema filtering, code correction, and self-consistency on SPIDER-Test, but the standalone TNT test-set performance (without these add-ons) is not reported. This makes it difficult to assess the baseline improvement on the held-out test set, as the paper reports standalone dev results (Tables 1, 2) but only combined test results (Table 6).

### Trivial

- **Overstatement in Section 5**: The claim of "pioneering validation of the feasibility of integrating tabular and textual modalities" (line 130) is too strong given prior work on table-aware LLM architectures (e.g., TAPAS, TAPEX, TableLlama, Table-GPT, and MLLMs with table support). The paper's novelty lies in its specific design choices (column-wise contrastive learning, bi-dimensional attention for LLM integration), not in being the first to combine tables with LLMs. The related work section (Section 7) acknowledges these prior efforts, making the "pioneering" phrasing inconsistent with the paper's own survey.

## Nice-to-Haves

- Adding one more table understanding task (e.g., TabFact for table fact verification) would substantially strengthen the generality claim. The paper's claim architecture and training are task-agnostic, so this should be feasible without retooling the framework.
- A t-SNE or UMAP visualization of the learned column embeddings, showing that semantically similar columns cluster together even when column names are anonymized, would make the representational quality claim more directly interpretable.
- Reporting standard errors over 3 runs would increase confidence, though single-run evaluation is common in NL2SQL.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Baselines are too weak; should include TableLlama, Table-GPT, etc."**: The paper compares TNT against text-based serialization using the same backbone LLMs. This is the appropriate comparison for evaluating representation quality—TableLlama and Table-GPT are full instruction-tuned systems designed for different objectives. Comparing against them would conflate representation quality with instruction-tuning quality and base model choice. The paper's baselines are standard and appropriate for the claim being tested.

- **"Asymmetric comparison in Table 1 (TNT gets content, text gets only names)"**: The headline 14.4% gain on non-semantic schemas compares TNT (using column embeddings that encode cell content) against text baselines without cell values. This IS the point of the paper—column embeddings should encode content better than text can. The paper provides a controlled comparison in Table 5 where both TNT and text baselines receive the same number of example values, and TNT still wins. The asymmetric setup in Table 1 is a deliberate stress test of the representation, not a rigged comparison.

- **"Missing implementation details (number of attention layers, hidden dimensions, learning rates, etc.)"**: The paper's reproducibility statement (line 276-280) notes that all source code and resources are in the supplementary materials, which is standard practice. The paper provides the key architectural decisions (sentence transformer = all-MiniLM-L6-v2, k=5 learnable queries, three LLM backbones, temperature=0 for decoding).

- **"No statistical significance tests"**: Single-run evaluation on NL2SQL benchmarks is the community standard; the paper uses temperature 0 decoding to eliminate randomness. Requesting confidence intervals or multi-run significance tests is a methodological preference, not a standard requirement for this task.

- **"Non-semantic column experiment should use real enterprise databases"**: The paper's anonymization of 80% of column names is a reasonable and controlled proxy. Demanding real enterprise data is scope creep beyond what an academic paper can reasonably provide.

- **"The paper should be a major revision, not ready for acceptance"**: This is a judgment call from the harsh reviewer, not a specific weakness. The paper's contribution is solid and the evaluation, while limited to one task, is rigorous within that scope.

## Novel Insights

The most interesting observation from the reviews is that TNT's column-wise contrastive pre-training (Section 4.1) is the key enabler for the non-semantic schema results. The ablation showing that removing pre-training causes a sharp loss decline during alignment (Figure 5) suggests the pre-training teaches the encoder to build column representations that are robust even when schema names provide no signal. This insight—that the pre-training stage prevents shortcut learning on schema patterns—is well-supported and is arguably the paper's most important finding beyond the overall performance numbers.

## Suggestions

1. **Add one more table understanding task**—TabFact or WikiTableQuestions—to substantiate the generality claims. This directly addresses the major weakness without requiring a full benchmark sweep.

2. **Run a controlled soft-prompt ablation** where randomly initialized tokens are trained through the same three-stage pipeline (pre-training → alignment → instruction tuning) as the column embeddings. If TNT still outperforms, the structure-aware encoding is proven beneficial; if not, the training data matters more than the architecture.

3. **Tone down the generality rhetoric** in the abstract and Section 5 (remove "pioneering validation"), or add a second task. The evaluation supports the claim that TNT improves NL2SQL table understanding; it does not yet support the claim of a general-purpose table modality.

4. **Report standalone TNT test-set results** on SPIDER-Test in addition to the combined results in Table 6, and include a decontamination analysis of the pre-training data relative to SPIDER.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>