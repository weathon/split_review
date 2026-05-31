Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper identifies three "discordances" (aggregation error, noise amplification under DP, and α sensitivity) that degrade LoRA in privacy-preserving federated learning, and proposes FFA-LoRA, which freezes the randomly initialized A matrix and only trains the zero-initialized B matrix. The method reduces trainable parameters by half and is theoretically motivated as the α→∞ limit of LoRA. Experiments compare FFA-LoRA with vanilla LoRA on RoBERTa and LLaMA, primarily on GLUE tasks under varying privacy budgets and data heterogeneity levels.

## Strengths

1. **Clear identification of three specific discordances with mathematical formulation.** Section 3 formalizes the aggregation error (Equation 4 showing the mismatch between product-of-averages and average-of-products), provides a synthetic noise amplification illustration (Figure 1), and discusses α sensitivity. These analyses give a principled account of why LoRA may underperform in privacy-preserving FL, independent of the proposed fix.

2. **FFA-LoRA's aggregation error is analytically eliminated.** Equation (5) shows that with fixed A₀, the FedAvg aggregation of FFA-LoRA exactly matches the ideal model averaging (no cross-term mismatch). This is a direct theoretical advantage over LoRA that is clean and verifiable.

3. **Robustness to rank under strong privacy guarantees.** Table 5 (exp_rank_DP) shows that at ε=1 on QNLI, FFA-LoRA maintains accuracy between 81.87% and 83.01% across ranks 2–16, whereas LoRA degrades sharply from 80.54% (r=16) to 58.15% (r=2). This ablation supports the claim that FFA-LoRA is less susceptible to noise amplification and parameter budget sensitivity.

4. **Practical simplicity and communication savings.** The method halves the number of trainable parameters compared to LoRA and eliminates the need to tune α, which are concrete practical benefits.

## Weaknesses

### Fatal
None.

### Major

