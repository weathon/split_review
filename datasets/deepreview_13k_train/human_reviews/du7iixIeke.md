# Clip Body and Tail Separately: High Probability Guarantees for DP-SGD with Heavy Tails

- Decision: Reject
- Scores: 3, 6, 1, 8, 3

## Abstract
Differentially Private Stochastic Gradient Descent (DPSGD) is widely utilized to preserve training data privacy in deep learning, which first clips the gradients to a predefined norm and then injects calibrated noise into the training procedure. Existing DPSGD works typically assume the gradients follow sub-Gaussian distributions and design various clipping mechanisms to optimize training performance. However, recent studies have shown that the gradients in deep learning exhibit a heavy-tail phenomenon, that is, the tails of the gradient have infinite variance, which may lead to excessive clipping loss to the gradients with existing DPSGD mechanisms. To address this problem, we propose a novel approach, Discriminative Clipping~(DC)-DPSGD, with two key designs. First, we introduce a subspace identification technique to distinguish between body and tail gradients. Second, we present a discriminative clipping mechanism that applies different clipping thresholds for body and tail gradients to reduce the clipping loss. Under the non-convex condition, \ourtech{} reduces the empirical gradient norm from {\small ${\mathbb{O}\left(\log^{\max(0,\theta-1)}(T/\delta)\log^{2\theta}(\sqrt{T})\right)}$} to {\small ${\mathbb{O}\left(\log(\sqrt{T})\right)}$} with heavy-tailed index $\theta\geq 1/2$, iterations $T$, and arbitrary probability $\delta$. Extensive experiments on four real-world datasets demonstrate that our approach outperforms three baselines by up to 9.72\% in terms of accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Discriminative Clipping (DC), a novel algorithm for gradient clipping when gradient norms follow a heavy tailed distribution. Current techniques assume the norms follow subgaussian distributions, so these methods can incur in high utility drop for heavier tailed distributions. 

DC identifies the subspace containing the gradients to separate the tail, and after that performs clipping with different thresholds. For a subWeibull distribution, DC reduces empirical risk. Their experiments show improvements up to 10% over baselines.

### Strengths
The paper studies a relevant problem in the privacy and optimization community. Typically, DP-SGD degrades model performance, with respect to the non-private model. This paper proposes an interesting idea of setting two different clipping values. If the distribution of gradients is heavy tailed, then it should help performance by reducing the bias introduced by overclipping.

### Weaknesses
 **Unclear relation to previous work:**
- I read Bu et al. 2024 and could not find “the small gradient assumption”, only the observation that in the range [0.1, 1000], the smaller clipping values worked better when training GPT2 and Imagenet.

**Unclear claims and terminology:**
- Throughout the paper symbols are mixed, undefined, and sentences are ambiguous, making it hard to validate the correctness of theorems and proofs. Specifically, this ambiguity could break the privacy guarantee (e.g. incorrect noise calibration due to undefined noise variables), a fundamental aspect of the paper. Similarly, the description of the algorithm could be made clearer. Below I provide some examples.

  - Comment for Line 35: clipping is performed to bound the maximum divergence rather than “obtaining”.


  - Comment for Line 36: Gradient clipping can introduce bias so the estimation is not unbiased. I am not sure if saying “gradient noise” is appropriate, but rather sampling.

  - Theorem 4.1 does not introduce what “c” is. Is it the clipping value? And the bound does not depend on it so it is unclear why it is introduced. Further, I think  $\delta$ from the privacy guarantee and $\delta$ from the high probability bound share the same symbol? How is the noise defined in this version of DP-SGD? The version in the appendix specifies it,  but still depends on two constants m_1, m_2 that are also not introduced in the theorem statement.

  - Similarly, theorem 5.1. uses constants that have not been defined, specifically q, T, B.

  - Lines 297-299 sketch the proof for the privacy guarantee but it is hard to follow, yet a crucial aspect of the paper: 
    
    “According to the results of trace sorting,…” What results?
    “we apply two clipping thresholds for gradient perturbation, making it essential to reanalyze the unified privacy 
    guarantees of our composition mechanism.” I found this sentence unclear.

  - Section 5.1. is hard to follow due to several unjustified statements.

  - Algorithm 1 and the corresponding adjacent could be more precise (see questions)

**Informal privacy claims**
- Throughout the manuscript the privacy parameters are mixed with high probability bound parameters disrupting the flow of the paper and clarity about statements. Further, it is hard to parse and validate that the privacy claims can be derived given the gaps. The interpretation of the privacy parameter as a high-probability bound parameter corresponds to Probabilistic DP, not approximate DP.

