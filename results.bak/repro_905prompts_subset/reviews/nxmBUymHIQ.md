Now I have everything I need. Let me write the consolidated final review.

## Summary

This paper proposes LoLoRA, a method that replaces gradient-based training of the LoRA A matrix with local unsupervised updates (HPCA) during the forward pass, avoiding the need to store input activations for backpropagation through A. The paper provides a theoretical result (Theorem 4.4) proving that optimal A spans the top eigenvectors of the input covariance matrix, justifying both the EVA initialization and the HPCA-based online adaptation. Experiments span GLUE (RoBERTa-large), MetaMathQA (LLaMA-3.1-8B), LLaVA-v1.5-7B, and ablations on TinyLlama-1.1B.

## Strengths

1. **Rigorous theoretical characterization of optimal A (Theorem 4.4).** The paper proves that, under the random regression Assumptions 4.1–4.2, the set of optimal A matrices for frozen-A LoRA is exactly the set of nonsingular linear transformations of the top r eigenvectors of the input covariance. This provides a formal justification for the empirically motivated EVA initialization (Paischer et al., 2024) and is a genuine theoretical contribution to the LoRA literature.

2. **Systematic ablation of local update rules (Table 6).** The paper compares five local update rules (HPCA variants, autoencoder, SoftHebb) across ranks r∈{2,4,8} on TinyLlama-1.1B / Alpaca. This is a thorough empirical characterization. HPCA (uniform) and HPCA (svd first) consistently approach full LoRA perplexity (e.g., r=8: 2.535 vs 2.521), demonstrating that the proposed local updates are a viable alternative to gradient-based A training.

3. **Demonstrated memory savings vs. standard LoRA.** On LLaMA-3.1-8B (MetaMathQA), LoLoRA uses 26 GB extra memory vs. 30 GB for standard LoRA — a 13% reduction — while matching accuracy (82.9%). On GLUE, the paper reports up to 20% memory reduction. These savings come from not storing activations for backpropagation through A, a genuine advantage over standard LoRA.

4. **Convergence to PCA is proven for the autoencoder variant (Theorem 4.6).** The paper formally shows that minimizing the local symmetric autoencoder loss `𝔼_z ½‖z − AᵀAz‖²` converges to a matrix whose row space spans the dominant eigensubspace, providing additional theoretical grounding for the AE update rule.

## Weaknesses

### Major

1. **The conclusion's central performance claim is contradicted by the paper's own data.** The conclusion states: "Our experiments showed that HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." Verifying against the tables: (a) **GLUE (Setup 1):** LoLoRA HPCA numerically *underperforms* LoRA-FA (uniform) on 5 of 8 tasks (CoLA, RTE, MNLI, QQP, SST-2) and ties on STS-B — this is not "consistent outperformance." (b) **MetaMathQA (Setup 2):** LoLoRA HPCA (82.9%) and LoRA-FA (uniform) (82.6%) are within error bars — a tie. (c) **LLaVA (Setup 3):** LoLoRA HPCA (loss 1.075) is better than LoRA-FA (uniform) (loss 1.087) — this one holds. This means the claim is accurate for at most 1 of 3 setups, not 2. Moreover, LoLoRA HPCA never outperforms LoRA-FA (EVA) — the strongest frozen-A baseline — in any experiment. This disconnect between the headline claim and the evidence is the paper's most serious weakness.

2. **The method does not outperform the strongest baseline it is compared against.** Across all experiments, LoLoRA HPCA matches but does not beat LoRA-FA with EVA initialization. On MetaMathQA both achieve 82.9%. On LLaVA, LoLoRA (loss 1.075) is worse than LoRA-FA (EVA) (loss 1.070). On GLUE, LoLoRA is between LoRA-FA (uniform) and LoRA-FA (EVA) but always below standard LoRA. Since EVA initialization requires only a one-time PCA precomputation — not a separate training pass — the practical advantage of LoLoRA's online adaptation over the simpler static initialization is unclear. The paper acknowledges this indirectly (Section 5.4: "all local update rules that converge to the optimal PCA subspace... perform equally well. Similarly, LoRA-FA with EVA initialization achieves comparable performance") but the framing in the conclusion contradicts this nuance.