1. **Asymmetric learning rate search between methods is unexplained and potentially unfair.** The DP experiments (Table 1) report LoRA results using η ∈ {0.01, 0.02, 0.05, 0.1} while FFA-LoRA uses η ∈ {0.1, 0.2, 0.5, 1} — an order of magnitude difference with no overlap and no overlap in ranges. The paper states "We report the best result from a set of experiments" but provides no rationale for why the ranges differ. If LoRA could benefit from learning rates above 0.1 (a plausible scenario given that LoRA's A matrix gradients are initially small due to B₀=0), it was never given that chance. Since the paper's strongest evidence — the 39% vs. 78% gap on MNLI under DP — comes from this comparison, the fairness concern directly undermines the central empirical claim. *Why it matters:* The paper's primary evidence for the core contribution is suspect; readers cannot tell whether FFA-LoRA genuinely dominates or whether LoRA was undertuned.

2. **Missing α tuning for LoRA in all DP experiments despite identifying α sensitivity as a key discordance.** The paper argues that LoRA's sensitivity to α (Discordance 3) is a problem, yet all DP experiments fix α=8 for LoRA without searching over α (e.g., {2, 4, 8, 16}). The paper should compare the best-tuned version of each method. Since FFA-LoRA's claimed advantage includes eliminating α tuning, the paper needs to establish that even with a well-tuned α, LoRA underperforms FFA-LoRA. *Why it matters:* Without this control, the α sensitivity argument is used to motivate the method but is not tested as a baseline confound.

3. **The α-scaling experiment and the initialization experiment are absent from the main text.** The paper outlines ablation questions about α sensitivity and initialization (Section 5.2), and claims "It has been shown in proof of Thm. 1 that the scaling factor does not affect the overall performance of the algorithm" — but no empirical results, table, or figure for the α experiment appears in the extracted text. Similarly, the initialization subsection is a single sentence with no results. *Why it matters:* These are experiments the paper itself committed to running; their absence means the claimed insensitivity to α and initialization is not empirically demonstrated in the main text.

### Minor

1. **The LLaMA experiment is reported in two sentences without variance, experimental details, or privacy setting.** The paper reports 17.12% vs. 15.68% for GSM-8K but provides no information about the number of clients, data heterogeneity configuration, DP budget (if any), or run variance. Claiming "state-of-the-art" without these details is insufficient to support the generalization claim to LLMs.

2. **Theorem 1 (α→∞ limit) is stated without explicit assumptions about learning rate scaling.** The theorem states that as α_LoRA → ∞, the LoRA trajectory converges to the FFA-LoRA trajectory. The discussion later mentions "as α increases and η decreases" (line 252) and "as long as the learning rate is scaled accordingly" (line 259), but the theorem statement itself does not specify this dependency. A reader encountering the theorem in isolation could interpret it as claiming convergence for any fixed learning rate, which would be incorrect. The proof is in the appendix (stripped by parser), so the correctness cannot be evaluated from the main text alone, but the presentation is unclear.

3. **The vision experiment (Food-101) is mentioned in a single sentence with no quantitative results.** "In short, the algorithms performs similarly compared to the language classification tasks" conveys no evaluable information. This experiment should either be presented with numbers or removed.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment that directly measures the aggregation error term (‖½(∑B_k A_k) − (½∑B_k)(½∑A_k)‖) during training would directly validate Discordance 1 beyond the synthetic analysis.
- Reporting wall-clock time or FLOPs to substantiate the claimed communication/computation savings.
- Statistical significance tests (e.g., paired across runs) for the main DP comparisons.

## Removed Points

- *Criticism about the noise amplification example being "not justified" (Critic Point 4, and sections about Figure 1):* The paper clearly labels this as a synthetic verification (line 167: "We provide synthetic verification with Figure 1"), specifies the matrix dimensions (1024×1024, r=8), and derives the σ=0.99 value from standard DP accounting on SST-2. The analysis is not claiming to be an empirical measurement of actual training noise; it shows a mathematical property of the LoRA structure. Removed.
- *Criticism about FFA-LoRA still having linear noise from A₀ (Critic's Point 4 sub-point):* The paper explicitly states "making FFA-LoRA *less susceptible* to noise than LoRA" (emphasis added), not "immune to noise." The analysis correctly notes the absence of the quadratic ξ_Bξ_A term. The paper's claim is accurate as written. Removed.
- *Criticism about missing appendix/proof (Critic Point 2 sub-point):* Parser strips appendices; criticism about the proof being in the appendix is invalid per review policy. However, the substantive concern about missing assumptions in Theorem 1 is retained (see Weakness Minor #2).
- *"Halve the communication cost" as overstatement:* The claim is relative to LoRA, which is factually correct (half the trainable parameters). Removed.
- *Pure formatting/style nitpicks (grammar, typos, etc.):* These are parser artifacts, not author errors. Removed.

## Novel Insights

None beyond the paper's own contributions. Neither reviewer offered a novel synthesis that recontextualizes the paper in a surprising way. The crispest observation is the harsh critic's framing: the paper's strongest contribution may be the three discordances as diagnostic tools, with FFA-LoRA being a natural fix rather than a surprising technical innovation. This is a reasonable reading but is consistent with the paper's own framing.

## Suggestions

1. **Run a controlled hyperparameter search with overlapping LR ranges** for both LoRA and FFA-LoRA (e.g., {0.005, 0.01, 0.05, 0.1, 0.5, 1}) and also search α for LoRA. Report which hyperparameters were selected per task and per privacy level. This single change would address the most serious threat to the paper's validity.

2. **Either provide the missing α and initialization ablation experiments**, or clearly state why they are omitted (e.g., if they are deferred to an appendix, note that explicitly with a reference).

3. **Flesh out the LLaMA experiment** with number of clients, heterogeneity configuration, DP setting (if any), and variance across runs, or remove the "state-of-the-art" claim.

4. **Restate Theorem 1 with explicit assumptions** about the relative scaling of learning rate and α, and provide a proof sketch or clearer intuition in the main text.

## Score and Decision

The core idea — fixing A in LoRA for privacy-preserving FL — is clean, well-motivated by the three discordances, and practically appealing. The analytical advantage on aggregation error is rigorous, and the rank robustness results (Table 5) are convincing.

However, the paper's strongest empirical evidence (Table 1, DP results) is compromised by an unexplained asymmetric learning rate search that may disadvantage LoRA, and by the absence of α tuning for the LoRA baseline. These are not speculative concerns — the paper's own text shows non-overlapping LR ranges and fixed α=8 without justification. The LLaMA experiment is too sparse to support the claimed generalization. The missing α and initialization ablations further weaken the empirical case.

The paper has real merit and addresses an important problem, but in its current form the experimental evidence is not sufficient to establish that FFA-LoRA consistently outperforms a well-tuned LoRA baseline. I recommend major revision with a corrected experimental setup.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>