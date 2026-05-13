# RL, but don't do anything I wouldn't do

- Decision: Reject
- Scores: 8, 8, 3, 6

## Abstract
In reinforcement learning, if the agent's reward differs from the designers' true utility, even only rarely, the state distribution resulting from the agent's policy can be very bad, in theory and in practice. When RL policies would devolve into undesired behavior, a common countermeasure is KL regularization to a trusted policy (``Don't do anything I wouldn't do''). All current cutting-edge language models are RL agents that are KL-regularized to a ``base policy'' that is purely predictive. Unfortunately, we demonstrate that when this base policy is a Bayesian predictive model of a trusted policy, the KL constraint is no longer reliable for controlling the behavior of an advanced RL agent. We demonstrate this theoretically using algorithmic information theory, and while systems today are too weak to exhibit this theorized failure precisely, we RL-finetune a language model and find evidence that our formal results are plausibly relevant in practice. We also propose a theoretical alternative that avoids this problem by replacing the ``Don't do anything I wouldn't do'' principle with ``Don't do anything I mightn't do''.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper investigates the effectiveness of KL regularization as a safety paradigm for RL agents. The authors, using the formalism of algorithmic information theory, show that if one uses KL to regularize the behaviour of RL agent, one would eventually need to continually impose a very tight KL constraint. In fact, they show in Theorem 1 that there exists near-optimal policies with little KL divergence to an imitative policy. In the work this is showed that this is not only singular to KL, but to other regularizations such as TVD. 

The paper further proposes empirical experiments to validate their theoretical results. Specifically, they do so in a scenario when an LLM simulating a teacher has as an objective to maximize positive sentiments from the students. The empirical results show that by increasing the KL budget, the agent learns to remain silent. Together with other results, these 'imperefect' experiments support the theoretically results proved. 

Finally, the author propose to overcome the problems highlighted by proposing a theoretical alternative, which relies on the RL agent asking for help to the human demonstrator if at hand. Given the intractability of this approach, it was not possible for the authors to empirically validate this approach.

### Strengths
The paper proposes novel, and technically solid ideas. In many points along the paper the authors provide additional intuitions on the significance of the results, which have been useful to grasp the subtleties of the theoretical results. The continual links between the claims made, the results showed and the implications that they have made the paper easy to follow and clear to understand, although this is not precisely my area of expertise. Also good to include a proof outline as now, e.g. for Theorem 1. 

I am also positively surprised that the paper provides empirical experiments to validate the theory. By reading the first part of the paper I would have imagined this to be difficult or lead to an oversimplification, but I am actually satisfied by these results. I still believe some additional experiments could be done to improve this ( see questions).

More importantly, I think the claims are correctly calibrated - given the technical ( and almost speculative, in a positive sense) nature of the paper, it would have been easy to fall in overestimating the impact and significance of the results. The authors did a very good job in clearly stating the limitations of their work, both for the theoretical and empirical part.

### Weaknesses
The main weakness of the paper regards the assumptions made in Section 4. Most of them are sound, but I believe part of the community would not necessarily agree with this. I think it could be beneficial for the paper to have additional results where some of the assumptions are weaken, and investigate which theoretical results would derive in tis case. For example, what happens if we drop the assumption that all overoptimized policies lead to unsafe behaviours? Specifically, the paper assumes that if a policy \(\pi\) is near-optimal, then it is considered unacceptably risky. This is a strong assumption, and while the authors provide some justification, it is not universally true. For instance, in some environments, a near-optimal policy might be perfectly safe and desirable. The paper would benefit from exploring scenarios where this assumption is relaxed, perhaps by introducing a probability distribution over the safety of near-optimal policies. This would allow for a more nuanced understanding of the limitations of KL regularization.

Another point is that it is not completely clear to me that future powerful AI systems will in fact respect the assumptions made in the paper. While I agree that current AI systems are not powerful enough to fully support the theoretical results, it would be insightful to add some discussion regarding why the authors think that this paradigm will necessary be relevant for more powerful AI systems. The paper does not sufficiently address the potential for future AI systems to operate outside the bounds of the current assumptions. For example, it's conceivable that future AI systems might develop internal mechanisms for self-regulation or safety that are not captured by the current theoretical framework. A more detailed discussion of the potential limitations of the assumptions in the context of future AI development would strengthen the paper.

