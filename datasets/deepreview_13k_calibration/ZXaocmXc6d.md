# From Lazy to Rich: Exact Learning Dynamics in Deep Linear Networks

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Biological and artificial neural networks develop internal representations that enable them to perform complex tasks. In artificial networks, the effectiveness of these models relies on their ability to build task specific representation, a process influenced by interactions among datasets, architectures, initialization strategies, and optimization algorithms. Prior studies highlight that different initializations can place networks in either a \emph{lazy} regime, where representations remain static, or a \emph{rich/feature learning} regime, where representations evolve dynamically. Here, we examine how initialization influences learning dynamics in deep linear neural networks, deriving exact solutions for \emph{‘$\lambda$-balanced’} initializations—defined by the relative scale of weights across layers. These solutions capture the evolution of representations and the Neural Tangent Kernel across the spectrum from the \emph{rich} to the \emph{lazy} regimes. Our findings deepen the theoretical understanding of the impact of weight initialization on learning regimes, with implications for continual learning, reversal learning, and transfer learning, relevant to both neuroscience and practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper theoretically derived the exact solutions for the learning dynamic of $\lambda$-balanced initializations in two-layer linear networks and discussed the implications in continual learning etc.

### Strengths
Originality: The paper built on top of existing work by extending from zero-balanced condition into $\lambda$-balanced scenarios, leading to a continuum from lazy to rich regime in terms of weight structure of two consecutive layers. 

Quality: Solid theoretical derivations backed with rich simulation results. 

Clarity: The paper is very well-written. 

Significance: The $\lambda$-balanced discussed in the paper covers from architecture shapes to initialization schemes and relate these structural properties to the learning regimes, which will be of interest to the neuroscience community as well as continual learning and beyond communities.

### Weaknesses
The only weakness of the paper is on the weak demonstration of applications.

### Questions
a. Could the authors comment on how they would expect the results to generalize to more complex tasks?

b. Although it is mentioned some choice of $\lambda$ may be beneficial to transfer learning due to induced lazy learning in the shallow layer (D3), it would be at least better to show a performance increase.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work extends previous results on the exact dynamics of deep linear networks to include the lambda-balanced initialization conditions, where lambda is a tunable parameter that allows for exploration of a full range of dynamics from lazy to rich learning. By detailed analysis of the result, the authors showed that the transition from the lazy regime to the rich regime depends on the complex interaction of multiple factors, including the balance parameter lambda and the network architecture. This paper then also discusses potential application of the results on more complicated learning paradigms such as continual learning, reversal learning and transfer learning.

### Strengths
1.	The paper is very well structured and the theoretical results are clearly written. 
2.	It is a novel and interesting idea to model the range of dynamics from lazy to rich with the balance parameter \lambda. 
3.	The authors analyzed their theoretical results on interesting semantic task examples, and showed multiple implications of their theory on other learning paradigms.

### Weaknesses
1.	The technical and theoretical novelty of this work is limited, the method used in this paper has mostly been established in Braun et. al. 2022, this work extends to the \lambda-balanced case, which is more general. However, the extension is achieved by enforcing a stricter assumption that the input is whitened, limiting the applicability of the results. 
2.	This paper makes several very strong assumptions such as task-aligned initialization, whitened inputs, linear networks, etc. It would be nice if the authors can show even some empirical evidence that these assumptions may be somewhat relaxed while the main results still qualitatively hold. 
3.	The applications are only briefly discussed. I think the paper would benefit from making the theoretical results in section 4 more concise and moving some of the application results (transfer learning for example I think is very interesting) to main text.

