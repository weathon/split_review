Now I'll produce the final review.

## Summary

ZerOmics proposes a framework that adapts LLMs to single-cell analysis via dual-alignment: pre-training an SC encoder to align expression profiles with gene text summaries, then multi-task instruction-tuning an LLM (LLaMA2-13B) on labeled SC tasks. The goal is cross-dataset and cross-task generalization without fine-tuning on target datasets. The paper evaluates cell type annotation, rare cell identification, tumor cell discovery, and cell pathway inference across diverse sequencing technologies.

## Strengths

- **Novel dual-alignment pipeline with ablation support**: Aligning SC expression data with gene text summaries during pre-training, then aligning SC embeddings with the LLM via multi-task instruction tuning, is technically well-motivated. The ablation study (Table 5) verifies that each component — text summaries, the SC model, the SC tokenizer, and the mixture of LoRAs — contributes positively, with all variants underperforming the full model.

- **Cross-dataset generalization across diverse sequencing technologies**: Table 1 reports that ZerOmics achieves best or second-best cell-type annotation on four datasets spanning 10x scRNA-seq, Smart-Seq2, 10x scATAC-seq, and MERFISH, while fine-tuned baselines (scGPT, scBERT, Geneformer) degrade sharply on the unseen modalities (scATAC-seq, MERFISH). This demonstrates generalization beyond the technologies seen in prior pre-training corpora.

- **Cross-task transfer to an unseen task**: Section 4.3 shows ZerOmics can perform cell pathway inference (CPI) — a task not seen during instruction tuning — reaching competitive performance against fine-tuned Geneformer in the zero-shot setting, and surpassing LangCell-CE after 10-shot tuning. This is a genuinely demonstrated emergent capability.

- **Systematic LLM scalability analysis**: Section 4.5 evaluates five LLM variants (LLaMA2-7B/13B/70B, LLaMA3-8B/70B), showing consistent gains with model size. The finding that LLaMA3 does not consistently outperform LLaMA2 provides a non-obvious insight about model capacity vs. pre-training data quality for this domain.

## Weaknesses

### Fatal
None.

### Major

1. **Model scale confound between ZerOmics and baselines is not controlled.** ZerOmics uses LLaMA2-13B (13B parameters), while the SC-specific baselines (scBERT, Geneformer, scGPT, scFoundation, LangCell) are orders of magnitude smaller. The paper ablates LLM size within ZerOmics (Section 4.5) but never benchmarks these smaller LLM variants against the SC baselines on the same tasks. Consequently, the reader cannot determine whether performance gains come from the proposed pipeline or simply from the vastly larger backbone. A controlled experiment running ZerOmics with a 7B backbone and comparing directly to the SC baselines on the same tasks is absent. This undermines attribution of the reported improvements to the dual-alignment pipeline.

2. **Data overlap between instruction tuning and evaluation is never specified.** The paper collects 91.5M cells for instruction tuning (Sections 3.2, 4.1) but never states whether the evaluation datasets (PBMC68K, Pancreas, BMMC, MOP, Airway, CTC, LungCancer, HDHC, Liver) are held out. If the model was instruction-tuned on PBMC68K cells and then evaluated on PBMC68K, the "cross-dataset" claim collapses into held-out test performance within a multi-task learning setup. The same concern applies to the CPI evaluation (RQ2): the paper does not clarify whether HDHC/Liver cells or related pathway information appeared in the 91.5M instruction-tuning pool. This omission directly threatens the validity of the cross-dataset and cross-task generalization claims. The paper must clarify these splits.

### Minor

1. **"Zero-shot" framing is imprecise.** The paper repeatedly describes ZerOmics as a "zero-shot method" that "does not rely on specific downstream data" (abstract, Section 1), yet Stage 2 performs supervised multi-task instruction tuning on labeled datasets from multiple downstream tasks. The evaluation demonstrates cross-dataset and cross-task generalization after supervised multi-task training — a legitimate and valuable capability — but this is not "zero-shot" in the sense of solving unseen tasks from instructions alone without task-specific labeled data. The title, contributions, and motivation all lean on this framing, which sets inaccurate expectations.

2. **"First" claim is contradicted by the paper's own related work.** The paper claims "the first zero-shot method" and "the first general model based on LLMs for SC multi-omics analysis." Yet Section 2.2 discusses LangCell, which "demonstrat[es] initial 'representation' abilities in zero-shot and few-shot scenarios," and Cell2Sentence, which directly uses language models for SC analysis. The paper should state the precise novelty (first to use multi-task instruction tuning with dual-alignment for LLM-based SC analysis) rather than claiming primacy broadly.

