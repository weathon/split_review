# When Hard Negative Sampling Meets Supervised Contrastive Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3

## Abstract
State-of-the-art image models predominantly follow a two-stage strategy: pre-training on large datasets and fine-tuning with cross-entropy loss. Many studies have shown that using cross-entropy can result in sub-optimal generalisation and stability. While the supervised contrastive loss addresses some limitations of cross-entropy loss by focusing on intra-class similarities and inter-class differences, it neglects the importance of hard negative mining. We propose that models will benefit from performance improvement by weighting negative samples based on their dissimilarity to positive counterparts. In this paper, we introduce a new supervised contrastive learning objective, SCHaNe, which incorporates hard negative sampling during the fine-tuning phase. Without requiring specialized architectures, additional data, or extra computational resources, experimental results indicate that SCHaNe outperforms the strong baseline BEiT-3 in Top-1 accuracy across various benchmarks, with significant gains of up to $3.32\%$ in few-shot learning settings and $3.41\%$ in full dataset fine-tuning. Importantly, our proposed objective sets a new state-of-the-art for base models on ImageNet-1k, achieving an 86.14\% accuracy. Furthermore, we demonstrate that the proposed objective yields better embeddings and explains the improved effectiveness observed in our experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new loss, SCHaNe, for supervised contrastive learning. The main idea of this novel loss is that introducing importance weights for negative samples based on their dissimilarity plays a significant role in improving performance. Experiments show that SCHaNe is an effective method for enhancing performance on various datasets, particularly in few-shot tasks.

### Strengths
1. The assumption that this paper aims to validate is both simple and easy to understand. Furthermore, the proposed objective is straightforward and intuitive. 
2. There is a clear improvement in performance when compared with the conventional cross-entropy loss. 
3. The paper is generally well-organized and presents its content logically.

### Weaknesses
1. One of the main weaknesses I've identified is that the primary baseline used in this paper is Cross-Entropy (CE) loss, not Supervised Contrastive Learning (SupCon). If the paper's central claim is that 'introducing importance weights for negative samples based on their dissimilarity plays an important role,' then I believe SupCon should be the main baseline for comparison. Although SCHaNe outperforms SupCon in the few-shot setting as shown in Table 3, the inclusion of SupCon results in other settings—such as in Table 1, Table 2, and Figure 4—could strengthen the paper. The current comparison to CE loss, while showing improvement, does not directly validate the core claim about the importance of dissimilarity-based weighting within a contrastive learning framework. A more rigorous evaluation would involve comparing against SupCon with different weighting schemes or variations of hard negative mining, to isolate the specific contribution of the proposed weighting method.
2. BEiT-3 is primarily utilized as the main architecture. The Future Work section suggests that extending this method to various architectures may be promising, but I believe that evaluating the proposed method across different architectures should be included in this paper. The lack of experiments on diverse architectures limits the generalizability of the findings. For example, it is unclear how SCHaNe would perform with CNN-based architectures, or with transformers of different sizes and configurations. The paper should demonstrate that the performance gains are not specific to BEiT-3 by including results on a variety of models with different inductive biases.
3. The proposed method appears to be limited in its applicability to various tasks, such as dense prediction tasks. While this may not be a significant drawback, explicitly stating this limitation could enhance the paper. Moreover, the paper claims that “Our SCHaNe objective function can be applied using a wide range of encoders, such as BERT for natural language processing tasks,” yet there are no experiments provided to substantiate this claim. The absence of experiments on NLP tasks or dense prediction tasks raises concerns about the scope and versatility of the method. The paper should either provide evidence for these claims or temper them to reflect the actual experimental scope. The lack of experiments in these areas makes the claims feel unsubstantiated.

Minor: The presentation of the paper could be improved. For instance, the notation in Equations 2-4 is confusing. If I understand correctly, $\beta$ should vary with the index, but it might be misunderstood as a constant since it lacks an index. In Equation 2, $z$ denotes the label, which is not the case in Equations 3 and 4. Regarding Figure 4, while the trend is important, we cannot directly compare the accuracies across various downstream tasks in an 'apple-to-apple' manner.

