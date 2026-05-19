- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 3, 6, 6
Now I have all the information I need. Let me carefully synthesize the final review, verifying each claim against the paper.

## Summary

**Paper:** Deep Backtracking Counterfactuals (DeepBC) — a practical method for computing backtracking counterfactuals in deep structural causal models. The paper derives two variants (stochastic via Langevin Monte Carlo, and mode via constrained optimization with an iterative linearization algorithm), relates these to the standard Wachter counterfactual explanation framework, and demonstrates causal compliance, versatility, and modularity on Morpho-MNIST and CelebA.

---

## Strengths

- **Rigorous derivation of tractable objectives from the von Kügelgen et al. formalization.** Equations (7) and (9) (lines 127–142) show how the sampling and optimization problems derive from the backtracking conditional, making a previously intractable formulation computationally feasible for deep SCMs.

- **Causal compliance demonstrated concretely on Morpho-MNIST.** Figures 3 and 4 show that when intensity is the antecedent, DeepBC changes the upstream variable thickness in accordance with the causal law, whereas interventional counterfactuals break this relationship. The paper also shows that when thickness (a root node) is the antecedent, both methods agree — a clean consistency check (Section 4.1, lines 300–307).

- **Modularity demonstrated via mechanism swapping on CelebA.** Figure 6 shows that replacing the learned beard mechanism with a manually constructed one yields an interpretable out-of-distribution counterfactual, illustrating how DeepBC's explicit modeling of individual structural equations supports modular reuse (Section 4.2, lines 337–339).

- **Versatility in supporting multiple antecedent variables, distance functions, and stochastic sampling.** The paper demonstrates antecedents over subsets of variables (thickness-only, intensity-only, gender+age), sparse variants, different distance functions, and a Langevin-based sampling procedure (Sections 3.4, 4.1, 4.2).

- **Closed-form iterative algorithm via Levenberg-Marquardt linearization.** Algorithm 1 uses a first-order Taylor approximation yielding convex quadratic subproblems with a closed-form solution (Equation 15), which the paper states converges faster than gradient descent (Section 3.3).

- **Explicit connection to counterfactual explanations.** Section 3.2 shows that DeepBC reduces to the Wachter formulation under specific structural assumptions (Equation 13), positioning DeepBC as a generalization that accounts for noise and multiple causally related variables (Figure 2).

- **Extension to categorical variables via differentiable approximation.** Equation (14) adapts the Gumbel reparameterization trick to make categorical nodes invertible and differentiable, enabling DeepBC to handle discrete attributes (Section 3.4).

---

## Weaknesses

### Fatal

None.

### Major

- **Lack of quantitative evaluation metrics in the main paper.** The experiments are almost entirely qualitative (scatter plots, image examples, density contours). No numerical metrics are reported in the main body to substantiate claims about causal compliance or counterfactual quality. For example, on Morpho-MNIST one could report the average change in thickness when intensity is the antecedent across many samples and compare it to the known causal relationship. On CelebA, attribute consistency rates (e.g., what fraction of counterfactuals have the predicted attribute values consistent with the causal graph?) could be computed. The paper mentions "quantitative experiments" in an appendix reference (line 341), but the main paper as presented here lacks any numbers. This makes it harder for readers to calibrate how reliably the method works across many queries versus the illustrative examples shown.

- **VAE invertibility approximation is discussed but its empirical impact is not studied.** The core derivation assumes exact invertibility of the reduced form (line 61). For conditional normalizing flows this holds exactly, but for conditional VAEs — used for the image component in both experiments — the inversion is only approximate (decoder(encoder(x)) ≈ x, line 75). While the paper acknowledges this limitation and cites theoretical justification (Reizinger et al., 2022) in Section 2.2, and discusses it further in the limitations (lines 377–378), it never empirically examines how reconstruction errors or information loss from the VAE's lower-dimensional latent space affect counterfactual quality or causal compliance. Without this analysis, the reader cannot assess how often the method operates in the regime assumed by the theory, and whether the causally compliant property degrades gracefully with approximation quality.

### Minor

- **Baseline comparisons are limited.** The "tabular non-causal explanation" baseline (Section 4.2) is reasonable for illustrating the sparsity-in-attribute-space point, but the paper does not compare against standard image-based counterfactual explanation methods (e.g., Goyal et al. 2019, Boreiko et al. 2022, both cited by the paper). The paper argues that deep counterfactual explanation methods (Eq. 14) are not applicable for sparse changes (line 329), but a non-sparse comparison on CelebA would still be informative to contextualize DeepBC's behavior against established methods.

