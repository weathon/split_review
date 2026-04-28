# The Optimization Landscape of SGD Across the Feature Learning Strength

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
We consider neural networks (NNs) where the final layer is down-scaled by a fixed hyperparameter $\gamma$. 
Recent work has identified $\gamma$ as controlling the strength of feature learning.
As $\gamma$ increases, network evolution changes from ``lazy'' kernel dynamics to ``rich'' feature-learning dynamics, with a host of associated benefits including improved performance on common tasks.
In this work, we conduct a thorough empirical investigation of the effect of scaling $\gamma$ across a variety of models and datasets in the online training setting.
We first examine the interaction of $\gamma$ with the learning rate $\eta$, identifying several scaling regimes in the $\gamma$-$\eta$ plane which we explain theoretically using a simple model.
We find that the optimal learning rate $\eta^*$ scales non-trivially with $\gamma$. In particular, $\eta^* \propto \gamma^2$ when $\gamma \ll 1$ and $\eta^* \propto \gamma^{2/L}$ when $\gamma \gg 1$ for a feed-forward network of depth $L$.
Using this optimal learning rate scaling, we proceed with an empirical study of the under-explored ``ultra-rich'' $\gamma \gg 1$ regime.
We find that networks in this regime display characteristic loss curves, starting with a long plateau followed by a drop-off, sometimes followed by one or more additional staircase steps.
We find networks of different large $\gamma$ values optimize along similar trajectories up to a reparameterization of time.
We further find that optimal online performance is often found at large $\gamma$ and could be missed if this hyperparameter is not tuned.
Our findings indicate that analytical study of the large-$\gamma$ limit may yield useful insights into the dynamics of representation learning in performant models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the scaling law between $\gamma$, the feature learning strength parameter, and $\eta$, the learning rate, both empirically in a diverse set of data (MNIST, CIFAR, TinyImageNet) and model architectures (MLPs, CNNs, Vision-Transformers), and theoretically in simple setting with deep linear network. They observed a characteristic phase portrait in the $\gamma-\eta$ plane, and showed that the learning rate scales as $\eta \sim \gamma^2$ in the lazy regime ($\gamma << 1$) and $\eta \sim \gamma^{2/L}$ in the rich regime ($\gamma >> 1$). They confirmed this phase portrait empirically by sweeping over every pair of $\gamma, \eta$ in a log-spaced grid running from $\gamma = 10^{-5}$ to $10^5$ and analytically by theoretically analyzing a deep linear network models for both MSE loss and cross-entropy loss. They also observed and reported various dynamical phenomenon such as "catapult effect", "silent alignment", and "progressive sharpening".

### Strengths
The paper provides extensive empirical study for the scaling law of $\eta$ (learning rate) and $\gamma$ (feature learning strength), and also provided an analytical explanation using deep linear network that matches with the empirical results.

**Originality**
1. The paper investigates the scaling relationship between feature learning strength $\gamma$ and learning rate $\eta$ in both lazy, rich, and ultra-rich regime. To my knowledge, I haven't seen work that extensively address this topic.

**Quality**
1. Empirical study: The paper provided an extensive empirical study across $\gamma$ and $\eta$ plane, ranging from $\gamma = 10^{-5}$ to $10^5$ and $\eta = 10^{12}$ to $10^{-12}$ with a diverse set of dataset (MNIST, CIFAR, TinyImageNet) and model architectures (MLP, CNN, Vision Transformer), and confirmed that the claimed scaling laws are observed across different datasets and models.
2. Theoretical analysis: In a simple settings (deep linear network), the paper derived the $\gamma-\eta$ scaling law for both MSE and cross-entropy loss, and showed that the theoretical results match with the empirical observations. The authors also produced an analytical phase portraits in Fig 6 that match with the empirical phase portraits from parameters sweeping.
3. Analysis of dynamical phenomenon: The paper also reported various learning dynamic phenomenon that was reported in earlier works, including catapult effect, silent alignment, step-wise loss drops, progressive sharpening, in various $\gamma-\eta$ region that they perform the  parameter sweeping.

