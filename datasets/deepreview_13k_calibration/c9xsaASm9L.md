# Enhancing Neural Training via a Correlated Dynamics Model

- Decision: Accept
- Avg Score: 4.25
- Scores: 8, 3, 5, 1

## Abstract
As neural networks grow in scale, their training becomes both computationally demanding and rich in dynamics. Amidst the flourishing interest in these training dynamics, we present a novel observation: Parameters during training exhibit intrinsic correlations over time. Capitalizing on this, we introduce  \emph{correlation mode decomposition} (CMD). This algorithm clusters the parameter space into groups, termed modes, that display synchronized behavior across epochs. This enables CMD to efficiently represent the training dynamics of complex networks, like ResNets and Transformers, using only a few modes. Moreover, test set generalization is enhanced.
    
We introduce an efficient CMD variant, designed to run concurrently with training. Our experiments indicate that CMD surpasses the state-of-the-art method for compactly modeled dynamics on image classification. Our modeling can improve training efficiency and lower communication overhead, as shown by our preliminary experiments in the context of federated learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript introduces an interesting idea, namely, *correlation mode decomposition (CMD)*, to cluster the parameter into groups. Instead of considering the top eigenvectors of the Hessian, the idea of CMD efficiently models training dynamics. The insights of CMD can be applied to communication-efficient distributed training.

### Strengths
* In general this manuscript is well-structured. 
* This manuscript considers an interesting aspect of modeling the training dynamics of complex networks. The idea of using clustered parameters looks novel to the reviewer.
* The manuscript has a good logic flow, from the definition of the post-hoc CMD to online CMD and embedded CMD.
* Sufficient numerical results also justify the effectiveness of the CMD. An extension to FL is also provided in the manuscript.

### Weaknesses
 * Authors are encouraged to improve the writing quality of the current manuscript.
* Regarding the experiments on FL, it remains unclear to the reviewer why only two communication-efficient FL baselines, namely APF and A-APF, are considered for the evaluation. More recent SOTA methods need to be taken into account.

### Questions
NA

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel observation and methodology related to the training dynamics of large-scale neural networks. The authors observe that the parameters during the training of neural networks exhibit intrinsic correlations over time. Capitalizing on this observation, they introduce an algorithm called Correlation Mode Decomposition (CMD). CMD clusters the parameter space into groups, termed modes, that display synchronized behavior across epochs. This representation allows CMD to efficiently encapsulate the training dynamics of complex networks like ResNets and Transformers using only a few modes, enhancing test set generalization as a result. An efficient CMD variant is also introduced in the paper, designed to run concurrently with training, and the experiments indicate that CMD surpasses the performance of existing methods in capturing the neural training dynamics.

### Strengths
* The paper introduces a novel observation regarding the intrinsic correlations over time of parameters during the training of neural networks. This insight is leveraged to develop a new algorithm, Correlation Mode Decomposition (CMD), which is a creative contribution to the field.

* Despite the complexity of the topic, the paper seems to be structured and articulated in a manner that allows the reader to follow the authors' logic and methodologies.

### Weaknesses
 * The citation format within the text could be improved for consistency and adherence to academic conventions. Utilizing citation commands like \citet or \citep would enhance the readability and professionalism of the references within the text.

* Figure 2 Analysis: The benefits of the CMD method as depicted in Figure 2 are not evidently clear. In the left plot, it would be helpful to see the results over a more extended range of epochs to ascertain the method's effectiveness over a longer training period.
In the middle plot, there appears to be a visual discrepancy or blur on the right side that might need clarification or correction.

* Algorithm Explanation and Comparison: A more detailed explanation and justification of the CMD algorithm's design and implementation are necessary for a thorough understanding. The comparison seems limited, primarily focusing on P-BFGS. It would be enriching to see comparisons with other relevant methods, such as pruning methods, to gauge the CMD algorithm's relative performance and novelty.

* The presentation of some concepts and terminologies, such as the "modes" in CMD, might be unclear or lack sufficient explanation, making it challenging for readers unfamiliar with the topic.

*  Discussions or demonstrations regarding the scalability of the CMD algorithm when applied to larger or more complex neural network models would be a valuable addition to assess the method's practical applicability.

