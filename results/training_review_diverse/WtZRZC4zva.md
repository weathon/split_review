Now I have all the information I need. Let me produce the consolidated review.

---

## Summary

This paper tackles the problem of privacy-preserving relational learning for fine-tuning LLMs on graph data. The core contribution is a **decoupled negative sampling strategy** that ensures each relation affects at most one loss tuple, thereby making DP-SGD applicable to relational learning where standard coupled negative sampling would cause unbounded sensitivity. An efficient per-tuple gradient computation is also introduced to reduce the memory footprint from O(KMpd) to O(KM(p+d)+pd), enabling fine-tuning of models up to Llama2-7B. The method is evaluated on four text-attributed graph domains (AMAZ, MAG) for zero-shot and few-shot relation prediction and entity classification under ε ∈ {4, 10}.

## Strengths

1. **A principled solution to a well-motivated problem.** The paper correctly identifies that standard DP-SGD fails in relational learning because coupled negative sampling causes a single relation perturbation to affect multiple loss terms in a batch. The decoupled sampling strategy — uniformly sampling negative entities from V rather than from the complement set or using in-batch positives — cleanly bounds sensitivity to one tuple per relation (Sec. 3.2). This is a conceptually simple but effective insight that opens up a new problem setting.

2. **Memory-efficient gradient computation addresses a real scalability bottleneck for LLMs.** Standard DP libraries hook gradients per token per entity, requiring O(KM) gradient copies per loss term for K entities with M tokens each. The paper derives an alternative that records stacked output r and stacked input a and computes r a^T directly, reducing memory from O(KMpd) to O(KM(p+d)+pd) (Sec. 3.3). This makes the approach feasible for 7B-parameter models, which would otherwise exhaust GPU memory.

3. **Broad and realistic evaluation across multiple domains, model sizes, and privacy levels.** Experiments span four text-attributed graphs (AMAZ-Cloth, AMAZ-Sports, MAG-USA, MAG-CHN), three model families (BERT-base, BERT-large, Llama2-7B), and two privacy levels (ε=4, ε=10). The cross-domain transfer setup (train on one domain, test on another) realistically simulates cold-start recommendation and cross-regional deployment. At ε=4, the method substantially outperforms base models (e.g., BERT.base on MAG-USA: 4.41% → 22.08% PREC@1 in zero-shot relation prediction) and the randomized-response baseline, while staying within a few points of the non-private upper bound.

4. **Systematic study of hyperparameter trade-offs provides actionable guidance.** Figure 3 shows the effects of negative sample size k, batch size b, clipping threshold C, and noise multiplier σ. The results — larger batches improve signal-to-noise ratio, small C works best, and k saturates around 4–8 — align with principles from non-relational private learning and provide practical guidance for deploying the method.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical variance or error bars are reported for any experimental result.** All tables (1–3) and figures present single numbers with no standard deviations, confidence intervals, or multiple seeds. Since DP training injects calibrated Gaussian noise, outcomes are inherently stochastic. Without variance estimates, the reader cannot assess whether differences between methods (e.g., ε=4 vs. ε=10) or across domains are reliable. While the performance gains are large and likely real, the lack of any variance quantification significantly weakens the empirical evidence. This is the most consequential gap in the evaluation.

2. **Hyperparameter tuning procedures are underspecified and may leak privacy.** The paper states: "We tune hyperparameters based on the InfoNCE loss under given privacy parameters" (Sec. 4.1). It does not clarify whether this tuning uses the private training data, what search space was explored, or whether the privacy cost of tuning was accounted for in the reported ε. If the same data used for fine-tuning was also used to select C, learning rate, or k, the reported ε values may be underestimates. This is a methodological gap that must be addressed for the privacy guarantees to be credible.

### Minor

3. **The efficient gradient computation is not validated with empirical memory or runtime benchmarks.** Section 3.3 provides a theoretical complexity reduction from O(KMpd) to O(KM(p+d)+pd), and the method clearly works in practice (the Llama2-7B experiments would otherwise be infeasible). However, no experiment reports GPU memory consumption, wall-clock time, or scalability with respect to K, M, or model size. Explicit memory profiling (e.g., peak memory with and without the efficient computation) would directly verify a central claim of the paper.

4. **The randomized response baseline is acknowledged as computationally unrealistic.** The paper notes that RR requires Θ(N²) operations per entity (Sec. 4.1) and only provides results for ε=10. While this is an understandable limitation for a first-of-its-kind method, the paper would be strengthened by an ablation comparing decoupled (proposed) vs. coupled (standard) negative sampling with a heuristic sensitivity bound, even if loose. Such an ablation would directly demonstrate the necessity of the decoupling design, which is the paper's main conceptual contribution.

