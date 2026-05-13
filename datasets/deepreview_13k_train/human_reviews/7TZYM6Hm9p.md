# Entropy-based Activation Function Optimization: A Method on Searching Better Activation Functions

- Decision: Accept
- Scores: 5, 6, 8, 5

## Abstract
The success of artificial neural networks (ANNs) hinges greatly on the judicious selection of an activation function, introducing non-linearity into network and enabling them to model sophisticated relationships in data. However, the search of activation functions has largely relied on empirical knowledge in the past, lacking theoretical guidance, which has hindered the identification of more effective activation functions. In this work, we offer a proper solution to such issue. Firstly, we theoretically demonstrate the existence of the worst activation function with boundary conditions (WAFBC) from the perspective of information entropy. Furthermore, inspired by the Taylor expansion form of information entropy functional, we propose the Entropy-based Activation Function Optimization (EAFO) methodology. EAFO methodology presents a novel perspective for designing static activation functions in deep neural networks and the potential of dynamically optimizing activation during iterative training. Utilizing EAFO methodology, we derive a novel activation function from ReLU, known as Correction Regularized ReLU (CRReLU). Experiments conducted with vision transformer and its variants on CIFAR-10, CIFAR-100 and ImageNet-1K datasets demonstrate the superiority of CRReLU over  existing corrections of ReLU. Extensive empirical studies on task of large language model (LLM) fine-tuning, CRReLU exhibits superior performance compared to GELU, suggesting its broader potential for practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors propose a theoretical framework for defining optimality of an activation function (without the optimization considerations). Using Taylor's expansion, the authors extend their framework to search for better activation functions (EAFO - Entropy based Activation Function Optimization) and later also define the worst activation function with boundary conditions. Using the EAFO framework and starting from ReLU, the authors derive a better and novel activation function CRReLU (Correction Regularized ReLU). The authors later demonstrate on three datasets CIFAR10, CIFAR100 and ImageNet-1k where the new found activation function outperforms ReLU on classification performance. Lastly, authors also show improved performance on LLM fine tuning tasks when the CRReLU was swapped out with the ReLU activation function.

### Strengths
1. The paper is written clearly and concisely, and is easy to read. 
2. An information theoretic framework for defining optimality of activation functions for classification tasks is a great approach to search for activation functions and could potentially generate insights. The authors indicate several properties of worst activation functions in i.e. being bounded however this might require more careful analysis but serves as a good stepping stone for future follow up works.

### Weaknesses
1. The premise for EAFO is that extremas in the entropy space after transformation with the activation function correspond to better separability of features in the resulting space but that doesn’t mean better classification performance. Moreover, unlike in discrete space the entropy in the continuous random variables also changes with the scale. However, that might not have any impact on the classification performance. Why do the authors believe this is the right measure to define how good an activation function is? The authors should provide a more rigorous justification for using entropy as a proxy for feature separability and ultimately, classification performance. The connection between minimizing entropy and achieving better generalization is not clearly established, especially considering that entropy is sensitive to scaling and may not directly correlate with the discriminative power of features.
2. Can the authors rank different activation functions based on the EAFO framework? For example, comparison of ReLU and PReLU should point to PReU being better. Since there is already experimental evidence that PReLU is better, if EAFO could confirm it, that would be a great contribution. Similarly please consider ranking 3-4 activation functions to justify the utility of this framework. The authors need to demonstrate the framework's ability to differentiate between known activation functions with varying performance characteristics. A more comprehensive analysis, including a ranking of several common activation functions, would significantly strengthen the claims of the proposed framework.
3. For the experiments, what are the error bars? How many training runs per result? This is important to understand the statistical significance of the results. The lack of error bars and information about the number of training runs makes it difficult to assess the reliability and statistical significance of the reported results. The authors should provide this information to allow for a proper evaluation of their experimental findings.

