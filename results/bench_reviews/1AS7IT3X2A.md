Now I have a thorough understanding of the paper and calibration anchors. Let me compose the final review.

## Summary

The paper argues that foundation model unlearning (FMU) should shift from data-tracing machine unlearning (which removes specific training data points) to knowledge-tracing FMU (which removes specified knowledge or capabilities), because many FM stakeholders (regulators, enterprise users, end users) lack access to training data and can only express requests at the semantic level. The position is supported by two arguments: a practical stakeholder argument and a cognitive science analogy, and is concretized through a CLIP case study that unlearns fine-grained visual concepts while preserving coarse-grained recognition using existing MU methods with a proposed hinge loss, achieving a 95.20% quality-utility trade-off.

## Strengths

- **Clear, actionable position that addresses a genuine practical gap.** The formalization—unlearning requests as $\mathcal{D}^f \subseteq \{\text{data, knowledge}\}$ with $\mathcal{D}^r = \emptyset$—is precisely defined and captures a real problem: most stakeholders who would issue unlearning requests for FMs cannot identify specific training data points. The stakeholder analysis in Section 3.1 and Figure 2 makes a concrete, relevant case for why the data-tracing formalization breaks down for FMs.

- **The case study operationalizes the abstract position convincingly.** Unlearning fine-grained classes (e.g., Audi A1) while preserving coarse-grained recognition (e.g., "car") at 95.20% Q-U score demonstrates that knowledge-level unlearning requests can be translated into workable algorithms without access to original training data, using only 30–50 proxy images per target class (Table 4). The hierarchical retention setup and hinge loss formulation (Equation 1) are technically sound contributions.

- **Table 1 provides a useful comparative framework** that crystallizes six dimensions of difference between data-tracing MU and knowledge-tracing FMU, making the position easy to assess and debate.

## Weaknesses

### Major

- **The claimed paradigm shift is less sharp than presented—existing FMU work already operates at the knowledge level, and the paper's own case study confirms this continuity.** The paper frames knowledge-tracing as a departure from data-tracing, but several cited works—Eldan & Russinovich (2023) removing "Harry Potter" knowledge, Gandikota et al. (2023) erasing concepts from diffusion models, and the broader model editing literature—already specify unlearning targets as concepts, capabilities, or behaviors rather than individual training data points. More critically, the paper's case study converts knowledge-level requests ("unlearn Audi A1") into data-level problems by collecting exemplar images and applying existing data-tracing MU methods (gradient ascent, NPO, task vectors, etc.). The paper itself acknowledges in Section 5: "we anticipate that the unlearning methods in the proposed knowledge-tracing paradigm will still rely on data for unlearning." This means the "paradigm shift" is primarily about the *input specification* (who requests unlearning and what language they use) rather than fundamentally different unlearning methodology. The position would be stronger and more honest if it centered this insight—reframing the interface between requesters and unlearners—rather than claiming a paradigm departure. Additionally, Table 1 claims knowledge-tracing FMU has no retention set, yet the case study constructs $\mathcal{D}_{\text{Parent}}^r$ (Section 4.1.2), which functions as a retention set derived from the forgetting set's parent classes, contradicting the formal claim.

### Minor

- **The cognitive science argument adds little weight.** Section 3.2 draws an analogy between human forgetting at multiple levels of abstraction and knowledge-tracing FMU. However, as the paper's own counterargument in Section 5 acknowledges ("Airplanes fly in a way different from how birds fly"), the fact that human forgetting operates at the knowledge level provides no evidence that machines *should* or *can effectively* unlearn at the knowledge level. The analogy is not developed into a reasoned argument—it remains a suggestive connection. This does not undermine the position, which stands primarily on practical grounds, but it weakens one of the paper's two stated pillars of support.

- **The definition of "knowledge" is treated as self-evident, limiting the generality of the proposal.** The case study equates knowledge with class labels in a taxonomy, which works for visual classification but leaves open how knowledge-tracing FMU would handle more complex or entangled forms of knowledge (e.g., factual associations, reasoning abilities, behavioral tendencies). The paper does not substantively engage with the mechanistic interpretability or knowledge editing literatures that grapple with what constitutes "knowledge" in neural networks, despite citing them. This is understandable given scope, but it means the proposal's most challenging cases remain underspecified.

