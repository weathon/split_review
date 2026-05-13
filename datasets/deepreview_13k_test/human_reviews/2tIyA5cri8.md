# Sparse Autoencoders Reveal Temporal Difference Learning in Large Language Models

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
In-context learning, the ability to adapt based on a few examples in the input prompt, is a ubiquitous feature of large language models (LLMs). However, as LLMs' in-context learning abilities continue to improve, understanding this phenomenon mechanistically becomes increasingly important. In particular, it is not well-understood how LLMs learn to solve specific classes of problems, such as reinforcement learning (RL) problems, in-context. Through three different tasks, we first show that Llama $3$ $70$B can solve simple RL problems in-context. We then analyze the residual stream of Llama using Sparse Autoencoders (SAEs) and find representations that closely match temporal difference (TD) errors. Notably, these representations emerge despite the model only being trained to predict the next token. We verify that these representations are indeed causally involved in the computation of TD errors and $Q$-values by performing carefully designed interventions on them. Taken together, our work establishes a methodology for studying and manipulating in-context learning with SAEs, paving the way for a more mechanistic understanding.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates whether Llama 3 70B has internal representations that support temporal difference learning. First, it demonstrates that Llama can solve RL tasks significantly better than chance. Next, it trains a sparse autoencoder (SAE) and finds features correlated with TD error. Finally, it causally intervenes on these features to show that in-context RL performance degrades without those specific TD features.

### Strengths
This is an excellent paper. It asks a very interesting question and provides compelling evidence for the conclusion that Llama represents TD error and uses it to solve RL problems in-context. The section on successor representations was a welcome surprise in section 5, and offered more evidence for TD learning, even absent any rewards. The paper was also quite easy to follow and laid out the argument in a very natural way. I don't have any major complaints.

### Weaknesses
Only minor weaknesses.

1. In the background section on RL, TD is presented for a fixed policy, and then the paper switches to Q-learning, assuming the policy chooses \argmax_a Q(s,a). But this will change the policy as the Q function is updated, so it's not technically the same setting.
2. It was a bit unclear what "control lesion" referred to in Fig. 2F. And more generally, I was not familiar with the "lesion" terminology, so a brief definition would be welcome. I assume it's a form of activation patching?
3. I would have liked slightly more explanation regarding "clamping" the activations. I assume this means setting them to a specific value, but how is that different from deactivating them (i.e. clamping them to zero)? Is the purpose of clamping the activations to show degraded, unchanged, or improved performance?
4. Line 458, mangled sentence "our study is, we have explored".

### Questions
Could you please provide clarification re: weaknesses 2 & 3?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a mechanistic analysis of internal activations of the Llama 3 70b model during three different in-context reinforcement learning tasks. In particular, the authors use Sparse Auto-Encoders (SAEs) to generate latent space representations of the residual streams and show how they correlate with TD Errors and Q-values of Q-learning agents trained to solve the same tasks. Furthermore, they show that relationship between the latent representations and the TD Errors is causal by intervening on the latent representations, which causes a degrading in the performance of the model.

### Strengths
I think the paper is well written and the setting and the experimental details are generally well explained. The contributions are also clearly stated. Furthermore, as far as I can tell, the presented experimental methodology is also sound. Although it is a known fact that Transformers can potentially perform In-Context RL, especially if trained for it, it is the first time, to the best of my knowledge, that a mechanistic analysis is conducted on a model which was pre-trained on next token prediction. In addition, even if the methods used (e.g. SAEs) are already well established in the mechanistic interpretability literature, it is insightful to see how they can be successfully used also to better understand how LLMs solve In-Context RL. Hence, even if the problem of In-Context RL is well studied in the literature and the interpretability methods used are also well established, overall I think the presented results shed more light on the inner workings of how LLMs can solve RL tasks in-context, which can be significant and insightful for the community.

