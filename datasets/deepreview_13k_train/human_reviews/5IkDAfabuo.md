# Prioritized Generative Replay

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Sample-efficient online reinforcement learning often uses replay buffers to store experience for reuse when updating the value function. 
However, uniform replay is inefficient, since certain classes of transitions can be more relevant to learning. While prioritization of more useful samples is helpful, this strategy can also lead to overfitting, as useful samples are likely to be more rare. 
In this work, we instead propose a prioritized, parametric version of an agent's memory, using generative models to capture online experience. This paradigm enables (1) \textit{densification} of past experience, with new generations that benefit from the generative model's generalization capacity and (2) \textit{guidance} via a family of ``relevance functions'' that push these generations towards more useful parts of an agent's acquired history. We show this recipe can be instantiated using conditional diffusion models and simple relevance functions such as curiosity- or value-based metrics. 
Our approach consistently improves performance and sample efficiency in both state- and pixel-based domains. We expose the mechanisms underlying these gains, showing how guidance promotes diversity in our generated transitions and reduces overfitting. We also showcase how our approach can train policies with even higher update-to-data ratios than before, opening up avenues to better scale online RL agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work proposes a form of sample based experience replays that leverages a generative model to provide and augment samples drawn from the replay buffer. To avoid overfitting, a set of guidance functions are used to steer the generative process toward diverse and useful samples. The generative replay mechanism is a diffusion model that is conditioned on some auxiliary information. The authors propose a few different versions of this conditioning such as intrinsic curiosity, TD error, or Q values. The idea is that using these scores, the generative model can be steered towards generating high quality samples. Given such a replay mechanism, this work evaluates model free and model-based RL agents trained via this generative replay on gym and dmc.The results show improvement on both pixel based and state based tasks. There are also ablations with larger policy networks and higher generative data rations, which show further improvements.

-------------------------------------------------
I thank the authors for a substantive rebuttal that addressed my and (as far as I can tell) other concerns. I therefore raise my score to an 8.

### Strengths
* This work proposes a scalable method for training model-free or model-based agents in a variety of domains. I believe the formulation is simple enough to be integrated into and improve other approaches. 

* I also found the presentation clear and easy to read. 

* I found the scaling experiments to be very compelling, I'm a little concerned about the general thrust of driving up the syn-real data ratio as high as possible, since we do need to ground the generations in real experience. But I still think insights here are valuable.

### Weaknesses
I have two points of contention with this work. 
1. From a paradigm perspective, I don't understand how this is different from prior work in model-based RL that apples intrinsic rewards to a learned dynamics model [1] or world-model [2]. These methods also utilize a generative model as a copy of the environment, then train the agent in simulation to acquire interesting data (under the intrinsic reward). It seems that this method does the same, except that instances, rather than full trajectories are generated. I do see how this is different than just applying an intrinsic bonus during training, since here the synthetic data has a chance to be more diverse. 

2. I thank the authors for providing numerous experiments, but I am not at all convinced that this method is robust to the choice of guiding function F. ICM is known to be susceptible to the noisy TV problem, where difficult-to-model environmental factors score arbitrarily high under ICM. The chosen tasks are too simple perceptually to see this problem. This in and of itself is not a problem, but it means that we need to search for another F that works for our task which is hard in practice. In the meantime, there are other intrinsic rewards that do not suffer from this pathology [3].

### Questions
I'll rephrase my above concerns as questions. 

1. How is this method novel with respect to prior work that uses intrinsic rewards on rollouts from a learned dynamics model? It seems like a very similar approach to acquiring data that scores well under a given guidance function F, where F can be ICM or another intrinsic reward. 

2. How does this method handle noisy-tvs?

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
3

### Summary
This paper proposes a conditional diffusion model as a synthetic replay buffer to combat early overfitting in online reinforcement learning and to diversify experiences for the learning model. This is achieved with a relevance function that selects samples that are rare but important for learning based on the temporal difference error, the value of a learned Q-function and a modified intrinsic curiosity module.

### Strengths
One of the strength of this paper are the clear and concise language as well as good structured presentation of the proposed method.
It is quite logical to improve on the already existing prioritized experience replay method and implement it in the generative domain. The method is explained well and should be quite easily reproducable.
Overall the research could be a valuable contribution to the reinforcement learning community.

### Weaknesses
A topic i feel like missed somewhat are the different ways to approach generative replay such as mentions of other generative models (e.g. variational auto encoders, gaussian mixture models) and why they were not used.
One thing i found rather off putting and this is very nitpicky is that the Tables 1, 2 and 3 are a bit crammed and slightly off from each other.

