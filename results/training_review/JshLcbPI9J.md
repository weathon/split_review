Now I have all the information needed to synthesize the final review. Let me compose it.

## Summary
The paper introduces DeepBC, a practical framework for computing backtracking counterfactuals in deep structural causal models (SCMs). It derives two variants: stochastic DeepBC (Langevin Monte Carlo sampling) and mode DeepBC (constrained optimization via iterative linearization). The method measures distances between factual and counterfactual in the structured latent space of the SCM, ensuring causal mechanisms remain intact. Experiments on Morpho-MNIST and CelebA demonstrate causal compliance, versatility (support for multiple variable types and antecedents), and modularity (ability to replace individual mechanisms).

## Strengths
- **Principled formulation of backtracking counterfactuals in deep SCMs.** The paper translates the theoretical framework of von Kügelgen et al. (2022) into tractable optimization and sampling objectives (Eqs. 5–8, 15–16), directly enabling practical implementation for high-dimensional data where the required marginalizations would otherwise be intractable.
- **Clear empirical demonstration of causal compliance on Morpho-MNIST.** When intensity is used as the antecedent, DeepBC changes both thickness and intensity (preserving the learned causal relation), whereas interventional counterfactuals break this relation and produce out-of-distribution images (Figures 4–5). The scatter plots in Figure 3 quantitatively visualize this distinction across multiple antecedents.
- **Modularity demonstration via mechanism exchange.** Figure 7 shows that replacing the beard-generation mechanism while keeping all other modules intact produces an interpretable out-of-distribution counterfactual — a property unique to the modular causal approach and impossible for monolithic non-causal methods.
- **Versatility across variable types and settings.** The framework handles continuous scalars (Morpho-MNIST), binary attributes and images (CelebA), categorical variables (via a temperature-softmax approximation), multiple distance functions (L2, sparsity), and supports both point estimates and sampling — going well beyond the typical instance-label setup.
- **Formal grounding connecting to the counterfactual explanations literature.** Section 3.2 shows mathematically that under specific assumptions (two-variable graph, invertible generative model, deterministic classifier), mode DeepBC reduces to a generalized form of the Wachter et al. (2017) formulation, clarifying the relationship between causal and non-causal approaches.

## Weaknesses

### Fatal
None.

### Major
- **CelebA baselines are limited.** The comparison on CelebA includes only a tabular non-causal method (a simplified Wachter-style regressor on attributes) and a wrong-graph ablation. While the tabular baseline is a reasonable non-causal comparator, the paper would be significantly strengthened by comparing against at least one well-established counterfactual explanation method (e.g., DiCE, or a full implementation of Wachter et al.) on the same task with the same generative model. The claim that DeepBC is "superior" to non-causal approaches is not fully supported without such a comparison.
- **Key algorithmic claim about convergence is unsubstantiated in the main text.** The paper states that the Levenberg-Marquardt-like iterative algorithm (Algorithm 1) "converges after much fewer iterations than gradient descent algorithms" (line 240) but provides no convergence comparison, runtime data, or iteration counts in the main paper. This claim is deferred to the supplement, but the main paper should include at least a brief summary of evidence for this claim.

### Minor
- **Main paper experiments are qualitatively oriented; quantitative metrics are deferred to the supplement.** The primary validation consists of scatter plots and example images. While the paper mentions quantitative experiments in the supplement (Section sec:numerical_celeba), the main paper body would benefit from including at least one quantitative metric (e.g., validity rates, proximity, or image quality scores) to give readers an immediate sense of the method's reliability beyond cherry-picked examples.
- **Invertibility assumption is a real limitation, and its practical impact is not quantified.** The paper honestly acknowledges this restriction (Section 6) and discusses future work. However, for the VAE-based models where invertibility is only approximate, the paper does not quantify how much information is lost in the encoding-decoding cycle or how this error propagates to the counterfactual. This would help users understand when the method might fail.
- **No ground-truth comparison on Morpho-MNIST.** Since the true structural equations for Morpho-MNIST are known (provided in the appendix), the paper could compute the exact backtracking distribution analytically and compare DeepBC's outputs to this ground truth. This would provide a strong quantitative validation that is currently missing.
- **Categorical variable extension is heuristic and not empirically validated.** The softmax-based approximation (Eq. 10) introduces temperature and reference category hyperparameters, but the paper provides no experiments validating how well this approximation works or how sensitive results are to the temperature choice.
- **No discussion of failure cases.** The paper would benefit from examples where DeepBC fails to satisfy the antecedent or produces implausible outputs, providing a more balanced assessment.

