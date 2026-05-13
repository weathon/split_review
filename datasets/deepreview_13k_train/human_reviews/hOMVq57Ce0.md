# Piecewise Linear Parametrization of Policies: Towards Interpretable Deep Reinforcement Learning

- Decision: Accept
- Scores: 3, 6, 8, 6

## Abstract
Learning inherently interpretable policies is a central challenge in the path to developing autonomous agents that humans can trust. Linear policies can justify their decisions while interacting in a dynamic environment, but their reduced expressivity prevents them from solving hard tasks. Instead, we argue for the use of piecewise-linear policies. We carefully study to what extent they can retain the interpretable properties of linear policies while reaching competitive performance with neural baselines. In particular, we propose the HyperCombinator (HC), a piecewise-linear neural architecture expressing a policy with a controllably small number of sub-policies. Each sub-policy is linear with respect to interpretable features, shedding light on the decision process of the agent without requiring an additional explanation model. We evaluate HC policies in control and navigation experiments, visualize the improved interpretability of the agent and highlight its trade-off with performance. Moreover, we validate that the restricted model class that the HyperCombinator belongs to is compatible with the algorithmic constraints of various reinforcement learning algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a framework for interpretable reinforcement learning that attempts to balance interpretability, performance, and computational complexity. They propose learning a set of piecewise linear policies, which have the benefit of interpretability of linear models. They ensure that the number of piecewise linear policies is not too large which would inhibit practical interpretability. They present the empirical performance of their framework, HyperCombinator, in control and navigation tasks.

### Strengths
- The communication in the paper is clear. The authors clearly describe the desiderata for the ideal interpretable RL methods, and are clear about how their proposed approach seeks to address these points.
- The authors' commitment to maintaining linear policies at some level is good, as these will always be very interpretable on their own.
- The authors provide nice visualizations of their approach and their empirical results.

### Weaknesses
 - The contribution level is low in this paper. Pasting together a set of linear policies does not seem that differentiated from prior work.
- It's not clear practically how interpretable the resulting model is. I suppose the user is supposed to inspect the linear model coefficients to understand what the policy is doing. However, there is not much discussion of this. For example, how should I interpret the coefficient heatmap in Figure 3?
- As it stands, it seems the approach is less of a compromise between interpretability and performance and more of a deterioration of performance while only gaining a little bit of interpretability.

### Questions
How complex of environments can the HC framework handle without fully losing performance?

### Soundness
2 fair

### Presentation
3 good

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
The paper proposes to make Deep RL more interpretable by training a policy which is a piecewise linear parameterization of policies. It is supposed to solve most of the set of constraints an interpretable policy should satisfy (Section 3). The method works by using a Gumbel Softmax to select the different linear polices and then interpreting predictions based on the linear models. Some experiments show the  ability of their model to converge is more or less equal to normal methods, and arguments are made that is interpretable.

### Strengths
The strength of this paper is that is is proposing a reasonable solution to a very difficult problem of interpretable deep RL. I like the general idea and it makes sense, and results are reasonable enough. It should also pave a way for counterfactual reasoning as the authors suggest, and several other possible future directions.

### Weaknesses
There are two main weaknesses of the paper in my view.

Firstly, there appears to be clear limitations of the method performance wise, it appears to really struggle to latch onto the similar abilities of the black-box, which can be problematic as reducing performance has catastrophic effects on user trust (and then appropriate reliance etc.) Or at least, HC64 etc. is needed to get reasonable performance as opposed to HC8.

Second, the authors don't actually show the method being particularly useful for anything. It isn't always necessary to do this, but I feel here it would have helped a lot. Usually, explainability methods are used to debug, teach, regulate, calibrate reliance, or offer recourse etc., but this method isn't shown to be able to do any of those things.

### Questions
* Sorry if I missed it, but does this work for pixel-based input data?
* Do you see this being useful for debug, teach, regulate, calibrate reliance, or offer recourse etc.,? If so, why didn't you demonstrate this.

