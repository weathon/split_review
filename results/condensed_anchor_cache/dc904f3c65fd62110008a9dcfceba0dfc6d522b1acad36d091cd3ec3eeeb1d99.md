- Decision: Reject
- Scores: 3, 3, 6

## Merged Review

### Summary
This paper studies visual-textual misalignment in text-to-image (T2I) generation, proposing a classification called Conceptual Blind Spots (CBS). The authors employ LLMs to identify problematic concept pairings and introduce a Mixture of Concept Experts (MoCE) framework to alleviate CBS during the diffusion model’s denoising stages. A new dataset of text prompts is collected for evaluation. Experiments compare against a standard Stable Diffusion baseline and report improved faithfulness.

### Strengths
- The paper collects a valuable benchmark / dataset of text prompts for evaluating text-to-image models. [R1, R2, R3]
- The idea of composing generation for each object in a specific order (using LLMs to determine the order) provides insights for future research. [R1]
- The conceptual blind spot problem is relevant and timely; several T2I models face this limitation. [R2]
- Evaluation and results look great. Human evaluation and qualitative analysis further strengthen the proposed framework. [R3 – this reviewer is substantially more positive (rating 6) than the other two (ratings 3 each), finding no major weaknesses. The other two reviewers have significant concerns about presentation and experimental setup.]

### Weaknesses
- **Presentation and clarity are poor across the paper.** Important terms such as “conceptual blind spots,” “concept pairs,” and “Socratic reasoning/questioning” are not clearly defined. [R1, R2, R3] The explanation of categories A, B, C (e.g., “In this category, one concept (A or B) demonstrates a dominant relationship, either with an underlying C or…”) is unclear – it is not specified whether A and B are always in the text prompt or C is inferred, and how this leads to misalignment. [R2] The methodology section is confusing: how is the proposed metric $D$ used during generation? Why is a binary search algorithm used? An algorithm table would help. [R1] Notations are wrong; for example, in the Background of Section 4, $I$ should not denote the input image. [R1] Some sections required multiple readings (reviewer 3). The number of test samples in the human evaluation section is not clearly stated. [R3] There is a disconnect between the abstract and the three key contributions in the introduction – the dataset is listed as a key contribution in the introduction but is not mentioned in the abstract. [R3]
- **Missing details on dataset construction.** The paper describes collecting 259 concept pairs initially, then 159 achieving a Level 5 rating after screening, but the process for deriving the categories and patterns in Table 1 is insufficiently detailed – are the categories exhaustive? What criteria distinguish between them? [R2] How does GPT help in identifying the concept pairs? What instructions or prompts were given? What were the guidelines for human researchers? [R2] The screening process and criteria for Level 5 rating are not clearly defined. [R2]
- **Experiment setting is problematic.** Only the standard Stable Diffusion model is used as baseline. No comparison is provided against related works mentioned in Section 2. [R1] The proposed metric $D$ is used both during generation (as a guidance signal) and for evaluation, which could create an unfair advantage for the proposed method. [R1]
- **Missing related works.** Several relevant citations are omitted, e.g., [1], [2], [3], [4] (specific references not listed in the reviews). [R1]
- **Lack of analysis of failure cases.** The paper does not discuss which types of prompts the MoCE framework gets right versus where it fails. [R3 – reviewer 3 raises this as a curiosity; no major weakness otherwise, but it is a missing analysis.]