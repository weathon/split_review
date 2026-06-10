## Summary

The paper introduces the **training Jacobian** — the Jacobian of trained parameters with respect to their initial values — as a framework for analyzing the geometry of SGD training in small neural networks. Computing this matrix for a 1-hidden-layer MLP (width 64, 4810 parameters) trained on UCI digits, the authors identify three spectral regions: a large "bulk" of singular values near 1 (≈60% of dimensions), a "chaotic" region of values >1, and a "stable" region of values <1. They show that bulk directions are carried through training almost linearly across seven orders of magnitude, have negligible effect on in-distribution predictions but affect OOD predictions, and that the bulk subspace overlaps with the nullspace of the parameter-function Jacobian on test data. A causal intervention (restricting SGD to the bulk) confirms the bulk is functionally inert.

---

## Strengths

1. **Empirical validation of near-perfect linearity along bulk directions across seven orders of magnitude**: Section 3.2 (Fig. 3a) shows that perturbing the initialization along a bulk singular vector produces a response in the trained model that matches the Jacobian's linear prediction almost exactly for stimulus sizes ranging from $10^{-3}$ to $10^{3}$. The projection onto orthogonal directions remains negligible. This directly validates the central premise that the training Jacobian is a meaningful descriptor of training dynamics in the bulk.

