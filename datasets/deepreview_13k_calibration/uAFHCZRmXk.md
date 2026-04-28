# Two Effects, One Trigger: On the Modality Gap, Object Bias, and Information Imbalance in Contrastive Vision-Language Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Contrastive vision-language models (VLMs), like CLIP, have gained popularity for their versatile applicability to various downstream tasks. Despite their successes in some tasks, like zero-shot object recognition, they perform surprisingly poor on other tasks, like attribute recognition. Previous work has attributed these challenges to the modality gap, a separation of image and text in the shared representation space, and to a bias towards objects over other factors, such as attributes. In this analysis paper, we investigate both phenomena thoroughly. We evaluated off-the-shelf VLMs and find that while the gap's influence on performance is typically overshadowed by other factors, we find indications that closing the gap indeed leads to improvements. Moreover, we find that, contrary to intuition, only few embedding dimensions drive the gap and that the embedding spaces are differently organized. To allow for a clean study of object bias, we introduce a definition and a corresponding measure of it. Equipped with this tool, we find that object bias does not lead to worse performance on other concepts, such as attributes per se. However, why do both phenomena, modality gap and object bias, emerge in the first place? To answer this fundamental question and uncover some of the inner workings of contrastive VLMs, we conducted experiments that allowed us to control the amount of shared information between the modalities. These experiments revealed that the driving factor behind both the modality gap and the object bias, is an information imbalance between images and captions, and unveiled an intriguing connection between the modality gap and entropy of the logits.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a comprehensive study of contrastive VLMs, particularly examining why they excel at object recognition but struggle with attribute detection. The paper investigates how the modality gap and object bias affect downstream performance, and why these phenomena emerge.
The study supports these conclusions through extensive experiments using various models (particularly CLIP ViT-B/16 and SigLIP ViT-B/16) and datasets.

### Strengths
I've reviewed this paper and noticed many improvements from the previous version:
- Takeaway 1 is now much clearer. The section effectively demonstrates how common confounding factors affect results, and shows that when they control for these factors, a smaller modality gap indeed leads to better performance in downstream tasks.
- The authors have introduced a new metric called RMG, which successfully addresses the limitations of L2M.
- Takeaway 2 is interesting, and it leads nicely into Takeaway 3, which shows that we can actually reduce the modality gap using post-hoc methods.
- Overall, this is a well-written study that thoroughly examines both the modality gap and object bias in contrastive vision-language models.

### Weaknesses
 - I think most of weaknesses that have been seen in the previous submission was addressed.

### Questions
- For Takeaway 3, can you elaborate what "the modalities have different local neighborhoods" mean?

### Soundness
3

### Presentation
3

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
This paper extensively investigates the modality gap.
Different from the previous works, which hypothesize the modality gap is caused by the cone effect at model initialization or object biases, the authors analyze the modality gap from a modality information imbalance perspective.
They hypothesize the information imbalance between the two modality data (i.e., image and text) causes the modality gap and object bias, and demonstrate the hypothesis through extensive empirical studies.
In addition, they provide an analysis that how models lead to the modality gap with imbalanced image-text data.
Summarized 7 takeaways and corresponding analysis provide a novel insight into the modality gap research.

### Strengths
**[S1]** This paper introduced a new perspective on the modality gap, providing rich insight to the researchers and practitioners.

**[S2]** The paper is well-written and extensive experimental analysis is sufficient to validate their hypothesis and argument.

**[S3]** Proposed metrics to measure the modality gap (i.e., RMG) and object/attribute biases (i.e., MOAD) are well designed to intuitively compare the corresponding components.

**[S4]** The provided appendix is ​​sufficient to follow the details and experimental setting of the paper, enabling a better understanding.

### Weaknesses
 **[W1] Mismatch in the level of information imbalance between synthetic data and real data settings**
- The authors provide experimental validations on fully-controlled synthetic data and real data.
With synthetic data, information imbalance is defined based on the number of attributes, making it reasonable and sufficient to validate their hypothesis.
However, half/quarter captions of real data are derived by randomly dropping the part of captions.
I wonder if this strategy can hold the same hypothesis as in synthetic data. Please see Q2 below.

**[W2] The lack of evidence on actual pretrained VLMs**
- This paper suggests that the modality gap or the object bias can be reduced by data filtering or caption enrichment, and the performance can also be improved. However, there is a lack of analysis on real pretrained VLMs (e.g. pretrained CLIP and SigLIP) with large modality gaps. See Q3 below.

### Questions
**[Q1] L261**
- I think "with the largest mean" in L261 should be "with the largest mean differences."

**[Q2] Caption setup in Section F.1**
- The authors made the half and quarter captions by randomly dropping the part of a caption.
This approach may cause incompleteness in the caption itself rather than information imbalance.
Is there a strategy to verify the quality of the generated captions?
I think the paper would be better if there is an analysis using metrics that could verify that half/quarter captions are grammatically perfect but only contain different amounts of information.

