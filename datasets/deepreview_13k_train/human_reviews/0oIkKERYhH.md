# DOG: Discriminator-only Generation Beats GANs on Graphs

- Decision: Reject
- Scores: 3, 6, 3, 5

## Abstract
We propose discriminator-only generation (DOG) as a generative modeling approach that bridges the gap between energy-based models (EBMs) and generative adversarial networks (GANs). DOG generates samples through iterative gradient descent on a discriminator's input, eliminating the need for a separate generator model. This simplification obviates the extensive tuning of generator architectures required by GANs. In the graph domain, where GANs have lagged behind diffusion approaches in generation quality, DOG demonstrates significant improvements over GANs using the same discriminator architectures. Surprisingly, despite its computationally intensive iterative generation, DOG produces higher-quality samples than GANs on the QM9 molecule dataset in less training time.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a generative modeling approach for graph data.  It creates samples by iteratively optimizing the input to a discriminator, eliminating the need for a separate generator model. This simplification reduces the complexity of tuning generator architectures. The study shows that in the graph domain, where GANs have historically underperformed diffusion approaches in generating high-quality data, the proposed method outperforms GANs using the same discriminator architectures.

### Strengths
1) In this paper,  authors present a method to train GANs without generator. It successfully generate good images, which is convincing.  

2) Paper is easy to follow.

3) Authors conduct effective experiments to support the proposed method.

### Weaknesses
I have a few questions, which is as following:

1) The proposed method is not new for me. Previous works already distill knowledge from the pretrained Discriminator into a new generator or noise (noise is update when optimizating). Thus I guess there are less contributions in this paper. 

2) One import problem is why the proposed method works better for the graph data. I fail to find the reason why it works. I think it is important aspect that authors should explain. 

3) How about the inference time? I guess I need to update a new noise again.

4) Although authors conducting a few experiments, the used datasets are small and little.

### Questions
My main concerns are two views: (1)  why it works better for the  graph data (2) it is not new without generator, since distilling knowledge from the pertained discriminator has been studied previously.

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
The authors present an innovative approach to training Generative Adversarial Networks (GANs) for graph tasks, utilizing only the discriminator in a process similar to diffusion models. They offer a novel iterative method that removes the traditional generator, proposing a training scheme that progressively refines sample generation through the interaction with the discriminator. A theoretical underpinning is provided with a convergence analysis demonstrated on simple 1-D grid data. Experiments across both synthetic datasets (such as 25-Gaussian, Community-small, and SBM) and real-world datasets (including QM9 and Proteins) demonstrate that this generator-free GAN approach yields results on par with existing methods like SPECTRE (GAN-based) and DiGress (Diffusion-based). Additionally, thorough ablation studies for factors, including  the number of channels, layers, optimization steps, and loss functions, providing some insight into the model's design choices.

### Strengths
1. The approach of training a discriminator without a generator is novel, particularly given its empirical effectiveness in graph tasks. 


2. The authors present a method that achieves competitive performance with traditional GANs and diffusion-based models, offering a compelling alternative in the field. The authors' extensive research across graph and image generation tasks convincingly demonstrates that their method can produce quality samples without a generator, showcasing its efficacy.


3. The method is simple but useful.

### Weaknesses
1. While the authors provide a simple convergence analysis for their generator-free training method, the provided analysis falls short of explaining why removing the generator yields improved results for graph tasks, diminishing the persuasiveness of the approach.

2. Despite the proposed method's ability to operate without a generator, it incurs longer training times. 

3. Table 6 includes ablation studies for several factors, dissecting the influence of steps, channels, layers, and optimizers separately, could yield a clearer, more convincing analysis.

### Questions
Please refer to the weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose a discriminator-only generation (DOG) as a generative modeling approach. The DOG model generates samples through iterative gradient
descent on a discriminator’s input,  which is a commonly utilized technique in the field of adversarial attack research. In the graph domain, DOG demonstrates significant improvements overGANs using the same discriminator architectures.

### Strengths
This article introduces a novel approach by employing a single discriminator model for the generative process. This approach stands out because state-of-the-art generative adversarial networks typically rely on a pair of discriminator and generator models, making the training process time-consuming. Given the recent advancements in discriminator models such as CLIP, DINO, or SAM, utilizing these models as the discriminator to generate high-fidelity data has the potential to significantly advance the field of generative modeling.

### Weaknesses
The approach employed in the paper may appear to lack novelty. This is because the method of accumulating $\nabla_{x}D$ on the data point $x$ is a commonly utilized technique in the field of adversarial attack research. Moreover, in recent studies, certain generative models, such as those mentioned in references [1] and [2] have also adopted this method for tasks related to image generation and latent space editing.

Furthermore, the motivation of the article remains unclear and somewhat confusing. The author's underlying rationale for comparing the DOG method with the EBM approach is not explicitly communicated, making it challenging to discern the purpose of this comparison. Specifically, the paper does not adequately address why the unique characteristics of graph data necessitate a departure from established EBM practices or how DOG offers a distinct advantage in this context. The lack of clarity regarding the theoretical underpinnings of why DOG would outperform EBMs on graph data weakens the paper's overall contribution.

