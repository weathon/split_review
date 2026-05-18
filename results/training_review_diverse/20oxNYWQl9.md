Now I have a thorough understanding of the paper and all review inputs. Let me produce the final consolidated review, carefully verifying each claim against the paper.

---

## Summary

This paper proposes a data selection algorithm that combines $(k,z)$-clustering with sensitivity sampling to select a representative subset of training data under Hölder continuity of the loss. The core theoretical result (Theorem 5) shows that with only $O(k + 1/\varepsilon^2)$ model inferences, the weighted average loss of the selected sample approximates the full-dataset average loss up to a multiplicative $(1\pm\varepsilon)$ factor plus an additive term $\varepsilon\lambda\Phi_k$, where $\Phi_k$ is the $k$-means clustering cost. The paper also provides an $r$-round adaptive extension (Theorem 6), a discussion of linear regression (Section 4), and experiments on CIFAR-10, MNIST, and a gas sensor regression dataset showing competitive or superior performance compared to uniform sampling, $k$-center coresets (Sener & Savarese, 2018), and leverage score sampling.

## Strengths

- **Theoretical guarantee that improves on prior $k$-center coreset bounds**: Theorem 5 proves a bound where the additive error depends on the $(k,z)$-clustering cost $\Phi_k$, which can be much smaller than the $n \cdot \max\text{-distance}$ bound implied by the $k$-center approach of Sener & Savarese (2018). This directly addresses the outlier-sensitivity issue raised in the introduction, since $(k,z)$-clustering with small $z$ is more robust than $k$-center.

- **Very low inference cost in terms of model loss queries**: The algorithm requires only $O(k + 1/\varepsilon^2)$ queries to the loss function (Theorem 5). This sublinear number of loss evaluations is a concrete advantage over methods that must query many or all points, and directly tackles the second limitation (costly inference) noted in Section 1.

- **Principled lower bound motivating the adaptive approach**: Theorem 4 provides a lower bound showing that uniform sampling cannot achieve error better than $\varepsilon n \sup \ell$ under only Hölder continuity, theoretically justifying the need for adaptive sampling. The paper connects this to the proposed method in Section 3.2.

- **General applicability beyond classification**: The paper formulates the problem for general loss functions (Definition 2), extends to linear regression (Section 4, Assumption 8), and shows experimental results on both classification and regression tasks. This addresses the fourth question from the introduction regarding limitations of prior work to classification only.

- **Empirical outperformance on standard benchmarks**: On CIFAR-10 and MNIST, the proposed loss-based and gradient-based sampling consistently achieve higher validation accuracy than both uniform sampling and the $k$-center coreset of Sener & Savarese (2018), especially at small sample sizes (Figure 2). On the gas sensor regression task (Figure 1), clustering-based sampling performs nearly on par with leverage score sampling while being drastically faster.

- **Novel synthesis of clustering and sensitivity sampling**: The combination of $(k,z)$-clustering with sensitivity sampling (Feldman & Langberg, 2011) for data selection is a genuinely different algorithmic idea from prior $k$-center coresets, validated both theoretically and empirically.

- **Adaptive multi-round extension**: Theorem 6 shows that with $r$ rounds of $k$ queries each, the additive error can be reduced to $\varepsilon\lambda\Phi_{k\cdot i}$, providing a trade-off between query budget and round complexity.

## Weaknesses

### Fatal
None.

### Major

- **The regression section (Section 4) lacks theoretical guarantees**. Unlike the main classification setting, no theorem is provided for linear regression. The paper states assumptions (Assumption 8) and sketches an algorithm, but presents no bound of the form $\Delta(S) \leq \dots$. The empirical result on one dataset (gas sensor) is promising but stands without formal backing. This makes the regression contribution feel incomplete relative to the paper's stated goal of providing a "more generic data-selection algorithm."

- **The experimental protocol for neural networks does not cleanly align with the theoretical setting.** In Section 5.2, the algorithm uses a warm-start model trained on $k' = 0.2k$ random points, then queries $k'' = 0.2k$ cluster centers for loss values, and extrapolates to sample the remaining points. This involves a multi-stage process (initial model training, then loss extrapolation) that goes beyond the single-round fixed-loss setting of Theorem 5. The paper does not clarify whether or how the theoretical guarantees apply to this warm-start, multi-stage procedure, nor does it isolate the effect of the sensitivity sampling component from the initial training phase.

- **The claimed $\Delta(S)$ formulation is not fully justified as a proxy for the actual learning objective.** The paper claims (Section 2.1) that "proving a bound on $\Delta(S)$ implies the result of Sener & Savarese (2018) (under their assumption about the model loss)," but this claim is neither argued nor proven. Sener & Savarese's goal is to bound generalization error of a model *retrained* on the coreset, not just the empirical loss approximation on a fixed model. The paper's loss approximation guarantee does not directly translate to retraining guarantees without additional assumptions that are not stated. The paper acknowledges the definitional difference but overclaims the implication.

### Minor

- **The inference cost claim ($O(k + 1/\varepsilon^2)$) does not account for the cost of obtaining embeddings.** The paper claims only $O(k + 1/\varepsilon^2)$ inferences from the model, but to compute the clustering used in the algorithm, one needs embeddings for every data point. If these embeddings come from the model itself (e.g., last-layer representations), this requires a forward pass for all $n$ points, making the total cost $O(n + k + 1/\varepsilon^2)$. The paper does mention that embeddings might come from a "generic all-purpose embedding" model (line 120), but this cost is still nonzero and should be acknowledged for honest comparison with baselines.

