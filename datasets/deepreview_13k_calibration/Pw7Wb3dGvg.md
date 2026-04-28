# Understanding Llava's Visual Question Answering in a Mechanistic View

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Understanding the mechanisms behind Large Language Models (LLMs) is crucial for designing improved models and strategies. While recent studies have yielded valuable insights into the mechanisms of textual LLMs, the mechanisms of Multi-modal Large Language Models (MLLMs) remain underexplored. In this paper, we apply mechanistic interpretability methods to analyze the visual question answering (VQA) mechanisms in the first MLLM, Llava. We compare the mechanisms between VQA and textual QA (TQA) in color answering tasks and find that: a) VQA exhibits a mechanism similar to the in-context learning mechanism observed in TQA; b) the visual features exhibit significant interpretability when projecting the visual embeddings into the embedding space; and c) Llava enhances the existing capabilities of the corresponding textual LLM Vicuna during visual instruction tuning. Based on these findings, we develop an interpretability tool to help users and researchers identify important visual locations for final predictions, aiding in the understanding of visual hallucination. Our method demonstrates faster and more effective results compared to existing interpretability approaches. Our code, data and interpretability tool will be made available on GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the mechanisms behind visual question answering (VQA) in Llava. The authors apply mechanistic interpretability methods to compare VQA mechanisms with textual question answering (TQA), focusing on color-related tasks. The analysis in this paper reveals that VQA mechanisms share similarities with TQA, as visual features exhibit significant interpretability when projected into the embedding space. Additionally, the authors observe that Llava enhances Vicuna's abilities during visual instruction tuning. Based on these insights, the authors propose an interpretability tool that identifies important visual regions for predictions, providing a more effective and computationally efficient explanation compared to existing methods. The proposed approach offers a valuable resource for understanding visual hallucinations in MLLMs.

### Strengths
1)	The research problem addressed in this paper is highly intriguing and contributes to a deeper understanding of the operational mechanisms of Multimodal Large Language Models (MLLMs).
2)	This paper compares the attention mechanisms of LLMs when handling VQA and TQA tasks, offering a very novel research perspective.
3)	This paper developed an interpretability tool for VQA to help identify the key image patches that influence the model's predictions.

### Weaknesses
1)	My main concern is that all the experiments in this paper are conducted on color-related questions, so the conclusions may not be applicable to all VQA examples. The paper does not provide sufficient justification for generalizing from color-based VQA to other types of visual reasoning tasks. For example, tasks involving spatial relationships, object counting, or fine-grained object recognition might rely on different mechanisms within the MLLM. The authors need to demonstrate that the observed interpretability patterns hold across a more diverse set of VQA tasks, or at least provide a strong argument for why color-based analysis is representative of broader VQA behavior.
2)	Did the authors verify the hypothesis mentioned in line 225 of section 3.2? If so, I hope they can provide this evidence in the paper.
3)	I am curious about the specific form of the probability function p in Equation 6 and 7. It is unclear how this probability is calculated, particularly in the context of inner states. Does it involve a softmax over the entire vocabulary, or is it a more localized probability calculation? The paper needs to clarify the exact mathematical operation and the inputs to the probability function.
4)	What do the green, blue, and pink colors in Figure 1 represent? I hope the authors can add a necessary legend or explanation to the figure.
5)	There are several spelling errors in the text, such as "Figure 3" in line 368, which I suspect is a typo and should actually refer to "Figure 5."

### Questions
1)	Did the authors verify the hypothesis mentioned in line 225 of section 3.2? If so, I hope they can provide this evidence in the paper.
2)	I am curious about the specific form of the probability function p in Equation 6 and 7.
3)	What do the green, blue, and pink colors in Figure 1 represent? I hope the authors can add a necessary legend or explanation to the figure.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents the analysis of the visual question answer mechanisms in Llava for color answering question tasks, by applying the mechanistic interpretability methods. Based on the analysis result, the paper also introduces an interpretability tool that identifies the image patches that explain the final prediction.