### Questions
1. My main concern regarding the manuscript is—entropy as an indicator of better classification seems like a very strong statement. One of the key reasons why Sigmoid is not preferred over ReLU is due its optimization properties (vanishing gradients). Since the EAFO framework is completely agnostic to that, the contribution of this framework becomes significantly weaker. If the authors could empirically show how EAFO could be used in practice or justify the choice of entropy as an indicator for activation function optimality, that could help address my concerns
2. Another suggestion is to actually compare the entropy post training of neural networks trained with different activations, not just at the end, but also in the intermediate layers. Since the activation function is being used throughout the network, does lower entropy also help there? If not, should only be the last few layers be equipped with CRReLU?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a theoretical framework to learn a high-performance activation function. It theoretically shows that a worst activation function exist and empirically show that their proposed framework learns significantly improved activation functions compared to SoTA activation function.

### Strengths
The proposed framework to learn activation is shown to perform significantly better than the SoTA activation function theoretically as well as empirically.

While different networks and tasks require different activation functions for the best performance, the proposed framework simplifies this design choice by transferring the activation choice to automated learning during the optimization stage.

### Weaknesses
Although the paper demonstrates substantial empirical improvements, the reported results fall considerably short of state-of-the-art (SoTA) baseline accuracies. For instance, CNNs using ReLU activation commonly achieve test scores above 0.9. Specifically, the reported accuracies on CIFAR-10 and ImageNet-1K are significantly lower than what is typically expected from modern architectures, raising concerns about the overall effectiveness of the proposed activation function in a practical setting. The lack of competitive baseline performance makes it difficult to assess the true potential of the method.

Additionally, there is no direct comparison between SoTA neural network architectures (such as ViT and CNN) using their standard activation functions and those with the proposed activation function. This makes it unclear how much the new activation function improves upon SoTA. The paper should include a comparison where the proposed activation is integrated into a standard, pre-trained model and then fine-tuned on the target task. This would provide a more direct and convincing evaluation of the activation function's capabilities.

In the LLM fine-tuning task, the improvement over GeLU activation is minimal. The reported gains are not substantial enough to justify the complexity of the proposed method, especially given the computational overhead associated with learning a new activation function. This raises questions about the practical utility of the method in large-scale language models.

### Questions
Why is the baseline accuracy on ImageNet and CIFAR-10 so low? State-of-the-art networks typically achieve test scores over 0.9 on CIFAR-10 and above 0.8 on ImageNet-1K.

In LLM fine-tuning tasks, the paper reports marginal improvements over GELU. Could the authors provide further insight into the specific benefits of CRReLU in this context, beyond numerical accuracy improvements?

How would CRReLU perform if evaluated on more diverse NLP tasks or models with larger parameters, and would any tuning adjustments be needed?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper targets the fundamental challenge of activation function design in deep neural networks, which has relied heavily on empirical knowledge rather than a systematic understanding and theoretical foundations. The authors thus propose a new theoretical framework connecting information entropy to activation function performance, which verifies the existence of a worst-case activation function (WAFBC) and thereby develops an entropy-based optimization method (EAFO). The key theoretical contribution of this work is establishing that moving away from WAFBC can consistently improve the model’s performance, leading to a systematic approach for activation function optimization. Built upon this, the authors present Correction Regularized ReLU (CRReLU), demonstrating its great performance across vision transformers and language models. The experiments are comprehensive, covering both image classification (CIFAR-10/100, ImageNet-1K) and language model fine-tuning tasks, with thorough ablation studies and theoretical guarantees.

### Strengths
**(S1) Theoretical Foundation:** This paper establishes a solid mathematical framework connecting information entropy to activation function performance. The derivation begins with principles of information theory and extends through functional analysis to establish clear relationships between data distributions and activation behavior. Specifically, the proof of the Worst Activation Function with Boundary Conditions (WAFBC) existence is clear, utilizing variational calculus and the Euler-Lagrange equation to demonstrate global maximality. As such, it not only provides insights into why certain activation functions perform better than others but also explains long-observed empirical phenomena, such as the superior performance of unbounded activation functions (like ReLU) compared to bounded ones (such as sigmoid and tanh), which offers both theoretical guarantees and practical optimization guidance.