3. **No statistical significance or variance reporting.** All main results (Tables 1–5) are reported as point estimates without standard deviations, confidence intervals, or number of runs. For a paper making comparative claims ("best or second-best," "surpassing SOTA"), this prevents assessing whether observed differences are meaningful or within noise.

4. **Key baselines from related work are not evaluated.** Cell2Sentence and BioTranslator are discussed in Related Work (Section 2.2) as the closest prior works integrating text or LLMs for SC analysis, yet neither appears in the experimental comparisons. This weakens the empirical positioning.

5. **CPI comparison is asymmetric.** In Table 4, ZerOmics (zero-shot) is compared against Geneformer and LangCell-CE that have been fine-tuned on CPI. The more informative comparison — against zero-shot/off-the-shelf versions of those baselines on CPI — is not provided.

### Trivial

1. The explanation for why LLaMA3 does not consistently outperform LLaMA2 ("ZerOmics benefits more from larger models capable of capturing complex interactions... rather than from merely expanding the LLM's knowledge base") is post-hoc and unsupported by any analysis. This is a minor interpretative overreach in one paragraph.

## Nice-to-Haves

- An ablation testing whether the dataset abstract in instructions is actually informative, or whether instructions without it perform similarly.
- An ablation testing whether the broadcasting addition design (same gene text embedding applied to all cells) could be improved by incorporating cell-specific gene context.

## Removed Points

These points were raised by reviewers but are removed or demoted for the reasons stated:

- **Tables are embedded as images, cannot extract values**: Parser limitation, not a paper flaw.
- **Gene corpus number "$43.3" is garbled**: Parser artifact; the original paper has the correct value.
- **SC Model architecture details missing**: The paper references prior work ("Yang et al.") and supplementary sections that were stripped. This is standard practice for conference papers.
- **Broadcasting addition "loses cell-specific gene context"**: This is a design choice with a stated rationale (computational efficiency, providing static gene functional information). It is not self-evidently a weakness.
- **Instruction template ablation requested**: This is an additional experiment suggestion, not a weakness in the current paper.
- **"Zero-shot" framing is "fatal"**: The critic characterized this as fatal, but cross-dataset generalization after instruction tuning is a legitimate usage in the transfer learning literature, and the cross-task CPI experiment genuinely demonstrates zero-shot transfer. The issue is imprecision in framing, not invalidity of the approach.

## Novel Insights

The most striking pattern across the reviews is the tension between the paper's genuine technical contribution — a dual-alignment pipeline that couples gene text with expression data before feeding into an instruction-tuned LLM — and evaluation choices that prevent clean attribution of the reported gains. The cross-task CPI result (Section 4.3) is the paper's strongest evidence of emergent capability, yet it is undercut by the absence of zero-shot baselines and uncontaminated held-out data. The scalability study is informative but stops short of the controlled comparison needed to separate pipeline effects from scale effects. The paper would benefit most from tightening evaluation design (data split transparency, model size controls) rather than adding more tasks or ablations.

## Suggestions

1. **Explicitly state which datasets are in the instruction tuning set and which are held out.** Provide a table mapping every evaluation dataset to its usage (pre-train only, instruction-tune, evaluation), and clarify whether the 91.5M instruction-tuning cells overlap with any evaluation data.
2. **Run a controlled experiment with a 7B LLM backbone** and compare directly to the SC-specific baselines (scGPT, Geneformer, LangCell) on the same tasks, controlling for model scale. Alternatively, show that fine-tuning the SC baselines with the same instruction-tuning protocol narrows the gap.
3. **Reframe the contribution precisely**: replace broad "zero-shot" claims with "cross-dataset and cross-task generalization via multi-task instruction tuning," and specify in what respect ZerOmics is first (e.g., first to use multi-task instruction tuning with dual-alignment for LLM-based SC analysis).
4. **Report all main results with standard deviations** over at least 3 runs.
5. **Include zero-shot baselines** for the CPI experiment — evaluate Geneformer and LangCell off-the-shelf on CPI without fine-tuning.
6. **Include Cell2Sentence and BioTranslator** in the main evaluation, as they are the closest prior LLM-based SC methods.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>