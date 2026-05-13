# Towards Interpreting Visual Information Processing in Vision-Language Models

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Vision-Language Models (VLMs) are powerful tools for processing and understanding text and images. We study the processing of visual tokens in the language model component of LLaVA, a prominent VLM. Our approach focuses on analyzing the localization of object information, the evolution of visual token representations across layers, and the mechanism of integrating visual information for predictions. Through ablation studies, we demonstrated that object identification accuracy drops by over 70\% when object-specific tokens are removed. We observed that visual token representations become increasingly interpretable in the vocabulary space across layers, suggesting an alignment with textual tokens corresponding to image content. Finally, we found that the model extracts object information from these refined representations at the last token position for prediction, mirroring the process in text-only language models for factual association tasks. These findings provide crucial insights into how VLMs process and integrate visual information, bridging the gap between our understanding of language and vision models, and paving the way for more interpretable and controllable multimodal systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work applies mechanistic interpretability techniques to understand how visual information is localized and processed in VLMs. This work:

- Tries to localize where information processing happens within VLM transformers
- Applies the “logit lens” (Nostalgebreist 2020) to understand how representations of visual tokens evolve across layers of the transformers
- Applies attention knockout to see how blocking attention between different subsets of tokens in the transformer causes the accuracy of the VLM to decrease

For localization, they find that ablating object tokens with a buffer has the most impact on model performance on the 3 ablations, with two LLaVA VLMs. For the logit lens, they find that patch embeddings at different layers can be mapped to corresponding meaninful tokens in the tokenizer vocabulary.

**EDIT 11/25/2024:** I am raising my score from 6 to 8, and soundness from 3 to 4, after the author response.

### Strengths
1. Important problem: The authors address an important problem of understanding how visual knowledge is localized and processed in transformer-based VLMs.

2. The formulation of each sub-question is well-motivated, the method and metrics are well-designed, the analysis of each sub-question is really thorough, and the findings are well summarized.

3. The paper is very well-written and easy to follow.

### Weaknesses
1. **Evaluated insufficient VLMs:** As the authors acknowledged, the analysis is performed on only two VLMs from the same (LLaVA) family. However, the methodologies should be easily extendable to other transformer-based VLMs. 

    A key sticking point of mechanistic interpretability methods is that we do not know how the findings generalize to other models, so it is hard to take any findings at face value when they have only been performed on one model (especially when some of the findings contradict findings from other works, e.g. VLMs rely on features stored in register tokens). It is crucial to determine if the observed localization patterns are specific to the LLaVA architecture or if they represent more general principles of visual processing in VLMs. The lack of diversity in the models tested makes it difficult to draw broad conclusions about how visual information is processed in these architectures. Specifically, the use of only LLaVA models, which share a common architecture and training methodology, may lead to conclusions that are not applicable to other VLMs with different architectures, such as those employing different attention mechanisms or pre-training strategies. This limits the impact of the findings, as the field needs to understand the commonalities and differences across various VLM architectures.

2. **Results of "logit lens" analysis are hard to interpret:** While the authors find some interesting mappings between visual patches and output tokens, it's hard to tell if these are meaningful correspondences or an artifact of cherry-picking/confirmation bias, since we see mappings for only a handful of patches, and only at one layer (although it is unclear which one). The presented examples lack a systematic approach to validate the observed mappings. Without a clear methodology for selecting and evaluating these patch-token pairs, it's difficult to ascertain whether the observed correspondences are representative or merely coincidental. The absence of a quantitative analysis of the logit lens results makes it challenging to assess the overall significance of the findings. Furthermore, the lack of analysis across multiple layers makes it difficult to understand how these mappings evolve during the processing of visual information. The current presentation leaves the reader questioning the robustness and generalizability of the logit lens analysis.

### Questions
In Figure 3, what layer do these unembeddings correspond to? Are these all from a specific layer, or did you select instances from different layers that matched human interpretations?

### Soundness
4

### Presentation
4

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
This paper studies how VLMs, particularly LLaVA, process and integrate visual information. Through ablation studies, the authors show that object information is localized in specific visual tokens, which evolve into interpretable text-like representations across layers. Attention flow experiments reveal that the model extracts object-specific information in mid-to-late layers while processing contextual information in earlier layers.

