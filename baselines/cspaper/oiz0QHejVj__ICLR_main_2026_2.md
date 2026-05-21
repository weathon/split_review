---
job_id: 8daa3d3a-97a4-4ade-a900-2710f6a971f1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: oiz0QHejVj.pdf
paper: CLIP-Map: Structured Matrix Mapping for Parameter-Efficient CLIP Compression
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on representation learning and efficient compression of CLIP-style vision-language models through structured parameter mapping and distillation.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, method, experiments, quantitative results, and conclusion; while there are notable technical and experimental weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious content targeting automated review systems in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes CLIP-Map, a CLIP compression framework that replaces select-based pruning with a learnable mapping-based compression stage followed by retraining with knowledge distillation. The core idea is to compress width using Kronecker-factorized mapping matrices \(F^{in}\) and \(F^{out}\), compress depth using a learnable layer-combination matrix \(L_{depth}\), and stabilize optimization via a diagonal inheritance initialization that preserves part of the pretrained weights at the start of training. Experiments on zero-shot retrieval and zero-shot classification compare CLIP-Map against TinyCLIP and several other reported baselines across different compression ratios.

## Strengths
1. The paper tackles a relevant problem. Efficient CLIP-like models remain important, especially under high compression ratios where simple pruning often degrades sharply. The framing of compression as learned parameter mapping rather than parameter selection is a meaningful change in perspective.

2. The method is conceptually simple and reasonably intuitive. The decomposition in **Equations (3) and (4)** is the key technical device, replacing a prohibitively large linear map \(R_l \in \mathbb{R}^{D_2^2 \times D_1^2}\) with two smaller matrices \(F_l^{in}, F_l^{out} \in \mathbb{R}^{D_2 \times D_1}\). This makes the proposed mapping stage at least computationally plausible.

3. The proposed initialization is empirically useful. The ablation in **Table 5** shows a dramatic gap between diagonal initialization and random/Xavier/Kaiming initialization. Even though the theoretical explanation is weaker than claimed, the empirical message is clear: initialization matters a lot for this mapping parameterization.

4. The paper includes experiments at multiple compression regimes, and the strongest empirical case is at aggressive compression. In **Table 1**, at the 1.0% compression ratio, CLIP-Map consistently improves over TinyCLIP and its longer multi-stage variant on both MSCOCO and Flickr30K retrieval metrics. Those gains are not tiny, for example MSCOCO TR@1 improves from 12.5 to 15.8 and Flickr30K IR@1 from 14.6 to 17.9 against the stronger TinyCLIP baseline.

5. The training-efficiency angle is potentially useful. Although mostly documented outside the main story, the paper repeatedly emphasizes that CLIP-Map uses fewer stages and fewer total epochs than progressive TinyCLIP-style compression. This is aligned with the design shown in **Figure 2**, which presents a simpler two-stage mapping-plus-retraining pipeline.

6. The figures help communicate the intuition. **Figure 1** is a useful high-level comparison between select-based pruning and the proposed mapping-based process, and **Figure 3** makes the width-then-depth compression mechanism more concrete by visually showing how inherited diagonal structure is preserved before learning off-diagonal combinations.

