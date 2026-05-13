# SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
The recent advancements in large language models (LLMs) with billions of parameters have significantly boosted their performance across various real-world applications. However, the inference processes for these models require substantial energy and computational resources, presenting considerable deployment challenges.
In contrast, human brains, which contain approximately 86 billion biological neurons, exhibit significantly greater energy efficiency compared to LLMs with a similar number of parameters. Inspired by this, we redesign 7\textasciitilde70 billion parameter LLMs using bio-plausible spiking mechanisms, emulating the efficient behavior of the human brain.
We propose the first spiking large language model as recent LLMs termed SpikeLLM. Coupled with the proposed model, a novel spike-driven quantization framework named Optimal Brain Spiking is introduced to reduce the energy cost and accelerate inference speed via two essential approaches: first (second)-order differentiation-based salient channel detection, and per-channel salient outlier expansion with Generalized Integrate-and-Fire neurons.
Our proposed spike-driven quantization can plug in main streams of quantization training methods. In the OmniQuant pipeline, SpikeLLM significantly reduces 25.51\% WikiText2 perplexity and improves 3.08\% average accuracy of 6 zero-shot datasets on a LLAMA2-7B 4A4W model. In the GPTQ pipeline, SpikeLLM realizes a sparse ternary quantization, which achieves additive in all linear layers. Compared with PB-LLM with similar operations, SpikeLLM also exceeds significantly. We will release our code on GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose SpikeLLM, an energy-efficient large language model designed to tackle the increasing energy demands of current LLMs. They highlight two approaches namely, Generalized Integrate-and-Fire (GIF) neurons  and Optimal Brain Spiking framework to compresses spike length. The experimental results show improvements compared to the baselines used in the paper.

### Strengths
The paper is well motivated and addresses a genuine problem of the increasing energy cost of LLMs. Experimental results show improved performance compared to the used baselines.

### Weaknesses
1) The temporal dynamics of the model is not explained in details. There is very limited results on the activity sparsity of the model, energy-efficiency comparison with other efficient LLMs (Table 5 only compares with LLAMA-1-7B)
2) The authors can use better baselines for comparison such as 1.58 bit LLM [1], IR-QLoRA[2]. 
3) There is no experimental results showing 1-bit inference on neuromorphic chips. Even simulation showing spiking activity and convergence to similar result (as the merged spike) will demonstrate that we can use the model for efficient on-chip inference. No code has been added as part of the experiment. It is hard to understand how one would run the network in a 1-bit setting. If 1-bit (activity) inference cannot be shown experimentally then we cannot actually call this method spiking.

### Questions
1) Since this approach assigns different values of T corresponding to saliency of particular channels, can you please explain the temporal dynamics of the model (preferably during the on chip 1-bit inference phase) with a schematic diagram?

2) In Table 6, SpikeLLM uses  ternary GIF neurons as weight quantizers. What is the quantization level of the activations?

3) The results shown in Table 3 for SpikeLLM variants, all have activation quantization levels >= 4. Can we really call the models spiking?

4) Can the authors please compare their results to current sota quantized LLMs.

Please see weaknesses as well.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper is the first to introduce SNNs into LLMs, an innovation that deserves high commendation and demonstrates the broad applicability of SNNs. Additionally, the authors combine quantization techniques with SNNs to propose GIF neurons and an OBS framework. Overall, I consider this paper to make a significant contribution.

### Strengths
1. This study is the first to apply SNNs to large-scale language models with up to 70 billion parameters, filling a gap in the field.
2.: The authors provide a good analysis of issues in quantized LLMs and propose a Spike-Driven Quantization method that effectively addresses these problems.
3. The proposed GIF neurons leverage the time steps of SNNs to mitigate outliers that may result from direct quantization.
4. The method is thoroughly trained and tested on LLAMA-2-7B and LLAMA-2-70B models, validating its effectiveness. To my knowledge, this is the first time that SNNs have been tested on a model as large as LLAMA-2-70B.

### Weaknesses
1\I strongly suggest that the author takes the time to offer a comprehensive and meticulous description of the precise experimental results. It is essential to highlight the pivotal discoveries and thoroughly explore their potential ramifications within the broader context of the study.
2\It would greatly enhance the transparency and accessibility of the research if the author decides to open source the code. This action would not only foster a collaborative environment but also enable other researchers to replicate and extend the findings, ultimately advancing the field.
3\To fully ascertain the efficacy and superiority of the proposed method, it is imperative that the author conducts a more extensive series of experiments. These experiments should rigorously compare the performance of the current approach with various artificial neural network (ANN) alternatives, providing a comprehensive analysis of their respective strengths and weaknesses.

