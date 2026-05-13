# MatMamba: A Matryoshka State Space Model

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
State Space Models (SSMs) like Mamba2 are a promising alternative to Transformers, with faster theoretical training and inference times -- especially for long context lengths. Recent work on Matryoshka Representation Learning -- and its application to Transformer backbones in works like MatFormer --  showed how to introduce nested granularities of smaller submodels in one universal elastic model. In this work, we present MatMamba: a state space model which combines Matryoshka-style learning with Mamba2, by modifying the block to contain nested dimensions to enable joint training and adaptive inference. MatMamba allows for efficient and adaptive deployment across various model sizes. We train a single large MatMamba model and are able to get a number of smaller nested models for free -- while maintaining or improving upon the performance of a baseline smaller model trained from scratch. We train language and image models at a variety of parameter sizes from 35M to 1.4B. Our results on ImageNet and FineWeb show that MatMamba models scale comparably to Transformers, while having more efficient inference characteristics. This makes MatMamba a practically viable option for deploying large-scale models in an elastic way based on the available inference compute

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work extends Matryoshka Representation Learning to Mamba2, a representative architecture for state-space models, proposing MatMamba. MatMamba introduces a training pipeline that generates numerous sub-models, each offering different performance-efficiency trade-offs, within a single training run. The authors analyze the effectiveness and scalability of the proposed method.

### Strengths
- This work validates the scalability of Matryoshka Representation Learning by demonstrating its applicability to state-space models (SSMs). It considers both Mamba-vision and Mamba-language models, confirming effectiveness across both tasks. 
- The methodology and problem setting are well-established and well-motivated.

### Weaknesses
- For the MatMamba-LM model family, only evaluation loss is reported. The submission would be strengthened by including evaluations on downstream tasks as well.

### Questions
- What is the main difference you observed between elastic inference on Matformer and MatMamba during the experiment? Since MatMamba essentially follows the approach used in Matformer, I'm curious if any unique challenges were encountered specific to the Mamba architecture.

### Soundness
4

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
3

### Summary
This paper introduces MatMamba, a novel approach to State Space Models (SSMs) that combines Mamba model with Matryoshka-style learning. The proposed model embeds nested sub-models within a single super-architecture, allowing for dynamic inference across different granularities without the need for separate training. This setup facilitates scalable and efficient deployment in both vision and language models by dynamically adjusting model sizes based on compute availability. Through extensive testing on tasks such as image classification and language modeling, MatMamba demonstrates comparable or superior performance to baseline Mamba2 models while maintaining flexibility and efficiency.

### Strengths
(1) Adaptive Inference Resource: MatMamba allows the extraction of multiple nested submodels from one single model, enabling versatile deployment options, from edge devices to cloud settings, without the need for retraining. By using the Mix’n’Match approach, MatMamba optimizes for various performance-compute trade-offs, allowing resource allocation adjustments based on current needs.
(2) Scalability and Performance: The model exhibits scalability on par with transformers and baseline Mamba2 models in both image and language tasks. The author provides multiple model sizes ranging from 30M parameters to 1.4B parameters, which demonstrates scalability.
(3) The nested structure maintains a consistent metric space, ensuring that different granularities yield compatible outputs, which is beneficial for downstream applications like retrieval.

### Weaknesses
(1) Dependency on Explicitly Trained Granularities for Optimal Performance: While MatMamba’s Mix’n’Match approach offers flexibility, untrained granularities do not perform as effectively as explicitly optimized ones, showing degradation in performance and accuracy.
(2) Limited Exploration of Self-Distillation Techniques: The paper mentions that self-distillation or other techniques could further enhance interpolation accuracy in untrained granularities, suggesting room for improvement in the training setup.
(3) Limited Evaluation on Language Tasks: The author trained a large model up to 1.4B parameters, but did not conduct more experiments on text-generation benchmarks used to evaluate LLMs. I reckon that it would be better if the author could run the proposed MatMamba through datasets like MMLU, HellaSwag, GSM8K, ARC and etc.

### Questions
See the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents MatMamba, which introduces a nested Matryoshka structure on a Mamba2 state space model. The resulting elastic network architecture can be used to generate multiple smaller sub-networks at deployment time without any additional training, similar to prior work in this area such as Matformer and Flextron. The training process involves gradient accumulation on 4 subnetworks with a single backward pass for parameter updates. MatMamba is evaluated on vision and language tasks with elastic network sizes ranging from 35M to 1.4B.

### Strengths
* The paper is very well-written, with the main ideas and results presented clearly. It was a pleasure to read.
* Elastic networks have shown significant promise for Transformer networks, since they can be used to generate tailored networks for specific deployment scenarios at no additional training cost (once elastic training is complete). The paper makes a contribution in this relevant and promising direction.
* Evaluation and results across vision and language looks strong overall.

### Weaknesses
* There doesn’t seem to be a systematic way of selecting smaller sub-networks given a deployment constraint. For a given parameter or latency budget, should all dimensions be proportionally reduced? How is this proportion decided?
* Novelty: this work appears to be a straightforward application of Matryoshka principles to the SSM domain; apart from the obvious changes needed for SSMs, the training algorithm remains nearly identical to the Matformer work.
* It’s not clear if the scaling trends continue beyond the ~1.5B parameter mark. Do the authors have any insights here? I understand that training larger networks can be quite resource-intensive, but at least a discussion on expected scaling trends would be useful.
* I don’t agree with the claim made on line 456. Downstream task performance must be reported for MatMamba-LM using a standard framework like LM-Eval-Harness. While validation loss is a good starting point, performance on a variety of downstream tasks can provide a more complete picture of LLM performance (which is why most work dealing with LLMs reports these numbers).

### Questions
* Why is g set to 4? Have you explored other values? How does the method scale when g is lower/higher?
* How is MatMamba's long context performance? SSM-based architectures can perform poorly on long-context tasks, and I’d be curious to see if MatMamba maintains this trend, or perhaps improves it. MatMamba’s superior performance at higher resolutions in the vision domain provide somewhat of an indication here.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents MatMamba the application of Matryoshka techniques (Kusupati 2022) to models based on the Mamba2 architecture.
The authors apply the Matroyshka technique to most layers, leading to a close-to linear downscaling capability. 
They can show that jointly learning one model at four granularities matches the performance of models trained at the single scales.
For vision experiments, the Mix'n'Match technique using layer dimensionalities in between granularities matches/surpasses an interpolated 
performance, whereas in Language Modeling there is a degradation using this technique. The presented technique binds representations at 
different model scales, making potential for e.g. more efficient speculative decoding techniques.

### Strengths
The authors show that Matryoshka-style model tying/training can be applied to Linear Transformers/Matrix SSMs/Fast-Weight Programmers.
They show results on how the Mix'n'Match interpolation degrades performance across modalities.

### Weaknesses
It is a combination of existing techniques.

### Questions
Can you give a citation / relevant prior work for the claim in L.456f ?
There is a typo in L.522.
Do you think that the different Mix'n'Match behavior for language and image modeling is intrinsic to the modality or might be specific to MatMamba?

### Soundness
3

### Presentation
3

### Contribution
2