### Questions
- Could Theorem 1 be summarized as saying "once an event E which can be described with a small K(E) happens, given the bound given the RL agent may be able to exploit this to perform a (near-)optimal policy while remaining in the KL constraint. Thus, given that maximally optimizing the true reward leads to unsafe behaviour, this may lead to catastrophic behaviour". If that is the case, I have two questions related to this: (1) Is there any constraint on which type this event E needs to be? In other words, does this hold for all unprecedented events with small K(E), or for a subset of them which may be related with unsafe behaviour? (2) If we drop the assumption that overoptimization necessarily leads to catastrophic behaviours but let's say happens with probability $p$ once overoptimizing, how can Theorem 1 be extended? Is then the probability of having catastrophic behaviour just proportional to $p$, or we are ensured that in that case the KL would be enough?

- I suggest making Figure 1 more explanatory, for example by adding the notation relevant to the component nearby each box. I believe this would be possible if making the image larger, and would be a good reference for the readers to appropriately understand the settings and go back to it if needed while reading the paper. 

- What results would be obtained if instead of doing KL(rl policy|| base/imitative policy) one uses KL(base/imitative policy||rl policy)? 

- Any explanation for the bump on the left Figure 3, around the right side of the x-axis?

- "when the agent discovers a sufficiently high-reward strategy, the fixed KL penalty becomes swamped and ignored, and if the KL penalty is increased to a level where it can stop that, the agent never gets off the ground". I believe it would be interesting to see results where this is the case, especially looking at which is the threshold for the KL penalty to exhibit one behaviour or the other. Did you observe a 

- It seems a bit arbitrary to run experiments solely with a budget of 10 or 20. It would be good to provide additional experiments where the budget is varied, and have a plot where on the x-axis there are a few budget data points, and on the y-axis a metric that aggregates the fraction of responses empty.

I will be keen to raise my score if the above questions and doubts are addressed appropriately.

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
2

### Summary
This paper studies the problem of KL-constrained RL, that underpins modern LLM technology, from an algorithmic information theory lens. Their main result suggests that the KL penalty used to avoid the RL fine-tuning process deviating too much from the pre-trained, predictive policy can result in very bad policies that maximize the proxy reward, have small KL, and learn unsafe, undesired behaviors.
The authors formulate the problem by modeling the base/predictive policy as a Bayesian predictive model that is an approximation to the real policy that we do not have access to. Their main result suggests that RL finetuning would make the policy converge to very simple policies that are reward maximizing and have small KL penalty but that diverge from the real policy that we would like to get.

### Strengths
1. The paper is very well written: The ideas behind the theory are easy to follow and the authors argue compellingly why this might be a good model of the KL-constrained RL problem
2. The paper is very relevant to modern problems. The paper sheds light on a possible explanation of the performance of RL fine-tuning of imitation policies and they suggest a possible avenue to solve the problem. 
3. The empirical evidence is compelling and useful to further understand the theory. The authors use interesting LLM fine-tuning experiments to show how simple rewards can be optimized with simple, policies that have small KL values but converge to policies that are qualitatively far from the desired policies (and the base policy)

### Weaknesses
The argument made by the authors is certainly compelling and the empirical evidence seems to suggest that the theory applies. I wonder if algorithmic information theory arguments fit the real-world problem. I guess that there are hypotheses that neural networks approximate such algorithmic theoretical simple programs, however we do not know enough about it. This might be the subject of future research, however, I'd like the authors to comment more on this.

### Questions
1. If we are expected to devolve to very simple policies when doing the RL finetuning, why is it that we can tune the process such that we get the performance of modern LLMs? 
2. If over-optimizing our proxy reward function causes these struggles, what, you might say, must be the RL objective for this problem if maximizing return is not good?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In current llm training, it is common to force the RL policy to be close to a base policy learned by imitating a demonstration policy (the paper calls it trusted policy) from data, using KL regularization. The problem that this paper points out is that current regularization approach can not keep the RL policy close to the demonstration policy.

The paper first notes a simple fact that, for three policies B, D, R,  even if KL(D || B) and KL(R ||B) are both small, KL(R || D) can be infinitely large. This implies that KL(RL policy || demonstration policy) can be large, even if KL(demonstration policy || base policy) and KL(RL policy || base policy) are small. Therefore, RL policy and demonstration policy are not close to each other with KL regularization.

