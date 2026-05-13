# Hessian-Aware Training for Enhancing Model Resilience for In-Memory Computing

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Deep neural networks are not resilient to bitwise errors in their parameters: even a single-bit error in their memory representation can lead to significant performance degradation. This susceptibility poses great challenges in deploying models on emerging computing platforms, such as in-memory computing devices, where frequent bitwise errors occur. Most prior work addresses this issue with hardware or system-level approaches, such as additional hardware components for checking a model’s integrity at runtime. However, these methods have not been widely deployed since they necessitate substantial infrastructure-wide modifications. In this paper, we study a new approach to address this challenge: we present a novel training method aimed at enhancing a model’s inherent resilience to parameter errors. We define a model-sensitivity metric to measure this resilience and propose a training algorithm with an objective of minimizing the sensitivity. Models trained with our method demonstrate increased resilience to bitwise errors in parameters, particularly with a 50% reduction in the number of bits in the model parameter space whose flipping leads to a 90–100% accuracy drop. Our method also aids in extreme model compression, such as lower bit-width quantization or pruning ∼70% of parameters, with reduced performance loss. Moreover, our method is compatible with existing strategies to mitigate this susceptibility.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a training algorithm that enhances the resilience of PIM to bitwise errors in model parameters. This method uses a second-order Hessian-based approach, minimizing the sharpness of the loss landscape to improve error. The proposed method demonstrates improved resilience to single-bit errors, aids in efficient model compression (e.g., quantization and pruning), and complements existing defensive techniques.

### Strengths
Strength:
1.	The proposed training method make the NN parameter space smooth and make it robust to various perturbations, e.g., bitwise flip error, quantization and pruning, etc.

### Weaknesses
Weaknesses:

1.	The novelty of proposed method is limited. How does it differentiate with prior work in robustness-aware optimization and hardware/software co-design methods for ReRAM PIM?, e.g., HERO: Hessian-Enhanced Robust Optimization for Unifying and Improving Generalization and Quantization Performance.

2.	Since the author mentioned hardware defense, the proposed method slightly reduce the number of sensitive weights, which can hardly defend malicious bit-flip attacks which always attacks the rest vulnerable bits.

3.	Hutchinson's method to approximate Hessian trace is also widely used, and it is not a novel method. This sampling is actually more costly than the paper I cited.

4.	It is not convincing why IMC noise robustness issue contains random bitflip, which is not physically validated.

### Questions
1.	The novelty of proposed method is limited. How does it differentiate with prior work in robustness-aware optimization and hardware/software co-design methods for ReRAM PIM?, e.g., HERO: Hessian-Enhanced Robust Optimization for Unifying and Improving Generalization and Quantization Performance.

2.	Since the author mentioned hardware defense, the proposed method slightly reduce the number of sensitive weights, which can hardly defend malicious bit-flip attacks which always attacks the rest vulnerable bits.

3.     What are the major machine learning contributions? Using hessian trace as a penalty to improve robustness and smoothness is extensively studied in the AI/ML community.

### Soundness
3

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
4

### Summary
This paper proposes using Hessian trace to enhance the model's resilience to a bit-flipping error by changing the loss landscape and avoiding model going into sharp local optima.

### Strengths
Strength:
* Complete experiments results from accurcay to loss landscape visualization

### Weaknesses
Weakness:
* The results part is vague without the mention of model accuracy under bit-wise error. For example, I am quite confused about Table 3, where the baseline even has a better accuracy. I am wondering whether the authors should report accuracy under attack and also show the trend of accuracy change with increasing error ratio. It is unclear how the proposed method improves resilience to bit-flips if the baseline accuracy is higher, and the paper lacks a clear demonstration of the model's performance when subjected to bit-flip attacks.
* The error generation is not a fixed policy for all models. The authors use bitwise errors for the easy task, MINIST, while only flipping the MSB for IMAGNET. I don't think it is a fair setting for experiments. The choice of error injection strategy seems arbitrary, and the paper does not provide a strong justification for using different methods across different datasets and models. This makes it difficult to compare the results and draw meaningful conclusions about the generalizability of the proposed method.
* Moreover, using Hessian to avoid the model going into sharp loss and increase the model's resilience to bit-error is not a new idea, which is already widely explored in quantization, weakening the novelty of this paper. The paper does not adequately address the existing literature on using Hessian information for improving model robustness, particularly in the context of quantization, where similar techniques have been explored.

### Questions
Please see weakness.

### Soundness
2

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
4

### Summary
This paper presents a method called Hessian-Aware Training to improve the resilience of deep neural networks (DNNs) against bitwise errors in model parameters, an issue that affects DNNs deployed on error-prone, emerging computing hardware. The approach minimizes the sensitivity of models to these errors by leveraging the Hessian trace to guide training. This method is shown to reduce the proportion of sensitive parameters (those likely to cause a large accuracy drop if altered), with results indicating up to a 50% decrease in the number of high-impact bitwise errors. The paper further demonstrates how Hessian-Aware Training can support compression techniques, such as quantization and pruning, with minimal accuracy loss.

### Strengths
1- The proposed approach provides a novel and effective method for improving the robustness of DNNs to bitwise errors in parameters by leveraging the Hessian trace as an optimization objective during training. This strategy is unique compared to more typical hardware or system-level solutions and represents a substantial step toward integrating resilience at the model level.

2- Extensive experimental evaluation across multiple models and datasets, including MNIST, CIFAR-10, and ImageNet, illustrates the practical effectiveness of the Hessian-Aware Training method. The results strongly demonstrate improved resilience to bitwise errors and show the approach’s versatility in enhancing compression techniques, such as quantization and pruning, with minimal accuracy loss.

