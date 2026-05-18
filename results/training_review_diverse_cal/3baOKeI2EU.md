Here is the consolidated final review.

---

## Summary

This paper proposes UniCoTT, a unified teacher-student distillation framework that transfers structured chain-of-thought reasoning (chain, tree, and graph) from LLMs to smaller language models. The core ideas are: (1) an answer-conditioned iterative prompting strategy to construct diverse CoT structures (UniCoT) with improved rationality; (2) a node-level supervised contrastive loss to leverage multi-node explanations; and (3) a structural consistency learning strategy that enforces reasoning-path constraints in the student's latent space. Experiments on factual reasoning, multiple-choice QA, and NLU tasks across BERT, RoBERTa, and XLNet backbones show consistent improvements over PLM baselines, CoT distillation, and SCOTT.

## Strengths

1. **First unified framework for structural CoT distillation.** Prior work (SCOTT, vanilla CoT distillation) considers only single-chain explanations. UniCoTT is the first to handle chain, tree, and graph structures within a single distillation framework, as claimed and demonstrated in Tables 1–3 where tree/graph variants outperform chain-only variants.

2. **Answer-conditioned iterative construction reduces hallucination.** By conditioning each generation step on the gold answer \(a^*\) (Eq. 1), UniCoTT produces explanations with higher inference consistency than baselines, as quantified by the LAS metric (Table 5). This directly addresses a known failure mode of LLM-generated explanations.

3. **Strong and consistent empirical results across diverse settings.** UniCoTT outperforms PLMs, CoT distillation, and SCOTT on nearly all metrics across 10 datasets spanning factual reasoning, multiple-choice QA, and NLU, using three different student backbones (BERT, RoBERTa, XLNet). The ablation study (Table 4) confirms the independent contribution of each proposed loss component.

4. **Structural consistency learning with ablation support.** The structural decoupling and entanglement losses (\(\mathcal{L}_{sd}, \mathcal{L}_{se}\)) improve performance across all structures, and removing either causes a clear degradation. This validates the core claim that enforcing structural constraints in the latent space aids knowledge transfer, regardless of how one evaluates the theoretical framing.

## Weaknesses

### Major

1. **DSbS listed as a baseline but no results reported.**  
   Section 4.1 explicitly lists DSbS (Hsieh et al., 2023) as a comparison method. However, the paper provides no bullet point description of DSbS (unlike PLMs, CoT, and SCOTT), and DSbS results never appear in the textual discussion of Tables 1–3. The reader cannot verify whether the comparison was actually conducted. The authors must either present the DSbS results or remove it from the baseline list with an explanation. As it stands, the evaluation is incomplete and potentially misleading.

2. **Graph-structured UniCoT construction is underspecified and possibly incoherent.**  
   The paper states that the adjacency matrix for graph UniCoT is initialized by "randomly assign[ing] multiple connections for each node while ensuring the overall graph remains connected" (Section 3.2). It does not specify: (a) how multi-parent explanations are combined in the prompt (concatenation? ordering?); (b) whether the graph is constrained to be a DAG, or how cycles are handled; (c) how the generation order is determined when a node has parents that have not yet been generated; (d) the number of nodes \(N_v\) used. These omissions make the graph variant irreproducible as presented. The reference to "A.8" suggests some details may be in the appendix, but the main text alone cannot stand.

3. **The relation matrix \(\mathcal{R}\) rests on an unvalidated assumption about answer-proximity in random graphs.**  
   The paper claims nodes closer to a sink node are "more refined" and "semantically nearing the answer" (Section 3.2). This is plausible for chains and trees, where generation order follows a monotonic reasoning progression. However, for the randomly-connected graph variant, the sink node is simply the last generated node, and shortest-path distance to this sink may have no semantic relationship to answer-relevance. The paper provides no analysis (e.g., correlation between \(\mathcal{R}\)-derived distances and actual reasoning quality) to support this design choice for the graph case.

### Minor

