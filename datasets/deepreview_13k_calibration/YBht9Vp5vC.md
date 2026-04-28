# UrbanMLLM: Joint Learning of Cross-view Imagery for Urban Understanding

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 6, 5, 6

## Abstract
Multimodal large language models (MLLMs) have exhibited remarkable capabilities for performing complex vision-language tasks in various domains.
Currently, MLLMs based on urban imagery in urban studies are only developed focusing on remote sensing imagery.
However, except for the macroscopic information from remote sensing imagery, effective urban understanding also requires detailed appearance information of urban zones from street-view imagery, which is largely overlooked by existing MLLMs.
The primary challenges of developing such a versatile urban MLLM are twofold. 
Firstly, it needs a large-scale corpus with well-organized, cross-view urban imagery paired with corresponding text for cross-modal training.
Secondly, traditional MLLMs typically learn image-text pairs independently, hard to support joint modeling of cross-view urban imagery.
To address these challenges, in this work, we propose UrbanMLLM, a novel MLLM that jointly learns from remote sensing and street-view imagery to harness their complementary information.
We first collect a large-scale dataset containing satellite-view and street-view imagery along with their geotags and annotated texts.
Technically, we propose a brand MLLM architecture with a cross-view perceiver to explicitly connect visual information of cross-view urban imagery.
We also introduce a novel pre-training paradigm based on structural interleaved urban image-text documents integrating satellite-view, street-view imagery and related textual descriptions.
This approach encourages the model to implicitly learn the relationships between different types of urban imagery, enhancing the understanding in each domain.
We evaluate our model on a comprehensive benchmark comprising 13 diverse urban understanding tasks across satellite-view, street-view, and cross-view domains. These tasks include scene classification, object reasoning, spatial relationship reasoning, geo-localization, landmark reasoning, and indicator prediction, providing a robust assessment of the model's capabilities.
Extensive experiments demonstrate that UrbanMLLM achieves an average of 27.3\% and 25.5\% performance improvement compared with the best open-sourced and closed-sourced MLLMs, respectively.
Moreover, we thoroughly study the impact of different pre-training data choices and model scales on performance, offering practical insights for effective MLLM design.  The proposed UrbanMLLM offers a scalable and versatile solution for understanding urban environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors created a multimedia LLM (MLLM) with the purpose of solving urban
understanding tasks. Specifically, the authors trained their UrbanMLLM model
with satellite and street-view images, in addition to text. The UrbanMLLM
includes a cross-view perceiver module to integrate satellite and cross-view
images. A pre-training method is used to then integrate the text.

### Strengths
S1: The authors collected a dataset that includes both satellite and cross-view
images. Though, not much details are presented about this dataset.

S2: The UrbanMLLM model performs well against general MLLM models.

S3: The authors tested a large variety of urban understanding tasks.

### Weaknesses
W1: Other than stating that 2 million satellite and cross-view images were
used, not much information is presented about the dataset. For example, where 
did the ground truth information to calculate accuracy come from? Also, the
authors state that the dataset covers the whole of the US. I am sure that,
just for street-view images, there are more than 2 million in the US. How
did the authors select the used images and how uniform or concentrated did
they select images for certain cities?

W2: The utilized perceiver module in the UrbanMLLM is a previously proposed 
component by DeepMind, hence the novelty of the architecture seems a bit 
limited.

W3: It seems the performance of UrbanMLLM was compared against general MLLMs
which were not trained on the same dataset. Since only UrbanMLLM was trained on
both the satellite and cross-view images from the authors dataset it is not 
very surprising that UrbanLLM's performance is overall better. Thus, the 
comparison in this paper does not seem to be quite apples-to-apples.

### Questions
Please see my comments under Weaknesses. I would be interested in the authors'
explanations on the issues that I listed there.

Page 1:
In the abstract and introduction, I think it would be good if the authors
could be a bit more specific about what kind of applications their UrbanMLLM
is supposed to support. There are many urban applications and clearly UrbanMLLM
is only suitable and targeted towards a subset of them.

Page 2:
The authors state that the dataset covers the whole United States. They also
mention that 2 million images where used. I would assume that coverage of the
whole US would require more images. So this dataset must be very sparse. How
did the authors decide which images to select?