3. **Missing critical baseline comparisons in main experiments.** PiSSA (Meng et al., 2024) is a well-known data-driven initialization method for LoRA. It appears only in the TinyLlama ablation (Table 5) but is absent from the main GLUE, MetaMathQA, and LLaVA tables (Tables 1–4). Given that the paper's core claim is about improving over frozen/static initialization baselines, the omission of PiSSA from the primary comparisons weakens the evaluation. The ablation shows PiSSA performs comparably to random uniform initialization on TinyLlama, but this does not substitute for a full comparison.

### Minor

1. **The SNL update equation is not specified in the main paper.** Algorithm 1 uses `LocalRule(A, z, u)` as a placeholder and references Oja (1989) and Appendix B. The exact update (e.g., `A ← A + η(u zᵀ − A u uᵀ)` or similar) and its learning rate/optimizer details are not provided. While the algorithm is well-known in the Hebbian learning community, the paper would benefit from stating the update explicitly for reproducibility.

2. **Overlap in error bars suggests many differences are not statistically significant.** Across all tables, many comparisons between methods fall within one standard deviation. The paper does not report any significance tests (e.g., paired t-tests or confidence intervals for differences). This is not unusual for this setting, but given the marginal nature of the improvements claimed, the lack of statistical rigor is notable.

3. **The theory assumes stationary per-layer targets (Assumptions 4.1–4.2), which is violated in practice.** The paper acknowledges this limitation in the conclusion ("we considered each submodule isolated with stationary targets, which is not strictly the case"). However, no experiment measures whether the learned A actually aligns with the evolving input covariance during training, which would bridge the theory–experiment gap. The theoretical section motivates the EVA initialization but does not provide a compelling reason for preferring online HPCA updates over the static initialization, since the theory assumes stationarity.

### Trivial

None.

## Nice-to-Haves

- **Memory breakdown table:** The paper reports peak memory but does not break down the components (activations, optimizer states, weights). A per-component comparison would clarify exactly where LoLoRA saves memory compared to standard LoRA and where it adds overhead (optimizer state for A) compared to LoRA-FA.
- **Training wall-clock time for GLUE and MetaMathQA:** Table 4 reports run times for LLaVA, but the other experiments do not. Since the local update adds computational overhead per step, quantifying this for all settings would help practitioners assess the trade-off.
- **A scenario with distribution shift:** The paper's core motivation is that online adaptation of A matters when the input distribution shifts. The current experiments use static single-task fine-tuning. A continual learning or multi-task sequential fine-tuning experiment would directly test this hypothesis and strengthen the paper.

## Removed Points

