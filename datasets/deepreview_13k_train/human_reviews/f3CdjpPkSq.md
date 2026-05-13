# Action Sequence Augmentation for Action Anticipation

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Action anticipation models require an understanding of temporal action patterns and dependencies to predict future actions from previous events. The key challenges arise from the vast number of possible action sequences, given the flexibility in action ordering and the interleaving of multiple goals. Since only a subset of such action sequences are present in action anticipation datasets, there is an inherent ordering bias in them. Another challenge is the presence of noisy input to the models due to erroneous action recognition or other upstream tasks. This paper addresses these challenges by introducing a novel data augmentation strategy that separately augments observed action sequences and next actions. To address biased action ordering, we introduce a grammar induction algorithm that derives a powerful context-free grammar from action sequence data. We also develop an efficient parser to generate plausible next-action candidates beyond the ground truth. For noisy input, we enhance model robustness by randomly deleting or replacing actions in observed sequences. Our experiments on the 50Salads, EGTEA Gaze+, and Epic-Kitchens-100 datasets demonstrate significant performance improvements over existing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a data augmentation strategy (ActSeq) for the task of action anticipation. The paper recognizes multiple challenges of action anticipation - 1). multiple possible action sequences, 2). action ordering bias from the datasets, 3). interleaved actions from interleaved goals and present an augmentation strategy to address these challenges.

Given the action sequence video, video grammar is derived using Action Grammar induction algorithm. Then the cross-tree early parser predicts alternative next actions based on the observed actions and random modifications of insertion, deletion and replacement is further applied. Overall, this augmentation gives 3x (3 times) the size of the original dataset.

The method is evaluated on three action anticipation datasets - epic kitchens, egtea gaze+, and 50salads. The data augmentation strategy is incorporated with multiple prior works and their performance with and without augmentation is compared. These methods show improvement with data augmentation.

### Strengths
The paper addresses concrete challenges that arise in the task of action anticipation and presents a simple approach of data augmentation to address the ordering bias and multiple scenarios possibility when anticipating actions. The paper also presents an exhaustive evaluation on three action anticipation datasets. The idea of interleaved goals and interleaved actions is interesting.

### Weaknesses
The contribution and the novelty of the paper seem to be limited. Previous works [1,2] have explored some components of the proposed approach such as exploring grammar for activity prediction and data augmentation for temporal bias which is similar to the random modification of the proposed idea. Can the authors emphasize the contributions and especially the novelty of the work?




### Questions
The datasets explored in the paper predict only a single action given the observed actions. Would the proposed data augmentation strategy also work in scenarios where multiple actions (e.g. 20 actions) have to be predicted given the observed actions?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce a data augmentation strategy, where they synthetically generate plausible, unobserved sequences of actions that obey the constraints of a grammar they induce over the action labels. They demonstrate this helps performance across a variety of models and datasets.

### Strengths
1) The induction of a grammar over actions is vitally important due to the combinatorial nature of action sequence modeling. Actions can be arranged quite flexibly, and video datasets are not large enough to span all the variations over action sequences.
2) The rules of the grammar capture well capture the hierarchical and compositional nature of action. This grammar they've induced can be applied in other domains (e.g. robotics, action recommenders, etc), which otherwise would normally be handwritten.
3) The models and datasets were chosen well.

### Weaknesses
1) The results for Tables 8 and 9 are reporting Top 5. Top 1 results for action anticipation predictions are also helpful to see. Your data augmentation approach likely best improves the Top 5 results, but could possibly be hurting the Top 1 results by training over plausible but unlikely future actions.
2) A qualitative figure would be nice to see. Or at least a visualization of the trees for one of the datasets. 
3) I don't fully understand Table 1. Why are there negative values? There is no caption and the Figure is confusing. This figure is vital for understanding how Figure 3e) is constructed.

### Questions
1) Inducing a grammar over the observed actions is good, but I suspect an LLM could be used as an alternative source of action sequence augmentations, especially considering the Grammar operates only over narration-derived actions. Is there any reason to believe this isn't the case, or where one fails where the other would succeed? A qualitative example would be nice.
2) There's a paper (Therbligs for Action Understanding) [1] below that imposes a grammar over actions based on commonsense rules. They perform action anticipation as well, with improved performance due to these rules enabling the modeling of plausible sequences that abide by the rules. This paper should be included in the Related Works.
3) I wonder if this approach improves the data efficiency of a network, in that it needs less action sequences. This is claimed in Section 3 but not empirically explored (the way to do that would be to do an experiment where low-data model is compared with and without the augmentations).
4) Is there an augmentation strategy that rather than increase the augmentations by a set factor, uses the set of all plausible sequences for data augmentation?


