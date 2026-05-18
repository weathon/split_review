Confirmed. Section 7 contains the heading, four research questions (Q1–Q4), and nothing else before Section 8 — zero tables, zero figures, zero numbers. Now I'll produce the final review.

---

## Summary

This paper proposes SPG, a neuro-symbolic framework that factors the learning of inductive spatial concepts (e.g., staircase as towers of increasing height) from few demonstrations into three stages: (i) Sketch — an LLM generates a coarse program signature from natural language; (ii) Plan — MCTS searches for grounded action sequences guided by a physical-reward function, accelerated by neural pruning and macro-actions from a concept library; (iii) Generalize — an LLM distills the grounded plan into a general inductive program for the concept library. The idea of decoupling these objectives is conceptually well-motivated and targets a genuine challenge in embodied concept learning.

## Strengths
- **Principled factorization of the concept-learning problem.** The Sketch–Plan–Generalize decomposition cleanly separates the distinct subproblems of signature inference (LLM), grounded search (MCTS with neural pruning), and program abstraction (LLM), each of which has different computational demands and failure modes. This is a genuine conceptual contribution over prior work that entangles these objectives. (Sections 5, Figure 2)
- **Formal definition of inductive spatial concepts.** Equation 1 provides a recursive decomposition (induction term, composition term, base term) that gives the learning objective (Equation 2) clear structure and distinguishes the paper's scope from prior concept-learning work that does not model physical construction. (Section 4)
- **Modular and efficient plan search design.** The combination of macro-actions from a growing library (reducing plan length) with a neural action predictor that prunes primitive actions (reducing branching factor from |A_c|+|A_p| to |A_c|+1) is a well-reasoned approach to scaling search as the concept library grows. (Section 5.2)
- **Continual learning via a growing concept library.** The curriculum-learning setup (primitives → simple structures → complex compositions) and the mechanism of adding learned programs back into L for reuse are sensible design choices for hierarchical concept acquisition. (Section 5.3)

## Weaknesses

### Fatal
- **No experimental results are presented.** Section 7 (Results) contains the heading, four research questions (Q1–Q4), and nothing else — zero tables, zero figures, zero quantitative or qualitative outcomes. The paper then transitions directly to Section 8 (Conclusion), which asserts "Extensive evaluation demonstrates accurate program learning and stronger generalization" without any supporting data having been shown. A paper whose central claims — outperforming LLM-only and neural baselines, generalizing out-of-distribution, enabling embodied instruction following — are entirely unsubstantiated cannot be accepted. The method description may be interesting, but without results it is a proposal, not a completed contribution.

### Major
- None. The fatal flaw above is dispositive; additional major issues are speculative without results to ground them.

### Minor
- **Neural action predictor is under-specified.** The `move_head(direction)` primitive is described as "trained on a corpus of pick-and-place instructions" (Section 5.2) with only a citation to prior work. The paper does not explain what training data is used, what supervision signal is employed, or how this predictor generalizes to unseen spatial configurations. Since the claimed efficiency gain (branching factor reduction) depends critically on this component's reliability, this is a gap in the method description.
- **"Quasi-symbolic" grounding module is vague.** The visual grounding module (Section 5.1) is described at a high level (ResNet-34 extractor, concept embedding module, quasi-symbolic executor with "filter" behaviors). The term "quasi-symbolic" is not defined, and it is unclear what is learned vs. hard-coded, and how this module interfaces with the LLM's output. References to prior work (Mao et al., 2019; Kalithasan et al., 2023; Wang et al., 2023c) do not clarify which capabilities are assumed.
- **Continual learning: unclear whether neural components are retrained.** The paper states (Section 5) that upon learning a new concept, "L ← L ∪ H*". Since downstream searches use `Make_<cpt>(size)` as macro-actions, it is unclear whether adding a new concept requires retraining the neural action predictor or grounding module, or whether the library is purely symbolic.
- **Formalism coverage of claimed concept types is unclear.** The formal definition (Equation 1) uses a single induction term with exponent λ ∈ {0,1}. The paper claims to handle structures like "boundary," "arc-bridge," and "x-shaped patterns" (Section 6), but does not show how these fit the single-induction-term template or whether they require multiple induction terms or nested compositions.

### Trivial
- The reference to "A.3," "A.4," "A.5" in Section 5 and "C.3" in Section 5.2 refer to appendix content that was stripped by the parser. While the guidelines assume the appendix exists, the main paper would benefit from inline summaries of key details.

## Nice-to-Haves
- Should the paper be resubmitted with results, it would benefit from an ablation isolating the contribution of Sketch (LLM-only), Plan (MCTS search), and Generalize (LLM abstraction) separately, so the reader can see which component drives the improvement.
- Search efficiency numbers (wall-clock time, node expansions) would make the claimed scalability concrete.

## Removed Points
- Harsh critic's criticism about the lack of detail on how the "quasi-symbolic executor's pre-defined behaviors" are obtained: the paper cites prior work (Mao et al., 2019; Kalithasan et al., 2023; Wang et al., 2023c) which is standard for modular components. This is a minor specificity preference, not a substantive flaw.
- Strength Finder's claim that "Strong inductive generalization demonstrated through systematic evaluation" (Strength #3) and "Demonstrated applicability to embodied instruction following" (Strength #6): these claimed strengths cite Section 7 and the abstract, but Section 7 contains no results data. These strengths are unsupported and removed.
- The harsh critic's point about the appendix being "essential" and stripped: the parser stripping appendices is a known artifact; we assume the appendix exists per guidelines. The criticism about missing appendix content is removed.
- The harsh critic's point about Dataset III generalization split not specifying whether test structures are qualitatively different: the paper does state Dataset III "includes concepts of larger size than those in training to test generalization" (Section 6), which addresses the question. This point is removed as the paper already answers it.

## Novel Insights
None beyond the paper's own contributions. The three-stage factorization (Sketch–Plan–Generalize) is the core idea, but without results it cannot be assessed as a validated insight.

## Suggestions
- **Include a complete experimental section** in any resubmission. At minimum: tables of program accuracy, IoU, and MSE for all datasets; comparisons against all four baselines; ablations of MCTS components (P, L, neural pruning); and efficiency measurements (search time, node expansions).
- Clarify the training setup for the neural action predictor — what data, supervision, and generalization properties it has.
- Define "quasi-symbolic" more precisely and specify which components of the visual grounding module are learned vs. hard-coded.
- Explain whether adding a new concept to the library requires retraining any neural components.
- Show how each claimed structure type (boundary, arc-bridge, x-shaped patterns) maps onto the formal definition in Equation 1.

## Score and Decision

**Originality:** The Sketch–Plan–Generalize factorization is a novel and well-reasoned decomposition of the inductive concept-learning problem.  
**Importance of research question:** Highly relevant — enabling embodied agents to learn grounded spatial concepts from few demonstrations is an important open problem.  
**Claims supported:** Not at all. The paper makes strong claims about outperforming baselines and generalizing out-of-distribution, but provides zero experimental evidence.  
**Soundness of experiments:** Cannot be evaluated — no experiments are reported.  
**Clarity of writing:** Generally clear method description, but the missing results section makes the paper feel incomplete.  
**Value to the community:** The conceptual framework has merit, but in its current form the paper provides no validated contribution.

The paper proposes an interesting conceptual framework but contains no experimental results whatsoever. The central claims — that the method outperforms LLM-only and purely neural baselines, generalizes inductively, and enables embodied instruction following — are entirely unsubstantiated. A method paper without results cannot be accepted. The fatal flaw overrides all strengths.

MY FINAL SCORE: <pineapple>1.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>