# Ranking-aware adapter for text-driven image ordering with CLIP

- Decision: Accept
- Avg Score: 6.25
- Scores: 3, 8, 6, 8

## Abstract
Recent advances in vision-language models (VLMs) have made significant progress in downstream tasks that require quantitative concepts such as facial age estimation and image quality assessment, enabling VLMs to explore applications like image ranking and retrieval.
However, existing studies typically focus on the reasoning based on a single image and heavily depend on text prompting, limiting their ability to learn comprehensive understanding from multiple images.
To address this, we propose an effective yet efficient approach that reframes the CLIP model into a learning-to-rank task and introduces a lightweight adapter to augment CLIP for text-guided image ranking.
Specifically, our approach incorporates learnable prompts to adapt to new instructions for ranking purposes and an auxiliary branch with ranking-aware attention, leveraging text-conditioned visual differences for additional supervision in image ranking.
Our ranking-aware adapter consistently outperforms fine-tuned CLIPs on various tasks and achieves competitive results compared to state-of-the-art models designed for specific tasks like facial age estimation and image quality assessment.
Overall, our approach primarily focuses on ranking images with a single instruction, which provides a natural and generalized way of learning from visual differences across images, bypassing the need for extensive text prompts tailored to individual tasks

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper introduces a **Ranking-Aware Adapter for Text-Driven Image Ordering with CLIP**, designed to enhance CLIP’s capability in text-guided image ranking. Key points include:

1. **Objective**: The method reframes CLIP into a learning-to-rank (LTR) task, using a lightweight adapter to improve ranking tasks across image attributes (e.g., facial age, object count, image quality).

2. **Ranking Adapter Design**: The adapter consists of:
   - **Learnable Prompts** for adapting CLIP to new ranking instructions.
   - **Auxiliary Ranking Branch** that uses ranking-aware attention to focus on text-conditioned visual differences.
   - **Two Parallel Heads** for regression (individual image ranking score) and pairwise ranking supervision (to capture relative differences across images).

3. **Performance**: The adapter consistently outperforms fine-tuned CLIP on tasks such as facial age estimation, image dating, image quality assessment, and object count sorting.

4. **Evaluation and Ablation Studies**: The model is validated on multiple benchmarks, showing improved ranking accuracy, particularly as dataset complexity grows. Ablation studies highlight the contributions of each component, confirming the benefit of ranking-aware attention for pairwise comparisons.

This method enhances CLIP’s ability to rank images without exhaustive task-specific tuning, aiming to generalize across ranking tasks. Let me know if you'd like to dive into specific aspects like strengths, weaknesses, or contributions.

### Strengths
- *Generalizable Across Ranking Tasks*: The ranking-aware adapter is designed to handle multiple text-driven ranking tasks (e.g., age estimation, object counting, image quality assessment) without requiring extensive task-specific tuning. This flexibility suggests that the approach could generalize across diverse ranking applications, potentially making it adaptable for other vision-language tasks where relative comparisons matter.

- *Improved Performance on Benchmarks*: the proposed method improves performance on tasks like object count sorting, facial age estimation, and image aesthetics assessment, which could indicate its effectiveness in capturing ranking relationships across different domains.

### Weaknesses
 - **Clarity and Reproducibility Issues**: The paper is challenging to follow, with several instances where the context is unclear, and symbols (e.g., Eq(5) and ΔO) are introduced without proper explanation. This lack of clarity makes it difficult to fully understand the method and poses challenges for reproducing the results. In particular, additional context is recommended regarding:
   - The specific role and application of the ranking score across different tasks.
   - Which of the two heads (regression or ranking) produces the final output, especially for each individual task.
   - How MAE is computed in experiments like facial age estimation and image dating, given that the model primarily performs ranking rather than explicit regression or classification.
   - What exactly is being ranked in each experiment, as this varies by task and isn’t sufficiently explained.

- **Ambiguity in Terminology and Methodology**: The claim that the paper “reframes the CLIP model into a learning-to-rank task” is ambiguous and could be misleading. A model cannot be reframed into a task; it can be adapted or extended to handle a task. In my understanding, the approach here is simply to add an adapter on top of the existing CLIP model, with CLIP’s image and text encoders used as frozen feature extractors. The authors are encouraged to clarify what they aim to achieve in reframing CLIP for ranking and to describe more precisely how this method differs from other approaches to ranking with CLIP features.

