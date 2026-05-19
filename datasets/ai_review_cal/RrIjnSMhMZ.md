- Decision: Reject
- Avg Score: 2.50
- Scores: 1, 5, 1, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces **meta specification** as an alternative design principle for open-ended learning systems (OELS), where the underlying system is defined implicitly through constraints on a generalized representation space rather than through explicit enumeration. The core mechanism is a **watchmaker function** — a generalized stochastic evolution function — paired with verification routines that enforce realizability and validity. The paper contributes a formal unified framework for describing OELS (Section 2), the meta specification concept with implicit system definition via rejection sampling (Section 4), and an illustrative implementation co-evolving robot morphologies (URDF) and robotic tasks (PyBullet code) using an LLM-based watchmaker function (Section 5).

## Strengths

1. **Formal unified framework for OELS (Section 2).** The paper provides explicit, well-structured formalizations of agent and task subsystems (\( \mathcal{S} = \langle S_A, S_T \rangle \)), evolution functions, progress monitors (\( E_A, E_T \)), controllers (\( O_A, O_T \)), and the distinction between the dynamical system and control mechanism. This gives the community a common language for describing and comparing diverse OELS implementations — a genuine conceptual contribution.

2. **Novel concept of meta specification with formal implicit system definition (Section 4).** The idea of defining a system through constraints on a generalized representation space rather than explicit enumeration is clearly articulated. The mathematical formulation — \( \mathcal{X}_{\mathcal{R}} = \{x \in \mathcal{V} \mid \Delta_{\mathcal{R}}(x)=1\} \) with \( \Phi_{\mathcal{X}_{\mathcal{R}}}(x' \mid x) \propto \Phi_W(x' \mid x) \Delta_{\mathcal{R}}(x') \) — cleanly captures how a watchmaker function paired with verification implicitly defines a valid system. The insight that verification can be less complex than generation (Section 4.3) is well-motivated.

3. **Connection to foundation models is timely and interesting.** The observation that LLMs can serve as generalized evolution functions over rich representation spaces (DSLs, code, URDF) bridges the gap between the conceptual framework and a practical instantiation, pointing to a concrete research direction.

4. **Transparency about limitations.** Section 5 explicitly notes that training is omitted, a control mechanism is absent, and the implementation is "only the underlying dynamical system" serving to illustrate potential rather than to demonstrate a complete OELS. This honesty is commendable and makes the paper's actual claims clearer.

## Weaknesses

### Major

- **No evidence supporting the central claim that meta specification reduces design complexity.** The paper repeatedly asserts that meta specification can "significantly expand the space of possibilities while reducing design complexity" (abstract, Sections 1, 6), but provides zero measurement, comparison, or even a proxy for design complexity. No explicit-specification baseline of comparable scope is constructed for comparison. How much designer effort went into the prompt engineering? How does the verification routine complexity scale compared to direct specification? Without any evidence on this axis, the paper's primary motivational claim remains an unsupported intuition. This is the most significant gap because it is central to the paper's value proposition.

### Minor

- **The "demonstration of viability" considerably overreaches what is shown.** While the paper is transparent that the implementation lacks agent learning and a control mechanism, it nonetheless uses this demonstration to claim "viability" of the meta specification principle. What is actually shown is that an LLM can generate diverse robot morphologies and task descriptions that pass basic validity checks — a static generation pipeline, not an open-ended learning system. The step from "LLMs can produce diverse valid outputs" to "meta specification enables OELS" is large and unbridged. The paper would benefit from toning down "viability" claims to match what is actually demonstrated.

- **"Emergent novelty" is supported only by qualitative/visual inspection.** The paper reports observing "ant-like creatures," "horse-like quadrupeds," and "Walker machines" (Section 5), describing the diversity verbally and with three example images. No quantitative novelty metric (behavior characterization distance, archive coverage, phylogenetic diversity) is used. While qualitative examples are useful for illustration, the claim of "emergent novelty" as evidence for the approach requires stronger grounding.

- **No analysis of the watchmaker function's sample efficiency or operational cost.** The ~40% validity rate is reported, but there is no discussion of how many LLM calls were needed per valid output, the cost per evolutionary step, or how this would scale. For a system using GPT-4 per evolution step, these are critical practical concerns.

- **No ablation of the verification routines.** The paper does not analyze how the system behaves without verification, which constraints are responsible for most rejections, or whether the verification routines are overly conservative (rejecting valid states). The interplay between the watchmaker and verification — central to the approach — is not empirically characterized.

- **LLM selection is motivated only by "an intriguing connection."** No justification is given for why GPT-4 specifically is appropriate as a watchmaker function, how its stochasticity relates to the required conditions, or whether a smaller/cheaper model could suffice. Given that the watchmaker function is the key enabler of the approach, this choice deserves deeper analysis.

### Trivial

None.

## Nice-to-Haves

- A small-scale comparison with an explicit specification baseline (even a manually parameterized space of comparable range) would substantially strengthen the design-complexity claim.
- Discussion of which classes of constraints resist automatic verification and how partial verification could be handled would round out the contribution.
- Details of prompt structure and prompt engineering effort (currently deferred to App. C, which is stripped by the parser) would aid reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Watchmaker functions are never formally defined / conditions C1, C2 are missing."** — The paper's Section 4.1 states that watchmaker functions "must satisfy certain conditions" and then Section 4.2 explicitly says "Recall that (C2) stipulates that, in expectation, there is a ε probability that the watchmaker function produces valid and realizable outputs." This proves C2 was defined and that conditions were present in the original paper. Their absence from the parsed text is a PDF-extraction artifact. The harsh critic's assertion that "C1, C2, and any others are referenced nowhere" is factually wrong for C2. Removed.

2. **"The space of possibilities is undefined and unmeasured."** — The paper formally defines the space of possibilities in Section 2 as the Cartesian product of agent and task spaces, and in Section 4 as \( \mathcal{X}_{\mathcal{R}} = \{x \in \mathcal{V} \mid \Delta_{\mathcal{R}}(x)=1\} \). The claim that this quantity is "undefined" misunderstands the formalism. The separate criticism that the reachable fraction is not analyzed is valid and is retained as a minor weakness above. The "undefined" part is removed.

3. **Criticisms about missing appendix content (App. A, B, C).** — The parser strips these sections. They exist in the original submission. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. However, the reviewer process surfaces an important observation: the paper's framing conflates two distinct claims — (a) that meta specification is a viable OELS design principle, and (b) that LLMs can serve as watchmaker functions within it. The evidence for (b) is stronger than the evidence that (b) implies (a). The paper would benefit from more sharply distinguishing these two claims and calibrating its conclusions to each.

## Suggestions

1. Add at least a minimal quantitative evaluation of design complexity — even a coarse metric like "number of designer-specified constraints/parameters" compared to an explicit specification baseline — to substantiate the paper's central claim.
2. Either include a proxy for learning (e.g., a few gradient updates per evolved agent) to close the loop, or explicitly reframe the paper as introducing a design principle with a preliminary generation-only plausibility check, removing "viability of OELS" language.
3. Report the number of LLM API calls, cost estimates, and the per-constraint rejection rate from verification to ground the practical feasibility discussion.
4. Replace qualitative novelty claims with at least one quantitative diversity measure (e.g., pairwise behavior distance, archive coverage).
