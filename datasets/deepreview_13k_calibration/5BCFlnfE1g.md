# Demystifying CLIP Data

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 6, 8

## Abstract
Contrastive Language-Image Pre-training (CLIP) is an approach that has advanced research and applications in computer vision, fueling modern recognition systems and generative models. We believe that the main ingredient to the success of CLIP is its \textit{data} and \textit{not} the \textit{model} architecture or pre-training {objective}. However, CLIP only provides very limited information about its data and how it has been collected, leading to works that aim to reproduce CLIP's data by filtering with its model parameters. 
In this work, we intend to reveal CLIP's data curation approach and in our pursuit of making it open to the community introduce Metadata-Curated Language-Image Pre-training (MetaCLIP). 
MetaCLIP takes a raw data pool and metadata (derived from CLIP's concepts) and yields a balanced subset over the metadata distribution. 
Our experimental study rigorously isolates the model and training settings, concentrating solely on data.
MetaCLIP applied to CommonCrawl with 400M image-text data pairs outperforms CLIP's data on multiple standard benchmarks. 
In zero-shot ImageNet classification, MetaCLIP achieves 70.8\% accuracy, surpassing CLIP's 68.3\% on \mbox{ViT-B} models. Scaling to 1B data, while maintaining the same training budget, attains {72.4\%}. Our observations hold across various model sizes, exemplified by  ViT-bigG producing {82.1\%}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a data curation pipeline for CLIP training. The paper evaluates the model performance resulting from different data curation pipelines, and shows that the proposed pipeline outperforms closed-source CLIP, as well as Open CLIP. Moreover, an interesting finding from the paper is that balancing the metadata distribution is the key to improving performance.

### Strengths
- The paper tackles an important problem in the community regarding the opacity of data curation processes of foundation models. Moreover, it promises to open-source part of the efforts, including data curation code and training data distribution.

- The paper is also strong in terms of empirical evaluation, including various data sizes, and different implementations of the balancing steps. Huge resources are devoted to the evaluation part.

### Weaknesses
 - The main weakness lies in the technical novelty. The paper is a commendable effort to reproduce the data curation pipeline that has already been described in the original CLIP paper (Radford et al, 2021), and report the findings for reproducing an existing data curation technique. The paper's novelty can be greatly enhanced by exploring some new technical components beyond what's already described in Radford et al 2021.

 - Page 3"this post-hoc data pruning approach has limited utility, as the computational resources saved have already been expended during the initial training of the model." The reviewer has some concern regarding this comment. While posthoc data pruning still requires training an initial model, the pruned dataset can also allow efficient model improvement, which is usually an iterative process involving experimentation with different model hyperparameters.

 - Is there a specificreason to omit some other data curation baselines proposed in the DataComp paper?

 - What is the meta data distribution for OpenCLIP?

### Questions
1. Page 3"this post-hoc data pruning approach has limited utility, as the computational resources saved have already been expended during the initial training of the model." The reviewer has some concern regarding this comment. While posthoc data pruning still requires training an initial model, the pruned dataset can also allow efficient model improvement, which is usually an iterative process involving experimentation with different model hyperparameters.

2. Is there a specificreason to omit some other data curation baselines proposed in the DataComp paper? 

3. What is the meta data distribution for OpenCLIP?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims at reproducing the data collection and construction process of the original CLIP, which is still unknown to the reserach community, despite of the brief introduction in the CLIP paper, and some followup public datasets like LAION or DataComp. Specifically, it first collects some high-quality metadata based on Wikipedia and WordNet, uses them to retrive text entry from snapshots of CommonCrawl, and employs a balancing strategy to build a more diverse and balanced data distribution. The CLIP model trained on the resulting dataset shows comparable or superior performance compared to CLIP or OpenCLIP.

### Strengths
1. The effort to reproduce the exact data construction procedure of the original CLIP paper is well motivated and appreciated. As the authors pointed out, the later datasets like LAION or DataComp, all adopt trained CLIP model during data collection. How to build a high-quality and diverse image-text dataset from scratch, like WIT400M, is still a mystery to the community.
2. Given that CLIP is such a important foundation model that connects image and text, the data crafting pipeline and the resulting dataset are of clear importantce to the community. Also, the lessons learnt in this work could potentially benefit future efforts to construct high-quality open datasets in other areas as well.
3. The writing is good. The overall logistics follow a reasonable thread of investigation.
4. The performance of the model trained on MetaCLIP often show superior performance compared to LAION or WIT.

### Weaknesses
1. I find that the authors use the average accuracy across multiple datasets as a major performance metric throughout the paper. This is examplified by table 4/5 in the main texts, and also some tables in the appendix. This does not make sense to me. Those datasets come with different number of classes and number of samples. For instance, averaging the accuracy of a dataset of 10 classes (e.g. EuroSAT), and a dataset of 102 classes (e.g. Flowers), is unreasonble, because misclassifying all samples in one class corresponds to 10% accuracy in the former dataset, but corresponds to ~1% accuracy in the former dataset. I know that some other works, like DataComp, also keep this practice. But I feel a more reasonable approach is to compare the performance on individual datasets, and how many datasets on which the MetaCLIP model prevails. As such, the authors should list results on individual datasets, not report some average accuracies.

2. Following previous one, I find results in table 8 in appendix tend to be more comprehensive, as the model is also evaluated on ImageNet distribution shift datasets and retrieval datasets. The organization of this paper can be enhanced if the table 4/5 in the main text also report results on those dataset.

3. Some data filtering details could be further detailed. For example, the last sentence in page 4 (sorry but this submission does not have a line number) talks a bit about some *noise reduction... (e.g., regular expression on dates, ids etc.)*. Also, figure 5 in the appendix shows some *URL & Text Dedup* and *NSFW Image Dedup*, but does not describe them in details. The authors are encouraged to list more detailed descriptions on those noise reduction and deduplication processes, and also explain their effects on the resulting dataset.

### Questions
1. How does different choices of metadata affect the final dataset? I know the authors follow the procedure listed in the original CLIP paper, but I feel like the decision to use Wikipedia and WordNet can be futher explained by 1) either a comprehensive distribution probing or visualization of the metadata used in the paper (right now only top-20 entried are showed, and they seem very general and vague wordings); 2) remove some metadata sources (like no wordnet synset), or tune the threshold hyper-parameters like PMI or view frequency.

