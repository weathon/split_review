# An Image is Worth Multiple Words: Learning Object Level Concepts using Multi-Concepts Prompts Learning

- Decision: Reject
- Scores: 3, 6, 8, 6

## Abstract
Textual Inversion, a prompt learning method, learns a singular text embedding for a new ``word'' to represent image style and appearance, allowing it to be integrated into natural language sentences to generate novel synthesised images. 
However, identifying multiple unknown object-level concepts within one scene remains a complex challenge.
While recent methods have resorted to cropping or masking individual images to learn multiple concepts, these techniques require image annotations which can be scarce or unavailable.
To address this challenge, we introduce \textit{Multi-Concept Prompt Learning (MCPL)}, where multiple unknown ``words'' are simultaneously learned from a single sentence-image pair, without any imagery annotations. 
To enhance the accuracy of word-concept correlation and refine attention mask boundaries, we propose three regularisation techniques: 
\textit{Attention Masking}, \textit{Prompts Contrastive Loss}, and \textit{Bind Adjective}.
Extensive quantitative comparisons with both real-world categories and biomedical images demonstrate that our method can learn new semantically disentangled concepts. 
Our approach emphasises learning solely from textual embeddings, using less than 10\% of the storage space compared to others.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method to associate new words into concepts. The proposes three techniques: attention masking, prompts contrastive loss, and bind adjective. The applications they adopted is the image synthesis / editing when replacing some of the original concepts in a sentence, with a different concept (i.e. image editing over disentangled concepts). They also claim to introduce a novel dataset for this application.

### Strengths
- They claimed to release code and dataset upon publication.
 - The paper targets important research areas.

### Weaknesses
 - The paper is not very clear to read. The idea seems to be straightforward, but the description of the method is a bit ambiguous. I have to read multiple times to make sure I understand the method accurately.
 - In experiments, the authors show multiple interesting qualitative results. However, there are very little quantitative results, and it is very hard to compare with other methods and understand the contribution of this effort.

### Questions
Attention masks and contrastive loss on different concepts seems to be a widely used method. It would be great if the authors can explain a bit more about the novelty of their work.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a Multi-Concept Prompt Learning (MCPL) method that extracts multiple prompts from single images under the stable diffusion framework. A motivation study is first provided to demonstrate the current limitation. The proposed method is based on Textual Inversion and incorporates multiple regularisations (including Attention Masking, Prompts Contrastive Loss, and Bind Adjective) to disentangle multiple objects. The concepts are learned from a new dataset and evaluated by two designed protocols, followed by application visualizations.

### Strengths
-  To achieve multi-concept extractions from a single image, the proposed method leverages novel regularisation losses without relying on any groundtruth object segmentation
-  Overall, the paper is clearly structured and easy to follow. The motivational study introduces the problem and the current limitation in a systematic way
-  The experiments are well-designed with both real-world categories and out-of-domain biomedical images involved during the evaluation
-  Comprehensive analysis is conducted with t-SNE visualizations and embedding similarity evaluation.

### Weaknesses
 - Some recent works (such as Break-A-Scene) on similar tasks could also be mentioned in the related work section. On the other hand, though it would be a bit unfair to directly compare with Break-A-Scene (due to its given segmentation inputs), it could still be interesting to treat its performance as an upper bound and comment on how a good segmentation mask would affect the learned concepts.
- More implementation details could be added, particularly on prompt initialization. It seems a bit unclear how to initialize all learnable embeddings by the same word, “photo” in a random manner. Besides, one may be curious about how the number of prompts is determined, especially for MCPL-all.
- It would be better to discuss the limitations of current work in the last section and point out some future improvement directions.

### Questions
- It seems that all learned concepts (nouns) are associated with a pre-defined adjective description in the prompt (such as “a green *”). Are these adjectives playing roles in disentangling the concepts? What if the initial prompt is provided in the form “A * and a @”?
- I wonder if there are any examples of cases when the number of objects in the image is mismatched with the number of learnable concepts

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To tackle the issue of learning multiple individual concepts simltaneously, in this paper, the authors propose MCPL. The authors first conduct preliminary studies to show that vanilla MCPL to jointly learn multiple concepts is feasible, but it is not adequate to learn correlations between objects and locate corresponding concepts. To tackle this issue, the authors propose three techniques: AttnMask, PromptCL, and PromptCL with Bind adj.. The proposed full MCPL-one can correctly recognize and localize different concepts.

