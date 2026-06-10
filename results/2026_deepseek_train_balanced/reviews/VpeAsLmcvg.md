Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes SiVA (Singular Value Adaptation), a PEFT method that computes the SVD of each pre-trained weight matrix, freezes the singular vectors U and V, and trains only the smallest k singular values via gradient descent. The method is motivated by a theoretical framework connecting effective rank to PEFT performance, and is evaluated across vision (ViT), language understanding (RoBERTa-Large on GLUE), language generation (GPT-2 Medium on E2E), and instruction tuning (LLaMA2-7B on Alpaca).

## Strengths

1. **Clean, principled method design**: SiVA formulates ΔW = U S V^T where U and V come from the pre-trained weight's SVD, and only the smallest singular values in S are trained. This is conceptually simple, directly motivated by the effective-rank hypothesis, and yields strong parameter efficiency (2× to 50× fewer trainable parameters than LoRA) while maintaining competitive performance across vision and language benchmarks. The ablation study (Table 6) directly validates the two key design choices — using W's singular vectors vs. random ones, and training the smallest vs. largest singular values — both showing clear performance drops when violated.

2. **Strong performance-per-parameter across multiple domains**: SiVA achieves competitive or best results on GLUE (RoBERTa-Large) with orders of magnitude fewer parameters, best or second-best scores across all four E2E NLG metrics with GPT-2 Medium, and on-par results with LLaMA2-7B instruction tuning. The per-parameter efficiency is consistently demonstrated (Figures 1 and 3).

3. **Deterministic, seed-independent formulation**: Unlike VeRA, FourierFT, and NOLA which rely on random bases and require storing random seeds, SiVA's U and V are derived deterministically from the pre-trained weights. This eliminates cross-layer crosstalk from shared random bases and removes dependence on RNG implementations — a genuine practical advantage that the paper correctly identifies.

4. **Ablation experiments directly tied to theoretical claims**: The ablation study in Table 6 tests exactly the two predictions from Theorems 2 and 3 (random vectors vs. aligned SVD vectors, bottom vs. top singular values) and confirms both predictions, providing empirical support that goes beyond aggregate performance comparisons.

## Weaknesses

### Major

1. **Theorem 1 contains a mathematically unjustified constraint for "arbitrary" B**: Theorem 1 states "‖B‖²_F = Σ(δσ_i)² ≤ C" where δσ_i = σ_i(A+B) − σ_i(A). This equates the Frobenius norm of B to the sum of squared changes in A's singular values. For an arbitrary matrix B, ‖B‖²_F = Σ σ_i(B)², and this is not generally equal to Σ(σ_i(A+B) − σ_i(A))² — the two quantities coincide only when A and B share singular vectors (or under other very specific conditions). The theorem therefore optimizes over a differently constrained space than claimed. This is a genuine mathematical slip in the paper's theoretical centerpiece. While the insight that training aligned, small singular values is sensible and the method works without this theorem, the framing as a rigorous derivation is compromised. (This weakness is partially mitigated by Theorem 3, which later shows alignment is optimal, but Theorem 1 is presented as a result about *arbitrary* B.)

2. **The central effective-rank hypothesis is supported by only a single dataset**: Contribution (i) claims that "the performance of transformer models on downstream tasks is correlated to the effective ranks of the query and value matrices." The evidence for this is Table 1 and Figure 1 (left), which show results on Stanford Cars (ViT-Base) alone. A correlation claim about "downstream tasks" generally — especially one used to motivate the entire method — requires broader support across multiple tasks, models, and perhaps layers. Without controlled experiments that vary effective rank independently of other factors, the direction of causality is also unclear: does higher effective rank cause better performance, or do better-tuned models incidentally have higher effective rank? This undercuts contribution (i).

### Minor

3. **The ≈13.5% improvement over SoTA on Stanford Cars lacks transparency**: Table 1 reports "accuracy score ≈13.5% above" other methods. This is an unusually large improvement that warrants careful scrutiny. No error bars, confidence intervals, or breakdown of which methods are compared are visible in the extracted text, and the specific experimental conditions (hyperparameters, selection protocol) for this result are not described. Providing standard deviations and a detailed experimental setup would increase confidence.

