# Parrot: Multilingual Visual Instruction Tuning

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
The rapid development of Multimodal Large Language Models (MLLMs) like GPT-4V has marked a significant step towards artificial general intelligence. 
  Existing methods mainly focus on aligning vision encoders with LLMs through supervised fine-tuning (SFT) to endow LLMs with multimodal abilities, making MLLMs' inherent ability to react to {\em multiple languages} progressively deteriorate as the training process evolves. 
  We empirically find that the imbalanced SFT datasets, primarily composed of English-centric image-text pairs, lead to significantly reduced performance in non-English languages. This is due to the failure of aligning the vision encoder and LLM with multilingual tokens during the SFT process.
  In this paper, we introduce \mame, a novel method that utilizes textual guidance to drive visual token alignment at the language level. \name makes the visual tokens condition on diverse language inputs and uses Mixture-of-Experts (MoE) to promote the alignment of multilingual tokens. 
  Specifically, to enhance non-English visual tokens alignment, we compute the cross-attention using the initial visual features and textual embeddings, the result of which is then fed into the MoE router to select the most relevant experts. The selected experts subsequently convert the initial visual tokens into language-specific visual tokens.
  Moreover, considering the current lack of benchmarks for evaluating multilingual capabilities within the field, we collect and make available a Massive Multilingual Multimodal Benchmark which includes 6 languages, 15 categories, and 12,000 questions, named as {\bf MMMB}.
  Our method not only demonstrates state-of-the-art performance on multilingual MMBench and MMMB, but also excels across a broad range of multimodal tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims at the multilingual issues in recent MLLMs and proposes a MoE-based alignment layer to this end. First, the authors find that existing MLLMs are not friendly to non-English queries and analyze this from the imbalanced training datasets. A simple solution would be to train a new adapter for each language, but this approach is not feasible due to the limited number of training pairs. This paper thus introduces Parrot, which trains a soft adapter under the MoE framework. To fully test the multilingual ability of MLLMs, this paper also releases a Massive Multilingual Multimodal Benchmark(MMMB). Results on MMMB and MMBench show that Parrot has a better multilingual alignment with limited training data.

### Strengths
1) The problem that improves the multilingual abilities of MLLMs is an open and challenging problem. This paper develops a simple and efficient insight for the community.

2) This idea that uses MoE-based adapter is interesting. It can learn from the limited image-text pairs and show good performance empirically.

3) The collected new benchmark MMMB would be useful for subsequent research.

4) Extensive comparison and ablations show the efficiency of the proposed model.

### Weaknesses
1) Parrot  depends on balanced datasets and does not consider unbalanced situations, which are the most common in practice. That is saying that Parrot may not satisfy the scaling law. When considering massive training pairs, unbalanced cases occur, which could lead to sub-optimal MoE learning, sticking in the same predicament as existing MLLMs.

2) Lack of a strong baseline. I wonder about the performance of a naive baseline where we first translate the question into English and then translate the English answer back to the target language.

### Questions
1) At the first pretraining stage, is the MoE initialized with random parameters? If yes, how can we learn a good Projector under a random MoE?

2) An open question: What is the most real benefit for today's MLLMs? Recent MLLMs can be divided into two groups: 1) dataset-driven, these models adopt simple adaptor to map images into the language space (Qwen-vl, llava, gpt-4o, gemini Pro) and jointly train MLLMs on massive image-text data. 2) tokenization-based models, these models believe a good image tokenization can align the image and text well (Parrot, [1][2]). In my opinion, the simple structure and target datasets fine-tuning may have better robustness and improvement than small structure-based modifications.

[1] https://arxiv.org/abs/2408.05019
[2] https://arxiv.org/pdf/2405.01926

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes Parrot, an MLLM designed to handle multilingual tasks. Parrot follows the LLava architecture, introducing an additional MoE module after the visual projector to enhance multilingual understanding. During training, Parrot translates public datasets into multiple languages and adopts a two-stage training scheme similar to LLava. To assess multilingual capabilities in MLLMs, the paper introduces MMMB (Massive Multilingual Multimodal Benchmark), encompassing 6 languages, 15 categories, and 12,000 questions. Parrot demonstrates strong performance on both MMBench and MMMB.

### Strengths
1. High reusability—the proposed approach is simple and highly portable.
2. Extensive experimentation—the paper validates multilingual capability across multiple benchmarks.
3. Open-sourced multilingual benchmark dataset (MMMB) to support multilingual evaluation for MLLMs.

