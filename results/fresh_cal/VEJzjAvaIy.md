Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper studies whether the empirical Neural Tangent Kernel (NNK) converges uniformly to the limiting NTK during training under cross-entropy loss in classification problems. The paper claims two main results: (1) strict positive definiteness of the NTK for multi-layer fully-connected and residual networks with bias terms (Proposition 1), and (2) a proof by contradiction showing that if NNK converged uniformly to NTK, then the network outputs would diverge, which in turn would make the NNK diverge — contradicting the boundedness implied by convergence, hence uniform convergence fails (Theorem 2). The paper provides a proof sketch and supporting experiments on synthetic data and MNIST.

## Strengths

1. **Well-motivated and clearly framed question.** The paper asks a precise theoretical question — whether NTK convergence, well-established for MSE regression, holds under cross-entropy classification — and correctly identifies this as an open problem. The contrast between regression (where uniform convergence holds) and classification is clearly drawn in Sections 1 and 4.

2. **Theorem 1 and the dynamical equation are correctly derived.** The derivation leading to the dynamics of \(V_t\) in equation (5.4) and the monotonicity argument showing \(u(t)\to 0\) and \(|f_t(x_i)|\to\infty\) under a positive lower bound on the NNK's minimal eigenvalue is sound. The gradient flow equation (3.2) connecting the NNK to output dynamics is clearly presented.

3. **Experimental results are qualitatively consistent with the claim.** Figures 1–4 show that in practice the NNK does not stabilize during training; Figure 2 confirms NTK convergence at initialization, while Figures 3–4 show NNK values diverging during training under cross-entropy. This provides empirical support for the paper's qualitative thesis.

4. **The paper explicitly addresses bias terms in the NTK analysis.** Proposition 1 claims to extend prior strict-positive-definiteness results to networks with bias terms, which is a nontrivial extension needed for the argument.

## Weaknesses

### Fatal

None.

### Major

1. **The central link between function divergence and kernel divergence is missing from the proof sketch.** This is the critical gap. In Section 5, after establishing that \(|f_t^{\mathrm{NN}}(x_i)|\to\infty\) (equation 5.5), the paper states: "Combined with the specific network structure, we can derive that \(\lim_{t\to\infty} \sup_{x,x'\in\{x_i\}_{i=1}^n} |K_t^m(x,x')|\to\infty\)" — with no derivation, equation, or argument. The NNK \(K_t^m(x,x') = \langle\nabla_\theta f(x), \nabla_\theta f(x')\rangle\) could in principle stay bounded, grow, or even shrink depending on how parameters evolve and how gradients align, even if outputs diverge. This step is the heart of the contradiction argument — without it, Theorem 2 is unsubstantiated.

2. **Mismatch between the stated quantitative bound and the proof sketch.** Theorem 2 claims a specific quantitative lower bound \(\lambda_0/(2n^2)\) on the supremum gap between NNK and NTK. However, the proof sketch in Section 5 only argues for qualitative divergence (\(|K_t^m| \to \infty\)) and never derives or even mentions the constant \(\lambda_0/(2n^2\). The bound appears in the theorem statement without any supporting calculation. If the bound is meaningful, it needs to be derived; if it is arbitrary, it should be removed.

3. **Theorem 2's FC statement lacks an explicit quantifier.** For the fully-connected case, the theorem reads \(\sup_{t\ge 0}|K_t^{\mathrm{FC}}(x,x')-K^{\mathrm{FC}}(x,x')|\ge \lambda_0/(2n^2)\) without specifying whether this holds "for all \(x,x'\)" or "there exists \(x,x'\)." The ResNet case explicitly says "there exists \(x,x'\)." This imprecision in a theoretical paper is concerning and makes the FC claim ambiguous.

### Minor