- The core mechanism for capturing differential information between image pairs, as implemented in Eq. (1)-(3), appears questionable. Specifically, the attention mechanism in Eq. (1) normalizes across tokens from both images, but the resulting submatrices $A_i$ and $A_j$ used to compute $O_i$ and $O_j$ are not individually normalized. This raises concerns about whether $O_i$ and $O_j$ can be considered valid attention-weighted combinations, and whether their difference $O_{i,j} = O_i - O_j$ effectively captures differential properties. In cases where one of the attention submatrices, say $A_j$, is close to zero, $O_{i,j}$ would primarily reflect information from $O_i$, failing to capture the intended relative differences. Furthermore, the experimental results showing that normalizing $A_i$ and $A_j$ makes no significant difference, along with the marginal impact of replacing subtraction with concatenation (Table 6, row 2), challenge the importance of the differential information mechanism. It is also unclear whether using $O_i + O_j$ would change results, further undermining the claimed importance of the subtraction operation.

- The updated Eq. (3) introduces a significant change in the method's implementation by averaging the difference of $O_i$ and $O_j$ over $M$ relational tokens and passing it through a feed-forward network. This is a departure from the original description where $O_{i,j}$ was simply the difference of $O_i$ and $O_j$. It is unclear whether the reported results correspond to the original or updated formulation, which makes it difficult to evaluate the validity of the findings. The lack of a code implementation further exacerbates this issue, hindering reproducibility and transparency.

### Questions
Please see the weaknesses section on questions.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an efficient approach to enhance the CLIP model for image ranking tasks by reframing it as a learning-to-rank problem. It introduces a lightweight adapter with learnable prompts and a ranking-aware attention branch to leverage text-conditioned visual differences. This method consistently outperforms fine-tuned CLIP models across various tasks, achieving competitive results in facial age estimation and image quality assessment. By focusing on image ranking with a single instruction, the approach offers a generalized way to learn from visual differences without relying heavily on extensive text prompts.

### Strengths
1. The writing is clear and well-structured, making the content easy to follow. The logical flow helps readers grasp the key concepts without difficulty.

2. The motivation behind the study is explained exceptionally well. It highlights that existing research often centers on reasoning from a single image and relies heavily on text prompts. This approach restricts the ability to achieve a comprehensive understanding when multiple images are involved. By addressing these limitations, the study aims to enhance multi-image reasoning capabilities.

3. The method diagram is presented with clarity, making it easy for readers to comprehend the proposed approach. This visual aid effectively supports the explanation of complex processes, ensuring that the methodology is accessible to a broad audience.

4. The experimental results show impressive performance across several datasets. This demonstrates the robustness and effectiveness of the proposed methods, indicating their potential for broader application in various contexts.

### Weaknesses
1. Comparison with Existing Methods: There is a need to clearly delineate the core differences between OrdinalCLIP, L2RCLIP, and NumCLIP compared to existing methods, which might not be fully addressed. Specifically, the paper should elaborate on how the proposed method's approach to learning visual differences through a ranking-aware attention mechanism differs from the direct alignment of images with numerical values used in these prior works. A more detailed explanation of the architectural and functional distinctions is needed to fully appreciate the novelty of the proposed approach.

2. State-of-the-Art Comparisons: The article does not adequately compare the proposed models to state-of-the-art multi-modal large language models (LLMs), which could provide a more comprehensive evaluation of their performance. The lack of comparison with models like InstructBLIP or similar architectures limits the ability to benchmark the proposed method against current leading approaches in the field. This comparison is crucial to understand the relative strengths and weaknesses of the proposed method in a broader context.

3. Performance on Complex Benchmarks: The performance on complex counting benchmarks like TallyQA and CLEVR is not thoroughly evaluated, leaving questions about the models' capabilities in more challenging scenarios. While the paper shows results on simpler counting tasks, the absence of evaluation on more complex benchmarks, which require a deeper understanding of relationships and attributes, makes it difficult to assess the generalizability of the proposed method to more intricate visual reasoning tasks.

### Questions
1. The paper utilizes CLIP with ConvNeXt-L, which differs from the backbone networks in existing methods. Does this affect the fairness of experimental comparisons?

2. Does the model require separate adapter networks for different tasks, and how might this impact its generalization to unseen scenarios?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a modified CLIP model for text-guided image ranking, using a lightweight adapter with ranking-aware attention to enhance understanding of visual differences across multiple images. By incorporating learnable prompts for ranking instructions, the approach reduces dependence on extensive text prompting. The method outperforms fine-tuned CLIP on various tasks and rivals specialized models in areas like facial age estimation and image quality assessment.

