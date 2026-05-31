## Human Reviewer 1

### Summary
This paper introduces grounding-IQA, a new task paradigm that integrates multimodal referring and grounding capabilities with image quality assessment (IQA) to enable fine-grained quality perception. The authors identify that existing MLLM-based IQA methods primarily rely on general contextual descriptions, limiting their ability to perform detailed quality assessment. To address this, grounding-IQA consists of two subtasks: GIQA-DES (grounding-IQA-description), which provides detailed quality descriptions with precise spatial locations such as bounding boxes, and GIQA-VQA (visual question answering), which focuses on quality-related questions for local image regions. The authors contribute GIQA-160K, a dataset constructed through an automated annotation pipeline, and GIQA-Bench, a comprehensive benchmark that evaluates model performance from three perspectives: description quality, VQA accuracy, and grounding precision. Experimental results demonstrate that the proposed task paradigm, dataset, and benchmark effectively facilitate more fine-grained IQA applications.

### Strengths
1.  The paper is well-organized with a clear logical flow, making it easy for readers to understand the motivation, methodology, and contributions. The task paradigm is clearly defined with concrete subtasks (GIQA-DES and GIQA-VQA), facilitating comprehension of the proposed approach.

2.  The proposed automated annotation pipeline for constructing GIQA-160K represents a valuable contribution to the field. This approach addresses the scalability challenge of obtaining fine-grained quality annotations with spatial grounding, potentially benefiting future research in grounded IQA tasks.

3. GIQA-Bench provides a well-designed evaluation framework that assesses model performance from three complementary perspectives: description quality, VQA accuracy, and grounding precision. This multi-faceted evaluation approach enables thorough analysis of grounding-IQA capabilities and sets a solid foundation for future work in this area.

### Weaknesses
1. Questionable Task Scope and Definition: The paper claims to address image quality assessment (IQA), which is a broad concept encompassing various quality dimensions such as saturation, color distortion, noise, compression artifacts, etc. However, the proposed method primarily focuses on motion blur of objects, which requires enhanced referring and grounding capabilities. This narrow focus does not adequately represent the full spectrum of IQA. The work would be more convincing if the problem were explicitly defined as "motion blur assessment" or "local distortion grounding" rather than claiming to solve general fine-grained IQA. The current framing creates a mismatch between the stated goal and actual contribution.

2. Limited Generalization Evidence: Even for motion blur assessment, the method's scope appears limited. Most examples showcase salient objects (e.g., people, animals, vehicles), but it remains unclear whether the approach generalizes to other scenarios such as text blur, background element blur, or subtle quality degradations in non-salient regions. The proposed benchmark does not sufficiently demonstrate the model's generalization capability across diverse object categories and blur scenarios, raising concerns about practical applicability.

3. Lack of Evaluation on Public Benchmarks: A critical experimental gap is the absence of evaluation on established public IQA benchmarks. The authors only test their trained model on the self-proposed GIQA-Bench, which limits the ability to assess the method's performance relative to existing approaches and raises questions about potential dataset-specific overfitting. Evaluation on standard IQA datasets would provide stronger evidence of the method's effectiveness and facilitate fair comparison with prior work.

### Questions
1. The automated annotation process relies on an existing MLLM (Q-Instruct) to label blur regions, which raises concerns about robustness and error propagation. Can the authors provide evidence demonstrating the reliability of this approach? A potentially more robust alternative would be to synthesize the dataset using pristine images and applying controlled blur degradations at different levels, which would provide natural bounding box annotations and standardized quality labels. How does the current approach compare to such synthetic data generation methods?

2. The paper lacks detailed description of how data contamination between GIQA-160K and GIQA-Bench is prevented. Can the authors explicitly explain the data split strategy and provide evidence (e.g., image similarity checks, source verification) to ensure that the benchmark is completely disjoint from the training data?

3. Given that models like Q-Instruct already possess strong IQA capabilities, wouldn't it be more efficient to enhance their grounding abilities rather than training a new model from scratch? Can the authors justify this design choice and discuss whether a fine-tuning or adapter-based approach on existing IQA-capable MLLMs might achieve comparable or better results with fewer resources?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes a new IQA paradigm named Grounding-IQA. By combining multimodal referring/grounding with IQA, the framework achieves more fine-grained image quality evaluation. The authors design two tasks, GIQA-DES and GIQA-VQA, and construct an automated annotation pipeline to build a dataset named GIQA-160K. The authors also propose GIQA-Bench for performance evaluation. Both quantitative and qualitative results demonstrate the effectiveness of the proposed Grounding-IQA.

### Strengths
1. Introducing multimodal grounding into IQA is a reasonable idea that aligns with human assessment logic. It also improves interpretability. 
2. The dataset GIQA-160K and the benchmark GIQA-Bench are well-designed contributions to the community. The automated pipeline is well-structured, which supports further research.
3. Both quantitative and qualitative results validate the effectiveness of the proposed Grounding-IQA. Comparisons with various MLLMs (general, grounding, IQA) further confirm its advantages.
4. Additional experiments in the supplementary material, including traditional score-based IQA tasks, user studies, and downstream tasks, provide further evidence of effectiveness.
5. Ablation studies and visualizations support the validity of the designed pipeline and dataset.
6. The paper is well written, with extensive figures, tables, and pseudocode that facilitate understanding.
7. The supplementary material includes detailed implementation information, visualizations, and analytical results, making the content comprehensive.

