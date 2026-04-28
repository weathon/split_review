# RetroInText: A Multimodal Large Language Model Enhanced Framework for Retrosynthetic Planning via In-Context Representation Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 3, 8

## Abstract
Development of robust and effective strategies for retrosynthetic planning requires a deep understanding of the synthesis process. A critical step in achieving this goal is accurately identifying synthetic intermediates. Current machine learning-based methods often overlook the valuable context from the overall route, focusing only on predicting reactants from the product, requiring cost annotations for every reaction step, and ignoring the multi-faced nature of molecular, resulting in inaccurate synthetic route predictions. Therefore, we introduce RetroInText, an advanced end-to-end framework based on a multimodal Large Language Model (LLM), featuring in-context learning with TEXT descriptions of synthetic routes. First, RetroInText including ChatGPT presents detailed descriptions of the reaction procedure. It learns the distinct compound representations in parallel with corresponding molecule encoders to extract multi-modal representations including 3D features. Subsequently, we propose an attention-based mechanism that offers a fusion module to complement these multi-modal representations with in-context learning and a fine-tuned LLM for a single-step model. As a result, RetroInText accurately represents and effectively captures the complex relationship between molecules and the synthetic route. In experiments on the USPTO pathways dataset RetroBench, RetroInText outperformed state-of-the-art methods, achieving up to a 5% improvement in Top-1 test accuracy, particularly for long synthetic routes. These results demonstrate the superiority of RetroInText by integrating with context information over routes. They also demonstrate its potential for advancing pathway design and facilitating the development of organic chemistry.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors target a more realistic retrosynthesis scenario, considering multi-step synthesis and cost function. Solving retrosynthesis planning and multi-step reasoning about the intermediate is important, which current LLM-based methods overlook. To tackle this, the authors suggest an E2E framework involving learnable multimodal LLM utilizing a 3D molecule encoder and (possibly closed source) LLM generating text descriptions for intermediate synthesis steps. By fusing the multimodal information via the proposed attention mechanism and leveraging LLM generated reaction descriptions, the proposed method outperformed semi-template-based and template-free SOTA methods and recorded comparable performance to the SOTA template-based method in RetroBench.

### Strengths
- The authors proposed a principled way to leverage LLM in retrosynthesis using multiple modalities, including molecular structure (2D graph and 3D conformation) and text descriptions of chemical reactions.
- The authors' method of generating text descriptions and ranking candidate reactants for multi-step retrosynthesis would inspire many future researches.
- Until now, LLM-based retrosynthesis methods have primarily focused on single-step retrosynthesis, leaving few studies available for the potentially more significant multi-step retrosynthesis in the domain. Additionally, they have not considered the reaction cost, which is crucial in real-world reaction pathways. By conducting multi-step retrosynthesis based on a value function that takes into account a cost function, the authors have narrowed the gap between LLM-based retrosynthesis and real-world applications.
- The proposed method outperformed not only semi-template-based and template-free methods but also most template-based methods. This is interesting because the performance is achieved largely based on LLM’s generalization via ICL and reasoning ability, without relying on inductive bias, including reaction template, so with further future potential.

### Weaknesses
 - The motivation to maximize mutual information of 2D graph and 3D conformation is not sufficiently presented. If one can use 3D conformation, which is generally believed to have more information than a 2D graph, what is additional information from the 2D graph? It seems that Table 3 does not resolve this matter.
- It is necessary to add the ablation of 1D molecular sequence substituting graph embedding to demonstrate the supremacy of spatial representation, considering that the molecular sequence is generally regarded as a more advantageous modality than 2D graph and 3D conformation. Could you add the ablation study?
- I wonder how much the proposed framework is sensitive to the quality of textual description and what quality control process would help (GPT-3.5 could be quite old these days for SOTA-level performance achievement), which I found no available analysis related. Could you provide an analysis related to this matter?

### Questions
- In section 4.2, Textual Generator and Encoder, there is a confusing explanation related to the use of textual description. The authors used textual descriptions of the intermediate molecules along all pathways but, in test time, only used the text description of the product molecules to prevent information leakage, which is a train-test mismatch. But why is this data leakage, given that ChatGPT is not trained during training time?

