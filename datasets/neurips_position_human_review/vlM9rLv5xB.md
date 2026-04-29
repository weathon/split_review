# The Right to Red-Team: Adversarial AI Literacy as a Civic Imperative in K-12 Education

- Decision: Accept
- Scores: 7, 8, 3

## Abstract
The increasing societal integration of Large Language Models (LLMs) and agent-based AI demands a new civic competency: adversarial reasoning. This position paper argues that K-12 AI education must move beyond passive literacy to actively equip students with skills in responsible adversarial prompting and ethical system "hacking." Such capabilities are essential for citizens to critically probe AI systems, understand their inherent limitations, identify manipulative patterns, and hold them accountable. We posit that cultivating a generation skilled in "red-teaming" AI is vital for maintaining transparency, preventing undue influence, and fostering a democratic engagement with these transformative technologies.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The main argument in the paper is that education must go beyond teaching students to consume AI-generated content critically, but also incorporate methods to teach them to interact with AI systems adversarially, exploring and discovering for themselves the limits and failures of those systems, which they define as adversarial reasoning. Critically, backed by child rights and democratic theory, they support their argument by showing that adversarial reasoning is a civil right. The authors then provide a detailed methodology for implementing their proposition in K-12 education, which they identify as having the necessary scale and impact for implementation.

### Strengths
A great strength of the paper is the argument for moving towards decentralized AI red-teaming: empower citizens with the right to contest AI systems they (nowadays, have pretty much no choice but) use, thus reducing the concentration of power in the hands of large organizations. This debate must be given more attention in the field.

Most of the discussion in human-AI safety currently focuses on the AI systems and how to make them safer for users — this paper turns this perspective around, arguing for a decentralized approach that focuses on making users themselves wiser in their interactions with AI. This decentralized approach is less fragile, in the sense that if new, misaligned AI systems gain popularity, users will already be prepared.

They also propose a realistic implementation method that leverages K-12 education.

### Weaknesses
I can see the benefit of having more people find flaws in the models, which could be used to inform companies. But AI is different from a bug in the sense that organizations might (unfortunately) be interested in misleading people (recall the Facebook-Cambridge Analytica scandal). I totally agree with the necessity of empowering citizens, but I do not agree with putting so much weight on red-teaming.

The authors motivate their argument by saying that companies would hardly be able to find every failure mode of their models with in-house red-teaming alone (which I agree with). They also show that adversarial reasoning is a civil right. I agree with the construction of these two observations separately, but I can't see a clear connection. If we accept the conclusion that adversarial reasoning is a civil right, it does not matter how capable in-house red-teaming labs are — citizens must have access to such a right regardless of their utility to companies.

From a misinformation perspective, it is not clear why we need to upgrade from critical reading of AI-generated content to adversarial reasoning, since there is no fundamental difference between misleading content created by another human or generative AI (besides scale).

### Questions
I could not find the following evidence in the reference Morales-Navarro (2025): “Similarly, Morales-Navarro (2025)’s research with ninth-grade students revealed that adolescents who spent a week jailbreaking and patching language models were more likely to disclose exploits to teachers and less tempted to share them on social media” (p. 6). I would like to ask the authors to elaborate on this.

### Presentation
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper argues that K–12 AI education must evolve beyond passive AI literacy to actively cultivating students' skills in responsible adversarial prompting and ethical system "hacking." It makes a case grounded in public epistemic crises, spectacular failures of AI, democratic vulnerabilities, and the civic necessity of adversarial reasoning. The paper further addresses common objections, demonstrates that such skills are teachable, and proposes concrete actions in policy and standards.

### Strengths
1. The argument for integrating adversarial reasoning as a civic skill is novel and urgent, especially in the face of misinformation, opaque AI systems, and trust deficits in public technology.
2. The paper transitions logically: from diagnosing a societal crisis → establishing the educational need → addressing counterarguments → demonstrating feasibility → calling for policy-level action.
3. Ending with concrete policy and standards proposals makes the paper impactful beyond theory, pushing it toward real-world implementation.

### Weaknesses
More detail is needed on how to scale this in actual K–12 classrooms: What age groups? What teacher training is needed? How do you evaluate responsible use?

### Questions
How is “adversarial AI literacy” defined in concrete terms for a K–12 audience?
Is it limited to prompt engineering or does it extend to technical red-teaming?

### Presentation
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This position paper is premised on the observation that opaque, large-scale AI systems result in a profound gap in accountability that existing models of AI literacy cannot address. The authors advocate a shift in K-12 education from a passive “critical consumption” stance towards “adversarial reasoning,” a more proactive method. This approach entails equipping students with the ability to ethically red-team AI systems to uncover biases, limitations, and failure modes.

The authors advocate that this form of active, critical inquiry is a civic responsibility to safeguard democratic governance, and the main argument of the paper. Its principal contributions are: (1) adversarial AI literacy is framed as a civic responsibility to act as a distributed public overseer; (2) the results of early classroom studies are presented to show that these skills are teachable and encourage prosocial behavior; (3) a comprehensive policy proposal is advanced that includes curriculum mandates, a Right to Red-Team for students, and federally equitable funding models for implementation.

### Strengths
The paper's primary strength emerges from an outstandingly well articulated argument pertaining to an issue of fundamental importance to the NeurIPS community. It adroitly motivates the need for adversarial AI literacy and frames it as a democratic obligation for public responsibility. The argument culminates in a set of actionable policy proposals, having commenced from the issue of AI opacity.

The authors reinforce the argument's position by citing pertinent and diverse recent ML safety research on adversarial attacks, early AI education policy, as well as overarching policy frameworks. The positions articulated in the paper are timely, provocative, and likely to generate essential debate on public engagement in AI safety and governance. The proposed actions, while concrete, are bold and galvanizing to the community in order to provoke debate.

### Weaknesses
The trustworthiness of the paper is seriously compromised due to the use of fictitious events from 2025 to frame the issue. Real AI failures documented in the literature should be the framing of the paper. Furthermore, the paper appears to rely too heavily on the implemented evidence, presenting informally within small pilot studies as a universal proof of a mandate instead of framing as promising but preliminary findings.

Consideration of alternative overlooked positions would improve the paper. These include: 1) Lending oversight of auditing the models pre-deployment to an independent government body as an overly protective regulatory approach, thereby easing the burden on the lay citizen. 2) Different focus on interpretability as teaching to inspect models instead of to break them. Lastly, the proposal is in deep need of addressing the intricately mixed questions of legal liability the adopting schools would face with such a curriculum.

### Questions
Your proposed Right to Red Team leans on responsible disclosure, which is a complicated standard, even among practitioners. Can you devise a tangible, tangible, school-level protocol for this? If a student uncovers a novel, extremely critical vulnerability in a proprietary system, what are the precise actions a teacher must take? Who decides whether the disclosure was responsible, and how does your approach protect students and schools from lawsuits if a vendor breaches the terms on which the disclosure was deemed responsible?

The paper underscores this work as paralleling white-hat cybersecurity; however, the risks associated with LLMs, such as scalable misinformation, tend to be far more harmful. What particular technical safeguards in the secure sandbox would prevent a student from leveraging their skills to create harmful content, leak a jailbreak exploit to the public internet, or otherwise alter the system? Addressing these questions would greatly bolster the argument for the proposal’s safety and feasibility.

### Presentation
3
