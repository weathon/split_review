Now I have a solid calibration picture. Here is my final consolidated review.

---

## Summary

ARENABENCHER proposes a framework for automatically evolving static benchmarks by having a pool of models generate candidate rewrites of test cases, filtering them through an LLM judge, and selecting those that consistently degrade performance across multiple models via iterative refinement. The core idea — using multi-model aggregated feedback rather than single-model adversarial signals — is well-motivated and addresses a real gap in benchmark contamination research. The paper evaluates on three domains (GSM8K, CommonsenseQA, Harmful Behaviors) and reports that the updated benchmarks are harder while maintaining alignment and fairness.

## Strengths

- **Multi-model feedback consistently outperforms single-model feedback across all settings.** Table 1 shows a clear, monotonic pattern: for every model and every domain, the accuracy drop (or ASR increase) is larger with m=3 than with m=1. For example, Llama-3.2-3B on GSM8K drops 47.7% with m=3 vs. 32.8% with m=1; Mistral-7B-I's ASR increase jumps from 2.2% to 23.6%. This provides direct evidence that aggregating signals across multiple models produces genuinely harder test cases.

- **Cross-domain generality demonstrated on three distinct benchmarks.** ARENABENCHER is evaluated on mathematical reasoning (GSM8K), commonsense reasoning (CSQA), and safety (Harmful Behaviors). The framework increases difficulty in all three while maintaining alignment (91–94%) and fairness (85.5–92.8%), showing the method is not limited to a single task type.

- **Explicit fairness mechanism with empirical verification.** Section 3.3 describes near-uniform model sampling to avoid concentrating difficulty on a subset of models. The resulting fairness scores in Table 2 (e.g., CSQA improving from 82.9% to 92.8%) provide concrete evidence that the mechanism works.

- **Human annotation validates semantic fidelity.** Independent annotation of 100 randomly sampled GSM8K updates shows 95% alignment and 96% correctness. This human verification partially addresses concerns about the automated LLM judge and provides evidence that the increased difficulty does not purely reflect broken test cases.

- **Honest reporting of failure cases.** Figure 2 presents a clearly invalid update that passed the automated verifier, and the paper explicitly discusses both failure modes (missing constraint, added operation). This transparency is commendable and helps practitioners understand the framework's limitations.

## Weaknesses

### Major

- **No comparison against any existing benchmark augmentation method.** The paper cites MATH-Perturb (Huang et al., 2025), AR-AR (Yang et al., 2025; Abedin et al., 2025), Automatic Robustness Stress Testing (Hou et al., 2025), and gradient-based adversarial rewriting (Liu et al., 2023; Mo et al., 2025) in §2, and argues that these methods have limitations (single-model focus, local perturbations). Yet the evaluation compares ARENABENCHER only against its own m=1 variant and the original benchmarks. Without any empirical comparison, the reader cannot assess whether multi-model feedback actually provides benefits over existing approaches — or whether the difficulty increases simply reflect generating harder but possibly broken test cases at a rate comparable to simpler baselines. This is the single largest gap in the paper.

- **No statistical reliability measures.** All results in Tables 1 and 2 are single numbers with no error bars, confidence intervals, or multiple seeds. The pipeline involves random components: model subsampling (m=3 out of 6), random candidate generation, and selection. Repeated runs could yield meaningfully different results. Without any measure of variance, the quantitative comparisons (e.g., m=1 vs. m=3, difficulty differences across domains) are uninterpretable as evidence of systematic effects. This is a standard expectation for experimental ML papers.

- **Circularity in automated alignment verification.** GPT-4o is used for ability extraction, candidate generation, correctness verification, and alignment scoring (line 230). The alignment metric thus reflects GPT-4o's judgment of whether its own generation pipeline preserved intent. The human evaluation on 100 GSM8K samples partially breaks this circularity, but (a) it is limited to one domain — no human evaluation for safety (where alignment is most critical) or commonsense reasoning; (b) the paper does not report per-sample agreement between the human and automated judges, so the false-positive rate of the automated verifier on these 100 samples cannot be assessed. The case study in Figure 2 confirms that the verifier has real blind spots, but their frequency across the full benchmark is unknown.

### Minor

- **Verifier failure rate unquantified.** The case study (Figure 2) shows a clearly invalid update that passed the automated verifier. The human evaluation suggests approximately 4–5% of GSM8K updates may be problematic, but this is only for one domain. The paper does not report the verifier's rejection rate during candidate generation (what fraction are filtered as invalid?), nor does it analyze which types of updates the verifier systematically misses. This makes it difficult to assess how much of the reported difficulty increase reflects genuine challenge vs. artifact.

- **No ablation of the ability extraction component.** The framework hinges on extracting a structured "ability description" to guide candidate generation, but the paper never tests whether this improves generation quality over simply conditioning on the original question and answer. An ablation comparing generations with and without the extracted ability description would clarify whether this step contributes meaningfully.

- **Limited model pool for a "diverse" claim.** The pool includes 6 models from 3 families, all under 8B parameters. While the paper describes these as "diverse" in terms of families and training procedures, the absolute scale is limited. This weakens the generality of claims about "multi-model" feedback — the method is demonstrated only on small open-source models, not on the wider range of architectures and scales that real benchmarks must handle.

