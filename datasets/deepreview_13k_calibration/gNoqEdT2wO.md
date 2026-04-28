# A Multimodal Class-Incremental Learning benchmark for classification tasks

- Decision: Reject
- Avg Score: 2.33
- Scores: 3, 3, 3, 1, 3, 1

## Abstract
Continual learning has made significant progress in addressing catastrophic forgetting in vision and language domains, yet the majority of research has treated these modalities separately. The exploration of multimodal continual learning remains sparse, with a few existing works focused on specific applications like VQA, text-to-vision retrieval, and incremental multi-tasking. These efforts lack a general benchmark to standardize the evaluation of models in multimodal continual learning settings. In this paper, we introduce a novel benchmark for Multimodal Class-Incremental Learning (MCIL), designed specifically for multimodal classification tasks. Our benchmark comprises a curated selection of multimodal datasets tailored to classification challenges. We further adapt a widely used Vision-Language model to multiple existing continual learning strategies, providing crucial insights into the behavior of vision-language models in incremental classification tasks. This work represents the first comprehensive framework for MCIL, establishing a foundation for future research in multimodal continual learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a multimodal class-incremental learning benchmark, consisting of Oxford Flowers, CUB and DVM-CAR datasets. The authors select Flava as the primary model for evaluating vision-language continual learning on the MCIL benchmark. The authors also include 3 baselines (DualPrompt, L2P, Experience Replay) for multimodal class-incremental learning evaluation.

### Strengths
This paper introduces a Multimodal Class-Incremental Learning benchmark. The paper demonstrates the relevance and utility of the proposed benchmark by adapting a widely used model (Flava) and providing insights into its performance.

### Weaknesses
1. My major concern is that the contribution is limited. This benchmark is referred to as multimodal, but it only includes visual and language modalities, and is limited to image classification tasks. However, such a so-called multimodal class-incremental learning (MCIL) classification task has already been investigated. There are some works on class-incremental learning using visual-language models[1-5] and it seems that there is no difference between their setting and the proposed MCIL setting. The authors should clarify and carefully discuss the differences between them. Besides, apart from the visual and language modalities, there are also works investigating the audio-visual incremental learning problem [6], and I suggest the authors should conduct a comprehensive literature review before proposing a new benchmark. The authors should explicitly compare their proposed benchmark to the existing works, highlighting any key differences or improvements. Additionally, the authors should expand their literature review to include audio-visual and other multimodal incremental learning approaches, and discuss how their benchmark relates to or differs from these broader multimodal settings.
2. The datasets CUB, Oxford Flowers, and DVM-CAR are all small-scale datasets. Some core settings are missing from the experiments, such as experiments on ImageNet1K and experiments with different numbers of tasks, which are widely adopted in different class-incremental learning works. I suggest the authors to justify their choice of datasets and explain why they believe these are sufficient for evaluating multimodal class-incremental learning.
3. I cannot understand why methods similar to CLIP and ALIGN do not meet Eq1. Although these methods cannot generate a unified multimodal feature representation, they still accomplish classification tasks by calculating cosine similarities. At the same time, I also fail to understand how Flava is used. What is the text input of Flava in the MCIL setting?
4. The survey of related work is not comprehensive enough, and the compared baseline methods are not comprehensive. The recent works only include L2P and DualPrompt, which is insufficient for a benchmark evaluation. Since the authors choose Flava, which generates a unified feature representation, classic CIL methods such as Regularization-based methods (e.g. LwF) and replay-based methods (e.g. iCaRL) can also be used in the Flava model. I suggest the authors could refer to [7] for a comprehensive review of CIL methods. The authors are advised to supplement relevant experiments.
5. Some minor issues:
    - The number of images in line 144 and line 152, '.'->','
    - The title of Figure 1 is too simple.
    - In Table 1, it would be easier to understand if UB and LB are listed separately, and the best results among other methods are bolded. The formatting of Table 1 could also be improved.
    - I suggest the authors add a figure to illustrate the whole pipeline of the proposed MCIL setting.

### Questions
1. What is the text input of the Flava model in the MCIL setting?
2. What is the difference between the proposed MCIL and existing CLIP-based CIL problem?
3. Why Oxford Flowers, CUB and DVM-CAR are chosen, why not include larger-scale dataset?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This manuscript introduces a benchmark for Multimodal Class-Incremental Learning (MCIL). The benchmark comprises a selection of multimodal datasets tailored to classification challenges.

