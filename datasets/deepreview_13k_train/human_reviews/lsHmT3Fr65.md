# Adversarial Testing in LLMs: Insights into Decision-Making Vulnerabilities

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
As AI systems, particularly Large Language Models (LLMs), rapidly advance towards surpassing human cognitive capabilities, ensuring their alignment with human values and safety standards emerges as a formidable challenge. 
This study addresses a crucial aspect of superalignment by investigating the decision-making capabilities and adversarial vulnerabilities of LLMs, focusing on GPT-3.5, GPT-4 and Gemini-1.5, within structured experimental settings that mimic complex human interactions.
We applied an adversarial framework to two decision-making tasks—the two-armed bandit task and the Multi-Round Trust Task (MRTT)—to test the vulnerabilities of LLMs under adversarial conditions. 
In the bandit task, the adversary aimed to induce the LLM's preference for the predefined target action with the constraint that each action must be assigned an equal number of rewards. For the MRTT, we trained two types of adversaries: one aimed at maximizing its own earnings (MAX) and the other focused on maximizing fairness (FAIR).
GPT-4 and Gemini-1.5 showed a bias toward exploitation in the bandit task, prioritizing early-established strategies, which made them predictable and vulnerable to manipulation. 
GPT-3.5, while more exploratory in the bandit task, demonstrated more risk-seeking behavior in the MRTT, leading to increased vulnerability in interacting with the MAX adversary.
Notably, Gemini-1.5 excelled in the MRTT, adapting effectively to adversaries and outperforming both GPT-3.5 and GPT-4 by balancing risk and cooperation with its adversaries. 
By presenting a specific set of tasks that characterizes decision-making vulnerabilities in LLM-based agents, we provide a concrete methodology for evaluating their readiness for real-world deployment. 
The adversarial framework proved a powerful tool for stress-testing LLMs, revealing the importance of ensuring that AI models are both robust against adversarial manipulation and responsive to fairness cues in complex, dynamic environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an  exploration of the decision-making vulnerabilities of Large Language Models (LLMs) by applying an adversarial framework to two classic decision-making tasks: the two-armed bandit task and the Multi-Round Trust Task (MRTT). The authors test three prominent LLMs: GPT-3.5, GPT-4, and Gemini-1.5, comparing their performance to human participants in both tasks.

### Strengths
The proposed framework looks interesting. The problem of LLM decision making with adversarial testing is new.

### Weaknesses
Prompt Robustness:  LLMs can be very sensitive to the prompt design. Is the observation a product of particular prompt design? The paper has only used a single prompt for both the tasks. A generic framework could be designed where prompts can be varied and new scenarios added to check the robustness of the results. Please create variations of the scenarios to make sure the observations are indeed generic. Please also give the temperature of the LLM used and if possible make more runs to report trends.

In MRTT, it needs to be ensured to conduct the experiment with different range of values to check if they hold before inferring conclusions on LLM behavior .

Lack of understanding of GPT 3.5 exploratory mechanisms : Though evidence accumulation is well studied in humans , it is still relatively new in LLMs. The inference that the switching action of GPT 3.5 underlies robust exploration strategies needs more evidence, though the current adversarial design might not accommodate it. It could just be a greedy mechanism that is immune to this particular choice of adversarial attack instead of any robust exploratory mechanism.

Controlled Environments: While the use of controlled environments allows for rigorous experimentation, it may not fully capture the complexity of real-world decision-making scenarios. Inclusion of some realistic RL scenarios as a case study or an experiment will benefit the paper from an alignment perspective. Also, the capabilities of the adversary can be specified more clearly with applications.

Please improve captions of figures and include at least one open source LLM if possible.

### Questions
In  L320 'burned target' is not clear to me. Can u please elaborate.

In L327, it is give "Unlike GPT-3.5, GPT-4 and Gemini-1.5 consistently preferred the target action once established." I dont think this is new information , prior papers have explored LLM decision making and fixations on rewards in a greedy mechanism, but they haven't been cited. Please check the following papers:
Can large language models explore in-context?
Controlling Large Language Model Agents with Entropic Activation Steering

In the original Dezfouli paper from which the experiment design is inspired also has a Go/No Go paradigm, any reason why this wasn't tested?

### Soundness
2

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
3

### Summary
This work presents a framework to evaluate the decision-making processes of language models under adversarial settings. This work evaluates popular LLMs on two settings – a) a two-arm bandit task and b) a multi-round trust task (MRTT). Results show that LLMs are more prone to exploitation than humans on the bandit task. On the MRTT task, Gemini-1.5 outperforms all baseline methods, notably GPT-4. Overall, the results show that there is still scope for improvement in the decision-making strategies of popular LLMs.

### Strengths
1. The problem setting is relevant and interesting. As LLMs scale and improve, it is a generally interesting question to understand their decision-making processes, particularly under adversarial settings. 
2. The results, although in toy settings, are noteworthy. It is notable that it is possible to train a powerful adversary, and that an RNN-model can replicate the decision-making processes of a LLM to a certain degree.

