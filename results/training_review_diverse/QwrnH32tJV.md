Now I have a thorough understanding of the paper and can verify the reviewer claims directly against the text. Let me synthesize the final review.

---

## Summary

This paper develops a theoretical framework for identifiability of concepts when data come from multiple classes of observations. The core idea is that pairwise and local comparison across classes — inspired by cognitive development — can recover hidden concepts without parametric assumptions on concept types, functional relations, or generative models. The main results are: (1) Theorem 1/Proposition 1 show that unique concepts between any class pair (or local set) can be disentangled from others; (2) Theorem 2 proves that under a Structural Diversity condition (Assumption 1), all class-dependent concepts are identifiable up to element-wise invertible transformations and a permutation; and (3) Proposition 3 shows the hidden class–concept structure matrix M is recoverable without the Structural Diversity condition. Experiments on synthetic data (with ground-truth MCC) and real-world datasets (Fashion-MNIST, AnimalFace, Flower102) support the theory.

## Strengths

1. **Nonparametric identifiability result (Theorem 2).** The paper proves that class-dependent concepts can be identified up to element-wise invertible transformations and a permutation under the Structural Diversity condition, without assuming linearity, additivity, disjoint Jacobians, or parametric generative models. This is a genuine advance over prior work that required such restrictions (e.g., Rajendran et al. 2024; Brady et al. 2023; Lachapelle et al. 2023).

2. **Flexible partial identifiability via local comparison (Theorem 1, Proposition 1).** The framework supports identification of subsets of concepts even when global conditions fail, as long as sufficient local diversity exists. Most prior identifiability results are all-or-nothing — this flexibility is a meaningful extension.

3. **Nonparametric recovery of the hidden class–concept structure (Proposition 3).** The paper shows the binary structure matrix M can be recovered up to row permutation without requiring the Structural Diversity condition, going beyond concept identification to the problem of discovering latent dependency structure.

4. **Synthetic validation with ground truth.** The synthetic experiments (Fig. 4, 5) directly measure Mean Correlation Coefficient (MCC) against known ground-truth concepts and show that models respecting the theory's structural conditions substantially outperform the base model. This provides direct empirical support for the identifiability claims.

5. **Honest discussion of assumptions and limitations.** The paper explicitly discusses when Structural Diversity may fail (e.g., breeds of dogs sharing all concepts), compares its assumptions to prior work, and acknowledges that its assumption does not supersede prior approaches but offers a complementary direction.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1's conditions are stated in terms that reference the estimated model, creating a clarity problem for a theory paper.** The condition in Theorem 1 involves $\hat{\mathcal{D}}_{:,i}$ (the support of the *estimated* model's Jacobian) and requires a matrix $\mathrm{T} \in \mathcal{T}$, where $\mathcal{T}$ is defined through the relationship $D_{\hat{\mathbf{c}}}\hat{g} = \mathbf{T} D_{\mathbf{c}}g$ between estimated and true quantities. The paper's "Discussion on Assumptions" attempts to argue this is mild, but the theorem's preamble as stated requires the reader to verify conditions that depend on the unknown estimator. In standard identifiability results, assumptions should be stated in terms of the ground-truth process alone. Following Lachapelle et al. (2022) and Zheng et al. (2022), this may be a proof-structure issue resolvable with clearer presentation, but in the current form it undermines the reader's ability to independently assess the theorem's meaning. **The paper should rewrite the condition so it either (a) refers only to the true data-generating process, or (b) explicitly states it as a condition on the proof that is provably satisfied when the model matches the distribution.**

### Minor

2. **Real-world experiments demonstrate interpretability, not identifiability.** The paper states that real-world experiments "validate our theoretical results" and that results "indicate that hidden concepts can be identified." However, the real-world datasets (Fashion-MNIST, EMNIST, AnimalFace, Flower102) lack ground-truth concept sets, so no measure of identifiability (e.g., MCC against true concepts, uniqueness across runs, or consistency with the Structural Diversity condition) is provided. The visual concept galleries show that learned representations are semantically meaningful — but interpretability is not the same as identifiability. Many prior methods produce equally interpretable vectors without any theoretical guarantees. The synthetic experiments (which do have ground truth and MCC measurements) are the proper validation of the theory; the real-world section should be presented as a demonstration of practical applicability rather than as evidence for identifiability.

3. **No proof sketch in the main text.** For a paper whose primary contribution is theoretical, the main text contains no high-level outline of the proof arguments for any theorem. A concise sketch (e.g., why Jacobian-spanning combined with class diversity leads to an invertible transformation between estimated and true variables) would significantly improve reader comprehension and allow assessment of plausibility without diving into the appendix. The paper currently reads more like a discussion of results than a technical paper.

4. **The Structural Diversity condition could benefit from a more detailed comparison with prior identifiability conditions.** The paper does compare its approach to prior work (lines 122–123, noting differences from sparsity assumptions and the $2n_A+1$ domain requirement), but a dedicated subsection or table contrasting what existing results require (e.g., number of domains from Hyvärinen et al. 2024; properties of conditional densities from Khemakhem et al. 2020; restrictions on mixing functions) with what the proposed theory requires would clarify the novel contribution. The paper claims prior work lacks "general theoretical support" for concept learning, which somewhat overstates the gap given that existing nonlinear-ICA results are also about latent-variable identifiability with auxiliary variables.

