Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper provides a theoretical analysis of the training dynamics and in-context learning (ICL) generalization of a **one-layer Mamba model** (simplified via standard assumptions including \(\mathbf{A}=-\mathbf{I}\) to a gated linear attention form) on binary classification tasks with additive outliers. It proves convergence bounds (Theorem 1) and generalization guarantees for distribution-shifted outliers (Theorem 2), characterizes how the linear attention selects relevant patterns while the nonlinear gating suppresses outliers and induces a local bias (Corollaries 1–2), and compares with one-layer linear Transformers (Theorems 3–4), claiming Mamba tolerates a higher outlier fraction. Synthetic experiments support the theoretical predictions and extend to three-layer models.

## Strengths

- **First theoretical analysis of training dynamics for a one-layer Mamba-derived model in ICL with outliers.** The paper provides explicit convergence and sample-complexity bounds (Theorem 1, Equations 8–10) and generalization guarantees under distribution-shifted outliers (Theorem 2, Equations 12–13). No prior work has provably characterized the training dynamics of this architecture class in the ICL setting.

- **Clean mechanistic characterization of how gating enables outlier suppression.** Corollaries 1 and 2 prove that the linear attention selects context examples sharing the query's relevant pattern, while the nonlinear gating suppresses outlier-containing examples (Equation 17) and induces an exponential decay in importance with index distance from the query (Equation 18). These predictions are experimentally verified in Figures 3 and 4.

- **Quantitative comparison of training requirements between Mamba and linear Transformers.** Theorems 1 and 3 give explicit conditions on batch size, iterations, and prompt length for both architectures, showing that Mamba requires larger batch sizes (\(B \geq B_M\) vs. \(B_T\)) and more iterations (\(T_M = \Theta(l_{tr}) T_T\)) but that this additional training cost yields robustness gains — a nuanced trade-off derived from the model structure.

- **Multi-layer experimental validation.** Section 4.2 extends the one-layer theory to three-layer architectures, confirming that the attention selection and gating patterns hold in deeper models (Figures 3, 4) and revealing the positional sensitivity of Mamba to outliers (Table 1), consistent with the local-bias mechanism in Corollary 2(ii).

- **Flexible test-time outlier model.** Theorem 2 allows test-time outliers to be positive linear combinations of training outliers (Equation 11) with an orthogonal additive component, and the labeling function can be any deterministic or stochastic mapping (Definition 2), capturing scenarios like the data-poisoning example in Figure 1.

## Weaknesses

### Fatal
None.

### Major

1. **The model studied is a simplified proxy whose connection to the full Mamba architecture is not empirically validated.** The paper derives equation (3) from the Mamba recursion under specific assumptions (\(\mathbf{A} = -\mathbf{I}\), specific discretization choices detailed in Appendix E.1). While mathematically valid, the resulting model is a gated linear attention mechanism. The paper's title, abstract, and contributions frame the work as analyzing "Mamba," but the experiments exclusively use equation (3) rather than an actual Mamba implementation (Gu & Dao, 2023). There is no experimental comparison between equation (3) and the full Mamba architecture on the same tasks to validate that the simplification preserves the relevant ICL and robustness behavior. This gap means the paper's theoretical conclusions are rigorously established only for the simplified gated linear attention model, not necessarily for Mamba as deployed in practice.

