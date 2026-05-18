Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes Adaptive Guided Erasure (AGE) for concept erasure in diffusion models. The key insight is that existing methods map undesirable concepts to a fixed generic target (e.g., "a photo"), which is suboptimal. Through an empirical analysis of concept-space structure using a newly introduced 25-concept dataset (NetFive), the authors observe that erasure impact is localized to semantically related concepts. This motivates a minimax optimization: the outer loop erases the undesirable concept while preserving model capabilities, and the inner loop dynamically selects a target concept that is closely related to the erased concept but not its synonym. The target is further enriched via Gumbel-Softmax into a continuous mixture of concepts. Experiments on object removal, NSFW erasure, and artistic style removal show AGE significantly outperforms prior methods (ESD, UCE, CA, MACE) in preserving benign concepts while maintaining erasure effectiveness.

## Strengths

1. **Novel minimax formulation for adaptive target selection**: Equations (4–5) introduce an inner maximization over target concepts that simultaneously maximizes erasure distance (ensuring the target is not a synonym) and preservation distance (ensuring the target is locally related to the erased concept). The Gumbel-Softmax relaxation to continuous mixtures is a technically clean solution to the discrete search problem. (Section 4)

2. **Strong empirical results on preservation**: Table 1 shows AGE achieves PSR-5 of 95.6% on object-related concept erasure, approaching the original SD model's 97.6%, while the best baseline (MACE) achieves only 72.8%. This near-perfect preservation is maintained while still achieving 98.1% ESR-1 erasure and the best FID (16.1). The gap over baselines is large and consistent. (Section 5.1, Table 1)

3. **Controlled analysis linking target choice to preservation quality**: Section 3.2 systematically evaluates seven target strategies (synonym, related, general, unrelated, empty) across five concept subsets, showing that "in-class" related-but-not-synonym targets consistently yield the best preservation. This directly motivates the method's design. (Section 3.2, Figure 2)

4. **Interpretable learned targets in NSFW experiments**: Figure 4 shows that AGE automatically selects targets (e.g., "Model", "Drawing", "Toy") that correlate strongly with less sensitive body parts ("Feet") but weakly with sensitive ones ("breasts"), providing direct evidence that the optimization finds the intended kind of target concept. (Section 5.2, Figure 4)

## Weaknesses

### Fatal

None.

### Major

1. **Missing ablation isolating adaptive target selection as the source of gains**: The paper's central thesis is that *adaptive* target selection drives the preservation improvements. Yet there is no controlled condition where AGE uses a fixed or random target while keeping all other optimization details (minimax formulation, Gumbel-Softmax, regularization, etc.) constant. The analysis in Section 3.2 uses a different evaluation setup (NetFive, generation capability) than the main experiments (Imagenette, PSR/ESR). Without this ablation, the observed gains cannot be causally attributed to adaptivity rather than other aspects of the optimization procedure. This is the single most important missing experiment for validating the paper's core claim.

2. **Insufficient implementation details for the minimax optimization**: The paper does not specify how the bilevel problem is solved in practice. Key questions left unanswered: Are outer parameters θ' and the inner variable π updated in alternation or jointly? How many inner steps per outer step? What is the search space C for each experiment (full vocabulary? ImageNet classes? a hand-picked list)? What Gumbel-Softmax temperature is used and was it tuned? While the code is anonymously released, the paper itself should provide enough detail for a reader to understand the optimization dynamics without reading code. (Section 4, lines 126–132)

3. **Limited scale of concept-space analysis relative to the scope of claims**: The NetFive dataset contains only 25 ImageNet concepts organized into 5 tight semantic clusters (dogs, vehicles, instruments, buildings, equipment). The observed "locality" — that erasing one concept mainly affects others in the same cluster — is partially a consequence of this design: with clear semantic gaps between clusters, within-group effects dominating cross-group effects is almost inevitable. The paper also claims the "first comprehensive study of the concept space structure" (Section 6, line 201), which is an overstatement given the evaluation set's limited size and structure. The geometric claims (sparsity, locality, asymmetry) would be much stronger with a larger, more diverse concept set and a formal statistical test of locality (e.g., correlation of Δ(cₑ, cⱼ) with CLIP text embedding similarity).

### Minor

1. **The generation capability metric $G_{c_e}(c_j)$ is never formally defined**: The paper states "measure using the metrics:" (line 63) but the sentence is truncated, and no explicit formula is given. While the metric is operationally clear from context — it is a percentage of generated images where a pre-trained classifier detects the concept — a precise definition (e.g., "top-1 accuracy of a ResNet-50 classifier over 500 generated images") is essential for reproducibility and would avoid ambiguity about whether it is top-1, top-5, or mean softmax confidence. (Section 3, line 63–64)

