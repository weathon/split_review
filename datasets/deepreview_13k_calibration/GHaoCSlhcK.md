# PROGRESSIVE KNOWLEDGE DISTILLATION (PKD): A MODULAR APPROACH FOR ARCHITECTURE-AGNOSTIC KNOWLEDGE DISTILLATION

- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 5, 5, 3, 3

## Abstract
\textbf{Knowledge distillation (KD)} is a key technique for training \textbf{lightweight deep neural networks}, particularly in \textbf{resource-constrained environments}. While existing KD methods utilize intermediate features to improve student models, they often overlook the proper \textbf{alignment between teacher-student layers} and fail to select the most \textbf{informative data} for training each student layer. These limitations are especially pronounced in \textbf{architecture-agnostic scenarios}, where different network architectures complicate knowledge transfer.

We propose \textbf{PKD}, a \textbf{Progressive Knowledge Distillation} framework that progressively aligns teacher and student layers through \textbf{feature-based modularization}. Each student module is trained using the most \textbf{representative features} from its corresponding teacher module, starting with the shallowest layers and progressively moving to deeper ones. This training method enables efficient, architecture-agnostic knowledge transfer across a variety of model architectures. \textbf{Experiments on CIFAR-100 and ImageNet-1K} demonstrate that PKD outperforms baseline models, achieving performance improvements of up to \textbf{4.54\%} and \textbf{6.46\%}, respectively, thereby validating its effectiveness in diverse neural network settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a new method for knowledge distillation from teacher models to student models. The main idea is to divide the teacher model and the student model into several different modules by using a metric CKA defined in previous works, and align the feature representations of the corresponding modules on the teacher and student models. The authors propose to use PCA to extract informative features in the modules across a set of samples, and minimize the difference between those informative features in the teacher and student models. Results on several dataset across different combinations of teacher models and student models showed good results of the proposed method.

### Strengths
1. The idea is novel to me. It includes using CKA to group the layers of a neural network into different modules and using PCA to align the module representations of the teacher model and the student model. 
2. The results are strong compared with existing methods.

### Weaknesses
The main weakness is the poor presentation, which makes the methods unclear. I don't mean that the language is poor, which is easy to fix; what I mean is the entire presentation. There are numerous things unclear in the description of the method. In fact, even the main optimization problem such as the loss function is unclear. Let me start with this point.

1. What's the main optimization problem? Is eqn (2) the loss function? If yes, then how do you encourage the representations of two modules in the teacher model and student model to be similar, by considering that eqn (2) doesn't containt this kind of term? Is it eqn (7)? But the optimization variable of this problem is the 0-1 vector c, not the weights of the student model.  Please explicitly state the main optimization problem and clarify how the different equations (2 and 7) relate to the overall optimization process for the student model. Please provide a clear explanation of how the similarity between teacher and student model representations is encouraged in the optimization process.

2. The main contribution of the work, using PCA to extract the most informative feature of a module, is poorly described. In fact I doubt the correctness of the method. Assume the original data matrix A has n rows (corresponding to n samples) and m rows (corresponding to m features). After doing PCA, A is transformed to another matrix B of n samples and k rows, and usually k<m. It is impossible that B is part of A. But L233-239 indicate that PCA selects some columns (indicated by KI) of the original data matrix R_i to form a new matrix. Please provide a step-by-step explanation of their PCA process, clarifying how it differs from standard PCA if that's the case.
In addition, eqn (3) defines a single item mv, so-called mean variance. It's an average over m features. But the text below the equation states that we need sort mv. For a single item, how do we sort it? BTW, Please also specify the meaning of the symble |X| in eqn (3).

3. How do we solve the optimization problem in eqn (7)? The optimization variable is a 0-1 vector, which makes the problem a descrete optimization problem, which is hard to solve. Please provide details on the specific algorithm you used to solve this discrete optimization problem, and discuss any approximations or relaxations if applicable.