2. **The test-time outlier condition is restrictive.** Theorem 2, Condition (a), requires every test-time outlier to belong to the set \(\mathcal{V}' = \{v \mid v = \sum_{i=1}^V \lambda_i v_i^* + u,\ \sum_{i=1}^V \lambda_i \geq L > 0,\ u \perp \ldots\}\) (Equation 11). While the orthogonal component \(u\) provides flexibility, the \(\lambda\) component of the outlier must lie in the cone spanned by training outlier patterns with a strictly positive sum of coefficients. This excludes test-time outliers whose projection onto the training-outlier span has a non-positive sum of coefficients — for example, a new outlier pattern that is negatively correlated with the training outliers. The paper claims this "captures a wide range of possible outlier patterns," but the range of undetectable outliers (those failing the positive-sum condition) is substantial and not characterized. Without this condition, the gating mechanism (which depends on \(\mathbf{w}^\top \mathbf{p}_i\)) may not suppress the outlier, so the robustness guarantee is contingent on an assumption that is not justified as realistic.

3. **Mamba's robustness is highly position-dependent, a significant limitation not reflected in the headline claims.** Table 1 shows that when outliers are placed closest to the query (CQ), Mamba's accuracy drops to 82.73% (vs. 93.96% for linear Transformers), while Mamba excels when outliers are far from the query (FQ: 99.73%) or at random positions (R: 99.67%). The paper correctly notes this is consistent with the exponential-decay mechanism in Corollary 2(ii), but this finding substantially qualifies the claim that "Mamba maintains accurate ICL generalization even when the fraction of outlier-containing context examples approaches 1." Robustness is contingent on outlier placement, and an adversary who controls positioning can severely degrade Mamba's performance while leaving linear Transformers largely unaffected.

### Minor

1. **The comparison with linear Transformers is based on sufficient conditions, not tight bounds.** The paper explicitly states (line 191) that "the comparison is made between sufficient conditions for the desired generalization," and Remark 6 acknowledges that large Transformers can achieve robustness. However, the headline claim ("Mamba can tolerate \(\alpha\) close to 1 while linear Transformers cannot exceed \(1/2\)") is stated as a crisp comparative finding. Theorem 4's \(\alpha < 1/2\) condition is a sufficient condition for the linear Transformer's generalization — the paper does not prove it is necessary. Without necessity, the claimed superiority is not rigorously established as a property of these architectures rather than of the specific sufficient analyses employed.

2. **The "\(\alpha\) goes to 1" claim is context-dependent.** The theoretical bound gives \(\alpha < \min(1, p_a \cdot l_{tr}/l_{ts})\). In the experiments (\(p_a=0.6\), \(l_{tr}=l_{ts}=20\)), this gives \(\alpha < 0.6\), yet experiments show good performance up to \(\alpha \approx 0.8\). While this suggests the sufficient condition is conservative, it also means the "\(\alpha \to 1\)" framing requires \(p_a \cdot l_{tr} \geq l_{ts}\), which is not highlighted. The experimental performance at \(\alpha=0.8\) exceeds the theoretical guarantee.

3. **No ablation isolating the gating mechanism's contribution.** The paper compares Mamba (gating + linear attention) to a linear Transformer (no gating). An additional ablation — e.g., removing the gating from the Mamba model (setting \(G_{i,l+1}=1\)) while keeping the same architecture otherwise — would more cleanly isolate the gating effect within the same model class. The cross-architecture comparison conflates architectural differences beyond gating.

4. **The upper bound on \(l_{tr}\) in Theorem 1 Condition (iii) is not explained.** The bound \(p_a^{-1}\,\text{poly}(M_1^{\kappa_a}) \gtrsim l_{tr}\) is nontrivial and its technical origin is not discussed in the main text. It is unclear whether this upper bound is a meaningful practical constraint or an artifact of the proof technique.

### Trivial

None that pass the filtering criteria. Minor notational density is standard for theory papers of this type.

## Nice-to-Haves

- An experiment running the actual Mamba architecture (Gu & Dao, 2023) on the same synthetic tasks to validate whether the simplified model (3) faithfully reproduces Mamba's ICL and robustness behavior.
- An ablation where the gating is removed from the Mamba model (i.e., \(G_{i,l+1}=1\)) to isolate the gating effect within the same architecture.
- A discussion of whether the sufficient conditions in Theorems 2 and 4 are tight or can be made necessary under the same data model.
- Exploration of whether the position-sensitivity issue (CQ failure) can be mitigated by architectural modifications (e.g., position-aware gating).

## Removed Points

These points from the reviews were checked against the paper and removed with justification:

1. **"The derivation from (1) to (3) relies on assumptions that are not justified in the main text"** — Removed. The paper explicitly states "Following the assumption in Theorem 1 of (Gu & Dao, 2023), we select \(\mathbf{A} = -\mathbf{I}_m\) for simplicity of analysis" (line 59) and the derivation is in Appendix E.1. This is standard practice for theory papers.

2. **"The resulting model is no longer Mamba; it is a gated linear attention"** — Partially removed. While the model is a simplified form, the paper transparently derives it from the Mamba recursion under stated assumptions. The paper IS analyzing what it claims: a one-layer Mamba with \(\mathbf{A}=-\mathbf{I}\). The concern about empirical validation is kept in Major weakness 1.

3. **"The paper does not compare with other SSMs like S4, H3"** — Removed. The paper's comparison is intentionally designed to isolate the effect of gating vs. no gating. Adding S4/H3 comparisons would be scope creep and does not weaken the paper's core contribution.

4. **"The paper does not provide any experiments on real-world data"** — Removed. The main text focuses on synthetic experiments matching the theory, which is standard. The paper references real-world data experiments in Appendices B.1 and B.2 (stripped by parser).

5. **"The paper does not provide intuitive explanation of how outliers are detected"** — Removed. Corollary 2 and the surrounding discussion (including Remarks 7–8) explain how \(\mathbf{w}^\top\mathbf{p}_i\) detects outliers: the gating values become very small for outlier-containing examples.

6. **"The paper lacks discussion of limitations"** — Removed. Section 5 and Remark 6 acknowledge the one-layer scope and note that large Transformers can achieve robustness. While a more thorough limitations section would strengthen the paper, the claim that it is entirely absent is false.

7. **Critique about experimental evidence for the simplified model approximating real Mamba** — Demoted from the harsh critic's "fatal/structural" framing to Major weakness 1. The concern is valid but the paper is transparent about its assumptions, so it is not a fatal misrepresentation.

## Novel Insights

A genuinely novel observation emerges from synthesizing the reviews: the **position-dependent robustness** finding (Table 1 CQ case) reveals that Mamba's gating mechanism — which the paper presents as a pure strength — is a double-edged sword. The exponential-decay local bias (Corollary 2(ii)) that suppresses distant clean examples when outliers are placed near the query creates a failure mode that linear Transformers, which lack this position-dependent mechanism, do not suffer from. This suggests the architectural advantage of gating for outlier robustness is contingent on the assumption that outliers are not adversarially positioned, which the paper's framing does not adequately caveat.

## Suggestions

1. **Clarify the scope of the claims.** The paper should more clearly distinguish between results proven for the simplified model (gated linear attention derived from Mamba with \(\mathbf{A}=-\mathbf{I}\)) and claims about the full Mamba architecture. Consider either (a) running experiments on the actual Mamba architecture to validate the simplification, or (b) reframing the paper's title and contributions to reflect that the analysis targets the gated linear attention model that arises from a one-layer Mamba under specific assumptions.

2. **Characterize the position-sensitivity limitation more prominently.** The CQ failure case (Table 1) should be discussed in the abstract or introduction as a qualifier on the robustness claims, not relegated to the end of Section 4.2.

3. **Discuss the restrictiveness of the test-time outlier condition.** The paper should explicitly characterize the space of outliers not covered by Condition (a) of Theorem 2 and discuss whether the positive-sum constraint is a necessary condition for the proof or could be relaxed.

4. **Acknowledge the sufficient-condition limitation in the comparative claim.** The paper's current phrasing (e.g., "linear Transformers can only tolerate \(\alpha < 1/2\)" in the abstract) reads as a proven architectural limitation. Adding caveats that this is derived from a sufficient condition, not a necessary one, would improve intellectual honesty.

5. **Add the gating-only ablation.** An experiment with the gating fixed to 1 within the Mamba architecture (i.e., removing the gating mechanism while keeping everything else identical) would cleanly demonstrate that the observed robustness advantage is attributable to gating rather than other architectural differences.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>