### Questions
1. Lack of Logical Structure in Related Work: The related work section primarily lists existing studies without a systematic analysis of the development and challenges of SNNs and quantization methods.
2. Unclear Formula Description: The explanation of Equation 5 (lines 239-244) is not intuitive, making it difficult for readers to understand the specific meaning of the GLIF model.
3. Insufficient Visualization: There is a lack of intuitive graphical illustrations to demonstrate how the GLIF model divides long binary sequences into smaller segments over multiple time steps.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a post-training quantization scheme for large language models (LLMs). The quantization function is computed by a spiking neural network. The contributions over prior works are a reduction of the requires number SNN simulation steps by grouping time-steps into low-bit integer operations, handling outliers by allowing certain channels to conduct multiple simulation steps, and detecting outliers in weights and activations offline. Results are compared to the OmniQuant baseline and show improved downstream task performance on a standard evaluation protocol.

### Strengths
The paper is technically sound, well written and clear in its presentation. Tables 3 and 4 meet the standards of evaluation of the LLM community. Figures 1 and 2 assist the reader in following the presented method. The extend of the material is on par with recent quantization works that have been published recently in top ML conferences (e.g. [1], [2]). The authors compare their method on the standard evaluation benchmarks for LLMs reporting both downstream task performance and language modeling performance of large scale models from LLAMA 7B to 70B.

ANN-SNN conversion as a research field is of relevance to the ICLR community. Prior methods were not evaluated at this large scale. It is expected that ANN-SNN conversion methods would face similar issues regarding outliers as classical LLMs do. The authors use the core component of SNNs, i.e. temporal processing, to counter outliers and to compute channels with potential outliers in higher precision through longer simulation time. It is worth pointing out that using higher precision for such channels has been prominently studied in the literature (e.g. [3]), and saliency-driven calibration has been studied for quantized LLM (e.g. in [4]). Also ANN-SNN conversion based on integrate-and-fire neurons that model increased precision by conducting multiple steps was presented in prior works (e.g. [5], [6]). The core contribution of this paper is therefore the combination of these concepts to demonstrate > 7B parameter LLM quantization by handling outliers with increased simulation time budgets for certain channels. The paper therefore allows the comparison of rate-coded spiking neural networks against classical quantization methods in the large scale domain of LLMs.

