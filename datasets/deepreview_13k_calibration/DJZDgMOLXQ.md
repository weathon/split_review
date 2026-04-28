# Prediction Error-based Classification for Class-Incremental Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 8, 5, 5

## Abstract
Class-incremental learning (CIL) is a particularly challenging variant of continual learning, where the goal is to learn to discriminate between all classes presented in an incremental fashion. Existing approaches often suffer from excessive forgetting and imbalance of the scores assigned to classes that have not been seen together during training. In this study, we introduce a novel approach, Prediction Error-based Classification (PEC), which differs from traditional discriminative and generative classification paradigms. PEC computes a class score by measuring the prediction error of a model trained to replicate the outputs of a frozen random neural network on data from that class. The method can be interpreted as approximating a classification rule based on Gaussian Process posterior variance. PEC offers several practical advantages, including sample efficiency, ease of tuning, and effectiveness even when data are presented one class at a time. Our empirical results show that PEC performs strongly in single-pass-through-data CIL, outperforming other rehearsal-free baselines in all cases and rehearsal-based methods with moderate replay buffer size in most cases across multiple benchmarks

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a challenging variant of continual learning, known as Class-incremental learning (CIL). The goal in CIL is to learn to distinguish all classes that are introduced incrementally. Existing strategies often exhibit excessive forgetting and score imbalance for classes not seen together during training.

The authors introduce a novel approach, Prediction Error-based Classification (PEC). Unlike traditional paradigms, PEC calculates a class score by gauging the prediction error of a model trained to mirror the outputs of a static random neural network for that class. This method is likened to a classification rule based on Gaussian Process posterior variance.

PEC offers several practical benefits, such as sample efficiency, ease of tuning, and effectiveness even when data are presented class by class. Empirical results demonstrate that PEC performs robustly in single-pass-through-data CIL, outperforming other rehearsal-free baselines and, in most cases, also rehearsal-based methods with a moderate replay buffer size across multiple benchmarks.

Small issues:
In 4.4: "We hypothesize this is due to [...]" - Please re-read the sentence.

### Strengths
- Very well written and easy to follow, despite the complexity. The authors aim to provide intuitive explanations, without sacrificing formal clarity. Thanks!
- The method offers clear practical advantages of existing alternatives and good performance.
- Theoretical connections are drawn to substantiate the motivation.
- Empirical results are convincing.
- Experimental setup is described in depth.

### Weaknesses
 - I previously saw this on Arxiv. This is not a double-blind review. I don't see any guidelines of how to deal with this. Hence, I at least want to mention it here.

### Questions
- In the intro it says: "Nonetheless, these methods typically perform worse with class-incremental learning than in the easier task-incremental setting" - How is task incremental easier than class incremental? Is it not simply a more general problem?
- You say: "[...] the teacher network’s middle layer is typically wider than the student’s one." Why?

### Soundness
4 excellent

### Presentation
4 excellent

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
The authors present PEC (Prediction Error-based Classification), a method for continual learning and class-incremental learning in which for each class, a student neural network learns to reproduce a randomly-initialized-and-then-frozen neural network only on examples from that class. Continual learning concerns supervised learning where data is not iid and may evolve. Task-based class incremental learning involves single-pass training in stages where only a few classes need to be discriminated between but detecting the union of all classes is required at test phase (in production).  The authors argue that the one-model-per-class approach of PEC prevents forgetting and interference between classes and can handle one-class-at-a-time-presented scenarios. They argue that using a neural net mapping is easier and simpler than creating a generative model for each class.   Theoretical connections between the method and gaussian processes are derived, given known results about the correspondence between very wide neural nets and gaussian processes. Mostly strong experimental results are presented in comparison with 11 competing approaches , although imbalanced training sets can give PEC some trouble

### Strengths
The paper is extremely well written and clear. The approach is original as far as I know, although I'm not an expert on continual learning. I've refereed for NeurIPS, ICML, ICLR and AAAI for the past several years, and this is one of the best written papers I've refereed.  The concept and motivation underpinning the approach are easy to understand and well presented. There is a nice dovetail between theory and experiment with the correspondence with gaussian processes, and it's particularly theoretically satisfying to see neural net width helping but depth not helping given the theoretical correspondence of GPs with wide neural nets. It's also a  nice counterweight to the prevailing research neural net trends of the past decade, in which the benefits of depth (the D in DNN), i.e. > 1 hidden layer, have been the main focus.

