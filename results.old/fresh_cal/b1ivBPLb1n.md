Here is my consolidated final review.

---

## Summary

This paper introduces BigDocs, a large-scale (7.5M image-text pairs) multimodal dataset for document understanding, curated from 16 permissively-licensed datasets. It also presents BigDocs-Bench, a benchmark suite of 10 structured-output generation tasks (HTML, LaTeX, SVG, etc.), along with a toolkit and trained models. The core contribution is a license-permissive, traceable dataset that aims to fill a gap in open document-training data for commercial and academic use.

## Strengths

- **Thorough license-first curation process that addresses a genuine gap.** The paper systematically surveys 133 datasets, filters out 72.5% with non-permissive or unclear licenses, and retains only those with permissive terms (Section 3.1, "License Filtering"). This directly addresses the documented barrier that ~80% of existing document datasets have restrictive or unclear licensing.

- **New benchmark suite targeting structured code output from images.** BigDocs-Bench introduces 10 tasks (Screenshot2HTML, Table2LaTeX, Image2SVG, Image2Flow, etc.) with 329k training samples focused on long-format code generation — a task type poorly covered by existing document benchmarks that center on QA or OCR (Section 4, Table 1). Tasks like GUI reasoning and flowchart extraction address real-world use cases.

- **Controlled comparison against DocStruct4M shows consistent improvements across architectures.** Under an identical training protocol (CPT on BigDocs vs. DocStruct4M, then FT on DocDownStream), models trained on BigDocs achieve higher average scores across 12 general document benchmarks for all four tested architectures (DocOwl1.5-8B, Qwen2VL-2B, Phi-3.5-Vision-4B, LLaVa-NeXT-7B) (Table 2). This provides clean evidence that BigDocs' curation and coverage translate to measurable gains.

- **Human evaluation shows a BigDocs-trained 4B model beating GPT-4o on Table2LaTeX.** In a human study with 28 annotators and 1,900 judgments, Phi3.5-Vision fine-tuned on BigDocs achieves a 63% win rate (31% draw) over GPT-4o on Table2LaTeX generation (Figure 4). This demonstrates that a small open model equipped with a permissive training dataset can outperform a leading closed-source system on a specific generation task.

- **Unified metadata framework for traceability.** The paper introduces a metadata system that separately tracks image licenses and annotation licenses, documents all transformations applied, and provides systematic provenance — described as the first such approach for visually rich documents (Section 3.2).

## Weaknesses

### Fatal
None.

### Major

- **The "permissively-licensed" claim is in tension with included "Fair Use" components, and the conclusion overstates the licensing uniformity.** Section 3.1 acknowledges that some included datasets (e.g., OCR-VQA) have images under "Fair Use" — a US legal doctrine, not a license, and one that does not guarantee redistribution rights. The paper documents this in metadata, which is good practice. However, the Conclusion (line 204) states "All BigDocs artifacts will be freely available under permissive licenses," which contradicts the earlier caveat. Users relying on the headline claim for commercial deployment could be misled. The paper should either clearly delineate which components are truly permissive vs. use-at-your-own-risk, or replace/remove the problematic components. This does not invalidate the dataset's value (most of it is genuinely permissive, and the documentation is transparent), but it does mean the central claim needs qualification.

- **Comparisons against GPT-4o are presented without sufficient caveat, inflating the headline results.** The abstract states that training with BigDocs "improves average performance up to 25.8% over closed-source GPT-4o." However, GPT-4o was evaluated "off-the-shelf" (zero-shot, line 173), while the BigDocs model received task-specific fine-tuning. This is a standard experimental design choice — comparing a specialized fine-tuned model against a general-purpose model — but the framing in the abstract and introduction omits the zero-shot caveat, making the improvement appear more dramatic than it is. The controlled comparison against DocStruct4M (same protocol) is the clean evidence; the GPT-4o comparison should be framed as "a 4B model fine-tuned on BigDocs can match or exceed GPT-4o zero-shot," which is itself an interesting finding.

- **Contamination analysis is image-only; text-level overlap is not assessed.** The contamination check uses CLIP-based image similarity (Section 3, Figure 3), which is reasonable for detecting near-duplicate images. However, for document understanding tasks, text-level contamination (overlap between training captions/QA pairs and evaluation questions/answers) is arguably more critical — especially since the paper acknowledges BigDocs contains training splits of TabFact, WTQ, and TextVQA (line 104). The radar plots also show BigDocs having *higher* contamination than DocStruct on MMMU and DudeMini, which is not discussed. At minimum, the paper should report text-level n-gram overlap or explicitly caveat the scope of the analysis.

### Minor

- **DocDownStream — used in the two-stage training pipeline — is never described.** The training protocol (Section 5.1) mentions fine-tuning on "DocDownStream" for instruction alignment, but the paper does not specify what tasks it contains, its size, or its license status. This is a reproducibility gap: readers cannot assess what confounds might be introduced by this uncharacterized stage.

