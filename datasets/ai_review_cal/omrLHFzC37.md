- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8
Now I have enough information. Let me write the final consolidated review.

## Summary

The paper proposes DecomFL, a federated learning algorithm that uses zeroth-order optimization to reduce per-round communication from O(d) to O(1) in both uplink and downlink, transmitting only scalar gradient values and random seeds. Theoretically, it achieves a standard convergence rate with linear speedup and a dimension-free rate under a low-effective-rank assumption. Empirically, it demonstrates dramatic communication savings on LLM fine-tuning (MB vs. TB).

## Strengths

1. **Genuinely dimension-free communication per round.** The algorithm design (Sections 3.2–3.3) is clever and well-motivated. By decomposing ZO gradients into a scalar and a perturbation vector (reproducible from a seed), both uplink and downlink communication costs become O(1) per round—independent of model dimension d. Table 1 formalizes this clearly, and Algorithms 1–2 provide a concrete implementation. This is a clean, non-trivial algorithmic contribution.

2. **First dimension-free convergence rate under low effective rank in FL.** Theorem 2 establishes a convergence rate of O(√κ/√(mPR)) under the κ-effective rank assumption, which is independent of d. The paper correctly identifies this as a first in distributed FL (line 55). The analysis additionally quantifies the smoothing parameter μ, fixing the unrealistic μ→0 assumption in prior work (lines 338–340).

3. **Empirical evidence of massive absolute communication savings.** On OPT-1.3B fine-tuning, DecomFL transmits <2 MB total per client while achieving accuracy comparable to MeZO and FedZO (Table 2). Even accounting for potential issues with baseline numbers, the DecomFL costs are independently verifiable from the algorithm's per-round cost and are orders of magnitude below the 10.8 GB/round that standard methods require. The MNIST and Fashion experiments further demonstrate the trend across model sizes and tasks.

4. **Clean theoretical rate with linear speedup.** Theorem 1 and Corollary 1 establish a rate O(√d/√(mPKR)) under standard assumptions, explicitly showing linear speedup in m, P, and K. Figure 1 ablates both P and K, confirming the predicted behavior.

## Weaknesses

### Fatal
None.

### Major

1. **FedZO baseline communication costs are internally inconsistent with simple sanity checks.** The paper reports FedZO costs on SST-2 as 0.27 TB (OPT-125M) and 1937.15 TB (OPT-1.3B). Since FedZO transmits the full d-dimensional model each round, the cost per round scales proportionally to d (i.e., 10.4× more for OPT-1.3B than OPT-125M). The actual ratio of 1937.15/0.27 ≈ 7174× implies FedZO used ~690× more rounds for the 10.4× larger model—a discrepancy of two orders of magnitude with no explanation in the paper. This does not invalidate DecomFL's own costs (which are derived from the algorithm design and reported independently), but it undermines the headline comparison of "1 MB vs. 1937 TB." The paper must clarify whether (a) the FedZO numbers include something beyond per-round model transmission, (b) drastically different round counts were used per model size, or (c) there is a calculation error. Without this, the central comparative claim is not properly evidenced.

### Minor

2. **Low-effective-rank theory restricted to K=1, while experiments use K>1.** The paper explicitly restricts Theorem 2 to a single local step (K=1, line 318). The justification (that local steps are less beneficial for DecomFL because communication cost scales with K) is reasonable but means the dimension-free guarantee does not formally cover the multi-step regime used in the MNIST and Fashion experiments. This is a gap between theory and practice that the authors acknowledge but do not bridge quantitatively.

3. **Missing hyperparameter details for LLM experiments.** The paper reports learning rate, momentum, and local steps for MNIST/Fashion, but does not state the learning rate, batch size, number of rounds R, local steps K, or smoothing parameter μ for the LLM fine-tuning experiments in the available text. While some details may be deferred to an appendix (which is stripped by the parser), the main text should at minimum identify these critical values for reproducibility of the central LLM results. 

4. **"Nearly identical" claim overstates the evidence.** The paper states "the communication costs for both model sizes are nearly identical" (line 435). For DecomFL with P=5, the costs are: SST-2 0.18 MB vs. 0.12 MB, RTE 0.12 MB vs. 0.90 MB, BoolQ 0.12 MB vs. 0.90 MB. The RTE and BoolQ costs differ by 7.5× between model sizes. While all values remain tiny compared to baselines, the "nearly identical" language is imprecise for these cases.

### Trivial

5. **No standard deviations reported.** No error bars or confidence intervals are provided for any experiment, including the LLM fine-tuning table. Given the small client counts (2 clients sampled from 8), variability may be non-negligible.

6. **Fashion experiment x-axis not clearly defined.** The "effective communication vector length" on the x-axis of Figure 2 is not explained in the caption or text; inference is required to understand that it is cumulative scalars transmitted per client.

## Nice-to-Haves

- **Report wall-clock time or FLOPs.** The paper notes that ZO methods are computationally expensive but provides no runtime data. Since DecomFL trades computational cost for communication savings, reporting runtime for a representative configuration would help practitioners assess the trade-off.
- **Include BAFFLE as a baseline.** BAFFLE also achieves O(P) uplink via ZO but has O(d) downlink; comparing against it would better isolate DecomFL's novel contribution of dimension-free downlink.
- **Test on heterogeneous data splits.** The MNIST experiment uses Dirichlet(α=1), which is nearly i.i.d. A more heterogeneous setting (e.g., α=0.1) would strengthen the evaluation of real-world applicability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Speculative floating-point determinism concern:** The harsh critic raised that different clients may have different floating-point arithmetic causing drift over many rounds. This is a theoretical concern with no evidence that it occurs in practice in the experiments. No experiments in the paper show instability of this kind.
- **Severity of learning rate condition:** The harsh critic noted Theorem 1's learning rate bound is restrictive. This is a standard feature of ZO convergence analysis, not a weakness specific to this paper; the rate itself is what matters.
- **Client count scaling (downlink depends on M):** The paper's Table 1 already explicitly shows the M dependence in the downlink complexity (2MKP). This is disclosed, not hidden.
- **Top-K poor performance with k=10%:** This is a standard or even generous choice for communication efficiency; the critic's suggestion that 10% is too large is speculative. The paper cannot be faulted for using a common configuration.
- **Missing related works:** I cannot verify whether related works were mentioned, as I lack external sourcing.
- **Formatting/style/typo nitpicks:** Parser artifacts, not author errors.
- **Missing appendix content (proofs, hyperparameters):** The parser strips appendices; claims about missing content that would be in the appendix are not verifiable from available text.

## Novel Insights

None beyond the paper's own contributions. The reviews do not reveal any interpretation of the work that the paper itself does not already articulate.

## Suggestions

1. **Clarify the FedZO communication numbers.** Add a clear derivation: state the number of rounds R for each method and model size, the per-round cost formula used for FedZO, and show that the reported TB values follow from these. If the round counts differ across model sizes, explain why. If there was an error, correct it and re-report.

2. **Report missing hyperparameters for LLM experiments in the main text or a clearly referenced appendix.** Specifically: learning rate, batch size, smoothing parameter μ, local steps K, and total rounds R for each configuration.

3. **Add standard deviations or error bars to the LLM results table**, ideally over multiple runs or seeds.

4. **Tone down the "nearly identical" communication cost claim** for datasets where the costs differ by a factor of 7.5× (RTE, BoolQ). Qualify the statement or report the range.

5. **Consider reporting wall-clock time** for at least one representative configuration (e.g., OPT-125M on SST-2) to help readers understand the computation-communication trade-off.