**[Q3] Reverse process in Section 6.1**
- The authors provide the experimental validation by training the model with "full" captions and fine-tuning with "half" and "quarter" captions. It is reasonable and makes sense. But can we expect the same effect on the reverse process?
In other words, can the performance of the pretrained VLMs (e.g. CLIP, SigLIP in this paper), which have a large modality gap, be improved, while reducing the modality gap by fine-tuning on an enriched dataset?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
- This is an analysis paper, investigating the modality gap and object bias in VLMs. The authors argue that information imbalance is the root cause of both phenomena.
- A larger modality gap correlates superficially with better performance, but this is due to confounding factors like model size. Controlling for these shows that a smaller gap is beneficial.
- The authors introduce MOAD, a metric to measure object bias, and conduct experiments on synthetic and real-world datasets.
- They find that the modality gap is primarily driven by a few embedding dimensions and linked to entropy.
- Authors suggest that the model leverages the modality gap as a feature to manage prediction uncertainty.

### Strengths
- Clear and concise introduction of the problem, motivation, and takeaways.
- MOAD metric provides quantifiable measure of object bias.
- Well-designed experiments show compelling evidence for information imbalance hypothesis. Good coverage of 98 VLMs (e.g., CLIP and SigLIP).
- The proposed connection between the modality gap and entropy is intriguing

### Weaknesses
 - There could be more analysis on real-world datasets to help solidify the claims.
- [Minor] There could be more in-depth discussion on the limitations of the findings.
- [Minor] There could be more explanation of mitigating the information imbalance.
- [Nitpick] Typo: "Extend details for Section 5" -> "Extended details for Section 5")

### Questions
Can you provide examples of caption enrichment strategies that could effectively reduce the information imbalance?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates two potential causes of the inferior performance of contrastive VLMs on downstream attribute recognition (compared to the often good downstream object recognition performance), namely, modality gap and object bias. The paper suggests that both modality gap and object bias are not directly related to the inferior performance problem, though they claim that with better controls modality gap seems to somewhat related.
Finally, the paper does controlled experiments on small-scale dataset to confirm that information imbalance (i.e., the concepts that are present in image but not in the corresponding captions) in a dataset is strongly correlated with modality gap and object bias. Decreasing information imbalance seems to give better downstream attribute recognition performance.

### Strengths
1. The paper provides in-depth investigation of the relationship between the inferior performance of contrastive VLMs on downstream attribute recognition and two potential causes (modality gap and object bias). They show that the relation is not substantial (though they claim that with better control the relation on modality gap exists, but I am not personally convinced given their evidence). This is informative for people studying these two factors. Importantly, they demonstrate that information imbalance might be a more important (causal) factor to investigate.
2. They give evidence for reducing the information imbalance leads to better attribute recognition performance, as a solution to this problem on contrastive VLMs. They also provide a way to do this by using trainable temperature.
3. The experiments presented in the paper are in general well-controlled.

### Weaknesses
1. To me, the major claim in the paper is that information imbalance causes both modality gap and object bias, and that even though these two are not substantially correlated with attribute recognition performance, decreasing information imbalance mitigates them and seemingly increase the overall attribute recognition performance. However, the paper spends most of the content to demonstrate details on modality gap and object bias, many of which are overly detailed. For example: in section 4.2, the authors talk about many attempts to naively close the modality gap, all of which fails to keep the model performance. I think contents like this can be briefly summarised and the details can be put into supplementary materials, since these details might diverge into information that doesn't help readers grasp the core of the main claim.
2. The major claim is interesting and informative. However, the evidence of it is mainly done on the simple synthesised dataset MAD. The authors give evidence on real-world datasets in Figure7 (c), but the evidence on RMG is much weaker (if significant at all) compared to that with MAD. Since this is evidence for the major claim, the author might consider adding more experiments (more model architectures, more datasets, and presumably a better way to control the number of attributes) for this. The current evidence on real-world datasets is not compelling enough to support the claim that reducing information imbalance consistently improves attribute recognition across diverse scenarios. The lack of strong results on RMG, a more complex real-world dataset, raises concerns about the generalizability of the findings beyond the controlled synthetic setting.
3. The authors claim that “when we control for these factors, we observe the expected negative correlation, i.e., a smaller gap seems to correlate with better performance” (L245). However, the data they provided cannot support this claim, even when treating the significance values loosely. Some training datasets (e.g., DataComp-1B, OpenAI) clearly give positive correlation. The authors should consider removing this claim or providing more substantial evidence. The phrasing “seems to correlate” is too weak to justify the claim, especially given the contradictory evidence presented in the paper itself. A more rigorous analysis, potentially involving statistical significance testing across different datasets, would be needed to support such a strong statement.
4. The overall presentation of the paper is not ideal, in that many “questions” (e.g., “Is object bias explained by the global word frequencies of the dataset?”) can be turned into statements. The question-answering patterns in the writing highlight the motivations. However, in this paper there are so many of them, and the text devoted for completing this pattern probably does not worth it. The author might consider using more statements instead.

### Questions
1. I think detailed contents on modality gap and object bias can be put into supplementary materials, since these details might diverge into information that doesn't help readers grasp the core of the main claim.
2. The author might consider adding more experiments (more model architectures, more datasets, and presumably a better way to control the number of attributes) to show that RMG also decreases with less information imbalance.
3. The authors should consider removing the claim “when we control for these factors, we observe the expected negative correlation, i.e., a smaller gap seems to correlate with better performance” or providing more substantial evidence.
4. The author might consider converting most of the question-answering patterns in the paper to statements.
5. The field of "Partial Multi-Label Learning" seems to be relevant to this paper (as another way to solve the information imbalance). I wonder if the authors are aware of this and if this will give a better solution than trainable temperature.

### Soundness
3

### Presentation
2

### Contribution
3