- **Runtime and convergence are not reported.** The paper claims the Levenberg-Marquardt-style algorithm converges faster than gradient descent (line 240) but provides no quantitative runtime or iteration count data. For practitioners evaluating the method, these numbers would be helpful.

### Trivial

None.

---

## Nice-to-Haves

- A controlled experiment on synthetic data with known ground-truth SCM, measuring the error in recovering true counterfactual outcomes (e.g., MSE of downstream variables) for DeepBC versus input-space methods.
- An ablation comparing DeepBC results on a dataset where normalizing flows are used for *all* variables (so invertibility is exact) versus the VAE-based implementation used here, to isolate the impact of the invertibility approximation.
- Comparison with the closed-form backtracking solution for additive noise models (von Kügelgen et al., 2022) on the Morpho-MNIST setting — though the paper's mechanisms are not additive noise, this would further contextualize the contribution.

---

## Removed Points

These points were flagged in the input reviews but are removed with justification:

- **"Causal sufficiency assumption not discussed for real data"** — The paper states the assumption (line 59), which is standard for SCM-based methods. This is not a weakness specific to this paper.
- **"Wrong-graph baseline only checks consistency with assumed graph, not correctness"** — The paper uses this baseline to show *sensitivity* to graph misspecification, which is a useful diagnostic. The paper does not claim it validates causal correctness.
- **"Conflates two different paradigms (explaining true mechanisms vs. model predictions)"** — The paper clearly distinguishes these in Section 3.2 and Figure 2's caption. The paper's claim is that DeepBC addresses a *different question*, not that one subsumes the other.
- **"Missing discussion of Nasr et al. 2023"** — The paper cites Nasr et al. 2023 in the context of invertible mechanisms (line 61 footnote). The related work section appropriately focuses on the most directly relevant methods.
- **"OOD counterfactuals — unclear when desirable"** — The paper demonstrates modularity as a *property* (the ability to swap mechanisms), not as an argument that OOD counterfactuals are inherently desirable. The demonstration is a proof-of-concept.
- **"No evidence that interventional counterfactuals are OOD" / "Weakens claim about faithful insights"** — The paper provides visual evidence (Figure 4) and a clear explanation (thickness-intensity correlation). Quantitative OOD measures would strengthen but are not required for the paper's qualitative demonstration.
- **"Missing related works" / "Missing appendix content"** — Parser artifact; these sections exist in the original submission.
- **"Human plausibility ratings needed"** — Beyond scope for a methods paper introducing a new algorithmic framework.
- **"Should defend the CelebA causal graph"** — The graph is from Yang et al. 2020, a standard citation; defending graph validity is not required.
- **"Identifiability undermines claims"** — The paper discusses identifiability honestly as a limitation (lines 371–372), noting that this affects any method in this class, not just DeepBC.

---

## Novel Insights

The two input reviews do not contribute genuinely novel observations beyond the paper's own contributions. The harsh critic's analysis is thorough but largely restates the paper's known limitations (qualitative evaluation, VAE approximation) rather than revealing hidden issues. The strength finder correctly identifies the paper's demonstrated properties. Neither review uncovers an unstated assumption or methodological flaw that the paper itself does not already surface.

---

## Suggestions

1. **Add quantitative metrics in the main paper.** At minimum, on Morpho-MNIST: report the average change in thickness when intensity is the antecedent across many factual points (for both DeepBC and interventional), showing that DeepBC tracks the known causal relationship while interventional does not. On CelebA: report attribute consistency rates or compute a causal metric like agreement with the assumed structural equations.

2. **Empirically study the VAE invertibility approximation.** On a dataset dimension where normalizing flows are feasible for all variables, compare DeepBC results with a VAE-based implementation vs. a fully flow-based implementation. Show how counterfactuals change as a function of reconstruction error or latent dimensionality.

3. **Include a stronger image-based baseline.** Even if the comparison is imperfect (e.g., the baseline method does not model causal structure), comparing DeepBC outputs to an established image-based counterfactual explanation method would help the reader understand the practical differences.

4. **Report runtime and iteration counts** for the mode DeepBC algorithm vs. standard gradient descent to substantiate the convergence claim.

---
