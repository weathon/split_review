# M-BioBERTa: Modular RoBERTa-based Model for Biobank-scale Unified Representations

- Decision: Reject
- Scores: 5, 8, 3

## Abstract
Transformers provide a novel approach for unifying large-scale biobank data spread across different modalities and omic domains. We introduce M-BioBERTa, a modular architecture for multimodal data that offers a robust mechanism for managing missing information. We evaluate the model using genetic, demographic, laboratory, diagnostic, and drug prescription data from the UK Biobank, focusing on multimorbidity and polypharmacy related to major depressive disorder. We investigate the harmonized and modular representations in M-BioBERTa for patient stratification. Furthermore, leveraging the learned representations to forecast future disease and drug burdens outperforms traditional machine learning approaches applied directly to the raw data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors presented a novel modular transformer based model to capture multi-modal EHR data and analyzed a large scale EHR dataset in the form of UK biobank.

### Strengths
The main strengths of the paper are as below
- The proposed idea is intuitive and makes a lot of sense when trying to model such large scale EHR datasets. 
- The method shows performance improvement over selected baselines on both regression and classification tasks
- The appendix section drills down into the performance of the model around a number of key aspects such DM and Hypertension. In the context of health, it is often important for models to be investigated for their usage around specific usage criterion. The results are promising in these sections.

### Weaknesses
Some of the key aspects that can improve the model are as follows
- The main drawback is around the deleted baselines. Apart from XGB the selected baselines are rather weak. Even for the selected baselines, the feature selection and processing should be discussed in more details
- The method description is rather convoluted and difficult to follow. The main claim of the architecture is rather muddied and difficult to review for importance
- The modalities while discussed in the beginning is under-analyzed in terms of their contribution for predictive/modeling performance. The authors should consider ablation of modalities

### Questions
There are a couple of aspects that the authors can clarify
- For temporal embeddings, have the authors considered standards methods such as cosine embeddings? 
- In section 3.4, while describing the unified cross-attention decoder, is the function of the "dedicated cross-attention units" to capture "inter-modal correlations" or intra-modal correlations?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces M-BioBERTa, a modular transformer architecture for multimodal biobank data. M-BioBERTa ulitizes multiple unimodal RoBERTa encoders for individual data modalities, the model employs a unified RoBERTa decoder with cross-attention layers for cross modal training. Unimodal encoders are pre-trained on its respective modality before unified training. M-BioBERTa introduces novel elements like temporal embeddings for longitudinal data and mixed tabular embeddings for heterogeneous types. The authors utilize UK Biobank data to train and benchmark M-BioBERTa. M-BioBERTa outperforms baselines in disease and drug burden prediction, effectively handling missing modalities. Overall, it presents a novel approach for learning unified representations from multimodal biobank data.

### Strengths
1. Unimodal encoders enables handling of systematically missing multimodal data. Each encoder can be separately trained in parallel on their own data.  Cross modal attention fuses unimodal representations capturing interactions between modalities. 

2. Temporal and tabular embeddings are vital for domain specific (biomedial) performance and M-BioBERTa pays clear attention to them 

3. M-BioBERTa outperformed ML baselines on downstream predictive tasks using the UK Biobank data suggesting that it captures clinically relevant patterns.

4. Assuming typical transformer scaling laws M-BioBERTa is a great candidate to scale models using multimodal biomedical datasets.

### Weaknesses
1. There is a limited discussion on the scaling behavior of the proposed model architecture. Specifically, the paper lacks an analysis of how performance changes with increasing model size (number of parameters) and training data. This is crucial for understanding the practical applicability of M-BioBERTa, especially given the computational demands of transformer models. The paper should include experiments that vary model size and training set size to show the model's scaling properties and identify potential bottlenecks.

2. The paper does not include ablation studies to directly demonstrate the benefits of key components like the temporal embeddings and mixed tabular embeddings. For example, it is unclear how much performance gain is attributable to the temporal embeddings versus simply using the raw time series data. Similarly, the impact of the mixed tabular embeddings compared to using simpler embedding strategies is not quantified. Ablation studies are needed to isolate the contribution of each component.

