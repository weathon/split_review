# Federated Dynamical Low-Rank Training with Global Loss Convergence Guarantees

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 5, 8, 5, 5

## Abstract
n this work, we propose a federated dynamical low-rank training (FeDLRT) scheme to reduce client compute and communication costs - two significant performance bottlenecks in horizontal federated learning. Our method builds upon dynamical low-rank splitting schemes for manifold-constrained optimization to create a global low-rank basis of network weights, which enables client training on a small coefficient matrix. A consistent global low-rank basis allows us to incorporate a variance correction scheme and prove global loss descent and convergence to a stationary point. Dynamic augmentation and truncation of the low-rank bases automatically optimizes computing and communication resource utilization. We demonstrate the efficiency of FeDLRT in an array of computer vision benchmarks and show a reduction of client compute and communication costs by up to an order of magnitude with minimal impacts on global accuracy.
\renewcommand{\thefootnote}{\fnsymbol{footnote}}

\footnotetext[1]{{
This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes. The Department of Energy will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan(\url{http://energy.gov/downloads/doe-public-access-plan}).}
\renewcommand{\thefootnote}{\arabic{footnote}}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the FeDLRT algorithm to jointly reduce client compute and communication cost in Federated Learning (FL). The method consist in estimating a global low-rank basis of network weights and constraing local client optimization to that manifold, with an optional variance-reduction term applied to local updates.
The work presents a convergence proof of the proposed algorithms and variants for non-convex objectives in full participation, demonstrating that FeDLRT achieves state-of-art linear convergence rate.
Experiments include theoretical settings (linear least squares regression) and computer vision setup (CIFAR-10 with ResNet-18/AlexNet/VGG and CIFAR-100 with ViT), and are convincing in showing the effectiveness of the proposed approach.

### Strengths
- The approach has strong theoretical guarantees, and the empirical results seems matching the theory;
- The method jointly reduces communication cost and client compute, since clients only optimize smaller matrices w.r.t. full weights

### Weaknesses
 - **Poor introduction of the premises for the algorithm:** in my opinion the second part of section 2 is not clear enough in explaining the concepts the proposed algorithm is based on. In particular, it is not evident which technical innovations this work brings with respect to previous works. Authors are encouraged to dedicate more space to discuss how this work build on previous concepts and how it advances the state of the art. Specifically, the motivation for introducing a global low-rank basis, instead of allowing each client to have its own, is not sufficiently justified. While the authors mention the computational cost of SVD, this seems insufficient as the SVD would be performed on the server, which is typically assumed to have high computational resources. The benefits of the global basis in terms of convergence guarantees should be more clearly articulated, especially in contrast to methods that train only low-rank components on clients.
- **Poor comparison with other approaches:** the proposed method is compared essentially only with FedLin and FedAvg, while many methods exist in the categories the authors outline in the introduction ((i) methods that only communicate compressed updates and (ii) methods that reduce by also learning low-rank factors). Other related methods in this area are correctly cited but not well-discussed and not considered in the evaluation, such as FedPara [1], FedDLR [2], FEDHM [3]. Additionally, related papers that I believe should be included and discussed are LBGM [4] and FetchSGD [5]. The comparison should not only focus on the communication cost but also on the computational cost at the client and server side, as well as the memory footprint. A more detailed comparison with methods like LBGM [4], which also uses a global basis and provides convergence guarantees, is necessary. Furthermore, the authors should discuss the differences in the convergence analysis and assumptions compared to these methods. Another line of works that should be considered is subnetwork training in FL, for example FjORD [6], which achieves training and communication efficiency by locally training subnetwork via Ordered Dropout.


### Questions
- Could you better describe the relationship with respect to the above related works both regarding the methodology and the convergence guarantees?
- What are the assumptions regarding statistichal heterogeneity for the convergence of FeDLRT? I did not find an equivalent of the common "bounded gradient dissimilarity" assumption for the low-rank training of the proposed method, and I wonder what are the guarantees in heterogeneous FL
- With respect to the previous question, can you propose some experiments similar to the ones presented for real-world dataset (e.g. CIFAR-10 with ResNet18) in heterogeneous cases (e.g. Dirichlet split as standard)? I would like to see an assessment of the performance of the proposed methods in non-convex case on real-world dataset, as opposed to the (valuable) results already provided for the linear squares regression in figure 1.

**Other suggestions:**
- **Presentation of theoretical results:** Theorems 1,2 and 5 should be lemmas in my opinion, since they are intermediate results necessary for the convergence rates. Please evaluate providing also a more in-depht discussion of these results
- **Organization of figures:** figure 6 in hardly readable in a printed version of the manuscript. Please evaluate enlarging the font size as well as the size of the overall figure. Alternatively, results in tabular form could be an option. I also suggest not to put wrap figure 4 in the text, as it makes the text less readable.
- **Empirical validation of assumption 1:** I think that and empirical validation of assumption 1 could benefit the clarity and the robustness od the paper. While the assumption seems reasonable in homogeneous cases and the corresponding methods seems pretty equivalent in performance in the provided experiments, I expect statistical heterogeneity to play a role in this matter. Could you plot the quantity in the LHS of eq. 14 in one of the real-world experiments of your setup (e.g. CIFAR-10 with ResNet18), in iid and non-iid conditions?

### Soundness
3

### Presentation
2

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
The authors introduce a strategy (FeDRLT) for federated training which enables cheaper communication and client computational costs by training over low-rank decompositions of weights. Their algorithm includes a variance correction term to reduce client drift. The convergence of DRLT is $\mathcal{O}(1/T)$ with respect to minimal gradient norm. The authors perform LLSR and CIFAR-10 experiments of FeDRLT against FedLin and pure FedAvg, which performs respectably.

### Strengths
-Very clear narrative and motivation. Bi-directional compression is very desirable for FL and still a relatively open problem. 

-The experiments perform very well against full-sized counterparts. The variance correction alleviates client drift and enables greater numbers of client participation.

-The convergence rate is good and clear proofs are provided for all guarantees. 

-The technique seems like a new approach to low-rank FL and comes equipped with an interesting variance reduction mechanism. As bi-directional compression is still relatively rare in the compressive FL landscape, this work could be valuable, but please see weakness.

### Weaknesses
 -The work is at worst incremental and at best, not adequately compared against similar efforts. The authors must compare against one or more compression works which shrink the gradient and/or weights. These works include FetchSGD [1] (gradient compression), ComFetch [2] (bi-directional compression + correction), Fjord [3] (model splitting), LASER [4] (gradient compression, HeteroFL [5] (model splitting), PriSM [6] (model splitting), etc. The field of compressive FL is rich (and saturated) and the methods described in the paper are reminiscent of other approaches. 

-The variance correction mechanism is not a novel approach for compressed federated learning. In FL, sometimes this approach is referred to as "error feedback," and is necessary for most compression techniques [5] to compensate for reconstruction error, but doubles as a client-drifting mechanism as it is aggregated over all clients. See [6] for another mechanism and general discussion of variance reduction for distributed SGD. The authors should comment their approach in light of this existing literature. 

-The experiments are weak. LLSR is insufficient nowadays to demonstrate the efficacy of an FL algorithm. Although CIFAR-10 and CIFAR-100 experiments are conducted, it does not appear that there is any ablation over varying degrees of heterogeneity, which is absolutely necessary for a work which is attempting to combat client drift. The authors should ablate over varying Dirichlet allocations of classes and compare their algorithm to a few other compression works or at least mimic their setups and compare cited numbers.

### Questions
See Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a federated dynamical low-rank training (FeDLRT) approach aimed at reducing both compute and communication costs for clients in horizontal federated learning, addressing two key bottlenecks in this field. FeDLRT leverages dynamical low-rank splitting methods to construct a shared, global low-rank basis for network weights, enabling clients to train on a much smaller coefficient matrix rather than the full model. The global low-rank basis remains consistent across clients, allowing for an integrated variance correction scheme and ensuring convergence to a stationary point. Additionally, FeDLRT dynamically adjusts the rank through augmentation and truncation, optimizing resource usage in real-time.

The authors validate FeDLRT’s effectiveness on various computer vision benchmarks, demonstrating significant reductions—up to an order of magnitude—in both client compute and communication requirements, while maintaining high accuracy.

### Strengths
Overall, the paper is well-structured and clearly written, making it relatively easy to follow the development of ideas and contributions. The flow of the narrative allows readers to engage with the paper’s content without difficulty. 

The inclusion of thorough discussions between technical sections, such as detailed explanations following each lemma and theorem, is particularly valuable. These discussions help clarify the purpose and implications of the theoretical results, making the technical content more accessible and aiding readers in understanding the significance of each result within the broader context of the paper.

The algorithm is presented effectively, with a well-organized description and clear pseudo-code. This clarity in presentation facilitates understanding of the method and makes it easier for others to replicate or build upon the approach.

Additionally, the paper includes an extensive experimental section in the appendix, showcasing a wide range of deep neural network (DNN) experiments. This supplementary section broadens the paper’s experimental validation, demonstrating the versatility and effectiveness of the proposed method across various architectures and datasets. The breadth of experiments contributes to a more comprehensive evaluation, which is especially beneficial for readers interested in practical applications of the theoretical findings.

### Weaknesses
1. **Abstract Length and Clarity**: The abstract is brief and could be expanded to provide a clearer, more comprehensive overview of the main ideas and contributions of the paper. Currently, it may be difficult for readers to fully grasp the paper’s objectives and significance from the abstract alone.

2. **Introduction and Literature Review**: Both the introduction and the literature review sections are quite short and lack depth. An expanded literature review would provide readers with a better understanding of the existing work in the field and how this paper’s contributions fit within that context.

3. **Client Drift Reduction Methods**: The paper does not discuss several important client drift reduction techniques, such as ProxSkip, S-Local-SVRG, and 5GCS. Notably, S-Local-SVRG predates FedLin and introduces essential concepts for handling client drift. The TAMUNA method also offers communication acceleration, variance reduction, and client drift correction through compression, which could provide useful context for this paper.
    - References:
        - Mishchenko, Konstantin, et al. "Proxskip: Yes! local gradient steps provably lead to communication acceleration! finally!." International Conference on Machine Learning. PMLR, 2022.
        - Hu, Zhengmian, and Heng Huang. "Tighter analysis for proxskip." International Conference on Machine Learning. PMLR, 2023.
        - Gorbunov, Eduard, Filip Hanzely, and Peter Richtárik. "Local sgd: Unified theory and new efficient methods." International Conference on Artificial Intelligence and Statistics. PMLR, 2021.
        - Grudzień, Michał, Grigory Malinovsky, and Peter Richtárik. "Can 5th generation local training methods support client sampling? yes!." International Conference on Artificial Intelligence and Statistics. PMLR, 2023.
        - Condat, Laurent, et al. "TAMUNA: Doubly Accelerated Federated Learning with Local Training, Compression, and Partial Participation." International Workshop on Federated Learning in the Age of Foundation Models in Conjunction with NeurIPS 2023.

Could you please add a comparison in the table that includes not only the mentioned papers but also other relevant works? This would provide a more comprehensive view of the existing literature and allow readers to better understand how your approach stands in relation to other methods.

4. **Compression in Federated Learning**: The literature review would also benefit from mentioning works on local methods for federated learning that incorporate compression. This line of research is relevant for addressing communication efficiency, an area where this paper aims to contribute.
    - Relevant papers:
        - Haddadpour, Farzin, et al. "Federated learning with compression: Unified analysis and sharp guarantees." International Conference on Artificial Intelligence and Statistics. PMLR, 2021.
        - Li, Zhize, et al. "SoteriaFL: A unified framework for private federated learning with communication compression." Advances in Neural Information Processing Systems 35 (2022): 4285-4300.
        - Meinhardt G. et al. Prune at the Clients, Not the Server: Accelerated Sparse Training in Federated Learning //arXiv preprint arXiv:2405.20623. – 2024.

5. **Notation and Formulation**: The notation used in the formulation is non-standard and may confuse readers. The symbol $ C $ is commonly used to denote the client cohort size (i.e., the mini-batch size of clients), while other symbols like $ M $ or $ n $ are often used for the total number of clients. Changing this notation would improve clarity.

6. **Client Drift Correction Communication Requirements**: The paper mentions that client drift correction requires additional communication. However, recent work, such as ProxSkip and SCAFFOLD, shows that client drift correction can be achieved without extra communication. Referencing these methods and discussing this point would clarify the communication requirements of different approaches.

    - Reference: Yu, Yaodong, et al. "TCT: Convexifying federated learning using bootstrapped neural tangent kernels." Advances in Neural Information Processing Systems 35 (2022): 30882-30897.

7. **Lipschitz Continuity of Gradients**: The paper's assumptions about Lipschitz continuity (or \( L \)-smoothness) of gradients are not rigorously defined. It would be helpful to clearly state these assumptions to ensure they align with the rest of the analysis.

8. **Clarity of Lemma 1**: The statement of Lemma 1 is somewhat unclear. To improve readability, it would be beneficial to make this lemma more rigorous and precise.

9. **Theorem 1**: Theorem 1 is also ambiguously stated, particularly regarding the meaning of the inequality provided. Adding a discussion to explain the significance of this inequality and how it relates to the paper's objectives would be beneficial.

10. **Theorem 2**: Similar to Theorem 1, Theorem 2 is stated in a way that may be confusing to readers. Providing a clear interpretation of the inequality and its implications would enhance understanding.

11. **Convergence Rate in Theorem 3**: In Theorem 3, the first term exhibits a convergence rate of \(1/T\), but the second term does not decrease (even with a diminishing step size). This contrasts with other methods that correct for client drift, which offer convergence guarantees to the exact minimizer without residual noise or error terms. It would be helpful to explain why this residual term persists in the analysis.

12. **Assumption 1**: Assumption 1 appears restrictive but lacks commentary. Including a discussion on the motivation and implications of this assumption would clarify its role in the analysis and inform readers about its necessity.

13. **Clarity of Theorem 4**: Theorem 4 is somewhat confusing, especially regarding the inequality it presents. A more thorough explanation of this inequality and its relevance to the paper’s objectives would be beneficial.

14. **Corollary 1 Convergence Rate**: Similar to Theorem 3, Corollary 1 includes a term with a convergence rate of \(1/T\) but also a second, non-diminishing term, even with a decreasing step size. Notably, other client drift-correction methods guarantee convergence to the exact minimizer without such persistent error terms. Discussing this difference would improve clarity.

15. **Connections to Strongly Convex or PL Cases**: The current theoretical results are limited to the general non-convex setting, which tends to yield conservative bounds. There are no results for strongly convex, convex, or PL-conditioned non-convex cases, though the first set of experiments is on a linear regression task, a convex problem. Clarifying how the theoretical findings connect to the experiments would enhance coherence between the theory and practical validation.

### Questions
Please check Weaknesses section

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this work, the authors propose a new algorithm to perform the task of horizontal federated learning. In this particular setting, all clients share the same model architecture and data features. The compute available on the client side is fairly limited and the costs associated with the communication between the central server and the clients are expensive. Current state of the art federated learning algorithms suffer from memory, compute and communication costs that scale quadratically with the size of the problem. 

To address the aforementioned issues, the authors propose a federated dynamical low-rank training scheme (FeDLRT) with and without variance correction, incorporating both a full and a simple variance correction method. The proposed method transfers only low-rank factors between the server and clients, hereby reducing the communications costs as compared to traditional methods. Furthermore, each client optimize over a small coefficient matrix. The memory, compute and communication costs of FeDLRT scale linearly with $n$. 

The authors provide convergence result of their algorithm with full and simple variance correction schemes. To show the convergence guarantees to a stationary point, the work assume that the client and server-side loss functions are $L$-smooth but not necessarily convex. Finally, the authors demonstrate the efficiency of FeDLRT in an array of computer vision benchmarks and show a reduction of client compute and communications costs up to an order of magnitude with minimal impacts on global accuracy.

### Strengths
1) This work is well motivated. The challenges faced in horizontal federated learning are clearly stated and this work introduces a new algorithm to address these issues.

2) Computational results are promising.

3) Authors provide convergence results for their algorithm.

### Weaknesses
1) The authors compare the computational costs of their scheme with 3 algorithms in table 1. However, in their experiments their only compare with FedLin. It would be helpful to compare their work with the other algorithms.

2) The description of the algorithm (section 3.1) can be improved. The authors should try to explain each step of their algorithm better. Also Algorithm 2 (which is not an algorithm) is placed in the appendix. As far as I noticed, there is no mention of Algorithm 2 in main body of the paper. Yet Algorithm 2 contains the important definitions/notations that are used throughout section 3.1. The authors can consider adding all these concepts in Section 3.1 while they explain the algorithm.

