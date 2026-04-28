# Transferring Learning Trajectories of Neural Networks

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Training deep neural networks (DNNs) is computationally expensive, which is problematic especially when performing duplicated or similar training runs in model ensemble or fine-tuning pre-trained models, for example. Once we have trained one DNN on some dataset, we have its learning trajectory (i.e., a sequence of intermediate parameters during training) which may potentially contain useful information for learning the dataset. However, there has been no attempt to utilize such information of a given learning trajectory for another training. In this paper, we formulate the problem of "transferring" a given learning trajectory from one initial parameter to another one (named {\it learning transfer problem}) and derive the first algorithm to approximately solve it by matching gradients successively along the trajectory via permutation symmetry. We empirically show that the transferred parameters achieve non-trivial accuracy before any direct training, and can be trained significantly faster than training from scratch.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel algorithm for transferring a learning trajectory from one initial parameter to another, which can significantly reduce the computational cost of training deep neural networks. The algorithm formulates the learning transfer problem as a non-linear optimization problem for the policy function and matches gradients successively along the trajectory via permutation symmetry to approximately solve it. The empirical results show that the transferred parameters achieve non-trivial accuracy before any direct training and can be trained significantly faster than training from scratch. However, the algorithm's limitations include the assumption that the source and target tasks are related, and the lack of a detailed analysis of the computational cost of the algorithm.

### Strengths
1. The proposed algorithm is a novel approach to the problem of transferring a learning trajectory from one initial parameter to another. The idea is interesting.
2. The algorithm is theoretically grounded and can be solved efficiently with only several tens of gradient computations and lightweight linear optimization.
3. The empirical results show that the transferred parameters achieve non-trivial accuracy before any direct training and can be trained significantly faster than training from scratch.

### Weaknesses
1. The empirical evaluation of the algorithm is conducted on a limited set of benchmark datasets, namely Cars and CUB. While these datasets are valuable, the paper lacks a demonstration of the algorithm's performance on more complex and large-scale datasets. This raises concerns about the generalizability of the proposed method to real-world scenarios involving diverse data distributions and complexities. For example, it would be beneficial to evaluate the algorithm on datasets like SUN397 or iNaturalist2017 to assess its robustness and scalability.

2. The paper does not provide a detailed analysis of the computational cost of the algorithm, particularly regarding its scaling behavior with respect to network size and the number of training epochs. The algorithm involves gradient computation and matching, which could potentially become computationally expensive for larger neural networks. A thorough complexity analysis, including the order of growth for both gradient computation and matching (e.g., O(N^2) for backpropagation and O(N^3) for the Hungarian algorithm), would provide valuable insights into the practical applicability of the method.

3. The paper does not fully address the implications of the algorithm's reliance on the permutation symmetry of intermediate neurons in feed-forward MLPs. While this property is exploited effectively, the paper does not explore how the algorithm might be adapted or extended to handle network architectures that deviate from this structure, such as Transformers, which have more complex symmetry considerations due to their attention mechanisms.

### Questions
1. How sensitive is the algorithm's performance to the assumption that the source and target tasks are related, and how well does it perform when the tasks are unrelated?
2. How does the proposed algorithm compare to other methods for transferring learning trajectories, such as fine-tuning or transfer learning?
3. How well does the algorithm perform on datasets that are not included in the empirical evaluation, and how does its performance compare to other methods on these datasets?
4. Can the algorithm be extended to handle more complex neural network architectures?
5. How does the computational cost of the algorithm compare to other methods for transferring learning trajectories, and how does it scale with the size of the neural network and the number of training epochs?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
### Problem Statement

The paper introduces a novel problem called the "learning transfer problem", aimed at reducing training costs for seemingly duplicated training runs on the same dataset by transferring a learning trajectory from one initial parameter to another without actual training.

### Main Contribution

The paper's contributions include: (1) formulating the new problem of learning transfer with theoretical backing, (2) deriving the first algorithm to solve it, (3) empirically demonstrating that transferred parameters can accelerate convergence in subsequent training, and (4) investigating the benefits and inheritances from target initializations. Through these contributions, the paper presents a promising avenue to significantly reduce the computational cost and time required to train DNNs, especially in scenarios involving model ensembles or fine-tuning pre-trained models.

### Methodology

