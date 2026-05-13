# Causal Discovery via Bayesian Optimization

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Existing score-based methods for directed acyclic graph (DAG) learning from observational data struggle to recover the causal graph accurately and sample-efficiently. To overcome this, in this study, we propose DrBO (DAG recovery via Bayesian Optimization)—a novel DAG learning framework leveraging Bayesian optimization (BO) to find high-scoring DAGs. We show that, by sophisticatedly choosing the promising DAGs to explore, we can find higher-scoring ones much more efficiently. To address the scalability issues of conventional BO in DAG learning, we replace Gaussian Processes commonly employed in BO with dropout neural networks, trained in a continual manner, which allows for (i) flexibly modeling the DAG scores without overfitting, (ii) incorporation of uncertainty into the estimated scores, and (iii) scaling with the number of evaluations. As a result, DrBO is computationally efficient and can find the accurate DAG in fewer trials and less time than existing state-of-the-art methods. This is demonstrated through an extensive set of empirical evaluations on many challenging settings with both synthetic and real data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose DrBO (DAG recovery via Bayesian Optimization)—a novel DAG learning framework leveraging Bayesian optimization (BO) to find high-scoring DAGs.  To address the scalability issues of conventional BO in DAG learning,  the authors replace Gaussian Processes commonly employed in BO with dropout neural networks, trained in a continual manner. DrBO is computationally efficient and can find the accurate DAG in fewer trials and less time than existing state-of-the-art methods. This is demonstrated through an extensive set of empirical evaluations on many challenging settings with both synthetic and real data.

### Strengths
Learning DAG from data using BO is novel and interesting.  The authors overcome the scalability issue of conventional BO by leveraging dropout in neural networks. Experimental results show that the proposed method is effective and can achieve improved results. The paper was written with technical details.

### Weaknesses
N/A

### Questions
Could the authors give more details on how to ensure the binary adjacent matrix is a DAG in the optimization steps?

### Soundness
3

### Presentation
3

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
This paper proposes an efficient causal discovery algorithm with Bayesian optimization. In particular, the authors consider a variant of Vec2DAG (Duong et al., 2024) for the DAG constraint, and use dropout neural networks and continual training scheme to optimize the adjacency matrix. Experiments show the efficiency and effectiveness of their method.

### Strengths
- This paper is written clearly, with clear and detailed descriptions of their method and experiments.

- They performed extensive experiments for validation.

### Weaknesses
 - While there exist some causal discovery algorithms with Bayesian optimization, it seems not proper to state “To our knowledge, this is the first score-based causal discovery method based on BO ”. I think it should be corrected.

- Throughout the paper, from the experiments, it is demonstrated that the proposed method can give better performances in both accuracy, sample-efficiency, and scalability, compared with other SOTA baselines. Generally, such a great method needs more assumptions or conditions to be satisfied. But intuitively, I cannot find these assumptions or conditions. Did this method have some other implied assumptions or conditions (like more hyperparameters)? 

- In experiments, it would be good to compare some Bayesian causal discovery methods (Deleu et al., 2022: Tranet al., 2023; Annadani et al., 2023), since they are all causal discovery methods. Or explain the reasons why not comparing with them.

- The code is not available for reproduction.

### Questions
- In Eq.(4), is the matrix $R$ strictly upper-triangular?
- In Figure 1(b), did the authors still use 1000 samples for the large-graph experiments? $n=1000$ for the graph with 100 nodes?
- In Figure 3(a), why in general smaller $k$ could obtain higher performances, compared with the full-rank cases?

### Soundness
3

### Presentation
3

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
This paper develops a Bayesian optimization method for score-based causal discovery. Several design choices are adopted, which include (1) developing a low-rank DAG representation, (2) replacing Gaussian process in conventional Bayesian optimization with dropout neural networks, (3) learning the DAG score indirectly via node-wise local scores, and (4) training in a continual way. Empirical studies are provided.

### Strengths
- The paper is well written and easy to follow.
- Developing effective search procedure for score-based causal discovery is an interesting and important topic. The proposed method adopts various design choices and is practical.
- The search method is reasonable.
- The empirical studies demonstrate that the proposed method considerably outperforms existing methods.

### Weaknesses
 - Some of the baselines considered are not adequate.
