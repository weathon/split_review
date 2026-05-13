# Part-aware Personalized Segment Anything Model for Patient-Specific Segmentation

- Decision: Reject
- Scores: 1, 5, 5, 8

## Abstract
Precision medicine, such as patient-adaptive treatments utilizing medical images, poses new challenges for image segmentation algorithms due to (1) the large variability across different patients and (2) the limited availability of annotated data for each patient. 
    In this work, we propose a data-efficient segmentation method to address these challenges, namely \emph{\textbf{P}art-aware \textbf{P}ersonalized \textbf{S}egment \textbf{A}nything \textbf{M}odel} ($\mathbf{{P}^{2}SAM}$).
    Without any model fine-tuning, \ppsam enables 
    seamless adaptation to any new patients relying only on one-shot patient-specific data. 
    We introduce a novel part-aware prompt mechanism to select multiple-point prompts based on part-level features of the one-shot data.
    To further promote the robustness of the selected prompt,
    we propose a retrieval approach to handle outlier prompts.
    Extensive experiments demonstrate that \ppsam improves the performance by $\texttt{+} 8.0\%$ and $\texttt{+} 2.0\%$ mean Dice score within two patient-specific segmentation settings, and exhibits impressive generality across different application domains, \eg, $\texttt{+} 6.4\%$ mIoU on the PerSeg benchmark.
    Code will be released soon.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The article addresses challenges in personalized treatment within modern precision medicine, particularly in the context of medical image segmentation. The key issues it aims to solve include:

1.	Patient Variability: There is considerable variability among different patients, which complicates the segmentation of tumors and critical organs in medical images.
2.	Limited Annotated Data: Many existing segmentation algorithms rely on large amounts of annotated training data. However, personalized treatment often encounters a shortage of such data for individual patients, making it difficult to train models effectively.

To overcome these obstacles, the authors propose a new approach formulated as an in-context segmentation problem, leveraging the promptable segmentation mechanism of the Segment Anything Model (SAM). Their method, named P2SAM (Part-aware Personalized Segment Anything Model), allows for seamless adaptation to new, out-of-distribution patients using only one-shot patient-specific data.

### Strengths
1. The manuscript is clearly expressed and presents the research in a logical and structured manner, although some sentences are lengthy and could benefit from simplification to enhance readability.
2. The paper presents substantial qualitative results and includes experiments across multiple datasets, demonstrating a considerable amount of work.

### Weaknesses
1. Representation: The overall logic of the paper appears problematic to me. The title and introduction emphasize "Precision Medicine," yet the writing primarily focuses on highlighting the general applicability of the proposed method. Numerous examples and results are presented from the natural image domain, while the content related to "Precision Medicine" is notably limited, which may cause confusion for readers.

2. The motivation for the "Part-aware Prompt Mechanism" is unclear: what is the reasoning behind this approach, and how does it address challenges in medical tasks? The architecture diagram is also based on natural image applications, leaving it unclear how the proposed method tackles issues specific to precision medicine. Additionally, there is no discussion on how this approach handles different modalities in medical imaging, which the paper should address.

3. Method: Several aspects require further clarification and enhancement. 

     a. Firstly, the decision to use only a single negative point per cluster raises concerns regarding its sufficiency. A more robust approach would involve utilizing multiple negative points to enhance model generalization.

     b. Secondly, while the method is designed for patient-specific segmentation, it raises concerns about its application to multi-segmentation tasks. A discussion on how the part-aware prompt mechanism could adapt to scenarios involving multiple segmentations would improve the methodology's applicability.

     c. Additionally, the manuscript relies on 2D segmentation, which requires numerous points for effective performance. This issue remains unaddressed, and the choice not to utilize native 3D models is not sufficiently justified. Given the advantages of 3D models in capturing spatial relationships and providing more comprehensive context in medical imaging, exploring their potential application in this study would strengthen the methodology.

