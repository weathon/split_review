# AERO: Softmax-Only LLMs for Efficient Private Inference

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The pervasiveness of proprietary language models has raised privacy concerns for users' sensitive data, emphasizing the need for private inference (PI), where inference is performed directly on encrypted inputs. However, current PI methods face prohibitively higher communication and latency overheads,  primarily due to nonlinear operations. In this paper, we present a comprehensive analysis to understand the role of nonlinearities in transformer-based decoder-only language models.  We introduce AERO, a four-step architectural optimization framework that refines the existing LLM architecture for efficient PI by systematically removing nonlinearities such as LayerNorm and GELU and reducing FLOPs counts. For the {\em first time}, we propose a Softmax-only architecture with significantly fewer FLOPs tailored for efficient PI.  Furthermore, we devise a novel entropy regularization technique to improve the performance of Softmax-only models. AERO achieves up to 4.23$\times$ communication and 1.94$\times$ latency reduction. We validate the effectiveness of AERO by benchmarking it against the state-of-the-art.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents an optimization framework to make large language models more efficient for private inference by minimizing non-linear operations such as LayerNorm and GELU. The proposed architecture, AERO, includes a Softmax-only model that reduces both communication and latency overheads. A novel entropy regularization technique is introduced to prevent training instabilities and entropic overload in the model.

### Strengths
1. This paper highlights an important research area—private inference (PI)—and extends the study of PI for LLMs by providing valuable insights into the impact of LayerNorm, a topic that has not been extensively explored before.

2. The insights into entropic overload and the proposed solution, entropy regularization, are both novel contributions.

### Weaknesses
1. Replacing GeLU with ReLU has been proposed in the work [1]. Despite this paper proposes insightful analysis, this method is not totally novel.
[1] Dake Chen, Yuke Zhang, Souvik Kundu, Chenghao Li, and Peter A Beerel. Rna-vit: Reduceddimension approximate normalized attention vision transformers for latency efficient private inference. In IEEE/ACM International Conference on Computer Aided Design (ICCAD), 2023.

2. Although AERO achieves notable reductions in communication overhead and latency, there is a trade-off in terms of higher perplexity compared to baseline models. As Iron [2] provides efficient private inference protocols for layernorm, I would suggest the authors to compare the PPL and PI savings with Iron.

[2] Meng Hao, Hongwei Li, Hanxiao Chen, Pengzhi Xing, Guowen Xu, and Tianwei Zhang. "Iron: Private inference on transformers." Advances in neural information processing systems 35 (2022): 15718-15731.

3. The acronym FFN is first introduced in line 70, but its full name, Feed-Forward Network, does not appear until line 108. This slight inconsistency in placement could lead to some confusion for readers.

### Questions
The proposed AERO framework and experiments primarily focus on models with fewer than 1B parameters, limiting the insights into its performance and scalability on larger LLMs commonly used in industry. This might restrict the applicability of the findings to more demanding real-world scenarios. What are the authors' perspective on how AERO might perform with larger models and whether they anticipate similar benefits or new challenges at a larger scale?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the efficient private inference of LLM and proposes an algorithm using only Softmax nonlinear functions. The problem of privacy inference studied is of practical value. The proposed scheme can greatly reduce the nonlinear operation in LLM and has practical application value.

### Strengths
The proposed scheme can greatly reduce the nonlinear operation in LLM and has practical application value.

### Weaknesses
The introduction does not fully introduce the motivation of the research, and does not elaborate on whether the proposed algorithm can solve the challenges mentioned in the introduction. The experimental results lack more detailed evaluation of test accuracy and other indicators.

### Questions
1. The introduction of the paper emphasizes the importance and challenge of private inference. However, how the proposed AERO addresses these challenges is not fully described. Why reducing nonlinear operations can help LLMS perform private inferences needs to be explained in more detail.

2. How much gain and benefit will the proposed scheme bring to private inference? This requires further objective numerical evaluation.

3. The author describes in the limitation that this work mainly discusses the PPL performance of the model. What is the test performance on the actual NLP task? This needs to be explained in the experimental results section.

4. The content of the appendix is not in good shape, and there is no text introduction under many sub-headings, which makes it difficult for readers to obtain information from them.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the AERO framework, a new method to optimize large language models (LLMs) in resource-constrained contexts, such as private inference (PI), by systematically reducing non-linear operations until Softmax becomes the model’s sole source of non-linearity, thereby enhancing computational efficiency. The main contributions of this work are as follows:

