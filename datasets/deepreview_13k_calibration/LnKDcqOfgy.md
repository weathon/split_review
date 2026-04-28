# Rate/Distortion Constrained Model Quantization for Efficient Storage and Inference

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
The proliferation of large pre-trained neural networks has recently revived research in both quantization of network weights (for faster inference), and in their
compression (to reduce file sizes). However, there has so far been little idea transfer between the two lines of research. In this paper, we combine techniques from
quantization and compression to propose an efficient and highly effective post-training compression method for large neural networks. Our method extends the
recently published quantization method OPTQ (Frantar et al., 2023) with a tunable
rate/distortion trade-off by introducing a cost per bit into OPTQ's rounding
operation. Crucially, we estimate the bit rate based on the predictive model used
in the state-of-the-art neural network compression method NNCodec (Becking
et al., 2023). In our experiments with several standard pre-trained networks from
the computer vision community, our method leads to significantly (up to 2.7x)
smaller file sizes than NNCodec at equal model performance, generally compressing to less than half a bit per network weight and implicitly pruning insignificant weights.
Additionally, and in contrast to NNcodec, our method offers the same opportunities for inference speed-ups as OPTQ. By proving that file size and inference
cost can be reduced simultaneously, we hope that our contribution shows a path
towards deploying large neural networks on end-user devices, alleviating privacy
concerns, regulatory constraints, and dependency on large service providers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a post-training compression technique that combines recent advancements in quantization and compression. It extends the OPTQ framework by incorporating a rate-distortion trade-off, achieved through the addition of a bit-cost function inspired by NNCodec’s entropy model. The resulting OPTQ-RD method effectively balances compression strength and inference speed, achieving high compression ratios with minimal performance degradation across various CNNs.

### Strengths
The method can be applied without modifying network architectures, broadening its utility for different models.

The method’s ability to operate in a post-training setting with minimal calibration data makes it practical for real-world deployment.

The evaluation demonstrates that the proposed method consistently outperforms the baselines in terms of weight compression while preserving accuracy on par with them.

### Weaknesses
## Claims:

The paper does not reference previous methods that address the same problem [1,2].

The authors claim that OPTQ-RD achieves fast inference time; however, as I understand, only the weights are quantized, while activations remain in the floating point, typically resulting in a minimal reduction in inference time. This approach may reduce memory usage or storage, particularly in the context of compression and quantization for large language models (LLMs). However, it has a limited impact on convolutional neural networks (CNNs), especially those used in the experiments.


## Experiments:

The experimental setting is quite limited. VGG, which is not commonly used in practice, is known to have sparse weights, making it difficult to generalize the findings to more widely adopted network architectures.


Although bits per weight appears promising, Figure 1 and Table 1 provide little insight into its relevance to practical metrics, such as latency or energy consumption. Additionally, the plots suggest that, in intermediate cases, there is only a narrow range where the proposed method outperforms the vanilla baseline of OPTQ+DeepCABAC.


## Writing

The authors begin the abstract with a statement on pre-trained large models and discuss recent work on LLM quantization, yet these topics appear unrelated to the core of this study. Conducting evaluations only on CNNs without addressing LLMs or even ViTs is entirely valid; however, if they are not central to the paper, it raises the question of why these topics are mentioned at all.

### Questions
How does the choice of entropy model impact compression outcomes, and could other entropy models be seamlessly integrated into the method?

How does the method handle outliers in model weights, especially in architectures with significant variations in weight distributions? While this may seem out of scope, it could provide insight into the method's effectiveness in quantizing activations.

If the method is compatible with various quantization schemes, could you evaluate the impact of different schemes on large language models (LLMs)? A model with 1 billion parameters should be sufficient for this validation.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents OPTQ-RD, an extension of the OPTQ quantization method that introduces a rate-distortion trade-off. By adapting the quantization step to account for bit rate using an entropy model, the proposed framework compresses neural networks and maintains model accuracy. The method is experimentally evaluated on several computer vision models such as ResNets and VGG16 on CIFAR10 and ImageNet datasets.

### Strengths
1) The paper proposes a combination of quantization and compression methods, which is bridging the gap between optimizing for storage and inference. The integration of an entropy model (DeepCABAC) into the quantization process distinguishes the proposal from the other SOTA methods.
2) The proposal is evalauted on computer vision datasets to demonstrate its effectiveness.
3) The paper is well written and structured.

