# Interactive Speculative Planning: Enhance Agent Efficiency through Co-design of System and User Interface

- Decision: Accept
- Scores: 8, 6, 5

## Abstract
Agents, as user-centric tools, are increasingly deployed for human task delegation, assisting with a broad spectrum of requests by generating thoughts, engaging with user proxies, and producing action plans. However, agents based on large language models (LLMs) often face substantial planning latency due to two primary factors: the efficiency limitations of the underlying LLMs due to their large size and high demand, and the structural complexity of the agents due to the extensive generation of intermediate thoughts to produce the final output. Given that inefficiency in service provision can undermine the value of automation for users, this paper presents a human-centered efficient agent planning method -- Interactive Speculative Planning -- aiming at enhancing the efficiency of agent planning through both system design and human-AI interaction. Our approach advocates for the co-design of the agent system and user interface, underscoring the importance of an agent system that can fluidly manage user interactions and interruptions. By integrating human interruptions as a fundamental component of the system, we not only make it more user-centric but also expedite the entire process by leveraging human-in-the-loop interactions to provide accurate intermediate steps. Code and data will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Describes a speculative planning algorithm for LLM agents that assumes an approximate model and a target model. It is assumed that the target model is more capable but slower than the approximate model. Planning is performed by the approximate model until it is deemed to deviate from the target model, at which time the approximate model is corrected. Human interaction is also addressed via a rescheduling algorithm and the ability to interrupt and modify the plan.

### Strengths
The problem is relevant, agents are slow and we should try to make them more responsive.

The approach is novel afaik.

The algorithm itself is clearly described.

### Weaknesses
The algorithm trades off time with efficiency. Are there ideas to also improve efficiency?

The selection of an approximate model and the target model may be difficult to satisfy, and increase system complexity in practical applications.

### Questions
The evaluation could be improved by comparing a smaller and larger model from a particular model family, i.e. 8b vs. 70b llama using the same approach. 

Are there more efficient approaches to validating the approximate models plan without comparing directly to the target models plan?

If the user interrupts the plan, do you envision that they edit the agents trajectory directly? or provide feedback and have the agent regenerate the step?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an interesting approach to reduce the potential latency of LLM-based systems and an approach where user and user interruptions are build into system design. The approach involves two different agents: an faster but more error-prone approximation agent and a slower but more accurate target agent. Depending on the accuracy of approximation agent, the speed of system can be significantly faster , and in the worst case, comparable to a non-speculative planning agent.

### Strengths
Overall, the architecture of using a faster (but potentially inaccurate) agent and a slower (but possibly more accurate) in order to reduce the latency of the system is an interesting idea and can potentially work well for certain tasks with careful UI considerations.

### Weaknesses
1. The method applies to synchronous Human-AI interaction where a human is in the loop and waiting for agent response in real time. An entirely different application of Agents is asynchronous interaction (where a human may not be in the loop in real-time, e.g. perform this action every day at this time ..). I would encourage the authors to highlight this in order to position their work better. 

2. I vehemently agree with the statement "A fully automated “blackbox” agent system with prolonged response delays is suboptimal for user experience". However, I believe the paper uses the term "user-centric" a bit loosely, I am not quite sure how the current method is more "user-centric". There are many places of contention:

a) Given approximation agent and target agent can (often) disagree, it means initial responses may be overwritten or multiple intermediate responses shown to user. Without careful UI design, this can lead to user confusion and lack of transparency on what is going on. 
b) User in the loop workflow where user can actively take part in the decision making is absolutely necessary. However, in the current system, the window for interruption is basically the time for target agent to execute. The user can potentially take time to read the response from approximation agent, process it, decide if it needs to be revised manually and then potentially frame the revision in text or voice, all of which can take some amount of time.  I am failing to see how this is "user-centric" when user is hurried to interrupt within a window of short time.
c) I did not fully understand how this mechanism can work when the action execution can be anything of consequence in the user interaction (e.g. sending an email or request for money to split bill on a mobile pay application). This in practice would mean, if the approximation agent is wrong, the system would perform tons of incorrect actions that can not be reversed. I would like a more detailed limitations of where this approach can work and where it should not be applied. 
 
More generally, there are established ways to study human factors aspects of Human-AI interaction, employing carefully controlled user studies. The current "theoretical approach" to human factors  is an interesting first step but leave a lot of questions unanswered that could potentially make or break the interaction.

### Questions
1. Could a theoretical focus on system latency lead to newer issues in the human-AI interaction? 
2. Is this approach suitable for all tasks? A more detailed discussion would be useful.

