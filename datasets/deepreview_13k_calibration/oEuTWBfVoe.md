# Model Based Inference of Synaptic Plasticity Rules

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Understanding learning through synaptic plasticity rules in the brain is a grand challenge for neuroscience. Here we introduce a novel computational framework for inferring plasticity rules from experimental data on neural activity trajectories and behavioral learning dynamics. Our methodology parameterizes the plasticity function to provide theoretical interpretability and facilitate gradient-based optimization. For instance, we use Taylor series expansions or multilayer perceptrons to approximate plasticity rules, and we adjust their parameters via gradient descent over entire trajectories to closely match observed neural activity and behavioral data. Notably, our approach can learn intricate rules that induce long time-dependencies, such as those incorporating weight decay. We validate our method through simulations, accurately recovering established rules, like Oja's, and more complex hypothetical rules incorporating reward-modulated terms. We assess the resilience of our technique to noise and, as a tangible application, apply it to behavioral data from \emph{Drosophila} during a probabilistic reward-learning experiment. Remarkably, we identify an active forgetting component of reward learning in flies that enhances the predictive accuracy of previous models. Overall, our modeling framework provides an exciting new avenue to elucidate the computational principles governing synaptic plasticity and learning in the brain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper develops a meta-learning model for synaptic plasticity rules. They parameterize the plasticity rule as a polynomial function, or a multi-layer perceptron, of the pre-, post-activity, weight and global reward, and by gradient descent update the learning rule to minimize a loss that depends on the output trajectory. Differently from previous work, they optimize over the whole trajectory, instead of final weights/activity, and apply it also to behavioural data, instead of neural activity. One application has the loss as the distance to a target trajectory, obtained from a ground truth learning rule (Oja’s rule), which is successfully recovered. In the second application, the output activity represents the probability of taking an action on a reward-seeking task, and the target is a trajectory of actions taken. This is applied to experimental data of a fruit fly in a setting where the rewarding action changes over time. A reward-based rule of the form x*(R - E[R]) - a*w is recovered, and variations with and without E[R] or -a*w factors are discussed.

### Strengths
The main novel contributions of the paper are the optimization over trajectories, instead of endpoints, and fitting behavioural data. 
- Optimizing over trajectories might be more efficient and appropriate when such data is available. 
- Fitting a family of plasticity rules to data will strengthen our knowledge of mechanisms at work in different systems.
- It is significant to propose a new dataset that can be modelled by this approach.

Previous literature on inferring plasticity rules is properly referred to.

The simulation results seem sound.

The general methodology is clear (apart from the questions outlined below).

### Weaknesses
The main weaknesses are:
- Methodological choices
- Theoretical grounding of learning rules
- Limited novelty of trajectory optimization

There are methodological questions that should be clarified, listed also in the Question section below.

It is unclear why there are multiple output neurons, how they are pooled, and if they all learn the same thing. Is it the case that one needs multiple output neurons just to have enough data, and it would be equivalent to having many instantiations of the simulation with single output neurons? Do the neurons for Oja's rule all simply learn the first principal component?

Related to this point, if all neurons in the output layer learn the same thing, the study in Fig.2 with noise and sparseness might simply reflect how many "trials" are needed for a single neuron simulation. Noise in this case would just make gradients for the meta-learning less informative, needing more trials, which would be true for any learning simulation.

One main contribution of the paper relative to previous work is optimizing trajectories, instead of endpoints, but it is not clear if this is a substantial advancement. It would strengthen this point to have more results and discussion on this difference. What kind of data can this model tackle that endpoint optimization can't? Would the results be the same? Is it a matter of data efficiency? How would endpoint optimization behave in the fly dataset? A technical point: is backprop through time used?

One main contribution of the paper is the fitting of behavioral data. But there is a gap between modelling a synapse and a whole system as if the fly was a single neuron. Why can modelling a single neuron work in this case? Isn't this approach more appropriate for neural data from the relevant neurons in the fly mushroom body?

There is a lack of theoretical grounding of the learning rules studied, e.g. that the Oja rule will learn the PC1; what are the optimal learning rules for the reward-based task?; what is the effect of the weight decay term on the learning rule?

There is no discussion on the time scale inherent to the learned weight decay term. How does it relate to trial times? Related, the effect of the time scale of the E[R] is subtle and will have a different effect if the average is within a trial or over multiple trials (see Fremaux, Sprekeler, Gerstner, J Neuroscience, 2010). Related to this point, did the authors try learning the E[R] factor separately, or learning the time scale? The discussion on weight dependent vs. expected reward factor loses strength due to these limitations.

The MLP rules are included but never discussed. They should be better motivated and referred to.

Minor:

