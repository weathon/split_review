# Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities across multimodal tasks such as visual perception and reasoning, leading to good performance on various multimodal evaluation benchmarks. However, these benchmarks keep a static nature and overlap with the pre-training data, resulting in fixed complexity constraints and data contamination issues. This raises the concern regarding the validity of the evaluation. To address these two challenges, we introduce a dynamic multimodal evaluation protocol called Vision-Language Bootstrapping (VLB). VLB provides a robust and comprehensive assessment for LVLMs with reduced data contamination and flexible complexity. To this end, VLB dynamically generates new visual question-answering samples through a multimodal bootstrapping module that modifies both images and language, while ensuring that newly generated samples remain consistent with the original ones by a judge module. By composing various bootstrapping strategies, VLB offers dynamic variants of existing benchmarks with diverse complexities, enabling the evaluation to co-evolve with the ever-evolving capabilities of LVLMs. Extensive experimental results across multiple benchmarks, including SEEDBench, MMBench, and MME, show that VLB significantly reduces data contamination and exposes performance limitations of LVLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper seeks to change the static nature and data contamination of benchmarks for vision-language models.  The paper introduces VLB: vision-langauge bootstrapping that dynamically generates new visual question answering samples via bootstrapping.  The goal is for the evaluation protocol to evolve with VLM capabilities.  The paper finds that existing VLMs struggle on the new benchmark.

### Strengths
1. The paper identifies an important research direction: existing benchmarks are static and because of large-scale pretraining data, it is hard to verify is some test data has leaked into the pretraining or training data. This makes evaluation difficult and the paper seeks to develop a new paradigm for evaluation.
2. The idea of using insights from user interactions to inform the transformations V and L is interesting.  
3. The experiments are comprehensive.

### Weaknesses
1. The role of user interaction is not defined in detail.  See Q1.
2. Question rephrasing has been previously explored in several other works on VQA (eg. VQA Rephrasings dataset) or robustness work such as VQA-LOL, VQA-Subquestions and others. What is the overlap of the proposed work with those benchmarks?
3. The work focuses only on VQA but there are several tasks that VLMs can perform.  Can the framework also handle capabilities that have to be evaluated without VQA?

### Questions
1. For example in figure 3(a), how is the visual attention and linguistic understanding converted into V1, V2, L1, L2 etc.?
2. How is it verified that the generated questions are not found in the pretraining data? Does using the VLB method ensure that? This is not discussed in the analysis.

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
4

### Summary
This work proposes a new evaluation protocol, Vision-Language Bootstrapping (VLB), for comprehensively evaluating large vision-language models (LVLMs) with reduced data contamination and dynamic difficulty. Existing benchmarks like MM-Bench are constructed from fixed image-question pairs, which are partially observed in the training procedure of LVLMs. In VLB, both the image and the question can be modified to change the difficulty and avoid answering by memorization, while preserving the consistency with the original answer. Different operations in changing the image or question result in a series of difficulty levels. Extensive experiments are conducted to show performance change with VLB, through which the work poses new challenges for LVLMs.

### Strengths
1. Thorough experiment results validate the dynamic evaluation protocol VLB. First, a judge model is introduced to ensure that the dynamic image-question pair is still consistent with the original answer. Second, human examination on 2,100 samples verifies that less than 5% samples would introduce inconsistency.

2. The composition of multiple strategies effectively reduces data contamination and enables a wide range of difficulty levels. VLB can serve as a more reliable evaluation protocol than the traditional static ones.

3. The new evaluation protocol can be readily combined with existing LVLM benchmarks.

### Weaknesses
1. The major concern lies in the performance variance. Even with the same image-question sample and the same bootstrapping strategy, different dynamic samples can be generated, due to the randomness in GPT-4V and PowerPaint. However, the experiments do not show the scale of this variance caused by randomness. If this variance is large, the performance metrics may be less reliable. It is crucial to quantify the standard deviation of the performance metrics across multiple runs with different random seeds for each bootstrapping strategy to assess the robustness of the evaluation protocol. Without this analysis, it's difficult to determine if the observed performance differences are statistically significant or simply due to random variations in the generated samples.

2. Although the human verification (Figure 11) shows high consistency for each bootstrapping strategy, it is unclear if the consistency remains with composition of multiple strategies (e.g., V1+V3+L4). The errors may accumulate, and more changes to the image-question pair tend to break the original consistency. The consistency verification should be extended to combinations of strategies, not just individual ones. The potential for error propagation when combining multiple transformations needs to be explicitly addressed, as this could undermine the validity of the evaluation when using composite strategies. A detailed analysis of the consistency rate for combined strategies is necessary to ensure the reliability of the proposed evaluation method.

3. The bootstrapping strategies rely on GPT-4V and PowerPaint. If they are replaced/combined with models with similar functions, can similar observations remain? The dependence on specific models like GPT-4V and PowerPaint raises questions about the generalizability of the findings. It is important to investigate whether the observed performance trends are consistent when using alternative models for image and text manipulation. This would help establish the robustness of the proposed evaluation protocol and its applicability across different tool models. The study should include experiments with different models to assess the sensitivity of the results to the choice of these tools.

4. Some minor suggestions that do not affect the rating:
    - The bootstrapping strategies may be reordered to reflect the difficulty level. For example, how about making "removing existing objects" V1 and "adding new objects" V3?
    - In Figure 3(c), L3 should be "add relevant context."