**(S2) Technical Originality and Soundness:** The proposed EAFO method represents a significant advancement in activation function design. Unlike previous ones that largely relied on empirical knowledge, EAFO provides a principled and systematic framework. The derivation of correction terms through analysis of the information entropy functional's Taylor expansion is insightful, enabling both static design and potential dynamic optimization. The introduction of learnable parameters in CRReLU demonstrates a thoughtful balance between theoretical purity and practical adaptability. Moreover, its potential extension to dynamic optimization during training seems to open new research directions, while maintaining backward compatibility with existing architectures and optimization techniques. 

**(S3) Thorough Experiments:** Experiments in this work are comprehensive and well-designed, covering multiple network architectures and task domains. Extensive ablation studies and sensitivity analyses are also conducted to show the methods’ effectiveness. Concretely, the evaluation across vision transformers (ViT, DeiT, TNT) and LLMs (GPT-2) shows broad applicability, while the performance improvements on classical computer vision benchmarks (like CIFAR-10/100 and ImageNet-1K) provide strong practical validation. The large-scale experiments on language model fine-tuning using Direct Preference Optimization (DPO) provide valuable insights into the method's scalability and generalization capabilities. Moreover, the computational efficiency analysis is particularly useful, showing minimal overhead despite the addition of learnable parameters. 

**(S4) Presentation Clarity:** 
This manuscript exhibits great clarity in presenting mathematical concepts and empirical results. The progression from theoretical foundations through practical implementation is logical and well-structured, making the work accessible to a broader audience while maintaining technical insights. The mathematical derivations are with appropriate detail and clear step-by-step explanations, facilitating reproducibility and future extensions. In addition, the thorough implementation details, including pseudo-code and network architecture considerations, ensure the practical applicability of this work.

### Weaknesses
 **(W1) Theoretical Limitations:** The authors make the assumption of Gaussian distribution for the input data distributions in this paper. While it is mathematically convenient, it requires more rigorous justification. While the authors cite the Central Limit Theorem and previous works supporting this assumption in deep neural networks, modern architectures like transformers with complex operators like self-attention mechanisms may exhibit significantly different distribution patterns. This work would benefit from a more detailed analysis of how distribution deviations affect the theoretical guarantees. Specifically, the theoretical framework relies on the assumption that the input data to the activation functions follows a Gaussian distribution, which simplifies the mathematical analysis but may not accurately reflect the complex, non-linear transformations that occur in deep networks, particularly in deeper layers or with transformer architectures. The impact of deviations from this assumption on the derived worst-case activation function and the subsequent optimization method needs further investigation. In addition, the convergence properties during the training process, particularly the interaction between the learnable parameter and standard network weights, lack thorough theoretical treatment. The paper does not provide a rigorous analysis of how the learnable parameter ε affects the convergence rate or stability of the training process, especially when combined with standard optimization techniques like stochastic gradient descent. A more detailed analysis of the gradient flow and the potential for oscillations or divergence due to the introduction of this parameter is needed.

**(W2) Experimental Concerns:** The experimental results, while generally strong, reveal several areas requiring deeper investigation. The performance compared to GELU in DeiT experiments raises important questions about the interaction between CRReLU and knowledge distillation processes. It deserves a more thorough analysis, potentially exploring alternative distillation strategies that are more compatible with the CRReLU's properties. Besides, the initialization strategy for the learnable parameter appears somewhat arbitrary (set to 0.01). The choice of 0.01 as the initial value for the learnable parameter ε lacks a clear justification, and the paper does not explore the sensitivity of the results to different initializations. A more systematic approach to selecting this initial value, potentially based on theoretical considerations or empirical analysis, is needed. Moreover, the absence of experiments on classical CNN architectures leaves a significant gap in demonstrating the method's generality, particularly given the widespread use of CNN-based network architectures. The evaluation is primarily focused on vision transformers and language models, while neglecting classical CNN architectures, which are still widely used in various applications. This limits the generalizability of the findings and raises questions about the method's effectiveness in different architectural contexts.

