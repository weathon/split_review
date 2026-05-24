Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper proves that causal decoder-only Transformer language models are *almost surely injective* — distinct prompts produce distinct last-token hidden representations — using real-analyticity arguments. The authors prove this property at initialization, sketch an argument that it is preserved under training, and provide large-scale empirical validation (billions of pairwise comparisons across six models, finding zero collisions). They further introduce SIPIT/SIFT, an algorithm that exploits injectivity to recover the exact input text from per-position hidden states with provable linear-time guarantees and demonstrate 100% accuracy in practice. The paper connects these technical findings to data-protection implications.

## Strengths

1. **Novel theoretical framing of injectivity via real-analyticity.** The core insight — that Transformer components are real-analytic functions, so collisions between prompts are confined to measure-zero parameter sets — is elegant and yields a clean proof of almost-sure injectivity at initialization (Theorem 2.2). This meaningfully extends prior work (Sutter et al. 2025) by focusing on *last-token* representations and the *parameter-to-function* map rather than the entire hidden matrix.

2. **Massive-scale empirical validation with zero collisions.** The paper conducts ~5 billion pairwise comparisons across six diverse models (GPT-2, Gemma-3, Llama-3.1, Mistral, Phi-4, TinyStories) at multiple layers. Minimum pairwise distances are far above any plausible collision threshold (e.g., 0.001 to 9.02), convincingly demonstrating that injectivity holds in practice for trained models. The analysis across depth (Figure 3), quantization (Tables 2, 3), and sequence length (Figure 5) is thorough.

3. **First provable exact inversion algorithm from hidden states.** SIPIT exploits causal structure and injectivity to recover prompts token-by-token with 100% accuracy, exploring <0.22% of the vocabulary on average (Table 4). The gradient-guided candidate policy is nontrivial and makes the algorithm practical. The comparison against HARDPROMPTS (which achieves 0% accuracy) honestly demonstrates the advantage of having provable guarantees.

## Weaknesses

### Major

- **Theorem 2.3 (training preservation) proof is incomplete in the main text.** The argument requires showing that $\det D\phi(\theta) = \det(I - \eta \nabla^2 \mathcal{L}(\theta))$ is **not identically zero** — otherwise the Jacobian could vanish on a set of positive measure, breaking the absolute-continuity argument. The paper merely asserts "one can check this by evaluating at a simple parameter setting" without providing even a sketch of such a setting. Given that the Hessian depends on the full architecture, training data, and loss, this verification is nontrivial. The full proof is deferred to the appendix (which is stripped), so it cannot be assessed. This gap undermines the paper's central claim that injectivity holds "throughout training."

- **Corollary 2.3.1 (SGD/mini-batch) contains a mathematical error.** The proof claims that at a point $\theta_*$ where the single-sample Jacobian determinant is "sample-independent and nonzero," the batch Jacobian $I - \eta \frac{1}{|B|} \sum_i H_i(\theta_*)$ coincides with the single-sample one "by linearity of differentiation." This is not justified: the batch Jacobian is the average of individual Hessians, and there is no reason this average equals any individual $I - \eta H_i(\theta_*)$ at the same $\theta_*$, let alone that its determinant remains nonzero. Even if each $I - \eta H_i(\theta_*)$ is nonsingular, a convex combination could accidentally have an eigenvalue $1/\eta$. This is a genuine gap in the proof.

- **The title and framing overclaim relative to what is proven.** The title "Language Models are Injective" is broader than the actual result, which applies to causal decoder-only Transformers with real-analytic activations. Non-causal architectures (BERT, T5), models with ReLU activations, and quantized models (where the theory technically fails) are covered but the title does not reflect these restrictions. The legal/privacy framing in Section 6 (hidden states = "verbatim text") outruns the demonstrated attack, since SIPIT requires access to *per-position* states at a chosen layer — a much stronger assumption than having only the last-token representation, which the injectivity theorem actually addresses.

### Minor

- **The proof sketch of Theorem 2.2 is imprecise.** The construction uses language like "set one attention head so that the last position attends *almost entirely* to $i^*$," which suggests a limit behavior not obviously realizable with finite parameters (softmax cannot produce an exact delta). The full proof is in the appendix, so this is a presentation gap rather than a fatal error, but the main-text sketch should be more precise.

- **SIFT/SIPIT naming inconsistency.** The abstract and experimental section refer to "SIFT," while Section 3 introduces the algorithm as "SIPIT" (Sequential Inverse Prompt via ITerative updates). This inconsistency suggests hasty writing and should be resolved.

- **The threat model for inversion is under-defined.** The paper states "we do not define a full adversarial model" and assumes access to per-position states at a chosen layer. This makes the strong privacy/legal claims in Section 6 difficult to evaluate — the gap between "injective in theory from the last-token state" and "practically recoverable from per-position states" is acknowledged but not bridged.

### Trivial

- None beyond the naming inconsistency noted above.

