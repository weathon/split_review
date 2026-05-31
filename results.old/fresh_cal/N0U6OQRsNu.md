Now I have all the information needed. Let me compile the final consolidated review.

---

## Summary

This paper proposes ATTENDING, a federated learning framework that combines spatial-channel attention with personalized model pruning to address system and data heterogeneity. The key idea is to use an attention module to compute per-channel importance scores, prune each client's model according to its capability level, then aggregate pruned models on the server by reordering channels by attention scores before weighted averaging—enabling aggregation without transmitting binary mask matrices. Evaluations on MNIST, CIFAR10, and CIFAR100 report accuracy improvements up to 11.3% over baselines with a 32% average reduction in model footprint.

## Strengths

- **Attention-guided pruning eliminates the need for binary mask transmission during aggregation (Section 3.3, Eq. 8):** Prior pruning-based FL methods require clients to send binary mask matrices along with model weights. ATTENDING's attention-matching mechanism reorders channels by their attention scores before averaging, and reconstructs the full model structure from the original global model—avoiding per-client mask transmission. This design choice addresses a real limitation in prior work.

- **Accuracy improvements on non-IID data are substantial (Section 4.2, Fig. 4):** The paper reports that ATTENDING achieves up to 11.3% higher average accuracy on non-IID partitioned datasets compared to baselines. The ablation (Fig. 4) confirms that the full attention mechanism (pruning + matching) contributes 8–14.59% accuracy gains over an L1-norm/no-matching variant on CIFAR10/100 in IID settings, and larger gains in non-IID settings.

- **Lightweight attention module (Section 3.1):** The attention module adds only 0.2% additional trainable parameters for the 2NN model and is removed after pruning, so it incurs no inference cost. This pragmatic design choice is important for resource-constrained clients.

- **Scalability demonstrated with 1,000 clients (Section 4.5, Fig. 6):** The method maintains consistent accuracy in a large-scale FL environment (1,000 total clients) across IID and non-IID settings, confirming the approach is not limited to small client pools.

## Weaknesses

### Fatal
None.

### Major

- **The attention matching mechanism's core alignment assumption is not validated (Section 3.3).** The mechanism sorts channels within each layer by their attention scores before weighted averaging, under the assumption that this ordering aligns semantically corresponding channels across clients. However, attention scores are computed on each client's local (potentially non-IID) data. A channel receiving high attention for "deer antlers" on one client and "automobile wheels" on another could both rank highly, yet sorting by score alone does not guarantee semantic alignment. No theoretical reasoning or empirical evidence (e.g., measuring channel correspondence across clients, comparing sorted vs. random reordering) is provided. Without this validation, the mechanism's ability to mitigate permutation invariance remains an unsubstantiated claim (stated at line 147). This is the paper's central claimed innovation, and the evidence for it is incomplete.

- **The ablation study conflates multiple components and does not isolate the attention matching mechanism (Section 4.3, Fig. 4).** The ablation compares "ATTENDING w/ ATT" (full method) against "ATTENDING w/o ATT" (L1-norm pruning + no attention matching + no attention module). This simultaneously changes three variables: (a) attention-guided pruning vs. L1-norm pruning, (b) attention matching vs. no matching, and (c) presence vs. absence of the attention module for feature extraction. The observed gains cannot be attributed to any specific component. To isolate the matching mechanism, the paper should compare (i) full ATTENDING, (ii) ATTENDING with attention pruning but random/no channel reordering, and (iii) ATTENDING with attention pruning but reordering by a different criterion. The current ablation does not rule out the possibility that all gains come from better pruning targets or the feature extraction benefit of the attention module during training.

- **No variance or statistical significance reporting (Section 4.1).** The paper states experiments were run three times with different seeds and means were reported, but no standard deviations, confidence intervals, or significance tests are provided. Given that FL methods (FedAvg, FedProx, etc.) can vary substantially across runs, the claimed improvements (e.g., 11.3%) could be within noise. This omission weakens all comparative claims.

### Minor

- **Baseline configuration details are underspecified (Section 4.1).** The paper lists eight comparison methods but does not describe how they were configured for heterogeneous pruning scenarios—e.g., how FedDrop (a client dropout method) was adapted to the structured pruning setting, whether baselines used the same per-level pruning ratios, and whether they were given equivalent architectural flexibility. Without this information, the fairness and interpretability of comparisons are limited.

