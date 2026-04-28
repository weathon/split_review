# Effective pruning of web-scale datasets based on complexity of concept clusters

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 8, 3, 5

## Abstract
Utilizing massive web-scale datasets has led to unprecedented performance gains in machine learning models, but also imposes outlandish compute requirements for their training.
In order to improve training and data efficiency, we here push the limits of pruning large-scale multimodal datasets for training CLIP-style models. Today's most effective pruning method on ImageNet clusters data samples into separate concepts according to their embedding and prunes away the most prototypical samples. We scale this approach to LAION and improve it by noting that the pruning rate should be concept-specific and adapted to the complexity of the concept. Using a simple and intuitive complexity measure, we are able to reduce the training cost to a quarter of regular training. By filtering from the LAION dataset, we find that training on a smaller set of high-quality data can lead to higher performance with significantly lower training costs. More specifically, we are able to outperform the LAION-trained OpenCLIP-ViT-B/32 model on ImageNet zero-shot accuracy by 1.1p.p. while only using 27.7\% of the data and training compute. 
Despite a strong reduction in training cost, we also see improvements on ImageNet dist. shifts, retrieval tasks and VTAB.
On the DataComp Medium benchmark, we achieve a new state-of-the-art ImageNet zero-shot accuracy and a competitive average zero-shot accuracy on 38 evaluation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper seeks to prune large-scale multimodal datasets (e.g., LAION) for training CLIP-style models for training and data efficiency. Building upon SSP-pruning, Density-Based-Pruning picks the number of samples per cluster based on the overall complexity of a particular cluster, and achieves state-of-the-art results on LAION.

### Strengths
1.	This paper proposes Density-Based-Pruning to improve data efficiency on large-scale multimodal datasets.
2.	This paper conducts detailed hyperparameter selection experiments, which made the experimental results more convincing.

### Weaknesses
1.	The related work section contains excessive content, and there is a considerable amount of duplication. Besides, it is better to introduce “coreset selection[1-3]”, as it is closely related to your work.

2.	Missing some baselines for comparison, including random selection and other data pruning methods [3-4].

3.	The description in the methods section is very confusing.

4.	In Fig. 4(right), more sample points are needed for convincing conclusions.

5.	In Table 2, it would be better to include SSP-Pruning as a baseline for comparison.

6.	The tasks are relatively simple (ImageNet zero-hot). Could we compare DBP with other baselines on different tasks?

7.	In the methods section, the filtering pipeline includes deduplication, CLIP score filtering, and Density-Based Self-Supervised Prototypes pruning. However, there is no description about CLIP score filtering. The description about deduplication does not provide me with any useful information.

### Questions
1.	In Fig. 4(right), more sample points are needed for convincing conclusions.
2.	In Table 2, it would be better to include SSP-Pruning as a baseline for comparison.

3.	The tasks are relatively simple (ImageNet zero-hot). Could we compare DBP with other baselines on different tasks?
4.	In the methods section, the filtering pipeline includes deduplication, CLIP score filtering, and Density-Based Self-Supervised Prototypes pruning. However, there is no description about CLIP score filtering. The description about deduplication does not provide me with any useful information.

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
The paper proposes a dataset pruning method broadly applicable to web scale datasets such as LAION. The authors build upon important prior work at the ImageNet scale (SSP-Pruning, Sorscher et al., 2022), which attempts to rebalance a dataset by clustering, and then sampling datapoints inversely proportional to their cluster centroids. The authors improve upon this procedure by noting that clusters have varying degrees of importance, both as a result of the average distance of points from the centroid as well as the average distance of the centroid from other centroids, and determine the proportion of samples to be pruned proportional to the importance. The authors demonstrate the supremacy of this method, DPB, through an array of experiments that the pruned datasets jointly save on compute while increasing overall performance.

### Strengths
The paper's extensive analysis of their new method across multiple datasets and benchmarks makes a compelling case for the high performance of their method. The dimensions of ablations, and the high level takeaways from those ablations in the results section are clear -- DBP outperforms SSP Pruning, outperforms CLIP filtering, DBP outperforms SemDeDup alone, and Deduplicaiton is crucial to the success of the method. These takeaways make the contribution quite compelling.

### Weaknesses
The core weaknesses concern clarity of the results, and the overall difficulty in connecting the many different - at times seemingly disparate - results that are thrown together in the narrative.

For one, the paper begins by proposing an improvement to SSP, but defers any result about the paper to a small table in the appendix, for a single model and single dataset -- it would help to do a more comprehensive evaluation to make clear the improvement being proposed. The authors attempt to briefly make a broader connection that their work is akin to density based pruning -- this is where the relative lack of optimization over the number of clusters -- which very much controls how the density is approximated -- is puzzling. Indeed, the 5 point plot of Figure 6-d leaves much to want, where we are led to believe 500 is the best, because it is better than 100 (?) and 10000. More ablations here would help clarify things. In general, more time assessing Density based pruning methods (e.g. for a datapoint, if its k nearest neighbors approximate it well, it can be discarded) would significantly improve the narrative of the paper. 

On the other hand, the quadratic program, though interesting and unexpected in a paper of this type, seems like overkill -- assigning the maximum number of points to each cluster whose expected number of samples is above the maximum, and redistributing the remaining samples proportionally among the remaining clusters (and repeating) seems like it would achieve what the authors are seeking to do (if not exactly what the QP does) without the overhead of a QP solver, and all the space in the paper it consumes. 

