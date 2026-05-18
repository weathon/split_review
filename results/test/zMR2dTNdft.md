I have thoroughly analyzed the paper and all reviewer claims. Let me now compile the final review.

---

## Summary

This paper defines a class of "mirror reflection symmetries" in loss functions and proves (Theorem 1) that every such symmetry implies a linear stationary condition O^Tθ=0, with weight decay and gradient noise both driving the model toward this constraint. It then applies this framework to rescaling, rotation, and permutation symmetries—showing they are instances of mirror symmetry—and derives that they respectively cause sparsity, low-rankness, and homogeneous ensembling. The paper connects the theory to collapse phenomena (neural collapse, posterior collapse, dimensional collapse, loss of plasticity) and proposes a differentiable constraint algorithm (DCS). Experiments on linear regression (sparsity), matrix factorization (low-rank), and ResNet18 (neuron homogeneity) provide supporting evidence.

## Strengths

1. **Novel unified framework for diverse symmetries**: The paper is the first to treat rescaling, rotation, and permutation symmetries as instances of a single mathematical structure (mirror reflection symmetry). Prior works studied each symmetry case-by-case; the unified perspective is a genuine conceptual contribution that enables transferable insights across symmetry types.

2. **Theorem 1 establishes a general mechanism linking symmetry to structured constraints**: The theorem shows that any O-mirror symmetry forces O^Tθ=0 to be stationary (part 1), and that both weight decay (parts 3-4) and large gradient noise (Section 2.3) drive the model toward this constraint. This provides a theoretical basis for why sparsity, low-rankness, and homogeneity emerge from common architectural symmetries—a mechanism that goes beyond the classical understanding that L2 regularization always yields dense solutions.

3. **Clear derivations for the three major symmetry types as corollaries**: Sections 3.1-3.3 provide explicit constructions showing how rescaling symmetry (n1=(1,1), n2=(1,-1), O=I), rotation symmetry (using the fact that I-2Π is orthogonal), and permutation symmetry (explicit projection matrix P) each imply specific mirror symmetries, with corollary theorems describing the resulting behavior. The concrete Hessian computation for a tanh network (Section 2.2) validates the theory on a nontrivial example.

4. **Experimentally supported predictions**: The matrix factorization experiment (Figure 1, mid) is particularly well-controlled: the vanilla model (with rotation symmetry) converges to low-rank solutions under large gradient noise, while adding a residual connection (which removes the rotation symmetry) causes the model to remain full-rank throughout training. This directly attributes the low-rank tendency to the symmetry, not to unrelated optimization effects.

5. **Theoretical explanation of diverse collapse phenomena**: Section 3.4 connects loss of plasticity, neural collapse, posterior collapse, and dimensional collapse to a single underlying cause (symmetries in the loss function). This provides a unifying narrative for phenomena previously studied in isolation, and the theory suggests concrete remedies (breaking symmetries or injecting noise).

## Weaknesses

### Fatal
None.

### Major

1. **The SGD dynamics analysis (Section 2.3) is heuristic and insufficiently rigorous for a theory paper.** The derivation uses a second-order expansion, a "diagonal approximation" of the Hessian, and references to Lyapunov exponents without establishing that the assumptions hold. The critical learning rate formula (Eq. 7) is presented as "qualitatively correct" but the conditions under which the expansion is valid, the independence of Hessian blocks, and the applicability of the random matrix product framework are not justified. The claim that "one can show that Pw converges to 0 in probability if and only if the Lyapunov exponent ... is negative" is stated without proof or citation that directly applies to this setting. This section aspires to be a central contribution (explaining why gradient noise substitutes for weight decay), but the analysis is not at the same standard as the rest of the paper. The paper would be stronger if this section were either made rigorous or reframed as a suggestive discussion with caveats clearly stated.

### Minor

2. **The ResNet18 experiment (Figure 1, right) does not isolate permutation symmetry as the causal mechanism.** The paper compares training with vs. without weight decay, showing that neuron correlations become more block-structured when weight decay is present. However, weight decay reduces parameter norms generally, which could make neurons more similar even without a symmetry-based mechanism. A controlled comparison where permutation symmetry is explicitly broken (e.g., by adding fixed random biases to each neuron while keeping weight decay) would clarify whether the homogeneity is indeed caused by the symmetry or is a side effect of norm reduction. The other two experiments (sparsity and low-rank) are better controlled, so this is a gap in the experimental portfolio rather than a fatal flaw.

3. **The DCS algorithm (Eq. 8) is described but not empirically validated in its general form.** Only one special case (Spred for rescaling symmetry) is cited from prior work. The paper does not test whether the general formulation works for enforcing, e.g., low-rank constraints beyond what the existing theory already predicts. This limits the practical contribution of the algorithmic proposal.

4. **The L1 equivalence argument (Section 2.4) is sketched but not fully worked out.** The change of variables from s to z = s² and the claim about the existence of the right derivative at z=0₊ rely on the second-order expansion derived in Section 2.3, which itself is heuristic. The precise sense of "L1-equivalent" (equivalence of minimizers? dynamics? regularization paths?) is not formalized.

### Trivial
None.

