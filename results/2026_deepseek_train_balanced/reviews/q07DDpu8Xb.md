## Summary

This paper studies identifiability in causal representation learning with latent additive noise models under distribution shifts. The core theoretical contribution is a non-parametric condition (Assumption iv) characterizing which types of soft-intervention distribution shifts enable identifiability, with proofs of both sufficiency and necessity, plus partial identifiability results when the condition is only partially met. The theory is extended to post-nonlinear latent causal models. An algorithm based on sequential VAE with sparsity-inducing masks is proposed, and experiments on synthetic data, image data, and semi-synthetic fMRI data are presented.

## Strengths

- **Sufficient-and-necessary condition for identifiability** (Remark 3.6): The paper formally establishes that condition (iv) is both sufficient (Theorem 3.1) and necessary (contrapositive of Theorem 3.5b) for component-wise identifiability under the nonlinear ICA framework, providing a stronger theoretical guarantee than the sufficient-only conditions typical of prior work (Liu et al. 2022, 2024; Ahuja et al. 2023).

- **Partial identifiability propagating through identifiable nodes** (Theorem 3.5, Remark 3.7): The result that $z_i$ remains identifiable even when its parent nodes are unidentifiable is genuinely non-trivial and distinguishes this work from hard-intervention methods. This follows because noise variables are identified first (via assumptions i–iii) and condition (iv) relates each node to the noise of its parent (Lemma A.3). The paper explicitly contrasts this with prior works (Ahuja et al. 2023; Seigal et al. 2022; Buchholz et al. 2023; Varici et al. 2023) that do not offer similar partial identifiability.

- **Generalization from linear/polynomial to additive noise and post-nonlinear models**: The theory extends from the restricted model classes of prior work to general latent additive noise models (Eq. 2) and further to post-nonlinear models (Eq. 5), enabling the use of MLPs and transformers rather than polynomial bases, which avoids the numerical instability and exponential growth of polynomial models.

- **No requirement for single-node interventions or observation at the specific $\mathbf{u}_{i'}$ value**: The paper relaxes a key requirement of hard-intervention methods. Remark 3.3 clarifies that condition (iv) constrains the function class, not the sampled data — the specific $\mathbf{u}_{i'}$ where the causal edge is removed need not appear in training data.

## Weaknesses

### Major

1. **Disconnect between the theory's central condition and the algorithm.** The paper's main theoretical contribution is condition (iv), which characterizes exactly which distribution shifts enable identifiability. However, the algorithm in Section 5 is a sequential VAE with autoregressive priors and L1 sparsity masks — standard techniques that bear no explicit relationship to condition (iv). The paper states the algorithm is "guided by our underlying theory" (abstract, line 4) but never specifies how. There is no mechanism to test whether condition (iv) holds, to enforce constraints derived from it, or to exploit its structure beyond the vague justification that identifiability "guarantees" the causal ordering will be learned correctly (line 138). Concretely, the same algorithm would be equally reasonable without condition (iv), meaning the experiments do not validate the paper's core theoretical claim about *which* distribution shifts matter.

2. **Synthetic experiments are critically under-described.** The data generation process (Section 6) is described in three sentences. No details are given about: the causal graph structure used, the functional form of $g_i^\mathbf{u}$, how the data respects condition (iv) in the "satisfied" case, or how it was modified to violate condition (iv) for Figure 2. The paper claims that Figure 2 "demonstrates both sufficient and necessary condition" — a far-reaching conclusion resting on a single experiment whose setup is opaque. Without a clear description, the reader cannot assess whether the empirical "failure" of identifiability is attributable to violation of (iv) or to confounding factors (insufficient samples, optimization difficulty, etc.).

3. **No statistical rigor in any experiment.** No error bars, confidence intervals, or multiple-seed results are reported for any experiment (synthetic, image, or fMRI). Figure captions do not indicate whether values are from a single run or averaged. Given the known training variability of VAEs, this omission substantially weakens the empirical claims and makes the reported MPC values (e.g., 0.981 on fMRI) difficult to interpret.

### Minor

