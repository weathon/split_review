# Retrieval-based Zero-shot Crowd Counting

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Existing crowd-counting methods rely on the manual localization of each person in the image. While recent efforts have attempted to circumvent the annotation burden through vision-language models or crowd image generation, these approaches rely on pseudo-labels to perform crowd-counting. Simulated datasets provide an alternative to the annotation cost associated with real datasets. However, the use of large-scale simulated data often results in a distribution gap between real and simulated domains. To address the latter, we introduce knowledge retrieval inspired by knowledge-enhanced models in natural language processing. With knowledge retrieval, we extract simulated crowd images and their text descriptions to augment the image embeddings of real crowd images to improve generalized crowd-counting. Knowledge retrieval allows one to use a vast amount of non-parameterized knowledge during testing, enhancing a model's inference capability. Our work is the first to actively incorporate text information to regress the crowd count in any supervised manner. Moreover, to address the domain gap, we propose a pre-training and retrieval mechanism that uses unlabeled real crowd images along with simulated data. We report state-of-the-art results for zero-shot counting on five public datasets, surpassing existing multi-model crowd-counting methods. The code will be made publicly available after the review process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes ReZeS-Count, a retrieval-based framework for crowd counting under zero-shot conditions by leveraging both visual and textual information from a simulated dataset. The approach employs knowledge retrieval to incorporate multi-modal data, enhancing the inference capabilities of the model on real, unlabeled crowd images. Extensive experiments demonstrate that ReZeS-Count achieves state-of-the-art performance across multiple datasets, showcasing the effectiveness of retrieval-based zero-shot learning for crowd counting.

### Strengths
1. This approach effectively bridges the gap between simulated and real data by leveraging multi-modal retrieval and weakly-supervised learning.

2. ReZeS-Count outperforms existing annotator-free and self-supervised methods across multiple public datasets, establishing itself as a robust zero-shot crowd-counting method.

3. The paper provides extensive ablation studies, assessing the impact of various components and retrieval configurations, which offers valuable insights into the effectiveness of different aspects of the model.

### Weaknesses
1. The title “Retrieval-Based Zero-Shot Crowd Counting” may not fully align with the actual methodology presented. The approach is more akin to cross-dataset crowd counting rather than true zero-shot learning, as the model still relies on labeled data from a different (simulated) domain. This creates a somewhat misleading impression of the generalization capabilities claimed in the paper. A revised title that reflects the cross-dataset nature of the problem might be more accurate.

2. The paper’s current comparison tables could lead readers to assume that ReZeS-Count is a purely unsupervised method, akin to CrowdCLIP and similar approaches, while it actually uses quantity annotations from the simulated dataset. This reliance on labeled synthetic data should be clarified explicitly. Adding a new column to the tables that indicates the type of annotation (e.g., labeled synthetic data vs. unlabeled real data) would help clarify the supervision levels used by each method. This additional detail is crucial for fair comparisons and to avoid misinterpretation of the method’s level of supervision relative to other “annotator-free” approaches.

3. The paper would benefit from a more thorough qualitative analysis of the features learned by ReZeS-Count. Specifically, an investigation into which visual and textual features are most influential in the retrieval process could enhance understanding of the model’s zero-shot capabilities.

### Questions
See the weakness.

If the authors address the above concerns, I would support the acceptance of this paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes ReZeS-Count, a retrieval-based zero-shot crowd counting approach. It leverages external knowledge retrieval, extracting image-text pairs from a simulated crowd dataset to augment real crowd image embeddings. Experiments demonstrate that the ReZeS-Count outperforms current zero-shot crowd counting approaches.

### Strengths
1. External information is relatively easy to obtain compared to detail annotations. This method makes the first attempt to utilize external information during testing for improving crowd counting accuracy, reducing reliance on labeled data.
2. Experiments illustrate that the proposed zero-shot method achieves competitive performance compared with the fully-supervised method MCNN.

### Weaknesses
1. Lack of efficiency analysis in the manuscript. Will this approach become time-consuming as the retrieval space scales?
2. What is the baseline method? As shown in Table 4, even the model in line 1 surpasses the fully supervised method MCNN. Which design component is the most critical for achieving this?
3. The presentation of this manuscript could be improved. What is the structure of the count decoder? According to Figure 3, the decoded values are integers. It is not clear how to decode these integer counts.

### Questions
Please refer to the weaknesses.

### Soundness
2

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
3

### Summary
This paper presents a zero-shot counting method based on synthetic data and vision-language models.

