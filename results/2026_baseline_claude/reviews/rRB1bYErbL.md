## Summary
R-HORIZON is a method for constructing multi-step, inter-dependent reasoning queries by chaining existing single-problem datasets (via a numerical offset dependency). The paper uses this to build a six-dataset benchmark that evaluates 25+ Large Reasoning Models (LRMs) and reveals systematic performance degradation as the reasoning horizon grows. It also uses the same composition to generate training data for RLVR, showing improvements on both multi-horizon benchmarks and standard single-problem tasks (+7.5 on AIME2024).

---

## Strengths

- **Breadth of empirical validation.** The benchmark covers 25+ models spanning 1.5B–235B parameters across math, code generation, and agentic tasks, with multiple levels of composition (n ∈ {1,…,20}). This is unusually thorough for a methods/benchmark paper and yields reliable trend estimates.

- **Double payoff: evaluation + training data.** A single composition pipeline serves both as a diagnostic benchmark and as a data factory for RLVR. The finding that composed training data improves *single-problem* accuracy (+7.5 AIME2024) beyond what single-problem training achieves is genuinely surprising and practically important.

- **Rollout efficiency analysis.** The paper shows that composed queries yield ~20% more effective rollout samples (Solve None and Solve All both reduced), explaining mechanistically why composed training is superior. This is a concrete, quantifiable insight beyond surface accuracy numbers.

- **Multi-dimensional analysis.** The paper goes well beyond reporting numbers: it characterises effective reasoning length, error position stabilisation, reflection locality, and thinking budget allocation, providing a rich picture of where and why LRMs fail under long horizons.

- **Scalable and annotation-free.** The construction pipeline requires no new human annotations; it recycles existing verified QA pairs, making the approach reproducible and cheap.

---

## Weaknesses

### Fatal
None.

### Major

1. **Mechanically trivial dependency construction.** Algorithm 1 implements the dependency function as a simple linear offset: f_i(x) = x + (m_{i+1} − a_i). This replaces a key variable in problem i+1 with the previous answer plus a constant, which is pure numerical substitution requiring no semantic cross-problem reasoning. A model that carries over any number and plugs it in arithmetically handles the dependency correctly even if it doesn't understand why. As a result, the benchmark tests *long-context sequential arithmetic* more than *genuine long-horizon reasoning*. This weakens the core claim that R-HORIZON exposes long-horizon reasoning limitations, as opposed to long-context arithmetic precision limitations.

2. **Training experiments confined to a single 7B model.** All RLVR experiments use R1-Qwen-7B only. The claimed benefits—+7.5 on AIME2024, improved reflection, better budget allocation—may be specific to this model, its training regime (Skywork-OR1 pipeline), or the capacity class. No evidence is provided that findings generalise to 32B or larger models where the performance gap from composed training might be smaller or larger for different reasons.

3. **Expected accuracy baseline assumes sub-problem independence.** Equation (4) estimates expected accuracy as ∏ p_i, where p_i is the atomic pass rate. This independence assumption ignores that the composed problems are *not* independent—the answer to problem i determines the numerical content of problem i+1. If a model makes a numerical error in problem i, problem i+1 becomes a different (possibly easier or harder) problem. The baseline therefore does not correctly isolate the compositional difficulty and can over- or under-estimate how much extra degradation is attributable to composition versus inherent task difficulty.

### Minor

1. **Anomalous result in benchmark table.** The MATH500 entry for one Qwen3-32B row at n=4 reads 127.6, which is physically impossible (accuracy > 100%). Although this appears to be a formatting or OCR artifact, it raises questions about whether other numerical entries in the dense multi-row table may have silent errors.

2. **Non-monotone WebShaper results.** o4-mini achieves 43.7% at n=1 but 87.6% at n=2 on WebShaper, a clear non-monotone anomaly. This is not explained in the paper. It may reflect prompt sensitivity or tool-call parsing artefacts for agentic tasks, but without explanation it undermines confidence in the agentic evaluation.

3. **All-or-nothing scoring interacts confusingly with composition depth.** At n=16, even a model with 90% per-problem accuracy would score 0.9^16 ≈ 19% under the independence baseline, making the absolute numbers difficult to interpret or compare across n. A complementary partial-credit metric (e.g., fraction of sub-problems correct) would disambiguate whether models are near-misses or completely failing.

### Trivial

- Some data rows in Figure 3 are duplicated (two entries for Qwen3-32B, each with different values), which is confusing even if both may be valid model variants.

---

## Nice-to-Haves

- Extend training experiments to at least one 32B model to check whether the +7.5 improvement scales.
- Add a semantic dependency construction (e.g., the answer is used as a count or index in a combinatorics/geometry problem) to demonstrate the method is not limited to numerical offset substitution.
- Provide ablations on whether the performance gap vs. expected accuracy shrinks if the expected baseline is corrected for dependency structure (using the joint probability rather than the product of marginals).

---

## Novel Insights

The clearest novel insight is the "model-specific effective reasoning length" finding: each LRM has an intrinsic token budget threshold—roughly 4–6k tokens for 7B models and 8–10k tokens for 32B models on MATH500—beyond which accuracy degrades sharply regardless of the task. This is evidenced by the stabilisation of the error-position curve (Figure 6). Equally novel is that training with composed multi-problem data improves *single-problem* performance beyond what single-problem training achieves, which implies that long-horizon training provides a general reasoning benefit that cannot be attributed purely to task-specific optimisation. The rollout efficiency explanation (composed queries reduce the fraction of "all-correct" rollouts, thus maintaining informative reward variance throughout training) provides a mechanistic account for why this generalisation occurs.

---

## Suggestions

- Compare R-HORIZON's semantic dependency mode (for code or geometry tasks where cross-problem relationships are genuinely semantic) against the offset-only math dependency to show which failure modes are truly long-horizon vs. arithmetic.
- Add per-model partial-credit accuracy curves alongside the all-or-nothing metric so readers can distinguish "catastrophic failure" from "near-miss" degradation.
- Investigate whether the +7.5 AIME gain persists when using the original (non-composed) test split, i.e., rule out that the composed training set leaks information about AIME-style problems.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>