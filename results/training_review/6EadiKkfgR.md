Now I have all the information needed to write the consolidated review.

## Summary

This paper formalizes the concept of semantic equivalence (Definition 2.1) through the lens of conditional label distributions and investigates when contrastive learning can learn representations that encode these equivalence relations. The authors propose a Distributional Alignment Hypothesis (Definition 4.1) connecting contrastive and downstream data distributions, and prove that under this alignment and additional strong assumptions (conditional equivalence, basis condition), optimal contrastive models map semantically equivalent symbols to identical vectors (Corollary 4.3). A controlled experiment on modular addition (ModAdd/CModAdd) verifies that the theoretical predictions hold in a setting where all assumptions are satisfied by construction.

---

## Strengths

- **Formal framework for semantics in contrastive learning.** The paper provides a precise definition of semantic equivalence (Definition 2.1) rooted in conditional outcome distributions, and establishes a theoretical chain (Theorem 4.2 → Corollary 4.3) connecting contrastive conditional equivalence to downstream semantic equivalence under the Distributional Alignment Hypothesis. This offers a clean mathematical foundation for the often-observed but poorly formalized "semantic structure" in contrastive embeddings, complementing prior information-theoretic and latent-variable analyses (Arora et al. 2019; HaoChen et al. 2021).

- **Controlled experiment directly testing the theory.** The ModAdd/CModAdd experimental setup is cleanly constructed so that all theoretical assumptions hold by design. Figure 2a demonstrates that during contrastive training, Euclidean distances between semantically equivalent symbols decrease steadily while non-equivalent distances do not converge, providing direct empirical verification that the mechanism in Theorem 4.2/Corollary 4.3 operates as predicted.

- **Transparent acknowledgment of limitations.** Section 7 ("Threats to Validity") explicitly discusses the strength of the assumptions (conditional equivalence, alignment hypothesis) and acknowledges that verifying the alignment hypothesis is impractical in most real-world settings. The Future Work section (Section 10) identifies relaxation of these assumptions as a necessary next step.

---

## Weaknesses

### Fatal
None.

### Major

- **Scope mismatch between title/framing and the actual method analyzed.** The title "Contrastive Learners Are Semantic Learners" and the abstract's phrasing ("the optimal model for a simple contrastive learning procedure") imply broad coverage of standard contrastive methods (SimCLR, MoCo, etc.). However, the paper analyzes a specific asymmetric variant where one branch extracts a **symbol** (e.g., a cropped patch) and the other extracts its **context**, with separate encoder functions. While the paper calls this "a simple variation of SimCLR" (Section 2.2, lines 59–60), it never discusses whether—or how—standard contrastive learning with random augmentations and symmetric encoders can be cast into this symbol–context framework. A reader expecting an analysis of standard contrastive learning will find the gap substantial, and the paper does not qualify its claims accordingly.

- **The Distributional Alignment Hypothesis builds the conclusion into the premise.** Definition 4.1 directly equates downstream semantic equivalence with contrastive conditional equivalence (∀y,ρ: p_D(y|u,ρ)=p_D(y|v,ρ) ⟺ ∀ρ: p_C(ρ|u)=p_C(ρ|v)). The left side of this biconditional *is* the definition of semantic equivalence (Definition 2.1) for the downstream task. Consequently, Corollary 4.3 largely recapitulates this definitional choice: if the two equivalence relations coincide by assumption, then learning one recovers the other. The non-trivial work is Theorem 4.2 (conditional equivalence → embedding equality), but the alignment hypothesis itself is doing most of the heavy lifting by stipulating that the two tasks' equivalence structures match perfectly. The paper acknowledges this is strong (Section 7) but offers no relaxation, bound on misalignment, or measure of how much the conclusion degrades when alignment is only partial—which is the practically relevant case.

- **Experimental validation is confined to a single toy setting.** The ModAdd task (N=16, k=8) is a minimal synthetic problem where all theoretical assumptions are hand-crafted to hold. The experiments do not include: (a) any evaluation on non-synthetic data, (b) comparison to standard contrastive learning (e.g., standard SimCLR on the same inputs), (c) ablations probing robustness when the conditional equivalence or alignment assumptions are partially violated (e.g., adding noise to context distributions), or (d) tests establishing whether the learned embeddings truly satisfy ℰ*(u)=ℰ*(v) or merely become closer (Figure 2a distances do not converge to zero; the paper offers a plausible explanation but no verification). The classification experiment (Figure 2b) demonstrates only that pre-trained embeddings accelerate early learning on a small dataset—a well-known generic finding that does not specifically validate the semantic equivalence theory.

### Minor

- **The normative claim about "good representations" is under-supported.** Section 6 argues that "good representations should, at a minimum, encode semantic equivalence relations" and claims this is "strongly supported by Figure 2b." However, Figure 2b only shows faster convergence, not that semantic equivalence is the causal mechanism behind the improvement. The claim is positioned as a conclusion rather than a hypothesis to be tested.

