# Genomic Foundationless Models: Pretraining Does Not Promise Performance

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
The success of Large Language Models has inspired the development of Genomic Foundation Models (GFMs) through similar pretraining techniques. However, the relationship between pretraining performance and effectiveness in downstream genomic tasks remains unclear. Additionally, the high computational cost of pretraining raises questions about its cost-efficiency. To assess the usefulness of pretraining in genomics, we evaluated seven different GFMs across various benchmarks, comparing them to their counterparts with randomly initialized weights. Surprisingly, we found that randomly initialized models can match or even surpass the performance of pretrained GFMs in finetuning and feature extraction tasks. We also discovered that pretrained GFMs fail to capture clinically relevant genetic mutations, which are crucial for understanding genetic disorders and phenotypic traits. Our results indicate that most of the current pretrained GFMs lack a ``foundational'' understanding of genomics and provide minimal utility, even for basic tasks such as sequence classification. These findings collectively highlight the need for critically rethinking the pretraining approaches for genomics. Our code is available at https://github.com/nxifemwt/GFMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper questions the value of pretraining in genomic foundation models (GFMs), demonstrating that randomly initialized models can often match or even surpass pretrained GFMs on several tasks.

### Strengths
1. The paper proposes an interesting perspective in challenging the assumed superiority of pretrained models in genomics;
2. The experiments were thorough in comparing pretrained models with randomly initialized counterparts across various genomic tasks;
3. The writing is clear and easy to follow.

### Weaknesses
1. Although the results suggest current methods may not work, the paper could explore alternative pretraining objectives or paradigms that might better align with biological complexity.
2. There lacks an explanation or analysis on why specific models, such as Mistral or DNABERTv2, might perform better or worse on certain tasks, which would provide better insight.

### Questions
1. Could different pretraining tasks or loss functions enhance mutation sensitivity or biotype classification, specifically for detecting single-nucleotide variants?
2. The paper indicates certain tokenization changes improved performance. Would further model-specific optimizations, such as vocabulary adaptations or alternate pooling strategies, yield better results?
3. Given that pretrained models in other domains often benefit from more extensive data and compute, is there a threshold or scaling that could make pretraining beneficial for GFMs?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work benchmarks the effectiveness of the Genomics Foundation Models (GFM) compared to randomly initialized models. Their experiments indicate that GFMs offer limited or even no advantages over randomly initialized models on many tasks.

### Strengths
1. The paper is well-written and easy to follow.
2. The experiments are comprehensive and well-presented, except for a few ones (see Weaknesses). 
3. The mutation experiments are very interesting.

### Weaknesses
1. Findings 1 is not well-supported
    - Figure 1 is missing leading. Given that different GFMs differ significantly in the number of parameters (e.g., 450k v.s. 500M), I don't understand what the authors aim to convey with this figure. A randomly initialized large model achieving better performance than a pre-trained small model does not suggest the pre-training is not helpful. 
    - A pairwise comparison of the pre-trained and random versions of the same model, as shown in Figure 2, is much more meaningful. In fact, as shown in Figure 2, the pre-trained model performs better than the random counterparts in most cases, which actually suggests the effectiveness of pre-training. The improvement of pre-training over randomized is more significant on more distinguishable datasets like histone (i.e., different models achieve distinct performances) and less significant on promoter/enhancer. I would attribute this insignificance mainly to the datasets (See below).

2. As shown in Figure 2, all the models ranging from 450k to 500M parameters achieve near-identical performance on many datasets of the NT benchmark, especially on promoter and enhancer. This indicates this benchmark may not be suitable for differentiating different models' capabilities. If the dataset could not differentiate different pre-trained models, it's hard to believe it can effectively differentiate pre-trained/random models. I would suggest more experiments on other benchmarks/datasets that can clearly differentiate the performance of different models. You may consider the datasets used in HyeneDNA (species classification), DNABERT-2 (GUE), and Caduceus (Genomics Benchmark).


Overall, I appreciate the authors' efforts in conducting this amount of experiments. Yet the results are not convincing, and the main conclusion (findings 1) is not well-supported. I will consider increasing my scores if more convincing results are presented.

### Questions
1. For NT, why use the 1000G instead of NTv2-multispecies? The v2 one is much better.
2. It's nice to compare the models in both finetuning and feature extraction. Why don't you use the same datasets for finetune/feature extraction? I would suggest the same feature extraction experiments on the same selected portion of the NT benchmark, like the histone datasets, to provide more convincing observations on the feature extraction of GFMs.

### Soundness
2

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
4

### Summary
The paper critically evaluates the assumption that pretraining offers significant advantages in Genomic Foundation Models (GFMs). Through extensive comparisons, the authors show that randomly initialized models can achieve performance comparable to or exceeding that of pretrained models across a variety of genomics tasks.

### Strengths
1. The study includes a detailed analysis across several GFMs with random initialization methods, providing a broad view of the pretrained effect on genomic benchmarks. 
2. The observation that pretrained models often fail to capture clinically relevant mutations, particularly for tasks that require sensitivity to sequence variation.
3. The authors conducted extensive and convincing experiments on genomic datasets to validate their hypotheses.

### Weaknesses
1. Lack of further analysis on model behavior. For instance, why do random models outperform pretrained models on some tasks? Why does Mistral perform better in mutation sensitivity analysis?
2. The experiment on ClinVar uses a limited sample size (only one gene), which may limit the generalizability of the conclusion that pretrained models lack sensitivity to mutations.
3. The single nucleotide sensitivity analysis lacks comparative experiments. There is no direct comparison between random and pretrained models in the mutation sensitivity analysis and the ClinVar experiments.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the performance of genomic foundationless models, particularly focusing on the implications of pretraining. While the topic is pertinent, the paper presents several critical issues that undermine its contributions and clarity.

### Strengths
- The exploration of pretraining in genomic models is an important area of research, especially given the growing interest in applying deep learning to genomics.
- Potential Impact: Understanding the limitations of pretraining in this context can provide valuable insights for future research.

### Weaknesses
 - The findings largely reiterate known limitations of pretraining without offering new insights or approaches. The paper does not present a compelling argument for how its contributions advance the field.

- The experimental validation lacks rigor. There is a failure to adequately compare the proposed models with established methods, making it difficult to evaluate the significance of the results. A large number of genetic tasks that have been established have not been mentioned and tested for relevance.

- The conclusions drawn from the experiments are overly broad and not sufficiently supported by the data presented. The authors claim that pretraining does not promise performance without adequately accounting for various contextual factors.

### Questions
- It's not that pre-training doesn't work. It's that gene sequences haven't found a more appropriate pre-training strategy.

- It doesn't make sense to me to disregard the EVO model, which has the largest pre-training scale, doesn't it?

### Soundness
2

### Presentation
2

### Contribution
2
