Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper identifies a critical gap in tool-integrated math LLMs: they lack the autonomy to decide when to use chain-of-thought reasoning versus code execution, relying instead on externally dictated instructions. The authors propose AutoCode4Math, an Expectation-Maximization (EM) framework that treats methodology choice as a latent variable, alternating between self-exploration to discover a reference strategy (E-step) and self-refinement via off-policy RL (M-step). The practical implementation includes a novel self-reflective data synthesis strategy that creates multi-round responses transitioning between failed and successful methodologies. On the challenging MATH benchmark, AutoCode4Math improves DeepseekMath-7B accuracy by 20 absolute points (45.04% → 65.28%) while reducing code executions by up to 65%, with consistent gains across Llama-3.1, Qwen2Math, and DeepseekMath families.

## Strengths

- **Novel problem formulation and framework**: The paper formalizes the under-explored problem of autonomous methodology-selection in math LLMs and casts it as an EM problem with a latent variable representing the methodology choice. Treating the choice between CoT and code as something the model should learn on its own, rather than being told, is a genuine conceptual contribution (Section 2.2).

- **Substantial and balanced empirical gains**: The accuracy improvements are large and meaningful — +20% on MATH for DeepseekMath-7B (from 45.04% to 65.28%) and +7% on GSM8k (from 82.4% to 89.38%) — while simultaneously reducing code execution rates by up to 65–90% (Table 1, confirmed in the paper text). This demonstrates that the model learns not only *when* to use code but also *when not to*, yielding both performance and efficiency gains.

- **Generalization across model families and baselines**: The method is validated on three different model families (Llama-3.1, Qwen2Math, DeepseekMath) with consistent improvements. It outperforms DotaMath (which uses external annotations) and AlphaMath (which uses beam search at test time) using only greedy decoding, and is competitive with or exceeds several larger models (Table 1, Section 3.1).

- **Insightful analysis of learned behavior**: The alignment-rate analysis in Section 3.3 provides interpretable evidence for *how* the model improves — not just that it improves. The oracle-based categorization (StrictAlign, AllowCode, MisAlign) and the finding that AutoCode achieves higher strict alignment with the oracle compared to standard RL (Fig. 4) support the claim that the EM framework internalizes a principled methodology-selection strategy.

## Weaknesses

### Fatal

None.

### Major

- **E-step mathematical inconsistency between derivation and implementation**. The paper derives the reference strategy as proportional to the product of the prior and the Q-function: $s^*(c \mid x_q) \propto p_\theta(c\mid x_q)\,Q(x_q,c)$. However, Eq. (8) writes it as $s^*(c\mid x_q) = \exp(\alpha \cdot p_\theta(c\mid x_q)Q(x_q,c;\theta)) / Z(x_q)$. Exponentiating the *raw product* (rather than a log-linear combination $\exp(\alpha[\log p_\theta + \log Q])$) yields a distribution that differs from a properly normalized product. The paper neither justifies this exponentiation nor acknowledges the departure. That said, the practical implementation uses $\alpha = \infty$ (hard-max, greedy selection), under which both formulations collapse to the same argmax — so the inconsistency affects the theoretical framing, not the empirical results. Nevertheless, it undermines the claimed theoretical grounding and should be corrected or explicitly labeled as a modeling choice.

- **Insufficiently controlled and under-described RL baseline in the key ablation**. The ablation against "standard RL without explicit methodology-selection" (Section 3.2, Fig. 3, Table 2) is central to the claim that the EM formulation itself is responsible for the improvement. However, the paper provides almost no details about this baseline: what exact objective function it uses, whether hyperparameters were tuned, the number of rollouts, the clipping scheme, the learning rate schedule, or the number of iterations. Without this information, it is impossible for readers to assess whether the RL baseline was reasonably well-tuned or whether its rapid plateau reflects poor hyperparameter choices rather than a fundamental limitation of standard RL. This gap weakens the central comparative claim of the ablation study. Note: the paper's *main* results (Table 1) compare against strong published baselines (ToRA, DotaMath, AlphaMath, etc.) and stand on their own; this weakness pertains specifically to the ablation that attempts to isolate the EM advantage.

### Minor

