Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes DOTP (Data Poisoning with Optimized Trigger), a backdoor attack on Federated Learning that dynamically optimizes a backdoor trigger's pixel placement and values each round to minimize divergence between malicious and benign model updates. Using only data poisoning (no model poisoning), the attack achieves high success rates (typically >90% Final ASR) against ten state-of-the-art defenses based on analyzing client model updates, with only 5% malicious clients, while maintaining main-task accuracy. The key empirical contribution is demonstrating that a data-only attack can systematically evade server-side defenses by aligning backdoor and benign objectives through trigger optimization.

## Strengths

- **Comprehensive and convincing empirical evaluation**: Across four datasets (FashionMNIST, FEMNIST, CIFAR10, Tiny ImageNet) and ten server-side defenses (Median, Trimmed Mean, RobustLR, RFA, FLAIR, FLCert, FLAME, FoolsGold, Multi-Krum, FedAvg), the proposed attack achieves Final ASR exceeding 50% in all cases and >90% in most, substantially outperforming fixed-trigger (FT) and distributed-fixed-trigger (DFT) baselines (Figure 3). This breadth directly supports the central claim.

- **Two-factor analysis isolates the concealment mechanism**: Table 3 cleanly separates the contribution of "Trigger Optimization" ($\widetilde{ASR}$, no malicious updates) from "Trigger Optimization + Concealment" ($\ddot{ASR}$, with malicious updates). The large gap between them (e.g., FedAvg+CIFAR10: $\widetilde{ASR}=55.6 \rightarrow \ddot{ASR}=100$) provides direct evidence that update concealment — not just trigger optimization — drives the attack's success.

- **Effectiveness at very low malicious client ratio (MCR=5%)**: The attack succeeds with only 2 out of 50 clients being malicious, which is lower than the 10%+ typically required by prior data-poisoning attacks (Table 4). This is practically significant because a stealthy attack needs few adversaries.

- **Novel free-shape, free-placement L0-norm trigger optimization**: Algorithms 1–2 optimize both the placement and values of trigger pixels without pre-specifying shape or location, under an explicit size constraint. This is a genuine technical advance over prior work that fixes trigger shape and placement.

- **Stealthiness is maintained**: The main-task accuracy of the global model stays within ±2 percentage points of the attack-free baseline across all experiments, confirming that the attack does not degrade benign performance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Theoretical framing overstates what is proved**: Section 5 develops Propositions 1–3 for a linear regression model, which the text itself introduces as "to explain the intuition" (line 570). However, the abstract, introduction, and Section 5 claim these as "theoretical justifications" (lines 18, 102, 137, 664) without adequately qualifying that the proofs are confined to the linear setting and do not transfer to the deep neural networks used in experiments. The empirical evidence is strong enough to stand on its own, but the framing creates a gap between what is claimed and what is delivered. This is a presentation issue, not a fatal flaw — the paper would be stronger if it explicitly described the linear analysis as intuitive motivation and relied on the two-factor experiment (Table 3) as the primary explanation.

- **No sensitivity analysis for the trigger training dataset size $D$**: The attack requires malicious clients to assemble a "trigger training dataset" from their local benign data. The paper does not study how large $D$ must be for the gradient-based placement selection to generalize reliably. If a client has very limited local data (common in FL), the trigger learned from a few dozen images may not transfer. Without this analysis, the attack's practicality in low-data regimes is unclear.

- **A3FL comparison uses a single poison rate (0.5) where A3FL's default is 0.25**: The paper evaluates A3FL within "our FL configurations and attack settings" (line 1176), which uses a 0.5 poison rate versus A3FL's default 0.25. While using the same settings across all compared methods is standard practice and a higher poison rate generally helps attacks (not hurts them), testing A3FL at its own default rate would strengthen the claim that the proposed method's advantage is structural rather than setting-dependent.

### Trivial
None.

## Nice-to-Haves

- A direct measurement of cosine similarity between malicious and benign model updates for DOTP vs. baseline attacks under various defenses would provide a clean diagnostic of why the attack evades detection, complementing the ASR-based evidence.
- A brief table of wall-clock time per round for the trigger optimization step across datasets would help practitioners assess the attack's computational burden.
- An ablation comparing the gradient-based placement selection (Algorithm 1) to random placement of the same number of pixels would confirm the value of the placement optimization.
- An evaluation against differential privacy (e.g., Gaussian noise with clipping) — while outside the paper's stated scope of defenses based on analyzing model updates — would be a natural stress test for a claim about "state-of-the-art defenses" in real-world FL.

## Removed Points

- **"The trigger placement algorithm is a heuristic"**: The reviewer calls Algorithm 1 a "greedy solution to a non-convex selection problem." This is correct but not a weakness — the paper does not claim optimality. Gradient-based saliency is a standard, well-motivated approach. The ablative comparison against random placement belongs in Nice-to-Haves, not Weaknesses.

- **"No evaluation against DP-based defenses"**: The paper explicitly scopes its defense evaluation to "defenses that adhere to the fundamental privacy-preserving principles of FL" and those "based on analyzing clients' model updates." Criticizing the absence of DP — which is a fundamentally different defense category — amounts to scope creep. The paper's claims about evading update-analysis defenses are fully supported without DP evaluation.

- **"Weakness of A3FL comparison — different poison rates"**: The critic claims the comparison "conflates two different attack paradigms" and that the conclusion is not generalizable. However, (1) the same 0.5 poison rate is applied to all attacks — this is standard experimental fairness; (2) a higher poison rate (more poisoned data) should benefit A3FL, not hurt it; (3) the paper's conclusion specifically addresses A3FL's *unlearning-based* optimization approach failing to align with the benign objective, not dynamic objectives in general. The suggestion to also test at A3FL's default rate is a reasonable nice-to-have, not a weakness of the existing comparison.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Reframe the theoretical analysis (Section 5) explicitly as "intuitive motivation using a linear model" rather than "theoretical justification," and rely on the two-factor experiment (Table 3) as the primary evidence for the concealment mechanism.
- Add an experiment varying the size of the trigger training dataset $D$ (e.g., 1, 10, 50, 100, all available samples) to establish the attack's data requirements and clarify its practicality for low-resource clients.
- When comparing with A3FL, include an additional column testing A3FL at its native 0.25 poison rate alongside the 0.5 rate to eliminate any concern about setting mismatch.

## Score and Decision

The paper makes a clear empirical contribution: a data-only backdoor attack that systematically evades a broad suite of server-side defenses by optimizing triggers to align malicious updates with benign ones. The evaluation is thorough and the results are convincing. The main weaknesses — overclaimed theory framing, missing sensitivity on $D$, and a minor A3FL comparison issue — are all addressable in revision and do not undermine the paper's core empirical contributions. The paper should be accepted.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>