### Questions
1) As mentioned in table 1, FeDLRT enjoys a lower computation, memory and communication costs that scales linearly with $n$ unlike other current algorithms. This is a significant strength of this work so it might be helpful to mention this in Section 1. 

2) (line 210) If there is no page limit, it might be helpful to add the proof of lemma 1 or a sketch of the proof to the main body of the paper.

3) (line 210) If i understand correctly, using Lemma 1 the authors are able to reduce the communication costs. This could be explained in more detail.

4) (Figure 1) You can consider placing Figure 1 on page 6.

5) It would be interesting to see computational results with different singular value truncation threshold. This could be added or the effect could be explained briefly (if there is a page limit). Further, how is this selected?

6)  Many plots in this paper can be improved for neatness and clarity.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper considers federated learning training with dynamical low-rank training scheme that allows to reduce both computations, since the training is performed directly in the low-rank space, as well as communications as only low-rank representations of neural networks need to be communicated instead of the full layers. This allows for efficient training in the low-resource & low-communication FL setup.

### Strengths
The paper is well written and easy to follow.
The paper provides proof of convergence of their proposed method when local gradients on clients are deterministic.
The paper provides a way of combining their algorithm with variance correction due to difference in data distribution on different clients.
The paper provides experimental verification of their proposed method.

