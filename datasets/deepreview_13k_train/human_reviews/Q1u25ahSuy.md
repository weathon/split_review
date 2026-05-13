# SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
\vspace{-2px}Recent advances in large language model (LLM) pretraining have led to high-quality LLMs with impressive abilities. 
    By compressing such LLMs via quantization to 3-4 bits per parameter, they can fit into memory-limited devices such as laptops and mobile phones, enabling personalized use. 
    However, quantization down to 3-4 bits per parameter usually leads to moderate-to-high accuracy losses, especially for smaller models in the 1-10B parameter range, which are well-suited for edge deployments. 
    To address this accuracy issue, we introduce the Sparse-Quantized Representation (SpQR), a new compressed format and quantization technique which enables for the first time \emph{near-lossless} compression of LLMs across model scales, while reaching similar compression levels to previous methods. 
    SpQR works by identifying and isolating \emph{outlier weights}, which cause particularly-large quantization errors, and storing them in higher precision, while compressing all other weights to 3-4 bits, and achieves relative accuracy losses of less than $1\%$ in perplexity for highly-accurate LLaMA and Falcon LLMs. This makes it possible to run 33B parameter LLM on a single 24 GB consumer GPU without any performance degradation at 15\% speedup
    thus making powerful LLMs available to consumer without any downsides. Specifically, we provide an efficient GPU inference algorithm for SpQR which yields faster inference than 16-bit baselines at similar accuracy, while enabling memory compression gains of more than 4x.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents Sparse-Quantized Representation (SpQR), a compression technique for large language models (LLMs) that reduces the weight to 3-4 bits per parameter while maintaining near-lossless accuracy. SpQR isolates and retains outlier weights at high precision and compresses the rest, effectively fitting larger LLMs on devices with limited memory. The approach is shown to preserve model accuracy, reduce memory usage by over 3.4x, and increase inference speed by 15-30% compared to traditional 16-bit models.

======Update 11/26======  Most of my concerns have been addressed through the author's rebuttal and I am revising my score to a 6.

### Strengths
- SpQR can compress LLM weights to 3-4 bits per parameter with less than 1% relative accuracy loss.
- It not only reduces the memory footprint by over 3.4x but also speeds up inference by 15-30% compared to 16-bit models.

### Weaknesses
 - SpQR's methodology, which focuses on outlier management and mixed-precision quantization. Prior works have already delved into the impact of outliers on quantization [1] and the use of mixed-precision quantization [2] to optimize resource use. Hence, SpQR represents an evolutionary improvement in engineering work on LLM weight compression, refining rather than making some novel change in the field.
- The two-step quantization process might be more complex than traditional methods, potentially leading to more involved implementation and tuning.
- While the paper claims efficiency improvements, the actual gains may depend on specific model architectures and deployment scenarios, and there could be overheads associated with managing the sparse representations.
- The benefits of SpQR are maximized with specific hardware capabilities, which may not be universally available.

### Questions
Could you clarify how the 3-bit matrix multiplication was executed on the A100 GPU architecture? Was the focus primarily on optimizing memory access by compressing the weights, while the computation itself was conducted using 4-bit matrix multiplication to balance performance and memory efficiency?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new quantization method, SpQR, for the weights of LLMs. This method first isolates the outlier weights and keeps them in high precision, then it employs a grouped quantization for higher accuracy. During inference, SpQR uses sparse-matrix multiplication for the outliers and uses dense-quantized matrix multiplication for “base” weights. As a result, compared with the 16-bit model, it can achieve 3.4x compression and 20-30% speedup without any degradation in perplexity.

### Strengths
* Give a deep analysis of the outliers in the weights and show different distribution patterns of them, which can help isolate the outliers from the weights.
* Propose a grouped quantization, which is more fine-grained than prior methods, for better model accuracy. Also, propose a two-level quantization to reduce the overhead of the group-wise statistics.
* Experiments show the real speedup on GPUs to demonstrate the effectiveness of the proposed method.

### Weaknesses
 * The proposed method has limitations and may not be easily applicable to activation quantization in LLM. During inference, the memory accesses for activations also take a large amount of time.
* The unstructured sparse pattern of the outliers is not very friendly to GPUs, and this will impose significant overhead on the computation.

### Questions
* In section 4.1, high-sensitivity outliers, there are two types of outliers, i.e., group-wise outliers and individual outliers. In section 4.2, the weight outliers are stored with the Run-Length Coding, which saves the relative index. Are the group-wise outliers used in the proposed method? Or only save individual outliers? For the two types of outliers, do they both use the same format to store?
* As for the weights in multi-head attention and the MLP, is there any difference when quantizing those weights? Or they are all the same? 
* Did you compare the model accuracy and the real speedup with the 8-bit weight quantization methods? I just wanna if it is worth quantizing the weights to 4-bit with such a large overhead from the unstructured sparse outliers.
* Can you compare the performance between the quantized GEMM with 4-bit SpQR and the quantized GEMM with a normal 4-bit weight quantization method? It is better to do such ablation to show the performance overhead of the grouped quantization and the unstructured sparse outliers.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a hybrid sparse-quantization framework named Sparse-Quantized Representations (SpQR), which identifies the isolating outlier weights and stores them in higher precision while compressing all other weights to 3-4 bits. To overcome the challenge of poor GPU support, a sparse-matrix multiplication algorithm is proposed. The proposed achieves compression levels comparable to previous methods with less performance degradation.

