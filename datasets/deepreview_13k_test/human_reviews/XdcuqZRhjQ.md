# LifelongSotopia: Evaluating Social Intelligence Of Language Agents Over Lifelong Social Interactions

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
Humans engage in lifelong social interactions through interacting with different people under different scenarios for different social goals. This requires social intelligence to gather information through a long time span and use it to navigate various social contexts effectively. Whether AI systems are also capable of this is understudied in the existing research. In this paper, we present a novel benchmark, LifelongSotopia, to perform a comprehensive evaluation of language agents by simulating multi-episode interactions. In each episode, the language agents role-play characters to achieve their respective social goals in randomly sampled social tasks. With LifelongSotopia, we find that goal achievement and believability of all of the language models that we test decline through the whole interaction. Although using an advanced memory method improves the agents' performance, the best agents still achieve a significantly lower goal completion rate than humans on scenarios requiring an explicit understanding of interaction history. These findings show that we can use LifelongSotopia to evaluate long-context language models and the social intelligence of language agents over lifelong social interactions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
LIFELONG-SOTOPIA, a new benchmark for evaluating LLMs' social intelligence in long-term interactions (assessing mainly believability and goal completion rate of these agents), builds on SOTOPIA to simulate multi-episode interactions between role-playing agents with social goals.  A memory mechanism allows agents to leverage past interactions, but experiments show that providing full history hinders performance due to inconsistency.  Performance improves with summarized memory, yet LLMs still struggle with complex social scenarios requiring explicit use of past interactions, underperforming humans.

### Strengths
- Novel and Important Problem: This paper tackles the crucial and under-explored area of evaluating social intelligence in LLMs over extended, multi-episode interactions. This is a interesting step beyond static benchmarks and short interactions, aligning more closely with the dynamics of (simulated) human social behavior.

- Extending Benchmarks: The LIFELONG-SOTOPIA benchmark, building upon SOTOPIA, provides a structured and repeatable method for evaluating LLM agents.

- Open Science: The commitment to open-sourcing the code and data is commendable and will facilitate future research in this important area.

### Weaknesses
Limited Diversity of Harder Scenarios: While the hand-crafted harder scenarios are a valuable addition, their limited number raises questions about the generalizability of the findings regarding the models' limitations in leveraging past context. A larger and more diverse set of challenging scenarios would strengthen the conclusions. Would it be perhaps meaningful to enlist a taxonomy of social situations of interest and the complexity in which "social intelligence" would need to address? It would allow us to start building scenarios grounded in dimensions of social intelligence we care about, and would help readers understand where the research is taking us to.

Reliance on LLM for Evaluation: Despite the efforts with BELEXT, does the reliance on GPT-4 as the primary evaluator introduces a potential bias? Exploring alternative evaluation methods, including human evaluation on a larger scale, would enhance the objectivity of the results.  While Llama 3.1 was explored, more justification for why it is insufficient could be also beneficial.

Lack of Ablation Study:  An ablation study investigating the impact of different components of the advanced memory module (e.g., summary length, specific aspects included) would provide a deeper understanding of its effectiveness. This would be an interesting result to many. AFAIK, lots and lots of memory mechanisms have been tested in many different contexts, but very few have offered insights on how memory mechanisms should be constructed.

Exploration of Relationship Dynamics: The paper focuses on different relationship types but doesn't deeply explore how relationship dynamics evolve over multiple episodes. Relationships are more of a byproduct of social (and cognitive) interactions, and not something we're given to. I feel like this specific setup to be a bit superficial, and not too useful.

