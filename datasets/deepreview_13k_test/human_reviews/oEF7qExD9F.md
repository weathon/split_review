# LMUFormer: Low Complexity Yet Powerful Spiking Model With Legendre Memory Units

- Decision: Accept
- Scores: 3, 8, 6, 6

## Abstract
Transformer models have demonstrated high accuracy in numerous applications but have high complexity and lack sequential processing capability making them ill-suited for many streaming applications at the edge where devices are heavily resource-constrained. Thus motivated, many researchers have proposed reformulating the transformer models as RNN modules which modify the self-attention computation with explicit states. However, these approaches often incur significant performance degradation.
The ultimate goal is to develop a model that has the following properties: parallel training, streaming and low-cost inference, and state-of-the-art (SOTA) performance. In this paper, we propose a new direction to achieve this goal. We show how architectural modifications to a fully-sequential recurrent model can help push its performance toward Transformer models while retaining its sequential processing capability. Specifically, inspired by the recent success of Legendre Memory Units (LMU) in sequence learning tasks, we propose LMUFormer, which augments the LMU with convolutional patch embedding and convolutional channel mixer. 
Moreover, we present a spiking version of this architecture, which introduces the benefit of states within the patch embedding and channel mixer modules while simultaneously reducing the computing complexity. 
We evaluated our architectures on multiple sequence datasets. Of particular note is our performance on the Speech Commands V2 dataset (35 classes). In comparison to SOTA transformer-based models within the ANN domain, our LMUFormer demonstrates comparable performance while necessitating a remarkable \rev{$53\times$} reduction in parameters and a substantial \rev{$65\times$} decrement in FLOPs. Furthermore, when benchmarked against extant low-complexity SNN variants, our model establishes a new SOTA with an accuracy of 96.12\%. 
Additionally, owing to our model's proficiency in real-time data processing, we are able to achieve a 32.03\% reduction in sequence length, all while incurring an inconsequential decline in performance.git}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a sequential network that exploits Legendre Memory Units (LMU) module as its temporal computational core. It has been shown that the proposed network, which is called LMUFormer, can achieve a similar performance to transformers with less number of parameters and operations.

### Strengths
1) The accuracy performance of the proposed work is decent and the memory/operation reduction is significant.

2) The paper is also well-written and easy to read and understand.

### Weaknesses
1) The contribution of this work is rather limited as it relies on a previously proposed module (i.e., LMU). It is not also clear why the proposed network yields a better accuracy.

2) My main concern is the performance of such a network when pre-trained. The main advantage of transformers come from its pre-training stage which allows the model to perform well on downstream tasks during fine-tuning. To learn and store those pre-training data, transformers contains numerous parameters. As such, I am not supersized by the results reported in this paper since the transformer used for the comparison was not pre-trained and consequently it is expected to see a better performance from LMUFormer. What would be the performance of LMUFormer on well-known benchmarks such as GLUE? Can LMUFormer be pre-trained?

3) Lack of theoretical analysis and reasoning on the superior performance of LMUFormer.

### Questions
See my concerns listed as weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work combines Legendre Memory Units (LMU)  with convolutional patch embedding and convolutional channel mixer in its network design to improve accuracy. It also introduces a spiking version to further improve its inference efficiency. On speech recognition tasks, their results show a significant reduction in both model size and FLOPs compared to the SoTA AST model. It also achieves higher accuracy compared to other low-complexity SNN designs. It also shows it can achieve competitive accuracy with only two-thirds of the seq length due to its sequential processing capability.

### Strengths
- The addition of the convolutional patch embedding (w/ 1d conv) and convolutional channel mixer to LMU is well explained and justified.
- The model can be trained in parallel and has the streaming capability during inference. It does not need to wait until the entire input sequence is available, which can reduce the compute complexity and memory requirement.
-  This transformer design achieves competitive accuracy on a wide range of tasks compared to its counterparts with low compute complexity. It also demonstrates better classification accuracy in long token tasks compared to other linear-complexity attention designs.

### Weaknesses
- The results could be made stronger if the model size and compute complexity comparison can be added to every performance comparison table (Table 1,2,4).
- Ops represented in the paper for SNN can be a very optimistic proxy for latency performance. It is worth mentioning that SNNs might not be easily accelerated on off-the-shelf hardware like CPUs and GPUs. It might require specialized hardware to demstronate its advantage in latency and energy reduction.

### Questions
1. Is there a reason why Am(t) is changed to Am[t-1] from eqn(1) to eqn(2) for discretization?
2. From eqn (4), it seems the LMU module is composed of mainly matrix-vector operations, which is similar to RNN. Is it correct that we can also parallelize it across the time dimension? can you elaborate on how it can be solved in non iterative way to enable parallelized training? 
3. I'm curious to know how its measured training and inference time compares to that of other linear-time transformers like Linformer on the off-the-shelf hardware.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a LMU based model that also has a spiking variant. The goal is to explore the accuracy gap between transformer based model with LMU based model with more complex sub-modules.