### Weaknesses
1. Although implementation details of the pipeline are provided, some settings lack explanation or analysis. For example, why the discrete coordinates are set to 20×20, and why the number of tasks differs in GIQA-Bench?
2. The work applies Llama-3 for evaluation. Considering the existence of more advanced models such as Llama-4, using them could provide more accurate evaluation results.
3. The impact of dataset scale on performance is not investigated. It is not certain whether 160K data is necessary.

### Questions
1. Explain the considerations of specific parameter settings in the pipeline.
2. Evaluate LLM-Score and Acc (W) using Llama-4 and analyze the results.
3. Conduct ablation studies on the dataset (GIQA-160K) size.

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
5

---

## Human Reviewer 3

### Summary
The paper proposes Grounding-IQA, a new paradigm for Image Quality Assessment (IQA) that couples spatial grounding with quality reasoning so models can locate and describe the local regions responsible for perceived degradations. It introduces two tasks: GIQA-DES (quality description with precise locations) and GIQA-VQA (region-aware quality QA where questions/answers include coordinates). To train and evaluate, the authors build GIQA-160K via an automatic pipeline and a 100-image evaluation set GIQA-Bench that scores description quality, VQA accuracy, and localization. Fine-tuning several mainstream MLLMs on GIQA-160K yields consistent gains on GIQA-Bench over generic MLLMs, pure grounding models, and pure IQA models, indicating better fine-grained perceptual quality understanding.

### Strengths
1. The paper integrates grounding with IQA to localize the regions causing quality defects—making it highly actionable for editing and restoration.
2. Its end-to-end labeling/training pipeline—detection, IQA filtering, box merging, and coordinate–text fusion—is scalable and reproducible.
3. A large training corpus and a targeted benchmark with multi-faceted metrics (generation, QA, localization) enable comprehensive evaluation.
4. Consistent gains across multiple MLLM backbones, with ablations indicating the effectiveness of multi-task training and box-handling strategies.

### Weaknesses
1. Fix typographical errors in the references.
2. Some novel IQA methods like (VisualQuality-R1) should be included.
3. Conduct user studies to evaluate how well the output descriptions align with the corresponding images.

### Questions
See weakness.

### Soundness
4

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
5

---

## Human Reviewer 4

### Summary
The paper introduces Grounding-IQA, a novel Image Quality Assessment (IQA) approach tailored for multimodal large model learning (MLLM). The framework decomposes IQA into two subtasks: (1) GIQA-DES, which performs fine-grained, subject-level quality evaluation via grounding-based descriptions, and (2) GIQA-VQA, which assesses low-level attributes at localized regions using a visual question answering paradigm. The authors further present GIQA-160K, a large-scale dataset constructed with an automated annotation pipeline, and GIQA-Bench, an evaluation benchmark that jointly measures description quality, VQA accuracy, and grounding precision.

### Strengths
The manuscript is clearly organized, with a strong logical flow and well-designed figures and tables that effectively illustrate the framework and experimental setup. The writing quality is generally high, facilitating easy comprehension of complex ideas. Furthermore, the benchmark construction is comprehensive and well-motivated — evaluating models from multiple dimensions (descriptive, interrogative, and spatial grounding) offers a holistic view of multimodal IQA performance.

### Weaknesses
While the contribution of a large-scale dataset and benchmark is substantial, the main novelty resides primarily in dataset creation and annotation procedures rather than in methodological innovation. The proposed framework mainly adapts existing MLLM capabilities and fine-tuning strategies to the IQA domain. As such, the work may align more closely with a dataset or benchmark track rather than the ICLR main track, where new learning methodologies or theoretical insights are typically emphasized.
Additionally, there are a few minor grammatical issues throughout the text—for example, “provide” should be “provides” (line 53), and “new coordinates is” should be “new coordinates are” (line 268).

### Questions
1.Dataset Construction Details：The paper mentions that GIQA-160K was built through an “automated annotation pipeline.” Could the authors elaborate on how annotation quality and consistency were ensured? Was there any human verification or filtering process?How are noisy or ambiguous quality descriptions handled? Are there examples of failure cases in the annotation process?
2.Whether human evaluation was included to validate these metrics.Without this information, it’s difficult to judge how faithfully GIQA-Bench reflects perceptual IQA quality.
The framework decomposes into GIQA-DES and GIQA-VQA. How much does each component individually contribute to overall IQA performance? An ablation study showing the relative importance of each subtask (and their potential synergy) would clarify whether the decomposition is truly beneficial or merely conceptual.
4.It would be constructive if the authors could discuss potential limitations — for instance, the reliance on large-scale multimodal models that are computationally expensive to train and deploy, or the dataset’s possible bias toward certain types of degradation. A discussion on how future work might reduce these dependencies or enhance scalability would improve the paper’s outlook.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3