### Strengths
1. While outlier input features have been observed in existing work, this work is the first to demonstrate that similar outliers occur in the weights, for particular output hidden dimensions. 

2. This work not only indicate the advantages of weight quantization in terms of memory saving, but design a specific sparse-matrix multiplication algorithm, which demonstrates the advantage of inference time of proposed in Tab. 3.

3. This paper is well-written and organized, and the supplementary material is sufficiently detailed (such Tab. 10).

### Weaknesses
1. The experiment results related to large vision model (such SAM/DINOv2) are expected also.

### Questions
1. Are there experimental results that also quantify the activation?

### Soundness
3 good

### Presentation
3 good

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
Through extensive analysis of large language model outliers, the proposed method, SpQR, adopts a dual-stage weight-only quantization with small group sizes, achieving 3 or 4-bit precision per parameter. For the outliers, SpQR preserves them in FP16 with an unstructured format using an indices matrix. SpQR provides details on the implementation of both encoding and decoding algorithms. Experimental results show competitive performance on next-token generation tasks in language modeling, such as Wikitext2, C4, PTB with Falcon, and LLaMA. Notably, the provided GPU inference algorithm exhibits faster latency compared to 16-bit baselines while maintaining similar accuracy.

### Strengths
* Detailed analytical demonstrations of outliers in large language models.
* Offers a detailed breakdown of how the two-stage quantization works in conjunction with the sparse representation for outliers.
* Sets aside outlier values in a sparse, unstructured format to keep the accuracy of the language model's performance, which is a more advanced concept than previous methods.
* The overall problem statement and its algorithmic solution are clear and easy to understand.

### Weaknesses
1. *Evaluation Benchmarks:* While the authors have acknowledged this in their limitations, the absence of performance evaluations on trendy benchmarks for generative models (such as MMLU, mathematical reasoning performance like GSM8K, or coding abilities such as humaneval) represents a weakness. Evaluating at least one of these benchmarks is crucial to better ascertain the proposed algorithm's effectiveness.  
2. *Quantization Baselines:* SpQR demonstrates good accuracy using a very small group size. Therefore, I kindly suggest comparing it with baselines like RTN, GPTQ [1] and AWQ [2] by applying a group size. While it's important to compare accuracy at identical bit-width levels, it's equally crucial to evaluate inference latency at the same accuracy level. In this context, SpQR might offer reduced memory usage. Since SpQR introduces a new representation by combining dual quantization with sparse outliers, it's essential to provide a presentation that underscores the advantages of SpQR in relation to conventional methodologies. Specifically, a comparison of the memory footprint and computational cost of SpQR's sparse outlier representation versus dense representations used in other methods would be beneficial. This should include a breakdown of the memory required for indices and the computational overhead of handling sparse data during inference.
3. *Inference Time:* SpQR employs a two-stage quantization process to utilize a very small group size, allowing for fine-grained representation and enhancing accuracy through the use of sparse representation for outliers. While it is evident that this proposed method will yield very positive results in terms of accuracy, there is a growing concern that the associated latency overhead needs to be better managed. In other words, the method presents a well-analyzed problem statement combined with easily understandable techniques that have high accuracy. However, it seems to have a weakness in the latency overhead of the two-stage quantization with such a small group size and the latency overhead for the sparse representation of outliers. Therefore, it would have been more beneficial if there had been a more varied presentation of the latency results, which arise from combining sparse matrix multiplication with quantization matrix multiplication. Specifically, in the "Inference Time" section and paragraph, the speed of the end-to-end proposed algorithm is measured. However, it would have been a better presentation if the latencies without sparse outliers and with sparse outliers were both disclosed, allowing readers to recognize the performance trade-off easily. To delve into more specifics, when sparse outliers are excluded, there should be a new baseline (such as existing prior kernels [1, 2] for weight-only quantization) comparing the latency of the quantized model where the proposed two-stage quantization has been applied. Furthermore, discussing the additional overhead when introducing sparse outliers after such a comparison would have been an excellent addition.  Ideally, to assess the performance of SpQR, it would enhance clarity if the author could specify the difference in accuracy when comparing the proposed SpQR to 4-bit group-wise methods like RTN, GPTQ [1], and AWQ [2]. At the same time, understanding the inference latency of SpQR, especially given its very small group size in comparison to these 4-bit group-wise weight-only quantization methods, would be beneficial. Lastly, highlighting its memory efficiency would further improve the clarity.

### Questions
* There are typos in the manuscript (in sections 5, 3rd paragraph 'emory'). I suggest revising them.
* In the "Ablations" paragraph of section 5, the mention of "16-bit statistics" seems to require clarification regarding the group size.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