1. In the Softmax-only model, the authors apply weight normalization and scaling techniques to the linear layers within the feed-forward network (FFN), effectively preventing training collapse. This shift from activation normalization to weight normalization avoids non-linear calculations during the inference phase, thereby improving inference efficiency.

2. In the Softmax-only architecture, the authors merge two linear layers in the FFN into a single linear layer, reducing the FFN’s FLOPs by 8x without compromising model performance. Additionally, they prune the deeper FFN layers, further enhancing computational efficiency.

3. To address issues of entropy overload and entropy collapse that are prone to occur during training in the Softmax-only architecture, the authors propose an entropy regularization method. By penalizing extreme entropy values during training, this method ensures a balanced entropy distribution across attention heads, maintaining model stability and performance.

### Strengths
The paper demonstrates a range of strengths in terms of originality, quality, clarity, and significance, as detailed below:

The AERO framework presents a novel approach by systematically reducing non-linear operations until Softmax becomes the model’s sole non-linearity, thereby enhancing computational efficiency. Its originality lies in the combination of several innovative techniques, including the use of weight normalization and scaling instead of traditional activation normalization, merging FFN layers to reduce FLOPs by 8x, and applying entropy regularization to address issues of entropy overload and entropy collapse during training.

The paper employs a rigorous research methodology, conducting experiments across multiple models (such as GPT-2 and Pythia) and various context lengths. Detailed ablation studies demonstrate the effectiveness of each component within the AERO framework, such as weight normalization and entropy regularization. These experimental results enhance the technical reliability of the paper and support its main conclusions.

The paper is well-structured, with clear explanations of its motivations, methods, and experimental results. Complex concepts, such as entropy regularization and the transition from activation normalization to weight normalization, are thoroughly explained, aiding readers in understanding the rationale and benefits behind these technical choices.

By improving the efficiency of LLMs in PI scenarios, the AERO framework addresses a critical issue in deploying LLMs in resource-constrained environments. This approach holds significant value in the field of privacy-preserving machine learning, potentially facilitating broader applications of LLMs in privacy-sensitive or resource-limited settings. The demonstrated reductions in FLOPs, communication costs, and inference latency contribute meaningfully to the field.

### Weaknesses
1. Lack of Detail in Entropy Regularization Implementation:  
   While entropy regularization is an important part of the AERO framework, the paper does not provide sufficient detail on how the regularization thresholds (for addressing entropy overload and entropy collapse) are selected. A clearer explanation or additional experiments testing different threshold values could strengthen the understanding of this technique and its practical application.

2. Limited Comparison with Existing Non-linear Reduction Techniques:  
   The paper primarily focuses on its unique approach but provides limited comparison with other existing methods that aim to reduce non-linear operations in LLMs. Incorporating experiments or discussions comparing AERO with similar frameworks could help highlight its relative strengths and weaknesses, making the contributions clearer.

3. Absence of Optimization with Specific Privacy-Preserving Techniques in Real-world PI Applications:  
   Although the paper demonstrates AERO’s efficiency improvements in terms of FLOPs, communication cost, and inference latency, it lacks evaluations in real-world PI application scenarios, especially in conjunction with specific privacy-preserving techniques, such as multi-party computation or homomorphic encryption. Including benchmarks that evaluate AERO’s performance when combined with these privacy techniques could further showcase the method’s practicality and effectiveness in actual applications.

### Questions
1.Could the authors provide more detail on how the entropy regularization thresholds were selected for addressing entropy overload and entropy collapse? Were these values determined empirically, or was there a specific criterion used? Further insights here would help clarify the robustness of the regularization approach.

2.The paper highlights the novelty of reducing non-linear operations to a Softmax-only model, but could the authors provide additional comparisons with other existing methods beyond LayerNorm-free design? (Are there any more SOTA that aim to achieve similar goals?)  

3.While weight normalization was shown to prevent training collapse, how does it affect the model's generalization ability in different contexts? 

4.Could the authors elaborate on how AERO performs in real-world private inference scenarios, especially when integrated with specific privacy-preserving techniques like homomorphic encryption or multi-party computation?

5. Realizing the limited computational resource and time, the reviewer is still curious about AERO's performance on large models other than GPT-2 and Pythia-70M.

### Soundness
3

### Presentation
4

### Contribution
3
