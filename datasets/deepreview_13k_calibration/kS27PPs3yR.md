# Fine-grained Abnormality Prompt Learning for Zero-shot Anomaly Detection

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Current zero-shot anomaly detection (ZSAD) methods show remarkable success in prompting large pre-trained vision-language models to detect anomalies in a target dataset without using any dataset-specific training or demonstration. 
However, these methods are often focused on crafting/learning prompts that capture only coarse-grained semantics of abnormality, \eg, high-level semantics like `\texttt{damaged}', `\texttt{imperfect}', or `\texttt{defective}' on carpet. They therefore have limited capability in recognizing diverse abnormality details with distinctive visual appearance, \eg, specific defect types like color stains, cuts, holes, and threads on carpet.
To address this limitation, we propose \coolname, a novel framework designed to 
learn \underline{F}ine-grained \underline{A}bnormality \underline{Prompt}s for more accurate ZSAD. 
To this end, we introduce a novel \textit{compound abnormality prompting} module in \texttt{FAPrompt} to learn a set of complementary, decomposed abnormality prompts, where each abnormality prompt is formed by a compound of shared normal tokens and a few learnable abnormal tokens. 
On the other hand, the fine-grained abnormality patterns can be very different from one dataset to another. To enhance their cross-dataset generalization, we further introduce a \textit{data-dependent abnormality prior} module that learns to derive abnormality features from each query/test image as a sample-wise abnormality prior to ground the abnormality prompts in a given target dataset.
Comprehensive experiments conducted across 19 real-world datasets, covering both industrial defects and medical anomalies, demonstrate that \coolname substantially outperforms state-of-the-art methods by at least 3\%-5\% AUC/AP in both image- and pixel-level ZSAD tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel framework for zero-shot anomaly detection (ZSAD) that focuses on learning fine-grained abnormality prompts without requiring detailed human annotations or text descriptions. Key contributions include the development of a Compound Abnormality Prompting (CAP) module for generating complementary abnormality prompts and a Data-dependent Abnormality Prior (DAP) module aimed at enhancing cross-dataset generalization. The authors assert that their method, FAPrompt, significantly outperforms existing state-of-the-art solutions in both image- and pixel-level ZSAD tasks across 19 real-world datasets.

### Strengths
1. The paper is clearly written and well-organized, making complex ideas accessible. Diagrams and figures effectively illustrate key ideas, enhancing reader comprehension.
2. The experiments are thorough, encompassing 19 diverse datasets from both industrial and medical domains. The results demonstrate substantial improvements over current state-of-the-art methods, reflecting the high quality of the proposed approach.

### Weaknesses
1. There is marginal improvement in pixel-level ZSAD in Table 2. In contrast, the simple AnomalyCLIP achieves comparable, and even superior, results on industrial datasets.
2. The design of DAP is very similar to CoCoOp, and using a fixed M across images with varying scales of anomalous regions is unreasonable.
3. Missing necessary baseline: AnomalyCLIP with an ensemble of multiple abnormality prompts with orthogonal constraint loss; otherwise, it is difficult to justify the fine-grained prompts.

### Questions
1. Could you provide additional evidence to substantiate the claim that the prompt-wise anomaly scores visualized in Figure 3 demonstrate the discriminability of FAPrompt? A comparison with visualizations from baseline models would effectively highlight the advantages.
2. To better verify the necessity of using multiple prompts, it is suggested to include more detailed ablation experiments, such as k=1 with and without CAP/DAP, similar to those in Table 4.
3. Ablation studies on the number of layers with learnable tokens and the length of the tokens should be included.
4. Minor: I recommend merging Table 3 and Table 4 for improved method comparison.

### Soundness
3

### Presentation
4

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
This study proposes FAPrompt to learn fine-grained abnormalities in Zero-shot Anomaly Detection (ZSAD) and classify anomalies based on data-dependent characteristics. To address the limitations of focusing on coarse-grained abnormality semantics, the authors introduce compound abnormality prompting (CAP) and a data-dependent abnormality prior (DAP) module, along with distinct loss terms to effectively train the CAP and DAP modules.

### Strengths
The motivation of this study is reasonable, and the proposed method is novel. Additionally, the method has been validated across diverse datasets.

### Weaknesses
1. The description of the learnable layers in the DAP module is missing.
2. The visualization in Figure 1 of the proposed methodology conflicts with the actual experimental results shown.