### Questions
The biggest question is how grounded are we in social interaction theory? and/or to what extent should we be grounded? I was hoping to understand what specifically we mean by "social intelligence", and whether we can build a computational model of such things before running experiments. There has been many attempts to advance subtypes of social intelligence (loosely defined) like cooperation (like deepmind's concordia) and competitiveness (like the diplomacy paper). I think essentially it comes down to can we reliably simulate where cognitive biases and constraints meet social biases and constraints. Could authors shed some light? I feel like believability and goal completion to be a bit too simplistic.

How sensitive are the results to the specific prompt used for generating the episode summaries in the advanced memory module?
Have you considered using other metrics beyond BEL and GOAL to evaluate social intelligence, such as measures of empathy, cooperation, or persuasion?

What are the potential ethical implications of developing LLMs with improved social intelligence, particularly in the context of long-term interactions? The paper touches upon this, but more elaboration would be beneficial.
How might the findings of this work inform the design of more socially intelligent LLM agents and their integration into real-world applications?

Would a curriculum learning approach, where agents are gradually exposed to more complex social scenarios, lead to improved performance in LIFELONG-SOTOPIA?

Could the evaluation be further improved by incorporating a metric that considers the efficiency with which the agents achieve their goals (e.g., number of turns required)?  Humans may prioritize efficiency in certain social situations.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the LIFELONG-SOTOPIA benchmark, a novel evaluation framework designed to assess social intelligence in language agents through simulated multi-episode social interactions. It studies three aspects of language agents: 1.the consistency over long term social interactions, 2. social intelligence and 3. the utilization of memory and early results shows that the current language agents are insufficient in those three axises compared to human baselines.

### Strengths
- This paper explores an important and relatively underexamined area of research: social intelligence in the context of multi-episode and lifelong interactions. Although the findings reveal that current language agents fall short of human capabilities in this regard, the study provides a crucial foundation for future research and offers a valuable dataset and benchmark for subsequent investigations.
- The experimental design and metrics employed (e.g., Believabilityextended) are well-conceived, lending credibility to the results. The discussion regarding the utilization of memory modules in the context of social intelligence is particularly insightful, offering a nuanced understanding of their role in this domain.

### Weaknesses
The result would be more sound if quantitative and qualitative evaluations from human can be provided, rather than relying on on LLM-based judgement.

### Questions
It would be great if the evaluations of other models (Figure 4) can be included as well in the future to provide more comprehensive comparisons.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed a benchmark LIFELONG-SOTOPIA as well as a set of evaluation metrics SOTOPIA-EVAL to evaluate the lifelong social intelligence of language agents. 

The benchmark uses the 40 characters and 90 relations in the SOTOPIA database, uses GPT-4 to create scenarios for each pair of agents to interact with. The role play game includes characters, social goal, secret, relationship, and the scenarios for each pair of agents to have conversations with, and each pair of agents are served with multiple episodes for life-long learning of each other. The benchmark evaluates the believalbility and goal completion two aspect of the agents.

The paper benchmarked GPT-4o, Gemini-1.5, Llamma-3.1 as well as humans' performance, with two memory settings of each: complete interaction history, and concise summary of each episode.

The paper observed that the benchmarked agents lack social intelligence through declining believalbility and goal completion rates compared to humans. The paper also found that using a more concise memory across episode offered better performance compared to using the entire interaction history as memory.

### Strengths
1. The paper investigated in an important problem: life long social intelligence
2. The paper created a benchmark, LIFELONG-SOTOPIA, to study the problem, and the SOTOPIA-EVAL to evaluate believalbility and goal completion, the two aspects of the language agent's performance
3. The paper benchmarked 3 models as well as human evaluations, and presented the performance gap between two
4. The paper proposed a memory condensation method to improve models' performance
5. The paper introduces a set of hand-crafted 'hard scenarios' that probe agent's ability to retrieve relevant past information for current episode purpose
6. The paper is clear and well structured

### Weaknesses
One of the main contributions the paper wishes to highlight is the lifelong learning of the language agents over multiple episodes of interactions between each pair. However, the main results (Figure 3) and the current evaluation metrics (BEL and GOAL) do not critically answer the question: how would agent's past learned interaction change their current behavior, for example, compared to no interaction history at all. As the authors stated in Ln 447, "the past context provided to them may not always be needed and approaching each scenario independently can also allow you to achieve near-perfect performance." 

On this note, 
1) it would be helpful to provide quantitative evaluation to compare with VS without interaction history, and 
2) More experiments on the 'harder scenarios' should be the main results to support the benchmark purpose of lifelong learning'
3) Subsequently, additional evaluation criteria are needed for the harder scenarios (Appx E), as BEL only focuses on if the agent's behavior is 'natural, realistic, and aligned with their profile', and 'GOAL' only evaluates if agent has achieved each scenario goals. An explicit evaluation on how the agent changes their behavior conditioned on their past interactions should be introduced to better measure their lifelong learning capabilities.

### Questions
1. If each episode includes two agents, and their goal could be in contradiction to each other (e.g. Figure 1(1)), then whose GOAL COMPLETION is the metric evaluating?
2. Section 3.1: dataset stats?
3. Table 1: was there only one human evaluator to cross validate GPT-4 as an evaluator's performance?
4. Ln 458-459: why did the authors remove Llama's evaluation, an open sourced model, for Figure 4 harder scenarios,  due to 'the limited availability of API credits'?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new variant of the Sotopia benchmark for evaluating language model agents on iterated social interactions. In this setting, pairs of language model agents adopt different personas (e.g., “Ethan, a 34-year-old chef”) and must achieve various social goals (e.g., “Convince your friend to join you on a trip”). Models are evaluated by GPT-4, based on their ability to achieve these social goals and improve over time from one interaction to the next. The paper evaluates two classes of models, (1) long-context models, and (2) models with a memory-augmentation system which provides short summaries of past interactions, finding that the latter approach performs better.

### Strengths
1. The core idea behind this paper is an important one: humans adapt their interactions to each other not just over the course of a single interaction, but over the course of a lifetime. It is therefore reasonable that we might want language models to exhibit these same behaviors, and some work has attempted to achieve this goal (e.g., the “memory” function in ChatGPT). However, it is difficult to evaluate whether past user interactions actually improves model performance or not
2. The qualitative examples in the appendix are informative about current model failure modes, and the finding that models degrade in performance with past interaction history in context is interesting 
3. The paper is well-written and easy to understand

### Weaknesses
My main concern is that the benchmark does not have significant headroom for model improvement beyond a naive baseline. In particular, it seems clear that including a full history of past interactions degrades model performance, but the advanced memory models and human experiments (lines 412-414) show roughly constant scores across iterations. This suggests that it might not be possible, in principle, to outperform a model with no memory at all.

However, if the authors can convince me that this is not true, I would be willing to raise my score.

### Questions
1. Did you run any experiments on models that have no memory of past interactions at all? How do these perform compared to the models with the advanced memory module?
2. Do either the goal completion or believability scores depend on past interactions? If so, it seems reasonable that GPT-4o might not be a very good evaluator, and even careful humans might struggle

### Soundness
2

### Presentation
3

### Contribution
2
