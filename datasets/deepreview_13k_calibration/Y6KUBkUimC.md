# Scalable Ranked Preference Optimization for Text-to-Image Generation

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
Direct Preference Optimization (DPO) has emerged as a powerful approach to align text-to-image (T2I) models with human feedback. Unfortunately, successful application of DPO to T2I models requires a huge amount of resources to collect and label large-scale datasets, \eg, millions of generated paired images annotated with human preferences. In addition, these human preference datasets can get outdated quickly as the rapid improvements of T2I models lead to higher quality images. In this work, we investigate a \emph{scalable} approach for collecting large-scale and \emph{fully} synthetic datasets for DPO training. Specifically, the preferences for paired images are generated using a pre-trained reward function, eliminating the need for involving humans in the annotation process, greatly improving the dataset collection efficiency. Moreover, we demonstrate that such datasets allow averaging predictions across multiple models and collecting ranked preferences as opposed to pairwise preferences. Furthermore, we introduce \methodName~to enhance DPO-based methods using the ranking feedback. Applying \methodName~on SDXL and SD3-Medium models with our synthetically generated preference dataset ``\datasetName'' improves both prompt-following (on benchmarks like T2I-Compbench, GenEval, and DPG-Bench) and visual quality (through user studies). This pipeline presents a practical and scalable solution to develop better preference datasets to enhance the performance and safety of text-to-image models. %

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the preference optimization of T2I diffusion models, particularly SD3-Medium and SDXL. The main contribution made by this paper has two folds. 1) This paper proposed a new synthetic preference dataset containing rankings annotated by existing preference models, which cost less than similar datasets with human annotation. 2) Based on the ranking-based dataset, this paper proposes a new DPO method using the ranking information to improve the prompt following and generation quality of T2I diffusion models.

### Strengths
- The overall presentation of this paper is clear.
- I like the idea that extending existing human preference dataset with (win, lose) tuple to having more items, naturally leading to a rank based preference dataset.
- The experiments are conducted on both big and medium sized models: SDXL and SD3-Medium, which is adequate. The comparison experiments with other models finetuned with DPO and different preference datasets show that the proposed new dataset and method has better performance than others.

### Weaknesses
 - Overall, I like the idea of using rank-based preference dataset and DPO, which should be able to provide more fine-grained preference guidance than (win, lose) style DPO and datasets. My only concern is that it is unclear whether the performance improvement of the proposed RankDPO is more because of the new synthetic dataset or the rank-based DPO. According to my understanding, in Table 3, DPO-SDXL, MaPO SDXL, SPO SDXL, and the proposed RankDPO SDXL are fine-tuned with different preference datasets, which mixes the impact of the new dataset and new DPO model. It would be better if the author could provide the insight about whether dataset or the rank-based DPO, is more important to the performance improvement over other preference optimization models. What if train DPO/SPO/MaPO with newly collected rank preference dataset? For example, randomly pick two images from a rank set and set the one with the lower rank to be the "win" and the other to be the "lose". What if finetune with RankDPO but using existing preference datasets? For example, set the "win" sample to be rank 1 and the "lose" sample to be rank 2. In my opinion, these insight is super important to this paper and would be beneficial to the community.

### Questions
No

### Soundness
2

### Presentation
2

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
Overall, this is a very good and solid paper. The paper addresses the challenges of applying Direct Preference Optimization (DPO) to text-to-image (T2I) models, particularly the resource-intensive process of collecting human preference datasets. The authors propose a scalable approach for creating large-scale synthetic datasets for DPO training, using a pre-trained reward function to generate preferences for paired images. This method allows for averaging predictions across multiple models and collecting ranked preferences instead of just pairwise preferences. The researchers introduce RankDPO, an enhancement to DPO-based methods that utilizes ranking feedback. Applying RankDPO on SDXL and SD3-Medium models with the synthetic "Syn-Pic" dataset improves both prompt-following and visual quality, offering a practical solution to enhance the performance and safety of T2I models.

### Strengths
1. The writing of this paper is clear and easy to follow. It's easy to understand the main contributions of this paper as I summarized above.
2. The contributions of this paper are solid. [Method contribution] The authors propose a new performance optimization method RankDPO, and the effectiveness is well supported by extensive experiments on SDXL, SD3-Medium models and GenEval, T2I-CompBench benchmarks. [Dataset contribution] To make the ranking-based preference optimization work, the authors collect a new dataset Synthetically Labeled Preference Dataset (Syn-Pic), which can benefit future research in text-to-image community.

### Weaknesses
No obvious weaknesses. Please check the questions section.

### Questions
1. How to evaluate the reliability of the Reward Models when building the Syn-Pic dataset? Do you conduct a human evaluation study, for example, do you calculate the correlation between the reward model ranking and human evaluation ranking?
2. There are some other text-to-image benchmarks as I know, for example, HRS-bench [*]. Can you explain the reason why not include other benchmarks in your paper?

[*] Bakr, E. M., Sun, P., Shen, X., Khan, F. F., Li, L. E., & Elhoseiny, M. (2023). Hrs-bench: Holistic, reliable and scalable benchmark for text-to-image models. In Proceedings of the IEEE/CVF International Conference on Computer Vision (pp. 20041-20053).