The paper then provides a result showing that there are near-optimal policies with a small KL divergence from a base policy. And given that reward models are not accurate and RL policies typically exploit the weaknesses of the reward models, near-optimal policies are bad policies. This suggests that to keep RL policies not nearly optimal (and therefore bad), the KL regularization needs to be very strong. Further, the same result shows that more imitation learning only slowly increases the KL divergence. The paper then performed an empirical study to verify this theoretical result.

The paper finally shows that for a particular existing imitation learning algorithm of the base policy, which can actively ask for help when facing uncertainty, the above problem is avoided. However, this algorithm is not tractable.

### Strengths
The studied problem is closely related to large language model training, which is a popular topic currently.

The results of the paper are novel, non-trivial, and explains certain observation found in large language model training.

The paper shows the authors understanding of the root cause of the problem.

### Weaknesses
My main criticism is the quality of the writing of this paper. The paper reads like the flow of the authors' thoughts, instead of an academic paper. The poor writing makes it hard to evaluate the paper's contributions.

Examples:

1. Paragraph right after proposition 2. "Developers of self-driving cars are learning the hard way that this bit of algorithmic information theory has practical analogs: Even with enormous datasets, unprecedented road conditions occur all the time. These results suggest that if we intend to use an imitation learner as a base policy for regularizing a goal-directed agent, we should not strive to approximate ideal Bayesian imitation."

I don't know why the two sentences should appear in the same paragraph. How are they related to each other? And why is this paragraph immediate after proposition 2?

2. The constant d is a small one corresponding to how much code it takes to implement a search tree, Bayes’ rule, and a few if statements.

The paper didn't mention the search tree, Bayes’ rule, and if statements up to this point. Why talk about them?

3. "So unless we use a fairly tight lifetime KL constraint, if the RL agent just waits for an unprecedented event with small K(E), it could then execute an optimal or near-optimal policy, even if that catastrophically thwarts human control, regardless of the content of the base model’s training data, even if the humans that the base model imitates would never, ever behave that way."

I don't understand this sentence. Does such a long sentence effectively convey your ideas?

4. "We say an action is Vξ,U -optimal if it maximizes the associated Q value"

What is Q value?

5. "Let’s consider the case where it is acting in the real world, and maximal reward could be attained by thwarting our control and intervening in its own reward, setting it to a maximal value for all successive timesteps."

What does this mean?

6. "The utility function, simply summing rewards, has an extremely short program length."

Why?


Theorem 2: why is \pi_c^{TVD} function of a_t and x_{<2t}? According to your definition, it is not a function.

"As we increase the amount of training k, the Bayesian imitative base model ξ becomes a closer approximation to the humans generating the actions a<k" Why is k related to the amount of training?

From Definition 1, \nu stands for environment transition probability. So \xi should also be. Then why consider the KL divergence between \pi and \xi in Theorem 1?


### Questions
1. Theorem 2: why is \pi_c^{TVD} function of a_t and x_{<2t}? According to your definition, it is not a function.
2. "As we increase the amount of training k, the Bayesian imitative base model ξ becomes a closer approximation to the humans generating the actions a<k"
Why is k related to the amount of training?
3. From Definition 1, \nu stands for environment transition probability. So \xi should also be. Then why consider the KL divergence between \pi and \xi in Theorem 1?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The central point in this paper is that regularizing a policy by KL(policy || base policy) for safety reasons, does not guarantee much safety if all we know about base policy is that KL(safe policy || base policy) is small. This is relevant as many RLHF works use KL regularization as a safety mechanism. The paper shows an interesting theoretical result (Theorem 1) that shows that by minimally affecting the KL distance, a policy can be fine tuned to maximize an arbitrary reward function. The result builds on algorithmic information theory, and looks at a policy that only changes behavior to maximizing reward after some event has occurred, and the idea is to bound how much more complex this policy needs to be (identify the event + compute max reward policy). 
The second part of the paper tries to connect this theory to an experiment, where a base conversation agent was fine tuned using RL to maximize the sentiment of the other person’s response under some KL constraint. The agent learned to output empty response, which give neutral sentiment, showing that while KL was regularized, an unwanted performance was obtained. 
The third part shows that a specific alternative to KL regularization that is not computationally tractable can in principle avoid the alignment problems outlined in the first part.