### Trivial
- None beyond minor presentation formatting that does not affect content.

## Nice-to-Haves
- Ablation on the penalty parameter λ and distance weightings.
- Comparison to the backtracking examples in von Kügelgen et al. (2022) using the same additive noise models.
- A quantitative modularity test (e.g., simulate a domain shift on Morpho-MNIST and show that retraining only the affected component outperforms retraining the entire model).

## Removed Points
The following points raised by reviewers are removed or significantly weakened per policy:
- **"No quantitative evidence whatsoever"** — Removed because the paper explicitly references quantitative experiments in the supplement (Section sec:numerical_celeba), which was stripped by the parser. The main paper is qualitatively oriented, which is a valid concern (kept above as a minor weakness), but the claim of zero quantitative evidence is inaccurate.
- **"Overclaimed connection to counterfactual explanations (Issue 2)"** — Weakened/removed because the paper's mathematical derivation is sound and the assumptions are clearly stated. The paper does not claim that all counterfactual explanation methods are special cases of DeepBC under all conditions — it shows a specific reduction under clearly scoped assumptions and then explains what DeepBC adds beyond this setting. The framing is appropriate.
- **"Missing discussion on how to choose p^B"** — Weakened. The paper discusses multiple distance functions (L2, L0 sparsity, weighted variants) and notes that any differentiable distance can be used (Section 3.4). This is adequate for a methods paper; a full ablation is a nice-to-have.
- **"No discussion of mixing time / burn-in for stochastic DeepBC"** — Removed as a nitpick about standard MCMC methodology that is not expected for a paper introducing a new algorithmic framework.
- **"Wrong graph baseline is too trivial"** — This is a reasonable ablation that validates the importance of correct causal structure; the criticism is not substantial enough to retain.

## Novel Insights
The reviews collectively highlight that while the paper's formalism is sound and the core idea is novel, the evaluation relies more on qualitative illustration than rigorous quantitative benchmarking. The most insightful observation cutting across reviews is that the paper bridges two communities (causal inference and counterfactual explanations) but the empirical evaluation does not yet fully exploit this bridge — in particular, the lack of comparison to standard counterfactual explanation methods on a controlled task leaves the claimed advantages partially unvalidated. This speaks to a broader pattern in papers introducing new frameworks: the formalism is often ahead of the evidence base.

## Suggestions
1. **Strengthen the CelebA evaluation** by comparing DeepBC against at least one standard counterfactual explanation method (e.g., DiCE or a full Wachter implementation with L1 distance) on the attribute space, with quantitative metrics (validity, proximity, sparsity, image FID).
2. **Provide ground-truth validation on Morpho-MNIST:** compute the exact backtracking distribution analytically and report quantitative deviation (RMSE, likelihood) between DeepBC outputs and ground truth.
3. **Include one convergence plot** in the main paper comparing Algorithm 1 to gradient descent on the penalty objective, with iteration counts and wall-clock time.
4. **Quantify VAE invertibility error** by measuring reconstruction error (e.g., MSE between x and d(e(x))) on the test set and showing how this correlates with counterfactual quality.

## Score and Decision

**Originality:** Good — the paper provides the first practical framework for backtracking counterfactuals in deep SCMs, beyond the simplified additive-noise settings of prior work.  
**Importance of research question:** High — backtracking counterfactuals offer a philosophically and practically distinct alternative to interventional counterfactuals, with potential impact in explainability and scientific insight.  
**Claims support:** Moderate — the formalism is sound and qualitative evidence is convincing, but quantitative support and baseline comparisons are weaker than expected for the strength of the claims.  
**Soundness of experiments:** Moderate — experiments demonstrate the claimed properties but rely heavily on qualitative examples; lack of comparison to standard CFE methods weakens conclusions about superiority.  
**Clarity of writing:** Good — notation is clear, derivations are well-structured, and the connection to counterfactual explanations is explainable.  
**Value to the community:** Moderate-to-high — the method fills a genuine gap and the modularity property is particularly valuable for domain adaptation and out-of-distribution reasoning.

Taking stock: The paper makes a real and well-formulated contribution. The weaknesses are about the depth of experimental validation, not about the correctness or novelty of the method. No fatal flaws exist. The paper would benefit from stronger baselines and a more quantitative main-paper evaluation, but the core contribution is solid and the experiments do demonstrate the unique properties of the method qualitatively.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>