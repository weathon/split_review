# ToM-agent: Large Language Models as Theory of Mind Aware Generative Agents with Counterfactual Reflection

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Recent studies have increasingly demonstrated that large language models (LLMs) possess significant theory of mind (ToM) capabilities, showing the potential for simulating the tracking of mental states in generative agents. In this study, we propose a novel paradigm called ToM-agent, designed to empower LLMs-based generative agents to simulate ToM in open-domain conversational interactions. ToM-agent disentangles the confidence from mental states, facilitating the emulation of an agent's perception of its counterpart's mental states, such as beliefs, desires, and intentions (BDIs). Using past conversation history and verbal reflections, ToM-Agent can dynamically adjust counterparts' inferred BDIs, along with related confidence levels. We further put forth a counterfactual intervention method that reflects on the gap between the predicted responses of counterparts and their real utterances, thereby enhancing the efficiency of reflection. Leveraging empathetic and persuasion dialogue datasets, we assess the advantages of implementing the ToM-agent with downstream tasks, as well as its performance in both the first-order and the second-order ToM. Our findings indicate that the ToM-agent can grasp the underlying reasons for their counterpart's behaviors beyond mere semantic-emotional supporting or decision-making based on common sense, providing new insights for studying large-scale LLMs-based simulation of human social behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes a novel framework, ToM-agent, aimed at enhancing LLMs in generating open-domain conversational interactions with Theory of Mind (ToM) capabilities. This approach enables agents to simulate tracking mental states—specifically, beliefs, desires, and intentions (BDIs)—of their conversation counterparts by introducing methods for dynamically updating inferred BDIs and confidence levels based on past conversations. A unique feature of the ToM-agent is its counterfactual reflection mechanism, which evaluates the discrepancies between predicted and actual responses to refine the agents’ understanding of mental states. Through experiments on empathetic and persuasive dialogue tasks, the study demonstrates that ToM-agent can better align with human social behaviors compared to traditional LLM-based agents, particularly in understanding complex conversational nuances beyond simple semantic support.

### Strengths
Originality: The paper introduces a fresh approach by applying Theory of Mind (ToM) to open-domain conversations with LLMs, an area traditionally limited to narrow, task-based settings. The ToM-agent’s design, which tracks beliefs, desires, and intentions (BDIs), is a promising direction for making LLMs more socially aware and adaptable.

Quality: The paper presents solid experimental results on two conversational tasks, showing the ToM-agent's ability to accurately understand mental states. The ablation studies, which highlight the counterfactual reflection’s role in improving performance, add depth to the evaluation.

Clarity: The paper is well-structured, with clear explanations and visual aids that make complex ideas like counterfactual reflection and BDI tracking easy to understand. Key concepts, such as the distinctions between first- and second-order ToM, are defined effectively, supporting reader comprehension.

Significance: By enabling agents to better track human mental states, this work has the potential to enhance conversational AI applications. Although higher-order ToM is not explored, the framework represents an important step in developing more socially aware agents, which could benefit fields like psychology and human-computer interaction.

### Weaknesses
 - The paper mentions suboptimal confidence levels in “bad” dialogue examples but doesn’t go into detail about why these examples failed or how they could be improved. A deeper analysis of these cases, especially where the ToM agent’s confidence wavered, would help identify model limitations and provide insights for improving reliability in complex scenarios.
- While the study uses GPT-4 and GPT-3.5, it lacks comparisons with a wider range of ToM-capable models. A more comprehensive evaluation could be made.
- The paper does not report inter-rater agreement for human evaluations of first- and second-order ToM, which weakens the credibility of subjective assessments.

### Questions
Working on the weaknesses listed would suffice.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This study introduces ToM-Agent, designed to extend the application of ToM to open-domain conversational scenarios. The model leverages the BDI (Belief, Desire, Intention) tracking mechanism that distinguishes between belief and confidence By simulating varying degrees of confidence in different mental states, ToM-Agent enables more psychologically nuanced and natural conversations.

### Strengths
- This paper is well-written. 
- Using open-domain empathetic and persuasive dialogue datasets showcases the potential for practical implementations. 
- Experimental results validate the proposed method's effectiveness.

### Weaknesses
This paper addresses a highly relevant topic, but the methodological innovation is limited. The approach mainly depends on prompting LLMs to assess BDIs and confidence levels, which poses scalability challenges. Furthermore, the study would benefit from incorporating more baselines and providing additional details about the human evaluation process, including annotator qualifications and evaluation criteria.

