# ClassDiffusion: More Aligned Personalization Tuning with Explicit Class Guidance

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Recent text-to-image customization works have been proven successful in generating images of given concepts by fine-tuning the diffusion models on a few examples.
However, these methods tend to overfit the concepts, resulting in failure to create the concept under multiple conditions (\textit{e.g.}, headphone is missing when generating ``a {\tt <sks>} dog wearing a headphone'').
Interestingly, we notice that the base model before fine-tuning exhibits the capability to compose the base concept with other elements (\textit{e.g.}, ``a dog wearing a headphone''), implying that the compositional ability only disappears after personalization tuning. 
Inspired by this observation, we present ClassDiffusion, 
a simple technique that leverages a semantic preservation loss to explicitly regulate the concept space when learning the new concept. Despite its simplicity, this helps avoid semantic drift when fine-tuning on the target concepts. Extensive qualitative and quantitative experiments demonstrate that the use of semantic preservation loss effectively improves the compositional abilities of the fine-tune models. In response to the ineffective evaluation of CLIP-T metrics, we introduce BLIP2-T metric, a more equitable and effective evaluation metric for this particular domain. We also provide in-depth empirical study and theoretical analysis to better understand the role of the proposed loss. Lastly, we also extend our ClassDiffusion to personalized video generation, demonstrating its flexibility. Our project page are \url{https://classdiffusion.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work delves into the captivating realm of text-to-image customization. However, current tuning-based methods often struggle with a common pitfall: they tend to overfit to the limited concepts presented in their training datasets. This overfitting can significantly diminish the model's compositional abilities. The authors highlight that this decline is mainly due to the semantic shifts that occur with customized concepts during the fine-tuning process.  To address this issue, the authors introduce an approach called ClassDiffusion. This technique revitalizes the model's compositional strength by restoring its connection to the original semantic space. Through a series of thorough experiments, the authors demonstrate the effectiveness of ClassDiffusion and the fresh insights it brings to interconnected fields. The results not only showcase its prowess but also pave the way for exciting advancements in the domain.

### Strengths
1. The authors unveil the intriguing underlying cause behind the overfitting of SD. Rather than a typical case of overfitting, they suggest it’s more about semantic drift—a perspective I find quite compelling, though I still believe overfitting truly occurs.

2. This paper is not only well-written but also flows smoothly, making it a pleasure to read.

3. The inclusion of additional relevant baselines demonstrates the authors' thorough research and deep engagement with the topic.

4. The authors provide a wealth of comprehensive experimental results, reinforcing the strength of their proposed ideas.

### Weaknesses
1. I agree that semantic drift occurs during fine-tuning. This drift arises because the model is an intricate network filled with numerous parameters. When we fine-tune with only few samples, the adjustments to these parameters are minimal, yet the model still retains its generative capabilities. In my view, semantic loss may struggle to restore the original semantic space, as it doesn’t preserve the nuances of the drift encountered. Theoretically, utilizing the entire training text data could mitigate this issue.

2. While I think that the proposed method is quite straightforward and effective,  it should be explained further.

3. The figures in this paper could use some enhancement—except for Figure 4, which stands out nicely. The other figures are somewhat simplistic, and certain visuals, like Figure 2, lack clarity when paired with their captions.

4. Although the writing is commendable, both the tables and figures require refinement. For instance, in Table 1, every similarity is bolded, which could lead to confusion.

### Questions
see weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript introduces "ClassDiffusion," a methodology for personalizing text-to-image generation. Leveraging a semantic preservation loss, this method facilitates rapid and efficient concept customization, and prevent the semantic drift during the fine-tuning process. The results demonstrate that the proposed work is competitive with leading frameworks in various image generation tasks.

### Strengths
1. The proposed work observes the reason why the existing methods suffer from the issue of compositional ability with experiments and theoretical analysis.

2. The authors have developed a framework for generating personalized images that effectively ensure the compositional capabilities for concept personalization tuning.

2. The paper provides experimental results, including both quantitative and qualitative assessments, showcasing the superior performance of the framework. The results clearly highlight the effectiveness of the proposed method in facilitating personalized image generation.

### Weaknesses
1. In Figure 5, the method utilizes the semantic preservation loss. However, it is unclear how it would perform with fine-grained subjects (two dogs or two cats with different breed). Clarification on whether the method can effectively manage such fine distinctions and a visual representation of joint embeddings for both similar and diverse subjects would be beneficial.

2. Recent methodologies [1, 2] have demonstrated the capability to learn multi-concept personalization, it remains uncertain if the proposed work can handle multiple personalized instances, particularly for contexts involving up to five subjects. Although quantitative results for two subjects are provided in the paper, the absence of qualitative results for three or more subjects in both the main text and appendix is a notable omission. Including these results would substantiate the method's capability in more complex scenarios.

### Questions
Given the concerns mentioned, particularly around the method's scalability to more complex multi-subject personalizations and the rationale behind the loss choices, I recommend a "marginally below the acceptance threshold" for this paper. Enhancements in demonstrating multi-subject capabilities, clarity in embedding visualization, and justification for the choice of technology could potentially elevate the manuscript to meet publication standards.

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
2

### Summary
This paper addresses a critical issue in text-to-image personalization models: the loss of compositional ability after fine-tuning. The authors identify that after personalization tuning, models struggle to generate images that combine the personalized concept with other elements (e.g., a personalized dog wearing headphones). Through experimental and theoretical analysis, they attribute this to semantic drift of the personalized concept from its superclass. They propose ClassDiffusion, which introduces a semantic preservation loss to maintain alignment between personalized concepts and their superclass during fine-tuning.

### Strengths
1 The paper provides a thorough investigation of a significant problem in personalization models, supported by both empirical observations and theoretical analysis.

2 The proposed solution is elegantly simple yet effective, making it practical for implementation.

3 The experimental results demonstrate clear improvements over existing methods.

### Weaknesses
1 The paper lacks comprehensive ablation studies to demonstrate the impact of different components of the semantic preservation loss.

2 While the authors mention extending their method to video generation, this aspect feels somewhat underdeveloped and could benefit from more detailed exploration.

### Questions
1 Include more detailed ablation studies to validate the design choices in the semantic preservation loss.

2 Expand the evaluation section with more quantitative metrics specifically designed to measure compositional ability.

3 Provide more extensive comparisons with other state-of-the-art methods that attempt to address similar issues. Include more diverse case studies beyond the dog-headphone example to demonstrate the generality of the approach.

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
3

### Summary
For text-to-image customization task, the authors suggest that all tuning-based models will inherently suffer from the over-fitting introduced by this process, which leads to weakening in the compositional ability of the model. They hypothesize that the decline in this compositional ability stems from the semantic drift of the target concept away from superclass target during fine-tuning. They analyze the experimental and theoretical aspects in turn, and introduce ClassDiffusion to address the issue of weakening compositional capacity after fine-tuning.

### Strengths
1. The authors explain what they work do with a vivid example, which is easy for readers to understand.
2. The authors theoretically analyze the sampling difficulty based on the joint conditional probability distribution.
3. The paper is written logically and clearly, from experimental phenomenon, theoretical proof, and solution method respectively.
4. The authors extend the proposed method to the video field.

### Weaknesses
1. The paper mentions that “CLIP-T metric can hardly reflect the actual performance of personalized generation” but CLIP is still used to calculate Loss (Equation 10). The rationale for using CLIP for loss calculation, despite its limitations for evaluation, should be more thoroughly explained. It is not sufficient to state that they are isolated problems, as the choice of loss function directly impacts the training process and thus the final performance. A more detailed justification is needed, perhaps discussing why CLIP is still a suitable choice for capturing semantic similarity in the text embedding space, even if it fails in the image-text space.
2. The paper mentions “higher SPL weights preserve combining ability better” and “lower SPL weights restore specific concept features more effectively”, why is the weight of SPL set to 1 in dataset A. Is this the optimal value? It needs to be further discussed. The paper should include a more rigorous ablation study, exploring a wider range of SPL weights and providing quantitative metrics to support the choice of 1. The current justification is weak, and the trade-off between combining ability and concept fidelity should be explored more thoroughly.
3. The writing is somewhat redundant. For example, it is not clear how significant Figure 2 is. While the figure attempts to show a real-world application, it does not provide any quantitative analysis or unique insights beyond what is already shown in Figure 1. The paper would benefit from a more focused presentation, removing redundant figures or providing more detailed analysis of the results shown in Figure 2.
4. The paper mentions that "we found that the CLIP-T metric can hardly reflect the actual performance of personalized generation", but does not clearly explain how this is found. Whether it is based on references to other works is very confusing. Evidence or references should be provided to support their claim about the limitations of the CLIP-T metric for evaluating personalized generation. This would strengthen the justification for introducing a new metric. The claim needs to be backed by either empirical evidence within the paper or by citing relevant literature that demonstrates the shortcomings of CLIP-T in this specific context.
5. The paper mentions "we introduce the BLIP2-T metric", is this metric proposed by the authors? It should be clarified whether this is a novel metric proposed by the authors or whether it's based on existing work. If it's novel, more details on its development and validation are requested. The paper needs to clearly state the origin of the BLIP2-T metric and, if it is not novel, provide proper citations to the original work.
6. Is Figure 3a an experimental result or a schematic diagram? If it is a schematic diagram rigorous notation is recommended. More detailed captions or annotations should be provided to improve clarity. The paper should clarify whether Figure 3a is a visualization of experimental data or a conceptual diagram. If it is a visualization, the data source and processing steps should be described. If it is a diagram, it should be presented with rigorous notation and clear labels.

### Questions
1. The paper mentions that "CLIP-T metric can hardly reflect the actual performance of personalized generation" but CLIP is still used to calculate Loss (Equation 10). The rationale for using CLIP for loss calculation, despite its limitations for evaluation, should be explained.

2. The paper mentions "higher SPL weights preserve combining ability better" and "lower SPL weights restore specific concept features more effectively", why is the weight of SPL set to 1 in dataset A. Is this the optimal value?  An ablation study or justification should be provided for the choice of 1 as the SPL weight, and how they balanced the trade-off between preserving combining ability and restoring specific concept features should be discussed.

3. The writing is somewhat redundant. For example, it is not clear how significant Figure 2 is. The Figure 1 is already shows the performance of proposed method.

4. The paper mentions that "we found that the CLIP-T metric can hardly reflect the actual performance of personalized generation", but does not clearly explain how this is found. Whether it is based on references to other works is very confusing. Evidence or references should be provided to support their claim about the limitations of the CLIP-T metric for evaluating personalized generation. This would strengthen the justification for introducing a new metric.

5. The paper mentions "we introduce the BLIP2-T metric", is this metric proposed by the authors? It should be clarified whether this is a novel metric proposed by the authors or whether it's based on existing work. If it's novel, more details on its development and validation are requested.

6. Is Figure 3a an experimental result or a schematic diagram? If it is a schematic diagram rigorous notation is recommended.  More detailed captions or annotations should be provided to improve clarity.

### Soundness
3

### Presentation
3

### Contribution
2
