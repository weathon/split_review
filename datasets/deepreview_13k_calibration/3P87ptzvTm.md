# Optimal Multiple Transport with Applications to Visual Matching, Model Fusion and Beyond

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Optimal transport (OT) has wide applications including machine learning. It concerns finding the optimal mapping for Monge OT (or coupling for Kantorovich OT) between two probability measures. This paper generalizes the classic pairwise OT to the so-called Optimal Multiple Transportation (OMT) accepting more than two probability measures as input. We formulate the problem as minimizing the transportation costs between each pair of distributions and meanwhile requiring cycle-consistency of transportation among probability measures. In particular, we present both the Monge and Kantorovich formulations of OMT and obtain the approximate solution with added entropic and cycle-consistency regularization, for which an iterative Sinkhorn-based algorithm (ROMT-Sinkhorn) is proposed. We empirically show the superiority of our approach on two popular tasks: visual multi-point matching (MPM) and multi-model fusion (MMF). In MPM, our OMT solver directly utilizes the cosine distance between learned features of points obtained from off-the-shelf graph matching neural networks as the pairwise cost. We leverage the ROMT-Sinkhorn algorithm to learn multiple matchings. For MMF, we focus on the problem of fusing three models and employ ROMT-Sinkhorn instead of the Sinkhorn algorithm to learn the alignment between layers. Both tasks achieve competitive results with ROMT-Sinkhorn. Furthermore, we showcase the potential of our approach in addressing the travel salesman problem (TSP) by searching for the optimal path on the probability matrix instead of the distance matrix. Source code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduced the Monge and Kantorovich formulations of a novel Optimal Transport problem, termed Optimal Multiple Transportation (OMT), between more than two probability measures. OMT minimizes the total pairwise transportation costs while ensuring cycle consistency. By adding the entropic and cycle consistency regularization, OMT can be efficiently solved by an iterative Sinkhorn algorithm, termed ROMT-Sinkhorn. As a side product, the authors developed a new formulation for the Traveling Salesman Problem (TSP). The newly introduced problem, TSP-OMT, can be solved greedily in the probability space instead of the conventional distance space. Finally, empirical results showed the effectiveness of the proposed ROMT-Sinkhorn algorithm in two applications: multi-point matching and multi-model fusion.

### Strengths
- To the best of my knowledge, the introduced OT problem in this paper is novel.
- This paper is well-written and easy to follow.
- The authors clearly distinguished between Multi-marginal OT and OMT.
- The cycle consistency requirement is well-motivated in applications.
- The effectiveness of the proposed RMOT-Sinkhorn is supported by the empirical results to some extent.

### Weaknesses
 - The literature review for model fusion is not well-written.
- This paper lacks some theoretical results.
- My main concern is the scalability of OMT-Sinkhorn. All examples/experiments only consider three measures.
- The literature for Model Fusion lacks a lot of related papers. Here are a few recent papers on the topic of model fusion:
  - [r1] Hongyi Wang, Mikhail Yurochkin, Yuekai Sun, Dimitris Papailiopoulos, and Yasaman Khazaeni. Federated learning with matched averaging. In International Conference on Learning Representations, 2020.
  - [r2] Mitchell Wortsman, Gabriel Ilharco, Samir Ya Gadre, Rebecca Roelofs, Raphael Gontijo-Lopes, Ari S Morcos, Hongseok Namkoong, Ali Farhadi, Yair Carmon, Simon Kornblith, et al. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In International Conference on Machine Learning, pp. 23965–23998. PMLR, 2022.
  - [r3] Michael S Matena and Colin A Raffel. Merging models with fisher-weighted averaging. Advances in Neural Information Processing Systems, 35:17703–17716, 2022.
  - [r4] Akash, Aditya Kumar, Sixu Li, and Nicolás García Trillos. "Wasserstein Barycenter-based Model Fusion and Linear Mode Connectivity of Neural Networks." arXiv preprint arXiv:2210.06671 (2022).
  - [r5] Ainsworth, Samuel K., Jonathan Hayase, and Siddhartha Srinivasa. Git re-basin: Merging models modulo permutation symmetries. In International Conference on Learning Representations, 2023.
  - [r6] Dang Nguyen, Trang Nguyen, Khai Nguyen, Dinh Phung, Hung Bui, and Nhat Ho. On cross-layer alignment for model fusion of heterogeneous neural networks. In ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5. IEEE, 2023.
  - [r7] Stoica, George, Daniel Bolya, Jakob Bjorner, Taylor Hearn, and Judy Hoffman. "ZipIt! Merging Models from Different Tasks without Training." arXiv preprint arXiv:2305.03053 (2023).
  - [r8] Imfeld, Moritz, Jacopo Graldi, Marco Giordano, Thomas Hofmann, Sotiris Anagnostidis, and Sidak Pal Singh. "Transformer Fusion with Optimal Transport." arXiv preprint arXiv:2310.05719 (2023).
