# InstructBrush: Learning Attention-based Visual Instruction for Image Editing

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Diffusion-based image editing methods have garnered significant attention in image editing. However, despite encompassing a wide range of editing priors, these methods are helpless when handling editing tasks that are challenging for users to accurately describe. We propose InstructBrush, an inversion method for instruction-based image editing methods to bridge this gap. It extracts editing effects from example image pairs as editing instructions to guide the editing of new images. Two key techniques are introduced into InstructBrush, Attention-based Instruction Optimization and Transformation-oriented Instruction Initialization, to address the limitations of the previous method in terms of inversion effects and instruction generalization. To explore the ability of visual prompt editing methods to guide image editing in open scenarios, we establish a Transformation-Oriented Paired Benchmark (TOP-Bench). Quantitatively and qualitatively, our approach achieves superior performance in editing and is more semantically consistent with the target editing effects. The code and benchmark will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies visual prompting for image editing settings, in which the edit is given by a {before, after} pair. Building upon existing works, this paper aims to improve current approaches by adding more detail and precision to the editing (e.g., fine-grained details, localization). To that end, a novel framework called InstructBrush is introduced, which includes Attention-based Instruction Optimization and Transformation-oriented Instruction Initialization. Quantitative and qualitative results indicate the effectiveness of the proposed framework.

### Strengths
- This paper is among the first works focusing on more fine-grained details in visual prompting for image editing. Most existing works focus on learning the "global" edit from a given {before, after} pair (e.g., turning a photo into a watercolor style), which often fails to capture fine-grained details (e.g., editing only the color of the water in a cup).
- While "attention manipulation" for image editing is not new, using this technique in "visual prompting" is novel and interesting.
- The experiments section is extensive and results are convincing.

### Weaknesses
Please make sure to attribute the correct papers. There are some formulas in the manuscript that do not seem to be correctly attributed to the original papers. For example, in line 760, I believe this formula was proposed or partially proposed in [1, 2, 3, etc.].

### Questions
Generally, I am inclined to accept this paper. At this time, I do not have any major concerns regarding its technical aspects or novelty. My only concerns are related to attribution to previous works, as there are instances where it may come across as overclaiming. I'd rate this paper 6.5-7, but unfortunately this there is no 7 option in the rating.

### Soundness
3

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
3

### Summary
This paper addresses the challenge of edits that are difficult to describe through user input alone. To address this, it introduces the InstructBrush method, which includes techniques such as Attention-based Instruction Optimization and Transformation-oriented Instruction Initialization. Additionally, it presents an evaluation benchmark, TOP-Bench, to assess the method's performance. Quantitative results demonstrate a competitive performance.

### Strengths
The paper highlights an important observation that many practical edits are indeed challenging to articulate in natural language. In response, the authors introduce a benchmark for evaluating performance on this issue, and their quantitative results indicate strong performance.

### Weaknesses
The primary concern is that, although the paper aims to address the challenge of edits that are hard to describe in language, the authors still rely on converting image pairs into a descriptive template with a fixed vocabulary list. It would seem more logical to explore the direct relationship between image features and to encode these editing directions directly within the generation model. If transitioning these concepts into language is essential, then the focus should be on translating image differences into descriptive language. Existing editing methods appear sufficient for such language-based tasks.

Additionally, some of the qualitative results highlighted in the paper remain suboptimal, especially when compared to IP2P+GPT-4o.

### Questions
1. In line 281, the notation "CAP_x" is used but not previously defined. Is this intended to be "P_x"?
2. The Time-aware Instruction method does not appear effective in the Peach-Apple example in Figure 5. Could an ablation study on this be provided?
3. It would be beneficial to include an ablation study on the optimization of the initial m tokens compared to optimizing the full set of tokens.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper propose InstructBrush, an inversion-based method for instruction-driven image editing in diffusion models, addressing limitations in handling complex edits. By extracting editing effects from example image pairs, InstructBrush guides novel edits with Attention-based Instruction Optimization and Transformation-oriented Instruction Initialization to enhance inversion and generalization. The paper also introduces TOP-Bench, a benchmark for evaluating instruction-based editing in open scenarios. InstructBrush shows superior performance and semantic alignment in edits, with plans to release the code and benchmark upon acceptance

