---
job_id: 2f18cc80-2b4d-4c11-aed8-6f8ece1cb937
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 1FCZ4f8dAY.pdf
paper: Tensor Learning with Orthogonal, Lorentz, and Symplectic Symmetries
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies equivariant machine learning architectures and learning theory for tensor-valued functions, with applications to physical sciences and time series.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including Abstract, Introduction with related-work discussion, methodological sections (Sections 2 to 4), experiments and quantitative results (Section 5, Tables 1 to 3), and a concluding discussion (Section 6). While I found several exposition and notation issues, especially around some equations and statement details, these do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, instructions targeting automated reviewers, or other manipulative content in the provided paper text or figure content.

# Expected Review Outcome:
## Summary
This paper develops characterizations of tensor-to-tensor equivariant functions under diagonal actions of several classical groups, first for polynomial $O(d)$-equivariant maps and then for entire functions under indefinite orthogonal groups, including Lorentz, and the symplectic group. The main practical message is that these characterizations lead to explicit parameterizations of equivariant models, with experimentally instantiated versions applied to stress-strain prediction, path signature estimation, and sparse vector estimation.

## Strengths
The paper has a real mathematical core. The main theorem in Section 3, especially **Theorem 1** on Page 5 and the more practical **Corollary 1** on Pages 5 to 6, gives a concrete invariant-theoretic parameterization of equivariant tensor polynomials. This is not just a vague universality claim, the authors spell out the construction via tensor products, contractions, and isotropic tensors. For readers who care about building actual models rather than only abstract representation-theoretic existence, this is a meaningful contribution.

I also appreciate that the paper goes beyond $O(d)$ and attempts a unified treatment of indefinite orthogonal and symplectic symmetries in **Section 4**. Even though some details are deferred, the move from compact orthogonal symmetry to Lorentz/symplectic settings is interesting and broadens the relevance of the framework, especially for physics-flavored applications.

The paper does a decent job connecting the theory to implementable architectures. In particular, **Figure 1** on Page 7 is helpful: it makes the structure in **Corollary 1 / Equation (11)** much more concrete by showing the two branches, invariant scalar coefficients from pairwise dot products, and tensor-product basis elements built from inputs plus isotropic tensors. This figure supports the authors’ claim that the theory is not merely formal, it visually clarifies the recipe used later in experiments.

There is also a nice specialization result for symmetric matrices in **Corollary 2** on Page 6. Reducing an $O(d)$-equivariant function on symmetric matrices to a permutation-equivariant map on eigenvalues is elegant and leads to a practical architecture for the material science task. This is one of the most convincing bridges between the abstract theory and a simple model design.

The empirical results are generally favorable. In **Table 1** on Page 8, the gains on the stress-strain task are substantial across all training-set sizes, and the comparison against both a plain MLP and an augmented MLP makes the sample-efficiency argument more credible. Likewise, in **Table 2** on Page 9, the path-signature model substantially outperforms all listed MLP baselines for both the orthogonal and Lorentz settings. Even in the more mixed sparse-vector setting, **Table 3** on Page 10 shows that the equivariant learned model can be competitive or best in several non-ideal regimes where the fixed SoS-inspired baselines are no longer strongest.

The paper is also generally well motivated and places itself against relevant lines of work, including invariant-theory approaches and Clebsch-Gordan / irrep-based methods. I appreciated the direct discussion on Page 3 comparing the proposed parameterization to e3nn/escnn-style constructions.

## Weaknesses
1. **There are several mathematical and notation-level errors in the main paper, and some are not cosmetic.**  
   The most obvious one is on **Page 4, immediately after Equation (5)**, where the transformation rule for a $2_{(+)}$-tensor is translated into matrix notation as
   \[
   g\cdot b = M(g)\, b\, M(g)^{\frac{1}{2}},
   \]
   which is clearly inconsistent with the preceding index expression and should presumably be $M(g)\,b\,M(g)^\top$. This is not a minor typo in an appendix, it appears in the main exposition right after introducing the core tensor action. For a paper centered on explicit tensor transformation rules, such an error matters because it undermines confidence that the notation has been checked carefully.

   A second issue appears in **Corollary 3, Equation (21) on Page 8**, where the outer sum is written as
   \[
   \sum_{t=0}^{\lfloor \frac{1}{2}\rfloor},
   \]
   which cannot be right since it should depend on the output order $k$, analogous to Corollary 1. Again, this is in a central theorem-like statement. When theorem statements contain malformed bounds, readers are left to reverse-engineer the intended result. For a mathematically heavy paper, that is a real presentation and verification problem.