### Weaknesses
1. The paper provides convergence guarantees for their method only if the gradients are deterministic, which is limiting the potential applications of their algorithm. Specifically, the analysis does not account for the stochasticity inherent in mini-batch gradient descent, which is the standard practice in training neural networks. This significantly restricts the practical relevance of the theoretical results.

Experimental evaluation is limited:

2. Experimental results are provided only for the artificial dataset, and for cifar 10 and cifar 100 datasets, which are not FL-related benchmarks. Evaluating on more realistic FL datasets, such as [R1, R2] would make the paper stronger. The current benchmarks do not adequately represent the challenges of real-world federated learning scenarios, particularly in terms of data heterogeneity and client availability.

3. Paper does not give all of the details of experiments, thus not reproducible. Several key details that are missing:
3.1. How learning rate was chosen in Cifar-10 experiments
3.2. How the data was split across the clients in Cifar-10 experiments.
3.3. On Cifar-10 experiments first warm-up is performed on 1 client, but how that 1 client was chosen is not mentioned in the paper.

4. Paper does not tune the learning rate, but uses the same learning rate for different algorithms - that might give advantage to some algorithms. Tuning the learning rate is needed for fair comparison. The lack of per-algorithm hyperparameter tuning makes it difficult to assess the true potential of the proposed method relative to existing baselines.

