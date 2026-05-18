Now I have all the evidence I need to write the review. Let me produce the final consolidated assessment.

---

## Summary

This paper introduces ZO-PoG, a framework that jointly optimizes discrete text prompts and continuous embeddings for black-box pre-trained language models. It alternates between policy-gradient updates over Gumbel-Softmax parameters (for discrete tokens) and zeroth-order gradient updates in a low-dimensional subspace (for continuous prompts). The paper provides convergence analysis establishing a sub-linear rate, and experiments on five GLUE tasks across RoBERTa-large, GPT2-XL, and Llama3 show consistent improvements over BBT, BDPL, and SSPT.

## Strengths

- **First joint discrete–continuous prompt optimization for black-box PTMs.** The paper correctly claims novelty in unifying these two lines of work (BBT-style continuous optimization and BDPL-style discrete optimization) in a single alternating framework. Ablation studies (Figure 3) confirm that neither component alone matches the full method, validating the collaborative design.

- **Consistent empirical improvements across multiple backbones and tasks.** Results are reported on three model families (encoder-only, decoder-only, modern LLM) and five GLUE tasks, with ZO-PoG outperforming all baselines in nearly every setting. The 5.17% improvement on WNLI (RoBERTa-large, len=50) over the best baseline is a concrete, non-trivial gain.

- **Convergence analysis under standard assumptions.** Despite imperfections, Theorem 1 provides a formal convergence guarantee — an ε-stationary point with total query complexity O(√(nκ)/ε³) — which is absent from most competing black-box prompt methods (BBT, BDPL, SSPT). The analysis is a valid attempt to characterize the alternating algorithm's behavior.

- **Ablation studies systematically isolate each component.** Figures 2 and 3 remove the Gumbel-Softmax trick, the discrete optimization, and the continuous optimization separately, showing that the full ZO-PoG consistently outperforms all ablated variants. This directly supports the claim that the *collaboration* between discrete and continuous optimization is the source of improvement.

- **Clear motivation: addressing suboptimal initialization.** The paper identifies a genuine limitation in BBT (random discrete initialization) and directly addresses it by learning a task-informed discrete distribution before continuous tuning.

## Weaknesses

### Fatal

None.

### Major

- **Unsubstantiated claim of reduced computational expense.** The conclusion (Section 6) states ZO-PoG "reduces the computational expense in the Black-box setting," yet the paper provides **no forward-pass counts, wall-clock times, total query budgets, or any cost comparison whatsoever** between ZO-PoG and the baselines. For a black-box method where query cost is the primary practical concern, this is a significant omission. ZO-PoG runs *I₁* discrete samples + *I₂* ZO perturbations per iteration — two sampling loops — so the natural question is whether the improved accuracy justifies the higher cost. Without cost data, the efficiency claim is unsupported.

### Minor

- **σ_g is undefined in Proposition 1.** The variance bound in Proposition 1 includes the term σ_g², but this quantity is never defined in the paper. The bound itself (O(1/I² + 1/B)) is also stated without derivation. While this does not invalidate the overall convergence argument — a bounded variance assumption is standard, and σ_g could simply be defined as the relevant constant — its absence makes the proposition incomplete as written. The paper should define σ_g explicitly (e.g., a bound on the gradient estimator variance given bounded losses).

- **Some results within one standard deviation of baselines.** The critic correctly notes that on several configurations (e.g., RoBERTa-large, prompt length 20 on SNLI and QNLI), the margins between ZO-PoG and the best baseline are small with overlapping error bars. With only 3 random seeds, the improvement is not always statistically unambiguous. This does not negate the overall trend — ZO-PoG wins on nearly all settings — but the strongest improvement claims would benefit from a significance test or more seeds.

- **Novelty is incremental, not architectural.** The method alternates two established techniques (policy gradient for discrete prompts, ZO gradient for continuous prompts), each applied as in prior work (BDPL, BBT). The contribution is in the combination and the alternating optimization, not in a fundamentally new optimization algorithm. The paper's novelty claim ("the first to jointly optimize") is accurate but modest in scope — this is a sensible engineering integration validated by ablation, not a new class of optimizer.

