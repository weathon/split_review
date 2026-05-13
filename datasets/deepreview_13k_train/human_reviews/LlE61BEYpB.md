# FLARE: Fine-tuned Long-context Acceleration with ReLU-enhanced FIRE

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Deploying large language models (LLMs) on resource-constrained edge devices is challenging due to computational bottlenecks, memory bottlenecks, and -- for long-contexts -- specifically the Softmax operation in the attention mechanism. While using ReLU in place of Softmax has been explored, and FIRE as an alternative to RoPE has been explored for models trained from scratch, there has been little work towards exploring fine-tuning models to utilize these efficient algorithms, or the combination of the two.

In this paper, we contribute FLARE, a method for fusing Rectified Linear Activations (ReLU) with Relative Encodings (specifically FIRE), and we share a particular recipe which allows these to be fine-tuned effectively into existing models and fused to create efficient long-context inference. Following this recipe yields markedly better validation loss, long-context inference speed, and successfully introduces the property of length-generalization -- the property where the model gains high accuracy for contexts lengths several times larger than trained -- unlike RoPE -- without further fine-tuning.   

Once FIRE and ReLU are both fine-tuned into a model, we show these can be mathematically fused into a single, more efficient operation, which on average was found to shave 98.9\% of FIRE operations and produce a Probability matrix with 98.9\% zeros in its lower-triangle.