2. **Some theoretical claims are broader than what is cleanly justified in the main paper, and too much of the burden is pushed to the appendix.**  
   The core compact-group averaging argument for **Theorem 1** is understandable from the main text plus the appendix. However, the leap to non-compact groups in **Section 4**, especially the generalization to equivariant entire functions in **Theorem 2** on Pages 7 to 8, is much harder to assess from the main paper alone. The authors say the “full generalization” is in Appendix G, but the main text gives only a compressed statement and then immediately treats it as ready-to-use. Since the non-compact case is one of the stated headline contributions, I would have liked at least a more explicit explanation in the main paper of why the compact averaging trick has a valid replacement and what assumptions are essential.

   Relatedly, the step from polynomial characterizations in Section 3 to entire-function characterizations in Section 4 feels under-motivated from an ML perspective. The actual models in experiments use MLP-parameterized scalar coefficient functions, not literal globally convergent Taylor expansions. The bridge from “entire” to practical networks is therefore conceptually looser than the paper suggests.

3. **The practical scalability of the proposed parameterization is a serious concern, and the paper acknowledges it only partially.**  
   On **Page 6**, right after **Equation (11)**, the authors state the direct evaluation complexity as
   \[
   \mathcal{O}\!\left(k'! n^{k'}(Qdn^2 + d^{k'})\right).
   \]
   That is already a warning sign. The method is combinatorial in the output order and input count, and the architecture relies on enumerating many tensor-product basis terms and permutations. The paper says this is practical only for small $k'$, which is honest, but it also means the claimed generality is quite a bit ahead of the demonstrated practicality. The experiments stay in low-order settings where this enumeration is manageable, so the paper does not really establish that the framework is useful for genuinely higher-order tensor learning beyond small handcrafted cases.

   This matters because the paper repeatedly positions itself as a generic recipe for tensor-to-tensor equivariant learning. Right now, it is more accurate to say it gives a generic characterization, with practical instantiations only in restricted low-order regimes.

4. **The empirical section is promising but not broad enough to support some of the stronger comparative claims.**  
   The comparisons in **Tables 1 to 3** are mostly against plain MLPs, augmented MLPs, a task-specific prior method (TFENN), and SoS-inspired hand-designed maps. That is a reasonable starting point, but it is not enough to establish that this invariant-theoretic construction is competitive with broader modern equivariant-network frameworks. The paper discusses e3nn/escnn-style methods in the introduction, and also mentions Pearce-Crump’s Brauer-group-equivariant networks, but none of these are included experimentally. Since one of the core claims is that the proposed parameterization provides a usable alternative to representation-theoretic constructions, the lack of direct empirical comparison to such architectures weakens the practical significance.

   This is especially relevant for the Lorentz setting in **Table 2**. The authors claim strong Lorentz-equivariant behavior, but only compare to non-equivariant MLPs and augmentation. A stronger test would compare against a Lorentz-equivariant baseline from the literature or at least a generic matrix-group-equivariant construction.

5. **The experimental methodology leaves open fairness and robustness questions.**  
   In several places, the paper compares models with different parameter counts or different inductive-bias strengths. For example, **Table 4** in the appendix shows the stress-strain models are approximately parameter matched, which is good, but the main paper’s **Table 1** relies partly on published TFENN numbers rather than a unified reimplementation. For path signatures, **Table 5** shows “same width” and “same # params” baselines, which is helpful, but the main paper does not discuss variance or stability beyond three trials in **Table 2**, and those datasets are very small, 1024 trajectories each. For sparse vector estimation, **Table 3** is interesting, but the learned model labeled “Ours” has a very large parameter count according to **Table 6** in the appendix, much larger than the MLP baseline. The main text does not really discuss whether the performance gains in some rows come from symmetry, capacity, or both.

   Put differently, the experimental story is suggestive rather than airtight. The paper demonstrates that symmetry helps relative to weak baselines, but it does not yet isolate the exact source of gains as cleanly as it could.

6. **Some results are mixed, and the discussion does not sufficiently analyze failure modes.**  
   **Table 3** on Page 10 is not uniformly favorable to the full method. There are several rows, especially diagonal or identity covariance cases, where “Ours” is substantially worse than either SoS or the diagonal variant. For instance, under Bernoulli-Gaussian with identity covariance, the SoS baseline reaches $0.962 \pm 0.002$ while “Ours” is only $0.342 \pm 0.043$. That is not a small gap. The caption does mention an exception, but the paper does not really unpack why the full pairwise-inner-product architecture underperforms so sharply in some structured regimes. If anything, these rows suggest the model may overfit or fail to exploit the right sufficient statistics in regimes where the theory-driven SoS maps are well aligned with the problem.

   I would have liked a sharper discussion of when the richer equivariant parameterization helps, and when it hurts. Right now, the sparse-vector section sometimes reads like a broad success story, while the table is more nuanced.

7. **The exposition is often harder than it needs to be, even for a mathematically mature audience.**  
   There are many places where notation is overloaded or slightly inconsistent. On **Page 4**, Equation (5) uses $\pi$ in the exponent, although the surrounding definitions use $p$ for parity. In **Appendix B**, index names fluctuate and there are a few typographical inconsistencies such as $k_{t_1,\ldots,t_r}$ versus $k_{\ell_1,\ldots,\ell_r}$ on **Page 19**. In **Section 4**, the notation shifts from parity labels to arbitrary characters $\chi$ in a way that is mathematically reasonable but pedagogically abrupt. These are all survivable, but they add friction.

   More importantly, several practical modeling choices are under-explained in the main paper. For example, when **Remark 1** says the coefficient functions $q_{t,\sigma,J}$ are implemented as MLPs, the paper does not explain in the main text how parameter sharing is organized across indices and permutations, except later in task-specific appendix material. Given that the architecture is one of the advertised outputs of the theory, this implementation bridge deserved more space in the main paper.

8. **The positioning relative to prior work is solid but still incomplete in a key direction.**  
   The paper does discuss representation-theoretic and Brauer-algebra-related approaches, which is good. Still, the contrast to broader reductive-group-equivariant neural-network frameworks is underdeveloped, particularly for the Lorentz and symplectic claims. Since the paper’s stated advantage is not only mathematical characterization but also practical architecture design, it should do more to explain what is genuinely easier, more expressive, or more implementable here compared to these more general frameworks.

9. **The figure is helpful conceptually, but it also reveals a gap between theory and implementation complexity.**  
   Returning to **Figure 1** on Page 7, the visualization clearly shows that even for $4$ input vectors and a rank-2 output, the basis already includes all ordered input tensor products plus isotropic terms. The figure succeeds as an explanatory device, but it also makes visible how quickly the basis size grows. This supports one of my concerns above: the paper has a strong characterization result, yet the figure unintentionally highlights that the construction may become unwieldy very fast. I think the authors should lean into this and discuss basis pruning, structured sharing, or low-rank approximations more explicitly.

## Questions
1. For the typo-level but important issues in the main theory statements, can the authors explicitly confirm and correct the intended formulas in **Page 4 after Equation (5)** and in **Corollary 3 / Equation (21)**? A clean erratum-style clarification here would materially increase my confidence in the technical presentation.

2. Can the authors explain more concretely, in the rebuttal, what part of the non-compact-group argument is essential for **Theorem 2** beyond “see Appendix G”? In particular, what assumptions are truly needed for the averaging replacement, and are there cases where the theorem would fail without them?

3. How are the scalar networks $q_{t,\sigma,J}$ parameterized in practice across different tuples $(t,\sigma,J)$? Are they all independent, partially shared, or generated by a smaller shared network? A concise description of the sharing scheme and resulting parameter growth would help evaluate the architecture more fairly.

4. Regarding **Table 3**, can the authors provide a more precise explanation for the rows where the full “Ours” model performs dramatically worse than SoS or the diagonal variant, especially the Bernoulli-Gaussian identity-covariance case? Is this due to optimization, sample complexity, architectural mismatch, or something else?

5. Can the authors comment on whether their framework can be combined with basis selection or low-rank truncation strategies to mitigate the combinatorial growth implied by **Equation (11)** and visually apparent in **Figure 1**? Even a discussion would help clarify how far the method can scale beyond the present toy-to-medium settings.

6. A direct comparison to at least one stronger equivariant baseline, especially for the Lorentz setting, would substantially increase my confidence. If such experiments already exist, even at small scale, they would strengthen the paper.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
3: good. The central claims are mostly supported, and the mathematical direction is serious, but several errors in theorem statements / notation and the limited empirical breadth keep me from a 4.

## Presentation Rating
2: fair. The paper is readable and motivated, but there are too many notation inconsistencies and a few genuine formula errors in the main text for me to call the presentation good.

## Contribution Rating
3: good. The invariant-theoretic characterization of equivariant tensor maps across these symmetry groups is valuable and relevant to the ICLR community, even if the practical evidence is narrower than the general framing suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a meaningful theoretical contribution and promising experiments, and I can see it making a useful poster. That said, the main-text mathematical typos, some under-explained theoretical steps, and the limited breadth of empirical comparisons keep it from being a comfortable accept.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and carefully checked the main mathematical statements and empirical evidence, although some appendix-heavy arguments would still benefit from author clarification.