# Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Current multimodal large language models (MLLMs) often underperform on mathematical problem-solving tasks that require fine-grained visual understanding. The limitation primarily arises from inadequate perception of geometric primitives during image-level contrastive pre-training (e.g., CLIP). Current efforts to enhance MLLM performance have focused on scaling up mathematical visual instruction datasets and employing stronger LLM backbones, yet these approaches often neglect persistent visual recognition errors in MLLMs. In this paper, we systematically evaluate the visual grounding capabilities of state-of-the-art MLLMs and uncover a negative correlation between their visual grounding accuracy and problem-solving performance. Notably, even advanced models like GPT-4o demonstrate a significant error rate (70\%) when identifying geometric entities, highlighting that fine-grained visual understanding remains a crucial bottleneck in visual mathematical reasoning. To address this, we propose a novel approach, SVE-Math (Selective Vision-Enhanced Mathematical MLLM), featuring a geometric-grounded vision encoder and a feature router that dynamically adjusts the contribution of hierarchical visual feature maps. Our model recognizes accurate visual primitives and generates precise visual prompts tailored to the language model's reasoning needs. In experiments, SVE-Math-Deepseek-7B outperforms other 7B models by 7.7\% on MathVerse and is compatible with GPT-4V on MathVista. Despite being trained on smaller datasets, SVE-Math-7B matches the performance of models trained on significantly larger datasets, evaluated on GeoQA. Our findings provide critical insights for future research, highlighting the need for more effective integration of fine-grained visual understanding in MLLMs.  We will release model weights, code, and instructions upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper first identifies visual recognition errors prevalent of current MLLMs by a pilot study. Then the paper introduces GeoGLIP, a vision encoder specifically trained to identify geometric elements in the image. The feature from the trained geometric vision encoder is later merged with the feature of the original CLIP vision encoder, aiming at more precise geometry perception. The authors prove the effectiveness of their method by evaluating on various benchmarks.

### Strengths
+ The paper proposes a novel perspective that the errors of visual mathematical problems come from poor visual perception.
+ The three training tasks of GeoGLIP closely matches the analysis in Fig. 1. The paper is self-contained and well-written.

### Weaknesses
 + The major concern is whether addressing the visual perception error is sufficient for the mllm to correctly solve these tasks. The visual mathematical questions also require advanced reasoning capability, especially merging both the visual and textual information. Only correctly identifying the graph seems to be far enough to solve a mathematical problem. Detecting the texts, shapes or curves in the graph does not necessarily suggest the model understands the element. How much GeoGLIP actually helps in understanding and reasoning seems marginal. The pilot study shown in Fig. 1 also only analyze the error of visual descriptions, while neglecting other potential core problems of MLLM for visual mathematical questions.
+ The effectiveness of the proposed GeoGLIP is not validated. The authors need to report the performance of the model trained with same instruction data only without the GeoGLIP encoder to illustrate the improvement brought by it. Otherwise, the improvement may be from the Geo170K data.
+ The overall performance advantages of SVE-Math compared to previous works are not very obvious.

### Questions
+ How much more computational cost and inference time is introduced by GeoGLIP?

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
To address the limitations of multimodal large language models (MLLMs) in solving math problems involving images, this paper proposes a Selective Vision-Enhanced Mathematical MLLM. It leverages a geometric-grounded vision encoder and a feature router to help MLLMs better comprehend mathematical image features, thereby improving their performance on math problems with visual components.

### Strengths
1. The paper clearly articulates the problem it aims to address, and the overall writing is easy to follow.

2. The paper enhances MLLM's ability to recognize mathematical images and solve math problems by introducing geometry-rich visual information, achieving improvements on several benchmarks.

### Weaknesses
1. Using more detailed visual features for solving math problems is an intuitive idea, as is combining geometric and semantic features at different levels. However, you should conduct additional ablation studies to validate the effectiveness of this approach. For instance, consider using vision encoders from other similar models on your dataset/training your model on the training data of other models.

2. In Table 1, some experimental results differ from those provided in the official MathVerse table. For example, you show the cot-e score for SPHINX-Plus and the w/o score for SPHINX-MOE. When comparing with other models on the same benchmark, you should ensure thorough variable control.

3. You mention using synthetic data, but the paper does not include any description, details, or examples of the synthetic data generation process.

4. The paper does not present any output examples from the model.

5. As a “data collection-model training-benchmark testing” type of paper, the performance improvements on benchmarks are minimal in the absence of novelty.

### Questions
1. In terms of writing, the paper’s section distribution could be improved. You should allocate some space to introduce synthetic data, dedicate more space to ablation studies to validate the method's effectiveness, and reduce the length of the Methods section.

2. Please provide more details and examples of the synthetic data.

3. Please provide examples of the model’s outputs to demonstrate its ability to recognize geometric elements and Chain-of-Thought (CoT), as you compared cot-e performance with some models in Table 1.

4. In the Introduction, you mentioned a finding: instructing MLLMs with fine-grained visual information improves top-1 accuracy compared to providing only worded questions, while providing all visual cues for solving a math question decreases accuracy. How does your approach—primarily by introducing more geometry-rich visual information—address the issue highlighted by this finding?

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
4