### Strengths
This paper proposed a multimodal CIL benchmark, and migrate some classical methods to this benchmark for testing. Continual learning techniques are deployed on a vision-language model.

### Weaknesses
Weakness：
1: The test datasets of the benchmark are few and simple, which are only three common datasets.
It doesn't look like a complete and good benchmark. 

2: There are already multimodal CIL protocols in existence, such as [1], [2], [3], and your benchmark seems to overlap with them to a high degree. This benchmark seems to be not significant.
[1]: CLIP MODEL IS AN EFFICIENT CONTINUAL LEARNER
[2]: AttriCLIP: A Non-Incremental Learner for Incremental Knowledge Learning
[3]: Class-Incremental Learning with CLIP: Adaptive Representation Adjustment and Parameter Fusion

3: The experimental method for migration is not sufficient. The Dual-Prompt and L2P methods used are relatively classic but outdated methods. The latest methods such as [4], [5], [6], [7], etc. may also need to be migrated to further measure the necessity of the benchmark.

[4]: Coda-prompt: Continual decomposed attention based prompting for rehearsal-free continual learning
[5]: Promptfusion: Decoupling stability and plasticity for continual learning
[6]: One-stage Prompt-based Continual Learning
[7]: Hierarchical decomposition of prompt-based continual learning: Rethinking obscured sub-optimality

4: The multimodal model selected in this paper is also relatively outdated. If more advanced MLLM models such as LLava1.5, CogVLM, CogVLM2 are used to conduct experiments on the benchmark, the significance of the benchmark can be further explained.

5: The content of the paper is insufficient and lacks sufficient analysis and explanation of the particularity and necessity of this benchmark.

### Questions
see the weakness

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents the Multimodal Class-Incremental Learning (MCIL) benchmark, aimed at evaluating multimodal continual learning methods specifically within classification tasks. The authors utilize the Flava architecture as a baseline to assess how vision-language models adapt to incremental learning scenarios. They identify significant challenges faced by these models when dealing with multimodal data and shifting distributions.

### Strengths
- The majority of existing research focus on single modality based continual learning.The introduction of the MCIL benchmark is important in the field of multimodal continual learning. By providing a standardized framework, it fills a critical gap in current research, enabling more consistent evaluation and comparison of models.

- The paper includes some experimental results of current methodologies in Multimodal Class-Incremental Learning.

### Weaknesses
1. The motivation for this work is unclear. Given the strong capabilities of current vision-language models, why is incremental learning for multimodal classification necessary? Presently, vision-language models can handle image classification effectively with either visual or text input alone; both modalities are not needed simultaneously to perform well. Additionally, I noticed that in the proposed MCIL benchmark, the authors remove samples where the description explicitly mentions the ground-truth category. However, this approach does not fully prevent leakage, as the text may still indirectly reveal category information through similar words or phrases that are difficult to detect and remove. It would be helpful if the authors could clarify the specific use case or scenario for this task to help readers better understand the motivation behind it.

2. The presentation is poor and the experiments are insufficient. It seems a semi-finished product submission with just 7 pages of main contents.

### Questions
Weakness Section

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper addresses the gap in multimodal continual learning by introducing a novel benchmark for Multimodal Class-Incremental Learning (MCIL), designed specifically for classification tasks across multiple modalities. While continual learning has progressed in the vision and language domains independently, multimodal continual learning remains underexplored, particularly in classification contexts. Current research has focused on specific applications like VQA and text-to-vision retrieval, lacking a standardized benchmark to fairly compare and evaluate methods in multimodal settings.

The proposed MCIL benchmark includes a curated selection of multimodal datasets for classification and adapts a popular vision-language model (Flava) across various continual learning strategies. This setup allows a systematic evaluation of model performance in handling incremental learning with diverse data sources. By providing experimental insights into the behavior of vision-language models within this framework, the paper establishes a foundation for future research in multimodal continual learning, aiming to enhance knowledge retention and cross-modal alignment over time.

### Strengths
This paper gives lots of description about the used models, metrics and datasets, clearly illustrating the pipeline and experimental settings.

