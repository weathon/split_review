- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes that the high variance of score function estimates from denoising score matching (DSM) — particularly at small noise levels — contributes to generalization in diffusion models. The authors study this theoretically using linear score estimators and derive that, under a specific scaling limit, the expected reverse-diffusion distribution is equivalent to running the optimal score's reverse process and then convolving with a data-dependent kernel (the "V kernel"). They analyze the kernel's form for Gaussian data, orthogonal features, and Gaussian mixtures, arguing it implements an inductive bias that adds more noise in low-probability regions.

## Strengths

- **Theorem 1 formally links score-estimation variance to a noise kernel in the reverse process.** Section 4 states the theorem for linear score estimators trained with DSM: under the stated asymptotic limit, the expected reverse-diffusion distribution solves an SDE whose drift uses the optimal score and whose noise covariance is given by the V kernel (Eq. 16). This directly formalizes the paper's central claim.

- **The V kernel is computed in closed form for Gaussian data, showing state-dependent smoothing.** Eq. (18) gives \(V(\mathbf{y}) = \frac{Z_\sigma}{4c}[1 + (\mathbf{y}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{y}-\boldsymbol{\mu})]\,\mathbf{I}\), illustrating that added noise is larger far from the mean and smaller near it — a form the paper convincingly argues is sensible for generalization.

- **The V kernel connects to the Fisher information matrix for Gaussian mixtures.** Section 5.4 shows that for Gaussian mixture features, the covariance matrix appearing in the V kernel is the Fisher information matrix, meaning the kernel applies least smoothing where the score is most sensitive to parameter changes — an elegant connection.

- **The paper explicitly derives the singular variance of the DSM target at small times.** Eq. (6) computes \(\operatorname{Cov}[\nabla_{\mathbf{x}_t}\log p(\mathbf{x}_t|\mathbf{x}_0)] = \frac{1}{\sigma_t^2}\mathbf{I}\) which diverges as \(t \to 0\). This quantifies the "high variance" at the core of the mechanism and is directly cited as the source of the effect.

- **The derivation traces how the V kernel emerges from standard DSM practice.** Section 2 describes the specific time-sampling distribution \(\lambda_*(t)\) and \(\epsilon\)-parameterization used by Stable Diffusion and Karras et al. (2022), connecting the theoretical result to widely used training procedures.

## Weaknesses

### Fatal
None.

### Major

- **The scaling assumption \(N\Delta t = c\) lacks justification for practical regimes.** Theorem 1 requires \(N \to \infty\) and \(\Delta t \to 0\) with \(N\Delta t = c \gg 1\) held constant. This joint limit is needed to make the noise term \(O(1)\), but the paper does not argue why this limit is relevant to practical diffusion models (where \(N\) is fixed and \(\Delta t\) is chosen independently for sampling accuracy). Without discussing how the qualitative effect persists for finite \(N, \Delta t\) outside this specific scaling, the theoretical mechanism's connection to actual diffusion model behavior remains unclear.

- **No empirical validation of the core claim.** The paper's title asserts that high variance estimates "help diffusion models generalize," yet the paper contains zero experiments or simulations — not even on toy data satisfying its own assumptions (e.g., a Gaussian mixture with a linear score estimator). For a paper advancing a causal claim about a mechanism for generalization, this is a significant evidential gap. A simple controlled simulation matching the theory's assumptions would substantially strengthen the contribution.

### Minor

- **The definition of "generalization" is broad enough to include any deviation from the empirical score.** The paper defines generalization as the estimator "learning something different than [the empirical] score function" (Section 3). Any smoothing — including isotropic Gaussian noise — would satisfy this definition. The paper qualitatively argues that the V kernel's state-dependent form is beneficial, but does not quantitatively demonstrate that its smoothing constitutes *meaningful* generalization (e.g., plausible interpolation, improved held-out metrics) over simpler alternatives.