2. **Causal subspace intervention cleanly separates correlational from causal claims**: Section 3.6 (Fig. 7) shows that restricting SGD to the bulk subspace makes it impossible to reduce training loss, while restricting to the complement performs as well as unconstrained training. Unlike prior correlational analyses (e.g., Li et al. 2018's projection experiments which only measure impact on final loss), this intervention demonstrates that the bulk corresponds to parameters that genuinely do not need to change.

3. **Multi-faceted convergence of evidence linking the bulk to data structure**: The paper ties together four independent lines of evidence: (a) bulk subspace overlaps with the nullspace of the parameter-function Jacobian on test data but not white noise (Sec. 3.4, Fig. 5b); (b) bulk is preserved across random seeds and shuffled labels but disappears on white noise (Sec. 3.5, Fig. 6b); (c) bulk perturbations negligibly affect in-distribution outputs but affect OOD outputs (Sec. 3.3, Fig. 4); (d) left and right singular vectors of the bulk are nearly identical (Fig. 1b). This convergence is compelling.

4. **Careful handling of the bulk boundary via sweeping**: Rather than fixing an arbitrary threshold on $|\sigma_i - 1|$, Sec. 3.5 sorts singular vectors by distance to 1 and sweeps over $k$, reporting results for all cutoffs against a random-subspace baseline (Fig. 6a). This eliminates sensitivity to threshold choice.

---

## Weaknesses

### Fatal
None.

### Major

1. **Claims of generality are unsupported by the evidence**: Every experiment uses a single architecture (MLP with one hidden layer of width 64), a single small dataset (UCI digits, 1,797 examples), a single optimizer (SGD with momentum), and a single training duration (25 epochs to zero loss). The abstract and introduction state findings as general properties of neural network training ("the singular value spectrum consists of three distinctive regions," "the bulk depends strongly on the data distribution"), but these are observations about one specific configuration. Several uncontrolled confounds are not discussed: **(a)** The model is heavily overparameterized (4,810 parameters for 1,797 examples) and trained to exactly zero loss — the large bulk of near-unit singular values may be a direct consequence of the solution manifold being high-dimensional. **(b)** Training with cross-entropy loss to zero loss drives logits to ±∞ and weight norms to grow without bound; the "chaotic" singular values orders of magnitude >1 could reflect this rather than a general property of nonconvex optimization. **(c)** No architectural variation (CNNs, transformers, deeper MLPs, different widths) is tested. The paper's central empirical claims remain unvalidated outside this single setup.

2. **Critical hyperparameters are not reported**: The paper states "SGD with momentum" but does not specify the learning rate, momentum coefficient, batch size, or weight initialization scheme. Line 205 references "identical hyperparameters to those used in Section 3.1" but Section 3.1 does not state them either. This prevents reproduction and makes it unclear whether the findings are robust to different hyperparameter choices.

### Minor

1. **No statistical reporting of variance**: No confidence intervals, error bars, or number of replicates are reported for any experiment — including the perturbation linearity measurements (Sec. 3.2), KL divergence measurements (Sec. 3.3), and subspace similarity analysis (Sec. 3.5). All of these quantities would vary across random seeds, but the paper presents single-run results.

2. **The chaotic region receives no mechanistic analysis**: The paper names the chaotic region (singular values > 1) and asserts it is "due to the nonconvexity of the objective" (line 85), but provides no evidence for this claim. No experiment characterizes what distinguishes chaotic from bulk directions at a mechanistic level, or why constraining training to the chaotic subspace allows it to succeed (Sec. 3.6).

3. **PFJ analysis only at initialization, not tracked through training**: The connection between the training Jacobian bulk and the parameter-function Jacobian nullspace (Sec. 3.4) is computed on a *randomly initialized* model (line 150). The paper does not discuss whether this relationship holds throughout training or only at initialization, which limits the mechanistic insight.

4. **No discussion of the zero-loss / overparameterized regime**: Training to exactly zero loss on an overparameterized model means the solution is not unique. The paper does not discuss whether its findings would change if training were stopped earlier (when test loss plateaus but training loss is nonzero) or if the model were not overparameterized.

5. **No quantitative comparison to prior dimensionality measures**: The introduction discusses Li et al. (2018) (intrinsic dimensionality via random projections), Song et al. (2024) (Hessian eigenspace), and Gur-Ari et al. (gradient/Hessian alignment), but the paper never quantitatively compares the "active subspace" found via the training Jacobian to these prior measures on the same network and dataset.

### Trivial
None.

---

## Nice-to-Haves

- Deepening the mechanistic explanation for why bulk directions affect OOD behavior — e.g., examining what specific features change when perturbing along a bulk direction, or whether the effect correlates with distance from the training data manifold.
- Comparing the active subspace dimensionality (complement of the bulk) to intrinsic dimensionality measured by Li et al.'s random projection method on the same network, which would directly connect this work to prior literature.
- Exploring the relationship between the training Jacobian and the time-averaged Hessian for realistic networks, given the extensive literature on Hessian spectra.
- Adding at least 2–3 meaningfully different experimental configurations (e.g., a small CNN on a subset of CIFAR-10, a different optimizer like Adam, training stopped before zero loss) to test whether the three-region spectral structure generalizes.

---

## Removed Points

These points were flagged for removal but are included here in case they are useful:

- *Harsh critic's claim about missing stopping criterion*: The paper does specify 25 epochs (line 80). The critic says "other than 'near-zero training loss'" but the duration is explicitly stated. Partially inaccurate → removed.
- *Harsh critic's claim about "no reported search over hyperparameters"*: This is a description, not a weakness; the paper never claims to do a hyperparameter search → removed.
- *Harsh critic's "Strengthening the Paper on Its Own Terms" section*: These are constructive suggestions, not weaknesses → moved to Nice-to-Haves.
- *Strength Finder's strengths that are generic or conflict with verified weaknesses*: All five identified strengths were concrete, specific, and verified against the paper text; none were removed.
- *"Typos, formatting" and similar nitpicks*: None present in the original criticism; not applicable.

---

## Novel Insights

The reviewers largely converged on the same assessment. The most insightful observational from the reviews is the recognition that the paper's strongest finding — the causal subspace intervention (Sec. 3.6) — cleanly separates this work from prior correlational analyses of training dimensionality (Li et al. 2018, Song et al. 2024). The harsh critic correctly identified that this intervention proves the bulk is not merely a descriptive artifact but corresponds to parameters that genuinely do not need to change. However, neither reviewer fully interrogated whether the intervention experiment is circular: since the bulk is *defined* as the set of directions with singular values close to 1 (i.e., directions where parameters don't change), constraining training to these directions failing to make progress is partially tautological — the value is in the quantitative measure of *how many* dimensions are truly needed, not in the qualitative existence of inert directions. This self-consistency check is still informative, but weaker than a non-tautological test of the framework's predictions.

---

## Suggestions

1. **Broaden the empirical scope** with at least 3–4 meaningfully different conditions: a different architecture (small CNN on a subset of CIFAR-10), a different optimizer (Adam), a different training regime (early stopping before zero loss), and a non-overparameterized model. Calibrate the paper's claims to match what the evidence supports.

2. **Report all hyperparameters**: learning rate, momentum coefficient, batch size, and initialization scheme. This is a basic reproducibility requirement.

3. **Add confidence intervals or error bars** across multiple random seeds for all quantitative measurements, particularly the subspace similarity analysis (Sec. 3.5) and KL divergence measurements (Sec. 3.3).

4. **Discuss the overparameterization and zero-loss confounds explicitly** — either acknowledge them as limitations or provide evidence that the findings are robust to these factors.

5. **Quantitatively compare the active subspace dimensionality to prior measures** (Li et al.'s intrinsic dimensionality, Song et al.'s Hessian complement) on the same setup to position this work relative to existing literature.

6. **Provide a mechanistic analysis of the chaotic region** rather than simply asserting it is "due to nonconvexity."

---

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>