The discussion section would benefit from a more clear discussion of where the shortcomings of the method are relative to the other methods presented in the paper. For example, DBP does a tiny bit better than TMARS on Imagenet, but more significantly worse on Imagenet Dist and Average but a discussion of the latter point is entirely missing. Whether pruning in a density based manner affects model robustness seems like a subject at least worth touching on. Same for the retrieval plot in Figure 4 -- why is it that SemDeDup does worse than LAION-440B, but DBP catches up? An analysis of what is happening here would help understand the paper considerably. 

Beyond that, the many different numbers in the paper -- as a result of different filtering models (CLIP-B16 or CLIP-L/14), differing number of epochs, differing initial dataset size (LAION-50M or 440M) -- make the results very difficult to connect and piece together across tables and figures. If some consistency across variables were afforded -- or at least enough ablations such that there is an extra column in each table connecting the numbers in other tables to that table, it would make the information much easier to process.

### Questions
If the intuition is that it is density based pruning, why only 500 clusters? The 5 point plot of figure 6-d suggests that clusters between 100 and 10000 should be better explored since there are sharp peaks in that range. 

Figure 5: Why not use concatenate CLIP's text + image embedding?

How is it that SemDeDup does worse than LAION-440M for VTAB, but DBP does better?

A notable decrease in performance on ImageNet dist shifts and Retreival tasks -- does the DBP type of pruning hurt generally hurt robustness? 

Why use CLIP-B16 Score for Figure 3, but CLIP-L/14 Score for Table 1?

Update: thank you for taking the time to answer my questions, they are sufficiently addressed.

### Soundness
3 good

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
This work scales SSP-Pruning to web-scale datasets, investigate how the complexity of different concepts within a dataset can be used for pruning, and report further improvements over regular SSP-Pruning. They evaluate it with CLIP pre-training and report the results on classification task: it shows data efficiency in terms of pre-training.

### Strengths
The paper is well structured and the motivation is clear. It is interesting to study the data efficiency of CLIP pre-training to reduce the computational resources.

### Weaknesses
1. The biggest concern I have is about the technical novelty. The main idea is based on SSP-Pruning. Therefore, the technical contribution is very trivial. 
2. This work only reports the results on image classification. How about the zero-shot results of CLIP in retrieval tasks, such as COCO/Flickr30k image-to-text and text-to image retrieval? The zero-shot retrieval performance is also very important to measure the quality of pre-training and the effectiveness of the proposed method. The paper mentions about the retrieval task and shows some results in Figure 3 but I am not sure the implementation details: which dataset do they use? It would be helpful to report the results on standard benchmark (COCO/Flickr30k). 
3. The method involves CLIP-score filtering to curate a new dataset to train CLIP. I am unsure if such involvement is fair, as the filtering itself is similar to distilling some knowledge from a well-trained CLIP. Then, the new CLIP is somehow learning from the well-trained CLIP on large-scale datasets. Therefore, it may not be fair to claim the data efficiency for the proposed method.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on improving the training and data efficiency of CLIP-style models by pushing the limits of pruning large-scale multimodal datasets. By adapting the pruning rate to the complexity of different concepts within the dataset, the authors are able to reduce training costs to a quarter of regular training. They outperform the LAION-trained OpenCLIP-ViT-B/32 model on ImageNet zero-shot accuracy by 1.1 percentage points while using only 27.7% of the data and training compute. Additionally, they achieve a new state-of-the-art ImageNet zero-shot accuracy and competitive performance on 38 evaluation tasks in the DataComp Medium benchmark. The findings demonstrate the potential of pruning methods for improving the efficiency of training multimodal models.

### Strengths
1. The method proposed in this paper exhibits a certain degree of novelty.
2. The paper extensively validates its findings using a large-scale experimental dataset, although experiments with even larger models were not performed.
3. The practical applicability of the approach presented in this paper suggests its value in real-world scenarios.

### Weaknesses
1. We cannot determine if the current data is effective for training ViT-B-16 and ViT-L-14 models.
2. The majority of the experimental evaluation metric is Imagenet zero-shot top1. Is there any bias in the algorithm towards Imagenet data?
3. Detailed results for each dataset in VTAB are not provided.
4. The difference between DBP and SSP-Pruning is the choice of how many examples are taken from each cluster. It seems that innovation has some shortcomings
5. In Fig.3, 222M performs worse zero shot accuracy than 166M, please give a reasonable explanation.
6. Why weren't models of the same size, such as CLIP ViT-L-14, OPENCLIP LAION400M ViT-L-14, EVA ViT-L-14, and DINOv2 ViT-L-14, used for clustering comparisons?

### Questions
In this paper， the author scales SSP-Pruning to web-scale datasets and demonstrates that the pruning criterion can also transfer to the DataComp benchmark.
Q1: In Fig. 1, the author shows they reduced the LAION-CAT440M to 166M and improved the zero-shot performance on Imagenet, can you provide more results? such as zero-shot transfer and linear probe performance on different datasets.
Q2: Does the robustness of model training change when the dataset size is reduced? Please provide robustness evaluation results.
Q3: The difference between DBP and SSP-Pruning is the choice of how many examples are taken from each cluster. It seems that innovation has some shortcomings
Q4: In Fig.3, 222M performs worse zero shot accuracy than 166M, please give a reasonable explanation.
Q5: Why weren't models of the same size, such as CLIP ViT-L-14, OPENCLIP LAION400M ViT-L-14, EVA ViT-L-14, and DINOv2 ViT-L-14, used for clustering comparisons?
Q6:

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
