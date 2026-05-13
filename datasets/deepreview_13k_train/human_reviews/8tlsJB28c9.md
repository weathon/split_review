# M2Edit: Locate and Edit Multi-Granularity Knowledge in Multimodal Large Language Model

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Multimodal knowledge editing is an important method for modifying outdated or incorrect knowledge in Multimodal Large Language Models (MLLMs). However, existing datasets for multimodal knowledge editing lack multi-granularity knowledge. In this paper, we present a more realistic dataset called M2Edit, which includes three distinct types of knowledge: entity, relation, and action. Additionally, existing knowledge editing methods for MLLMs lack the ability to handle multi-granularity knowledge and generalize to multimodal data. To address these limitations, we propose the multimodal knowledge editing method MLE. This approach identifies key knowledge layers within different components and collaboratively edits the various components of MLLMs. As a result, we observe significant improvements in visual generality performance, ranging from 4.8 to 10.8, and achieve the best overall performance on knowledge data of different granularities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper works on multimodal knowledge editing.
It introduces a new dataset for this task, M2Edit (Multi-Granularity Multimodal knowledge Editing dataset). This dataset incorporates multi-granularity knowledge (relation, entity, and action) to address the limitations of existing multimodal knowledge editing datasets.
Moreover, the paper proposes a multimodal knowledge editing method, MLE (Multimodal Location-based Editing).
It identifies key knowledge layers within different components of MLLMs and collaboratively edits them to improve the model's performance on multimodal data. The method demonstrates significant improvements in visual generality performance and performs well in terms of different knowledge granularities.

### Strengths
1. The paper is overall clear and well-organized.
2. The paper proposes a useful dataset M2Edit including multi-granularity knowledge. This addresses the limitations of previous multimodal knowledge editing datasets.
3. The proposed method MLE can edit multi-granularity knowledge within MLLMs.
4. The report experiments verify the performance of MLE.

### Weaknesses
1. The paper ignores the discussion on the complexity of the MLE method.
2. The paper currently has limited analysis of error cases. Adding this could inspire further research work.
3. The uploaded material doesn't include the code, only the used dataset.
4. The paper doesn't mention how many samples the method edits at once, so it seems the paper does not report the results of batch editing.
5. The introduced dataset M2Edit seems to include counterfactual knowledge. How does the MLE perform with real-world knowledge as in [1,2]?

### Questions
1. Line 483, To address --> to address
2. It is hard to recognize the sentences with the striped background in Figure 2.
3. Can you provide some analysis of error cases?
4. The supplementary material only contains the M2Edit dataset. What about the code of MLE?
5. The paper should explain how the various metrics are computed.
6. How many samples do you edit at once? What is the performance of MLE when editing with several samples?

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
2

### Summary
The paper introduces M2Edit, a dataset with entity, relation, and action knowledge types, designed for multimodal large language models (MLLMs). It highlights the challenge of knowledge editing across different granularities within MLLMs and proposes the MLE (Multimodal Location-based Editing) method to tackle this. MLE sequentially identifies and edits key knowledge layers within MLLMs, enhancing generality and effectiveness in multimodal contexts. The model demonstrates improved accuracy and generalization over previous methods.

### Strengths
- Innovative multi-granularity approach in knowledge editing for MLLMs, addressing a gap in existing datasets.
- The MLE method shows significant performance improvements, particularly in visual generality and model adaptability.
- Offers detailed methodology for locating and editing specific knowledge layers within MLLMs, aiding model interpretability.

### Weaknesses
The proposed method is evaluated on a limited range of multimodal models, which restricts the generalizability of the findings across other MLLMs with different architectures or training objectives. Specifically, the recent VL models like QwenVL2, Llava should be evaluated.

### Questions
No

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper explores advanced techniques in knowledge editing for multimodal large language models (MLLMs). 
The authors introduce M2Edit, a dataset to enhance multimodal knowledge editing by incorporating multi-granularity knowledge types—entities, relations, and actions. 
They highlight the limitations of existing methods and datasets in addressing multi-granularity and multimodal challenges. 
The paper proposes a method, MLE (Multimodal Location-based Editing), which improves knowledge editing by identifying and modifying key knowledge layers across the various components of MLLMs. 
Experiments show that the method improves visual generality performance and achieves superior results on multi-granularity knowledge compared to existing benchmarks.