### Weaknesses
- The main weakness of the paper is that being an experimental work, I find the number of experiments conducted to be a bit limited. I think that more experiments should be conducted to further support the contributions of the paper (I saw that the authors mention this in future works/limitations, but I think the current paper would benefit from more ablation to make the evidence stronger). In particular, I suggest that the authors (as they also mention) should try to repeat the experiments they present with different models (at least one more) to prove that their results hold in general for "big enough" models. This would be really insightful since it would tell us that different models, even if trained differently, learn similar representations or make use of similar strategies to solve tasks. Furthermore, I think it would be insightful to conduct experiments on larger environments to better understand both to what extent these models are capable of performing In-Context RL and to analyze if, even at larger scale, these models still make use of TD Erros and Q-Values to solve the task
- One minor concern regards the extent of the novelty of the work: as I mentioned above, although I agree with the authors that it is the first time (to the best of my knowledge) that it was shown that models trained on next-token prediction perform In-Context RL exploiting TD Errors, there are already quite some works exploring TD Learning in Transformers (both at a theoretical and experimental level). Furthermore, the methodology used for the mechanistic analysis is also already well established in the mechanistic interpretability literature.

### Questions
Some small additional comments and questions I had:
- In the definition of the Q function in Section 2 (Methods, at page 2), shouldn't there be a conditioning on the initial state and action inside the expectation? Also, shouldn't the sum start from $t=0$ instead of $t=1$?
- In Section 3, you claim that Llama 3 most likely implements "classic" Q-Learning rather than myopic Q-learning based on the negative log-likelihood. However, in Figure 2, looking at the correlations, it seems that the myopic Q-learning has in general comparable if not higher correlations to the latent representations. Couldn't this suggest that the model is implementing the myopic algorithm instead? Furthermore, is the difference in negative log-likelihood statistically significant?
- In Figure 5, what do the horizontal lines in subplots B & C represent?

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
1

### Summary
This paper is way out of my expertise and hence I cannot provide a meaningful review.

### Strengths
.

### Weaknesses
.

### Questions
.

### Soundness
2

### Presentation
2

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
The paper looks for evidence of whether Llama3-70B model can simulate the TD-learning algorithm for solving RL tasks. The authors evaluate this using simple toy RL environments. They train different SAEs for the different tasks and find features that correlate highly with TD-errors and Q-values. They confirm that these features are causal in predicting actions by performing interventions on such features. Based on these evidence, the authors conclude that the LLM is simulating the TD-learning algorithm.

### Strengths
1. The study evaluates their hypothesis through a series of tasks to substantiate their empirical claims.
2. Intervention experiment with the features to confirm their causal roles.
3. The writing is clear and easy to understand. However, some details are missing. See in questions.

### Weaknesses
My main objection with the paper is that there is a simpler alternative hypothesis that could equally explain all of the results. Given the simplicity of the task, the LLM could be implementing the following algorithm to solve the tasks:


Step 1: Keep a track of the maximum points for each episode in the context.

Step 2: Predict the actions from the episode that has the maximum points.


This algorithm is simple to implement for the LLM given previous works on LLMs implementing greater than circuit [1] and induction heads [2]. Also, for the Two-Step Task, the first 7 episodes are provided by using a random policy, which should cover all the 4 different trajectories possible in the task.

The features that the authors find using SAEs could be features that are tracking the maximum points across episodes. These features will have high correlation with Q-values, and are also causal so interventions on them should show similar results as shown in the paper.

I recommend that the authors conduct experiments designed to refute this hypothesis. See questions for some suggestions on experiments that can be performed.

References:

[1] How does GPT-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model. https://arxiv.org/abs/2305.00586

[2] In-context Learning and Induction Heads. https://arxiv.org/abs/2209.11895

### Questions
1. In the plots on max correlation with values/errors (eg fig 2c, 2d, 3, 4b, 4c, etc.), is the correlation computed with the value/error of the action predicted by the LLM at the given state? If yes, then it would be valuable to check whether there are features that correlate with value/error of non-optimal actions. This could help in distinguishing whether the LLM is actually implementing TD-learning or the max-point episode algorithm provided above.
2. Can you provide how the NLL score computed? I couldn't find it in the appendix either. Particularly, are you computing the log probabilities of Q-learning agent by doing a softmax using the Q-values over actions?
3. Are you using any discount rate for the Grid World Task? If yes, please provide it.

### Soundness
2

### Presentation
4

### Contribution
3
