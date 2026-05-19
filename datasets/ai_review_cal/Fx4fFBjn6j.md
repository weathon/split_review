- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5
Now I have all the information needed. Here is the finalized consolidated review.

---

## Summary

This paper introduces *feedback-weight matching*, a method to enable Direct Feedback Alignment (DFA) for fine-tuning pre-trained fully connected networks. The approach reconstructs DFA feedback matrices by decomposing pre-trained weights (feedback matching) and then re-expresses the weights in terms of those matrices (weight matching). This induces strong weight alignment (WA) and gradient alignment (GA), which standard DFA fails to achieve during fine-tuning. Experiments on image classification and BERT fine-tuning show significant improvements over standard DFA, including the first successful DFA fine-tuning of Transformer models. A theoretical analysis connects the method to WA/GA and shows a synergistic effect with weight decay.

## Strengths

1. **Novel method with formal grounding in WA/GA theory.** Definitions 3.4–3.5 and Proposition 3.6 provide a principled argument that feedback-weight matching induces strong weight alignment, and Proposition 3.8 shows direct gradient-alignment improvement for two-layer networks. This is a clear departure from prior DFA methods that rely on fixed random feedback and offers a theoretical lens missing from earlier empirical studies (e.g., Chu & Bacho, 2024).

2. **First theoretical analysis of why DFA fails at fine-tuning.** Proposition 3.3 provides a formal argument (via the weak/strong WA framework) showing that standard DFA with random feedback matrices cannot satisfy strong weight alignment when starting from backpropagation pre-trained weights. This goes beyond prior observations of instability and gives a concrete explanation.

3. **First successful DFA fine-tuning of Transformer models (BERT).** Table 2 reports that feedback-weight matching achieves a 0.76 Pearson correlation on STSB (BERT-Small) versus 0.10 for standard DFA, and 0.53 Matthews correlation on CoLA versus 0.06. Standard DFA is described as "barely conducting fine-tuning at all" on these tasks, and prior work (Launay et al., 2020) found DFA difficult even for from-scratch Transformer training.

4. **Ablation study isolating each component.** Table 3 systematically removes feedback matching, weight matching, and weight decay. Weight matching is shown to be critical (e.g., correlation drops from 0.76 to -0.0 without it), and weight decay has minimal effect without feedback-weight matching, supporting the claim of a synergistic effect.

5. **Quantitative WA/GA tracking confirming the theoretical predictions.** Figure 1 directly plots WA and GA over training epochs. The proposed method achieves high WA and GA from the start, while standard DFA shows low initial values, visually corroborating the theoretical analysis in Sections 3.2 and 3.3.

## Weaknesses

### Fatal
None.

### Major

1. **The decomposition step (Equation 6) is underspecified.** The paper requires decomposing the pre-trained weight \(W_{1<l<L}^0\) into \(\bar{F}_l \bar{F}_{l-1}^\top\) (and \(W_L^0\) into \(\bar{F}_{L-1}^\top\)) but provides no concrete algorithm, pseudocode, or discussion of how this is performed in practice. Questions left unanswered: (a) What are the dimensions of \(\bar{F}_l\)? Standard DFA feedback matrices are \(n_l \times n_L\); are the reconstructed matrices the same shape? (b) What method is used — SVD, Cholesky, learned factorization? (c) What happens when the factorization can only be approximate (e.g., when the weight matrix is full-rank and the target factorization rank is constrained)? Without this specification, a central step of the method is not reproducible as described. This is the paper's most significant gap and must be addressed.

2. **Empty Limitations section.** Section 6 ("Limitations and Future Works") is a complete placeholder with no content. The paper does not discuss: the performance gap relative to backpropagation (averaging 2.32% on image tasks and larger on NLP tasks), the restriction to fully connected architectures, computational overhead of the factorization, or generalizability to other pre-training/fine-tuning scenarios. An explicit discussion of limitations is standard for a paper of this scope.

### Minor