Finally, we benchmark inference speed improvements for custom hardware as well with custom CUDA kernels. Using Power, Performance, and Area (PPA) analysis, we show that FLARE operates at eight times the frequency of Softmax while consuming only 0.1\% of the power and 0.11\% of the energy per cycle. Our custom CUDA Kernel shows 3.8x faster operation than Softmax FlashAttention. We believe this shows the potential of fine-tuning new algorithms in pre-trained models, and we share our fine-tuning recipes, code and custom hardware designs at \url{https://anonymous.4open.science/r/nanoGPTBD54}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper propose to combine FIRE position encoding method with ReLU activation to serve as an efficient attention mechanism for long context input. It evaluates on GPT-2 within a commercial EDA tool. The experiment is designed to fine-tune GPT-2 with the new architecture on OpenWebText data. The validation loss and inference speed is compared to demonstrate the effectiveness of the method.

### Strengths
1. reasonable but less common paper writing flow.
2. effective proposal on combining FIRE with ReLU to replace softmax based attention. 
3. solid implementation on proposed ReLUFlashAttention and hardware profiling.

### Weaknesses
1. the paper presentation is poor, e.g., typos, figure formatting, section organization, etc. 
2. the idea is driven by single model experiment and lack of insightful analysis.
3. L83-L90, the notation "n" is missing definition. 
4. L322, "don't" is less formal. 
5. Fig. 8 and Fig. 9, captions are not centered. 
6. The number 20K seems to be model dependent, and it cannot generalize to other models. There is no guarantee how long to fine-tune the proposed method, which is also mentioned as a concern of instability from using ReLU as in L151. 
7. why only compare ReLU and softmax in section 8? 
8. where are other curves in figure 3, 5 and 7?

### Questions
1. L83-L90, the notation "n" is missing definition. 
2. L322, "don't" is less formal. 
3. Fig. 8 and Fig. 9, captions are not centered. 
4. The number 20K seems to be model dependent, and it cannot generalize to other models. There is no guarantee how long to fine-tune the proposed method, which is also mentioned as a concern of instability from using ReLU as in L151. 
5. why only compare ReLU and softmax in section 8? 
6. where are other curves in figure 3, 5 and 7?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents the ideas to improve the performance and energy consumption for LLM models. Ideas presented in the paper can be summarized in the following points
* Replacing Softmax with ReLU for attention blocks.
* Integrating the above change in FIRE positional encodings to show the effectiveness of the technique for a long context (termed as FLARE).
* Study of improvement in performance of softmax block on GPU.
* Study of improvement in PPA of hardware implementation of FLARE vs Softmax.

### Strengths
* Paper has been written clearly with progressive introduction of concepts.
* It captures and presents interesting insights about the training models with FLARE and Softmax.

### Weaknesses
 * The major weakness is the lack of novelty (or a lack of clarity in conveying the primary contribution). To the best of my understanding, the paper provides the following contributions:

  * Replacing Softmax with ReLU for attention blocks.
  > * The use of ReLU instead of Softmax is well-studied (e.g., [1] [2]). The paper provides evidence of the feasibility of replacing Softmax with ReLU; however, the results align with expectations set by [1]. As noted in reference [1], "we observe that attention with ReLU divided by sequence length can approach or match traditional Softmax attention in terms of scaling behavior as a function of compute for vision transformers." This is consistent with the results presented in the paper. It will be helpful to prominently mention any new insights that will be helpful for the community. Specifically, the paper should clarify if the ReLU attention mechanism is being used with or without the scaling factor of sequence length. If the scaling factor is being used, then the results are not novel, and if not, then the paper should provide a detailed analysis of the impact of not using the scaling factor on the model's performance and convergence.
  * Integrating the above change in FIRE positional encodings to show the effectiveness of the technique for a long context (termed as FLARE).
  > * Line 260-261: "At time of writing, we haven’t seen any previous attempts to finetune FIRE encodings into models to add longer context capabilities". Ref [3], the paper which introduced FIRE contains the section named "FINETUNING ON LONG TEXT BENCHMARK". Please highlight the difference with your work. The paper needs to clarify whether the finetuning in the FIRE paper [3] involves only the weights of the model or also the positional encodings themselves. If the FIRE paper also finetunes the positional encodings, then the novelty of this work is further diminished. If only the model weights are finetuned in [3], then the paper should highlight this difference and provide a detailed analysis of the impact of finetuning the positional encodings on the model's performance and length generalization.

  * Study of performance improvement in the softmax block on GPU.
  > The practical enhancement achieved by using ReLU with zero-skipping is impressive for both CUDA and hardware implementation. However, an analysis of the overall impact on the model's execution time is lacking. Please include the end-to-end execution time of the models presented in the paper, as this will help underscore the comprehensive impact of the proposed change. The paper should also include the overhead of zero-skipping in the end-to-end execution time. The paper should also include a breakdown of the execution time for different parts of the model to understand the impact of the proposed change on the overall execution time.

  * Study of improvements in PPA for hardware implementation of FLARE vs. Softmax.
  > The significance of this study would be strengthened by adding the percentage area of the blocks in a DNN ASIC accelerator or alternative metrics to quantify the overall impact of these hardware modifications. The paper should also include the power consumption of the blocks in a DNN ASIC accelerator to understand the impact of the proposed change on the overall power consumption. The paper should include a detailed analysis of the area and power consumption of the different components of the FLARE and Softmax blocks to understand the source of the improvements.

### Questions
* Is there a reason for using the 130nm PDK for the PPA comparison, given that it is several generations old? The results could differ significantly on more recent technologies, and employing a newer technology node would enhance the credibility of the results.
> Some more advanced open-source PDKs are available, such as [1][2]. However, depending on the tools used, integration may not be straightforward.

[1] https://github.com/mflowgen/freepdk-45nm   
[2] https://eda.ncsu.edu/freepdk15/

### Soundness
2

### Presentation
3

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
The paper tackles the challenge of deploying large language models (LLMs) on edge devices by optimizing attention mechanisms. Specifically, the authors replace the Softmax operation used in traditional transformers with ReLU, aiming to improve computational efficiency for long-context sequences. They also integrate FIRE (Functional Interpolation for Relative Encoding) to improve the handling of long input sequences. The paper introduces a system named FLARE, which combines ReLU-based attention with FIRE encoding and fine-tunes it on GPT-2 to showcase the performance benefits in terms of speed, efficiency, and memory usage.

### Strengths
While the idea of using ReLU in place of Softmax has appeared in prior research, this paper is novel in the sense that it combines it with FIRE positional encoding for long-context acceleration. The focus on deploying these techniques for edge devices is timely and practically relevant, given the rising demand for efficient LLMs in constrained environments.

Besides, the paper presents a well-structured experimental evaluation, profiling memory usage, speed, and power efficiency. The experiments are thoughtfully designed to show how ReLU-based attention performs compared to Softmax on long-context inference. 

In terms of the writing quality, the paper is clear and easy to follow, with well-defined objectives and explanations of both ReLU and FIRE techniques. The figures and tables help convey the improvements in speed and power usage, though additional comparisons with other positional encodings would have been helpful.

### Weaknesses
1. The core ideas—using ReLU instead of Softmax and FIRE for positional encoding—are borrowed from prior work. The contribution lies mainly in engineering and integration, rather than in proposing a new method or theory. This makes the paper more of an “A + B”-style contribution.

2. The paper primarily evaluates performance on GPT-2. It is unclear how well the proposed optimization generalizes to larger models like Qwen, LLaMA, or LLaMA-2. Could these gains be replicated on models with billions of parameters? Further benchmarking would have strengthened the paper. As long as the authors mentioned that they had access to 80GB A100s, I think larger and more-updated models shall be fine-tuned in the similar approach with FSDP support, and the results shall be included in the experiments to demonstrate the effectiveness of the purposed algorithms,.

3. The paper claims the target of improving inference efficiency on edge devices, but only the experiment of PPA hardware has been provided. In real edge devices like an android device, the power measurement is not that straightforward. I know the authors could not directly use edge-LLM implementations like Llama.cpp to test on a real edge because modifications on the backend and the computation-graph formulation stage are required, but I think it is fine to implement a single attention block and test on different real edge platforms, to give a more direct sensing of the effectiveness of the proposed algorithms.

4. I think the only validation loss could not demonstrate the ability of a language model before and after fine-tuning. More down-stream tasks are more important than validation loss.

### Questions
My question is summarized as:

1.  Can the proposed method scale to larger models like Qwen, LLaMA, or LLaMA-2?

2.  How would the method perform on real edge devices, like Android phones? Could a single attention block be tested on such devices for more practical insights?

3. Why were downstream tasks not included to assess the fine-tuned model’s real-world performance beyond validation loss?

### Soundness
2

### Presentation
4

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
Deploying transformer models on edge devices with limited battery life presents significant challenges, particularly for long-context applications. The Softmax operation often becomes a major bottleneck due to constraints like reduced memory bandwidth and parallelism, making it hard to utilize latency-optimizing techniques. This paper proposes a solution by fine-tuning the ReLU function as a replacement for Softmax, along with utilizing Functional Interpolation for Relative Position Encoding (FIRE), which improves model efficiency and maintains accuracy. The resulting algorithm, ReLU-enhanced FIRE (FLARE), combines these techniques, reducing power consumption and operational complexity, which is particularly suitable for large language models on edge devices.

### Strengths
1.	The tackled problem is relevant to the community.
2.	The proposed method is useful for reducing the computation complexity of large language models.

### Weaknesses
1.	The limitations of the related work and how these issues are addressed in the proposed method should be clarified.
2.	This work builds upon several related works and combines multiple techniques. A clear distinction between what is novel in the proposed method and what is implemented based on existing methods is required.
3.	The proposed method should be discussed in more detail describing all the operations involved. Please also explain all the design decisions made to develop it.
4.	The experimental setup and tool flow used to conduct the experiments should be discussed in more detail.

### Questions
1.	What are the limitations of this paper and what are the potential impacts at large scale of this work?

### Soundness
2

### Presentation
2

### Contribution
2
