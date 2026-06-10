Here is my final consolidated review.

---

## Summary

This paper addresses silent data corruption (SDC) errors during gradient aggregation in distributed training. It formally models these errors as per-worker Gaussian noise added to the averaged gradient ("gradient inconsistency"), then theoretically proves that this causes accumulated model divergence and a non-convergent term in the convergence bound (Theorem 3.2). To mitigate the issue, the paper proposes PAFT, a system comprising PAFT-Sync (periodic parameter synchronization with frequency H) and PAFT-Dyn (asynchronous overlap with dynamic frequency scheduling based on profiled error degree). Experiments on ResNet-18/50, GPT-2, and LLaMA-2 across 4–32 GPUs show that PAFT restores near-oracle convergence for small-to-moderate noise degrees.

## Strengths

- **Clear theoretical characterization of gradient inconsistency and its convergence impact.** Lemma 3.1 provides a closed-form expression for accumulated model divergence under noisy gradients ($\mathbb{E}||\bar{\theta}_{t+1}-\theta_{t+1}^{m}||^{2} = \frac{(M+1)\sigma^{2}}{M}\sum_{s=0}^{t}\eta_{s}^{2}$). Theorem 3.2 identifies a non-convergent term $T_3$ that only vanishes at zero learning rate, providing a principled mathematical explanation for why naive DSGD fails under gradient noise. This goes beyond prior empirical observations of SDC errors by formally linking the noise magnitude to convergence failure.

- **PAFT-Dyn's adaptive synchronization scheduling is grounded in the theory.** The dynamic adjustment of synchronization frequency $H$ based on the signal-to-noise ratio derived from the convergence analysis is a clean connection between theory and system design. Table 3 quantifies the benefit: PAFT-Dyn reduces the extra overhead by up to 11.0% compared to fixed-frequency PAFT-Sync at 32 workers.

- **Empirical validation spans multiple model families, optimizers, and noise patterns.** The evaluation covers CNNs (ResNet-18/50 on CIFAR-10/100) and LLMs (GPT-2 pretraining, LLaMA-2 finetuning), with both SGD momentum and Adam. Results consistently show that PAFT recovers near-oracle convergence for $\sigma^2 \leq 0.001$, where vanilla noisy training fails. The burst-noise experiment (Figure 9) demonstrates PAFT's ability to recover from intermittent large noise, which is the most realistic failure scenario.

## Weaknesses

### Fatal
None.

### Major

- **The Gaussian noise model is a significant simplification of actual SDC errors.** The paper models gradient inconsistency as independent per-worker additive Gaussian noise (Definition 2.1). Real SDC errors (bit flips in memory or network packets during all-reduce) have structured, non-Gaussian patterns — they can corrupt specific tensor elements, flip signs, or produce outliers. The paper's theoretical analysis, convergence bound, and simulated experiments all depend on this Gaussian assumption. While the paper acknowledges different noise degrees and burst patterns, it does not validate against a more realistic fault model (e.g., random bit flips in gradient elements, injection at the communication level). This is not a fatal flaw — the Gaussian model is a reasonable first-order abstraction — but it leaves open the question of whether PAFT's guarantees translate to actual hardware SDC behavior.

- **The experimental scale is modest for a paper claiming to address "at scale" fault tolerance.** Experiments max out at 32 GPUs with small models (ResNet-50, GPT-2, LLaMA-2 via LoRA fine-tuning). The paper's own introduction motivates the problem using incidents from LLaMA-3 and Fire-Flyer clusters operating at hundreds to thousands of GPUs. The claimed "good scalability" is supported only by a wall-clock time trend at 4–32 workers, with 18.9% overhead at 32 GPUs. No evidence is provided at the scales where SDC errors are reported to be practically problematic. This is a gap between the motivating examples and the demonstrated results.

### Minor

- **PAFT-Sync (periodic parameter synchronization) is a straightforward application of a well-known technique.** The core mitigation mechanism — periodically averaging model parameters across workers — is periodic model averaging, a standard approach in distributed optimization (McDonald et al., 2010; Zhang et al., 2015; McMahan et al., 2017). The paper's novelty lies in (a) formulating the GA error problem, (b) providing theoretical analysis of divergence under this specific noise model, and (c) adding the adaptive frequency scheduling and asynchronous overlap in PAFT-Dyn. The framing could more accurately position the contribution as applying and theoretically grounding periodic synchronization for a specific error class, rather than implying a fundamentally new fault-tolerance paradigm.