5. Paper shows only 93% of accuracy of Cifar10 for 32 workers (I believe it is coming from suboptimal stepsize schedule that is just constant over training), which is quite low and quite far from stoa Cifar10 accuracy. Analysis of how close the proposed algorithm can reach to stoa accuracy is missing.

### Questions
1. In table 1, what is “b”? I think “b” was not introduced before. Is it a batchsize? 
2. Why in Figure 6, when clients increase from 1 to 4 , accuracy increases, but later decreases? This is not intuitive to me. 
3. It is also not very intuitive to me - why does the accuracy drop with a larger number of clients? Since with larger number clients, the number of local steps is smaller, it might point to the better performance of methods without variance reduction, such as FedAvg. I am also wondering if such behavior comes from suboptimal choice of hyperparameters. 
4. Could you also plot confidence intervals together with the median? 
5. Table 1 is slightly too small, if printed on the paper. 
6. I did not fully understand the algorithm. Why do you need to do basis augmentation and what does it mean? Also why is the $\tilde S^\star$ not diagonal?

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
3

### Summary
To reduce client computing and communication costs, this paper proposes a dynamic low-rank training method. The algorithm creates a global low-rank basis of network weights, enabling client training on a small coefficient matrix. This paper also gives the theoretical convergence guarantee of the algorithm with the variance correction scheme.The authors provide empirical validations on the theoretical results as well.

### Strengths
1. The proposed method is well-motivated, the paper reduces the number of training parameters using the dynamic low-rank approximation method with less performance sacrifice.
2. This paper gives the convergence analysis of the federated dynamical low-rank training (FeDLRT) method.
3. The empirical results show that the federated dynamical low-rank training (FeDLRT) method is better than FedLin.

### Weaknesses
1. The method only considers the full participation case without partial participation.
2. In addition to FedLin, other low-rank training methods should be considered such as [1].
3. In experiments, the number of clients is too small. In more realistic settings, more clients and partial participation should be considered.

### Questions
See in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3