**Significance**
1. The paper showed the scaling relationship between feature learning strength $\gamma$ and learning rate $\eta$ in both lazy, rich, and ultra-rich regime. This scaling law enables the authors to find the range of possible learning rate to train models in ultra-rich regime, an area that few previous work touched on. Using the suitable learning rate, the authors show that in models trained in the ultra-rich regime can exceed or match the performance of models trained in rich regime, which open a potential area to improve current model training dynamics.

### Weaknesses
While the paper addressed a significant topic in the feature learning area and provided reasonable empirical and theoretical results, I think the clarity of the paper still have lots of room for improvement to help the readers have an easier time to read the paper. Specifically, the authors can consider to try to re-organize the paper flow to focus on the key points: Since the key results of the paper is the scaling relationship between feature learning strength $\gamma$ and learning rate $\eta$, the paper can be reorganize so that these key theoretical and empirical results come first and emphasized in the paper, instead of leaving the theoretical results at the end of the paper, and mention many other detailed results in the middle of the paper.

### Questions
**Questions**
1. [L137] Why further downscale by $1/\gamma$? Isn’t the $\mu P$ scaling already scale by a factor of $1/\gamma$?
2. I couldn't find any information in the paper about how many repetition were run for each empirical results? Would appreciate if you can provide some information about this.

**Suggestion**
1. [L068] Key contribution should be clear and emphasizing the key points (usually 3-4 key points). This current key contribution section is too long and difficult to follow. I’d appreciate if the authors can re-organize this section to make the key contribution clearer to the readers.
2. [L068] Hyperlink each key contribution with the section and/or figure that demonstrate the key contribution so that readers have easier time to follow.
3. [L215] Explicitly mention whether this scaling results are for MSE or cross-entropy loss, since they have different scaling. I was quite confused when the author states that “At small $\gamma$, $\eta \sim \gamma^2$ for lazy networks”, but Fig 2d shows that $\eta \sim \gamma$ instead, but later I realized that the claim “At small $\gamma$, $\eta \sim \gamma^2$ for lazy networks” is for MSE, and the authors have another section for cross-entropy loss.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper systematically studies the effect of $\gamma$, which is the scale of the output layer of the neural networks, on the optimization and generalization dynamics of neural networks through experiments. They recovered a couple of phenomena that have been analyzed in the literature, including lazying training, catapult effect, silent alignment, etc. They also observed that the generalization performance is similar when $gamma$ is greater than $1$ if the network is trained sufficiently long. Furthermore, they use a simple deep linear neural network with a single univariate data to explain the optimal learning rate scaling.

### Strengths
1. This paper is well-written and the logic is easy to follow. The experiments are nicely done and the theoretical results are well presented. 

2. There are some interesting empirical observations. For example, they observe that in the feature learning regime i.e., $\gamma \geq 1$, the generalization performance will end up being similar with different $\gamma$, if the learning rate is appropriately chosen. I also find the connection between silent alignment and edge os stability quite interesting and worth further investigation.

### Weaknesses
1. One concern is the significance of this paper. Feature learning is an interesting topic, but I believe that this kind of parameterization is not commonly used in practice, i.e., large $\gamma$ with the model being centered. Furthermore, the learning rate used in this paper is constant hence is far from practice. Therefore, I am not sure if the insights observed in this paper can shed light on practical network training.

2. This paper may provide valuable insights for theoretical analysis. However, many of the phenomena discussed, such as lazy training, the catapult phase, and silent alignment, have already been extensively studied. Although the ultra-rich regime is analyzed in depth, it does not appear particularly interesting, as the generalization performance turns out to be similar to that of $\gamma=1$. All in all, the paper presents a nice summary of the network training dynamics, but I do not find anything particularly new or significant.

