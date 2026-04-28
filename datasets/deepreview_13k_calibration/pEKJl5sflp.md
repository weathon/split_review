# Scalable Modular Network: A Framework for Adaptive Learning via Agreement Routing

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we propose a novel modular network framework, called Scalable Modular Network (SMN), which enables adaptive learning capability and supports integration of new modules after pre-training for better adaptation.
This adaptive capability comes from a novel design of router within SMN, named agreement router, which selects and composes different specialist modules through an iterative message passing process.
The agreement router iteratively computes the agreements among a set of input and outputs of all modules to allocate inputs to specific module.
During the iterative routing, messages of modules are passed to each other, which improves the module selection process with consideration of both local interactions (between a single module and input) and global interactions involving multiple other modules.
To validate our contributions, we conduct experiments on two problems: a toy min-max game and few-shot image classification task. 
Our experimental results demonstrate that SMN can generalize to new distributions and exhibit sample-efficient adaptation to new tasks. 
Furthermore, SMN can achieve a better adaptation capability when new modules are introduced after pre-training. 
Our code is available at https://github.com/hu-my/ScalableModularNetwork.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel approach for scalable modular framework. They propose a unique method for learning routing among a set of modules by averaging outputs across input tokens, computing agreement with each of the input tokens, refining the outputs based on this agreement, and finally aggregating these refined outputs for final  classification. The method showcases adaptability to a new task (parity code task) after training on a different task (min-max detection). However, the scalability and adaptation mechanisms, especially when new modules are introduced or when there are multiple layers of modules, are not clearly explained.

### Strengths
1. The method displays remarkable results on a toy dataset and adapts well to new tasks (parity code task)
2. Better performance on the ConvNet backbone for few-shot classification task on real-world datasets as compared to previous methods.

### Weaknesses
1. The scalability of the proposed method is not clearly demonstrated. The paper does not specify how the weights \(W_a\) in the agreement router and \(W_c\) in the module parameters are adapted when new modules are introduced. This is a crucial aspect for understanding the method's applicability to more complex scenarios where the number of modules might grow significantly.
2. The paper proposes a method that works on a single layer, which is quite restrictive. The authors do not elaborate on how the method translates when using multiple layers of modules. This raises concerns about the method's generalizability to deeper architectures, which are common in modern deep learning.
3. A detailed computational cost analysis is missing. This is crucial for understanding the trade-offs between performance and computational resources, especially since the proposed method seemingly demands more compute by activating all modules repeatedly. The authors should provide a comparison of FLOPs, training time, and inference time with other relevant methods.
4. The performance on the ViT backbone does not mirror the improvements seen on the ConvNet backbone. This inconsistency raises questions about the method's robustness and its ability to generalize across different backbone architectures. The authors should investigate the reasons behind this discrepancy and discuss potential limitations.
5. The method needs additional loss terms to prevent degeneracy, similar to Top-K approaches. Without a mechanism to ensure that different modules are utilized, the model might converge to a solution where only a few modules are consistently selected, defeating the purpose of having a diverse set of modules.

### Questions
1. How is \(W_a\) adapted when new modules are introduced, and how does this adaptation impact the performance ?
2. Can you explain the relationship between \(y\) from Equation 4 and the outputs from the modules?
3. How does the method work when there are multiple layers of modules?
4. In Equation 12, is W_c frozen or trainable when new modules are added?
5. With only two modules, what is the value of K in the Top-K method in Table 1, and how does this compare to an Ensemble approach where all modules are activated?
6. Could you provide more insight on what occurs in every iteration of the proposed method, and elaborate on the notion of agreement in this context?
7. Could you add more on the trade-off between computational cost and accuracy of the proposed method vs prior methods?
8. Is there a plan to conduct experiments showcasing the scalability of the method, particularly when adapting to a new task by adding new modules without forgetting old tasks? You can choose the same setup of learning min-max detection and parity code task one after the other by adding new modules.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an innovative modular network framework, the Scalable Modular Network (SMN), which represents a significant advancement in the realm of adaptive learning. SMN not only enhances the capacity for adaptive learning but also offers a seamless mechanism for integrating new modules post pre-training, thus markedly improving overall adaptability. This adaptive process is underpinned by the ingenious "agreement router" integrated within SMN, which streamlines the module selection process by carefully weighing both local and global interactions. Throughout the experimental validation on two distinct problems, a toy min-max game, and a few-shot image classification task, SMN consistently showcases remarkable generalization abilities to new data distributions and demonstrates sample-efficient adaptation to novel tasks. Notably, SMN's adaptation capabilities are further enhanced when new modules are introduced after pre-training. These results underscore the potential of the SMN to continually evolve and improve its adaptive capabilities.

### Strengths
1. This paper effectively presents the motivation behind the study and articulates the issues addressed by the proposed method in a well-structured manner.
2. The authors provide a comprehensive review of existing methods related to modular neural networks. They also meticulously analyze the drawbacks and issues that need resolution in these existing approaches.
3. The Scalable Modular Network (SMN) is presented as a concise and efficient method with remarkable clarity in both its rationale and technical details. The paper offers ample explanations, discussions, and evidence to underpin the theoretical foundation of SMN. 
4. The inclusion of implementation details and experimental settings further substantiates the fairness of comparisons across two distinct problems. 
5. Moreover, the study hints at the significant potential value in large-scale modular networks capable of seamlessly integrating additional modules.