- Can the authors provide the complexity analysis of OMT-Sinkhorn?
- Eq. 15: “We set $\delta_k > 0$ for $k < K$ to make  $(P_k)_{ii}$ approach 0 for every $k < K$, and $\delta_K < 0$ to make $(P_k)_{ii}$ approach 1.” Should the coefficients be set reversely?
- **Scalability**. Can the authors demonstrate the applications for more measures? Like in OTFusion (Singh & Jaggi, 2020), the authors can fuse 4 and 6 models. In addition, the scale of the architecture in model fusion is also relatively small. Model fusion can fuse ResNet, LSTM, and even Transformer.
- The number of baselines is quite limited. One possible baseline can be generated from the optimal solution of Multi-marginal OT. Given $P$ is the optimal solution for multi-marginal OT. We can have $P_1 = \sum_{i_3 = 1}^{n_3} P_{i_1, i_2, i_3}$. $P_2$ and $P_3$ can be defined similarly. Another simple baseline is to iteratively fuse two models.
- Tab. 3: For CIFAR10 + VGG11, the finetuned accuracy is the same as the best pre-trained one, which raises concerns about efficiency.

**Minor**: 
- The title of Section 2.3 should be only “Visual Point Matching and Model Fusion” because the usage of OT is not mentioned enough.
- Notation consistency for $\mathbb{R}^{+}$.
- Should use different notations for $\mathcal{C}$ in Eq. (7) and (8).
- entropy regularization → entropic regularization
- The usage of $\delta$ as a regularization coefficient should be avoided as $\delta$ denotes the Dirac measure earlier.
- “Tab. 3 shows the fusion results” This sentence can be removed from Section 3.4.
- Some typos

### Questions
- The literature for Model Fusion lacks a lot of related papers. Here are a few recent papers on the topic of model fusion:
  - [r1] Hongyi Wang, Mikhail Yurochkin, Yuekai Sun, Dimitris Papailiopoulos, and Yasaman Khazaeni. Federated learning with matched averaging. In International Conference on Learning Representations, 2020.
  - [r2] Mitchell Wortsman, Gabriel Ilharco, Samir Ya Gadre, Rebecca Roelofs, Raphael Gontijo-Lopes, Ari S Morcos, Hongseok Namkoong, Ali Farhadi, Yair Carmon, Simon Kornblith, et al. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In International Conference on Machine Learning, pp. 23965–23998. PMLR, 2022.
  - [r3] Michael S Matena and Colin A Raffel. Merging models with fisher-weighted averaging. Advances in Neural Information Processing Systems, 35:17703–17716, 2022.
  - [r4] Akash, Aditya Kumar, Sixu Li, and Nicolás García Trillos. "Wasserstein Barycenter-based Model Fusion and Linear Mode Connectivity of Neural Networks." arXiv preprint arXiv:2210.06671 (2022).
  - [r5] Ainsworth, Samuel K., Jonathan Hayase, and Siddhartha Srinivasa. Git re-basin: Merging models modulo permutation symmetries. In International Conference on Learning Representations, 2023.
  - [r6] Dang Nguyen, Trang Nguyen, Khai Nguyen, Dinh Phung, Hung Bui, and Nhat Ho. On cross-layer alignment for model fusion of heterogeneous neural networks. In ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5. IEEE, 2023.
  - [r7] Stoica, George, Daniel Bolya, Jakob Bjorner, Taylor Hearn, and Judy Hoffman. "ZipIt! Merging Models from Different Tasks without Training." arXiv preprint arXiv:2305.03053 (2023).
  - [r8] Imfeld, Moritz, Jacopo Graldi, Marco Giordano, Thomas Hofmann, Sotiris Anagnostidis, and Sidak Pal Singh. "Transformer Fusion with Optimal Transport." arXiv preprint arXiv:2310.05719 (2023).
