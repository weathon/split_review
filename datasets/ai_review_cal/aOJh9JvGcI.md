- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

PharmaVQA proposes using a Bilinear Attention Network (BAN)—a technique from Visual Question Answering—to condition molecular graph representations on textual questions about pharmacophore features (e.g., counting hydrogen bond donors). The resulting "knowledge prompts" are concatenated with a separately encoded molecular representation for downstream tasks including property prediction, drug-target interaction, and ligand identification. The method is evaluated on 46 benchmark datasets and validated by identifying literature-confirmed ligands from an FDA-approved molecule set.

## Strengths

- **Broad and multi-task empirical validation**: The method is evaluated on 46 datasets spanning molecular property prediction (classification and regression), drug-target interaction (BindingDB classification and regression), and ligand discovery (three targets). This breadth directly supports claims of generalizability.

- **Practical ligand discovery validation with literature confirmation**: For HPK1, FGFR1, and VIM-1, 10/20, 15/20, and 16/20 of the top-20 predicted molecules respectively are confirmed as ligands by literature reports (Section 5.5). This goes beyond standard benchmark metrics to demonstrate practical utility.

- **Novel application of VQA/BAN to molecular representation**: Adapting the Bilinear Attention Network—originally designed for image+text VQA—to condition molecular graph features on textual pharmacophore queries is a creative and technically sound idea. Using multiple "glimpses" and multiple question types (P questions, S glimpses) to produce attention-guided embeddings is a reasonable design.

- **Alignment loss for attention fidelity**: The alignment loss (Equation 11) explicitly supervises the attention map to match ground-truth functional group membership, which is a principled design choice that ties interpretability to the training objective.

## Weaknesses

### Fatal
None.

### Major

- **"Retrieval-augmented" framing is misleading throughout the paper**. The title, abstract, introduction, contributions list, and conclusion all describe the method as "retrieval-augmented" or "retrieving pharmacophore-related information directly from molecule databases." In reality, the model does not retrieve from any external database or knowledge base. It uses BAN to compute a joint embedding of the molecule graph and a textual question—this is a **multimodal conditioning mechanism**, not a retrieval system. The term "retrieval" occurs in Section 1 ("retrieval-based approach," "directly retrieving pharmacophore-related information"), the contribution bullet ("retrieval-augmented visual question-answering framework"), and Section 6 ("directly retrieving key data from molecular libraries"). This is not a minor phrasing nitpick; it is the central characterization of what the method does, and it is inaccurate. A reader expecting actual database retrieval will be misled about the nature of the contribution.

### Minor

- **Gap between pharmacophore motivation and implementation**: The paper motivates pharmacophores as involving "the difficulty of accurately capturing the diverse arrangements of functional groups that are essential for specific interactions" (Section 1). However, the actual method reduces pharmacophores to counting occurrences of **seven predefined functional group types** via RDKit (Section 5.2: "we ask how many are present"). Spatial arrangement, distances between groups, and 3D conformation—hallmarks of pharmacophore modeling—are not captured. The method is better described as "functional-group-conditioned representation" than "pharmacophore-guided." The authors acknowledge this in the conclusion ("Future work will focus on... incorporating 3D structural data"), but the discrepancy between the stated motivation and the actual method remains.

- **Ligand discovery comparison to KPGT is not controlled**: Section 5.5 reports that PharmaVQA identified 10 and 15 potential ligands for HPK1 and FGFR1 (top-20), compared to KPGT's published numbers of 12 and 13, and claims "competitive advantage." However, these are KPGT's numbers from KPGT's own screening protocol—different docking scores, thresholds, and candidate pools may have been used. A proper head-to-head comparison under identical conditions is needed to support a claim of advantage. The observation that PharmaVQA finds six HPK1 and four FGFR1 ligands not found by KPGT is interesting but could simply reflect different scoring distributions.

- **No ablation studies**: The paper does not ablate the contribution of each component (VQA prompts, pharmacophore count loss, alignment loss). It is unclear whether the VQA conditioning adds value beyond simply concatenating RDKit-computed pharmacophore counts with the graph embedding. A simple baseline using an MLP on pharmacophore counts + graph features is absent.

- **No hyperparameter sensitivity analysis**: The loss has two hyperparameters α and β (Equation 12), the BAN module has glimpses S and questions P, and dimensions d_k are tunable. No analysis of sensitivity to these choices is provided.

- **Interpretability evidence is limited**: The case study (Section 5.6) shows the model attends to tokens like "hydrogen", "bond", "donors" in the donor question. This demonstrates the model can align attention with its training signal, but it is weak evidence of chemical understanding—it shows the model can identify the words in a question that describe the functional group it was trained to count. This does not demonstrate novel insight about chemistry.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Adding a baseline that directly uses pharmacophore counts as features (e.g., MLP on counts + graph embedding) would clarify whether the VQA mechanism itself provides benefit beyond the counts.
- Including 3D structural information (as the conclusion suggests for future work) would better align with the pharmacophore motivation.
- Reporting results for all 46 datasets in a machine-readable table in the main text or appendix would improve verifiability.

## Removed Points

- **"Core experimental results are unverifiable (tables unreadable)"** — REMOVED. The tables are rendered as images in the parser output; this is a parser artifact, not an author error. The original submission contains readable tables.

- **"Alignment loss requires per-node labels that may not be available"** — REMOVED. The paper describes obtaining functional group membership via RDKit substructure matching, which is a standard and fully automated procedure requiring no external annotations.

- **Criticism that the approach does not discuss why existing methods fail to handle pharmacophores specifically** — REMOVED as a weakness. The paper's related work section (Section 2) discusses limitations of existing methods ("often overlook the critical spatial and functional relationships"), which provides adequate motivation.

- **Criticism about missing related works** — REMOVED per instructions (cannot verify existence of missing references without external sources).

- **Strength claiming the method "directly addresses the challenge of capturing diverse functional group arrangements"** — REMOVED because it conflicts with the verified weakness that the method only counts functional groups rather than capturing their arrangement.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution honestly.** Remove all "retrieval-augmented" and "retrieving from databases" language from the title, abstract, and throughout. The method is a VQA-conditioned graph representation that uses BAN to attend over molecular graphs guided by text queries about pharmacophore features. This is still a solid contribution.
2. **Add ablation studies** that isolate the contributions of: (a) the VQA/BAN conditioning, (b) the pharmacophore count loss L_ph, (c) the alignment loss L_align, and (d) a simple baseline that concatenates RDKit pharmacophore counts with graph embeddings without VQA.
3. **Provide a controlled comparison** for the ligand discovery experiments by running KPGT (or a comparable baseline) on the exact same molecule library with the same docking pipeline.
4. **Either strengthen the pharmacophore modeling** to include spatial information (distances, relative positions) or explicitly scope the paper's contribution as "functional-group-conditioned" rather than "pharmacophore-guided."
5. **Report α and β values** and add a brief sensitivity analysis showing whether results are robust to their choice.