The experimental results look strong to me but also credible in their honesty, with PEC usually but not always winning.

### Weaknesses
My biggest concern with the paper is a lack of emphasis on or elucidation of a crucial aspect of the approach, namely, the details of the random parameter generation for the teacher neural network.  Algorithm 1 says 'initialize phi with random values' but doesn't say how. I had to dig into appendex B to figure out that default PyTorch initialization was used, i.e.,  Kaiming.   Those of us who have coded up neural nets completely from scratching using only low level programming in e.g. C++ or even Python with only numpy know well that the details of the initialization can make a big difference to the speed and/or success of training, certainly for sigmoidal activations and to some extent for ReLu/GeLu. If the neural net weights are too large relative the input magnitudes, you can get stuck in the saturated, near-constant regions of the activation function and the training error will barely move. If the weights are too small, you can get stuck for a long time in the linear region of the activation function and it can take a long time for training to implement any nonlinearity.  Now, it may well be that Kaiming initialization with GeLu or ReLU and then freezing will ~always result in a reasonable, useful teacher network which successfuly discriminates between classes, but this needs to be emphasized by the authors. I also wish they had done experiments to see how sensitive the results are to the initialization. 

I also think this sentence on page 3 is wrong/confusing:

"As the architectures for g and h, we use shallow neural networks with one hidden layer, either
convolutional or linear, followed by a final linear layer"

When I read that in some cases the hidden layer is linear and the final layer is linear, I found it strange...that would mean the whole neural net is a linear mapping and it would seem surprising to me that a linear mapping would characterize the class well enough. However, in Table 5 on page 13, I saw that in fact there is a GeLu layer, so there is some nonlinearity. This should be clarified on page 3.

That brings up another suggestion: although architecture choices are explored in section 4.5, it would be a nice ablation-ish experiment to see how 0-hidden layers (i.e. purely linear logistic regression) does as a target teacher network.  Is the nonlinearity of the neural net actually important? The GP theory correspondence would suggest yes, but it would be nice to either confirm that or learn from a result of a linear teacher actually being successful,

Another minor point: I don't think the title conveys the core of the approach very well.  Technically, "prediction error" is indeed involved, but prediction error usually refers to a prediction you actually care about intrinsically in the real world rather than predicting a random neural net mapping.  Something along the lines of 'random neural net class modeling for continual learning' might be a better title. That's just my two cents, though, and I'm not even sure you're allowed to change the title.

### Questions
Do you have experiments on 0-hidden-layer teachers?

Do you have experiments on sensitivity to initialization? Can you emphasize the importance of sensible initialization in the main body of the paper? Not everyone will know to use an out-of-the-box reliably smart initialization like Kaiming which is designed to get the neural to be living in the "right" regions of the activation function.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed the Prediction Error-based Classification (PEC) method in class-incremental learning, which mitigates the possible issue of data storage in the discriminative classification, and the issue of learning good generative models with limited data. To resolve these issues, the authors proposed to train simple class-wise generative (student) networks, which are used to replicate the results from the frozen random (teacher) network. The decision then is made by choosing the class with the smallest error between a student and the teacher network.

### Strengths
* The proposed PEC is a novel method as an efficient alternative to the generative models in class-incremental learning.
* The extensive experiments support the good performance of the proposed method in single-pass-through-data class-incremental learning.

### Weaknesses
 * Since the student networks in the proposed method are decoupled from each other, the method ignores the intrinsic interdependence among classes.

* The "efficiency" claimed in the contribution is less empirically supported.  Furthermore, due to the individual design for student networks, is this a good plus when the number of classes increases?

* The notations are bad. In algorithms, the number of classes is $N$ but later it is denoted by $C$ in equation (1). In proposition (2), I believe $N$ denotes the sample size but it was denoted as the number of classes in Algorithm 1.

