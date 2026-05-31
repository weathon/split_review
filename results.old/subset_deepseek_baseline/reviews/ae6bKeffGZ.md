## Summary

Arithmetic-Bench is a dynamic benchmark that evaluates LLMs on basic arithmetic operations (addition, subtraction, multiplication, division) across varying digit lengths, plus related sub-tasks like copying, reversing, and base conversion. The paper argues that arithmetic is a proxy for multi-step reasoning, provides a theoretical argument linking capacity to reasoning, and benchmarks over 20 models. The main empirical finding is that all models fail dramatically when the number of digits exceeds about 10 for multiplication and around 100 for addition, indicating a lack of length generalization.

## Strengths

- **Clean, scalable, and reproducible design.** The benchmark is purely synthetic, problems are randomly generated per digit length, and evaluation uses a straightforward substring match. This avoids many pitfalls of static benchmarks (memorization, formatting ambiguity, human bias).
- **Broad model coverage.** The paper tests a wide range of model sizes and families (LLaMA, Qwen, DeepSeek, GPT) across 1–100 digits, producing clear length generalization curves. This gives the community a systematic picture of current limitations.
- **Demonstrates memorization on finite datasets.** Figure 2 shows that models can memorise the AIME test set after many epochs, illustrating the risk of using static reasoning benchmarks. This strengthens the motivation for using dynamic arithmetic tasks.
- **Reasoning vs. non-reasoning model comparison.** The observation that reasoning models (DeepSeek R1, QwQ, Qwen3-think) outperform non-reasoning models on multiplication but not on simple addition is a useful empirical finding (Table 4, Table 5).

## Weaknesses

### Fatal

- **Theorem 2 is unsupported and does not justify the proxy claim.** The statement “Any reasoning task can be encoded as an equivalent arithmetic problem by mapping basic operations to numbers” is not formalised, let alone proven. Encoding a complex reasoning task (e.g., logical deduction over first-order logic) as a single integer arithmetic problem would require polynomial-time reductions with proper complexity classes, which the paper does not provide. The claim that arithmetic performance is a *proxy* for general reasoning ability remains an assertion without evidence. This undermines the paper’s central motivation.

### Major

- **No comparison with existing arithmetic benchmarks.** The paper mentions Math401 and BIG-Bench arithmetic but does not run its benchmark against them on the same models. Without a comparative analysis, it is unclear whether Arithmetic-Bench reveals anything beyond what those simpler benchmarks already show. The paper cannot claim that its benchmark is “better” or that it “addresses limitations” of existing ones without such experiments.
- **Theoretical capacity analysis is too trivial to be useful.** Theorem 1 (a container cannot hold more than its capacity) is vacuously true and adds no insight. The connection to parameter-capacity scaling laws (Allen-Zhu & Li 2024) is cited but not integrated with the benchmark results. The paper never actually estimates the information content of arithmetic tasks or measures model capacity limits. The theory section does not inform the experimental design or analysis.
- **The error accumulation analysis (Section 3.2) is basic probability and irrelevant to the benchmark.** The verification model (one independent verification) is not implemented or tested. The analysis does not interact with the empirical results or the benchmark design. It reads as a generic comment rather than a part of the paper’s technical contribution.
- **Evaluation metric “a in b” is insufficiently justified.** For multi-digit numbers, a correct substring could appear by chance (e.g., a 3-digit correct chunk inside a longer wrong output). The paper dismisses this as “extremely low” probability, but does not measure the false-positive rate on their own data. In a benchmark claiming rigorous evaluation, this is a significant concern.

### Minor

- **The claim that “memorization is impossible because the space is infinite” is conflated with “memorization provides no advantage.”** While it is true that the full space of n-digit multiplications is too large to brute-force memorise, models could still memorise patterns (e.g., multiplication by small numbers, particular digit-level regularities). The paper does not analyse what aspects of arithmetic a memorising model could learn.
- **The length generalization curves are only shown for multiplication (Figure 1).** The paper mentions 100-digit addition failures but does not plot the curve. A fuller picture would include curves for all main tasks.

### Trivial

- None beyond what has been noted.

## Nice-to-Haves

- Include length generalization curves for all tasks (addition, subtraction, division).
- Compare against existing benchmarks (Math401, BIG-Bench arithmetic subset) on the same models to demonstrate added value.
- Provide a formal encoding of a standard reasoning problem (e.g., a simple logical deduction) into arithmetic to concretely support Theorem 2.
- Measure the false-positive rate of the “a in b” metric on the actual outputs.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

1. **Drop or substantially revise Theorem 2 and the capacity analysis.** The current theoretical framework is not rigorous and does not support the proxy claim. If the authors wish to argue that arithmetic is a proxy, they should either provide a formal reduction or fall back to the weaker but defensible position that arithmetic is a *useful testbed* for length-generalization and multi-step exactness, without overclaiming.
2. **Add direct comparisons with existing arithmetic benchmarks** (Math401, BIG-Bench arithmetic). This would clarify whether the dynamic, length-varying design yields different insights from static fixed-length benchmarks.
3. **Report false-positive rates for the substring evaluation** on a validation set of model outputs, or switch to exact-match (after normalising formatting) and relax the strictness only for minor formatting variations.
4. **Show length generalization curves for all four main operations** to give a complete picture of failure modes.
5. **Tone down the claim that arithmetic is a proxy for “general reasoning.”** The current evidence (a weak correlation in Table 5 and an unsupported theorem) is insufficient. Instead, position the benchmark as a test of *computational stability and length generalization*—a valuable but narrower property.

## Score and Decision

MY FINAL SCORE: 4.0</score>
MY FINAL DECISION: Reject</decision>