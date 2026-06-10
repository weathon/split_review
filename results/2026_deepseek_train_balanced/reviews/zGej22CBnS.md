Now I have thoroughly verified the claims against the paper. Here is my synthesized final review.

---

## Summary

This paper introduces the Byte-Token Representation (BTR) Lemma, which provides an exact decomposition of byte-level sequence probabilities from any tokenized language model using "cover encodings." From this lemma, the authors derive an inference-time algorithm that converts tokenized LMs into byte-level LMs without retraining, correcting a phenomenon they term "tokenization bias." The method is applied to two use cases: fill-in-the-middle (FIM) code completion (≈18% improvement on CodeLlama-7b) and cross-vocabulary model ensembling (up to 3.7% improvement on HumanEval).

## Strengths

- **The BTR Lemma is a clean, correct theoretical contribution.** The decomposition of \(P(x^n_1)\) into a sum over disjoint cover encodings (Lemma 1) is a principled and non-trivial insight. It goes beyond the heuristic "token healing" fix by providing an exact accounting of all valid tokenization paths that could generate a given byte prefix. The lemma is stated for any deterministic tokenizer, not just BPE/MPE, which gives it genuine generality.

- **The efficient sampling algorithm (§4.2) is practical and well-motivated.** Rather than recomputing the full cover set at each byte, the authors show how to incrementally update the cover encoding set from one byte to the next by partitioning the previous cover set into \(C_{n+1}(a)\) and \(\bar{C}_{n+1}(a)\). This reduces the per-step cost to a single forward pass (plus bookkeeping), making the method usable in practice. The authors honestly acknowledge the upfront \(O(n\ell)\) cost and memory overhead in the limitations.

- **The Markov chain sanity check (§3.2) validates the theory in a controlled setting.** Demonstrating that the BTR correction recovers the exact ground-truth transition probabilities on a 3rd-order Markov chain with a trained transformer provides strong evidence that the theoretical analysis is sound and the algorithm is correctly implemented.

- **The FIM application solves a real, acknowledged problem.** The SPM-mode tokenization issue (prompts truncated mid-token) is a known practical problem in code infilling. Showing that byte-level decoding recovers the ≈18% gap between SPM and PSM modes, and even beats token healing by 1%, is a concrete demonstration of practical value.

## Weaknesses

### Fatal
None.

### Major

- **The headline FIM improvement (18%) rests on a single model and a single benchmark.** The FIM experiments (Section 5, line 431) are conducted only with CodeLlama-7b on the random-span infilling benchmark from Bavarian et al. (2022). No results are shown for other model families (DeepSeek-Coder, StarCoder, GPT-based FIM models), other model scales, or other FIM benchmarks. The abstract and introduction present this 18% as a general result ("achieves an approximately 18% improvement in FIM coding benchmarks"), but without evidence that it generalizes beyond this specific combination, the claim is overextended. The paper's theoretical contributions do not depend on the breadth of the FIM evaluation, but the headline empirical claim does. Either broader evaluation or explicit qualification of the scope is needed.

- **The ensemble results lack comparison against the most closely related alternative methods.** The related work section (line 368) discusses Huang et al. (2024) and Gu et al. (2024) as previous approaches to vocabulary-agnostic ensembling, and the paper explains why the BTR approach is theoretically more principled. However, no empirical comparison against these methods is provided. Without this, the reader cannot assess whether the 3.7% HumanEval improvement reflects an advantage of the BTR framework over alternatives, or simply reflects the well-known benefit of ensembling. An apples-to-apples comparison on at least one benchmark would substantially strengthen the ensemble contribution.

### Minor

- **The "O(1)" complexity claim in the contributions list is imprecise as stated.** The contributions (line 76–77) say the algorithm "carries an O(1) computational cost in terms of model runs." This is true for the *per-sampled-byte* cost after the initial cover encoding search, but the cover search itself costs up to \(O(n\ell)\) model runs for an \(n\)-byte prefix (line 315). The paper does acknowledge this in the algorithm description and the limitations section, but the contribution statement omits this qualification. Readers evaluating the method's efficiency will see "O(1)" and may be misled about the total cost. The paper should explicitly state "O(1) per sampled byte after an initial \(O(n\ell)\) precomputation."

