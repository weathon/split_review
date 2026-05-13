# HyperINF: Unleashing the HyperPower of the Schulz's Method for Data Influence Estimation

- Decision: Reject
- Scores: 6, 5, 3, 5, 5, 5, 5, 5

## Abstract
Influence function provides a principled method to assess the contribution of individual training samples to a specific target, yet their high computation costs limits its applications on large-scale models or datasets. 
 Existing methods proposed for influence function approximation have significantly reduce the computation overheads. However, they mostly suffer from a unsatisfied accuracy due to the lack of strong convergence guarantees. The family of hyperpower methods are well-known for their rigorous convergence guarantees on matrix inverse approximation, while the matrix multiplication operation can involve intractable memory and computation costs on large-scale models.
 We propose HyperINF, an efficient and accurate influence function approximation method which leverages the hyperpower method, specifically the Schulz's iterative algorithm.
 To deal with the computation-intensive matrix multiplication, we incorporate the generalized fisher information (GFIM) as a low-rank approximation of the hessian matrix, which reduces the memory and computation overheads to a constant costs independent of ranks on LoRA-tuned models. 
 We first demonstrate the superior accuracy and stability of HyperINF compared to other baselines through a synthetic convergence simulation of matrix inversion. We further validate the efficacy of HyperINFthrough extensive real-world data attribution tasks, including mislabeled data detection and data selection for LLM and VLM fine-tuning. 
 On LoRA-tuned models, HyperINF achieves superior downstream performance with minimal memory and computational overhead, while other baselines suffer from significant degradation. The codebase is available at \url{https://anonymous.4open.science/r/HyperINF-B702}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper identifies the lack of convergence in computing hessian inverse to be the primary source of poor performance of existing data attributions methods. To alleviate this, the authors look to the family of hyperpower methods. Specifically, the authors leverage the Schulz method for its convergence guarantees. They show promising empirical performance (with minimal computational overhead) on various data attribution / mislabelling tasks.

### Strengths
- The problem that this paper addresses is a challenging one, and one of increasing importance/popularity in the community.
- The writing is pretty clear, and the experiments are well described.
- The proposed method is sound, and can potentially see adoption in the community/real world.

### Weaknesses
 - The main contributions of this paper are not clearly disentangled from the overall story. In particular, my understanding is that the primary contribution of this paper is identifying that the Schulz method from the matrix inverse can be efficiently applied in this setting. The rest of the pipeline (Hessian inverse based attribution, Fisher Information Matrix etc) is borrowed from existing work in the field.
- I'm hesitant to use the term marginal/ limited novelty as the authors have made an important observation about an important problem and proposed a (albeit, given previous work, straightforward) method to alleviate it. However, the way the paper is structured currently certainly makes the paper seem like it has very limited novelty. The core idea of using the Schulz method for approximating the Hessian inverse, while potentially impactful, is not presented as a significant methodological leap. The paper could benefit from a more nuanced discussion of the specific challenges in applying the Schulz method to this context, and how the authors have addressed them, rather than simply stating its application. The lack of a detailed analysis of the method's limitations and failure modes further contributes to the perception of limited novelty.


### Questions
- What do you view as the single main contribution of this paper?
- If the main contribution is indeed the incorporation of the Schulz method, was there a reason the paper was positioned and written as a "new data attribution method" instead of "evaluating better matrix inverse methods for data attribution"?
- I notice you have included some discussion of other matrix inverse methods in Appendix F. How were the matrices chosen for the experiments? Were they random, or drawn from some real world data attribution settings? Are certain methods better than others for certain distributions of matrices?
- Did you try other techniques for matrix inversion such as Neumann series approximation and successive over relaxation?

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
4

### Summary
This paper proposes to address the efficient and effective data attribution problem, with application to LLM and LVM fine-tuning.

The authors first based on LISSA and DATAINF, propose to attribute validation loss to individual fine-tuning examples, via a product of gradient, Hessian inverse, and a vector. The bottleneck of the computation is in the inverse of the large Hessian matrix, which has dimensionality d\times d. LISSA use the iterative method to find $H^{-1}v$, while DATAINF uses the Sherman-Morrison formula and the Fisher Information Matrix (FIM) approximating the Hessian for efficient computation of $H^{-1}v$.
The proposed HyerPower method is in Eq. (5), where the GFIM is used in place of FIM.

Schulz’s method is a hyperpower iterative method, since "Schulz’s method demonstrates superior accuracy in terms of error rate and significant efficiency gains from the GPU acceleration on matrix multiplications".

Overall, the paper used a new numerical computation method (Schulz’s method) to gain efficiency, under the framework set by previous work (influence function by Koh & Liang, 2020, and DATAINF/LISSA).

The experimental results are somehow strong:
1) simulation showed that LISSA and DATAINF won't converge, while Schulz’s method converges quickly.
2) on a LORA-tuned LLM Roberta-large, they showed that the mislabeled data points can be detected by HYPERINF more accurately.
3) on a LORA-tuned LLM (Llama2-7B), they showed that data selected by HYPERINF leads to better fine-tuning accuracy.
4) on a LVM, they showed that data selected by HYPERINF leads to better pre-training.