### Weaknesses
1. The in-house dataset is not discussed in detail, such as whether it will be open-sourced, and whether the manual calibration process mentioned in lines 365-366 follows the same methodology as MMMB construction. The lack of detail regarding the in-house dataset's construction, particularly concerning noise control and data diversity, makes it difficult to assess its quality and potential impact on the model's performance. Furthermore, the absence of information on whether this dataset will be made public hinders reproducibility and further research.
2. There is no experimental analysis on Parrot's performance loss in a single language, for example, whether the use of multilingual data and the MoE module reduces the model's English proficiency. The paper does not investigate the potential trade-offs in performance when using multilingual training data and the MoE module, specifically whether the model's proficiency in English, which is often the most well-represented language in training data, is negatively affected.
3. Parrot’s training consists of two stages, largely following LLava’s approach. However, the inclusion of the MoE architecture raises questions about its integration in stage 1. Specifically, how are the MoE weights initialized? If initialized randomly, is it optimal to include the MoE in stage 1, given that this stage focuses on aligning multimodal features? Additionally, if the MoE is indeed included in stage 1, an ablation study on whether to freeze or not freeze the MoE module would be insightful. The paper lacks clarity on the MoE module's role during the initial pre-training stage, particularly regarding its initialization and whether its parameters are updated during this phase. This raises concerns about the efficiency of the training process and whether the MoE module is effectively utilized from the beginning.

### Questions
1. As mentioned in Weakness #1, will the in-house dataset be open-sourced? The construction process should be explained in more detail, particularly regarding noise control and data diversity.
2. As mentioned in Weakness #2.
3. Parrot’s training consists of two stages, largely following LLava’s approach. However, the inclusion of the MoE architecture raises questions about its integration in stage 1. Specifically, how are the MoE weights initialized? If initialized randomly, is it optimal to include the MoE in stage 1, given that this stage focuses on aligning multimodal features? Additionally, if the MoE is indeed included in stage 1, an ablation study on whether to freeze or not freeze the MoE module would be insightful.

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
3

### Summary
This paper addresses the imbalance in the quantity of SFT data for different languages within training datasets used in MLLM's SFT process, which results in suboptimal alignment performance for various languages with limited data. To tackle this issue, the authors propose a novel structure that combines the cross-attention and MoE structure, enabling the input visual tokens to MLLM to be conditioned on the language input. Furthermore, to address the current lack of comprehensive benchmarks for multilingual multimodal tasks, the authors propose a new benchmark, named MMMB, which provides a more extensive evaluation for multilingual MLLMs. Extensive experiments validate the effectiveness of the proposed method on multilingual benchmarks.

### Strengths
- The author's observation regarding the lack of balance among different languages in the SFT data of MLLMs is insightful.
- The proposed method is simple and efficient.
- The benchmark proposed by the author is rigorous and highly relevant for evaluating multilingual MLLMs.
- The paper is well-written and easy to follow.
- The experiments are comprehensive, demonstrating the effectiveness of the method proposed by the author.

### Weaknesses
 - **Regarding the issue of alignment:** I agree with the author's observation that the imbalance of SFT data among different languages may lead to poor alignment between vision tokens and multilingual tokens in MLLMs. However, it should be noted that the alignment data in the pretraining phase consists of English-only data, and the amount of data in the pretraining phase is significantly larger than that in the SFT phase. Would the impact of alignment between visual tokens and different language tokens be more severe in the pretraining phase?
- **Lack of comparison for the latest MLLM models**: Some of the VLMs the author compares are outdated. Could the evaluation include the latest VLMs, such as Qwen2-VL [1] and LLaVA-OV [2]?
- **About the scalibility**: Introducing a language-aware structure is an effective approach, but if similar structures are not introduced, would simply increasing the proportion of different language data in the SFT data yield a similar improvement in model performance? In larger models, such as those with 30B or larger model, is the performance gain from this model design consistent?

### Questions
Please see the above weaknesses.

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
The paper aims to strengthen the multilingual ability of vision-language models.
Due to the data imbalance problem, vision-language models often perform better on English-based data while suffering from low performance on language with scarce data.

To address the problem, the paper proposes a routing strategy with textual guidance.
The router makes the image embeddings language-aware.
Moreover, the paper collects new data for non-English languages with the assistance of GPT-4.

Experiments on MMBench show reasonable improvements over baseline models, like LLaVA.

### Strengths
(1) The paper is clear and easy to follow.     
(2) The data imbalance problem in vision-language models is interesting.

### Weaknesses
(1) How to train the language transformation experts for the MoE module?        
     Are there explicit constraints to optimize the routing?                
     As the paper mentions training the baseline LLaVA with the multilingual data suffers from data imbalance problem.                 
     However, the proposed training strategy can also suffer from the problem:                  
          I. The routing strategy can be dominated by English-based data.                        
          II. The language transformation experts should perform worse for languages with fewer data.                  
     The authors should discuss how the above two problems are addressed.  

(2) How does the MoE module affect model performance as the data size of each language increases?
     Also, how does the increased data size affect the baseline model performance, like LLaVA?

(3) The proposed method actually injects language information into the image embeddings, making $H_v$ language-aware.
      Another straightforward baseline is to train several translation expert models, translating other languages into English.

### Questions
(1) Carefully study how the performance of language transformation experts affects the overall performance.        
(2) Inspect how the router works, like looking into the classification accuracy for different languages.         
(3) Compare with the baseline models fairly, like using the same training data.

### Soundness
2

### Presentation
3

### Contribution
2
