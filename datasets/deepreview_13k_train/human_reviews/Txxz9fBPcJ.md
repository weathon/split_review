# Can LLMs Enhance Performance Prediction for Deep Learning Models?

- Decision: Reject
- Scores: 6, 8, 5, 5, 6

## Abstract
Accurate performance prediction of Deep Learning (DL) models is essential for efficient resource allocation and optimizations in various stages of the DL system stack. While existing approaches can achieve high prediction accuracy, they lack ability to quickly adapt to new hardware environments or emerging workloads. 
This paper leverages both Graph Neural Networks (GNNs) and Large Language Models (LLMs) to enhance the accuracy and adaptability of DL performance prediction. Our intuition is that GNNs are adept at capturing the structural information of DL models, naturally represented as graphs, while LLMs provide generalization and the ability to quickly adapt to various tasks thanks to extensive pre-training data.
We empirically demonstrate that using GNN-derived graph embeddings as inputs to an LLM outperforms traditional representations, including high-level text summary and lossless semi-structured text (e.g., JSON), for this task. Furthermore, we propose a structured pre-training strategy to enable model adaptation to new hardware environments, significantly reducing the need for extensive retraining. Our experiments validate the effectiveness of this approach, showing an 8.8 percentage-point improvement in accuracy over a state-of-the-art GNN baseline. Notably, when adapted to new hardware with few samples, our method achieves a remarkable 30--70 percentage-point increase in accuracy compared to the GNN baseline.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work combines GNN and LLM for predicting the performance of a DL model in a certain hardware environment. It first verifies that using graph embeddings serve as effective input tokens for an LLM for performance prediction. A GNN foundation model is further proposed to avoid retraining. A specialized dataset verifies that GNN + LLM achieves higher accuracy and better efficiency than pure text-based methods.

### Strengths
- The paper is well-organized and easy-to-follow.

- The proposed method does not require retraining for a new model or a new hardware environment.

- A new dataset is brought about.

- Experimental results support that the proposed method achieves better advantages.

### Weaknesses
This work follows Perozzi et al. (2024)'s finding. What's the technical differences between the two works? Without such a comparison, it is hard to judge the technical novelty of the second contribution (line 108-109), which is the key contribution in my opinion.

### Questions
Will the code and dataset be released?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a deep learning-based system for predicting the performance of deep learning models. It combines a GNN encoder for producing a representation of the model's computational graph with an LLN which incorporates hardware details and the like. To adapt to novel hardware architectures and/or models, fine-tuning is employed. A comprehensive series of experiments demonstrates that this approach outperforms competing approaches and can transfer well with limited data.

### Strengths
1. The paper presents a novel approach to performance modeling for deep learning which outperforms existing approaches.
2. Improved performance modeling is highly impactful for many parties trying to decide whether to invest in new hardware, or budget for model deployment.
3. A comprehensive set of experiments demonstrates the benefit of the approach.
4. The paper is clear and well-written.

### Weaknesses
1. The dataset considered for evaluation (NNLQP) focuses exclusively on vision tasks, and almost all models considered are CNNs (there is one study which shows good results for low-data transfer to ViTs). The paper would be stronger if it considered models from additional modalities, most notably transformers on text tasks. Specifically, the lack of evaluation on sequence-based models like LSTMs or BERT variants limits the generalizability of the findings. The performance characteristics of these models, with their recurrent or attention-based architectures, can differ significantly from CNNs, and it's unclear if the proposed approach can accurately capture these differences.
2. Likewise, the hardware considered does not include recent GPU architectures, e.g., H100 GPUs, and is mostly focused on dedicated inference devices. While this is valuable to include, it neglects server-class GPUs which are probably more widely deployed, and which have very different hardware characteristics. The absence of server-class GPUs, which often have different memory hierarchies and compute capabilities, makes it difficult to assess the model's performance in more common deployment scenarios. Furthermore, the paper does not address the impact of different memory bandwidths and cache sizes on performance prediction.
3. Many models these days require multiple GPUs even for inference. It is not clear how the approach handles this situation. The paper does not discuss how the GNN encoder and LLN would adapt to model parallelism or data parallelism across multiple GPUs. The communication overhead between GPUs, which can significantly impact performance, is also not considered. This is a critical omission, as multi-GPU setups are increasingly common for large models.

### Questions
Please see comments/questions under weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel approach that combines Graph Neural Networks (GNNs) and Large Language Models (LLMs) to predict the inference latency of deep learning (DL) models. DL models are first converted into graphs with feature matrices via the Open Neural Network Exchange (ONNX) format. These graphs are then processed by a GNN to generate graph embeddings, which are concatenated with token embeddings from the LLM. The authors propose a three-stage training pipeline: (1) GNN pre-training, where the GNN is trained using Graph Masked Auto Encoder techniques; (2) Graph-Text Adaptation, which aligns the GNN's graph embeddings with the LLM’s text embeddings using a projection layer and LoRA (Low-Rank Adaptation); and (3) Performance Prediction Fine-Tuning, which simultaneously trains both models. The results indicate that this multi-modal approach achieves lower Mean Absolute Percentage Error (MAPE) and higher accuracy compared to baseline methods and adapts well to new DL architectures and hardware configurations with limited training data.

### Strengths
-	The paper's method, which utilizes GNN embeddings as inputs for LLMs, is novel for performance prediction tasks. Unlike previous works, this approach combines GNN and LLM in a structured, multi-stage training pipeline to optimize both models for this task, showing high adaptability to new architectures and hardware.

-	The proposed method shows considerable improvement in performance prediction metrics (e.g., MAPE, accuracy) compared to baselines, demonstrating strong potential for adaptability to new hardware configurations and DL architectures with limited training samples.