**Experimental setting is not clearly explained**
- Details about the baselines are missing, making it difficult to assess why the proposed method is outperforming all other methods. For example, details on the hyperparameter tuning process for both DC and the baselines are needed for the results on table 1. A short description that allows interpretation of results is necessary. Additional details can be left to the appendix.

**Minor:** 
- Some citations are missing parenthesis. 
- I would recommend introducing the definition of heavy tailed index earlier in the introduction. 
- Section 3.1 has several typos
- What do the authors mean by “private batch size” in the input of algorithm 1?

### Questions
1. How can one verify in practice if one or two thresholds should be used?

2. Section 5.1. Introduces subspace identification. The authors mention the similarity between gradients and a subspace. How is this similarity defined? 

3. Can the authors clarify this sentence? “Due to the high-dimensional nature of gradients, their normalized versions act as mutually orthogonal eigenvectors”. Are the authors claiming that  all gradients are orthogonal? Or that body and tail gradients are orthogonal? What is the intuition behind this? 

4. On Algorithm 1:

    - How are c1 and c2 tuned?

    - How is the batch generated in line 5 of the algorithm? Poisson sampling, without replacement, cyclically traversing the dataset? This has an impact on the privacy bound. 

    - How is the sub-Weibull distribution specified in line 6 of algorithm 1? How are $g_t^tail$ and $g_t^body$ defined?
 
    - The authors state that gradients are “divided into the light body or heavy tail”. So the set of per-example gradients in a batch is split in two mutually exclusive groups? Or each gradient is split into two components? The algorithm suggests the latter but the description is unclear.

    - How are the clipping values for baselines defined? From the heatmaps it seems like large c_2 values always work best. So I would imagine that baselined also profited from a large (unique) clipping value.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new DP-SGD like training algorithm, the key idea is to clip gradient using different threshold for body and tail distributions. The proposed algorithm first identify if a sample belongs to body or tail using subspace identification, then clip and add noise correspondingly. Convergence analyses are conducted to show the algorithm is guaranteed to converge with comparable or improved rates with over algorithms. Experiments show the algorithm can have improved performance in practice.

### Strengths
1. The proposed algorithm is studied in both theory and practice. Yielding better results in both cases. The idea of clipping different samples using different threshold is interesting, with the actual algorithm also being solid with guarantees. 
2. The idea of clipping samples with different thresholds worth further exploring by the community. Clipping with a single threshold is known to have issues for class-imbalanced data and may create fairness issues, using different clipping threshold could be a way to mitigate this though it is not touched in this work.

### Weaknesses
1. The proposed algorithm seems to have significantly higher computation cost compared with standard DP-SGD. Specifically, the subspace identification step, which involves computing a projection, adds a non-trivial overhead. This projection requires either a full SVD or an iterative method like power iteration, both of which can be computationally expensive, especially for high-dimensional models. The cost is not just a constant factor, but rather scales with the dimensionality of the model parameters, making it a potential bottleneck for large-scale applications.

2. The algorithm introduces more hyperparameters to tune in practice. While the authors suggest a relationship between the two clipping thresholds, the subspace identification introduces additional parameters like the subspace dimension and the threshold for determining body vs. tail samples. This increases the complexity of hyperparameter tuning, requiring more experimentation to find optimal settings. The sensitivity of the algorithm to these new hyperparameters is not fully explored, and may require significant effort to optimize in practice.

### Questions
1. In practice what is a good way to balance privacy budget for subspace identification and privacy budget for gradient noise?
2. Have the authors considered label-based clipping threshoulds?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes a novel approach, Discriminative Clipping (DC)-DPSGD,
with two key designs. First, it introduces a subspace identification technique to
distinguish between body and tail gradients. Second, it presents a discriminative
clipping mechanism that applies different clipping thresholds for body and tail
gradients separately to reduce the clipping loss. Under the non-convex condition
and heavy-tailed sub-Weibull gradient noise assumption, DC-DPSGD reduces
the empirical risk.

### Strengths
1. Proposing DC-DPSGD with a subspace identification technique and a discriminative clipping
mechanism to optimize DPSGD under sub-Weibull gradient noise assumption. To our knowledge,
this is the first work to rigorously address heavy tails in DPSGD with high probability guarantees.

2 Presenting a high probability guarantee with best-known rates for the optimization performance
of DPSGD, and improve it to faster rates by DC-DPSGD

3. DC-DPSGD consistently outperforms three baselines with up to 9.72% accuracy improvements, demonstrating the effectiveness
of our proposed approach.

