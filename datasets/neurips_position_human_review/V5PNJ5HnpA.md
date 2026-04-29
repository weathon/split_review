# Reality Check: A New Evaluation Ecosystem Is Necessary to Understand AI's Real World Effects

- Decision: Reject
- Scores: 7, 5, 4

## Abstract
Conventional AI evaluation approaches concentrated within the AI stack exhibit systemic limitations for exploring, navigating and resolving the human and societal factors that play out in real world deployment such as in education, finance, healthcare, and employment sectors.  
AI capability evaluations can capture detail about first-order effects, such as whether immediate system outputs are accurate, or contain toxic, biased or stereotypical content, but AI's second-order effects, i.e. any long-term outcomes and consequences that may result from AI use in the real world, have become a significant area of interest as the technology becomes embedded in our daily lives. These secondary effects can include shifts in user behavior, societal, cultural and economic ramifications, workforce transformations, and long-term downstream impacts that may result from a broad and growing set of risks. 
**This position paper argues that measuring the indirect and secondary effects of AI will require expansion beyond static, single-turn approaches conducted in silico to include testing paradigms that can capture what actually materializes when people use AI technology in context.** Specifically, we describe the need for data and methods that can facilitate contextual awareness and enable downstream interpretation and decision making about AI's secondary effects, and recommend requirements for a new ecosystem.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This position paper argues that current AI evaluation methods, primarily benchmarking, are inadequate for understanding AI's real-world societal impacts. The authors contend that while benchmarking captures "first-order effects" (immediate system outputs), it fails to measure "second-order effects" (long-term consequences of AI deployment). They propose a new interdisciplinary evaluation ecosystem incorporating field testing, red teaming, and value-sensitive design principles. The paper calls for moving beyond static, computational evaluation toward dynamic, contextually-aware methods that involve stakeholders and capture how humans actually interact with AI systems in deployment. The authors recommend establishing testing hubs with expertise from academia, industry, and civil society to develop more comprehensive evaluation frameworks that can inform policy and deployment decisions.

### Strengths
1. The paper tackles a genuinely important problem with AI evaluation that has real implications for AI safety and governance. The interdisciplinary approach is refreshing and necessary for this complex topic. 

2. The systematic critique of benchmarking limitations is thorough and well-reasoned. The proposed framework, integrating value-sensitive design with field testing and red teaming, is innovative and practically oriented. 

3. The writing demonstrates broad expertise across multiple relevant fields. The paper successfully makes the case that current evaluation approaches are insufficient for understanding AI's societal impacts, which is a crucial insight for the field. 

4. The extensive literature review shows deep engagement with relevant work across disciplines.

### Weaknesses
1. The paper would benefit from more concrete examples of successful implementations of the proposed methods. While the authors critique benchmarking limitations, they could better address potential counterarguments about the scalability and cost-effectiveness of their proposed alternatives. 

2. The paper lacks a discussion of how to standardize or validate the proposed contextual evaluation methods. Some claims about benchmarking limitations may be overstated - benchmarking has evolved significantly, and some recent work does attempt to address real-world relevance. 

3. The paper could better acknowledge the practical challenges of implementing their proposed ecosystem, including resource requirements and institutional barriers. The transition between describing problems and proposing solutions could be smoother.

### Questions
1. How would you envision standardizing field testing and red teaming methodologies across different organizations and domains to ensure comparable and reliable results?

2. What specific mechanisms would you propose to balance the need for comprehensive contextual evaluation with the practical constraints of time and resources that organizations face?

3. Could you provide more details on how the proposed evaluation ecosystem would handle the challenge of keeping pace with rapidly evolving AI capabilities while maintaining methodological rigor?

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
The authors contend that current AI evaluation methods, particularly benchmarking, fall short in capturing contextual information, referred to as second-order effects. They further argue that, when these limited evaluation methods are combined with the vast heterogeneity in how humans interact with AI in real-world settings, the result is a near-infinite complexity that hampers the development of a comprehensive evaluation framework. Reproducibility is also identified as a major challenge, as existing benchmarks tend to be static in design, lack systematic structure, involve limited stakeholder input, and fail to account for cultural nuance. Therefore, the authors advocate for an AI evaluation ecosystem that is contextually aware and grounded in real-world dynamics.

### Strengths
The authors clearly state their position: the current evaluation system, which relies heavily on AI benchmarks, fails to capture the social dynamics between AI and humans. They argue that context awareness should be grounded in value-sensitive design (VSD) principles and supported by key integration practices such as stakeholder engagement, field testing, and red teaming, among others.

### Weaknesses
The authors did not substantiate their proposed solutions with concrete, contextual examples from real-world applications, such as text generation and object detection etc. While the third-order effect is briefly mentioned in Table 1, the paper lacks any meaningful discussion of its relevance to AI evaluation systems. Additionally, the authors overlook a significant body of ongoing research that addresses the societal impact of AI algorithms, as well as issues of reproducibility and explainability, leaving important perspectives unacknowledged.

### Questions
1. Does the proposed AI ecosystem aim to replace current benchmarking methods, such as leaderboards, or complement them?

2. How can human bias be mitigated when human input directly influences the development and evaluation of AI algorithms?

3. Could building an AI evaluation system grounded in contextual factors—such as culture or discipline—hinder progress toward developing artificial general intelligence?

4. If AI evaluation is based on contextual information, how can a standardized, uniform evaluation framework be established across diverse applications?

### Presentation
3

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
Existing AI evaluation benchmarks primarily focus on first-order effects (e.g., does the AI system produce accurate predictions?), while second- and third-order effects (e.g., long-term downstream impacts on users and society) remain largely unexplored. The paper argues that a new ecosystem should be developed to measure these indirect impacts of AI systems.

### Strengths
1. Effectively highlights the limitations of current AI evaluation practices (e.g., model benchmarking on static datasets).

2. Calls for a new context-aware AI measurement and impact evaluation ecosystem involving stakeholders from both AI and non-AI domains.

### Weaknesses
1. Since the limitations of current AI benchmarking practices are highlighted, it would be helpful to discuss specific technical solutions that the NeurIPS community should consider.

2. Human-Computer Interaction (HCI) and Human-AI Interaction (HAI) researchers already actively study the impact of AI on user behavior. They incorporate tactics mentioned in the position paper, such as red teaming and conduct field experiments. The authors should clarify what specifically is missing from current HCI/HAI research.

3. The proposed measurement/evaluation ecosystem lacks specific details and remains high-level. The paper would benefit from providing concrete examples of how contextual data adds value in specific domains (such as medical decision-making with AI versus AI support in education).

### Questions
1. How can the NeurIPS community contribute to developing a more effective and useful measurement/evaluation system?

2. What gaps exist in current HCI/HAI research regarding the measurement of AI's impact on users and society? What specific, actionable steps could address these limitations?

3. What are some specific examples of leveraging contextual data in certain domains? Could the authors provide a clearer picture with examples?

### Presentation
3
