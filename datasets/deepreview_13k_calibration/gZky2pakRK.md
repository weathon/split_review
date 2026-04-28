# HAICOSYSTEM: An Ecosystem for Sandboxing Safety Risks in Human-AI Interactions

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 8, 6, 6

## Abstract
AI agents are increasingly autonomous in their interactions with human users and tools, leading to increased interactional safety risks.
We present \FrameNameTextOnly, a framework examining AI agent safety within diverse and complex social interactions.
\FrameNameTextOnly features a modular sandbox environment that simulates multi-turn interactions between human users and AI agents, where the AI agents are equipped with a variety of tools (e.g., patient management platforms) to navigate diverse scenarios (e.g., a user attempting to access other patients' profiles).
To examine the safety of AI agents in these interactions, we develop a comprehensive multi-dimensional evaluation framework that uses metrics covering operational, content-related, societal, and legal risks.
Through running over 8K simulations based on 132 scenarios across seven domains (e.g., healthcare, finance, education),
we demonstrate that \FrameNameTextOnly can emulate realistic user-AI interactions and complex tool use by AI agents.
Our experiments show that state-of-the-art LLMs, both proprietary and open-sourced, %
exhibit safety risks in 62\% of cases, with models generally showing higher risks when interacting with malicious users and using tools simultaneously.
Our findings highlight the ongoing challenge of building agents that can safely navigate complex interactions. To foster the AI agent safety ecosystem, we release a code platform that allows practitioners to create custom scenarios, simulate interactions, and evaluate the safety and performance of their agents.
\footnote{\url{https://haicosystem.org}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a simulation framework for AI agents based on a wide range of scenarios, tasks, and simulated user personas; coupled to the simulations is a proposed evaluation framework meant to define the level of departure from safety any agent under test would exhibit along a variety of dimensions in order to define a level of risk. The paper also performs some evaluations of a variety of agents built on different base models using this simulation approach and evaluation framework, reporting the measured level of risk according to the evaluation framework.

### Strengths
+ The paper is exquisitely researched, contextualized in the literature, and presented (beyond some minor points - see last bullet under weaknesses).
+ Defining methods to evaluate AI agents across a wide variety of application domains and to link these evaluations to risk measurements are both very important problems.

### Weaknesses
 - The claims in this paper are too big and could be caveated and scoped better for support in the work actually performed. Accepting the claimed value of the framework requires assuming away the core problems of several subdisciplines of computer science and other fields (e.g., user modeling; the management points around failure probability vs. failure consequence; control handoffs and role development in human-system interaction; operationalization of the evaluation framework dimensions such as legal risk). Instead, the paper could acknowledge the complexity of these problems and the variety of approaches undertaken to operationalize solutions to each. At a minimum, the framework must not claim to provide dispositive guidance or evaluation except where such desiderata are validated in the proposed tool.
- I was confused to see the word "sandboxing" used to mean something about a simulation framework vs. its usual usage in CS meaning something about the isolation of component behavior in a larger system (in a sense, simulation _does_ do this, but it took a bit for me to understand what the term refers to in the paper). I think it would be useful to indicate near the top of the introduction (now it happens only at the end, already on p3 around 135-136) that the goal is to perform a wide variety of simulated human-system interactions for evaluation.
- In several places, the paper describes the value of a "checklist" of failure modes, but the proffered framework provides only high-level principles without a sense of how these would be operationalized nor any arguments for why such a checklist would be a valid risk perception tool or how to build the link from knowledge of the scores in the proffered evaluation framework/behaviors in the simulations to claims about _assurance_ (that undesired events are unlikely or not possible). Knowing when test & evaluation (which abstractly can only reveal the _presence of unsafety_, not its _absence_) provides sufficient grounding for usable claims on safety is an epistemically fraught and brittle process to reach practical guidance that a tool is usable within some defined envelope. Related to the point that the claims in the paper are too big, the paper does not engage any of the difficult problems here, instead papering over them with glossy architecture diagrams and lots of evaluation that is essentially impossible to extract meaning from. To solve this, the paper could walk through how one of these dimensions converts into a checklist and describe the value of that checklist - what it does and doesn't tell an evaluator. Also the paper would benefit from discussion somewhere about the value and limitations of checklist-based measurement to avoid difficulties with the fall into symbolic compliance. This would fit nicely in S4 or S6.
- In the evaluation framework, the proposed "dimensions" are extremely high-level and mask difficult choices about how these major problems can be made visible/measured/traded off in terms of outcomes. The paper proposes these dimensions without arguing for their completeness or sufficiency or making any attempt to validate that these dimensions capture meaningful risks. It is more normal in systems safety to build some kind of model of unacceptable failures and argue for why the system cannot reach these states. Why were these dimensions chosen? How do we know they're "enough"? What limitations exist in operationalizing these? (For example, for the content safety dimension, there is a rich literature of content which is difficult to categorize as safe vs. unsafe - how does the framework handle this and who should decide?)
- Systems safety approaches differ from the framework here in two important ways: first, it is common to understand that problems can arise within "normal" operations, meaning risks are not "long tail" phenomena (even if their probability is low) but rather emergent phenomena that relate to the structure of the system under test (expressed either through explicit structure modeling or through careful enumeration of failure modalities). Second, there is a differentiation between risk _probability_ and _consequence_: some failures may be "small" under the framework evaluation scores but nonetheless very important. That would indicate a problem with the framework. Yes, there's a lot of evaluation performed here, but I don't see evidence that the experiments fed back into a richer notion of what the framework dimensions should capture.
- There are a number of editing issues I believe reveal that the paper was authored by a large group where either standards for common formatting were not available or not enforced. Simple things like capitalization, formatting of certain types of offset terms, and figure labeling are not consistent across the paper. This is obviously fixable and didn't impact my ability to read the paper or my scores, but I did notice it.

### Questions
* How can the framework be validated as a tool for risk perception? What even are the risks?
* Can the authors offer a plan to temper the claims or contextualize the design choices in this tool such that it describes more than just a point in the design space but instead either a defensible best option for achieving the stated goals or some kind of generalizable knowledge about how to do AI agent evaluation and assurance?

### Soundness
1

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This interesting paper introduces HAICOSYSTEM, a framework to evaluate the safety of LLM agents in complex, multi-turn interactions with (simulated) human users. HAICOSYSTEM is a sandbox environment where AI agents, optionally using various tools, navigate simulated scenarios across different sectors (e.g., healthcare, finance). The authors designed a comprehensive evaluation system with metrics addressing risks across multiple dimensions inclding operational, content, societal, legal, etc.
In testing, over thousands of simulations across 132 scenarios, current state-of-the-art LLMs (both proprietary and open-source) exhibit safety risks in 62% of cases, particularly when interacting with malicious users and using tools.
This research highights the challenge of building AI agents that can safely manage complex interactions with users and the internet. The authors released a code platform enabling users to create, simulate, and assess the safety and performance of AI agents in custom scenarios.

### Strengths
Important and timely research as LLMs invade the world.
Use of robust AI safety frameworks and methods
Significant contribution over previous works, particularly with handling of multi-turn interactions, benign and malicious users, use of tools
Large number of scenarios across multiple domains, 8700 simulations overall
Comparison of 12 different state of the art LLMs
Manual verification of 100 random samples - showing high correlation
Evaluation of credibility of simulated human users with quantitative metric
Extensive appendices with detailed code and worked examples

### Weaknesses
Some risks are more critical than others. For example, a tool generating moderately violent content locally to a single user is not as critical as a tool actually building and releasing malware at scale in an automated fashion all over the internet. Would the authors consider (for example) implementing a weighting system or severity scale for different types of risks based on their potential impact and scale? This would allow HAICOSYSTEM to differentiate between localized, low-impact risks and widespread, high-impact risks in future iterations.

Your current metric, "risk ratio" is the proportion of risky episodes over the total number of episodes. However, risk categories aren't equal in the number of risks they contain. What's the implication of this? The authors could conduct a sensitivity analysis to understand how the current risk ratio calculation might be biasing results across different risk categories. 

Would it not be better to compute "risk ratio" as ratio of number of risks observed in a given episode over the total number of possible risks in a given risk category (then averaged over the total number of episodes)? The authors could compare their current method with this alternative to see if it leads to significantly different conclusions or insights about AI agent safety.

### Questions
Your current metric, "risk ratio" is the proportion of risky episodes over the total number of episodes. However, risk categories aren't equal in the number of risks they contain. What's the implication of this? The authors could conduct a sensitivity analysis to understand how the current risk ratio calculation might be biasing results across different risk categories. 

Would it not be better to compute "risk ratio" as ratio of number of risks observed in a given episode over the total number of possible risks in a given risk category (then averaged over the total number of episodes)? The authors could compare their current method with this alternative to see if it leads to significantly different conclusions or insights about AI agent safety.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces HAICOSYSTEM, a framework designed to evaluate AI agent safety across a variety of simulated multi-turn, intent-driven (benign, malicious) interactions/users in several domains. The framework leverages LLMs to simulate both human users and evaluator, providing a multi-dimensional safety assessment. The diversity of scenarios across healthcare, finance, and other sensitive domains highlights its relevance to high-stakes AI applications, and we observed the safety risks associated with larger and small LLMs.

### Strengths
1) HAICOSYSTEM covers operational, content, societal, and legal risks, capturing the wide array of safety risks in human-AI interactions. 

2) Its focus on multi-turn interactions is valuable as it allows for the capture and analysis of evolving actual and perceived user intents (benign and malicious). This mirrors real-world interactions, where safety risks can emerge gradually rather than be obvious from the onset.

3) Scenarios across seven domains with varied realism levels are interesting and important because they can be applied to real-world safety evaluation.