### Strengths
1. The paper analyzes the mechanisms of textual QA in Vicuna and visual QA in Llava, by utilizing the mechanistic interpretability methods. 

2. The paper presents an interpretability tool based on the above analysis to locate the important image patches for final prediction.

### Weaknesses
1. The research scope is limited. It only analyzes the textual QA in Vicuna and visual QA in Llava for the color answering question. As the QA tasks can be in a variety of forms, and there are many leading LLM and VLM models, it would be more helpful to discuss the generalization of the presented study to other QA types and models.  

2. The mechanism analysis for textual QA is based on paper [1]. The technical novelty appears limited. Specifically, the core hypothesis presented in Figure 1 (b) of this paper is highly-similar to that proposed in [1] and depicted in Figure 1 ([1]). Explaining the difference and innovation compared to the related work would help to understand the novelty of this work. 

3. The mechanism analysis for visual QA is similar to that for the textual QA, in terms of methodology and results.

### Questions
1. Understanding visual hallucination appears to be an important goal. It would be helpful to define the meaning and scope of visual hallucination that are concerned in this work, and how this study helps to address them.

2. It is claimed that the presented interpretability method is versatile and can be applied to questions beyond color identification. The appendix A does provide some examples. But it would be better to provide more explanations, for example, if the methodology for color identification problem can be directly applies or if any adaption should be made.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper aims to uncover the mechanisms behind Visual Question Answering (VQA) in Llava, a multimodal language model, by comparing it with Textual Question Answering (TQA) in Vicuna. The authors use interpretability methods to analyze how visual features influence predictions and to demonstrate a novel interpretability tool that identifies image patches critical for predictions. The paper also claims that this tool is computationally efficient, offers superior interpretability over attention-based methods, and helps understand issues like visual hallucination in multimodal models.

### Strengths
1. **Relevant Objective and Context**: The paper addresses a relevant problem in multimodal large language models (MLLMs) by focusing on the lack of interpretability in VQA tasks. This is a current and important research area with clear motivations in making MLLMs more interpretable.

2. **Insightful Mechanistic Analysis**: The authors undertake a detailed investigation into both VQA and TQA, presenting an analysis that compares attention mechanisms and embeddings in Vicuna and Llava. This comparison is informative, highlighting the potential similarities in processing mechanisms across text and visual modalities.

3. **Computational Efficiency in the Interpretability Tool**: The interpretability tool is presented as being computationally efficient, allowing for real-time or near-real-time interpretations. This efficiency could make the tool valuable for applications where rapid interpretability is essential.

### Weaknesses
1. **Lack of Innovation**: The paper lacks significant innovation, as it primarily extends existing interpretability techniques to a specific task (color-based VQA) rather than introducing fundamentally new approaches or theoretical insights into model interpretability. The application of log probability increases to identify salient image regions, while useful, is not a novel methodological contribution in itself. The core idea of using changes in output probabilities to understand model behavior has been explored in other contexts, and this work does not significantly advance the state of the art in interpretability techniques.

2. **Bad Presentation**: The presentation quality of figures is subpar. For instance, Figure 4 is poorly labeled and challenging to interpret, undermining the clarity of the findings. Additionally, the paper mistakenly claims that Figure 3 displays results across 1,024 attention heads, which is inaccurate and reflects a lack of attention to detail in presentation.

3. **Lack of Theoretical Foundation for Interpretability Claims**: The interpretability tool, while empirically tested, lacks a rigorous theoretical foundation explaining why log probability increases offer a superior interpretative value compared to attention scores. The paper does not provide a formal justification for why changes in log probabilities should be considered a more reliable indicator of feature importance than attention weights, especially given that attention mechanisms are explicitly designed to capture relationships between inputs and outputs.

4. **Limited Experimental Scope**: The paper evaluates the interpretability tool primarily on color-based VQA tasks, which do not capture the full complexity of VQA challenges. Tasks like spatial reasoning or more abstract visual concepts are not tested, making it unclear whether the tool would perform as well in these contexts. Only one model and one dataset are considered in this paper. The reliance on a single, relatively simple task limits the generalizability of the findings.