### Weaknesses
1) The generalizabity of the proposal on other model architectues and datasets is not evaluated explored. Addressing this issue running some extra experiments would strengthen the paper. Specifically, the paper focuses on VGG16 and ResNet architectures, which are relatively well-established. It would be beneficial to see how the method performs on more modern architectures, such as Transformers or MobileNets, which have different characteristics in terms of parameter distribution and sensitivity to quantization. Furthermore, the datasets used are limited to CIFAR10 and ImageNet, and it is unclear how the method would perform on datasets with different characteristics, such as those with higher resolution images or different types of data (e.g., text or audio).
2) Table 1 presents the comparison with other compression techniques, however there is no comparison with the works reported in the related work section (e.g., those using quantization, pruning, and knowledge distillation). This could provide a more comprehensive performance context and help the reader understand better the benefits of the proposal. The current comparison is limited to a few compression techniques, and it does not provide a clear picture of how the proposed method compares to other state-of-the-art methods in the broader field of model compression. For example, it would be important to compare against methods that combine quantization with pruning or knowledge distillation, as these are common techniques used in practice.
3) It would be beneficial to mention what is the novelty of the proposal. The way it is written currently, it is seems that the proposal is incremental in terms of novelty as it is a combination of various existing techniques. The paper does not clearly articulate the unique contribution of the proposed method, and it is not clear how it differs from existing methods. The paper should clearly state the novelty of the proposed method and highlight the key differences from existing approaches.

### Questions
1) How does the proposed method work for other architectures apart from VGG16 on ImageNet and the ResNets on CIFAR10? 
2) What are the trade-offs in selecting the size of the calibration sets, and how does this affects models with significantly more parameters than the ones tested?
3) How does this method compares agaainst other SOTA works? Currently,  the proposal is compared with very limited SOTA works (Table 1)
4) Could you please mention the novelty of the proposal (please see the weaknesses above)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This submission proposed to combine neural network quantization (after training, Post-Training Quantization (PTQ)) and parameters compression (compression) for storage in an end-to-end procedure. The quantized parameters are guided to compression-friendly distribution. Specially, after network is trained, it used OPTQ for parameter quantization. The OPTQ used is reformulated to combine DeepCABAC (a compression method) by Lagrange, leading to a quantization results considering compression requirement. The Lagrange factor trading off quantization and compression is layer-wise by considering the Hessian in each layer.

Experiments in Computer Vision tasks (ResNet series and ImageNet, CIFAR10) demonstrate its efficiency in performance and compression.

### Strengths
- The idea of the proposed method is straight forward and easy to understanding.
- It is interesting of combining quantization (for efficient inference) and compression (for storage).

### Weaknesses
 - The main methods used in this submission is published and well-known. The submission merely combine the methods with a Lagrange formulation.


### Questions
- In experiments, the submission use Bits-Per-Weight to represents the compression performance, how is it related to the actual storage?
- As I understand, the compression take effects in disk (offline storage), instead of memory (online inference), is the proposed method benefit for inference speed?

### Soundness
3

### Presentation
3

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
The authors propose a method to combine compression with neural network quantization. The authors add a rate-distortion penalty to the rounding function and toggle its weighting to control the trade-off between compression rates and model quality. They conclude that their added compression penalty improves compression rates without severely impacting model quality.

### Strengths
The authors investigate combining ideas from the fields of neural network quantization and compression. They introduce a penalty to the rounding procedure that allows a practitioner to control the rate/distortion trade-off. The penalty works as they hypothesize.

### Weaknesses
While the experiments support their hypothesis, the baselines and models are insufficient. Since the authors are investigating post-training quantization techniques, it is expected to also test on language models. If model size is an issue for the authors, there are reasonably sized models to experiment with that are similar sizes to ResNet50 (e.g., Pythia-70M). Furthermore, if focusing only on convolutional architectures, it is important to test MobileNets, which are notoriously challenging and useful benchmarks. Finally, the design space for the Pareto frontier is unclear as the quantization levels for OPTQ are not disclosed. Furthermore, the evaluation is limited to image classification tasks on CIFAR10 and ImageNet, which are not representative of the breadth of applications where model compression is critical. The lack of experiments on more complex tasks and datasets limits the assessment of the method's general applicability. The authors also fail to compare against Deep Compression [1], a seminal work in model compression, which reported significant compression rates on VGG16. It is unclear if OPTQ-RD provides any significant uplift over this. Finally, as OPTQ was designed for and tested on LLMs, the author's acknowledgment of the challenges with LLMs implies a degradation in performance of that workload. This is an important challenge for the authors to either characterize or address in order for the work to be relevant to this conference.

### Questions
- What is the design space for the Pareto frontier?
- Did you quantize each of the models to different bit widths?
- If you are quantizing to 8-bit weights and activations before the penalty, it doesn't seem surprising that a compression penalty would cause significant savings. OPTQ (and other PTQ techniques for that matter) can push bit widths lower before significant degradation. Did you try quantizing weights and activations to 4 bits as the baseline?
- Why not test on parameter-efficient architectures such as MobileNet, EfficientNet, etc.?
- Why not test on small language models?

### Soundness
3

### Presentation
2

### Contribution
2
