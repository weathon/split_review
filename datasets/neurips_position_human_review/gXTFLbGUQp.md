# Military AI Needs Technically-Informed Regulation to Safeguard AI Research and its Applications

- Decision: Accept
- Scores: 5, 9, 7

## Abstract
Military weapon systems and command-and-control infrastructure augmented by artificial intelligence (AI) have seen rapid development and deployment in recent years. 
However, the sociotechnical impacts of AI on combat systems, military decision-making, and the norms of warfare have been understudied. 
We focus on a specific subset of lethal autonomous weapon systems (LAWS) that use AI for targeting or battlefield decisions. 
We refer to this subset as AI-powered lethal autonomous weapon systems (AI-LAWS) and argue that they introduce novel risks—including unanticipated escalation, poor reliability in unfamiliar environments, and erosion of human oversight—all of which threaten both military effectiveness and the openness of AI research.
These risks cannot be addressed by high-level policy alone; effective regulation must be grounded in the technical behavior of AI models. 
We argue that AI researchers must be involved throughout the regulatory lifecycle.
Thus, we propose a clear, behavior-based definition of AI-LAWS—systems that introduce unique risks through their use of modern AI—as a foundation for technically grounded regulation, given that existing frameworks do not distinguish them from conventional LAWS.
Using this definition, we propose several technically-informed policy directions and invite greater participation from the AI research community in military AI policy discussions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the concept of AI-powered Lethal Autonomous Weapon Systems (AI-LAWS) and argues that these systems, distinguished by their reliance on machine learning for targeting, decision-making, or coordination, pose unique and urgent risks that current legal and policy frameworks fail to address. These risks include brittle generalization, opacity in decision processes, escalation in conflict zones, and the erosion of scientific openness due to civil-military entanglement. The authors propose a behavior-based definition for AI-LAWS, grounded in their actual function rather than vague notions like “full autonomy” and advocate for technically informed governance. They offer concrete policy recommendations such as banning AI control over nuclear weapons, establishing international validation standards, rejecting AI-based battlefield command (“AI generals”), and safeguarding civilian AI infrastructure and academic independence. The main argument of the paper is that current policies for regulating autonomous weapons fail to address the real-world risks introduced by modern AI systems, and that regulation must be grounded in technical behavior with direct involvement from AI researchers.

### Strengths
This paper excels in presenting a timely, well-structured, and technically grounded argument for the need to regulate AI-powered lethal autonomous weapon systems (AI-LAWS). It clearly defines its terms, introduces a behavior-based oversight framework, and supports its claims with concrete examples of deployed systems, real-world risks (e.g., drift, brittleness, misclassification), and detailed citations from both the AI and policy literature. The paper is especially strong in connecting AI technical failure modes to geopolitical and institutional consequences, making a compelling case for the inclusion of AI researchers in the regulatory lifecycle. The topic is highly relevant to the NeurIPS community, as it addresses the dual-use nature of ML research, the erosion of academic openness, and the ethical obligations of researchers. Its recommendations are actionable, its structure is clear, and it meaningfully engages with alternative views. Overall, it makes an impactful and well-supported contribution to a critical and underdiscussed area.

### Weaknesses
While the paper presents a strong position, several areas could be clearer. The proposed oversight criteria for AI-LAWS, based on whether a system uses ML and contributes to lethal decisions, are useful but not supported by detailed examples of how to detect or verify these conditions in real systems. The rubric would be stronger if applied to specific systems in Table 2 to show how it distinguishes high-risk cases. The paper also states that AI researchers should be involved in oversight but does not explain how this would happen, e.g., through system testing, access to classified models, or formal review roles. In several places, the risks discussed (e.g., opacity, drift, brittleness) are technically valid, but the paper could clarify how they differ from risks in non-lethal AI systems.

### Questions
The paper raises important points, but several areas would benefit from further clarification and development to strengthen its practical impact and address key ethical concerns.
-- Recommendation 1: Clarify how the behavioral criteria for AI-LAWS can be applied in real systems and how evaluators should assess risks like misclassification, drift, or escalation.
-- Recommendation 2: Provide a concrete example from Table 2 to show how the rubric identifies a system as an AI-LAWS.
-- Recommendation 3: Address how the framework applies to systems that influence but do not directly execute lethal actions.
-- Recommendation 4: Specify the role AI researchers are expected to play in oversight, including the type of access or responsibilities required.
-- Recommendation 5: Explain why risks such as bias, opacity, and brittle generalization demand separate treatment in military AI systems compared to civilian ones.

### Presentation
3

---