### Strengths
- The reviewer finds the authors' motivation for considering multi-granularity in knowledge editing to be interesting, which aligns with intuitive understanding of the subject.
- The dataset contributed by the authors (if executed flawlessly) could potentially be a significant asset to the field of multimodal knowledge editing.
- The method introduced by the authors outperforms the baseline.

### Weaknesses
The paper's primary issue appears to be the unclear expression and presentation of content, with so many details lost, making it difficult for the reviewer to understand the whole story fully. Furthermore, significant potential issues have been identified within the dataset section.

- The reviewer questions the setting of multimodal knowledge editing as posited by the authors, perceiving that it remains limited to textual LLM thinking. Notably, the M2Edit only edits the textual part of image-text pairs, which implies no equivalent editing for visual knowledge, thereby not affecting the image component. If the entire multimodal knowledge editing topic is defined in this manner, the reviewer questions the scientific validity of this definition and suggests that a fundamental improvement is necessary. The reviewer suggests that the authors further clarify this point in their discussion.
- While the paper mentions relational type knowledge in a triplet format, the examples shown in Figures 1 and 2 do not represent triplets but rather entity-level knowledge. The manifestation of relation-level knowledge editing remains unclear. The reviewer recommends that the authors revise and clarify this point clearly in the text.
- The dataset claims the importance of three levels of knowledge but does not integrate these levels within a single scope; different levels of annotations cannot coexist within the same instance, which likely limits the dataset's utility. Therefore, the reviewer hopes that the authors can further explain and clarify this matter.
- The data annotation process is not clearly articulated, raising concerns about the control over data quality, especially as it relies entirely on an automated process via ChatGPT, which is prone to introducing noise. Please provide a detailed description of this step in the manuscript.
- Figure 2 is really challenging to understand; it is unclear what the multiple lines of text within circles represent. Please provide further details.
- Similarly, Figure 3 is also difficult to decipher; the meanings of various arrows and shapes within the figure are not explained, and the significance of the different rectangles in the bottom-left box and what r, s, t represent are not clarified. Please provide additional information.
- In the methods section, the authors claim that to address the limitations of existing knowledge editing methods—which cannot handle multi-granularity knowledge and lack generalization on multimodal data—they propose a method called MLE (Multimodal Location-based Editing). However, the reviewer does not understand the causal relationship between the existing methods' inability to handle multi-granularity knowledge and the proposed "Locate Then Edit" approach. Is it necessary for multi-granularity knowledge editing to be implemented specifically through a "Locate Then Edit" method?
- The methods were only validated using older MLLMs like BLIP2-OPT and MiniGPT4, which may not represent the most advanced MLLMs, thus not sufficiently proving the effectiveness and generality of the proposed multimodal knowledge editing methods. The reviewer suggests adding more MLLMs for experimental comparison.
- The experimental analysis conducted by the authors lacks sufficient depth and breadth. The reviewer strongly recommends enhancing the content of the experimental analysis.
- The absence of any anonymous links for accessing model code and data examples impedes the reviewer's ability to further investigate and address the issues raised, casting doubts on the reproducibility of the research. Will the authors consider open-sourcing the code and resources?



Overall, the writing and expression in the paper are overly casual and lack the refinement expected in scholarly communication.

- There is a grammatical error on page three, line 112.
- All images in the paper are non-vectorial.
- The citation format throughout the paper does not adhere to standard academic norms.
- There are numerous detail-oriented issues, such as inconsistent punctuation in equations—some equations end with a comma or period while others do not, creating a disorganized appearance.

### Questions
The paper contains quite many aspects that are not clearly explained, making it challenging for the reviewer to understand. Below are some questions that need addressing:


- The term "in-scope" mentioned in Figure 2 and its caption is ambiguous; does it refer to "in-domain"?
- The caption in Figure 2 states, "After editing the MLLMs, the in-scope samples need to be generalizable, and the out-of-scope samples should not be unchanged", but this statement is confusing and lacks clarity.
- The head entity "Arcadia" mentioned on page four, line 177, is not visible in the middle part of Figure 2, making the reviewer confused about its inclusion and relevance.
- Beyond BLIP2-OPT and MiniGPT4, how does the proposed method perform on other state-of-the-art MLLMs?

### Soundness
2

### Presentation
1

### Contribution
2