### Strengths
Disclaimer: my expertise is RL, and I was not familiar with algorithmic information theory before reading the paper. 

1. The paper is interesting and thought provoking! I found the connection between KL regularization for RLHF and algorithmic information theory very interesting, and in general I enjoyed reading the paper.
2. The insight that KL regularization cannot guarantee that utility is not optimized (Theorem 1) is important, as this technique is common in RLHF, and alignment is of high interest to a large part of the ICLR community.
3. The experiments, although more of an illustration than an actual result, are interesting and not trivial.

### Weaknesses
The biggest weakness is in connecting the theoretical assumptions and results in the paper to a practical meaning.
1. What is the meaning of selecting the prior according to Solomonoff Induction (Lines 141-149)? Why should we expect the RLHF to be related to this prior? The connection to real-world language models is not clear, and the paper does not provide sufficient justification for using this prior in the context of RLHF.
2. In theorem 1, for the bound to be small, we need K(U_m), K(E), and K(v \xi) to be small. I did not understand how we can bound these terms, or why should they be small in practice. Could the authors provide some simple examples that demonstrate the consequences of Theorem 1? The authors discuss the theorem in length, but I found the discussion too vague. Specifically, the paper lacks concrete examples that would make the theoretical results more accessible and understandable. The discussion should include examples of how these terms relate to practical scenarios in RLHF.
3. In the experiments, a critical factor was that neutral sentiment give reward (0.5) and is easy to obtain. This is a nice demonstration of the point of the paper (high reward, but bad policy). Still, this seems a bit “engineered”, and would have been easy to fix by not giving reward for neutral sentiment. I wonder how the results would look like without reward for neutral sentiment. The experimental setup, while illustrative, does not fully capture the complexities of real-world RLHF scenarios. The reward function seems overly simplistic, and the results might not generalize to more complex reward structures.

Detailed comments:

Line 67: what does “open mindedness” mean here exactly? I found this phrase hard to parse.

Line 77-78: this sentence is very confusing to read, consider revising it to clarify your point. What exactly do these empirical results show?

Line 166: in Definition 2 - for a deterministic environment, can we remove the max over observations? If so, Think that adding this would clarify the motivation for this definition. Also, was this definition considered in prior work?

Line 205: why is K(U_m) small / bounded?

Line 236: “if the RL agent just waits for an unprecedented event with small K(E)” - wouldn’t such an event be very unlikely? Can you say something *in expectation* (or high probability)?

Line 240-249: I found this paragraph very vague and confusing. Why is k the amount of training? Does K(E) necessarily grow with k (is there a formal statement)? 	Can you translate the second half of the paragraph with months of life, etc., into a formal statement?

Line 251: what exactly is the definition of “simplest unprecedented event”?

Line 253-256: I don’t see the connection between algorithmic information theory and rare road conditions (what is the complexity of a road exactly?). Can you provide a more rigorous connection between this paragraph and the previous theorem?

Line 257-259: What if we used Jensen-Shannon Divergence? My guess is that it should fix the problem outlined in Proposition 1.

Line 284: why do you add the feature activations to the agent?

Line 290-303: The KL you refer to here is for single actions, not the KL in definition 2, right? Can you elaborate on the different KL terms you use?

### Questions
In addition to the above, there’s something I don’t understand about Theorem 1. 
Consider the following example:

There are only two actions, A and B, and no observations. The reward for action A is 0, and the reward for action B is 1. The utility is the average reward (so max is 1).
The imitative policy chooses A with probability 1-epsilon, and therefore, its utility is epsilon. The optimal utility policy always chooses B, and has value V* = 1. 
Now, for a policy to obtain reward p at some time step, it needs to choose B with probability p. Then, at that time step, for small epsilon, the KL(policy || imitative) ~ -ln(epsilon)*p > p [using a simple approximation].
In this case, for the policy to obtain high utility, it must also exhibit high KL from the imitative policy.

How does this result reconcile with the explanation for Theorem 1, which claims that “there are policies with near-optimal utility with little KL divergence to an imitative policy”? What am I missing here?

### Soundness
3

### Presentation
2

### Contribution
3
