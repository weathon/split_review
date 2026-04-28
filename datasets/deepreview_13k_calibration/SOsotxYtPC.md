# LoGra-Med: Long-Context Multi-Graph Alignment for Medical Visual-Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
\vspace{-0.1in}
State-of-the-art medical multi-modal large language models (med-MLLM), such as \textsc{LLaVA-Med} or \textsc{BioMedGPT}, leverage instruction-following data in their pre-training stages.
However, those models primarily focus on scaling the \textit{model size} and \textit{data volume} to boost performance while mainly relying on the autoregressive learning objectives. Surprisingly, we reveal that such learning schemes might result in a weak alignment between vision and language modalities, making these models highly reliant on extensive pre-training datasets — a significant challenge in medical domains due to the expensive and time-consuming nature of curating high-quality instruction-following instances.
We address this challenge with a new multi-graph alignment algorithm, namely \textsc{LoGra-Med}, which enforces triplet correlations on the latent embedding space among image modalities, conversation-based descriptions, and extended contextual captions. Owing to this technique, the model is encouraged to capture the semantic meaning of the context, handle linguistic variability where the captions or questions may differ from training instances, and learn cross-modal associations, linking visual elements with various textual interpretations.
To scale our algorithm to the med-MLLM setting, we also design an efficient end-to-end learning scheme based on advanced black-box gradient-estimation techniques that permit fast forward and backward steps through the LLM model (LLaMa 7B). Empirical results show that we can match the performance of LLAVA-Med pre-trained on 600K image-text pairs from PMC-15M for Medical VQA tasks and significantly outperform it when trained on only $10\%$ of the data. For instance, on VQA-RAD, we exceed LLAVA-Med (both trained on $10\%$) by $20.13\%$ and achieve near parity with the $100\%$ pre-training setting ($72.52\%$ vs. $72.64\%$).
Additionally, we also surpass other SOTA pre-training methods and med-MLLM such as \textsc{BiomedGPT} on \textit{visual chatbot} or \textsc{RadFM} on \textit{zero-shot image classification with VQA}, showcasing the power of multi-graph alignment in improving vision-language integration for medical-MLLM.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a multi-graph matching objective to enhance the vision-language alignment in generative VLMs for medical tasks. The authors motivate the need for such an auxiliary learning objective from a training efficiency point of view, showing that the next token prediction loss function demands a large amount of visual instruction tuning data that's not easy to acquire. To reduce the sample complexity, this paper proposed their method of treating visual features, text features, and augmented text features (based on a more verbose version of the ground truth answer) as graphs and letting the VLM learn to match between the triplets. Since solving a multi-domain graph alignment problem is computationally expensive, the authors propose a more scalable solution by separately aligning each domains with a barycenter graph. The experiments in the paper show that multi-graph alignment significantly improves upon LlaVA-Med, at both low pretraining data (10%) and full data regimes across a wide range of tasks.

### Strengths
I like how the paper motivates the necessity of the proposed algorithm from the perspective of training efficiency, which is quite refreshing. The experiments also validate that the proposed algorithm indeed results in better learning outcomes at low data regimes and even does so when using all the pretraining data. 

The presentation of the core methodology flows very well, with tight logical connections. The gradient-based method to by-pass the high time complexity of the solver also seems reasonable.

The paper also seems to be quite comprehensive in terms of baselines. The ablation studies are satisfactory, especially the one without “long-context”.

The experiment details in the supplemental material is very comprehensive, including important details such as system prompt and evaluation protocols.

### Weaknesses
I have concerns regarding the core methodology.