I think overall, given the positives and negatives, I lean a bit towards acceptance, but will await the rebuttal etc. to mutate my score later. Thanks.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
### Problem Statement

The paper addresses the challenge of crafting interpretable policies in Deep Reinforcement Learning (DRL) to foster the development of trustworthy autonomous agents. The conventional linear policies, while interpretable, lack the expressivity to tackle complex tasks. In light of this, the authors advocate for piecewise-linear policies that aim to marry the interpretability of linear policies with enhanced performance akin to complex neural models.

### Methodology

To this effect, they introduce the "HyperCombinator" (HC), a neural architecture that embodies a piecewise-linear policy with a controlled number of linear sub-policies. Every interaction with the environment engages a specific linear sub-policy, enhancing the interpretability while maintaining competitive performance. The architecture is a preset number of sub-policies, each in the form of a set of linear coefficients, gated by a MLP with one-hot output with Gumbel-softmax reparameterization allowing end-to-end training.

### Main Contributions

The key contributions encapsulated in the paper are as follows:

- They delineate the attributes that a desirable interpretable piecewise-linear policy should exhibit.
- They design the HyperCombinator, a novel architecture that encapsulates a piecewise-linear policy with a defined number of linear sub-policies, and which is amenable to a broad spectrum of RL algorithms.
- They analyze the interpretability of HyperCombinator.
- They conduct evaluations of the model on control and navigation tasks, showcasing that the model retains a robust performance despite its curtailed expressivity.
- They leverage the interpretability of HC to develop two visualizations that elucidate the policy's reactions to inputs and unveil the temporal abstractions in task execution through tracking the sequence of sub-policies employed.

### Strengths
### Originality and significance

The problem of interpretable Deep Reinforcement Learning is of great practical value. Despite the simplicity of the proposed approach, it attains competitive performance while providing much more interpretability compared to conventional deep neural networks. The formulation of desired properties of an interpretable policy is also insightful.

### Writing

The paper is very well written. The organization is logical, presentation accurate and efficient. First laying out the desired properties and then evaluating the method against the properties makes the paper very easy to follow.

### Weaknesses
 - The method has limitations that prevent it from being applied to complex problems of larger scale: The policy loses interpretable as soon as the number of linear sub-policies grows large.

### Questions
- In the Cheetah control setup, is the action space continuous? If so, what does the "action 0" in Figure 3 mean? Is it one dimension of the action? Then it is not proper to refer to it as "for one action of $\tilde{\pi}$".
- Why are SAC and RIS chosen as the base alogrithm for RL in the experiments?
- Are subpolicies trainable? Besides the diversifying regularizations for the MLP, would similar regularizations encouraging a diversified sub-policy help with the learning and model capacity?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a novel architecture for actor-critic algorithms with the goal of increasing the interpretability of the learned policies. The proposed architecture learns a model that maps each input to a linear function, which is used to predict the agent's action. The underlying assumption is that, if we can understand the set of linear functions used to produce actions, then the model is "partially" interpretable. 

The new architecture, HyperCombinator (HC), is evaluated with SAC, where the actor model is replaced with an HC. The SAC-HC algorithm is evaluated on the DeepMind Control Suite benchmark. The empirical results show that the performance of SAC-HC in terms of sample efficiency is similar to that of SAC. 

The paper also presents plots showing how different linear functions are used across different episodes of problems such as Cheetah.

### Strengths
Policy interpretability is an important topic, since policies we can understand and verify are important in real-world scenarios. 

It is also interesting to see empirical evidence that it is possible to perform well in commonly used benchmarks with models with less capacity. 

Another strength of the paper is its clarity and ease of understanding. While the topics discussed aren't necessarily simple, the authors have done a good job presenting their results.

### Weaknesses
I have two main concerns with this paper. The first is about a whole body of work on programmatic policies that the paper overlooks. The second is about the weak evaluation related to the interpretability of the proposed model. I'll detail each concern below.