4. Why do we need the optimization problem defined in eqn (7)? In my opinion, we can simplely force the student model to have the same number of modules as the teacher model, then distill knowledge from the module(i) in the teacher to the module (i) in the student, and progress from i=1 to the total number of modules. Why do you need to select an "optimal" set of modules from the student for distillation? Please explain the advantages of the proposed approach using eqn (7) compared to this simple method, or consider including a comparison with this simple approach in the experiments.

5. As some techniques are from (Wang et al., 2024), which also deals with KD between different architectures, then what's the major difference between this work and that work? In fact, the paper doesn't discuss the relationship between the proposed work and other works about KD between different architectures. The writing gives readers a false impression that this is the first work that deals with KD between different architectures. Please have a more detailed comparison with previous methods to highlight the specific novel contributions of the proposed approach.

6. In experiments, for doing PCA on the teacher model, how many input samples were used? By setting the variance threshold 10^-4, usually (for both teacher and student) the feature dimensions were reduced from what numbers to what numbers? Please discuss how sensitive the results are to these parameters (number of input samples and variance threshold) and provide more details on the typical reduction in feature dimensions for both teacher and student models.

7. The paper mentions several times about Appendix, but I don't find it. Please remind me where it is if the authors did uploaded it.

### Questions
The first four questions listed in the weakness section above.

### Soundness
2

### Presentation
1

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
This paper mainly targets improving knowledge distillation through heterogeneous structures and proposes a progressive manner to achieve the goal. Specifically, the layers are first categorized into a set of functional modules whose features are close in between the same module and distant across different modules. Knowledge distillation is then conducted progressively according to the sequence from shallow to deep modules to ensure the best knowledge transfer efficiency in heterogeneous knowledge distillation. Moreover, PCA is utilized to select the most important features to optimize the distance from the teacher.

### Strengths
1. This paper adopts a progressive modular and sequential training pipeline for knowledge distillation, which is soundly motivated as the learning of deep networks inherently endows different levels of abilities for different layers. Therefore, the progressive modular and sequential training also appears to be an implicit curriculum learning pipeline to learn gradually from low-level features to high-level conceptual understandings. 
2. This method's performance is competitive, as its accuracy on most heterogeneous benchmarks outperforms OFA and many other representative works. 
3. This study groups different layers into different modular groups according to their CKA distance instead of intuitive grouping according to layer indices. This idea is interesting as it avoids possible misalignment in the features of different architectures.

### Weaknesses
1. The idea of progressive internal knowledge distillation from shallow to deep layers has already been proposed [1], which shares a similar learning curriculum to align the shallow layers first and then the deep layers.
2. The designed pipeline is too complicated to scale up. For example, the step that discerns what features are to be aligned requires PCA and the computation of the Gram matrix of deep features. As the network parameters and resolution of images scale up, it would soon become a computational bottleneck for real visual applications.

### Questions
While this study's performance in heterogeneous knowledge distillation is appealing, the reviewer is still more concerned about its complexity and potential inability to scale up. Therefore, I would like to vote for weak reject as for now, but I am open to changing my scores if the authors address my concern.

### Soundness
3

### Presentation
2

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
The paper proposes a Progressive Knowledge Distillation (PKD) method for teacher-student pairs with heterogeneous architectures. It first divides the teacher and student networks into several modules based on feature similarity. Then, it selects representative teacher-student features using PCA analysis and enforces their alignment. Experimental results on CIFAR-100 and ImageNet-1K demonstrate clear accuracy improvements over selected baselines.

### Strengths
1. Promising experimental results. The proposed PKD consistently outperforms the selected baselines across various teacher-student network configurations.
2. Clear and detailed description of the experimental settings.