3- The technique has potential applications beyond model robustness, as it could complement existing hardware- and software-based resilience mechanisms. The paper discusses several examples, which underscores the broader implications of Hessian-Aware Training and suggests valuable synergies for real-world DNN deployments.

### Weaknesses
- The method’s reliance on the Hessian trace may limit scalability in very large models, where the computational costs of Hessian approximation could present a challenge. Although the paper addresses this with a truncated approach (focusing on top-p eigenvalues), the limitations around computational complexity remain a practical consideration. Specifically, the paper does not provide a clear analysis of how the computational cost scales with model size and the number of parameters, making it difficult to assess the practical applicability of the method for models with millions or billions of parameters. The choice of 'p' for the top-p eigenvalues is also not well justified, and its impact on the effectiveness of the method needs further investigation. It is unclear how the selection of 'p' affects the trade-off between computational cost and resilience. 
- The results on fully connected layers appear more promising than those for convolutional layers in architectures like ResNet, where residual connections may already provide a certain level of resilience. The paper does not delve into why the method is less effective for convolutional layers, and it is crucial to understand the underlying reasons for this discrepancy. It is possible that the Hessian trace is not a good indicator of sensitivity for convolutional layers, or that the method needs to be adapted to account for the specific characteristics of these layers. Furthermore, the paper does not explore the impact of different convolutional layer configurations (e.g., kernel size, stride, padding) on the effectiveness of the proposed method. Expanding the method’s effectiveness across different model architectures and layer types could further increase the approach’s practical impact.
- The use of an additional regularization term in training (Hessian trace) could introduce additional tuning complexity, especially in larger models. Practical guidelines on hyperparameter selection for varying model scales could be helpful for potential adopters to maximize the resilience benefits without extensive hyperparameter optimization. The paper lacks a systematic study on the sensitivity of the method to the regularization coefficient. It is unclear how the optimal value of this hyperparameter varies with model architecture, dataset, and training regime. Without clear guidelines, users may struggle to find the right hyperparameter settings, which could limit the practical applicability of the method.

### Questions
- Could the authors expand on potential strategies to make the method more computationally efficient, especially when dealing with very large-scale models?
- Given that convolutional layers with residual connections showed limited benefit, could the authors discuss ways to adapt the approach for models with a large proportion of residual or skip connections?
- In applications with severe hardware constraints, does the method provide enough benefit to justify the added training cost, or would alternative resilience strategies (e.g., quantization alone) be preferable?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a technique to improve resilience to bitwise errors. It consists of using the trace of the Hessian as a proxy for error sensitivity and, consequently, as an additional regularization term during model training. This methods results in models exhibiting flatter loss landscape as well as lower accuracy degradations when subject to adversarial bitwise flipping. Impact on pruning and quantization is also investigated. Results are reported on image classification tasks on a few models (BaseNet, LeNet, ResNet18, ResNet50) and datasets (MNIST, CIFAR-10, ImageNet).

### Strengths
- the paper is well structured and easy to follow

### Weaknesses
 - the presentation of this paper is extremely misleading: it is introduced as a work on noise-resilience targeted at In-Memory Computing (IMC), but the methodology it employs for validation (adapted from [1]) applies specifically to adversarial attacks. The same adversarial attacks would have catastrophic impact on model performance irrespective of the hardware, IMC or not, when flipping a single exponent bit may change a value by several order of magnitude (depending on the precision being used). In fact, the original paper [1] deals with *non-IMC* models, on standard digital hardware. Noise characteristics typical of IMC hardware (e.g., Analog IMC) do not follow at all the patterns of adversarial attacks. While it is certainly the case that IMC may introduce additional sources of noise, the "frequent bitwise error" mentioned in the abstract is not uniformly distributed across bits. In this manuscript, the authors evaluate performance drop due to bitwise errors following 3 methodologies:
1. across all possible individual bits flipping for MNIST (giving equal weight to each configuration)
2. across only the exponent bits (thus the most impactful) for CIFAR-10 
3. only changing the most significant exponent bit for ImageNet

None of these methods is a fair representation of noise in IMC hardware. They may be however suitable to analyze the impact of targeted adversarial attacks, as [1] does. My view is further supported by the fact that beyond title, abstract, and introduction, there is no mention of IMC-related experiments across the manuscript
- viewed as a manuscript about model safety / security instead of noise resilience for IMC, as hinted in two paragraphs in Section 6, the scope and potential impact become significantly more limited
- Fig. 1 and 2 show distributions plots of number of bits that cause a certain level of Relative Accuracy Drop (RAD). I would have expected to observe a shift in distribution but the integral below the updated curve (yellow) is significantly lower that the reference (blue). Does this mean fewer flip combinations were tested? Or does this mean instead that a significant percentage of bit flips caused negative RAD (i.e., improve performance) upon application of this method, and are therefore not included in this plot? This would be rather surprising
- the impact of training with Hessian-based regularization on pruning resilience is arguably the clearer demonstration of a potential advantage of this technique. However, the experimentation is limited to a single model/task combination, making it impossible to determine whether this outcome is generalizable
- quantization results are not impressive, with similar performance with vs. without Hessian regularization down to 4 bits. I would also argue that 4-bit weight-only quantization of such small models is a solved and currently irrelevant problem. Today, LLM with billions of parameters can quantized to 4 bits weights with minimal accuracy degradation. The 2-bit quantization results show some improvement, but the degradation observed is still massive, the models remain practically unusable

### Questions
- I would recommend the authors to either re-frame the paper as a technique to mitigate adversarial attack, or present experiments that relate to IMC noise

### Soundness
2

### Presentation
3

### Contribution
2
