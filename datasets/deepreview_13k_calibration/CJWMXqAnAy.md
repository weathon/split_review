# Optimization-Biased Hypernetworks for Generalizable Policy Generation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Policy learning through behavior cloning poses significant challenges, particularly when demonstration data is limited. In this work, we present HyPoGen, a novel optimization-biased hypernetwork structure for policy generation. The proposed hypernetwork learns to synthesize optimal policy parameters solely from task specifications, by modeling policy generation as an approximation of the optimization process executed over a finite number of steps and assuming these specifications serve as a sufficient representation of the demonstration data. By incorporating structural designs that bias the hypernetwork towards optimization, we can improve its generalization capability while being trained only on source task demonstrations. During the feed-forward prediction pass, the hypernetwork effectively performs an optimization in the latent (compressed) policy space, which is then decoded into policy parameters for action prediction. Experimental results on locomotion and manipulation benchmarks show that HyPoGen significantly outperforms state-of-the-art methods in generating policies for unseen target tasks without any demonstrations, achieving higher success rates and evidencing improved generalizable policy generation capability. Our work underscores the potential of optimization-biased hypernetworks in advancing generalizable policy generation. Our code and models will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces HyPoGen, a hypernetwork that generates policies for unseen tasks without demonstrations by learning policy parameters directly from task specifications. By structuring the network to mimic optimization, HyPoGen generalizes effectively despite limited training data. Experiments show it outperforms state-of-the-art methods on locomotion and manipulation tasks, achieving higher success rates in unseen scenarios. The authors will release the code and models.

### Strengths
- The paper was well-written.
- The experimental results show that performance improvement is significant.

### Weaknesses
 - In general, I am curious about the limitation of the proposed method. Please refer to the questions section.

### Questions
- Could the proposed approach work in discrete action space?
    - Is there any potential difficulties or benefits of applying this approach for discrete actions?
- In the experiments section, it seems that the generated policy was adapted in the scenario in which task is slightly modified, such as the desired speed of the agent changed. Can authors provide more experiments that policy is generated for more distinct tasks, such as meta-world?
- Though the authors provide average success rate, it would be also important to show the variance of the success rate.

[1] Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning, Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Avnish Narayan, Hayden Shively, Adithya Bellathur, Karol Hausman, Chelsea Finn, Sergey Levine

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel hypernetwork architecture for policy generation in behavior cloning, with a focus on generalization to unseen tasks without requiring extra expert demonstrations. Unlike existing methods that apply hypernetworks to generate policy network parameters directly from a task specification, the proposed hypernetwork architecture, HyPoGen, iteratively generates a policy network by simulating gradient-based optimization, where the pseudo "gradients" are conditioned on the task specification. Additionally, the generation of these pseudo "gradients" across different layers of the policy network is structured to follow the chain rule. The primary idea is that the inductive biases introduced by simulating gradient-based optimization can help improve policy generation quality and improve generalization to unseen tasks. Experimental results show that HyPoGen outperforms baseline methods in generating policies for unseen tasks without any demonstration and that the policy performance improves during the simulated optimization guided by the trained hypernetwork.

### Strengths
1. The paper addresses the challenge of generalizing policy generation to unseen tasks without any demonstration, a realistic and difficult problem in imitation learning.

2. The main contribution of the paper is the novel hypernetwork architecture, HyPoGen, which introduces inductive biases to generate a policy network by simulating gradient-based optimization. The architecture performs iterative pseudo "gradient"-descent where the pesudo "gradients" are enforced to follow chain rule across different layers of the policy netowrk, an interesting and sensible approach.

3. It is demonstrated through extensive experiments on locomotion and manipulation benchmarks that HyPoGen outperforms baseline methods in generalizing to unseen tasks without any demonstration. Additionally, several empirical cases studies (notably in Table 4) provide evidence that the proposed hypernetwork architecture effectively simulates an iterative optimization process. 

4. The paper is well organized and clearly written, with a thorough discussion of related work to place it within existing research. The rationale behind the HyPoGen architecture design is clearly explained, and the construction of the hypernetwork's inner components is presented effectively.

### Weaknesses
1. The training process of the proposed hypernetwork is described somewhat briefly in Section 4.2. Although the set of learnable parameters and the loss function (Eq. 1) are discussed, likely implying end-to-end training over source tasks to minimize the BC loss (Eq. 1) while optimizing all learnable parameters simultaneously, this part could be elaborated more explicitly. Including pseudocode in the appendix might be helpful if the training procedure is not this straightforward. 

2. In Section 5.4, there is an analysis of the statistics of the generated policy network parameters with different initial values of $\theta_0$ (Table 3). Are other hypernetwork parameters, apart from $\theta_0$, kept fixed across different initial values of $\theta_0$, or are they retrained separately for each initial value of $\theta_0$? In either case, the presented statistics in Table 3 might not be able to sufficiently answer the question whether HyPoGen remembers a fixed set of parameters for each specification. Specifically, if the other hypernetwork parameters are not retrained, observing the statistics of generated policy network parameters may be less meaningful as the hypernetwork is not adapting to the $\theta_0$ value in use; if the hypernetwork is retrained for different initial values of $\theta_0$, it could still be the case that HyPoGen remembers a fixed set of parameters for each specification for a given $\theta_0$.



