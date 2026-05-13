# IMPaCT GNN: Imposing invariance with Message Passing in Chronological split Temporal Graphs

- Decision: Reject
- Scores: 5, 3, 5, 6, 5

## Abstract
This paper addresses domain adaptation challenges in graph data resulting from chronological splits. In a transductive graph learning setting, where each node is associated with a timestamp, we focus on the task of Semi-Supervised Node Classification (SSNC), aiming to classify recent nodes using labels of past nodes. Temporal dependencies in node connections create domain shifts, causing significant performance degradation when applying models trained on historical data into recent data. Given the practical relevance of this scenario, addressing domain adaptation in chronological split data is crucial, yet underexplored. We propose Imposing invariance with Message Passing in Chronological split Temporal Graphs (\IMPaCT), a method that imposes invariant properties based on realistic assumptions derived from temporal graph structures. Unlike traditional domain adaptation approaches which rely on unverifiable assumptions, \IMPaCT explicitly accounts for the characteristics of chronological splits. The \IMPaCT is further supported by rigorous mathematical analysis, including a derivation of an upper bound of the generalization error. Experimentally, \IMPaCT achieves a 3.8\% performance improvement over current SOTA method on the ogbn-mag graph dataset. Additionally, we introduce the Temporal Stochastic Block Model (TSBM), which replicates temporal graphs under varying conditions, demonstrating the applicability of our methods to general spatial GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the problem of domain adaptation of temporal maps and proposes a method to realize the invariant property based on realistic assumptions. The method takes into account the characteristics of temporal splitting and also introduces the Temporal Stochastic Block Model (TSBM) to replicate the temporal graph under different conditions.

### Strengths
1. This paper addresses the intriguing challenge of proposing the invariant messaging function IMPaCT to tackle the domain adaptation issues in graph data that arise from temporal splitting.
2. The authors establish a framework of assumptions grounded in observable properties and introduce an invariant theory for first-order and second-order moments, which offers a robust theoretical foundation for future research.
3. The IMPaCT method demonstrates substantial improvements in classification accuracy across multiple datasets when compared to existing state-of-the-art methods, highlighting its advantages in processing graph data effectively.

### Weaknesses
1.The paper explores the problem of out-of-distribution generalization in temporal graphs; however, the INTRODUCTION section does not adequately address the unique challenges associated with this issue. The authors should elaborate on how the difficulties of out-of-distribution generalization in temporal graphs differ from those encountered in static graphs and Euclidean data (e.g., images). A clearer articulation of these challenges would enhance the understanding of the problem's significance and context.

2.There is a lack of comparison between relevant aspects of the proposed work and existing methods. Could the authors clarify how their approach measures up against current state-of-the-art techniques in the domain?

3.How is the effectiveness of the PMP and MMP in adjusting the invariance of the first moments assessed?The MMP only collects information from past nodes, which may lead to insufficient information. How do the authors explain the potential impact of this limitation on model performance?

4.On what theoretical basis is the weight adjustment of generating nodes in GenPMP based? Can the authors explain in detail how the rationality of \(P_{t_{\text{max}}}(\Delta)/P_{\tilde{t}}(\Delta)\) was determined and its impact on the results?

5.Please explain why different baselines are used on different datasets?

6.The authors assert that this paper tackles the challenge of domain adaptation in graph data resulting from temporal splitting. However, as far as I am aware, the ogb datasets are predominantly utilized for node classification in static graphs. How effectively does the proposed method perform on dynamic graph datasets, such as Tmall and MathOverflow?

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies the impact of chronological split in temporal graph learning. The authors propose a family of message passing methods named IMPaCT that accounts for the distribution shift between training and test due to the temporal effect.

### Strengths
S1. Chronological split affects the temporal graph learning's performance, and this paper aims to study this important problem.

S2. Experimental results show improvements in test accuracy.

### Weaknesses
W1. There are many related works about out-of-distribution generalization and invariant representation learning on graphs, as evidenced by several surveys and GitHub repo. It seems a bit contradicting to the authors' claim that there are not many related works. It would be great if the authors could further explain why these lines of works are not discussed.

W2. The observation about the decreasing proportion of neighbors as $|	ilde{t} - t|$ increases are mostly driven by the example in citation networks. I think this makes sense in citation networks, but it is unclear whether this trend also holds in other networks, say user-item interaction graphs in recommender systems or online social networks, where users can join or leave the system/network at any time. The authors define a function g that represents the proportion of neighboring nodes as a function that decays as $|	ilde{t} - t|$ increases, but it is unclear if this is a necessary condition for the proposed method. The paper also lacks a clear definition of the symmetricity assumption, even though it is implicitly used.

W3. It would be great if the authors could discuss what types of shift (or the discrepancy between which distributions) this paper considers in a more formal way.

W4. I am a bit confused where the authors discussed the claim: "As discussed, the target node receives twice the weight from $\tilde{t}\in\mathbf{T}^{\text{double}}_{t}$ against $\tilde{t} \in \mathbf{T}^{\text{single}}_{t}$." Could you please provide a pointer?