* The proposition (2) is problematic.
  * The $\epsilon$ should relate to $\gamma$ and $N$, otherwise, it sounds your approximator can achieve any $\epsilon$ under the current samples and probability tolerance. Additionally, why there is no $\gamma$ in the proof of proposition (2)?
  * As the authors pointed out $H$ is the Gaussian process which is approximated/replaced by the network $h$. Thus, there should be another term to quantify this approximation error, which is dependent on the width of the neural network. However, I cannot see anything implying this information in the theorems.

### Questions
* “If, on the other hand, some out-of-distribution input x is considered, then the error … is unlikely to be small” in Section 3.1: Even though seen $\boldsymbol x$ can push $g_{\theta^c}$ and $h_\phi$ to be closer by learning $\theta^c$, does this necessarily means that the difference $\| g\_{\theta^c}(x)-h\_\phi(x) \|$ for OOD $\boldsymbol x$ is unlikely to be small? 
* Why does PEC have identical performances on different task splits as in Tables 1 and 2?

### Soundness
2 fair

### Presentation
2 fair

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
This paper introduces a method called Prediction Error-based classification (PEC) for Online Class-Incremental Learning. Unlike existing methods in the continual learning literature, relying upon discriminative and generative classification paradigms, it presents a novel classification approach for continual learning. The method involves fitting a shallow predictor network for each task class to match a single random prior network. At inference, the final classification is determined by selecting the class with the smallest error between all the fitted models up to the current task and the output representation of the random prior network. The authors emphasize that the classification rule they employ is theoretically justified as an approximation of a rule based on Gaussian Process posterior variance. This approach operates in an exemplar-free scenario, doesn't rely on a pre-trained network, and can handle the  problem of having a single class per task. The authors conducted empirical experiments, showing  that their approach enhances performance compared to exemplar-free baselines and exemplar-based methods relying on generative or discriminative classification paradigms. The authors highlight that their approach exhibits class-imbalancing issues, and they propose two methods to mitigate this problem: Buffer Balancing, which relies on an evolutionary optimization algorithm and an exemplar memory buffer, and Equal Budget, which equalizes the number of training iterations for different classes.

### Strengths
*  The introduction is well-written and they clearly motivate why they propose prediction error-based classification.
*  The novel usage of a Random Prior Network and multiple predictor network for online class incremental classification. 
*  The PEC's ability to work in exemplar-free, from scratch, one class-per-task settings is a valuable feature. These settings, especially the combination of these ones, are infrequently assessed by the literature.

### Weaknesses
The major weakness of this paper lies in the experimental evaluation where the authors assess the performance of the proposed method:


* **SOTA Architecture Comparison**:  The  authors have designed the PEC predictor models to align  with the parameter count of reference literature networks.  Specifically for the evaluation of SOTA methods, the PEC authors employ simpler networks architecture for  SVHN, MNIST, while they employ the standard Resnet18  for Cifar10, Split-Cifar100 and the miniImagenet dataset. These latter tasks are considered more challenging in comparison to SVHN and MNIST.  My primary concern revolves around the use of the standard Resnet18 that the authors employ for evaluating SOTA methods. Training the standard Resnet18 can be difficult, especially when the number of training iterations is limited (i.e. in online setting), primarly due to the large number of parameters (11.2M as reported in the  table 6 of the Appendix B.1 of the paper). In response to this challenge, recent sota online approaches rely upon a **reduced** version of Resnet18, which consists approximately on 1.1M of parameters [g] [h] [i] [l] [m] [n]. This reduced network is commonly favored for online continual learning due to its computational efficiency and ease of optimization. Utilizing the reduced Resnet18 as a reference is essential to ensure a fair comparison with the existing literature, especially since PEC uses shallow models easier to train than Resnet18. It's worth noting that doing so would require the overall number of parameters in the PEC models to be reduced to 1.1 million to match the reference architecture. The authors should clarify if the ResNet18 used for comparison is the original one or a modified version, and if modified, which specific changes were applied.


