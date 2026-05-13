# Evolved LLM Schemas for Mid Vision Feedback

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
In this work, we present ELF (Evolving LLM-Based Schemas for Mid-Vision Feedback), a framework that integrates schema evolution with Mid Vision Feedback (MVF) for visual learning. We leverage Large Language Models (LLMs) to automatically generate schemas: executable semantic programs operating over sets of context categories (e.g., ”animate” or ”inanimate”). We integrate schemas into visual processing via MVF, a method that utilizes top-down feedback connections to inform mid-level visual processing with high-level contextual knowledge. To optimize these schemas we utilize EvoPrompt, an evolutionary algorithm that refines schemas through iterative search, resulting in improvements in accuracy and contextual consistency. We demonstrate the effectiveness of ELF across multiple datasets and multiple architectures for the task of object classification

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- The paper presents ELF (Evolving LLM-Based Schemas for Mid-Vision Feedback), a framework integrating schema evolution with Mid-Vision Feedback (MVF) for enhanced visual learning.
- ELF uses Large Language Models (LLMs) to automatically generate executable schemas—semantic programs based on contextual categories that inform visual processing.
- The framework employs EvoPrompt, an evolutionary algorithm, to iteratively refine schemas for improved classification accuracy and contextual alignment.
- ELF demonstrates effectiveness across multiple datasets and models, showing that evolved schemas can be transferred to different architectures, maintaining performance improvements.
- The approach emphasizes biologically inspired feedback, where high-level context guides mid-level feature representation, mirroring how biological vision systems operate.
- The work highlights ELF's adaptability and potential for bridging vision and language, enhancing visual processing by aligning representations with task-specific contextual knowledge.

### Strengths
- The paper presents originality through its development of ELF, a framework that uniquely combines LLMs with Mid-Vision Feedback (MVF) to mimic biological vision systems, enhancing visual learning by integrating high-level contextual knowledge into mid-level feature processing.
- The use of EvoPrompt for schema generation and iterative refinement demonstrates a creative application of evolutionary algorithms, expanding the role of LLMs beyond traditional text-based tasks into schema-based visual learning.
- The quality of the research is supported by comprehensive experiments across CIFAR100, ImageNet, and Caltech101, showing consistent improvements in accuracy and schema transferability across different architectures. The methodology is detailed enough to ensure reproducibility.
- Clarity is maintained throughout the paper, with well-organized sections and the effective use of diagrams to illustrate complex processes such as schema generation and MVF integration. This helps readers grasp the approach and its underlying mechanisms.
- The significance of the work lies in its contribution to the field of vision-language integration, demonstrating how LLM-generated schemas can be used to guide and improve visual processing. The framework shows potential for wider application in various vision tasks that require contextual adjustments.
- ELF’s demonstrated ability to transfer schemas across datasets and architectures underscores its adaptability and robustness, making it a promising tool for advancing vision systems in real-world scenarios and opening doors for further exploration in schema-driven learning.

### Weaknesses
- The paper's focus on a limited set of visual contexts (e.g., animate/inanimate, nature/urban) restricts the generalizability of findings. Expanding experiments to include a wider variety of context types would enhance the applicability and depth of the results.
- Transferability across more diverse datasets is not fully explored. While the paper shows results for CIFAR100, ImageNet, and Caltech101, adding experiments on more challenging datasets with higher intra-class variability could strengthen claims of generalizability.
- The paper lacks a thorough comparison with other context-modulating techniques beyond its scope (e.g., attention-based feedback mechanisms). Including a comparison with alternative top-down or context-driven approaches would offer clearer insights into ELF’s relative strengths and weaknesses.
- Analysis of failure cases is minimal. Presenting specific examples where ELF did not perform well or where the schema approach struggled would provide valuable insights for future iterations and improvements.

### Questions
- Could you elaborate on how the complexity of the generated schemas affects interpretability and practical use? Are simpler schemas equally effective or is there a trade-off between complexity and performance?
-  Do you anticipate any challenges in integrating ELF with existing vision systems in industry settings? What adjustments or considerations would be necessary to adapt ELF for these scenarios?
- How critical is the initial set of schemas generated by GPT-4 on the overall results? Would the use of a different LLM or a smaller language model significantly impact ELF's effectiveness?

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
4

