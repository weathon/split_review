# Annotation Efficiency: Identifying Hard Samples via Blocked Sparse Linear Bandits

- Decision: Reject
- Scores: 5, 3, 6, 8

## Abstract
{
This paper considers the problem of annotating datapoints using an expert with only a few annotation rounds in a \textit{label-scarce} setting. We propose soliciting reliable feedback on difficulty in annotating a datapoint from the expert in addition to ground truth label. Existing literature in active learning or coreset selection turns out to be less relevant to our setting since they presume the existence of a reliable trained model, which is absent in the label-scarce regime. However, the literature on coreset selection emphasizes the presence of difficult data points in the training set to perform supervised learning in downstream tasks~\citep{mindermann2022prioritized}. Therefore, for a given fixed annotation budget of $\mathsf{T}$ rounds, we model the sequential decision-making problem of which (difficult) datapoints to choose for annotation in a sparse linear bandits framework with the constraint that no arm can be pulled more than once (\textit{blocking constraint}). With mild assumptions on the datapoints, our (computationally efficient) Explore-Then-Commit algorithm \texttt{BSLB} achieves a regret guarantee of $\widetilde{\mathsf{O}}(k^{\frac{1}{3}} \mathsf{T}^{\frac{2}{3}}   +k^{-\frac{1}{2}} \beta_k + k^{-\frac{1}{12}} \beta_k^{\frac{1}{2}}\mathsf{T}^{\frac{5}{6}})$ where the unknown parameter vector has tail magnitude $\beta_k$ at sparsity level $k$. To this end, we show offline statistical guarantees of Lasso estimator with mild Restricted Eigenvalue (RE) condition that is also robust to sparsity. Finally, we propose a meta-algorithm \texttt{C-BSLB} that does not need knowledge of the optimal sparsity parameters at a no-regret cost.  We demonstrate the efficacy of our \texttt{BSLB} algorithm for annotation in the label-scarce setting for an image classification task on the PASCAL-VOC dataset, where we use real-world annotation difficulty scores.
}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the challenge of efficiently annotating data points under the constraints of limited annotation rounds in a label-scarce environment. It proposes a novel methodology that integrates expert feedback on the difficulty of annotating specific data points, leveraging a sparse linear bandits framework. This approach focuses on selecting the most informative samples to annotate, which optimizes the use of scarce expert resources by prioritizing data points that are both challenging and representative. Theoretical results show the sub-linear regret of the proposed BSLB algorithm.

### Strengths
1. The application of sparse linear bandits to annotation in a label-scarce environment addresses a significant practical problem in machine learning, particularly in situations where acquiring labeled data is expensive or logistically difficult. 
2. Introducing blocking constraints into the bandit problem formulation is novel and aligns well with practical scenarios where data points cannot be repeatedly annotated.
3. This paper provides a rigorous theoretical analysis on the regret which quantifies the efficiency of the BSLB algorithm. This analysis is backed by proofs that demonstrate how the algorithm effectively balances exploration and exploitation under sparsity and blocking constraints.

### Weaknesses
1. It would be beneficial to make a more thorough comparison with the works that do not assume blocking constraints. Is there any instance where the blocking constraints would clearly fail for those existing algorithms like Hao et al. (2020)? Specifically, the paper should elaborate on how the exploration strategies of existing sparse linear bandit algorithms would be impacted by the blocking constraints. For instance, if an algorithm relies on sampling from a distribution over arms and the blocking constraint prevents resampling, how would this affect the algorithm's ability to explore the arm space effectively? A more detailed discussion of this would be beneficial.
2. It would be good to move the definition and description of regret being concerned earlier in the paper. It might confuse the readers with the discussion on the regret without knowing what regret is being considered. The paper should explicitly define the regret being used, including the specific comparison being made (e.g., against the best fixed action in hindsight, or against an oracle policy). This definition should be placed before any discussion of the regret bounds to ensure clarity.

### Questions
Is it possible to make some modifications to the existing sparse linear bandit algorithm to accommodate the blocking constraints? What are the key difficulties that the blocking constraints add to the problem?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studied a sparse linear bandit problem with an additional blocking constraints, i.e., no arm can be pulled more than once. The authors developed an explore-then-commit-type of algorithm which achieves a T^{2/3} regret guarantee with known sparsity level (and under certain assumptions). The authors also developed a corralling algorithm to deal with cases without knowing the sparsity level.

### Strengths
It is nice to see that the authors develop their theoretical guarantees considering the effect of the tail magnitude $\beta_k$ at sparsity level $k$. The authors also provide a corralling algorithm to deal with cases without knowing the sparsity level.