### Weaknesses
1. The theoretical contribution is very limited: Although they mentioned there is some improvement. However, such improvement is just logarithmic terms. Note that for non-convex ERM, the best-known result for the gradient norm is O(\frac{d^1/2}{(n\epsilon)^2/3}). Thus, I do not know why the authors only mention a comparison with DP-SGD. If you use DP-SPIDER, you can already achieve $O(\frac{d^1/2}{(n\epsilon)^2/3})$. Thus, the theoretical results are very limited. The authors claim an improvement in the convergence rate, but this is only in the logarithmic terms, which is not a significant practical improvement. The core issue is that the stated convergence rate of $O(\frac{d^{1/4}}{(n\epsilon)^{1/2}})$ is not the best known result for non-convex optimization with differential privacy. The comparison should be made with the optimal rate, not just DP-SGD. The authors need to clearly justify why they are not comparing against the optimal rate and why their result is significant given the existence of better rates. The current analysis does not adequately address this point.

2. The algorithm itself is also unsurprising. It uses the projection on subspaces. However, such an idea has been widely studied in the DP deep learning literature. But there is no comparison between them. The use of subspace projection for gradient manipulation is not novel in the context of differentially private deep learning. The authors fail to adequately position their work within the existing literature on subspace-based methods for DP-SGD. There is no discussion of how their approach differs from or improves upon existing methods, which is a significant oversight. A thorough comparison with existing subspace projection techniques is necessary to establish the novelty and contribution of their method. The lack of such a comparison makes it difficult to assess the true value of their proposed approach.

3. The experiments are not convincing. For example, Auto-S/NSGD is mainly designed for better clipping. Its performance actually is comparable to the original DP-SGD.  I would like to see whether the method can achieve SOTA for CIFAR 10 for private pertaining rather than fine-tuning. DP-PSAC is also for another clipping and it is not SOTA. If the author provides a new clipping method, then comparing with these two methods is sufficient. It does not. So it is very strange to compare with these methods. The experimental evaluation is weak and does not provide sufficient evidence for the effectiveness of the proposed method. The comparison with Auto-S/NSGD and DP-PSAC is not compelling, as these methods are not state-of-the-art and do not represent the best possible baselines. The authors should have compared their method against the best available differentially private training methods for CIFAR-10, especially in a pre-training setting, to demonstrate its practical relevance. The current experimental setup does not adequately showcase the potential of the proposed approach.

### Questions
This outer loop in algorithm 1 is the mistake made by the author? The input does not specify E and subsequent algorithm does not use c. from high level understanding, seems like only the inner loop for T is required?

When g_t^{tail} shows up, I do not know what it means. The presentation for algorithm is confusing. Which makes it hard to check the soundness of the privacy guarantee.

The privacy proof for trace sorting is too complicated; could the author simply do it?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work proposes a discriminative clipping (DC) method for training non-convex smooth models with DP-SGD when gradients are in a class of heavy-tailed sub-Weibull distributions. The method, DC-DPSGD, first employs a subspace identification technique to categorize the per-sample gradient of each batch into a light-body or heavy tail, and then uses a smaller clipping threshold for light-body gradients and a larger threshold for heavy-tailed gradients. The method is found to achieve a better balance between clipping loss and required DP noise, which results in performance improvement at least poly(logT) i.t.o. high-probability excess empirical risks. The work is well-motivated, and the idea of using different clipping thresholds is interesting. Moreover, numerical experiments suggest the method is promising, and insights into the impacts of hyperparameters are interesting.

### Strengths
1. interesting idea of discriminative clipping, supported with solid theoretical analysis
2. models and assumptions are sufficiently general and cover a lot of existing settings as special cases.
3. extensive numerical experiments demonstrating the effectiveness of the proposed method; impacts of hyperparameters on performance might be of practical interest.

### Weaknesses
It comes to my attention that the subspace identification technique (step 9 of alg 1) seems not a true classifier that classifies each gradient into a light body or a heavy-tailed. Instead, it simply selects a portion of gradients whose linear transformation $V_{t, k}^	op \widehat{\mathbf{g}}_t(z_i)$ are ranked top-p% by squared l2 norm (because $tr(xx^	op)=|x|_2^2$). It would be good if the authors could reply to my this concern.



