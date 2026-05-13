# Dissecting Adversarial Robustness of Multimodal LM Agents

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
As language models (LMs) are used to build autonomous agents in real environments, ensuring their adversarial robustness becomes a critical challenge. Unlike chatbots, agents are compound systems with multiple components, which existing LM safety evaluations do not adequately address. To bridge this gap, we manually create 200 targeted adversarial tasks and evaluation functions in a realistic threat model on top of VisualWebArena, a real environment for web-based agents. In order to systematically examine the robustness of various multimodal we agents, we propose the Agent Robustness Evaluation (ARE) framework. ARE views the agent as a graph showing the flow of intermediate outputs between components and decomposes robustness as the flow of adversarial information on the graph. First, we find that we can successfully break a range of the latest agents that use black-box frontier LLMs, including those that perform reflection and tree-search. With imperceptible perturbations to a single product image (less than 5% of total web page pixels), an attacker can hijack these agents to execute targeted adversarial goals with success rates up to 67%. We also use ARE to rigorously evaluate how the robustness changes as new components are added. We find that *new components that typically improve benign performance can open up new vulnerabilities and harm robustness*. An attacker can compromise the evaluator used by the reflexion agent and the value function of the tree search agent, which increases the attack success relatively by 15% and 20%. Our data and code for attacks, defenses, and evaluation are available at url_removed_for_review.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This papers studies the robustness of multimodal language model agent **systems** to attacks which attempt to force the agent to take arbitrary actions. The authors introduce the concept of agent graph, which is a graph whose nodes are the system components and the edges represent the flow of data from one system component to the other, and the weight of each edge represents how likely is an attack to succeed after the given component. This graph allows a more comprehensive understanding of how vulnerable each component is and whether it robustifies or weakens the system. Using this approach, the authors studies the robustness of the different components uner several attacks both text-only and image-based against several models, and also show the effectiveness (or lack thereof) of different defenses.

### Strengths
- The authors look at the entire deployed system and not only at the LLM component of the system. This is very important as the individual components of the system might amplify or reduce robustness (as shown by the paper).
- While at the beginning feels a bit of an unnecessary formalization, I ended up liking describing the system as a directed graph where the weights of the nodes represent the likelyhood of success of the attack after the given component.
- VWA-Adv seems to be a good dataset to evaluate the robustness of agents in an adversarial environment and the design choices are sound.
- The threat modeling is realistic.

### Weaknesses
 - The main complain I have is that there is no discussion whatsoever regarding (indirect) prompt injection attacks [1] and all the related literature. Prompt injection attacks are very relevant as they use a similar attack vector (an adversary manipulating untrusted data) which has the same aim (trigger some specific actions). The paper would benefit from a discussion of prompt injection attacks and an explanation on how "Text access" attacks differ from those.
- I find the caption of the figures too short. I believe they could benefit from more detailed descriptions of the figures. For example, the caption for Figure 3 could include an explanation of what happens in each of the subfigures. What does the arrow with "1.0" in the bottom right part of Figure 3.c mean? Is it an attack?
- How are tasks evaluated? The paper mentions "We employ evaluation primitives from Koh et al. (2024a) and manually annotate the evaluation function.", but I believe that these details should be included in this paper too (at least in the appendix) to make it self-contained.
- In general, the narrative of "x improves security if kept uncompromised, but it decreases it if compromised" slightly dangerous by giving a false sense of security. When evaluating the security of a system, one should consider the worst case scenario. So, while I find these insights valuable, as they can be useful to understand where to focus when coming up with a defense, I believe that they should rephrased differently to reflect that the fact that, in fact, they are insecure.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines the vulnerability of multimodal language model agents to adversarial attacks, particularly in the context of web-based environments. The authors create a framework, Agent Robustness Evaluation (ARE), to systematically analyse the robustness of different agent components and their interactions. They find that even state-of-the-art agents, including those using GPT-4 and incorporating advanced techniques like reflection and tree search, are susceptible to attacks.

### Strengths
The framework models agents as graphs, with each node representing an agent component and each edge representing the flow of information between components. ARE decomposes the final attack success into edge weights that measure the adversarial influence of information propagated on the edge. This framework could allow researchers to understand the robustness/vulnerability of various components and agent configurations.

The paper shows some baseline defenses based on prompting and consistency checks and finds that they offer limited gains against attacks. This finding highlights the need for more research on robust defenses for multimodal agents.

### Weaknesses
The main weakness of the submitted paper is that it does not clearly motivate and explain why the proposed framework is representative of a real scenario and the usage of integrated LLMs. Although we can, of course, not expect to model the real world perfectly, it remains unclear why the proposed framework is a good approximation.

**The study focused on a specific threat model** where the attacker is a legitimate user of the platform with limited capabilities. This might not encompass the full range of potential threats that agents could face in real-world deployments. For example, attackers with more sophisticated capabilities or access to internal systems might be able to bypass the limitations considered in this study and launch more effective attacks.

**The defenses explored in the paper are quite basic** and show limited effectiveness against the attacks. While they offer some insights into potential defense strategies, more sophisticated and robust defenses are needed to mitigate the vulnerabilities identified in the paper effectively.

**The attacks presented in the paper rely on well-engineered versions of existing attacks**, adapted to the agent setting. This means that the true risk of these attacks could be higher as more advanced and novel attack strategies are developed.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes attack method against multi-modal agent. It considers four types of agent framework and different attack scenarios (white-box. black-box).

### Strengths
The paper is well-written and easy to follow. Evaluations are comprehensive.

### Weaknesses
The contribution of the paper lies more on the construction of the robustness evaluation framework for agent framework. More discussions on the technical challenges of this would be beneficial to emphasize the contribution.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the adversarial robustness of multi-modal LLMs in a realistic threat model built upon VisualWebArena. The created Agent Robustness Evaluation (ARE) framework uses a graph to show the information flow and assesses agent vulnerabilities across text and visual modalities. The paper pays special attention to how the robustness of agents changes concerning individual components. Furthermore, the framework will be accessible for stress testing after the review period.

### Strengths
The evaluation framework is novel and addresses a high-impact topic as the importance of multimodal agents continues to grow. The curation of 200 adversarial tasks and evaluation functions is a great contribution to accelerate security research in this field and the paper offers valuable insights into agent vulnerabilities.

### Weaknesses
Spelling errors (e.g. We instead of Web in the abstract)

Limited modalities (text, image). An extension to video and sound would be great for future work.

The paper addresses the setting of the VisualWebArena. Further studies in other settings would help for more generalisable insights. The same applies to investigating multi-agent interactions and agents that use function calling.

The authors themselves call the used defences “simple”. Investigation of stronger defences would be of interest to show the extent of vulnerability of an organisation using state of-the-art methods.

### Questions
Could the authors elaborate on how ARE might be adapted or extended to other kinds of environments beyond the web-based scenarios tested?

What are the performance losses that are caused by various defences? Which ones are hypothesized by the authors to offer the based protection/performance trade-off?

The performance of a state-of-the-art defence setup on ARE would be of interest

### Soundness
3

### Presentation
3

### Contribution
2