4. **Notational error in the node-level supervised contrastive loss (Eq. 6).**  
   Equation (6) writes the contrastive loss as \(\exp(v_j \cdot v_{j'}/\tau)\), where \(v_j\) and \(v_{j'}\) are defined as text strings (explanations). The dot product requires vector representations, which are correctly defined as \(h_j = \text{Encoder}_{\text{SLM}}(v_j)\) in Eq. (5). The equation should read \(h_j \cdot h_{j'}\) rather than \(v_j \cdot v_{j'}\). Additionally, the paper does not specify how negative samples are drawn (within-batch? cross-instance?), what batch size is used, or how many nodes per UniCoT participate in the contrastive loss. These details affect reproducibility.

5. **Theoretical framing of structural consistency learning is partially overclaimed.**  
   Theorem 1 states an upper bound on the structural error, and the paper asserts that minimizing \(\|\mathbf{T}_\mathcal{S}\|_F\) (via rank maximization, citing prior work) is achieved by \(\mathcal{L}_{sd}\) and \(\mathcal{L}_{se}\). The logical chain from "maximize the rank of \(\Sigma_\mathcal{S}\)" to the specific forms of \(\mathcal{L}_{sd}\) (Eq. 9) and \(\mathcal{L}_{se}\) (Eq. 10) is asserted rather than derived; the losses closely resemble regularization terms from Barlow Twins / VICReg. This is not a fatal flaw — the losses are empirically validated by ablation — but framing it as a rigorous theoretical contribution overstates what is actually shown. The paper would be better served by presenting this as a principled adaptation of representation-learning regularizers.

6. **Inference procedure for UniCoTT could be clarified.**  
   The paper states that "student models can obtain explanations generated by CoTs at the inference stage of all methods" (Section 3.5) and that only the final output is used for evaluation. However, it is not fully clear whether the *structure* of UniCoT (multiple nodes, relation matrix) is used at inference or only during training. If structure is discarded at inference and only the final answer is predicted (with mask), the paper should state this explicitly to avoid confusion about what distinguishes UniCoTT at test time.

### Trivial

7. The abbreviation "DSbS" is used without being spelled out. Readers unfamiliar with Hsieh et al. (2023) will not know what it stands for.

## Nice-to-Haves

- Ablation results across more than one student backbone (Table 4 uses only RoBERTa-base) would strengthen the analysis, though the current scope is acceptable.
- Concrete examples (actual text) of generated UniCoTs for chain, tree, and graph structures on a representative question would help demonstrate that the construction method produces meaningful reasoning.
- Specifying the number of nodes \(N_v\) for each structure (chain, tree, graph) and the tree depth would improve reproducibility.

## Removed Points

These points were flagged by reviewers but are removed per policy:

- **"Missing proof of Theorem 1"** — The paper references "A.8" (appendix), and the parser strips appendix content. Per policy, criticisms about missing appendix proofs are removed.
- **"Figure 5 referenced but not in main text"** — This is likely a reference to an appendix figure; parser artifacts are not author errors.
- **"No derivation of the bound provided"** — The bound is stated as a theorem; the derivation (if any) belongs in the appendix, which is stripped.
- **"The paper should also cover Y / domain Z"** — The paper's scope (factual reasoning, MC QA, NLU) is already broad; demands for further breadth constitute scope creep.
- **Several formatting/style nitpicks** about the "node-level supervision contrastive loss" wording inconsistency and missing figure references — these are parser extraction artifacts.

## Novel Insights

The most interesting tension in the reviews is around the theoretical framing. The paper's structural consistency losses are empirically effective (ablation confirms this), and they are clearly inspired by well-known self-supervised learning objectives (Barlow Twins, VICReg). The reviewer correctly notes that the claimed "theorem-level" grounding is not fully substantiated by what appears in the main text. However, this does not detract from the empirical finding that regularizing the student's latent space with structure-mimicking terms (decoupling + entanglement) improves distillation. This is actually a pragmatic and transferable insight: you do not need a formal proof that a loss minimizes a specific bound for it to be an effective structural regularizer. The paper would be stronger if it acknowledged this lineage more directly and positioned the structural consistency loss as a *principled adaptation* rather than a new theoretical result.

## Suggestions

1. **Fix the missing DSbS results.** Either add them to all tables, or remove DSbS from the baseline list and explain why (e.g., incompatible task formulation).
2. **Specify graph construction details:** clarify whether graphs are constrained to be DAGs, how multi-parent prompts are assembled, and how generation order is determined. Report \(N_v\) for all structures.
3. **Correct Eq. 6:** replace \(v_j \cdot v_{j'}\) with \(h_j \cdot h_{j'}\) and specify the negative sampling procedure (batch-level? memory bank?), batch size, and number of nodes used per UniCoT.
4. **Tone down the theoretical framing** for structural consistency learning. Position \(\mathcal{L}_{sd}\) and \(\mathcal{L}_{se}\) as an adaptation of rank-maximization regularizers (cite Barlow Twins / VICReg directly) rather than a derived consequence of Theorem 1. Keep the theorem as motivation, but do not claim it formally justifies the specific loss forms.
5. **Clarify inference:** state explicitly whether UniCoT's structure is used only during training or also at test time, and how the final prediction is produced.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>