## Human Reviewer 2

### Rating
9

### Rating Number
9

### Confidence
5

### Summary
The paper defines AI-powered lethal autonomous weapon systems (AI-LAWS) as military systems using modern AI/ML that present unique risks beyond conventional LAWS. It proposes criteria that makes a military AI systems high-risk such as essential AI/ML components and autonomous targeting/force application. It calls for technically informed regulation with AI researchers involved. The paper also recommends targeted policies: banning AI in nuclear launch and battlefield command, setting international validation standards, clarifying civilian AI infrastructure’s legal status, and preserving civil-military boundaries.
The paper has a clear position: AI-LAWS are a distinct new category needing oversight with AI researchers in the loop.

### Strengths
- The argument is well-structured, moving from problem framing to a practical oversight rubric and targeted policy recommendations. 
- The paper clearly identified the risk of AI lethal weapons systems, and showed examples of real-world use in Tables 1 and 2.
- The paper effectively distinguishes AI-LAWS from conventional autonomous weapons.
- The topic is highly relevant to the NeurIPS community and critical given the current state of geopolitics around the world.

### Weaknesses
- The proposed definition and criteria of AI-LAWS is clear as a concept, but lacks concrete metrics, or examples of how it would be enforced in real-world policy.
- The paper presented the current existing frameworks as alternative views, but it should have also discussed opposing views that discuss infeasibility of regulating AI-LAWS or views of defense stakeholders who may see current oversight as sufficient.
- The paper doesn't clearly specify the role of AI researchers for each policy recommendation they present.

### Questions
- How do you plan to translate the definition into measurable benchmarks that can be applied consistently across different geopolitical and security contexts to classify AI-LAWS?

- Among the listed risks which should be addressed first in regulation and how should limited oversight resources be allocated?

 - How effective is the proposed approach compared to just integrating AI-LAWS oversight into broader military AI governance frameworks, rather than treating them as a distinct category?

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper’s focus is an emerging technology referred to as AI-LAWS: lethal autonomous weapons that integrate AI. The authors argue that current governance efforts are insufficient for AI-LAWS: they require a distinct regulatory regime from conventional LAWS, into which AI experts are substantially integrated. This need stems from novel risks – including opacity, post-deployment drift, brittleness under distribution shift, miscalculation/escalation, and erosion of human oversight – that are both poorly addressed by current frameworks and poorly understood by those lacking AI expertise. To resolve definitional ambiguity, the authors propose a shift to behavior-based criteria for identifying AI-LAWS, and advocate for a slew of policies for the oversight of the systems that meet those criteria: (1) ban AI control of nuclear deployment; (2) develop more rigorous international standards for technical validation AI-LAWS via a voluntary international consortium; (3) ban “AI generals”; (4) clarify the legal status of dual-use AI infrastructure; and (5) establish greater institutional separation between civil and military AI.

### Strengths
The authors successfully establish the importance and timeliness of addressing AI-LAWS oversight, and sharply articulate associated risks, providing a compelling case for why a new governance regime is needed vs. conventional LAWS. Technical aspects like opacity and brittleness under distribution shift are clearly explained and make a strong case for the integration of technical expertise, alongside an explicit and concrete validation agenda (out-of-distribution robustness, red-teaming, end-to-end trials). Proposed prohibitions (against AI in nuclear deployment and “AI generals”) seem sufficiently narrowly drawn and potentially politically feasible. The topic is highly relevant to the NeurIPS community, especially in light of the papers’ call for the participation of ML experts in setting validation criteria and standards for AI-LAWS.

### Weaknesses
The proposed behavior-based definition of AI-LAWS does seem like a step toward greater clarity, but the authors could have provided greater justification for why this definition is sufficiently operational. In particular, the description of Criterion 1 as simply the use of those AI methods “that pose AI-specific risks” may be underspecified, conflicting with the authors’ claim that their definition offers a “practical tool for identifying high-risk systems.” 
The authors’ proposal of international standards creation via voluntary consortium as opposed to treaties seems novel and interesting for discussion, but likely raises questions about incentives, enforceability, and auditability that remain under-addressed in the paper.
While recommendations are actionable, perhaps the paper’s most central thesis – that greater AI expertise ought to be integrated into AI-LAWS oversight – remains at times vague. Greater attention could be paid to institutional/governance structures, and specific recommendations could be provided for ensuring that technical expertise is involved at all levels.

### Questions
What mechanisms do you foresee for the enforcement of standards set by a voluntary consortium? How often do you expect revisions to standards to happen? How to integrate this into existing fora?

### Presentation
4
