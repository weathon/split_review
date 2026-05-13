# Meta-Continual Learning of Neural Fields

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Neural Fields (NF) have gained prominence as a versatile framework for complex data representation. This work unveils a new problem setting termed Meta-Continual Learning of Neural Fields (MCL-NF) and introduces a novel strategy that employs a modular architecture combined with optimization-based meta-learning. Focused on overcoming the limitations of existing methods for continual learning of neural fields, such as catastrophic forgetting and slow convergence, our strategy achieves high-quality reconstruction with significantly improved learning speed. We further introduce Fisher Information Maximization loss for neural radiance fields (FIM-NeRF), which maximizes information gains at the sample level to enhance learning generalization, with proved convergence guarantee and generalization bound. We perform extensive evaluations across image, audio, video reconstruction, and view synthesis tasks on six diverse datasets, demonstrating our method’s superiority in reconstruction quality and speed over existing MCL and CL-NF approaches. Notably, our approach attains rapid adaptation of neural fields for city-scale NeRF rendering with reduced parameter requirement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Briefly, this paper presents a strategy to continually and rapidly learn neural fields in a meta-learning manner. The paper further introduces a fisher information maximization loss for neural radiance fields. The proposed method advances in leading to no performance degradation incurred by forgetting during test-time by synergizing modular architecture with meta-learning.

### Strengths
+ The paper is well written and easy to follow. 
+ Extensive and comprehensive experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
 + The technical novelty of the proposed method seems to be marginal since the authors directly employ the existing techniques. For instance, Fisher Information against catastrophic forgetting has already been proposed by Kirkpatrick et al., 2016. The authors do discuss the relation to this method and claim that their proposed FIM loss operates at the sample level rather than the parameter level. However, it is difficult to identify the advantage of the proposed FIM loss over the parameter-level approaches in CL (Chaudhry et al., 2018; Konishi et al., 2023) without fair experimental comparison and detailed discussion.

+ More detailed discussions and analyses in Table 1 are required to demonstrate the contribution of the proposed method. Specifically, the current analysis lacks depth in explaining why the proposed method outperforms existing approaches, and it does not provide sufficient insight into the specific scenarios where the method excels or falls short. The discussion should also include an analysis of the trade-offs between performance and computational cost.

+ More recent state-of-the-art methods should be included for comparison to demonstrate the superiority of the proposed method. For instance, missing some SOTA methods, e.g., (Chung et al., 2022 and Po et al., 2023), for comparison on the MatrixCity dataset in Table 1. The absence of these comparisons makes it difficult to assess the true advancement of the proposed method in the context of the current state-of-the-art.

+ More ablation studies in the main paper are required to demonstrate the contribution of the main component (i.e., the FIM loss) of the proposed method in the main paper. The authors only provide some results about the mod and MIM  with two different hidden dimensions in Appendix Table 2. The lack of detailed ablation studies makes it difficult to understand the individual contributions of each component of the proposed method. Specifically, the impact of the FIM loss on the overall performance should be thoroughly investigated with varying hyperparameters and datasets.

### Questions
Please refer to the Weaknesses section.

There is a wrong citation in either Line 322 (EWC Chaudhry et al., 2018) or Line 402 (EWC (Kirkpatrick et al., 2016) ). Actually, Chaudhry et al., 2018 denote their method as EWC++.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The problem of continual learning in neural fields is an important topic. This work focuses on addressing the issues of catastrophic forgetting and slow convergence in existing approaches by proposing a new paradigm called MCL-NF. It introduces the Fisher Information Maximization loss. The experiments demonstrate that the proposed method can achieve satisfactory results.

### Strengths
1.	This paper is well-written.
2.	This work combines meta-learning and continual learning paradigms into neural field training to address the challenges of catastrophic forgetting and slow convergence, which is interesting.
3.	This paper demonstrates the advantages of their method in experiments, which alleviates the issue of slow convergence to some extent.

