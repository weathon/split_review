## Summary

This paper introduces Arithmetic-Bench, a dynamic benchmark for evaluating multi-step reasoning in LLMs through basic arithmetic operations (addition, subtraction, multiplication, division) and related sub-tasks (copying, reversing, counting, base conversion). The authors argue that arithmetic tasks serve as a proxy metric for general reasoning ability, provide theoretical analysis connecting arithmetic performance to reasoning capacity, and empirically demonstrate that current state-of-the-art models fail to generalize to arithmetic operations involving more than 10 digits, revealing fundamental limitations in their reasoning mechanisms.

## Strengths

- **Well-motivated problem**: The paper correctly identifies critical limitations of existing math benchmarks (contamination, memorization, evaluation difficulty) and makes a compelling case for why synthetic arithmetic benchmarks address these issues. The argument that large-number arithmetic cannot be solved through memorization due to the infinite space of possible problems is theoretically sound and practically important.

- **Clean, principled benchmark design**: Arithmetic-Bench is elegantly simple—randomly generated problems with deterministic answers, easy evaluation via substring matching, and natural difficulty scaling through digit length. The inclusion of sub-tasks (copy, reverse, space, count) provides diagnostic value by isolating specific sub-skills needed for multi-step reasoning.

- **Strong empirical evidence of failure**: The length generalization curves (Figure 1) clearly show that all models, including GPT-4o and DeepSeek-R1, exhibit a sharp accuracy drop from near-perfect to zero at around 10-11 digits for multiplication. This is a striking and reproducible finding that highlights a fundamental limitation of current architectures.

- **Theoretical grounding**: The paper provides formal definitions connecting arithmetic to reasoning (Definitions 1-2) and a capacity argument (Theorem 1) explaining why finite-parameter models cannot memorize infinite arithmetic spaces. The error accumulation analysis (Section 3.2) offers a principled explanation for why verification can dramatically reduce error rates.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 2 is not a valid proof**: The claim that "If a model cannot learn an arithmetic problem, it cannot learn a reasoning problem of equivalent complexity" is presented as a theorem with a proof sketch, but the proof is insufficient. The argument that "any reasoning task can be encoded as an equivalent arithmetic problem" is not substantiated—there is no construction showing how arbitrary reasoning tasks (e.g., logical deduction, planning) map to arithmetic problems while preserving complexity. This is a significant overclaim that undermines the paper's theoretical contribution. The paper would be stronger if it presented this as a conjecture or hypothesis rather than a proven theorem.

- **Limited experimental scope for key claims**: The correlation analysis (Table 5) between multiplication accuracy and AIME performance is based on only 6 data points, making it difficult to draw robust conclusions. The claim that "reasoning models exhibit stronger multiplication ability compared to non-reasoning models" is supported by only a handful of model comparisons. More systematic experiments with controlled variables (e.g., same base model with and without reasoning training) would strengthen this claim.

- **Missing analysis of failure modes**: The paper documents that models fail on large-number arithmetic but provides limited analysis of *how* they fail. Do models produce outputs of incorrect length? Do they make systematic errors (e.g., carrying errors in specific positions)? Do they fail to even attempt the computation? Understanding the failure modes would provide valuable insights for improving models and would strengthen the paper's contribution.

- **Uneven evaluation across models**: The paper uses n=10 problems per digit length for Qwen and LLaMA but only n=1 for DeepSeek and GPT models due to "resource limitations." With only 1 sample per digit length, the accuracy estimates for these models have very high variance, making comparisons unreliable. This is particularly problematic for the length generalization curves where individual data points at each length are based on a single trial.

### Minor

- **The proxy metric argument is underdeveloped**: The analogy to text rendering in image generation (Section 1.4) is interesting but the paper does not provide evidence that improving arithmetic performance leads to improved performance on other reasoning tasks. Without demonstrating transfer, the claim that arithmetic is a "proxy metric" remains speculative.

- **The memorization experiment (Figure 2) is not well-integrated**: The experiment showing that models can memorize the AIME test set through repeated training is interesting but feels disconnected from the main contribution. It would be more relevant to show that models *cannot* memorize large-number arithmetic problems, which is the paper's central claim.

- **Limited discussion of chain-of-thought prompting**: Given that the paper evaluates multi-step reasoning, there is surprisingly little analysis of how chain-of-thought prompting affects performance. The paper mentions Scratchpad/CoT in related work but does not systematically evaluate whether CoT improves arithmetic performance on this benchmark.

### Trivial
None.

## Nice-to-Haves

- Include error analysis showing the distribution of error types (digit count errors, specific position errors, etc.) to provide insights into failure modes.
- Evaluate whether providing intermediate scratchpad space or explicit step-by-step instructions improves performance.
- Test models on the same arithmetic problems with and without chain-of-thought prompting to isolate the effect of explicit reasoning.
- Include a small-scale experiment showing that models *cannot* memorize large-number arithmetic even with extensive fine-tuning, to directly support the paper's central claim.

## Novel Insights

The paper's most novel insight is the observation that arithmetic tasks provide a "natural testbed" for reasoning because they are deterministic, require structured multi-step execution, and have clear correctness criteria, while being immune to memorization due to the infinite problem space. The sharp phase transition in accuracy at around 10 digits for multiplication across all tested models is a striking empirical finding that suggests a fundamental architectural limitation rather than a data or training issue. The theoretical connection between information capacity and arithmetic generalization, while not fully proven, provides a useful framework for thinking about why current models fail to generalize.

## Suggestions

- Reframe Theorem 2 as a conjecture or hypothesis rather than a proven theorem, and provide a more rigorous discussion of what would be needed to prove it.
- Increase the sample size for DeepSeek and GPT evaluations to at least n=10 per digit length to ensure reliable accuracy estimates.
- Add a systematic error analysis section that categorizes and quantifies different types of errors made by models on large-number arithmetic.
- Include experiments with chain-of-thought prompting to understand whether explicit step-by-step reasoning improves performance on this benchmark.

## Score and Decision

The paper makes a solid contribution by introducing a well-designed, principled benchmark that cleanly exposes a fundamental limitation of current LLMs. The empirical findings are clear and reproducible, and the motivation for the benchmark is strong. However, the paper overclaims on theoretical contributions (Theorem 2 is not properly proven) and has some experimental limitations (uneven sampling, limited correlation analysis). The core contribution—the benchmark and the empirical demonstration of failure—is valuable and likely to be useful to the community. The paper is borderline between accept and reject; I lean toward accept because the benchmark itself is a useful contribution and the empirical findings are important, but the theoretical overclaims need to be addressed.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>