### Summary
This paper introduces SVE-Math, a Multimodal Large Language Model (MLLM) designed for mathematical question answering. It incorporates a GeoGLIP module to enhance the visual encoder's perception of mathematical elements and utilizes a routing module to prioritize features from CLIP. The training process for SVE-Math consists of three stages: GeoGLIP training, cross-modal alignment, and instruction tuning.

### Strengths
1.The approach of enhancing the visual encoder for improved mathematical performance is both innovative and logical.

2.The routing module is well-designed and demonstrates significant performance improvements in the ablation studies. However, I believe that the routing module is not specifically designed for mathematical reasoning tasks and can be applied to a wider range of scenarios.

3.The paper is well-structured and easy to understand.

### Weaknesses
1.My main concern is the performance results, which are not particularly impressive. While SVE-Math achieves competitive scores on several benchmarks, the improvements over the previous works are marginal, raising questions about the effectiveness of the approach.

2.Building on the first point, I believe a significant portion of the performance improvement in MLLMs stems from the data used. The scale and quality of training data are critical for MLLMs. Could you elaborate on any unique handling or augmentation techniques applied to the training data? 

3.Could the authors provide more explanation of why the routing module is specifically designed for mathematical reasoning tasks? Relying solely on empirical evidence is not sufficient to substantiate this claim.

### Questions
Please refer to weakness. Can the proposed methods be applied to other mathematical problems beyond geometric figures and problems?

### Soundness
2

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
5

### Summary
The paper proposes the SVE-Math-7B model to improve the math reasoning skills of current MLLMs. The authors start by analyzing the performance on mainstream models' math reasoning tasks to show the geometric information's effectiveness. Based on the observation, the author proposes the architecture of SVE-Math with a pre-trained GeoGLIP, a fusing connector with dual visual encoders, and further fine-tuning the baseline models. The authors conduct experiments on mainstream math-relative benchmarks such as MathVerse and MathVista and show improvements compared with baselines.

### Strengths
1. The paper discovers and discusses the math-solving problem of MLLMs, which is a significant and widely-concerned problem for current MLLMs. The solution with GeoGIP and math-relevant fine-tuning is efficient for the problem.
2. The analysis in Figure 1 clearly shows the drawbacks of LLaVA and GPT-4o, and shows the effectiveness of geometric information. 
3. The methods and experiment periods are well organized and easy to follow. The authors conduct experiments on mainstream math datasets and clearly show the results.

### Weaknesses
1. The main weakness is that the ablation analysis is not sufficient to demonstrate the improvements of all the components. The author proposes the GeoGLIP, dual visual encoder connector, math-specific finetuning with Geo170K, MathV360K datasets. However, the analysis of such aspects is lacking. The authors only conduct experiments on the design of connectors, which is not the key claim for the contributions, as many papers have used similar fusing approaches for visual encoders. I think the authors could clearly explain where the improvements come from, especially for the GeoGLIP and the math-relevant training datasets. Specifically, the contribution of the GeoGLIP, a lightweight visual encoder, is not well-supported by ablation studies. The authors should provide more direct comparisons, such as using a standard visual encoder with similar parameter size or directly providing geometric information as input, to isolate the effects of the proposed GeoGLIP architecture and its pre-training. The impact of the math-specific datasets, Geo170K and MathV360K, on the overall performance is also not clearly demonstrated. It is unclear whether the improvements are due to the enhanced visual perception from GeoGLIP or the math-specific fine-tuning datasets. 
2. Although the authors show improvements over baselines, the performance for SVE-Math-7B is significantly behind the state-of-the-art models (e.g. more than 60 accuracy on MathVista). I assume the approach proposed by the author is universal, therefore the results of state-of-the-art models are lacking. The paper should include a more comprehensive comparison with state-of-the-art models, particularly those achieving higher accuracy on benchmarks like MathVista. This comparison should not only focus on accuracy but also consider the model size and computational resources required. The current results do not clearly position the proposed method relative to the best-performing models in the field. 
3. The effectiveness of GeoGLIP is not confirmed. I wonder how the tiny visual encoder with less than 50M parameters can help the overall learning results. As shown in the visualization results, directly providing geometric-relevant information in a proper manner may also lead to similar performance. The authors could conduct sufficient experiments to explain this issue. The paper lacks a detailed analysis of how GeoGLIP's specific architecture and pre-training contribute to the observed improvements. It is not clear if the performance gains are due to the geometric information captured by GeoGLIP or simply due to the increased model capacity. The authors should provide a more thorough investigation into the inner workings of GeoGLIP and its impact on the overall model performance.

### Questions
As stated in the weakness periods, clarifying the issues can better demonstrate the conclusion of the paper. 
1. What are the improvements with math-specific datasets? 
2. Why using GeoGLIP based on Swin-T is effective for results? As illustrated in the visualization results, the usage of the models provides geometric information, so the authors may provide more comparisons by providing direct geometric results, or directly using GLIP. 
3. The results for current models are somehow out-of-date. The authors are encouraged to equip proposed approaches on state-of-the-art level MLLMs. 
4. The math problems may already be solved with better data curation or reasoning processes, as many papers have done on such problems. The author could provide explanations and superiority for the proposed methods and provide comparisons with other methods on math problems.
Therefore, based on the weaknesses and questions stated above, I think the paper is below the acceptance threshold in the current situation.

### Soundness
3

### Presentation
4

### Contribution
2
