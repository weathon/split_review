Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper introduces FedAda², a class of jointly adaptive federated learning algorithms that avoid transmitting preconditioners between the server and clients (saving communication) while using memory-efficient local optimizers (SM3) to reduce on-device memory cost. The authors provide a theoretical convergence analysis (O(T^{-1/2}) for non-convex objectives) and empirical results on StackOverflow (with differential privacy), CIFAR-100, and GLD-23K, showing that FedAda² retains the accuracy benefits of joint adaptivity at a fraction of the communication cost.

## Strengths

- **Communication efficiency without sacrificing accuracy**: The paper demonstrates that removing preconditioner transmission and using zero-initialized client preconditioners achieves competitive or better accuracy than full preconditioner transmission. When evaluated on a communicated-bits basis (Figure 2), FedAda² and the communication-efficient baseline converge the fastest. This is the central practical contribution and is well-supported by the experimental design (a natural ablation chain: server-only → joint with transmission → joint w/o transmission → SM3-compressed).

- **Memory-efficient client-side adaptivity via SM3**: By instantiating client-side preconditioners with SM3, FedAda² maintains statistics at parameter-group granularity rather than per-coordinate, reducing on-device memory overhead. The paper explicitly notes that SM3 "exploits natural activation patterns…to efficiently synthesize a low-rank approximation of the preconditioner," and this compression is key to scalability on resource-constrained devices.

- **Theoretical convergence guarantee matching state-of-the-art**: Theorem 6 and Corollary 8 prove that FedAda² converges at rate O(T^{-1/2}) for general non-convex objectives, matching the best known rates for federated non-convex optimization. The paper claims (line 70) that no prior work provides convergence results for jointly adaptive optimization that explicitly support methods like Adam and AdaGrad, which would be a useful theoretical contribution if substantiated.

- **Empirical validation across diverse domains and tasks**: FedAda² is tested on text classification (StackOverflow with DP), image classification (CIFAR-100), and fine-grained visual recognition (GLD-23K with ViT finetuning). Across all three, jointly adaptive methods outperform FedAvg and server-only adaptive baselines.

- **Robustness to asymmetric server-client optimizer configurations**: Section 6.2 (Figure 7) investigates asymmetric setups (e.g., Adam on server, AdaGrad on client) and reports stable performance, highlighting the flexibility of the framework.

- **Interesting empirical insight about SM3 stabilization**: The paper observes that removing preconditioner transmission destabilizes worst-case runs, but SM3 compression "restabilizes the losses" — the authors hypothesize a denoising effect of the low-rank projection. This is an actionable, non-obvious finding.

## Weaknesses

### Fatal
None.

### Major

- **The convergence analysis is presented in a form too minimal to verify**: Theorem 6 is given only as asymptotic orders (Ψ₁–Ψ₆ with Θ/Ω/O notation) with undefined constants, piecewise conditions that are not fully explained, and the full proof deferred to the (stripped) appendix. The notation is dense and confusing in places (e.g., the relationship between η and ηℓ, the conditions on the piecewise cases in Ψ₅ and Ψ₆). The strong claim (line 70) that "there are no known convergence results of jointly adaptive federated optimization that explicitly support several popular methods including Adam and AdaGrad" is a significant literature claim that the available text does not substantiate. While the asymptotic rate O(T^{-1/2}) matches best-known results, it is also the same rate as standard SGD for non-convex optimization, and it is unclear whether joint adaptivity provides any advantage in the convergence rate itself or only in the constants / practical behavior.

- **Gap between theoretical assumptions and experimental setup**: The theory assumes full-batch client gradients (line 19), which is a strong assumption not used in the experiments (which use mini-batches). The paper acknowledges this as "a limitation of our theory" (line 72) but does not discuss how or whether the theory extends to the mini-batch stochastic setting that is actually evaluated. This limits the connection between the theoretical claims and the empirical validation.

### Minor

- **The formal algorithm pseudocode is not visible in the extracted text**: Section 3 or 4 (likely "Algorithm 1" referenced on line 99, and "Algorithm 5" on line 31) appears to have been garbled during parsing, leaving only the fragment `\section{13: end for }`. While the algorithm is well-described conceptually throughout (avoid preconditioner transmission, zero-initialize client preconditioners, use SM3 for memory efficiency), the absence of the explicit update rules and communication protocol in the available text makes it harder to precisely understand the mechanism. This appears to be a parser artifact rather than an author omission.

- **The "blended optimization" discussion (Section 5.1) feels tangential**: Paragraphs at lines 73–75 introduce a general framework for distributing local optimizer strategies, but this discussion is not clearly connected to the FedAda² algorithm or the paper's experiments. It reads as a forward-looking remark rather than a contribution of the current work.

