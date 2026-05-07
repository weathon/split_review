Now I have a thorough understanding of the paper and calibration anchors. Let me write the final review.

## Summary

The paper argues that Explainable AI (XAI) is "causal discovery in disguise": the true Structural Causal Model (SCM) of the data-generating process constitutes the ground truth for all explanations, and XAI's persistent lack of consensus stems from failing to recognize and pursue this target. The paper categorizes XAI methods into data-based (Q1–Q2), model-based (Q3–Q4), and decision-based (Q5–Q6) questions, maps these onto observational, interventional, and counterfactual causal queries respectively, and states formal necessity and sufficiency theorems to ground its claim. It then discusses practical challenges and future directions including concept discovery, relation discovery, and interactive approximate modeling.

## Strengths

- **Clear, provocative position on a topic of genuine contemporary interest**: The claim that "XAI is causal discovery in disguise" is crisp, debatable, and speaks directly to a widely acknowledged problem—XAI's lack of consensus and ground truth. The reframing is engaging and invites productive disagreement.
- **Systematic mapping of XAI questions to causal query types**: The categorization of XAI into Q1–Q6 (data/model/decision) and the mapping to observational/interventional/counterfactual queries (Figure 1, Sections 2.1–2.3) provides a genuinely useful organizing framework that allows practitioners to locate their methods within a causal hierarchy and identify implicit causal commitments.
- **Concept-alignment spectrum identifies a concrete under-appreciated gap**: Section 5.1's spectrum from "fully specified concepts" (e.g., SHAP on tabular features) to "low-level features" (e.g., pixel-level saliency maps) pinpoints a real limitation—explanations in low-level features may be causally faithful but explanatorily useless, and concept-based methods like TCAV cannot discover "unknown unknowns."
- **Honest engagement with practical limitations**: Section 4.1 candidly details faithfulness, causal sufficiency, sample complexity, and Markov equivalence class challenges that make obtaining the true SCM infeasible in practice.

## Weaknesses

### Fatal
None.

### Major

- **The central theorems are circular, formalizing a tautology rather than proving the substantive claim**. Definition 4.1 states: "we say an answer to any of the six core XAI questions (Q1–Q6) is accurate and complete if it coincides exactly with what the true Structural Causal Model (SCM) M predicts for that query." Given this, Theorem 4.2 (sufficiency) simply says: the true SCM produces answers matching the true SCM. Theorem 4.3 (necessity) says: a different model differs on at least one query from the true SCM. Both are trivial consequences of the definition. What would be needed to support the paper's claim is an independent argument for *why* XAI questions should be answered by the true SCM—e.g., showing that non-SCM-based explanations systematically fail at their intended purposes. The abstract promises a "proof" of necessity and sufficiency, but the formalism delivers a definitional stipulation, not an argument. This is the paper's stated core contribution, and its hollowness significantly undermines the position.

- **The paper equivocates between explaining the model f and explaining the world's SCM M**. The paper explicitly distinguishes f (the predictive model) from M (the world's causal model) in footnote 1 (line 61: "f represents the predictive model to be explained, distinct from the causal model of the world, M"). Yet Q3 ("How does the model transform inputs to outputs?") and Q4 ("How do the model's internal mechanisms function?") are questions about f's behavior, not about M. The paper claims M answers these by "tracing causal pathways in G" (line 171), but a model's internal mechanisms (e.g., which features f relies on, how its weights operate) need not correspond to the world's causal structure—a biased model that relies on spurious correlations can be perfectly explained ("this model uses feature X because its weights assign it high importance") without any reference to M. The paper does not address why understanding model behavior requires the world's SCM rather than the model's own structure, and this unaddressed distinction is central to evaluating whether "XAI is causal discovery in disguise."

- **The paper concedes its own necessity claim, reducing the position to a weaker and less distinctive form**. Section 4.1 (lines 362–370) states: "correlation-based explanations (e.g., feature importances, saliency maps) may suffice when the goal is to detect patterns, biases, or anomalies rather than to enable interventions" and "the required level of causal grounding depends on the stakeholder's objective." If non-causal methods suffice for some legitimate XAI purposes, then causality is not *necessary* for XAI—it is necessary for a specific subset of XAI use cases. The position then softens from "XAI is causal discovery in disguise" to "some explanations benefit from causality," a far more modest claim that much prior work already endorses (including work the paper itself cites: Karimi et al., 2021; Beckers, 2022; Chou et al., 2021).

### Minor

- **The mapping from XAI methods to causal queries is asserted rather than argued in Section 2**. For instance, the paper claims attention mechanisms "align closely with the principles of causal discovery" because they "focus on key features" (line 79)—this is a loose analogy, not a demonstration that attention constitutes or requires causal discovery. Similarly, the claim that feature interaction methods are "closely related to understanding causal mechanisms" (line 99) requires more than assertion. These assertions are important because they underpin the "in disguise" thesis, yet they receive no analytical support.

