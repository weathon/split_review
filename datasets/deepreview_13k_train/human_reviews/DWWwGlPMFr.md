# LEMoN: Label Error Detection using Multimodal Neighbors

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
Large repositories of image-caption pairs are essential for the development of vision-language models. However, these datasets are often extracted from noisy data scraped from the web, and contain many mislabeled examples. In order to improve the reliability of downstream models, it is important to identify and filter images with incorrect captions. However, beyond filtering based on image-caption embedding similarity, no prior works have proposed other methods to filter noisy multimodal data, or concretely assessed the impact of noisy captioning data on downstream training. In this work, we propose \ours, a method to automatically identify label errors in multimodal datasets. Our method leverages the multimodal neighborhood of image-caption pairs in the latent space of contrastively pretrained multimodal models. We find that our method outperforms the baselines in label error identification, and that training on datasets filtered using our method improves downstream classification and captioning performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a label error detection method for multimodal datasets. Specifically, the authors first use pre-trained vision-language models to extract image-caption embeddings. Then they leverage the distance of multi-modal neighborhoods to detect the label error of image-caption datasets. This paper also provides a theoretical analysis of the feasibility of the proposed method.

### Strengths
1. The research problem is important. The image-caption datasets are widely used to train multimodal models. Detecting the label errors in these datasets is important for downstream tasks.
2. The idea of using pre-trained multimodal models is well-motivated and the theoretical analyses are reasonable. 
3. This paper is very well organized and written in general.

### Weaknesses
1. The details of the application on the unimodal dataset need to be clarified. How to define the nearest neighbors of text in unimodal datasets like CIFAR10/100？
2. Figure 3 can be improved. These lines overlap too much and are difficult to distinguish.
3. In the downstream captioning task, the improvements over CLIP similarity seem trivial. Can the authors provide some analysis of the possible reason？

### Questions
see the weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a new way to filter noisy multimodal data. Besides of using image-caption embedding similarity, the new approach leverages the multimodal neighborhood of image-captions pairs to identify label error. The method demonstrates improvements in label error detection and enhances performance on downstream captioning tasks.

### Strengths
This paper introduces a novel approach that uses multimodal nearest neighbors to assess the relevance between images and captions, providing both theoretical justification and empirical validation for the proposed method. The experiments evaluate its effectiveness in detecting label errors and its impact on downstream classification and captioning models.

### Weaknesses
The current experiments lack the breadth needed to fully demonstrate the impact of adding nearest neighbor terms. It would be beneficial to include a comparison using only single-side nearest neighbor term, and to present the actual values of all three terms for clearer insight. Specifically, the paper does not provide a clear breakdown of how each term ($d_{mm}$, $s_m$, and $s_n$) contributes to the overall performance across different datasets. The interaction between these terms is not well-understood, and the paper would benefit from a more detailed analysis of their individual and combined effects. For example, it is unclear why the nearest neighbor terms are more effective on some datasets than others, and a more thorough investigation into this phenomenon is needed. Furthermore, the paper should explore the sensitivity of the method to the choice of neighborhood size ($k$) and radius ($r$).

### Questions
1. In section 3, a few symbols are not explained, like r, D, k etc. It's better to split the section 3 into multiple sub sections to explain each term separately
2. Is there any explanation that why using pure CLIP similarity performs better than LEMoN on Flickr30k?

### Soundness
3

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
This paper presents an approach to detect misalignment between image-text pairs to clean image-text datasets. To achieve it, they propose a new metric that considers the distance between the image-text pairs and neighbors in image and text space. 

The high-level idea of their metric to compute label-error score is as follows. 
1. Given an image-text pair that is neighboring a target pair, if the text is far from the target text, but the image is close to the target image, the target pairs can be inconsistent. 
2. The neighboring pair used above can be also mismatched. To account for such a case, they weigh the score by using the similarity between the neighboring pair. 

Empirically, they evaluate the effectiveness of the proposed metric by image-classification dataset, an image-caption dataset such as COCO, and a medical image-report dataset. For evaluation in the image-text dataset, they randomly inject noise into the supervision of the dataset, e.g., replacing object names. Overall, their metric seems to be better than existing metrics in detecting noises, but the improvement was marginal in image-captioning.

