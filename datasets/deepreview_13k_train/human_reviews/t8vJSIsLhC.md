# SMPE: A Framework for Multi-Dimensional Permutation Equivariance

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Permutation equivariance (PE) is an important inductive prior for addressing tasks such as point cloud segmentation, where permuting objects in the input set maintains the output features of each object.  However, the state-of-the-art PE methods mainly focused on one dimensional cases, which cannot meet the requirements of multi-dimensional tasks such as auction design, pseudo inverse computation, and multiuser resource allocation in wireless networks. It is evidenced that the direct incorporation of high-dimensional equivariance in network design necessitates tensor operations and complicated parameter sharing patterns, which contribute to its limited exploration. In this paper, we propose a novel serial multi-dimensional permutation equivariance (SMPE) framework to address these challenges.  By serially composing multiple one-dimensional equivariant layers and incorporating dense connections for feature reuse, the proposed SMPE framework enables cross-dimensional interactions among objects while maintaining multi-dimensional equivariance.  Additionally, we extend the SMPE framework to scenarios of permutation invariance as well as the hybrid equivariance and invariance through pooling operations. We use an extensive set of experiments to evaluate the framework on contextual auction design, pseudo inverse computation, and multiuser wireless communication tasks. It is observed that the SMPE framework not only maintains excellent equivariance property to support variable set sizes, but also outperforms the state-of-the-art models. For example, SMPE could gain as high as 8.4% and 14.4% improvements over the state-of-the-art methods in two typical multiuser resource allocation scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel serial multi-dimensional permutation equivariance framework called SMPE by serially composing multiple one-dimensional equivariant layers and incorporating dense connections for feature reuse to enable multi-dimensional interactions.

### Strengths
1. The proposed SMPEL seems to be reasonable.

2. The experimental results demonstrate the effectiveness of the proposed SMPE.

### Weaknesses
1. The pooling operation for multi-dimensional permutation invariance is not clear. Which type of pooling do you use in the proposed method? How does the pooling layer help with the multi-dimensional permutation invariance? Specifically, it's unclear how the pooling operation is applied across different dimensions to achieve invariance, and whether it preserves the necessary information for downstream tasks. For example, does the pooling operation reduce the feature dimension, and if so, how does this impact the model's ability to capture complex interactions?

2. Some experimental setups are not clear. For instance, in Section 4.2, the authors do not explicitly mention what evaluation metric is used in Table 2. It's unclear which type of pooling is used in the proposed method. Furthermore, the description of the training configurations and their impact on the results is not sufficiently detailed. For example, what are the specific differences between configurations A, B, and C, and how do these differences affect the performance of different model variants?

### Questions
1. How does $\bar{X}_\mathbb{P}$ with the weight $\mathcal{w}^{GI}_P$ to preserve the global information? How do you learn the weights $\mathcal{w}^{GI}_P$ and $\mathcal{w}^{PE}_P$? Can you elaborate on this?

2. The pooling operation for multi-dimensional permutation invariance is not clear. Which type of pooling do you use in the proposed method? How does the pooling layer help with the multi-dimensional permutation invariance?

3. In the experiment, the authors provide various variants of SMPEN. For instance, in Table 3, SMPEN2D-TF sometimes outperforms SMPEN3D-TF, while SMPEN3D-TF achieve the best performance in different training settings. Given a task, how to determine which type of methods should be chosen to achieve the best performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces SMPE, a multi-dimensional permutation equivariant framework. The framework combines 1D equivariant functions applied to individual dimensions to preserve higher-dimensional equivariance. By incorporating feature reuse and cross-dimensional global information, SMPE facilitates interactions among objects in all dimensions, enhancing expressivity. Additionally, the framework can be extended to achieve multi-dimensional invariance using pooling operations. Experimental results show that networks constructed using the SMPE framework outperform other approaches and can operate on sets of varying sizes.

### Strengths
* It is valuable to preserve higher-dimensional equivariance.
* The theoretical analyses are provided. 
* The experimental results show the method have significant improvements over the baselines.

### Weaknesses
1. One concern is about the evaluation. 1) The adopted tasks in this paper consider the dimensions no more than 3D. This may not reflect the effectiveness of the proposed method, since the paper claims its contribution in **high-dimensional** permutation equivariance. Specifically, the experiments do not explore scenarios where the input data has more than three dimensions with permutation equivariance, which is a significant limitation given the method's stated goal. 2) The tasks seem simple that they only consider a linear mapping. It would be better to evaluate the method in real-world datasets, where the mapping from inputs to outputs could be complex. The current tasks, such as the pseudo-inverse calculation, do not fully represent the complexity of real-world scenarios where the mapping is highly non-linear. It would be better to show the method can be an effective module in neural networks for complex tasks.

2. Another concern is about the novelty. The idea seems straightforward to combine 1D equivariant functions applied to individual dimensions to preserve higher-dimensional equivariance. While the authors provide a theoretical analysis, the core idea of applying 1D equivariant functions across dimensions is not particularly novel. The paper would benefit from a more detailed comparison with existing methods that also leverage 1D equivariant operations, highlighting the unique aspects of their approach beyond the specific combination method.

### Questions
1. Can this method act a high-dimensional permutation equivariant module in other neural networks for more complex tasks?

2. Most graph neural networks are known as permutation equivariant, and most pooling methods are permutation invariant. What about the comparisons of this method with these works?

3. What is the distance metric for calculating MAE&MSE in the experiments? 

4. What about the tasks with more dimensions, e.g., more than 3D?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method for obtaining neural networks with higher-order permutation equivariances. This concerns tensors where multiple dimensions are equivariant. The main approach uses a composition of first order permutation equivariant functions. Features are pooled from all subsets of dimensions to facilitate exchange of information between the different dimensions.

### Strengths
- Straightforward and easy to understand method, well-written
- I believe the method to be novel
- While there is existing work handling this subject, I believe that this is a useful *practical* contribution to the literature.
- Interesting applications used in experiments, solid results

### Weaknesses
 - I believe that this topic has been studied before as part of more general treatments of permutation equivariance, such as in [1] under the name of higher-order permutations. As such, the techniques used themselves are fairly standard and novelty therefore limited, even if their exact combination is new.
- The experiments could be made stronger by comparing on existing settings, so that it's possible to compare against existing numbers in papers. Some of the performance benefits of the proposed method could be explained simply by insufficient tuning of the baseline models.
- It would be good to see further ablation to test some of the claims made in the paper. For example, it would be good to check the performance impact of the parallel computation vs sequential computation.

### Questions
It seems like using all possible subsets can be limiting in terms of scalability. Can you think of more efficient alternatives that don't sacrifice too much in model capacity?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a multi-dimensional permutation equivariance framework named SMPE to pave the way for the design of multi-dimensional permutation equivariant networks.

### Strengths
- This work provides the first exact algebra-based definition of multi-dimensional permutation equivariance.

- The experiments are extensive, including contextual auction design, pseudo inverse computation, and typical wireless communication tasks.

- The research can benefit many real applications including point cloud analysis, graph analysis, pseudo inverse computation, typical wireless communication, etc.

- The proposed technique seems sound, and its effectiveness is verified by experiments.

### Weaknesses
 - The running time of all the methods could be compared to show the efficiency of the proposed method.

- The hyperparameter settings of the model should be listed in the text.

- Two related works [1,2] about graph permutation invariance are missing in the discussion.

- The source codes and the datasets could be provided to facilitate the reproducibility of this work.

### Questions
Please respond to the weaknesses listed in the previous text box.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