### Trivial

- None.

## Nice-to-Haves

- A deeper engagement with the model editing / knowledge editing literature beyond Section 6's brief paragraph, analyzing whether knowledge-tracing FMU is genuinely distinct from or complementary to those efforts.
- Empirical or analytical evidence about actual stakeholder needs (e.g., analysis of real unlearning requests, regulatory documents, or industry use cases) to strengthen the practical argument.
- A more explicit acknowledgment that many recent FMU papers already operate at the knowledge/concept level, and an analysis of what knowledge-tracing FMU adds beyond recognizing this de facto trend.

## Removed Points

- *Critic demanded novel experiments, baselines, and ablations beyond what the case study provides.* Removed because this is a position paper; the case study is illustrative, and demanding additional empirical validation is misapplying standard research paper criteria.
- *Critic claimed the paper overclaims "paradigm shift."* The strong framing is appropriate for a position paper. However, the legitimate underlying concern—that the distinction from existing work is not as sharp as presented—is preserved as a Major weakness above, reframed as a substantive argument issue rather than a rhetorical overclaim.
- *Critic claimed the case study section reads like a standard research contribution rather than position paper evidence.* This is a style concern masquerading as a weakness; position papers are allowed to include case studies.
- *Critic claimed the stakeholder argument is "asserted without evidence" and lacks interviews or regulatory analysis.* Position papers can argue from reasoning and examples without primary empirical evidence. The practical argument is plausible and coherent; additional evidence would strengthen it but is a Nice-to-Have, not a Major weakness.
- *Strength finder claimed "cognitive science grounding" as a strength.* Filtered down—the cognitive science section provides context but is not a strong argumentative pillar, as analyzed in Minor Weakness.

## Novel Insights

The most interesting tension in the paper is actually underexploited: the case study's construction of $\mathcal{D}_{\text{Parent}}^r$ reveals that knowledge-tracing FMU doesn't eliminate retention sets—it *derives* them from the knowledge hierarchy. This suggests a more nuanced position than the paper states: knowledge-tracing FMU's real contribution may be that it allows retention sets to be *inferred from the knowledge specification itself* rather than requiring access to training data. This reframing—which would make the "paradigm shift" about automatic derivation of what to preserve from what to forget—is arguably more precise and defensible than the current framing.

## Suggestions

- Reframe the position to center the insight that knowledge-tracing FMU is about *who can specify unlearning and how*, rather than claiming it replaces data-tracing methods. Acknowledge that many existing methods already work at the knowledge level and focus the contribution on the formalization of the request interface and the derivation of constraints (like the parent retention set) from the knowledge specification itself.
- Correct the inconsistency in Table 1 regarding the retention set—the case study explicitly constructs one, so claiming $\mathcal{D}^r = \emptyset$ is misleading. Clarify that knowledge-tracing FMU *derives* the retention specification from the knowledge hierarchy rather than requiring training data access.

## Score and Decision

**Calibration anchors:**
- **High (≥6):** mfd6GRW4Az (6.0, oral) — ML unlearning position paper with strong policy analysis; PegEYWWXvx (6.0) — FM paradigm shift with case studies
- **Medium (~5):** 8ZH52QHIZV (5.33, reject) — XAI paradigm shift that reviewers found was mainly reframing of existing work; xnNHXepQ9h (5.33, accept) — adaptive sensing paradigm shift with case studies
- **Low (≤4):** FJF1sa6elQ (3.33, reject) — evaluation hierarchy as literature review; g8Fo6qtnMR (4.0, reject) — expert orchestration as relabeled routing/MoE

This paper is stronger than the low anchors (it has a clear position, formalization, and supporting case study, unlike pure literature reviews or relabelings). It is comparable to the medium anchors—like 8ZH52QHIZV, it claims a paradigm shift that is arguably a reframing of existing practice, but it has a more concrete and technically sound case study. It falls short of the high anchors because those papers either had deeper policy/normative analysis (mfd6GRW4Az) or more substantively novel frameworks. The paper's position is worth discussing but the gap between the "paradigm shift" framing and the actual contribution (reformulating the unlearning request interface) brings it below the clear-accept threshold.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>