### Strengths
1. The motivation is clear: while previous methods require generating multiple captions for input images, this approach only needs a single rank-related text prompt.
2. The proposed ranking-aware adapter achieves superior performance over fine-tuned CLIP and is competitive with specialized models for tasks like facial age estimation and image quality assessment, offering a versatile solution for text-guided image ranking.

### Weaknesses
1. Although the motivation of this paper is clear, the technical contribution does not appear strong enough from my perspective. I will wait to see other reviewers’ comments on this aspect.
2. In Equation (2), the symbols $V_i$ and $V_j$ are not explained. Adding the shapes or dimensions of certain symbols in Equation (2) would enhance clarity.
3. Regarding the experiments: why does ranking-aware attention utilize three MLP blocks?

Minor Issues:
- Consider adding count numbers to the results in Figures 5 and 6 for clarity, as done in Figure 7(a).
- The citation format in Lines 417, 309, 160, and 161 appears inconsistent. I suggest the authors review the full paper and adjust citation formatting for consistency with Line 424 if needed.
- The symbols between Figure 3 and the main text are inconsistent. For example, the symbol for relation tokens is $\mathbf{q}$ in Figures 2 and 3 but $q$ in Equation (1).
- Some symbols in Figure 3 are unclear. $A_i$ is a matrix, but $P$ represents dimension. What does $A_i(1-P)$ signify?
- The column margins in Tables 1 and 2 are too wide, causing the tables to appear cramped together, and the right edge of the table extends beyond the page, which affects visual appeal.

### Questions
- Are the weights of the relational ranking-aware attention also frozen? If they are trainable, a trainable symbol should be indicated in Figure 2.
- How does the relational ranking-aware attention handle multiple images (i.e., more than two)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a light-weight rank adapter which allows using an existing pre-trained CLIP model for any ranking task. The authors propose using learnable text prompts along with a light-weight cross-attention based ranking module which can measure visual differences between pairs of images. This approach is much simpler than some of the preceding works as it is able to be trained for the learning-to-rank task using a single text prompt such as "sort by number of [category]" compared to some of the prior works which would try to use multiple text prompts followed by contrastive learning to teach CLIP how to rank. Their solution is intuitive, elegant and can be readily adapted to any existing CLIP type framework without the need of fine-tuning the CLIP encoders. They show SoTA performance on a variety of learning-to-rank tasks such as facial age estimation, colored image dating, object counting etc. They also validate all their design choices in the ranking module with ablations and show abundant qualitative examples of their method. The appendix also covers interesting future directions such as ranking based on multiple attributes and analyzing how the transferability of ranking works across domains. Overall I think the paper is quite well written and provides a very elegant solution to the learning to rank problem and is well substantiated with experiments and ablations.

### Strengths
1) The paper is very well written and it is clear to understand the method section. The idea of replacing multiple rank specific prompts in prior work with a single 'sort by x' is simple and well motivated and simplifies the architecture quite a bit. The use of cross-attention in both the ranking adapter and the auxiliary ranking module makes intuitive sense to obtain text-conditioned image features and to get "pairwise image" differences respectively. 
2) The experimental section is well detailed and results are shown on a variety of different benchmarks for ranking. The appendix also covers more examples of tasks. The ablation section also validates the design choices for the ranking modules quite well. Overall the results are impressive beating all existing methods on a wide range of tasks. 
3) The method proposed is light-weight as it does not require fine-tuning of CLIP encoders and only of the ranking modules and all the experiments were run on a single 3090Ti GPU, which is impressive. 
4) The paper discusses abundant qualitative examples across the different benchmarks and also discusses interesting future directions such as ranking across multiple attributes and the generalizability of ranking across benchmarks.

### Weaknesses
1) The paper only shows results on a single image backbone in the CLIP architecture (ConvNeXt-L). Also, it resizes images to 320X320 whereas most of the prior work (LR-CLIP, Ordinal-CLIP, NumCLIP) uses an image size of 224X224 and they use the ViTB/16 image encoder. It would be good to show results with this setting as it will ensure a fair comparison with prior baselines and it will also provide some insight into the generalizability of the ranking modules across different architecture types. 
2) The paper only shows results with the pairwise ranking loss. It might be interesting to look at how the results vary by using other losses like triplet loss or the ranked list loss as presented by Wang et al (2021). Using a ranked list loss might also allow to not use the auxiliary ranking module which computes the pairwise attention matrix for the image features.

### Questions
1) Have you tried any experiments in ranking images by the number of objects in general, irrespective of the category of objects? For example just sorting on the "number" of whatever object is present in the image. That might help gauge how well the architecture is able to abstract out the "count" of objects.

### Soundness
4

### Presentation
4

### Contribution
4
