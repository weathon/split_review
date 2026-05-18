Now I have all the information needed to produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the full review.

---

Here is my consolidated review:

## Summary

ODEFormer introduces the first transformer capable of inferring multidimensional ODE systems in symbolic form from a single observed solution trajectory, addressing a gap left by prior univariate-only transformer approaches. The paper also contributes ODEBench, a curated benchmark of 63 ODEs spanning dimensions 1–4. Extensive experiments show ODEFormer achieving state-of-the-art accuracy on both the Strogatz dataset and ODEBench, with substantially better robustness to noise and irregular sampling than existing methods (PySR, SINDy, ProGED, genetic programming baselines), while requiring only seconds for inference versus minutes for most competitors.

## Strengths

1. **First transformer for multidimensional dynamical SR.** The paper explicitly contrasts with prior work (Becker et al., 2023) limited to univariate ODEs, and demonstrates a working system for systems up to dimension 6 at training time and dimension 4 at evaluation. This is a clear advance over the state of the art.

2. **Introduction of ODEBench, a much-needed benchmark.** The paper identifies serious limitations of the existing Strogatz dataset (only seven 2D systems, imprecise integration, misleading annotations) and contributes ODEBench: 63 ODEs (1D–4D) curated from real-world phenomena with two initial conditions each. This is a concrete and reusable contribution that should benefit the community.

3. **Superior robustness to noise and irregular sampling.** In Figure 3, ODEFormer maintains high accuracy as noise (\(\sigma\) up to 0.1) and subsampling (\(\rho\) up to 0.5) increase, while competing methods degrade substantially. The advantage grows with corruption level, which is practically relevant for real-world noisy observational data.

4. **Fast inference.** ODEFormer runs on the order of seconds, versus minutes for all methods except SINDy (Figure 3, right panels). This speed advantage is a practical strength for iterative scientific discovery workflows.

5. **Generalization evaluation.** The paper evaluates on both reconstruction (same initial condition) and generalization (different initial condition), going beyond prior work like ProGED that only reports reconstruction. The generalization results show rankings consistent with reconstruction, demonstrating that ODEFormer's success is not merely memorization of a single trajectory.

6. **Ablation study revealing insensitivity to trajectory length.** Figure 2 shows performance is surprisingly robust to the number of points, which is a useful practical insight for data-scarce settings.

7. **Novel embedding scheme for variable-length, multi-dimensional inputs.** The paper's approach of tokenizing each dimension separately, then using a 2-layer FFN to project back to a single embedding per timestep, allows a single trained model to handle varying trajectory lengths and system dimensionalities.

## Weaknesses

### Major

1. **Mismatch between training operator vocabulary and benchmark operator requirements.** The model is trained on a restricted operator set: unary operators are only {sin, x→x⁻¹, x→x²} and binary operators are only {+, ×}. The decoder vocabulary includes tokens for other operators (e.g., the paper illustrates with `cos`), but the model never sees these during training and **cannot output expressions using them**. Many ODEs in ODEBench and even some in the Strogatz dataset likely use operators outside this vocabulary. Because the evaluation uses only numerical R² (threshold 0.9), a prediction that approximates well numerically using a structurally different expression within the limited vocabulary counts as a "success." This conflates numerical approximation within a restricted function class with discovering the true symbolic form. The paper's lack of explicit acknowledgment of this limitation is a significant oversight — the Discussion section mentions chaotic systems, unobserved variables, and higher-order ODEs but not this operator gap. For the claim of performing "symbolic regression" on these benchmarks to be properly supported, the authors should either (a) report symbolic recovery rates on the subset of benchmarks whose operators are within the training vocabulary, or (b) clearly frame the method as a numerical approximator within a fixed operator set and discuss the implications.

2. **No symbolic correctness metric reported.** The paper evaluates only R² (threshold-based accuracy) and never checks whether the predicted expression is symbolically equivalent to the ground truth. The paper defends numerical evaluation (lines 253–258) on grounds of simplification ambiguity and cases where different expressions yield identical outputs. However, this defense does not justify omitting *any* symbolic analysis: even an imperfect attempt (e.g., `sympy.simplify` on the difference between prediction and ground truth) on the subset where both the prediction and ground truth use the same operators would be informative. The generalization metric mitigates this concern somewhat (a wrong symbolic form is unlikely to generalize to new initial conditions), but the paper itself notes that "consistently across all models, accuracies drop by about half" from reconstruction to generalization (line 378), confirming that many reconstructed expressions are indeed wrong. Without *any* symbolic analysis, the reader cannot assess how often the model recovers the correct symbolic structure versus finding a numerically close proxy. This is a significant gap for a paper whose central claim is about *symbolic* regression.