- Can the authors provide the complexity analysis of OMT-Sinkhorn?
- Eq. 15: “We set $\delta_k > 0$ for $k < K$ to make  $(P_k)\_{ii}$ approach 0 for every $k < K$, and $\delta_K < 0$ to make $(P_k)_{ii}$ approach 1.” Should the coefficients be set reversely?
- **Scalability**. Can the authors demonstrate the applications for more measures? Like in OTFusion (Singh & Jaggi, 2020), the authors can fuse 4 and 6 models. In addition, the scale of the architecture in model fusion is also relatively small. Model fusion can fuse ResNet, LSTM, and even Transformer.
- The number of baselines is quite limited. One possible baseline can be generated from the optimal solution of Multi-marginal OT. Given $P$ is the optimal solution for multi-marginal OT. We can have $P_1 = \sum_{i_3 = 1}^{n_3} P_{i_1, i_2, i_3}$. $P_2$ and $P_3$ can be defined similarly. Another simple baseline is to iteratively fuse two models.
- Tab. 3: For CIFAR10 + VGG11, the finetuned accuracy is the same as the best pre-trained one, which raises concerns about efficiency.

**Minor**: 
- The title of Section 2.3 should be only “Visual Point Matching and Model Fusion” because the usage of OT is not mentioned enough.
- Notation consistency for $\mathbb{R}^{+}$.
- Should use different notations for $\mathcal{C}$ in Eq. (7) and (8).
- entropy regularization → entropic regularization
- The usage of $\delta$ as a regularization coefficient should be avoided as $\delta$ denotes the Dirac measure earlier.
- “Tab. 3 shows the fusion results” This sentence can be removed from Section 3.4.
- Some typos

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considered a multiple transport problem with applications in visual matching, model fusion. More particular, instead of working on OT problem between distributions, the paper considered  a sequence of ordered distributions and find the transport plan such that its circular compositions of transportation map is actually the identity map.  The authors added another regularized  function to deal with the cycle-consistency requirement, then use the entropic approach of Cuturi to deploy Sinkhorn algorithm to estimate its solution. The authors applied the methods to solve multi-point matching and multi-model fusion and demonstrated their methods for several datasets, i.e Pascal VOC, Willow, MNIST and CIFAR-10.

### Strengths
It appears to be interesting theoretical variation of OT problem. 
The authors  derived an algorithm to find its solution through the connection with the Sinkhorn algorithm. 
The experiment results show a slightly improvement to the one of using Sinkhorn algorithm.

### Weaknesses
Performance of the proposed method is incremental improvement to that of using Sinkhorn without the cycle consistency requirement.

In comparison with Sinkhorn's method, RMOT-Sinkhorn just have one more constraint for the last mapping. In fact, it is not much different from the one using Sinkhorn.

I do not agree with other two metrics, i.e CR and CACC, assessing the performance of methods, since they favor the author's method.

In the problem of multi-matching and model fusion, I do not see that the method is natural application to those problems unless the data sets have cyclical structures. From Figure 5 for example, I do not see the data have that cyclical structure, if we switch the order  of pictures of the second column and third column, does it change the final results? The most natural applications, among those presented, of the method is TSP, but the empirical result is still worse than its current SOTA result.

With the cycle consistency requirement, the problem wants a solution which is a permutation matrix at every transportation stage, since product of "transition" matrices, (all entries are non-negative),  must be equal to identity matrix. Hence the real constraint is to make the transport maps are close to permutation.  The objective function (17) is just a relaxed version of the true objective function. What is the guideline for choosing the parameter $\delta$ and $\epsilon$?

