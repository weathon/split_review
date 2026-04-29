# Prohibiting Generative AI in any Form of Weapon Control

- Decision: Accept
- Scores: 8, 5, 7

## Abstract
This position paper argues that the use of generative artificial intelligence (GenAI) to control, direct, guide or govern any weapon, either in situ or remotely, should be prohibited by government agencies and non-governmental organizations. Such a moratorium should exist until hallucinations can be successfully modeled and predicted. Generative AI is inherently unreliable and not appropriate in environments that could result in the loss of life.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This position paper argues that generative artificial intelligence should be banned from controlling, directing, or governing any weapon system due to the inherent unreliability of hallucinations. The authors present a comprehensive analysis that spans AI reasoning capabilities, uncertainty management, and the deployment of safety-critical systems. Using the SRKE (Skill-Rule-Knowledge-Expertise) framework, they argue that GenAI lacks the higher-order reasoning required for weapons applications. The paper draws parallels with self-driving car failures to illustrate potential risks associated with weapons systems, examines technology readiness levels across different autonomous systems, and concludes with recommendations for research on hallucinations and the development of testing infrastructure before any weapons deployment.

### Strengths
The paper demonstrates strong technical rigor through its introduction of the SRKE framework, which provides a systematic method for evaluating AI reasoning requirements and moves beyond simplistic capability assessments to nuanced analysis of uncertainty handling. This contribution is well-grounded in empirical evidence, particularly the authors' use of real-world data from autonomous vehicle deployments that includes specific failure modes and intervention rates, lending practical credibility to their theoretical arguments. The work successfully bridges technical AI research with policy implications, offering actionable recommendations for both researchers and policymakers in a way that makes complex technical issues accessible to broader audiences. Additionally, the comprehensive scope of analysis spans multiple relevant domains from hallucination research to technology readiness assessment, providing a holistic view of the challenges that strengthens the overall argument through interdisciplinary integration.

### Weaknesses
While the paper identifies hallucination prediction as a key research need, it provides limited guidance on specific technical approaches beyond existing methods like RAG and knowledge graphs, leaving readers without a clear roadmap for addressing the core technical challenges. The heavy reliance on self-driving car examples as analogies may not fully capture the unique operational constraints and requirements of military applications, including different risk tolerance levels and human oversight structures that could significantly alter the risk-benefit calculations. The analysis would benefit from more direct engagement with military AI researchers and defense technology developers to better understand current approaches to AI safety in weapons systems, as the current perspective appears somewhat removed from actual defense AI development practices. Beyond this, there are some misspellings in various parts of the paper that need to be reviewed and corrected by the author.

### Questions
1. Could you elaborate on specific technical approaches for hallucination prediction beyond the methods mentioned? What would a research roadmap look like for achieving reliable hallucination modeling?
2. How would you assess proposals for graduated AI deployment in weapons systems, starting with low-uncertainty scenarios and robust human oversight before expanding to more complex situations?
3. While the paper focuses on risks, how would you structure a formal risk-benefit analysis framework that could guide decision-making about specific AI applications in defense contexts?

### Presentation
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The position paper argues for prohibiting the use of generative AI in all kinds of weapon control systems until hallucinations can be successfully modeled and predicted. They argue that hallucinations make the weapon control systems that use GenAI are unreliable, and therefore dangerous.

The authors of the paper lay out three main types of arguments to justify their position: 
1)	Automated reasoning in these systems is probabilistic and not rule-based (deterministic)
2)	Reasoning under uncertainty may leads to decision/outcome errors
The authors list a few examples to justify their position, such as accidents by autonomous driving cards and weapon drones.

### Strengths
The topic is very relevant and important to the NeurIPS community, especially as we observe the proliferation of AI use in automated and remote weaponry. I trust that the NeurIPS community would be very interested in ensuring the safe and reliable use of AI and would want to prevent any backlash from the general public against the use of AI if it is perceived to be unsafe and dangerous.
The paper lists some examples (failures/errors of autonomous driving cars, drones making mistakes) to argue that fully autonomous AI systems have had many errors/accidents and have caused fatalities. Therefore, they should be deployed for safety-critical tasks.