### Questions
1. I am curious how do you conclude that the optimal learning rate is $\gamma^{2/L}$ for $L$-th layer neural network? I understand that for the deep linear network with a single univariate sample the optimal one is that value, but I am surprised that for deep nonlinear networks it still holds, and the power is quite specific. Does the generalization performance have a big gap when the learning rate is $3/L$ or $2/(L+1)$?

2. In practice, the learning rate decay is useful to improve the generalization performance, and it may avoid optimization from divergence. Do you think the optimal learning rate will be different if you include learning rate decay?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors conduct a systematic and comprehensive empirical study on the effect of scaling the hyperparameter $\gamma$, located in the final layer, which controls the strength of feature learning, across a variety of datasets and tasks. In this context, a small $\gamma$ corresponds to the kernel regime, while $\gamma = 1$ represents the mean-field regime, where feature learning can still occur even with infinite width. 

First, the authors examine the relationship between $\gamma$ and the maximal learning rate, empirically demonstrating that the maximal learning rate scales nontrivially with $\gamma$. Using this optimal learning rate scaling, they then explore the ultra-rich regime, $\gamma \gg 1$. In this large $\gamma$ regime, the network exhibits consistent training dynamics across different values of $\gamma$. Also, the model always achieves optimal performance when $\gamma$ is sufficiently large.

### Strengths
1. The experiments are conducted systematically, making the results highly convincing. The paper is also well-written and clear.

2. The observation that networks with a larger $\gamma$ can often achieve the same or even better performance than those with $\gamma=1$ after sufficient training time is intriguing. This suggests a potential new technique to improve performance in practice. It's also interesting to see that networks with large $\gamma$ exhibit very similar training dynamics after an appropriate time rescaling.

### Weaknesses
1. I am somewhat unclear on how these results translate to practical applications. While the empirical findings in this paper are robust, the setup does not precisely match real-world scenarios (e.g. the architectures are different). I wonder what insights could be derived if we consider a standard practical setup.

2. I believe the paper would benefit from a more detailed and mathematically formulated introduction to the networks’ structure and parametrization.

### Questions
See the weakness part.

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
The paper empirically studies the relationships among the scaling hyperparameter $\gamma$, learning rate $\eta$ in neural networks, and the overall performance of neural networks.

### Strengths
1. The paper is clearly written and well-organized.
2. The authors conduct a variety of experiments across multiple datasets and network architectures, exploring different combinations of 
$(\gamma,\eta)$. The figures presented are particularly effective in conveying the findings.
3. The optimal scaling of $(\gamma,\eta)$ offers valuable insights for selecting hyperparameters in empirical studies.

### Weaknesses
1. Although the title emphasizes "Feature Learning", the paper does not adequately elaborate on this concept. There is insufficient empirical evidence regarding whether and how feature learning occurs when $\gamma\gg1$. I recommend that the authors provide more detailed results comparing the weights of networks that exhibit feature learning to those that behave according to the NTK regime. Specifically, a more granular analysis of the weight matrices, beyond just the final layer, is needed. For example, examining the singular value decomposition of weight matrices in different layers could reveal more about the nature of learned features under varying $\gamma$ values.
2. The theoretical framework relies on an oversimplified linear model with a constant target. To gain a better understanding of feature learning, I suggest the authors analyze more complex targets, at least simple single-index models such as $f(x)=\langle a, x \rangle^p$. This is crucial because the constant target assumption may not capture the nuances of feature learning in more realistic scenarios. The current model is too simplistic to explain the observed phenomena fully.


### Questions
1. In Figure 4, which illustrates the dynamical phenomena under different $\gamma$ settings, the conditions for 4(a) and 4(b) differ (CCN for CIFAR and MLP for MNIST, respectively). Are there similar saddle point phenomena as observed in 4(b) under the conditions of 4(a), or catapult phenomena like those in 4(a) under the conditions of 4(b)?
2. Are there differences in the weights of the first few layers under various $(\gamma,\eta)$ combinations, in addition to the weights of the final layer shown in Figure 5?
3. What are the implications of this work on representation learning?

### Soundness
3

### Presentation
3

### Contribution
2