2. **LPIPS interpretation in the artistic-style experiment is confusing**: For erasing performance, higher LPIPS (more distortion from the original model's output for the erased concept) is desired. The paper reports AGE's LPIPS of 0.80 vs. CA's 0.82 and calls AGE "slightly lower," but this means CA achieves more distortion (better erasure by LPIPS) than AGE. The paper primarily relies on CLIP score for the erasing claim, but the LPIPS framing in the text is inconsistent with the desired direction and needs clarification. The paper partially addresses this by noting LPIPS is a complementary metric (line 186), but the prose still conflates the two. (Section 5.3, lines 185–191)

3. **The paper does not clearly distinguish its approach from MACE's multi-target strategy**: The introduction states that previous methods share a "common principle of mapping to a fixed, generic target" (line 18), but MACE (Lu et al., 2024) explicitly uses *multiple* target concepts. While MACE's targets are still predetermined rather than adaptively selected, the characterization is imprecise. The discussion should clarify how MACE's approach differs from AGE's and why AGE still outperforms it, especially since MACE achieves the best *preservation* metrics in the artistic-style experiment (Table 3).

### Trivial

None beyond what has been noted above; the paper is generally well-written.

## Nice-to-Haves

- A table or figure showing the top-3 concepts in the learned Gumbel-Softmax target mixture for a few erased concepts would strengthen the claimed interpretability.
- Confidence intervals or error bars on the main experimental results (Tables 1–3) would help assess the significance of the reported improvements, especially where margins are small (e.g., FID differences of 0.3–1.8).
- Additional preservation metrics for the artistic-style experiment (e.g., a style classifier if available) would strengthen the evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Abnormal concepts are not a new insight"** (Harsh Critic, Other Observations): The paper explicitly acknowledges that these concepts "have low generation capability even before the erasure" (line 77). The paper does not claim this as a novel insight — it is presented as an observation from the analysis. The criticism is valid in noting it is not deep, but it mischaracterizes the paper's claim. Removed per rule: strawman weakness that misunderstands the paper.

- **"Fatal: metric never defined"** (Harsh Critic, Critical Issue #1): The metric is operationally defined throughout Section 3.1 — $G_{c_e}(c_j)$ is a percentage (0–100%), $G_0(c_j) \approx 60\%$ and $\approx 100\%$ for different concepts, and the gap is $\Delta(c_e, c_j) = G_0(c_j) - G_{c_e}(c_j)$. The sentence at line 63 is incomplete (parser artifact), but the operational meaning is clear from context and figures. Downgraded from fatal to minor (see Minor Weakness #1) because the qualitative patterns (locality, asymmetry) are robust to the exact metric choice.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add an ablation experiment** comparing AGE with a fixed-target variant (e.g., target = "a photo" or a random concept) while keeping the minimax formulation and Gumbel-Softmax infrastructure identical. This would directly validate that adaptive targeting — not just the minimax framework — drives the preservation gains.

2. **Provide a precise specification of the bilevel optimization algorithm**: include the number of inner-loop steps per outer step, whether updates are alternating or simultaneous, the Gumbel-Softmax temperature, the composition of the search space C for each experiment, and the computational cost.

3. **Expand the concept-space analysis** to a larger and more diverse concept set (at least 50–100 concepts from diverse semantic categories) and provide a statistical test of locality (e.g., correlation of $\Delta(c_e, c_j)$ with CLIP text embedding similarity between concepts).

4. **Clearly define $G_{c_e}(c_j)$** with an explicit formula (e.g., $G_{c_e}(c_j) = \frac{1}{500} \sum_{i=1}^{500} \mathbf{1}[\text{classifier top-1}(x_i) = c_j]$ where $x_i$ are images generated with prompt $c_j$ from the sanitized model).

5. **Tone down the claim** of "first comprehensive study" to better reflect the limited scale of the analysis (25 concepts in 5 clusters).

## Score and Decision

The paper identifies a genuine limitation of fixed-target concept erasure and proposes a methodologically principled solution (minimax adaptive target selection) that achieves substantially better preservation than prior work. The main experimental results are strong and consistent across three tasks. However, the lack of an ablation isolating the adaptive target selection, together with incomplete implementation details and an overclaimed concept-space analysis, prevent the paper from being fully convincing in its current form. These weaknesses are addressable with additional experiments and clarifications.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>