In the figures, it should show the factors in the ticks (e.g. x*R), instead of the binary parameter indexes, which are hard to decode.

### Questions
How are the inputs x_t sampled? N(0,1)?
How exactly are the neurons from the output layer pooled in each application?
Do all neurons in the output layer learn the same thing?

Is the loss and gradient local in time or backpropagated through time?
How does the trajectory loss compare with the end goal loss?

What do the MLP learning rules learn?

Why is the E[R] term not learned as a separate term?
How does the result depend on the time scale of E[R]? 
What is the time-scale inherent to the learned weight decay term?

How should one relate the learning rule for a single neuron to the output behaviour or a whole system?

### Soundness
2 fair

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
The paper proposes to learn parametrized synaptic plasticity rules in recurrent rate networks by optimizing on loss functions defined on the neural trajectories and/or behavioural data. The method is validated using Oja's rule, and also applied to neural and behavioural data from the fruit fly. In the latter experiment, the method identifies a weight-dependent term that accounts for better predictions of fly behaviour.

### Strengths
1. The idea to directly fit plasticity rules to neural or behavioural data, rather than to functional tasks, to get biologically plausible rules is interesting.

2. The experiments with the fly data are also interesting. In particular, the careful exploration to test different hypothesis about the synaptic mechanism underlying fly choice behaviour led to interpretable results on which plasticity rules, and in particular, which terms in the rule could modulate forgetting learned associations, and bidirectional plasticity. 

3. The paper is clearly written, concepts and related work are well-explained and overall, quite easy to follow.

### Weaknesses
1. The fact that the method is restricted to rate networks precludes interesting synaptic rules from spiking networks (e.g. spike-timing dependent plasticity) that could explain a wider a range of plasticity mechanisms, and thus limits the set of interesting rules that could be inferred using this method.

2. I am skeptical of the generalisability of this method, since the discovered rules would strongly depend on the choice of loss function for the neural / behavioural data. While the experiments in section 4.2 with robustness to noise and sparsity work in the idealised setting, the robustness is demonstrated with Gaussian noise, which the MSE loss is by definition capable of ignoring, in the limit of infinite data. However, with real-world neural/behavioural data, we cannot always pinpoint the exact distribution of noise, and it would be practically quite difficult to construct a loss function that is robust to unknown noise. I am thus skeptical that the method would generalise to arbatrarily complex neural behaviours or trajectories, and that the inferred plasticity rules in these settings would be biologically plausible.

3. Section 7 mentions that "[a]nother issue is the model's "sloppiness" in the solution space; it fails to identify a unique sparse solution even with extensive data". If this is the case with the current experiments in sections 4-6, how does this affect the interpretation of the results and how much can we rely on the experimental predictions about plasticity mechanisms? For instance, which particular experiment/solution forms the basis for the conclusions about the decay mechanism in 6.1 and bidirectional plasticity in 6.2?

4. The experiments in section 6, appear to add terms to the parametrized rule based on previously hypothesised plasticity mechanisms in the fruit fly. Although, this was an effective method of exploration in this particular instance, how would this generalise to neural / behavioural datasets for which such hypotheses do not exist, or are unsatisfactory? If instead, we could perform rule inference using this method using MLPs or some other form of parametrization, how would we interpret the resulting rules?

Taken together, it seems that although this method provides more biologically plausible rules that plasticity rule inference via optimizing for network function (Tyulmankov et al 2022, Confavreux et al 2020, Lindsey and Litwin-Kumar 2020, etc.), it swaps one set of loss functions for another, but still shares many of the same problems of generalisability and interpretation.

### Questions
1. How generalisable is the method, when in its current form, it cannot be applied to spiking networks?
2. How generalisable is the method, when constructing a loss function on neural activity / behaviour with unknown noise sources?
3. How interpretable / reliable are the inferred plasticity mechanisms when the model fit is "sloppy" with limited data?
4. How generalisable is the inference mechanism when we do not have satisfactory a priori hypotheses about the underlying plasticity mechanism?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper infers synaptic plasticity rules from experimental data on neural activity or behavioral trajectories by parameterizing the plasticity function to provide theoretical interpretability and facilitate gradient-based optimization.
They use Taylor series expansions or multilayer perceptrons to approximate plasticity rules and adjust parameters via gradient descent over entire trajectories to match observed neural activity or behavioral data closely.
They also learn intricate rules that induce long nonlinear time-dependencies, such as those incorporating postsynaptic activity and current synaptic weights, and validate through simulations, accurately recovering established rules, like Oja's, as well as more complex hypothetical rules incorporating reward-modulated terms.

### Strengths
The framework's ability to parameterize the plasticity function provides a balance between theoretical interpretability and practical optimization.