### Soundness
2

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
The paper introduces RetroInText, a multimodal framework for retrosynthetic planning, enhanced by in-context learning with large language models. RetroInText leverages textual descriptions generated by ChatGPT and molecular 3D and graph-based representations to improve retrosynthesis prediction accuracy.  This framework leverages detailed textual descriptions of reaction procedures generated by ChatGPT, combined with molecular graph and 3D features, to create multimodal representations that better capture the complex relationships between molecules and synthetic routes. The model incorporates an attention-based fusion mechanism that integrates these multimodal representations, enabling it to learn from both molecular structure and contextual information. By fine-tuning a MolT5 for single-step retrosynthesis, RetroInText adapts to the intricate nature of retrosynthesis tasks. On the USPTO pathways dataset, RetroInText achieves up to a 5% improvement in Top-1 test accuracy over state-of-the-art methods

### Strengths
The paper has the following strengths:
1. The paper’s integration of molecular graph, 3D structure, and in-context textual data provides a comprehensive approach to retrosynthetic planning. This combination allows RetroInText to capture the complexity of chemical synthesis from multiple perspectives, marking an original approach in retrosynthesis where LLMs are used to contextualize synthetic routes. This multimodal approach demonstrates high methodological quality, even though the performance gains are limited. By introducing this multimodal approach, the paper shows potential significance for future studies aiming to integrate similar techniques in other fields.
2. Using ChatGPT to generate in-context textual descriptions based on IUPAC names and structural features is an approach that enriches retrosynthetic planning with additional chemical insights. This originality suggests potential for further exploration in LLM-assisted retrosynthesis. Although the actual significance may be limited by the gains achieved, the concept of using LLMs to add synthetic context could inspire similar uses in adjacent fields.
3. RetroInText employs an attention-based fusion module that effectively combines textual and structural molecular representations. This fusion step is crucial for allowing the model to weigh and integrate these varied inputs. In terms of quality, the fusion module is a well-executed method for ensuring that multimodal data can interact meaningfully, enhancing the model’s potential to capture complex dependencies between chemical steps. The mechanism is clearly described, adding to the clarity of the methodology, though the actual impact on performance is modest.
4. The paper’s adaptation of MolT5, a language model originally designed for SMILES-based tasks, as a single-step retrosynthesis predictor is a clever methodological choice. Treating the retrosynthesis task as a translation problem aligns well with the model’s strengths, bringing originality to how language models are applied in chemistry. This choice also reflects quality in adapting existing models to new domains. However, while the approach is interesting, the overall improvement in prediction accuracy suggests that this strength is more exploratory than transformative.
5. The paper provides a good assessment of the contributions of each module through ablation studies, helping to clarify the unique roles of textual and structural data in the model. This thorough evaluation approach enhances clarity, making it easier to understand the marginal improvements contributed by each component. The methodological rigor shown here is a positive aspect of the paper’s quality, even if the results themselves do not indicate a significant practical advancement.

### Weaknesses
 The paper suffers from the following weaknesses:

