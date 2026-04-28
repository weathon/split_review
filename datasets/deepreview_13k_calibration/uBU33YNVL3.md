# Bounded Loss Robustness: Enhancing the MAE Loss for Large-Scale Noisy Data Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 3, 5

## Abstract
Large annotated datasets inevitably contain noisy labels, which poses a major challenge for training deep neural networks as they easily fit the labels. 
Noise-robust loss functions have emerged as a notable strategy to counteract this issue, with symmetric losses, a subset of the bounded losses, 
displaying significant noise robustness. 
Yet, the class of symmetric loss functions might be too 
restrictive, with functions such as the Mean Absolute Error (MAE) being susceptible to underfitting.
Through a quantitative approach, this paper explores the learning behavior of bounded loss functions, particularly 
the limited overlap between the network output at initialization and non-zero derivative regions of the loss function.
We introduce a novel method, "logit bias", which adds a real number, denoted as $\epsilon$, to the logit at the correct class position.
This method addresses underfitting by restoring the overlap, enabling MAE 
to learn, even on datasets like WebVision, consisting of over a million images from 1000 classes.
Extensive numerical experiments show that MAE, in combination with our proposed method, can compete with state-of-the-art noise robust loss functions.
Remarkably, our method relies on a single parameter, $\epsilon$, which is determined by the number of classes, resulting in a method that uses zero dataset or noise-dependent hyperparameters.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the learning behavior of bounded loss functions and proposes a modified version of MAE (adding logit-bias), addressing its under-fitting issue, especially when used in scenarios with a large number of classes. Both theoretical and numerical analyses demonstrate the picture behind the proposed logit-bias. Experiments show the proposed method's effectiveness and superiority over other noise robust losses.

### Strengths
- the paper is well-written, and the idea is clearly presented.
- the observation of the overlapping between the distributions of the averaged error and the logit and its implication on network learning is keen and illuminating. 
- the proposed logit-bias is simple yet effective.

### Weaknesses
 - the study of learning behavior still needs to be completed. It only considers the learning at the initialization stage.
    - for example, in Fig. 4, the test acc using MAE* degrades in the late stage of training when the noise is present. Why does this happen? It would be interesting to investigate the learning behavior during the full training phase.
- it would be desirable to consider more types of noise, e.g., skewed label noise, feature-dependent noise, etc., and more network architectures.
- the way of choosing optimal $ \epsilon $ needs to be explored more.

### Questions
- should we not consider the two temperatures as parameters for the Bi-Tempered loss? 
- how would the overlapping state change during training? would a dynamically tuned $\epsilon$ helpful? would you consider other strategies for choosing $\epsilon$?
- is it possible, based on your observation, to design an initialization method that can also improve the overlapping?
- as had been noticed in the paper, training with the logit-bias may introduce a kind of inductive bias to the resulting network, and this issue is addressed in a heuristic way by using small $\epsilon$ values. However, a smaller $\epsilon$ would have reduced its ability to restore overlapping. Could you elaborate on how this inductive bias would affect the trained model? Is there a systematic way to mitigate it?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this study, the authors analyzed the dynamics of early-stage learning by computing the average backpropagation error, providing quantitative insights into how increasing the class count influences initial learning, especially in the context of bounded loss functions such as Mean Absolute Error (MAE). They introduced a hyperparameter-independent approach called "logit bias," which realigns the distribution of a newly initialized network, enabling effective learning with MAE loss even in scenarios with a multitude of classes. Empirical evidence demonstrates the effectiveness of this method, with logit bias enhanced MAE loss showing comparable or superior performance across datasets spanning ten to a thousand classes. This is significant as such outcomes were previously largely exclusive to Cross Entropy or biTemp loss, which tend to overfit. The authors argue that their method is a first step towards a comprehensive framework that allows for noise-robust learning, regardless of the number of classes, and without an over-reliance on fine-tuned hyperparameters.

### Strengths
1. This paper offers a novel insight into the underfitting phenomenon observed in some robust loss functions, pinpointing the discord between the non-zero range of the average error and the logit distribution of a newly initialized network as the primary culprit.

2. The approach of this paper is simplicity and efficiency, requiring only a single parameter, ϵ, which is directly determined by the number of classes.

3. The paper provides clear details about the experimental setup, allowing for reproducibility and further exploration by other researchers.

### Weaknesses
1. The notations are not clearly defined; for example, the meaning of $\delta_{nj}$ is unclear. Furthermore, the relationship between $z_k$, $a_j$, and the activation function is not explicitly stated, making it difficult to understand the exact computations and the role of each variable in the proposed method. The lack of clarity in defining these fundamental components hinders the reproducibility and interpretability of the results.

2. This method is only designed for MAE, could it be expanded to help other robust losses? While the paper focuses on MAE, it does not explore the potential of applying the logit bias to other robust loss functions. This limits the scope of the work and raises questions about the generalizability of the proposed approach to other loss functions that might also benefit from a similar bias adjustment. The paper would be strengthened by a discussion of the challenges and possibilities of extending this method to other robust loss functions.

3. The empirical improvement is trivial. In the dataset CIFAR100 and with Resnet-34, it only achieves the state-of-the-art for clean data. The gains over existing methods are not substantial, particularly when considering the wide range of existing techniques for handling multi-class classification problems. The paper would benefit from stronger empirical results, demonstrating a more significant improvement over existing methods across a broader range of datasets and network architectures.