### Strengths
1. They provide a new metric to detect label noise in image-text data, which is reasonable. Also, their experiments verify that the proposed metric outperforms an existing metric in detecting errors in their settings. 
2. Their writing and presentations are clear, and mostly easy to follow. 
3. Their approach includes some hyper-parameters, but the robustness to such parameters is also investigated. 
4. They conduct a wide rage of experiments which can be insightful for readers.

### Weaknesses
I am concerned that the experiments are not so focused on noisy image-caption datasets although their motivation is to handle issues of noisy data collected from the web.

1. Their approach seems to be mainly designed to detect label errors in image-caption datasets. However, the effectiveness of applying filtering to such a dataset seems to be marginal according to Table 4. I think label-error identification is proven to be effective by improving performance on downstream tasks. In this sense, the effectiveness of the proposed approach is not proven enough.

2. They conduct experiments on COCO and Flickr to show the effectiveness of the image-caption dataset. Then, the effectiveness of their metric is verified only on the synthetic noise they created. However, there can be more diverse types of noise in real image-caption data collected from the web. For example, some captions might focus on a specific aspect of the image while others have details. According to the experiments, it is not clear how their metric behaves in such cases.

3. Also, according to their appendix, their metric does not show much gain in the CC3M, which is webly collected. I actually feel that the authors had to conduct more analysis on this kind of dataset since their main motivation seems to detect errors on this kind of dataset, rather than image-classification dataset.

### Questions
1. It took some time to understand the intuition behind Eq. 2. I think it is better to provide high-level ideas of what Eq. 2 is computing.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents LEMoN, a novel approach designed to identify inconsistencies in image-caption pairs, with a focus on label noise detection. The proposed method demonstrates improved detection performance in classification and captioning tasks. Additionally, the paper offers theoretical justifications to support the proposed cross-modal scoring method.

### Strengths
1. The work introduces an original scoring method for label noise detection.
2. The proposed method is intuitive and clearly explained.
3. The method exhibits notable improvements across most experiments involving synthetic label noise, especially among training-free approaches.

### Weaknesses
1. The theoretical justifications provided in the paper contain several significant flaws, limiting their effectiveness as a core claim:
   - Theorem 4.1 appears to contain contradictory conditions, where the variable $\eta$ is defined as normal but also subject to the constraint $|\eta| > \epsilon$.
   - In Proposition A.1, Part 3 (line 885), the inequality does not hold, as the condition on $y' \ne y$ cannot be omitted. This leads to the conclusion $\mathbb{E} \le p\mathbb{E}$ with $p < 1$, implying that $\mathbb{E} = 0$.
   - There is frequent interchange between labels and embeddings, which results in incorrect conclusions. For example, in line 913, the embedding of $y'$ is replaced with label $y$ and an additive term $\eta$. However, according to Assumption 1 (line 855), both $y'$ and $y$ should be labels, not embeddings.
   - The expectation operator is lost when transitioning from the equation in line 915 to the one in line 917.
   - In the proof of Theorem 4.2 (line 954), the variance of $\frac{1}{k} E$ should be expressed as $\frac{1}{k^2} Var E$, rather than $\frac{1}{k} Var E$.
2. While the paper claims novelty in applying multi-modal scoring to label noise detection, this approach has recently been explored in [1].
3. The provided source code does not include implementations of the baseline methods. As a result, it remains unclear how the hyperparameters for these baseline methods were tuned, particularly given that the authors introduced a new set of synthetic datasets.
4. Some previous works [2] evaluate the area under the accuracy/filter-out-rate curve on real datasets, which provides a better understanding of filtering quality in real-world applications. The authors address this metric in Appendix I.12, where the results suggest that Deep k-NN may be a more effective alternative. However, these results are presented for only two datasets, limiting the generalizability of the findings.

### Questions
1. Which implementations of the baseline methods were used, and how were their hyperparameters selected?
2. How does LEMoN compare to VDC [1] in terms of strengths and weaknesses?
3. What is the inference speed of LEMoN relative to other methods? How does it scale with larger datasets, and is it feasible to apply this method to billion-scale datasets?
4. Why does LEMoN not show improvements in terms of the area under the accuracy/filter-out-rate curve?

### Soundness
2

### Presentation
3

### Contribution
2
