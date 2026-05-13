# Mitigating Spurious Correlations in Zero-Shot Multimodal Models

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Multimodal models or Vision Language Models (VLMs) have reshaped the paradigm in machine learning, offering zero-shot capabilities that require no additional training when adapted to new classification tasks. However, despite their advancements, spurious correlations still exist in VLMs. Existing approaches to tackle this issue often require target label annotations, contradicting the principle of zero-shot classification, or they primarily focus on a single modality, risking misalignment between text and image modalities. Others rely on extensive domain knowledge or large language models (LLMs) to characterize spurious features, making the performance sensitive to the generated prompts and undermining zero-shot capability. In response, we propose a new solution that tackles spurious correlations in VLMs within the zero-shot setting. Our approach utilizes a translation operation that preserves the latent space distribution to address issues of spurious correlations. In particular, our method is grounded in and inspired by a theoretical analysis, which identifies that the optimal translation directions are along the spurious vector. As VLMs unify two modalities, we compute spurious vectors from the text prompts and guide the translation for image embeddings, aligning the requirements for the fusion of different modalities in VLMs. We conducted experiments on benchmark datasets, which have shown significant improvements in worst-group accuracy. Additionally, our visualizations of VLMs further demonstrate the effectiveness of this intervention.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors proposed a method to address spurious correlations in Vision Language Models while preserving their zero-shot capabilities. Drawing on theoretical analysis to explore optimal strategies for translating image embeddings, they introduce TIE—a simple algorithm that guides the translation of image embeddings based on the text prompt. The core idea is  to apply a translation transformation in the latent space using "spurious vectors" derived from text prompts to better align text and image embeddings. Experimental results on real-world datasets demonstrate that this approach not only improves the worst-group accuracy across all datasets but also achieves comparable overall accuracy, enhancing the robustness of VLMs across modalities.

### Strengths
- The important task of mitigating spurious correlations in VLMs
- The interesting idea of applying a translation transformation in the latent space for cross-modal alignment
- Rigorous theoretical analysis to examine optimal strategies for translating image embeddings
- Quantitative and qualitative results validating the effectiveness of the proposed method

### Weaknesses
 - More in-depth discussion of the method is necessary (Why does it work? When does it fail? etc.)
- English can be improved

### Questions
- Have you conducted an evaluation of the quality of the predicted pseudo-spurious labels on a validation set in order to analyze and bridge the accuracy gap between TIE and TIE*?

- In large-scale datasets and tasks, how valid is the assumption of a single spurious feature for the entire dataset? How can spurious features be efficiently identified on a per-data-point basis?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- Paper proposes TIE, a method to mitigate spurious correlations in VLMs.
- TIE uses a translation operation in the latent space, guided by spurious text prompts, to shift image embeddings away from spurious features.
- The approach preserves the embedding distribution, unlike projection-based methods.
- TIE*, a variant, uses the VLM itself to infer spurious labels when explicit labels are unavailable.
- Experiments on several benchmarks show improvements over other methods.

### Strengths
- TIE/TIE*'s translation-based approach is a novel contribution to the field as far as I know.
- The method has strong theoretical analysis
- It effectively addresses spurious correlations without requiring training or labeled data.
- The experimental results are good.

### Weaknesses
 - TIE relies on accurate spurious prompts. The authors propose TIE* but its performance is not as good as TIE. Further investigation into the limitations of TIE* and potential improvements would help.
- The experiments focus on CLIP-based models. Exploring TIE/TIE* on other VLMs would be helpful.
- nitpick: the capitalization of the term "TIE" implies its an acronym. If it is an acronym, it's unclear what it stands for.

### Questions
1. How sensitive is TIE to the choice of spurious prompts? Are there any guidelines for selecting effective prompts?
2. What are the failure cases of TIE* and how can automatic inference of spurious labels be improved?

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
4

### Summary
The paper proposes a way to robustify VLMs like CLIP against spurious correlation. The proposed method (TIE) does not require any extra data and fine-tuning; and operate across modalities (as opposed to previous method that only operates in single modalities). In order to preserve the image embedding distribution, the proposed method is based on a translation operation in the embedding space, and find the optimal translation vector based on theoretical analysis. In practice, this translating vector is found using spurious text prompts.

Theoretically, the authors show how this method compare to another zero-shot rebustification method, Roboshot; and show the major drawback of Roboshot that is tackled by TIE. Empirically, the method outperforms almost all existing baselines.

### Strengths
- Very nice theoretical analysis that backs the proposed methods. First the authors derives what is the optimal translation vector based on the definition of zero-shot classification and group robustness problems.
- Very nice comparison with RoboShot, which strongly shows why the proposed method is necessary to improve upon RoboShot.
- Strong empirical results with strong baselines.
- Nice visualization results in 4.5, strongly backs the claim why CLIP robustification is necessary in the first place.

### Weaknesses
1. Some notations need to be clarified (check Questions).
2. I think the TIE* procedure needs to be clarified more, do we need to know possible values of $t_a$ beforehand? this need to be made clearer in the early in the writing when TIE* is introduced.

### Questions
1. What is $h_a$ in Theorem 1? is it image embeddings w/ spurious features $a$ regardless of the label?
2. What is the difference between $t_{spu}$ and $t_a$? (Equation 9)
3. For TIE*, does it mean we need access to all possible spurious features descriptions? Not necessarily a drawback as mostly in datasets we know this beforehand

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the spurious correlations existing in VLMs, the authors propose a new solution called TIE  that tackles spurious correlations within the zero-shot setting without requiring target label annotations, which would contradict the zero-shot principle. TIE utilizes a translation operation in the latent space that preserves the distribution of image embeddings, guided by text prompts to address spurious correlations. This approach is theoretically grounded, identifying optimal translation directions along the spurious vector.

### Strengths
1. The experiments in this paper are comprehensive and have been verified on datasets from many different fields (four different image domains), proving that the method is universal and has good generalization properties.

2. The structure of the paper is clear, and the methods proposed are easy to follow.

### Weaknesses
1. The performance improvements of the proposed method are not particularly obvious.

2. When RESNET-50 is used as the backbone, the proposed method performs poorly. Is there a way to solve the misalignment between text and image?

3. How do we ensure the accuracy of the textual hints provided when using artificially identified fake features? Is there an evaluation mechanism to verify the effectiveness of these hints?

### Questions
1. When RESNET-50 is used as the backbone, the proposed method performs poorly. Is there a way to solve the misalignment between text and image?

2. How do we ensure the accuracy of the textual hints provided when using artificially identified fake features? Is there an evaluation mechanism to verify the effectiveness of these hints?

### Soundness
3

### Presentation
3

### Contribution
3