### Questions
What exploration method does the agent use?
Could the exploration method be improved instead of the sample generation to improve diversity of samples?
Would a combination of both a better exploration and this method be the optimal and a possible solution?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes to use conditional diffusion models to improve the experience replay for an RL learning agent. The method proposed improves performance by improving the diversity of the samples in the experience replay buffer and reducing overfitting.

### Strengths
1. The paper is well written and provides a clear explanation of their method.
2. The research problem addressed in the paper is well laid out and is an important one to improve the performance of RL methods.

### Weaknesses
1. While the method shows improved performance, it is a bit simple as it combines existing elements in diffusion models and RL to propose the solution.
2. It would be useful to compare the effect of different kinds of exploration bonuses.

### Questions
1. Is the method compatible with different kinds of exploration bonuses? If so, how do you think they would compare?
2. How do you think the method would do when simply having diverse samples does not imply usefulness? An example is the noisy tv problem.
3. How sensitive is the algo towards the frequency of the inner loop in Algo 1?
4. Can multiple relevance functions be combined?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a framework called Prioritized Generative Replay (PGR), a novel approach to enhance sample efficiency in online reinforcement learning (RL). Traditionally, replay buffers store experienced transitions and replay them uniformly or with prioritization based on metrics like TD-error. However, the authors point out that uniform replay can be inefficient, and prioritization can lead to overfitting. PGR addresses these issues by using a conditional generative model to create a parametric replay buffer. 

The paper claims that this allows for two key advantages:
1) Densification: The generative model can create new, plausible transitions beyond those directly experienced, enriching the training data, especially in sparsely explored regions.
2) Guidance: By conditioning the generative model on "relevance functions," the generated transitions can be steered towards areas more critical for learning, such as states with high novelty or uncertainty.

The authors also explore various relevance functions, including return, TD-error, and curiosity. They find that curiosity, based on the prediction error of a learned dynamics model, performs best. This is attributed to its ability to promote diversity in the generated transitions, thus reducing overfitting. They also show that their approach consistently improves performance and sample efficiency in both state- and pixel based domains.

### Strengths
1) PGR offers a fresh perspective on replay buffers by combining generative modeling with guided replay. Framing this problem as a conditional generation problem with diffusion models is novel.
2) Diffusion model typically uses one single set of HPs requires no additional tuning I'd assume. This works well for PGR
3) Empirical results on various benchmarks demonstrate that PGR consistently outperforms existing model-free and model-based RL algorithms, as well as a generative replay baseline without guidance. Also has been shown to work in both state-based and pixel-based environments. 
4) PGR is shown to scale well with larger policy networks and higher synthetic-to-real data ratios (important ablation that I wanted to see), potentially enabling more data-efficient training of large-scale RL agents. Really important result for scaling to many real use cases.
5) The authors also provide insights into why PGR works, particularly highlighting the role of curiosity in promoting diversity and reducing overfitting.

### Weaknesses
1) The curiosity-based relevance function relies on a learned dynamics model, which might be challenging to train accurately in complex environments. The paper does not sufficiently address the potential for compounding errors in the dynamics model to negatively impact the quality of generated transitions, especially in scenarios with high environmental stochasticity or where the dynamics are inherently difficult to model. This could lead to the generation of unrealistic or misleading transitions, thereby hindering rather than helping the learning process.
2) Increasing Synthetic Data ratio does not benefit PGR and the unconditional baseline (SynthER) equally. PGR scales better at r=0.75 than SYNTHER but neither benefits from 0.875. We would think the trend would be consistent? whats the intution behind this? Also this figure 7 could be improved with the variation in r being shown. The paper lacks a clear explanation for why increasing the synthetic data ratio beyond a certain point does not yield further improvements, and why the performance of PGR and SynthER diverges at higher ratios. The lack of a detailed analysis of the trade-offs between real and synthetic data, and how this balance affects the overall learning process, is a significant weakness. The absence of a sensitivity analysis on the synthetic data ratio further compounds this issue.
3) (Minor) writing issues throughout the paper with some missing words etc. Please re-read the paper and make the necessary changes.

### Questions
1) How robust is PGR to errors in the learned dynamics model? Are there ways to mitigate the impact of inaccurate dynamics predictions on the curiosity-based relevance function?
2) Could PGR be extended to offline RL settings? If so, what modifications would be necessary?
3) How does PGR's performance compare against PER baselines which use approximate parametric models of prior experience?
4) Are there any other relevance functions thats been tried out? As thats core to the working of PGR.

### Soundness
4

### Presentation
3

### Contribution
3