### Questions
1. In figure 1, the label for x-axis is "pre activation $z_k$", but there is no information about the activation function, I wonder what is the specific meaning of $z_k$, $a_j$ and $\delta_{nj}$.

2. How to get the output error of $\delta_n$ in Tabel 1? Is that related to activation function?

------
I acknowledge that I have read the response of the authors. However, I am not convinced by the contribution of this work. Therefore, I tend to keep my score as 5.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to handle label noise. They observed that although bounded losses exhibit robustness against label noise, they suffer from serious underfitting. Taking MAE example, the authors explore its learning behavior. Motivated by this, they propose a new method called logit bias to address the underfitting.

### Strengths
1. This paper is well-organized and easy to follow.
2. This paper is well-motivated. Specifically, the authors analyze the learning behavior of MAE at the early stage of training process, revealing the reason why MAE suffers from underfitting.
3. Based on the above analysis, the author proposed logit bias, which is easy to implement and really helps to alleviate underfitting in some cases based on their experimental results.

### Weaknesses
In my humble opinion, the contributions of this paper seem limited and do not achieve the bar of ICLR.
1. It is widely known that bounded loss such as MAE suffers from underfitting, an early work [1] also performed gradient analysis to explain this phenomenon. Although the analysis in this paper is somewhat different from the early work, I don't think it provides enough new insights. Specifically, while the authors analyze the gradient behavior of MAE, the core observation that the gradient magnitude diminishes as the error increases is already established. The paper's analysis, while quantifying the effect based on the number of classes, does not fundamentally alter the understanding of why MAE underfits. The connection between the number of classes and the underfitting issue, while potentially interesting, is not presented with sufficient theoretical depth to be considered a significant contribution.
2. The proposed method "logit bias" seems too simple. It is definitely okay if it is effective enough, unfortunately, it is not. The method essentially adds a constant bias to the logits, which is a very straightforward modification. While simplicity can be a virtue, in this case, the method lacks novelty and does not demonstrate a substantial improvement over existing methods. The empirical results do not show a clear advantage of logit bias over other robust losses, and the improvement achieved is often marginal.
3. The current experimental results are not sufficient to demonstrate the effectiveness of the proposed method. First, most experiments are performed on symmetric label noise, I wonder if the proposed method can also handle asymmetric noise. I know that Webvision contains asymmetric noise, but its noise rate is relatively low. Moreover, even for symmetric label noise, the proposed method lags behind some previous methods such as genCE in many cases. Finally, I noticed that the authors claim that genCE has no hyper-parameter. I guess that they set $q$ of GCE to 0.7 by default. However, in my experience, the performance of genCE can improve remarkably if we elaborately adjust $q$. For instance, if we set $q$ to 0.5 or a smaller value, genCE might outperform other robust losses on WebVision. In fact, considering that MAE* has one hyper-parameter, it is unfair to freeze $q$ of genCE.

### Questions
Please see above.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explored the learning behavior of MAE (one of symmetric loss functions), i.e. the limited overlap between the network output at the initial phase and non-zero derivative regions of the loss function. For tackling this issue, the paper introudced 'logit bias' to restore the overlap, and enabled MAE to learn on datasets with noisy labels. Extensive experiments on various datasets show the effectiveness of the proposed method.

### Strengths
1. The paper provided detailed  analysis of proposed 'logit bias' from both theoretical (Eq.1 -- Eq.4) and experimental point of view (comparing with various loss functions).
2. The author's writing is very good, and the entire paper is relatively easy to understand.
3. Simple algorithm, easy to follow as only one additional parameter (ϵ) are needed.
4. The experimental results are reliable and sufficient to verify the effectiveness of this method.
5. The last paragraph of Section 4 discusses some limitations.

### Weaknesses
This work looks like intuitively observing experimental results and then providing theoretical explanations. This is a reasonable research method, however, this explanation requires sufficient experiment validation. (I do not think the current experiment results are convincing yet)
- This paper can also be accepted if the proposed loss function can achieve SOTA in at least one task across various datasets, however, the current experimental results have not shown superiority. (Reviewer cujv has also pointed out that empirical improvements are trivial. And, Reviewer jRF4 pointed out benchmarks are not sufficient.)
- From a theoretical perspective, redesigning the loss function by introducing constants is not novel enough for me. I listed some references in face recognition domain:
1) Deng, Jiankang, J. Guo and Stefanos Zafeiriou.“ArcFace: Additive Angular Margin Loss for Deep Face Recognition.” 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2018): 4685-4694.
2) Wang, H., Yitong Wang, Zheng Zhou, Xing Ji, Zhifeng Li, Dihong Gong, Jin Zhou and Wei Liu. “CosFace: Large Margin Cosine Loss for Deep Face Recognition.” 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition (2018): 5265-5274.

### Questions
1. "thus laying the foundation for a universal classification framework." Can this work support this strong conclusion?
2. one paper relates to this work, would you please give some comments (comparison): IMAGE for Noise-Robust Learning: Mean Absolute Error Does Not Treat Examples Equally and Gradient Magnitude's Variance Matters,Published at ICLR 2023 Workshop on Trustworthy and Reliable Large-Scale ML Models.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
