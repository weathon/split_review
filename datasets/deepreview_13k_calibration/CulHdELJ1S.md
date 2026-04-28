# HUB: Enhancing Learned Optimizers via Hybrid Update-based Strategy

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Learned optimizers are pivotal in meta-learning and recent advancements in scalable learned optimizers have showcased superior performance over traditional, hand-designed counterparts in diverse tasks. However, their adoption is impeded by certain limitations, such as difficulties in handling out-of-distribution tasks, uncontrollable behaviors, and inferior performance in fine-tuning tasks. To address the issue of generalization in these optimizers, we propose a Hybrid-Update-Based (HUB) optimization strategy, inspired by the latest advancements in prompt tuning and result selection techniques in large language and vision models. Compared to previous methodologies (Pr'emont-Schwarz et al., 2022; Heaton et al., 2020), our approach enables a more sophisticated integration between hand-designed and learned optimizers and significantly reduces the computational overhead of hybridization. Our approach broadens the applicability of learned optimizers to tasks beyond their initial training distribution, and it has been validated through a series of diverse tasks, demonstrating significant advantages and unique robustness against out-of-distribution tasks compared to meticulously hyperparameter-tuned competitors. In this paper we also delve into a theoretical analysis of the hybrid strategy's impact on the behaviors and inherent traits of learned optimizers, offering deeper insights into their functionalities and interactions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed a hybrid scheme for training neural networks, which combines classic, hand-designed optimizers (e.g., Adam) and learned optimizers (e.g., VeLO). The proposed hybrid scheme is a reweighted combination of the updates from a hand-designed optimizer and a learned optimizer. The reweighting coefficients are decided by the gradient magnitudes of weights within one each layer, by feeding them into a softmax function. The formulation in Eqn. (5) implied that the proposed hybrid scheme mostly depends on the learned optimizer updates, with very weak influence from the hand-designed updates, while the authors suggested that the coefficients can be inverted for specific tasks like fine-tuning.

The authors conducted experiments on a wide range of training tasks and neural networks.

### Strengths
+ The integration of learned optimizers with classic, hand-designed optimizers has been desired for a long time.
+ The proposed method is simple enough and easy to implement.
+ The authors did a large amount of empirical experiments to show the effectiveness of the proposed method.

### Weaknesses
 - The proposed method is a hybrid scheme. A key issue of a hybrid scheme is the difficulty to guarantee the convergence, which is the highlight of the two highly-related methods mentioned in the paper: (Pr'emont-Schwarz et al., 2022; Heaton et al., 2020). The authors mentioned the computation complexity but discard the discussion of theoretical analysis. The lack of convergence guarantees, especially in non-convex optimization landscapes common in deep learning, is a significant concern. While hand-designed optimizers like Adam have some convergence properties in convex settings, these do not directly translate to the non-convex scenarios where neural networks are trained. The paper should address how the hybrid approach affects convergence behavior, especially compared to using either a hand-designed or learned optimizer alone. The interaction between the two optimizers and its impact on convergence is not clear.

- This paper is poorly written (to the extent where the overall quality of this work is significantly influenced in my humble opinion), making it difficult to understand the intuition behind the default hybrid scheme formulated in Eqn (5). The arrangement of contents also made it difficult to read, such as the tables in the experiment section. The presentation lacks clarity, making it hard to grasp the core ideas and the motivation behind the specific formulation. For instance, the rationale behind using gradient magnitudes to determine the reweighting coefficients is not well-explained, and the connection between this choice and the overall performance is unclear. The tables, instead of being integrated into the text, are presented in a way that disrupts the flow of reading.

- Considering the essense of high-demensionality of modern neural networks, the influence brought in by the hand-designed update in Eqn. (5) would be really weak. Probabily only one or two weights in each layer that have really dominant gradient will lean towards the hand-designed update in a meaningful sense. The authors did not show the histogram of the elements of the weighting matrix throughout the manuscript. I am really curious to see such observations to understand the behaviors of the proposed method in real-world scenarios. The claim that the hybrid scheme effectively leverages both optimizers is not sufficiently supported by empirical evidence. The paper should include an analysis of the distribution of the weighting matrix elements to show how the hybrid scheme behaves in practice. Without this, it's hard to assess the true impact of the hand-designed optimizer.

### Questions
- In Fig. 1, the authors illustrated that LGL2O calculates the loss and gradient for the two types of optimizers separately. Are there specific technical designs that keep us from using the same shared computation strategy as in HUB?

- The baseline accuracies of ResNet-50 and Xception on CIFAR-10 are too low. I checked the benchmark on CIFAR-10. These two networks should be able to easily achieve >95% testing accuracies. I wonder if the baseline networks are correctly and fully trained.

### Soundness
2 fair

### Presentation
1 poor

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
This paper presents a simple algorithm to prevent learned optimizers from collapsing (e.g., giving incorrect outputs). The proposed algorithm is essentially a weighted average between learned and hand-crafted optimization rules. On multiple tasks, both in- and out-of-distribution, the authors show that the proposed algorithm can help boost performance.

### Strengths
- The topics is interesting to me. Learned optimization could be a promising topics for future research. 
- The proposed techniques are simple and straight-forward to implement.

### Weaknesses
 A few relevent papers are missing from the reference which I will explain as follows: 

[r1] distills the learned rules into specific mathematical expressions, which also provides "effective control". There are also works characterizing the generalization behaviors of L2O [r2-r4]. Please consider discuss these works. 

[r1] Symbolic Learning to Optimize: Towards Interpretability and Scalability

[r2] Hyperparameter tuning is all you need for lista

[r3] Understanding deep architecture with reasoning layer

[r4] M-L2O: Towards Generalizable Learning-to-Optimize by Test-Time Fast Self-Adaptation

-----

Regarding Figure 2(c), would it be an easier solution to use just early stopping? 

-----

There is almost no analysis to experiments results in Section 4.1. Section 4.2 paragraph 1 seems to be cut off and unfinished. Also I have a same question here: would the baselines experience fluctuations? Can early stop can help? 

-----

I would not criticize this paper as lacking novelty as the authors have already conducted a lot of experiments. However I think there is plenty of rooms for the presentation to be improved. Spacing could be make more compact to accommodate more details regarding the experiments. Right now I have to look back and forth to understand what the tasks really are. 

-----

Minor errors:
"tasks undertaken during training", Traditional optimizers such as SGD", "convext optimization problems": a space is missing before the reference. Also the whole contribution bullet #2. Please proof-read carefully and add necessary spacing.


### Questions
"Consequently, even a few misguided steps within this “black box” can significantly disrupt the entire training process, with no means to prevent such adversities." -> is there any example to support this?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Learned optimizers play a crucial role in meta-learning, offering improved performance compared to traditional, manually designed optimizers across various tasks. However, these learned optimizers face challenges such as handling tasks beyond their training data, unpredictable behavior, and suboptimal performance in fine-tuning tasks. The authors’ introduce a Hybrid-Update-Based (HUB) optimization strategy that integrates hand-designed and learned optimizers. HUB is tested on a variety of tasks to illustrate its efficacy in out-of-distribution tasks. The authors also provide some theoretical analysis of HUB.

### Strengths
- Improving the working of learned optimizers (LO) is a challenging and important task to increase their adoption. The problem addressed in the paper is thus relevant and important to the community.
- A key strength of the approach is its simplicity: a convex combination of the LO and hand-designed update. The approach is significantly simpler and more efficient than LGL2O that requires actually checking the model performance after the updates from both Lo and hand-designed optimizer. This combination weight is derived from the softmax of the gradients.
- Experiments are adequate both in quality and quantity. I especially like the experiments on out-of-distribution tasks and fine-tuning.

### Weaknesses
 - How does one reconcile with the use of a hand-designed optimizer during training when the goal is to train using a robust LO? Doesn’t it defeat the purpose of an LO? Strategies that enable LO to work well (stable convergence) will be more interesting and beneficial. The ideas presented in the paper do not improve the robustness of the LO, rather mitigate issues when using it for training a different task. The results indicate only a marginal difference between VeLO (LO), ADAM, and HUB results. Thus, begging the question, the need for an LO.
- I find the motivation driven by vanishing gradients and the hybrid update equation 5 to be contradicting. When faced with vanishing gradients the convex combination factor of the hand-designed update will be close to 0, forcing the updates to depend on the LO. As LO can be unstable near the optima, how does the proposed strategy facilitate model convergence? The paper does not adequately address the scenario where the learned optimizer, which is known to be unstable near the optima, is solely responsible for updates when gradients are small, potentially leading to divergence.
- There has been (at least one) recent work [1] that also attempts to overcome the challenges with LO raised in the paper. This method appears to be much simpler than the proposed approach. It would be helpful to have some comparison against it.
- Can you clarify if the stability results on ADAM are authors’ contributions or a restatement of existing literature?


### Questions
please see the weaknesses

--- Post authors' response
I thank the authors for the detailed response. 

While I agree that the approach is simple, I am not entirely convinced with the motivation  of combining LO and SGD updates. Hence, I retain my recommendation.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
They propose a Hybrid-Update-Based Optimization Strategy (HUB) which trade-off the involvement between a hand-designed optimizer and a learned optimizer to improve the efficient and performance. The proposed method has been validated on different types of  computer vision tasks across different types of models.

### Strengths
1. The method analysis is clear and visualization is helpful.
2. The experiments are solid and comprehensive.
3. The proposed method is novel and performs well on different types of  computer vision tasks across different types of models.

### Weaknesses
1. Lack of discussion about the computation cost of the proposed method when model size increase. Specifically, the computational overhead of calculating the SoftMax across all layer's gradient matrices, and how this scales with increasing model parameters, is not addressed.
2. Lack of the GPU memory usage discussion. It is crucial to understand the memory footprint of the proposed method, especially when training large models, as memory constraints can significantly limit the applicability of the method.
3. The proposed method inspired by prompt tuning is not clear. The connection between the proposed hybrid update strategy and the core principles of prompt tuning, particularly how it leverages pre-trained model knowledge, is not well-established.

### Questions
1. Compared with other method, how will the SoftMax influence the computation time when model size increase? Since it will compute the SoftMax of all layer's gradient matrix.
2. I am curious about the GPU memory usage between the proposed method with others. Since if we want to train a large model, we will also consider if the overall pipeline can be fit on our computation resources.
3. I am still confused how the proposed method inspired by prompt tuning? I do not see the relationship between them.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
