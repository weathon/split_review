# Organizing Unstructured Image Collections using Natural Language

- Decision: Reject
- Scores: 3, 5, 8, 5, 6

## Abstract
\vspace{-.05in}
Organizing unstructured visual data into semantic clusters is a key challenge in computer vision. Traditional deep clustering (DC) approaches focus on a single partition of data, while multiple clustering (MC) methods address this limitation by uncovering distinct clustering solutions. The rise of large language models (LLMs) and multimodal LLMs (MLLMs) has enhanced MC by allowing users to define clustering criteria in natural language. However, manually specifying criteria for large datasets is impractical. In this work, we introduce the task \tasktitle (\taskshort) that aims to automatically discover clustering criteria from large image collections, uncovering interpretable substructures \textit{without requiring human input}. Our framework, \methodfirsttitle (\methodshort), uses text as a proxy to concurrently reason over large image collections, discover partitioning criteria, expressed in natural language, and reveal semantic substructures. To evaluate TeDeSC, we introduce the COCO-4c and Food-4c benchmarks, each containing four grouping criteria and ground-truth annotations. We apply TeDeSC to various applications, such as discovering biases and analyzing social media image popularity, demonstrating its utility as a tool for automatically organizing image collections and revealing novel insights.
\begin{center}
    \textcolor{red}{\textbf{Disclaimer:}} \textcolor{red}{Potentially sensitive content.}
\end{center}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a LLM-based method (the "TeDeSC" method) to address a proposed variant of the "semantic multiple clustering" problem, where both the clustering criteria and the groupings within each criterion are not known a priori and have to be generated with respect to the given data set.  

Given a set of images, the proposed TeDeSC (Text Driven Semantic Multiple Clustering) method leverages the ability of LLMs and MLLMs to generate the clustering criteria for the images and the groupings in each criterion.  For generating the clustering criteria, multi-modal LLMs (MLLMs) are used first to generate a caption for each image, and then the generated captions are fed to LLMs to generate a set of criteria that are relevant to the given images.  For generating the groupings within a criterion C, each image is first fed to a MLLM to generate a caption, conditioned on the criterion C; then, the captions of all of the images will go through a three-step process using LLMs to assign to each image a triplet of group labels, at three levels of semantic granularity.

Along the development of the proposed method, previously existent benchmark data sets are expanded with richer ground-truth clustering criteria and groupings.  The expanded ground-truth clustering criteria and groupings provide better coverage over the many valid grouping options in collections of images with high scene complexity.

### Strengths
(S1) Besides the main proposed approach "TeDeSC", the paper also describes other interesting approaches of using LLMs to build the "criteria proposer" and the "semantic grouper".  The descriptions of those other approaches set a nice context to highlight and differentiate the main features of the proposed "TeDeSC" approach.

(S2) The three applications described in Section 5 are quite motivating.  Those applications illustrate how an approach for "semantic multiple clustering" (such as the proposed "TeDeSC" method) can be used in discovering spurious correlations and human bias in data, and in data understanding.  However, I feel that the paper should focus more on describing the details of the TeDeSC method, rather than using two pages to describe the three applications.

(S3) The new benchmark data sets produced in this work may be interesting for future work.

### Weaknesses
(W1) The paper puts too much content in the appendix. Much of that content should be in the main text to make the paper self-contained. For example, the paper can be more readable if it has more descriptions on the proposed approach, on the evaluation metrics and methodology, etc.

(W2) More descriptions are needed about the proposed methods.

(W3) More descriptions are needed about the evaluation metrics and methodology.

(W4) The figures are too small (for example, Figures 4, 5, and 6).

(W5) The definition of the proposed variant of the "semantic multiple clustering" problem seems to be not fully defined. The definition doesn't specify the objective that the generated clusters should achieve (e.g., optimal with respect to some notions, etc.).