W5. It is questionable whether aligning first and second moment implies invariance, as skewness, tailedness, modes could all affect the shape of a distribution.

W6. Overall this paper is not self-contained. I have a hard time understanding many math notations in theorems given the lack of explanation in the main body (e.g., almost all theorems starting from theorem 4.3), and I need to check back and forth between main body and appendix to understand the paper. I believe a reorganization of the contents are needed for better clarity.

W7. The evaluation protocol is unclear to me. For example, PNY is proposed but never evaluated, so I am not sure what the purpose is to have PNY here. MMP, PMP, JJNorm is only evaluated on LDHGNN, but not on RevGAT and GAMLP, while GenPMP is not evaluated on LDHGNN. 

W8. What is the rationale of evaluating on LDHGNN, RevGAT, and GAMLP rather than classic temporal graph learning models? Also, the authors do not explain what SimTeG, TAPE, and GLEM are. Overall, the choice of baseline methods are very vague.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
1

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
This paper studies the problem of domain adaptation on temporal graph data under chronological splits. It introduced a novel IMPaCT approach to enforce invariant message passing via the 1st and 2nd moment alignments. The invariance of the proposed invariant message passing is theoretically analyzed. Experimental results also demonstrated the effectiveness of the invariance regularizations on real-world temporal graphs.

### Strengths
**Originality:** This paper studied the issues of chronological splits in applying GNNs to temporal graphs. It empirically observed the distribution shifts induced by the chronological splits. Then a novel IMPaCT was proposed by enforcing invariant node representation learning. Both the 1st and 2nd moments of aggregated messages were leveraged to improve the feature invariance. 

**Quality:** Theoretical analysis showed the invariance of the iterative message aggregation using the proposed approaches. Besides, the generalization error bound based on the Wasserstein-1 distance was derived to show the impact of invariant message aggregation.


**Clarity:** The motivation of the studied problem was clear. The issues of chronological splits were validated in several real-world temporal graphs. 


**Significance:** The developed theoretical analysis and algorithms extended the applications of GNNs from standard static graphs to temporal graphs under distribution shifts.

### Weaknesses
(W1) The defined approximate expectation $\hat{\mathbb{E}}[M^{k+1}_v]$ requires the IID assumption of $X_w$. This assumption is not justified on temporal graphs. Specifically, the features of nodes at different time steps are unlikely to be independent and identically distributed, as temporal dependencies are inherent in the data. The assumption that $X_w \overset{\text{IID}}{\sim} {x_{\tilde{y}\tilde{t}}^{(k)}}$ for all $w \in \mathcal{N}_{v}(\tilde{y}, \tilde{t})$ is a strong one that needs further justification or relaxation.

(W2) Theorem 4.1 and Theorem 5.1 show that PMP layers result in the invariance if the previous representation is invariant. It is unclear how the invariance of the initial representation can be guaranteed. If the previous representation is not invariant, will the aggregation of PMP layer worsen the invariance? The theorems provide a conditional guarantee, but the practical implications of non-invariant initial representations are not fully addressed. It is crucial to understand how deviations from initial invariance affect the overall performance and convergence of the proposed method.

(W3) Another concern is the related work and baselines in the experiments. Graph domain adaptation and temporal GNNs have been studied in recent years. Those works can be discussed in the related works, and recent graph domain adaptation and temporal GNNs can be employed as the baselines to validate the effectiveness of the proposed approaches. The lack of comparison with existing methods in these areas makes it difficult to assess the true novelty and performance gains of the proposed approach. Specifically, it is important to compare against methods that explicitly address domain shifts in temporal graphs, not just general GNN baselines.

### Questions
(1) It is confusing why the target node receives twice the weight from $\tilde{t} \in \mathbf{T}_t^{double}$ against $\tilde{t} \in \mathbf{T}_t^{single}$.

(2) The generalization error bound depends on $C$ and $V$ defined in Section 4.3. The tightness of the derived generalization error bound can be further illustrated. As shown in lines 311-314, $V$ can be large in some cases.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses domain adaption issues in graph data, particularly in datasets where the train and test splits are organized chronologically. The proposed method, named IMPaCT, assumes the separability of relative connectivity among nodes in the graph at different time points. Based on this assumption, the authors impose the invariance property in message-passing methods and provide various theoretical analyses on the generalization error.

### Strengths
- The paper is well structured, clearly presenting the problem and the proposed solution. The theoretical foundation of the proposed methods is robust, and experiments are presented to demonstrate their effectiveness.
- If we accept the correctness of the assumptions, especially Assumption 3 regarding the separability of relative connectivity, the proposed idea is quite intuitive. That is, if the first moment of the previous representation remains invariant over time t, the expectation of the aggregated message can be independent of t when the target node (label y, time t) receives information twice from neighbors in T_{single}.

