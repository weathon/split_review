## Summary

This paper introduces conceptor theory (Jaeger, 2014) — originally from reservoir computing — to LLM activation steering. The authors derive closed-form linear and affine projection matrices (conceptors) as solutions to a regularized MSE minimization objective, and show that these conceptor-based steering functions outperform traditional additive steering vectors on six function-vector tasks (antonyms, present-past, English-French, singular-plural, country-capital, capitalize) and three composite functions, across GPT-J (6B) and GPT-NeoX (20B). The paper further applies Boolean composition operations (AND, OR, NOT) on conceptor matrices to combine multiple steering objectives.

## Strengths

- **Closed-form optimal linear and affine steering solutions derived from first principles (Propositions 1 and 2, Eqs. 11–13).** The paper formulates steering as minimization of an MSE-plus-regularization objective and obtains unique closed-form conceptor matrices expressible solely in terms of concept-conditional second-moment/covariance and the aperture α. This goes beyond prior additive steering methods, which relied on heuristic averages of activation vectors without a provably optimal criterion. The solutions connect to an existing body of conceptor theory, lending them mathematical grounding.

- **Conceptor steering consistently outperforms additive steering on all six function tasks across two model scales (Figure 2, Section 4.1).** The paper reports that conceptor-based steering achieves higher accuracy than additive steering (the baseline from Todd et al., 2024) on every evaluated task for both GPT-J and GPT-NeoX across the majority of layers. This provides direct evidence that the proposed method delivers better empirical performance than the prior standard on the tasks tested.

- **Boolean AND composition of conceptors outperforms arithmetic-mean combination of steering vectors on composite functions (Figure 3, Section 4.2).** When combining two individual steering objectives into a composite one, the AND operation on conceptor matrices yields higher accuracy than the standard approach of averaging steering vectors. This demonstrates a principled compositional advantage that goes beyond vector arithmetic.

- **Systematic comparison across four method variants.** Table 1 provides head-to-head accuracy numbers for linear conceptors, affine conceptors, additive vectors, and mean-centered additive vectors on the same six function-vector tasks using GPT-J, enabling clean ablation of the contribution of each component.

## Weaknesses

### Fatal

None.

### Major

- **Gap between the "provably optimal" theoretical form and the actual implemented form (Section 3 vs. Section 2.3–2.4).** The theoretical derivation gives the steering function as a direct projection: linear case \(f_c(\mathbf{H}) = C\mathbf{H}\) (with \(C = \tilde{\Sigma}_c(\tilde{\Sigma}_c + \alpha^{-2}I)^{-1}\)), affine case \(f_c(\mathbf{H}) = C(\mathbf{H} - \mu_c) + \mu_c\). However, the actual implementation (Eqs. 16–17) uses a *residual* form with an extra hyperparameter \(\beta_c\):

  \[
  f_c(h_\ell) = h_\ell + \beta_c C_\ell h_\ell \quad\text{(linear)},\qquad
  f_c(h_\ell) = h_\ell + \beta_c(C_\ell(h_\ell - \mu_c) + \mu_c) \quad\text{(affine)}
  \]

  The paper states "We empirically found that the conceptor-based steering method works best if it acts additively on the residual stream" (Section 3, line 224) — acknowledging that the theoretically derived form underperforms in practice. This means the empirical results may reflect the residual formulation plus careful \(\beta_c\) tuning rather than the theoretical framework, and the paper provides **no ablation** comparing the direct theoretical form against the residual form. Without this comparison, the reader cannot determine whether the "provably optimal" derivation is driving the results or whether the ad-hoc residual modification is responsible. This directly undercuts the paper's headline claim of provably optimal steering.

- **Results reported as "best performance across all hyperparameters and across all layers" (Table 1 caption, line 256).** Reporting the maximum accuracy over all hyperparameter choices and all layers is an optimistic upper bound that does not reflect what a practitioner could achieve with a held-out validation set. This inflates the apparent advantage and is not a standard evaluation practice. The paper should report results from a proper train/validation/test split (or at minimum, report per-layer results with a fixed hyperparameter selection procedure).

### Minor

- **Proposition 2 (affine conceptor) lacks a proof.** The derivation is referenced only as "Proof.1" (line 215) with no supporting detail. The change in the regularization coefficient from \(\alpha^{-2}\) (linear case) to \(2\alpha^{-2}\) (affine case) is not explained, making the derivation opaque. A skeptical reader cannot verify that the claimed optimal affine solution is correct without reconstructing the proof themselves.

- **No standard deviations or confidence intervals reported despite 5 runs with different seeds.** The paper states (line 249) that experiments are repeated 5 times and results are averaged, but never reports variance. This makes it impossible to assess the statistical significance of the observed improvements.

- **No comparison with non-additive steering baselines.** The paper compares only against additive steering vectors. Established alternative methods such as Inference-Time Intervention (Li et al., 2023), optimized steering vectors (Cao et al., 2024), or other linear probe based interventions are not compared, leaving open the question of whether conceptor steering outperforms a broader set of approaches.