Overall, it appears to be interesting problem. But it also appears to be a slightly different version of multi-OT problems, thus it looks like an incremental solution to some current methods. The contribution to OT theory is also limited, i.e no proof of convergence property etc.

### Questions
In table 1, why does the Sinkhorn perform better than RMOT-Sinkhorn in PCA-GM in the AC index?

In table 1, column NMGM, we have CR $100\%$ but the ACC is only equal to $93.76\%$. Does it mean that the consistent rate is not a good indicator of  accuracy  rate?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a generalized form, called optimal multiple transportation (OMT), for optimal transport with multiple probability measures.
In particular, given K distribution measures and their samples, the authors organize them as a loop and consider the pairwise OT problems with a cycle-consistency regularizer. As a special case of this problem, the authors further consider applying the method to solve TSP, in which multiple push-forward steps are implemented by the multiplication of the OT plan and itself and regularized by the cycle-consistency regularizer.
A Sinkhorn-like algorithm is proposed to solve the OMT problem approximately. 
The proposed OMT is shown to be effective according to empirical results in the domains of visual point set matching and multi-model fusion.
The OMT also demonstrates the potential for solving the challenging TSP problems in probabilistic space, in contrast to traditional methods working in the distance space.

### Strengths
1. This paper is well-organized and well-written. The authors provide sufficient details about their work and easy to understand. 

2. Generalizing the optimal transport model to multiple distribution measures is an interesting and significant problem.

3. It’s interesting to see the application of OMT on the TSP problem.

### Weaknesses
1. I don’t find much novelty in the idea of minimizing the transportation costs between each pair of distributions and using the constraint $\prod^K_{k=1} \tilde{P}_k=I$  to ensure cycle-consistency. It’s also quite common to apply entropy regularization and transform the cycle-consistency into a regularizer.

2. What about the runtime efficiency of OMT? It would be nice if the authors could show the convergence curve of the proposed algorithm.

3. What about the stability of OMT? Given K sample sets/distributions, the method requires organizing the sets as a loop. Is it robust to the order of the sets? An analytic experiment should be added.

4. The baselines shown in Table 1 are relatively weak. Why don’t the authors consider multi-marginal transport as a baseline? In particular, in the sample/distribution matching tasks, many OT-based methods can be used to achieve multi-source matching, e.g., Wasserstein barycenter [1], Multi-marginal OT (MMOT) [2], and so on. 

5. I suggest the authors add a stronger ablation study about the effectiveness of the cycle-consistency regularizer. More baselines[3] should be considered in the experiment of Fig.5.

### Questions
Please see above.

### Soundness
2 fair

### Presentation
3 good

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
This paper proposes Optimal Multiple Transport (OMT), which handles the case where one needs to compute multiple optimal transports 
between several distributions that are linked together by a cyclic dependency structure (a sample from the first distribution should ‘travel’
back to its original location after being transported to several other distributions). They propose an algorithm to solve an associated optimization problem,  which is an extension of the Sinkhorn algorithm. After making links with the traveling salesman problem (TSP), they present two applications of their algorithm to visual multi-point matching and multi model fusion, where the proposed approach leads to benefits in terms of performance.

### Strengths
- The idea of enforcing consistency between multiple transport is original, neat and interesting.  
 - the transposition to the TSP problem is very interesting.

### Weaknesses
 - it is not clear if in the general setting there exist a solution to problem (8). What are the conditions for the feasible set not to be empty ?  
- lack of justifications and analyze for algorithm 1. 
- how to build a cycle (ordering of measures) is not discussed in the paper

(see my comments below)

- Existence of solution for Eq 9 should be discussed. Notably, it seems that as soon as there is mass splitting or whenever one measure has a small number of atoms, the composition (product) of couplings can not yield identity (as soon as there might be rank deficiency in the coupling matrix), and the feasible set is empty. In the reviewer’s opinion, this should be detailed or analyzed. 