### Questions
- The study builds upon existing frameworks, utilizing reflection mechanisms and ToM capabilities of LLMs. Introducing BDIs along with confidence levels is an interesting addition. However, evaluating BDIs and confidence levels using an LLM based on previous dialogue history raises scalability concerns. As the number of agents grows and conversations become longer, the accuracy of confidence assessments may decrease, potentially limiting the scalability of the proposed approach.

- The paper extends prior research by integrating BDIs rather than focusing solely on beliefs. However, the rationale for this added complexity is not clearly articulated. A comparison with a simpler baseline model that updates only beliefs would help clarify the value of incorporating the full BDI framework.

- The experiments rely exclusively on GPT-series models. Including open-source LLMs such as LLaMA could enhance the generalizability and applicability of the findings.

- While the approach is resource-intensive, the performance gains appear marginal. Moreover, the human evaluation lacks transparency—details regarding the qualifications of the annotators and the specific assessment criteria are not provided. More information on the evaluation framework used by human annotators would be beneficial to understand the robustness of the evaluation process.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework to integrate first- and second-order theory of mind (ToM) reasoning into open-domain conversational interaction. The proposed ToM-agent uses beliefs, desires, and intentions (BDIs) to represent an agent’s mental status. During the interaction, the ToM-agent generates utterances based on the inferred top-k BDI candidates of another agent. The estimation of confidence level is disentangled from the BDI representation. Since the predicted and the observed utterances of the other agent may be different, the paper also introduces a counterfactual reflection method to compare the utterances to update the inferred BDI candidates. The evaluation based on the simulated LLM agents shows improved performance in 1st- and 2nd-order ToM inference and increases the success rate in the downstream tasks.

### Strengths
- This paper is the first to integrate ToM reasoning into open-domain conversation.
- Unlike other ToM papers that focus on false belief understanding, this paper includes explicit modules for 2nd-order ToM inference and counterfactual reflection to improve the predicted BDIs.
- The experiments cover two types of dialogue tasks showing promising results for conversations that involve the mental states of other agents.

### Weaknesses
 - The experiments simplify the design of one of the agents as not both agents have the BDI module of the other agent. This will make the types of conversation more limited. For example, if the agent wants to say something to make the other agent empathetic, this won’t be possible if the other agent only has a self-BDI module.
- Since the measurement of the predicted and true BDI is based on the similarity, why does this paper use annotators to evaluate similarity instead of using text embedding to compute similarity as mentioned in section 5.1? What is the inter-rater agreement for these three annotators? Are they ratings calibrated? This way of evaluating similarity adds a huge variance to the evaluation results, making it hard to judge the improvements between runs.

### Questions
- In Table 3, the counterfactual reflection has a similar performance as the reflection in GPT-3.5 and only has more improvements with GPT-4. It seems like the proposed method requires an LLM with better reasoning capability. What are the capability requirements or will any open-source LLMs benefit from the proposed method?
- Why is it important to disentangle confidence level and BDI if the proposed method only selects the top BDI for generating utterances?
- In Figure 2, why the 2nd order ToM judgment module doesn’t receive input from the “BDI tracking with CR” figure?

### Soundness
3

### Presentation
3

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
This paper introduces the TOM-Agent, a conversational model designed to generate responses based on inferred Beliefs, Desires, and Intentions (BDIs). The model uses counterfactual reasoning to update these mental state estimations dynamically during conversations. Performance evaluations focused on the accuracy of first and second mental state estimations and the overall success rate of conversations demonstrate that the TOM-Agent with counterfactual reasoning achieves the best performance.

### Strengths
The paper effectively separates belief from confidence, allowing for dynamic updates to BDIs as conversations progress.

The implementation of counterfactual reasoning is innovative; it shifts from indirect mental state estimation to direct prediction through conversational utterances, enhancing transparency of the prediction process.

### Weaknesses
The application of this model to open-domain conversations raises questions, particularly where BDIs are not explicitly defined or where it is impractical to enumerate all possible BDI combinations used for response ranking.

It would be better to provide a qualitative example on the definition and true BDI annotations in the empathetic and persuasion dialogue.

Figures 3 and 4 are ambiguous regarding the dialogue scenarios they represent (empathetic or persuasive). It can provide more insights to see how the confidence curve changes under different types of dialogues or which condition may trigger “good” or “bad” examples.

Adding transcripts of interactions between humans and the agent would provide a clearer demonstration of the model's practical effectiveness and user experience.

### Questions
The experimental setup where one agent tracks self-BDI and another tracks other-BDI is unconventional. What is the result to equip both agents with the ability to track both self and other BDIs?

### Soundness
3

### Presentation
2

### Contribution
3