### Weaknesses
The paper’s argument hinges on the idea that until hallucinations can be modeled and predicted, using GenAI to control weapons should be prohibited. There is no evidence provided to support why this condition must be met though.
The arguments presented focus on the unreliability of automated reasoning, esp. when dealing with uncertainly. The examples presented are depictions of a vision system failing to interpret what it is “seeing” due to weather conditions, or because it has never been exposed to a similar env. during training. These errors are not related to “GenAI hallucinations”. It may be reasonable to argue that autonomous cars should not be used until vision systems can get a better handle of “interpreting” the car’s surrounding. But the argument does not transfer to “hallucinations” “generated” by a GenAI system. It is limited to “classification/recognition” errors made the AI system.
The paper fails to address other critical areas where misuse of these systems could occur. By solely focusing on high hallucination rates as a primary concern, the paper overlooks other risks associated with AI misuse, such as unintended consequences from lack of transparency or accountability in AI’s reasoning and decision-making processes

### Questions
The authors extend the same arguments to any safety-critical system, which they define as a system that directly or indirectly results in human injury or death. I have a couple of questions for the authors:
1) Would you take the same position for systems impacting the mental safety of people besides their physical safety?
2) Do you think other issues should also prevent the use of weapon control systems until fixed, for example adequate explainability and real-time traceability/observability of the reasoning steps and decisions being made by the weapon control system?

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
5

### Summary
This position paper argues that generative AI (GenAI) should be completely prohibited from controlling any weapon systems due to its fundamental unreliability and high hallucination rates. The authors demonstrate that GenAI cannot reliably reason under uncertainty—a critical requirement for military applications—citing evidence from self-driving cars where AI systems miss objects or hallucinate non-existent threats, requiring constant human oversight. 
Using a framework showing that autonomous agents need four levels of reasoning (Skills, Rules, Knowledge, and Expertise), they argue that current GenAI only operates reliably at the basic skills level, while weapons require expert-level reasoning under maximum uncertainty. Unlike drones that underwent 30 years of military testing before deployment, GenAI reached commercial use in just 6 years without thorough safety validation, making it too dangerous for weapons applications until hallucinations can be predicted and controlled through dedicated research programs and new testing frameworks.

### Strengths
* Provides alarming concrete statistics: hallucination rates of 28.6-79%, GPT-4 planning success of only ~12%, spatial reasoning accuracy of just 7.9-53.3%
* Makes abstract AI risks tangible through specific, measurable failure rates
* Self-driving car analogy is particularly effective - uses the most advanced public autonomous AI to demonstrate weapon system risks
* Specific incidents (Cruise bus crash, federal crash data showing missed detection rates, false positive rates) make technical failures concrete
* Addresses urgent current developments (Anduril-OpenAI partnership, ChatGPT gun incidents) before widespread deployment
* Intervenes at a critical policy moment when nations are racing to weaponize AI, but deployment isn't yet entrenched
* SRKE framework effectively shows why current AI falls short of autonomous weapon requirements
* Risk assessment matrix visualizes maximum danger (high safety criticality + high non-determinism)
* Historical timeline analysis (30 years for drones vs. 6 years for GenAI) powerfully demonstrates rushed deployment concerns

### Weaknesses
* Firstly, I think the abstract can be improved. It is hard to clearly understand the overview of the paper from the abstract only.
* Figure 1: Despite being the paper's central framework, it lacks a descriptive caption explaining the four SRKE building blocks (Skills, Rules, Knowledge, Expertise) and how they relate to increasing uncertainty
* Figure 2: Presents a subjective risk assessment without concrete mathematical metrics for the axes - "safety criticality" and "non-determinism" remain undefined and unmeasurable, making the plot more impressionistic than scientific
* Heavy reliance on OpenAI models (GPT-4, ChatGPT) for evidence rather than drawing from a broader range of AI systems and architectures
* While AI may not be the ideal solution for making decisions under high uncertainty, it can serve as a valuable assistant to ease the pressure in such situations. I’m curious about your thoughts on taking a less extreme stance—prioritizing more thorough testing first, while also ensuring that weapon–human interaction feels more like collaboration than outright replacement.

### Questions
* On Human-AI Collaboration: What are your thoughts on AI as an intelligent assistant rather than a replacement? Could AI reduce cognitive load while maintaining human authority over lethal decisions?
* On Testing and Robustness: What specific methodologies would you propose to build more reliable AI models for safety-critical applications? How can we design evaluation protocols that capture real-world uncertainties?
* On Hallucination and Comparative Performance: Do you believe hallucinations can be completely eliminated, or should we focus on managing them? Do you have comparative statistics on human versus AI failure rates under stress and time pressure?
* On Dynamic Human-AI Teaming: How would you address scenarios requiring dynamic shifts between human and AI control - such as when operators are incapacitated or situations demand split-second responses? Could graduated autonomy provide a middle ground between prohibition and unrestricted AI weapons?

### Presentation
2