### Questions
1. Is my understanding of the training procedure of the proposed hypernetwork correct, i.e. are all trainable parameters of the hypernetwork, including $\theta_0$, trained simultaneously in an end-to-end fashion?

2. Are any parts of the hypernetwork parameters retrained for each initial value of $\theta_0$ when performing the analysis of Table 3? See Weakness 2 above for further context of this question.

3. Appendix B.1 provides the range, granularity, and number of samples of tasks specifications in different environments used in the experiments. Is task specification sampling done uniformly? Is the source-test task partition also uniform? If so, for the cases where only one task parameter varies, could there be very similar specifications among the source tasks for most test tasks? For example, Table 6 shows that the Cheetah environment has about 40 possible specifications, and there are 40 samples, so nearly every specification appears in either source or target tasks (assuming sampling without replacement).

4. It is mentioned that the optimization is performed in a compressed latent space. What is the dimension of this latent space?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In low-data settings, using a hypernetwork can be promising. However, classical hypernetworks have critical issues, such as overfitting, which can limit their generalization capability. To address this, the authors modify the role of the hypernetwork. Instead of directly predicting the policy weights, they iteratively compute the weights in a manner similar to multi-step gradient descent. This reformulates the optimization problem for the hypernetwork to predict gradients instead of weights directly, which the authors empirically show leads to better performance and generalization on locomotion and manipulation tasks.

### Strengths
This work strengthens hypernetworks by altering the training optimization be guided to output intermediate gradient steps, a novel approach for hypernetworks, especially in policy settings.

The writing and figures are clear, and the experimentation is thorough, with a wide range of baselines that use the same policy network architecture and specification encoder. Performance consistently surpasses that of the baselines.

I found the section "Does HyPoGen actually perform optimization?" particularly interesting and insightful that showcases how it is actually like an optimizer.

### Weaknesses
Overall, I think this work is strong, and I would be interested in seeing additional analysis on how closely the predicted intermediate gradients align with true gradients that would result from directly optimizing the policy. While the authors have shown that the iterative optimization process effectively reduces the loss over time, it would be valuable to quantify the similarity between these predicted gradients and the actual gradients obtained through standard gradient descent. Such an analysis could fortify the claim that the hypernetwork is indeed guided to predict meaningful gradients, rather than simply memorizing an update path. This comparison would strengthen the case for the hypernetwork's ability to emulate true gradient-based optimization, supporting its effectiveness in generalizing to unseen tasks. While this is not a critical weakness, it would serve as a valuable addition that could make the work even more compelling.

### Questions
I think mentioning learned optimizers : https://arxiv.org/pdf/2209.11208 can be relevant to the overall framing of this work. 

I also am wondering how well would directly training the hyper network on the true gradients be, such that instead of it resembling back propagation, it is exactly back propagation (assuming no training error) .

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose to incorporate inductive biases about optimization into a hyper-network framework that generates policies for different tasks. They do so by parameterizing the hypernetwork updates based on the chain rule and also on a delta to the current weights. They show that these inductive biases help HyPoGen outperform previous methods when generalizing across a set of related tasks.

### Strengths
- The method is presented and motivated well.
- The experiments provide compelling evidence that HyPoGen outperforms previous methods (at least based on the average).
- The idea of neural gradients for policy generation is interesting. The methods presented in this paper for incorporating optimization inductive biases into hypernetworks could lead to future interesting work.

### Weaknesses
 - The variances for Table 1 / 2 (reported in Table 13/14) are quite high (on the order of 100-200). This makes it harder to argue that HypoGen is better than the previous methods when the gap is often on the order of a few tens of units. It would be fairer to report exact confidence intervals in the main text to make the comparison more clear.
- The computational costs of HyPoGen aren’t directly addressed. Since it requires multiple steps to keep decreasing the loss, how does the computational cost compare to other methods (especially something like HyperZero)? This makes me think that other baselines could be relevant to assess the tradeoff between computational cost and performance. For example, instead of parametrizing the full chain rule (equation 6/7), can the majority of the benefit be obtained by framing the problem just as a delta from the previous step (equation 5).
- While the paper claims that HypoGen leads to better generalization, Fig. 4,5,6,7,8,9 show generalization somewhat qualitatively and it is not super clear (other than Fig. 4) that HyPoGen generalizes better than the other methods. Are their more precise metrics that could show this generalization more clearly (i.e. report performance within one std of training distribution and outside of that for the relevant methods).

### Questions
- What happens if HyPoGen is applied for many more steps (Fig. D)? Does the loss keep going down, or does it “overfit” eventually?
- What is the strategy for choosing the number of hyper-optimization steps? Do harder problems (more out-of-distribution for example), require more optimization steps?
- Does HyPoGen work for larger policy models / harder environments (the policy networks at the moment seem to be only 2 layer MLPs)?

### Soundness
2

### Presentation
4

### Contribution
3
