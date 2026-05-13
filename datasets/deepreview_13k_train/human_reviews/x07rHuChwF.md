# Euclid: Supercharging Multimodal LLMs with Synthetic High-Fidelity Visual Descriptions

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
Multimodal large language models (MLLMs) have made rapid progress in recent years, yet continue to struggle with \emph{low-level visual perception} (LLVP)---particularly the ability to accurately describe the geometric details of an image. This capability is crucial for applications in areas such as robotics, medical image analysis, and manufacturing. 
In this paper, we first introduce \emph{Geoperception}, a benchmark designed to evaluate an MLLM’s ability to accurately transcribe 2D geometric information from an image. Using this benchmark, we demonstrate the limitations of leading MLLMs, and then conduct a comprehensive empirical study to explore strategies for improving their performance on geometric tasks. Our findings highlight the benefits of certain model architectures, training techniques, and data strategies, including the use of high-fidelity synthetic data and multi-stage training with a data curriculum. Notably, we find that a data curriculum enables models to learn challenging geometry understanding tasks which they fail to learn from scratch. Leveraging these insights, we develop \emph{Euclid}, a family of models specifically optimized for strong low-level geometric perception. Although purely trained on synthetic multimodal data, Euclid shows strong generalization ability to novel geometry shapes. For instance, Euclid outperforms the best closed-source model, Gemini-1.5-Pro, by up to 58.56\% on certain Geoperception benchmark tasks and 10.65\% on average across all tasks.

