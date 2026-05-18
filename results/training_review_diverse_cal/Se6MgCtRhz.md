Now I have a thorough understanding of the paper and can verify all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces Herald, a framework for generating a large-scale Natural Language–Formal Language (NL-FL) dataset from Mathlib4 (Lean 4). The pipeline incorporates structural information — dependency-graph ordering, neighbor statements, docstrings, and retrieved examples — to produce high-quality NL translations of formal statements and proofs. A dual augmentation strategy (tactic-based decomposition of proof states + LLM-based paraphrasing) expands the dataset to 580k NL-FL statement pairs and 44k proof pairs. The authors fine-tune DeepSeek-Prover-Base 7B on this dataset and report 93.2% accuracy on miniF2F-test statement formalization, outperforming baseline models.

## Strengths

1. **Novel dependency-level translation order.** The paper identifies a real failure mode in prior work — LLMs fabricating missing dependent definitions — and addresses it by extracting a DAG of theorem dependencies from Mathlib4 and informalizing in dependency order (Section 3.1.1). This hierarchical approach is principled and likely improves translation quality by ensuring that dependent definitions have already been translated before the target theorem is processed.

2. **Large-scale dataset with multi-source augmentation.** Tactic-based augmentation (Section 3.2.1) extracts localized sub-goals from intermediate proof states, validated through the Lean compiler, generating 580k valid formal statements from 110k original theorems. Combined with LLM-based paraphrasing (rewriting, abstraction, omission, multilingual translation), this substantially expands data coverage beyond prior datasets like MMA (88k) or Lean Workbook. The scale alone (580k statement pairs) is a significant resource for the community.

3. **Rigorous multi-stage validation pipeline.** The validation pipeline (Section 4.1.2) couples compiler checks for syntactic validity with LLM-based back-translation and NLI checks for semantic fidelity. This four-step verification is more robust than relying on a single signal, and is well-motivated for ensuring that autoformalized statements are both syntactically correct and meaning-preserving.

4. **Real-world formalization demonstration.** The successful formalization of a Stacks Project section (Normal Extensions in field theory) into runnable Lean 4 code with only two theorem modifications needed (Section 4.3) provides concrete evidence that the pipeline transfers beyond benchmark datasets to graduate-level mathematics. This is a non-trivial and compelling case study.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled baseline comparison.** The paper reports that baselines (TheoremLlama, InternLM2-Math-Plus-7B, Llama3-instruct) underperform the Herald translator by large margins (e.g., 93.2% vs. 73.0% on miniF2F-test), but does not specify whether these baselines were evaluated under the *exact same* Pass@128 protocol with the complete 4-step validation pipeline (compiler check + back-translation + NLI). The footnotes to Table 1 mention ad-hoc adaptations — manually adding headers, truncating outputs to extract statements — which suggest the evaluation protocol was not uniform. Without confirmation that all baselines were given the same number of samples, the same temperature settings, and the same validation pipeline, the reported margins could partially reflect methodological artifacts rather than genuine superiority. The paper's central empirical claim is weakened by this ambiguity.

2. **No training-test overlap analysis.** The Herald training set is derived from Mathlib4, and miniF2F is also partly drawn from Mathlib4. The paper does not conduct or even mention any deduplication check — by name, signature, or statement content — between the training data and the evaluation sets (miniF2F, Extract Theorem, College CoT). Given the dataset scale (580k statement pairs), the risk of systematic overlap is non-negligible, and its absence undermines confidence in the reported accuracy numbers. This is a standard expectation for any empirical paper that trains on a corpus and tests on a benchmark derived from the same ecosystem.

### Minor

1. **Augmentation quality is unvalidated.** Tactic-based augmentation decomposes proof states into localized statements, and LLM-based paraphrasing generates alternative phrasings. However, no human evaluation or systematic quality check is performed on these augmented statements. The paper asserts they address "distribution imbalance" (Section 3.2), but provides no evidence about whether the augmented statements are mathematically well-formed, non-trivial, or whether the multilingual translations (Chinese, French, Russian) are correct. Random subsampling addresses redundancy, not quality.

2. **Proof pairs (44k) created but not used in the main experiment.** A full subsection (3.1.2) describes proof informalization in detail, but the Herald translator is trained only on statement pairs. This creates a disconnect between the paper's description of its pipeline and the actual experiment. While releasing the proof pairs as a dataset resource is valuable, integrating them into the central experiment — even as an ablation — would strengthen the paper.