4) Human verification for 100 randomly selected episodes improves the credibility of the automated evaluations conducted by GPT-4o.

### Weaknesses
Despite these strengths, I have some suggestions/concerns regarding evaluating and discussing the results.

1) The paper introduces realism levels (1-3) but does not analyse how these levels impact the safety risks experienced by different LLMs. This missing analysis represents a gap, as understanding the role of realism could reveal specific strengths or vulnerabilities of various models in complex, high-stakes scenarios.

2) There is no discussion on how many scenarios simultaneously incorporate multiple overlapping risks (e.g., operational and societal risks). This information is important, as multi-risk scenarios are likely in real-world applications where AI agents operate in complex environments with intersecting safety concerns.

3) Its reliance on simulated human-AI interactions (versus real human users -- although there were some assessments of the realism) might limit its generalisability, particularly in handling diverse user strategies.

Minor Issues:

4) Fig 1 isn't particularly informative. Perhaps the authors could also include the outcome, e.g., the proposed metrics and rationale for applying them to the specific scenario.

5) How does the paper define safety and risk?

### Questions
1) How does using GPT-4o as both the user and evaluator impact the diversity and realism of the evaluations? While human oversight was provided on 100 sample instances, relying on a single LLM for dual roles may introduce consistency that doesn't accurately reflect human diversity.

