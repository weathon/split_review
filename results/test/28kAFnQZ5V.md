Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

The paper proposes the Tensorized Attention Model (TAM), which extends the Transformer attention mechanism to handle three object types (query, key/memory, and semantic) via Tucker decomposition. The key innovations are: (1) dimension-aligned Tucker decomposition allowing variable-length query, key, and semantic sequences; (2) semantic fusing to collapse the 3D attention tensor into a 2D matrix for source-to-target transformation; and (3) iterative multi-core averaging that avoids storing all core tensors simultaneously, reducing memory overhead. TAM is evaluated on response selection tasks using Reddit (NFL, Politics) datasets, showing substantial accuracy gains over BERT and Tensorized Transformer baselines.

## Strengths

- **Variable-length multi-object attention via dimension-aligned Tucker decomposition (Sections 4.1–4.2, Eq. 4)**: TAM operates on D-dimensional column vectors rather than object-length matrices, allowing Q, K, and S to have different lengths. This overcomes a core limitation of the prior Tensorized Transformer (Ma et al., 2019), which required equal lengths. The empirical results confirm the advantage: e.g., TAM achieves R10@1 of 0.508 on NFL vs. 0.185 for Tensorized Transformer(SCR) (Table 2).

- **Iterative multi-core averaging for memory efficiency (Section 4.3, Eq. 7)**: TAM sums attention tensors on-the-fly, discarding previous tensors after each iteration. This allows up to 20 cores on Politics with minimal parameter growth, whereas the Tensorized Transformer is limited to 2 cores due to memory constraints and overfitting (Section 5.6, Table 6; Section 5.3).

- **Semantic fusing for effective source-to-target transformation (Section 4.2, Eq. 5–6)**: Instead of the "split&concat" method used in prior work, TAM collapses the semantic axis to produce a 2D attention matrix, then performs matrix multiplication with V followed by Add&Norm. The ablation (Table 4) confirms this is critical: removing semantic fusing drops NFL R10@1 from 0.508 to 0.321.

- **Consistent and large accuracy gains on Reddit datasets (Tables 2–3)**: From scratch on Politics, TAM achieves R10@1 of 0.571 vs. 0.221 for BERT(CR) and 0.244 for Tensorized Transformer(SCR). The pretrained hybrid BERT^P(SCR)-TAM reaches 0.653 on Politics, outperforming standalone BERT^P (0.494) and a two-stage BERT stack (0.498).

- **Ablation study validates key design choices (Table 4)**: Controlled comparisons for "w/o Semantic Fusing" and "w/o Query Aligned" help isolate the contributions of individual components.

## Weaknesses

### Fatal
None.

### Major

- **Unsubstantiated TweetQA claims (Introduction lines 37–39, Contributions)**: The introduction and contribution summary explicitly state that TAM was evaluated on the TweetQA dataset and "consistently outperformed existing Transformer-based methods in terms of accuracy." However, the evaluation section (Section 5) never presents any TweetQA results — not in any table description, not in the results discussion (Section 5.4), and not in the ablation or core analysis. The only mention in the evaluation is "We also conducted evaluations on the TweetQA dataset" (line 183), which says evaluations were done but provides no numbers. Since the paper's central empirical claims explicitly invoke TweetQA as supporting evidence, the absence of these results is a serious omission that prevents readers from verifying a stated contribution. The authors must either present the TweetQA results or remove all claims about them.

- **Contradictory and ambiguous layer count specification (Section 5.2, lines 190–192)**: The paper first states "All models utilize 12 transformer encoder layers" (line 190), then later states "the terms 'BERT' or 'TAM' indicate unpretrained models with 4 layers" (line 192). It is impossible for the reader to determine which configuration produced the results in Tables 2 and 3. If the "from scratch" experiments use 4-layer models for BERT and TAM while the comparison methods use 12 layers, the comparison is unfair to the baselines. If all models use 4 layers, the initial statement is incorrect. Either way, the reader cannot evaluate whether the reported gains reflect a genuine architectural advantage or an uneven playing field. This must be clarified.

### Minor

- **Unclear mathematical notation for the core method (Eq. 4, lines 114–118)**: Equation (4) uses a subscript $(q,:,:,j,:,l)$ on an outer product $(\mathbf{Q}_{:,i} \odot \mathbf{K}_{k,:} \odot \mathbf{S}_{s,:})$ that is not standard and not clearly explained. The description "the outer product where first, fourth, and sixth dimensions are activated" is insufficient to resolve the ambiguity. The dot product between the core tensor element $\mathcal{G}_{q,j,l}$ and this outer product is also not well-defined. Since the Tucker decomposition formulation is the core methodological novelty, this lack of clarity hinders understanding and reproduction. The idea is discernible at a conceptual level, but the precise computation is not.