### Strengths
+ The computational time and memory usage for data attribution are greatly reduced by HYPERINF.
+ the effectiveness and efficiency are demonstrated on several tasks, showing the generality of HYPERINF.

### Weaknesses
 - The novelty may be limited, in the sense that an existing numerical power method is applied to an existing problem (The identification of the challenge and the solution are still recognized).
- There are some experimental observations that are not explained well. See the questions

 In Table 2 & 4, it shows that when selecting a smaller portion of bad data, the improvement over DATAINF is very limited (e.g., in Table 4, HYPERINF has 53.2 and the runner-up has 53). Any explanation about this?

In Table 3, why dense fine-tuning gives worse performance than sparse fine-tuning?

Did you try several initialization for LISSA and DataInf? HYPERINF may have unstability issue too and multiple initializations should be tried.

Can you make your contributions in Eqs. (4-6) clear by comparing your methods to existing technique? It seems that these equations are adopted from previous work.

### Questions
In Table 2 & 4, it shows that when selecting a smaller portion of bad data, the improvement over DATAINF is very limited (e.g., in Table 4, HYPERINF has 53.2 and the runner-up has 53). Any explanation about this?

In Table 3, why dense fine-tuning gives worse performance than sparse fine-tuning?

Did you try several initialization for LISSA and DataInf? HYPERINF may have unstability issue too and multiple initializations should be tried.

Can you make your contributions in Eqs. (4-6) clear by comparing your methods to existing technique? It seems that these equations are adopted from previous work.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a new method for efficiently approximating influence function, which contains two steps: (1) based on certain assumptions, decompose the expected gradient outerproducts into the kronecker products between identity matrix and average covariance matrix of gradient columns. (2) use Schulz's method to invert the matrix.

### Strengths
Trending topic, the line of data attribution is very important, especially in the era of foundation models.

### Weaknesses
I am mainly concerned about the assumption made in Lemma 1. I seem to not find any justification for the assumption of zero expectation and independence for gradient columns where the randomness is taken over the label $y ~ p(y|}x, \theta)$. However, this seems to be the key result for the paper (I don't think the application of using Schulz's method for matrix inverse is very impressive). I also took a look at the proof for Lemma 1 and I find it poorly written, which involves typos like 'Var(g(:,k), g(:,k))' and other stuff. The only justification for the assumption I found in the paper is in line 223-224, but it's still very unclear. What does it even mean by "each column is independent and identical"? With respect to which probability distribution?

I took a look at the pseudocode of the algorithm. It seems that to compute generalized FIM, the author uses the groundtruth label $y_i$ instead of sampling from $y ~ p(y|}x_i, \theta)$. This is a mistake (but understandable), and the same mistake was also made in DataInf. Bartlett’s identities are with respect to model distribution $p(x, y, \theta) = p(x)p(y|}x, \theta)$, not the groundtruth distribution! This issue has been discussed in the optimization community https://arxiv.org/abs/1905.12558. While the two quantities might be fairly close to each other for well-trained classifiers, I am not sure about the language model. Since this issue is a common mistake, it won't lower my score for the paper, but I recommend the author include a paragraph of discussion on this issue.

### Questions
Why not compare with K-FAC and EK-FAC approach? https://arxiv.org/abs/2308.03296 I think this is the most relevant work as K-FAC is fairly similar to Section 3.1.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes using the Schulz's method to approximate the inverse of Hessian matrices that appears in the influence function. The authors demonstrate in Figure 1 that the Schulz's method can converge to the ground-truths while other baselines, such as LiSSA, diverge. Besides, their experiments on downstream tasks show that better approximation of inverse could lead to better performance.

