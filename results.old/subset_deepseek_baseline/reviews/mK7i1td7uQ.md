## Summary

The paper introduces ConforFormer, a foundation model for molecular representations that learns to produce task-agnostic frozen embeddings by explicitly accounting for conformer diversity via contrastive learning. Built on the Uni-Mol 3D-transformer backbone, the model is trained with an NT-Xent loss that pulls together embeddings of different conformers of the same molecule while pushing apart those of different molecules. The resulting 512-dimensional embeddings can be frozen and used directly (with a simple MLP head) for property prediction and similarity search. The authors also introduce PharmIsomer, a benchmark for evaluating isomer/conformer discrimination, and show that their contrastively trained models can infer molecular graph-like features from 3D geometries alone.

## Strengths

- **Novel problem framing**: The paper is the first to explicitly incorporate conformer diversity as a contrastive learning objective within a molecular foundation model, addressing a genuine physical reality—molecules exist as ensembles of 3D structures—rather than relying solely on 2D graphs or single 3D geometries.
- **Clean methodology**: The contrastive objective (NT-Xent) is well-motivated, clearly defined, and integrated into the Uni-Mol pre-training in a principled way with a weighted multi-task loss. The use of weakly supervised signal (conformer pairs) without injecting graph structure is elegant.
- **Rigorous analysis of frozen embeddings**: The paper thoroughly examines the trade-off between stability and performance when freezing the backbone, showing 2-3× lower standard deviation in classification benchmarks. This is practically valuable for small real-world datasets.
- **PharmIsomer benchmark**: The new benchmark for discriminating conformers from isomers is a useful contribution. The demonstration that contrastive training dramatically improves this discrimination (from 8% to 83% precision at 50% recall) provides compelling evidence that the model learns molecular graph structure implicitly.
- **Reproducibility**: The authors provide code, model weights on HuggingFace, and dataset samples, and they carefully document their replication efforts and deviations from Uni-Mol.

## Weaknesses

### Fatal

No fatal errors invalidate the paper’s core claims.

### Major

**Missing critical baselines for frozen embeddings**: The paper compares frozen ConforFormer embeddings only to frozen Uni-Mol (their replication) and ablations. It does not compare to other frozen molecular embeddings, such as those from MolCLR, GEM, or even simple Morgan fingerprints with an MLP. Without such baselines on the same property prediction tasks (Tables 1 and 2), it is impossible to assess whether ConforFormer’s frozen embeddings are practically useful. The claim of “on par or exceeding most 2020s level methods” is based on comparisons to *fine-tuned* literature results, not to other frozen embedding approaches.

**Performance gap limits practical utility**: On several key classification benchmarks (BBBP, BACE, ClinTox, ToxCast), the frozen ConforFormer-OMol embeddings are significantly worse than the fully fine-tuned Uni-Mol (e.g., ClinTox 0.716 vs 0.919, BACE 0.751 vs 0.857). While the paper highlights stability improvements, such drops likely outweigh the benefits in most applied settings. The paper does not adequately demonstrate that the trade-off is acceptable.

**Unsubstantiated claim about graph inference**: The paper argues that ConforFormer “learned to infer molecular graph-like features from 3D geometries alone.” While the isomer discrimination results support this claim, the evidence is indirect. No direct probing of graph-level feature detection (e.g., bond existence, functional groups) is provided. The correlation between isomer discrimination and property prediction quality is also not established.

**No evaluation of adapter strategies**: The paper notes that unfreezing a few layers improves performance to nearly fully unfrozen levels (mentioned in the SI), but this is not explored systematically in the main text. For a paper advocating frozen embeddings as a practical solution, the lack of investigation into lightweight adapters (e.g., LoRA, prefix tuning) is a significant omission.

**Incomplete ablation of contrastive objective**: The ablation studies (section E in SI) are referenced but not summarized in the main paper. We need to see how varying the contrastive loss weight, temperature, or number of conformers affects the quality/cost trade-off to understand the design choices better.

### Minor

- The model name is inconsistently written as both “Conformer” and “ConforFormer” in the text; “Conformer” (often capitalized) conflates with the chemical term.
- The writing would benefit from tighter focus; section 2.3 (technical practices in transfer learning) is well-known and starts belatedly.
- The paper claims that “no chemical embedding model capturing the diversity of 3D molecular conformations has yet been published,” but it should acknowledge that methods like GraphMVP and MolCLR use contrastive learning with augmentations that somewhat capture 3D diversity (e.g., 3D conformers via stochastic perturbations) even if not explicitly trained on multiple conformations.

### Trivial

- The number of unique molecules in the Uni-Mol dataset is given as 20.9M, but the paper later says 19M; this should be checked.
- Figure 3 captions repeat “The figure consists of three subplots…”—redundant.
- Section 4.2 mentions “Post-training the model on the train part of the PharmIsomer dataset saturates the backbone part…”, but this experiment result is not shown in a table or figure.

## Nice-to-Haves

- Compare frozen ConforFormer embeddings to frozen embeddings from other pre-trained models (e.g., MolCLR, GEM, ChemBERTa-2) on the MoleculeNet benchmarks to establish relative performance.
- Show the effect of the contrastive loss weight (\(\lambda\)) on both property prediction and isomer discrimination in a single figure in the main paper.
- Provide a few case studies where the model’s frozen embeddings are used for similarity search on real-world datasets (e.g., hit expansion from high-throughput screening) to demonstrate practical utility.
- Include error bars in Figure 4 (precision–recall) by bootstrapping or multiple runs.

## Novel Insights

Beyond the paper’s own contributions, a genuinely novel insight is that learning to align conformer embeddings via contrastive learning leads to an emergent ability to discriminate between 3D geometries that belong to the same molecular graph and those that do not—even though the model never sees explicit graph connectivity. This suggests that molecules, as continuous potential energy wells, have a latent graph structure that can be recovered purely from samples of their 3D geometries through appropriate regularization. The finding that a simple cosine threshold on frozen embeddings can achieve 83% precision at 50% recall for isomer detection demonstrates that the learned embedding space naturally organizes by molecular identity rather than by shape similarity.

## Suggestions

- Add a table comparing frozen ConforFormer embeddings to frozen embeddings from at least two other pre-trained molecular models on the MoleculeNet benchmarks (classification + regression). This is essential to validate the claim that ConforFormer provides “performant, compact frozen embeddings.”
- Include a small-scale adapter study (e.g., LoRA, prefix tuning) in the main paper—or at minimum, show the results of unfreezing the last 1-3 layers on the same benchmarks—to demonstrate that the frozen embedding limitation can be overcome with minimal extra parameters.
- Provide a quantitative analysis (e.g., using attention maps or probing classifiers) to support the claim that the model learns molecular graph features, such as predicting bond existence or local chemical environments from the CLS token.
- Clarify in the main text that the “frozen” setting still requires training a linear/MLP head, and discuss how many parameters are actually trained in that setting compared to full fine-tuning.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>