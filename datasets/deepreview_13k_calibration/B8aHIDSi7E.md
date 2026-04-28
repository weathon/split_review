# Getting Free Bits Back from Rotational Symmetries in LLMs

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
Current methods for compressing neural network weights, such as decomposition, pruning, quantization, and channel simulation, often overlook the inherent symmetries within these networks and thus waste bits on encoding redundant information. 
In this paper, we propose a format based on bits-back coding for storing rotationally symmetric Transformer weights more efficiently than the usual array layout at the same floating-point precision.
We evaluate our method on Large Language Models (LLMs) pruned by SliceGPT \citep{ashkboosslicegpt} and achieve a 3-5\% reduction in total bit usage \emph{for free}
across different model sizes and architectures without impacting model performance within a certain numerical precision.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors highlight that the rotational symmetries of SliceGPT introduce redundancies. Based on SliceGPT, they propose further compressing the weights by the bits-back coding algorithm. Specifically, rather than treating all weight configurations as unique, they encode weights up to an equivalence class defined by rotations, enabling smaller memory requirements. They conducted experiments on several benchmarks with multiple models. The results verify the effectiveness of their proposed method.

**Strengths**
1. The proposed method is novel and insightful
2. The proposed method is well-motivated and has the potential to make a broader impact.
3. The experiment results are promising.

**Weaknesses**
1. The writing is not self-contained. Specifically, the paper relies heavily on bits-back coding. However, they do not properly connect SliceGPT with the previously proposed bits-back coding. It is hard to understand the actual algorithm.
2. It is questionable if the method can be applied in the real world given the compression/decompression and matrix decomposition procedures involved. The run speed of this method could be slower than that of the vanilla Transformer model.

In summary, the paper is insightful and well-motivated. However, the writing is not self-contained and the overhead could hinder the real-world application. As a result, I recommend a weak acceptance.

### Strengths
1. The proposed method is novel and insightful
2. The proposed method is well-motivated and has the potential to make a broader impact.
3. The experiment results are promising.

### Weaknesses
1. The writing is not self-contained. Specifically, the paper relies heavily on bits-back coding. However, they do not properly connect SliceGPT with the previously proposed bits-back coding. It is hard to understand the actual algorithm.
2. It is questionable if the method can be applied in the real world given the compression/decompression and matrix decomposition procedures involved. The run speed of this method could be slower than that of the vanilla Transformer model.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes the application of the bits-back algorithm to reduce the overhead of additional matrices introduced by pruning large language models (LLMs) using SliceGPT. In the SliceGPT method, an additional matrix is introduced for the rotation matrix, which helps in maintaining accuracy but results in additional computational overhead, thereby acting as a compression overhead. To address this issue, we propose an algorithm that encodes/decodes the rotation matrix using the bits-back algorithm, demonstrating that the rotation matrix can be computed solely through the decoding process during inference. Our proposed method shows an additional 3-5% improvement in compression efficiency compared to the practical compression rate of SliceGPT.

### Strengths
* The paper proposes a method to compress the rotation matrix Q introduced by SliceGPT using the bits-back algorithm, effectively reducing the parameter overhead.
* It demonstrates that the rotation matrix Q can be encoded and decoded using the bits-back algorithm without requiring a calibration set, relying solely on the weight matrix.
* The study shows that while the actual compression rate of SliceGPT with the rotation matrix Q is approximately 9%, the proposed method can achieve a closer-to-expected compression rate of 13%. It also demonstrates that applying the proposed encoding method to the rotation matrix Q in models such as OPT and LLaMA2-7B does not result in significant differences in Commonsense Reasoning (CSR) performance.

### Weaknesses
 * The paper lacks sufficient analysis and experimentation regarding the practical impact on latency and throughput during inference when decoding the rotation matrix Q using the proposed method. Specifically, the paper does not provide any measurements of the time required to decode the rotation matrices during the model loading phase, nor does it analyze how this decoding time scales with model size or the number of rotation matrices. This is crucial because the decoding process, while not part of the core inference loop, still contributes to the overall time required to deploy a model.
* The proposed method is somewhat limited in scope, as it can only be applied after the implementation of SliceGPT, thereby restricting its applicability. The paper does not explore the possibility of applying the bits-back algorithm to other types of model compression techniques or to other forms of redundancy that might exist within LLMs. This limits the broader impact of the proposed approach.
* The actual benefits of encoding the rotation matrix Q in terms of inference latency and throughput might be minimal. It is likely that during the prefill stage, the additional decoding step for the rotation matrix Q could result in higher inference latency and lower throughput compared to SliceGPT alone. The paper does not provide any analysis of the computational cost associated with decoding the rotation matrix, nor does it discuss potential optimizations that could be applied to reduce this cost. Furthermore, the paper does not consider the memory bandwidth implications of decoding the rotation matrix, which could be a bottleneck in practical deployments.

### Questions
* How does the proposed method perform in terms of inference latency and throughput gains compared to SliceGPT when applied on actual hardware like GPUs? If the effectiveness of this aspect is demonstrated, I would be inclined to increase my rating.

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
2

### Summary
The paper presents a novel training-free compression technique of large language models that exploits rotational symmetries in the weight space. It uses bits-back coding, a compression strategy that takes advantage of these rotational symmetries to compress Transformer models by about three to five percent while impacting the model's perplexity in a negligible way. The method was tested on SliceGPT-pruned Transformers, namely the OPT and Llama-2.

### Strengths
- The paper presents bits-back coding used on neural network models, mainly focusing on enlarging language compression. 
- The proposed method is computationally feasible since it runs without retraining. 
- The paper's novel technique is evaluated on models, such as OPT and Llama-2, demonstrating performance metrics are not significantly affected in terms of perplexities drop.

### Weaknesses
 -  This approach is inherently SliceGPT pruning and Transformer-specific architecture, which may also limit its use to other neural networks or pruning techniques.
- The methodology relies only on Transformer architectures, so applicability to lighter models suited to edge devices could be considered.

### Questions
- What is the prospective effectiveness of the method when it comes to implementation on the models with precision format lower than float16? 
- Is it possible to apply the bits-back coding method to the architectures that are not transformers or the architectures compressed with different methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes to apply a coding scheme to utilize symmetries made available by the SliceGPT method for training-free weight-only quantization. The resulting method achieves an additional 3-5% reduction in the total weight sizes for SliceGPT compressed models. The authors show that their resulting models do not diverge significantly from the original models when evaluated on tasks such as PIQA, WinoGrande, and HellaSwag.

### Strengths
1. The proposed method is training-free, making the result independent from the choice of calibration set.
2. The proposed method can be computed using only a CPU, without heavy computational requirements. This will make adoption easier.

### Weaknesses
1. The improvement of 3~5% appears small unless the method does not impose other overheads. However, there is no detailed analysis of how much memory the other components, such as the correction code, use.

2. Additionally, the work does not include any analysis of the overhead in terms of the time required for inference caused by applying additional computations to the model. Even if computing the rotation can be performed on CPU, there should be an analysis of the effect on inference latency when measured end-to-end.

### Questions
The beginning of Section 2 uses the word “delving” prominently. As the word “delve” is strongly associated with large language model outputs, we advise the authors to rephrase the sentence.

### Soundness
2

### Presentation
2

### Contribution
2