### Strengths
The experiment results strongly support the benefits of more accurately approximating the inverves of Hessian matrices when using influence function.

### Weaknesses
 - I did not see any differences between Lemma 1 presented in the submission and Lemma 1 in (Yang et al., 2022).

- The paper seems to suggest that the performance boost is mainly due to a more accurate approximation of the inverse of Hessian matrices in the influence function. In Figure 1, it shows that LiSSA does not converge, which should not be the case. My guess is that the authors adopted the implementation from Koh and Liang (2017), which may not align well with the theory. That being said, LiSSA can be implemented in a way that guarantees convergence; see Appendix D in (Bae et al., 2022). Therefore, I do not think the authors have made a fair comparison in Figure 1.

Minor:

- Regarding the introduction of the influence function, I would suggest that the authors refer to (Bae et al., 2022) for how the ideal assumptions of strong convexity and attainable optimal solutions can be mitigated. 

- I would recommend that, regarding Eq. (3), the authors explicitly write down that the two expectations are taken over $(X,Y) \sim p(X)p(Y|f_{\boldsymbol\theta}(X))$ for clarity. It demonstrates that the approximation holds if $p(Y|f_{\boldsymbol\theta}(X))$ fits the training data well. Nevertheless, in the context of Eq. (3), this approximation is always there by using the first-order Taylor approximation of $f_{\boldsymbol\theta}(X)$.

### Questions
Suppose that a Hessian matrix $H$ is invertible and satisfies $\\|H\\| \leq U$ for some scalar $U>0$, what are the complexities of using LiSSA and Schulz's method to approximate $H^{-1}$?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new influence function approximation scheme (HYPERINF) based on Schulz’s iterative algorithm for matrix inversion and the generalized Fisher Information Matrix. The authors elaborate on the intuitions and the details of the algorithm, and also numerical experiments demonstrate the algorithm's advantages over benchmark methods.

### Strengths
The paper is well-written and easy to follow. It provides a thorough account of the existing methods for the problem. The proposed method is new and naturally integrates existing ideas for approximating the Hessian matrix. Numerical results show the promise of the method compared to benchmarks.

### Weaknesses
I have the following comments about the paper:

My main concern is that the proposed method is a combination of several existing ideas: 
- The general Fisher information matrix is from the DataInf paper of Kwon et al. (2024) 
- The blockwise structure of the Hessian matrix is from Zhang et al. (2024) a;b
- The Schultz’s method is a well-known algorithm for matrix inversion.
To this end, the proposed method is more like an ad-hoc engineering improvement of the existing method. 

More specifically, if we view it as an extension of Kwon et al. (2024) that adopts the Schultz’s method, the computational advantage and accuracy improvement against DataInf in Kwon et al. (2024) seem not quite significant to me.

In the numerical experiment, it seems unfair to evaluate LISSA using the Frobenius norm when v is randomly generated. If LISSA performs poorly as the authors argue (e.g., with an approximation error around 10^5 as noted on line 301), why does LISSA outperform other methods in some cases, such as for HellaSwag on line 411?

Also, how are some of the experimental parameters chosen? For example, rank = 64 is used in some cases and rank = 16 in others, why this choice? Why is the comparison in line 388 limited to training the model on the full dataset for just one epoch?

On the theoretical side, the computational complexity of equation (23) should be O(d^2), while the complexity of equation (22) should be O(d^3). Even though these complexities may be further optimized, they can never be reduced to O(d) and O(d^2) as I understand.

Minor note: 
1). Line 207, identify -> identity
2). In equation (4), there shouldn't be a factor 1/r in the last term.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper is motivated by the computational challenge of influence functions, and proposes an approximation method based on the Schulz's iterative algorithm. In particular, the generalized fisher information is used to construct a low-rank approximation of Hessian matrix. Experiments of proposed method is illustrated on simulation, mislabeled data detection,  data selection for LLM, and VLM fine-tuning.

### Strengths
- This paper proposes a principled method to approximate influence function, which is a very important topic in modern learning with large-scale models and datasets
- The proposed method is evaluated on various applications including LLM training