- **The "inherently adaptive" claim in the conclusion (Section 5, line 270) is asserted without experimental support.** The paper claims that "activations residing within the conceptor's region would experience minimal change whereas activations outside of the conceptor's region experience a more substantial shift" — a concrete, testable prediction that no experiment validates. Similarly, the claim that the conceptor matrix can be fused with attention head weights "to not impact model latency" (line 272) is mentioned without any timing or computational-cost measurements.

- **No sensitivity analysis of the aperture parameter α.** The conceptor's aperture α is a key parameter controlling the trade-off between signal preservation and regularization, but the paper provides no ablation or guidance on how to select α for different tasks or layers.

### Trivial

- "across across" (line 249) — duplicated preposition.
- The section numbering has minor inconsistencies (e.g., "3.1" and "3.2" appear as spurious suffixes in body text, suggesting cross-reference artifacts).
- The sentence at line 254 has a dangling superscript "5" ("most layers.5.") — likely a footnote reference that lost its rendering.

## Nice-to-Haves

- A head-to-head comparison against Singh et al. (2024)'s guarded affine steering functions would directly demonstrate the benefit of relaxing the guardedness constraint and clarify the paper's claimed improvement over prior theory.
- An ablation comparing the direct theoretical form \(f_c(h) = C h\) against the residual form \(h + \beta C h\) (with and without \(\beta\) tuning) would resolve the central ambiguity about whether the results are driven by the theory or the engineering adaptation.
- Standard deviations or confidence intervals on the accuracy numbers would allow assessment of statistical reliability.
- Measuring the actual computational overhead (in FLOPs or wall-clock time) of conceptor steering vs. additive steering would help practitioners evaluate the trade-off.

## Removed Points

The following points from the input reviews were removed after verification:

- **"The 'optimal' claim is overblown because the objective is reconstruction error, not downstream steering quality."** — Removed as a standard framing issue. Every optimization-based method in ML uses a proxy objective; the paper defines "optimal" with respect to its stated objective, which is standard practice. The criticism would apply to virtually any method that optimizes a tractable proxy rather than the ultimate evaluation metric.
  
- **"Evaluation is too narrow (missing sentiment, truthfulness, bias, safety, multi-turn dialogue)."** — Removed as scope creep. The paper explicitly focuses on function-vector tasks (Todd et al., 2024) and in-context learning, which is a well-defined subdomain of activation steering. The abstract and claims are appropriately scoped to "in-context learning tasks."
  
- **"The 99% mean-centering improvement is unexplained / extraordinary."** — Removed. The paper clearly attributes this to mean-centered additive steering (Jorgensen et al., 2023b) on the country-capital task. Large relative improvements are possible when baseline accuracy is low, and the paper's framing is about additive steering (not conceptor steering) in that sentence.
  
- **"The residual formulation is an ad-hoc modification."** — Kept but contextualized. The criticism is valid that the residual form diverges from the theory, but calling it "ad-hoc" is the authors' own description ("We empirically found..."). This is transparency, not concealment. I have kept the substantive concern as a Major weakness about the missing ablation, not about the modification itself.

## Novel Insights

None beyond the paper's own contributions. The key observation — that conceptor matrices from reservoir computing can be applied to LLM activation steering and outperform additive vectors on function-vector tasks — is the paper's original contribution, not something the reviewers discovered.

## Suggestions

1. **Run an ablation comparing the direct theoretical form against the residual form.** This is the single most important addition. Show results for \(f_c(h) = C h\) vs. \(h + \beta C h\) (with β=1 and β tuned) on at least a subset of tasks. If the residual form is necessary for good performance, explain *why* — this could actually deepen the contribution by revealing something about how transformers encode concepts in the residual stream.

2. **Provide the proof of Proposition 2** (or a clear citation to where it can be found). The change from α⁻² to 2α⁻² in the affine case is non-trivial and should be derived or explained.

3. **Report variance** (standard deviations or confidence intervals) over the 5 random seeds.

4. **Adopt a proper evaluation protocol**: select hyperparameters (including β and α) on a validation split and report test-set results, rather than reporting the best over all hyperparameters and layers.

5. **Add a sensitivity analysis** for the aperture parameter α across tasks and layers.

6. **Either test the "adaptive steering" claim** with an experiment measuring activation change magnitude as a function of distance from the conceptor region, or remove the claim as speculation.

## Score and Decision

**Score: 5.0** — A marginally below-acceptance submission. The idea of applying conceptor theory to LLM activation steering is genuinely interesting and the closed-form derivations are a meaningful step beyond purely heuristic additive steering. The empirical results on function-vector tasks are promising. However, the major gap between the theoretically "optimal" form and the empirically deployed residual form — coupled with the lack of an ablation to bridge them — undermines the paper's central claim. The evaluation protocol (reporting best over all hyperparameters and layers without proper validation) further weakens the evidence. These are fixable issues, but in their current state the paper does not convincingly demonstrate that the theoretical framework (rather than the engineering adaptation) drives the reported improvements. The paper would benefit from one round of substantial revision to align theory with practice and adopt standard evaluation practices.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>