## Summary
This position/philosophy paper challenges the "black box" metaphor widely used to characterize neural networks. The central argument is that XAI discourse implicitly assumes *correlative continuity* — that causal continuity across a system guarantees the existence of individuatable intermediary features correlating with the target output. Using the example of a potter's clay exhibiting a self-propagating wobble that reappears after a pause (with no recoverable intermediate "wobble-encoding" feature in the static clay), the author argues this assumption is a fallacy, and that neural network "opacity" may not be opacity at all — there may simply be no hidden features to find. Three consequences are drawn: a resolution of the "secret owls" subliminal learning puzzle (Cloud et al., 2025), implications for AI trust discourse, and a call to revise the language of opacity.

---

## Strengths

- **Genuinely original conceptual move**: The distinction between *causal* continuity and *correlative* continuity is precisely formulated and historically grounded. The point that our expectation of intermediary correlates is a contingent empirical regularity — not a necessary metaphysical truth — is philosophically interesting and underappreciated in the XAI literature.
- **Elegant motivating example**: The potter's clay analogy is well-chosen; it is a low-level, physical, non-behavioral system that avoids the contested terrain of intentionality and high-level causation, and the argument that no feature of the still clay at t₂ "encodes" the oscillation frequency is intuitively compelling.
- **Well-scoped application**: Using Cloud et al.'s (2025) subliminal learning study — where an LLM's owl preference is transmitted through semantically void number sequences — as a worked example grounds the philosophical argument in a concrete, contemporary empirical puzzle.
- **Appropriate intellectual humility**: The paper repeatedly acknowledges that the clay-style explanation is not guaranteed for every neural network case, and correctly notes that degrees of correlative continuity are both system- and feature-dependent.

---

## Weaknesses

### Fatal
None.

### Major

1. **The analogy between clay and neural networks may be structurally disanalogous in the key dimension.** Clay is a materially homogeneous, continuously deformable medium with genuinely holistic intermediate dynamics. Neural networks, by contrast, have clearly *individuated* intermediate states — weight matrices and activation vectors with specific, fully determined numerical values. Even if these intermediate states are not human-interpretable, they constitute precisely defined mathematical objects. The student model's weights, after training on the owl-teacher's number sequences, *do* differ in measurable, in-principle-detectable ways from a model trained on sequences from a non-owl teacher. This is not merely a practical limitation; it is, in principle, a statistical signal. The paper never demonstrates that the neural network case falls on the "clay" side of the spectrum rather than the "gene-before-DNA" side (where intermediary features exist but are not yet understood). The dismissal of the intermediary state with "the overall form of the data set" is persuasive for clay but far less obviously correct for discrete, parameterized systems.

2. **The paper attacks a stronger version of the assumption than most XAI researchers hold.** The XAI literature's frustration is not typically that hidden features *must exist* (and cannot be found); it is that we cannot find *human-interpretable* or *causally explanatory* features among those that do exist. The paper conflates "no individuatable correlate exists" with "no interpretable correlate exists." Most XAI work already accepts that no clean, human-interpretable correlate will be found, and is working on approximations. The paper's philosophical reframing (ontological gap vs. epistemic gap) does not obviously change this research agenda or undermine its justification.

3. **The practical consequences in Section 3 are underdeveloped relative to the strength of the claim.** The paper presents three consequences but then substantially walks them back. Section 3.2 explicitly admits: "the dissolution of opacity does not alone resolve disputes concerning trust." Section 3.3 says the effects will be "subtle and diffuse." For a paper arguing that a central metaphor in XAI is a "myth" built on a "fallacy," the consequence analysis offers little that is actionable or surprising. It is unclear what, concretely, ML researchers should do differently in response to the paper's argument.

### Minor

- The central empirical hook (Cloud et al., 2025) is a very recent arXiv preprint (arXiv:2507.14805). The strength of the subliminal learning effect and the plausibility of the mechanism are not independently established, and the paper builds the "owls" case study heavily on it. The hedging in footnote 15 ("to develop this argument effectively would require a paper of its own") makes the connection to the argument somewhat programmatic rather than substantive.

- The "god's eye view" thought experiment in Section 2.3 is the philosophically pivotal moment — the claim that even an omniscient observer could not individuate a wobble-correlated feature in the still clay — but it is asserted rather than argued. A more careful treatment would address why the holistic form of the clay truly resists feature individuation at all granularities, rather than just at human-accessible granularities.

### Trivial
None worth noting.

---

## Nice-to-Haves
- A more rigorous comparison of clay versus neural network intermediate states: do weight matrices of LLMs differ detectably (e.g., via CKA, probing classifiers, or activation statistics) between owl-trained and non-owl-trained variants? If they do, this would count as correlative continuity and partially undercut the argument. Engaging this possibility directly would strengthen the paper considerably.
- The paper would benefit from a sharper characterization of which XAI methods or claims actually presuppose correlative continuity in the strong form being attacked, rather than treating the assumption as uniform across the field.

---

## Novel Insights
The paper's genuinely novel contribution is the importation of a philosophy-of-science concept — the non-necessity of correlative continuity in causal chains — into the ML explainability discourse. The specific claim that opacity-language in XAI rests on an implicit and unjustified metaphysical assumption (that causal pathways must be traceable through individuatable intermediary features) is a novel and pointed critique. The clay example, while not from ML, provides an unusually clean illustration of a counterexample that avoids the murkiness of biological or social causation. Whether this insight ultimately survives the disanalogy objection is the core open question, but the framing itself is a contribution not previously articulated with this precision in the ML literature.

---

## Suggestions
- Address directly whether the distributed numerical state of a trained LLM (weight matrices) constitutes a "correlative" intermediate feature. The paper needs to either argue that weight matrices cannot serve this role (they are "holistic" in the relevant sense) or explain why their existence does not save correlative continuity.
- Engage with mechanistic interpretability work (circuits, superposition, features as linear components) — these efforts are premised on *finding* individuatable correlates in neural networks. The paper should explain whether this work is (a) misguided because no such correlates exist, or (b) sometimes successful, in which case the fallacy is more local than claimed.
- Make the three consequences more concrete and actionable for ML practitioners; even one clearly falsifiable prediction or one change in methodological practice would greatly strengthen the paper's value to ICLR readers.

---

## Score and Decision

This is a philosophically stimulating position paper making an original conceptual argument. Its core logical move — distinguishing causal from correlative continuity — is sound and underappreciated. However, the transfer of that argument to neural networks rests on a structural analogy (clay ≈ neural network intermediate state) that is not adequately defended against the obvious objection that neural network weights are discrete, individuatable, and in-principle statistically detectable. The practical consequences drawn are vague and partially self-undermined. For an ML venue specifically, the lack of actionable implications for the research community is a significant gap. The paper reads as a first pass at an important argument that needs further elaboration before it can sustain its strong claims.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>