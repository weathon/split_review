# DisEnvisioner: Disentangled and Enriched Visual Prompt for Customized Image Generation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-1mm}
In the realm of image generation, creating customized images from visual prompt with additional textual instruction emerges as a promising endeavor. However, existing methods, both tuning-based and tuning-free, struggle with interpreting the subject-essential attributes from the visual prompt. This leads to subject-irrelevant attributes infiltrating the generation process, ultimately compromising the personalization quality in both editability and ID preservation. In this paper, we present \textbf{DisEnvisioner}, a novel approach for effectively extracting and enriching the subject-essential features while filtering out -irrelevant information, enabling exceptional customization performance, in a \textbf{tuning-free} manner and using only \textbf{a single image}. Specifically, the feature of the subject and other irrelevant components are effectively separated into distinctive visual tokens, enabling a much more accurate customization. Aiming to further improving the ID consistency, we enrich the disentangled features, sculpting them into a more granular representation. Experiments demonstrate the superiority of our approach over existing methods in instruction response (editability), ID consistency, inference speed, and the overall image quality, highlighting the effectiveness and efficiency of DisEnvisioner.
Project page: \href{https://disenvisioner.io/}{\textcolor{blue}{\fontfamily{cmtt}\selectfont{disenvisioner.io}}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces DisEnvisioner, a method aimed at enhancing the customization capabilities of image diffusion models. The approach involves training two models: DisVisioner, which disentangles subject-specific features from subject-unrelated features, and EnVisioner, which enriches these disentangled features. Quantitative and qualitative experiments demonstrate that DisEnvisioner effectively extracts subject information while discarding unrelated details, significantly enhancing customization capabilities.

### Strengths
- The paper is well-written and easy to follow, with figures that clearly illustrate the concepts.
- The visual results are impressive, with the original subject details well-preserved.
- The topic is engaging and holds potential for practical application.

### Weaknesses
 - **Missing Ablations:** The importance of CLIP prior initialization and augmentation in training DisVisioner has not been fully investigated.
- **Unclear Mechanism for Ensuring Disentanglement:** While the concept of disentangling subject-specific and unrelated features is intriguing, the method section does not clearly explain how this disentanglement is achieved. It remains unclear what guarantees that only subject-related information is retained. Specifically, the method lacks a clear explanation of how the subject token is isolated from the background and other irrelevant details during training. The loss function used in the diffusion model applies to the entire image, making it unclear how the subject token learns to represent only subject-specific features. This raises concerns about the robustness of the disentanglement process and whether the subject token truly captures the intended information.

### Questions
- During the training of DisVisioner, how is disentanglement achieved? Given that the diffusion model’s objective imposes a loss on both the object and the background, it’s unclear how only subject information is learned for the subject token. Could the authors provide visualization examples or experiments of the learned disentangled tokens?
- What types of augmentations are used during DisVisioner’s training?
- Can this method be extended to use multiple images as conditioning to enhance reference image details?
- Since DisVisioner’s training requires the class name from ImageNet for prior initialization, does this limit its generalization to classes outside ImageNet?

### Soundness
3

### Presentation
3

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
The paper introduces DisEnvisioner, a novel approach aimed at enhancing image customization from visual prompts while addressing the limitations of existing methods in interpreting subject-essential attributes.Empirical evidence demonstrating the superiority of DisEnvisioner over existing methods in various aspects, including instruction response (editability), ID consistency, inference speed, and overall image quality.

### Strengths
The paper introduces DisEnvisioner, a novel framework that addresses significant challenges in customized image generation by focusing on feature disentanglement and enrichment. The originality lies in the identification of the crucial role that subject-essential attributes play in the customization process, which is a new viewpoint that goes beyond existing methods reliant on either tuning or tuning-free approaches.

The clarity of the paper is commendable. The authors present their arguments logically, making it easy for readers to follow their reasoning and understand the significance of their contributions. Key terminologies and concepts like "subject-essential attributes" and "feature disentanglement" are well-defined

### Weaknesses
1.The advancement of the methodology has not been sufficiently demonstrated; some indicators (e.g. image-alignment for ID-consistency (C-I, D-I) as shown in Table 1) are inferior to other similar methods (e.g., IP-Adapter, BLIP-Diffusion, etc.),you cloud provide more evidence to support your claim in abstract "Experiments demonstrate the superiority of our approach over existing methods in instruction response (editability), ID consistency,"

2.The EFFECT OF DISVISIONER has not been adequately explained; there is a lack of comparative experiments with and without DISVISIONER to validate its effectiveness. You cloud compare results with and without the DiVisioner component while keeping other parts of the system constant.

3.The EFFECT OF ENVISIONER has not been sufficiently substantiated; the paper's explanation regarding the EFFECT OF ENVISIONER only presents a few cases (as shown in Fig. 8), which lacks persuasiveness.You could provide a larger-scale comparison by human evaluation or image-alignment for ID-consistency (C-I, D-I) to measure the improvement in ID consistency or image quality.

4.Ablation on token’s numbers in DisVisioner lack of QUANTITATIVE result.You might measure performance across various metrics (like those in Table 1) for different token number configurations.

### Questions
1.Could you please explain how subject features and irrelevant features are learned, and why they can be disentangled by transformer blocks without additional supervision?

2.Please improve the quantitative comparison experiment regarding the EFFECT OF DISVISIONER (Ablation study).

3.Please improve the quantitative comparison experiment regarding the EFFECT OF ENVISIONER (Ablation study).

4.Please improve the quantitative comparison experiment on the Ablation of token numbers in DisVisioner, and supplement the comparison experiments for $n_s=1, n_i=0$ and $n_s=0, n_i=1$.

### Soundness
2

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
The paper, titled "DisEnvisioner: Disentangled and Enriched Visual Prompt for Customized Image Generation," presents a novel approach to generating customized images from visual prompts with additional textual descriptions. The main contributions are:

1. Proposing DisEnvisioner, a tuning-free framework that effectively disentangles subject-essential attributes from irrelevant features, improving the overall quality of customized image generation.

2. Introducing a two-stage architecture with DisVisioner to separate subject-essential and irrelevant features, and EnVisioner to enhance subject consistency.

3. Demonstrating through experiments that the proposed approach outperforms existing methods in terms of editability, identity (ID) consistency, and inference speed while requiring minimal fine-tuning or reference images.

### Strengths
Originality: The introduction of DisVisioner and EnVisioner for disentangled visual prompt processing is a novel approach, effectively addressing the challenge of maintaining subject identity while generating customized images.

Quality: The experiments are well-conducted, demonstrating the effectiveness of the proposed method in preserving ID consistency and reducing subject-irrelevant features.

Significance: The approach enables high-quality, customized image generation in a tuning-free manner, which is practical and efficient for real-world applications.

Clarity: The overall structure of the paper is well-organized, and the experimental results effectively showcase the advantages of the proposed method over existing baselines.

### Weaknesses
Limited Theoretical Justification: The paper lacks sufficient theoretical grounding for the proposed disentangling mechanism. For example, the method for separating subject-essential and irrelevant features relies primarily on empirical observations without rigorous theoretical backing. Specifically, the paper does not delve into the mathematical properties of the attention mechanism used for token separation, nor does it provide any formal analysis of how the orthogonal tokens achieve disentanglement. The lack of a theoretical framework makes it difficult to understand the limitations of the approach and how it might generalize to different types of visual prompts.

Comparison with Existing Methods: The paper does not provide extensive comparisons with some of the most recent advancements in text-to-image generation (e.g., Transformer-based approaches). Including a wider range of baselines would help position this work within the current state of the field. The current comparisons are limited to methods that do not fully represent the state-of-the-art in text-to-image generation, particularly those employing large-scale transformer architectures. A more comprehensive comparison would include methods that utilize attention mechanisms and large language models for image generation, which are now standard in the field.

### Questions
Could the authors provide more theoretical insights into the disentanglement mechanism and why it works well for customized image generation? The current explanation is mostly empirical.

How does DisEnvisioner compare to other recent Transformer-based text-to-image generation methods? Adding these comparisons could help readers better appreciate the novelty of the approach.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DisEnvisioner, a novel tuning-free method for generating customized images from a single visual prompt enriched with additional textual instructions. Existing image generation methods, both tuning-based and tuning-free, often struggle to isolate the essential attributes of a subject in the visual prompt, leading to unwanted, subject-irrelevant features that compromise customization quality, editability, and identity (ID) preservation. DisEnvisioner addresses this by disentangling the subject-essential features from irrelevant details, separating them into distinct visual tokens. This separation improves customization precision and allows for enhanced ID consistency. By further refining these disentangled features, DisEnvisioner creates a more granular representation of the subject, which bolsters the model's ability to maintain ID consistency across generations. Experimental results demonstrate that DisEnvisioner outperforms current methods in editability, ID consistency, inference speed, and overall image quality, establishing its effectiveness and efficiency for personalized image generation.

### Strengths
DisEnvisioner demonstrates several strengths over competing methods in the areas of customization quality, editability, identity consistency, and efficiency, as shown in the provided results:

Customization Quality (C-T): With a score of 0.315, DisEnvisioner shows the highest performance in customization (C-T), indicating that it excels at incorporating subject-specific details while staying true to the given instructions.

ID Consistency (D-I): DisEnvisioner scores 0.802 for ID consistency (D-I), surpassing most other methods except for IP-Adapter. This score reflects its ability to maintain subject identity throughout image generation, reducing unwanted attribute drift.

Instruction Response (C-I): DisEnvisioner scores 0.828, slightly lower than some methods like IP-Adapter and DreamBooth but still within a strong range. This indicates good responsiveness to textual instructions while retaining visual prompt characteristics.

Inference Speed (IV): DisEnvisioner achieves a lower inference value of 0.026, indicating faster inference compared to methods like DreamBooth and DisenBooth, making it efficient for real-time or rapid customization needs.

*Runtime (T)**: DisEnvisioner has a runtime of 1.96 seconds, placing it on par with IP-Adapter, which is one of the fastest. This efficient runtime makes it more practical for applications needing quick processing.

Mean Rank (mRank): With an mRank of 2.0, DisEnvisioner achieves the highest overall ranking among the methods tested, suggesting that it consistently performs well across different evaluation metrics.

### Weaknesses
DisEnvisioner, while showcasing significant advancements, has some limitations that temper its overall impact:

Lack of State-of-the-Art Results Across All Metrics: DisEnvisioner does not outperform all baseline models in every metric. For instance, its performance in instruction response (C-I) and identity consistency (D-I) does not reach the top scores achieved by IP-Adapter and DreamBooth. Specifically, while the paper claims superior editability, the lower C-I and D-I scores suggest a potential trade-off where the model might be prioritizing editability at the expense of accurately following instructions and maintaining strict identity consistency. This mixed performance limits DisEnvisioner’s claim to outright superiority across all customization aspects, indicating that while it excels in some areas, it is not universally superior.

Limited Test Dataset: The dataset used for evaluating DisEnvisioner is relatively constrained, potentially affecting the generalizability of the results. The DreamBooth dataset, while containing a variety of subjects, might not fully represent the breadth of real-world visual prompts. A more extensive and varied dataset, including more complex scenes, diverse object types, and different lighting conditions, would provide a clearer picture of the model's adaptability and robustness across diverse tasks and use cases. The current dataset might not be sufficient to fully validate the model's performance under diverse conditions.

Room for Improved Analysis on Underperformance Against IP-Adapter: Although DisEnvisioner demonstrates strengths in disentangling features, it would benefit from further analysis on why it lags behind IP-Adapter in specific tasks like instruction accuracy and ID consistency. The paper does not provide a detailed explanation of why the disentanglement strategy, which is a core contribution, does not translate to superior performance in these metrics compared to IP-Adapter. Understanding these discrepancies, such as whether the disentanglement process introduces some loss of information or if the feature enrichment is not fully optimized for these specific tasks, could inform targeted improvements to make DisEnvisioner more competitive in these areas.

### Questions
Question: Could the authors elaborate on the specific factors that led DisEnvisioner to underperform IP-Adapter in terms of instruction accuracy (C-I) and ID consistency (D-I)?

Suggestion: Analyzing and explaining these performance gaps would provide useful insights into DisEnvisioner's design choices. This could also help clarify if the approach is inherently less suited to certain customization aspects or if there are areas where further tuning could close the performance gap.

Question: Given the limited dataset, how confident are the authors in DisEnvisioner’s generalizability to a broader range of tasks and more diverse visual prompts?

Suggestion: Evaluating DisEnvisioner on additional datasets with varied visual content and textual instructions could better assess its robustness. Additional results on a larger dataset could substantiate the claims of effectiveness and versatility.

Question: How does the feature enrichment step improve ID consistency, and could the authors provide more details on its implementation?

Suggestion: Adding a more in-depth explanation of the enrichment process and its effect on ID consistency would be beneficial. Additionally, showing comparisons before and after this step could better demonstrate its impact on maintaining subject integrity.

### Soundness
3

### Presentation
3

### Contribution
3