- **No error bars or confidence intervals despite 5 random seeds (Section 5.3)**: The paper reports using five random seeds for reproducibility but presents only point estimates in all tables. Without standard deviations, the reader cannot assess whether the reported improvements (e.g., the 0.003 gap between TAM and a baseline) are statistically reliable.

- **Core count sensitivity unexplained (Section 5.6, Table 6)**: TAM requires 3 cores for NFL but 20 cores for optimal performance on Politics. The paper does not analyze why this disparity exists or whether it reflects sensitivity to dataset characteristics (e.g., vocabulary size, dialogue length, domain specificity). This makes the configuration choices appear ad hoc.

### Trivial

- The description of "w/o Query Aligned" (Section 5.5, line 231) is terse; whether the variant still uses Eq. (4) with a different core tensor size or a fundamentally different computation could be stated more explicitly.

## Nice-to-Haves

- A direct "2D-attention" variant of TAM (i.e., TAM without the semantic stream, using only Q and K/V but still employing Tucker decomposition) would isolate whether gains come from the tensorized attention mechanism itself or from the additional semantic modality. The Tensorized Transformer baseline serves a different purpose (parameter compression for self-attention) and is not a substitute for this ablation.

- A discussion of wall-clock time, FLOPs, or training/inference memory beyond the brief statement in Section 5.6 would help practitioners assess the practical cost of the accuracy gains.

- An algorithmic description or pseudo-code for the iterative averaging procedure (Section 4.3) would clarify the memory efficiency claim.

## Removed Points

- **Data leakage in input construction**: The reviewer claimed that including the response in the K/V stream introduces information leakage. This is a misunderstanding of standard response selection cross-encoder setups, where the model always sees a candidate response paired with the context and scores their match. The paper describes this correctly (Section 5.1, line 183). No leakage is present.

- **Strengths from the Strength Finder that were filtered**: The strength that "ablation study validates key design choices" was partially qualified by the Strength Finder itself noting a possible tie on NFL for "w/o Query Aligned" (0.511 vs 0.508). This discrepancy cannot be verified from the extracted text (table images are not rendered). The overall trend on Politics (0.518 vs 0.571) supports the paper's claim, so the strength is maintained but qualified appropriately in the strengths section above.

- **Generic strengths from Strength Finder** (e.g., "addresses important problem") were removed as they lack specific, citable content tied to the paper's contributions.

## Novel Insights

The paper's central insight — that aligning Tucker decomposition along the dimension size D rather than object length Q/K/V enables variable-length multi-object attention — is genuine and distinguishes TAM from prior tensorized transformers. The iterative averaging trick (Section 4.3) is a practical engineering contribution that makes multi-core tensor attention feasible where it previously caused memory overflow. However, the reviews do not surface any novel insight beyond what the paper already claims.

## Suggestions

1. **Present or retract TweetQA results**: Either include a table with TweetQA numbers (or add columns to existing tables) and discuss them in Section 5.4, or remove all TweetQA claims from the introduction and contributions. A central empirical claim cannot remain unsubstantiated.

2. **Clarify the layer count for every experiment**: State explicitly for each table and each method how many layers were used. The contradiction between "12 layers" and "4 layers" must be resolved with a clear explanation of which setting applies to which experiment.

3. **Rewrite Eq. (4) with precise notation**: Define the Tucker decomposition as a sum over the core tensor modes using standard tensor index notation (e.g., with explicit Einstein summation or mode- products). A small worked example (e.g., Q=3, D=2) would help readers verify they understand the computation.

4. **Add standard deviations to all tables**: Since five seeds were run, reporting ±σ is a low-cost improvement that would significantly strengthen the paper's statistical credibility.

5. **Analyze the core count discrepancy** between NFL (3 cores) and Politics (20 cores): Even a brief discussion of why different datasets need different core counts would help readers assess the method's robustness and practical deployment considerations.

## Score and Decision

Originality: 6/10 — Tucker decomposition for multi-object attention is a meaningful extension. Importance: 6/10 — multi-object relationships are relevant in dialogue and other tasks. Claims support: 3/10 — strong Reddit results but missing TweetQA evidence and ambiguous layer specs undermine confidence. Soundness: 4/10 — experimental issues with layer count and missing error bars. Clarity: 4/10 — unclear math, contradictory layer descriptions. Value to community: 5/10 — if the issues are resolved, the architectural idea has value.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>