1. The paper seems to have skipped simpler solutions that might as well worked and jumped right into a complex proposal. In section 3.4, the authors argue the necessity of their scalable multi-graph alignment algorithm by saying pairwise graph alignment requires K choose 2 pairs. But in this specific case, K is 3 and K choose 2 is really only 3 pairs. From my point of view, this really should be the method to be tried first before moving on to more complex formulations. 
2. I am too sure what leads to LoGRA’s success due to how the visual & text representations are obtained. In its essence, the representations from both modalities are sets with varying number of elements. For images, this will be different number of patches due to different resolutions; for text, it’s whatever the number of tokens the ground truth answer corresponds to. The authors are simply taking a naive average over the elements. I really doubt the average of word embeddings / visual tokens will end up giving any meaningful representations. I would like to see some analysis on this design choice, for example comparing the distribution of cosine similarity (for example) between positive and negative pairs, so that I know the proposed objective is really forcing the alignment instead of picking up some other signals. 
3. As far as I know, most medical datasets are highly imbalanced, but the paper seems only to report the overall accuracy instead of per-disease macro scores. This is a bit concerning since if all the alignment algorithm does is to guild the model to favor the majority class, we will get a model with high accuracy but no practical use. I think for classification tasks, macro F1 scores should be reported. For VQA tasks, per-disease scores should be reported for datasets that include a class-label for the image-question-answer pair.
4. I think the word “long-context” is misused: from the examples, it looks like the so called “long-context” texts are no more than a few hundred words. Based on the context of the paper, the authors really meant a more verbose / extended rewrite of the original ground truth answers as an augmentation for the triplet learning. A better terminology should be used to distinguish this paper from works dealing with long-context tasks, which usually consumes at least tens of thousands of tokens for each query.

### Questions
1. I’m actually a bit confused on why the graph perspective is needed here. It seems the paper is solving the exactly the same problem as optimal transport, but all these optimal papers do not talk about graphs? 
2. I wonder, without using the verbose version, how’s this paper different from the PLOT paper, since it’s essentially solving a matching problem between 2 domains?
3. I find counterintuitive that DCI provides mixed results. What’s the explanation here? To be honest, I would be totally fine if those “+DCI” are not there. But if the authors decide to add these experiments, then they need to explain why utilizing multi-scale features are harmful for some cases.

### Soundness
3

### Presentation
3

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
This work propose a method that aiming for decrease the data needed for medical Multi-Modal large langauge model pre-training by enforcing triplet correlations on the latent embedding among image, descriptions, and captions. How to efficiently pre-train large models with limited data in medical domain is a quite important topic, and thus the motivation is good enough. However, the reason behind applying multi-gprah alignment is not well-explained. And this process required retrain the LLM model, which is more costful compared other methods.

### Strengths
1. This model propose a method to convert auto-gressive finetuning to Graph-alignment task, a fresh perspective. This seems interesting but lack of motivation.
2. The results showing that the proposed method is definetly increase the performance on different tasks with limited datasize. This is quite important and might showing a new way except data curation.
3. Some of the detail are not well-explained in the paper, please refer to the weakness and quesiton section. I will consider adjust my scores based on the authors response.

### Weaknesses
1. The motivation of adding graph alignment task in the pre-training stage is not explained.
2. This paper also cite the work of MedTrinity(Xie et al.2024), but you didn't include their results in your comparison tables for your experiments. Their model's performance on some dataset are better than yours, you should include them to give readers a fair comparision. You may argue that their training data is larger than yours. But your method also introduce augmented description data generated by GPT-4.
3. SInce you introduced more data by extending the short answer to long answers. So, when you finetuning the LLavaMed basedline with 10% data, do you also include the extended version answer?
4. The core novelty of this work is questionable. It appears to be a direct extension of prior work that uses a combinatorial method for contrastive learning by employing two transformations of the same image to form two graphs. The main difference here is applying two transformations to the text prompts (short and long text) to form two graphs. This incremental change lacks significant innovation.

### Questions
1. Why extending the short answer to longer-context, why would that beneficial the pre-training? 
2. Have you run any qualification test on the GPT generated text?
3. Would you mind to clarify, when you mentioned "10% data", you mean, "10% datasize for the stage2 instruction-tuning stage, but the datasize for the stage1 pre-trianing is still fullzie". Is that correct?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors introduced a self-supervised multi-graph alignment objective strategy for pre-training medical MLLM. Specifically, the proposed method aligns the triplet consisting of the input image, its instruction data, and its extended long context generated by GPT. The graphs of images, the instruction data, and the long context are trained to align with the barycenter graph. The authors perform experiments on multiple downstream tasks, and the proposed method outperforms baseline methods. The proposed method achieved better performance with the limited amount of pre-training dataset.

### Strengths
1. The empirical results demonstrate that the proposed approach can reduce the demand for pre-training data for MLLM alignment, outperforming previous approaches.

