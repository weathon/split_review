# AI Agents Should be Regulated Based on the Extent of Their Autonomous Operations

- Decision: Reject
- Scores: 8, 7, 6

## Abstract
This position paper argues that AI agents should be regulated by the extent to which they operate autonomously. AI agents with long-term planning and strategic capabilities can pose significant risks of human extinction and irreversible global catastrophes. While existing regulations often focus on computational scale as a proxy for potential harm, we argue that such measures are insufficient for assessing the risks posed by agents whose capabilities arise primarily from inference-time computation. To support our position, we discuss relevant regulations and recommendations from scientists regarding existential risks, as well as the advantages of using action sequences---which reflect the degree of an agent’s autonomy---as a more suitable measure of potential impact than existing metrics that rely on observing environmental states.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper states that AI agents should be assessed based on their capabilities for autonomous operation instead of on the amount of data that went into training.

### Strengths
The paper states clearly what the current state of the art is in the domain of AI regulations. Existing approaches (training compute and inference compute) are clearly described and their use (or lack thereof in the case of inference compute) is well explained.

### Weaknesses
It is slightly unclear what is meant by "autonomous" in the context of LLMs, long-term decision making, and physical world interactions.

The paper seems a bit EU-centric, focusing on the EU AI Act. There is a recent OECD report that focuses on AI capabilities that could also be included (https://www.oecd.org/en/publications/introducing-the-oecd-ai-capability-indicators_be745f04-en.html)

### Questions
The paper mentions autonomous operation and decision making over time - how are these addresses in the autonomous cars community?
At what level are the proposed regulations meant? National, international, independent?
Who should decide on acceptable capabilities?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This position paper argues that current regulatory approaches focused on AI training compute are insufficient for addressing the existential risks posed by advanced AI agents. The authors propose a new regulatory framework that limits the extent of autonomous operations by constraining the length and structure of action sequences or action graphs that AI agents can take without human oversight. The paper explains that action sequences better capture potential risks in open-ended environments than training configurations. It advocates a conservative, empirically grounded approach, allowing longer autonomous behavior only after shorter sequences have been shown to be strongly acceptable. The paper also considers multi-agent scenarios and outlines possible implementation and enforcement strategies, presenting the framework as a baseline and a call to action for future research.

### Strengths
1. The paper argues that existing regulations focused on AI training compute are inadequate for addressing the existential risks posed by advanced AI agents, and emphasizes the need for regulatory frameworks that focus on the agent’s autonomous behavior and decision-making process.

2. The paper proposes a novel and thoughtful framework based on limiting the length and structure of autonomous action sequences (and action graphs), offering a more practical way to assess and manage risks from real-world AI behavior.

3. The paper discusses existing regulatory strategies, such as the EU AI Act, and effectively explains their limitations given the growing complexity and autonomy of modern AI systems.

4. The authors considered multi-agent scenarios and thoughtfully extended the framework by introducing action trees and action graphs.

5. The paper is well-written and easy to understand.

### Weaknesses
1. The authors mention that for some advanced AI agents, the line between training (when the AI learns) and inference (when it uses what it has learned) may become blurry, but they don’t explain how this would affect regulators’ ability to monitor, measure, or enforce limits on autonomous behavior.

2. The paper suggests that we should only allow AI agents to do longer tasks if we've tested and proven that doing slightly shorter tasks is safe. But in the real world, there are so many different kinds of tasks and situations, it would be too slow and difficult to test each one. As AI agents become more powerful and operate in more complex environments, this kind of safety testing might not keep up or work well at scale.

### Questions
Please see weaknesses.

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This position paper argues that regulatory frameworks for advanced AI agents should shift focus from training/inference compute metrics to the extent of autonomous operations, measured by the length and structure of action sequences (or graphs) that an agent can undertake without human intervention. The authors critique existing proposals, such as the EU AI Act’s FLOP-based thresholds. and show they fail to capture risks posed by agents whose capabilities primarily arise at inference time .  After reviewing agent architectures and compute-based regulations, they formalize a framework in which any sequence of autonomous actions beyond an empirically validated safe length T is prohibited. They further generalize from single-agent sequences to multi-agent action trees/graphs, and suggest implementation via developer submissions of (i) a designated action space, (ii) an autonomy limit on sequence length, and (iii) safety evidence for shorter sequences. The paper positions this as a baseline call to action toward more robust, state-agnostic regulation of AI agents against existential risk.

### Strengths
1. The paper persuasively shows why training or inference compute alone cannot bound long-horizon strategic risks, illustrating pitfalls such as parallelized inference and blurred inference–training boundary.

2. By basing regulation on action‐sequence length, the authors introduce a concrete, implementation-ready criterion that sidesteps unobservable state-based impact measures .

3. Extending from linear sequences to action graphs, they accommodate collaborative agent behaviors, increasing the framework’s applicability.

4. The suggested developer submissions (action space, autonomy limit, safety evidence) provide a tangible workflow for regulators and incentivize explicit enumeration of permissible actions.

### Weaknesses
1. The framework is largely conceptual. There are no experiments or case studies demonstrating how one chooses a safe threshold T for real-world LLM‐based agents or measures empirical safety evidence.

2. While action spaces must exclude "dangerous" options, the paper provides little guidance on how to identify or verify that all individual actions are safe under diverse deployment contexts. From an RL perspective, credit assignment is still a hard problem to solve. How to identify which actions could be unsafe in the future?

3. The paper does not address how malicious actors might craft action sequences that appear safe by design yet covertly embed hazardous sub-sequences.

### Questions
How would one empirically derive or validate a maximum safe action-sequence length T for a given agent class? What statistical or simulation-based protocols do you envision?

Can you provide concrete examples of how to enumerate a designated subspace of actions for LLM agents (e.g., token generation vs. external API calls) and decide which primitives warrant regulation?

What red-teaming methodologies could regulators employ to ensure that declared safety evidence is robust against adversarially crafted action sequences that exploit semantic loopholes?

### Presentation
3