### Questions
Please see the weaknesses section above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduced a novel supervised contrastive learning objective function called SCHaNe. SCHaNe enhances model performance without requiring specialized architectures or additional resources. The proposed approach combines supervised contrastive learning with hard negative sampling to optimize the selection of positive and negative samples, thereby achieving state-of-the-art performance.

### Strengths
1.	This paper proposes a novel supervised contrastive learning objective function, SCHaNe, which incorporates hard negative sampling during the fine-tuning phase. 
2.	The proposed method achieves state-of-the-art performance on ImageNet-1k and outperforms the strong baseline BEiT-3 in Top-1 accuracy across twelve benchmarks, with significant gains in few-shot learning settings and full-dataset fine-tuning.

### Weaknesses
Strengths*
1.	This paper proposes a novel supervised contrastive learning objective function, SCHaNe, which incorporates hard negative sampling during the fine-tuning phase. 
2.	The proposed method achieves state-of-the-art performance on ImageNet-1k and outperforms the strong baseline BEiT-3 in Top-1 accuracy across twelve benchmarks, with significant gains in few-shot learning settings and full-dataset fine-tuning. 
Weaknesses*
1.	The paper could benefit from a more detailed comparison with existing methods. While the authors compare the proposed method with the strong baseline BEiT-3, they do not compare it with other similar state-of-the-art methods [1][2] in the field.
2.	The starting point of the work [2] is very similar to this article. I hope the author can further clarify the relationship with it so that readers can further understand the core starting point of the article.

### Questions
1.	Can the authors provide a more detailed comparison and analysis with existing methods? See the Weaknesses section for details.
2.	In Table 3, the performance of the CE + SimCLR method is much lower than that of the CE method alone. At the same time, according to the description in the table, Label is not used in this part. How is this part of CE implemented, and why does the performance drop after adding SimCLR?
3.	If possible, can the method proposed in this article be easily integrated into other models (such as other pre-trained models or other few-shot learning methods) like BEiT-3? I hope the article can give relevant explanations and results.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new supervised contrastive learning objective function called SCHaNe, which addresses the limitations of the cross-entropy objective function used in pre-trained image models. SCHaNe incorporates hard negative sampling during fine-tuning to enhance the efficacy of contrastive learning. Experimental results demonstrate that SCHaNe outperforms the baseline model BEiT-3 in Top-1 accuracy across twelve benchmarks, with significant gains in few-shot learning settings and full-dataset fine-tuning. The proposed objective function sets a new state-of-the-art for base models on ImageNet-1k, achieving an accuracy of 86.14%. Additionally, the paper shows that SCHaNe produces better embeddings and explains the improved effectiveness observed in the experiments. Overall, the contributions of this work include the introduction of SCHaNe and its superior performance in few-shot learning and full dataset fine-tuning, establishing new state-of-the-art results.

### Strengths
1. The method has been validated on multiple datasets, and comprehensive experiments have been conducted on downstream datasets.

2. The work appears to be relatively comprehensive, with a clear motivation, detailed method description, and important parameter ablation experiments. Overall, it seems well-executed and promising.

### Weaknesses
1. To enhance the credibility of our research, you should consider using the same base models (such as ViT or Swin) as other studies for our baseline in Table 1 and Table 2.

2. In order to provide a more comprehensive analysis, the results in Table 1 and Table 2 should include the performance of contrastive learning without the hard negative mining method.

3. The representation of Formula 3 needs to be clarified to ensure better understanding, as it is currently not very clear.

4. To provide a more complete comparison, Figure 3 and Figure 4 should include the results of BEiT-3-CE + contrastive learning, in addition to the results of our proposed method.

5. In each comparative experiment, it is important to clearly indicate the improvement achieved by the hard negative mining method on top of the performance obtained with CE + contrastive learning. This will help demonstrate the added value of our approach.

### Questions
1. Why did you choose BEiT-3 as your base model? There are other base models like DINOv2, CLIP, etc.

2. Cross-entropy and contrastive learning have similar forms, so why is the hard negative sampling only applied to the contrastive learning part and not to the cross-entropy part?

3. In general, fine-tuning with cross-entropy (CE) loss is not strongly coupled with the batch size, while contrastive learning can be affected by the batch size. This can limit the flexibility of fine-tuning with CE when combined with contrastive learning. What are your thoughts on this issue?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