- **Human evaluation covers only one domain.** The human annotation (100 GSM8K samples) provides useful validation but is limited to math reasoning. For the safety domain (Harmful Behaviors), where alignment is arguably most critical, there is no human verification at all. The 90.6% alignment score for the safety domain relies entirely on the circular GPT-4o judge.

### Trivial

- None.

## Nice-to-Haves

- Ablation of the √K heuristic for selecting m=3. The paper cites ensemble tree theory but does not test alternative values (e.g., m=2, m=4, m=6).
- Quantification of computational cost (number of GPT-4o calls, model forward passes, total cost) for the full pipeline.
- Analysis of semantic similarity between original and updated test cases (e.g., n-gram overlap) to assess residual leakage potential.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- "Model pool is not diverse" — The paper uses three families (Llama, Qwen, Mistral) at different scales. While the absolute size range is limited (1B–7B), calling them "diverse" in terms of families is reasonable.
- "The √K heuristic is not justified" — The paper cites ensemble heuristics (Breiman 2001; Chen & Guestrin 2016) as justification. An ablation would strengthen this, but the justification is present.
- "Original fairness is already high so improvement is marginal" — GSM8K fairness goes from 84.8% to 87.8% and CSQA from 82.9% to 92.8%. The CSQA improvement is substantial, and maintaining fairness while increasing difficulty is itself a meaningful result.
- "Case study undermines the paper" — The paper honestly reports a failure case and discusses its causes. This is transparency, not a weakness. The underlying issue (unquantified verifier failure rate) is retained as a minor weakness above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add at least one external baseline.** The single highest-impact addition would be a simple baseline: generate candidates identically but select based on loss from a single fixed model (single-model adversarial), and a no-feedback random selection baseline. Even these simple baselines would isolate the benefit of multi-model aggregation. Comparison against an existing method like MATH-Perturb or Automatic Robustness Stress Testing would be even stronger.

2. **Run the full pipeline multiple times with different random seeds** and report mean ± std for all metrics in Tables 1 and 2. This is essential for the m=1 vs. m=3 comparison to be interpretable.

3. **Extend human evaluation to at least the safety domain** (Harmful Behaviors), where automated alignment judgments are least trustworthy. Report per-sample agreement between human and automated judge to establish the verifier's false-positive/negative rate.

4. **Report the verifier's rejection rate** — what fraction of generated candidates are flagged as invalid at each iteration? — and conduct error analysis on the false positives (candidates that pass the verifier but are actually invalid).

5. **Ablate the ability extraction component** by comparing generations with and without the structured ability description to confirm it improves candidate quality.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| adSdHgWGBB (Wasm test generation) | 3.00 | R1 (low) | Weaker paper; ARENABENCHER has a more interesting problem and clearer contribution |
| BltaWJZMeR (DataSciBench) | 3.20 | R1 (low) | Weaker; ARENABENCHER's multi-model feedback idea is more novel |
| ymt4crbbXh (AutoBencher) | 6.25 | R1 (mid) | Stronger paper — has baselines, novelty metrics, broader evaluation; ARENABENCHER lacks these |
| iv1TpRCJeK (∀uto∃∨∧L) | 6.33 | R1 (mid) | Stronger — has formal verification, cleaner evaluation; ARENABENCHER's evaluation is less rigorous |
| 7o6SG5gVev (TestGenEval) | 6.25 | R1 (mid) | Stronger — comprehensive benchmark with thorough analysis |
| chfJJYC3iL (LiveCodeBench) | 6.25 | R1 (mid) | Stronger — large-scale, contamination-free benchmark |
| YrycTjllL0 (BigCodeBench) | 9.00 | R1 (high) | Much stronger — broad, rigorously evaluated benchmark |
| syThiTmWWm (Cheating Automatic Benchmarks) | 7.75 | R1 (high) | Much stronger — sharp analysis, clear findings |
| ikqcUzUogm (BIND rule-following) | 4.75 | R2 | Similar tier — both have evaluation gaps, but ARENABENCHER's idea is more novel |
| riTiq3i21b (SWE-bench Multimodal) | 5.00 | R2 | Comparable — both have clear contributions with evaluation weaknesses; SWE-bench M was accepted |
| GnBBSlUb0S (Black-Box Adversarial Attack) | 4.60 | R2 | Slightly weaker — more narrow topic |

**Round 1 bracket:** 4.0–6.0. **Round 2 narrowing:** Comparison with SWE-bench Multimodal (5.00, accepted) and BIND (4.75, rejected) places ARENABENCHER in the 4.5–5.5 range. The paper's core idea is genuinely novel and well-motivated, which pushes it above the 4.5 floor, but the missing baselines and lack of variance measures prevent it from reaching the 5.5+ tier where papers like AutoBencher (6.25) sit.

**Final score:** 5.0. The paper has a real contribution and is clearly presented, but the evaluation is incomplete in ways that prevent the claims from being fully supported. The most critical gap is the absence of any comparison against existing benchmark augmentation methods — without this, the claimed advantages over prior work are asserted rather than demonstrated.

**Decision:** Reject. The core idea is promising and worth developing further, but the evaluation as presented does not meet the bar. Major revisions adding external baselines, multiple runs with variance, and broader human evaluation could make this publishable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>