## Nice-to-Haves

- A controlled permutation-symmetry experiment for ResNet (breaking symmetry with random biases) would strengthen the experimental validation.
- Empirical evaluation of the general DCS formulation beyond the Spred special case would increase its practical impact.
- The SGD analysis could be reframed as a heuristic discussion with clear caveats rather than presented as a derivation, or made rigorous under stated simplifying assumptions.

## Removed Points

The following points from the reviewer inputs were removed with justifications:

1. **"The main theorem is presented as a central result, but no proof or even a proof sketch is provided in the main text"** — Removed per instruction: the paper references appendix sections (`\ref{app sec: exp concerns}`, `\ref{app sec: transformer}`), and the parser strips those sections. The proof of Theorem 1 was likely in the stripped appendix. The rule states: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references."

2. **"The mapping from common symmetries to the paper's mirror symmetry is not established"** — Removed. The paper does establish the mapping. For rescaling symmetry with scalars (u,w): choosing ρ = -w/u gives ℓ(u,w) = ℓ(-w,-u) [n₁=(1,1) mirror], and ρ = w/u gives ℓ(u,w) = ℓ(w,u) [n₂=(1,-1) mirror]; for vectors, ρ = -1 gives ℓ(u,w) = ℓ(-u,-w) [O=I mirror]. For rotation symmetry: the rotation group contains all orthogonal matrices, and I-2Π is orthogonal by construction, so invariance under all orthogonal matrices implies invariance under this specific reflection. For permutation symmetry: an explicit projection matrix P is constructed. The critic's specific objections (e.g., that reflection maps are "not rescaling transformations for arbitrary (u,w)") are mathematically incorrect for reasons given above.

3. **"The paper overstates its novelty and scope"** — Removed. The paper acknowledges prior works on each specific symmetry and explicitly states that they studied these case-by-case. The claim "no unifying theory exists" is accurate—prior works did not provide a general theoretical framework connecting all three symmetry types. The related works section clearly delineates what prior work covered and what it did not. The unification itself is the novelty, which the critic acknowledges ("the unified framing could be valuable").

4. **"The experiments do not convincingly isolate the role of symmetry — the matrix factorization experiment does not compare to a version where rotation symmetry is removed"** — Removed as factually incorrect. The paper's Figure 1 caption explicitly states: "The inset shows that the model always stays full-rank if we remove the rotation symmetry by introducing residual connections." The experiment does exactly the controlled comparison the critic demands.

5. **"Missing parts and places to improve" points about proofs not being in the main text** — Removed per the appendix-stripping rule.

6. **Criticisms about the paper being "a position piece rather than a theoretical contribution"** — Removed as this assessment was based on the missing-proof criticism, which is removed.

7. **The statement that "the theory itself is unproven" (in the context of plasticity loss)** — Removed as derivative of the removed proof criticism.

## Novel Insights

The most striking observation from synthesizing the reviews is that the paper's novel contribution—the unified mirror-symmetry framework—is actually validated by the very structure of its own arguments in an interesting way: the fact that all three common symmetry types (rescaling, rotation, permutation) can be instantiated as O-mirror symmetries despite their very different algebraic forms (diagonal scaling group vs. orthogonal group vs. discrete permutation group) itself confirms the generality of the framework. The paper's proof sketches for each case reveal that the common thread is the existence of an involutive transformation (reflection) within the symmetry group, which is a surprisingly uniting property given how different these groups appear on the surface. The fact that the critic's objection to the mapping was mathematically incorrect further reinforces this point—the mapping is natural once one examines the group structure properly. None beyond the paper's own contributions.

## Suggestions

1. **Strengthen the SGD analysis**: Either make Section 2.3 rigorous under clearly stated simplifying assumptions, or reframe it as an intuitive discussion / conjecture with explicit caveats. The current presentation mixes heuristic derivation with confident claims, which undermines the paper's overall rigor.

2. **Add a controlled ResNet experiment**: Compare standard training (weight decay + permutation symmetry) against a version where permutation symmetry is broken (e.g., adding fixed random biases to each neuron's output) while keeping weight decay fixed. This would confirm that the observed homogeneity is symmetry-driven rather than a generic norm-reduction effect.

3. **Evaluate the DCS algorithm**: Apply the general formulation (Eq. 8) to at least one concrete problem beyond Spred (e.g., enforcing low-rank structure in matrix factorization or sparsity in a neural network) to demonstrate practical utility.

4. **Clarify the L1 equivalence**: Formalize what "L1-equivalent" means (e.g., equivalence of minimizer sets, equivalence of regularization paths) and provide a clean argument for the existence of the derivative at z=0₊ without relying on the heuristic SGD analysis.

## Score and Decision

This paper makes a genuine theoretical contribution by unifying three important symmetry types under a common framework and proving that mirror symmetries imply structured constraints. The core ideas are novel and the potential impact is significant. However, the heuristic SGD analysis, limited experimental controls for the permutation symmetry case, and untested algorithmic proposal prevent the paper from being a fully realized contribution. The paper would benefit from a major revision cycle to address these gaps.

**Score**: 6.0

**Decision**: Accept (borderline)

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>