## Summary

This paper proposes "feedback-weight matching," a method to enable reliable fine-tuning of pre-trained neural networks using Direct Feedback Alignment (DFA). The key insight is that standard DFA fails during fine-tuning because back-propagation pre-trained weights do not satisfy the strong weight alignment (WA) condition needed for DFA to work. The proposed method performs two steps: (1) reconstruct feedback matrices by decomposing pre-trained weight matrices, and (2) re-initialize weights to match those reconstructed feedback matrices, thereby inducing strong WA and gradient alignment (GA). Experiments on image classification (CIFAR-10, SVHN, STL-10) and NLP (GLUE with BERT) show substantial improvements over standard DFA fine-tuning.

## Strengths

1. **Novel problem framing with principled diagnosis.** The paper identifies a concrete, theoretically grounded cause for DFA's failure in fine-tuning: pre-trained weights do not satisfy strong WA (Proposition 3.3). This goes beyond prior observations of difficulty (Chu & Bacho, 2024) by tracing the problem to a specific structural condition, and the proposed method directly targets this cause. Applying WA/GA analysis to the fine-tuning setting is a genuine contribution.

2. **Large and consistent empirical gains.** The method achieves a 7.97% accuracy improvement on SVHN (6-layer network: 82.67% vs. 74.70% for standard DFA), and raises Pearson correlation on STSB from 0.10 to 0.76 with BERT-Small (Table 2). These are substantial, task-spanning improvements that convincingly demonstrate the method's effectiveness.

3. **Clean ablation study isolating component contributions.** Table 3 shows that removing weight matching causes a large accuracy drop (e.g., 83.16% to 79.77% on SVHN) while removing feedback matching has a smaller effect. This decomposition of the method into two mechanisms is informative and honest — it shows which component drives the gain.

4. **Demonstration of weight decay synergy.** The paper shows theoretically (Proposition 4.1) and empirically (Table 4) that weight decay improves accuracy by 8.35% on average when combined with the proposed method, while having minimal effect without it. This is a non-obvious finding that extends prior FA+weight-decay analysis to the DFA fine-tuning setting.

## Weaknesses

### Fatal

None.

### Major

1. **The core decomposition procedure is underspecified, making the method non-reproducible from the paper alone.** Equation (6) states that for intermediate layers, $\bar{F}_l \bar{F}_{l-1}^\top \equiv W_{1<l<L}^0$ — a decomposition of pre-trained weights into feedback factors. The paper provides no algorithm, no SVD, no rank constraint, no iterative procedure, and no regularization to accomplish this. The problem is nontrivial because each $\bar{F}_l$ appears in two adjacent decomposition equations (for layer $l$ and layer $l+1$), creating consistency constraints. The text simply says "Equation (6) requires us to decompose the pre-trained weight" without saying how. The grep for "SVD," "factorization," "pseudo-code," or "Algorithm" returned zero matches. The paper claims code is available, but the paper itself does not define its own central operation. This is not a minor omission — it is the method itself. A reader cannot tell whether the claimed improvements stem from the intended mechanism or from an arbitrary implementation choice for the factorization.

2. **Theoretical argument for Proposition 3.6 (that the method induces strong WA) is asserted, not proven.** Proposition 3.6 states that after feedback-weight matching, DFA updates induce strong WA. No proof or dynamical argument is given — it is simply claimed. The original Refinetti et al. (2021) analysis shows strong WA emerges from specific training dynamics over time; the paper does not establish that those same dynamics hold after re-initialization. This weakens the theoretical scaffolding: Lemma 4.1 then uses the strong WA expression ($W_l^t = c_l^t \bar{F}_l \bar{F}_{l-1}^\top$) to derive error bounds, but whether strong WA actually holds under the method is not rigorously established. The logical chain (Proposition 3.6 → Lemma 4.1 → Proposition 4.1) has a weak link at the start.

### Minor

1. **Details of applying the method to BERT are sparse.** The paper says feedback-weight matching is applied to "attention, intermediate, and block outputs of the encoder layers in a similar way to previous works (Launay et al., 2020)." But Launay et al. applied standard DFA (random feedback matrices) to Transformers — they did not decompose pre-trained weights into feedback matrices. The paper does not explain how the factorization in Equation (6) handles non-square attention projection matrices, how the consistency constraint propagates across BERT's many weight matrices, or whether the factorization is applied per-component or globally. Given that the NLP results show the largest gains over standard DFA, this omission is significant.

2. **Method is framed as "fine-tuning" but involves re-initialization.** Equation (7) replaces pre-trained weights $\bar{W}_l^0$ with $\bar{F}_l \bar{F}_{l-1}^\top$. If the decomposition is not exact (e.g., due to rank constraints or dimension mismatches), the re-initialized weights differ from the original pre-trained weights. The paper claims the method "preserves the knowledge embedded in the pre-trained weights" (line 110) without testing this — e.g., by measuring the re-initialized network's accuracy on the original pre-training task before any DFA fine-tuning. This gap between the "fine-tuning" framing and the actual operation should be acknowledged.