**(W3) Dynamic Optimization Challenges:** This work employs dynamic optimization during training, which potentially faces several practical challenges. For example, the computational complexity analysis of dynamic optimization is insufficient, particularly for large-scale networks where activation function optimization could introduce substantial overhead. The interaction between dynamic activation optimization and common training techniques (batch normalization, residual connections, dropout) also requires more detailed analysis. I recommend the authors conduct more experimental validation and analysis to address these issues. The paper's discussion of dynamic optimization is limited, and it does not provide a detailed analysis of the computational overhead associated with updating the activation function parameters during training. The interaction between dynamic activation optimization and other common training techniques such as batch normalization, residual connections, and dropout is not thoroughly investigated, which could affect the overall performance and stability of the training process.

**(W4) Implementation and Scalability Considerations:** The practical implementation of EAFO and CRReLU requires more detailed treatment, particularly regarding numerical stability and computational efficiency at scale. Discussion of potential gradient flow issues when the learnable parameter ε takes extreme values, and the mitigation strategies are all not provided. Additionally, the paper would benefit from analysis of how the method performs under resource-constrained conditions, such as mobile devices or edge computing scenarios. All these could provide more insights to the researchers and practitioners in the community, and thus propel further research. The paper lacks a detailed discussion of the numerical stability of the proposed method, particularly when the learnable parameter ε takes extreme values. The potential for gradient explosion or vanishing due to large or small values of ε is not addressed, and the paper does not provide any mitigation strategies for these issues. Furthermore, the analysis of the method's performance under resource-constrained conditions, such as mobile devices or edge computing scenarios, is missing, which is crucial for practical deployment.

### Questions
**(Q1) Dynamic Optimization Implementation:** While the authors suggest the potential for dynamic optimization of activation functions during training, the practical implementation remains relatively unclear. Could the authors elaborate on:

- Concrete strategies for making dynamic optimization computationally tractable in large networks?
- Specific approaches to balance the frequency of activation function updates with computational overhead?
- Empirical evidence or theoretical bounds on the expected performance gains from dynamic optimization? Understanding these aspects would help assess the practical value of the dynamic optimization extension.

**(Q2) Initialization and Training Stability:** The choice of ε=0.01 as initialization appears somewhat arbitrary. Could the authors provide:

- Analysis of how different initialization values affect training dynamics and final performance?
- Guidelines for selecting optimal ε values based on network architecture or task requirements?
- Can we investigate potential instabilities or failure cases under different initialization schemes? This information would be crucial for practitioners implementing CRReLU in their own networks.

---
**Additional Comment:**

I hope my review helps to further strengthen this paper and helps the authors, fellow reviewers, and Area Chairs understand the basis of my recommendation. I also look forward to the rebuttal feedback and further discussions, and would be glad to raise my rating if thoughtful responses and improvements are provided.


---
## **-------------------- Post-Rebuttal Summary --------------------**

The additional experiments, discussions, and revised manuscript provided by the authors have significantly strengthened the work and addressed most of my concerns. I suppose this work can provide knowledge advancement to the field, and I look forward to the final revised manuscript, incorporating the additional information presented in the rebuttal stage.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a systematic approach to address the problem of activation function optimization in artificial neural networks (ANNs). By leveraging information entropy theory, the authors theoretically demonstrate the existence of the worst activation function under boundary conditions (WAFBC). They then propose the Entropy-based Activation Function Optimization (EAFO) methodology, which provides a framework for designing better activation functions. Utilizing this methodology, the authors derive a novel activation function called Correction Regularized ReLU (CRReLU) from the conventional ReLU. Extensive experiments on vision transformer variants and large language model (LLM) fine-tuning tasks demonstrate the superior performance of CRReLU over existing ReLU variants.