## Weaknesses
1. The paper overstates what the mapping preserves, and the central “less information loss” claim is not really established.  
   The introduction and contributions repeatedly contrast select-based pruning with mapping-based compression and suggest that the latter “preserves the full information” or has “fewer information loss” because it avoids hard parameter removal. But under **Equations (3) and (4)**, the compressed weight is still \(W' = F^{out} W (F^{in})^\top\), which is a low-dimensional bilinear projection of the original matrix. This is still a lossy compression map whenever \(D_2 < D_1\). In other words, the method changes the nature of the loss, it does not avoid it. Why this matters: the main motivation of the paper is built on this distinction, so the paper needs either a more precise statement, such as preserving more task-relevant information empirically, or a formal argument about approximation capacity relative to select-based inheritance. As written, the narrative is too strong and not justified by the mathematics.

2. The mathematical presentation has several inconsistencies and underspecified elements.  
   There are multiple notation issues in the core objective section on **Pages 4 to 7**:
   - In **Equation (1)**, the right-hand side is said to lie in \(\mathbb{R}^{D_2 \times D_2}\), but \(Vec(W_l')\) is a vector, so this should be \(\mathbb{R}^{D_2^2}\), not a matrix-shaped codomain.
   - In **Equation (2)**, the summation index uses \(l\) on both sides and also defines \(l'\). This is a small notation issue, but it makes the layer-combination formula unnecessarily confusing. It should be something like \(\sum_{j=1}^{L_1} L_{depth}[l',j] W_j\).
   - In **Equation (11)**, the “cross-entropy between teacher logits and student logits” is underspecified. Standard distillation usually needs either KL divergence between softened distributions or explicit normalization/temperature treatment. Writing \(CE(logits^s, logits^t)\) is not a complete specification because cross-entropy expects a target distribution, not raw logits.
   - In **Equation (12)**, the paper writes \(logits_{T2T}^s\), which appears inconsistent with the CLIP objective and likely should be \(I2T\). This is not a harmless typo because it affects the definition of the training loss.
   - In **Equation (13)**, the total loss uses \(\mathcal{L}_{soft}\), while **Equation (11)** defines \(\mathcal{L}_{distill}\). This mismatch leaves the final objective ambiguous.
   These are core equations, not peripheral notation. Why this matters: if the objective is not cleanly specified, the method is harder to reproduce and some empirical conclusions become harder to trust.

3. The depth-compression mechanism is underdeveloped and potentially problematic.  
   The paper states in **Equation (2)** that each new layer is a linear combination of old layers through \(L_{depth}\), and **Figure 3** illustrates this as a weighted mixing of layer parameter blocks. However, several important details are missing:
   - Is \(L_{depth}\) shared across different parameter types within a transformer block, or separate for attention and FFN matrices?
   - Are the coefficients constrained, for example normalized, nonnegative, or sparse?
   - How are residual pathways and layer norms handled under depth compression?
   - Does the same combination apply to both text and image encoders identically?
   Without these details, the claimed “unified” compression pipeline is not actually fully specified in the main paper. Why this matters: depth compression is one of the advertised contributions, yet most of the reader’s understanding is left at a cartoon level.

4. The empirical comparison is heavily concentrated on TinyCLIP, and the broader baseline story is weak.  
   In the main paper, the practical comparison is almost entirely against TinyCLIP or paper-reported results from other models trained on different datasets and different scales. **Table 3** especially mixes methods with different architectures, data, and parameter counts, then draws favorable conclusions about both effectiveness and efficiency. For example, MobileCLIP and MoPE-CLIP use different training data or capacities, and the paper itself acknowledges these mismatches on **Page 8**. That makes the comparison more anecdotal than decisive. Why this matters: the paper’s contribution is a new compression method, so the burden is to compare rigorously against strong compression alternatives under controlled settings, not mainly against one baseline plus several loosely comparable reported numbers.

5. Some tables contain internal inconsistencies or suspicious model naming/configuration issues that reduce confidence in the experimental section.  
   There are several places where the presentation becomes hard to follow:
   - In **Table 1**, the 50.8% compression row labels the authors’ model as \(\text{CLIP-Map}_{tiny}\) for a 39×10 setting, which is inconsistent with the surrounding naming and seems likely to be a typo for base.
   - In **Table 3**, “CLIP-Mapbase” appears multiple times for parameter settings 0.8+0.3, 8+3, and 39+19. This conflicts with the architecture naming in **Section 4.1** and **Table 6** and makes it unclear which variant is actually being compared.
   - **Table 6** itself contains obvious inconsistencies, for example at 1.0% compression it lists “CLIP-Mapbase (Ours)” with 0.8+0.3 parameters, which does not match the intended scale name.
   These are not fatal on their own, but they create friction when trying to verify the claims. Why this matters: when model scale names and parameter counts are inconsistent, it becomes harder to assess fairness and reproducibility.

6. The zero-shot classification results are mixed enough that the headline claim should be toned down.  
   The text says CLIP-Map shows strong performance across most tasks, but **Table 2** is more nuanced. At the tiny scale, CLIP-Map does improve over TinyCLIP on many datasets, but it also loses on some, sometimes substantially, such as VOC2007, EuroSAT, and GTSRB. At the larger 39M scale, the comparison is even less uniformly favorable, with noticeable drops on MNIST, PCam, GTSRB, and KITTI. The base-scale story is basically parity, not clear superiority. Why this matters: the paper’s broader generalization claim should reflect that gains are strongest for retrieval and for more aggressive compression, not uniformly across all downstream zero-shot tasks.

7. The “fewer training epochs” and “less engineering complexity” claims are not evaluated rigorously enough.  
   The paper emphasizes simplicity and efficiency compared with progressive compression pipelines. **Figure 2** indeed presents a visually simpler two-stage process, and **Table 11** in the appendix suggests wall-clock savings over TinyCLIP for some scales. However, the main paper does not provide a controlled accounting of total optimization cost, hyperparameter tuning effort, or implementation complexity. In fact, CLIP-Map introduces a separate mapping stage with its own initialization, factorized parameterization, and design choices for sharing transforms across modules. Why this matters: the claimed simplification is plausible, but the evidence in the main paper is not strong enough to elevate it to a contribution claim.

8. The theoretical argument for diagonal inheritance initialization is weaker than the paper suggests.  
   The discussion on **Page 6**, around **Equations (5) to (10)**, argues that independent standard initializations can cause “distribution shifting” because the variance of the Kronecker-structured mapping is multiplicative, \(\mathrm{Var}(R)=\sigma_A^2 \sigma_B^2\). But multiplicative variance alone is not enough to establish instability. Depending on \(\sigma_A^2\) and \(\sigma_B^2\), the product may even be smaller than 1 and not obviously problematic. Also, \(R_{width}\approx I\) in **Equation (10)** is only a heuristic statement, since \(R_{width}\) is rectangular in the compressed setting and cannot literally be an identity map. The empirical usefulness of the initialization is convincing, but the derivation does not really prove the stated explanation. Why this matters: the paper leans on this section to justify the core optimization trick, so the distinction between intuition and proof should be clearer.

9. The method description is too narrow relative to the actual CLIP parameter structure.  
   In **Section 3.1**, the method is introduced for square matrices \(W_l \in \mathbb{R}^{D_1 \times D_1}\), but CLIP contains embeddings, projection layers, MLP expansions, attention projections, and modality-specific components with nonuniform shapes. The appendix says these are handled by reusing \(F_{emb}^{out}\) across many submodules, but this is a major design choice that is not discussed in the main paper. Why this matters: the difference between the clean square-matrix exposition and the real architecture is not cosmetic; it affects expressivity, parameter sharing, and fairness of comparison.

10. The paper does not disentangle how much of the gain comes from mapping, initialization, depth mixing, and distillation.  
   The main positive results in **Table 1** and **Table 2** are after retraining with distillation. **Table 4** studies mapping-stage duration, and **Table 5** studies initialization, but there is no clean main-paper ablation that isolates:
   - width mapping only vs width + depth mapping,
   - diagonal inheritance vs manual weight copying,
   - retraining with and without distillation,
   - shared transforms across modules vs per-module transforms.
   **Figure 4** in the appendix suggests distillation in the mapping stage changes training dynamics, but this is not integrated into the central analysis. Why this matters: without such decomposition, it is harder to identify what the actual methodological advance is beyond “a different initialization path before standard CLIP distillation.”

11. The paper’s positioning against prior work is somewhat narrow.  
   The related work discusses pruning, distillation, and model growth methods such as LiGO and LeTs, which is appropriate, but the paper does not sufficiently position itself against a broader set of structured compression alternatives beyond select-based pruning. Given that the method is essentially a learned structured projection of pretrained weights, more direct discussion of structured low-rank compression, matrix factorization, or architecture-aware transformation approaches would strengthen the novelty argument. Why this matters: the paper currently risks presenting the contribution as more distinct than it may actually be.

12. Exposition quality is uneven, with many grammar and terminology problems in the main paper.  
   There are repeated issues such as “feature presentation ability” instead of representation ability, “widely applications,” “to mapping the original model,” and several inconsistent names or symbols across sections and tables. This is not just stylistic polish. For a paper whose method relies on several coupled operators and stages, these inconsistencies materially increase the effort required to verify the work.

## Questions
1. Please give a fully precise definition of the training objective used in the retraining stage. In particular, in **Equation (11)**, are you using KL divergence between temperature-scaled teacher/student softmax distributions, or literal cross-entropy with teacher probabilities? Please write the exact formula including temperature and normalization. Also please resolve the mismatch between \(\mathcal{L}_{distill}\) and \(\mathcal{L}_{soft}\), and clarify whether **Equation (12)** should use \(logits_{I2T}^s\) rather than \(logits_{T2T}^s\).

2. Please clarify the exact parameterization of depth compression from **Equation (2)**. Are the coefficients in \(L_{depth}\) unconstrained, row-normalized, or sparse? Are they learned separately for each parameter type within a transformer block, or shared across all block parameters? A precise answer here would substantially increase confidence in reproducibility.

3. Can you provide a controlled ablation in the main paper that separates:
   - mapping only, no retraining,
   - mapping + retraining,
   - diagonal inheritance vs Xavier/Kaiming while holding everything else fixed,
   - width-only compression vs width+depth compression?
   Right now, the strongest conclusions rely on the full pipeline, so it is hard to attribute gains to the proposed mapping itself.

4. Please explain the naming inconsistencies across **Table 1**, **Table 3**, and **Table 6**. Which variants correspond to 0.8+0.3, 8+3, and 39+19 exactly? A cleaned-up and internally consistent table would help a lot.

5. For the 50% compression regime, **Table 1** suggests CLIP-Map is roughly competitive rather than clearly better than TinyCLIP, and **Table 2** shows mixed downstream behavior at larger scales. Do you view the main benefit as specifically concentrated in extreme compression? If so, I think the paper should state that much more explicitly.

6. The initialization story in **Equations (5) to (10)** reads more heuristic than theoretical. Can you either tighten the argument or reframe it clearly as intuition supported by the strong empirical evidence in **Table 5** and **Figure 6**? A more careful explanation would improve the paper.

7. In **Figure 3**, the width-compression and depth-compression pipeline is visually intuitive, but the figure leaves open whether every module in the transformer uses the same \(F^{in}, F^{out}\) scheme or whether some are shared and others are separate. Please annotate this more explicitly in the figure or caption.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work studies model compression for deployment efficiency and does not introduce a new dataset, human subjects protocol, or obviously harmful application beyond the standard concerns associated with CLIP-like models.

## Soundness Rating
2: fair. The core idea is plausible and some empirical gains are real, especially at high compression, but the method specification has important ambiguities in the loss definitions and depth-compression parameterization, and the evidence does not fully support several central claims.

## Presentation Rating
2: fair. The high-level story is understandable and the main figures are useful, but notation inconsistencies, equation issues, table naming problems, and frequent writing errors materially hurt clarity.

## Contribution Rating
2: fair. The mapping-based compression perspective is interesting and potentially useful, particularly under aggressive compression, but the contribution is not yet supported strongly enough by rigorous positioning, controlled ablations, and precise technical specification to clear the ICLR bar.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a promising core idea and some genuinely encouraging results, especially at extreme compression, but there are too many unresolved issues in mathematical specification, experimental framing, and presentation for me to recommend acceptance in its current form.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the technical formulation, figures, and tables carefully, though some implementation details remain unclear because of the paper’s own ambiguities.