1. While RetroInText introduces a multimodal framework, the performance gains it achieves over baseline models are relatively modest, with only a 5% improvement in Top-1 accuracy on the RetroBench dataset. This incremental improvement does not fully justify the complexity introduced by the multimodal integration of text, graph, and 3D structure data. To enhance the significance and novelty of this work, the authors could focus on refining specific modules, such as further tuning the MolT5 model or the fusion mechanism, to achieve more substantial performance gains. The reported 5% improvement is also not clearly contextualized against the range of typical improvements in the field, making it difficult to assess its true impact. A more detailed comparison with other state-of-the-art methods, including a discussion of the typical performance gains seen in retrosynthesis, would be beneficial.
2. One area that is not explored by the paper but feels lacking is that the paper is using GPT 3.5. Compared to more recent models (GPT-4o, Llama 3) the performance of GPT 3.5 is limited especially in science domains. Although in-context textual descriptions generated by ChatGPT add an innovative dimension, they may not offer significant chemical insights specific to retrosynthesis tasks compared to the newer models. Additionally, the generic nature of these descriptions could lead to data that does not substantially improve the model’s understanding of chemical reactions. Therefore, experiments for comparison when a less generic description is provided by more recent LLMs is missing that could shed light on the effectiveness of the methodology. Also a more effective approach could also involve fine-tuning open-source LLMs or using a chemistry-specific language model trained on domain-specific texts to produce text that better captures the critical reaction features. The paper does not explore the impact of the prompt used to generate the text, which could significantly affect the quality and relevance of the descriptions.
3. While the attention-based fusion module is a central part of RetroInText, the authors do not clearly justify why it is the optimal choice for combining multimodal data in retrosynthesis. The paper could be improved by a deeper analysis of the fusion mechanism, potentially comparing it with alternative fusion strategies (e.g., cross-attention or co-attention modules). Such an analysis would add clarity and help readers understand whether the observed performance gains are due to the multimodal data itself or the specific fusion approach chosen. The paper lacks a detailed explanation of the specific advantages of the chosen cross-attention mechanism over other alternatives, particularly in the context of retrosynthesis. The computational cost and efficiency of the chosen fusion method are also not discussed.
4. The evaluation focuses primarily on Top-k accuracy metrics, without providing chemical interpretability insights or explaining how the model might aid chemists in real-world settings. Retrosynthesis models are most useful when their predictions can be understood and trusted by chemists, yet the current metrics do not assess interpretability. Including an analysis of the quality of the predicted intermediates or comparing predicted synthetic pathways with experimentally validated routes would strengthen the paper’s practical relevance and significance. The paper does not provide any analysis of the chemical validity of the predicted pathways, which is crucial for practical application. The evaluation also lacks a discussion of the limitations of the model in terms of the types of reactions it can handle and the complexity of the molecules it can process.

### Questions
Here are the questions for the RetroInText paper:
1. Could the authors explain the difference in Retro* and Retro*-0 search algorithms? This was not provided in the text.
2. For the results table provided no uncertainty/error is provided in the overall performance. This makes the comparison of numbers quite hard. Especially given the fact that most attention based models' performance change quite a bit between different random seeds. Would the authors provide experimental repeats and with that present standard deviation of the performance to better compare RetroInText to other baselines?
3. Please provide the detail on the compute power and the time it takes for training and inference of RetroInContext compared to other baselines.
4. ChatGPT is used to generate textual descriptions, yet these descriptions may lack specificity and relevance for retrosynthetic tasks. Could the authors provide more detail on why they selected ChatGPT over domain-specific LLMs or fine-tuning a language model on chemistry-specific corpora? 
5. Would the authors consider adding metrics that assess the interpretability of predictions or evaluate the predicted intermediates' consistency with known chemistry principles?

### Soundness
3

### Presentation
4

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
The paper focuses on retrosynthesis analysis of molecules using large language models (LLMs) such as ChatGPT. It employs ChatGPT to generate reaction descriptions, then incorporates both text and structural information of the product molecules into another model, MolT5, to suggest potential reactants. The A* algorithm is then used to search for synthesis routes. This work addresses an important problem with an interesting approach, capable of generating reaction descriptions alongside reaction formulas, potentially improving interpretability in retrosynthesis analysis. The paper could benefit from improvements in the discussion of its motivation, methods, and experiments.

### Strengths
1. **Originality**: The idea of using LLMs to generate text descriptions for retrosynthesis is interesting.
2. **Quality**: The paper presents a generally reasonable framework.
3. **Clarity**: The paper includes figures and algorithms to aid readability.
4. **Significance**: The paper presents experiments with promising results.

### Weaknesses
 **Originality**: The motivation of the paper needs further clarification from different perspectives:

1. Lines 44-46: Why are graph and SMILES representations limited in capturing the complexity of chemical structures? How does the major focus of this paper—text—help solve these issues? This conclusion is counterintuitive, as many recent studies have shown that graph- or SMILES-based models often outperform even the most advanced text-only models, such as LLMs.

2. Lines 51-53, 66-68: Throughout the paper, it is unclear how the proposed idea addresses these issues.

