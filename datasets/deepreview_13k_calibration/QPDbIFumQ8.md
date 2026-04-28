# EMMA: Efficient Visual Alignment in Multi-Modal LLMs

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Multi-modal Large Language Models (MLLMs) have recently exhibited impressive general-purpose capabilities by leveraging vision foundation models to encode the core concepts of images into representations. These are then combined with instructions and processed by the language model to generate high-quality responses. Despite significant progress
in enhancing the language component, challenges persist in optimally fusing visual encodings within the language model for task-specific adaptability. Recent research has focused on improving this fusion through modality adaptation modules but at the cost of significantly increased model complexity and training data needs. 
In this paper, we propose \textbf{EMMA} (\textbf{E}fficient \textbf{M}ulti-\textbf{M}odal \textbf{A}daptation), a lightweight cross-modality module designed to efficiently fuse visual and textual encodings, generating instruction-aware visual representations for the language model. Our key contributions include: (1) an efficient early fusion mechanism that integrates vision and language representations with minimal added parameters (less than 0.2\% increase in model size), (2) an in-depth interpretability analysis that sheds light on the internal mechanisms of the proposed method; (3) comprehensive experiments that demonstrate notable improvements on both specialized and general benchmarks for MLLMs. Empirical results show that EMMA boosts performance across multiple tasks by up to \textbf{9.3\%} while significantly improving robustness against hallucinations

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces EMMA, a lightweight cross-modality module that implements visual-language early fusion, generating instruction-aware visual representations for the language model. This module adds less than 0.03% of parameters to the framework while boosting performance across multiple MLLM benchmarks.

### Strengths
* Leveraging the inherent alignment properties of pre-trained CLIP text and vision encoders to implement an early fusion module is intuitive.
* The model's structural design is characterized by its simplicity and clarity.
* The analysis presents a novel perspective on modality adaptation.

### Weaknesses
 * In line 251, it is mentioned that current methodologies depend on complex cross-modality modules, particularly highlighting mPLUG-Owl2. However, the paper does not provide a theoretical comparison with methods like LLaVA and Qwen-VL, which utilize straightforward projection layers that add only a minimal number of parameters to achieve visual-language alignment.

* The proposed EMMA introduces a Modality Adaptation module based on the correlation between word tokens in instructions and visual tokens. However, this methodology lacks performance guarantees when instructions are verbose or correlate poorly with visual tokens. The benchmarks selected in the paper are skewed towards VQA tasks, which inherently possess a high correlation between instructions and visual tokens. It is imperative that benchmarks assessing fine-grained perception capabilities, such as document understanding and OCR tasks (e.g., Chartqa[1] and Docvqa[2]), should also be evaluated to ensure comprehensiveness. Furthermore, the slight performance declines observed on ChartQA and DocVQA suggest a potential limitation in handling tasks requiring precise spatial reasoning and text recognition, which should be further investigated with additional OCR benchmarks such as AI2D, OCRbench, TextVQA, and InfoVQA to ascertain whether the method can achieve comparable performance to LLaVA 1.5 or whether it consistently impairs performance on such tasks.

* Lack of comparison with visual-language early fusion works (e.g., QA-ViT[3]).

* In line 295, the claim that leveraging the inherent alignment properties of CLIP encoders obviates the need for complex cross-modal modules and extensive training to attain alignment is deemed unwarranted, given that the instruction embeddings fed into the LLM are not inherently aligned with CLIP features. Indeed, the proposed EMMA incorporates a projection layer akin to LLaVA after its Modality Adaptation module and also adopts the pre-alignment training from LLaVA. The reviewer considers this projection layer a pivotal component of EMMA's alignment achievement. Conducting additional ablation experiments wherein this projection layer is replaced with a simple linear projection or removed entirely could potentially strengthen the authors' argument.

* While Line 319 mentions the utilization of data from the same datasets, the 1.8M training samples employed by EMMA deviate in quantity from those used in any of the baselines, rendering it challenging to demonstrate the effectiveness of the Modality Adaptation module. Given that LLaVA 1.5 is fully open-source and shares a very similar structure with EMMA, adding the following experimental results would significantly strengthen this paper: (1) the outcomes of EMMA using the 1.2M training set from LLaVA 1.5, and (2) the results of LLaVA 1.5 utilizing the 1.8M training set from EMMA.

