# MCNC: Manifold-Constrained Reparameterization for Neural Compression

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The outstanding performance of large foundational models across diverse tasks, from computer vision to speech and natural language processing, has significantly increased their demand. However, storing and transmitting these models poses significant challenges due to their massive size (e.g., 750GB for Llama 3.1 405B). Recent literature has focused on compressing the original weights or reducing the number of parameters required for fine-tuning these models. These compression methods generally constrain the parameter space, for example, through low-rank reparametrization (e.g., LoRA), pruning, or quantization (e.g., QLoRA) during or after the model training. In this paper, we present a novel model compression method, which we term Manifold-Constrained Neural Compression (MCNC). This method constrains the parameter space to low-dimensional pre-defined and frozen nonlinear manifolds, which effectively cover this space. Given the prevalence of good solutions in over-parameterized deep neural networks, we show that by constraining the parameter space to our proposed manifold, we can identify high-quality solutions while achieving unprecedented compression rates across a wide variety of tasks and architectures. Through extensive experiments in computer vision and natural language processing tasks, we demonstrate that our method significantly outperforms state-of-the-art baselines in terms of compression, accuracy, and/or model reconstruction time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed a new approach to compress deep neural networks. The basic idea is to enforce the DNN parameters to lie on a k-dimension manifold for every chunk of d parameters where k << d. The proposed approach uses a generator model that maps a low-dimensional uniform distribution (k-dimension) to a high-dimensional uniform distribution (d-dimension). Evaluations on computer vision and NLP tasks demonstrate that the proposed approaches can achieve extremely high compression rates.

### Strengths
+ The proposed algorithm outperforms baselines in the high compression rate regions
+ The idea is interesting and shows that there exists a set of parameters in a DNN that lies in the lower-dimension manifold.  
+ Evaluations are thorough

### Weaknesses
The paper presents an interesting idea of compressing neural network parameters into a low dimension manifold. Instead of training a generator to produce the neural network parameters, the proposed approach can use a randomly-initialized generator to project a trainable k-dimension vector into a d-dimension vector as parameters. I find the idea very interesting. The empirical results also demonstrate that the approach can achieve better accuracy under extreme compression rates.

With that said, here are a few concerns on the work
- The benefits of achieving extreme compression rates under the high accuracy loss are not clear to me. Using table 1's result as an example, with 1% percentage of model size, the proposed approach can achieve an accuracy of 49% compared to the baselines which are 33%-39% on ViT-Ti model. However, compared to the baseline model accuracy 76.2%, it is a huge accuracy drop (more than 20%). Under this context, one might consider using a different model variant that is smaller but achieves a higher accuracy than compressing the ViT-Ti model.  Although the proposed method can achieve better accuracy compared to baselines under high compression rates, I am concerned about how likely such advantages would be useful in practice due to the significant accuracy drop compared to the non-compressed or lightly-compressed model.

- Table 4 highlights the same concern. The trainable parameters from the LoRA model are already minimal compared to the number of parameters in the LLaMA-2 7B and 13B. With the quantization from NOLA and MCNC, both of them slow down the training throughput of the model. I agree with the advantages of MCNC compared to NOLA, but neither approaches are appealing compared to running the original LoRA method.

### Questions
Can the author clarify how does the benefit of the proposed approach over baselines translate to practical computational performance gains?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new approach to parametrize the network parameters: via another generator model. Specifically, weights are split into blocks(vectors) of size $d$ (i.e., $\mathbb{R}^d$) and parametrized to be coming from a $k$-dimensional space ($\mathbb{R}^k$) via mapping $\phi: \mathbb{R}^k \to \mathbb{R}^d $. The mapping $\phi$ is defined as a compact feed-forward neural network with sine activation with number of layers and hidden dimensions being hyper-parameters of choice; though for most experiments there are not more 3 layers with hidden dimensions of not more 1024. The mapping $\phi$ is randomly initialized, and fixed. The only trainable parameters are the actual inputs to the $\phi$, i.e., the inverted image of parameters in this lower-dimensional space. The authors demonstrate that such a simple setup allows to train from scratch and finetune various models in parameter efficient way.

