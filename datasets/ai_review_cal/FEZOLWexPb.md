- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I will compose the final consolidated review, cross-referencing everything against the actual paper text.

## Summary

MAESTRO introduces a self-supervised set representation learning architecture for cytometry data. It combines masked autoencoding (with a novel Non-Random Block Masking strategy) with a self-distillation (teacher-student) framework, built on Set Transformer attention blocks (ISAB, PMA, SAB). The model produces fixed-dimensional immune profile embeddings from samples containing up to ~1.4M cells, handling variable set sizes and permutation invariance. Experiments on a large cytometry cohort show MAESTRO outperforming manual gating, k-means, Deep Sets, Set Transformer, and OTKE on diagnosis classification, sex classification, age regression, and cell-type distribution retrieval.

## Strengths

- **First self-supervised set representation learning architecture at cytometry scale.** The paper demonstrates processing of samples with up to 1,386,520 cells (Section 4.1), far beyond the ~10,000-cell subsampling ceiling that prior set methods (Deep Sets, Set Transformer, OTKE) require. This is a genuine methodological advance validated by the data scale reported.

- **Formal theoretical grounding.** The paper proves permutation invariance for PMA (Theorem 3) and permutation equivariance for ISAB and SAB (Theorems 2, 4), and establishes MHA's permutation properties (Theorem 1). ISAB's O(nm) complexity with inducing points (Section 3.1.2) provides the efficiency argument for handling large cytometry datasets.

- **Novel NRBM masking strategy with qualitative validation.** Non-Random Block Masking (Algorithm 1) groups semantically similar cells via cosine similarity before masking contiguous blocks. Figure 2 shows that the model reconstructs cells in UMAP regions where no unmasked input cells exist (dashed boxes), demonstrating a capability that random masking would not naturally achieve — this is a concrete qualitative demonstration of the method's behavior.

- **Consistent empirical outperformance across multiple tasks.** According to the paper's claims in Section 4.4, MAESTRO achieves superior accuracy, AUC, F1 for diagnosis/sex classification and lowest MAE, highest R² for age regression compared to all baselines, and outperforms on cell-type distribution retrieval (Figure 5). The ablation study (Table 1) further indicates that both masked modeling and self-distillation components are essential to performance.

## Weaknesses

### Fatal
None.

### Major

- **Baseline training protocol is critically underspecified.** The paper states in Related Work that "Deep Sets and Set Transformer are supervised approaches" (line 23), and in Section 4.4 that baselines receive "a random subset of 10,000 cells." But it never states whether they were (a) trained with full supervision on the diagnosis/age/sex labels and then evaluated on held-out data, or (b) adapted to a self-supervised framework. If (a), this is an apples-to-oranges comparison — a fully supervised model versus SSL + linear probing — and the paper must explicitly state this and discuss the implications. If (b), the adaptation method is not described. Without this information, the reader cannot assess whether the comparison is fair or interpret the magnitude of MAESTRO's claimed improvements. This is the most consequential weakness in the paper.

- **No numerical results are provided in text or machine-readable tables.** All quantitative evidence (Figure 4: accuracy, AUC, F1, MAE, R²; Figure 5: cell-type MAE; Table 1: ablation) is presented only as embedded figure images. No actual numbers are reported anywhere in the main text. The evaluator cannot verify the magnitudes of improvements, compute effect sizes, or compare across methods. This is an evidential presentation issue that prevents independent assessment of the paper's core claims, regardless of whether the figures are legible in the original PDF.

- **No training hyperparameters or optimization details are given anywhere in the paper.** The paper does not report learning rate, batch size, optimizer, number of ISAB layers, number of inducing points, mask ratio(s), loss weights, temperature parameters, training epochs, data splits, or any other reproducibility-critical detail. This makes the method impossible to reproduce or build upon. For a method paper claiming state-of-the-art results, this is a serious omission.

### Minor

- **Self-distillation loss function is not specified.** Section 3.2 mentions "non-linear projection heads on the latent embeddings to align representations" and Figure 1 shows the teacher-student framework, but the exact loss (e.g., cross-entropy between softmax outputs as in DINO, MSE in embedding space, or something else) is never defined. The interplay between the reconstruction loss and distillation loss — how they are weighted and combined — is also not stated.

- **NRBM motivation is implicit rather than explained.** Algorithm 1 describes the mechanism (group by cosine similarity, mask contiguous block, then shuffle), and Figure 2 shows its qualitative effect. But the paper does not provide explicit reasoning for *why* block-masking semantically similar cells is beneficial over random masking — e.g., whether it forces harder reconstruction tasks or prevents the model from exploiting local redundancy. The ablation study (Table 1) apparently tests this, but the table is inaccessible as an image.

