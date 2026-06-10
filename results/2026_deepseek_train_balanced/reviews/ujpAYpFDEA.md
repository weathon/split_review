Here is my consolidated review:

---

## Summary

This paper opens a new problem: can a user querying an LLM service determine whether that service applies watermarking to its outputs? The authors propose Water-Probe, a detection method that exploits consistent distributional biases introduced by fixed watermark keys across similar prompts, and Water-Bag, a defense that increases key-selection randomness. Experiments span 8 watermarking algorithms and 9 LLMs.

## Strengths

- **Novel problem framing with clear practical motivation**: The paper cleanly separates *text-level imperceptibility* (can a watermarked output look natural?) from *service-level imperceptibility* (can a user tell the service itself uses watermarks?). This distinction is absent from prior work and has real-world relevance—providers may not want to disclose watermarking. The paper convincingly argues that prior text-level work and watermark-cracking work address different questions.

- **Broad empirical coverage yields a non-trivial finding**: Water-Probe is tested across 8 watermarking algorithms (including distortion-free methods like Aar, DiPMark, γ-reweighting) and 9 LLMs of varying sizes (1.5B–13B). The consistent result that even *distortion-free* watermarks are detectable at the service level is concrete and important—it shows that distribution-free ≠ undetectable when the same key is reused.

- **Core detection insight is sound and clever**: The idea of using two correlated prompts and comparing distribution *differences* under two watermark keys (thereby canceling the unknown original distribution) is elegant. The two variants (v1 for n-gram watermarks using a dummy prefix; v2 for fixed-key-list watermarks using shared random-token prefixes) are natural adaptations to different watermark structures, not ad-hoc hacks.

## Weaknesses

### Fatal

None.

### Major

- **Water-Bag inversion is a property, not a construction**: Equation 12 defines what an inverted key must satisfy—averaging the distributions from key and inverted-key recovers the original. But the paper provides no algorithm, example, or proof of existence for such an inversion for any concrete watermarking method (e.g., KGW). For KGW, the watermark key determines a green/red list split; what does it mean to "invert" this such that averaging the two biases yields the original logits? Without a construction, Water-Bag cannot be implemented, and the experimental results claimed for it cannot be interpreted. Since Water-Bag is presented as the paper's third contribution, this is a substantial gap.

- **Variance estimated from only 3 repetitions**: The z-test (on which detection decisions rest) uses a standard deviation computed from 3 experimental repetitions (line 209). Estimating a variance from 3 data points yields an extremely unstable estimate. The qualitative conclusions (large separation between watermarked and non-watermarked similarity values) likely survive this issue, but the reported z-scores and significance levels are not trustworthy. The paper should use bootstrapped intervals, more trials, or at minimum explicitly flag this limitation.

### Minor

- **Theoretical apparatus is decorative, not quantitative**: The Lipschitz continuity assumption (Assumption 1) is stated without verifying or estimating *L* for any tested algorithm—and for methods like KGW with a hard green/red split, the transformation may be discontinuous. Theorem 1 asserts ρ > 0 without bounding it in terms of any measurable quantity. The z-test's null mean μ=0.1 is set ad hoc (line 209). These elements give an impression of rigor that the paper does not deliver. The paper would be better served by framing the theoretical content as intuition-building motivation rather than formal proof.

- **Prompt construction assumptions acknowledged but untested**: Water-Probe-v1 assumes a prefix like "abcd" does not affect the subsequent output distribution. The paper states this is "challenging to ensure" but does not test whether *different* prefixes produce systematically different similarity values. Water-Probe-v2's key approximation (Figure 4) shows spread for some prefixes but includes no analysis of how this approximation error propagates into detection accuracy. These assumptions are plausible but untested.

- **No comparison against simpler detection strategies**: Since this is a new task, no prior methods exist. However, the paper would be stronger by comparing against trivial baselines—e.g., does the variance of repeated outputs under a single prompt, or the KL divergence between output distributions for different prompts, already separate watermarked from unwatermarked models? Without this, it is unclear whether Water-Probe's specific cross-prompt, cross-key design is necessary.

- **Query cost undiscussed**: Water-Probe-v2 requires at least 10⁴ queries per detection. The paper notes this but does not discuss whether this cost is practical in realistic threat scenarios, or whether detection could work with fewer samples through other techniques.

### Trivial

None.

## Nice-to-Haves

- Report ROC curves or detection rates at a fixed false-positive rate (e.g., 1%) alongside average similarity values.
- Test temperature robustness on more than one model (currently only Llama2-7B).
- Provide confidence intervals for the main similarity results using more than 3 trials.

## Removed Points

These points were flagged in the input reviews but removed per the filtering rules. Treat them with caution.

- *Missing tables via \input{}*: The harsh critic noted that tables are embedded via \input{} commands. These are present in the original submission; the parser strips them. Removed per hard rule on parser artifacts.
- *No baselines presented as a fatal issue*: The critic presented this as a "critical issue." Since no prior methods exist for this new task, the natural baseline is the unwatermarked null case, which the paper provides. The call for simple alternative methods is a reasonable suggestion but not a fatal flaw. Demoted to Minor.
- *General "overclaimed scope" criticism without concrete anchoring*: The critic's statements about "the central claim is unanchored" lacked a specific sentence or table anchor. Removed per filtering discipline.
- *Strength Finder's "important problem" framing*: Generic praise about the problem being "important" was dropped. Only the concrete, evidence-backed strengths were retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the Water-Bag inversion concretely.** Provide an explicit construction for KGW (the algorithm used in the Water-Bag experiments): what does an inverted master key look like, and how is it computed? If existence is not guaranteed, state that and explain what the experimental results actually show.
2. **Replace the 3-repetition variance estimate.** Either use bootstrapped confidence intervals from more trials, or report detection results without relying on parametric z-tests (e.g., directly report empirical separation with error bars).
3. **Add at least one trivial baseline.** Even a simple entropy comparison or per-token probability variance would help establish that Water-Probe's specific design is needed, not just sufficient.
4. **Tighten the theoretical framing.** Either remove Assumption 1 and Theorem 1 (since they provide no quantitative predictions used in the experiments) or replace them with clear intuitive justification that matches the paper's empirical nature.
5. **Test the prompt prefix assumption.** Compare Water-Probe-v1 similarity values under different "irrelevant" prefixes to quantify the assumption's impact.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>