### Strengths
The paper presents very simple yet powerful idea of essentially hashing high-dimensional weights into lower-dimensional manifold. Instead of hashing directly from higher to lower dimension, the proposed approach fixes the inverts of the hashing function (i.e., generator), and learns the "hashed" outputs via sgd. This idea has deep roots in random projections/random hashing literature, and as such I am very glad that similar approach can be exploited for the parameter efficient training of the neural networks.

### Weaknesses
Overall, I think the paper does a good job in validating the soundness and effectiveness of the proposed approach, however, I think it can be significantly strengthened:
1. In the exposition of the idea, the actual architecture of the generator network comes very late; with actual numbers/settings coming in appendix! I think, the simplicity of the approach must be showcased from the beginning, I highly suggest to add simple pytorch code showing how easy is to plug and play with the method
2. Similar to the previous weakness, I think authors should consider recommending some bulletproof settings that would work for most of the cases (like number of layer in $\phi$, number of dimensions, some rules of thumb, how long to train, optimizer settings) to easy any potential adoption: at the end of the day, the ideas have very limited impact if not used in practice. 
3. Theoretical guarantees of any sorts would be welcome as well: how universal is such a generator network? can it be used to train/finetune any neural network or it has limitations? Specifically, it is unclear what is the expressive power of the proposed parameterization, and whether it can approximate any weight matrix given enough capacity of the generator network. Moreover, it is unclear how the choice of the generator architecture affects the optimization landscape and the convergence properties.
4. While the papers literature review is extensive, I think the connection to hashing must be explored in depth and more papers included into review (some suggestions: Structured Multi-Hashing for Model Compression,  Lossy weight encoding for deep neural network compression)

### Questions
Please address weaknesses above.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a reparameterization to train neural networks which leads to a lower memory footprint for transferring and storing the parameters. The paper achieves this by re-parameterizing the network parameters to lie on a lower dimensional spherical manifold. The method uses a “generator” network for this, mapping k-dimensional vectors onto a d-dimensional sphere. The k-dimensional vectors are then trained. The paper compares this method against multiple model compression and efficient training methods, demonstrating performance gains.

### Strengths
1. Strong empirical results, with comparisons against other compression methods on various modalities and architectures demonstrating the proposed method’s effectiveness.
2. Extensive ablation studies for each component of the method, as well as for choices of hyper-parameters, giving some intuition on how 
3. Demonstration of real world speedups

### Weaknesses
1. My main gripe with the paper is that the method is not very well motivated. For example, the paper claims that a randomly initialized generator is enough to span the entire space of weights in a higher dimension, but never shows much empirical evidence beyond an experiment in low dimensions. It is not clear if this result also holds in higher dimensions. I would have ideally liked to see a theoretical result around the expressivity of the manifold constrained reparametrization, but even an empirical investigation showing that one does not lose out on expressivity would be great. Specifically, the paper lacks a rigorous analysis of how the generator's architecture and initialization affect the reachable subspace of the original parameter space. The claim that a random generator is sufficient needs more justification, especially considering the non-linear nature of neural network weight spaces. The paper should explore the impact of different generator architectures and initialization schemes on the final performance of the model. Furthermore, the paper does not discuss the potential for the generator to introduce biases or limitations on the expressivity of the reparameterized network. 
2. Continuing on my previous point, from table 10, it appears that a trained generator is better for larger models. However, this result is down-played in the text description, with the narrative claiming that the improvement is "marginal". The paper should provide a more detailed analysis of the trade-offs between using a trained versus a randomly initialized generator, especially in the context of larger models. The claim that the improvement is marginal is not sufficiently supported by the data, and the paper should explore the reasons why a trained generator might be more beneficial for larger models. It is important to understand if the performance gains with a trained generator are consistent across different model sizes and architectures, and if there are specific scenarios where a trained generator is essential for achieving optimal performance.

### Questions
1. How was the wasserstein distance computed for Fig 2? If I understand correctly, there is no closed form expression to compute this metric in higher dimensions. 
2. Why does ViT-S have better accuracy for smaller models in Tab 1? Is it an artifact of high variance in the results?
3. How were reconstruction GFLOPs computed for Table 4?
4. How much slower is training MCNC as compared to baseline LoRA?

### Soundness
3

### Presentation
2

### Contribution
3