## Nice-to-Haves

- **Direct experimental test of training preservation.** The paper could measure pairwise distances at multiple checkpoints during training (or simulate gradient steps from random initialization on a small model) to empirically validate that injectivity persists throughout training. This would strengthen the weakest link in the theoretical narrative.

- **Clarify scope of applicability upfront.** The assumptions (causal decoder-only, real-analytic activations) are currently revealed gradually; stating the exact model class at the start of Section 2 would improve reader comprehension.

- **Provide a concrete parameter construction for the separation argument** in Theorem 2.2's sketch, rather than the informal "almost entirely" language.

## Removed Points

The following points from the input reviews were identified as unreliable, factually incorrect, or not applicable to this paper:

1. **Criticism about the Jacobian determinant verification being an impossible gap.** The harsh critic claimed this is a "substantive gap that undermines the paper's central claim" and that the absolute-continuity preservation argument needs a properness condition. **Reason for removal:** The critic's claim that more than the Inverse Function Theorem is needed to preserve absolute continuity under pushforward is incorrect for C^1 maps with nonvanishing Jacobian a.e. — the standard change-of-variables / area formula suffices. The "not identically zero" verification is indeed missing from the main text, but this is already captured as a Major weakness above without overstating it as fatal.

2. **Criticism about the 10⁻⁶ collision threshold being arbitrary.** **Reason for removal:** The minimum distances reported (0.001 to 9.02) are so far above 10⁻⁶ that the threshold choice is irrelevant. The critic acknowledges this: "the results are convincing." This is a nitpick that does not affect the conclusions.

3. **Criticism about methods comparison with HARDPROMPTS being unfair.** **Reason for removal:** The paper explicitly acknowledges the difference in setting and still presents the comparison with appropriate caveats. The comparison shows HARDPROMPTS achieves 0% accuracy on this task, which is a factually correct result.

4. **Criticism about not testing models at initialization or during training.** **Reason for removal:** The claim "injectivity holds after training" is tested by measuring collisions on trained models. The critic wants a more granular test (checkpoints), but the empirical validation is consistent with and supports the theoretical claim. This is a nice-to-have extension, not a missing essential experiment.

5. **Criticism about Theorem 3.2's robustness bound being "trivial."** **Reason for removal:** The bound correctly characterizes the noise tolerance of nearest-neighbor recovery in terms of the minimum inter-token distance. While elementary, it provides a formal guarantee and is standard for such settings.

## Novel Insights

The harsh critic's observation about the Corollary 2.3.1 error is genuinely insightful — the claim that the batch Jacobian "coincides with the single-sample one by linearity of differentiation" is mathematically unsound, as linearity gives the gradient as an average but the Jacobian of the gradient is the Hessian, and averaging Hessians does not preserve individual Hessian properties. This is a distinct and more subtle issue than the training-preservation gap, and it would likely escape a casual reading. The authors should either provide a different argument for stochastic updates (e.g., showing that each batch update map also has non-identically-zero Jacobian by a direct construction) or restrict the claim to full-batch GD.

## Score and Decision

### Calibration

**Round 1 — Bracketing (all queries: "theoretical analysis of transformer architectures showing injectivity or information preservation"):**
- Weak anchors (<3.5): range 1.50–3.33 — papers with weak or flawed theoretical analyses
- Middle anchors (3.5–7.5): range 4.00–7.00 — includes both rejected (4.0–4.5) and accepted (5.5–7.0) papers
- Strong anchors (>7.5): range 8.00–8.50 — top-tier theoretical contributions

Initial bracket: **4.5–6.5**. The paper has real contributions and strong experiments, ruling out the <4.5 range, but its theoretical gaps and overclaiming rule out the >6.5 range.

**Round 2 — Narrowing:**
- Induction Head paper (`m4ESoE5wnZ`, avg 4.50, Reject): purely constructive theory with minimal experiments. **Current paper is significantly stronger** — it has extensive experiments and a more rigorous theoretical framework.
- Signal Propagation paper (`utSqpxQHXq`, avg 6.00, Accept): complete theoretical analysis with some empirical validation. **Current paper is weaker** — it has stronger experiments but the training preservation theory is incomplete and Corollary 2.3.1 has an error.
- Multi-Index Models paper (`2Q0U2rV2Jz`, avg 5.50, Accept): solid theory with idealized assumptions and no validation. **Current paper is comparable** — stronger in empirical validation but weaker in theoretical rigor.
- Readout Representation paper (`pODHH9DLeA`, avg 6.00, Accept): methodological contribution with experimental validation. **Current paper is comparable or slightly weaker** due to the theoretical gaps.

Narrowing to **5.0–5.5**. The paper is meaningfully above a rejected 4.5 paper (induction head) but below a solid 6.0 accepted paper (signal propagation) due to the incomplete training preservation proof and the SGD corollary error. It sits alongside or slightly below the 5.5 multi-index paper.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>