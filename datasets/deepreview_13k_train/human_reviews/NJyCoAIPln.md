# Branch-level Network Re-parameterization with Neural Substitution

- Decision: Reject
- Scores: 3, 3, 5, 6, 3

## Abstract
In this paper, we propose the neural substitution method for network re-parameterization at branch-level connectivity. The proposed neural substitution method learns a variety of network topologies, allowing our re-parameterization method to exploit the ensemble effect fully. In addition, we introduce a guiding method for reducing the non-linear activation function in a linear transformation. Because branch-level connectivity necessitates multiple non-linear activation functions, they must be reduced to a single activation with our guided activation method during the re-parameterization process. 
Being able to reduce the non-linear activation function in this manner is significant as it overcomes the limitation of the existing re-parameterization method, which works only at block-level connectivity.
If re-parameterization is applied only at the block-level connectivity, the network topology can only be exploited in a limited way, which makes it harder to learn diverse feature representations.
On the other hand, the proposed approach learns a considerably richer representation than existing re-parameterization methods due to the unlimited topology with branch-level connectivity, providing a generalized framework to be applied with other methods. 
The proposed method improves the re-parameterization performance, but it is also a general framework that enables existing methods to benefit from branch-level connectivity.
In our experiments, we show that the proposed re-parameterization method works favorably against existing methods while significantly improving their performance when applied to the proposed branch-level connectivity.
Upon acceptance, we will make our implementation publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper propose a branch-level network re-parameterization method,  including two core design, neural substitution and guided activation.  Neural substitution is used to aggregate features from multiple branches (the number is N). Unlike traditional block-level methods which produces single output, it generates N outputs for feeding into next blocks,  encouraging the learning of richer representations.  The guided activation utilizes the activation mask of the aggregated features of all branches to threshold the generated outputs. Experiments on multiple backbone architectures and classification datasets show that the proposed method improves representation diversity across branches and can obviously improve the accuracy compared to baseline methods.

### Strengths
1. The work aims to enhance the richness and diversity of multi-branch networks, which is a valuable direction of research. The proposed strategy is easy to implement and can be readily integrated into some widely-used backbone networks.

2. The authors provide pseudo code and illumination for the algorithm, which is helpful for understanding the work.  

3. Experimental results show that using the method can obviously benefit the accuracy of baseline networks (e.g., DBB and ACNet). The authors provide analysis for its advantage on feature diversity across branches and ensemble effect when dropping a single block.

### Weaknesses
1. The design and implementation of the work is build on block-level re-parameterization architectures, while the core of the work seems less matching the motivation of network re-parameterization. Network re-parameterization works mainly target at decoupling the training-time and inference-time network structure, typically complicating the training models but converting it into a simple architecture for inference by the consideration of deployment and efficiency. The operation neural substitution introduces  Nx memory overhead on feature aggregation compared to block-wise methods (even more for catching the intermediate input).  The method actually addresses the feature diversity of multi-branch, through a better aggregation strategy, rather than network re-parameterization.

2. The authors need to provide the analysis on memory overhead, which is an important metric for real-world application.

3. The description for the method need to be improved. The section of method and introduction lack of sufficient description for the mechanism and the insight behind, although algorithms (1 and 2) and illumination (figure 3 and 5) are provided to explain the method.  For example, I think the stochastic operation (shuffle) can largely improve the richness of features compared to without it. The authors emphasize multiple times about ``nearly unlimited topology of branch-level connection’’, if using the setting without stochastic, aggregating features in a regular order is intractable to approach it. Moreover, the guided activation is designed specially for ReLU nonlinearity, which needs to be discussed.

4. It would be valuable to see the generalization on different CV tasks in experiments beyond classification.

### Questions
1. The figure 6 shows the feature similarity comparison. It would be interesting to see if the similarity reduction mainly comes from stochastic or neural substitution.