### Trivial

- The variance bound in Proposition 1 (line 213) contains a formatting error — "‖\underbrace{...}" — that makes the expression difficult to parse. This appears to be a LaTeX rendering issue.

## Nice-to-Haves

- Provide a direct query-efficiency comparison: plot test accuracy vs. number of forward passes for ZO-PoG vs. BBT, BDPL, and SSPT under matched query budgets. This would substantiate (or refute) the computational-expense claim.
- Show the learned discrete tokens qualitatively for different tasks, demonstrating whether the discrete optimization yields interpretable, task-relevant tokens.
- Conduct a sensitivity analysis for key hyperparameters (temperature τ, smoothing μ, subspace dimension d) to guide practical use.

## Removed Points

These points from the reviewer are flagged as invalid or misinformed; they are listed here for transparency but should not be weighed in the decision.

1. **"REINFORCE-type update is not a gradient of L(α,z) but a different object."** — Factually incorrect. The paper (Section 3.2) correctly applies the policy gradient theorem: ∇_{α_i} E_T[L(T)] = E[L(T)∇_{α_i} log P(t_i|α_i)]. The REINFORCE estimator is an *unbiased* estimate of this gradient. The critic confuses the estimator with a fundamentally different object.

2. **"Sub-linear convergence is used imprecisely."** — The paper shows T = O(L_max/ε²), which gives ‖∇L‖² = O(1/T), a standard sub-linear rate in non-convex optimization. This is correct usage.

3. **"CoLA failure on decoder models is acknowledged but not investigated."** — The paper (Section 5.2, lines ~311) provides a specific investigation: it attributes the issue to grammatical acceptability aligning with encoder-only pretraining, and notes that learned prompts may include grammatically incorrect tokens. The critic's claim is false.

4. **"Missing appendix details / hyperparameter values."** — The parser strips appendix sections from all papers; these details exist in the original submission. Algorithm 1 already lists all key hyperparameters as input.

5. **"Ablation charts lack error bars."** — The figures are images; error bars may be present in the original PDF. The parser can strip visual elements.

6. **"The smoothness assumption on L w.r.t. α is unmotivated."** — L(α,z) = E_{T~P(T|α)}[L(f(...))] is an expectation over a Gumbel-Softmax distribution, which is smooth in α (softmax with temperature τ>0). With bounded loss (Assumption 3), the expected loss inherits smoothness under standard regularity conditions. The assumption is standard and well-motivated.

7. **"Variance bound O(1/I²) is wrong — typical is O(1/I)."** — The estimator in Eq. (5) uses a leave-one-out baseline that subtracts the mean of I samples. This specific variance-reduced estimator can achieve O(1/I²) dependence under the given assumptions. Without derivation the bound is opaque, but the scaling is not prima facie wrong.

8. **"Experimental setup is underspecified (d, A, learning rates, etc.)."** — Algorithm 1 explicitly names η_α, η_z, τ, μ, I₁, I₂, B, and d as input parameters. Specific numerical values typically appear in the appendix (stripped by parser) or the provided code repository.

9. **"The paper should do Y / Z unrelated experiments"** — Several suggestions (adding more models, tasks, domains) constitute scope creep. The paper's five GLUE tasks across three model families are a reasonable experimental scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Either remove the computational-expense claim or support it** with forward-pass counts or wall-clock times comparing ZO-PoG to each baseline under matched budgets.
2. **Define σ_g explicitly** in Proposition 1 to complete the variance bound.
3. **Report statistical significance** or run additional seeds (e.g., 5 or 10) to clarify whether the small-margin results are reliable.
4. **Add a qualitative analysis** of learned discrete tokens for a few tasks to illustrate what the discrete optimization captures.

## Score and Decision

This paper presents a sensible combination of two existing black-box prompt optimization techniques, validates it with ablation studies showing the collaboration is the source of improvement, and provides convergence analysis that many competitors lack. The weaknesses are real but manageable: the efficiency claim is unsupported, σ_g is undefined in the theory, and some improvements are small. None of these threaten the core contribution. The paper is a solid, incremental advance that would benefit from stronger cost analysis and theoretical housekeeping.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>