### Summary
This paper presents a method, ELF, to leverage LLMs for mid-vision feedback. The method consists of the automatic production of schemas with GPT-4 and evolutionary search, injecting feedback from these schemas into the middle of a vision network, and producing higher-performing classification networks. The authors report results on a small ResNet, ShuffleNet, MobileNet, and ViT, and analyze performance across LLMs and contexts applied.

### Strengths
S1. The method is straightforward and delivers clear boosts in performance. The authors show that MVF with schemas from LLMs has promise for vision tasks, and present evidence across models along with an LLM ablation.

S2. The writing is efficient and concise. Though there is room for improvement in clarity (see below), the authors write with no “fluff” and describe their methods in a straightforward way.

### Weaknesses
W1. The writing in this paper is a bit hard to follow, especially the abstract, introduction, and figures. 
- The abstract could use some more context in general, especially for some terms (like what a “schema” and “visual learning” is in this context). I can vaguely understand the method being used from reading the abstract (glossing over what an e.g., “semantic program” is), but the actual task being solved is unclear to me. I may just be unfamiliar with this specific subfield of work and common terminology, but in the computer vision space at least, other readers may appreciate a clearer abstract with less unfamiliar jargon.
- The introduction provides some useful information especially in terms of biological motivation, but the problem being solved and the goal task is still unclear. What gap is this method actually addressing?
- Some of the figures are quite confusing to follow, for example:
  - Figure 3. It’s unclear where a reader should start and what path they should follow. Additionally, the function of each arrow is confusing (e.g., what is the output of the evolutionary search and how is it integrated into the other modules it is pointing to?). These details don’t need to be written explicitly in this figure and crowd it if the depiction itself is more straightforward.

W2. The technical implementation of Figure 5 is entirely unclear. How are the contexts extracted from model features, and where do the parameters of the affine transformation come from? How can we be certain that the transformations are being applied to feature projections that cleanly correspond to a single context?

W3. This paper needs more ablations and analyses, including:
- This method seems to require many forward passes per inference, implying an accuracy-efficiency tradeoff. There is no analysis of how the efficiency (commonly measured in FLOPs) scales in training or inference.
- Studying which layer (or combination of layers) responds best when injected with feedback. Is it true that adding feedback to the layers corresponding to “mid-level visual processing” results in the best performance?
- Experiments on larger, more modern models. Consistent boosts across larger CNNs, ConvNeXt models, more ViT sizes, and pre-trained ViTs would provide a more compelling argument for ELF.

### Questions
Q1. What is the exact prompt fed into GPT? Pretrained LLMs will know about datasets like CIFAR-10 or ImageNet, so depending on how they are prompted they may recognize the first schema as a collection of CIFAR-10 categories and thus be biased to generate schemas “well-aligned” to the use case. While this can help accuracy in your experiments, the problem is that unfamiliar datasets (e.g., a new satellite image dataset) may not lead to the same boost because GPT will not provide as helpful of schemas.

Q2. Image classification, especially on CIFAR-10 or ImageNet, is a task whose performance is largely saturated by well-trained models these days (like DINOv2, for example). How does this method help for more challenging classification tasks like fine-grained classification, nonstandard domains, or even tasks outside of classification?

Q3. Were these models trained from scratch or fine-tuned?

Apologies if there are some weaknesses in the questions section and vice versa; they tend to blend together when pointing out missing analyses. 

Overall, I find this paper to be decently-written and on a good path to be published in the near future. However, there is more work to be done on both the experiment and presentation side to provide a compelling case for ELF in the vision community, and I hope that the authors can take this review as helpful and encouraging feedback to strengthen their paper.

### Soundness
4

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
4

### Summary
In this work, the authors propose ELF (Evolving LLM-Based Schemas for Mid-Vision Feedback), which combines schema evolution with Mid Vision Feedback (MVF). Based on the method of EvoPrompt, the authors utilize the large language model (LLM) as the crossover and mutation operator in the evolutionary algorithm to find a good context split paradigm in Mid-Vision Feedback through the evolutionary algorithm. Finally, the authors conduct experiments on multiple models and data, and give quantitative results, showing the superiority of the overall scheme (ELF) compared with the baseline in the general sense of image classification.

### Strengths
1. This paper searches for the optimal schema in Mid Vision Feedback (MVF) through the EvoPrompt method, providing inspiration for the expanded use of EvoPrompt.