1. **Relationship to implicit bias literature is not discussed.** Theorem 1's conclusion that \(|f_t(x_i)|\to\infty\) under a positive-min-eigenvalue condition is reminiscent of the well-known implicit bias phenomenon for logistic loss on separable data (Soudry et al. 2018, Ji & Telgarsky 2019). The paper claims it does not require data separability (Section 2.1), but it does not discuss whether the condition \(\tilde{\lambda}_0(t)\ge C\) itself implicitly forces separability or how the result relates to this known body of work. The synthetic experiment shuffles labels to mitigate separability concerns, but the theoretical connection is left unclear.

2. **The proof of Proposition 1 (strict positive definiteness with bias) is deferred, and its implications for the ResNet case are unclear.** The ResNet NTK formula is cited from Huang et al. (2020), which assumes no bias terms, while the paper's ResNet definition (equation 2.2) includes bias at the input layer. The paper handles this via an input transformation (augmenting with 1 and normalizing), but whether this is sufficient for multi-layer bias handling in the FC case is not argued in the main text.

3. **Experiments are illustrative but do not quantitatively validate the theorem.** The MNIST experiment (Figure 4) shows visible fluctuations of NNK values, which is consistent with non-convergence, but discarding the first 10 epochs without clear justification could hide early dynamics. No quantitative metric (e.g., the minimal eigenvalue of the kernel matrix over time, or a direct estimate of the claimed bound \(\lambda_0/(2n^2)\)) is reported.

### Trivial

None.

## Nice-to-Haves

- **Clarify the quantifier in Theorem 2 (FC case)** and derive or contextualize the \(\lambda_0/(2n^2)\) bound.
- **Discuss the implicit bias literature** explicitly and explain how Theorem 1 relates to or goes beyond known results about weight divergence under logistic loss.
- **Measure the minimal eigenvalue of the empirical kernel matrix** over time in experiments, rather than only tracking pointwise NNK values, to more directly test the theoretical claim.
- **Explain why the first 10 epochs are discarded** in the MNIST experiment, or present the full trace.

## Removed Points

These points were flagged by reviewers but are removed or downgraded for the reasons below:

- *Strict positive definiteness proof is "unverified" / missing* — The proof is likely in the appendix, which was stripped by the parser. The rule states that criticisms of missing appendix content should be removed. The paper clearly states the claim (Proposition 1) and cites prior work; whether the proof is correct cannot be judged from the main text alone, so this is not a valid weakness against what is presented.
- *Typos ("disconverges", "euqation", "postive", "overfti", "marix")* — These are parser artifacts, not author errors, per instructions.
- *Remark 1 not appearing in text* — Likely stripped with appendix.
- *"The results can be easily generalized" claim is unsubstantiated* — This is a minor scope claim typical in theory papers; it is not central to the contribution.
- *Strength about "clear proof sketch"* — The dynamical equations are clear, but the overall proof sketch has a major gap (retained as a weakness, not a strength). This strength conflicts with the verified weakness and is dropped.
- *Strength about "applicability to general network structures"* — Generic and not evidenced in the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fill the central proof gap.** The step from \(|f_t(x_i)|\to\infty\) to \(\|K_t^m\|\to\infty\) requires a rigorous argument connecting parameter divergence (Corollary 1) to gradient behavior. For ReLU networks, this would likely require analyzing how diverging pre-activations affect the gradient norms through backpropagation, and showing that the direction of gradient growth does not cancel the inner product. Without this step, Theorem 2 is unproven.

2. **Derive or contextualize the \(\lambda_0/(2n^2)\) bound.** Either show how this constant emerges from the contradiction argument, or if it cannot be derived from the current proof, state a qualitative divergence result instead.

3. **Fix the quantifier in Theorem 2 (FC case)** to match the ResNet case.

4. **Discuss data separability.** Clarify whether the condition \(\tilde{\lambda}_0(t)\ge C\) implies data separability, and how Theorem 1 relates to the known implicit bias literature.

5. **Strengthen the experiments.** Track the minimal eigenvalue of the empirical kernel matrix over training time to provide a more direct test of the theoretical claim.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>