### Questions
Please check the weakness section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work introduces VLB, a benchmark generation strategy aiming to prevent the baseline models from being evaluated on contaminated data (data leakage in essence). VLB extends current LVLM benchmarks by employing bootstrapping strategies to create altered test cases in variable difficulties in a controllable manner. The experimental results using VLB-modified benchmarks show that data leakage is evidently prominent in existing practices, and VLB may help establish fairer baselines for LVLM evaluations.

### Strengths
The paper is a pleasant read and is easy to follow. The paper is written in a well structured way following a clear plot line. I particularly find the parts where the bootstrapping strategies are introduced well written, which greatly helps me understand this work on an intuitive level.

### Weaknesses
I do have one particular concern regarding the veracity of the VLB-modified data.

VLB strategies such as V1 (editing in a new object in the image) and L4 (adding irrelevant context in to the text) modify the original test case in a controlled manner. **However, how do we verify if the original test cases have been loyally modified in the way we want?** So far, such veracity verification steps are only observed in Figure 11 using human verification on a small batch of sampled data. The authors should consider additional automated verification techniques, such as the shift in semantic scores/image-text alignment metrics before vs after applying VLB strategies. 

After all, we do not want to re-evaluate LVLMs on wrongly generated test cases, which undermine the entire effort of VLB to start with.

### Questions
Here I also list down a few minor suggestions.

1. The naming order of the VLB strategies could be changed so that the easy ones be introduced first. For example, it would feels more natural to first introduce L3, so that readers can more easily tell that, from Table 2, L3 is the positive alternative with additional helpful cues and lead to mostly improvement performance. The same idea applies for V2 as in Table 1.
2. The term 'data contamination' is not a coined term. I sense the authors want to describe the phenomenon that pre-training data already entail the contents for the supposedly unknown test set cases. In fact, this already has had a name **data leakage** as in (Chen et al, 2024). Let's stick with the established terminology. But feel free to correct me if the authors believe the two have any nuanced difference.

Typo: Table reference missing at Line 707.

Update 11/23: Raising my assessment according to the authors' response.

After all, I find this work very intriguing although the contribution feels a bit lackluster. However, I am open for reassessment after learning more from the exchange with the authors in the rebuttal period.

Chen et al, 2024. Are We on the Right Way for Evaluating Large Vision-Language Models?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a dynamic multimodal evaluation strategy to avoid data contamination for benchmarks. It shows that current popular evaluation benchmarks exist image-only contamination and image-text contamination. Image bootstrapping and language bootstrapping method can be used separately or in combination to adjust the difficulty of the questions while keeping the answers unchanged. Several experiments on 3 benchmarks and 8 VLMs are provided to verify the author's point of view.

### Strengths
1. The paper proposes a novel dynamic multimodal evaluation framework VLB, which has a a flexible complexity adjustment evaluation mechanism.
2. By editing images and modifying questions, a set of evaluation samples with different levels of complexity can be generated. This method can be used to probe the upper and lower bounds of VLMs' capabilities in certain tasks.
3. The VLB framework is highly versatile. It can be easily plugged in a lot of benchmarks.

### Weaknesses
1. Authors use many models, such as GPT-4V, PowerPaint, SAM, to insert and remove objects from original images and employ GPT-4 for language reconstruction. Each step requires consistency evaluation, which may increase the complexity of implementation and lead to more unexpected errors or inconsistencies. The reliance on multiple external models introduces potential points of failure and makes the framework harder to reproduce and maintain. The specific prompts used for these models are also a concern, as subtle variations can lead to significant differences in the generated data.
2. Generating new visual and language samples takes a long time, especially during large-scale evaluations. It also requires significant computational resources to produce new samples. The authors do not provide concrete numbers on the time and resources required for their approach, making it difficult to assess the practical feasibility of their method.
3. The VLB framework relies on PowerPaint, SAM and GPT-4V to generate new visual and language samples. The performance of the framework is therefore limited by the capabilities of these models and any biases they may have. The authors do not discuss the potential impact of these limitations on the overall evaluation results.
4. Although DME can generate diverse samples, the performance of VLMs may decrease on these samples, and the specific reasons for this are not clear. The authors do not provide a detailed analysis of why the performance of VLMs decreases on the dynamically generated samples. It is unclear whether the performance decrease is due to the increased difficulty of the samples or some other factors.
5. Lack visualization for error analyses. The authors do not provide sufficient visualization to understand the types of errors made by the models on the dynamically generated samples. This makes it difficult to gain insights into the strengths and weaknesses of the models.

### Questions
1. In practice, how can you ensure that when generating a lot of new samples, changes in images and questions do not introduce unnecessary bias or semantic errors?
2. Are there any automated validation methods that can guarantee semantic consistency across all generated samples?
3. When the external tools, such as PowerPaint, SAM and GPT-4V, being relied upon have limitations, for example, sometimes there will be some artifacts after using PowerPaint to remove an object, how does the DME ensure the fairness and accuracy of the evaluation?
4. How to improve the interpretability of evaluation results?
5. How to assist researchers in better understanding the specific areas where the model underperforms?
6. Can you provide the specific VLMs mentioned in Table 1? For example, InternVL2-1B or InternVL2-2B or … InternVL2-76B.
7. In Figure 4 “image outpainting” part, the proportion of the floor in the image V3 is larger than in the Vanilla image, and the question is “What type of flooring does the kitchen have?”, so in this situation, can “image outpainting” be defined as a hard task?
8. Have you resized the image when using PowerPaint and GPT-4V?

### Soundness
3

### Presentation
1

### Contribution
3
