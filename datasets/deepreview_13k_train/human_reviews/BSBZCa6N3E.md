# Retrospective Learning from Interactions

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
Multi-turn interactions between large language models (LLMs) and users naturally include implicit feedback signals. If an LLM responds in an unexpected way to an instruction, the user is likely to signal it by rephrasing the request, expressing frustration, or pivoting to an alternative task. Such signals are task-independent and occupy a relatively constrained subspace of language, allowing the LLM to identify them even if it fails on the actual task. This creates an avenue for continually learning from interactions without additional annotations. We introduce \textsc{ReSpect}, a method to learn from such signals in past interactions via retrospection. We deploy \textsc{ReSpect} in a new multimodal interaction scenario, where humans instruct an LLM to solve an abstract reasoning task with a combinatorial solution space. Through thousands of interactions with humans, we show how \textsc{ReSpect} gradually improves task completion rate from 31\% to 82\%, all without any external annotation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author proposes a novel framework, Retrospective learning from past interactions (RESPECT), for improving the LLMs based on signals from past interactions via retrospection. They also contributed with a task, Multi-turn Grounded Interaction Scenario (MULTIREF), a conversational interaction scenario where two partners, a speaker and a listener, coordinate on the selection of a set of items. They further fine-tuned an LLM with different optimization techniques with the data collected from the proposed task and framework.

### Strengths
- The idea of learning from past mistakes is really interesting and the proposed framework, RESPECT, doesn't depend on the optimization strategy. As highlighted in the paper, this framework can be used with various optimization strategy (Supervised Learning, Reinforcement Learning, Utility Maximization).
- The paper also contributed with a new task, MULTIREF, which will be very useful for the future development of this domain.

### Weaknesses
 **Major:**
- **Excessive use of training data:** The proposed method relies heavily on data. The model is fine-tuned at each step with all the interaction data acquired from past steps. Now, although the authors mention that they are taking measures to avoid overfitting (lines 246-248), this much repeated data usage would eventually result in overfitting. Specifically, the method aggregates all past interaction data and uses it to fine-tune the model at each round. This repeated exposure to the same data, even with standard regularization techniques, increases the risk of the model memorizing the training data rather than generalizing to new interactions. The authors should provide a more detailed analysis of how they are mitigating this risk beyond standard fine-tuning practices.
- **Lack of metric evaluation:** Although the authors showcases various observations and results through plots and confusion matrix, they lack the tables for comparing different metics. Having those results will significantly boost the paper quality. The absence of tables makes it difficult to quantitatively assess the performance gains and compare the different optimization techniques. The authors should include tables with standard metrics such as accuracy, precision, recall, and F1-score, to provide a more rigorous evaluation.
- **Lack of generalizability of proposed method:**
  - **Across different LLMs:** The proposed framework is only tested on one LLM (IDEFICS2-8B). Now, although this framework can be applied over other LLMs, it is unclear whether it will boost their performance or not. One reason authors might have seen such improvement is because the tested LLM is bad at that particular task. If we have a very good LLM then this framework might not help much as we will have less interaction data to fine-tune model on. The paper lacks evidence that the proposed framework is effective across different LLM architectures. It is possible that the observed improvements are specific to the chosen LLM and may not generalize to models with different capabilities or pre-training data. The authors should investigate the framework's performance on a diverse set of LLMs to establish its robustness.
  - **Across different tasks:** Another interesting extension of the proposed method can be over different tasks. Currently authors have only tested over a particular task but it would be interesting to see if it can be extended over other tasks like summarization (authors have highlighted this as future work in discussion). The evaluation is limited to a single task, MULTIREF, which makes it difficult to assess the framework's general applicability. The authors should explore the framework's performance on other tasks, such as text summarization or question answering, to demonstrate its versatility.
- **Scalability:**
  - **Heavy reliance on human feedback:** The proposed framework relies heavily on human feedback. Although the authors have countered the problem of annotating the responses, the problem of getting good interaction data still remains a crucial problem, making it hard to scale. The framework's reliance on human interaction data limits its scalability. While the authors address the annotation cost, the need for human-in-the-loop interactions remains a bottleneck, especially for large-scale deployments. The authors should explore methods to reduce the dependency on human interaction, such as using synthetic data or self-play techniques.
  - **Cost:** Another issue with scalability is the cost associated with getting quality interaction data. As mentioned by authors, this small experiment took over a month to collect data and costed $11k USD (line 347). This also makes it harder to use the proposed method in real time. The high cost and time associated with data collection make it impractical for real-time applications. The authors should investigate methods to reduce the cost and time required for data collection, such as using more efficient data collection strategies or leveraging existing datasets.

**Minor:**
- Adding information about MULTIREF in the introduction will help in understanding the contribution of the paper.
- Information on LoRA configuration used for fine-tuning is missing.
- Very similar labels are used for control and HH data in figure 4, making it hard to interpret. Maybe changing it with something else will make it more interpretable.
- **Repeated variable:** Authors have repeated the use of variable t. At line 90 it represents time while at line 141 it represents turn and at line 145 it is again used as time.
- **Typo:** Fullstop (.) missing in line 422. "(supervised vs. RL/KTO) Overall" → "(supervised vs. RL/KTO). Overall"