- Regarding the optimization part, there is no clear justification for the alternating scheme proposed here (solving sinkhorns, then updating the cost matrix for every sub-problems). I think there might be connections to Generalized Conditional Gradients or Majoration-Minimization methods here (as the ones used in the POT library). I encourage the authors to better justify their algorithm 1. Also, what is the impact of the entropy parameter $\epsilon$ in solving the problem (10) ? How do you set it ? How many iterations wrt. K are needed for finding a solution ? In the reviewer’s opinion, this would deserve a discussion in the paper. 

- Authors do not mention the case when K=2. However, I believe that it might also be interesting. In the case where the number of samples (atoms) is the same in the two distributions (with uniform distributions), we have obviously that $P P^T = Id$ but when  mass splitting occur,  it is not always the case. What is then the impact of the regularization on the original sinkhorn problem ?  

- In the applications of OMT (visual point matching, or neural model fusion), how do you define the sequences/orderings of measures ? Are there any change in the performances if one changes this ordering (as we can expect because of the non-commutativity of coupling matrices product) ?  More generally, and as soon as K>2, I guess that the choice of the cycle (when given a set of input measures) is in itself a problem. It could be better discussed in the paper  

Minor comments
 - in Eq 7 the first k should be a capital K
- I do not really understand the difference between Eq. 10 and 17 
- Figure 3 could be enhanced to better distinguish the differences between the two versions of the transport plans, which is difficult to see at a first glance 
- p6, what do you mean by ‘… Algorithm 2 can not achieve the ideal closed-loop solution which may be
due to the simple setting of δk and too many regularized terms of closed-loop constraints’ ? 
- in Multi point matching, performance measures such as CR or CACC show a bias toward the presented method, since it directly relates to the criterion which is optimized.

### Questions
In general, I like the idea of cycle consistency argued by the paper, and the connection to TSP is very stimulating.. However, and this is preventing me from giving an higher score, there are a number of issues with this paper. Provided that some of them are solved during the discussion phase, I will be willing to change my evaluation.  Here are potential questions and remarks for the authors :

- Existence of solution for Eq 9 should be discussed. Notably, it seems that as soon as there is mass splitting or whenever one measure has a small number of atoms, the composition (product) of couplings can not yield identity (as soon as there might be rank deficiency in the coupling matrix), and the feasible set is empty. In the reviewer’s opinion, this should be detailed or analyzed. 

- Regarding the optimization part, there is no clear justification for the alternating scheme proposed here (solving sinkhorns, then updating the cost matrix for every sub-problems). I think there might be connections to Generalized Conditional Gradients or Majoration-Minimization methods here (as the ones used in the POT library). I encourage the authors to better justify their algorithm 1. Also, what is the impact of the entropy parameter $\epsilon$ in solving the problem (10) ? How do you set it ? How many iterations wrt. K are needed for finding a solution ? In the reviewer’s opinion, this would deserve a discussion in the paper. 

- Authors do not mention the case when K=2. However, I believe that it might also be interesting. In the case where the number of samples (atoms) is the same in the two distributions (with uniform distributions), we have obviously that $P P^T = Id$ but when  mass splitting occur,  it is not always the case. What is then the impact of the regularization on the original sinkhorn problem ?  

- In the applications of OMT (visual point matching, or neural model fusion), how do you define the sequences/orderings of measures ? Are there any change in the performances if one changes this ordering (as we can expect because of the non-commutativity of coupling matrices product) ?  More generally, and as soon as K>2, I guess that the choice of the cycle (when given a set of input measures) is in itself a problem. It could be better discussed in the paper  

Minor comments
 - in Eq 7 the first k should be a capital K
- I do not really understand the difference between Eq. 10 and 17 
- Figure 3 could be enhanced to better distinguish the differences between the two versions of the transport plans, which is difficult to see at a first glance 
- p6, what do you mean by ‘… Algorithm 2 can not achieve the ideal closed-loop solution which may be
due to the simple setting of δk and too many regularized terms of closed-loop constraints’ ? 
- in Multi point matching, performance measures such as CR or CACC show a bias toward the presented method, since it directly relates to the criterion which is optimized.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