[1] Dessalene, Eadom, et al. "Therbligs in action: Video understanding through motion primitives." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Thanks the authors for this ICLR submission.

Summary:

This work identifies two major problem in action anticipation research: **1)** the default dataset split-up only allows for partial exploration over the entire action space, and **2)** noisey action labels induced by the imperfect preprocessing step (e.g., action recognition). To this end, this paper proposes a data augmentation method to enhance both the observable context and the prediction target (i.e., future steps). Moreover, a more noisy-robust version of data is generated by randomly deleting or replacing action elements.

### Strengths
- Easy to follow.
- Nice discussion on the three main issues in action anticiaption from line34-45!
- Approach is technical sound. Although, as mentioned in the future work, the optimal solution is to perfectly de-compose interwined action sequences, the method in this paper serves as a practical temporary solution.  
- Interesting study on the order bias. 
- Some Improvements over standard benchmarks across a variety of baseline methods.

### Weaknesses
 - (Minor) The manuscript could be written better
    - Inconsistent dataset name in Table 3 & 4 and line 407 - EGTEA Gaze+, EGTEA Gaze, EGTEA. Please consider make the dataset names consistent throughout the submission, which will make it easier to follow and make connections.
    - Table 7, 8 & 9 captions are sentences, and should be ended with period. Please follow the basic academic writing protocol to better the  the wrtting.
    - Given no appendix, it is better to explain the evaluated **verb, noun, action** items for epic-kitchen. Please include a section explaining the evaluated items and/or terminology. It is recommended that academic paper should be self-contained, so that readers can find all information within a single paper.  

- (Minor) The MAOB study is interesting, yet it is incomplete - none has been done to other experimented datasets (e.g., EGTEA and Epic-Kitchen). I would like to suggest extending such study to the EGTEA and Epic-Kitchen-100 datasets. It will be insightful to check the correlation between the reduction of order bias and the performance improvements, which will be a strong supporting evidence for th ActSeq. method to be accepted. 
- (Minor) From Table 3 & 4, it is seen that the amount of useful information does not scale well the times (`X`) of augmentation, which is a concern. The solution to settle down the **X** hyperparameter seems critical. Please provide some discussion on the trade-offs here and initialize some considerations on how to decide this hyper-parameter.  
- (Minor) This method requires really large number of augmentations, e.g., **12X** more sequences, to bring significant improvements (e.g., > 1 % in **Recall**). Arguably, it costs much longer training time and compute resources, specially on large datasets. The efficiency is questionable. Please provide information on the computational costs of their method compared to baseline approaches, or to discuss potential strategies for improving efficiency while maintaining performance gains.
- (Minor) It would be remiss to ignore similar ablation study as in Table 3 & 4 on the other two datasets, i.e., 50 Salads and Epic-Kitchen-100, as they differ from the EGTEA Gaze+ in size, domain and data distribution. Showing more information will be essential to better evaluate the generalizability of the ActSeq. method. Please consider complete the ablation section with such experiments.

Missing reference:
- On diverse asynchronous activity anticipation, ECCV  2020.

### Questions
see weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces ActSeq, a data augmentation method for video action anticipation. To address the ordering bias in the training data, authors built a grammar base and alternate videos based on the grammar. Both observations and future action are alternated. The proposed method is evaluated on 50Salads, EGETA Gaze+, and EPIC-Kitchens-100. Results show ActSeq improves baseline methods consistently.

### Strengths
1) This paper tackels an important issue of action anticipation
2) The action goal is specifically modeled and can be interpreted
3) The proposed augmention method obtains promissing results on benchmark datasets.

### Weaknesses
1) For equation1, same atomic actions may appear multiple times in a video, the count may not be accurate.
2) One action may have more than one prerequisite actions, only modeling the pairwise dependencies may not be optimal since the high-order dependencies are not considered.
3) Some atomic actions have higher frequencies in training data, which leads may affect the AGI model
4) There are few comparison with other augmentations methods. Only random processing is compared in Table 6. Simple augmentation methods, such as rotation and adding random noise, may also improve the performance. To demonstrate the superiority of ActSeq, a comparison with other augmentation methods is preferred.
5) Details of generating augmented videos are missing

### Questions
1) How are the videos manimpulated? Do the augmented videos look realistic?
2) From the reulsts in Tables 3-5, why 5x augmentation is worse than 3x?

### Soundness
2

### Presentation
3

### Contribution
2