- **Human evaluation lacks inter-annotator agreement reporting.** The study involves 28 evaluators and 1,900 annotations (Section 5.3), but no agreement metrics (e.g., Cohen's kappa) are reported, making it difficult to assess annotation reliability.

- **The "10 novel tasks" claim is slightly oversold.** While most tasks are genuinely new, GUI2UserIntent is explicitly repurposed from SeeClick (line 139), and Image2Flow uses LLaMA 3.1-generated data without independent validation of the synthetic ground truth (line 132). The paper should more clearly distinguish entirely new datasets from reformatted/adapted ones.

- **Tree Edit Distance for Screenshot2HTML is acknowledged as limited, but the paper does not validate whether it correlates with human judgment.** The metric operates on DOM structure, which may not capture visual fidelity well. Human evaluation partially mitigates this, but a correlation analysis between TE Dist. and human preference would strengthen the metric's credibility.

- **The hidden test set is mentioned (line 117) but never used in reported results.** Its purpose and whether results would change with it are unclear.

### Trivial
- None that warrant listing here (parser artifacts that exist in the extracted text do not appear in the original submission).

## Nice-to-Haves

- **Subsample BigDocs to match DocStruct4M's size (4M) and rerun the comparison.** This would disentangle whether improvements come from curation quality or scale.
- **Add an ablation isolating the contribution of the CPT stage from the DocDownStream/FT stage.** This would help users understand which component of the pipeline drives gains.
- **Report text-level contamination** (e.g., longest common substring or n-gram overlap between training captions and evaluation questions).
- **Validate the synthetic flowchart data** used in Image2Flow (generated by LLaMA 3.1) by spot-checking against human annotations.

## Removed Points
These points were raised by reviewers but removed with justification:
- **"Fair Use issue is a structural/fatal flaw"** — Kept as Major instead of Fatal because the paper is transparent about the issue, documents it in metadata, and the majority of the dataset is genuinely permissive. The contradiction with the Conclusion statement is the real problem, not the presence of Fair Use components themselves.
- **"Two-stage training introduces uncontrolled advantage that undermines core comparison"** — Demoted from Major to Minor because the primary comparison (BigDocs vs. DocStruct4M) uses an identical protocol so the comparison is fair. Only the GPT-4o framing is problematic, captured in a separate Major point.
- **"Code availability cannot be verified (paper says upon acceptance)"** — Removed per hard rule: cited entities and their release plans are assumed to exist as stated.
- **"Missing appendix content, proofs, references"** — Removed per hard rule: these are known PDF-to-text parser artifacts.
- **"Related works missing"** — Removed per hard rule: the reviewer has no external source to verify this.
- **Various formatting nitpicks and typos** — Removed per hard rule.
- **"Paper needs larger dataset / more models"** — Removed as generic one-size-fits-all criticism; the dataset size (7.5M) and model zoo (4 architectures) are already adequate.
- **Strength Finder's generic/unsupported strengths** (e.g., "addresses an important problem," "targets an interesting question") — Removed as generic/superficial.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. **Qualify the licensing claim precisely.** Replace the blanket "permissively licensed" statement in the Conclusion with language that explicitly notes the small number of Fair-Use components and directs users to the metadata for per-component details. This would resolve the contradiction between the Conclusion and Section 3.1.
2. **Reframe the GPT-4o comparison throughout.** Change "improves up to 25.8% over GPT-4o" to "enables a 4B model to outperform GPT-4o zero-shot by up to 25.8%" or similar. The finding is still compelling without inflation.
3. **Add text-level contamination analysis** or explicitly limit the contamination claim to "image-level overlap."
4. **Describe DocDownStream** — even a brief paragraph listing its tasks, size, and license would significantly improve reproducibility.
5. **Report inter-annotator agreement** for the human evaluation.
6. **Clarify the role of the hidden test set** — either report results on it or state it is reserved for future use.

## Score and Decision

The paper makes a genuine contribution: a carefully curated, largely permissive-licensed document dataset and a benchmark suite targeting an underexplored task family (structured code output from images). The controlled comparison against DocStruct4M provides clean evidence that the dataset's curation and coverage translate to better downstream performance. The human evaluation on Table2LaTeX is a compelling proof point for the value of permissive document training data.

However, the paper has three issues that prevent unconditional acceptance: (1) the tension between the "permissively-licensed" headline and the included Fair-Use components, particularly in the overbroad Conclusion claim; (2) the inflated framing of GPT-4o comparisons without acknowledging the zero-shot evaluation protocol; and (3) the incomplete contamination analysis (image-only). These are fixable — they require clarification, not re-execution — but they need to be addressed to ensure the paper's claims are accurate and not misleading to downstream users.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>