4. Experiments: Several areas require clarification and enhancement.

     a. Firstly, it is unclear whether the number of clusters set for K-means is consistent across different datasets. A detailed explanation of how the clustering parameters are determined for each dataset would improve the robustness of the results and ensure comparability.

     b. Secondly, the comparison methods lack the inclusion of the latest medical-related benchmarks. Integrating more recent studies or state-of-the-art approaches would provide a more comprehensive evaluation of the proposed method's performance. This would help contextualize the results within the current landscape of medical imaging segmentation research.

5. The paper lacks comparisons with state-of-the-art (SOTA) methods. Numerous improvements to SAM tailored for medical imaging have been proposed, yet many of them are omitted in this work’s comparative experiments. Furthermore, several segmentation baselines widely used in the medical domain are not referenced, which casts doubt on the demonstrated effectiveness of the proposed method.

### Questions
1. Is the proposed method truly aimed at addressing "Precision Medicine," as suggested in the title and introduction, or is it intended as a more general approach applicable to both natural image and medical imaging domains? These are fundamentally different focuses, and clarity on this point is essential.

2. What is the motivation behind the proposed method, and how does it address some of the fundamental challenges in the medical imaging field, such as unclear lesion boundaries and significant variations across different imaging modalities? Clarity on how these issues are tackled is crucial.

3. Since the method claims to address patient-specific segmentation, it must consider the significant variability in characteristics across different diseases, such as liver cancer, pancreatic cancer, and rectal cancer. How does the proposed method ensure effectiveness when dealing with patients suffering from various diseases with distinct features?

### Soundness
2

### Presentation
3

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
The authors target patient-specific segmentation by proposing a new segmentation pipeline: (1) obtaining multiple point-prompts from the part-aware prompt mechanism, and (2) feeding these point-prompts to a prompt-based segmentation network, such as SAM. The authors also propose a similarity-based refinement to control the number of prompts found during step 1. Main experiments were conducted on the NSCLC and CVC-ClinicDB datasets where the proposed method achieves the state-of-the-art performances. Further experiments were conducted to show the method's performance against tracking algorithms and on the one-shot segmentation task.

### Strengths
1. The paper is well-written and easy to follow.
2. The experiments are thorough, covering various important and related topics. 
3. The proposed refinement strategy on the number of prompts is conceptually easy and seems effective.

### Weaknesses
1. Unclearness in writing: (a) The motivation for Table 3 is unclear. It overlaps with Table 1 and 2 and brings little additional information. (b) For the baseline methods: direct-transfer and fine-tune, looks like no prompts are provided during the evaluation stage. Can the authors verify this is true?
2. The contribution on the Part-aware Prompt Mechanism is unclear. Although the authors have demonstrated the effectiveness of the overall method, it is unclear if the improvements are from the part-based sampling strategy or merely because of having multiple prompts. Specifically, it's not clear if the part-aware mechanism provides more effective prompts than simply selecting multiple points based on other criteria, such as confidence scores from a segmentation model.
3. (Minor) The application range of the method is limited to patients with multi-exams.

### Questions
1. To demonstrate the effectiveness of the Part-aware Prompt Mechanism, could the author compared to a modified version of PerSAM where instead of selecting "two points with the highest and lowest confidence values", the authors may select the top K and bot K' points where K and K' matches P^2SAM. In this way, the authors can demonstrate that points found by the Part-aware Prompt Mechanism are more effective. 
2. Since authors have shown better one-shot segmentation performance, I am curious to see if the authors can show their method's performance beyond patients with multi-exams. For example, for some medical segmentation datasets without patients with multi-exams, can the author randomly select one image-mask pair as the prior and test the model's performance on other pairs.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This study introduces a segmentation model called P2SAM which enables efficient, personalized medical image segmentation based on one-shot patient-specific data, improving segmentation performance across different patients and domains.

### Strengths
1. The work introduces a "part-aware prompt mechanism" that leverages one-shot, patient-specific data for segmentation without additional fine-tuning. This feature is particularly suited to precision medicine applications where data annotation is minimal.

2. Unlike standard SAM applications, P2SAM integrates a distribution-similarity-based retrieval approach that optimizes the selection of prompts, enhancing segmentation performance and reducing ambiguities.