* **Discriminative Exemplar-Free Class Incremental (EFCIL) Comparison**: Comparing PEC, an online exemplar-free method, with other common exemplar-free approaches is crucial. In the main paper, only EWC [a] and Label Trick[b] are evaluated, with EWC designed for offline continual learning and not suitable for online settings. Other common weight regularization methods, such as MAS [c] and SI[d], are typically evaluated in the online continual learning literature, since they allows to compute online the weight importance. Moreover, LwF[e], regularizing output with knowledge distillation, is known to outperform weight regularization methods and is suitable for online settings.The absence of this comparison is noteworthy. The only other baseline provided by the authors in the main paper is "Label Trick"[b], involves training only the head of the current task. Nowadays, this is a common practice in exemplar-free approaches, since it has been shown to work better. All the exemplar-free implemented methods (included LwF) on FACIL (Masana et al. [f]) use this practice. All the exemplar-free method reported in the main paper must apply this trick. Moreover, in Appendix C.1.1, various EFCIL methods are presented, and it might be beneficial to move some of them to the main paper, implementing the Label Trick where applicable for a more comprehensive evaluation. The authors should clarify if the "Label Trick" is applied to all the EFCIL methods, and if not, why not.


 
* **Discriminative Exemplar-Based Class Incremental (EBCIL) Comparison**: PEC is an **Online** method. When comparing it with exemplar-based method, it is essential to align the compared methods with the current **Online** EBCIL literature. ER, A-GEM, DER++, ICARL, already reported in the main paper,  are common comparison in the online literature. On the other hand, BiC is an **offline**  method. This is because it requires additional epochs on a validation set to calibrate the classifier(thus violating online incremental constraints). X-DER, a recent work, is original designed in the multi-epoch setting (i.e. offline) but has been adapted in this paper to work in online setting. To ensure a comprehensive comparison with the current online literature, it's important to consider additional relevant approaches.  A straightforward  baseline to provide is "ER + LwF". Notably, ER-ACE [g] has recently delivered state-of-the-art results in online continual learning, so it is advisable to include this comparison in the main paper. Other approaches that should be evaluated include SCR [l] and RAR [m]. For a more extensive list of relevant comparison, you can refer to  Cormerais et al. [n]. The authors should justify the choice of EBCIL methods and explain why offline methods are included in the comparison.

* **Memory Requirements & Inference FLOPS Computation**: Regarding the **Memory Requirements**, PEC requires a linear increase of parameters with the number of classes encountered. While the authors acknowledge this intrinsic challenge in their approach and have discussed it in the limitations section, a more detailed analysis is necessary. Specifically, it's essential to examine how many parameters are utilized by each predictor networks per dataset and by the teacher network, to understand how much the memory increases across the tasks. As for the **FLOPS comparison**, the authors have not provided an analysis of the number of Floating Point Operations (FLOPS) required by their model. Since online methods are intended to work in environments with hardware resource limitations, it is advisable to disclose the number of FLOPS for both backward and forward passes. For training, FLOPS evaluation can be carried out, as demonstrated by [o]. As regards the inference step, in Section 3.1 the authors say that only two forward passes are needed to obtain the classification scores – one for the a merged student, and one for the teacher network. While this is true, considering the online nature of their method and its intended use in resource-constrained settings, it is crucial to provide and compare the overall number of FLOPS required by the forward pass for both teacher and student networks. Therefore, it is necessary to determine how much the FLOPS of PEC method increases compared to current state-of-the-art methods. The authors should provide a detailed analysis of the memory requirements and FLOPS, including a breakdown of the parameters for each network component and the number of FLOPS for both training and inference.


* **Buffer Balancing and Equal Budget**: The authors assert that their approach is afflicted by class imbalancing.However, they do not provide any theoretical motivation for this claim; they hypothesize that the issue may be linked to the number of gradient updates, as mentioned in Section 4.4 of the main paper. In cases where no theoretical motivation is available, it is necessary to conduct a detailed analysis that elucidates the factors contributing to this behavior. To address the class imbalancing issue, they authors introduce two strategies in the experimental section: Buffer Balancing and Equal Budget Strategies. While the easier Equal Budget Strategy it is well-explained in the paper (and in supplementary Section B.2), the **Buffer balancing**, based on CMA-ES optimization is considerable more complex and difficult to grasp. Therefore, additional details on how this optimization algorithm is used for online-class incremental learning should be provided to enhance understanding. Finally, a natural question arises: How well do existing methods perform in the class imbalancing setting compared to PEC? The authors should provide a more detailed explanation of the Buffer Balancing strategy, including the specific parameters used and the optimization process. Additionally, they should compare the performance of existing methods in class imbalanced settings.