The authors approximate the solution to the learning transfer problem by matching gradients successively along the trajectory via a permutation symmetry technique. The updates along the "source trajectory" are applied to update a target network with a different random initialization after being permutated such that the gradients of the two networks at the same "time step" are best matched under the permutation, resulting in the Gradient Matching along Trajectory (GMT) algorithm. To further optimize the space and time complexity of the algorithm, the authors propose to use linear interpolation of the initial and final parameters of the source network in place of the acutal training trajectory, and to re-use the mini-batch gradients evaluated along the trajectories to search for the best-matching permutations. The optimized verison of the algorithm is named "Fast Gradient Matching along Trajectory" (FGMT). The best permutations for parameter alignment at each time step are solved with a coordinate descent algorithm, iteratively optimizing for the permutation in each layer of the network by solving a linear assignment problem.

### Experiments

The learning transfer methods are evaluated on standard vision datasets with various architectures including CNN and MLP. Both random initializations and pre-trained initializations are used to evaluate and demonstrate the effect of GMT and FGMT in terms of 1) the performance after transfer; 2) the fine-tuning efficiency and performance after transfer.

Empirical evaluations reveal that the transferred parameters achieve non-trivial accuracy before any direct training and can be trained significantly faster than training from scratch, while inheriting the properties (e.g. generalization ability) from the parameter initialization.

### Strengths
### Originality and significance

The proposed task of learning transfer problem is novel and very interesting, with potentially wide applications, as the foundation-model paradigm prevails in many AI / DL fields. The proposed method is to progressively merge the target network with the source network using Git Re-basin, which is straightforward and efficient.

### Quality

Theoretical analysis is performed to justify the adopted method, in addition to a series insightful experiments. The experimental details are in general well documented. However, I find the experiments are not enough to support some of the claims, and will expand on this in the Weakness section.

### Writing

The writing is overall good, despite minor grammar problems. I find the mathematics in the paper is clear with consistent and self-explanatory notations. The problem is well motivated and formulated, and the main thesis is well conveyed.

### Weaknesses
### weaknesses:
 I am open to change my score if the authors can address the following concerns:

### Lack of experiments more closely demonstrating the actual usage of the proposed method

1. One potential usage of the proposed method suggested by the authors is to transfer the update of a foundation model to its fine-tuned versions. However, all experiments are limited to network architectures of relatively smaller scale, and to the cases where fine-tuning task shares exactly the same number of classes as the pre-training task, which differs from the realistic use-case of foundation models, which are of typically larger scale, and are used for various down-stream tasks with task-specific heads. Specifically, it would be valuable to see experiments involving larger models and scenarios where the fine-tuning task has a different number of classes than the pre-training task. This would more closely resemble real-world applications of foundation models and provide a stronger validation of the method's practical utility.

2. The authors claim that method can accelerate the training of an ensemble of neural networks. Although the computational cost of the proposed method is briefly described in the appendix, there is no figure or table systematically comparing the cost with traditional training / fine-tuning approaches. More crucially, no experiment compares the performance of the ensemble obtained with GMT / FGMT and traditional approaches. One concern is that, transfering one (or a limited number of) source trajectory, the diversity of the resulted target networks is limited (this is partially endorsed by the landscape visualization in Figure 7), which could hurt the performance of the ensemble. It would be beneficial to see a direct comparison of ensemble performance and a quantitative analysis of the diversity of the target networks generated by the proposed method versus traditional approaches.

### Lack of experiments verifying the Assumption (P), Theorem 3.1, and Lemma 3.2

Although the theoretical analysis abounds, it would be much more convincing to show these statements hold in real experiments. For instance, providing empirical evidence demonstrating the validity of Assumption (P) under different experimental conditions would strengthen the theoretical foundation. Similarly, illustrating the practical implications of Theorem 3.1 and Lemma 3.2 with concrete examples from the experiments would enhance the connection between theory and practice.

### Lack of experiments and discussion on the choice of $T$

It is not clear how $T$, the numebr of time steps, or rather, the number of samples taken from the source trajectory, influences the performance of the transfer result. It seems that $T$ does not really matter in the Naïve baseline and Oracle baseline, where the parameter-aligning permutation $\pi$ remains the same across time steps, which 1) would be good to be verified by the authors in the main text and 2) makes it interesting to explore the value of $T$ that GMT / FGMT requires to have good performance, because the computational cost is proportional to $T$. A sensitivity analysis of the transfer performance with respect to different values of $T$ would be highly informative.

### The "Generalization ability" part in section 4.3 is not clear