Page 2:
For some urban computing tasks there exist specialized architectures, e.g.,
for cross-view localization. The authors may want to refer to some of the
work, and also make it clear that they have a more general model in mind.

Page 5:
"imapact" -> impact

Page 7:
"The results showcase that UrbanMLLM achieves state-of-the-art performance,
which successfully ."
There is some text missing here at the end of this sentence.

### Soundness
2

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
5

### Summary
This paper proposes an urban research MLLM, called UrbanMLLM, which links visual information from cross-view urban images through a cross-attention mechanism and introduces a structured interleaved urban image-text pre-training framework. Meanwhile, the authors collect a large dataset of satellite view and street view images along with their geo-tagged and annotated texts to fill the lack of urban MLLM regarding street view-related data.

### Strengths
1. Collect and construct a dataset of satellite and street view images and their geo-tagged and annotated text, providing data support for subsequent research in the field.

2. Provides a framework for interacting with multi-view information, which to some extent alleviates the current problem of poor performance of Street View in the MLLM domain of urban research.

3. Although there are some problems in the experimental setup, after the adoption of the new dataset, a more obvious improvement in performance level has been achieved.

### Weaknesses
1. The data obtained by MLLM is inherently noisy and limited, and introducing it for training without special processing can result in models with a significant upper bound.

2. There does not seem to be a straightforward relationship between the direct information interaction of the perspective images and the performance of the larger model (e.g., Figure 13), and many MLLMs can produce correct answers without this mechanism. This may be because UrbanMLLM only focuses on the relationship between different perspective images of the same area and ignores the connection between the corresponding captions.

3. During the experiments, only UrbanMLLM was trained on the dataset collected by the authors, which is extremely unfair, and it is difficult to judge whether the difference in performance between different MLLMs is due to missing data or structural problems, or whether it is a problem with the pre-training process.

4. The results of LHRS-Bot and SkysenseGPT are not shown in Table II and in Table III. What is the reason for this?

5. Although the authors have validated the effectiveness of the proposed dataset to some extent, the validation set in the experiments has labels, which are captions generated by MLLM. How can the accuracy of the benchmark be guaranteed?

6. The performance of the proposed dataset under other model architectures needs to be verified, and also how the dataset performs under other benchmarks after pre-training needs to be given.

7. What is the reason for the fact that in Table 7, none of the components of UrbanMLLM-8B have a significant impact on the performance, and there is even a large gap for certain tasks?

### Questions
1. The results of LHRS-Bot and SkysenseGPT are not shown in Table II and in Table III. What is the reason for this?

2. Although the authors have validated the effectiveness of the proposed dataset to some extent, the validation set in the experiments has labels, which are captions generated by MLLM. How can the accuracy of the benchmark be guaranteed?

3. The performance of the proposed dataset under other model architectures needs to be verified, and also how the dataset performs under other benchmarks after pre-training needs to be given.

4. What is the reason for the fact that in Table 7, none of the components of UrbanMLLM-8B have a significant impact on the performance, and there is even a large gap for certain tasks?

### Soundness
2

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
This paper introduces UrbanMLLM, a new MLLM dedicated to urban understanding. Unlike previous works that primarily rely on remote sensing imagery alone, this approach integrates cross-view imagery through a proposed cross-view perceiver and a new pre-training paradigm. To effectively evaluate UrbanMLLM, this work also constructed the UrbanView benchmark, demonstrating notable improvements in urban understanding over both open-source and proprietary MLLMs.

### Strengths
1. Most designs appear technically correct with the paper being clear and practical to follow.

2. This work is well-organized, clearly outlining the need for enhanced urban understanding by incorporating street-view imagery with remote sensing imagery in the MLLM framework.

3. The proposed UrbanView benchmark is comprehensive, and the experimental results are promising, laying a solid foundation for future research in this domain.

### Weaknesses
Motivation：
The paper emphasizes that prior works have largely overlooked street-view images; however, this argument alone does not fully justify the motivation, especially as prior works are limited in number, and UrbanVLP has already explored this area to some extent. Furthermore, the three tasks—perception, reasoning, and prediction—do not seem to introduce substantial innovation or expansion. The tasks, while relevant, lack a clear demonstration of novel task formulation or a significant expansion of existing task definitions within the urban understanding domain. The paper needs to better articulate the specific challenges that these tasks address and why they require a new MLLM approach rather than adapting existing methods.