- **The 32% footprint reduction is a direct arithmetic consequence of the chosen pruning ratios, not a method-inherent result (Section 4.2, Table 4).** The pruning ratios are set to 0.7, 0.5, 0.3, 0.1, 0 for five uniformly partitioned client levels, yielding an average of exactly 32%. Any method using these ratios would achieve the same reduction rate. While the paper does demonstrate that the method can function at these ratios with good accuracy, presenting the 32% figure as an achievement of the method (abstract line 4, conclusion line 294) is misleading.

- **Scalability evaluation is limited (Section 4.5).** The large-scale experiment uses only MNIST, does not report error bars, and baselines are evaluated only at limited sample rates. This is insufficient to convincingly demonstrate scalability to large-scale, non-IID, complex-dataset scenarios.

- **Attention module grouping factor \(g\) is never specified (Section 3.1).** The spatial attention divides channels into \(g\) groups to reduce complexity, but the value of \(g\) used in experiments is not reported. This affects reproducibility.

### Trivial

- The Grad-CAM visualizations (Fig. 1) are qualitative; while helpful for intuition, they do not constitute a controlled evaluation of the method.

## Nice-to-Haves

- Communication cost analysis: The paper reports parameter/FLOP reduction but does not quantify communication savings from transmitting only pruned models. Since reduced communication is a practical benefit of pruning-based FL, quantifying this would strengthen the paper.
- Sensitivity analysis of the client distribution across pruning levels: The 32% reduction depends on the assumption of equal-sized client groups; evaluating different distributions would clarify robustness.
- A direct comparison with FedMA's matching approach (already cited in the paper) on the alignment problem would help position the contribution relative to existing permutation-invariance solutions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that aggregation "without binary mask matrices" is misleading because reconstruction reintroduces zeros:** REMOVED. This misinterprets the paper's claim. The paper claims the method aggregates "without the assistance of binary mask matrices" (line 19)—i.e., without transmitting per-client masks—which is true. The reconstruction step uses the original global model structure, not per-client masks. The claim does not assert that pruned weights cease to exist anywhere.

- **Criticism that FedMA is not cited or discussed:** REMOVED (factually wrong). The paper explicitly discusses FedMA at line 27: "Wang et al. (Wang et al., 2020a) demonstrate that the element-wise averaging of weights in FedAvg is a shortcoming due to the permutation invariance... and proposes the FedMA to alleviate the detrimental effects."

- **Criticism about equation notation inconsistency (semicolon vs. comma):** REMOVED (parser artifact per rules).

- **Missing related works mentions:** REMOVED per rules (do not mention missing related works without external confirmation).

- **Criticism that the attention module removal after pruning should be acknowledged:** REMOVED (the paper does acknowledge it at line 127: "the attention modules are removed to avoid unnecessary communication costs and reduce the resource consumption").

## Novel Insights

None beyond the paper's own contributions. The reviews affirm the core technical proposal (attention-guided heterogeneous pruning with reordering-based aggregation) but surface a gap between the paper's claimed innovation and its empirical validation: the most novel component—the attention matching mechanism for aligning channels across clients—is precisely the component that receives the weakest empirical support. The ablation conflates it with the attention module's more straightforward contributions (feature extraction, pruning guidance), and no direct evidence is offered that sorting by attention score produces semantically meaningful alignment. This pattern—an interesting but under-validated matching mechanism surrounded by better-supported but less novel components (pruning at specified ratios, attention for feature extraction)—is the paper's key unresolved tension.

## Suggestions

1. **Validate the attention matching mechanism directly.** Add an ablation that isolates channel reordering: compare (a) full ATTENDING vs. (b) attention-based pruning *without* reordering (weights averaged in original client order) vs. (c) attention-based pruning with random reordering. If (a) ≈ (b), the matching does nothing; if (a) ≫ (b), it matters. Also measure channel correspondence—e.g., compute cosine similarity between sorted channels across clients—to test whether sorting by attention score improves alignment.

2. **Report standard deviations** (or confidence intervals) for all main accuracy results. Three runs with different seeds is sufficient; the resulting variance should be shown.

3. **Clarify baseline configurations.** Describe how each comparison method was adapted to the heterogeneous pruning setup. If FedDrop was used as a client dropout method rather than a pruning method, explain the adaptation.

4. **Reframe the 32% average reduction.** Acknowledge explicitly that this is the average of the chosen pruning ratios—present it as the *operating point* of the method, not a discovery. The actual contribution regarding footprint is that the method achieves good accuracy *at these aggressive pruning levels*.

5. **Report the missing experimental details:** the number of groups \(g\) in spatial attention, which layers are pruned (all convolutional layers? only certain ones?), and hyperparameters for attention training.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>