### Soundness
3

### Presentation
3

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
This paper proposes a scalable approach to fine-tune text-to-image generation (T2I) models using DPO without requiring human annotation. The authors introduce a synthetic preference dataset collection method, where preferences are generated using off-the-shelf reward models, eliminating the need for human annotation. Additionally, this approach leverages model predictions across multiple models, enabling dense and ranked preferences rather than just parse pairwise ones. The authors also propose RankDPO, a framework that incorporates ranking feedback to enhance the DPO process. Their method, applied to SDXL and SD3-Medium models, demonstrates improved prompt alignment and visual quality on various benchmarks. This study contributes a cost-effective, efficient pipeline to advance T2I model alignment.

### Strengths
+ Scalable and cost-effective dataset collection with synthetic preferences.

+ The proposed RankDPO framework effectively leverages ranked feedback to improve text-image alignment

+ Experiments on benchmark datasets could verify the effectiveness of the proposed method.

### Weaknesses
 - Lack of novelty: Existing work (Wallace et al. 2024, Liu et al. 2024c) have proposed diffusion-based DPO and List-wise ranking-based DPO. It seems that the proposed method combines them to tune diffusion models. 

- More baseline methods, especially those used to generate images in the process of the construction of Syn-Pic, should be considered and compared in Tab 1, Tab 2, and Tab 3. 

- The performance improvement gained by RankDPO over DPO (5 Rewards) in Tab 4 seems marginal. The effectiveness of the list-wise or rank-wise DPO method may be not strongly verified.

Minors: 
It seems to be “Tab. 5” instead of “Tab. 4” in line 425.

### Questions
- The improvement in the non-spatial category of T2I-CompBench, as shown in Tab 2, seems not remarkable compared with others. Why is that and how to explain it? 

- How does the proposed method influence the quality of generated images (e.g., FID), although the alignment has been improved as shown in Tab 1-3?

- Is it possible that the proposed method just “distills” the useful knowledge from the models used to generated images in the process of the construction of Syn-Pic, especially those strong base models?

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
This paper introduces a powerful and cost-effective approach for the preference optimization of text-to-image models. Specifically, this work demonstrates how synthetically generating a preference optimization dataset can enable the collection of superior signals (e.g., rankings vs. pairwise preferences and ensembling preferences across models). Moreover, this paper also introduces a simple method to leverage the stronger signals, leading to state-of-the-art results on various benchmarks for prompt following and visual quality for both the diffusion and rectified flow models.

### Strengths
Inspired by the LLMs community, aligning T2I models with human feedback has become an important and practical topic to enhance existing T2I models. However, there are two major efforts in this area: 1) collecting large amounts of user preferences images for training and 2) fine-tuning with T2I models with reward functions. The former direction shows promising results when utilizing Direct Preference Optimization (DPO), but with expensive data collection cost, e.g., Pick-a-Picv2 costs nearly $50K. The later direction fine-tunes the T2I models by maximizing the reward functions with the generated images, but this process is computationally expensive and suffers from “reward hacking”, where this optimization process increases the reward scores without improving the quality of the generated images.

This paper address the above challenges and propose a scalable and cost-effective solution for aligning T2I models, which includes the following two contributions:
- Synthetically Labeled Preference Dataset (Syn-Pic).
- Ranking-based Preference Optimization (RankDPO).

The experimental results seem to consistently show the advantages of this approach, indicating that it is an effective solution.

### Weaknesses
 - **Lack of comparison of training costs.**  Cost-efficiency is the main claimed contribution of this work, but the paper only briefly mentions the monetary comparison (\$200 v.s. \$50K for Pick-a-Picv2). I believe that the gain of this work lies in the newly proposed loss function $\mathcal{L}_{\text{RankDPO}}$, so its training cost comparison, e.g., training time, gpus, flopts, and so on, should be included in main text and Tab.8.

- **Clarification of the ``*Reference model*'' definition**. The ``*reference model*'' defined in the method is not fully explained in lines 204 and 285, resulting in a less than intuitive understanding of the method.

- **Analysis of the effectiveness and limitations of Ground Truth.** I understand that Eq.5 is the core of the proposed RankDPO, which means that the model is supervised based on the reference model or the so-called ground truth (GT) preference, so I really want to know how this GT preference is obtained (Section 3.2 does not seem to mention)? Is there a subjective bias for GT that causes the performance of the model to have an upper limit (e.g., only select few intended t2I models)? Does the scale k of the adopted t2I models have an impact on the ground truth?

- **Lack of *scalable* explanations and quantitative or qualitative comparisons.** In line 92, it is claimed that this work is scalable, but there is a lack of theoretical explanation, qualitative analysis and quantitative comparison of scalability in the experiments and methods. In other words, are all previous methods not scalable? How to measure the scalability of this work? Can this work be adapted to the preference annotation of other tasks such as video and 3D? What is the connotation of this scalability? Please give a detailed explanation and clear definition.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