### Strengths
1. The proposed prompts contrastive loss as well as Bind adj. can effectively regularize the attention maps regarding concepts to localize onto correct position. And learning with AttnMask can also largely refine the attention mask boundary, thus reducing false positive attention values. All these methods benefit to textural inversion. 

2. Extensive experimental results illustrate that the proposed MCPL can effectively generate attention masks for corresponding concepts, which benefits to textural inversion task. 

3. The description of method and experiment section is polished and easy to understand.

### Weaknesses
The main concern is the analysis between MCPL-diverse mentioned in preliminary study and the full version of MCPL-one. The authors could provide visualization of generated natural concepts from MCPL-diverse as well as corresponding generated segmentation masks to support the observation. Specifically, it's unclear how the 'diverse' version handles the inherent ambiguity in associating multiple concepts with a single image without explicit supervision. The preliminary study suggests it's feasible, but the mechanism for disentangling these concepts and generating distinct masks remains vague. Furthermore, the comparison between MCPL-diverse and MCPL-one lacks a clear explanation of the architectural differences or training procedures that lead to the observed performance variations. It would be beneficial to understand if MCPL-diverse uses a different attention mechanism or if it relies on a different loss function to achieve its results. Without a deeper dive into these aspects, the reported results are difficult to fully interpret.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Multi-Concept Prompt Learning (MCPL) framework for simultaneously learning multiple prompts from one scene in order to address the challenge of managing multiple concepts in scenes with multiple objects. The authors conducted a motivational study to investigate the limitations of existing prompt learning methods in multi-concept settings and found that object-level learning and editing without manual intervention remains challenging. To enhance prompt-object level correlation, the authors propose regularization techniques including Attention Masking (AttnMask) and Prompts Contrastive Loss (PromptCL). Experimental results demonstrate that the MCPL framework enables enhanced precision in object-level concept learning, synthesis, editing, quantification, and understanding of relationships between multiple objects.

### Strengths
1.	A novel task of the Multi-Concept Prompt Learning (MCPL) framework, which enables simultaneous learning of multiple prompts from one scene. This approach addresses the challenge of learning multiple concepts within multi-object scenes, which has not been previously explored.

2.	Enhanced Object-Level Concept Learning: The proposed MCPL framework demonstrates enhanced precision in object-level concept learning, synthesis, editing, quantification, and understanding of relationships between multiple objects. This is validated through extensive quantitative analysis and evaluation of learned object-level embeddings.

3.	The paper proposes several regularization techniques to enhance the accuracy of prompt-object level correlation. These techniques restrict prompt learning to relevant regions, facilitate disentanglement of prompt embeddings, and the use of descriptive adjective words to bind each learnable prompt. These effective techniques contribute to learning object-level information under image-level supervision.

### Weaknesses
1.	The aim of this paper is to learn and compose multiple concepts in the same scene. However, the demonstrations to prove the composing ability are insufficient. In almost all demonstrations the concepts are composed in the same string as training examples without any changes and only some editing demonstrations are available. Upon the interaction between the two concepts is changed, the effects seem to be worse.

2.	Some writing mistakes exist in the paper. In the top right of Figure 3, the labeling of “on” and “under” should be reversed. On page 6, “The” in “Therefore The contrastive loss” should be lowercase in line 8 of the paragraph before “Implementation details”.

3.	The experiment is a little confusing. In the section “Baselines and experiments” on page 7, the author presents four learning methods to compare their effectiveness. However, the author seems not to explain the meaning of the first setting called textural Inversion applied to unmasked multi-concept images and the subsequent experiments don’t contain the effects of the first two settings. The detail and comparison for a setting called “MCPL-diverse” are also unavailable.

4.	The paper constructs a new dataset to evaluate the proposed framework for multi-concept learning. However, I see all provided examples contain only two distinct concepts so I doubt the generalization of this method.

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
