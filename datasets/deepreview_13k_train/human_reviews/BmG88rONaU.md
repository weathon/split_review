# Test-time Adaptation for Cross-modal Retrieval with Query Shift

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
The success of most existing cross-modal retrieval methods heavily relies on the assumption that the given queries follow the same distribution of the source domain. 
However, such an assumption is easily violated in real-world scenarios due to the complexity and diversity of queries, thus leading to the query shift problem.
Specifically, query shift refers to the online query stream originating from the domain that follows a different distribution with the source one.
In this paper, we observe that query shift would not only diminish the uniformity (namely, within-modality scatter) of the query modality but also amplify the gap between query and gallery modalities. 
Based on the observations, we propose a novel method dubbed Test-time adaptation for Cross-modal Retrieval (TCR). 
In brief, TCR employs a novel module to refine the query predictions (namely, retrieval results of the query) and a joint objective to prevent query shift from disturbing the common space, thus achieving online adaptation for the cross-modal retrieval models with query shift.
Expensive experiments demonstrate the effectiveness of the proposed TCR against query shift. 
The code will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the challenge of cross-modal retrieval in scenarios where the query data distribution deviates from the source domain, a phenomenon known as "query shift." This deviation often leads to a performance decline in cross-modal retrieval systems. The authors propose a novel approach called TCR: Test-time adaptation for Cross-modal Retrieval, which adapts cross-modal retrieval models during inference to account for query shift. The proposed method includes a query prediction refinement module and a joint objective function to prevent the disturbances caused by the query shift, enhancing the uniformity within the query modality and minimizing the gap between query and gallery modalities. The model is designed to operate effectively in real time by adapting to changing online queries. The approach was tested on six popular image-text datasets and demonstrated superior performance against existing test-time adaptation (TTA) techniques.

### Strengths
1) The paper tackles the underexplored problem of query shift in cross-modal retrieval, providing a comprehensive analysis of its effects on retrieval performance. The method's unique combination of query prediction refinement and multiple loss functions sets it apart from traditional TTA approaches.
2) The authors conducted extensive experiments across six datasets and compared their method against several state-of-the-art TTA models. The amount of experiments is fair and convincing. 
3) The paper proposes a joint objective consisting of three loss functions—uniformity learning, gap minimization, and noise-robust adaptation—that each address specific challenges introduced by query shift. This is a novel design for this problem.

### Weaknesses
1)  The authors provide only limited discussion regarding the sensitivity of the various hyperparameters involved, such as the temperature and trade-off parameters. A more detailed analysis would improve understanding of the model's adaptability to different scenarios. Specifically, the paper lacks a thorough exploration of how the temperature parameter (τ), which controls the sharpness of the probability distribution, affects the model's performance under varying degrees of query shift. The trade-off parameters for the different loss terms also require a more in-depth sensitivity analysis to understand their impact on the final results. Without this, it is difficult to assess the robustness and generalizability of the proposed method.
2) The approach heavily relies on pre-trained models and assumes the existence of a well-aligned common space. In cases where the source domain model lacks robust representations, the effectiveness of TCR may be diminished. This could limit the generalizability of the approach to pre-trained models of different quality. The paper does not adequately address the potential limitations when using pre-trained models that have not been trained on diverse datasets or have biases that could affect the alignment of the common space. This reliance on high-quality pre-trained models without a discussion of the implications for less robust models is a significant weakness.

### Questions
1) The proposed TCR method aims to enhance retrieval robustness under query shift by manipulating modality uniformity and the modality gap. Given the variety of potential shifts in real-world data (e.g., subtle cultural variations, extreme distortions, rare domain-specific content), how does TCR perform across these different types of shifts? 

2) Could the model's performance degrade if it encounters shifts it was not explicitly evaluated against? A thorough breakdown of the model’s robustness to a diverse set of query shifts would strengthen the understanding of its general applicability.

3) This paper introduces several hyperparameters, such as the temperature parameter (τ) for controlling the trade-off between smoothness and sharpness, and others for balancing the different loss terms. How sensitive is TCR to these hyperparameters, and how easy is it to tune them for new domains? Some more results from these ablations studies will be very beneficial.

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
3

### Summary
The paper presents a Test-time adaptation for Cross-modal Retrieval (TCR) method to address query shift, which is a critical and understudied problem in cross-modal retrieval tasks. Query shift occurs when the distribution of online query streams differs from the source domain, leading to performance degradation in existing models. TCR introduces a query prediction refinement module and a joint objective function to refine query predictions and prevent query shift from disturbing the common space. It improves the existing test-time adaptation (TTA) methods with the capacity to manipulate both the modality uniformity and modality gap. Overall speaking, this paper is well-organized and of practical value.

### Strengths
The proposed TCR method addresses an important problem and is supported by strong experimental results.

It provides extensive experiments demonstrating the effectiveness of TCR against query shift. The comparisons with existing TTA methods show convincing improvements, with is a strong validation of the ablation study .