### Strengths
* This paper is mostly easy to follow and well organized.
* Related background and works are discussed and introduced extensively.
* The intention of exploring this performance gap in function complexity feels intuitive and interesting.
* Experimental are conducted extensively amongst different models and tasks and comparing both accuracy and computational cost, results also look mostly promising.

### Weaknesses
* In task 2, there is still some accuracy gap between the proposed method and some transformer based methods. Is there any way to compare pLMU on the same task as well as resource usage? It feels the narrative is that accuracy wise on relative complex tasks LMUformer is on par with transformer based method while out-performing pLMU. Besides rMNIST task, it is difficult to tell how much performance gain that the proposed method would offer while (potentially) introducing extra hardware cost.

### Questions
* Does the proposed method suit SNN better and more nature? What about the training cost and time?

### Soundness
2 fair

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
Transformer models are highly accurate but complex and not suited for sequential processing, making them ill-suited for edge devices. RNNs are more suitable for these devices due to their lower complexity and sequential processing capabilities, but they often lag in performance compared to Transformer models. The paper proposes LMUFormer, a model that augments Legendre Memory Units (LMU) with convolutional patch embedding and convolutional channel mixers. This results in a fully-sequential recurrent model that approaches the performance of Transformer models while retaining the ability to process data sequentially.  A spiking version of LMUFormer is also introduced, which brings the benefits of states within the patch embedding and channel mixer modules, further reducing computing complexity.
The contribution lies in 
1. New Model Architecture: Introduction of LMUFormer, a novel architecture that combines LMUs with convolutional patch embedding and channel mixers, aiming to provide a balance between high performance and low complexity.

2. Performance: LMUFormer demonstrates impressive performance, particularly on the Speech Commands V2 dataset, showing comparable results to state-of-the-art transformer-based models but with significantly fewer parameters and lower computational complexity.

3. Spiking Version: Presentation of a spiking version of LMUFormer, establishing a new state-of-the-art in low-complexity Spiking Neural Network (SNN) variants with an accuracy of 96.12%, and demonstrating the ability to process real-time data efficiently.

4. Efficiency in Real-Time Processing: The model shows proficiency in real-time data processing, achieving a 32.03% reduction in sequence length with minimal performance decline, highlighting its suitability for streaming applications at the edge.

### Strengths
**Originality:**
- Innovative Model Design: The LMUFormer introduces a unique combination of Legendre Memory Units (LMU) with convolutional patch embedding and channel mixers, creating a novel architecture that stands out in the realm of spiking models and RNNs.
- Spiking Model Integration: The integration of a spiking version of the LMUFormer adds a layer of originality, as it brings the benefits of states within the patch embedding and channel mixer modules, while also aiming to reduce computing complexity.

**Quality:**
- Robust Performance: The LMUFormer demonstrates robust performance, especially highlighted by its results on the Speech Commands V2 dataset, where it shows comparable performance to state-of-the-art transformer-based models but with a significant reduction in parameters and computational complexity.
- Comprehensive Evaluation: The paper includes a thorough evaluation of the architectures on multiple sequence datasets, providing a solid basis for the claims made about the model’s performance and efficiency.

**Clarity:**
- Well-Structured: The paper is well-structured, with clear sections that logically flow from one to the next, making it easy for readers to follow the development of ideas and understand the proposed model.
- Detailed Explanations: The authors provide detailed explanations of the LMUFormer architecture, the spiking version of the model, and the motivations behind their design choices, contributing to the overall clarity of the paper.

**Significance:**
- Addressing Resource Constraints: The LMUFormer addresses a significant challenge in the field of edge computing and streaming applications, where devices are heavily resource-constrained. By providing a model that combines high performance with low complexity and sequential processing capabilities, the paper makes a meaningful contribution to this area.

### Weaknesses
**Addressing Potential Biases:**
Model Limitations: The paper could be improved by providing a more balanced view, including a discussion of potential limitations or scenarios where the LMUFormer might not perform as well. This would help readers develop a more nuanced understanding of the model’s applicability.

**Enhancing Reproducibility:**
Implementation Details: Providing more implementation details, including hyperparameters and training procedures, would enhance the reproducibility of the results, contributing to the paper’s overall quality.

**Real-Time Processing Analysis:** 
Given the focus on streaming applications and real-time data processing, a more detailed analysis of the model’s performance in real-time scenarios, including potential latency issues and how they are addressed, would be valuable.

**Software-Hardware codesign**
It would be nice to see a hardware simulation for SNN to learn all aspect of the new model, engergy, latency, throughput and any overhead, etc.

### Questions
- citation for S4 models?

- Could you add "how to get 32.03%" in section 5.5? I assume it is (128-87)/128? similarly to 70x and 140x to help reading

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
