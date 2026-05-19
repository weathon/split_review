- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6
Now I have all the information needed to produce a consolidated review. Let me synthesize.

## Summary

This paper proposes ReDeEP, a method for detecting hallucinations in RAG systems by using mechanistic interpretability to decouple the LLM's use of external context (via Copying Heads' attention patterns) from its reliance on parametric knowledge (via Knowledge FFNs' logit-lens divergence). The authors identify empirical correlations and attempt causal interventions linking these components to hallucinations, then combine ECS and PKS as covariates in a linear regression detector. Experiments on LLaMA2-7B/13B and LLaMA3-8B across RAGTruth and Dolly(AC) show consistent improvements over a range of baselines.

## Strengths

1. **Novel and well-motivated framing.** The paper correctly identifies that existing RAG hallucination detection methods treat parametric and external knowledge as confounded (Figure 2), and proposes to decouple them via mechanistic interpretability. This is a genuinely new perspective on the problem.

2. **Strong and consistent empirical results.** ReDeEP(chunk) achieves the best or second-best AUC, F1, and recall across all three model families and both benchmarks (Table 1). On LLaMA2-7B Dolly(AC), ReDeEP(chunk) AUC=0.7949 vs the best baseline (Trulens) at 0.7110 — a substantial gap. On LLaMA2-13B Dolly(AC), the gap is even larger (0.8420 vs 0.8089). The chunk-level variant nearly always improves over token-level, validating the design.

3. **Cross-model and cross-dataset generalization.** The method works on LLaMA2-7B, LLaMA2-13B, and LLaMA3-8B without apparent degradation, and generalizes from RAGTruth to Dolly(AC), which covers different task types (QA, summarization, information extraction).

4. **Empirical grounding of mechanistic components.** The paper systematically identifies that 1006/1024 attention heads show higher ECS on truthful vs. hallucinated responses (Figure 3a), and that later-layer FFNs have positive PKS-hallucination correlation (Figure 3e). These are concrete, quantifiable findings.

## Weaknesses

### Fatal
None.

### Major

1. **Core detection method's parameters are underspecified.** The hallucination score H(t) = Σ_{l∈F} α·P^l_t - Σ_{l,h∈A} β·E^{l,h}_t depends on four unspecified quantities:
   - **(i) Set A (Copying Heads):** Identified via OV-circuit eigenvalues, but no threshold or procedure is stated (line 48 just says "analyzing the positive eigenvalues"). 
   - **(ii) Set F (Knowledge FFNs):** Defined as "later layers that show strong correlations" (line 163), but which specific layers and what threshold constitutes "strong" is not specified.
   - **(iii) α and β:** Called "regression coefficients" (line 222) with the note that they are "> 0," but the paper never states whether they are learned (and if so, on what data, with what objective, and using what normalization) or set by hand. This makes the method un-reproducible.
   - **(iv) Transfer across models:** The empirical study identifies components on LLaMA2-7B, but it is unclear whether the same layer/head indices are transferred to LLaMA2-13B and LLaMA3-8B or re-identified — critical information since these architectures differ.

2. **Causal intervention experiment is too vaguely described to validate the causal claim.** The paper states only that noise was "applied to attention scores" and FFN outputs were "amplified" (line 184). No details are given on: noise type and magnitude, amplification factor, or how the experimental vs. control groups were exactly defined beyond "Copying Heads/Knowledge FFNs" versus "Other heads/FFNs." Without these details, the reader cannot assess whether the larger NLL difference in the experimental group reflects genuine causal involvement or confounding disruption of general processing. The paper's central claim of a *causal* relationship rests on this experiment, making this gap significant.

### Minor

1. **ECS uses last-layer hidden states without justification.** Equation (3) computes ECS using the *last-layer* hidden states of attended tokens. The paper does not explain why representations from the final layer (which aggregate all prior processing) are preferred over representations from the layer of the head under consideration. This choice conflates information across layers and may obscure head-specific contributions.

2. **Embedding model for chunk-level detection is not named.** Line 226 mentions "an embedding model (emb)" for chunk-level semantic similarity, but the specific model (e.g., sentence-transformers variant) is not stated, harming reproducibility.

3. **AARF threshold τ is not defined.** For mitigation, the paper uses a threshold τ (line 251) to decide when to intervene, but never specifies how it is chosen, what its value is, or whether it is tuned.

4. **No confidence intervals or significance tests in Table 1.** The main results table reports point estimates only. Given the variability inherent in hallucination detection, it is unclear whether the reported improvements (e.g., 0.74 vs 0.73 AUC) are statistically reliable.

5. **AARF evaluation is limited.** The mitigation results (Figure 6) report only GPT-4o pairwise preferences without numerical hallucination rates, making it hard to gauge the practical benefit or to compare against other mitigation approaches.

### Trivial
- The causal confounding diagrams in Figure 2 are described in the text with labels (i), (ii), (iii) but the figure uses color coding — a minor cross-reference mismatch.

## Nice-to-Haves

- Report the learned α and β values (and standard errors if applicable) to demonstrate that the regression does not rely on extreme or unintuitive weighting.
- Provide an ablation showing the effect of varying the Copying Heads eigenvalue threshold and the Knowledge FFN layer selection on detection performance.
- Add a scatterplot of ECS vs. PKS colored by hallucination label to visualize the joint decision boundary, complementing the correlation numbers.
- Report the computational overhead of accessing internal activations compared to black-box baselines.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Scaling sensitivity of the combined score" (Harsh Critic's Issue 3):** If α and β are learned regression coefficients, the regression automatically adjusts for scale differences between ECS and PKS. The concern that the linear combination is "dominated by one component" assumes fixed/shared coefficients, which contradicts the stated "regression coefficients" framing (even if the learning procedure is underspecified). This is superseded by Major weakness #1.
- **"Pearson correlation may miss non-linear relationships":** Pearson is the standard correlation measure in this setting. This is a generic methodological preference, not a specific flaw.
- **"Copying Heads identification data leakage":** Copying Heads are identified via OV-circuit eigenvalues, which depend only on model weights, not on labeled data. No label leakage is possible. The Knowledge FFNs are identified on the training set, but the test-set evaluation is held out — this is standard practice.
- **"The chunk-level attention computation is expensive":** Chunk-level attention weights are obtained by mean-pooling the *already computed* token-level attention matrix — no additional forward pass is required. The cost concern is overstated.
- **Strength Finder's "causal intervention validation":** The strength finder claims this is "stronger empirical evidence than typical observational studies," but as noted in Major weakness #2, the intervention is too vaguely described to support that claim. The attempt is commendable, but the evidence as presented is weak.
- **Generic strengths about "addressing an important problem" or "extensive evaluation":** These lack specific, concrete evidence anchors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fully specify the parameter estimation pipeline.** State: (i) how Copying Heads are selected (OV eigenvalue threshold), (ii) which layers are included in F and why, (iii) whether α and β are learned via logistic/linear regression on a validation split, and (iv) whether these sets are re-identified per model or transferred from LLaMA2-7B.
2. **Describe the causal intervention in full detail.** Include noise type, magnitude, amplification factor, and exact experimental/control group definitions.
3. **Name the embedding model used for chunk-level detection.**
4. **Add confidence intervals or bootstrapped standard errors** to Table 1 for key metrics (AUC, F1).
5. **Report τ for AARF** and describe how it was chosen.