### Strengths
1. The paper is well-written and well organized. There are effective diagrams and explanations that make complex concepts accessible.
2. The paper presents an innovative approach to understanding how visual tokens are processed in the language model component of VLMs. The insights on visual token alignment could inform practical techniques to improve VLM robustness and reduce hallucinations in multimodal tasks.
3. The authors design comprehensive experiments and ablation studies to support the findings.

### Weaknesses
1. The experiments only focus on the LLaVA model. The authors can consider other prevailing VLMs. The lack of diversity in model selection limits the generalizability of the findings. It is unclear whether the observed phenomena are specific to LLaVA's architecture or if they are common across different VLM designs. For example, models with different visual encoders or cross-attention mechanisms might exhibit different patterns of visual token processing. The study should include models with different architectural choices to validate the robustness of the conclusions.
2. The authors can provide more direct evidence (experiments) to support the potential applications of the proposed methods. While the paper offers interesting insights into the internal workings of VLMs, it does not demonstrate how these insights can be translated into practical improvements in downstream tasks. The paper lacks concrete experiments showing how the identified object-specific visual tokens can be manipulated to improve performance or mitigate issues like hallucinations. The potential application of modifying attention mechanisms based on the findings is not explored with empirical results.

### Questions
Is it easy to apply the methods and findings in this paper to downstream tasks?

### Soundness
4

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
4

### Summary
This paper presents a study of the processing dynamics of visual tokens within adapter-style VLMs, particularly focused on investigating where object information may be stored and how it is used throughout the model. 

The study is anchored around 3 main methods: 

1. The ablation of tokens pertaining to the locations of objects within images (by replacing with a globally averaged token). This is compared against the ablation of register tokens, random tokens, and high-gradient tokens (determined using the Integrated Gradients method for selecting tokens most influential in a given model decision). Experimental results (Table 1) show that  the ablation of object level tokens results in a significantly higher degradation in performance when compared against ablating comparable amounts of random or high-gradient tokens. 

2. Applying a Logit Lens style analysis to intermediate layers' representations to qualitatively study what information is encoded in intermediate representations of tokens as they flow through the model. A (I believe qualitative) study over this shows that activations of visual tokens in later layers of the model tend to be decoded by the unembedding matrix into tokens pertaining to concepts related to the image (e.g. an "eye" on a face). 


3. Attention knockout to better understand the importance of certain token group dyads for model performance. Results show that "knocking-out" attention from object tokens to the last visual token (which is conjectured to be used by VLMs to reason about outputs) results in a greater performance degradation when compared against knocking out all visual tokens except for those in the last row to the visual tokens in the last row. 

**Recommendation**
I think the paper is generally very well written, easy to understand, and generally supports its claims about the locality of object-level information to tokens pertaining to object regions in images. I have a few questions and concerns (see Weaknesses and Questions below) which I would value the authors addressing before I finalize my score (and which I think addressing could help strengthen the clarity of the paper). I am generally leaning towards recommending acceptance.

### Strengths
**Presentation**: The paper is very clearly written and the provided figures do an excellent job of communicating the experimental setup and results. I have some questions about implementation details that appear omitted, but everything that was included in the paper was generally very easy to follow due to the quality of the writing. 

**Token Ablation Experiments**: The experiments presented in section 3 appear quite thorough and soundly motivated/constructed. The filtration strategy selected to simplify the experimental setup makes sense, and the selection of baselines to compare object token ablation against provides good coverage of alternative explanations to the papers' hypothesis. As a result, the provided experimental results appear to clearly show the presence of object information within the tokens of object regions in images.

### Weaknesses
 **Attention Flow Experiments**: The attention flow experiments appear somewhat inconclusive. The provided experimental results do indeed show a distinct performance degradation when knocking out attention from object tokens in later layers to the last visual token when compared against knocking out attention from all rows to the last row. However, the authors state in L219-L228 that there are competing explanations about where information is aggregated (e.g. just within visual tokens vs. also within text tokens). I would have therefore expected an additional condition in Table 2 showing the performance of knocking out some variant of text token attention, especially given that the model must ultimately use the text tokens to generate a description. The current setup does not sufficiently isolate the contribution of visual token attention from the potential influence of text token attention in the final prediction.