### Weaknesses
Major
- I was put off when noticing that the general setup seems to include a general loss function $\ell$, yet the derivation relies on Equation (3), which restricts $\ell$ to be a log-likelihood function. This significantly limits the applicability of the proposed method, as many loss functions used in practice, such as mean squared error or contrastive losses, do not fall under this category. The paper should explicitly state this limitation in the introduction and abstract.
- From Table 1, it is clear that the proposed method, HyperINF, performs worse than the existing method, DataInf, in terms of all three complexities. The paper claims that DataInf has a $O(d^2)$ approximation error, making it prone to large approximation errors when $d$ is large. However, there is a lack of rigorous characterization or illustration of HyperINF's performance concerning approximation error. The paper needs to provide a more detailed analysis of the approximation error of HyperINF, including how it scales with the dimensionality of the problem and the rank $r$ of the low-rank approximation. Furthermore, the experimental results do not clearly demonstrate the advantage of HyperINF in terms of approximation error, especially when compared to DataInf.
- In particular, I am surprised to see that, even though the abstract mentions leveraging the low-rank structure, the proposed algorithm’s computational complexity barely depends on $r$, with even less dependence than DataInf. This is counter-intuitive, as one would expect the computational cost to decrease with a lower rank approximation. The paper should provide a more detailed explanation of why the computational complexity does not significantly depend on $r$ and how the low-rank structure is actually exploited in the algorithm.
- Regarding estimation accuracies in Table 2, the performance difference compared to DataInf is marginal or even worse in some cases. This raises concerns about the practical utility of the proposed method, as it does not seem to offer significant improvements over existing methods in terms of accuracy.

Minor
- Lemma 1 is essentially the same as Lemma 1 in the cited reference Yang et al. (2022). I think the proof is unnecessary, and credit should be given to the reference in the main text of the paper, rather than just saying "following the proof of Yang et al. (2022)" in the appendix.
- Equation (3): I believe a negative sign is missing.
- Figure 2: The plots are not color-blind-friendly.

### Questions
- Overall, I am not fully convinced that the proposed method is broadly applicable, and its theoretical contribution feels rather thin. I would appreciate it if the authors could clarify the mathematical derivations of the proposed method and address the weaknesses mentioned above.
- Regarding the numerical experiments, could the authors consider building additional experimental setups or metrics that go beyond accuracy comparisons, such as directly evaluating convergence speed, running time, etc.? This would also help present a more coherent narrative on the strengths of the proposed method.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses an important challenge in scaling influence functions to large-scale models by introducing HYPERINF. The authors propose combining Schulz's method with a generalized Fisher Information Matrix, achieving improved convergence performance for Hessian matrix inversion with greater efficiency. Through comprehensive experiments across mislabeled data detection and data selection tasks for both LLMs and VLMs, the method shows significant advantages over existing baselines.

### Strengths
1. The authors tackle the important challenge of estimating data influence in large-scale models.
2. The authors propose leveraging the GFIM to enhance computational efficiency and Schulz's method to improve the convergence guarantee, presenting a technically intriguing approach. They further demonstrate superior convergence performance over baselines in controlled settings.
3. The authors provide extensive experimental validation to support the effectiveness of their proposed method.

### Weaknesses
It is surprising that other baselines (e.g., DATAINF, LISSA, TracIN) sometimes show even lower performance than random selection (e.g., 5% AVG DATAINF, LISSA, TRACIN in Table 8, 5% AVG DataINF in Table 3, 5% and 20% AVG LISSA in Table 4). Additionally, the results vary across different selection ratios (e.g., in Table 2, QASC random selection shows the best performance at 5%, while influence-based methods show better performance at 20%), which is interesting to analyze, but at the same time, it makes me difficult to understand why each method shows different advantages across data distributions and ratios without enough discussion. While the authors explain this in terms of influence-based methods, the results differ among these methods (e.g., sometimes DataINF shows the best results, and sometimes LISSA performs best). It would be helpful if the authors could provide more discussion on this. Additionally, I asked about the rationale of the current evaluation dataset selection. Although the authors provided insights about which datasets are suitable for influence-based methods, it does not answer the point of the selection of four datasets in Tables 2 and 3. For example, is this experiment designed for the reasoning task? will the result be consistent even if we consider a dataset from a different task? The reason for this question is the gap between methods looks marginal and might be flipped if we consider different datasets (e.g., Table 2, 0.2% gap for 5% selection, and 1% for 20% selection, Table 4, 0.2% for 5% selection, 1.6% for 20% selection). Thus, the consistency of these results across different datasets, and models remains a concern.