- **The cover encoding search runtime is empirically underspecified.** The paper states (line 315) that "the actual number of inference runs is much lower" than the worst-case \(n\ell\) bound because "\(\mathrm{encode}(x^i_1)\) of the current iterations often contains encodings of the later iterations." No empirical characterization of this is given. For a practitioner deciding whether the method is practical for a 500-byte prompt, it matters whether the typical cost is \(n\ell \approx 4000\) model runs or more like 20. Reporting the empirical distribution of cover set sizes and model runs across the FIM/ensemble benchmarks would resolve this.

- **Token healing comparison precision.** The paper claims (line 66) that the method "surpasses a specialized fix, token healing, by 1%." But the FIM benchmark results for token healing are mentioned only in passing, and the 1% number is not shown in the text body (it may be in a table stripped by the parser). If it is in a table, this is fine; if not, the support for this particular claim should be clearer.

### Trivial
None.

## Nice-to-Haves
- An ablation quantifying what fraction of SPM-mode FIM errors are attributable to mid-token tokenization bias vs. other causes would clarify the scope of the method's relevance.
- An empirical comparison against at least one of the alternative ensemble methods cited (Huang et al., 2024; Gu et al., 2024) would ground the ensemble contribution.
- Reporting the typical empirical number of model runs required for the cover search on realistic prompt lengths would help practitioners assess practicality.

## Removed Points
These points from the inputs were examined against the paper and removed with justification:

- **Greedy decoding as a contradiction of the core framework** (Harsh Critic point 2): The reviewer claimed the unexplained greedy-decoding improvement "undermines the core framing ('statistically equivalent')." This is wrong. Statistical equivalence is about distributions over complete sequences; it does not constrain argmax paths under greedy search. The paper explicitly acknowledges (line 466) that "our theory does not provide insight into the employed greedy evaluation process" and honestly flags the observation as surprising. This is transparency, not a contradiction. **Removed.**

- **Missing statistical significance/variance** (Harsh Critic): Requesting confidence intervals for pass@k metrics on code benchmarks where single-run evaluation is standard is not a standard methodological requirement for this genre. **Removed per soft rules (genre-standard practice).**

- **"Statistical equivalence vs practical degradation" distinction** (Harsh Critic): The reviewer claimed the paper would benefit from a sharper separation between theoretical and empirical claims. The paper already separates these cleanly: §3 establishes the theory and definition of bias, §4 presents the correction algorithm, §5 tests empirically. **Removed as already addressed.**

- **"Not yet released" or reproducibility concerns about cited references**: The paper cites standard open models (CodeLlama, Yi-Coder, Mistral). **Removed per hard rules (do not question existence of cited references).**

- **Strength Finder's "single forward pass at the start of sampling"**: This is inaccurate — the cover search algorithm requires up to \(O(n\ell)\) model runs, not a single forward pass. The strength (algorithm is efficient per-step and requires no retraining) is kept but rephrased accurately in the Strengths section above. **Original claim removed, corrected version retained.**

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface observations about the paper that the authors do not already acknowledge.

## Suggestions

1. **Clarify the O(1) claim** in the contributions: replace "carries an O(1) computational cost in terms of model runs" with "carries an O(1) per-step cost after an initial O(nℓ) cover-encoding precomputation."
2. **Broaden the FIM evaluation** to at least one more model family (e.g., StarCoder or DeepSeek-Coder), or **qualify the headline claim** to refer specifically to CodeLlama-7b on the random-span benchmark.
3. **Add an empirical comparison** against at least one alternative ensemble method (Huang et al. or Gu et al.) on a single benchmark to ground the ensemble results.
4. **Report empirical cover search costs** (typical number of model runs for realistic prompt lengths) so practitioners can assess practicality.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>