# Large Language Models Miss the Multi-agent Mark

- Decision: Accept
- Scores: 5, 9, 6

## Abstract
Recent interest in Multi-Agent Systems of Large Language Models (MAS LLMs) has led to an increase in frameworks leveraging multiple LLMs to tackle complex tasks. 
However, much of this literature appropriates the terminology of MAS without engaging with its foundational principles. 
In this position paper, we highlight critical discrepancies between MAS theory and current MAS LLMs implementations, focusing on four key areas: the social aspect of agency, environment design, coordination and communication protocols, and measuring emergent behaviours. 
Our position is that many MAS LLMs lack multi-agent characteristics such as autonomy, social interaction, and structured environments, and often rely on oversimplified, LLM-centric architectures. 
The field may slow down and lose traction by revisiting problems the MAS literature has already addressed. 
Therefore, we systematically analyse this issue and outline associated research opportunities; we advocate for better integrating established MAS concepts and more precise terminology to avoid mischaracterisation and missed opportunities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper argues that current research on Multi-Agent Systems of LLMs (MAS LLMs) is missing foundational concepts from traditional MAS literature. In particular, the authors identify four key shortcomings of current MAS LLM research and advocate for improving them by bringing LLMs into traditional MAS research: 
1. LLM agents lack social intelligence, like interactive capabilities. 
2. MAS LLM environments are LLM-centric and communicate via natural language.
3. Coordination and communication protocols ignore issues studied in MAS research, e.g., asynchronous design.
4. Emergent behaviors are claimed without rigorous definitions or benchmarks. 
The authors advocate for integrating MAS principles into LLM-agent system design and highlight future research directions, such as pretraining LLMs for social intelligence and using asynchronous frameworks.

### Strengths
- The paper studies a well-motivated topic that is relevant to the NeurIPS community. MAS is the next step for AI research, while traditional MAS research is overlooked in many cases.

- The authors seem to have good awareness of both traditional MAS and LLM agent literature.

- The paper raises timely concerns about important issues, including designs like coordination protocols, evaluation standards, etc.

- The paper provides some future research directions for each limitation it points out.

### Weaknesses
- The support of some arguments is not super strong. The position may be stronger if it is substantiated through more concrete comparative analysis to show how traditional MAS can help more specifically.

- Some recommended future directions are vague. Ideas like pretraining LLMs to be social or adopting MAS-style communication are suggested, but how feasible these directions are is not entirely clear or concrete.

- Some of the alternative views are addressed, but some are not.

### Questions
- The paper proposes pre-training LLMs for social intelligence by exposing them to multi-agent interactions and behaviors. However, if the dataset already captures such interactions, whether from humans or other models or any sources that dataset is generated, isn’t that sufficient? What additional benefit does explicit multi-agent pretraining offer?

- How can we validate whether an LLM has truly learned “social behavior” or developed true Theory of Mind in a MAS setting?

- The authors argue that natural language is inefficient for agent communication, yet humans coordinate effectively using it. Are the authors suggesting that the development of MAS LLMs should not ultimately converge to human-like communication?

### Presentation
3

---

## Human Reviewer 2

### Rating
9

### Rating Number
9

### Confidence
4

### Summary
The position paper presents an important argument relevant to the development of LLMs in multi-agent systems (MAS). It highlights that many current MAS-LLM approaches lack essential multi-agent characteristics such as autonomy, social interaction, and structured environments, and instead rely on overly simplified, LLM-centric architectures. The paper articulates its position through four core critiques: (1) the absence of native social behaviors, (2) the dominance of LLM-centric environments that do not reflect realistic MAS settings, and (3) the insufficient treatment of coordination and communication challenges, (4) in quantifying the emergence of complex behaviors. To support these claims, the authors draw on compelling evidence from existing literature and methods.

### Strengths
The paper effectively challenges the dominant LLM-centric design paradigm and encourages a shift toward more principled, socially grounded MAS research. 

The argument is clearly communicated, and grounded in evidence from the literature, making it a valuable contribution to ongoing conversations at the intersection of ML, AI, and multi-agent research.

Furthermore, the paper is well-organised, with strategically placed side notes that effectively highlight key points and enhance readability.

### Weaknesses
Minor problem:
1.  The font size in Figure 1 is too small to read.

### Questions
The paper references a substantial body of literature to support its arguments. Incorporating summary figures or tables to synthesize and categorize these works could enhance the clarity and readability of the paper. Is it possible?

### Presentation
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
The paper argues that the recent development of LLM agents ignore decades of literature on agentic systems.

### Strengths
The paper argues that MAS-LLMs do not have the characteristics of traditional multi-agent systems. For each of the four characteristics, the authors give evidence from either first principles or from the literature that the MAS-LLMs fail to have a particular characteristic. The paper also gives suggestions for improving the MAS-LLMs by following in the prior MAS literature.

### Weaknesses
Not a weakness per se, but a nit. I would have liked to see the paper be organized to be less repetitive. As it stands, the position doesn't appear until the bottom of page 3 because the key portions of the arguments from sections 2-3 are outlined in the introduction at 4-5 paragraphs for each argument. This is excessive; I would have preferred to get to the position faster. The additional space could have been used to clarify the methodology of the literature review etc etc.

Additional nit: the text of figure 1 is illegible without breaking out my reading glasses. Please be kind to the aged!

### Questions
1. I believe that the LLM literature does not appropriately follow the prior literature. Why is that important? The paper currently reads as if not following the literature was simply a thing to be avoided, without arguing *why* not following the literature is bad for this specific case. (Other than a brief mention of "slowing down" or "losing traction".

### Presentation
3
