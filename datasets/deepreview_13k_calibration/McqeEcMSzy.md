# Task Vectors are Cross-Modal

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
We investigate the internal representations of vision-and-language models (VLMs) and how they encode task representations. We consider tasks specified through examples or instructions, using either text or image inputs. Surprisingly, we find that conceptually similar tasks are mapped to similar task vector representations, regardless of how they are specified. Our findings suggest that to output answers, tokens in VLMs undergo three distinct phases: input, task, and answer, a process which is consistent across different modalities and specifications. The task vectors we identify in VLMs are general enough to be derived in one modality (e.g., text) and transferred to another (e.g., image). Additionally, we find that ensembling exemplar and instruction based task vectors produce better task representations. Taken together, these insights shed light on the underlying mechanisms of VLMs, particularly their ability to represent tasks in a shared manner across different modalities and task specifications. Project page: \url{https://task-vectors-are-cross-modal.io}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores how vision-and-language models (VLMs) encode tasks across different modalities. The authors demonstrate that task vectors are cross-modal, enabling task information to transfer between modalities, which boosts performance. They further show that combining text instructions with examples enhances the sample efficiency of task vectors. Experimental results support all these findings.

### Strengths
1. This paper is well-written and easy to understand.
2. Discovering cross-modal task vectors and their transferability is an innovative approach.
3. The experiment appears to be thoughtfully designed and well-executed.

### Weaknesses
1. The methodology is straightforward. Although the authors mention that task vectors are cross-modal and can transfer between different modalities, this work appears to be an extension of previous work on function vectors. The method seems like a direct extension, which is trivial and lacks novelty.
2. Figure 2 suggests the possibility of transferring text ICL vectors to image-based tasks, but the specifics of the patching process are not thoroughly explained. The description lacks detail on how the task vector extracted from the text ICL is aligned and injected into the image processing pathway, especially given the different embedding spaces of text and images.
3. Mapping the input space to a vector, represented by $G$, is essential for generating task vectors; however, the authors do not clearly explain how this mapping is calculated. The explanation should include details on the specific layers and operations used to derive the task vector, and how this process differs between text and image inputs.
4. The method applies only to MLLM types that use a feature encoder, limiting its generalizability. For example, models like QWen, which lack a feature encoder, would not be compatible with this approach. The paper should more clearly acknowledge this limitation and discuss the implications for broader applicability.
5. In lines 241–244, the authors initially state that the top-1 decoding for both text and image ICL are similar, but they then claim that alignment with language is "not immediately obvious" for image ICL. This seems contradictory, as the table does not show significant differences between text and image ICL. Additionally, the explanation that "the model could have mapped the task vectors close to unused nonsense tokens" lacks supporting evidence. The claim about alignment should be better supported by analysis of the embedding spaces.
6. For several experimental results, such as task conflict and image ICL transfer, the paper primarily presents qualitative examples as evidence. Providing quantitative results would strengthen the claims. The lack of quantitative metrics makes it difficult to assess the robustness and generalizability of the observed effects.

### Questions
1. The paper does not include an Appendix, although some sentences in the main text reference it.
2. Line 351 should refer to Table 4 instead of Figure 4.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a method for identifying task vectors in the residual space of a auto-regressive VLM. Using a few samples of a task in one modality, the model can be patched to perform the same task in the other modality.

### Strengths
Originality:
 - The paper is the first to explore the area of multi-modal fewshot task learning via patch learning

Quality:
 - The experiments seem to fully explore the task-space in the domain of these llava-like models

Clarity:
 - The figures are intuitive and the results are clearly presented

Significance:
 - I personally think mechanistic interpretibility / model steering will be a new foundational paradigm, so I like to see more work in this space.

### Weaknesses
The main issue with the paper is it's clarity. It is incredibly difficult to read and follow. I did not realize the proposed method was for auto-regressive VLMs like LLava until page 5! The notation used throughout the paper is very unusual and led me to believe this method was for CLIP-like models. It wasn't until I did an external literature review were I found the prior work "Find Visual Task Vectors" uses the identical notation. While I'm not against maintaining the notation, it's clear some of the equations are for image generative models, not auto-regressive text generative models.

Patching itself is never actually described, not clear how the proposed method actually works at test time. Are there any hyper-parameters used? I know when I run model steering vectors, I'll normalize the vector and add it by 3x, is that happening here?

Logit lens is introduced and used without any explanation as to how it works. I have no idea how the experiment in figure 3 works.

I'm also disappointed mechanistic interpretability / model steering isn't put more front-in-center, as the proposed method is an application of model steering/patching (see Neel Nanda's cited papers). I felt a little bit misdirected.

Overall, the writing is a major hindrance to my judgement for the other aspects of the paper. I currently do not feel qualified to evaluate the experiments given their current descriptions. As a single example, I need more explanation of what "Exemplar xPatch" is and "Instruction + Exemplar xPatch" is. But to be clear, I have similar clarity issues for all the experiments.

While I believe the proposed method would be of interest to the community, I cannot recommend the paper in its current form.

Minor: 
 - table 1 has a hard time rendering on my computer. Can you lower the resolution quality of the images in it? I think the strawberry is extremely high resolution.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

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
The paper investigates the internal representations of vision-and-language models , specifically focusing on how task vectors encode information across different modalities. This paper present findings that conceptually similar tasks, whether specified through examples or instructions, yield similar vector representations in VLMs. This property enables task vectors to be transferred from one modality to another (e.g., from text to image), with the ensembling of exemplar and instruction-based vectors producing superior task representations. The research contributes to understanding the underlying mechanisms of VLMs, emphasizing their ability to maintain consistent task representations across modalities.

### Strengths
1. The paper introduces cross-modal task vectors, demonstrating that VLMs can generalize tasks across different input modalities (e.g., text to image) effectively,advancing multi-modal interpretability.
2. The paper reveals a consistent three-stage token evolution (input, task, answer) across modalities, providing deeper understanding of VLM internal mechanisms.
3. The finding that task vectors from language-only models can be applied in VLMs underscores the versatility of cross-modal task representations.

### Weaknesses
1. **Insufficient Validation Across Task Types**: The paper's validation is limited to a narrow range of task types. Expanding the evaluation to diverse tasks would strengthen its claims.

2. **Unclear description of key elements**: The method for obtaining task vectors is not described clearly, particularly regarding the specific settings and conditions.It would be beneficial to have a clearer explanation of the context and conditions under which these task vectors are derived, including any specific parameters or preprocessing steps involved.

3. **Lack of Methodological Details**: Key methodological details are not adequately explained, particularly in terms of the implementation of xPatch and xBase. The paper would benefit from a more in-depth description of how these configurations are set up and executed. Additionally, the combination of Instruction and Exemplar vectors in the Instruction + Exemplar xPatch approach is not described in sufficient detail. A clearer explanation of how these vectors are integrated would greatly enhance the paper’s clarity and reproducibility.

### Questions
See the section on weakness. We will increase the score based on the answer to the question.

### Soundness
3

### Presentation
3

### Contribution
3