### Questions
1. line 237, $c$ is not defined. I presume $c$ is the clipping threshold. However, because this is the first time $c$ appears and clipping threshold plays a key role, it would be good to clearly define it before using it.
2. regarding the weakness mentioned earlier, can we just privately select top-p% gradients having larger l2 norm, without projecting into a subspace? Any issue with this simple idea?
3. line 357, you may need a subscript $i$ for the notation $\hat{\lambda}^{tr}_{t}$?
4. Theorem 5.4, $C_u$ seems different from the performance measure in Theorem 5.3. And $\nabla \hat{L}_s$ is not defined.
5. Theorem 5.4 appears to be a bit confusing for me. As $p$ is a hyperparameter between 0 and 1, if we take $p\rightarrow 0$, will the result degenerate to that for a case with only light-tailed gradients? In other words, it seems we can fully control the performance by choosing the value of $p$?
6. typos around line 472, 2360.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an algorithmic method to improve the performances of differentially private training algorithm.

This method involves projecting the per-sample gradients on two sub-spaces, dubbed as body and tail gradients, and then applying a discriminative clipping mechanism to them, to enhance the performances and facilitate the optimization.

The paper proves upper bounds on the empirical risk as a function of the training iterations.

### Strengths
This paper studies an important problem, as it looks at improving the performances of differentially private (DP) optimization. The angle is also interesting, as the authors aim to improve the clipping mechanism differentiating it in two subspaces where the phenomenology should be qualitatively different. Considering different sub-spaces of the parameter space has already been considered to improve DP optimization, but, to the best of my knowledge, not with the perspective of the heavy tails of the distribution of the gradients.

### Weaknesses
The presentation, in my opinion, is everything but clear, from the very beginning of the paper. The authors quickly refer to the "gradient noise" without defining it. Considering that this work aims to the community of DP, I believe the average reader would think the authors refer to the injection of noise typical of DP-SGD, which is Gaussian and therefore not heavy tailed, generating the first confusion in this regard. Later it gets progressively clear that the authors refer to the randomness induced by the sub-sampling, and therefore the statistical discrepancy between the estimated (mini-batch) gradient with respect to the true empirical loss gradient. I invite the authors in clearly stating this from the very beginning, and to remark what randomness is addressed (and not) in this case.

The choice of references is also of dubious help. In line 46 Wang et. al (2021) does not seem to suggest using larger clipping threshold; while Gorbunov et al. (2020) looks at the clipping of the mini-batch average gradient, which is different from the per-sample clipping used to provide DP guarantees. The first one is (to the best of my knowledge) instead used for optimization purposes and to facilitate convergence, and does not provide the privacy guarantees of the per-sample clipping. This, again, does not help the reader. I invite the authors to review their choice of references (I did not loop over all of them), and in case some specific statement is taken from a paper, to also point the section in the citation.

The motivation of this work is also not clear. Multiple empirical works [1, 2, 3] (see, e.g., the second paragraph at page 6 of [2]) show that arbitrarily small clipping constant can provide optimal utility in private training. This paper aims to provide a control on the clipping constants assuming that the per-sample gradients might be heavy-tailed in the probability space of the data, but why is this a necessity in light of the experimental evidence from [1, 2, 3]? Is the setting different? Would their consideration fail in some setting that this paper aims to tackle? If yes, is there any experimental evidence of this?

In the main contributions the authors show an informal upper bound on the empirical risk, which reads $\log(\sqrt T)$ (which is $\Theta(\log T)$) - see line 103. How is this bound meaningful? If the labels are of constant order, trivial guess would provide an upperbound of $O(1)$ both on the empirical and population loss (while also guaranteeing privacy), which is better than the one given by the authors. What is the effective importance of this bound, and why is it informative? Can the authors elaborate on this?

The baselines are not completely fair. I would recommend using [2] as a better updated version for baselines on DP-SGD. Besides, the results obtaind by the authors look relatively strong, but no code is available and provided in the supplementary material. The algorithm is not as straightforward as DP-SGD and no auditing has been implemented to verify the effective guarantee of the algorithm. I remark that this is stated as a weakness given my opinion of the method not being carefully explained. Nevertheless, I do not consider this for my score, which is mainly due to the points I raised above.

### Questions
What do the authors mean by:

"the tuning parameters in the classical Abadi's clipping function are complex" in line 137?

"denote $k$-dimensional random projection sampled from heavy-tailed distributions." in line 156? Which distributions? In particular, I find the definition of $V$ rather obscure, and consequently the corresponding step in Algorithm 1. What does "extract orthogonal vectors" in the 6th line of the Algorithm mean? Can the authors be more precise?

"their normalized versions act as mutually orthogonal eigenvectors" in line 305? Independence in high dimension indeed generates approximate orthogonality, but this requires precise assumptions. As a counter-example, if the per-sample gradients where deterministic (i.e. concentrated to their non-0 expectation), Assumption 3.1 would still hold, while the gradients would all be parallel.

### Soundness
1

### Presentation
1

### Contribution
2