### Weaknesses
In Section 4.2, it is said that “We compare TCR with five SOTA TTA methods (Tent (Wang et al., 2021),  EATA(Niu et al.,2022), SAR(Niu et al.,2023), READ(Yang et al.,2024), and DeYO...”. These methods should be introduced in Section 2.2 of the related work part. 

Line 212, ,where Q and G denotes as query modality and gallery modality for clarity in the following. Change to “denote”

Tables 1 and 2 appear too early. They should not be on Page 7 but on the page where they are referred for the first time,

### Questions
see above comment

### Soundness
3

### Presentation
4

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
This paper introduces a novel setting, cross-modal retrieval under query shift. To address this challenge, it introduces a test-time adaptation method called TCR, which includes a query prediction refinement module to produce retrieval-optimized predictions for incoming queries. Additionally, it employs a joint objective function for online adaptation, effectively handling the query shift and noise.

### Strengths
1. The research question, cross-modal retrieval under query shift, is challenging and holds significant practical relevance.
2. Although this method builds on the principles of TTA, it also reveals TTA’s limitations in cross-modal retrieval and effectively overcomes these challenges.
3. Extensive experiments demonstrate the effectiveness of the proposed TCR method.
4. The paper is well-organized and well-written, enhancing the clarity and impact of its findings.

### Weaknesses
1. This research setting is limited by the assumption that each query batch contains i.i.d. samples. However, in real scenarios, query shift may occur unpredictably, introducing non-i.i.d. data within the same batch. This raises concerns about the method’s applicability under such conditions.
2. Regarding the emergence of query shift, I am curious whether temporal issues, such as temporal shifts or concept drift discussed in [1-3], are present in real-world scenarios. Could the authors provide relevant discussion on this aspect?   
    [1] Evolving standardization for continual domain generalization over temporal drift. *NIPS 2023*.
    [2] Temporal domain generalization with drift-aware dynamic neural networks. *arXiv preprint arXiv:2205.10664* (2022)
    [3]Online Boosting Adaptive Learning under Concept Drift for Multistream Classification, AAAI 2024
3. In Section 3.2.1 on candidate selection, it would be valuable to address two points: first, whether gallery shift affects the outcomes of nearest neighbor selection; and second, how the number of selected candidates impacts the results. Additional experiments should be conducted to clarify these aspects.
4. In Section 3.2.2, given the shift between the source and target domains, it is unclear why source-domain-like data can be directly selected based on centers. Could the authors provide further analysis and explanation on this approach?
5. In section 3.5the definition of S(x_{i}^Q) in Equation (11) lacks corresponding theoretical analysis.
6. In the experiments, the authors employed various methods to generate image or text query shifts. I believe the results may depend on the specific shift generation techniques used. Therefore, it is crucial to provide access to the data processing methods and code to ensure the reproducibility of the experimental results.
7. I recommend that the authors discuss the limitations of the proposed method and outline specific future research directions. This would provide readers with additional insights and considerations for further exploration.

### Questions
discussed in Weaknesses section.

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
This paper introduces a novel method named TCR for addressing the query shift problem in cross-modal retrieval. TCR employs a test-time adaptation approach that leverages a multi-scale adaptive convolutional neural network and a hybrid transformer module to refine query predictions and adapt to shifts in query distribution without additional training data. The method is designed to enhance the uniformity of the query modality and reduce the gap between query and gallery modalities, thereby improving retrieval performance. The study demonstrates TCR's effectiveness on image-text retrieval tasks using standard benchmarks and various corruption types.

### Strengths
1.	The paper proposes a novel test-time adaptation method (TCR) to address the query shift problem in cross-modal retrieval. This method achieves robustness against query shift by adjusting query predictions and designing a joint objective function, which is an interesting and potentially influential direction for research.
2.	The authors have conducted extensive experiments on multiple datasets, including COCO-C and Flickr-C, to verify the effectiveness of the proposed method. The experiments cover comparisons across different model types and sizes, as well as varying severity levels of query shift, demonstrating the robustness of the method.
3.	The paper not only introduces a new method but also provides an in-depth analysis of the impact of query shift on cross-modal retrieval, revealing how query shift can reduce the uniformity of the query modality and increase the gap between the query and gallery modalities. These theoretical analyses offer valuable insights for future research.

### Weaknesses
1.	The TCR method proposed in the paper performs model adaptation at test time, which may increase additional computational costs. It is recommended that the authors analyze the computational complexity of the model and the additional cost incurred, specifically detailing the time complexity of the multi-scale adaptive convolutional neural network and the hybrid transformer module, and how these scale with input size and model depth. Furthermore, a breakdown of the computational cost associated with the nearest neighbor selection in the query prediction refinement module would be beneficial.
2.	Are the COCO-C and Flickr-C datasets constructed by the authors themselves? It seems that the paper does not explain whether the results of the baseline methods for comparison were obtained by the authors' own experiments or cited from their respective articles. If they were obtained through their own experiments, it should be clarified whether such comparisons are fair (whether they were trained on the new baselines), which is quite confusing for readers. It is crucial to understand if the baselines were retrained under identical conditions as the proposed method, including data preprocessing, hyperparameter tuning, and training epochs, to ensure a fair and valid comparison.
3.	The authors are advised to provide more explanation on the baselines and to include a few actual examples of query shifts to help readers intuitively feel the task. Specifically, the paper should clarify the specific adaptation strategies employed by each baseline, such as the optimization algorithms, loss functions, and the specific layers that are updated during test-time adaptation. Additionally, providing concrete examples of how different types of corruptions (e.g., Gaussian noise, blur, contrast changes) manifest in both image and text modalities, and how these corruptions affect the retrieval performance would significantly enhance the reader's understanding.

### Questions
Please address my concerns proposed in Weakness.

### Soundness
3

### Presentation
3

### Contribution
2
