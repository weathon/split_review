# Managing Diffuse Risks in the Safe Deployment of Untrusted Large Language Models

- Decision: Accept
- Scores: 5, 8, 8

## Abstract
As large language models (LLMs) grow more powerful, they also become more difficult to trust. They could be either aligned with human intentions, or exhibit "subversive misalignment" -- introducing subtle errors that bypass safety checks. Although individual errors may not immediately cause harm, each increases the risk of an eventual safety failure. With this uncertainty, model deployment often grapples with the tradeoff between ensuring safety and harnessing the capabilities of untrusted models. In this work, we introduce the ``Diffuse Risk Management'' problem, aiming to balance the average-case safety and usefulness in the deployment of untrusted models over a large sequence of tasks. We approach this problem by developing a two-level framework: the single-task level (micro-protocol) and the whole-scenario level (macro-protocol). At the single-task level, we develop various \textit{micro}-protocols that use a less capable, but extensively tested (trusted) model to harness and monitor the untrusted model. At the whole-scenario level, we find an optimal \textit{macro}-protocol that uses an adaptive estimate of the untrusted model's risk to choose between micro-protocols. To evaluate the robustness of our method, we follow \textit{control evaluations} in a code generation testbed, which involves a red team attempting to generate subtly backdoored code with an LLM whose deployment is safeguarded by a blue team. Experiment results show that our approach retains 99.6\% usefulness of the untrusted model while ensuring near-perfect safety, significantly outperforming existing deployment methods. Our approach also demonstrates robustness when the trusted and untrusted models have a large capability gap. Our findings demonstrate the promise of managing diffuse risks in the deployment of increasingly capable but untrusted LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a defense for safely using untrusted large language models (LLMs) that may generate harmful outputs. This defense involves a two-step process. First, a trusted, weaker model monitors the stronger, untrusted model’s outputs, checking each task for potential harm. In the second step, the system monitors the long-term performance of the untrusted model, dynamically adjusting the acceptance threshold based on the model’s reliability. If the model consistently performs safely, the threshold is raised, making rejections less likely. Experiments in a code-generation test environment show that this approach achieves high safety with minimal compromise to the untrusted model’s effectiveness.

### Strengths
- The topic of safely using untrusted models is interesting.
- The paper is well-structured.
- The idea of dynamically assigning thresholds is nice.

### Weaknesses
Some weaknesses in my view:

- The authors should consider the potential synergy between tasks, as this might allow more stealthy attacks.
- There should be discussion on how to defend against adaptive attacks, where an adversary gradually increases the harmfulness of tasks.
- The assumptions underlying the strength of trusted models need further clarification, including whether these assumptions are reasonable.

I have three main questions regarding the synergy between tasks, potential countermeasures against attackers, and the assumptions underlying the attack model, as outlined below:

The proposed method does not seem to account for the synergy between tasks. Specifically, an adversary might bypass defenses by performing harmful actions through a sequence of well-designed tasks. For instance, if transferring money from A to B is harmful, the model could break this action into two steps: first transferring money from A to C, and then from C to B. Overlooking task synergy could fail to detect such harmful intentions.

The core of the proposed defense is dynamically adjusting the threshold that determines whether a task is untrusted based on the model’s credibility, which is calculated from previous performance. In this case, an adversary could adapt their behavior, first establishing credibility by performing safe tasks, then gradually increasing the harmfulness of their actions while keeping them below the threshold. Eventually, the threshold might become high enough that the system perceives all actions from the adversary as harmless, despite potentially harmful intentions.

The authors assume that, alongside the untrusted strong model, the defender has access to a series of weak trusted models to assess harmfulness. However, this assumption requires further discussion. If the trusted models are too weak, the untrusted model could deceive them. Conversely, if they are too strong, it raises the question of why these trusted models are not simply used to perform the tasks directly. The experimental setting raises this concern further, as the authors use Claude-3-Opus as a "weak" trusted model, which performs almost as well as the untrusted “strong” model.

### Questions
see the section on Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper takes inspiration from Paul Christiano's definition of a "low stakes" scenario and defines the problem of Diffuse Risk Management -- where the goal is to deploy a strong, but untrusted LLM to maximize usefulness while minimizing harm. This setting is very interesting and the paper clearly defines the problem formally. The paper then proposes a solution to this problem by decomposing the solution into a pair made up of (a) macro protocol and (b) a set of micro protocols. The micro protocols act at a task/problem instance level and output the input's answer along with an estimate of the safety score (based on a weaker but trusted model). The macro protocol employs this set of micro protocols and chooses between these responses based on the track record of the powerful but untrusted model. The macro protocol learns to estimate the usefulness/safety of a response based on an evolving set of hypotheses that get updated using a bayesian inference framework. The paper shows strong empirical evidence of the effectiveness of their adaptive protocol over static baselines. The authors conclude by discussing the limitations and proposing interesting future direction of research.

### Strengths
1. The problem being introduced is very interesting and relevant. The paper defines the problem statement very clearly.
2. The decomposition into micro and macro protocols is compelling and well explored
3. The paper provides strong empirical analysis using several state of the art models.
4. The paper provides useful details the appendixes.
5. The writing is generally very clear* and engaging.

* barring some details in the equations and mathematical formulation