3. Other transformer baselines are not considered for several downstream benchmarks. While RoBERTa is a reasonable baseline, the paper should also compare against other transformer architectures such as BERT, or variants like Longformer or Reformer, especially given the longitudinal nature of the data. This would provide a more comprehensive view of M-BioBERTa's performance relative to the state-of-the-art.

### Questions
1. How sensitive is M-BioBERTa to the choice of pretraining objectives beyond MLM? Could other self-supervised tasks (T5, UL2) further improve the representations? 

2. What is the impact of pretraining the encoders separately versus jointly pretraining the full model?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The research presents M-BioBERTa, a Transformer-based architecture designed to unify large-scale biobank data from diverse modalities and omic domains. The model's performance was evaluated using a wide array of data from the UK Biobank, which included genetic, demographic, laboratory, diagnostic, and drug prescription data, with a special emphasis on issues related to major depressive disorder such as multimorbidity and polypharmacy.

### Strengths
- Interesting idea on multi-modal learning over biobank data. 
- Utilizes numerous modalities of a sample. 
- Tackle the multi-modal nature through various forms of embeddings including temporal embedding.

### Weaknesses
 - Presentation is unclear. Many important details are missing.
- The evaluation is unclear. Lots of experiments are needed to justify the model design.
- The approach is a bit ad hoc. Requires more justifications.

- Why Roberta model? It would be great to justify it.  

How exactly is pre-training conducted? The authors mention that masked modeling is used. But here which part is masked? since there are multiple modalities, is it modality-specific masking? or others? have the authors experimented with any varieties of masking strategies? 

"The genomics data, sourced from SNPs, was encoded to display only the minor and major allele in the sequence." what does this mean? every sample has both minor and major alleles? That does not make sense? 

It would be great for the authors to give an exact example of what the input looks like. 

Is there ablations on which modality is most useful? For example, is genetics useful at all since some works have shown that EHR information overrides with genetics signals. 

Also, why are only 700 SNPs used? there are 800K genotyped SNPs, if not considering imputed arrays. These could be used for pre-training. 

The authors used MMD disease as the prediction task. The data curation is also based on this task, which is limited.

There are many pre-trained foundation models for each modality, why not use them? but to train itself?

What are clusters in the Figure 2 and 3? There are little information with the current set of labels. Could the authors change to other more meaningful labels? 

What is "Mean Absolute Percentage Error"? 

Why do AUROC and AUPRC differ so much? For example in Table 4, E10-14, XGB has 0.859 the best AUROC but 0.162 worst AUPRC?

### Questions
Why Roberta model? It would be great to justify it.  

How exactly is pre-training conducted? The authors mention that masked modeling is used. But here which part is masked? since there are multiple modalities, is it modality-specific masking? or others? have the authors experimented with any varieties of masking strategies? 

"The genomics data, sourced from SNPs, was encoded to display only the minor and major allele in the sequence." what does this mean? every sample has both minor and major alleles? That does not make sense? 

It would be great for the authors to give an exact example of what the input looks like. 

Is there ablations on which modality is most useful? For example, is genetics useful at all since some works have shown that EHR information overrides with genetics signals. 

Also, why are only 700 SNPs used? there are 800K genotyped SNPs, if not considering imputed arrays. These could be used for pre-training. 

The authors used MMD disease as the prediction task. The data curation is also based on this task, which is limited.

There are many pre-trained foundation models for each modality, why not use them? but to train itself?

What are clusters in the Figure 2 and 3? There are little information with the current set of labels. Could the authors change to other more meaningful labels? 

What is "Mean Absolute Percentage Error"? 

Why do AUROC and AUPRC differ so much? For example in Table 4, E10-14, XGB has 0.859 the best AUROC but 0.162 worst AUPRC?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