3. **The theoretical analysis is conducted on linear networks (Propositions 3.8, 4.1) and two-layer non-linear networks, then conjectured to generalize.** This is standard practice, but the gap between these simplified settings and the actual experiments (6-layer networks with ReLU, Transformer architectures with layer norm and residual connections) is large. The paper could strengthen its claims by testing on intermediate network depths or providing evidence that the key lemmas hold empirically.

### Trivial

- Figure 1's axis labels and legend colors are hard to distinguish in grayscale reproduction.

## Nice-to-Haves

- **Intermediate baselines for DFA fine-tuning.** The paper compares only against standard DFA (random feedback matrices). It would be informative to see results for hybrid approaches (e.g., DFA on the classification head only while keeping the encoder frozen, or applying DFA only to a subset of layers) to better isolate where the difficulty lies.
- **Rank and computational cost of the factorization.** Reporting the rank of the factorized feedback matrices and the cost of computing the decomposition (vs. standard DFA or BP fine-tuning) would help readers assess practical trade-offs.
- **Exact vs. approximate decomposition.** Clarify whether the $\equiv$ in Equation (6) demands exact equality or allows approximation, and if approximate, how the error is measured and controlled.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First" claim is overstated (Chu & Bacho 2024).** The paper acknowledges Chu & Bacho (2024) in lines 12 and 43, which studied the instability of switching from BP to DFA. The paper's claim ("first attempt... via an in-depth study") is distinguishably about proposing and analyzing a solution, not just observing the problem. This criticism misunderstands the paper's scope.
- **"Standard DFA baseline is a strawman."** Comparing against standard DFA fine-tuning (random feedback) is the natural baseline — it is the method that the paper aims to improve. Suggesting the authors should have tested DFA on a subset of layers or hybrid DFA/BP is scope creep. The paper shows its method works; exploring all possible intermediate DFA variants is not required.
- **"Limitations section is missing."** The paper has a "LIMITATIONS AND FUTURE WORKS" section (line 232); its emptiness in the extraction is a parser artifact. Parser-stripped content should not be held against the paper.
- **"Weight matching discards pre-trained knowledge."** If the decomposition is exact ($\bar{F}_l \bar{F}_{l-1}^\top \equiv W_l^0$), then $\bar{W}_l^0 = W_l^0$ and nothing is discarded. This criticism depends on whether the decomposition is approximate, which is part of the underspecification issue (kept as Major Weakness #1). As a standalone point it is not supported without evidence that the decomposition is inexact.
- **"The paper should also cover Y / additional tasks"** — demands for breadth outside the paper's scope.

## Novel Insights

The harsh critic's observation that the ablation study (Table 3) hints weight matching may be the dominant component (feedback matching contributes marginally) is worth highlighting — the critic frames this as a potential weakness, but it is actually a strength of the paper's empirical honesty. The paper acknowledges (line 214) that removing feedback matching yields only a marginal decline because the re-initialized weights are "amenable to arbitrary random feedback matrices." This suggests the method might work almost as well with weight matching alone (re-initializing to factorized weights) + random feedback, and the feedback-matching step is secondary. This is a genuinely useful insight that future work could investigate further: is the factorization of feedback matrices necessary, or is the weight re-initialization the critical step? The paper's current theory (Proposition 3.6) says both are needed for strong WA, but the ablation suggests otherwise.

## Suggestions

1. **Specify the decomposition algorithm.** This is the single most important fix. Provide pseudo-code: is it an SVD truncated to a specific rank? A least-squares decomposition? Does it enforce the adjacent-layer consistency constraint, and if so, how? Without this, the method is incompletely defined in the paper. If the code is the only full specification, state this explicitly and reference the relevant file/function.

2. **Strengthen the theoretical grounding of Proposition 3.6.** Provide at least a sketch of why the re-initialized weights combined with matched feedback matrices induce strong WA under DFA dynamics. If a full proof is not possible, state the conditions under which strong WA holds and verify them empirically (as the paper already does in Figure 1).

3. **Provide BERT-specific details.** Explain how the factorization applies to each BERT sub-layer (self-attention Q/K/V projections, output projection, intermediate feed-forward, layer normalization scaling factors if applicable). A table showing which weight matrices are decomposed and the resulting feedback matrix dimensions would largely resolve the concern.

4. **Verify knowledge preservation.** Measure the accuracy/loss of the re-initialized network ($\bar{W}_l^0$) on the original pre-training data or a held-out validation set, compared to the original pre-trained weights ($W_l^0$). This would directly test the claim that "knowledge embedded in pre-trained weights is preserved."

## Score and Decision

The paper addresses an interesting and practically relevant problem, and the empirical results are strong and well-documented. The ablation study is informative, and the weight-decay synergy finding is a genuine contribution. However, the paper has a significant structural weakness: the core method is not fully specified in the paper. The decomposition in Equation (6) is the central algorithmic operation, yet no algorithm, pseudo-code, or implementation strategy is provided. A reader cannot reproduce the method from the paper alone. Combined with the unsubstantiated Proposition 3.6 and the sparse BERT details, the paper as submitted falls short of the completeness standard for acceptance. The underlying idea and empirical validation are promising enough to warrant a resubmission with the missing specification filled in.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>