3. P2SAM is demonstrated to be effective across a variety of medical and natural image datasets, making it versatile for both patient-specific and general segmentation tasks.

4. Quantitative Improvements: The model shows notable improvement over existing methods (PerSAM and Matcher), with significant gains in Dice scores and mIoU in various datasets, proving the robustness of the approach in handling out-of-distribution medical images.

5. The paper presents extensive comparisons across multiple datasets and includes qualitative results that illustrate the model’s adaptability and performance in challenging segmentation tasks.

### Weaknesses
1. Complexity and Computational Cost: The proposed method, while innovative, involves complex modules (e.g., retrieval approach for optimal prompt selection) that may increase computational demands, potentially impacting usability in real-time clinical applications. The reliance on K-Means clustering and Wasserstein Distance calculations, while effective for prompt selection, introduces overhead that could be significant for high-resolution images or large datasets. The paper should include a more detailed analysis of the computational bottlenecks and explore potential optimizations to improve real-time performance.

2. Limited Generalization to Other Modalities: Although versatile within specific settings, the method's performance in more diverse medical imaging modalities (e.g., MRI or ultrasound) remains unexplored. The current evaluation focuses primarily on CT scans and endoscopy videos, which may not fully represent the challenges posed by other modalities with different noise characteristics, contrast levels, and anatomical structures. Further experiments are needed to demonstrate the robustness of the proposed method across a broader range of medical imaging modalities.

3. Ambiguity in Module Contributions: The study could benefit from additional ablation studies to further clarify each component's role, such as the part-aware prompt mechanism versus the distribution-similarity-based retrieval. While the paper presents results with and without the retrieval approach, a more granular analysis is needed to understand the specific contribution of each component under different conditions, such as varying image quality or segmentation complexity. For instance, it would be useful to evaluate the performance of the part-aware prompt mechanism with different types of prompts and similarity metrics.

4. Dependence on SAM Backbone: While P2SAM leverages SAM effectively, it is still heavily reliant on SAM’s architecture. Any significant updates to SAM or its successors may require substantial adaptation of P2SAM. The paper should discuss the potential challenges of adapting P2SAM to future segmentation models and explore strategies to mitigate these dependencies. This should include an analysis of the specific components of SAM that are most critical for P2SAM's performance and how these could be replaced or adapted in the future.

### Questions
1. Scalability to Other Imaging Tasks: Could P2SAM be effectively adapted to other domains, such as pathological imaging, or expanded to handle 3D volumetric data with higher efficiency?

2. Integration with SAM 2: The authors briefly mention SAM 2. How would the proposed retrieval mechanism and prompt system adapt to SAM 2's expanded capabilities in video and sequential data processing?

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
5

### Summary
This paper introduces P2SAM, a novel data-efficient segmentation approach tailored for precision medicine, where patient-specific variability and limited annotated data challenge traditional segmentation models. Unlike conventional methods that require fine-tuning, P2SAM achieves adaptation to new patients using only one-shot patient-specific data.

### Strengths
1. the task in significant in practice
2. the paper is easy to follow

### Weaknesses
1. my main concern is the paper ignores many significant previous work[1,2,3] doing the same task (segmenting follow-up medical images given a template image with prompt or mask). Many of previous works have been explored this task with much larger scale training, more comprehensive experimental testing, and human evaluation. The paper is encouraged to compare with them or highlight the difference with them. 
2. the paper takes MedSAM as a SOTA in its comparisons, however, MedSAM serves basically as a baseline and does not represent SOTA on most tasks.
3. the paper used adapter to efficiently fine-tune SAM on medical image segmentation while it is not compared with Med-SAM-Adapter[4] as a baseline.
4. the paper is also encouraged do comparison under diverse visual prompts beyond point and bbox, like scribble[5, 2] and mask[1], which have been widely-used and comprehensively explored in the medical image segmentation before.

### Questions
see weakness

### Soundness
2

### Presentation
3

### Contribution
2