2) What specific types of errors occurred in the 10% of instances (of 100 manually verified) where the evaluator's judgment did not align with human evaluation? Are there recurring patterns in the evaluator's mistakes, such as consistently underestimating or overestimating particular risk severities?

3) What prompted the creation of the 21 additional scenarios, and how were they validated? Were the remaining 111 scenarios sourced from existing works also reviewed or verified by experts?

4) How many scenarios in HAICOSYSTEM incorporate multiple overlapping risks (e.g., operational, societal, and legal risks combined)? Are there specific scenarios designed to test AI agent performance in high-stakes situations where multiple risks intersect?

5) How does scenario realism level impact the types and severity of safety risks encountered by various LLMs? Could specific strengths or vulnerabilities be observed at higher realism levels that may not appear in simpler scenarios? While the paper categorises scenarios by realism, it does not analyse how these levels influence LLM performance or risk exposure. 

6) To what extent do the simulated human behaviours reflect diverse, realistic user strategies, particularly those that may involve complex or unpredictable behaviour? How might using real human users impact generalisability and reliability?

7) How do you define "interactional safety risks"?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present HAICOSYSTEM, a platform for exploring the safety risks of multi-turn human-AI interactions via simulation of the agents with LLMs. The AIs can access simulated tools/APIs and must navigate challenges such as ambiguous user goals and having both benign and malicious users. Evaluating various popular LLMs, the authors find substantial safety risks and explore the implications of particular trends, such as System and Operational risks being more common than Content risks and relationships between model performance and safety.