2. Could in data construction process inspire data creating efforts in other areas? The authors are encouraged to add some related discussion, possibly in a *broader impact* section.

3. In section 4, it is mentioned multiple times that using a smaller *t* can *increases tail metadata matches*, like the last sentence in page 7. But my understanding is that a smaller *t* only leads less matches of head metadata, while all the matches of tail metadata are kept. Am I understanding it wrong?

4. Since randomness is introduced in the balancing stage, I wonder how much impact does it have with different random seeds?

5. Will the authors released detailed code (not just some demo) to reproduce their whole pipeline of data curation from scratch? For this work, I think it is not the resulting dataset MetaCLIP that is most valuable. How the authors arrive at the final dataset from some wiki pages and wornet synets to the final collection of diverse and high-quality image-text pairs really matters, and could make a big difference and push the community forward once open sourced.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper attempts to uncover the data curation process of the CLIP paper by Radford etc. The curation process is composed of several steps: 1) 500k entry construction 2) text2entry matching 3) entry2text indexing 4) entry balancing. Applying this pipeline to the CommonCrawl dataset, the resulting dataset achieves even better performance CLIP.

### Strengths
1. After almost three years the CLIP paper came out, it is great to see efforts following and investigating the data curation pipeline in the CLIP paper, whose proposed data diversification (balancing) was ignored by the other works, such as LAION. The paper would be interesting to the researchers working on data curation, and contrastive pre-training, too.
2. The experimental results are impressive and set the new state of the art.

### Weaknesses
1. The contribution of the paper is limited. The main contribution is the entry balancing used by CLIP. This balancing operation actually plays a similar role to the deduplication used in [1] and [2], where its effectiveness has been proven. Specifically, both entry balancing and deduplication aim to reduce redundancy and improve the diversity of the training data. While entry balancing achieves this by equalizing the number of samples per entry, deduplication, as described in [1] and [2], removes near-duplicate samples based on similarity metrics. Therefore, the novelty of the entry balancing approach is somewhat incremental, given the existing work on deduplication.

2. In Sec 3.4, when sub-sampling image-text pairs for each entry, in addition to the information density based rule, it is worth trying some model-based rules, e.g., image-text matching based rules. Although the paper mainly aims to reproduce the CLIP paper's results, it would lead to more contributions to go beyond CLIP reproduction and curate higher-quality datasets. For instance, one could incorporate a pre-trained image-text matching model to score the relevance of each pair and prioritize those with higher scores. This could potentially filter out noisy or irrelevant pairs more effectively than the information density rule alone.

### Questions
1. How many runs are conducted to get the quantitative experimental results in the paper (e.g., Table 4 and 5)? Are the standard deviations sufficiently smaller than the differences between different settings?
2. Any analysis on where the improvement over CLIP dataset is from in Table 4? Different raw data sources?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of the paper try to replicate the curation process employed by OpenAI to train their CLIP models. To that end, they highlight important excerpts from the original CLIP paper, and they try to replicate them as close as possible. The models trained on the resulting dataset show improved performance in imagenet zero-shot accuracy.

### Strengths
- the paper highlights several important excerpts form OpenAI's curation technique and tries to replicate them
- the authors do an ablation study over their choices to validate whether their choices are helpful
- the authors plan to release the curation data to the community

### Weaknesses
- the evaluation shows improvement in some downstream tasks, but not others. it would be nice to investigate this mixed performance, as to make sure that the curation technique is extremely tailored towards imagenet. Specifically, the paper should provide a detailed analysis of the tasks where the method does not improve performance, and discuss potential reasons for this. For instance, are there specific characteristics of these tasks that make them less amenable to the proposed curation technique? Are there biases in the curated data that negatively impact performance on certain tasks?
- there are other proposed approaches [1] for recreating WIT-400M, however, the authors do not compare their proposed approach with other approaches. This is a significant omission, as a comparative analysis would help to establish the relative strengths and weaknesses of the proposed method. The paper should include a comparison with at least the approach in [1], focusing on aspects such as the quality of the curated data, the computational cost of the curation process, and the performance of models trained on the resulting datasets.

### Questions
- how does the curation step proposed in this paper compare with the one used for LAION-400M
- can you please explain why your curation is not overfit towards ImageNet?
- can you please compare against approaches in datacomp?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