- **No measures of uncertainty on any quantitative result.** No standard deviations, confidence intervals, or bootstrap estimates are reported for any of the accuracy, AUC, F1, MAE, or R² values. While single-run evaluation is not uncommon in large-scale benchmarks, the absence of any variability estimate weakens the reliability claims, especially given the clinical relevance of the downstream tasks.

- **Dataset characterization in the main text is minimal.** Section 4.1 provides the cell count range (11,829–1,386,520) and mentions "disease diagnostic and meta data were provided by the primary clinician teams," but does not report number of samples, class balance, number of protein markers, patient demographics, or how train/test splits were constructed. The reference to "Appendix E.3.2" for batch structure details is stripped by the parser, but the main text should include at least a basic dataset summary table.

- **Cell-type distribution retrieval baseline setup is unclear.** Section 4.4 states "Details on each implementation can be found in F.5" (a stripped appendix). The main text does not explain how k-means, OTKE, Deep Sets, and Set Transformer produce embeddings or predictions for this task — e.g., whether Deep Sets and Set Transformer were used as pre-trained feature extractors or trained directly on the cell-type distribution prediction task.

### Trivial
None (the formatting issues visible in the extracted text are parser artifacts, not author errors).

## Nice-to-Haves

- An explicit ablation comparing NRBM against random masking (with identical mask ratio) would directly quantify the value of the proposed masking strategy.
- Reporting the teacher embedding performance (linear probe) versus the student embedding performance would justify the self-distillation design choice.
- Training time / memory usage benchmarks for MAESTRO across different set sizes would strengthen the scalability claims.
- Discussing potential batch effects and how they are controlled (or why they do not confound the results) would address a known concern in cytometry studies.

## Removed Points

- **scVI/scANVI omission claim** (Harsh Critic): The critic asserts the paper ignores scVI/scANVI. The paper's claim is specifically about *set representation methods* for "cytometry set data as a compact vector" — scVI learns per-cell representations, not set-level immune profiles. The paper's scope is clearly stated and this criticism misreads the claim.

- **"First attention-based..." novelty claim is not benchmarked against Perceiver IO** (Harsh Critic): The paper benchmarks against Deep Sets, Set Transformer, and OTKE — the most directly relevant set representation methods. Demanding comparison with Perceiver IO or other domain-adapted SSL methods is scope creep; the paper's claim is narrowly scoped to "the context of single-cell data" and the relevant baselines are provided.

- **"Unfair comparison" framing for supervised baselines** (Harsh Critic): The critic argues that comparing supervised baselines against SSL + linear probing is "structurally unfair." In standard SSL evaluation practice, *outperforming supervised baselines with a linear probe is a stronger result*, not a weaker one. The real issue (which is retained as a Major weakness) is that the baseline training protocol is underspecified, not that the comparison direction is unfair.

- **Figures are low-resolution / unreadable** (Harsh Critic): The figures appear as embedded-image references in the extracted text (parser artifact). The original PDF submission would contain proper figures. However, the lack of numerical values in text is a separate valid point that is retained.

- **Missing related works** (Harsh Critic): Not included per instructions, as I cannot verify their existence externally.

- **Strength Finder generic strengths** (e.g., "this paper addressed an important problem"): Removed; only concrete, evidence-grounded strengths are retained.

## Novel Insights

The harsh critic and strength finder converge on an important structural observation: the paper's central contribution (a self-supervised set representation model at unprecedented scale for cytometry) is genuinely novel and methodologically sound, but the evaluation section fails to provide the level of detail needed to verify the claimed improvements. Specifically, neither reviewer identifies a flaw in the architecture or theory — the problems are all in the **reporting** of the experiments. This suggests the paper's intellectual contribution is real but its presentation as a publishable unit is incomplete. A second insight: the NRBM strategy occupies an interesting middle ground between random masking (too easy) and adversarial masking; the paper would benefit from explicitly framing it in these terms rather than leaving the motivation implicit.

## Suggestions

1. **Specify the exact baseline training protocol.** State explicitly: were Deep Sets and Set Transformer trained with full supervision on each prediction task, or adapted to self-supervision? If supervised, acknowledge this and discuss why outperforming them with SSL + linear probing is meaningful. If self-supervised, describe the adaptation.
2. **Add a proper numerical results table** (in the paper, not an image) reporting accuracy/AUC/F1/MAE/R² for all methods on all tasks, ideally with means and standard deviations over multiple runs or cross-validation folds.
3. **Report all training hyperparameters** in a table: learning rate, batch size (or sampled N per batch), optimizer, number of layers/heads/inducing points, mask ratio ρ, loss weights, temperature parameters, number of epochs, and train/validation/test split sizes.
4. **Specify the loss function for self-distillation** and describe how the reconstruction loss and distillation loss are combined.
5. **Provide an explicit ablation of NRBM vs. random masking** at the same mask ratio to quantify the benefit of the semantic grouping strategy.
6. **Include a basic dataset summary** (number of samples per diagnosis class, number of protein markers, train/val/test split definition) in the main body.
