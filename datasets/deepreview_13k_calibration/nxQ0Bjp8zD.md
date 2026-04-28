# Provable In-context Learning for Mixture of Linear Regressions using Transformers

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5, 5

## Abstract
We theoretically investigate the in-context learning capabilities of transformers in the context of learning mixtures of linear regression models. For the case of two mixtures, we demonstrate the existence of transformers that can achieve an accuracy, relative to the oracle predictor, of order $\mathcal{\tilde{O}}((d/n)^{1/4})$ in the low signal-to-noise ratio (SNR) regime and $\mathcal{\tilde{O}}(\sqrt{d/n})$ in the high SNR regime, where $n$ is the length of the prompt, and $d$ is the dimension of the problem. Additionally, we derive in-context excess risk bounds of order $\mathcal{O}(L/\sqrt{B})$, where $B$ denotes the number of (training) prompts, and $L$ represents the number of attention layers. The order of $L$ depends on whether the SNR is low or high. In the high SNR regime, we extend the results to $K$-component mixture models for finite $K$. Extensive simulations also highlight the advantages of transformers for this task, outperforming other baselines such as the Expectation-Maximization algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper considers the problem of training Transformers to in-context learn mixtures of linear regressions models. The main result shows that Transformers of appropriate size can encode EM algorithm to solve the task with mixture containing 2 components, with error and size of Transformer depending on the signal to noise ratio (analogous result for more than two components is also showning the high signal to noise ratio regime). Additionally, excess risk bounds as a function number of training examples are also shown, adapting the analysis from Bai et. al..  Finally, the paper also has simulation studies showing that Transformers are indeed able to learn mixture of linear regression models, with error depending on various factors such as signal to noise ratio, number of in-context examples, number of mixture components and dimension.

### Strengths
The theory in the paper is thorough, showing how Transformers can encode the EM algorithm, capturing the role of various factors such as the signal to noise ratio and the number of layers.

The paper is written well and mostly easy to follow.

### Weaknesses
The main concern is regarding the significance of the results. The main contribution of the paper is in showing that the Transformers can encode the EM algorithm. However, such representability results do not shed light on what algorithmic mechanism Transformers actually learn, which is arguably the more interesting question.  Moreover, representability results can be misleading. For example, while numerous works showed that Transformers can encode gradient descent for solving linear regression in-context, recent work shows that the algorithm learned by Transformers demonstrate error convergence rate (as a function of number of layers) similar to second-order iterative methods, which is exponentially faster than first order methods like gradient descent.

### Questions
The setting considered for mixture of two regression models seems a bit unnatural, as the two mixture weights are assumed to be w and -w with equal probability. In this case, the mean squared error is minimized by just predicting 0 as the output. How important is this choice of mixture weights for the construction?

Also, the abstract suggests that trained Transformers beat the EM algorithm, but in the simulations section, I couldn't find any plots showing the performance of EM. Did I miss something?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies ICL in transformers for a mixture of linear regressions. They study a transformer with ReLU activation and show that it can implement a gradient EM algorithm, with bounds on the number of layers needed to do so. Based on this construction, the transformer inherits the statistical guarantees of the EM algorithm for ICL, and in particular find that this particular transformer performs better in a high SNR setting. Finally, they analyze a pretraining scheme based on ERM for ICL instances, deriving a generalization bound based on the number of ICL examples that the transformer is pretrained on. Finally, they perform numerical simulations to corroborate their theoretical results.

### Strengths
1. Prior work by Pathak et al.'24 shows that transformers can implement the posterior mean estimator, given access to the $K$ different regression weights in the mixture. This work instead shows that transformers can implement EM, which do not require access to the true regression weights. 
2. This work also gives statistical guarantees for a simple pretraining setting. 
3. In Section 4, the work generalizes the result to mixtures with more than 2 components. 
4. The EM analysis generalizes prior work of Balakrishnan et al.’17 to allow for multiple steps of gradient ascent for EM.

### Weaknesses
1. To further justify why the EM construction is interesting (without analyzing transformer training dynamics), it would be nice if the authors gave some argument (either based on experiments or previous work) suggesting that a transformer does implement an EM-type algorithm. 
2. As pointed out in the paper, the current experiments which train the transformer using the pretraining scheme from Section 2.3 suggest that the transformer does *not* learn to implement EM, as it doesn’t suffer from the same initialization issues as EM. 
3. The requirement on the prompt length $n$ being larger than $d$ in Theorem 2.1 seems somewhat limiting, could the authors comment on what might happen in the overparameterized regime where $n \ll d$?
4. Most of the theoretical contributions appear to be somewhat derivative, mostly using prior results from Pathak et al.'24 and Bai et al.'24.

### Questions
1. It might help to cut down on redundancy in the writing if you omit “of the order” before stating the big-O behavior of a function
2. I found the notation $f_{n,d,\delta}(\cdots)$ to be very hard to parse. I think it would be easier to interpret if you just wrote out the explicit functions. For example, it is hard for me to tell what is going on Theorem 2.2. 
3. There is a slight misuse of the big-O notation. In particular, it doesn’t make sense to have $f \ge O(g)$, you probably meant $f \ge \Omega(g)$ instead? (e.g., in the statement of Theorem 2.1)
4. In Section 5, please specify that you are using the training routine described in Section 2.3. 
5. Minor suggestion: in line 215, write the number of layers required for the low SNR regime $O(\sqrt{n/d}\log\log(n/d))$ to make it obvious that this is in fact exponentially larger than the high SNR regime.
6. Line 215, is this actually just showing an upper bound on the number of layers, or is there a true separation here?
7. Can you add a reference to the proofs for the main theorems (Appendix C for Theorem 2.3, Appendix D for the proof of Theorem 4.1)?
8. Appendix B should not be renamed, as it also contains the proof of Theorem 2.2
9. Line 509, should it say $D = 32, 64, 128$ (instead of 34)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors demonstrate the existence of a transformer architecture provably that can learn a realizable mixture of linear regression models - the authors support their theoretical findings with simulations wherein improvement over baselines such as EM algorithm is demonstrated.

