Now I have all the information needed to synthesize the final review. Let me carefully construct it.

---

## Summary

This paper proposes a mathematical formalization of experimental studies in ML, defines a quantifiable notion of generalizability (the probability that two independent empirical studies yield similar results), and develops an algorithm to estimate the minimum number of experiments needed to achieve a desired level of generalizability. The framework uses rankings as experimental results, kernels (Borda, Jaccard, Mallows) to encode study goals, and Maximum Mean Discrepancy (MMD) to measure distances between distributions of rankings. The method is demonstrated on two recent experimental studies (categorical encoders and LLM benchmarks).

## Strengths

- **First formalization of experimental studies for generalizability in ML.** The paper provides mathematically precise definitions of experiments, experimental conditions, factor types (design, held-constant, allowed-to-vary), ideal vs. empirical studies, and research questions (Section 3). This fills a genuine gap — existing frameworks from causal inference are inadequate for ML studies where there is no treatment/response variable.

- **Quantifiable definition of generalizability grounded in MMD.** Definition 4.1 formalizes generalizability as the probability that two empirical studies yield results within distance ε, using MMD with goal-specific kernels. The MMD choice is justified by its ability to handle sparse distributions and its theoretical guarantees.

- **Algorithm for estimating required study size.** Algorithm 1 (Section 4.3) provides a practical method to estimate n* using preliminary experiments, a log-log linear model fit, and extrapolation — directly addressing the practical question "How many experiments ensure generalizability?"

- **Demonstration on two real experimental studies with actionable insights.** The case studies (Section 5) show concrete results: e.g., for categorical encoders with goal g₂ (finding the best encoder), design factors (decision tree, full tuning, accuracy) need n*=28 experiments for (0.95,0.05)-generalizability, while (SVM, full tuning, balanced accuracy) needs n*=34 — and since both used 30 experiments, the framework identifies which configuration is and is not generalizable. This is a concrete, non-trivial finding.

- **Kernel toolbox tailored to study goals.** The three kernels (Borda for a specific alternative, Jaccard for top-k sets, Mallows for full ranking order) are clearly linked to distinct research goals, with principled bandwidth recommendations.

- **Clear distinction between generalizability and significance.** Section 1 explicitly separates these two independent aspects, with an example illustrating that significant findings may not generalize and vice versa.

- **Analysis of how many preliminary experiments are sufficient** (Section 5.3). The results show that the required N depends on the kernel (e.g., Mallows converges faster than Borda), providing practical guidance.

- **Open-source implementation** (GENEXPY module).

## Weaknesses

### Fatal
None.

### Major
None that survive filtering. (See Minor and Removed Points for justification.)

### Minor

- **The log-log linear model's validity conditions are not stated in the main text.** Proposition 4.2 asserts a linear relationship between log(n) and log(εₙ^{α*}) with an approximate fit ("≈"), and references an appendix for a proof in a simplified case. While the proof exists in the full submission, the main text does not clearly articulate to readers the conditions under which this relationship holds, when it can be expected to break down, or what diagnostics users should check. This makes the method feel more heuristic than it likely is.

- **Figure 4's validation is a stability check, not a correctness check.** The evaluation compares n̂* estimates from N preliminary experiments against n̂*₅₀ (the estimate at N=50) as a "ground truth." This measures internal consistency rather than recovery of the true n*. The paper notes that Appendix 1 provides synthetic experiments with known ground truth, but the main text's primary empirical validation is weaker than ideal. Readers relying only on the main text cannot tell whether the method recovers a meaningful quantity.

- **No comparison against simpler baselines.** The paper does not compare its estimates against even straightforward alternatives (e.g., a bootstrap estimating the variance of the mean rank, or a power-analysis-style heuristic like "use 30 datasets"). Without such comparisons, it is hard for readers to gauge whether the additional complexity of the kernel/MMD framework yields practically better estimates.

- **The gap between the definition (using ideal ℙ) and the estimator (using empirical ℙ̂**N**)** is acknowledged but not bounded. The paper states that ℙ̂_N converges to ℙ as N increases, but provides no bound on the approximation error or guidance on how large N must be for the estimate to be reliable in practice. This is noted as future work (Section 6).

- **No sensitivity analysis for kernel bandwidths.** The paper provides reasonable recommendations (ν=1/nₐ for Borda, ν=1/C(nₐ,2) for Mallows) but does not examine how n* estimates vary with these choices. Since the estimated n* plausibly depends on bandwidth, this is a gap.

- **Missing value imputation (worst rank) could bias results.** The paper imputes missing evaluations with the worst rank and mentions this as a limitation, but does not assess the sensitivity of the n* estimates to this choice.

