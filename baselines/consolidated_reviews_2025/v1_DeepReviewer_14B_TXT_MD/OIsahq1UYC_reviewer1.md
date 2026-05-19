### Summary

The paper considers a method of sampling from unnormalized density tables. The authors build upon previous work on diffusion-based samplers and GFlowNets to create a model that amortizes the integral of the unnormalized density function. The method is evaluated on a number of benchmarks and compared to previously proposed methods.

### Soundness

2 fair

### Presentation

1 poor

### Contribution

2 fair

### Strengths

The paper builds on interesting previous work and the experimental results seem promising.

### Weaknesses

#### Some Related Works


#### comment

I found the paper to be quite hard to read and understand, even though I am familiar with both diffusion models and GFlowNets. The paper seems to be trying to bridge the gap between the two concepts, but in my opinion it does not succeed in uniting them in a meaningful way. In particular, the paper introduces a lot of notation and terminology from both areas, but it does not explain them properly. I am still not sure what the contribution of the paper is, and how exactly the proposed method works.

The authors use a lot of notation, and I think that some of it is not used properly. For example, the authors use \mathcal{P} to denote the target distribution in many places, while it is actually a joint distribution over the reference process and the target distribution (which is a conditional distribution). The authors also use the term "state" to refer to a node in a graph, which is confusing since the method operates in continuous space. The notation p^refe_n is also not clearly defined, and it seems to change its meaning in different parts of the paper. The term "forward process" is used in a way that is opposite to its standard meaning in the diffusion model literature, which adds to the confusion. The explanation of how the method reduces variance in gradient updates is also insufficient. The connection to temporal difference learning is mentioned but not elaborated upon, leaving the reader to guess how the method avoids computing gradients over entire trajectories.

### Suggestions

The paper needs a significant revision to improve its clarity and accessibility. The authors should start by clearly defining all the notation and terminology they use, and they should avoid using the same symbol for different concepts. For example, they should use different symbols to denote the target distribution, the joint distribution, and the conditional distribution. They should also avoid using the term "state" to refer to a node in a graph, since the method operates in continuous space. The authors should also clarify the meaning of p^refe_n and explain how it is related to the reference process. The use of the term "forward process" should be reconsidered, or at least explained more carefully, to avoid confusion with the standard terminology in diffusion models. A table summarizing all the notations and their definitions would be very helpful.

To address the lack of explanation regarding variance reduction, the authors should provide a more detailed explanation of how their method relates to temporal difference learning. They should explain how the method uses local learning signals to update the model parameters, and how this avoids the need to compute gradients over entire trajectories. A simple example, perhaps in a tabular setting, would be helpful to illustrate this point. The authors should also explain how the flow function is used to estimate the partition function and how this is related to the importance weights. The connection between the flow function and the unnormalized target distribution should be made more explicit. The authors should also clarify the role of the learned function F in approximating the integral of the target distribution, and how this is used to compute the partition function.

Finally, the authors should clearly state the contribution of their work. What is the novel aspect of their method, and how does it improve upon previous work? The experimental results seem promising, but the paper needs to provide a more clear and convincing explanation of why the proposed method works. The authors should also discuss the limitations of their method and suggest directions for future research. The paper should be written in a way that is accessible to readers who are familiar with either diffusion models or GFlowNets, but not necessarily both. The current presentation makes it difficult to understand the core ideas of the paper, and a major rewrite is necessary to address these issues.

### Questions

* What exactly is the contribution of the paper? How does the method compare to previously proposed methods?
* What is the notation Q? I think it is not defined in the paper.
* The authors use \mathcal{P} to denote the target distribution \mu, but is not this the name of the joint distribution over the reference process and the target distribution (which is a conditional distribution)?
* What does it mean that the method uses "detailed balance"? In which sense is the method using this term?
* What does it mean that the method uses "local signals"? How does it work?
* What is p^refe_n? This notation is not explained in the paper.
* The authors say that they "amortize the integration computation into the learning of \theta". What does this mean? How does the method do this?
* How does the method estimate the partition function of the unnormalized target distribution?
* What is the relationship between the proposed method and the path integral framework?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