### Questions
My major concerns and questions are in the weakness section. However, there are other experiments that can further support the evaluation of the proposed approach and can help understand the performance of the  proposed method: 

* **Ablation on the proposed method - PEC vs Ensemble Discriminative Classifiers**: PEC takes inspiration from Random Network Distillation (Burda et al. 2018), originally  designed for detecting novel states in reinforcement learning, and from work of Ciosek et al. 2020. [q], which focused on  uncertainty estimation for out-of-distribution (OOD) detection. Notably, Ciosek et al. demonstrated that Random Priors outperformed Network Ensembling. PEC adapts the concept of Random Prior to the  incremental learning setting, using a Random Prior Network and training a single prediction network per class. This naturally leads to the question of how well their proposed method performs in comparison of  ensembling with multiple discriminative classifiers. Ensembling multiple discriminative classifiers involves training small networks  equipped with a Softmax Layer for each task, and then taking the argmax of the prediction across the models. This evaluation can be conducted with multiple classes per task, which is relatively easier than the single-class per task scenario but quite common in the online continual learning community. To perform these experiments requiring a network per task, an architecture with the structure similar to the one provided by Zenke et al. ([d] Appendix A) can be employed. 


* **Ablation on the proposed method - PEC vs Discriminative Classifier**: Although the reduced Resnet18 is used for comparison (as mentioned in the first point of weakness section), it is essential to note that training a deep network is inherently more challenging than training a shallow network, as performed by PEC. Additionally, when using a reduced ResNet18 architecture, a state-of-the-art online method should address the issue of Batch Normalization, which is currently a challenge in online class incremental learning [p]. PEC may have an advantage in this context since it employs shallow models for which batch normalization is not necessary.  To gain a deeper understanding of how well PEC performs compared to the discriminative methods, it would be valuable to evaluate some of the sota  methods (exemplar-free and exemplar-based) on SplitCifar100 or minImagenet datasets without using ResNet architecture. An option is to use the network provided  by Zenke et al. [d](Appendix A), not using batch normalization.This can help eliminate any bias stemming from architecture-specific issues in  incremental learning providing a better understanding of how well Prediction Error Based Classification performs in comparison to Discriminative classification.




**Summary Of The Review**

The paper introduces an adaptation of the Random Prior Network for Online Continual Learning. The theoretical foundation of this adaptation is not entirely novel, as it relies on the theory presented by Chosek et al. [q]. However, the application of the theory to the PEC classification framework in the context of online continual learning is interesting. 

Unfortunately, I have significant concerns  pertaining the experimental evaluation. The paper lacks a comprehensive and properly aligned comparison with the current literature on online continual learning, as mentioned in Weakness Section Points 1, 2, and 3.  Additionally, the paper does not provide  comprehensive assessments of Memory Impact and FLOPS Comparison, as noted in Weakness Section Point 4. Finally to enhance the quality of the experimental evaluation and to understand how much the proposed method works well, it would be beneficial to include a more thorough ablation study of the proposed method, as suggested in Question Section Points 1 and 2. 

Taking into account the above considerations, I believe that the paper still needs substantial work to be carried out, before it can be considered for publication. I thus believe that it shall not be accepted at the current issue of ICLR.

**References**

[d] Zenke et al. (2017). Continual Learning Through Synaptic Intelligence. Proceedings of machine learning research. 

[p] Q. Pham, C. Liu, H. Steven, "Continual Normalization: Rethinking Batch Normalization for Online Continual Learning," in International Conference on Learning Representations, 2022.

[q] Ciosek, Kamil et al. “Conservative Uncertainty Estimation By Fitting Prior Networks.” International Conference on Learning Representations (2020).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