**Quality**: The proposed framework needs more justification.

1. Lines 69-78: There is no clear connection between the proposed framework and the previous paragraphs. The idea of using "ChatGPT (Edwards et al., 2022) to present detailed descriptions of the reaction procedure" is bold and lacks justification. Can ChatGPT truly generate accurate reaction procedures? How reliable is it, and how can errors be prevented from misleading or disrupting the framework?

2. Some claims are incorrect. Line 479/Figure 1: MolT5 is not an LLM.

**Clarity**: The paper’s writing needs improvement.

1. Please check all citations. For example, the citation for ChatGPT on line 70 is incorrect, and the citation for ScScore (line 75) is missing.

**Significance**: The results presented in the paper need more justification.

1. The experimental setup is unclear. For instance, what are the specifications of the A* algorithm (e.g., search iterations, candidates, time)? What are the building blocks? 

2. The paper lacks case studies and systematic evaluations on the quality of reaction descriptions generated by ChatGPT.

3. Regarding the evaluation metrics, a single molecule can have multiple potential synthesis routes. How does the exact match metric comprehensively evaluate model performance if the model suggests a route different from the one in the dataset, yet still a useful route?

### Questions
1. What is the Retro*-0 algorithm?

2. How long does it take for the proposed framework to find a solution for a single molecule? Is it significantly longer than the baseline, given the many models involved in Figure 1?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper does two main things:

1. For retrosynthesis prediction, it fine-tunes MolT5 specifically for one-step retrosynthesis, aiming to improve accuracy in predicting the immediate precursor of a target molecule.

2. For the search algorithm, it introduces a synthetic complexity score, reaction cost (calculated as the negative log likelihood of a retrosynthesis prediction), and the captioning score to identify the most promising reactants. The prediction score, based on the three types of scores, helps prioritize reactants based on their likelihood of successful synthesis. To learn the prediction score effectively, the paper proposes a multimodal fusion module that combines 3D molecular conformation data and textual descriptions, producing a comprehensive molecular embedding that enhances learning.

Extensive experimental results demonstrate the superior performance of this proposed approach.

### Strengths
1. It’s impressive to see this paper employ set-wise matching between the predicted and reference starting materials in RetroBench's test dataset rather than relying on the search success rate. This metric is both more accurate and powerful, providing a true reflection of the model’s and search algorithm’s performance in practical multi-step retrosynthesis scenarios. Notably, this approach achieves state-of-the-art (SOTA) performance among template-free models.

2. The paper’s approach to fine-tuning a pretrained model on the retrosynthesis task is commendable. To the best of my knowledge, few works have leveraged existing pretrained models specifically for retrosynthesis, highlighting the potential for further exploration into how large molecule models can be pretrained and how foundation models can be fine-tuned for retrosynthesis. This paper suggests that a molecule foundation model, rather than a language foundation model, might be better suited for chemistry-focused tasks, a valuable insight for future research.

3. Additionally, the paper proposes a robust search algorithm that uses three key scores—synthetic complexity, reaction cost, and captioning score—to identify the most promising reactants during the search process. Furthermore, it incorporates both 3D structural data and textual information to enhance predictions. Though complex, this approach proves highly effective and could inspire future work to explore additional scoring metrics for search algorithms.

### Weaknesses
1. The writing could be improved for clarity. First, Figure 1 lacks sharpness; I recommend replacing it with a clearer vector diagram for better visualization. Additionally, restructuring the paper into two distinct sections—one for the retrosynthesis model and another for the proposed scoring method for guiding the search—would enhance readability and help readers better understand the key contributions.

2. The training process for the prediction score is not sufficiently explained. Equation 8c references only two score types: synthetic complexity score and reaction cost. However, Figure 1 also includes a captioning score, making it unclear how all three scores are utilized within the search process. Clarifying the use of these scores would improve understanding.

### Questions
Could this score be used as a reward to train a residual energy-based model [1] for reranking purposes?

[1] Preference Optimization for Molecule Synthesis with Conditional Residual Energy-based Models, ICML 2024

### Soundness
3

### Presentation
2

### Contribution
3