4. **SVD computational cost is not acknowledged**: SiVA requires computing the full SVD of every query and value weight matrix as a one-time initialization step. For LLaMA2-7B (32 layers × 2 matrices = 64 SVDs on 4096×4096 matrices), this is a non-trivial O(d³) cost per SVD. The paper compares methods purely on trainable parameter count without discussing this initialization overhead, the memory required to store full U and V matrices during training, or comparing against the negligible initialization cost of LoRA or random-basis methods. This makes the efficiency comparison incomplete.

5. **Missing error bars on GLUE results**: The paper reports means over 5 random seeds for GLUE but does not report standard deviations or show whether differences between methods are statistically significant (lines 155, 159). Given that many of the reported differences are small (1–2 points on some tasks), this makes it hard to assess whether SiVA's advantages are meaningful.

6. **No comparison against recent strong PEFT baselines**: Methods like DoRA (Liu et al., 2024) and PiSSA (Meng et al., 2024), which also modify weight matrix initialization, are not included in the comparisons. Since these are contemporary works operating in the same paradigm, their absence weakens the "state-of-the-art" positioning.

### Trivial

- None.

## Nice-to-Haves

- A more thorough analysis of how effective rank evolves during training across different layers and tasks would strengthen the paper's motivating hypothesis.
- Wall-clock training and inference time comparisons would provide practical context for the parameter-count advantages.
- An ablation varying k (the number of trained singular values) and comparing against training *all* singular values would directly test the sparsity claim from Theorem 2.

## Removed Points

The following points from the inputs were removed with justification:

- **Claim that the CV experiments section is "entirely missing"**: The paper explicitly states "experiments conducted across 7 datasets using ViTBase architecture" (Figure 1 right caption), mentions "ViT-Base and Large variants for image classification" (Section 4), and shows ablation on three CV datasets (Table 6). The specific result tables appear in image form that the text parser could not capture, but this is a parser artifact, not a paper omission.

- **Claim about Theorem 1 being "fatal" / "structural"**: Demoted to Major. The theorem has a genuine mathematical slip, but the method does not depend on this particular theorem for its validity — the empirical results stand independently, and the intuition (train small aligned singular values) is sound. The paper's framing as a "theoretical framework" rather than a formal proof also tempers the severity.

- **Criticism about "extraordinary claim of ≈13.5%" lacking any experimental foundation**: The paper does contain CV results (7 datasets, ViT-Base/Large). The ≈13.5% figure is stated in Table 1's caption; the results exist in the paper's figures. The lack of error bars is a separate, legitimate concern (retained as Minor weakness #3), but the claim that no experimental foundation exists is incorrect.

- **Generic criticism that the theoretical contribution is "substantially weaker than the paper's framing suggests"**: This is an opinion rather than a specific, verifiable weakness. The specific Theorem 1 issue is retained; the general dismissal is removed.

- **Strength claiming the theoretical framework is "rigorous"**: The Theorem 1 issue shows the framework is not fully rigorous. Tempered to "theoretically motivated."

- **Strength claiming the effective-rank discovery as "novel empirical discovery" with full support**: Demoted because the evidence is limited to one dataset.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses primarily surface issues with the paper's theoretical framing and evidential support rather than offering independent novel insights about the problem.

## Suggestions

1. Fix the mathematical framing of Theorem 1: either (a) explicitly restrict the claim to the setting where A and B share singular vectors (which Theorem 3 later establishes as optimal), or (b) use the Mirsky inequality to state a proper bound rather than an equality. The current "arbitrary B" framing is mathematically imprecise.

2. Broaden the evidence for the effective-rank correlation claim (contribution i) to multiple datasets and models beyond Stanford Cars, with controlled experiments that disentangle correlation from causation.

3. Disclose the computational overhead of SVD initialization (wall-clock time, memory) and compare it against the initialization cost of competing methods, so readers can evaluate the full practical trade-off.

4. Add standard deviations or confidence intervals to all main results tables, especially GLUE where many methods score within a narrow range.

5. Include DoRA and PiSSA as baselines for a more complete comparison.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>