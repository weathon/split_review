# BiDoRA: Bi-level Optimization-based Weight-Decomposed Low-Rank Adaptation

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
Parameter-efficient fine-tuning (PEFT) of large language models (LLMs) has gained considerable attention as a flexible and efficient way of adapting LLMs to downstream tasks.
Among these methods, weighted decomposed low-rank adaptation (DoRA) has emerged as a promising approach.
DoRA bridges the gap between low-rank adaptation (LoRA) and full fine-tuning (FT) by decomposing the weight matrices into magnitude and direction components, thereby maintaining learning behavior similar to FT.
Although DoRA shows encouraging performance, it introduces additional parameters compared to LoRA, which potentially increases the risk of overfitting.
Moreover, optimizing magnitude and direction simultaneously leads to a coupled gradient updating pattern for both components, limiting its learning capacity.
To overcome these limitations, we propose BiDoRA, a bi-level optimization-based PEFT method.
In BiDoRA, the direction and magnitude components are optimized on two distinct datasets at different optimization levels, mitigating the risk of overfitting.
Additionally, the asynchronous optimization of the two components promotes their decoupling, allowing for more flexible gradient updates suitable for various downstream tasks.
Evaluation of BiDoRA on fourteen datasets spanning natural language understanding, natural language generation, and token classification reveals that it significantly outperforms DoRA and other PEFT methods.
The superior performance of BiDoRA underscores its effectiveness.
The code for BiDoRA is available at \url{https://anonymous.4open.science/r/BiDoRA-5D31}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a method for parameter efficient fine tuning using bi-level optimization that competes with LoRA. Results test it on training RoBERTa and GPT-2 medium for NLU and NLG tasks respectively. The overall results demonstrate consistently better results than LoRA and DoRA.

### Strengths
- In experiments, the proposed method demonstrates consistently superior results compared to the others.
- The paper was written reasonably clearly, so I was able to follow the equations.

### Weaknesses
 - The motivation for the bi-level optimization approach was a bit vague. I did read the explanation in the introduction, but it says "Furthermore, in DoRA, the magnitude and incremental direction components are optimized concurrently, leading to a highly constrained updating pattern that may overlook the diverse learning patterns required for different downstream tasks." It is not clear what this means concretely... Specifically, it's unclear how concurrent optimization of magnitude and direction in DoRA leads to a 'highly constrained updating pattern'. A more detailed explanation of the limitations of concurrent optimization, perhaps with a concrete example of a scenario where it fails, would be beneficial.
- Experiments were on models that do not represent the state of the art at this point. It would be much more convincing if the methods were demonstrated to work on more powerful models (e.g. at least 7B). The current experiments on RoBERTa and GPT-2 medium, while useful as a starting point, do not fully demonstrate the scalability and effectiveness of the proposed method on more complex and larger models. The paper should include results on models that are more representative of current research trends.
- As noted in 5.7, the proposed method is accompanied with significant additional training time, which may limit its practical usefulness. The paper acknowledges the increased training time, but it does not provide a thorough analysis of the trade-off between increased performance and computational cost. A more detailed discussion of the practical implications of this increased training time, including the potential impact on resource usage and overall efficiency, is needed.

### Questions
None

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Low-Rank Adaptation (LoRA) is a parameter-efficient fine-tuning (PEFT) method. Weighted Decomposed Low-Rank Adaptation (DoRA) is a variant of LoRA, where the update matrix is decomposed into two components: magnitude and direction.

This paper argues that the additional parameters in DoRA increase the risk of overfitting, and simultaneously optimizing both magnitude and direction limits its learning capacity. To address these issues, the authors introduce Bi-Level Optimization-Based Weight-Decomposed Low-Rank Adaptation (BiDoRA), which integrates bi-level optimization into DoRA.

The core idea of BiDoRA is to separate the optimization of magnitude and direction. In the first phase, BiDoRA alternately trains magnitude and direction until convergence. Additionally, the training data for these two components is separated to further prevent overfitting: the magnitude is trained on a validation set, while the direction is trained on a training set. In the second phase, the direction is further trained on the combined dataset until convergence.

Experiments are conducted on natural language understanding (NLU), natural language generation (NLG), and token classification tasks. BiDoRA shows marginal improvements over the baselines, with almost all gains being less than 1 percentage point. Ablation studies reveal that the effects of different design components are relatively small. The training time for BiDoRA is 3.92 times that of LoRA, while DoRA requires 1.3 times the training time of LoRA.

### Strengths
* The paper is well-written and easy to understand.
* The authors' efforts to evaluate across multiple tasks are commendable. However, there are still many problems with these evaluations (see Weaknesses).

### Weaknesses
1. **The motivation of this paper appears to be questionable.** The authors claim that DoRA increases the risk of overfitting, basing this on two pieces of evidence:

   - DoRA introduces additional parameters compared to LoRA.
   - The gap between training and test accuracy curves for DoRA is larger than that of BiDoRA.

   However, these two points do not convincingly support the claim. First, while additional parameters can sometimes contribute to overfitting, they are not a sufficient condition for it. In fact, DoRA adds only a negligible number of parameters (0.01% of the model size, as reported by the authors) beyond LoRA. Moreover, prior work suggests that LoRA learns less than full fine-tuning and may even act as a form of regularization, implying that the risk of overfitting is generally low across these PEFT methods. The authors' argument that the small parameter increase in DoRA causes overfitting is not well-supported, especially considering the relatively small number of additional parameters. The claim that the training curves are indicative of overfitting is also weak, as these curves are highly sensitive to various factors like hyperparameters, model architecture, and dataset characteristics. The authors present results from only a single configuration, which limits the generalizability of their findings. Furthermore, the authors’ attribution of an *alleged overfitting problem* to DoRA’s concurrent training lacks a strong foundation. The core issue is that the evidence provided does not strongly link the concurrent training of magnitude and direction in DoRA to an increased risk of overfitting.

2. **The proposed BiDoRA method is overly complex and difficult to use.** It requires a two-phase training process, with the first phase itself consisting of two sub-steps. It also introduces two additional hyperparameters: the weight of orthogonality regularization and a ratio for splitting training and validation sets. This adds significant complexity to the training process, making it less practical. The increased complexity is not justified by the marginal performance gains. The method requires careful tuning of multiple hyperparameters and a multi-stage training process, which significantly increases the barrier to adoption. As a result, BiDoRA takes 3.92 times longer to train than LoRA, while DoRA requires 1.3 times the training time of LoRA, which is a substantial increase in computational cost for minimal performance gains.

3. **Performance differences between methods are minimal across evaluations**. In nearly all results, the performance differences between the methods are less than 1 percentage point, which may be attributable to random variation. Furthermore, the benchmarks selected are outdated and likely saturated. The reported improvements are not statistically significant, and the gains are too small to justify the added complexity and computational cost of BiDoRA. The lack of substantial performance improvement raises concerns about the practical value of the proposed method. The marginal gains are not compelling enough to warrant the adoption of a more complex and computationally expensive method.

### Questions
The results in Table 3 do not align with those reported in the original LoRA paper. In the original paper, LoRA achieves a BLEU score of 70.4 with 0.35M parameters. However, in your results, LoRA only reaches 63.7 BLEU with 0.39M parameters. This discrepancy suggests there may be errors in your evaluation or setup.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes BiDoRA, a new fine-tuning method that:
1. Decomposes the model’s weights into two parts—magnitude and direction.
2. Optimizes each part separately: The "direction" part is trained on one dataset split (training set), while the "magnitude" part is optimized using another split (validation set).
3. Iterates between these two optimization levels to decouple the updates, helping the model generalize better.

This bi-level approach allows BiDoRA to perform more like full fine-tuning while avoiding overfitting. In experiments across various NLP tasks, BiDoRA consistently outperforms other parameter-efficient fine-tuning methods like LoRA and DoRA. The authors validate BiDoRA on natural language understanding, generation, and token classification tasks, showing that it reduces overfitting and achieves better overall performance than existing methods.

### Strengths
Originality: BiDoRA introduces a unique bi-level optimization approach to fine-tuning large language models (LLMs), addressing a common tradeoff in parameter-efficient fine-tuning (PEFT) between generalization and computational efficiency. By decomposing the model’s weights into magnitude and direction components and optimizing each on different data splits, BiDoRA creatively combines aspects of neural architecture search with PEFT, offering a compelling alternative to current methods like LoRA and DoRA. This methodological innovation could inspire further development in PEFT techniques across domains.

And specifically I think it's interesting that in BiDoRA, both the magnitude and direction components are trainable, but they are optimized separately through a bi-level optimization framework.

Decomposition: The model's weights are decomposed into two parts:

Magnitude (m): Represents the scale of each parameter.
Direction (V): Represents the vector defining the orientation of each weight.
Optimization Approach:
BiDoRA optimizes the direction component at the lower level using a training set split. During this phase, the magnitude remains fixed, allowing the model to focus solely on finding the optimal direction adjustments.
At the upper level, BiDoRA optimizes the magnitude component by minimizing the loss on a validation set split, with the direction component fixed. This stage uses the optimized direction from the lower level to update the magnitude through hyper gradient descent.
Iterative Training:

The magnitude and direction components are iteratively updated until convergence. This iterative decoupling enables each component to learn independently while promoting generalization and reducing overfitting.
This bi-level approach allows each component to be optimized in a way that would ideally yield better performance than traditional PEFT methods, which tend to optimize these components together, leading to coupled gradients and potentially reduced flexibility.

Quality: The paper demonstrates a high level of rigor, with comprehensive experimental evaluations across multiple tasks, including natural language understanding, generation, and token classification. The experiments span diverse datasets, and the authors include robust analyses, such as ablation studies and weight decomposition, that substantiate the effectiveness of the bi-level optimization framework. This thorough evaluation establishes BiDoRA’s consistent performance advantage over existing PEFT methods, solidifying the validity of the approach.

Clarity: The paper is well-organized and clearly articulates both the theoretical underpinnings and practical implications of BiDoRA. Key concepts, such as weight decomposition and bi-level optimization, are introduced methodically, and diagrams aid in visualizing the process. Algorithmic details, hyperparameters, and dataset splits are documented with transparency, making it easier for readers and future researchers to reproduce and build upon this work.

Significance: The introduction of BiDoRA is a valuable contribution to the field of large language model fine-tuning, where computational efficiency is increasingly critical. By reducing overfitting and enhancing generalization, BiDoRA effectively bridges the gap between parameter efficiency and performance, providing a practical solution that could impact a wide range of applications requiring adaptable, high-performing LLMs. Its relevance to real-world LLM deployment in resource-constrained settings adds to the significance of its contributions.

### Weaknesses
Computational Cost and Efficiency: Although BiDoRA shows a significant performance improvement, the bi-level optimization approach introduces a high computational cost, as reported with nearly fourfold overhead compared to LoRA. This could limit BiDoRA’s practicality in scenarios where resources are constrained. An in-depth analysis of ways to reduce computational complexity without sacrificing performance—such as approximations, alternative regularization techniques, or a comparative exploration of optimization strategies with fewer computational steps—would enhance the method’s accessibility.

Hyperparameter Sensitivity and Tuning: The paper provides limited insight into the sensitivity of BiDoRA to hyperparameters like data split ratios, learning rates for each level, and the orthogonal regularization coefficient. Given that bi-level optimization frameworks often require precise tuning, a sensitivity analysis would help clarify the stability of BiDoRA’s performance under various configurations. This analysis would also support practitioners in understanding which parameters are most influential, guiding them in practical applications.

Scope of Evaluation on Model Types and Tasks: While BiDoRA’s evaluation spans diverse NLP tasks, it primarily focuses on RoBERTa and GPT-2 models. Expanding the scope to include additional architectures, particularly those with different structural properties (e.g., BERT or T5), would verify BiDoRA’s generalizability across model types. Furthermore, testing BiDoRA in non-NLP tasks, such as vision or multimodal tasks, would strengthen the claim of BiDoRA as a general-purpose PEFT framework and broaden its potential applications.

Limited Exploration of Overfitting Mitigation: The paper emphasizes BiDoRA’s success in mitigating overfitting through the decoupling of magnitude and direction optimizations. However, it does not provide an in-depth comparison with existing regularization techniques or alternative overfitting mitigation strategies within PEFT. A comparison or ablation study exploring how BiDoRA’s approach to overfitting compares with alternative techniques (e.g., dropout or adaptive regularization) would better demonstrate the unique value of the bi-level approach.

### Questions
Could the authors provide additional details on the computational efficiency of BiDoRA? Given the reported computational overhead (approximately four times that of LoRA), are there strategies under consideration for reducing this cost? For instance, would approximate or adaptive bi-level optimization approaches be feasible to explore?

Since bi-level optimization can sometimes suffer from convergence issues, could the authors clarify the convergence criteria used in BiDoRA? Additionally, are there any stability challenges encountered during training, and if so, how were these addressed? This information would be valuable for practitioners looking to implement BiDoRA in different contexts.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes BiDoRA, a novel method for parameter-efficient fine-tuning (PEFT). While based on DoRA's methodology, it introduces a bi-level optimization approach that optimizes parameters separately. The authors argue that this approach reduces overfitting and enables learning patterns more similar to full fine-tuning. Through experiments across various NLP datasets, they demonstrated that BiDoRA consistently outperforms both DoRA and other PEFT methods.

### Strengths
This work represents a valuable first attempt at applying bi-level optimization to PEFT, extending DoRA's magnitude/direction decomposition in a natural progression. Experimental validation includes a comprehensive evaluation across diverse NLP tasks, such as NLU, NLG, and token classification, with well-suited comparisons to baselines and detailed ablation studies demonstrating the effectiveness of each component. The implementation is both clear and reproducible, contributing to the overall technical completeness of the work.

### Weaknesses
Methodological Limitations: The approach may be perceived as a straightforward combination of existing methods (DoRA + bi-level optimization), which could limit its novelty. Specifically, the application of bi-level optimization, while not directly explored in the context of DoRA, leverages well-established techniques for hyperparameter optimization, making the core contribution incremental. Additionally, the method introduces substantial computational complexity, running at 3.92 times the cost of LoRA, and requires extra hyperparameter tuning, including the learning rate for the upper-level optimization and the finite difference approximation step size. The computational overhead is a significant practical concern, especially when considering the marginal performance gains over simpler methods. To address these issues, improvements in performance relative to computational cost are needed. Developing an automated framework for setting additional hyperparameters, such as Bayesian optimization, could also streamline the process and reduce user intervention, given the sensitivity of bi-level optimization to hyperparameter choices.

Experimental Limitations: The study lacks experiments involving recent large language models (LLMs), which is crucial for validating the method's scalability and effectiveness in modern NLP scenarios. The absence of experiments on models like Llama or similar architectures limits the generalizability of the findings. Furthermore, the study does not sufficiently analyze performance on very small datasets, where overfitting is a significant concern, and has limited exploration of data split ratio effects, which can influence the stability and convergence of bi-level optimization. To enhance experimental rigor, including evaluations with larger, contemporary models, examining performance across varying dataset sizes, and conducting sensitivity analyses across different split ratios would offer a more comprehensive assessment of the method’s effectiveness. Specifically, experiments should include datasets with fewer than 1000 training samples to evaluate the method's robustness to small data regimes.

Theoretical Limitations: The paper currently provides limited theoretical guarantees for generalization performance and lacks convergence analysis for the bi-level optimization approach. While bi-level optimization has been studied, the specific application within the DoRA framework requires a tailored analysis. Strengthening the theoretical foundation could be achieved by introducing an upper bound analysis for generalization error, demonstrating how the bi-level approach reduces error compared to standard fine-tuning, and supplying a convergence proof for the optimization algorithm, showing that the method converges to a stable solution under reasonable assumptions. The absence of such analysis makes it difficult to understand the conditions under which the method is guaranteed to perform well.

### Questions
1) Are there experimental results involving larger, more recent LLMs?
2) Is there an analysis for cases with very small dataset sizes?
3) Are there optimization plans in place to reduce computational complexity?
4) Is there additional analysis on how the choice of data split ratios affects performance?
5) Can theoretical guarantees for generalization error be provided?

### Soundness
3

### Presentation
3

### Contribution
3
