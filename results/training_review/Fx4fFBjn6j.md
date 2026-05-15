Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes feedback-weight matching, a method to enable fine-tuning of pre-trained neural networks using Direct Feedback Alignment (DFA). The key idea is to decompose pre-trained weights to construct matched feedback matrices and re-initialize the weights accordingly, thereby inducing strong weight alignment (WA) and gradient alignment (GA). The method is combined with weight decay for additional benefits. Experiments on image classification (CIFAR-10, SVHN, STL-10) and NLP (BERT-Tiny, BERT-Small on GLUE tasks) show consistent improvements over standard DFA fine-tuning.

## Strengths

- **First theoretical diagnosis of DFA's failure in fine-tuning using the WA/GA framework**: Section 3.1 and Proposition 3.3 formally argue that pre-trained weights from back-propagation do not satisfy the strong WA condition required for effective DFA learning, going beyond prior empirical observations (Chu & Bacho, 2024) to provide a principled explanation.

- **Novel feedback-weight matching method with formal connection to WA and GA**: Definitions 3.4–3.5 and Proposition 3.6 propose and prove that decomposing pre-trained weights into matched feedback matrices and re-initializing weights forces strong WA, and Proposition 3.8 shows this directly improves GA in the first layer. The method is simple, mathematically grounded, and directly addresses the diagnosed root cause.

- **First successful DFA fine-tuning of Transformer models (BERT)**: Table 2 reports that standard DFA achieves only 0.00–0.10 correlation on CoLA/STSB, while feedback-weight matching achieves 0.29–0.53 and 0.76 respectively, demonstrating applicability to practical pre-trained architectures where prior DFA from-scratch training already struggled.

- **Ablation study isolating each component's contribution**: Table 3 systematically evaluates the effect of removing feedback matching, weight matching, and weight decay individually, showing that weight matching contributes the largest performance gain while all three components are needed for the full benefit.

- **Identified synergy between feedback-weight matching and weight decay**: Proposition 4.1 and Lemma 4.1 theoretically derive that the method reduces the network output error bound, and Table 4 shows weight decay improves accuracy by 8.35% on average with feedback-weight matching but has minimal impact without it.

- **Consistent gains across multiple architectures and tasks**: Table 1 shows feedback-weight matching outperforms standard DFA on all 8 image classification fine-tuning settings (e.g., 82.67% vs 74.70% on SVHN), and Table 2 shows gains on all 4 reported NLP tasks, demonstrating generality.

## Weaknesses

### Fatal
None.

### Major

- **Underspecified weight factorization procedure with unstated rank constraints (structural)**: The core of the method (Definition 3.4) requires decomposing the pre-trained weight \(W_{1<l<L}^0\) into \(\bar{F}_l \bar{F}_{l-1}^\top\). The paper never specifies how this factorization is performed algorithmically. Critically, \(\bar{F}_l\) is \(n_L \times n_l\) and \(\bar{F}_{l-1}\) is \(n_L \times n_{l-1}\), so their product has rank at most \(n_L\) (the output dimension). For image classification with 10 classes and hidden layers with hundreds or thousands of neurons, exact factorization is generally impossible unless the pre-trained weight is already low-rank (rank ≤ 10). The paper assumes exact equality (\( \equiv \)) without discussing approximation, truncation, or the error introduced by an approximate decomposition. Without a concrete algorithm (e.g., SVD truncation with rank analysis) and an analysis of the approximation error, the method is not fully implementable as described, and the theoretical guarantees (which rest on exact equality) are disconnected from practice. This is the paper's most significant weakness.

### Minor

- **"With high probability" in Lemma 4.1 is unquantified**: The lemma claims \(r_l \geq 0\) "with high probability" but specifies neither the probability distribution nor the confidence level, making the claim impossible to evaluate rigorously.

- **\(F_l^\top F_l \equiv I\) assumption not guaranteed by the method**: The paper notes (near Equation 4) that strong WA implies strong GA only "given \(F_l^\top F_l \equiv I\)" (a condition from Refinetti et al., 2021). The feedback-weight matching procedure does not ensure this orthonormality condition, creating a gap between the claimed GA benefit and what the method provably delivers.

