# PerSense: Personalized Instance Segmentation in Dense Images

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Leveraging large-scale pre-training, vision foundational models showcase notable performance benefits. Recent segmentation algorithms for natural scenes have advanced significantly. However, existing models still struggle to automatically segment personalized instances in dense and crowded scenarios, where severe occlusions, scale variations, and background clutter pose a challenge to accurately delineate densely packed instances of the target object. To address this, we propose \textbf{PerSense}, an end-to-end, training-free, and model-agnostic one-shot framework for \textbf{Per}sonalized instance \textbf{S}egmentation in d\textbf{ense} images. Towards developing this framework, we make following core contributions. (a) We develop a new baseline capable of automatically generating instance-level point prompts via proposing a novel Instance Detection Module (IDM) that leverages density maps, encapsulating spatial distribution of objects in an image. (b) To mitigate false positives within generated point prompts, we design Point Prompt Selection Module (PPSM). Both IDM and PPSM transform density maps into personalized precise point prompts for instance-level segmentation and offer a seamless integration in our model-agnostic framework. (c) We introduce a feedback mechanism which enables PerSense to improve the accuracy of density maps by automating the exemplar selection process for density map generation. (d) To promote algorithmic advances and effective tools for this relatively underexplored task, we introduce PerSense-D, a diverse dataset exclusive to personalized instance segmentation in dense images. Our extensive experiments establish PerSense superiority in dense scenarios by achieving an mIoU of \textbf{71.61\%} on PerSense-D, outperforming recent SOTA models by significant margins of \textbf{+47.16\%}, \textbf{+42.27\%}, \textbf{+8.83\%}, and \textbf{+5.69\%}. Additionally, our qualitative findings demonstrate the adaptability of our framework to images captured in-the-wild.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces PerSense, a novel, training-free, and model-agnostic framework for personalized instance segmentation in dense images. The contributions of the paper are as follows:

1. New Baseline and Instance Detection Module (IDM): A new baseline is proposed, capable of automatically generating instance-level point prompts, featuring an Instance Detection Module (IDM) that utilizes density maps (DM) to provide candidate point prompts. A density map generator (DMG) highlights the spatial distribution of target objects. Automated Exemplar Selection: A class-label extractor (CLE) and grounding detector are used to automate the selection of effective exemplars, simplifying the DMG’s manual process. Point Prompt Selection Module (PPSM): A Point Prompt Selection Module (PPSM) is designed to reduce false positives within the candidate point prompts. IDM and PPSM are plug-and-play components that integrate seamlessly into the PerSense framework.

2. Feedback Mechanism: A feedback mechanism is introduced to automatically refine exemplar selection based on PerSense’s initial segmentation output, identifying multiple rich exemplars for DMG to improve segmentation accuracy.

3. PerSense-D Dataset: To facilitate personalized segmentation in dense images, the authors introduce PerSense-D, a dataset with 717 densely populated images across 28 object categories, providing a challenging benchmark for future studies.

### Strengths
(1) Innovative Training-Free Approach: By using density maps, PerSense avoids the need for extensive training, making it computationally efficient and adaptable to different dense segmentation tasks.
(2) Model-Agnostic Design: The PerSense framework can be seamlessly integrated with various density map generators and grounding detectors, enhancing its flexibility and usability.
(3) Comprehensive Evaluation: Experimental results on the newly introduced PerSense-D dataset show that PerSense significantly outperforms state-of-the-art methods, demonstrating its robustness and high performance in densely packed scenarios.

### Weaknesses
1. Methodological Innovation:  Although PerSense's training-free framework demonstrates some level of innovation, its reliance on density maps is not entirely novel, as similar approaches have been applied in traditional vision tasks. While the Instance Detection Module (IDM) and Point Prompt Selection Module (PPSM) bring some originality to the framework, they lack sufficient mathematical derivation or theoretical analysis to substantiate their uniqueness and theoretical advantage over existing methods. Specifically, the method for determining composite contours within the IDM, which uses a threshold of  $\mu + 2\sigma$ on contour areas, lacks a clear justification and may not be universally applicable across diverse datasets. Furthermore, the adaptive threshold in PPSM, while designed to balance true and false positives, lacks a rigorous mathematical explanation of how the scaling factor is derived and why it is optimal. The absence of a theoretical basis for these design choices makes it difficult to assess the robustness and generalizability of the approach.

2. Insufficient Baseline Model Comparisons: The experimental comparisons of PerSense are limited to a few general segmentation models (e.g., PerSAM, Matcher) and lack comparisons with other classic indoor segmentation or dense scene methods. For instance, in dense scene segmentation tasks, other clustering-based or feature-matching models might also provide effective solutions. The absence of such baseline model comparisons weakens the demonstration of PerSense's advantage in specific tasks. For example, methods that leverage graph-based approaches for instance segmentation, or those that use more sophisticated feature matching techniques, are not considered. This lack of comparison makes it difficult to ascertain whether the performance gains are due to the specific design of PerSense or if similar results could be achieved with existing techniques.