5. **Partial identifiability is not developed into a practical diagnostic.** The paper stresses that local comparison enables identification of *some* concepts even when global conditions fail (Theorem 1, Proposition 1). But it does not discuss how a practitioner would know *which* concepts are identifiable without already knowing the structure M. A diagnostic for practitioners, or at least a discussion of what can be inferred from data alone, would greatly increase practical value.

### Trivial

6. **Dense notation without a running example.** Section 2 introduces many symbols ($\mathcal{D}$, $\tau$, $\mathcal{T}$, $\hat{\mathcal{D}}$, $\mathcal{F}$, $\mathcal{T}_f$, $\operatorname{supp}$, $\mathbb{R}^n_S$) in rapid succession. A running example throughout this section (beyond Example 1 which appears only once) would reduce the cognitive burden significantly.

## Nice-to-Haves

- A dedicated table comparing Structural Diversity to prior identifiability conditions (minimum number of domains/classes, whether the mixing function is constrained, whether concept types are restricted).
- A discussion of how the structure M is obtained in practice — is it learned jointly with the concepts or assumed known? If learned jointly, does the optimization face local minima challenges?
- An empirical diagnostic for partial identifiability on synthetic data, showing that when Structural Diversity fails for some concepts, those concepts have lower MCC while others maintain high MCC.

## Removed Points

- **Criticism that Theorem 1 is "ill-posed" or "structurally flawed":** While the presentation is confusing and needs clarification, this is a clarity issue rather than a logical contradiction. The paper discusses why the condition is mild/automatically satisfied, and the approach follows established techniques (Lachapelle et al. 2022; Zheng et al. 2022). The reviewer's characterization as a "structural flaw that undermines the theorem's stated generality" overstates the severity — the issue is presentation, not correctness. Retained as Major weakness 1 with appropriate severity.

- **Criticism that the paper overstates the novelty because prior nonlinear-ICA results already cover similar scenarios:** The paper does cite and distinguish itself from these works (e.g., lines 122–123, noting the $2n_A+1$ domain requirement in prior work). The criticism is partially valid — a more detailed comparison would strengthen the paper — but the claim that prior work "already cover many of the scenarios the paper targets" is itself an overstatement given the paper's nonparametric treatment of concept types and generative processes. Retained as Minor weakness 4 with adjusted framing.

- **"Nonparametric" terminology concern:** The paper's usage is consistent with the nonlinear-ICA literature. This is a terminological preference, not a substantive weakness.

- **Formatting/style nitpicks** about notation density: Retained as Trivial weakness 6 with substance preserved; the formatting complaint itself is removed.

- **Missing proof sketch:** This is a genuine issue for a theory paper. Retained as Minor weakness 3.

- **Strength Finder's claim about "cognitive grounding":** This is a framing device rather than a technical strength. Moved here.

## Novel Insights

The reviews do not surface insights beyond the paper's own contributions. The core observation — that identifiability can be achieved through the structural pattern of class–concept diversity alone, without parametric assumptions on the generative process or concept types — is the paper's own contribution, not something the reviewers add.

## Suggestions

1. **Rewrite the conditions of Theorem 1** to state them entirely in terms of the true data-generating process, or explicitly clarify that the conditions involving $\hat{\mathcal{D}}$ are proof-internal and provably satisfied. This is the single most important fix for the paper's credibility.

2. **Reframe the real-world experiments** as demonstrations of applicability rather than validations of identifiability. Acknowledge explicitly that without ground-truth concepts, these experiments illustrate semantic interpretability and cross-environment consistency, but do not directly measure identifiability.

3. **Add a proof sketch** (6–10 sentences) for Theorem 2 in the main text, explaining how Jacobian-spanning combined with Structural Diversity leads to disentanglement.

4. **Add a comparison table** showing what existing identifiability results require (domain count, sparsity, linearity, etc.) vs. what the proposed theory requires, to clearly delineate the novel contribution.

5. **Provide a running example** throughout Section 3, such as a simple 2-class, 2-concept case with explicit matrices $M$, Jacobians, and supports, to help readers navigate the dense notation.

## Score and Decision

The paper tackles an important problem — provable identifiability guarantees for concept learning — and offers genuinely novel theoretical results (nonparametric identifiability through structural diversity, flexible partial identifiability via local comparison, recoverability of the latent structure). The synthetic experiments provide direct validation. The main weaknesses are presentational (Theorem 1's conditions are confusingly stated, no proof sketch, real-world claims overreach slightly) rather than structural. None of the identified weaknesses invalidate the paper's core theoretical contribution. The paper would benefit from revisions, but in its current form it represents a solid theoretical contribution that advances the state of the art in concept identifiability.

**Score: 6.5** — A solid paper with genuine theoretical contributions, weakened by presentation issues in the statement of the main theorem and some overclaiming in the experiments, but clearly above the acceptance threshold.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>