- **Limited practical guidance for choosing (α*, δ*).** The paper translates ε* into the more interpretable δ* (e.g., "average Jaccard coefficient = 0.95") but offers no guidance on what values of δ* are reasonable thresholds for real studies.

### Trivial
None.

## Nice-to-Haves

- A diagnostic or stopping rule to detect when the log-log linear model is a poor fit and the extrapolation is unreliable.
- A third case study where the predicted n* could be externally validated (e.g., via a replication study).
- Discussion of how violations of the i.i.d. assumption on experimental conditions affect the framework's applicability.

## Removed Points

These points from the reviews were removed or downgraded; they are listed here for transparency:

1. **"Proof is only a sketch in the missing appendix."** The paper's appendix (which contains the proof) was stripped by the paper parser. Per policy, criticisms about missing appendix content are removed. The proof exists in the original submission.

2. **"'Observed in our experiments' is not a justification."** The paper presents this alongside a referenced proof (in the appendix), not as the sole justification. This critique misreads the paper's argumentation.

3. **"Held-constant factors are not truly fixed across replications."** The paper defines these as fixed by design, which is a standard modeling choice for a formalization. The critic's concern about real-world variability is a question of modeling fidelity, not a flaw in the formalization itself.

4. **"The paper should cover additional tasks/domains."** Demands for scope expansion beyond the paper's stated direction (depth within its own framework vs. breadth across domains).

5. **Formatting/style nitpicks and parser artifact complaints.** These relate to PDF extraction issues, not the original submission.

## Novel Insights

Beyond the paper's own contributions, the most interesting pattern across the reviews is the tension between the paper's two layers of contribution. The formalization layer (definitions, factor taxonomy, ideal vs. empirical studies) is universally recognized as a valuable first step. The estimation layer (Algorithm 1, Proposition 4.2) is where the disagreements concentrate — not because the idea is wrong, but because the validation in the main text relies on internal consistency (n̂* vs. n̂*₅₀) rather than ground-truth recovery. This suggests the paper would benefit from restructuring to clearly separate the formalization contribution (which stands independently) from the estimation contribution (which needs stronger validation or more modest claims). The reviews also reveal that the kernel-based approach to encoding study goals is underappreciated as a contribution — it is the bridge that makes the MMD framework applicable to real ML studies, and it deserves more emphasis.

## Suggestions

1. **Move the conditions for the log-log relationship and the synthetic validation from the appendix into the main text.** The main text currently relies on a short Proposition 4.2 with a reference to the appendix. Even a brief statement of the conditions and a figure from the synthetic experiments would significantly strengthen the main paper.

2. **Reframe Figure 4 explicitly as a stability/convergence analysis** (not a correctness check), and clearly state that correctness is validated on synthetic data (in the appendix). A two-sentence explanation would prevent misinterpretation.

3. **Add at least one simple baseline comparison.** Even a comparison against a naive heuristic ("use n=30 for all studies") or a bootstrap estimate of rank variance would help readers calibrate the value added by the kernel/MMD framework.

4. **Add a brief sensitivity analysis for kernel bandwidths** (e.g., vary ν by ±50% and report how n* changes). This would take minimal space and address a natural concern.

5. **Provide practical guidance for choosing δ*** (or ε*) — e.g., what values correspond to "strong similarity," "moderate similarity," etc., in the context of ranking studies. Currently the paper translates ε* to δ* but leaves the user without a reference frame.

6. **Acknowledge the i.i.d. assumption explicitly and briefly discuss when it may be violated and what the consequences would be.** A single paragraph in the limitations section would suffice.

## Score and Decision

**Originality:** High. The formalization of experimental studies and the quantifiable definition of generalizability are novel.  
**Importance:** High. The problem of non-generalizable results is recognized as critical by the community; a framework to measure and plan for generalizability addresses a real need.  
**Claims support:** Moderate. The formalization and definitions are well-supported. The estimation algorithm is less well-supported in the main text (stronger support exists in the removed appendix).  
**Soundness:** Good for the formalization; moderate for the algorithm's validation.  
**Clarity:** Generally clear despite mangled section references (parser artifact).  
**Value to the community:** Significant. The GENEXPY module, the kernel toolbox, and the framework itself are likely to be used by researchers designing benchmarking studies.

The paper makes genuine contributions: a principled formalization of experimental studies, a quantifiable definition of generalizability, and a practical algorithm backed by case studies. The weaknesses (primarily around the algorithm's validation in the main text and lack of baseline comparison) are real but addressable and do not undermine the core contributions. The paper is above the acceptance threshold.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>