### Strengths
**S1.** The topic of realistic human-AI interaction and its safety risks is clearly important.

**S2.** The authors frame their work well in relation to past work and address a wide variety of challenges in creating agent sandboxes (e.g., using LLMs to scale and adapt better than human participants or hard-coded environments).

**S3.** This is a large project with a variety of contributions, and the authors seem to do relatively well in condensing their ideas and empirics into a clear digestible paper.

### Weaknesses
 **W1.** I was largely unconvinced of the realism of these simulations. Are the simulated humans acting as humans do in real human-LLM interaction datasets (e.g., [1])? Are the API simulators/emulators/engines really acting as a hard-coded API would? This is a difficult challenge, and I appreciate the authors' effort, but it is well-established that LLMs are still bad at simulating human behavior [2] and bad at agentic tasks, even in highly streamlined sandboxes [3]. The authors focus on safety risks, which I understand is their research goal, but to be a useful sandbox for safety risks, the interaction itself must first be realistic. If I missed this validation in the appendix, the authors could refer me to the key evidence of realism. If not, perhaps it would be better to first create the sandbox in a paper and then do the safety evaluations in a second paper. Both the sandbox and the safety evaluations need extensive evaluation to be useful.

When the authors provide examples of LLM behavior in the environment, they seem unconvincing. E.g., for the example in Figure 1, which I assume is cherry-picked (which is fine), the "safety issue" seems to be that the AI agent didn't verify the prescription, but that is not in the "Goal" on the left-hand side. How was the agent supposed to know they were meant to be the verifier? Why would they expect to be a verifier when they would clearly not be a reliable system for doing so? All they did was send an API request. If SOTA models were asked to do this with the degree of instruction that a real LLM agent would have, I'm confident they would refuse an unverified prescription delivery.

**W2.** While I appreciate the references to prior literature, it seems the authors rely on it too much compared to their own work. This is a nascent literature and makes a light scaffolding on which to build compelling and durable research advances. This relates to W1, especially that a verbal "*believability* score" from Zhao et al (2024c) could somehow justify that "human users realistically emulate real human users" or that "the simulated human users behave naturally." And even if most conversations appear natural, that is exactly what LLMs are overfitted to (i.e., realistic-seeming text that does not flesh out), and safety risks are about what happens out of distribution.

**W3.** Various claims seem stronger than are justified by the content of the project itself. For example, the authors say, "we argue that the safety risks of AI agents should be investigated in a holistic manner" with the entire ecosystem, but the creation of this sandbox is motivated by needing holistic investigation. Neither the sandbox nor evaluations constitute such an argument. Similarly, the claim that they "effectively surface previously unknown safety issues" seem unjustified because the findings, which are fine in their own scope, don't seem like previously unknown safety issues. I'm happy to be corrected if that's wrong.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