Lake of Detail：
1. While the appendix includes high-quality visualizations of the dataset, more details are needed for a new benchmark, particularly on data refinement, which is crucial. The data refinement process is not adequately described, leaving uncertainty about the quality control measures taken to ensure the reliability of the benchmark. Details on how noisy or ambiguous data points were handled, and the criteria used for data cleaning, are missing.

2. The paper does not discuss limitations or future work. Additionally, no accompanying code is provided to support its methodology and results. The lack of a limitations section makes it difficult to assess the scope and applicability of the proposed method. The absence of code hinders reproducibility and further research based on this work.

3. For a work targeting urban understanding, providing information on data collection, refinement, and model training time would be highly beneficial. The paper lacks specifics on the data collection process, such as the geographic distribution of the data, the temporal range of the imagery, and any potential biases introduced during data acquisition. Details on the computational resources required for model training, including the hardware used and the training time, are also missing.

Evaluation：
The paper introduces a new benchmark to comprehensively assess urban understanding capabilities. However, it lacks results on previous benchmarks, which, if included, would further validate the advantages of the proposed approach. The absence of comparative results on established benchmarks makes it difficult to assess the relative performance of the proposed model and benchmark against existing methods and datasets.

### Questions
Please refer to the Weaknesses. I'm willing to raise my score if my concerns are well addressed.

### Soundness
3

### Presentation
3

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
The paper introduces a novel multimodal large language model (MLLM) designed to integrate remote sensing and street-view imagery for a more comprehensive understanding of urban environments. The authors address the limitations of existing MLLMs that focus solely on remote sensing imagery. The key contributions include the development of a cross-view perceiver module within the MLLM architecture to facilitate the fusion of visual contexts, the creation of a large-scale multimodal urban imagery dataset with geotags and annotated texts, and a new pre-training paradigm based on structurally interleaved urban image-text documents. The model, named UrbanMLLM, is evaluated on a diverse set of 13 urban understanding tasks and demonstrates significant performance improvements over both open-sourced and closed-sourced MLLMs.

### Strengths
1. Originality: The paper presents a unique approach to urban understanding by jointly learning from remote sensing and street-view imagery, which is a novel contribution to the field of MLLMs.

2. Quality: The authors have constructed a large-scale dataset and developed a model architecture that addresses a significant gap in current MLLM capabilities. The experiments are thorough and well-designed to test the model's performance across a range of urban understanding tasks.

3. Clarity: The paper is organized with clear explanations of the methodology, experiments, and results.

### Weaknesses
1. Architecture-wise, I think the cross-attention mechanism in the cross-view perceiver is not a novel part. Hence, mode-side novelty is limited, although the interleaved image-text dataset is beneficial for the MLLM community.

2. In the evaluation, the baselines you chose are MLLMs, but it could be more comprehensive to compare yours with CLIP-based models.

3. You used InternVL2-40B to generate the captions for the UrbanView dataset. The dataset quality, especially the text quality, has not been verified/evaluated yet.

4. The statement from your abstract "MLLMs in urban studies are only developed focusing on remote sensing imagery" may be incorrect, unless you illustrate the comparison of the pertaining corpus proportion of different MLLMs.

5. Lack of bad case analysis.

### Questions
1. I think you mentioned the UrbanVLP using satellite and street-view images in Table 1, so I wonder if it is possible that the CLIP-based pertaining model can outperform the MLLM-based pertaining model. 

2. Is the vision encoder the same for both satellite and street-view images?

3. It is recommended to validate/evaluate the quality of text parts from the UrbanView dataset. Or how do you refine the text?

4. You should include a bad case analysis of UrbanMLLM, so the community can know the gap of the current best model towards comprehensive urban understanding.

5. Does UrbanMLLM support multi-image as input? If so, possible to include an ablation study on the number of images?

6. It seems that the scaling law does not totally apply to UrbanMLLM across all urban tasks. We expect you to dive into the explanation of the difference among urban tasks in terms of UrbanMLLM performance.

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
4

### Summary
This paper introduces UrbanMLLM, a multimodal large language model designed to improve urban understanding by jointly leveraging satellite and street-view imagery. The authors propose a cross-view perceiver module that facilitates the integration of satellite and street-level details, addressing the limitations of relying solely on remote sensing data. In addition, the paper introduces an interleaved pre-training paradigm, where satellite and street-view images are paired with relevant textual descriptions, creating a richer context for urban understanding tasks.