3. **Retrieval pipeline lacks reproducibility details.** The embedding model used for the 1,000 manually annotated examples and the larger search (Section 3.1.1) is never named. The reader is directed to "previous work" (gao2024) but no specific model identifier is given, making it impossible to reproduce the retrieval step.

4. **Human feedback iteration lacks quantitative measurement.** The six-round expert feedback process (Section 3.1.1) is described qualitatively — "over a dozen principles" were developed — but no before/after comparison is provided to demonstrate improvement. A small held-out set evaluated pre- and post-feedback would substantiate the claim.

5. **Internal test sets are under-documented.** Extract Theorem and College CoT are central to the evaluation (Table 1) but are described in only two sentences each (Section 4.1.3). Sample sizes (200 each), collection methodology, topic distribution, and the exact definition of "accuracy" for these datasets are not detailed, making the reported numbers difficult to interpret or reproduce.

6. **Numerical inconsistencies between narrative and table.** The abstract reports InternLM2-Math-Plus-7B at 74.0% on miniF2F-test, while Table 1 shows 73.0%. The introduction and contributions list TheoremLlama at 55.0%, while Table 1 shows 50.1%. These discrepancies, though small, erode attention to detail.

### Trivial
- Line 22 has a stray ".5" character: "55.0\% and 4.0\%).5 \citep{deepseekproverv15}" — likely a PDF extraction artifact.

## Nice-to-Haves
- Reporting Pass@1 alongside Pass@128 would give a meaningful lower bound on model reliability.
- An ablation study removing key pipeline components (dependency ordering, neighbor statements, retrieval) would demonstrate their individual contributions.
- Full proof generation results on miniF2F (statements + proofs) would connect the Herald pipeline to the community's standard evaluation setup and better justify the proof-level dataset.
- A human evaluation of a sampled subset of Herald's NL-FL statement pairs (e.g., 200 samples, two annotators, inter-annotator agreement) would directly substantiate the claim that Herald is more "reliable" than prior datasets.

## Removed Points

- **"The evaluation is statement formalization, not theorem proving; standard use of miniF2F is for full proof generation"** — This evaluates the paper against a task it does not claim to solve. The paper's stated scope is statement formalization, and evaluating on statement-level miniF2F is a valid (if narrower) use of the benchmark. The fair-comparison concern above is retained; this framing critique is removed.
- **"The ad-hoc modifications (adding headers, truncating outputs) likely disadvantage baselines"** — This is speculation rather than verified fact. The underlying concern about protocol equivalence is retained as Major weakness #1.
- **"Proof pairs are not used in the main experiment, creating a disconnect"** — Retained as Minor weakness #2, but the reviewer's framing of this as a major structural flaw is overblown; the dataset itself is a contribution, and the paper clearly scopes its experiment to statement formalization.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's ambitious pipeline (including proof-level data generation) and its narrow experimental validation (statement formalization only), but this observation is implicit in the paper itself.

## Suggestions

1. **Run the baselines under the exact same Pass@128 protocol with the identical 4-step validation pipeline**, and report whether the numbers change. This is the single most important action to secure the paper's empirical claims.

2. **Perform and report a deduplication analysis** between the Herald training set (including augmented statements) and each test set (miniF2F, Extract Theorem, College CoT). At minimum, check theorem-name overlap and statement-signature overlap.

3. **Specify the embedding model** used for the retrieval pipeline (Section 3.1.1) to enable reproduction.

4. **Provide more detail on Extract Theorem and College CoT**: exact collection methodology, size, difficulty distribution, and how "accuracy" is defined for each. Add these to an appendix.

5. **Correct the numerical inconsistencies**: both InternLM2 (74.0%→73.0%) and TheoremLlama (55.0%→50.1%) numbers in the introduction, abstract, and contributions should be harmonized with Table 1.

## Score and Decision

The paper presents a novel, well-motivated pipeline and produces a large-scale dataset that is a genuine community resource. The core ideas — dependency-ordered translation, structural context, tactic-based decomposition — are sound and likely to be influential. However, the evaluation is under-validated in two critical respects: the baseline comparison is not confirmed to be protocol-controlled, and no training-test overlap check is performed. These issues are addressable but currently weaken the paper's central empirical claims. The contributions are real, but the evidence for them requires tightening.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>