* The conclusion drawn in line 343 is not convincing. The findings in Figure 5(a) demonstrate that text tokens are indeed involved in the feature fusion process. Yet, they do not sufficiently establish that the alignment module effectively identifies the "most" informative textual tokens. The reviewer thinks the positions of the most valuable tokens for an arbitrarily given instruction are random, and the current framework adopting a simple linear layer, which allocates fixed importance weights for textual tokens during inference, can not adapt to this change. Moreover, while the training instructions are short and straightforward, it remains unclear how EMMA ensures the accurate identification of crucial textual tokens during the testing phase, particularly in cases where instructions are more complex, such as those including extensive hints or lectures that are essential for guiding responses in tasks like SQA. 

* The reviewer praises the methodology illustrated in Figure 6, which employs Mutual Information to assess the importance of aligned visual representations in the reasoning process. However, concerns about its reliability are raised. A significant counterexample emerges in situations where the dataset requires responses strictly in YES/NO format, making the mutual information between the visual representations and the response encodings lack meaningful relevance.

* Which figure does the conclusion in line 338 correspond to?

### Questions
* In line 295, the claim that leveraging the inherent alignment properties of CLIP encoders obviates the need for complex cross-modal modules and extensive training to attain alignment is deemed unwarranted, given that the instruction embeddings fed into the LLM are not inherently aligned with CLIP features. Indeed, the proposed EMMA incorporates a projection layer akin to LLaVA after its Modality Adaptation module and also adopts the pre-alignment training from LLaVA. The reviewer considers this projection layer a pivotal component of EMMA's alignment achievement. Conducting additional ablation experiments wherein this projection layer is removed could potentially strengthen the authors' argument.

* While Line 319 mentions the utilization of data from the same datasets, the 1.8M training samples employed by EMMA deviate in quantity from those used in any of the baselines, rendering it challenging to demonstrate the effectiveness of the Modality Adaptation module. Given that LLaVA 1.5 is fully open-source and shares a very similar structure with EMMA, adding the following experimental results would significantly strengthen this paper: (1) the outcomes of EMMA using the 1.2M training set from LLaVA 1.5, and (2) the results of LLaVA 1.5 utilizing the 1.8M training set from EMMA.

* The conclusion drawn in line 343 is not convincing. The findings in Figure 5(a) demonstrate that text tokens are indeed involved in the feature fusion process. Yet, they do not sufficiently establish that the alignment module effectively identifies the "most" informative textual tokens. The reviewer thinks the positions of the most valuable tokens for an arbitrarily given instruction are random, and the current framework adopting a simple linear layer, which allocates fixed importance weights for textual tokens during inference, can not adapt to this change.

* The reviewer praises the methodology illustrated in Figure 6, which employs Mutual Information to assess the importance of aligned visual representations in the reasoning process. However, concerns about its reliability are raised. A significant counterexample emerges in situations where the dataset requires responses strictly in YES/NO format, making the mutual information between the visual representations and the response encodings lack meaningful relevance.

### Minor:
* Which figure does the conclusion in line 338 correspond to?

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
3

### Summary
This paper introduces EMMA (Efficient Multi-Modal Adaptation), a lightweight module designed to improve cross-modal alignment in multi-modal large language models (MLLMs). EMMA integrates visual and textual encodings using a low-parameter approach that leverages pre-trained CLIP models. Specifically, the method incorporates both CLIP’s vision encoder and its text encoder into the multi-modality alignment module, taking advantage of their pre-trained alignment to fuse visual representations with instruction encodings efficiently. The proposed architecture adds less than 0.2% additional parameters, making it highly efficient compared to existing models such as mPLUG-Owl2.

### Strengths
1. Detailed analytical insights: The paper offers a thorough analysis of the modality alignment process through l1,  l2, and mutual information comparisons. This analysis provides deeper insights into how visual and textual tokens are integrated within the alignment module, enhancing the interpretability of the model's decision-making process.

2. Robustness against hallucinations: The empirical results highlight EMMA's superior ability to avoid hallucinations in multi-modal tasks, as demonstrated on benchmarks such as AMBER and FOIL. This robustness is critical for improving the reliability of MLLMs in real-world scenarios where model hallucinations can pose significant risks.