2. The authors conducted a set of ablation studies, which demonstrated the contribution of each component.

3. The visualization in the manuscripts helped me to better understand the proposed approach and experiments.

### Weaknesses
1. From Table 5, it seems that the generated long context data plays an important role in LoGra-Med. Without it, the performance is slightly lower than the baseline LLaVA-Med. Since LLaVA-Med doesn't use the generated long context data, these results cast doubt on the contribution of the graph alignment algorithm. For a fair comparison to validate that the performance gain is not mainly due to the extra data, the author could also pre-train LLaVA-Med with the long context data and compare the performance.

2. The proposed method's performance gain may come from the extra computing in training (the authors mention that the training time is longer than the baseline method by 1 hour) rather than the method itself. For a fair comparison, the authors may pre-train the LLaVA-Med baseline method using some self-supervised objectives (e.g., InfoNCE) or additional long context data for 1 hour.

3. The authors need to mention some of the important hyperparameters used. For example, what's the batch size B? I would assume the larger the batch size, the larger the graph. And what's the value of k used in the k-NN algorithm for building edges? Furthermore, details on how the graph is constructed are missing. For instance, how are the node features determined for each modality (image, instruction, long context)? Are they directly from the embeddings of the MLLM, or are there additional processing steps? The lack of clarity on these aspects makes it difficult to reproduce the results and fully understand the contribution of the graph alignment.

### Questions
1. Can you provide the hyperparameters used in the paper, including the batch size B and the value of k used in the k-NN?

2. Are there any experiment results presented in the paper that can prove the performance gain compared to LLaVA-Med is due to the graph alignment algorithm itself rather than additional data or extra computing?

### Soundness
3

### Presentation
3

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
This paper introduces LOGRA-MED, a novel approach addressing the data efficiency challenge in medical multi-modal large language models (med-MLLM) through multi-graph alignment. The work reveals that current autoregressive training methods like LLAVA-Med require extensive instruction-following data, showing a significant performance drop from 72.64% to 52.39% on VQA-RAD when reducing training data to 10%. To address this, LOGRA-MED enforces triplet correlations in the latent space among image features, instruction data, and GPT-4 generated extended contextual captions using a structure-aware graph matching framework. The method efficiently handles the combinatorial complexity of multi-graph alignment through an implicit maximum likelihood estimation approach with black-box gradient computation.

### Strengths
The technical innovation of LOGRA-MED lies in its formulation of vision-language alignment as a multi-graph matching problem, generalizing beyond traditional pairwise contrastive learning approaches. The theoretical foundation is particularly strong, proving both metric and geodesic properties of the graph alignment distance. The implementation cleverly circumvents the NP-hard nature of multi-graph matching using Lagrange decomposition and efficient heuristic solvers. The empirical results are comprehensive, demonstrating that with only 10% of training data, LOGRA-MED achieves 72.52% accuracy on VQA-RAD, nearly matching LLAVA-Med's 72.64% with full data. The method's effectiveness extends across various tasks including medical visual chatbot capabilities (44.82% overall score) and zero-shot classification on 23 datasets spanning microscopy, CT, and CXR modalities.

### Weaknesses
The reliance on GPT-4 for generating extended contexts raises questions about potential biases and the method's generalizability. While the paper demonstrates improved performance, the computational complexity analysis could be more thorough - the reported one-hour additional training time compared to LLAVA-Med merits deeper discussion given the sophisticated graph matching operations. The variable performance across different medical domains (particularly in PathVQA and some zero-shot classification tasks) suggests potential limitations in handling diverse medical contexts. The ablation studies, while informative, could benefit from exploring different graph construction strategies beyond k-nearest neighbors and analyzing the impact of various distance metrics in the graph matching formulation.

### Questions
The sensitivity of LOGRA-MED to the quality and consistency of GPT-4 generated contexts remains unclear？ 

how would the method perform with simpler context extension approaches or with different language models? 

The paper could elaborate on the interplay between the traditional autoregressive loss and the graph alignment objective, particularly regarding their relative contributions to the final performance？

The choice of hyperparameters in the graph construction phase, especially the selection of k in k-nearest neighbors, appears critical but lacks detailed justification？

### Soundness
3

### Presentation
2

### Contribution
2