3.  Dataset diversity: Although the PerSense-D dataset focuses on dense scenes, it is relatively small in scale (717 images) with limited category coverage, failing to fully represent diverse dense scenes. Real-world applications in personalized segmentation for dense scenes often require larger and more varied samples (e.g., different resolutions, scene types). The dataset's limited size and scope may not adequately capture the variability present in real-world dense scenes, potentially leading to overfitting or a lack of generalizability to other datasets. Additionally, the absence of a detailed analysis of the dataset's characteristics, such as the distribution of object sizes and the degree of occlusion, makes it difficult to assess the dataset's representativeness and the model's performance under different conditions.

4. Experimental Analysis : The ablation studies primarily highlight the incremental effects of IDM, PPSM, and the feedback mechanism, but do not thoroughly explore the synergy among components. For example, the impact of different density map generators (DMG) on model performance is not fully analyzed. Additionally, there is a lack of analysis on the specific contributions of multimodal features (e.g., visual and textual features) in personalized segmentation tasks, making it challenging for readers to understand the role of each feature in the overall performance. The ablation study should include more fine-grained analysis of the interaction between the modules, such as the effect of different combinations of modules, and also explore the impact of varying parameters within each module.

### Questions
1. Although the design of PerSense's modules is somewhat innovative, the theoretical support is insufficient. For instance, there is no mathematical proof of how IDM and PPSM improve segmentation accuracy, particularly regarding how they outperform other methods in generating point prompts in dense scenes. Further mathematical derivation would enhance the theoretical foundation of this approach.
2.The experimental validation of this feedback mechanism is limited, as it does not demonstrate the impact of different iteration counts on segmentation accuracy. For example, does varying the initial exemplar selection strategy or iteration count significantly affect model performance? .
3.In dense scenes, challenges like occlusion, lighting changes, and varying object sizes can affect the robustness of segmentation models. However, the paper does not conduct robustness experiments to address these factors. For instance, how does the model perform under low lighting, complex backgrounds, or heavy occlusion?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a training-free method to achieve personalized instance segmentation, which aims to segment what people want with refering images.  It develops a new baseline capable of automatically generating instance-level point prompts via proposing a novel Instance Detection Module (IDM) that leverages density maps, encapsulating spatial distribution of objects in an imageA dataset PerSense-D is proposed to boost this research area.

### Strengths
1. This article's research on the task of refining segmentation is valuable. The proposed dataset is helpful for the development of this field.
2. This method can achieve the desired effect without training, and has higher application value in this regard.

### Weaknesses
1. The writing and organization of the article need to be improved:
a. In Figure 1, "(a)" appears twice
b. The method section lacks a paragraph that links together how several modules operate. And the caption in Figure 2 is also very brief, requiring a description of the structure.
c. It is not recommended to write the abstract in the form of contribution (1), (2), (3)
2. In line 43, I did not get the difference between personalized instance segmentation and traditional instance segmentation. The traditional setting is also aimed at segmenting the specified categories in the image. Do I need to give a category name for input? After reading the article, my understanding is that by providing a template for referencing, other similar targets are required to be segmented. It does not mean segmenting the specified category, but segmenting the specified referencing. If I understand correctly, C3Det([1],CVPR2022) has a similar idea (even if it is a detection) and needs to be compared and discussed (its inspection results can be used for segmentation by SAM). SegGPT([2] ICCV2023) also uses some template images to segment the desired objects. Please compare and discuss.
3. SAPNet (CVPR2024) uses Point prompt combined with SAM to generate candidate masks, and selects masks that meet specific categories as outputs. This idea is similar to this article, please discuss it. (Even if the method uses point annotation, the point prompt predicted in the first stage of this article can be used as its input instead of point annotation.) In addition, methods such as Bestie (CVPR2022) have also predicted peak points as point prompts through affinity maps, density maps, and other methods. Please compare and discuss.
4. Although COCO and LVIS are not specifically designed for dense scenarios, they do not hinder the validation of our method in this paper. And the size of COCO and LVIS is still much larger than the dataset in this article. I acknowledge the contribution of the dataset, but I believe that validation experiments on COCO or LVIS are still necessary to demonstrate the effectiveness of the proposed method in this article. After verifying with more datasets, I will consider increasing the score.
5. Visualization can incorporate qualitative validation of some methods to demonstrate comparison with benchmark methods and show the effectiveness of the proposed modules.