### Questions
1. How do you address overfitting given the extensive reuse of training data at each fine-tuning step?
2. Can you provide comparison of models across different evaluation metrics?
3. Have you tested the framework on other LLMs or tasks to confirm generalizability? How might the framework’s usability vary with stronger LLMs that provides less interaction data?
4. Have you considered other optimization technique like Direct Preference Optimization (DPO) which uses the binary labeled data while fine-tuning the LLM?

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
The paper proposed a method to train a model with implicit human-in-the-loop feedback for a referential game. The proposed method first translate implicit human natural language feedback and quantize them into positive, (neutral), and negative labels, and then use the feedback to fine-tune the language model for decision making. 

The experiment is situated in a referential game, where human is serving as a speaker to describe a subset of tangrams, and the model is serving as the listener to pick out the objects the human was describing.

The paper experimented with three learning methods: supervised learning, REINFORCE, and KTO. The models were initialized with pre-trained IDEFICS2-8B weights and fine-tuned with LoRA. Each model setting was fine-tuned with 0/1/2/3 rounds (B-SUP for 6 rounds), before being deployed in the online setting to have human-bot evaluation. 

The paper observed that supervised learning method with binary quantization provided best performance, and that the feedback decoder's performance is relative stable across rounds and is consistent with human evaluation. The paper also observed that the human language is getting simpler with smaller vocabulary size and reduced utterance length across the rounds.

### Strengths
1. The paper proposed a learning method, RESPECT that utilizes implicit human-in-the-loop feedback for explicit action improvement
2. The paper experimented with 3 learning methods: supervised learning, REINFORCE, and KTO
3. The paper conducted thorough experiments in a multimodal referential game
4. The paper conducted pre-training as well as online testing for iterative model improvement and evaluation
5. The paper is very well structured and well-written. The paper analyzed in detail about learning strategy tradeoffs, feedback label selections, feedback decoder evaluation, and language analysis.

### Weaknesses
 The paper wishes to highlight the contribution on 'continual learning' and model's iterative improvement with human's online feedback, but the actual experiments conducted is slightly misleading. The authors were careful to distinguish the differences between 'round' and 'turn. 

- In the setup, each 'round' includes multiple 'turns' of interactions between a human and the bot. 
- The model is retrained after each 'round', with the history of all previous 'rounds'
- After fine-tuning at the end of each 'round', the model is fixed and deployed for evaluation

The main difference between proposed method versus the classic fine-tuning is the increasing context length during each fine-tuning round. It is unclear what the intended benefit is for the increasing context history?
For example:
- Interaction history could help personalize the message or have a better understanding the counter party's message, if the bot was interacting with the exact same human. It was unclear if the bots were interacting with the same human users across different rounds.
- Interaction history could help the bot understand the task goal, through multiple rounds of probing and try-and-error (like RL), only if the bot was not briefed on what the task goal (referential game) was. According to the experiment setup (Figure 1, 2, 3), the model seems to have prior knowledge of the exact task goal.

Beyond the examples illustrated above, the improved performance demonstrated in the paper might just be a result of fine-tuning with more data, and the expensive online evaluation among different turns showcased model's intermediate checkpoint performance. 

Nevertheless, the paper proposed a new method that turns implicit human feedback into explicit rewards that could help improve model's performance. It is the 'Continual Learning' aspects that lacks sufficient support.

### Questions
Ln 425-426: According to Section 4.2, RL includes both positive and negative rewards. What might be the reasons that including extra rewards would 'encourage a uniform distribution'?

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
- The paper presents RESPECT, a framework for LLMs to learn from implicit user feedback in multi-turn interactions. Rather than relying on external annotations, RESPECT enables models to retrospectively analyze past interactions and learn from cues like rephrased requests, signs of user approval, or frustration.
- This approach is applied in MULTIREF, a new multi-turn reference game where users instruct the model to select abstract shapes (tangrams), and the model gradually improves its accuracy based on decoded feedback signals.
- The study compares three learning strategies: supervised learning, REINFORCE, and KTO, finding that models using only positive feedback perform best.

### Strengths
- The use of continual learning in the RESPECT framework demonstrates strong potential for developing LLMs that improve continuously from real-world interactions.
- The retrospective aspect of RESPECT is particularly compelling, as it enables models to learn from user corrective feedbacks.

### Weaknesses
 - The experiments are confined to the MULTIREF scenario with abstract tangram shapes. This limited scope raises questions about the generalizability of RESPECT to other domains. Applying RESPECT to diverse settings, such as conversational agents could demonstrate its robustness and adaptability across a broader range of applications, particularly those involving complex language or high-stakes interactions.
- There's a risk that the model might overfit to specific patterns of implicit feedback rather than truly improving at the task.
- The paper does not compare RESPECT to other established methods for learning from implicit feedback or continual learning. Without such comparisons, it's difficult to assess the relative merits of this approach For example, methods in RLHF using preference modeling or utility maximization strategies  could serve as useful baselines.
- The feedback decoder relies on the model's ability to interpret implicit signals correctly. However, there's no guarantee that the model's interpretation aligns with the human's intended feedback. The paper would benefit from a more thorough analysis of cases where feedback may be misinterpreted and how this affects learning.
- While the paper shows improvement over six rounds for B-SUP, this may not be sufficient to fully understand long-term learning dynamics. The observed plateau and temporary decrease in performance warrant further investigation. Extended experiments over more rounds could provide insights into whether the approach continues to improve or stabilizes at a certain level.