### Questions
(Q1) In Section 3.1, "Caption-based Proposer": For each subset of captions, the proposed method prompts a LLM to elicit a set of partitioning criteria.  How consistent are the sets of partitioning criteria elicited from different subsets of captions?  Would a LLM generate criteria using different English words which are semantically the same?  How does the proposed method accumulate the subsets of captions and consolidate partitioning criteria that are semantically similar?

(Q2) In Section 3.2, "Caption-based Grouper": How diverse are the initial set of class names that are generated and assigned to the images?  How diverse are the output of the "multi-granularity cluster refinement"?  By the way, can we show some experimental data (perhaps in the "Experiments" section) about the number of images in the data sets and the number of distinct groups at each granularity level?

(Q3) In Section 4, "Evaluation metrics for Criteria Discovery": In the formula of TPR, how does it compute the intersection of the set of generated criteria (the set R) and the ground-truth criteria (the set Y)?  How does a "criterion token" in the set R match with a "criterion token" in the ground-truth set Y?  Do the criteria tokens in the set R and the set Y come from a small superset of common tokens?  

(Q4) In Section 4, "Evaluation metrics for substructure uncovering": Can we formulate the evaluation method of "Semantic Consistency" in a math formula?  For example, it will be helpful to show the math formula of the Semantic Accuracy (SAcc) metric.

(Q5) Figure 4:  Can we have some descriptions about how to read the figures in Figure 4?  

(Q6) Figure 5:  Can we have some descriptions about how to read the figures in Figure 5?  

(Q7) In Section 4.2, Table 2, "Comparison with criterion-conditioned clustering methods": How does the computation of CAcc(%) and SAcc(%) done, if the TeDeSC method generates more groupings than the ground-truth groupings?  Does having more groupings than the ground-truth groupings boost the value of CAcc(%) and SAcc(%)?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed a new way to organize image collections by leveraging LLM-assisted semantic multiple clustering. The proposed framework, TeDeSC, uses LLMs to convert images into texts and build a criteria proposer and a semantic grouper to discover potential semantic clusters describing a dataset. The TeDeSC provides us with a way to uncover the semantic structures and underlying biases of a dataset. Empirical studies on real-world datasets and AI-generated images validated its effectiveness.

### Strengths
1. The paper is well-organized and clearly written, with figures that effectively illustrate the motivation and methodology. 

2. The experimental setup is thorough, with well-designed evaluation criteria and informative visual representations. 

3. The proposed method is technically sound. Using LLM and multi-modal learning can improve the performance of many AI-related tasks.

### Weaknesses
1.  The proposed method leverages multiple LLMs to generate criteria and semantic labels, with each LLM component requiring dedicated prompt engineering. This introduces numerous design choices that may impact the system’s overall performance. To enhance the framework, it would be helpful if the authors provided quantitative metrics, such as a clearly defined loss function, to clarify the objectives behind the design choices and to better evaluate the approach's effectiveness. Specifically, the lack of a clear objective function makes it difficult to understand how the different prompt engineering choices affect the final clustering results. The authors should also discuss the sensitivity of the framework to different prompt variations and provide a more systematic approach to prompt design, rather than relying on an iterative process.

2. ​​​​There is a growing trend to apply large language models (LLMs) to enhance various AI-related tasks. While this paper is innovative from an application perspective, it would benefit from a deeper discussion of its scientific contributions. The paper needs to more clearly articulate the novelty of its approach beyond simply applying LLMs to a new task. The core methodological contributions need to be more explicitly stated and justified.

3. The overall design is primarily empirical. It could be strengthened by incorporating more theoretical analysis on the integration of its components. For example, a discussion on why using LLMs can improve image clustering, compared to previous studies, would provide valuable insights. Specifically, the paper lacks a theoretical justification for why the proposed method should be expected to perform better than traditional clustering methods. A more in-depth analysis of the theoretical underpinnings of the approach is needed.