In the "CONVERGENCE ANALYSIS" section, the reference to (Mescheder et al., 2018) is made in the context of using a dynamic system to establish the convergence of the gradient penalty. However, it is not entirely clear how the DOG model is related to this dynamic system. Additionally, there appear to be some mistakes in the convergence proof provided in the appendix.

In the "CONVERGENCE ANALYSIS" section, I remain perplexed by the choice to utilize the convergence of the Energy-Based Model (EBM) for comparison with the DOG model. The paper does not sufficiently justify why EBM convergence analysis is relevant or informative for understanding the behavior of DOG, particularly given the discrete nature of graph data and the potential limitations of EBMs in handling such data structures.

There are several typos present in the article. For instance, in the "Related work" section, "EMB" is likely a typo and should be corrected to "EBM."

The presentation of the ablation study for hyper parameters in Table 6 is not accurate or correct.

Are there any advantages to using the DOG model for graph data? I recommend that the author provide an advanced analysis, especially considering that the fundamental concept of iterative generation using gradients is not entirely novel. A more in-depth exploration of the theoretical advantages of DOG for graph data, potentially supported by a more rigorous mathematical analysis, would be beneficial.

### Questions
1. I would suggest that the author provides additional clarification regarding the motivation behind comparing the EBM model with the DOG model. This clarification would be valuable in improving the comprehensibility of the research and elucidating the rationale for conducting this specific comparison.

2. In the "CONVERGENCE ANALYSIS" section, the reference to (Mescheder et al., 2018) is made in the context of using a dynamic system to establish the convergence of the gradient penalty. However, it is not entirely clear how the DOG model is related to this dynamic system. Additionally, there appear to be some mistakes in the convergence proof provided in the appendix.

3. In the "CONVERGENCE ANALYSIS" section, I remain perplexed by the choice to utilize the convergence of the Energy-Based Model (EBM) for comparison with the DOG model

4. There are several typos present in the article. For instance, in the "Related work" section, "EMB" is likely a typo and should be corrected to "EBM."


5. The presentation of the ablation study for hyper parameters in Table 6 is not accurate or correct

6. Are there any advantages to using the DOG model for graph data?I recommend that the author provide an advanced analysis.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a generative model based on iterative gradient ascent of the discriminator. This generative model avoids the use of a generator during both training and sampling. During training, the discriminator learns from the data it generates itself. Experiments were conducted using both image and graph data. The model exhibits lower performance than standard GANs on image data, but it demonstrates superior performance over standard GANs on graph data.

### Strengths
* The paper is globally well written and structured, very easy to follow. 

* The presented algorithm is clear and makes sense. 

* The proposed generative model shows improved performance over standard GANs on graph data, although not SOTA.

### Weaknesses
 * Overall, the paper has neither strong theoretical results, neither strong experimental results. Moreover, a very similar work is not discussed (see below), which lowers the contribution. Authors should at least discuss the differences with this method.  

* The training process appears to lack a principled approach in the following aspect: there exists a mismatch between training and sampling times, which is typically an undesired characteristic. The discriminator generates samples by applying its gradient 'T' times, but the adversarial loss is only computed and back-propagated during the final step. This appears suboptimal since there is no guarantee that the gradients from the initial timesteps will be useful or provide appropriate guidance. Have there been instances of training runs failing to converge, or with catastrophic forgetting, and have you explored the possibility of learning from intermediate steps as well? The argument presented at the end of the section, suggesting that learning from intermediate steps would lead to memory issues, is not convincing. It is possible to choose to learn from intermediate timesteps with a 'stop-gradient' approach, which would not result in memory issues.

* The paper lacks theoretical justification for their generative model. The convergence analysis on a toy distribution is not sufficiently formalized and is a bit verbose. There is no explicit motivation or rationale provided for the use of their proposed generative model. Furthermore, while the argument regarding the min-max optimization is interesting, it does not clarify why their generative model would be superior in approximating distributions compared to a standard GAN; it primarily elaborates on how their approach might result in a better discriminator.

* Missing important references: 1: Mostly a recent similar work [1]. In this paper, the Discriminator Flow model is very similar to the one proposed by the authors. Discriminator Flow also consists in generating data with only a discriminator, and training the discriminator to distinguish between its own generated samples and training data. In this paper, the discriminator is trained on all intermediate timesteps, with timestep embedding.  2: Tanaka [2] which proposes to refine generated samples with discriminator's gradient. On image data, the updates are applied on the latent vector of the generator rather than directly on the image space. 

### Questions
* In diffusion models, embedding the time step seems to be a crucial component. Have you tried such strategy (i.e. embedding time step in the discriminator) in your model? 

* It would be interesting to have some more analysis on the sampling procedure. For example, visualizations of the samples along the timesteps, at least on image data, or observing the evolution of the gradient's norm along the timesteps, to better understand the generative process.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
