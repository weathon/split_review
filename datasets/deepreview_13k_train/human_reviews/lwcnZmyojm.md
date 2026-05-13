# QRazor: Reliable and Effortless 4-bit LLM Quantization by Significant Data Razoring

- Decision: Reject
- Scores: 6, 5, 6, 6, 3

## Abstract
Large-scale language models (LLMs) have demonstrated outstanding performance in language processing tasks, yet their deployment is often hindered by high memory demands and computational complexity. Although low-bit quantization techniques, such as 4-bit quantization, present a potential solution, they frequently lead to significant accuracy degradation or require substantial effort for such aggressive quantization approaches. To overcome these challenges, we introduce QRazor, a reliable and effortless quantization scheme designed to enable 4-bit quantization for weights, activations, and KV cache in transformer-based LLMs. The scheme involves two main stages: quantization and compression. During the quantization stage, weights, activations, and KV cache values are quantized with wider 8 or 16-bit integers as a basis to achieve nearly identical accuracy to the original full-precision LLM models, using the absolute max scaling. Subsequently, all data are compressed to 4-bit using our proposed significant data razoring (SDR) technique, which retains only the four most salient bits while discarding the others. Furthermore, we present an integer-based arithmetic unit dedicated to QRazor, enabling direct low-precision arithmetic operations without decompressing the SDR data. Despite the reduced quantization effort, QRazor achieves LLM accuracies better or comparable to state-of-the-art 4-bit methods. By also validating the hardware efficiency, our decompression-free arithmetic unit achieves 61.2\% and 57.8\% reduction in area and power consumption, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
QRazor presents a two-stage quantization process (quantization and compression) that allows for reliable 4-bit quantization of weights, activations, and KV cache in transformer-based LLMs

### Strengths
+ This technique retains only the four most salient bits while discarding others, enabling effective compression without manipulating data distributions

+ QRazor achieves LLM accuracies that are better or comparable to state-of-the-art 4-bit methods, despite reduced quantization effort

+ The paper presents an integer-based arithmetic unit specifically designed for QRazor, allowing for direct low-precision arithmetic operations without decompressing the SDR data

### Weaknesses
While the paper claims superior or comparable performance to state-of-the-art methods, it would be beneficial to see a more comprehensive comparison with other recent quantization techniques. I know there is a lot of quantization papers on LLMs and it's hard to keep up with it. But, it ll be good to at least compare with some recent works that are showing SOTA results: QuaRot [1], TesseraQ [2].

How will Qrazor perform on architectures beside Llama, say mistral or gemma? What about llama 3.2 specifically the edge versions: 1B, 3B models?

While the paper discusses hardware efficiency, it doesn't provide a detailed analysis of any potential computational overhead introduced by the two-stage quantization process. Also, is there an impact from a memory perspective?

### Questions
See weaknesses above

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel post-training quantization (PTQ) method, QRazor, designed for efficient low-bit quantization of large language models (LLMs). This technique aims to address the challenge of accuracy loss typically associated with aggressive quantization methods, especially at 4-bit precision. QRazor introduces a two-stage quantization and compression approach that first quantizes weights, activations, and KV caches to 8- or 16-bit integers using a method called absolute max scaling. It then applies a new compression technique, Significant Data Razoring (SDR), which selectively retains the most significant bits of data, reducing memory and computational demands without decompression. Experimental results show that QRazor achieves accuracy levels on par with state-of-the-art quantization methods.

### Strengths
Efficient Quantization: QRazor successfully enables 4-bit quantization for weights, activations, and KV caches while reducing the memory and computation costs of deploying LLMs in resource-constrained environments.

Adaptability Across Models: QRazor demonstrates effectiveness across different model types (e.g., LLaMA, LLaMA2) and quantization settings, showing flexibility and robustness in various use cases.

Extensive Evaluation: The paper provides detailed evaluations on task accuracy, resource usage, and power efficiency, supporting the method's applicability and benefits.

### Weaknesses
Accuracy Trade-offs: Although accuracy degradation is minimized, the paper does note some accuracy drops in specific tasks, especially under aggressive group compression settings. This could impact applications where even minor precision loss is critical.

Complexity of Scaling Parameters: The granularity of scaling parameters, such as per-channel and per-tensor configurations, introduces complexity in implementation and may require careful tuning to achieve optimal results.

### Questions
- How does the proposed method perform on fine-tuned LLMs for specific downstream tasks?

- It would be helpful to include the total number of parameters and FLOPs in all comparison tables for clearer evaluation of computational efficiency.

-It would be helpful to provide a direct comparison with prior works from the introduction section.

### Soundness
3

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
2

### Summary
This paper proposes a 2 stage quantization to reduce the memory and compute requirements for LLMs. It quantizes the weights, activations and KV caches in an LLM in two stages. They first quantize the FP16 parameters to integers and then compress these integers using their SDR algorithm. They show the benefits of their method by comparing with other Quantization methods on Llama and Llama2 class of models on lm-eval-harness.

### Strengths
1.⁠ ⁠Their method is simple to understand and shows significant benefits to the baselines
2.⁠ ⁠They show empirically that QRazor performs much better than the baselines at the same bitwidth.