- **The corollary announced after Theorem 1 is never stated.** Line 151 reads "One important corollary follows from the details of the argument:" and then Section 5 begins without the corollary ever being specified. This appears to be a missing piece of the manuscript.

- **Theorem 1's "approximately equivalent" is not made precise.** The theorem does not specify in what sense the approximation holds (weak convergence? a bound on some probability metric? mean-square error of some functional?), leaving the theoretical claim's exact content unclear.

### Trivial

- The path integral formulation (Eq. 11) is introduced without derivation or reference, which may confuse readers unfamiliar with this representation.

## Nice-to-Haves

- A discussion of how the V kernel's predictions might differ from or align with other proposed mechanisms for diffusion model generalization (e.g., manifold learning, discretization error, architectural inductive biases).
- An analysis of how the kernel behaves when features are learned (e.g., by a neural network) rather than fixed a priori, even if speculative.

## Removed Points

These points were raised by the reviewers but are removed as they do not survive verification:

- **"Dismissal of other potential sources of generalization is too quick"** — This is standard motivation framing in introduction sections. The paper cites relevant references and the discussion is appropriately brief for a setup.
- **"No comparison to alternative explanations"** — The paper discusses this in Section 1 with references. Demanding a more thorough comparison exceeds the paper's stated scope.
- **"No discussion of how the kernel behaves in realistic feature spaces (e.g., neural network features)"** — Scope creep. The paper acknowledges the linear estimator limitation, and discussing neural network feature spaces is beyond what can be expected from this theoretical treatment.
- **"Path integral formulation is not standard"** — Merely noting that a formulation is non-standard is not a weakness; the paper uses it for analytical convenience.
- **"Paper's structure places key result before interpretation"** — This is a subjective presentation preference, not a weakness.
- **Criticisms about missing references, appendices, or proofs** — Stripped by the parser.
- **Various speculations about what might happen under different assumptions** — Not grounded in what the paper actually says.

## Novel Insights

The two reviewer inputs largely overlap in identifying the core issues (scaling assumption, no empirical validation) and strengths (theoretical derivation, closed-form examples). Neither reviewer identified a genuine flaw in the mathematics itself beyond questioning the plausibility of the scaling regime. The most useful cross-cutting observation is that the paper's central mechanism depends on a specific joint limit whose connection to practice is not argued — this is a real structural concern that neither reviewer fully unpacks into why the scaling emerges (it balances estimation variance \(O(1/N)\) with the singular target variance \(O(1/\sigma_t^2) \sim O(1/\Delta t)\) to obtain an \(O(1)\) noise term), but also neither reviewer notes that this type of balancing limit is common in asymptotic theory. The paper would benefit from acknowledging that the limit is a theoretical device and explicitly discussing what happens when \(N\) and \(\Delta t\) are independently finite.

## Suggestions

1. **Add a small-scale simulation** in a setting that exactly satisfies the paper's assumptions (e.g., Gaussian mixture data, linear score estimator). Show that: (a) the empirical sampling distribution matches the V-kernel prediction, and (b) varying \(N\) and \(\Delta t\) produces the predicted changes in the kernel. This single addition would transform the paper from speculation to evidence.

2. **Clarify the scaling assumption.** Either (a) derive the same result without the joint limit (e.g., exact finite-\(N\) expressions), or (b) show the result holds in a more practical regime (e.g., \(N\) fixed but large, \(\Delta t\) small but not coupled to \(N\)), or (c) at minimum, provide a clear intuitive argument for why the \(N\Delta t = c\) regime captures the essential behavior and discuss how results degrade outside it.

3. **State the missing corollary** after Theorem 1 and make "approximately equivalent" more precise (e.g., specify the metric or convergence mode).

4. **Define a quantitative measure of generalization** (e.g., held-out likelihood, a diversity-quality tradeoff) and assess whether the V kernel's predictions improve upon the optimal (non-generalizing) score under this measure, at least analytically.