### Strengths
The authors claim that this study is the first one to combine synthetic data and VLM, achieving better performance than other LVM counting models.

### Weaknesses
Most of the paper is difficult to understand. Many variables are not well-defined, and the corresponding descriptions are confusing.

- What is the maximum inner product? What is its formulation?
- Section 3.2 is hard to understand. What is retrieved in this part? If the retrieval process is considered a black box, what is the input for the retrieval? What is the output of the retrieval? What is the database used for the retrieval?
- On line 259, how is the image encoder \(\Psi\) and text encoder \(\Phi\) pretrained? Are they derived from CLIP? If so, please add relevant descriptions and citations.
- Where does the image embedding \(\mathbf{e}_i\) come from?
- The pipeline is unclear. A figure demonstrating the overall process is required.
- What is the post-processing of \(\mathbf{e}'_i\) in Eq. (6)?
- In Eq. (7), how is \(\hat{c}_i\) estimated, and what is its ground truth (GT)? There is no prior reference or description explaining their source.



- In lin 238, what is the maximum inner product? What is its formulation?
- On line 259, how is the image encoder \(\Psi\) and text encoder \(\Phi\) trained? Are they derived from CLIP? If so, please add relevant descriptions and citations.
- In line 268, Where does the image embedding \(\mathbf{e}_i\) come from?
- The pipeline is unclear. A figure demonstrating the overall process is required.
- What is the post-processing of \(\mathbf{e}'_i\) in Eq. (6)?
-  In Eq. (7), how is (\hat{c}_i) estimated, and what is its ground truth (GT)? There is no prior reference or description explaining their source.


Some parts should be addressed to improve reading:

1. A figure should be present rather than only a description for the two-stage retrieval (real and then synthetic).

### Questions
- What is the maximum inner product? What is its formulation?
- Section 3.2 is hard to understand. What is retrieved in this part? If the retrieval process is considered a black box, what is the input for the retrieval? What is the output of the retrieval? What is the database used for the retrieval?
- On line 259, how is the image encoder \(\Psi\) and text encoder \(\Phi\) pretrained? Are they derived from CLIP? If so, please add relevant descriptions and citations.
- Where does the image embedding \(\mathbf{e}_i\) come from?
- The pipeline is unclear. A figure demonstrating the overall process is required.
- What is the post-processing of \(\mathbf{e}'_i\) in Eq. (6)?
- In Eq. (7), how is \(\hat{c}_i\) estimated, and what is its ground truth (GT)? There is no prior reference or description explaining their source.

### Soundness
2

### Presentation
1

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
The paper titled "Retrieval-Based Zero-Shot Crowd Counting" introduces a novel approach named ReZeS-Count that leverages knowledge retrieval to enhance zero-shot crowd counting performance.  The method addresses the challenge of distribution gap between real and simulated data by retrieving simulated crowd images and their text descriptions to augment the image embeddings of real crowd images.  This is achieved through a pre-training and retrieval mechanism that incorporates unlabeled real crowd images along with simulated data, thus reducing the annotation cost associated with real datasets.

### Strengths
#### Originality
- Introduces the ReZeS-Count framework, innovatively combining knowledge retrieval with zero-shot crowd counting, utilizing simulated data and text information to enhance real image embeddings.

#### Quality
- Demonstrates the effectiveness of the proposed method through extensive experiments on five public datasets, surpassing current crowd counting approaches.

#### Clarity
- The paper is well-structured, with a detailed explanation of the framework and its components in the methodology section.

#### Significance
- Addresses the challenges of annotation costs and distribution differences between real and simulated data in crowd counting.

### Weaknesses
1. While the paper claims state-of-the-art results on five public datasets, it would benefit from testing on more diverse datasets, particularly those with varying densities and complexities, to further validate the robustness of the ReZeS-Count framework.

2. Ablation Studies: The paper could provide more detailed ablation studies to isolate the contribution of each component of the framework.  For instance, the impact of the knowledge retrieval module could be quantified independently to understand its specific contribution to the overall performance.

3. Model Complexity: The paper could provide more insight into the computational complexity of the ReZeS-Count framework. Understanding the trade-offs between accuracy and computational resources is critical for practical applications.

4. Comparison with State-of-the-Art: While the paper claims state-of-the-art performance, but the comparison method is not the latest.

5. Theoretical Foundations: The paper could benefit from a deeper theoretical analysis of why the knowledge retrieval approach works for zero-shot crowd counting.

### Questions
Please refer to Section Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
