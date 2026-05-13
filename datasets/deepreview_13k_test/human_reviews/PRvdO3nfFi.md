# ReSi: A Comprehensive Benchmark for Representational Similarity Measures

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Measuring the similarity of different representations of neural architectures is a fundamental task and an open research challenge for the machine learning community.
This paper presents the first comprehensive benchmark for evaluating representational similarity measures based on well-defined groundings of similarity.
The representational similarity (\resi{}) benchmark consists of (i) six carefully designed tests for similarity measures, (ii) 23 similarity measures, (iii) eleven neural network architectures, and (iv) six datasets, spanning over the graph, language, and vision domains.
The benchmark opens up several important avenues of research on representational similarity that enable novel explorations and applications of neural architectures.
We demonstrate the utility of the \resi{} benchmark by conducting experiments on various neural network architectures, real world datasets and similarity measures.
The benchmark is extensible, future research can build on and further expand it.
We believe that the \resi{} benchmark can serve as a sound platform catalyzing future research that aims to systematically evaluate existing and explore novel ways of comparing representations of neural architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a comprehensive benchmark for evaluating 23 representational similarity measures across six similarity tests, twelve different architectures, and six datasets from diverse domains. Additionally, the paper offers insights for future research and aims to democratize a unified framework that ensures fair comparisons across different studies.

### Strengths
* The paper is well-written and easy to follow, with experiments clearly presented and tasks well-defined. Figures and tables are self-explanatory, significantly enhancing the manuscript's readability and accessibility.

* The authors have provided the code, ensuring full reproducibility of results and facilitating the community's ability to expand and build upon the benchmark. This openness supports transparency and encourages collaborative advancement in the field.

* The problem addressed is highly relevant and important for the community, as it remains an open question which metric is best suited for different scenarios.

### Weaknesses
* It’s unclear whether the similarities are calculated between two latent spaces (as suggested in formula 3, line 094) or between two individual representations (a single point), as written in line 095. Clarifying this distinction (and how each metric is adapted accordingly) could improve the reader's understanding. It seems to be between two latent spaces, but in Figure 2 (left), the metric is calculated between two points.

* When evaluating the text architectures:
  * Could you clarify the choice to test the same model with 25 different seeds, rather than exploring architectural variations like RoBERTa or ALBERT, which are available pretrained on Hugging Face? Including a wider variety of architectures might enhance the robustness and generalizability of the findings.
  * It would be helpful to either move the explanation of the choice to use the CLS token to the main manuscript or to reference the appendix. Additionally, you might consider testing alternative aggregation modalities, such as the mean or the last token, since these can yield different representations and may impact the results.

* The vision task may benefit from broader testing since only ImageNet with 100 subclasses is used. Expanding the evaluation to include the full ImageNet dataset or other widely-used datasets, such as ImageNet-1k, CIFAR-10, or CIFAR-100, could provide a more comprehensive assessment.

* The analysis could benefit from stronger takeaways. For instance, in lines 438-439, you suggest that the choice of measures should be task-specific, and in lines 453-455, you advocate for the development of best practices for using similarity metrics. However, these insights feel somewhat broad, and more concrete guidance could help readers understand how to apply the benchmark effectively.

* In line 413, it’s mentioned that some domain-specific trends can be identified, yet later (line 424), you note that no single measure consistently outperforms others across all tests, even within a single dataset. The first claim—that some metrics appear more suitable for specific modalities—is interesting and would benefit from a more in-depth discussion. Also, adding a summary table of these findings of the paper could help readers better understand the details.

### Questions
* What happens with different architectures for the text modality (e.g. some LLMs)?
* What is "IN21k" in line 282? Please write out the full name instead of using the acronym, as it’s unclear without a reference to the actual name.

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
4

### Summary
This paper presents the ReSi benchmark, a framework for assessing representational similarity measures across neural architectures from different domains. It features 23 similarity measures, twelve neural network architectures, and various datasets from graph, language, and vision. ReSi is proposed to support research on representation learning, reproducibility, and exploration of new approaches for comparing neural representations.

### Strengths
- The challenge of understanding learned representations better, especially in an unsupervised way is highly relevant and of practical importance.
- Reproducible and extensive experiments covering a wide range of metrics, domains and tasks.
- The paper is overall well-written and easy to follow. The figures and findings are clearly presented.

### Weaknesses
- I think the paper misses the opportunity to give the reader a better understanding of what drives the differences and inconsistent results of measuring similarity. Which types of measures perform well together and what feature of the representation is this driven by. Relevant aspects could be due to the way representations are normalized, what arithmetic function is used for computing the distance (e.g. dot-product, summed differences, etc.)
- Another angle to better understand similarity computations is from the point of interpretability, i.e. what features do the respective models pick up on and how do these change across models. I think this is an important and complementary direction to measuring different similarity scores and should be discussed (cf. [1,2,3]). 
- ReSi is presented as the “the first comprehensive benchmark for representational similarity” and can “yield rich insights” and a “theoretical understanding of representational similarity”. While I did find the general guidelines interesting and helpful, I think a deeper understanding of what causes these differences across metrics and domains is missing, and thus the above statements overstate the level of achievable insights from ReSi for me.