### Weaknesses
1.  Since they keep the most significant bits from the razoring point, they are not effectively using the range of their bitwidth. This is because they use integer shifts instead of floating point scales. The integer shifts, while computationally cheaper, limit the precision that could be achieved if a floating-point scaling factor was used, potentially leading to a loss of accuracy for values that fall between the discrete steps of the integer representation.
2.  Why are the FP16 accuracies for the same model different when comparing with baselines and QRazor in Table 1? This makes me question the fairness of the comparision.
3.  Because of these, it will be good to include experiemental results with different tasks and models for comparision. The current evaluation is limited to a specific set of tasks and models, and it is unclear how well the proposed method would generalize to other tasks and architectures. For instance, it would be beneficial to see results on tasks that require more complex reasoning or on models with different architectural characteristics.
4.  In table 1, what are the effective bit-widths of the baselines and QRazor? The paper should clearly state the effective bit-widths of the baselines and the proposed method to allow for a fair comparison. The effective bit-width should take into account all overheads, such as the bits used for scaling factors or flags.
5.  How do the area and power numbers compare for baselines? The paper lacks a comparison of the hardware area and power consumption of the proposed method against the baselines. This information is crucial for assessing the practical benefits of the proposed quantization technique, especially for deployment on resource-constrained devices.

### Questions
1.⁠ ⁠How does this quantization scheme affect the inference speed? Since the activations are quantized per token, I am assuming the inference speed takes a huge hit.
2.⁠ ⁠How does this method compare to weight-only-quantization methods like GPTQ, QuIP or FrameQuant? They show that activation quantization is not a huge bottleneck in LLM inference and are able to achive very low bitwidth for weights.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Qrazor, a post training quantization technique pushing toward 4-bit quantization for weights, activations, as well as KV cache values (optionally). Quantization is block based and performed in two stages. First, the blocks of the tensors are quantized to high-bit-width integers (16 bits), then a "razoring" technique is applied to reach the final target quantization bit-width: after conversion to sign-magnitude, the most significant non-zero bit is identified among all pre-quantized (16bit) elements within the target block. All the zero bits at more significant digits are removed from all the elements, then the next 4-bit in order of decreasing significance are retained, with rounding applied to the last bit (flooring as special case if rounding would cause overflow in the 4-bit representation.   The authors also study the powe advantage obtainable by performing the tensor operations at low precision instread of pre-expanding the quanzized numbers. The compare against previously published 4-bit quantization techniques.

### Strengths
The explanation is clear, the technique presented is  simple and straightforward: a combination of known techniques is applied leading to the method presented. 
Authors provide also a (simplified) estimation of power savings enabled by the technique with a dedicated unit that computes directly in low pecision formats. 
Comparison with respect to state-of-the-art competitive methods is presented.

### Weaknesses
The analysis of outlayers is quite superficial. It's unclear why it's not always the case that the initial truncation does not always lead a 1 in the most significant bit: if the Max value of the block is used for quantization to 16-bit, it should be the case, however if a max on a much larger block is used, then it can very well be the case that the max will squeeze almost all the bits of an entire block to zero). Since the max will tend to be the outlayer, then the loss of precision on all the numbers in a block could be massive.  
There is no discussion on implementation on existing hardware
The hardware idea proposed is discussed in isolation, leading to a inflation on the potential power advantages, since it neglects lots of HW that would not change (e.g. all the memory hieararchy). 
Comparison wrt SoA shows that improvements over fine-tuned previous work does not show super-impressive advantages.

### Questions
It would be very good to see for each block which bit would be non-zero on average, i.e. on average how many leading bits can be truncated, also it would be good to see the percentage of zerooed elements per block after the aggressive quantization step.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes QRazor. A fine-grained quantization techniques that shows an alternate way of doing max scaling at the group-level in terms of bit positioning and bitwise operations. The approach is however identical to fine-grained dynamic max scaling that has been massively explored before.

### Strengths
Unfortunately, there is not much that can be said here.

### Weaknesses
There are several weaknesses - please see the questions. To summarize, there are issues with respect to the novelty of the technique. QRazor is just doing fine-grained dynamic max scaled quantization, but it is disguised as a bunch of bitwise operations. In addition, the empirical evaluation is weak, focusing only on multiple choice questions.

### Questions
- Why is min-max scaling introduced if it is not used in the work. There's also no reference accompanying it. Section can be made shorter if we only introduce absolute max-scaling as the PTQ recipe employed (it probably won't even need to be a section of its own).
- Figure 1 is very hard to read without significant zooming and horizontal scrolling. The caption is also not helpful in understanding how the QRazor approach works.
- What does "2s complement except the sign bit for negative activations" mean? Is that referring to 1s complement or sign-magnitude?
- In line 191-192 the authors argue that a coarser grained scaling is favorable for activation quantization since it has to be done online. This is wrong. Since activation quantization is done online, its scaling and quantization should occur in the epilogue of the prior operation (either a layernorm or an activation function). Fine-grained scaling and quantization can be fused in cuda with said prior ops whereas coarse grained scaling would require a reduction operation (such as max) over the whole tensor (or channel) which would be slow.
- The proposed SDR technique is exactly the same as a dynamic per-group max. It just provides a hardware method to do it when the groups are coming from high-precision integers representations.
- In the results section, in Table 1: why is there a duplication of FP16 baseline for each model? And why are the duplicated baselines not having similar accuracy?
- Since W4A8 is highlighted, can we have a comparison to AWQ?
Can the authors add perplexity of the models in addition to scores on multiple choice questions (which can be noisy)? I suggest using Wikitext-103 test set.

### Soundness
2

### Presentation
1

### Contribution
2