### Weaknesses
The mathematical formulation could be improved by providing some details and an example.
    - E.g., "To establish credence on U ’s alignment, our macro-protocol tracks hypotheses h_i" could be clarified to indicate that the number of hypotheses is not related to the number of micro protocols (unless I'm misunderstanding something).
    - Similarly, in Eq 7, it is unclear what s_i refers to as it isn't referred to anywhere else
    - The effect of number of hypotheses, and how the authors develop the reference distributions etc. are missing, and such details are important for future work to build up on this work.

The other main weakness I see, and the authors already acknowledge this as a future work item is exploring the capability gap. This is very important, especially in a low-stake scenario (as assumed by the paper) because as Paul Christiano points out ((https://ai-alignment.com/low-stakes-alignment-f3c36606937f)), it is important in this setting for the humans/monitoring systems to understand the outputs of the LLM, and if we use a weaker model, is it feasible to assume the weaker model can always detect a stronger model's subtly malicious intent?

### Questions
1. While somewhat intuitive, it'd be great if you could add a discussion around why it's reasonable to expect that a weak trusted model can exist in the first place -- i.e., if the model is trusted due to extensive testing, why can't the same testing be done for the larger model? (Answer: because the larger model can be more subtle about cheating the test -- but what's the guarantee that the weaker tested model isn't capable of doing the same?).

2. Nit: Eq (5) -- Why is x_t missing from the equation but is part of the description?

3. I don't fully understand how the hypotheses are defined, how many should one define and how does that quantity impact the performance of the system. Either an example or description of the heuristics would be very useful here. 

4. What's the intuition behind adaptive protocol being _safer_ than static threshold protocol (Figure 2 [left])? E.g., i could set the static threshold to be very high such that it always triggers trusted model, which should ideally 'never' return unsafe code.


5. Does the red team have access to the model being queried? It's unclear because in the paper you say "To simulate the worst-case scenario, we grant the red team more affordance to adversarially attack the blue team and minimize safety: 1) given a micro-protocol used by the blue team..." -- does this imply access to the trusted model as well? If so, why would the red team have to estimate the blue team's monitor score? And if not, is it a reasonable threat model to consider?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a framework for safely deploying untrusted large language models (LLMs) by introducing Diffuse Risk Management to balance usefulness and safety in scenarios where subtle misalignments may go undetected. The approach involves two layers: micro-protocols to manage task-level interactions and macro-protocols to dynamically adjust the selection of micro-protocols based on the model’s observed behavior. This setup is evaluated in a red team vs. blue team setting, particularly on code generation tasks where backdoor vulnerabilities are plausible risks. The proposed methods reportedly improve both safety and usefulness tradeoffs compared to baseline approaches by continuously updating the model’s trust assessment and balancing between a powerful but risky model and a weaker, safer one.

### Strengths
- The research question is interesting and important, which is a valuable addition for safe LLM deployment.

- The red team vs. blue team evaluation on code generation tasks effectively demonstrates the framework's performance and practical relevance.

- Results show significant gains over baselines, indicating that the adaptive framework achieves a good balance between utility and safety.

### Weaknesses
 - The layered approach of micro-protocols for individual tasks and a macro-protocol for overall risk adjustment is promising, but the macro-protocol’s Bayesian update mechanism needs further clarification. Detailing how credence values are updated based on safety scores would make this process easier to replicate. Including pseudo-code or equations for these updates, specifically on initial priors and how evidence from each task influences credences, would enhance clarity. Additionally, the concept of a “mixed-strategy Nash equilibrium” to model interactions between red and blue teams is mentioned briefly; a more thorough integration of this equilibrium into the protocol's design would improve its practical relevance.

- Relying on a pre-defined reference distribution of aligned and misaligned outputs may limit scalability, particularly for rapidly evolving or open-ended tasks. Information on how this distribution was generated (e.g., sample size, diversity, labeling criteria) would enhance transparency, especially if future tasks diverge from those tested here. Discussing alternative strategies, like dynamically updating the reference set or using sampling techniques, could make this approach more feasible for real-world applications.

- The safety-usefulness tradeoff is well-explored, yet the effects of varying the safety coefficient (α) on model behavior would be worth examining. Showing how different α values impact the macro-protocol’s balance between safety and utility would clarify its adaptability to different risk levels. Also, adding performance comparisons across different red team tactics or over varying task sequence lengths could highlight whether the adaptive protocol consistently outperforms static approaches or if its advantages diminish in certain scenarios.

- The red team’s static attack strategy does not capture adaptive, iterative evasion that may be expected from real-world adversaries. Enabling the red team to adjust its strategy based on blue team responses would create a more rigorous test of the framework’s defenses. Additionally, although “sneakiness” is used to rate adversarial examples, it remains unclear how this is quantified or validated. Defining sneakiness in more detail, perhaps with examples of high- vs. low-sneakiness backdoors, would improve the credibility of the threat model.

- The reliance on a significant capability gap between trusted and untrusted models raises concerns about scalability. Testing the framework with a smaller gap, such as using different versions of similar models or narrowing the gap incrementally, would shed light on its robustness. Showing how detection accuracy varies with smaller capability gaps would help determine if this approach holds up as trusted models begin to approximate the untrusted model’s performance, a likely future scenario.

- While the approach is well-suited to code generation, other domains like recommendation systems or content moderation involve more subjective forms of misalignment. Discussing how the micro- and macro-protocols could adapt to detect implicit or subtle safety risks in these fields would broaden the framework’s applicability. Insights into handling subjective safety evaluations, where misalignment is not as binary as in code, would show how this approach could extend to tasks with different alignment requirements.

- A minor issue in the paper is a broken reference in Appendix G section, specifically in Finding 2, where the reference to the intended figure is missing (“Figure ??”).

### Questions
- How does the macro-protocol handle varying types of misalignment or malicious behavior in adaptive red team settings?

### Soundness
3

### Presentation
3

### Contribution
3
