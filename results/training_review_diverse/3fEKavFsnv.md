Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper studies MGT detection using kernel-based Maximum Mean Discrepancy (MMD). It identifies a key issue: when MGTs come from multiple LLM populations, the standard MMD training objective (MMD-D) suffers from inflated variance, degrading detection stability. The proposed solution, MMD-MP, removes the intra-class MGT term $k_\omega(y,y')$ from the training objective, yielding variance reduction and improved detection. The paper provides theoretical analysis (asymptotics, test power, uniform convergence) and extensive experiments across multiple LLMs showing consistent gains, particularly dramatic improvements (23-27% absolute test power) when detecting texts from unknown/unseen LLMs.

## Strengths

1. **Clear diagnosis of a practically important problem**: The paper identifies and empirically demonstrates that standard MMD training degrades when MGTs come from multiple LLM populations due to variance inflation. The variance decomposition analysis (Section 2.3) and Figure 2 concretely show how the $k_\omega(y,y')$ term drives this issue. This is a novel and well-motivated observation.

2. **Simple, well-motivated fix with strong empirical validation**: Removing the $k_\omega(y,y')$ term during training (MMD-MP) is a clean modification directly targeting the diagnosed problem. The results consistently show MMD-MP outperforming MMD-D across nearly all settings. The most striking results are on unknown LLM texts (Tables 5-6), where MMD-MP achieves 23.61%-27.65% absolute test power improvements over MMD-D and 3.25% AUROC improvement — evidence of genuinely better transferability.

3. **Strong performance under challenging conditions**: The method shows substantial gains when training data is limited (Table 2: 8.20% average improvement over MMD-D on 2 populations, 13.97% on 3 populations) and when data is unbalanced (Figure 3: 6.96%-14.40% improvement). These are practically relevant scenarios where existing methods struggle.

4. **Theoretical grounding beyond typical MGT detection papers**: Proposition 1, Corollary 1 (asymptotic test power analysis), and Theorem 1 (uniform convergence bound) provide theoretical support for the modified objective, which is more analysis than most papers in this area provide.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Training-testing objective mismatch**: The kernel is trained using the MPP objective (which excludes $k_\omega(y,y')$) but evaluated using the full MMD (which includes it). The paper provides a practical justification (Remark 2: MPP does not converge properly under $\mathfrak{H}_0$, so full MMD is needed for testing) and notes that empirically the two strategies give nearly identical results. However, this gap means the theoretical claims about MPP's variance properties are not directly linked to the actual test-time behavior. The paper would benefit from either a theoretical argument connecting MPP-optimal kernels to full-MMD test power, or a cleaner evaluation protocol where the test uses MPP directly with an appropriate threshold.

2. **Improvements on single-population detection are modest and may lack statistical significance**: On single-population ChatGPT detection (Tables 1-2), MMD-MP vs. MMD-D differences are small (e.g., 93.21 vs. 91.76, 92.31 vs. 91.38) with overlapping error bars. No significance tests are reported. The method's strength clearly lies in multi-population and transfer settings rather than single-population, and the paper should be more careful not to overclaim in this regime.

3. **C2ST baselines perform anomalously poorly**: C2ST-S achieves test power as low as 27.65 on Neo-S and 24.53 on multi-population settings — sometimes barely above chance. A classifier-based two-sample test with a reasonable architecture should capture _some_ signal. The paper does not discuss whether this reflects architectural choices, training issues, or fundamental limitations. This does not affect the paper's own contributions but weakens the baseline comparisons.

4. **Theoretical bound has limited practical force**: Theorem 1's uniform convergence bound scales with $\sqrt{D \log(R_\Omega n)}$ where $D$ is the parameter space dimension. For the deep neural network $\phi_{\hat{f}}$ used in experiments, $D$ could be very large, making the bound potentially vacuous. The $\mathcal{O}(n^{-1/3})$ rate is also slower than the standard $\mathcal{O}(n^{-1/2})$. This does not invalidate the empirical results, but it means the theory section contributes less rigor than its framing suggests.

### Trivial

1. **"Pairing rules" is used as an informal, undefined concept** (Section 2.3, line 149). The intuition is clear from context, but the term lacks a formal definition.

2. **Unbalanced experiment (Figure 3) description is sparse** — the caption and Section 5.3 give minimal detail about the setup beyond "2,000 HWT and 400 MGT training paragraphs."

## Nice-to-Haves

- A controlled experiment holding total MGT training size fixed while varying the number of LLM populations would more cleanly isolate the multi-population effect from simply having more training data.
- An ablation where the $k_\omega(y,y')$ term is down-weighted (rather than fully removed) via a hyperparameter $\lambda$ would test whether complete removal is necessary or just reducing the term's influence suffices.
- Reporting statistical significance (e.g., paired t-tests) for key comparisons where error bars overlap would strengthen the claims.

## Removed Points

- **"Missing experimental details (architecture, hyperparameters)"**: Per instructions, the parser strips appendix content. These details likely exist in the original submission.
- **"Synthetic experiment varies μ not population count"**: The real experiments (Tables 1-2) do vary the number of LLM populations, which is the actual test. The synthetic experiment evaluates a related but different aspect (variance magnitude). The criticism is partially addressed by the paper's existing experiments.
- **"No proof of Theorem 1 in main text"**: Per instructions, proofs are typically deferred to the appendix which the parser strips.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the training-testing mismatch as the key unresolved tension in the paper's framing, and the observation that the method's largest gains come in transfer/unknown-LLM scenarios (suggesting the mechanism is primarily about avoiding overfitting to diversity in $S_\mathbb{Q}$ rather than directly modeling multi-population structure). These are useful clarifications but the paper already covers them implicitly.

## Suggestions

1. Address the training-testing gap directly: either develop a test that uses MPP (with a corrected threshold), or provide a theoretical argument (e.g., the gradient of MPP is an unbiased estimate of the MMD gradient gradient under mild conditions) connecting the two. At minimum, show that the optimal kernel for MPP is near-optimal for full MMD.
2. Add statistical significance tests for comparisons where error bars overlap (e.g., single-population ChatGPT).
3. Discuss why C2ST-S/C2ST-L perform so poorly in the paper's setup — this is important context for practitioners reading the paper.

## Score and Decision

This paper makes a genuine contribution: it identifies a real and consequential problem (variance inflation in MMD from heterogeneous MGT populations), proposes a clean fix, and validates it with strong empirical results — especially the transferability gains (23-27% test power). The training-testing mismatch is the main unresolved tension, but it does not undermine the empirical findings. The weaknesses identified are minor relative to the contribution: the method works, the improvement is clear in the settings that matter (multi-population, limited data, unbalanced data, unknown LLMs), and the theoretical framing, while imperfect, adds value. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>