The use of established mathematical techniques, like Taylor series expansions and multilayer perceptrons, lends credibility to the approach.

The method's versatility is evident in its ability to learn both established rules like Oja’s and more complex, hypothetical ones.

Real-world application on Drosophila data and the discovery of an active forgetting component showcase the practical relevance and potential breakthroughs the framework can offer.

### Weaknesses
The paper is really interesting, but I have some key concerns. First and most importantly, I think this paper might not be a very good fit for the conference and might be better suited for a neuroscience journal/conference. For example, the paper tries to recover Oja's rule from experimental data. Though it is a good exercise, I feel it would be interesting if this method could be used to model a more generalized learning form and show the performance of using that learning method in small networks - suppose a Hopfield network with the new plasticity. Essentially, improves on top of Oja's method using the added information and makes it more biologically plausible.



### Questions
1. How were the plasticity rules shown in Table 1 derived? Were they ad-hoc variations of Oja's rule? It would be interesting if you could use some symbolic regression to find the optimal plasticity rule. 

2. Can you explain what you mean by "fits neural firing rate trajectories over the course of learning" in Page 2?

3. You mentioned "Performance benchmarks reveal that our framework
is capable of executing simulations with up to 106 synapses and 1000-time step trajectories in less
than an hour on an NVIDIA A100 GPU." - however, from what I understand, the experiments seem to have been done on a much smaller number of synapses. Can you clarify?

4. I could not fully understand the results in Section 4.2. It would be great if the authors  could add more details on "The remaining (1 − a) fraction of neurons are modeled by incorporating random noise drawn from the same distribution as the observed neurons."

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a gradient-based learning framework to infer biologically-plausible synaptic plasticity rules from experimental data. The method models the learning rule using polynomials of presynaptic, postsynaptic activities, current synaptic weight, and reward signal or with a multilayer perceptron. The proposed approach successfully recovers Oja's rule and plasticity in the fruit fly.

### Strengths
The paper has the following strenghts:

* It addresses a crucial question related to inferring synaptic plasticity from biological data, contributing to the field.

* The experiments conducted are intriguing and validates the proposed method.

* Limitations of the proposed algorithm are discussed at the end of the paper in detail.

* The availability of a documented and clear code enhances the reproducibility of this work.

### Weaknesses
I think the paper has several weaknesses. Please see the following list and the questions sections.

* The statement in the introduction regarding the biological plausibility of backpropagation may be too weak ("While the backpropagation ..., its biological plausibility remains a subject of debate."). It is widely accepted that backpropagation is biologically implausible.

* Regarding the following sentence in Section 3 "We further define a readout ... ,i.e., $\mathbf{m}^t = f(y^t).$", did you mean to write $\mathbf{m}^t = f(\mathbf{y}^t)$ ($\mathbf{y}^t$ with boldsymbol)?

* On page 4, "setting $\theta_{110} = 1$ and $\theta_{012} = -1$," the second term should be $\theta_{021}$ rather than $\theta_{012}$.

* The initialization of polynomial coefficient parameters is not clear, and it seems they are initialized close to zero according to  Figure 2. It would be valuable to explain how they were initialized.

* The paper models synaptic plasticity rules only for feedforward connections. It would be interesting to explore the impact of lateral connections (by adding additional terms in Equation 6). Have you experimented with such a setup?

* In page 7, the authors state that "In the case of the MLP, we tested various architectures and highlight results for a 3-10-1 neuron topology." What are the results for other various architectures? Putting them into the paper would also be valuable (as ablation studies).

* The hyperparameters for the experiments are missing? What is the learning rate, what is the optimizer, etc.?

* I do not see that much difference between the experiment presented in Section 4 and the experiment in (Confavreux et al., 2020) (Section 3.1) except the choice of optimization method. In your experimental setup, you also do not model the global reward. Therefore, I think it makes it more similar to the experiment in (Confavreux et al., 2020).

* Comparison to previous work is missing.

### Questions
* As a follow-up question related to my comment about the similarity with (Confavreux et al., 2020): (Confavreux et al., 2020) uses Covariance Matrix Adaptation Evolution Strategy (CMA-ES) as they state it has better scalibility with the network size compared to gradient based strategy. Why do you use gradient based strategy? What is the advantage?

* In the experimental setup in Section 5, if you do not neglect the hypothetical dependencies on $y_i$, would your framework correctly infer the learning rule, i.e., if you use $$g_\theta = \sum_{\alpha, \beta, \phi, \gamma} \theta_{\alpha, \beta, \phi, \gamma} x_j^\alpha r^\beta y_i^\phi w_{ij}^\gamma$$ would your model learn $\theta_{\alpha, \beta, \phi, \gamma} = 0 \quad \forall \phi \neq 0$?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