* The motivation behind applying CMD in federated learning seems a bit unclear and could benefit from a more explicit demonstration or explanation.

### Questions
* Could you clarify the visual discrepancy observed in the middle plot of Figure 2? What does the blur on the right side represent?

* Would it be possible to extend the range of epochs shown in the left plot to provide a more comprehensive view of the CMD method's performance over time?

* Could you elaborate on the motivation and rationale behind applying the CMD method in federated learning? 

* What considerations were made in choosing the comparative methods and evaluation criteria in this work?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel method (Correlation Mode Decomposition, CMD) to reduce the dimension of learning dynamics of neural networks, by leveraging correlations between learning dynamics. Using correlations between (the entire histories of) learning dynamics of each parameters, the proposed method first divides the set of parameters into several clusters (called modes),  identifies one representative parameter from each modes, and then represents the other parameters in each mode by scaling the representative and adding a bias. The paper also provides an online version of the dimensionality reduction (Online CMD) that can be used without memorizing the history of parameters during training, which still requires training of all parameters, and a parameter-efficient version (Embedded CMD) that enables us to reduce the number of trainable parameters gradually during training. The paper also propose to use the dimensionality reduction of learning dynamics for distributed learning. The paper empirically shows the superiority of CMD against standard training and the state-of-the-art methods of dimensionality reduction.

### Strengths
1. The procedure of CMD seems reasonable and also novel in dimensionality reduction of learning dynamics.
2. It may be also novel that their proposal to use the dimensionality reduction for distributed training, but less confident since I'm not an expert in this area.
3. Experimental results (Figure 3) shows a surprising result that Online/Embedded CMD outperforms full SGD on CIFAR-10, which seems somewhat contradictory because Online/Embedded CMD was designed to approximate the full SGD.

### Weaknesses
1. There are many unclear points in experimental results/figures.
    1. In each mode block in Figure 1 (Left & Middle), correlation between most of parameters tends to be less than 1.0, which does not satisfy the hypothesis behind the proposed method: `Any two time trajectories u, v that are perfectly correlated can be expressed as an affine transformation of each other`. The paper does not adequately address the implications of these imperfect correlations on the validity of the method. The method hinges on the assumption of strong linear relationships between parameter dynamics, yet the visualizations suggest this is not always the case. The paper should include an analysis of how the performance of CMD degrades as correlations deviate from 1.0.
    2. The y-axis in Figure 1 (Right) is unclear. It is not clear what the plotted values represent, making it difficult to interpret the figure's message. The lack of a label hinders understanding of the core argument of the figure.
    3. What are the different/common points between CMD and DMD? The paper highlights CMD vs DMD in Figure 1, but any description for DMD is not provided. The paper needs to clearly explain the DMD method and how it differs from CMD, especially since it is used as a comparison point. Without a proper explanation, the reader cannot assess the relative merits of the proposed method.
    4. Any theoretical evidence of Hypothesis 1 is not provided. The paper presents a hypothesis without any theoretical justification. This makes it difficult to assess the validity of the hypothesis and its impact on the proposed method. The lack of theoretical support undermines the scientific rigor of the paper.
    5. `Figs. 1, 6 demonstrate that Eq. (2) accurately represents the dynamics using a notably small set of modes` in Section 3.1 is overclaimed due to W1-1 and W3. Given the observed imperfect correlations and the lack of a clear explanation of DMD, this claim is not fully supported by the current evidence.
    6. Accuracies plotted in Figure 2 (Left) seem inconsistent with the corresponding accuracy in Table 1. It is also weird that test accuracy of CMD is consistently higher than training accuracy of CMD in Figure 2. This inconsistency raises concerns about the reliability of the experimental results and suggests a potential issue with the experimental setup or reporting. The higher test accuracy than training accuracy is particularly concerning and needs to be explained.
    7. The author claimed that `we observed that the reference trajectories can be selected once during training, and do not require further updates`. However I could not find such results in the paper. This claim needs to be supported by concrete experimental evidence and analysis. The absence of this evidence raises doubts about the practical applicability of the method.
    8. In Table 1, it is weird that CMD significantly outperforms full training (GD) although CMD is designed to approximate GD. At least, CMD should be worse than GD in training accuracy if CMD behaved as a regularizer as the authors claimed. If CMD outperforms GD even in training accuracy, I'm concerning that there should be some leakage or bug in experiments.