[1] Eberle et al. “Building and interpreting deep similarity models”, IEEE Transactions on Pattern Analysis and Machine Intelligence, 44(3), 2020.

[2] Janizek et al. "Explaining explanations: Axiomatic feature interactions for deep networks", CoRR, 2020.

[3] Vasileiou et al. “Explaining Text Similarity in Transformer Models”, NAACL 2024.

### Questions
- Should Eq. 3 map to R^N?
- It did not become clear initially what type of accuracy measures are considered; e.g. what task the model is trained to solved?
- I think coloring the labels of the similarity measures in Table 3 may be helpful for the reader (similar to the coloring in Fig. 3)

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a suite of benchmarking tasks to test the quality of a representational similarity metric. The tasks are designed around training models such that they are different in one specific way that leads to a certain expectation for similarity. Specifically, the authors propose 6 tasks:

(T1): Correlating similarity vs accuracy. Models are trained with only varied seeds.
(T2): Correlating similarity to actual model outputs.  Models are trained with only varied seeds.
(T3): Label Randomization: Randomizing different percentages of the labels. Models are expected to be more similar within the same percentage of randomization.
(T4): Shortcut affinity: Models are trained with random "shortcuts" that leak the correct label. The shortcut that always leaks the correct label, sometimes leaks the correct label and never leaks the correct label. Models should be more similar within group. 
(T5): Augmentation: models are trained with different kinds of augmentations adn models are expected to be more similar within the same type of augmentations. 
(T6): Layer Monotonicity: The similarity between layers is expected to be related to the distance between the layers. 

They apply their benchmarking tasks to three domains, graphs, language and vision and test 23 different representational similarity methods. 

The authors find that no similarity metric is always the best according to these metrics, however, there are some that tend to perform better than others, especially within a specific sub-domain (graph, language, or vision).

### Strengths
(S1) The goal of the paper is well-motivated and could be a valuable contribution to the community, since it is not clear how to compare representational similarity methods. 

(S2) The problem is quite challenging as it is hard to know exactly how two models differ, therefore the authors take reasonable steps to develop tasks in which they can approximately group models by differences in their performance or training method. 

(S3) The authors apply their benchmarking method on a comprehensive set of representational similarity methods in three popular domains in machine learning. 

(S4) The authors provide some interesting insights into differences between similarity methods and show that no single similarity method always performs the best.

### Weaknesses
(W1) Task 6 - I find that there are some careful considerations to use task 6 (see Q1). If the layers are chosen incorrectly, task 6 would have some issues for at least some vision models since skip connections could make neighboring layers dissimilar. Correcting/explaining this issue would shift my score to a 6. 

(W2) I found the depth of analysis to be somewhat limited. The authors could significantly strengthen the paper by providing some deeper analysis into a few similarity methods that explains how the similarity methods arrive at different similarity scores when comparing the same representations. For example, the authors show the impact of preprocessing by comparing two similarity methods that differ only in preprocessing: Orthogonal Procrustes (OrthProc) and Procrustes Size-and-Shape Distance (ProcDist). Can the authors analyze what the preprocessing does to the representation and how it changes the results of the method on the benchmarks? If this analysis and/or others are provided, I would consider improving the rating further. 

Minor ----
(W3) Section 3.1 should indicate more details of the tasks will be provided in Sec 3.5.

### Questions
Q1. Which layers are being used in the vision model experiments? I find that this information is not clearly provided in Sec. A.5 Vision.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces ReSi, a comprehensive bechmark for comparing neural representations.
The benchmark consists of (i) six carefully designed tests for similarity measures, (ii) 23 similarity measures, (iii) twelvecneural network architectures, and (iv) six datasets, spanning over the graph, language, and vision domains.
The benchmark is extensible; future research can build on it and further expand it.
The source code is publicly available.

### Strengths
1. Novelty. To the best of my knowledge, authors have introduced the first representational similarity bechmark.
2. Inside the benchmark, several rarely used similarity measures were tested (like Jaccard similarity), however, they showed promising results.
3. An in-depth analysis is provided; cases where some similarity measures tend to work well as studied.
4. The benchmark is quite diverse: in includes datasets from spanning graph, language, and vision domains.
5. The language of the paper is fine and it's easy to follow.
6. Impact. The comparison of neural representational similarity measures is a long-standing problem in deep learning.

### Weaknesses
1. Authors cite (Barannikov et. al, 2022.) several times as an example of representation comparison measure and experimental methodology, but don't include the proposed measure (RTD) into comparisons.
2. Stitching (Bansal, 2021) is not included intro the study.
3. Some important details of experiments are not disclosed: for example, CKA could be evaluated on the whole dataset or batches. Other similarity measures probably include hyperparameters as well.
4. The study might benefit from an Appendix with a brief description of all similarity measures under evaluation.

Bansal, Y., Nakkiran, P., & Barak, B. (2021). Revisiting model stitching to compare neural representations. Advances in neural information processing systems, 34, 225-236.

### Questions
1. Can you please clarify notations at Figure 3? Does boxes and bars mean quantiles?

### Soundness
4

### Presentation
4

### Contribution
4
