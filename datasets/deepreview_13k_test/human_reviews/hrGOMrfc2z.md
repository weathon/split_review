# Interactive Dialogue Agents via Reinforcement Learning with Hindsight Regenerations

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Recent progress on large language models (LLMs) has enabled dialogue agents to generate highly naturalistic and plausible text. However, current LLM language generation focuses on responding accurately to questions and requests with a single effective response.
In reality, many real dialogues are \emph{interactive}, meaning an agent's utterances will influence their conversational partner, elicit information, or change their opinion.
Accounting for how an agent can effectively steer a conversation is a crucial ability in many dialogue tasks, from healthcare to preference elicitation. Existing methods for fine-tuning dialogue agents to accomplish such tasks would rely on curating some amount of expert data.
However, doing so often requires understanding the underlying cognitive processes of the conversational partner, which is a skill neither humans nor LLMs trained on human data can reliably do.
Our key insight is that while LLMs may not be adept at identifying effective strategies for steering conversations \emph{a priori}, or in the middle of an ongoing conversation, they can do so \emph{post-hoc}, or in \emph{hindsight}, after seeing how their conversational partner responds. We use this fact to rewrite and augment existing suboptimal data,
and train via offline reinforcement learning (RL) an agent that outperforms both prompting and learning from unaltered human demonstrations. We apply our approach to two domains that require understanding human mental state, intelligent interaction, and persuasion: mental health support, and soliciting charitable donations.
Our results in a user study with real humans show that our approach greatly outperforms existing state-of-the-art dialogue agents.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper looks at training an LLM to play the role of a conversational agent, particularly in situations which require some manipulation for lack of a better term of the user towards a goal, for example making a donation to charity. 

The paper's main idea is that rather than looking at conventional RL based exploration guided only by a numeric reward function, to look at generated dialogs in full and to with "hindsight" identify turns where the dialog may be judged as having been suboptimal and steered the user away rather than towards the desired goal. Such data can then be regenerated from that sub-optimal turn forwards. This is done and that data is then used in an offline RL algorithm to update the LLM playing the role of the system. 

The paper compares to some prior works and reports results on 2 datasets.

### Strengths
The observation that feedback is more precise at the level of dialog regenerations having seen a full "rollout" is valid, given reward based feedback alone is a more difficult search space to optimise. 

The paper is clear in its motivations, compares against other published works and reports reasonable results based on an evaluation with different users.

### Weaknesses
One minor suggestion: it's claimed that the results in table 1 are statistically significant (line 453) however there's no detail given for how this was determined. This should be included.

### Questions
* Would doing RLHF/DPO on the bad versus better turn be a valid comparison to include here? By "bad" I mean the turn first identified as being sub-optimal in the hindsight stage, and by "good" I mean it's regenerated version. Unclear how similar this is to the offline ILQL algorithm which I admit to not looking up now. 

* what happens if you do multiple rounds of hindsight re-generation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method for enhancing dialogue systems using pre-trained language models (LLMs) through hindsight reinforcement learning (RL).
It utilizes LLMs to simulate human responses and generate new dialogue samples, which are then used to improve or supplement the original dataset, addressing the problem of lacking effective strategies in dialogue systems. The authors conducted experiments on two challenging tasks and demonstrated the effectiveness of this method. Additionally, they showed how to adjust dialogue strategies based on user feedback to achieve more natural and effective conversational interactions.

### Strengths
1. The article proposes a data augmentation method to improve the performance of dialogue agents.

2. It significantly outperforms existing fine-tuning methods in terms of efficiency, naturalness, and usefulness.

### Weaknesses
1. The article's innovation is limited.

2. The introduction of the article's methodology is not sufficiently clear.

3. Table 1 is too long.

4. The experimental analysis is insufficient.

5. There is a lack of objective evaluation metrics.

### Questions
NA.

### Soundness
2

### Presentation
2

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
The paper explores training dialogue agents that use reinforcement learning (RL) to improve their interactive capabilities, especially in complex tasks like mental health support and charitable persuasion. Unlike standard models focused on one-off responses, the authors propose a method called hindsight regeneration. This approach involves augmenting existing dialogue datasets by having the model review conversations in hindsight, identifying optimal actions post-interaction, and suggesting better responses to refine the dataset. The method employs offline RL, avoiding costly real-time exploration, and allows agents to generate more effective strategies over multiple dialogue turns.

### Strengths
By refining conversations after they occur, the model can learn from suboptimal dialogues and incorporate more effective conversational strategies. This approach allows for the development of more adaptive and goal-directed dialogue agents capable of managing complex, multi-turn interactions.

### Weaknesses
The main contribution of this paper seems to be only a dataset construction method, without any innovations in model or methodology. Since this is not a dataset track paper, the authors appear to be primarily reporting experimental results rather than providing a substantial contribution. If the authors can convince me otherwise, I would be willing to adjust my score.

### Questions
1. Although the author believes that BLEU and ROUGE metrics may not fully capture the model’s performance in dialogue, including these metrics could strengthen the experimental results.

2. It seems the author did not specify the datasets used for SFT and RL training.

3. The author introduces a human evaluation conducted by a group of 15 users. Could the author provide details on these users’ backgrounds, educational levels, and native languages? Additionally, was any consistency check performed on the scores given by these 15 individuals?

4. The author’s experiments use only LLaMA-7B as the base model. To demonstrate the generalizability of the approach, has the author considered adding other base models? For reference, here are a few that could be selectively added: LLaMA2-7B, LLaMA2-13B, LLaMA3-8B, Vicuna, WizardLLM, ChatGLM, MiniCPM, Qwen.

5. In Section 5, the author states, “Note that we train on a much smaller model than used in the prompting baselines, yet as we will show later, we still are able to outperform such more sophisticated LLMs.” Given that the model size for ChatGPT-3.5 has never been disclosed and the model itself has gone through several iterations, this statement may risk overclaiming.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce a method to augment existing datasets with hindsight regenerations. This method uses three components (i.e., hindsight controller, forward model and reward model) and four steps (Section 4 and Figure 2 provide a good overview of the method), in short the hindsight controller proposes alternative actions (using the full dialogue), a forward model simulates completed dialogues, the reward model evaluates dialogues and the generate dialogues (plus the original once) are used as trajectories in an offline reinforcement learning to learn the final policy.

The authors compare the trained model with advanced CoT baselines, and three method and data ablations. The human evaluation results  shows improvements in two domains such Mental health support and Soliciting charitable donations

### Strengths
Originality
- the proposed hindsight methods is original (to the best of my knowledge) and provide an effective way to train RL based dialogue systems. 

Clarity
- the overall paper is clear and easy to follow. I would have preferred more detail on the RL methodology, especially in section 4.3 ( Policy Optimization), where the authors provided a compacted explanation for a well known concept in RL but less well-known when applied to LLMs.

### Weaknesses
Significance & Quality 
- The human evaluation lacks of rigor and details. The paper does not provide enough details on how these 15 users has been instructed nor from what demographic comes from (e.g., english proficiency, etc). This is important to evaluate the significance of the results. 
- The results provide in Table 1 shows high variance, and no t-test or annotator inter-agreement is provided. Also the fact that a GPT-3 based prompting (ProCoT) has lower fluency is strange, usually LLM gets high human evaluation number.  Nevertheless this might be an artifact of a small annotator pool.
- Although not super accurate, the authors did not provide any automatic evaluation, this would have provided, even if minimal, a hook to compare different models.

### Questions
- How are the annotators instructed and trained for the task?
- What is the statistical significance of the results in Table 1?

### Soundness
2

### Presentation
4

### Contribution
2