2. I notices some differences between the performance of baseline methods in the paper and the ones reported in the DBB paper. For example, in DBB paper, the results on ImageNet with MobileNet, ResNet-18 and ResNet50 are (72.88, 70.99, 76.71) for DBB-Net and (72.14, 70.53, 76.46) for ACNet. In Table 2, the corresponding results are (70.78, 70.13, 77.50) for DBB-Net and (71.12, 70.02, 77.30) for ACNet. Some of the values are higher but the others are lower.  I think the gap may derive from the configuration difference. It would be highly recommended to report the results according to the configuration of baseline method (e.g., DBB) as well, enabling a more fair comparison.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is focused on branch-level network re-parameterization using neural substitution. The authors propose a generalized framework that can be applied to various network designs with branch-level connectivity and re-parameterizable non-linear activation functions. They demonstrate that their proposed method outperforms existing re-parameterization methods and can be adapted to different architectures.

### Strengths
The paper introduces a approach called Neural Substitution (NS) for network re-parameterization at the branch-level connectivity. This approach addresses the computational complexity issues of heavy multi-branch designs by substituting local paths. The authors also propose the use of guided activation methods to reduce non-linear activation functions during the re-parameterization process.

### Weaknesses
 -  The paper would benefit from enhancing its clarity and readability. It currently lacks a "Related Work" section, which is essential to contextualize the research and provide a comprehensive background.

- The content, particularly mathematical expressions, requires further clarification. For instance, in equation (1), the inclusion of a bias term $\beta$ in $\theta$ may be necessary for completeness. Additionally, there seems to be a typographical error in the subsequent equations where $\theta_1$ should be replaced with $\theta_2$. The rationale behind reducing only the first two $\theta$'s into $\widetilde\theta$ is not clear to me and needs explanation.

- The main idea is rather simple, more importantly, advancements over existing methods seem marginal, with many improvements being within a 0.3% accuracy range, which could be considered insignificant.

- The applicability of the proposed technique is demonstrated solely on CNN architectures. Its effectiveness on other architectural designs, such as fully connected layers or Transformers, is not addressed, raising concerns about its generalizability.

### Questions
See the weaknesses part above.

### Soundness
2 fair

### Presentation
1 poor

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
This paper introduces a branch-level re-parameterization method for transforming a residual-based model into a plain model. The paper leverages two primary techniques: neural substitution and guided activation. In particular, the neural substitution method enhances the ensemble effect of convolutional models, while the guided activation method facilitates the reparameterization of the non-linear activation function within the block. Experimental validation is performed on the CIFAR-100 and ImageNet datasets.

### Strengths
- This paper delves into the realm of designing plain models through re-parameterization literature. The proposed pipeline optimizes the utilization of ensemble effects in deep neural network models while circumventing the limitation of previous re-parameterization techniques, where non-linear activation had to be located outside the block. This research direction is intriguing and offers a valuable complement to existing re-parameterization methods.

### Weaknesses
 - Towards method
    - Regarding Neural Substitution, can you clarify whether you perform random shuffling of $\mu$ and $\nu$ during batch training, as mentioned in lines 12 to 14 of Algorithm 1? If so, could you provide insights on how to apply $\mu$ and $\nu$ during inference? The description of the shuffle operation lacks clarity, particularly concerning its implementation during training and its absence during inference. It is unclear how the weights are updated given the dynamic connections during training, and how these are consolidated for inference. The explanation needs to detail the specific mechanism by which the shuffle operation ensures diverse connections and how this is translated into the final re-parameterized model.
    - When it comes to Guided Activation, what is the rationale behind using the sum of features as a guiding factor for activation? Could you provide an explanation for this design choice? It appears that the guided activation (as shown in Figure 5) may not be formally equivalent to the original CNN structure, like ResNet, where non-linear activation resides within the block. The justification for using a sum of features as a guide is not sufficiently explained. The paper should provide a more detailed theoretical or empirical analysis to support this design choice. Furthermore, the claim of equivalence to the original CNN structure needs to be rigorously demonstrated, as the current explanation and Figure 5 raise concerns about the structural differences.