### Weaknesses
1. The motivation for this work is unclear. Given the strong capabilities of current vision-language models, why is incremental learning for multimodal classification necessary? Presently, vision-language models can handle image classification effectively with either visual or text input alone; both modalities are not needed simultaneously to perform well. Additionally, I noticed that in the proposed MCIL benchmark, the authors remove samples where the description explicitly mentions the ground-truth category. However, this approach does not fully prevent leakage, as the text may still indirectly reveal category information through similar words or phrases that are difficult to detect and remove. It would be helpful if the authors could clarify the specific use case or scenario for this task to help readers better understand the motivation behind it.

2. The presentation is poor and the experiments are insufficient. It seems a semi-finished product submission with just 7 pages of main contents.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel multimodal Class-incremental learning benchmark to standardize the evaluation of VLM models in a continual learning setting. It evaluates a widely used VLM with multiple existing continual learning methods on three curated multimodal datasets. The work is focused on multimodal classification tasks keeping other variables like tasks and domains fixed.

### Strengths
It is a focused work on the classification task while keeping other factors fixed. Such a controlled study can lead to more precise conclusions about the strengths and challenges of different methods in visual-language settings. The discussion of different methods is quite detailed. However, it should be supported with ablations and quantitative analysis.

### Weaknesses
1. The VLM methods and datasets included in this work only cover a narrow domain. A much wider study is required for establishing such a benchmark.  The work generalizes the observation using different continual learning methods using only one VLM model. More VLM models (at least one from each type) from Section 3.3 like CLIP or ALIGN, ViLBERT and latest approach like BLIP should be included in the evaluation to make stronger conclusions.

2. The datasets covered in this work belong to very specific domains like birds, cars, and flowers. More generic datasets should be included to make it a comprehensive framework. 

3. The setting of class-incremental learning studied in this work is not realistic because the continuous data usually does not arrive in pure chunks of classes and is often a mix of all classes in different proportions. For example, use something like 'the CLEAR Benchmark' by Lin et al. It captures a realistic temporal evolution of visual concepts. 

4. The limit of the paper is 10 pages. Additional results should in included in the main paper instead of the Appendix to improve the presentation of the paper. Details about the Dual Prompt (DP) model can be included in the main manuscript. 

5. The details about experiment settings including model implementation details are missing. For example - Was the Flava model pretrained on some dataset or was it trained from scratch? The reported standard errors are calculated on how many runs? How big is the training, validation and test set for each dataset? 

6. Presentation can be improved. Captions should be self-complete containing information about the experiment setup and conclusions. Captions like ‘Results.’ are not acceptable.

### Questions
1. The presentation of the paper should be improved including captions, figures and experiment details.
2. Add more VLM models to make conclusions more robust to the model choice.
3. I would recommend adding more ablations and quantitative analysis to make reasoning about the performance of continual learning methods stronger. 
4.  Also evaluate on generic datasets to make it a comprehensive framework.

Overall, I would recommend authors add more methods and generic datasets, provide more analysis, and pick a more realistic continual learning setting to set up a valuable multimodal CIL benchmark for the community.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper presents a new benchmark for multimodal class-incremental learning (MCIL) with a focus on multimodal classification tasks. The benchmark is formed using three existing benchmarks that consist of images along with their captions.  5 CL methods along with an upperbound and a lowerbound using Flava as the base model are tested on the benchmark by splitting each dataset into 10 incremental tasks.

### Strengths
I hardly can find a strengths in this work. The only thing that comes to my mind is that the writing quality is acceptable and the paper can be followed straightforwardly.

### Weaknesses
The contribution of this work is extremely weak. Three existing benchmarks are split and then five CL methods are run on the resulting tasks. Hence, new data is collected nor a new method is introduced. The paper is not well-motivated and it is not clear what this paper is going to offer to the research community.

### Questions
The paper is so weak and naive that it is not easy to come up with questions. The reason is that a work should be novel enough such that one can ask meaningful questions about the approach. I hardly could come up with the following questions:


1. What unique challenges does multimodal class-incremental learning present that are not captured by unimodal benchmarks? Other than changing the model from unimodal to multimodal, what is the specific challenge that makes this dataset specific?

2. What is the novelty and motivation of this work? What specific gaps in existing multimodal continual learning research does this benchmark address?

3. How this work can help researchers? How does this benchmark compare to or improve upon existing multimodal or continual learning datasets? How might researchers use this benchmark to develop new multimodal continual learning algorithms?

### Soundness
1

### Presentation
3

### Contribution
1