- **Theorem 3.1 (the labeled case) is not tested experimentally at all.** The paper introduces the labeled variant but the experiments only validate the unlabeled case (Theorem 4.2 / Corollary 4.3). A quick empirical check of the labeled case would strengthen the paper's completeness.

- **No discussion of how the asymmetric architecture choice affects results.** The paper uses separate encoder and embedding functions (ℰ and E) with parameters that "can be shared, partially shared, or separate" but does not ablate this choice or explain whether the theoretical results depend on the asymmetry.

### Trivial

- The research questions listed at the end of the introduction (lines 16–18) appear truncated or missing in the extracted text.
- Some table descriptions (Tables 1–2) are incompletely rendered, though the intended format is clear from context.

---

## Nice-to-Haves

- A bound or divergence measure that relaxes the alignment hypothesis—e.g., showing that small misalignment between the equivalence relations translates to bounded downstream error—would substantially increase practical relevance.
- A non-synthetic case study where the symbol–context decomposition arises naturally (e.g., masked language modeling with words as symbols and sentences as contexts, or image inpainting with patches) would broaden the paper's reach.
- An analysis of whether standard SimCLR with random augmentations can be seen as a special case of this framework (e.g., both branches extract overlapping "symbols" from the same input under random cropping).

---

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Paper never acknowledges the gap between its method and standard contrastive learning"** — The paper does call its method "a simple variation of SimCLR" and "the variant of SimCLR" (lines 58–60) and describes how the augmentations differ. It acknowledges it is a variant, though it does not discuss whether standard SimCLR fits this framework.

2. **"The notation is heavy without payoff" / "examples are not formalized"** — These are style nitpicks; the formal definition (Definition 2.1) is provided, and the examples are illustrative.

3. **"The proof is deferred to the appendix, so the main text does not help the reader judge correctness"** — The paper discusses the hypotheses and their justification in the main text (lines 73–76, 112, 207–212). Deferring full proofs to an appendix is standard practice.

4. **"The threats to validity section undercuts the paper's central claims"** — Acknowledging limitations is good scientific practice, not a weakness; it strengthens the paper's credibility.

5. **"Paper does not position its contribution relative to existing work"** — The paper does position itself: "Compared to these works, our analysis stems from the notion of semantic equivalence..." (line 222).

6. **Demand for standard benchmark evaluation / scalability experiments** — The paper explicitly scopes its experiments as "a small controlled experiment where the hypothesis of the previous theorem can be easily verified" (line 141). Requests for scale and non-synthetic benchmarks ask the paper to address a different purpose.

---

## Novel Insights

None beyond the paper's own contributions. The reviews largely recapitulate the paper's self-identified limitations rather than offering genuinely novel observations.

---

## Suggestions

1. **Reframe the paper's scope.** Revise the title and abstract to accurately reflect that the analysis studies a specific asymmetric, symbol–context variant of contrastive learning. Explicitly discuss whether (and how) standard contrastive methods like SimCLR with random augmentations fit into this framework, or clarify that the analysis applies only to structured decompositions of inputs into symbols and contexts.

2. **Either relax the alignment hypothesis or strengthen the empirical case.** The theoretical contribution would be significantly more impactful if the paper offered a quantitative bound on downstream error under approximate alignment (e.g., a Lipschitz-style continuity result). Alternatively, if the strong assumptions are to be retained, demonstrate their value by showing that contrastive pre-training under this framework significantly outperforms standard baselines on at least one non-trivially-sized task where the symbol–context structure is natural.

3. **Expand the experimental section.** Add at least: (a) an ablation where the conditional equivalence or basis assumptions are partially violated (e.g., noise injected into context distributions), (b) a comparison to a standard SimCLR baseline on the same data, and (c) a visual embedding projection (e.g., PCA/t-SNE) color-coded by ground-truth semantic classes to directly show the predicted cluster structure.

---

**Originality:** The formalization of semantic equivalence in the contrastive learning context is a genuine conceptual contribution, though the specific approach (studying optimal models under strong equivalence assumptions) overlaps with prior theoretical analyses.

**Importance of research question:** Understanding what semantic structure contrastive learning captures is important, and the question is well-motivated.

**Claims support:** The paper's main claims are supported logically under the stated assumptions, but the experimental support is limited to an idealized toy setting, and the scope of claims outstrips the actual method analyzed.

**Soundness:** The theoretical chain (Definitions → Theorem 4.2 → Corollary 4.3) appears logically sound under the assumptions. The experiments are clean but limited.

**Clarity:** The paper is generally well written, though the scope mismatch between the title/abstract and the actual method is confusing.

**Value to community:** The formal definitions (semantic equivalence, alignment hypothesis) could be useful conceptual tools for future work, but in the current form the paper's practical impact is limited by the strength of its assumptions and the narrow experimental scope.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>