- **The Section 5 recommendations are generic**: "Develop robust causal discovery algorithms," "advance causal representation learning," "promote interactive explanations" follow from any position that causality matters for XAI, not specifically from the "in disguise" framing. They do not help distinguish this paper's thesis from the weaker claim that "causal reasoning would improve XAI."

### Trivial
None worth listing.

## Nice-to-Haves

- A worked example showing how even an approximate causal model yields better explanations than a non-causal method on a concrete task would illustrate the practical import of the position, which is currently absent.
- Direct engagement with the "interpreting the model vs. interpreting the world" objection: when f and M differ (as they nearly always do), explaining f's behavior requires understanding f, not M. Addressing this head-on would substantially strengthen the argument.
- Explanation of why inherently interpretable models (e.g., short decision trees used as explanations) constitute "causal discovery in disguise"—the paper lists such methods (Section 2.2) but doesn't connect them to its thesis.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Overclaiming in the abstract about proving necessity and sufficiency"**: The abstract says "we prove the necessity and sufficiency of causal models for XAI." While the proofs are indeed circular (see Major weakness above), the provocation of claiming proof is within the norms of position papers. The substantive problem is the circularity itself, not the strength of the wording. Moved because "overclaiming" complaints about strong language are disfavored for position papers.
- **"Not enough empirical evidence"**: The paper takes a conceptual/argumentative approach using formal definitions and theorems. Demanding empirical validation is not appropriate for a position paper whose method is reasoning. The circularity of the reasoning is the issue, not the lack of experiments.
- **"Missing related works"**: Cannot verify whether specific related works exist; removed per rules.
- **"Paper is partly a literature review"**: Sections 2–3 do survey prior work, but this is standard background-setting for a position paper that then builds an argument on top. The paper does take a clear position and argues for it, so it is not merely a literature review.

## Novel Insights

The concept-alignment spectrum (Section 5.1) is a genuinely novel and useful observation: current XAI methods vary from operating on semantically meaningful features to low-level features like pixels, and explanations in the latter category may be causally faithful but explanatorily useless because they lack alignment with human concepts. This reframing suggests that the XAI community's evaluation debates are partly about the wrong thing—fidelity to model behavior vs. alignment with human-interpretable concepts—and that concept discovery (not just attribution) is a prerequisite for useful explanation. This insight stands independently of the paper's main thesis.

## Suggestions

- Replace Definition 4.1 with an independent criterion for "accurate and complete" XAI answers—e.g., one grounded in the purpose of the explanation (intervention, debugging, compliance)—and then show that only causal models satisfy this independent criterion. This would make the theorems non-tautological and dramatically strengthen the paper.
- Explicitly address the model-vs-world distinction: clarify whether Q3/Q4 are questions about the model f or about the world M, and if about f, explain why the world's SCM is needed rather than f's own structure. This is the most important objection the paper must confront.
- If the paper maintains that causality is necessary only for *actionable* explanations (as Section 4.1 suggests), state this as the position explicitly rather than claiming necessity for all XAI. A more constrained but defensible claim would be more valuable than a sweeping but undermined one.

## Score and Decision

Calibration anchors examined:

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| 8Ow7kh78fk (Strong AI methodology, entirely circular definitions, no substance) | 2.33 | This paper is substantially better: it has a clear position, useful organizational framework, honest limitations discussion |
| R6TXwNF1SB (Pillars of skill-acquisition, vague tautological pillars) | 3.0 | This paper is better: the Q1-Q6 framework and concept-alignment spectrum have real content |
| FJF1sa6elQ (Model multifacetedness, definitions-then-trivial-conclusions) | 3.33 | This paper is comparable but slightly better: its organizational contribution and honest limitations discussion add value |
| Omq9tUouSS (Symbolic systems, circular definitions used as argument) | 3.67 | Comparable: both have circular formalisms but this paper has more substantive discussion |
| 0TRVB5ghCR (Plausibility in XAI, avg 5.0) | 5.0 | This paper is slightly weaker: that paper had a more targeted, independently defensible claim |
| dVKcLgcCLZ (Causality for evaluation, well-argued with concrete CATs) | 6.67 | This paper is substantially weaker: dVKcLgcCLZ argued a similar "causality as framework" position but with concrete, non-circular conceptual tools (CATs) and case studies |

This paper sits in the 4–5 range. It has genuine strengths—a clear provocative position, a useful organizational framework (Q1-Q6 mapping), and the concept-alignment spectrum insight—but its central formal contribution (the theorems) is circular, it equivocates between explaining the model and explaining the world, and it concedes its own necessity claim. These are not minor presentation issues; they undermine the core argument. However, the paper is not empty or incoherent like the lowest-scoring anchors (2.33–3.0); it provides real conceptual value through its organizing framework. I place it at 4.5, above the purely circular papers but below papers with independently defensible arguments.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>