5. **Privacy accounting details are partially underspecified in the main text.** The subsampling procedure (Poisson vs. without replacement) is not explicitly stated — Algorithm 1 says "Randomly sample B_t from E with sampling ratio b/|E|," which is imprecise. The PRV accounting method is referenced but not justified for the specific subsampling scheme used. These clarifications are needed for reproducibility.

### Trivial
None.

## Nice-to-Haves

- A formal proposition with a proof sketch that per-tuple gradient clipping bounds sensitivity to C under decoupled sampling would add rigor (the current argument is clear but informal).
- Reporting training time per step or total wall-clock time would strengthen the computational practicality claim.
- An analysis of the privacy-utility gap between private (ε=4,10) and non-private (ε=∞) models, discussing practical deployment acceptability of the observed gap.
- For entity classification on imbalanced datasets (e.g., AMAZ-Cloth: 9 classes, 960K entities), per-class F1 would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper would benefit from a concrete example of the sensitivity explosion"** — The paper already provides detailed worked examples for both random negative sampling and in-batch negative sampling in Sec. 3.1 (lines 73–75), complete with worst-case analysis of how many tuples could be affected. This criticism reflects a misreading.
- **"Number of training steps T and noise multiplier σ are not reported"** — The paper explicitly states these are reported in Table tab:privacy_loss in Appx. appx:edp_exp (line 197). The appendix is stripped by the parser; these details exist in the original submission.
- **"Reproducibility details missing (training steps, lr schedule, optimizer settings)"** — The paper states "Other details are left in Appx. appx:exp" (line 155). These are standard experimental details that belong in the appendix and are present in the original submission.
- **"The gap between private and non-private is large — paper should discuss acceptability"** — This criticism misunderstands the nature of DP papers, where a utility gap is expected and honestly presented. The paper acknowledges this gap (line 199: "only a modest performance drop") and shows it is far smaller than the RR baseline gap.
- **"The paper does not provide a formal proof that per-tuple gradient clipping bounds sensitivity"** — The paper provides clear, sufficient reasoning: decoupled sampling ensures each relation affects at most one tuple, and clipping each tuple's gradient to C bounds the sensitivity to C. This is the standard DP-SGD argument applied to the relational setting and is rigorous enough for this venue.
- **"Entity classification interpretation should be more cautious"** — The paper's interpretation is measured and accurate: it reports that relational fine-tuning improves entity embeddings over base models, except for one domain where it notes a potential misalignment between objectives, citing prior work (line 249). This is appropriate.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation that the paper itself does not already articulate. The key insight — decoupled negative sampling to enable DP-SGD for relational learning — is the paper's own innovation.

## Suggestions

1. **Run all key experiments with 3–5 different random seeds and report means ± std.** This is the single most impactful addition the authors could make and directly addresses the most serious weakness. Given the computational cost of 7B models, even 2–3 seeds for a representative subset (e.g., BERT.base on all datasets, Llama2-7B on one dataset) would be valuable.

2. **Clarify the hyperparameter tuning procedure:** explicitly state whether tuning was performed on public data, a held-out validation set, or the training data itself. If the latter, explain how the privacy cost of tuning was accounted for.

3. **Report GPU memory consumption** for at least one configuration (e.g., Llama2-7B with and without the efficient gradient computation, at varying k and batch size) to empirically validate the claimed memory savings.

4. **Add an ablation that compares decoupled vs. coupled negative sampling** under a heuristic sensitivity bound. Even if the coupled approach yields loose privacy guarantees or worse utility, demonstrating this directly would strengthen the paper's core argument.

## Score and Decision

The paper addresses a genuinely underexplored problem with a clever, technically sound solution. The decoupled negative sampling insight is elegant and clearly explained. The evaluation is broad in scope (4 datasets, 3 model families, 2 privacy levels) and shows consistently strong results. The efficient gradient computation, while not empirically benchmarked, is theoretically well-motivated and practically validated by the feasibility of the 7B experiments.

The two major weaknesses — (1) no variance reporting and (2) underspecified hyperparameter tuning with potential privacy leakage — are significant. However, neither undermines the paper's core conceptual contribution, and both are addressable in a revision. The lack of error bars weakens confidence in the numbers but does not invalidate the large, consistent improvements observed across all settings.

This is a solid contribution that advances the state of the art in an important emerging area. With the suggested additions (multiple seeds, tuning clarification, memory benchmarks), the paper would be clearly above the acceptance threshold. I recommend acceptance with the expectation that these gaps are addressed in the camera-ready version.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>