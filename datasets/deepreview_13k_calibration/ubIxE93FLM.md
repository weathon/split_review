# Visually Descriptive Language Model for Vector Graphics Reasoning

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Despite significant advancements, current large multimodal models (LMMs) struggle to bridge the gap between low-level visual perception---focusing on shapes, sizes and layouts---and high-level language reasoning involving semantics, events and logic. 
This limitation becomes evident in tasks requiring precise visual perception, such as comparing geometric properties or solving visual algorithmic reasoning problems.
To study this failure mode, we focus on an important visual domain: \imgtype---images composed purely of 2D objects and shapes, which are prevalent in various LMM-based agent tasks in web, visual design, and OS environments.
We identify two key research questions: how can we enable precise visual perception, and how can we facilitate high-level reasoning based on such low-level perceptions?
To accurately capture low-level visual details, we utilize Scalable Vector Graphics (SVG) for precise encoding of visual scenes. 
However, SVGs are not readily interpretable by LLMs or LMMs in a zero-shot manner. 
To address this challenge, we propose the \textbf{Visually Descriptive Language Model (VDLM)}, which introduces an intermediate textual representation called \textbf{\bl (\blabbr)}. 
\blabbr translates SVGs into a text-based abstraction comprising primitive attributes (e.g., shape, position, measurement) along with their corresponding values.
\blabbr can be learned with task-agnostic synthesized data and represents visual primitives that are universal across various \imgtype.
This abstraction is more structured, allowing for direct interpretation by foundation models for zero-shot generalization to different reasoning tasks.
Without any human-annotated data, empirical results demonstrate that \oursfull leads to significant improvements in state-of-the-art LMMs, such as GPT-4o, across various low-level multimodal perception and reasoning tasks on \imgtype.
Additionally, we provide extensive analyses of VDLM’s performance, showing that our framework offers improved interpretability due to its disentangled perception and reasoning processes. 
Finally, we demonstrate the promise of this representation by showing a positive correlation between the quality of the \blabbr perception and the end-task performance. Project page: 
\url{https://mikewangwzhl.io/VDLM/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces VDLM that aims to decrease inaccuracies associated with modern VLMs by USING an intermediate representation Primal Visual Description (PVD), primitive geometry object descriptor that can help ground the interpretation of the image and increase the usability of the model on perception and reasoning tasks downstream tasks involving vector graphics. More specifically, the paper identifies Low-level visual reasoning tasks and High-level visual reasoning tasks, introducing benchmarks for evaluating the former and using VGBench-QA for the latter, and showing performance gains for both text and multimodal versions of VDLM.

### Strengths
- Interesting issue: The VLMs are known to struggle with low-level details in image analysis, making a low-resource solution like VDLM impactful.
- Benchmarking dataset: To the best of my knowledge the dataset is unique and is a significant contribution that could serve as a good benchmark for quantitative evaluation of current and future VLMs.
- PVD approach: Is intuitive and encodes a lot of information about the object in a relatively compact manner.

### Weaknesses
 - Practical usability: The Ontology of PVD is limited and seems like it would be hard to expand to more general use cases, furthermore it seems like PVD use would strain the context length significantly in any more complex use cases, thus while PVDs might be learnable in task-agnostic setting I am concerned about the generalizability of VDLM. Specifically, the current PVD ontology appears to be tailored to relatively simple geometric shapes and their spatial relationships. Extending this to more complex visual elements, such as intricate patterns, textures, or non-geometric forms, would likely require a substantial expansion of the ontology, potentially leading to a combinatorial explosion of PVD primitives. This could make the representation unwieldy and difficult to manage. Moreover, the sequential nature of PVD descriptions, where each object is described in terms of its geometric primitives and their attributes, could lead to very long sequences for even moderately complex scenes, exacerbating the context length limitations of current VLMs.
- Limited baselines: The paper reports numbers for Variations of GPT, LLaMA, ViperGPT models, however there are no comparisons with any symbolic approaches, making the positioning of the results hard to place. The absence of comparisons with symbolic methods makes it difficult to assess the relative strengths and weaknesses of VDLM. Symbolic approaches, which often rely on explicit representations and logical reasoning, might offer complementary advantages, especially in tasks requiring precise geometric reasoning or manipulation. Without such comparisons, it remains unclear how VDLM performs in relation to these established techniques, and whether it offers a genuine improvement or simply a different trade-off between accuracy and computational cost.

### Questions
- How would the method extend to SVG complexity found in websites and most usual use cases?
- How well could the method handle occlusion between distinct shapes?
- Could the authors provide further reasoning behind their choice of baselines? Why were symbolic reasoning approaches not included in the comparison?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel approach to enhance fine-grained image understanding by transforming raster images into a new vector graphics format called PVD, which consists of 9 distinct primitives. The authors propose a two-stage process: first, converting the raster image to an SVG format using a rule-based model, and second, converting the SVG to the proposed PVD format using a self-trained LLM. By incorporating the PVD representation into the LLM’s context, the authors report improved performance in fine-grained image understanding tasks. The paper also provides a comparative analysis with baseline approaches that input either raw images into VLMs or SVG representations into LLMs, highlighting the advantages of their method.

### Strengths
1. This work appears to be the first attempt to enhance foundation models' fine-grained image understanding capabilities by converting images into vector-based formats.
2. The introduction of the PVD vector graphics format offers a structure that seems better aligned with large language models.
3. Significant performance gains are observed when using the proposed PVD-based approach compared to directly using VLMs.

### Weaknesses
1. The rationale behind the two-stage transformation process (from PNG to SVG via a rule-based algorithm, and then from SVG to PVD via a self-trained LLM) requires further clarification. Specifically: (a) What fundamental distinctions, other than syntax, does PVD offer compared to SVG? The claim that PVD is a 'cleaner, higher-level abstraction' needs more rigorous justification. For instance, what specific types of noise or verbosity in SVG are problematic for LLMs, and how does PVD address these issues beyond simply reducing the number of points? (b) Why is an LLM necessary for the second step, given that SVG is a structured, well-defined format that could potentially be converted to PVD with rule-based transformations? The argument that rule-based conversion is 'impractical' needs to be substantiated with examples of the complexities involved. What specific SVG structures or variations make a rule-based approach infeasible? (c) Why not directly modify the rule-based raster-to-vector algorithm to output PVD instead of SVG? The assertion that the rule-based algorithm 'lacks awareness of the semantics of shapes' requires more detail. What specific semantic information is needed that the rule-based algorithm cannot capture, and how does the LLM acquire this information during the SVG-to-PVD conversion?
2. The proposed PVD format’s definition could benefit from further clarity, as there appears to be overlap among the 9 primitives (e.g., "composition-filled" could overlap with "polygon"; "path" and "grid" might overlap with "line segment"). Introducing a hierarchical structure might provide a clearer and more effective organization. The current definitions lack precise specifications, making it difficult to understand the exact distinctions between primitives. For example, what are the specific conditions under which a shape should be represented as a "composition-filled" versus a "polygon"? How does the system handle cases where a shape could be represented by multiple primitives? The lack of a formal grammar or specification for PVD makes it difficult to assess its expressive power and potential limitations.
3. The approach relies on synthesized data for training the LLM to convert SVG to PVD, which might limit the diversity and generalizability of the model’s performance. The paper should include a detailed analysis of the synthetic data generation process, including the range of shapes, complexities, and variations included. What measures were taken to ensure that the synthetic data adequately represents real-world image complexities? The potential for overfitting to the synthetic data should be addressed, and the paper should discuss how this limitation might affect the model's performance on real-world images.
4. Some terms in the paper could be refined for accuracy. For instance, the term "vector graphics" should refer to images defined by geometric primitives, such as SVG and PVD. In contrast, this work use that term "vector graphics" to refer to images rendered by SVG (which is the raster image in fact) (e.g., in the title and L91). Additionally, conflating "vector graphics" and "SVG" may be misleading (e.g., in L21–L22), as SVG is just one of several vector graphics formats.

### Questions
1. The results in Table 3 (Appendix) seem inconsistent with those in Table 1. If I understand correctly, Table 1 reports that GPT-4V achieved 58% in Angle Classification (AC) and 64% in Length Comparison (LC) with image inputs. However, Table 3 lists GPT-4V as achieving 58% in Angle Classification (AC) and only 57% in Length Comparison (LC). Could you clarify this discrepancy?
2. See questions raised in the weakness.

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
4

### Summary
This work focuses on vector graphics and proposes primal visual description (PVD) to better perceive and reasoning about 2D objects and shapes. Specifically, they propose PVD technique translates SVGs into a text-bassed abstraction aomprising primitive attributes along with their corresponding values. In this way, the PVD can replace the visual embeddings and directly participate in the LLM's reasoning process, improving the interpretability due to the disentangled perception and reasnoing processes.

### Strengths
1. The writing in this work is excellent, with clear logic that makes it easy to follow.

2. The experimental and analysis sections in this work are thorough and well-developed.

3. The concept of PVD is intuitive, simple, and effective.

### Weaknesses
1. The scope of application domains and evaluation data considered by the authors is too narrow. Although the authors mention web and OS environments as application scenarios in the abstract, the experimental evaluation is limited to simple SVG images. This may restrict the impact and significance of the work. In real-world applications, we cannot always assume that SVG-format images will be available. Furthermore, the reliance on a single, controlled dataset of synthetic SVGs limits the generalizability of the findings to more complex, real-world vector graphics with varying levels of noise and complexity.

2. The evaluation of high-level visual reasoning tasks is insufficient. First, only one benchmark was included in the validation, which limits the assessment of the method's robustness across different types of reasoning tasks. Secondly, the study only examined improvements for GPT-4V with VDLM support, which raises questions about whether other open-source, less capable LMMs (e.g., LLaVA-1.5, Qwen-VL) could benefit from VDLM as well. This is particularly important given the computational cost and accessibility of models like GPT-4V, and the need to understand the broader applicability of the proposed approach.

### Questions
1. What does the "VF" mean in Figure 1(b)? Does it denote the visual features?

2. Lacking discussion about related work [A]. It also highlights the disentangling of perception and reasoning for LMMs.

[A] Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs. NeurIPS 2024

I will consider raising the score if my concerns can be well addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method called VDLM, designed to improve large vision-language models capabilities to understand and reason about fine-grained visual concepts, specifically those well-suited to vector graphic representations. VDLM first converts an input image into a SVG format using a rule-based encoder. This SVG is then preprocessed and translated by a fine-tuned language model (e.g., Mistral-7b) into a structured JSON-like format called "Primal Visual Description" (PVD), which serves as an intermediate representation. Finally, this PVD is input into large vision-language models (e.g., GPT-4). The authors demonstrate that this pipeline improves performance of the base model (e.g. GPT4o) vs using a raw image or a raw/unprocessed SVG encoding.

### Strengths
* The paper focuses on an area of significant impact: improving visual reasoning/understanding in large vision-language models.

* The writing is clear and well-structured, making the methodology easy to follow.

* The proposed method achieves notable improvements in several evaluated tasks.

### Weaknesses
In my view, the main weakness of the paper is that, while it aims to "enable precise  visual perception and facilitate high level reasoning", the approach does not actually relies on visual perception. Instead, it sidesteps the need for genuine visual comprehension by essentially translating an image into text and performing all reasoning in text, limiting effectiveness for complex imagery requiring true visual inspection. Figure 5 supports this: only the GPT models show improvement, suggesting limited applicability unless the model’s text-based understanding is SoTA.  

SVG Limitations:  While the approach may work on some SVG, the claim in the abstract that SVG can accurately capture detailed visual scenes seems overstated, particularly within the context of this study. The rule-based SVG encoder, while effective for simple vector graphics, likely struggles with complex scenes that involve intricate textures, shading, or non-geometric elements. This limitation is not adequately addressed, and the paper does not provide a clear analysis of the types of visual information that are lost or distorted during the SVG conversion process.

Questionable Fine-Tuning Claim: The authors claim in line 085 “finetuning a model to reason about raw SVG codes can be inefficient and infeasible without corresponding task-specific annotations.”  This claim appears unsubstantiated, as fine-tuning an existing large multimodal model (e.g., LLaMA 3.2 11B, LLaVA) on the synthetic data generated for the PVD translator could potentially improve visual perception on such imagery without bypassing the need for vision. The authors do not provide any empirical evidence to support their assertion about the infeasibility of direct fine-tuning, nor do they explore alternative fine-tuning strategies that might mitigate the need for a separate PVD translation step. The lack of such experiments weakens the motivation for the proposed approach.

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
2
