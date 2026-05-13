# A Theoretical Perspective: When and How Self-consuming Training Loops Generalize

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
High-quality data is essential for training large generative models, yet the vast reservoir of real data available online has become nearly depleted. Consequently, models increasingly generate their own data for further training, forming Self-consuming Training Loops (STLs). However, the empirical results have been strikingly inconsistent: some models degrade or even collapse, while others successfully avoid these failures, leaving a significant gap in theoretical understanding to explain this discrepancy. This paper introduces the intriguing notion of *recursive stability* and presents the first theoretical generalization analysis, revealing how both model architecture and the proportion between real and synthetic data influence the success of STLs. We further extend this analysis to transformers in in-context learning, showing that even a constant-sized proportion of real data ensures convergence, while also providing insights into optimal synthetic data sizing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper theoretically studies Self-consuming Training Loops (STLs), where generative models generate their own training data. The key concept that the paper introduces is the recursive stability which the authors prove to be vital for generalization and for avoiding model collapse. After the general result on how the recursive stability is important, the authors move to provide an upper bound for the recursive ability for transformers. The theoretical results suggest a trade-off of synthetic data augmentation.

### Strengths
* The paper introduces a concept called recursive stability that addresses the complexity and difficulty of self-consuming training loops. It can be used to derive an upper bound on the generalization error of learning algorithms trained on the self generated (mixture of self-generated and real) dataset after any iterations of the self-consuming loop.

* The application to transformers is nice to have as it bridges to the most popular architecture in practice.

### Weaknesses
 *  The reviewer is concerned about the validity of this recursive stability which is supposed to be the core contribution of this paper. Details follow. The recursive stability $\gamma^i_n$ is a rather strong assumption, and it hides a lot of things underneath. For example, it is uniform not only in terms of the data point modification, but also uniform w.r.t. to any randomness in the STL process. It also depends on how the STL is performed, e.g., the ratio $\alpha$ of the data mixture. The paper derives an upper-bound on the  recursive stability $\gamma^i_n$ for transformer in Theorem 2 but the bound has an exponential factor $e^{B_WL}$ where $B_W$ is the bound on the norm of weights and $L$ is the depth. So it appears that $\alpha$ is required to be very close to $1$, i.e., almost only using real data, for the guarantee on model collapse to stand.
* Following up on the above concern, it is not really satisfying to see the paper jumps directly to the application to transformers in-context learning which is notoriously difficult to make the theory accurate. Why not apply the recursive stability and Theorem 1 to simple cases first, e.g., Gaussian models, where everything can be made accurate, to examine if the proposed recursive is indeed a valid property to look at? This means to examine the LHS and RHS of Theorem 1 accurately for simple cases and show that the bound is not vacuous.

### Questions
see the questions in the above section.

### Soundness
2

### Presentation
2

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
This paper theoretically examines the properties of self-training loops in training generative models. This is an area fo great interest and relatively limited theoretical analysis in current research. This paper aims to prove generalization bounds for self-consuming training loops. As they note, this can be difficult due to the distribution shift across training iterations, as well as the non-i.i.d nature of synthetic-real mixed training datasets. To address the challenge, this paper proposes a novel theoretical notion of recursive algorithmic stability, which allows for controlling the propagation of error across training generations. Leveraging this new theoretical concept, this paper proves a generalization bound. They show that this generalization bound resembles existing qualitative and empirical trends observed in the use of synthetic data. For example, the necessary role of including an appropriate proportion of real data. In addition to their general, model-independent results, this paper also studies the relevant problem of in-context learning in transformers. They provide a bound of the recursive stability of transformers on this task and demonstrate that a constant fraction of real data is sufficient to maintain stability. They additionally remark on the conflicting role played by self-consuming data: it increases the distribution shift in the training loop while decreasing the generalization error component of each step.

### Strengths
Overall, I am very supportive of this paper. Self-consuming data loops are currently an important topic in practical foundation model settings --both intentionally from the point of view of synthetic data and unintentionally from the point of view of leakage of model-generated content on the internet. While some existing works have theoretically demonstrated that self-generated data can lead to model collapse, as a practical matter self-generated data can often be leveraged in harmless or beneficial ways -- albeit without theoretical justification. This paper thus makes a significant contribution to placing the role of model-generated data on a more solid theoretical footing. They convincingly isolate some central technical challenges in understanding self-consuming training loops and propose an elegant and intuitive concept of recursive algorithmic stability to confront these challenges. This enables them to make a *key contribution* of presenting the **first** generalization bound on self-consuming training loops. The analysis of the transformer architecture is additionally interesting and instructive, establishing that their proposed recursive stability criterion holds naturally on realistic architectures and tasks. Throughout the paper, they demonstrate that their theory formalizes and quantifies many previous intuitions or folklore on properties of self-consuming training loops (such as the necessity of maintaining a proportion of real data -- or the benefits of synthetic data primarily arising in low real-data regimes). 

The paper is extremely clearly written. The proof sketch was insightful, yet accessible. Moreover, the authors interleave their technical and theoretical content with real-world motivation and implications. I found the paper quite enjoyable and educational to read.