### Weaknesses
1.	In the experimental section, the limited scenarios are my main concern, which makes me worry about the limitations of the method. Specifically, the experiments primarily focus on relatively simple image and video datasets, and do not adequately explore the method's performance on more complex and diverse datasets, such as those with significant variations in lighting, viewpoint, or object types. This raises concerns about the generalizability of the proposed approach to real-world scenarios.
2.	The paper uses a large number of quantitative metrics but lacks qualitative comparisons, especially for neural radiance fields. While quantitative metrics like PSNR and SSIM provide numerical measures of performance, they often fail to capture the perceptual quality of the rendered results. A qualitative comparison, such as visual comparisons of rendered images, would be beneficial to assess the visual fidelity of the proposed method.
3.	In neural fields, some incremental learning methods [1] might also need to be discussed, but they are not mentioned in the article. The absence of a discussion of relevant incremental learning methods in the context of neural fields makes it difficult to contextualize the proposed method's contribution and limitations within the existing literature.

4.	The paper is recommended to discuss the differences between continuous radiance fields and traditional continual learning. Issues like catastrophic forgetting and slow convergence have long been a focus of continual learning researchers, and a discussion of how these challenges manifest differently in the context of neural radiance fields would be valuable.

### Questions
Please kindly refer to the above weaknesses.

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
3

### Summary
The paper introduces Meta-Continual Learning of Neural Fields (MCL-NF), a framework merging modular neural architectures with meta-learning strategies to support continuous and adaptive learning of neural fields. The proposed approach aims to address the challenges in traditional continual learning for neural fields, such as catastrophic forgetting and slow convergence. The authors implemented Fisher Information Maximization loss (FIM loss) to optimize learning by emphasizing more informative samples, achieving improved generalization and learning speed. The paper’s extensive experiments across various tasks including image, audio, video and NeRF-based view synthesis, highlight the performance advantages of MCL-NF over existing methods. They offer an efficient and scalable solution suitable for large-scale and resource-constrained environments, advancing the capabilities of neural fields in sequential learning settings.

### Strengths
1. MCL-NF’s combination of modular architecture and optimization based meta-learning is innovative and meets the adaptability needs of neural fields. 
2. The method mitigates catastrophic forgetting through modularization and shared initialization, without the need for experience replay that can be resource-intensive. The modular approach within meta-continual learning sounds pretty compelling.
3. The FIM loss implementation is theoretically sound, supported by convergence guarantees, and introduces a detailed weighting mechanism for learning stability and efficiency. 
4. The paper provides thorough experimental results, showcasing the model’s performance on various datasets, supporting the robustness of MCL-NF. The concept of evaluating the method in different modalities definitely deserves recognition. 
5. This work helps understand the broader scope of how meta-learning techniques could be integrated successfully with frameworks for continual learning, particularly in the context of neural fields. This can help further research to consider similar synergies between learning paradigms, which may result in even more powerful and generalizable machine learning models.
6. The paper is well-organized and written in a clear, academic tone. It is suitably embedded in the meta-continual learning world  with relevant citations. The authors show their deep understanding of the topic by presenting the setting, highlighting its motivation and organizing the experiments in a structured way.