\vspace{3mm}
\coloremojicode{1F310} \textbf{Website}: \href{https://euclid-multimodal.io}{euclid-multimodal.io}

\coloremojicode{1F917} \textbf{Model Weights \& Datasets}: \href{https://huggingface.co/euclid-multimodal}{huggingface

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- The paper studies multimodal large language models (MLLMs) on the task of low-vele visual perception — particularly, testing and improving MLLMs for tasks related to Euclidean geometric concepts like points, lines, and angles.
- The first part of the study highlights significant failures of the recent open-sourced and closed-sourced MLLMs including GPT4o, Gemini, and Molmo.
- In the second part, the authors trained the MLLM on a very simple generated synthetic geometric data, which is composed of only 3 shapes (but multiple questions/answers per shape) for each geometric concept/axiom.
- They also introduce a geometry concept benchmark, named Geoperception, which is a filtered version of Geometry-3K corpus (Lu et al., 2021), as a test-bed to support the above two points.

### Strengths
- The paper studies an important and open topic of the application of MLLMs on geometric problem datasets. Furthermore, comparisons of prior SOTA MLLMs and their failures further enhance the importance of the paper.
- The release of the filtered GeoPerception benchmark will support future works.
- Achieves 3x performance boost compared to Gemini1.5-Pro on `PointsonLines` questions and roughty +15% on average.
- Paper writing is overall clear and related works are well covered.

### Weaknesses
 - Clarification regarding sampling multiple answers per question
    - "Molmo predicts every potential answer, leading to their poor accuracy scores" – If this means, that instead of only answering the required/asked points on the line, Molmo outputs all the points on the line –– this seems less critical. It would be great if the authors could also share the accuracy if the prediction is a superset of the required answer. Specifically, it would be useful to understand if the model is identifying the correct points but also including extraneous ones. This could be evaluated by considering a prediction correct if it contains all the required points, even if it includes additional incorrect ones.
    - How are multiple possible answers handled if some answers are incorrect, but there is at least one correct answer? As per evaluation score formulae, score = |Prediction| / |Ground Truth|. It will be again good to know the score of each MLLM if the formulae would have been score=1 if P is a subset of G. This will help understand if the accuracy of MLLMs can be enhanced by non-deterministic nucleus sampling. This is particularly important because the current metric penalizes models for over-generating, which might not reflect their understanding of the geometric concepts.
    - On the above point, how many solutions are sampled for each question? Is any form of nucleus sampling performed i.e. sampling multiple answers per question? Please provide details for the same.

- What does it mean to compose a dataset of only 3 shapes? Were all the training and the validation question-answer pairs for training generated only from 3 shape instances? Clarification on the differences between the terminology "shapes" and geometric question/answer pairs would be great. It's unclear if the 3 shapes refer to 3 distinct geometric configurations or if it refers to 3 instances of the same geometric concept with different numerical values. This distinction is crucial for understanding the diversity and generalizability of the training data.

- Following the above question, it might be important to increase the dataset by sampling more shapes from the geometric shape generation engine and then training on that dataset. The current approach might limit the model's ability to generalize to unseen geometric configurations. Expanding the variety of shapes could lead to more robust and reliable performance.

- Comparison against a baseline that performs supervised fine-tuning of existing MLLMs rather than training the vision part of MLLMs (fine-tuning vision backbone and adapter) from scratch. This is a crucial comparison to understand if the performance gains are due to the novel training approach or simply due to fine-tuning a large model on the task. Fine-tuning an existing MLLM could serve as a strong baseline to evaluate the effectiveness of the proposed method.

- Furthermore, it seems that the generated training dataset is relatively quite small. Comparison among different convolution and ViT-based image backbones might not be optimal under such small dataset settings. It would be nice to either test this on larger datasets or be subtle of this observation made. The same might be true for the training data curriculum. The small dataset size might lead to overfitting and make it difficult to draw meaningful conclusions about the effectiveness of different backbone architectures. It is important to validate these findings on a larger dataset to ensure the robustness of the results.

- Rather than designing a human-designed curriculum (based on what human finds complex), doing negative-hard mining might be a strategy to design a curriculum automatically. It would be great if the authors could compare against such a strategy. This could provide a more data-driven approach to curriculum design, potentially leading to better performance and faster convergence.

### Questions
- My main concerns are regarding the small size of the dataset (any clarifications on the true train dataset size), or results on enhanced dataset size would be appreciated. Conclusions made on such a small dataset cannot be accepted to scale with dataset size.
- It would be great if the authors could share results from the requested baseline (supervised fine-tuning of existing MLLM) and automatic curriculum training based on negative-hard mining.

If my main concerns on the small training dataset size are addressed, I would be happy to increase my rating.

### Soundness
2

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
This paper addresses the limitations of MLLMs in low-level visual perception. Specifically,  It introduces a benchmark, Geoperception, to evaluate MLLMs' ability to transcribe 2D geometric information.  Effective strategies for enhancing model performance are identified, including high-fidelity synthetic data and a data curriculum approach. It also develops a new family of models, named Euclid, optimized for geometric perception, which significantly outperforms existing models, demonstrating strong generalization to novel geometric shapes.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper conducts extensive experiments to systematically explore the impact of geometric shapes of increasing complexity and identifies some key lessons.
3. The paper shows that the Euclid model trained on high-fidelity synthetic data exhibits strong generalization capabilities, especially in real-world geometric shape understanding tasks, significantly surpassing existing leading MLLMs.

### Weaknesses
1. Concerns about Data Filtering with MLLM. Since Geoperception is a new benchmark intended to evaluate the precise geometric perception capabilities of MLLMs, and given that these models exhibit limited geometric understanding, it appears unreasonable to utilize gpt-4o-mini for data filtering purposes. The reliance on a model with known limitations in geometric reasoning to validate the very data designed to test such reasoning introduces a potential bias or circularity in the benchmark creation. Specifically, if GPT-4o-mini struggles with certain geometric configurations, it might inadvertently filter out valid but complex examples, thus skewing the benchmark's difficulty and scope.
2. Limited Comprehensive Geometric Understanding. The results in Table 4 shows the performance limitations of Euclid on multiple tasks, such as POC and LHC. They may be linked to the benchmark data distribution. It would be beneficial for the authors to conduct further experiments aimed at enhancing this aspect. The relatively poor performance on tasks like Point-On-Circle (POC) and Line-Has-Circle (LHC) suggests that the model might be overfitting to specific types of geometric relationships present in the training data, while lacking a more generalized understanding of geometric principles. This raises concerns about the model's ability to handle diverse and complex geometric scenarios beyond those explicitly seen during training.

### Questions
Please refer to the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new benchmark, Geoperception, sourced from Geometry-3K, to evaluate MLLMs' ability to perform geometric perception. The dataset is in QA form, and the benchmark has seven tasks. Most are about element relationships in geometric images, such as points, lines, and angles. The author also proposes a method called Euclid, a fine-tuned MLLM that may outperform other MLLMs.

### Strengths
Geometric perception benchmark may seem a novel topic to me. The benchmark can contribute to the MLLM community.

### Weaknesses
- Overall, this paper devotes a significant amount of space to introducing background information and other methods, while providing relatively fewer details about its own proposed approach. I think the amount of work is below the average level for ICLR. Therefore, I believe the contributions of this paper are insufficient for acceptance at a top-tier conference like ICLR.

- The proposed task is sourced from Geometry-3K and seems to be easier than it. Since Geometry-3K contains some calculations, while this benchmark is mainly about some relationships between elements, such as whether point A is on Line A. I know the paper is trying to explore the geometric perception topic, but Geometry-3K also needs some level of perception, or models cannot do the harder calculation.  

- For baselines, why not directly fine-tune some MLLMs on Geoperception, to compare with the method of Euclid?

- If an MLLM has been fine-tuned on this perception dataset, will it gain the ability of other types of perception, such as real images or medical images?

### Questions
- Why not consider the multiple-choices form for question answering?

- Is it possible to transform geometric figures into SVG code, just as VDLM, to evaluate the performance of the OpenAI-o1 model? Moreover, the authors may add some evaluation on some geometry MLLMs or math MLLMs.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors present Geoperception, a VQA dataset sourced from Geometry-3K. Geoperception requires reasoning over "surface-level geometric information" to identify points and line segments that satisfy conditions, and to classify angles. The authors evaluate a variety of existing MLLMs on the dataset and find that they do not perform consistently. Motivated by the results of the evaluation, the authors train their own MLLM, Euclid, on synthetic samples created using modified AlphaGeometry tooling. They also measure the effects of several design choices on their synthetic dataset.

### Strengths
1. The writing of the paper is above-average.
2. Diagnostic benchmarks are valuable and relevant to the ICLR community.
2. The results of the visual-tokenizer evaluation are interesting.

### Weaknesses
1. Performance on the benchmark seems likely moreso dominated by syntax than reasoning ability: "Certain models, such as GPT-4o-mini (Achiam et al., 2023) and Molmo-7B-D (Deitke et al., 2024), frequently either enumerate all potential components (e.g., all points in a diagram instead of the one on the lines) or every potential answer, leading to their poor accuracy scores." Given the authors have identified this as an issue, it seems difficult to conclude from the investigation that "Current MLLMs struggle to perceive low-level geometry annotations and relationships." The authors' claim that models have "no difficulty in understanding verbal instructions and questions" is not well-founded, as the models' ability to adhere to the answer template does not demonstrate an understanding of the question itself. It has not been demonstrated that "top models such as Gemini-1.5-Pro struggle significantly" as a result of "visual perception weakness rather than syntax error." Some questions are ungrammatical, such as asking "What is the point lying on circle with center G?" when the correct answer includes three points. Some are ambiguous, such as "Which line is longer, AE or ED?" where the answer can not be discerned from the symbols and requires measurement. Others are inconsistently labeled, like alphabetizing segment ends in answers ("CD") but not questions ("What is the line parallel to line EB?") or including duplicate answers ("ZV, VZ").
2. If the task itself had real-world application, the effect of syntax would be of lesser concern. However, "as a focused test bed" "designed to evaluate MLLMs’ ability to accurately perceive surface-level geometric information without requiring complex inference or reasoning" it is far removed from the "real-world applications" used to motivate the work: "spatial understanding for robotics, medical image analysis for accurate diagnosis, quality control in manufacturing to detect subtle defects, autonomous driving systems that rely on exact object localization or distance estimation, and augmented reality applications that demand precise overlay of virtual objects onto the real world."
3. The "detailed empirical exploration of MLLM architecture and training strategies" is disappointingly shallow. The only ablated architecture choice is the visual encoder. In their "investigation," the authors do not ask why the "CNN architecture performs better than ViT," they only present it as a "lesson." The second lesson, that "Tuning the visual encoder is beneficial," should be considered a given when one is evaluating on the training distribution. What is potentially compromised is generalization ability, which is why the ablations should have instead been measured on the evaluation set.
4. The authors' statement that they "demonstrate the limitations of leading MLLMs, and then conduct a comprehensive empirical study to explore strategies for improving *their* performance on geometric tasks" (emphasis added) is misleading. The authors do not improve the performance of existing MLLMs, opting instead to train their own from an existing visual encoder and language model. As such, it is difficult to say that "lessons we learn from this domain can be effectively generalized to a broader set of downstream domains that benefit from high-quality low-level visual perception." Had the authors tried finetuning an existing model, it's plausible that it would not be necessary to introduce a "data curriculum" to enable "models to learn challenging geometry understanding tasks which they fail to learn from scratch."
5. The curriculum training appears irrelevant as the "dataset generation engine can produce infinite samples for exhaustive task-specific training" and "Adaptive Curriculum" performance appears to match "Mixed Shape" at saturation when trained with 150% the samples (Figure 6). The authors' characterization of "mixed-shape training" as "spontaneous curriculum learning" is non-standard and is not aligned with literature. As it stands, it has not been demonstrated that "a data curriculum enables models to learn challenging geometry understanding tasks which they fail to learn from scratch." Why is it of practical value to "further enhance model efficiency on challenging shapes" and why is it true that "employing a curriculum-based training approach yields much more model potential than direct task training"?
6. The authors' claims are overstated. It is not true that "Euclid significantly outperforms current leading MLLMs," "surpassing the leading MLLMs by a substantial margin." It is outclassed by Gemini-1.5-Pro on one of the four tasks and exceeds it by less than a percent on another. The authors must correctly qualify their claims. When the full benchmark is included, the overall quantitative edge of the proposed model over the top-performing zero-shot baseline decreases from 14.29% to 4.81%. If "top models ... struggle significantly," it cannot be said that "Euclid achieves strong performance."

### Questions
1. Why are only four out of seven benchmark tasks used for evaluation of the proposed model (Table 4)?
2. In the related work, the authors write that "VDLM (Wang et al., 2024b) transcribes raster images into vector graphics and uses LLMs to reason over the SVG code. They find that although SVG code is not straightforward to understand, using LLMs to reason over SVG is consistently more effective than directly using MLLMs on original raster images." If reconstructing prior to reasoning is "consistently more effective," why is it not evaluated against? Why is it important that Geoperception be solved through intermediate-free VQA?
3. The authors state their task is "straightforward for humans" but do not provide quantitative comparison. Have they measured this?

Further comments:
1. The title does not seem very representative of the paper content and appears overly sensational. The authors are suggested to change it to remove mention of Euclid, which the authors have not demonstrated to be generally applicable outside the benchmark, and focus on Geoperception which seems to be the real contribution of the work.
2. The authors write "For our Euclid model, we include all geometry shape code used for training, along with demonstration diagrams and pseudocode for generating training questions and answers," but it does not appear that supplementary materials were submitted.

### Soundness
3

### Presentation
3

### Contribution
3