**Missing Related Work**

Below are some related works that I think the paper missed. The paper should cite some of these to better place its contributions within the existing literature. Others should serve as baselines in the experiments, as I explain later.

There's a line of research called Programmatically Interpretable RL (PiRL), see Verma et al. The goal in this line of research is to create programs that encode policies for RL problems. One of the key motivations behind PiRL is interpretability. Both Verma et al. and Bastani et al. use imitation learning to train interpretable models. Later, Qiu and Zhu found a way to learn similar policies with a fully differentiable approach, so there's no need for imitation learning. The architecture of Qiu and Zhu is essentially an oblique decision tree, which could also be trained with ReLU neural networks, as discussed in the work of Lee and Jaakkola and of Orfanos and Lelis.

The properties of ReLU networks share a lot in common with what's mentioned in the paper for the HC architecture:

1. "We make the functions $a$ and $\theta$ explicit through a new parametrization of the NN."

This is also possible with ReLU networks. In these networks, the function $a$ is the set of weights in the hidden layers, while $\theta$ is the function the model learns when the activation pattern is fixed (see Lee and Jaakkola for more). So, what makes the HC different from ReLU networks? The paper does not adequately explain the distinction, especially given that the local linear behavior of ReLU networks is a well-established property.

2. "We explicitly control the number of unique sub-policies of $\pi$ through the dimension $dG$ of the Gumbel-Softmax layer."

This is also the case with the number of neurons in ReLU networks. Another way to reduce the number of unique sub-policies in ReLU networks is to use a single hidden layer with strong L1 regularization (refer to Orfanos and Lelis). The paper needs to provide a more rigorous justification for why the proposed method of controlling sub-policies is superior to these existing techniques, particularly given that L1 regularization can also induce sparsity in the network's activations, effectively reducing the number of active linear regions.

3. "Policies modeled with the HyperCombinator differ from MLPs in that they usually aren't continuous at the border between linear regions."

I'm not sure why this is crucial, but ReLU networks also switch the linear function that gives the prediction when you move from one region to another. The paper should clarify why this discontinuity is a desirable property, as it could potentially lead to instability or erratic behavior in the policy.

4. "Our approach is locally interpretable, explaining the sub-policy applied to any given example."

This is true for ReLU networks mapped to Oblique Decision Trees too. The function that gives the prediction is at the leaf node. The path in the tree might not be easy to understand, but the linear function at the leaves is just as clear as those in the HC architecture. The paper needs to demonstrate how the interpretability of the HC architecture is superior to that of ReLU networks when both are analyzed at the level of their linear regions.

Given all these similarities, small ReLU networks should be used as baselines in the experiments. Specifically, the architecture by Qiu and Zhu showed strong results on the same benchmark problems used in this paper. The paper should also compare against other methods that explicitly learn interpretable policies, such as those based on decision trees or finite state machines.

Other papers I mention below might be less crucial but are related. So, it would be good to see where this paper stands within the broader literature. For example, Inala et al. discuss how to learn interpretable finite state machines for RL problems. Koul et al. learn FSM policies for RL problems from recurrent networks. Aleixo and Lelis look at programmatic policies in multi-agent RL. Trivedi et al. and Liu et al. learn a latent space of a domain-specific language which can be used to search for programmatic policies. All these papers explore potentially interpretable policies for RL problems, making them relevant to this submission.

**Lack of Evaluation on Interpretability**

The paper mostly gives anecdotal evidence when it comes to the interpretability of the policies. I appreciate the plots showing how the sub-policies work, but they're just examples. For some reason, the literature on interpretable policies doesn't focus much on evaluating interpretability. The papers I've listed below are weak in this area too. But none of them emphasize interpretability as much as this one does. The big unanswered question is: are these policies really interpretable, and if so, to whom?


### Questions
1. How does HC architecture compare with other works from the literature, especially those on the PiRL line of work? 

2. How can one properly evaluate the interpretability of these models?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