4. Biases in benchmark datasets have garnered considerable attention in recent years. For instance, [1] investigated geographic biases within the COCO dataset (used as a benchmark in this paper), and [2] explored spurious correlations between attributes like "Blond" and "Female" in the CelebA dataset. In response, developers of LLM products such as GPT and DALL-E have curated their training datasets and models to mitigate such spurious correlations. While the proposed method benefits from these mitigated biases by incorporating pre-trained LLMs into its pipeline, its contribution may be less impactful than suggested in Section 5, especially when compared to baseline methods trained from scratch on biased datasets. The paper should more clearly acknowledge the reliance on pre-existing bias mitigation efforts in LLMs and discuss how this impacts the novelty and significance of the proposed approach.

### Questions
In addition to the weakness, there is one more question as below.

1. If we choose different LLMs, how they will influence the performance of the proposed framework?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents semantic multiple clustering of images based on text generated through LLMs or MLLMs through prompting. The proposed method is unsupervised and produces multiple clusterings based on the criteria given in natural language without specifying number of clusters. The method automatically discovers multiple criteria for clustering and produces clustering at multiple granularities.  The paper also introduces two new benchmarks COCO-4c and Food-4c sourced from Food-101 and COCO-val with each having four clustering criteria. TeDeSC is applied to a variety of applications, including discovering biases in real-world datasets and text-to-image generative models, and analyzing the popularity of social media images.

### Strengths
The proposed method implements many approaches to discover the clustering criteria and compared the results.  For each proposer approach, a grouper approach is implemented which combines the similar criteria and assigns a name to it.
The results are analysed against the hard ground truth (annotated by human oracle)
The proposed method is applied on different applications achieved good results.

### Weaknesses
The entire method is based on use of LLMs or MLLMs through prompting. What is the effect of hallucination and biases present in these models?

The comparison with existing models is limited. Only two methods IC/TC and MMaP are considered.

In image-based proposer, an image grid (8x8) is constructed and passed to a MLLM for criteria generation. What is the significance of such a grid? The grid would have different type of images and will confuse the MLLM.

Criteria pool refinement process takes the model generated text and work on it. It may lead to hallucination. How would you justify it?

Typos
Page 1 last line …remove the
Table 28 – Highlighted values for Action-3c … both CACC

### Questions
Same as in weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the challenge of organizing large, unstructured image collections by introducing the task of Semantic Multiple Clustering (SMC). SMC aims to automatically group images into semantically meaningful clusters based on multiple, unknown criteria without requiring prior human input or predefined categories. To tackle this problem, the authors propose TeDeSC (Text Driven Semantic Multiple Clustering). This framework leverages large language models (LLMs) and multimodal LLMs (MLLMs) to discover clustering criteria and organize images accordingly. By translating visual data into textual form, TeDeSC enables the identification of hidden patterns within image collections. The authors evaluate their method on two new benchmarks they contribute—COCO-4c and Food-4c—and demonstrate its applicability in tasks such as discovering biases in text-to-image generative models and analyzing social media image popularity.

### Strengths
This paper tackles the challenge of organizing unstructured image collections without prior knowledge by introducing a new task called Semantic Multiple Clustering (SMC). This significant contribution fills a clear gap in the existing literature. The authors present a TeDeSC framework, which cleverly leverages large language models (LLMs) and multimodal LLMs (MLLMs) to automatically discover clustering criteria by turning visual data into text. This approach is innovative and showcases originality in methodology.

They conduct thorough experiments and introduce two new challenging datasets, COCO-4c and Food-4c, which better reflect real-world complexity. By comparing various design choices using appropriate metrics like True Positive Rate (TPR), Semantic Accuracy (SAcc), and Clustering Accuracy (CAcc), they provide a comprehensive evaluation of their method.

The paper is well-written, with a clear problem statement and a structured presentation. The effective use of figures and tables enhances understanding. Practical applications—such as uncovering biases in text-to-image generative models and analyzing social media image popularity—underscore the work's significance across different domains.

### Weaknesses
1. The explanation of the multi-granularity clustering in the Semantic Grouper isn't detailed enough, making it challenging to understand and reproduce the method thoroughly. Additionally, the paper doesn't discuss the computational costs or how well TeDeSC scales with large datasets, which is essential given that LLMs and MLLMs can be quite resource-intensive.