### Questions
See weakness part.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work focuses on personalized instance segmentation in dense and crowded scenarios. To this end, they propose PerSense, a training-free framework. Specifically, they use a class-label extractor (CLE) and a grounding detector to select the effective exemplars for a density map generator (DMG). Then, they propose an instance detection module (IDM) to generate point prompts from the density map and design a point prompt selection module (PPSM) to reduce false positive predictions. Last, the authors further introduce a feedback scheme to refine the exemplar selection and thus improve the performance of PerSense. Moreover, they propose a dataset, PerSense-D, for the evaluation of instance segmentation in dense images. However, I still have some questions about the experimental settings.

### Strengths
1. The proposed PPSM effectively removes the false positive predictions.
2. The proposed feedback mechanism further improves the density maps of DMG and boosts the performance of personalized instance segmentation.
3. The authors propose a new data set with 717 images and 28,395 objects for personalized instance segmentation.

### Weaknesses
1. The authors compare the proposed method with the SOTA methods on PerSense-D. However, I noticed that the authors conducted ablation studies on the same dataset to pursue the best performance. As there are no more results on other datasets, the superior performance of the proposed method needs to be verified. Specifically, the ablation study, which involves iterative adjustments and evaluations on the PerSense-D dataset, risks overfitting the method to the characteristics of this specific dataset. This makes the subsequent comparison against other methods less reliable, as the proposed method's performance might be artificially inflated due to the optimization process on the same data. The lack of evaluation on other datasets further exacerbates this concern, making it difficult to assess the generalizability of the proposed method.
2. In Table 2, it is unclear why the method achieves the best performance with a normalized factor equal to sqrt(2). More discussions on the insight of normalized factors are required. The choice of $\sqrt{2}$ as a normalization factor seems arbitrary without a clear theoretical or empirical justification. The paper should delve deeper into the mathematical properties of the density maps and the cosine similarity scores to explain why this specific value yields optimal results, rather than simply stating it as an empirical finding. The lack of a principled explanation makes it difficult to understand the underlying mechanism and limits the practical application of the proposed method.
3. Although the feedback mechanism effectively improves the performance of the proposed method, it seems that this mechanism violates the one-shot setting. In this sense, the comparison with Grounded-SAM seems not fair. The feedback mechanism, which refines exemplar selection based on initial segmentation results, introduces an iterative process that deviates from the strict one-shot learning paradigm. This iterative refinement, even if it doesn't use additional labeled data, still leverages information from the query image to enhance the model's performance, which is not present in a true one-shot setting. This makes the comparison with methods like Grounded-SAM, which adhere to a strict one-shot protocol, questionable.
4. At line 379, page 8, “x 1.02” should be “$\times 1.02$”.
5. In Table 2(c), “No of Shots” should be “No. of Shots”.

### Questions
I think at least the authors should split the proposed dataset for validation and testing.

### Soundness
2

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
4

### Summary
This paper proposes a training-free and model-agnostic one-shot framework for personalized instance segmentation in dense images. The proposed framework, PerSense, is featured with a Instance Detection Module (IDM), a Point Prompt Selection Module (PPSM), and feedback machanism to improve the accuracy of density maps. Besides the framework, a dataset PerSense-D is introduced for personalized segmentation in dense images and demonstrating the superiority of the proposed method by comparing it with the SOTA on this benchmark. According to the quantitative and qualitative results, the proposed method shows a performance improvement with a clear margin. Experiments are well analyzed and ablation study is well designed to show the effectiveness of proposed component.

### Strengths
1. Personalized instance-level segmentation which this paper target to solve is an interesting and important scenario for automation. The training-free manner ensures the ease for deployment.
2. Good performance of the proposed method from both qualitative and quantitative view and well experimental analysis. 
3. Dataset contribution. PerSense-D is introduced as a dataset exclusive to personalized segmentation in dense images.
4. The whole paper is well organized and presented.

### Weaknesses
1. This paper claim they provide a one-shot personalized segmentation framework in instance level. However, the main results reported in table 1 seems come from 4-shot setting according to table 2 (c). If so, the 1-shot result should be reported to support the claimed contribution.
2. The proposed framework is complex by combining lots of existing methods or modules. Although the inference time is evaluated, memory consumption is not reported, which is critical for real deployment. 
3. No result on standard segmentation datasets is reported. Results on datasets with fewer objects can provide a better understanding on the proposed framework.
4. It seems the feedback mechanism plays an important role to ensure a high performance. But better feedback may involve more local iteration to avoid false positive and instance missing, which leads to longer inference time.

### Questions
1. Will the codes and PreSense-D dataset be released?
2. Why does PerSense fail to have a superior performance over other methods on standard segmentation datasets with few object instances? Could authors have more discussion on the drawbacks of the proposed framework?

### Soundness
4

### Presentation
4

### Contribution
3