### Weaknesses
1. **Limited discussion of related works** on heterogeneous architectures and PCA-based methods. Below are some relevant examples. The authors are encouraged to conduct a more thorough literature review. Without a clear differentiation from existing methods, there is a concern about the novelty of the paper.  
   - Liu, Yufan, et al. "Cross-architecture knowledge distillation." *ACCV 2022*.
   - Hofstätter, Sebastian, et al. "Improving efficient neural ranking models with cross-architecture knowledge distillation." *arXiv:2010.02666* (2020).
   - Ni, Jianyuan, et al. "Adaptive Cross-Architecture Mutual Knowledge Distillation." *FG 2024*.
   - Chiu, Tai-Yin, and Danna Gurari. "PCA-based knowledge distillation towards lightweight and content-style balanced photorealistic style transfer models." *CVPR 2022*.
   - Guo, Yi, et al. "RdimKD: Generic Distillation Paradigm by Dimensionality Reduction." *arXiv:2312.08700* (2023).

2. **Unclear necessity and effectiveness of using CKA** for modularization. An ablation study comparing CKA-based modularization with simpler approaches, such as dividing networks based on feature map resolution, should be included. The current justification for using CKA is not sufficiently strong, particularly given the computational overhead it introduces compared to simpler alternatives. The paper should also address whether CKA is truly necessary for all architectures, or if simpler methods suffice for certain cases.

3. **Writing quality could be improved** to enhance rigor and clarity. For example:  
   - In lines 56-57, the phrase “it begins by training … representative features are transferred first” is unclear. It is not intuitive why training the shallowest module would ensure the most representative features. The paper lacks a clear explanation of why the shallowest layers are considered to contain the most transferable features, and how this assumption is validated.
   - There may be no need to distinguish between the two types of representation distances $d_{SM}$ and $d_{DM}$, as they are calculated in the same way. The paper should clarify the practical implications of this distinction, or remove it if it does not add value.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Progressive Knowledge Distillation (PKD) framework which progressively aligns teacher and student blocks through feature-based modularization. The alignment is based on CKA (centered kernel alignment) instead of MSE. The aligned feature is derived from PCA and named module-specific feature. Experiments on CIFAR-100 and ImageNet-1K demonstrate that PKD beats baseline models by a large margin.

### Strengths
Strengths:
+ Using CKA to replace MSE looks interesting;
+ Replacing original block output with module-specific-feature looks somewhat interesting;
+ The performance looks good.

### Weaknesses
Weakness
+ there are a bunch of existing works on progressive knowledge distillation, this papers does not mention and compare with. Here just listed a few published works below 
     
       + Self-knowledge distillation with progressive refinement of targets, ICCV 2021
       + Follow your path: a progressive method for knowledge distillation, ECML 2021
       + Progressive Blockwise Knowledge Distillation for Neural Network Acceleration, IJCAI 2018
       + Kernel based progressive distillation for adder neural networks, NeurIPS 2020
       + ...

+ What about the complexity of the propose method when comparing with other baselines?
+ The experiments are fairly small scale on CIFAR and ImageNet. Is it possible to show some results on large language models?
+ How do you pick the corresponding blocks/modulars for student network is still not very clear? Does this correspondence impact the final results? I hope the authors could elaborate more on this point.

### Questions
See previous weakness part for my questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the challenge of feature alignment in feature-based knowledge distillation (KD). The authors propose a novel method named PKD, consisting of two main components: Network Modularization, which groups layers in the networks into several distinct modules for distillation, and Modular Feature Alignment, which seeks to find the optimal alignment between the modules obtained from both the teacher and student networks. The method is evaluated on the CIFAR-100 and ImageNet-1K datasets, showing superior performance over existing methods.

### Strengths
1. The studied problem is significant. Feature alignment is a critical issue in hint-based knowledge distillation.
2. The performance improvement of the perposed method is remarkable

### Weaknesses
1. The method lacks novelty, as using CKA in loss functions is not a new approach [1,2].
2. Several modules in the method require an initial run of multiple epochs to determine optimal configurations, which introduces additional training overhead. Moreover, the selection of initial training epochs for each module introduces multiple hyperparameters that need to be tuned.
3. Ablation studies on the initial training epochs, loss function, and the threshold $\epsilon_{th}$ would be valuable to assess the impact of these elements.
4. Equations should follow a consistent style, and figures should be presented in high resolution for improved readability.

### Questions
Please follow the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