2. Experiments are limited on a single toy dataset CIFAR-10. I'm concerning whether the proposed method still works well on more large-scale, difficult learning tasks. The reliance on a single, relatively simple dataset limits the generalizability of the results. The paper needs to demonstrate the efficacy of CMD on more complex and realistic datasets to establish its practical value.
3. Since CMD identifies only single representative for each cluster, the method only leverage proportional relationships between parameter dynamics, which may lead to very limited expression power of the reduction method, especially in more complex learning scenarios. The use of a single representative trajectory may oversimplify the complex dynamics of neural network parameters and limit the method's ability to capture the full range of behaviors, especially in more challenging learning tasks.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors make a novel hypothesis about the way in which deep neural network weights dynamically evolve during training: "weights can be clustered into a very few highly correlated groups" (Hypothesis 1). The authors illustrate support for this hypothesis by examining the training of several different types networks on several different tasks, using post-hoc correlation based clustering. The success they found on these examples motivated them to develop an online method, which reduced computational demands and led to better accuracy than state-of-the-art low dimensional training methods. Lastly, the authors provided initial results on improving federated learning (and lowering computational costs) via their method.

### Strengths
1. This paper was well motivated and written. It was (for the most part) very easy to follow.

2. The hypothesis of highly correlated modes fits well within existing work (which the authors cite well), but is a highly novel discovery. This makes it impactful and interesting. 

3. The results the authors achieved are impressive. They performed better than standard methods of training, and achieved state-of-the-art results among low-dimensional training methods. They tested on a variety of tasks (including federated learning, which - the authors say - makes it the first use of dynamical modeling to reduce communication overhead). 

4. The Appendices are full of examples, pseudo-code, clarifying remarks, and extra details. This is a very packed paper.

### Weaknesses
I found no major weaknesses of this paper.

Here are a few points that whose clarification will enhance the quality of the paper: 

1. The notation used in Sec. 3.3 (Online CMD) is a little difficult to follow. Additionally, because the use of online CMD to train DNNs had been foreshadowed in earlier parts of the paper, I was confused by the lack of details on how the individual modes were trained - which was answered in Sec. 3.4. Explicitly mentioning, in Sec. 3.3., that more details are coming on the actual training are coming in Sec. 3.4, would help remove this momentary confusion. 

2. I did not understand the comment "Even though $\tilde{A}_m$ is re-evaluated at each time-step $t$, each $a_i, b_i \in \tilde{A}_m(t)$ are fixed scalars." (Sec. 3.3). Is this pre-empting the point made in Sec. 3.4 that, once embedded, a weight's $a_i, b_i$ are frozen? 

3. I felt like Sec. 3.5 (CMD Accuracy and Loss Landscape Visualization) is too quickly presented. What is the main takeaway? That you can use CMD to visualize the landscape, or that CMD training does a good job of finding the optimal parameters? Maybe this would be better in the Appendix?

4. I think the work on federated learning is very interesting and a great application of the approach. That being said, I did feel like the explanation of the approach was a little rushed (possibly due to lack of space) and Eq. 16 was a bit confusing. Improving the discussion around Sec. 4 would be helpful (and could be aided by putting Sec. 3.5 in the Appendix to get more room). 

Minor Comments: 

1. The acronyms in Table 2 should be clarified (I assume Mom is momentum but what is SCH?). 

2. Could you use DMD/Koopman methods to predict how the individual modes are going to evolve, thereby reducing the computational cost even more? 

3. The comparison of DMD with CMD in Fig. 1 is insightful. Recent work has found that using Graph Neural Networks can lead to better approximations of the Koopman operator, specifically for the training of DNNs [1]. Do you think the correlated modes you discover might explain this improved success (e.g., the GNN is able to better learn the correlated modes)?

4. There are several places where the first quotation marks in a quote are backwards. This can be remedied by using `` instead of '' in Latex.  

5. In Fig. 2, CMD is compared to GD. Should this be SGD?

### Questions
All my questions are posed in the section above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