### Weaknesses
1. The experiments conducted on a toy min-max game and few-shot image classification may not be sufficient to definitively establish the overall superiority of SMN, considering that SMN is positioned as a general framework. Additional experiments on a wider range of datasets and tasks, including more complex and diverse problems, would better illustrate the effectiveness of the method. For example, evaluations on tasks with higher dimensionality or more complex dependencies could reveal limitations not apparent in the current experiments. Furthermore, the current tasks are relatively low-dimensional; testing on high-dimensional data would be crucial to assess the scalability of the proposed method.
2. The paper falls short in providing adequate explanations of limitations and training costs. Specifically, the computational cost of the agreement router, which requires iterative calculations across all modules, is not thoroughly discussed. The paper should provide a detailed analysis of the time and memory complexity of the proposed approach, especially in comparison to alternative methods. Additionally, the limitations of the modular architecture, such as potential bottlenecks or challenges in scaling to a large number of modules, should be addressed.

### Questions
Please kindly find the comments in the weakness section.

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
The paper introduces the Scalable Modular Network (SMN), a modular framework with adaptive learning capabilities that can incorporate new modules after initial training for better adaptation.

**Key Features:** 
- **Agreement Router:** A unique component in SMN that iteratively selects and assembles specialist modules based on both local and global interactions.
  
- **Dynamic Module Selection:** Allows SMN to adjust module combinations adaptively based on input data.

- **Scalability:** Enables the addition of new modules post-training, enhancing adaptability.

**Benefits:** 
SMN efficiently selects modules for new samples, generalizes for out-of-distribution data, and can differentiate between similar sub-concepts using global information.

**Experiments:** 
Tests on a toy min-max game and few-shot image classification demonstrated SMN's adaptive capabilities, especially when adding new modules post-training.

**Significance:** 
SMN offers a solution to the challenge of composing specialist modules in neural networks, moving closer to achieving human-like learning efficiency in machines.

### Strengths
1. **Agreement Router:** Introduces a dynamic module selection mechanism, mirroring human cognitive abilities for efficient and adaptive learning.

2. **Scalability:** Allows for the integration of new modules post-training, ensuring the network's adaptability and evolution.

### Weaknesses
1. **Limited Experimentation:** The experiments are overly simplistic, conducted only on small datasets. The evaluation is limited to a toy min-max game and few-shot image classification using standard datasets. There is a lack of evaluation on more complex tasks or larger, more challenging datasets, which limits the assessment of the method's scalability and generalization capabilities.
 
2. **Lack of Broad Testing:** Results focus solely on classification tasks, with no results provided for large language models like LMM. The paper does not explore the applicability of the proposed method in other domains such as reinforcement learning, natural language processing, or time series analysis. This narrow focus restricts the understanding of the method's versatility and potential impact.

3. **Additional Fine-tuning:** The addition of new modules still requires extra fine-tuning, implying integration isn't as seamless as desired. The need for fine-tuning after adding new modules suggests that the method is not fully adaptive and may require significant computational resources and labeled data to integrate new modules effectively. The paper does not provide a detailed analysis of the fine-tuning process, including the number of samples required and the computational cost.

4. **No Comparison with MOE:** The paper doesn't offer a comparison with established methods like MOE, limiting the understanding of its relative performance. The absence of a comparison with Mixture of Experts (MoE) architectures, which are also designed for modularity, makes it difficult to assess the novelty and advantages of the proposed method. A direct comparison with MoE would provide valuable insights into the strengths and weaknesses of SMN.

5. **Efficiency Overlooked:** There's no comparison or discussion regarding computational efficiency or time delays, making it hard to assess the practicality of deployment. The paper lacks a thorough analysis of the computational cost, including FLOPs, training time, and inference time. Without this information, it is challenging to evaluate the practical feasibility of deploying SMN in real-world applications, especially those with resource constraints.

### Questions
See the weakness.
Additional Question:

1. **Pre-training Paradigm:** The abstract mentions the applicability of SMN in pre-training paradigms, but there seems to be limited experimental evidence or discussion on this. How does the SMN truly perform in a pre-training context?

2. **Comparison with Current Techniques:** Modern pre-training often employs methods like contrastive learning or MLM (Masked Language Model) loss. Is there a significant gap between SMN and these prevalent techniques? How does SMN align or differentiate from these established methods?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents Scalable Modular Network for better adaptive learning by incorporating new modules after pre-training. An agreement router is proposed to select specialist modules using an iterative message passing process. The approach is evaluated with a min-max game task and few-shot image classification task.

### Strengths
1. Modular networks have certain advantages in some machine learning settings such as meta-learning and continual learning.
2. The proposed agreement router is novel and effective.

### Weaknesses
1. Some evaluation under continual learning setting may be desirable. Evaluation in the paper is not sufficiently strong with one toy task and one few shot learning setting.

### Questions
1. Fix typos, e.g, "impose constrains on the number of activated..."

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