### Strengths
1. The proposed feature similarity-based unique phrase extraction is a simple yet novel approach. The results of the proposed method produce effectively edited images based on instructions.
2. The paper identifies limitations in the evaluation criteria used in conventional image editing and addresses these by proposing a new benchmark, TOP-Bench, to overcome such challenges.

### Weaknesses
1. One of the primary contributions, the attention-based instruction module, seems to be a relatively simple technique, without too much novel insight. The concept of using a learnable cross-attention module to optimize features in cross-attention space has previously been introduced[1]. Furthermore, the paper does not adequately address how this method improves upon existing techniques, particularly given the performance of IP2P+GPT-4 in certain cases. The paper needs to more clearly articulate the specific advantages of the proposed approach over existing methods.
2. The explanation of when the time-aware instruction is effective or ineffective seems insufficient. Additional details on this aspect would enhance clarity. Specifically, the paper lacks a detailed analysis of how the time-aware optimization impacts different types of edits, and under what conditions it provides a significant improvement versus when it might be unnecessary or even detrimental.
3. Adding more real-world image tests could improve the robustness of the results. Further comparative experiments with text-guided editing methods would also strengthen the analysis. The current experiments are limited in scope and do not fully demonstrate the method’s applicability to diverse and complex real-world scenarios. Additionally, the paper should provide a more thorough comparison with text-guided methods, highlighting the specific advantages and limitations of each approach.

### Questions
1. Ablation results regarding the degree of truncation would be insightful. To what extent does truncation impact the final results?
2. In certain cases, IP2P+GPT-4 appears to deliver superior results compared to other methods. Further insights into this comparison would be valuable.
3. If unique phrase extraction is conducted effectively, is it possible to sample images based on these conditions? It would be interesting to see how images generated from unique phrases align with actual concepts. If these generated images closely resemble the intended concepts, it would enhance the persuasiveness of the paper’s claims.

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
This paper emphasizes the extraction of editing concepts from exemplar image pairs and enhances the cross-attention layers of instruction-based editing diffusion models to achieve the desired image editing results.

### Strengths
- The paper introduces a novel approach for visual prompt editing and proposes a well-justified generation strategy.
- The proposed method yields more satisfactory results compared to other approaches on the given task.
- The writing is clear and easy to understand.

### Weaknesses
 - Input Constraint: A key issue is the requirement that the differences between the reference image pairs used for editing must not be too large. Since the model relies on Eq. 6 and Eq. 7 to extract differences at the pixel level, acquiring such image pairs is challenging. A possible way to obtain these pairs would be through text editing methods or the prompt-to-prompt approach. However, this makes the input conditions much more complex compared to simply providing text, significantly reducing the practicality of the proposed task design.

- Redundancy of Exemplar Image Pairs: The paper employs Unique Phrase Extraction to derive concepts from the image pairs and then uses the extracted textual features for editing. This raises questions about the necessity of using exemplar image pairs as input. If textual descriptions were provided directly, similar results could be achieved. The paper includes experiments with GPT-4v + IP2P, which demonstrate the effectiveness of this approach to some extent. However, I believe that slight modifications to GPT-4v + IP2P could achieve results similar to those proposed in the paper, deepening my concerns about the necessity of the method.

- Lack of Novelty: The Time-aware Instruction strategy used in the paper is too common, and the core idea resembles methods like recaptioning and null-text inversion. While the novelty issue is not as critical as the previous two concerns, it still raises doubts about the paper's originality.

### Questions
My main concerns are outlined in the Weaknesses section. While I acknowledge the authors' efforts in producing promising results, both the necessity of the task and the design of the method leave too many points that need improvement and discussion. Therefore, I believe the paper is not ready for publication.

### Soundness
2

### Presentation
3

### Contribution
2