### Weaknesses
1. The paper combines EvoPrompt and Mid Vision Feedback (MVF), but does not explain the principles and detailed processes of the two in the intrduction or related work section. In addition, the method section is a bit casual, without strict mathematical definitions and rigorous process expressions, making the method not specific and clear enough.
2. The paper does not have sufficient experimental demonstration of the contribution points. There is only an experimental comparison between ELF (the author's method) and the baseline without Mid Vision Feedback (MVF), but no comparison with the image classification result of Mid Vision Feedback (MVF). This does not prove that the schema searched by ELF (the author's method) is better than the schema in Mid Vision Feedback (MVF).
3. The description of the experimental section is not rigorous enough (potentially, it may lead to an imprecise experimental setting). For example, in the comparison of Stage1 and ELF in Table 1, the total training generations of the two do not seem to be consistent. Whether Stage1 has reached sufficient convergence may need to be explained. In lines #346-347, the author mentions using a 32x32 input size neural network for CIFAR100 experiments, but in lines #383-384, the experiment continues on ImageNet, switching to a larger ViT-B/16 and ResNet50, and the resolution setting is not explained at this time.
4. The analysis in the experimental part is not sufficient. The authors can show the difference between the schema optimized by EvoPrompt and the original schema (and MVF), and  explain clearly and more deeply the growth points brought by using EvoPrompt to optimize the schema.

### Questions
The writing of the paper needs to be polished, and the format of the paper needs to be improved. For example, the layout of Figure 2 and Figure 3, the pictures and the text should maintain a top-to-bottom relationship. In addition, in Tables 1 and 2, it is not standardized to put the comparison values ​​between different methods in the same column as the methods.

### Soundness
2

### Presentation
2

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
The paper proposes a visual learning framework based on mid-vision feedback (MVF) with schema evolution from LLM. The contributions include proposing a new approach to automatically generating the schemas for classes and applying these schemas for image classification with MVF. The experiments also demonstrate that training with the schemas for classification can improve the model performance on CIFAR-100, ImageNet, and Caltech101.

### Strengths
1. The idea of using MVF with LLM for generating class schema can be interesting for presenting more accurate ontology for each class instead of obtaining from the rouge output from LLM.

### Weaknesses
1. The approach for MVF is hard to follow. Some terms used to define MVF and how to apply it are unclear. For instance, "affine transformation" has often appeared in the paper and should be an important part of applying MVF. However, "affine transformation'" is not clearly defined, making the paper hard to read. Similarly, how the context output from the MVF can be used with the schema should provide more explanation. A recommendation would be adding a small subsection at the beginning of Sec. 3  for introducing how to apply MVF in more detail by defining the terminologies, such as how MVF is trained and also what affine transformation is, and also providing some math formulas for this operation.
2. Some format issues are found. The title for Sec. 2.1 is broken into two lines. Fig. 4 seems to have too many white spaces, and some of the words are not big enough. Making the figure concise by reordering each step and enlarging the word within the block can increase its readability. Some references to the tables do not exist. For instance, Tab. 4.1 is not seen in the paper. Many cited papers have already been accepted by conferences, but the citation is given in the non-updated version.  For instance, the paper from Sachit Menon and Carl Vondrick has been accepted by ICLR23, but the citation has not been updated. Additionally, the conference name is not consistent. For instance, some are written in "In Proceedings of the IEEE conference on computer vision and pattern recognition" and some are written in "In 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)"
3. No explicit schema examples are provided. One of the contributions of this paper is the generation of schemas. However, no demonstration of schemas is found in the paper. Providing some schemas in Sec. 3 or 4 can help readers know more about the ability of this approach. These schemas can be like an image-text pair to show the founding schemas for a specific image.
4. The proposed is simply the combination of MVF and EvoPrompt. No new or dedicated designs are made to combine or apply these two approaches. More clarification for the novelty should be addressed. For instance, discussing why the approach is non-trivial or why the direct combination is optimal.

### Questions
1. In Sec. 4, the authors state that the ablation for schemas will be given, but no related sections are found. Is this presented in Sec. 5 and Fig. 6? 
2. The models selected as the MVF backbone are not the SOTA ones. Why do the authors adopt these models as the baseline? Can this approach be applied to the current SOTA to enhance performance further?

### Soundness
3

### Presentation
2

### Contribution
2