### Weaknesses
1. Inconsistent writing and presentation: The overall writing of the paper is somewhat disorganized, making it difficult to follow and reducing its readability. For example, Section 3.1 is intended to introduce the EMMA method, but the section ends with a discussion of experimental results (in the last paragraph on page 6). Similarly, in Section 3.2, which is supposed to focus on the Analysis on Modality Adaptation by EMMA, the section starts by explaining model details, which would be better suited earlier in the paper. Additionally, Figure 1 is referenced only on page 6, even though it appears on page 2. Many figures and tables also lack proper axis labels and detailed captions, which further hinders the reader's ability to understand the data. For instance, it would be helpful to clarify the contents of the axes in Figures 2, 5, and 6.

2. Unfair experimental comparisons: The paper does not provide a fair and direct comparison between different vision-language adapters, which is essential since the focus is on adapter efficiency. While achieving complete consistency between the vision and language models might be challenging, it would be beneficial to at least include an additional set of experiments that utilize other adapters, such as [1-2], alongside the same vision and language models. This would allow for a more fair comparison of their performance against the EMMA adapter. By keeping the vision and language models constant across different methods, the paper could offer a clearer evaluation of the specific contributions made by EMMA’s adapter design.

### Questions
Please see weakness.

1. Can the authors provide more formulized descriptions of the proposed method? For example, this could include mathematical formulas or structured descriptions similar to those at the beginning of Section 3.2.

2. Can the authors include additional experimental comparisons with other adapter-based methods, such as [1-2] ? These would offer a more comprehensive evaluation of EMMA’s performance relative to other state-of-the-art adapters.

3. EMMA uses CLIP-ViT-L-14 as its visual encoder, but it's unclear whether the same visual model is used in the comparison models. Could the authors provide details on the visual models used by the other models in Tables 2 and 4, along with their parameter counts?

[1] MMA: Multi-Modal Adapter for Vision-Language Models

[2] Tip-Adapter: Training-free CLIP-Adapter for Better Vision-Language Modeling

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes EMMA, a lightweight cross-modality module designed to efficiently fuse visual and textual encodings, generating instruction-aware visual representations for the language model.

### Strengths
1-Clear motivation: Improving effeciency is important for MLLMs.
2-Well-written paper: Easy to follow.
3-Substantial experiments and corresponding discussion.

### Weaknesses
1-The model is very similar to LLaVA: EMMA introduces CLIP-text encoder and an early fusion module.
2-The involvement of CLIP-text encoder is not very convincing: CLIP is trained for classification task only, but EMMA is a general-purposed instruction-aware MLLM. I am doubtful about the effectiveness when CLIP-text encoder deals with long instructions. You may make some visualization of the activation when CLIP encounter some long instructions / tasks apart from classification.

3-The discussion in Sec. 3.2 should incorporate more datasets apart from MMVP. Because I am not sure of the effectiveness of the CLIP-text encoder as above.

4-Unfair comparison: Table 1 without LLaVA, but Figure 3 only compare with LLaVA. Should compare LLaVA in Table1 and compare mPLUG-Owl2 and other methods in Figure 3. You may provide a table / figure to compare more methods.

5-The scale of Figure 3 is inappropriate, slight improves with significant distance, e.g. 64.3 -> 66.19 in MMB-en. I think a histogram bar will be better.

6-The claim in line 247-250 is too absolute: *Therefore, a persistent challenge remains in effectively aligning these two modalities to ensure seamless fusion and task-specific adaptability.* Actually, task-specific adaptability is important, but previous works solve it by LLM (very large scale).

7-Figure5: Two legends: purple and light green. What do dark green bars represent? Cannot understand right figure. Please give more decriptions.

8-Performances improve slightly in lots of datasets.

9-POPE dataset has many subsets, should provide detailed performances on each of them in a table.

10-If you mentioned hallucination, you should discuss and cite more papers. For example, there are relation hallucinations: R-Bench[1], and MMRel[2], and some datasets containing attribute hallucination: MME[3]. I do not ask you to evaluate on a bunch of datasets, you are just suggested to cite them and then the readers will have a clear picture of the hallucination tasks.

### Questions
Please see the weakness.

My major concern is about the novelty, both the slightly incremental structure based on LLaVA and the effectiveness of CLIP-text encoder.

### Soundness
3

### Presentation
4

### Contribution
3