1. [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models](https://arxiv.org/abs/2211.10438)
2. [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://arxiv.org/abs/2308.13137)
3. [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/abs/2208.07339)
4. [SliM-LLM: Salience-Driven Mixed-Precision Quantization for Large Language Models](https://arxiv.org/abs/2405.14917)
5. [SpikeLM: Towards General Spike-Driven Language Modeling via Elastic Bi-Spiking Mechanisms](https://arxiv.org/abs/2406.03287)
6. [SpikeZIP-TF: Conversion is All You Need for Transformer-based SNN](https://arxiv.org/abs/2406.03470)

### Weaknesses
The fields of ANN-SNN conversion and LLM quantization are quickly moving. It is hence important to keep track of the recent developments in these fields. A weakness of this paper is that it is missing comparisons against some closely related recent papers.

[1. SpikeZIP-TF: Conversion is All You Need for Transformer-based SNN](https://arxiv.org/abs/2406.03470)
Related work that uses integrate-and-fire neurons to implement low-bit quantization in transformers. Arguably this work does not work with as large models as the present paper.

[2. SliM-LLM: Salience-Driven Mixed-Precision Quantization for Large Language Models](https://arxiv.org/abs/2405.14917)
Improves over OmniQuant with saliency based metrics, similar to the ones proposed here. The reviewer is missing a comparison in tables 3 and 4.

[3. QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs](https://arxiv.org/abs/2404.00456)
Shows that outliers can mostly be eliminated by mathematically equivalent parameterizations of LLMs (through appropriate weight matrix rotations). This work challenges some key claims made by the presented paper. E.g. line 370 claims "necessity to introduce SpikeLLM due to the inefficiency and incompatibility [...] of existing ANNs based quantisation strategies to spike neural networks". If outliers can be eliminated in LLMs, it seems likely that basic ANN-SNN conversion methods such as SpikeZIP would work in low precision even for larger LLMs.

### Questions
- Is it feasible to compute the Hessian for such large models? Are any approximations used to get the saliency from the Hessian?
- A related work paragraph on ANN-SNN conversion in the context of transformer based models would add value to the paper
- The reviewer suggests to reconsider the use of the term "auto-regressive" as a synonym for recurrent, recursive or sequential. Auto-regression is a particular processing paradigm for sequences that aim to regress themselves, and is usually not interchangeably used with terms like recurrent or recursive. 
- The reviewer suggests to reconsider the claims on "necessity for introducing SpikeLLM" e.g. in lines 25, 110, 120, 370 in face of works like QuaRot that show that one get's away with simply rotating the weights.
- It seems like the character "\~" is out of place between 7B~70B in multiple places. Perhaps use `\sim` instead
- Please incorporate QuaRot and SliM-LLM in both the related work and the comparision

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
This paper proposes the first large-scale spiking large language model that can scale the spiking neuron dynamics to handle models with 7 billion to 70 billion parameters. It has the potential to address the energy and computational resource limitations typically associated with running large language models. The main contributions proposed by the authors include:

1. Generalized Integral-Fire (GIF) neurons: This model compresses the spiking length by encoding the pulse train more efficiently. These neurons reduce the spiking length from T bits to T/L*log_2L bits. This novel approach improves coding efficiency while retaining the necessary computational power.

3. Optimal Brain Spiking (OBS) framework:a saliency-based spiking mechanism that dynamically allocates spiking steps based on the importance of channels within the network. Channels that are considered more important receive more spike steps to capture information, while less important channels receive fewer steps. This saliency-based approach enables more efficient quantization and information encoding, further improving energy efficiency.

4. Compatibility with modern hardware: SpikeLLM's GIF neurons and OBS framework can be deployed using both general matrix multiplication (GEMM) of traditional GPUs and event-driven neuromorphic chip architectures. This increases the feasibility of this method for deployment on neuromorphic hardware.

5. Experimental results: Through various benchmarks, SpikeLLM has significantly improved both performance and energy efficiency over traditional quantization methods used in LLM, such as OmniQuant and GPTQ pipelines. For example, it reduces the perplexity on WikiText2 by 24.85% and improves the common sense reasoning accuracy by 2.01% compared to the LLAMA2-7B model with standard quantization.

### Strengths
1. This paper attempts to solve the energy efficiency problem of LLM through SNN. This is a widely concerned issue. The author proposed several SNN based methods to solve the problems faced in traditional model quantization. The research problem is important and attractive, and the methods and experiments are of practical significance.

2.The author proposed three core methods: GLIF, SALIENCY-AWARE SPIKING STEPS (SASS), and OPTIMAL BRAIN SPIKING (OBP). The logic is clear and easy to follow:
-GLIF tries to encode more information in a single spike time step by merging L spiking steps
-SASS distinguishes the importance of different channels and assigns different quantization levels to different channels to balance the computational load and performance
-OBS determines the importance of any weights and activations through gradient methods.

3.According to the author's experiments, the proposed pipeline works well and outperforms the quantized ANN of the same level in terms of energy efficiency and performance. The authors conducted extensive testing on both the diversity of experimental datasets and model sizes.

### Weaknesses
1.Please explain/correct Eq3, it seems confusing to me.
2.In eq5, please fix the summation over t
3.Fig4(a) missing baseline label

My main concerns are about the computational complexity of the proposed method. The authors did not elaborate in detail in the article on the computational cost of the proposed GLIF, SASS, and OPTIMAL BRAIN SPIKING. Specifically:

4. For GLIF, In eq5, merging IF neurons of multiple steps into one step does reduce the requirement for SNN running time, but increases the computational cost of a single neuron; on the other hand, the implementation of neuromorphic hardware with multiple quantization levels is also unclear. Therefore, it is not sufficient to measure only auto-regressive steps here. Please provide a more detailed demonstration of the advantages of the proposed method.

5. For SASS and OBP,  Does the saliency calculation need to be performed both during training and inference? What is the additional computational cost? How can KV-caches be combined with the proposed method to further reduce the amount of computation? According to my understanding, eq10 only needs to be calculated once, but eq7 and 9 must be performed during inference. (point out if I am wrong) Please  elaborate on the additional computational cost.

Experiment result:

6. In table4, Most of the experimental results for 70b models are missing. The authors suggest that GQA makes training unstable. It would be good to have a more detailed analysis showing the key reasons and potential research directions here. In other words: how scalable is the approach proposed by the authors? What specific issues need to be addressed for stable scaling to 70b or larger models?

7. In table3, Although the proposed method is better than the traditional quantization method, the performance gap with the original model is still more than 10%, which limits the practicality of the method. The author proposed in Limitations: Continuous pretraining would boost the performance. What are the limits of both ann quantization and spiking llm boost? What is the performance difference with sufficient training time?

### Questions
See weakness. Listed below:
1.Please explain/correct Eq3, it seems confusing to me.
2.In eq5, please fix the summation over t
3.Fig4(a) missing baseline label
4.Please provide a more detailed demonstration of the advantages of the proposed method.
5.For SASS and OBP,  Does the saliency calculation need to be performed both during training and inference? etc
6.how scalable is the approach proposed by the authors? etc
7.What are the limits of both ann quantization and spiking llm boost? etc

### Soundness
3

### Presentation
3

### Contribution
3