- Some of the results may seem too good to be true. For example, achieving a SHD of 1.6 with only 1000 samples across 30 nodes and 240 edges seems highly challenging due to finite sample error. This concern is especially relevant when dealing with nonlinear data. (I look forward to the authors' clarification/explanation on this, and please correct me if I misunderstood anything.)
- Although BIC-NV is given, it seems that the experiments focus on equal variances. I would suggest adding experiments for different variances as well.
- Baselines: For linear case, GOLEM may also be included. Also, adding the results for more conventional search methods, such as GES/FGES, may also be helpful.
- Why does DAGMA-MLP performs so poorly for nonlinear data? The TPR is close to 0. If the reason is due to instability in optimization, the paper may consider adding NOTEARS-MLP that may be more stable.
- For Section 5.2, specifically Sachs data, did the paper use linear or nonlinear version of the method?

### Questions
- Is there a reason why the paper considers only identifiable models? That is, why general linear Gaussian model cannot be learned by the BIC-NV score?
- Although BIC-NV is given, it seems that the experiments focus on equal variances. I would suggest adding experiments for different variances as well.
- Baselines: For linear case, GOLEM may also be included. Also, adding the results for more conventional search methods, such as GES/FGES, may also be helpful.
- Why does DAGMA-MLP performs so poorly for nonlinear data? The TPR is close to 0. If the reason is due to instability in optimization, the paper may consider adding NOTEARS-MLP that may be more stable.
- For Section 5.2, specifically Sachs data, did the paper use linear or nonlinear version of the method?

### Soundness
2

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
5

### Summary
This paper introduces DrBO, a Bayesian Optimization-based framework for efficient and accurate DAG learning from observational data. By leveraging dropout neural networks instead of Gaussian Processes, DrBO addresses scalability issues while integrating uncertainty in score estimation. Empirical results demonstrate DrBO's improved efficiency and accuracy over existing methods across synthetic and real datasets.

### Strengths
- Using BO in causal discovery is interesting and novel. 
- The paper is very well written.

### Weaknesses
 - Using BO in causal discovery is interesting and novel.
- The paper is very well written.


 see questions.

 1. To my knowledge, the CBO series of papers assumes that the DAG structure is known and primarily focuses on optimizing policies with this prior knowledge. Therefore, these papers may not be directly relevant to the active causal discovery literature. Please revise this in the introduction to reflect the distinction.

2. The synthetic dataset, as first used in NOTEARS, is known to be relatively easy to learn, making pursuit of very low SHD scores less meaningful in recent research, especially the very simple linear gaussian case. How does your method perform on this dataset after standardization, as described in the paper *Beware of the Simulated DAG*?

3. The proposed method appears to be limited to ANMs in causal discovery, which restricts the scope of the paper. It may be more accurate to frame the task as DAG structure learning or Bayesian structure learning rather than causal discovery.

4. In Section 4.1, the authors mention that their method incorporates a low-rank adaptation of Vec2DAG. Does this imply an assumption about the data’s structure, as discussed in *On Low Rank Directed Acyclic Graphs and Causal Structure Learning*? Additionally, what would occur if \( k < d \)?

5. Replacing the Gaussian Process in Bayesian Optimization with Dropout is not uncommon, so it may not warrant being highlighted as a novel contribution in this paper.

6. While many prior works employ CAM as a pruning method, I believe this approach may lack justification here. Why would score-based search methods, including this paper, attempt to prune under nonlinear conditions? It's unusual for newly proposed methods to rely on post-processing from an older method.

7. Please compare this baseline method, *Truncated Matrix Power Iteration for Differentiable DAG Learning*, to your approach.

8. In Figure 1, several methods being compared fail to converge. For the tabulated results, have you ensured that all comparison methods have converged? Additionally, consider moving the running time details from the appendix to the main content, as the high time complexity is a notable limitation of the proposed method.

9. Please provide results for nonlinear functions with datasets of 50 and 100 nodes, detailing both performance metrics and running time.

### Questions
1. To my knowledge, the CBO series of papers assumes that the DAG structure is known and primarily focuses on optimizing policies with this prior knowledge. Therefore, these papers may not be directly relevant to the active causal discovery literature. Please revise this in the introduction to reflect the distinction.

2. The synthetic dataset, as first used in NOTEARS, is known to be relatively easy to learn, making pursuit of very low SHD scores less meaningful in recent research, especially the very simple linear gaussian case. How does your method perform on this dataset after standardization, as described in the paper *Beware of the Simulated DAG*?

3. The proposed method appears to be limited to ANMs in causal discovery, which restricts the scope of the paper. It may be more accurate to frame the task as DAG structure learning or Bayesian structure learning rather than causal discovery.

4. In Section 4.1, the authors mention that their method incorporates a low-rank adaptation of Vec2DAG. Does this imply an assumption about the data’s structure, as discussed in *On Low Rank Directed Acyclic Graphs and Causal Structure Learning*? Additionally, what would occur if \( k < d \)?

5. Replacing the Gaussian Process in Bayesian Optimization with Dropout is not uncommon, so it may not warrant being highlighted as a novel contribution in this paper.

6. While many prior works employ CAM as a pruning method, I believe this approach may lack justification here. Why would score-based search methods, including this paper, attempt to prune under nonlinear conditions? It's unusual for newly proposed methods to rely on post-processing from an older method.

7. Please compare this baseline method, *Truncated Matrix Power Iteration for Differentiable DAG Learning*, to your approach.

8. In Figure 1, several methods being compared fail to converge. For the tabulated results, have you ensured that all comparison methods have converged? Additionally, consider moving the running time details from the appendix to the main content, as the high time complexity is a notable limitation of the proposed method.

9. Please provide results for nonlinear functions with datasets of 50 and 100 nodes, detailing both performance metrics and running time.

### Soundness
2

### Presentation
3

### Contribution
2