- **Limited discussion of limitations**: The paper acknowledges only the full-batch assumption as a limitation. Other natural limitations — such as the impact of SM3's low-rank approximation error on convergence, sensitivity to extreme heterogeneity beyond bounded-gradient assumptions, or scenarios where FedAda² might underperform — are not discussed.

### Trivial
None.

## Nice-to-Haves

- A table quantifying memory per client (in MB) and total communication per round (in bits) for each method would make the efficiency claims more concrete. Currently, savings are described qualitatively (e.g., "reduces overhead significantly").
- Explicit reporting of key hyperparameters (number of clients per round, batch sizes, learning rate schedules) would improve reproducibility, though these details may reside in the stripped appendix.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Missing algorithm — the contribution is undefined"** (Harsh Critic's #1): Removed as factually overstated. The algorithm IS described in text: avoid preconditioner transmission, zero-initialize client preconditioners, use SM3 for memory efficiency. The formal pseudocode was likely stripped by the parser (the original paper references Algorithm 1 and Algorithm 5). The algorithm is sufficiently described to understand the contribution; the critic's framing of this as a fatal structural flaw is incorrect.

- **"Figures not included in extracted text — empirical claims unverifiable"** (Harsh Critic's #3, part): Removed as a parser artifact. Figures 1, 2, 3, and 7 are all referenced with image links in the extracted text; they exist in the original PDF submission.

- **"Missing hyperparameter details"** (Harsh Critic's #3, part): Removed per the rule about reproducibility nitpicks and potential appendix content. The paper reports 20 random seeds, 95% CIs, dataset and model specifications. Fine-grained hyperparameter details (learning rate schedules, client counts, batch sizes) are standard content for the appendix, which is stripped.

- **"Convergence bound uses same rate as SGD — no advantage"**: Removed as a strawman. The contribution is achieving the same rate *without* preconditioner transmission, which is the efficiency advantage. The rate matching SOTA is not a flaw.

- **"Proof is in the appendix / unreviewable"**: Removed per the rule about missing appendix content being a parser artifact. The full proof exists in the original submission.

- **"Reader cannot determine what FedAda² does"**: Removed. The paper clearly states: (1) avoid transmitting server preconditioners to clients, (2) zero-initialize client preconditioners, (3) use SM3 for memory-efficient local adaptivity. This is described in lines 4, 10–12, and 85.

- **Strengths from Strength Finder removed**: None removed — all six strengths are grounded in specific paper content and do not conflict with verified weaknesses.

## Novel Insights

The harsh critic's review performs a valuable service by identifying that the main-text theory sketch is too minimal for independent verification and that the full-batch theoretical assumption creates a gap with the practical experiments. However, the critic overstates the "missing algorithm" claim to a fatal degree — the algorithm is clearly described in text even if the formal pseudocode was garbled by the parser. The strength finder's observation about the SM3 stabilization effect (the "denoising" hypothesis) is a genuinely interesting insight that goes beyond what the paper itself emphasizes: the counterintuitive result that compressing preconditioners (which introduces approximation error) actually *restabilizes* training compared to the uncompressed communication-efficient baseline. This is a non-obvious phenomenon worth highlighting.

## Suggestions

1. **Present the algorithm pseudocode explicitly** in the main text (not just the appendix) so that the update rules, communication protocol, and the gradient-clipping step used in the analysis are transparent at a glance.
2. **Provide an interpretable bound** rather than asymptotic orders alone — even a simplified explicit bound showing how the local and global learning rates interact would make the theoretical contribution more accessible.
3. **Discuss how the full-batch theoretical assumption relates to the mini-batch experiments**, or extend the analysis to the stochastic setting, to close the gap between theory and practice.
4. **Acknowledge limitations** more thoroughly: when might FedAda² underperform? How does SM3 approximation error affect convergence? What about extreme data heterogeneity?

## Score and Decision

This paper addresses a well-motivated practical problem (communication and memory overhead in jointly adaptive federated learning) with a clean algorithmic idea, a theoretical convergence guarantee, and empirical validation across three datasets. The main weaknesses are that the theory is presented in a form too minimal to verify from the main text alone, and the full-batch assumption creates a gap with the stochastic experiments. Neither weakness is fatal — the algorithm is clearly described, the empirical results are present (parser artifacts notwithstanding), and the core contribution is sound. The paper would benefit from a more detailed theory presentation and a limitations discussion, but the current submission communicates the key ideas effectively.

**Score**: 6.5

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>