- **The theoretical bound's additive term ($\varepsilon\lambda\Phi_k$) is not discussed in practical regimes.** The bound is only meaningful when $\Phi_k$ (the clustering cost) is small relative to the total loss. The paper acknowledges this dependency but provides no discussion of when this holds (e.g., for well-clustered embeddings where classes are separable). Without this context, a reader cannot assess the practical relevance of the guarantee.

- **Algorithm pseudocode is referenced (Algorithm 1, Algorithm 2) but not present in the main text.** While the high-level procedure is described in prose (Section 1.1 and Section 5.2), the formal algorithms referenced in the paper are not included. This makes it harder for the reader to verify the exact procedure.

- **The lower bound (Theorem 4) is presented but not used to prove optimality.** The lower bound shows that uniform sampling fails without adaptive queries, which motivates the adaptive approach. However, no matching lower bound for the adaptive setting is provided, so the optimality of the proposed method is not established.

- **Minor notation issue in Theorem 5**: The bound states $\Phi_k(X)$ where the text later clarifies $\Phi_k(\mathcal{D})$ — a small inconsistency.

### Trivial
- Section numbering: Section 1.1 is used after Section 1, which is non-standard.
- Theorem 4 states "there is a constant $c_{:}$" — a typesetting artifact.

## Nice-to-Haves
- A brief discussion of regimes where $\Phi_k$ is small (e.g., scaling laws for well-separated clusters) would help contextualize the bound.
- An ablation isolating the effect of sensitivity sampling vs. clustering alone would strengthen the experimental evaluation.
- Reporting the cost of embedding computation alongside inference cost would give a more complete picture of computational requirements.

## Removed Points

- **"Algorithm not specified in main text — fatal omission"** (Harsh Critic #1, severity downgraded): The algorithm IS described at a high level in Section 1.1 and concretely in the experimental protocol (Section 5.2). The formal pseudocode (Algorithm 1, Algorithm 2) was likely in the appendix, which the parser strips from all papers. The description is adequate to understand the method. Remains as a **minor** weakness about pseudocode not being in main text, not a fatal omission.

- **"Circularity in theoretical guarantee"** (Harsh Critic #2): This criticism misunderstands the bound. The expression $\Delta(S) \leq \varepsilon(\sum\ell(e) + 2\lambda\Phi_k)$ is a standard multiplicative-plus-additive guarantee, not circular. The total loss appearing on both sides is by design — it defines a relative error bound. This is not a weakness.

- **"Lower bound not connected to the rest of the paper"** (Harsh Critic "Other Observations"): Section 3.2 explicitly states "The lower bound on $\Delta(S)$ in theorem 4 shows is that one must sample more carefully if good guarantees are desired." The connection is clearly stated. Removed as factually incorrect.

- **"The $k$-center guarantee translates into $n \cdot \lambda \cdot \max$"** — the reviewer's own comparison with $k$-center actually supports the paper's claim about improved robustness. Not a weakness.

- **"Missing related works"**: Per instructions, I cannot verify this without external sources.

- **"Typo in X vs D"** (originally presented as a sign of sloppiness): Downgraded to Trivial as a minor notation inconsistency.

## Novel Insights

None beyond the paper's own contributions. The combination of clustering and sensitivity sampling with Hölder continuity assumptions is itself the main novel contribution.

## Suggestions

1. **Include a formal algorithm statement in the main text** (even a brief pseudocode box) detailing the 1-round procedure: (a) compute $(k,z)$-clustering, (b) query loss on centers, (c) extrapolate via Hölder continuity, (d) sample remaining points via sensitivity sampling. This would remove ambiguity.

2. **Acknowledge and discuss the cost of embedding computation** explicitly. Clarify that the $O(k + 1/\varepsilon^2)$ claim refers specifically to loss-function inferences, and state the additional cost incurred for embeddings in the total runtime.

3. **Either provide a theorem for the regression setting or explicitly scope it as empirical only.** The current Section 4 promises theoretical backing ("Following our theoretical analysis in Section 4") but delivers none.

4. **Discuss regimes where $\Phi_k$ is practically small** (e.g., separable classes in embedding space, scaling with $k$ for natural data distributions) to ground the additive term in the theoretical bound.

5. **Clarify the relationship between the experimental warm-start protocol and the theoretical guarantees**, or explicitly note that the experiments go beyond the theory's assumptions.

---

## Score and Decision

**Originality**: Strong. The synthesis of $(k,z)$-clustering with sensitivity sampling for data selection under Hölder continuity is novel and well-motivated.

**Importance**: High. Data selection and coreset construction are central problems in efficient training of large models.

**Claims support**: Moderate. The theoretical claims are clear and plausible but would benefit from formal algorithm statements. The experimental support is promising but the protocol diverges from the theoretical setting.

**Soundness**: Moderate. The theory appears sound based on the stated results, though proofs are absent from the main text (likely in the appendix). The empirical methodology is reasonable but lacks ablations to isolate contributions.

**Clarity**: Fair. The high-level ideas are clear, but the lack of algorithm pseudocode and unclear relationship between theory and experiments reduce clarity.

**Value**: Good. The approach is a principled alternative to $k$-center coresets with clear advantages in outlier robustness and theoretical generality.

The paper has genuine contributions — a novel algorithmic idea with theoretical backing and promising empirical results. The weaknesses are real but not fatal: the regression section lacks theoretical closure, the experimental protocol doesn't cleanly match the theory, the embedding cost is unaccounted for, and algorithm pseudocode should be in the main text. These are addressable with revision.

**Score**: 6.0 — A solid paper with clear contributions and room for improvement in presentation and completeness.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>