4. **The fMRI experiment is framed misleadingly.** The paper states "real fMRI data" is used and implies the method is run on raw fMRI measurements (line 249). In reality, the six brain-region signals are used directly as latent variables $\mathbf{z}$, which are then passed through a *random nonlinear mapping* to generate synthetic observed data $\mathbf{x}$. The method is evaluated by comparing recovered latents to the original brain signals. This is an informative sanity check but is a semi-synthetic experiment, not a validation on raw fMRI data as advertised.

5. **Reliance on a fixed causal ordering is not critically examined.** The algorithm enforces an arbitrary order ($z_1 \succ z_2 \succ \dots$) and relies on the sparsity regularizer to discover the correct graph (line 138). The heuristic nature of this approach, its sensitivity to the chosen ordering, and the lack of any comparison with learned-order methods are not discussed or ablated.

6. **No ablation studies.** The sparsity penalty $\gamma \sum \|\mathbf{m}_i\|_1$ is a key hyperparameter whose effect on graph recovery is not studied. No comparison between enforcing vs. not enforcing the causal order is provided.

### Trivial

7. Several typographical errors and garbled text appear (e.g., "groundturthgroundtruth" in Remark 3.2, "team $b z_1$", "$\overset{\cdot}{+}$"), which are likely PDF extraction artifacts rather than author errors.

## Nice-to-Haves

- A more substantive proof sketch in the main text (e.g., the transformation of condition (iv) into a Jacobian constraint) would help readers assess the central theorem without relying entirely on the appendix.
- Including comparisons against hard-intervention methods (Ahuja et al., Buchholz et al.) on setups where both types of interventions apply would contextualize the claimed advantages — though this is scope-expansion beyond the paper's stated setting.
- An explicit diagnostic for condition (iv) or an experiment that systematically varies the degree of violation and shows monotonic degradation would directly validate the necessity claim.

## Removed Points

The following points from the input reviews were removed per filtering rules:

- **Criticism that the "sufficient and necessary" claim is overstated**: The paper carefully qualifies this as "under assumptions (i)-(iii), without additional assumptions" (Remark 3.6). This is a precise and standard framing of a framework-relative claim; the critic's reading was uncharitable.
- **Criticism that the identifiability-to-graph-structure leap is glossed over in Remark 3.4**: The paper cites Hoyer et al. (2008) and Peters et al. (2014) — standard references for additive noise model identifiability. The claim is brief but correct for the cited results.
- **Criticism about missing baselines (causal representation learning methods for hard interventions)**: These methods require single-node hard interventions, a fundamentally different data regime. The paper's comparison against polynomial soft-intervention models (Liu et al. 2024) is the natural competitive baseline. A demand to include hard-intervention methods would create an asymmetry favoring baselines under stronger assumptions.
- **Criticism about proofs being in the appendix**: The appendix was likely present in the original submission but stripped by the PDF parser.
- **Various formatting/style nitpicks and speculation-based criticisms**: Removed per hard rules.
- **Strength from Strength Finder about "empirical validation on real fMRI data"**: Demoted because the fMRI experiment is semi-synthetic (real signals mixed with synthetic nonlinear mapping), which weakens the claimed "real-world data" demonstration.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Describe the synthetic data generation for Figure 2 in detail: what causal graph, what functional form for $g_i^\mathbf{u}$, and how exactly was condition (iv) broken for the $z_1\to z_2$ edge?
2. Add error bars / confidence intervals to all experimental figures. Report results over at least 5 random seeds.
3. Either explain how the algorithm implicitly exploits condition (iv), or explicitly characterize it as a heuristic method *inspired by* (but not directly implementing) the theoretical condition, and adjust the paper's claims about "outstanding performance" aligning with "theoretical findings" accordingly.
4. Reframe the fMRI experiment to clearly state it is semi-synthetic, and present it as a controlled sanity check of the method's ability to recover known signals.
5. Add ablation on the sparsity penalty $\gamma$ and on the fixed ordering assumption.
6. Fix the textual artifacts (Remark 3.2) for camera-ready.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>