**Missing Details**: This is minor, but I think there's a number of experimental details missing whose inclusion could stand to strengthen both the clarity and reproducibility of the paper (see Questions below). Specifically, the lack of detail regarding the automated object detection and correspondence identification processes raises concerns about the robustness and generalizability of the findings. The absence of specific metrics or statistical measures for these automated steps makes it difficult to assess the reliability of the reported results.

### Questions
* L257 - 259: This is likely not necessary to clear up, but I'm curious if the authors tried ablating tokens by zeroing out embeddings rather than using the global average token? I imagine this might just generally hurt performance potentially adding a confounding factor to the experiments. Depending on the answer, perhaps mentioning the reason behind this design choice could add clarity. 

* L262-L266: How is it ascertained whether the target object o is mentioned in the generated description? Is this done manually or automatically? 

* L242-L246: How is correct identification determined? Is this automated or manual? 

* L329-:330: I'm wondering what the precise definition of "comparable number of tokens" is here? Is this compared to the average number of object tokens per image in the dataset? 

* L350-L352: How are correspondences identified, is this done by hand? If so, could the authors please comment on the statistics of how many images were evaluated, and if some measure of percentage of correspondences found was measured? In other words, I'm trying to get a sense of how reliably this behavior is observed in the model. Given the current level of detail provided, readers may assume that these results were cherry picked. 

* L369: "such numbers seemingly counting applies in background tokens." -- the wording is a little awkward, consider revising.

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
3

### Summary
This work proposes some interpretable experiments to investigate the flow of visual information processing in LLaVA-based VLMs. The authors find 3 synthetic tasks to test whether the blurred object tokens will affect the prediction accuracy of VLMs. Secondly, the attention blocking experiments investigate whether the VLMs rely on visual information summarization to predict the correct answer. The findings are interesting and vital to VLM development.

### Strengths
1. This work provides very important insights to the visual information processing of VLMs. Even if previous phenomena like the correlation between high-resolution SFT and good performance in LLaVA-1.6 has too some degree revealed that the object visual tokens can be very significant to the correct image understanding of VLMs, the quantitive analysis on such effects are not conducted.

### Weaknesses
1. The contributions on the interpretability of visual information processing in VLMs are well recognized, while the contributions on how we can adopt such information processing pattern on better prompting or training for VLMs are limited. For example, if the object visual tokens are vital for the answer prediction, is it possible that simply repeat them or augment them can lead to significant performance improvement? And maybe some text prompts or soft-prompts can well utilize such object visual tokens for better model understanding?

2. The investigations focus on object only, which are only important to the general VQA, captioning, and some specific object detection tasks. Beyond object visual tokens, the OCR tokens, text rendering tokens, and knowledge-related tokens can also be your study object. For example, what is the effect of blocking the important text tokens to the tasks of TextVQA, OCRVQA, MME, POPE?

3. The definition of last row of visual tokens in line 435 is very confused to me. For example, CLIP-L has 16*16 visual tokens, does it mean the last [-1,;] 16 tokens? It is recommend to provide a lot of explanations on that and why such experiments on last row visual tokens are required?

4. The experiments in Table 2 is highly related to how you split the early/mid/late layers. Since Phi-3 has less layers than the LLM used in LLaVA, vicuna-7b, is there any difference on your findings when you adopt LLaVA-Phi-3 as investigation VLMs?

### Questions
1. The definition of last row of visual tokens in line 435 is very confused to me. For example, CLIP-L has 16*16 visual tokens, does it mean the last [-1,;] 16 tokens? It is recommend to provide a lot of explanations on that and why such experiments on last row visual tokens are required? 

2. The experiments in Table 2 is highly related to how you split the early/mid/late layers. Since Phi-3 has less layers than the LLM used in LLaVA, vicuna-7b, is there any difference on your findings when you adopt LLaVA-Phi-3 as investigation VLMs?

### Soundness
3

### Presentation
2

### Contribution
3