3. **Theoretical analysis in a simplified setting.** Propositions 3.6 and 3.8 are proved for *linear* fully connected networks, while experiments use non-linear networks (ReLU) and Transformers. Conjectures 3.9 and 4.2 explicitly remain unproven. While this is common practice in ML theory papers, the gap between theory and experiment is larger than ideal. The paper would benefit from tightening this connection or being more explicit about what the theory does and does not cover.

4. **No variance or confidence intervals reported.** Given that performance improvements in some settings are modest (e.g., 1–3% on several image tasks), the absence of any measure of variability (multiple seeds, confidence intervals) makes it difficult to assess the statistical significance of the reported gains.

5. **No discussion of computational overhead.** The factorization step could be non-trivial for large layers (e.g., BERT's attention projections). Since one of DFA's purported advantages is efficiency, discussing the cost of feedback-weight matching relative to standard DFA or BP fine-tuning would be informative.

6. **Missing experimental details.** Details such as learning rate schedules, number of epochs, hyperparameter tuning protocol, and validation splits are not reported, which hurts reproducibility despite the promise of anonymous code release.

### Trivial
None.

## Nice-to-Haves
- Including a concrete example of the factorization (e.g., via SVD) for a small network would clarify the method significantly.
- Comparison against additional backpropagation-free fine-tuning baselines (e.g., training only a linear classifier, random projection methods like LoRA with random weights) would strengthen the empirical positioning.
- Measuring the distance (e.g., Frobenius norm) between original and re-initialized weights to explicitly verify they are equal in practice.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Weight matching discards pre-trained knowledge" (Harsh Critic's Issue 2).** Removed because it is factually incorrect. Equations (6) and (7) define \(\bar{F}_l \bar{F}_{l-1}^\top \equiv W_{1<l<L}^0\) and \(\bar{W}_{1<l<L}^0 \equiv \bar{F}_l \bar{F}_{l-1}^\top\), so \(\bar{W}_l^0 = W_l^0\). The re-initialized weights are *exactly* the original pre-trained weights by construction. The critic's concern that "new weights are not equal to the old ones" misunderstands the paper.

2. **"Comparison to standard DFA is not fair because weight initialization differs" (Harsh Critic's Issue 3).** Removed because it stems from the same misunderstanding. Since \(\bar{W}_l^0 = W_l^0\), both methods start from identical weights, and the ablation study in Table 3 already covers the relevant conditions (removing feedback matching or weight matching individually). The requested 2×2 ablation collapses to conditions already tested.

3. **"No algorithm or pseudocode" listed as a missing part.** Partially addressed by the retained Major weakness #1 (the decomposition is underspecified). The separate framing as a "missing part" is redundant.

4. **Various formatting/style nitpicks and criticisms about missing appendix content.** Removed per instructions — the parser strips appendices from all papers.

## Novel Insights

The Harsh Critic's observation that the decomposition step is underspecified is the most actionable finding: it identifies a concrete reproducibility gap that the authors can fix without changing the core idea. However, beyond the paper's own contributions, the reviews do not surface a genuinely novel synthesis. The Strength Finder correctly identifies the paper's main contributions but does not add new analytical insight beyond what the paper itself provides. None beyond the paper's own contributions.

## Suggestions

1. **Specify the factorization algorithm concretely.** Provide either (a) a direct formula using SVD (e.g., \(\bar{F}_l = U\Sigma^{1/2}, \bar{F}_{l-1}^\top = \Sigma^{1/2}V^\top\) from \(W_l^0 = U\Sigma V^\top\)), or (b) an iterative method, and state what rank \(r\) is used and how dimensions are handled for non-square layers. Include a short pseudocode block.

2. **Fill the Limitations section** with a candid discussion of: the performance gap to backpropagation, the restriction to fully connected architectures (and attention layers that can be treated as such), potential computational overhead, and settings where the method would not apply.

3. **Report results with multiple seeds** (at least 3–5) with means and standard deviations, especially for the smaller-gap settings (1–3% improvements) to establish statistical significance.

4. **Add experimental details** (learning rate, epochs, scheduler, validation protocol) either in the main paper or an appendix.

5. **Make the theory-experiment bridge clearer** by explaining which parts of the theoretical analysis are expected to carry over to the non-linear case and which remain conjectural.