In the "Generalization ability" part in section 4.3, the experiments and figures should be further clarified. From Figure 7, I assume that the task is to fit the CUB or Cars dataset (for the previously chosen 10-class subset), and the two "Standard" curves are for the target trajectories, which are transferred through FGMT to initialization pretrained with ImageNet-10%, leading to the green curves, but the explanations are really not clear. However, the main text explicitly states that the target initialization $\theta_2^0$ is "pre-trained on full ImageNet", which implies only *1* (instead of *2*) possible combination for FGMT for each fine-tuning dataset: starting from ImageNet-10%-pretrained, transferring the finetuning trajectory which starts from the ImageNet-Full-pretrained initialization). Another example is, I am not sure what validation the authors refer to when they mention that the ImageNet-Full pretrained initialization has "validation accuracy $\approx$ 72%" and the ImageNet-10% one has "validation accuracy $\approx$ 50%". More detailed descriptions of the experimental setup and a clearer explanation of the results in this section are needed.


### Minor
-   In the second last line of the second paragraph in Introduction: strength -> strengthen
-   On Page 5, right below Lemma 3.2: please make it explicit in which Appendix the proof is
-   On Page 6, in the "Linear trajectory" section, "such a linearly interpolated trajectory *satisfies* ..."
-   On Page 9, in the "Generalization ability" section, "generalizes poorly *than* ..." -> "generalizes poorly *compared to* ..."

### Questions
1. Data augmentation is widely used for the training of DNNs, which essentially (often randomly) modifies the dataset. Does this violate the assumption that the dataset is the same in the problem statement?

2. Even gradient-based, many optimization methods for DL can have updates very different from SGD (for example, Adam). Considering that the parameter alignment is done with gradient matching in GMT and FGMT, does the choice of optimization method changes the effect of GMT / FGMT? Ablation study regarding this could be worthwhile to add.

3. Why does the performance deteriorate in Figure 5d-5f? It is simply acknowledged without analysis and discussion.

4. In Figure 7, to better understand the effect of FT and FGMT, where would the FGMT-only parameters be in the landscape? What about permuted-source + FT?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The computational cost of training the neural network is high. 
To reduce these computational costs, this paper also intends to utilize a well-trained neural network. 
Contrast to previous studies, this paper proposes to use the training trajectory of neural networks for model training because it contains a lot of information. 
The authors dubbed this problem "learning transfer problem," which is the transfer of trajectories from one initial parameter to another. 

To this end, the paper proposes an algorithm that matches the gradient continuously along the trajectory through permutation symmetry. 
The authors demonstrate efficiency of the algorithm in two ways to evaluate the validity of the proposed algorithm. 

The first is the initialization scenarios that consists of random or pre-trained initialization to assess whether the transferred parameters via “learning transfer” without finetuning can enhance the accuracy. 
The other is the fine-tuning scenario to validate whether the transferred parameters can improve the learning speed.

With two scenarios, this paper empirically demonstrates the proposed algorithm can train the model quickly and efficiently.

### Strengths
The task, “learning transfer problem” the authors proposed is novel to me.

To address this problem, the authors proposed an algorithm to match the trajectories between source and target, which is seemly convincing. To evaluate the validity of the proposed algorithm, the authors, without any training, conducted an experiment that transfers the calculated parameter to match the trajectory, which performed somewhat successfully. 

In addition, as a result of fine-tuning after transferring the parameters, it is revealed that the performance increased very quickly.

### Weaknesses
1. There is a lack of motivation albeit the promising results. It is a lack of the evidence whether having the same trajectory between tasks is always good. Specifically, the paper does not adequately explain why aligning training trajectories would inherently lead to reduced computational cost. The argument that utilizing existing trajectories can reduce cost is not sufficiently supported, and the analysis in Sec. 4.3 appears to be more of a post-hoc analysis of experimental results rather than a clear motivation. The core question of whether forcing models to follow similar trajectories is beneficial for all tasks remains unanswered, and the paper lacks a strong theoretical or empirical justification for this assumption.
2. To experimentally prove that an initialization or architecture affects the similarity more than the dataset, it is necessary to verify it on more datasets. While the authors claim that the similarity of trajectories is more dependent on architecture than the dataset, the empirical evidence provided is not extensive enough to support this claim conclusively. The experiments should include a wider range of datasets and architectures to establish the robustness of this claim. The current experiments do not sufficiently isolate the effects of architecture and dataset on trajectory similarity, making it difficult to draw definitive conclusions.


### Questions
1. Does it show the good performance to make the model to have the same trajectory in tasks that are not related to each other?
2. Are these transferred models' ensembles better than scratch ensembles? What is it like from an ECE perspective?
3. In Sec. 3.4, there are an explanation why the transfer of the linear trajectory is more stable and has less variance than the transfer of the actual one. The authors explain that it may be because the actual trajectory contains noisy information. I think the theoretical or empirical evidence is necessary to support the explanation. 
4. I think we need to do the work shown in Fig. 5 to select the optimal parameter. Then shouldn't we put this process into the pseudo-code?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