### Questions
1.	A minor point: over-parameterization is commonly referring to the relation between the amount of parameters in the network (capacity of the network) vs. the amount of parameters needed to achieve zero training loss. I believe this may be different from ‘N_h > min(N_i, N_o)’?
2.	The assumption that the input data is whitened is relatively strong and not very applicable to realistic settings. Do you have any empirical evidence demonstrating that your observation at least qualitatively still holds for benchmark datasets without necessarily whitening the data?
3.	This may be just a typo. In Fig.2 b, in the caption it says lambda=0.001 but in the figure lambda=0.
4.	In previous works concerning lazy and rich dynamics, especially in infinitely wide networks, there’s usually the assumption that N goes to infinity and depending on how initialization scales with N the network resides in either the lazy or the rich regime. Here there doesn’t seem to be any assumptions about large N or the scaling of the initialization. Specifically since Nh=min(Ni, No), it seems that N is finite. However, it seems that the authors are able to get fixed NTK in the lazy regime without the assumption of large N in section 5. Is this specific to the linear network? Can you comment on how your results may scale to larger dimensional networks, and on the relation of your results and the lazy and rich regimes in the infinite width limit? 
5.	In Fig.4 b the simulation w1w1 and w2w2 labels seem to be reversed compared to the theory. 
6.	In Fig.5, how does the ratio between Nh and Ni (or Nh and No) play a role here?

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
4

### Summary
This study derives exact solutions (Theorem 4.3) to examine how initialization --- particularly the relative scale of weights across layers --- influences rich versus lazy learning in linear feedforward neural networks. The study relaxes several assumptions from prior work, notably the balanced assumption in Braun et al., which is a special case in here when $\lambda=0$. Extending this, the authors show in Theorem C.4 that the network transitions into a rich regime as $\lambda$ approaches 0, and into a lazy regime as $\lambda$ approaches infinity. Overall, this work significantly contributes to the ongoing investigation into how various network parameters influence rich versus lazy learning regimes, with demonstrated relevance to both neuroscience and deep learning.

### Strengths
•	This work is novel and timely.

•	Strong theoretical foundation: the approach extends a previous theoretical framework (Braun et al., 2022) to derive exact solutions for NTK, representation similarity, gradient flow, and loss. This allows for precise determination of how initialization (specifically, the $\lambda$ parameter) influences representation and learning dynamics under the given assumptions. However, I did not have the bandwidth to verify the proofs in the appendix, which affects my confidence score.

•	Insightful experiments demonstrating how $\lambda$ interpolates between learning regimes, with applications to both neuroscience and machine learning.

•	The manuscript is well-written, with a comprehensive literature review.

### Weaknesses
•	This work relies on a list of assumptions and focuses on a simple two-layer linear feedforward network, which deviates from real-world settings. However, this didn’t significantly impact my score, as the assumptions are already more relaxed compared to previous works, and the authors have adequately addressed these limitations in the discussion.

•	I wish there were more intuitive explanations of how \(\lambda\) interpolates between learning regimes. The authors provide some results in this direction, such as Theorem 5.1, which shows that under different limits of \(\lambda\), the transition function converges to sigmoidal (\(\lambda \to 0\)) and exponential (\(\lambda \to \pm \infty\)). However, it would be helpful to have more insight into how the limit of \(\lambda \to \pm \infty\) leads to a task-agnostic identity representation. Specifically, while the authors show convergence to these regimes, the underlying mechanism for how the relative scaling parameter \(\lambda\) enforces this behavior is not entirely clear. The connection between the mathematical limits and the resulting representational properties requires further elaboration.

•	I’m not sure if I have a good understanding of how the relative and absolute scales interact. While the authors demonstrated that in the extreme case where \(\lambda \to 0\), the rich regime occurs regardless of the absolute scale, I’m less certain about the case where \(\lambda \to \infty\), as the weight norm of one of the layers would presumably become very large. Large initialization can lead to lazy learning, so I’m unsure if it’s possible to decouple the contributions of \(\lambda\)-balanced initialization from large weight initialization. I believe some control experiments with large \(\lambda\) values using random (unbalanced) initialization but with the same \(W_1\) and \(W_2\) norms as the balanced case would help distinguish the two. It's unclear whether the observed lazy regime for large \(\lambda\) is due to the balancing constraint or the large magnitude of the weights.

### Questions
•	It would be interesting to understand more how this relative scale interact with other knobs that impact learning regimes. For instance, could you provide more discussion on how the relative scale and absolute scale of the weights interact? See the weakness point above. 

•	Could you offer more intuition on how \(\lambda \to \infty\) results in an identity representation (i.e., a task-agnostic representation)?

### Soundness
4

### Presentation
3

### Contribution
3