### Weaknesses
The Assumption 3 may raise the following issues:
- Ensuring invariance of 1st moment of the previous representation: the authors introduce Assumption 2 to address this concern. If the 1st moment of the previous representation is not invariant, how can the invariance of the aggregated message be maintained. How to ensure the 1st moment of initial features of graph nodes invariant? Specifically, the paper does not provide any theoretical guarantee that the initial node features will have invariant first moments across different time steps. This is a critical gap, as the entire method hinges on this assumption. If the initial features are not invariant, the subsequent message passing steps, even with the proposed modifications, may not lead to the desired domain adaptation.
- Effectiveness of graph modification: While modifying the original graph may benefit average message passing procedure, this approach might not be effective for other frameworks, such as Graph attention network or Message passing neural networks, where the weighting of average procedures is not independent of time t. The method's reliance on simple averaging makes it potentially unsuitable for more complex GNN architectures that use learnable weights or attention mechanisms. These architectures can adapt to temporal changes in the graph structure and node features, and the proposed modification might interfere with their learning process. For instance, in a graph attention network, the attention weights are dynamically computed based on node features and graph structure, and modifying the graph structure might disrupt the attention mechanism's ability to capture relevant information.

Minor comments:
- Line 852: Equation (30) may contain a typo.
- Line 1737, Equation (161), do P on the left-hand side and right-hand side refer the same one?
- in Subsection 6.1, the def of f(y,t) from Assumption 3 is not provided

### Questions
- See Weaknesses above.

### Soundness
3

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
4

### Summary
The paper addresses non-stationary behaviors observed at the temporal boundaries of temporal graphs. Specifically, it proposes weighting techniques to adjust message-passing operations, enabling the learned representations to maintain a degree of invariance over time. While the novelty is reasonable rather than groundbreaking, I appreciate the effort to tackle these issues, as I am not aware of other papers that address them explicitly.

### Strengths
- Addressing biases introduced by data partitions is a relevant and valuable challenge.
- Some of the proposed techniques are demonstrated effective in mitigating the targeted issues.

### Weaknesses
 - The paper presentation does not appear mature enough for publication.
- The math appears insufficiently rigorous.
- The proposed methods are limited to a specific family of message-passing operators that rely on average aggregation, without accommodating more complex methods like attention or target node-dependent messages.
- Some of the experiments are not convincing.



### Questions
Questions.
- The concept "Relative connectivity $\mathcal P$" is not clearly introduced. Does it represent the empirical distribution of edges across time and node classes?
- Where does the randomness associated with  $x_{yt}^{(k)}$ come from? Does it originate solely from the system model generating the node features? 
- Eq 7. Why is "IID"? It looks to me that they are not "identically distributed" as they depend on $k$, $y$ and $t$, nor independent due to the message passing.
- Eq 28, part b is said to be an approximation. If so then the equality symbol should not be used. Could you clarify in the paper which steps involve approximations and which provide strict equalities?
- Line 219 is in contrast with assumption 3. If the probability decays then the two contributions do not match. Am I missing something here? How can this apparent contradiction be reconciled?
- Training times in Table 3. How is it possible that training for 200 epochs takes only a fraction of a second? Why does PMP on SGC take less time than the baseline? 
- PNY and JJnorm on GCN have extremely long training times (about 500 X more than the others), which is concerning. Could you comment on it?
- Results on OGB-mag data are around 90% accuracy which does not appear in line with their website reporting ~57% for leading models. Could you elaborate on this?
- How difficult is it to port the designed techniques to more general message-passing operators and to apply them to the methods leading the OGB benchmarks?
- I could not find a discussion about the extent to which trainable model parameters within the message passing impact the proposed weighing techniques. Could you elaborate?
- Line 22. Which "unverifiable assumptions" are you referring to exactly?
- Line 128 "data from different environments may have interdependencies, and the extrapolating nature of environments complicates the problem." is completely unclear to me. Could you clarify it?


Further comments and suggested improvements:
- The addressed temporal graph learning problem is not formally stated. It becomes clear only once the datasets are presented. I suggest providing a thorough formulation and introducing there the adopted notation. In this regard, I suggest formulating a more general message passing involving a temporal graph so that the reader can relate to it the new methods later on.
- Figures 2 and 3 are not super informative and, in my opinion, unnecessary. Figure 2 only shows a decay along the temporal semi-axes - a concept that could be given for granted. Figure 3 is not accompanied by a description. 
- Denoting a distribution as $x_{yt}^{(k)}$ is rather confusing. 
- One important element is that the non-stationary behavior (here called invariance - which, by the way, I don't think is the most appropriate term to use here) comes from the edges rather than the node features, as per the assumptions made. However, such dependency from the edges does not emerge from the math developments. 
- What does "discrete value" mean in A.4? They are indeed positive integers.
- The term "persistent" in 4.1 is unclear.
- Table 3. Please provide variability indices (eg, std) alongside results.
- Decoupled GNN seems to not be introduced or referenced.

### Soundness
2

### Presentation
1

### Contribution
2