- **"Memory advantage over LoRA-FA is marginal or negative, not novel"** (Harsh Critic #2): Removed. The paper claims memory reduction relative to *standard LoRA*, not LoRA-FA. The abstract says "further reducing the memory required for fine-tuning" in the context of comparing to standard LoRA, and the method summary explicitly says "Both LoRA-FA and LoLoRA show up to 20% less GPU memory requirements in comparison to standard LoRA" (line 317). The critic's framing misattributes the comparison target.
- **"The actual local update rule is never defined in the paper"** (Harsh Critic, Section-by-Section Notes): Demoted from "fatal" to minor. The SNL algorithm is a well-known published method (Oja, 1989). Algorithm 1 and the description in Section 3.3 make the high-level procedure clear. The exact update is referenced to the original work. This is a standard citation practice, not an omission.
- **"LoLoRA underperforms LoRA-FA (uniform) on most GLUE tasks"** claim merged into Major Weakness #1. The critic's framing was correct but the severity is organizational (overclaiming in conclusion) rather than that the method is useless.
- **"The theoretical analysis is disconnected from the experimental setup"** (Harsh Critic #3): Significantly weakened. Theorem 4.4 directly connects to EVA initialization and HPCA updates. The paper explicitly states "This is exactly the form of A that HPCA updates converge to" (line 228). The theory-experiment link exists; the limitation is acknowledged in the paper. What remains is the minor concern that no empirical validation of alignment is provided.
- **"Runtime overhead of local updates"** and **"Ablation on optimizer state for A"**: Moved to Nice-to-Haves. These are useful additional analyses but not core flaws.
- **Strength Finder claimed strengths about "Memory reduction without accuracy loss"**: The memory reduction is real, but the accuracy improvement claim is not supported (the method ties with baselines, doesn't improve). Kept as a qualified strength.
- **Strength Finder strength about "Identified asymmetry between A and B adapters"**: This is already known from Zhu et al. (2024) and the paper positions it as complementary. The theoretical grounding (Theorems 4.4 and 4.5) is genuinely new. Retained.

## Novel Insights

None beyond the paper's own contributions. The key insight — that Theorem 4.4 characterizes the optimal frozen-A initialization as spanning the top input eigenspace — is the paper's own contribution. The reviewers surface no additional synthesis beyond this.

## Suggestions

1. **Reframe the conclusion honestly.** The paper's actual contribution is: (a) a theoretical proof that optimal A spans the top input eigenspace, and (b) a method (LoLoRA) that achieves this via online local updates, matching LoRA-FA (EVA) performance while avoiding the separate PCA precomputation. The claim of "consistent outperformance" should be replaced with language about "competitive performance" or "matching the strongest frozen-A baseline without requiring a separate PCA pass."

2. **Add PiSSA to the main experimental tables.** Since PiSSA is a widely used data-driven initialization, its absence from Tables 1–4 weakens the comparison. Adding it would strengthen the paper even if performance is comparable.

3. **Provide empirical validation of the theory–experiment link.** Measure the alignment between the learned A's row space and the top r eigenvectors of the evolving input covariance during training (e.g., subspace distance or explained variance ratio). This would directly test whether HPCA updates are actually converging to the optimal subspace predicted by Theorem 4.4.

4. **Add a distribution-shift experiment.** The paper motivates online updates as adapting to "input distribution shifts." A simple experiment fine-tuning on sequentially presented tasks (e.g., first task A, then task B) would test whether the online A adaptation provides a measurable benefit over static EVA initialization in non-stationary settings.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Queried three bands. Weak band (score < 3.5) returned PEFT methods papers at avg 3.0–3.33. Middle band (3.5–7.5) returned EVA (4.75), dEBORA (6.67), a matrix factorization theory paper (5.50), and a LoRA expressiveness theory paper (6.50). Strong band (>7.5) returned accepted papers at 8.0–8.5. Based on the theoretical contribution but limited experimental support, the initial bracket was [4.0, 6.0].

**Round 2 (Narrowing):** Queried within [4.0, 6.0] for LoRA initialization theory papers and within [4.5, 7.5] for local/online PEFT papers. Retrieved EigenLoRA (5.00), The Quest for Winning Tickets (5.20), and a local loss optimization paper (7.00, accepted). After reading full reviews, the Quest for Winning Tickets (avg 5.20) is a reasonable comparison point — it has a theory component plus experiments with moderate support, similar to the current paper. The EVA paper (4.75) is the most directly comparable anchor since it addresses the same research question (improving LoRA initialization via PCA) and was rejected.

**Score relative to anchors:** This paper is meaningfully stronger than the EVA paper (4.75) due to its rigorous theoretical proof (Theorem 4.4) and more systematic ablation study. It is comparable to the Quest for Winning Tickets paper (5.20) — both have a theoretical component with moderate experimental support but overclaiming issues. However, the overclaiming in the conclusion of this paper is more severe than in either anchor. Setting the score at the boundary reflects the genuine theoretical contribution weighed against the unsupported headline claim.

**Final score:** 5.0 — a paper with a solid theoretical contribution that advances understanding of LoRA initialization, but whose central performance claim is not supported by the evidence, and whose practical advantage over simpler baselines (LoRA-FA with EVA) remains unestablished.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>