### Questions
- How well do you expect RESPECT to generalize to other domains or tasks beyond MultiRef? Have you tested it in any other scenarios?
- Have you considered ways to mitigate the impact of feedback misinterpretation on learning?
- Have you considered any potential ethical implications of learning from implicit human feedback, such as privacy concerns?
- The paper mentions that negative feedback signals are generally underutilized due to challenges in integrating them effectively. Would a more nuanced approach to weighting or categorizing negative feedback improve the model’s performance? eg some negative feedback could carry more importance than others. For instance, if the user strongly corrects an action (e.g., "No, that's completely wrong"), this feedback could be weighted more heavily than a milder form of dissatisfaction (e.g., "Not quite right"). Assigning different weights would allow the model to learn more from severe mistakes than minor ones.
- What are the computational costs of implementing RESPECT, especially the retrospective analysis of past interactions?
- In Figure 3, there appears to be a formatting issue or typo. It says "positive or negative positive, neutral, or negative feedback," which seems confusing. Likely, this is unintended and should read either "positive, neutral, or negative feedback" or "positive or negative feedback".

### Soundness
3

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
5

### Summary
In this paper, the authors propose RESPECT, a new method for refining multimodal language models (in this case vision and language models) from interaction data automatically generated by a model while interacting with another agent when solving a referential task. 

To tackle this problem, the authors propose a new benchmark called MultiREF which requires agents to manipulate tangrams, specific abstract shapes that are well-known in the community for their ability to elicit interesting communicative grounding phenomena due to their intrinsic ambiguity.  

Based on this dataset, the authors focus on a very specific training regime which alternates two phases: 1) retrospection = decoding implicit feedback from past interactions by means of a classifier which derives feedback labels (i.e., positive, neutral, negative); 2) learning = refining the model using the feedback received from the previous stage. Because the authors simplify the prediction task to a classification task, they argue that Step 1) can be simply performed by a carefully prompted model to perform a simple binary/three-way classification task. For the second step, the authors test different learning strategies such as a) supervised learning from positive data only; b) Online reinforcement learning (using REINFORCE) with a hand-crafted reward function which leverages the labels derived by the classifier from Step 1. c) Kahneman-Tversky Optimisation (KTO) as a form of reinforcement learning from feedback (in this case, AI feedback).  

The authors set up a really complex evaluation with real users that interact with the system in real-time. In their evaluation, they start from IDEFICS2-8B model as their initialisation and use a frozen IDEFICS2-8B as the feedback decoder. From their evaluation, seems that there is still a long way to go to develop robust training regimes that can facilitate the type of adaptation required for these interactive tasks. In fact, the supervised learning variant seems to be the most robust which relies purely on positive examples and ignores negative ones.

### Strengths
1. Interesting evaluation that tests the system with real users over a period of 4 weeks. This represents a great effort to showcase the strengths and weaknesses of the different training regimes.
2. Very interesting idea to simplify the task of the "critic" to fixed labels that can be used for very specific training regimes
3. The authors test different training regimes that are well known in the community such as Supervised Learning, REINFORCE and KTO

### Weaknesses
1. Although I appreciate the rationale behind using tangrams, I wonder whether the authors could have tested this approach in more realistic reference game that are well-known in the community such as 20Q game [1], GuessWhat?! [2] or Photobook [3]. I feel like this would have given a much broader perspective on the robustness and reliability of the proposed training regimes for more complex language generation tasks

2. It's not clear to me what is the rationale behind using KTO compared to DPO which is more established (e.g., used by Meta for Llama 3.2 tuning). Considering that the authors have access to positive and negative examples, I wonder whether they should try DPO instead considering that has been tested more for VLMs

3. It's not clear to me how the authors complete their fine-tuning considering that most of the training regimes are not designed for dialogue data specifically. See Question 1 as well for details.

4. I think the authors are missing a simpler baseline that is fine-tuned using the final reward (i.e., whether you win or not the game) as a reward as was done in previous work [4]. 

5. The related work cites some interesting work related to using AI-generated feedback for improvement. However, the authors do not provide a baseline where this is explored for this game. For instance, the method proposed by Yuan et al 2024.

### Questions
1. It's not clear to me how the authors complete their fine-tuning considering that most of the training regimes are not designed for dialogue data specifically. For instance, if you have a dialogue of 4 turns, do you simply treat this as a single example or do you derive many examples for it? This is an important detail which I don't think is specified in the section that describes the training regime.

2. What kind of REINFORCE implementation did you use? Did you adopt a baseline term? I think it's important to report more detail to aid reproducibility

3. Considering that the action space of the model is very limited, have you considered a form of token masking to improve the performance of your algorithms?

### Soundness
3

### Presentation
3

### Contribution
4
