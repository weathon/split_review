## Summary

This paper studies how predictive differences between two continuations of the same prompt evolve inside pre-LayerNorm residual transformers. It claims that the dynamics are "neutral": differences neither systematically shrink nor grow in expectation. The authors derive a drift identity, a predictable drift corridor, and a blended reporting rule for testing neutrality. Experiments on GPT2 variants and Qwen2.5 models (0.5B–3B) are presented as empirical support. The paper argues that this neutrality is a necessary condition for hallucination persistence and that onset-focused mitigation strategies cannot eliminate persistence because the backbone dynamics remain neutral.

## Strengths

- **Novel theoretical framing.** The paper introduces a formal martingale-based framework for analyzing how predictive differences propagate through residual transformers. The drift identity and predictable drift corridor are new analytical tools that connect architectural structure to the evolution of divergence.
- **Clean experimental design.** The controlled probes (closed vs. open regimes), the use of sibling rollouts, and the statistical tests (t-test, Azuma–Hoeffding, e-process) are well-motivated and appropriately applied. The results are consistent across model scales and families.
- **Clear separation of concepts.** The paper carefully distinguishes between predictive divergence and semantic correctness, and between necessary and sufficient conditions for hallucination persistence. This nuance is often missing in the literature.

## Weaknesses

### Fatal

- **The central claim of closed neutrality is not justified in the main text.** The paper states that in the closed regime the conditional expectation of the drift increment is zero (Lemma 5, Appendix A.3), but provides no proof sketch or even an intuitive argument in the main paper. This claim is the foundation of the entire theoretical analysis. Without a clear justification, the soundness of the core result cannot be assessed from the main text alone. For a theory paper, this is a critical omission.

### Major

- **The connection to hallucinations is not empirically validated.** The paper's title and framing emphasize hallucinations, but the experiments only measure predictive divergence (JS divergence) between paired continuations. No experiment directly tests whether predictive neutrality leads to semantic hallucination persistence, or whether models can correct meaning while predictive differences persist. The paper's contribution to the hallucination problem remains theoretical and unsubstantiated by evidence.
- **The paper does not test the sufficiency direction.** The authors state that neutrality is necessary but not sufficient for semantic hallucinations, yet they provide no experiments that demonstrate cases where predictive differences persist but semantics converge. This weakens the practical relevance of the claimed necessary condition.

### Minor

- **Limited model scale.** The largest model tested is 3B parameters. While the theory suggests scale invariance, empirical validation at larger scales (e.g., 7B+) would strengthen the claim that neutrality is an architectural invariant.
- **Short horizon.** The experiments use N=32 steps. The paper acknowledges this but does not provide longer-horizon experiments to confirm that neutrality holds over extended generations.

### Trivial

- The mean-field lift section adds conceptual framing but little new mathematical content beyond linearity of expectation. It could be condensed without loss.

## Nice-to-Haves

- Include a proof sketch of closed neutrality in Section 3.1 to make the paper self-contained.
- Add experiments that directly measure semantic hallucination persistence (e.g., using factuality benchmarks) alongside predictive divergence.
- Test on larger models (e.g., Llama 3 8B) if accessible.

## Novel Insights

The paper's key insight is that the residual architecture of pre-LN transformers imposes a neutral dynamics on predictive differences, meaning that deviations neither systematically shrink nor grow. This reframes hallucination persistence as an architectural invariant rather than a training artifact. The drift identity and predictable drift corridor are novel analytical tools that connect the architecture to the evolution of divergence. However, the lack of empirical validation linking predictive neutrality to actual hallucination behavior limits the practical novelty.

## Suggestions

- Provide a proof sketch of Lemma 5 (closed neutrality) in the main text. Without this, the theoretical contribution is incomplete.
- Either rename the paper to reflect that it studies predictive divergence dynamics, or add experiments that directly connect predictive divergence to semantic hallucination persistence.
- Consider testing on larger models to strengthen the scaling claim.

## Score and Decision

The paper presents a novel theoretical framework and clean experiments for predictive divergence dynamics, but the central theoretical claim is not adequately justified in the main text, and the connection to hallucinations is not empirically validated. These are significant weaknesses for a paper that positions itself as a structural account of hallucinations.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>