2. The paper doesn't sufficiently explore the potential limitations of TeDeSC, such as the risk of introducing biases from LLMs and MLLMs into the clustering results. It would benefit from a deeper discussion on these biases, how to mitigate them, and the ethical implications—especially in sensitive areas like bias detection. Also, there's no discussion on how TeDeSC might be applied to other unstructured data types beyond images.

3. Using True Positive Rate (TPR) to evaluate criteria discovery without considering false positives might not give the complete picture. Including additional metrics or discussing how false positives could impact the results would provide a more comprehensive assessment. Moreover, the comparative analysis could be strengthened by adding more baseline methods or conducting ablation studies to isolate the contributions of each component within TeDeSC.

4. The user study on bias discovery in text-to-image generative models doesn't offer enough methodological detail. Providing more information about how the study was designed, who the participants were, what questions were asked, and the statistical methods used would enhance the credibility of the findings and help readers better assess the conclusions.

### Questions
First, I find the concept of multi-granularity clustering in your Semantic Grouper quite interesting. Still, I'm a bit unclear on how you determine the different granularity levels (coarse, middle, fine). Could you provide more details on this process? An illustrative example showing how these levels impact the clustering results would be beneficial.

Second, given that TeDeSC heavily relies on large language models (LLMs) and multimodal LLMs (MLLMs), I'm concerned about potential biases in these models affecting your clustering outcomes—especially in sensitive applications like bias detection. How have you addressed or mitigated these biases within your framework to ensure fair and unbiased results?

Third, in your evaluation of criteria discovery, you use True Positive Rate (TPR) but don't seem to account for false positives. Could you explain the reasoning behind this choice? How might false positives impact your system's performance, and do you think incorporating metrics that consider false positives would provide a more comprehensive assessment?

Finally, in the application section on bias discovery in text-to-image generative models, you mention a user study but provide limited details. Could you elaborate on the study design? Information such as the number of participants, their demographics, the questions they were asked, and the statistical methods used for analysis would enhance the credibility of your findings and help readers better understand the significance of your results.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the semantic multiple clustering task and proposes a two-stage framework named TeDeSC, which consists of Criteria Proposer and Semantic Grouper. This framework utilizes text as a proxy to automatically discovers grouping criteria in natural language from large image collections and uncovers interpretable data substructures. Extensive experiments conducted on 6 benchmarks and various real-world applications demonstrate its utility to reveal valuable insights.

### Strengths
1.	This work introduces a new task, i.e., Semantic Multiple Clustering (SMC), which is interesting and important for real-world applications.

2.	The framework can automatically discover both the criteria and the corresponding clusters from a image set from various granularities, which reduces the cost of manual annotation.

3.	The experimental part is quite comprehensive and presented with a rich and diverse manner.

### Weaknesses
1.	The framework proposed by the authors relies heavily on a variety of pre-trained LLMs and MLLMs, it is important to discuss the costs of time and resource required. Specifically, the paper lacks a detailed analysis of the computational overhead associated with using large language models for both the Criteria Proposer and Semantic Grouper stages. The memory footprint, inference time, and energy consumption should be quantified, especially when scaling to large image datasets. This is crucial for assessing the practical applicability of the method.

2.	The “ill-posed nature” in the Introduction needs further explanations. The paper mentions that the clustering problem is ill-posed due to the subjectivity of cluster definitions, but this needs to be elaborated with concrete examples. For instance, how does the framework handle situations where multiple valid but conflicting criteria exist? In addition, there is a lack of clear explanation of the meaning of the values in Figure 4 (b). The diversity scores are not clearly defined, and the paper does not provide sufficient context on how these scores are calculated and what they represent in terms of the quality of criteria discovery.

### Questions
Please refer to the Weakness.

In sum, I think this paper is an interesting paper. I would like to raise my score after further discussions.

### Soundness
4

### Presentation
3

### Contribution
4