- **The phrase "using merely a public query set" overstates the low-resource nature of the pipeline**. The abstract and introduction state that the approach uses "only a public query set," but the paper acknowledges (Section 3, Datasets paragraph) that the method "presupposes the model be able to solve math queries using code" and therefore uses SFT data from MetaMath, MathInstruct, OpenMath, and MMOS — many thousands of annotated (query + solution) examples — to equip the base models with code ability. The *AutoCode training stage* itself does not require additional human annotations, but the full pipeline depends on substantial prior SFT data. The phrasing could mislead readers about the total supervision required.

- **Self-reflective synthesis implementation is underspecified**. The paper states that the method uses "a reflective hint to transition to the another methodology" (Section 2.3.1) but never explains how this hint is realized — whether it is a special token, a hand-crafted prompt prefix, or a learned behavior. This detail is necessary for reproducibility and for critically assessing the data synthesis strategy.

- **Oracle preference for CoT is defensible but under-justified**. The oracle in Section 3.3 prefers CoT when both CoT and code succeed. While this choice makes sense if the goal is minimizing tool usage, the paper does not explicitly justify this design decision or discuss how alternatives (e.g., preferring code when both work) might change the alignment analysis.

### Trivial

None.

## Nice-to-Haves

- Algorithmic pseudo-code summarizing the iterative EM procedure (self-exploration → reference strategy → data synthesis → off-policy RL → repeat) would significantly improve clarity and reproducibility.
- Examples of learned methodology-selection decisions (both successful and failed) beyond what is shown in Fig. 1 would strengthen the qualitative analysis.
- An explicit statement of the off-policy correction form (beyond the clipping bounds) and the relative weighting between the RL term and the supervised term in Eq. (9) would aid reproducibility.

## Removed Points

These points from the reviewer inputs were evaluated against the paper and found to be invalid or unwarranted:

1. **Criticism that the self-reflective synthesis ablation figure reference is garbled/mislabeled** — Removed. The paper likely uses correct figure numbering in the original PDF; the apparent discrepancy (e.g., "Fig. 2 shows...NO REFL") is a parser artifact from PDF extraction. The ablation results are clearly reported in Table 2 and surrounding text.

2. **Criticism that the E-step equation makes the method "simply a heuristic" with no grounding** — Kept in modified form above. The critic's stronger claim that this invalidates the entire method is not supported, because with $\alpha=\infty$ (hard-max) the practical algorithm is unaffected. The inconsistency is a presentation/theoretical gap, not a practical flaw.

3. **Criticism about the paper's claim not being verifiable due to missing figures/tables** — Removed. The paper provides numerical results (Table 2 text, accuracy numbers in Section 3.1) that can be evaluated independently of any garbled figure rendering.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the work that the authors themselves do not already state.

## Suggestions

1. **Fix the E-step equation.** Replace Eq. (8) with the correctly normalized form consistent with the derivation: $s^*(c|x_q) = \frac{\exp(\alpha[\log p_\theta(c|x_q) + \log Q(x_q,c)])}{Z(x_q)}$, or explicitly state that the implementation uses hard-max over $p_\theta(c|x_q)Q(x_q,c)$ and note that the softmax in Eq. (8) is a modeling choice whose exponentiation form is a heuristic for smoothing (made moot by $\alpha=\infty$). The most important thing is transparency about the gap between the theory and the practical algorithm.

2. **Document the RL baseline thoroughly.** Add a table or paragraph specifying: the exact objective function used, number of off-policy samples, clipping bounds, learning rate, number of iterations, and whether hyperparameters were tuned (and if so, the search space). If the baseline is intended to be "standard RL" with a common configuration, state that explicitly and note any tuning effort.

3. **Specify the "reflective hint" mechanism.** Clarify whether the transition between methodologies in self-reflective synthesis is achieved via a template prompt, a learned token, or some other mechanism.

4. **Rephrase the "public query set" claims** in the abstract and introduction to acknowledge the SFT prerequisite, e.g., "using only public query sets and standard SFT data for initial coding ability."

5. **Provide ablation results** (EM vs. standard RL, NO REFL vs. full AutoCode) in a clean text table with accuracy and code-rate numbers for both GSM8k and MATH, not solely in figures.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>