### Strengths
The problem that is tackled is interesting. Given that the transformer architecture is a complicated blackbox, theoretical results demonstrating that transformers have the capabilities of modeling well-studied functions in literature is very important. The authors provide theoretical guarantees for the transformer architecture in different noise regimes - indeed, the results are impressive.

### Weaknesses
As a reader, I have several doubts and questions - most of them are minor but answers would help my understanding. 

1) In the first contribution bullet point, what is meant by oracle predictor? It is not defined in the preceding text.
2) A 2-component mixture implies that for a new datapoints, 2 responses are possible in expectation conditioned on the regressor. However, the transformer output can only provide 1 response via greedy sampling - how are 2 responses collected from the output of the transformer during prediction? I understand what is happening but an algorithm box is important. 
3) Can you elaborate on what is meant by "transformers are capable of implementing double loop algorithms such as EM algorithms"? Again I think an algorithm box should answer this.
4) In eq. 3, what is y_i'? Where is the prime coming from? How is y'_{n+1} set?
5) I have a fundamental question - It seems like the authors are not going only after parameter estimation - usually pursued in mixtures literature - but also prediction error. How is it even possible to bound the prediction error unless we know the regressor? Unless something like a min-loss is defined, bounding the MSE in L172-L174 looks fishy. Please decompose the MSE conditioned on the beta's - note that the function f is producing only a single value. If the magnitude of beta increases, then it is impossible to bound MSE in this context. 
6) The function read_{\beta} is defined in theorem statement - please provide definition prior to theorem statement. beta is a vector - however in Theorem 2.2, read_y() is used where y is a scalar. This is confusing. 
7) Theorem 2.1 does not mention the number of layers in the architecture (along with other details) - How is the FFN layer constructed? Details of the architecture given the dimension of the MoLR problem is critical in understanding.

### Questions
Please see above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proved that there exist transformers that are capable of learning mixtures of linear regression models by mimicking Expectation-Maximization algorithm. The authors analyzed the excess risk bound and the sample complexity for their constructed transformer for learning mixture of two linear regression models. Moreover, they also conducted experiments showing the effectiveness of transformers for this task.

### Strengths
(1) This paper showed that constructed transformers are capable of learning mixtures of linear regression models by mimicking Expectation-Maximization algorithms. While previous works [1] only proved that constructed transformers can implement oracle Bayes optimal predictor.

(2) This paper also derives convergence results with statistical guarantees for the gradient EM algorithm where the M-step involves T steps of gradient ascent, improving upon previous works [2] that considered only a single step of gradient ascent.

[1] R. Pathak, R. Sen, W. Kong, and A. Das. Transformers can optimally learn regression mixture models. In The Twelfth International Conference on Learning Representations, 2024.

[2] S. Balakrishnan, M. J. Wainwright, and B. Yu. Statistical guarantees for the EM algorithm: From population to sample-based analysis. The Annals of Statistics, 45(1):77–120, 2017.

### Weaknesses
(1): The authors claimed that simulation results showed transformers outperformed the EM algorithm in abstract. However, I did not find those experiments in this paper. Moreover, if the transformers, as the authors claimed, mimic EM algorithm to learn mixtures of linear regression models, then how and why could transformers outperform the EM algorithm?

(2): For the mixture of two linear regression model problems, the authors set $\pi_1=\pi_2=1/2, \beta_1=-\beta_2$. Thus, in Theorem 2.1, the $\beta^{OP}=0$, the optimal prediction of the transformer is $x^T_{n+1}\beta^{OP}=0$. The optimal prediction is always 0 and has no relevance to $x_{n+1}$. I think this is not a good setting for analyzing. Could the author analyze the problem in a more general setting?

(3): The authors only showed the existence of specifically constructed transformers that can mimic EM algorithm to learn mixtures of linear regression models. How transformers in reality can be trained to these parameters is not discussed.

(4): The main component of this paper "transformers can perform multiple gradient ascent steps during each M-step of the EM algorithm" is based on the well-established results in [3], which, to some extent, reduces the contribution and the novelty of this paper.

[3] Yu Bai, Fan Chen, Huan Wang, Caiming Xiong, and Song Mei. Transformers as statisticians: Provable in-context learning with in-context algorithm selection. Advances in neural information processing systems, 36, 2024.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper researches the in-context learning ability of the transformers to learn the mixture of linear regression problems. The classical approach is the EM algorithm, and the idea of this paper is to show that the transformers have the ability to implement the E and M steps respectively.

### Strengths
The paper is theoretically solid. It provides interesting insights into the underlying dynamic of in-context learning.

### Weaknesses
The scope of the paper is a bit limited. It only provides understanding of the in-context learning ability in a quite specific setup. Also, the writing of this paper is not sound enough: it does not provide a clear formulation of the problem setup and the workflow of the EM algorithm. The theorems and lemmas lack intuitions.

### Questions
Existing works on in-context learning have shown that transformers can learn the Bayes-optimal solution. How does this paper differ from the previous results?

### Soundness
3

### Presentation
2

### Contribution
2