The model is evaluated on a variety of tasks, including satellite image analysis, street-view analysis, and cross-view tasks, showcasing notable performance improvements over existing MLLMs. The results highlight UrbanMLLM’s ability to excel in both fine-grained perception tasks and more complex reasoning tasks, such as population density and spatial relationships. The extensive dataset and the diverse range of urban tasks provide a comprehensive testbed for the model’s capabilities. The authors also perform ablation studies to demonstrate the significance of each component, particularly the cross-view perceiver, in achieving performance gains.

Overall, the paper provides a robust framework for advancing urban understanding through multimodal fusion, and the results show clear improvements across several key metrics.

### Strengths
1. **Rich Dataset**: The paper makes use of an extensive dataset comprising over 2 million satellite and street view images, creating a large-scale cross-view interleaved pre-training dataset. This dataset greatly enhances the model's capacity for multimodal learning, allowing it to effectively capture the multi-level details of urban environments.
   
2. **Impressive Results**: UrbanMLLM demonstrates remarkable performance across several tasks, particularly in complex fine-grained tasks and reasoning tasks, such as object-level reasoning, spatial relationship reasoning, and depression rate prediction. The model significantly outperforms existing benchmarks, showing strong capabilities in urban understanding tasks.

3. **Diverse Task Coverage**: The experiments cover a wide range of tasks, including satellite imagery tasks, street view imagery tasks, and cross-view tasks. This diversity in task design validates the model's generalization and robustness, making the conclusions more compelling.

### Weaknesses
1. **Lack of Novelty**: While the paper provides a solid technical solution, it lacks innovation on the methodological front. The idea of combining satellite and street view images for urban understanding has been explored extensively in previous works. Although the cross-view perceiver module is introduced, its design is relatively simple, relying mainly on cross-attention mechanisms without deeper integration. Additionally, the interleaved data pre-training strategy is common and does not bring any groundbreaking technical advancement.

2. **Limited Model Comparisons**: The experimental section does not sufficiently compare the model with others in terms of **model size** and **training data** scale. The paper showcases UrbanMLLM's superior performance, but it remains unclear whether this improvement stems primarily from the large dataset or the model's architecture. A more in-depth discussion on these factors is necessary. Furthermore, the paper lacks comparisons with specific domain models, particularly in critical tasks such as **indicator prediction**. A comparison with models like **UrbanCLIP** and **UrbanVLP** would provide a more comprehensive evaluation of UrbanMLLM's performance in urban understanding tasks.

3. **Lack of Depth in Experimental Analysis**: While the experiments cover multiple task types, there is a lack of in-depth analysis on how the model performs across different subtasks. For example, the model excels in complex reasoning tasks like population density prediction, but it does not outperform certain closed-source models in simpler tasks like geographic location prediction. A more thorough discussion of the model's strengths and weaknesses across various tasks would add valuable insights into its overall performance.

### Questions
1. **Can you clarify how the cross-view perceiver module compares to more advanced fusion mechanisms used in similar multimodal tasks?**  
   While the cross-attention mechanism is effective, it seems like a relatively simple approach. Have you considered more sophisticated alternatives for deeper integration between satellite and street-view imagery? If so, what were the reasons for opting for the current design?

2. **What impact do the model's size and dataset scale have on the performance?**  
   It's not entirely clear whether the performance improvements are primarily driven by the large dataset and increased model parameters. Have you conducted any comparisons or ablation studies that analyze the performance of smaller models or less data? How would a smaller model perform under the same conditions?

3. **Why wasn't there a comparison with domain-specific models like UrbanCLIP or UrbanVLP in the indicator prediction task?**  
   Given the task-specific nature of indicator prediction, models like UrbanCLIP and UrbanVLP could provide a more relevant baseline. Could you provide insights into why these comparisons were not included, and how you believe UrbanMLLM would fare against such models?

4. **Can you elaborate on how the model handles simpler tasks, such as geographic location prediction?**  
   The paper mentions that the model falls slightly behind some closed-source models in certain tasks like geographic location prediction. Could you explain why this might be the case, and whether there are specific limitations in UrbanMLLM that contribute to this performance gap?

### Soundness
3

### Presentation
3

### Contribution
3