- **Sections 4.2 and 4.3 (detailed PAFT-Sync and PAFT-Dyn descriptions) are missing from the extracted manuscript.** The paper announces these subsections but the text jumps from Section 4.1 to Section 5. While the high-level mechanism is described in the Introduction/Abstract and evaluated in experiments, the detailed algorithm, pseudocode, convergence proof for PAFT-Sync, and precise dynamic scheduling policy are not available for review in the extracted version. This is likely a PDF extraction artifact (other formatting issues are present throughout), but it prevents full evaluation of the method's details.

- **The 18.9% wall-clock overhead at 32 GPUs is non-trivial.** The paper frames this as acceptable, but for a fault-tolerance mechanism, this overhead is substantial — especially before considering that actual SDC errors are rare events. A more thorough cost-benefit analysis (e.g., overhead amortized over the expected frequency of real SDC events) would strengthen the practical motivation.

- **No comparison against existing robust aggregation methods.** The paper acknowledges Byzantine fault-tolerance methods (voting mechanisms, median aggregation) in the Related Work and Limitations sections, and notes PAFT could be combined with them. However, it does not compare against even a simple baseline like gradient median or trimmed mean on the same noise model. Even if these methods target a different problem (malicious vs. unintentional errors), they operate on the same interface (noisy gradients) and would provide an informative anchor for PAFT's relative effectiveness.

### Trivial
None.

## Nice-to-Haves

- A fault injection experiment at the communication level (random bit flips during all-reduce) would substantially strengthen the claim that PAFT works for real SDC errors beyond Gaussian simulation.
- An ablation separating the benefit of PAFT from the natural effect of learning rate decay (which the paper itself notes helps, and grounds in the theory) would clarify the marginal contribution of periodic synchronization.
- Reporting throughput (samples/second) or communication volume alongside wall-clock time would be more informative for scalability assessment.

## Removed Points

These points were flagged during consolidation and are retained here for traceability; they should not be treated as valid weaknesses:

- **"The method description is critically incomplete" (harsh critic's point #1):** Sections 4.2/4.3 are missing from the extracted text, but this is almost certainly a PDF parser artifact (there are clear extraction artifacts throughout). The high-level method is described in the Abstract and Introduction, and the experimental evaluation demonstrates it. Removed as a parser issue rather than an author error.

- **"The paper overclaims novelty — periodic synchronization is well-known" (harsh critic's point #2, first part):** The paper's novelty claim is specifically about addressing *GA errors* (SDC during gradient aggregation), not about inventing periodic synchronization. The contribution is the *application and theoretical analysis* of periodic sync for this specific, underexplored problem. The claim "first effort to improve system reliability against GA errors at scale" is reasonable given the problem framing. The point about periodic sync being known is retained in weakened form under Minor weaknesses.

- **"The learning rate decay observation undermines PAFT's novelty" (harsh critic's end of Section-by-Section Notes):** The paper explicitly connects the LR decay observation to Lemma 3.1 and Theorem 3.2, showing that smaller learning rates reduce the divergence bound. This is an analysis, not an undermining observation. Removed as factually incorrect about what the paper says.

- **"Byzantine methods are mentioned which undermines the first-effort claim" (harsh critic's end of point #2 and Limitations section note):** The paper explicitly distinguishes GA errors (unintentional hardware errors) from Byzantine faults (malicious actors). Mentioning them as complementary future work does not undermine the paper's specific claim. Removed.

- **Various reproducibility nitpicks (missing hyperparameters, missing appendix proofs, missing statistical significance bars):** These are either parser artifacts or minor concerns that do not affect the core evaluation. Moved here per hard rules.

- **"Missing related works" concern:** Not included — reviewer does not have external sources to verify this.

## Novel Insights

The harsh critic raises a genuinely insightful tension that the paper does not fully address: PAFT's periodic synchronization only corrects *inconsistency* between workers (the divergence term in Lemma 3.1), but does not correct the *direction error* in the averaged gradient itself. The paper acknowledges this gap ("the noise not only introduces gradient inconsistency, but also the noised gradient direction that influences gradient descend") and correctly identifies it as the reason PAFT cannot fully close the gap for large noise. However, this framing also exposes a limitation in how the problem is scoped: the theoretical analysis conflates two effects under the same Gaussian model, but periodic synchronization only addresses one of them. A paper that cleanly separated these two failure modes — inconsistency vs. corrupted direction — would provide more actionable guidance. Beyond this, no novel insight emerges beyond the paper's own contributions.

## Suggestions

1. Add a fault-injection experiment that corrupts actual gradient tensor elements (e.g., random bit flips in the all-reduce buffer) to validate that PAFT transfers beyond the Gaussian simulation model.
2. Include at least one robust aggregation baseline (median gradient or trimmed mean with periodic sync) in the comparison to calibrate PAFT's effectiveness against existing approaches.
3. Provide a more detailed description of the dynamic H scheduling policy for reproducibility (the current "according to the signal-to-noise ratio" is underspecified).

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>