5. **Minimal Comparison with Established Interpretability Methods**: Although the paper compares its tool qualitatively against average attention-based approaches, it lacks a quantitative evaluation against other standard interpretability techniques. There is no quantitative comparison with methods such as gradient-based saliency maps or perturbation-based techniques, which are commonly used in the field. This lack of quantitative comparison makes it difficult to assess the true effectiveness of the proposed tool.

6. **No Analysis of Failure Cases**: The paper does not analyze scenarios where the interpretability tool might fail or provide misleading interpretations, such as in complex visual contexts or cases where there are multiple objects of the same color. Such an analysis would offer a more balanced perspective on the tool’s robustness and limitations. Lack of discussion on limitations

### Questions
1. Could you provide a theoretical explanation for why log probability increases might yield better interpretability than attention scores?
2. Have you tested the interpretability tool on more complex VQA tasks and other models?
3. Can you offer a quantitative comparison of your interpretability tool against standard methods?
4. What is limitation of this method?
5. Is there cases where this method failed?

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
The paper aims to explore the underlying mechanisms of visual question answering (VQA) in multimodal large language models (MLLMs), focusing on Llava, a model fine-tuned on the textual LLM Vicuna. The authors use mechanistic interpretability techniques to compare VQA with textual question answering (TQA), especially on color-based tasks. They find that VQA operates similarly to attention mechanisms observed in TQA, with the visual embeddings providing interpretable insights into images, such as color and object features. The study introduces an interoperability metric and a tool to help users identify key image regions influencing model predictions, enhancing understanding of phenomena like visual hallucination. The proposed method achieves greater interpretability and efficiency than existing approaches.

### Strengths
Mechanistic Insights into Multimodal Models: The paper provides a deep mechanistic understanding of visual question answering (VQA) in Llava, a multimodal large language model. By comparing VQA and textual question answering (TQA) mechanisms, it offers novel insights into how visual embeddings can be interpreted similarly to textual embeddings, extending the understanding of multimodal learning.

Effective Interpretability Tool: The development of an interpretability tool that identifies key image regions influencing predictions is a valuable contribution. This tool not only aids in understanding the VQA mechanisms but also addresses issues like visual hallucinations, offering real-time and more efficient explanations than traditional causal intervention methods.

Empirical Validation: The authors back their claims with thorough empirical analysis, using color prediction to demonstrate the similarities and differences between VQA and TQA mechanisms. The comparison of attention heads across Vicuna and Llava models further strengthens the findings, showcasing how visual instruction tuning enhances the pre-existing abilities of the base model.

### Weaknesses
Baselines: The paper mentions using log-probability increases to identify important image patches but does not compare or benchmark against traditional gradient-based attribution methods like Integrated Gradients (Sundararajan et al., 2017), Grad-CAM (Selvaraju et al., 2017), or SmoothGrad (Smilkov et al., 2017). Also, Gandelsman et al. (2023) explored text-based decomposition of CLIP’s image representations. These methods are feasible with llava.

Narrow Evaluation: The paper claims the robustness of the proposed metric. However, the experiments were only done with color attributes. It's hard to convince readers the metric generalizes to further recognition or visual reasoning tasks. Evaluation of real-world instead of synthetic data is also encouraged to inspire more findings.

Limit in Novelty and Contributions: The technical contribution of this paper is too incremental for acceptance. Basically, the paper doesn't contribute any method but just analyses LLMs and VLMs with existing methods. The findings are neither surprising. The overall contributions are therefore limited.

Limited Generalization to Other Models: While the study offers insights into Llava’s VQA mechanism, it remains unclear how well these findings extend to other multimodal models beyond Llava and Vicuna.

Line 134 typo serious -> series.

### Questions
1. Consider eval on more tasks, providing a more comprehensive analysis on various attributes/relationships/entities.
2. Test the method with more models.
3. Revise the related works and baselines to compare with.

### Soundness
3

### Presentation
2

### Contribution
2
