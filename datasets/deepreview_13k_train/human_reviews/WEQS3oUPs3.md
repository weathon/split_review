# Zero-Shot Goal-Directed Dialogue via RL on Imagined Conversations

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Large language models (LLMs) have emerged as powerful and general solutions to many natural language tasks. However, many of the most important applications of language generation are interactive, where an agent has to talk to a person to reach a desired outcome.
For example, a teacher might try to understand their student's current comprehension level to tailor their instruction accordingly, and a travel agent might ask questions of their customer to understand their preferences in order to recommend activities they might enjoy.
LLMs trained with supervised fine-tuning or ``single-step'' RL, as with standard RLHF, might struggle which tasks that require such goal-directed behavior, since they are not trained to optimize for overall conversational outcomes after multiple turns of interaction. In this work, we explore a new method for adapting LLMs with RL for such \emph{goal-directed dialogue}. 
Our key insight is that, though LLMs might not effectively solve goal-directed dialogue tasks out of the box, they can provide useful data for solving such tasks by simulating suboptimal but human-like behaviors. Given a textual description of a goal-directed dialogue task, we leverage LLMs to sample diverse synthetic rollouts of hypothetical in-domain human-human interactions. Our algorithm then utilizes this dataset with \emph{offline reinforcement learning} to train an interactive conversational agent that can optimize goal-directed objectives over multiple turns. In effect, the LLM produces examples of possible interactions, and RL then processes these examples to learn to perform more optimal interactions. Empirically, we show that our proposed approach achieves state-of-the-art performance in various goal-directed dialogue tasks that include teaching and preference elicitation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper utilizes LLM to simulate sub-optimal but human-like behavior to produce examples of possible interactions. The algorithm uses the data and offline reinforcement learning to train an interactive conversational agent to learn to perform more optimal interactions. Experiments show that the method achieves the most advanced performance in a variety of goal-oriented conversation tasks.
What contributions does it make: 
1.The paper propose a zero-shot RL algorithm that effectively optimizes for goal-directed dialogue tasks.
2.The idea of imagination engine (IE) that generates a dataset of diverse, task-relevant, and instructive dialogues makes sense.

### Strengths
1.The experimental analysis is detailed and methodical, and the case is clear and intuitive.
2.The idea of using LLM to imitate human behavior is interesting.

### Weaknesses
1.Even thought RL can combine parts of behavious seen form behavior policies in the data, it is not convincing that the RL can take all the long-term planing responsibility in the goal-oriented conversation tasks. 
2.The novelty of this paper is limited. The proposed method can be regarded as a pipeline of LLM generation and offline RL training.  
3.All the evaluation methods are human evaluation, which are highly subjective. 
4.More relevant works should be compared in the experiments.

### Questions
Need more details about the evaluators in the experiments, such as their education background.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study presents a reinforcement learning (RL) approach for training goal-directed dialogue agents on synthetic dialogues produced by large language models (LLMs). Known as the "imagination engine," this method generates training data from simulated talks instead of large-scale human-generated datasets. This technique yields agents who perform better on goal-oriented activities than typical LLMs, indicating a new direction for conversational AI development—one that can comprehend and accomplish difficult tasks with little to no human oversight.

### Strengths
1. It shifts the use of LLMs from direct interaction to data generation for optimization by introducing a zero-shot RL algorithm with a "imagination engine" that creatively creates synthetic conversation datasets for training dialogue agents.

2. Compared to traditional approaches, the method optimizes for goal-directed dialogues more effectively since it trains agents on a variety of human-like talks generated by LLMs that are customized for particular dialogue objectives.

3. The usefulness and efficiency of this approach are demonstrated empirically, as agents trained with it outperform state-of-the-art LLMs in interactive tasks.

### Weaknesses
A shortcoming of the work is its somewhat dependent use of human-generated prompts, suggesting opportunities for further development in automating zero-shot dialogue agents' training to work without task-specific human input.

### Questions
What are the detailed version specifications and hyper-parameter configurations of GPT-3.5 used in the imagination engine, and how do these parameters affect the generated dialogue quality and diversity?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper argues that LLMs trained with SFT or single-step RL might struggle with tasks that require goal-directed behavior. The authors propose a method to use LLMs to generate useful data for solving such tasks by simulating human-like behaviors. The data are used to train a conversational agent for goal-directed tasks with offline RL, in order to improve over the trained conversations. Their results show that the approach achieves better performance than directly prompting LLMs or training the agents with behaviour cloning, in various goal-directed dialogue tasks. However, there are concerns about how the human annotator evaluates the conversations and why the authors did not choose widely-used task-oriented dialogue benchmark datasets like multiwoz and schema-guided-dialogues (SGD).
In addition, although the results show that the learned agents are better than LLMs in information-seeking and generating less overwhelming responses in some specific tasks or domains, I wonder if the smaller agents are able to handle other domains, where the small agents might not have knowledge. Is it still a good alternative to LLMs in this case? Is it still useful?

### Strengths
This paper introduces an approach to generate goal-directed conversations with LLMs and then train a smaller agent to improve over these conversations. The human evaluation results show that the learning agents do generate responses that are more helpful in helping the users complete the tasks and generate less overwhelming responses.

### Weaknesses
1. Why not utilize the widely used task-oriented dialogue benchmarks, MultiWOZ and SGD? There are works that leverage LLMs for task-oriented dialogue by training a small model to generate dialogue actions (plans) with RL, guiding LLMs for improved responses [1]. Have you considered comparing with them?
2. From the examples comparing GPT-agent and IE+RL agents, GPT's responses didn't seem significantly inferior. How were the responses scored by the evaluators using the four criteria? Was there consensus in their annotations, and what was the level of agreement?
3. LLMs often produce overwhelming responses, but their strength lies in their capability to converse on a wide range of topics due to their inherent knowledge. While training a smaller model for better goal-oriented conversations for some specific domains and topics might seem more beneficial than directly using LLMs, is such a model able to handle out-of-domain tasks and topics? How does it perform when discussing topics outside its training data? If it can not handle out-of-domain topics, is such a model still practical and useful for real-world applications?
4. I feel that the paper complicates the data generation section by unnecessarily introducing numerous reinforcement learning concepts. Why introduce these concepts when it appear to be a simple data generation process, making it challenging to comprehend?

### Questions
See the weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