### Strengths
1. Theoretical Rigor: 
The paper provides a solid theoretical foundation for activation function optimization by introducing the concept of WAFBC and the EAFO methodology. This approach is novel and offers a fresh perspective on designing activation functions.
2. Practical Application: 
The derived CRReLU activation function shows significant improvements in performance across various tasks, including image classification and LLM fine-tuning, demonstrating the practical applicability of the proposed methodology.
3. Comprehensive Experiments: 
The authors conduct extensive experiments on multiple datasets and architectures, validating the effectiveness of CRReLU and providing a thorough evaluation of the proposed method.

### Weaknesses
 1. Limited Generalizability: 
The paper primarily focuses on ReLU and its variants. It would be valuable to explore the applicability of the theoretical framework to activation functions without an inverse function, such as Swish or Mish. The current methodology relies on the existence of an inverse function to calculate the differential entropy, which is a significant limitation. The authors should acknowledge that the proposed EAFO framework, in its current form, cannot be directly applied to activation functions lacking this property, and discuss potential alternative formulations or extensions that could address this limitation.
 2. Computational Complexity: 
The dynamic optimization during iterative training introduces significant computational complexity, which the paper does not address. The authors should discuss potential approaches or algorithms, such as gradient-based optimization or stochastic methods, that might mitigate these computational complexity issues, or provide a more detailed analysis of the trade-offs between performance gains and computational costs. The paper needs to provide a more thorough analysis of the computational overhead associated with the dynamic optimization of the activation function during training. Specifically, the authors should quantify the increase in training time and memory consumption compared to using a static activation function. Furthermore, they should explore and discuss techniques to reduce this computational burden, such as performing the optimization at a lower frequency than the weight updates or using more efficient optimization algorithms.
 3. Assumption of Gaussian Distribution: 
The assumption that data follows a Gaussian distribution simplifies the derivation of CRReLU but may not hold in all real-world scenarios. The authors should provide empirical evidence or theoretical analysis of CRReLU's performance under non-Gaussian data distributions, such as heavy-tailed or multimodal distributions, to address concerns about the robustness of the method. The paper needs to provide a more rigorous justification for the Gaussian assumption. While it might be a reasonable approximation in some cases, it is crucial to acknowledge that real-world data often deviates from this assumption. The authors should investigate the sensitivity of the proposed method to violations of this assumption and explore alternative theoretical frameworks that do not rely on this assumption, or at least provide empirical evidence of robustness under non-Gaussian conditions.
 4. Lack of Diverse Experiments: 
While the experiments are comprehensive, they are limited to specific datasets and architectures. Additional experiments on diverse datasets, such as medical imaging (e.g., MICCAI) or remote sensing data (e.g., EuroSAT), and architectures like convolutional neural networks (e.g., ResNet) or graph neural networks, would strengthen the generalizability claims. The paper should include experiments on a broader range of tasks and architectures to demonstrate the robustness and generalizability of the proposed CRReLU activation function. Specifically, the authors should evaluate its performance on tasks such as object detection, semantic segmentation, and graph-based learning, and on architectures such as ResNets, VGG, and graph neural networks. This would provide a more comprehensive assessment of the method's applicability.

### Questions
1. How does the EAFO methodology perform when applied to other activation functions, especially those without an inverse function, such as Swish or Mish?
2. Can the authors provide empirical evidence or theoretical analysis of CRReLU's performance under non-Gaussian data distributions, such as heavy-tailed or multimodal distributions, to address concerns about the robustness of the method?
3. What potential approaches or algorithms, such as gradient-based optimization or stochastic methods, can be explored to mitigate the computational complexity introduced by dynamic optimization during iterative training?
4. Would the authors consider conducting additional experiments on diverse datasets, such as medical imaging (e.g., MICCAI) or remote sensing data (e.g., EuroSAT), and architectures like convolutional neural networks (e.g., ResNet) or graph neural networks, to further validate the generalizability of CRReLU?

### Soundness
3

### Presentation
3

### Contribution
3