On the other hand, this method works well on the mislabeled data detection task, except for SST2. It would be also helpful if the authors could discuss this in more detail.

### Questions
1. Lemma 1 relies on the assumption that gradient columns are independently and identically distributed. However, it's unclear what this means in practice. For a gradient matrix, how can we justify that each column is independent? The authors should provide more insights or practical explanations for this assumption. 
2. While the proposed method shows clear advantages in controlled settings, it sometimes underperforms compared to baselines in practical applications, as indicated in Tables 2 and 3. What insights do the authors have about this discrepancy? Is this due to violated assumptions, or might the high-influence points selected by the proposed method not necessarily translate to improved accuracy?
3. I'm more concerned about the practical applications of this approach in LLM data selection. For example, when evaluating training point influence, should we only focus on D_val from the same distribution as D_train? As a model developer, I would be more interested in understanding how incorporating certain training data would improve general performance rather than just performance on the same distribution. Specifically, 5% of data selected from the proposed method can improve the general performance if the D_val consists of samples from multiple domains.
4. Since the performance gap may vary depending on the dataset, could the authors explain their criteria for selecting evaluation datasets?
5. Do the authors could further explain why dense fine-tuning shows strong performance with 5% data selection, compared to Lora-finetuned models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 8

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the problem of effective and efficient approximations for the Hessian matrix in Influence Functions for large-scale ML models. The paper points out that existing methods for this tasks, LiSSA and DataInf, have higher computation complexities and/or looser error bounds. This paper proposes HyperInf, which performs block-wise diagonal approximations of the Hessian matrix and its inverse and then approximate the inverse matrix with the iterative Schultz method. The paper shows that, empirically, this iterative Schultz method is robust to different initializations and, theoretically, enjoys a favorable convergence rate. The paper conducts empirical studies on mislabeled dection on the GLUE benchmark with BERT models, data selection for LLM fine-tuning, and training VLMs on instruction datasets and compares the performance of HyperInf with Random, TracIn, DataInf and LiSSA. Empirical results shows HyperInf achieves better overall performance.

### Strengths
The scope and motivation of the paper is clear. It is straightforward to understand what does this paper aim to improve.

The logical flow for theoretical development is coherent. The derivations are clear and the elobrations are accurate.

Experiments are diverse and the comparisons are comprehensive.

### Weaknesses
The work is heavily inspired by DataInf where many components are shared, such as the use of Fisher Information Matrix (FIM). Some theoretical analysis directly cites DataInf for results. This may pose challenges for some readers and mandate reading DataInf to fully understand this paper. It may be helpful to add additional introductions and comments of DataInf directly into the narrative of this manuscript and make it more indepedent.

**In general, the contribution of this paper appears incremental compared to DataInf. The major change is replacing the Sherman-Morrison formula to the iterative Schultz method for approximating matrix inversion.** Sherman-Morrison formula appears to be the standard approach for approximating matrix inversion, which is expected to work especially for low-rank matrices. This paper only cites its looser theoretical guarantee to motivate the development of the proposed method. In machine learning, theoretical bounds are often conservative which may or may not be relevant to the actual use case. There appears to be a major gap in the narrative and ncessciates in-depth comparisons and discussions, both theoreitcal and empirical.

The set of empirical studies is less conventional. Data selection for foundation models is known to be a tricky task where the selection scale has challenges the prior knowledge for the tradeoff between data quality and diversity. Influence-based method such as [Less: Selecting influential data for targeted instruction tuning] turns out to be less effective for selecting pre-training data and many selection methods may not outperform random baselines (Ref: [Rethinking Data Selection at Scale: Random Selection is Almost All You Need] ). Thus, I am not fully convinced by results on these experiments.

### Questions
Since these techniques are all designed for approximating the inverse of Hessian matrix, which is also a proxy for the difference in model performance compared to re-training the model without the sample.

Why not starting from fundamentals and conducting apple-to-apple comparisons on how each of these method approximate the inverse of Hessian matrix and how they relate to the actual leave-one-out error?

Besides, this paper misses the comparison for the actual compute overhead of each method. This could be a result of great interest.

### Soundness
3

### Presentation
2

### Contribution
2
