- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes GRABLI, a cross-modal pre-training method that aligns a Language Model (LM) with a Knowledge Graph (KG) via contrastive learning. The method simultaneously trains a GNN-based KG encoder and aligns its representations with LM entity representations using InfoNCE loss combined with masked language modeling. Evaluated on question answering (PubMedQA, MedQA, BioASQ) and entity linking (five corpora) using PubMedBERT and BioLinkBERT, the method shows consistent gains, including large zero-shot entity linking improvements (13.1–24.2% Acc@1).

## Strengths

- **Consistent gains across multiple QA benchmarks**: PubMedBERT with GRABLI shows mean accuracy improvements of 2.1%, 1.7%, and 6.2% on PubMedQA, MedQA, and BioASQ respectively (Table 1, lines 148–158), directly supporting the core claim that cross-modal KG alignment helps language understanding tasks.

- **Large improvements in zero-shot entity linking**: GRABLI increases PubMedBERT's average Acc@1 by 13.1% and BioLinkBERT_base's by 24.2% across five EL corpora (lines 161, Table 2), providing strong evidence that the alignment produces more distinguishable concept representations.

- **Efficient pretraining with limited data**: The pretraining dataset uses only 1.67M sentences covering ~600K UMLS concepts (line 120), yet delivers substantial improvements — validating the claim that GRABLI is effective after brief pre-training on a small alignment dataset.

- **Comprehensive ablation study**: Tables 3 and 4 systematically ablate loss terms, token-entity aggregation methods, graph encoder depth, and five distinct graph representation types (GAT, GraphSAGE, DistMult, TransE, linearized LM, textual-only), providing empirical justification for design choices.

- **Fair internal comparisons with strong biomedical base models**: The paper compares GRABLI-augmented models against their own base models (PubMedBERT, BioLinkBERT) as well as task-specific models (SapBERT, GEBERT) under consistent evaluation protocols.

## Weaknesses

### Fatal
None.

### Major

- **Unverifiable comparison with QA-GNN and GreaseLM**: The paper claims (line 160) that BioLinkBERT_large with GRABLI "performs on par or better than the task-specific QA-GNN and GreaseLM methods that reason over retrieved KG subgraphs." However, the paper does not specify whether these baseline numbers were obtained by re-running the models under controlled conditions or cited from original papers, nor does it provide any details on the subgraph sampling, fine-tuning protocols, or hyperparameters used. Without this information, the comparison is unverifiable, and one of the paper's more striking claims is unsupported.

### Minor

- **Missing relation extraction results**: Section 5.1 (line 137) states "Additionally, we perform evaluation on three biomedical relation extraction datasets" (ChemProt, DDI, GAR), but no results for these tasks appear in the main paper. These may be in a stripped appendix, but the main text lacks any pointer to where they can be found. Even if the method does not improve RE performance, the omission should be acknowledged; excluding negative results would be misleading.

- **No entity linking ablations**: The paper's largest gains are on zero-shot entity linking (up to 24.2% Acc@1), yet the ablation study (Sections 5.3–5.4, Tables 3–4) evaluates only QA tasks (PubMedQA, BioASQ). Since EL is where the method shines brightest, it would be informative to see which design choices (alignment loss, GNN architecture, contrastive formulation) drive those EL gains.

- **Text/table reference error**: Line 161 reads "Table 2 presents the evaluation results for aligned models on the QA task," but Table 2 is captioned "Evaluation results on biomedical entity linking" (line 131). The surrounding text correctly discusses entity linking, so this is clearly a copy-paste error. While minor, it is a presentation flaw that should be corrected.

### Trivial
None.

## Nice-to-Haves
- A brief qualitative analysis of the aligned representations (e.g., t-SNE plots or nearest-neighbor examples) would make the alignment mechanism more concrete, especially given the large zero-shot EL gains.
- Reporting standard deviations for entity linking results in the text (they may be in the table image) would improve statistical rigor, particularly on smaller datasets like SMM4H.
- A discussion of computational cost (training time, GPU memory) for the GNN versus linearized approaches would help practitioners choose between them.

## Removed Points
- **"BERN2 normalization introduces noise that is not analyzed"**: Generic preprocessing-noise concern that applies to virtually all NLP papers using entity linking tools. Not a concrete, specific weakness.
- **"Alignment may push LM representations toward structurally aggregated versions of its own concept-name embeddings"**: Speculative concern. The paper includes a "textual node representations" ablation showing that removing subgraph structure causes performance to drop, which already addresses this.
- **"No discussion of computational cost"**: Generic, not a core evaluation criterion. Moved to Nice-to-Haves.
- **"Standard deviations for EL results not reported"**: Cannot verify since EL tables are images. Moved to Nice-to-Haves.
- **"Models not released"**: Normal for anonymized submissions; paper states they will be released upon acceptance. Removed per hard rules.
- **Harsh critic's Strengthening/Qualitative suggestions**: These are constructive suggestions, not weaknesses. Addressed in Nice-to-Haves.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Clarify or remove the QA-GNN/GreaseLM comparison**: Either provide full reproduction details (hyperparameters, subgraph sampling, evaluation splits) or temper the claim to acknowledge that a direct comparison was not controlled. The paper's core contribution does not depend on this comparison.
2. **Add the RE results or remove the claim**: If the relation extraction experiments were run, include them (even if results are negative). If not run, remove the statement in Section 5.1 that evaluation was performed.
3. **Fix the "Table 2 presents…on the QA task" error**: Replace "QA task" with "entity linking task."
4. **Consider adding EL ablations**: Since the entity linking gains are the paper's most striking result, ablating design choices on EL would strengthen the empirical contribution.