- The presentation of the paper and explanation of the method is very clear. Although the method consists of several stages and different modules, the writing makes it easy to understand how each module is integrated in the training pipeline. 



- The authors propose a new training pipeline that can effectively optimize two different neural networks, GNN and LLM, to the task of performance prediction. Empirical results show that the resulting model has high adaptability to new hardware configurations or DL graphs given only a small set of training data.

### Weaknesses
-	In Table 3, the proposed method is compared against a single GNN baseline, which is insufficient to assess the enhancement from the method. The authors should add existing works such as [1] and [2] to their experiments for fair comparison with SOTA methods.

-	While this work demonstrates the feasibility of using GNN and LLM together to predict the performance of DL models, it lacks a thorough discussion on the specific challenges and characteristics that make this problem difficult to address using LLMs. In many fields, the effectiveness of LLMs is well established, and multi-modal language models are widely used. To strengthen the contribution of this paper, an analysis of why this problem requires an LLM-based approach and how it can be effectively addressed should be included.

-	the baseline accuracy of 51.72% reported in Table 3 is questionable, as it is significantly lower than the accuracy reported in the original paper (Average of Acc(10%): 59.73% in the original paper). Additional discussion on why the baseline shows lower accuracy compared to the original paper is needed.

-	The “Justification for the Proposed Architecture” section 4.2 is difficult to understand and confusing. Are the authors suddenly presenting justification for using LLMs by showing suboptimality of their early designs that use smaller LMs? Or are they presented as enhanced baselines which simply integrate language models to the GNN baseline?

### Questions
-	How do other baselines (e.g., [1], [2]) perform with the evaluation suite you used?

-	What are the specific challenges of using LLMs to predict the performance of DL models? There are already several works that use GNN and LLM together to encode the graph and make it understandable for LLMs [3], [4]. 

-	Why is the Acc(10%) of the GNN baseline much lower than the figure reported in the original paper?

[3] Bahare Fatemi, Jonathan Halcrow, Bryan Perozzi (2024), “Talk like a Graph: Encoding Graphs for Large Language Models”, The Twelfth International Conference on Learning Representations (ICLR 2024)

[4] Bryan Perozzi, Bahare Fatemi, Dustin Zelle, Anton Tsitsulin, Mehran Kazemi, Rami Al-Rfou, Jonathan Halcrow (2024), “Let Your Graph Do the Talking: Encoding Structured Data for LLMs”, https://arxiv.org/abs/2402.05862

### Soundness
2

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
5

### Summary
The paper proposes to use both graph neural networks (GNNs) and Large Language Models (LLMs) for a more accurate and generalizable performance prediction framework for deep learning models. The proposed method leverages a GNN-based encoder to generate graph tokens as inputs to the language model and achieves notable improvements against GNN-only or LLM-only baselines.

### Strengths
The proposed method, compared to baselines, takes network structure into consideration to achieve a better prediction accuracy while also maintaining a manageable computational cost.

### Weaknesses
- The LLM-based baselines provided in Table 1 all have very obvious drawbacks and therefore are not strong enough to serve as main baselines to illustrate the novelty of the proposed methods. The 'text' method does not include a network structure at all, which naturally leads to bad performance. The 'JSON' method uses a huge input in the LLM with possibly redundant information that significantly increases the training runtime and harms the accuracy.
- The breakdown results for different model architectures are missing.
- There seem to be different results reported in Table 6 of the original NNLQP paper, which reports a 79.51% accuracy.

### Questions
1. Can you provide a stronger LLM-only baseline? E.g., instead of using direct JSON input which can contain useless information, a more compact text-based and structured information can be passed to the LLM. 
2. What are the 'hardware details' in the prompt?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a new method that combines Graph Neural Networks (GNNs) and Large Language Models (LLMs) to predict the performance of deep learning models. GNNs can help capture the structural information in the model architectures, while LLM can help enhance the generalization and adaptation ability of the prediction model. To seamlessly combine them two, the proposed method pre-trains the GNN first and then uses two different stages to fine-tune the combined model. For the two-stage fine-tuning, the graph-text adaptation stage uses the text-adaption dataset to tune the LLM and the projection layer between GNN and LLM, and the performance prediction finetuning stage uses a multi-platform dataset to tune the whole model, including the GNN and LLM. Both of the two stages use LoRA and soft prompting methods for efficient model training. As a result, the proposed method can achieve better prediction accuracy than the previous GNN-based methods, especially for the adaptation to new hardware with few samples.

### Strengths
- This paper is well-written and easy to follow.
- This paper introduces a novel method that combines a GNN and an LLM for performance prediction tasks. It can help inspire many other GNN+LLM researches on those structured data.
- The evaluation clearly shows the effectiveness of the proposed method.

### Weaknesses
 - Although the total training time can be greatly reduced, the inference time will increase due to the computation of LLM. There will be a new inference performance issue when applying this method to the DL system stack. There is no discussion about the inference time.
- The proposed method heavily depends on multi-stage training, which must pre-train GNN and LLM first and then use two separate fine-tuning stages to finish the training. Each step needs a careful design for the training.

- Question about the results in Table 8. It seems that the GNN baseline can perform better on all of the fp32 platforms, and this result is contrary to the conclusion in the experiments section. But there is no discussion and any result about fp32 in the main body. It is better to have an explanation.

### Questions
Question about the results in Table 8. It seems that the GNN baseline can perform better on all of the fp32 platforms, and this result is contrary to the conclusion in the experiments section. But there is no discussion and any result about fp32 in the main body. It is better to have an explanation.

### Soundness
3

### Presentation
4

### Contribution
3