### Questions
1. Please provide specific examples or criteria that distinguish 'coarse-grained' prompts from the proposed fine-grained prompts. Clarifying this would help determine if the label is used due to a single prompt approach or if there is a deeper rationale.
2. Consider alternatives to averaging the abnormality prompts in the CAP module, such as selecting the most similar prompt for each detected abnormality. If other approaches were tested, sharing the rationale or results behind choosing the current method would add clarity.
3. Could the authors provide additional evidence or clarification on how the fine-grained distributions in Figures 1 and 3 align with each other? Additional context or visual consistency would strengthen the claim that each abnormality prompt represents a specific abnormal state.
4. The explanation regarding the effectiveness of the compound prompt seems insufficient. Could more information be provided on the outcomes when combining the normal learnable token with the abnormality token? Specifically, what results were achieved if CAP and DAP were applied independently, without this combination?
5. Could the authors clarify how this approach differs from existing prompt ensemble methods? Specifically, what distinguishes the process of averaging the abnormality prompts from a traditional ensemble approach, and in what ways does this differ from selecting the highest anomaly score across individual abnormality prompts?

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
The paper introduces FAPrompt, a novel framework designed to improve ZSAD by enabling fine-grained detection of abnormalities without requiring dataset-specific training or detailed human annotations. Unlike existing ZSAD methods that primarily capture coarse abnormality features, FAPrompt focuses on recognizing diverse, specific abnormality details across a range of datasets, such as industrial defects and medical anomalies.

### Strengths
1. FAPrompt addresses a key limitation in current ZSAD methods, which often struggle to identify fine-grained, specific abnormalities. By introducing learnable fine-grained abnormality prompts, FAPrompt improves both the accuracy and applicability of ZSAD in diverse contexts.
2. Comprehensive experiments show that FAPrompt outperforms state-of-the-art methods by notable margins (3%-5% improvements in AUC/AP) across both image- and pixel-level ZSAD tasks.

### Weaknesses
1. The novelty of FAPrompt is limited. The design of CAP seems a simple combination of prompt tuning and prototype learning. The use of an orthogonal constraint on the prompts, while potentially helpful, does not fundamentally alter the underlying simplicity of combining these two existing techniques. The method's core idea of using compound prompts to capture varying degrees of abnormality is not sufficiently distinct from existing methods that also aim to capture diverse features.
2. Besides CoOp and CoCoOp, other state-of-the-art prompt tuning approaches are expected for comparisons (e.g. PromptSRC[1] and TCP[2]). The lack of comparison with methods like PromptSRC, which uses self-regulating prompts for adaptation, and TCP, which focuses on textual-based class-aware prompt tuning, leaves a gap in understanding the relative performance of FAPrompt. These methods represent important baselines that should be considered to fully assess the contribution of the proposed approach.

### Questions
1. In table 4, image-level results on medical datasets show that CAP achieves the best result compared with FAPrompt, is there any further explanation?
2. How to demonstrate that CAP's ability of learning fine-grained abnormality semantics? In fig 3, fine-grained prompts (with different colors) seems not to be seperable.

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
The paper focuses on zero-shot anomaly detection by learning a set of fine-grained abnormality prompts based on CLIP. These abnormality prompts consist of shared normal tokens and specific abnormal tokens, providing fine-grained semantics of abnormality. To account for dataset variance, the authors further propose a data-dependent abnormality prior (DAP) to generate instance-aware prompts from the image patch features. Extensive experiments are conducted on 19 datasets, covering both industrial and medical scenarios, comparing the proposed method with a sufficient number of zero-shot anomaly detectors.

### Strengths
1. The design of compounding normal-abnormal tokens is interesting and novel.
2. The experiments are conducted extensively and demonstrate favorable performance.

### Weaknesses
1. The design of abnormality prompts is not entirely consistent with the concept of "fine-grained." Although CAP leverages a set of abnormality prompts with an orthogonal constraint loss, the final abnormality embedding is derived as the average of all abnormality prompt embeddings, resulting in a vector-based abnormality prompt prototype that essentially reduces the diversity of abnormalities. If there are multiple types of anomalies within an image, is a single abnormality prompt prototype sufficient?
2. The number of abnormality prompts, K, shows very limited difference to pixel-level detection results (see Figure 7), making it difficult to evaluate the necessity of multiple abnormality prompts. Additionally, Figures 4 and 7 are missing the results when K=1.
3. The proposed DAP is technically similar to CoCoOp, and it uses the features of selected image patches instead of the global image feature. Moreover, the parameter M appears to be quite sensitive for pixel-level ZSAD.

### Questions
1. I have some doubts about L087-L089. Since abnormality prompts have a different number of tokens compared to normal prompts, does this not make them easily distinguishable from normal prompts?
2. The first contribution is not accurate. The update of prompts indeed depends on human annotations in the cross-dataset scenario.
3. I suggest moving Figure 7 to the main manuscript, as both image-level and pixel-level zero-shot anomaly detection (ZSAD) are equally important for a comprehensive evaluation.

### Soundness
3

### Presentation
4

### Contribution
2