- Towards experiments
    - Merely reporting accuracy is not sufficient to demonstrate the superiority of your method. Considering that accuracy and speed can often be a trade-off in network design, it is advisable to include additional metrics, such as speed, parameters, and FLOPs (in reference to RepVGG [R1]). The paper's evaluation is incomplete without reporting computational costs. The lack of metrics like speed, parameter count, and FLOPs makes it difficult to assess the practical advantages of the proposed method. A comprehensive comparison with existing methods should include these metrics to provide a complete picture of the trade-offs.
    - Even when focusing on accuracy alone, the current evidence may not be adequate to establish the superiority of your method. In many settings, the improvement appears to be marginal, often less than 1%. The reported accuracy improvements are often marginal and do not convincingly demonstrate the superiority of the proposed method. The paper needs to demonstrate more substantial gains in performance, or provide a detailed analysis of the specific scenarios where the proposed method excels.
    - Figure 6 appears to be empty.

- Minor: There should always be a space between a word and its following reference. For example, 'The method RepVGG (Ding et al., 2021c)' instead of 'The method RepVGG(Ding et al., 2021c).'

### Questions
See *Weaknessnes*

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This is the comments from the fast reviewer.

In this study, the authors introduce a novel network reparameterization approach named
"Neural Substitution," which utilizes an unprecedented range of network topologies to
achieve more complex representations than current methodologies allow. By converting the
nonlinear activation function into a linear transformation, this method successfully navigates
past the constraints of traditional reparameterization techniques. The authors employ a
process they term "Guided Activation," replacing the nonlinear activation with a linear
counterpart to simplify computational demands while preserving the benefits inherent in a
multi-branch architecture. Validation across various datasets and network configurations
affirms the superiority of Neural Substitution over current block-level connectivity
approaches, a claim further substantiated by the results of an ablation study. Comparisons
with other reparameterization strategies highlight the proposed method's enhancements in
computational efficiency and model performance. Overall, Neural Substitution emerges as a
promising reparameterization method, poised to significantly impact future explorations in the
field.

### Strengths
as it claimed

### Weaknesses
The paper does encounter some challenges in terms of readability, with certain sections
displaying a propensity for overly elongated sentences that may impede comprehension and
introduce potential for misinterpretation. For instance, the introduction's discussion of
contributions is excessively verbose, obscuring the method's branch-level connectivity
advantages. Additionally, the background segment on structural reparameterization attempts
to condense an excessive amount of information into a single sentence.

Regarding the presentation of methods, the Neural Substitution section is eloquently
articulated, enlightening us to a sequence shuffle-based technique for diminishing the
dimensions of branch-level connectivity. However, the explanation within the Guided
Activation Function segment lacks specificity. It presents the principles of the Guided
Activation Function solely through an algorithmic lens without a direct comparison to
traditional methods, leaving the reader puzzled about its actual impact and application.

### Questions
- How does the proposed method compare to existing methods in terms of computational efficiency?
- Can the proposed method be applied to other types of neural networks, such as recurrent neural networks？
- How does the proposed method handle overfitting, and what measures were taken to prevent it during the experiments?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of better strategies for network reparameterization. This general line of work involves reparameterizing a potentially more complicated train time architecture into a specific test time architecture. The goal is to simplify and preserve performance, and different approaches make different design choices regarding the level of granularity at which the parameterization will be carried out. This work proposes reparameterizing at the branch level and a neural substitution scheme is presented. But this low-level of granularity creates a problem with handling the activation function, and therefore, a guided activation scheme is presented. Experiments show nominal gains.

### Strengths
1. Explores branch level re-parameterization which appears to have not been attempted in the literature. 

2. Guided activation applies reparameterization on the activations. 

3. Some gains in experiments are achievable.

### Weaknesses
1. The paper is not well written. The high level goal of this work should be laid out clearly but instead the paper assumes that the reader is intricately familiar with most of the existing works on re-parameterization. 

2. While I appreciate the interest in branch-level reparameterization, eventually the paper must be able to make a convincing case that the effort is worth it. The gains are marginal at best and don't appear to match up with other works (e.g., RepVGG). The choice of baselines is not explained. 

3. The technical contribution (neural substitution, guided activation) are somewhat minor. By themselves, this would not be a weakness if the experiments were comprehensive enough to show their value. Latency, memory footprint and other relevant issues that are central discussion points in other papers on this topic appear to be omitted.

### Questions
I find the general goal of this work relevant but find the degree of novelty in the main contributions and the overall rigor/comprehensiveness of the experiments (e.g., compared to RepVGG) underwhelming. Please explain if possible why these concerns are misplaced or incorrect.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