### Weaknesses
1. While the authors spend some efforts in trying to formulate their problem as a data labeling problem with a small labeling budget, I felt such setting is different from the problem the authors actually studied --- a sparse linear bandit problem with an additional blocking constraints. For instance, the objective of the proposed algorithm is to label data points that are hard to label to minimize the regret (covering the space was not the objective even though the proposed algorithm did that in order to minimize regret). But the objective of data labeling should be to learn a good classifier/regressor, which is inconsistent with your definition of the regret. Why not just formulating the problem as a sparse linear bandit problem?
2. The proposed algorithm only achieves a T^{2/3}-type of regret guarantee, which could be sub-optimal as a \sqrt{T}-type of guarantee is expected. Or the authors should provide a lower bound indicating that their guarantee is near-optimal in their setting.
3. In experiments, the proposed algorithm is completed in two rounds: exploration and exploitation. What about other active learning algorithms? Additionally, how do the other baselines incorporate the feedback on the hardness level? I'm also curious why the method of labeling all data points is outperformed by you algorithm in the hard-valid case.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper considers the problem of minimizing the regret between the hardness of the $T$ selected points and the top $T$ data points that have the top hardness, where $T$ is the budget number of rounds for the human experts to label. The paper treats each data point in the dataset as an arm (using linear bandit) and assumes a blocking constraint that each arm can only be pulled at most once. When the human expert is asked to label the data point, he/she is also asked to provide the hardness of this data point, which is assumed to have noise. The paper proposes an algorithm similar to explore-then-commit to solve the above problem and theoretically prove the upper bound of the algorithm. It also proposes another meta-algorithm that assumes less knowledge of the sparsity of the bandits. Finally, it compares its algorithm with other baselines algorithms using various datasets.

### Strengths
1. This paper has a strong theoritical guarantee for the algorithms it propose.
2. It compares its algorithm with various datasets, ranging from image, texts, and traditional ml datasets.

### Weaknesses
1. The motivation and problem setting confuse me, especially for the paragraph from line 67 to line 76. Does the label-scarce regime only applies to the assumption that 'each arm can be pulled at most once'? What are other specialities about this regime. This regime is also kind of broad as many active learning framework is under the assumption that the label is scarce so we want to actively choose valuable data points to sample. Can the authors also elaborate on what the exact use cases of the setting considered in the paper can be applied to the recommendation of perconalized products as described in that paragraph?
2. The assumption that the human will provide noisy hardness is valid, but given this assumption, why do the authors not consider the labels provided by the human expert are also noisy? Can the authors provide more insights or explicit explanations on possible noisy labels?
3. It also feels that the labels provided by the human expert is irrelevant in the problem setting as both the problem formulation and algorithm 1 focuses on getting the human feedback for the hardness $r$ rather than mentioning about the labels. If that is the case, will it be possible to just asking the users for the hardness of the datapoint? How will this affect the algorithm?

### Questions
1. What does a reliable trained model mean, does it mean the training data is 100% accurate or something else?
2. why this reliable trained model is absent in the label-scarce setting?
3. what kind of label does the human expert provide to the model? binary or multi-class?
4. Perhaps it is trivial, can the authors explain why the noise $\eta_t$ disappears from equation 1, is it due to condition 1 in line 191? But since equation 1 is not an expectation term, it confuses me. 
5. can the authors explain the technical difficulty in the lower bound, though it mentions that it is an open problem in the end. What is the "most likely" lower bound for this problem? As the authors mention that the upper bound could be improved to $T^{\frac{1}{2}}$.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the sample selection problem in active learning when the label budget is limited. The main contribution is to model this problem as a sparse linear bandit with a blocking constraint. To address this challenge, the authors propose an explore-then-commit algorithm incorporating several novel ingredients. Theoretical analysis demonstrates that the proposed algorithm achieves an $O(k^{1/3} T^{2/3} + k^{-\frac{1}{12}} \beta_k^{1/2} T^{5/6})$ bound and experiments are conducted to validate the effectiveness of the proposed method.

### Strengths
- The paper presents an interesting formulation of the sample selection problem in active learning as a sparse linear bandit problem. Several innovative techniques are introduced to derive an algorithm with theoretical guarantees.
- This paper is well-written, with the authors clearly explaining the motivation, technical challenges, and main contributions.
- Empirical studies are conducted to validate the theoretically oriented methods.

### Weaknesses
Overall, I do not see any major weaknesses in this paper, though several points are worth discussing:

- **Tightness of the Bound**: As mentioned in lines 349-351, the proposed method achieves the same $T^{2/3}$ regret bound as previous work under the hard sparsity condition. However, the lower bound for the soft sparsity condition remains unclear, and it is uncertain whether the $T^{5/6}$ dependence is tight. It would be beneficial to explore the tightness of this bound more rigorously, perhaps by constructing specific problem instances where the algorithm's performance approaches this bound. The current analysis does not provide a clear understanding of whether this $T^{5/6}$ dependence is inherent to the problem or an artifact of the analysis.
- **Model Assumptions**: The paper considers a scenario where the hardness of the sample is generated from a linear model, which may not always hold in practical settings. This assumption limits the applicability of the proposed method to real-world scenarios where the underlying relationship between sample features and hardness might be non-linear or more complex. The paper should acknowledge this limitation and discuss the potential impact of model misspecification on the algorithm's performance.


### Questions
- Could you provide more discussion on the lower bound of the problem? While establishing a precise lower bound may be challenging, it would be helpful to explain why achieving better results is difficult.
- Could you discuss how to handle cases with model misspecification, where the hardness of the sample is not generated by a linear model?

### Soundness
3

### Presentation
4

### Contribution
4