### Weaknesses
1. The setting, at least in the image domain, seems artificial - dividing the images into four patches (regardless of the size) seems to raise some concerns. It would be desirable to present an ablation study on it. The lack of a clear rationale for this specific patch-based approach, especially given the potential for alternative image decomposition techniques, makes it difficult to assess the generalizability of the method. An ablation study should explore different patch sizes or even alternative decomposition methods, such as overlapping patches or frequency-based decompositions, to determine the sensitivity of the results to this design choice.
2. From a continual learning perspective, this setting is highly confusing. It should be explicitly described how the data is selected, processed and how the model is evaluated. The paper does not clearly articulate how the continual learning tasks are constructed, particularly how the data is selected and processed for each task. The evaluation protocol also lacks clarity, especially regarding how performance is measured across the sequence of tasks and how the model's ability to retain knowledge from previous tasks is assessed. A more detailed explanation of the data selection, processing, and evaluation procedures is necessary to properly understand the experimental setup.
3. The paper lacks more recent methods in the main table. And even if MAML is a well-known method, it is quite outdated, with lots of recent enhancements such as La-MAML [1] for continual learning.  Moreover, the comparison is mostly made against methods in a different setting with only two methods in MCL (and MAML was published in 2017). The comparison to MAML, while a foundational meta-learning algorithm, is insufficient given the advancements in continual learning. The inclusion of more recent methods, especially those specifically designed for continual learning, is necessary to provide a more robust evaluation of the proposed approach. The limited number of methods in the same setting further weakens the comparative analysis.
4. And even in different settings (not MCL), the papers are well-established, but some of them nowhere near the current state-of-the-art. There is no elaboration how this approach differs from recently presented settings/methods such as [2]. And even if they are mentioned, such as ANML they are not compared against. The lack of comparison to state-of-the-art methods, even in different settings, limits the assessment of the proposed approach's novelty and effectiveness. The paper should clarify how the proposed method differs from recent approaches and provide a more comprehensive comparison to establish its position in the field. The absence of a comparison with ANML is a significant oversight, given its relevance to the topic.
5. Experimental results show the performance with a number of continual tasks set to only four, which raises concerns regarding the method’s scalability. The limited number of continual tasks (four) used in the experiments raises concerns about the scalability of the proposed method. The paper should include experiments with a larger number of tasks to demonstrate the method's ability to handle more complex continual learning scenarios. The lack of such experiments makes it difficult to assess the method's practical applicability in real-world settings.
6. These experimental results are largely dependent on PSNR as the main metric of reconstruction quality. Additional metrics, such as Structural Similarity Index (SSIM) for image and video tasks, or perceptual evaluation metrics for audio, would provide a more comprehensive validation of MCL-NF’s performance. The reliance on PSNR as the primary evaluation metric is insufficient to fully assess the quality of the reconstructions, especially in image, video, and audio tasks. The inclusion of additional metrics, such as SSIM for image and video tasks and perceptual evaluation metrics like PESQ for audio, would provide a more comprehensive and robust evaluation of the proposed method's performance.

Minor issues:
Line 155 - Redundant closing bracket

### Questions
1. Could additional strategies beyond Fisher Information, such as curriculum learning, improve MCL-NF's adaptability and reduce reliance on specific meta-learning techniques?
2. Should the paper also use different techniques of splitting the image than cropping into patches? The idea behind the method is based on that, and perhaps applying Fourier Transformations would be beneficial.
3. Could alternative loss functions achieve similar sample prioritization for continual learning? If so, what criteria would make FIM the preferred choice?
4. As far as I understand, we treat each image separately (batch size 1). How do we find the appropriate number of coordinates?
5. What insights can this setting bring to the continual learning community?
6. In the methods compared without modularization, do these approaches utilize the full MLP network capacity to match the parameter count of the modularized versions?
7. The Fisher Information Maximization loss introduces a new hyperparameter. Could you provide more details on how this hyperparameter was selected and discuss its sensitivity and impact on the model's performance?

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
2

### Summary
In this paper, the authors propose a new problem setting and strategy to introduce meta-continual learning in neural fields. They conduct extensive experiments to demonstrate that their approach outperforms baseline methods.

### Strengths
1.	Experiments on various datasets are conducted to validate the effectiveness of the method.
2.	The method is general and could be applied to many different applications.

### Weaknesses
1.	The implementation and comparison are conducted based on methods published in 2021 and 2022. Only SwitchNeRF was published in ICLR 2023, which was also long ago. It is kindly suggested to conduct experiments on more recent methods to evaluate the proposed approach. I would like to see some comparative experiments with [a].
2.	I would expect more visualization in the experiments, for example, comparison of view synthesis on MatrixCity dataset.
3.	The experiments should include some commonly used evaluation metrics, such as SSIM.

### Questions
See Weakness

### Soundness
3

### Presentation
2

### Contribution
2