- **Limited GLUE task coverage**: Only 4 of the standard GLUE tasks (CoLA, STSB, MRPC, RTE) are reported. Given that the paper claims general NLP fine-tuning capability, the omission of the majority of GLUE tasks (e.g., MNLI, QNLI, QQP, SST-2) raises a potential selectivity concern.

- **Missing experimental hyperparameters**: The paper does not report key training details (learning rate, batch size, number of epochs, optimization algorithm, weight decay schedules, feedback matrix dimension choices, or the specific factorization method used in practice), which hinders reproducibility.

- **No computational efficiency measurements**: The paper motivates DFA by its advantages (parallel updates, no back-propagation) but provides no timing, memory, or FLOPs measurements to substantiate that the method retains these benefits in the fine-tuning setting.

### Trivial
- The ablation text (line 214) has a cut-off value: the correlation score "drops from 0.76 to -0." with the second value incomplete.

## Nice-to-Haves
- Compare to DFA trained from scratch on the target dataset using the same factorized initialization (without pre-trained weights) to isolate whether the benefit comes from the pre-trained weights or simply from the factorized starting point.
- Report results on the full GLUE benchmark and include variance across multiple seeds.
- Provide computational overhead measurements (time and memory) for the factorization step and per-epoch training compared to back-propagation fine-tuning.
- Visualize the change in WA and GA over training for the Transformer experiments (Figure 1 is referenced but the data cannot be seen in the text version).

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Missing proofs in appendix**: The reviewer criticized that Propositions 3.3, 3.6, 3.8, and Lemma 4.1 lack formal proofs. The parser strips appendix sections from all papers; proofs exist in the original submission. Removed per instruction.
- **"First analysis" claim questioned given Chu & Bacho (2024)**: The paper explicitly cites Chu & Bacho's empirical observation and claims "first analysis" — the distinction between empirical observation and theoretical analysis is reasonable. Removed.
- **DFA on Transformers not specified**: The reviewer demanded architectural details for applying DFA to attention modules. The paper cites Launay et al. (2020) for the DFA-on-Transformers methodology, which is standard practice. Removed.
- **Proposition 3.3 lacks quantitative condition**: The reviewer criticized "unlikely" as vague. The proposition is a conceptual claim, not a quantitative bound. Removed.
- **WA/GA computation not explained for fine-tuning**: The paper defines both measures clearly in Definitions 3.1, 3.2, and 3.7. Removed.
- **Figures not visible**: Parser artifact. Removed.
- **Missing comparison to DFA with learned feedback / BP with DFA-like budget**: These are not standard baselines in the DFA fine-tuning literature; requesting them is scope creep. Removed.
- **Various formatting/style nitpicks**: Removed per instruction.

## Novel Insights

The reviewers' assessments surface an important tension that the paper itself does not fully address: the method's theoretical analysis assumes an exact factorization of pre-trained weights that is mathematically impossible under realistic dimensionalities (since the product \(\bar{F}_l \bar{F}_{l-1}^\top\) has rank bounded by the output dimension, typically 2–10). Yet the experiments show clear improvements. This suggests either that (a) the factorization is implemented via a low-rank approximation (e.g., SVD truncation) and still works, or (b) the strong WA/GA conditions can be meaningfully approximated rather than exactly satisfied. Neither possibility is discussed. This gap between the paper's theory (exact equality) and its practice (which must involve approximation) is the single most important issue the authors would need to resolve. A valuable contribution would be to analyze how the approximation error in the factorization propagates to WA/GA and final task performance, potentially showing that the method is robust to modest rank truncations.

## Suggestions

1. **Specify the factorization algorithm explicitly**: Provide the concrete procedure (e.g., SVD truncation to rank \(n_L\)), analyze the approximation error \(\|W_l^0 - \bar{F}_l \bar{F}_{l-1}^\top\|\), and discuss the conditions under which the approximation is faithful enough to still induce strong WA/GA.
2. **Quantify "with high probability" in Lemma 4.1**: Specify the distributional assumptions and confidence level, or replace with a cleaner deterministic bound.
3. **Report full experimental settings**: Provide learning rate, batch size, epochs, optimization algorithm, and the exact dimensionalities used in the factorization (including the rank of the truncated decomposition) to enable reproduction.
4. **Report performance on the full GLUE benchmark** or justify the subset selection.
5. **Add computational efficiency measurements** (training time, memory usage) to substantiate the efficiency motivation for DFA-based fine-tuning.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>