### Soundness
3

### Presentation
2

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
The paper introduces a speculative planning framework to improve the time efficiency of agent-based task planning. The paper tackles reducing latency by implementing two agent types. An approximation agent generates initial, potentially incorrect steps, which the more accurate target agent validates. This setup allows speculative planning to proceed concurrently, ideally saving time without sacrificing accuracy. Through experiments with two agent planning benchmarks, OpenAGI and TravelPlanner validation and metrics such as time efficiency, API costs, etc, the paper demonstrates the efficiency gains. It also allows users to get involved in the planning process. However, this aspect is speculative and has not been tested.

### Strengths
1) In terms of writing, the paper is well-organised and engaging. The planning algorithm is discussed well -- the speculative planning process is generally explained well. However, a more detailed discussion with a specific k-value around Fig 1 would be helpful in understanding the various scenarios and how these result due to the accuracy of A. For example, it will help the reader speculate how A's accuracy may impact the number of times replanning may be needed, etc.

2) The paper evaluates various settings (e.g., ReAct, CoT, MAD, and DG), revealing a good level of depth in its potential impacts. The experiments are thorough, with 4 settings and 2 planning benchmarks (OpenAGI and TravelPlanner). Metrics such as time efficiency, API costs, and stepwise validation provide a good depth of analysis, both positive and negative aspects.

3) In terms of novelty, while speculative planning may not be universally applicable, its potential to accelerate high-latency planning tasks is valuable for the AI community, especially for applications requiring real-time or near-real-time responses.

### Weaknesses
1) One downside, not fully addressed or discussed in the paper, is the increased cost. The paper largely supports its claims of time efficiency gains, presenting results indicating speculative planning can save time, especially in complex planning settings. However, cost savings are not fully supported, as all speculative settings incur higher costs. While this increase is expected, as A and T operate concurrently, the paper only highlights positives and does not discuss costs. To balance the discussion, the authors must discuss both sides: pros and cons in Sections 4.1 and 4.2. While time savings are the focus, I assume real-world deployments must balance cost and efficiency, particularly if A has very low accuracy and frequently diverges from the steps produced by T, which increases wasted resources. Therefore, an open discussion about this limitation must be expressed in the same units as efficiency is justified (%) and possibly what strategies may allow users to reduce the cost.

2) Although the title suggests a "co-design" with user interface considerations, the paper provides limited insights into UI and user interactions. I find this aspect genuinely troublesome. The paper is technical. Even the UI elements, such as producing the steps in the correct order etc., are technical contributions. This is not co-design from an HCI perspective. I also have a few more questions on this aspect, which are provided in the Questions section later.

3) The framework relies on hyperparameter k. In the experiments, the authors used k=4 -- why? The appendix does provide some insight into the sensitivity of this parameter. Still, since k is central to the scheme, providing some guidance on selecting k would be beneficial. For example, could we employ dynamic tuning of k, etc?


Minor issues:
- 048: and The sequential
- In Figure 1, please briefly state the reason for using Venmo as an example.
- Line 100: Statements like "This strategy [[potentially]] reduces the time a target agent" suggests either that this gain is not universal or that the authors have doubts about their results. If there are caveats regarding when we expect reduced time, then that needs to be made explicit.
- I did not find the Venmo case study or the diagrams helpful.

### Questions
Since the cost is one of the main issues:

1) Under what circumstances should each evaluation metric (e.g., accuracy vs. speed vs. cost) be prioritised, and how might these impact the framework's configuration, e.g., in terms of k? The cost increase is above 60% in some cases. For example, do the authors believe there is a case for solely focusing on cost and not efficiency and vice versa?

2) Do the authors have insight into reducing costs to make the approach more appealing? The appendix states: "...Implement a more sophisticated approximation-target judgment method..." --- What does this look like?

Regarding the ability of the users to intervene, etc.:

3) How do you envision training end-users on the speculative planning interface, particularly in complex tasks where they may need to understand and manage concurrent agent processes?

4) Also, given that user intervention is integral to your framework, how would you design the interface to facilitate timely and accurate user decisions?

Regarding resource-constrained environments:

5) What considerations should be explored for scaling the speculative planning framework in resource-constrained environments, especially where concurrent instances of T may lead to bottlenecks? 
6) Since the approach's success largely depends on the accuracy of A, what do the results and analysis of k (in the appendix) indicate in terms of any minimum thresholds for A's accuracy?

### Soundness
3

### Presentation
2

### Contribution
2