### Minor

1. **Rescaling procedure fails for zero initial condition components.** The paper rescales \(x_i(t) \to \tilde{x}_i(t) = x_i(t)/x_i(t_0)\) (line 233), which is undefined when \(x_i(t_0) = 0\). Several realistic ODEBench systems likely have zero components in their initial conditions (e.g., the Lorenz attractor with (0,1,0)). The paper does not specify how such cases are handled. While a simple \(\epsilon\)-offset fix exists, this omission leaves a practical gap in the inference pipeline.

2. **The Discussion does not mention the operator vocabulary limitation.** The Discussion section (lines 383–410) covers first-order ODEs, unobserved variables, chaotic systems, and single-trajectory inference, but omits the fact that the model can only output expressions within its training vocabulary. This is a notable gap in the paper's otherwise candid assessment of its own limitations.

### Trivial

None.

## Nice-to-Haves

- **Report symbolic recovery rates** on the subset of ODEBench/Strogatz equations whose operators are a subset of the training vocabulary {+, ×, sin, x⁻¹, x²}. If high, this would strongly support the symbolic regression claim. Even reporting the proportion of benchmarks that *can* be expressed within the training vocabulary would clarify the scope.
- **Separate performance** for benchmarks whose operators match vs. do not match the training vocabulary, to show whether the aggregate results are driven by approximable systems or genuinely matching ones.
- **Handle zero initial conditions** in the rescaling procedure, either via an \(\epsilon\) offset or a different normalization scheme (e.g., divide by range rather than by initial value).
- **Analyze chaotic vs. non-chaotic systems separately**, since the R² threshold may be too strict for chaotic systems where trajectories diverge exponentially under small symbolic errors. The paper already notes that chaotic systems are challenging (line 399) but could provide a separate breakdown.

## Removed Points

- **Criticism about "the paper does not discuss the effect of training data filtering on performance for simple systems (e.g., exponential decay)."** The paper explicitly discusses filtering out rapidly converging systems with 90% probability (lines 176–184) and shows the impact of dimensionality/complexity in the ablation study (Figure 2). The reviewer's request for a deeper per-equation-type analysis is a Nice-to-Have, not a weakness with the submitted content.
- **Criticism about chaotic systems using the same R² metric.** The paper already acknowledges that it "struggles with chaotic systems" (line 399) and discusses why chaotic systems are challenging (lines 399–401). The reviewer's suggestion of a separate analysis is a Nice-to-Have.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the generalization evaluation (unobserved initial conditions) reveals that roughly half of reconstructed ODEs are incorrect symbolically, even when they achieve R²>0.9 on the observed trajectory. The paper itself reports this (line 378) but does not fully interrogate what it implies about the limitations of single-trajectory identifiability. This finding, if analyzed more deeply, could motivate the field to move toward multiple-trajectory settings — a direction the paper mentions for future work.

## Suggestions

1. **Explicitly acknowledge and analyze the operator vocabulary limitation.** Report which fraction of benchmark systems can be expressed within the training vocabulary, and show symbolic recovery rates on that subset. If the rate is high, this directly strengthens the paper's claims; if low, honestly discuss this as a boundary of the method.

2. **Add a separate analysis** of reconstruction vs. generalization accuracy for equations whose operators are within the training vocabulary, versus those that require out-of-vocabulary operators. This would clarify whether the model's apparent success comes from genuine symbolic discovery or numerical approximation.

3. **Fix the rescaling procedure** to handle zero-valued initial conditions (e.g., by adding a small \(\epsilon\) or using a range-based normalization).

4. **Mention the operator vocabulary limitation in the Discussion** section alongside the other acknowledged limitations.

## Score and Decision

The paper makes a genuine contribution: it is the first transformer-based method for multidimensional dynamical symbolic regression, it introduces a much-needed benchmark, and it demonstrates strong empirical performance with practical speed and robustness advantages. However, the gap between the claimed contribution ("symbolic regression" of a system) and the evaluation (purely numerical R² with an operator vocabulary that does not match many benchmarks) is substantial enough that the paper's central claim is not fully supported in its current form. The weaknesses are addressable (adding symbolic recovery analysis on the matching subset and acknowledging limitations), but they require meaningful additions, not just clarifications.

I assign a score of **6.0** — a solid contribution that needs substantial revision to properly support its claims, particularly regarding what kind of "symbolic regression" is being performed and evaluated.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>