### Weaknesses
1. **Writing**: Writing is very poor and often redundant. The *abstract* and *conclusion* are longer than needed and do not effectively summarize the work. Specifically, the discussion and conclusion have a lot of redundancies, with lines (495-500) essentially repeating scaffolding from the conclusion. The first paragraph of the discussion (lines 450-458) is very generic and contributes little technical discussion. On the other hand, the *method* section does not build up motivation properly and dives straight into notation without a proper setup of the problem. For example, the statement *"The adversary assigns rewards to both potential actions with the constraint that each action receives an equal number of potential rewards (25 times)"* (Line 179) is unclear and lacks a concrete definition, which is standard in RL. I also think that a separate *related work* section should be added, and some content should be moved over from the introduction. The current flow of the *introduction* is not smooth. There are also experimental details missing (such as details about the human experiments for the bandit task). Furthermore, the title of the subsection on the bandit task (lines 174-175) incorrectly mentions MRTT in the first sentence, disrupting the flow. Line 180 also incorrectly refers to "GPT" instead of "LLMs", as the bandit experiment is also run on Gemini. 

2. **Experiments**: The experimental settings are very simplistic and although the insights are interesting, they might not scale/apply to real-world problem setups. 

3. **Method**: Some design decisions are unclear and do not seem optimal. For example, the adversary controls the observation of the LLM but it is unclear what this observation is for the bandit task. Similarly, I am not sure why the reward probabilities for both actions are set to be the same in the bandit task.


### Questions
1. What are the details about the human experiments conducted for the two-armed bandit task (how many humans, the setup of the human experiment, etc.,)? 
2. What is the observation $o_t$ in the bandit task? How does the adversary manipulate this observation?
3.  *“The adversary assigns rewards to both potential actions with the constraint that each action receives an equal number of potential rewards (25 times)”*. What does this mean? How is the constraint of the number of potential rewards enforced? The paper could really benefit from a better description of the mathematical setup. 
4. There should be some optimal way to solve the two-arm bandit problem (using algorithms like UCB). What do those trajectories look like and what does the action distribution look like in this case? That is, is there an optimal action distribution?
5. Why are the reward probabilities for both planets in the bandit task set to be the same? If they are slightly different (eg, 0.24 and 0.26), then the optimal limiting policy is to always select the higher probability planet. In such a setting, the target action of the adversary could be to induce the action of the lower reward planet. 
6. Figure 4 (sample simulation plots) have very low readability. I think the visualizations could be made better to show the overall trend of the actor and adversary policies. 
7. In the abstract, the bandit task is properly defined but the MRTT task is not. The abstract dives straight into the adversaries trained for MRTT without introducing what MRTT is. 
8. It would be interesting to provide some analysis on the learned RNN and how well it is able to model the LLM’s decision-making process.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper examines the decision-making capabilities and adversarial vulnerabilities of LLMs, specifically GPT-3.5, GPT-4, and Gemini-1.5, within structured experimental settings designed to simulate complex human interactions. The study employs an adversarial framework in two decision-making tasks: the two-armed bandit task and the Multi-Round Trust Task (MRTT). In the bandit task, the adversary’s goal was to manipulate the LLM’s preference towards a target action under equal reward conditions. In the MRTT, adversaries were trained either to maximize their own earnings (MAX) or to enhance fairness (FAIR).

### Strengths
1. The paper focuses on a good aspect when using LLM agents to solve online decision-making problems with adversarial environments.

2. The paper is overall well-written and easy to understand.

3. The behavioral analysis involving human beings is interesting.

### Weaknesses
1. The paper could be strengthened by including more recent and relevant studies, such as

Krishnamurthy, Akshay, Keegan Harris, Dylan J. Foster, Cyril Zhang, and Aleksandrs Slivkins. "Can large language models explore in-context?." arXiv preprint arXiv:2403.15371 (2024).

Despite it is an arXiv article to the best of my knowledge, this is among the first few papers seriously discussing applying LLMs to bandit-related problems.

2. Consider incorporating and evaluating more advanced LLMs, such as GPT-4 Turbo and the o1 model. Analyzing these newer models could provide a deeper understanding of the capabilities and limitations of current LLM technologies in adversarial decision-making contexts.

3. The paper considers a 2-armed bandit problem as a case study. It is necessary to extend the number of arms to general settings. The focus on a 2-armed bandit problem, while insightful, limits the generalizability of the findings. Expanding the experimental setup to include MAB problems with more than two choices could offer a more comprehensive view of LLM behavior in complex decision-making scenarios.

In summary, the authors are recommended to integrate comparisons with standard adversarial MAB algorithms and extend the analysis to more general MAB settings, including evaluations on GPT4 Turbo and o1 models.

### Questions
1. How does the proposed methods (for example, Gemini 1.5 based on the proposed framework) compare against classic algorithms such as EXP3 for adversarial bandit problems?

2. Can the performance of LLMs be theoretically guaranteed when facing adversarial environments? Can the proposed framework provide some insights?

### Soundness
3

### Presentation
3

### Contribution
2