### Weaknesses
I don't have any serious concerns about this paper. One potential weakness is that the paper primarily focuses on the theoretical angle and  mostly relates their findings to empirical observations in prior work. It could also be interesting if the authors were to add some of their own numerical simulations justifying their findings. Although it is understandable to exclude this, it would be interesting to have some numerical backing in the paper itself. The construction of a simulated setting or dataset would also help in understanding the relationships between the setting studied in this work and real-world setups.

The authors primarily use their theory to explain or justify existing empirical or conceptual observations about self-consuming training loops. However, I feel it would be quite exciting if authors could propose and test (even in simulated settings) some novel predictions made by their theory. Perhaps, this might also be a question of merely highlighting the currently novel predictions made by theory a bit more explicitly.

### Questions
1. Perhaps I missed something but what is the notation $\sum\limits_{z_{i} \in S_{i}, \alpha}$ referring to in line 358?
2. To clarify, in the in-context learning setup, the "synthetic data" inputs are not generated by a model but sampled according to the ground-truth distribution correct? 
3. Follow-up from (2), I wonder if you could comment on the fact that in many "real-world" synthetic data settings both the "input" and "output" components are sampled from the model. For example, when generating instruction/chat tuning datasets, I believe that both instructions and responses are synthetically generated often. How do you believe that would change your analysis? Seemingly, it would make recursive stability worse due to the additional error in the input distribution.

### Soundness
4

### Presentation
4

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
The authors attempt to present a theoretical framework to describe the generalization error of models when they are trained on synthetic data. They are motivated by the observation that multiple workflows presented in the literature on model collapse / self-consuming loops arrive at different conclusions. They introduce the notion of recursive stability, inspired by past notions of algorithmic stability like uniform stability, using which they quantify the propagation of error as model-fitting iterations progress. Finally, using these tools, they perform an analysis of in-context learning in transformers, obtaining generalization error estimates that describe the impact of real data in the model-fitting loop.

### Strengths
Through their notion of recursive stability, the authors have considered a much more general class of algorithms / models than what the prior literature has described. They have been able to go beyond explicit model calculations or estimation strategies. This notion allows them to decompose the generalization error and explicitly attribute each term to a specific statistical reason. Interestingly, the authors are also able to identify, through these upper bounds on the generalization gap, the effect of proportion of real data in the STL.

### Weaknesses
The authors attempt to present a theoretical framework to describe the generalization error of models when they are trained on synthetic data. They are motivated by the observation that multiple workflows presented in the literature on model collapse / self-consuming loops arrive at different conclusions. They introduce the notion of recursive stability, inspired by past notions of algorithmic stability like uniform stability, using which they quantify the propagation of error as model-fitting iterations progress. Finally, using these tools, they perform an analysis of in-context learning in transformers, obtaining generalization error estimates that describe the impact of real data in the model-fitting loop.

The authors have tried to be too general - this has significantly affected the readability of the paper. There are no examples of models provided. What models are recursively stable? How do we know the TV bounds will be of the same order? The paper really needs some examples for clarity. As of now, it is too hard to parse. Understandably it is a math paper, but a lot of what is written needs to be appropriately motivated as the premise addressed by the authors is an important empirical problem (the problem of model collapse) which the authors are tackling theoretically. I would recommend the authors to rethink their presentation for greater impact.

Further, to me the bounds derived are a rather straightforward application of "working with upper bounds" when the correct assumptions are in place. Thus, I feel the technical novelty is limited, and I am not sure if we are learning something substantially new from these upper bounds, than what we already knew about STLs.

Finally, the literature review is a little too crude. The authors should connect their results with those obtained by Gerstgrasser et. al. (2024), Dohmatob et. al. (2024), Alemohammad et. al. (2023), etc. because we know how specific workflows function already, and it is important to clarify that the present authors are not contradicting any existing result.

### Questions
1. In line 195, does $S_0'$ depend on $j$ or not? (the previous sentence suggests it does) If it does, then the provided formula doesn't make sense.

2. With regards to equation 1, let's consider $\alpha=0$ i.e. no real data is used. What is the behavior of the error gap? It seems to me that only the last term will matter and using the fact that $\lim_{\alpha\to0} (1 - (1-\alpha)^i)/\alpha = i$, this predicts a linear rate of increase of the generalization gap. Is this correct?

3. Following the point I make in 2 above, it seems to me that the discussion in lines 257-260 needs to change, because when $\alpha$ is too small, yes $\alpha^{-1}$ gets large but it's multiplied by $1-(1-\alpha)^i$ which is small too. They balance each other out exactly giving $i$.

4. I don't understand the final conclusion of Theorem 4. There are too many terms - which one matters the most? Gerstgrasser et. al. (2024), Marchi et. al. (2024) and Seddik et. al. (2024) have shown that the gap is like $\sum_i 1/i^2$, which is kind of similar to the second term in the upper bound, but it has $n^{-1}$ in front which makes me think that this term is a higher order term. The presented bound makes me think that only the first term $O(n^{-1/4})$ matters, but then the rate $\log(i)$ (essentially) seemingly contradicts past findings. I would urge the authors to actually connect this part with the more recent literature on accumulating data for avoiding model collapse.

### Soundness
3

### Presentation
2

### Contribution
2
