# Plug-and-Play Policy Planner for Large Language Model Powered Dialogue Agents

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
Proactive dialogues serve as a practical yet challenging dialogue problem in the era of large language models (LLMs), where the dialogue policy planning is the key to improving the proactivity of LLMs. 
Most existing studies enable the dialogue policy planning of LLMs using various prompting schemes or iteratively enhance this capability in handling the given case with verbal AI feedback. However, these approaches are either bounded by the policy planning capability of the frozen LLMs or hard to be transferred to new cases. 
In this work, we introduce a new dialogue policy planning paradigm to strategize LLMs for proactive dialogue problems with a tunable language model plug-in as a plug-and-play dialogue policy planner, named PPDPP. 
Specifically, we develop a novel training framework to facilitate supervised fine-tuning over available human-annotated data as well as reinforcement learning from goal-oriented AI feedback with dynamic interaction data collected by the LLM-based self-play simulation. 
In this manner, the LLM-powered dialogue agent can not only be generalized to different cases after the training, but also be applicable to different applications by just substituting the learned plug-in. 
In addition, we propose to evaluate the policy planning capability of dialogue systems under the interactive setting. 
Experimental results demonstrate that PPDPP consistently and substantially outperforms existing approaches on three different proactive dialogue applications, including negotiation, emotional support, and tutoring dialogues.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the transfer ability of proactive dialogues in the context of large language models (LLMs), the existing policy learning is hard to transfer to new cases. This work introduces a new paradigm for strategizing LLM-powered dialogue agents with a plug-and-play dialogue policy planner, called PPDPP. In addition, it also proposes an interactive setting for the policy evaluation. Empirical experiments on three datasets show promising results in both automatic evaluation and human evaluation.

### Strengths
1. This paper introduces a plug-and-play dialogue policy planner with LLMs for proactive learning.
2. Empirical results on three datasets show very promising results in both automatic evaluation and human evaluation, and good transfer ability.

### Weaknesses
So far No. (A good work with sufficient experiments)

### Questions
1. I try to understand why there is negative relative success rate in Figure 2?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents the Plug-and-Play Dialogue Policy Planner (PPDPP), an approach designed to address the challenges of proactive dialogues within the context of large language models (LLMs). PPDPP serves as a dialogue policy planner, employing supervised fine-tuning and reinforcement learning to enable a LLM powered dialogue system to adapt to a variety of dialogue scenarios. Authors introduce a tunable language model plug-in, allowing LLM-powered dialogue system to adapt to various cases and applications by simply substituting the learned plug-in. PPDPP outperforms existing LLM-based dialogue systems in negotiation, emotional support, and tutoring dialogues, showcasing its effectiveness in improving proactive dialogues.

### Strengths
- Utilizes a pluggable and fine-tuned dialog policy ranker for dynamic prompt selection, enhancing adaptability to various dialogue domains.
- Incorporates the LLM as a reward function, enabling RL-based dialogue policy planning.
- Employs a combination of supervised fine-tuning and online reinforcement learning (RL) for dialog policy ranker training.

### Weaknesses
 - Limited action/prompt space for the dialog LLM, potentially constraining adaptability to different domains.
- The primary distinction from other Reinforcement Learning from AI Feedback (RLAIF) works seems to be the mapping of the LLM's reward output from text space to scalar reward space, raising questions about the approach's uniqueness.
- The need for training different dialog policies for each dialog domain. This makes this system less generalizable.

### Questions
1. How is the reward LLM utilized during inference at each turn of dialogue?
2. Could you clarify the process of mapping the reward LLM's output to scalar values and its integration into the PPDPP during each dialogue turn?
3. Can you elaborate more on supervised fine-tuning used to PPDPP?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed to leverage LLM for goal-oriented dialogues. The motivation is that the current LLM are trained to passively follow instruction, and goal-oriented dialogues requires LLM to actively drive the conversation.
The authors proposed a plug-and-play dialogue policy planner. At each turn, this planner proposes a pre-defined action, and that action is translated into a template-based natural language instruction. Finally, LLM conditions on the instruction and dialogue history to generate the next response.
During training, two LLMs are used to generate self-play dialogues and the third LLM is used to score the dialogues. RL is used to then optimize the planner.

### Strengths
The authors proposed a reasonable way to integrate dialogue action prediction into the LLM, which can then optimized by RL. All the components (and even the reward models) are LLM pre-trained so it does not need annotations (except for SFT stage). Experiment results show good performance compared with baseline.

### Weaknesses
The proposed plug-and-play dialogue policy planner is a little bit hacky. PPDPP is separated from the dialogue LLM, and the actions it produces are mapped to pre-defined natural language instructions. PPDPP is essentially a prompt selector. It would be more interesting if it can not only select but also generate prompts, and if PPDPP can be integrated into the dialogue LLM (to avoid to use another pre-trained roBERTa model).

### Questions
Why do we want to sample the goal-oriented AI feedback for l times? (Equation 6). Do we observe large variance of the reward LLM?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
