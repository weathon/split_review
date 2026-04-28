# Fine-Grained Verifiers: Preference Modeling as Next-token  in Vision-Language Alignment

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 8, 6, 6, 5

## Abstract
The recent advancements in large language models (LLMs) and pre-trained vision models have accelerated the development of vision-language large models (VLLMs), enhancing the interaction between visual and linguistic modalities. Despite their notable success across various domains, VLLMs face challenges in modality alignment, which can lead to issues like hallucinations and unsafe content generation. Current alignment techniques often rely on coarse feedback and external datasets, limiting scalability and performance. In this paper, we propose FiSAO (Fine-Grained Self-Alignment Optimization), a novel self-alignment method that utilizes the model’s own visual encoder as a fine-grained verifier to improve vision-language alignment without the need for additional data. By leveraging token-level feedback from the vision encoder, FiSAO significantly improves vision-language alignment, even surpassing traditional preference tuning methods that require additional data. Through both theoretical analysis and experimental validation, we demonstrate that FiSAO effectively addresses the misalignment problem in VLLMs, marking the first instance of token-level rewards being applied to such models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the issue of modality misalignment in Vision-Language Language Models (VLLM). The authors demonstrate that a token-level reward is more effective than a sentence-level reward for aligning modalities. They apply a specially designed token-level reward during preference tuning to mitigate modality misalignment.

### Strengths
1. The proposed self-training approach does not need any additional data and external modules to mitigate the misalignment issue.
2. They find that coarse feedback, such as sentence-level rewards, shows a weak correlation with hallucination detection.
3. They are the first method to introduce token-level rewards for VLLMs preference tuning.

### Weaknesses
1. In Figure 2, you show that the correlation between CLIP-based sentence rewards and conventional evaluation metrics is weak. Could you also present the correlation between token-level rewards and conventional evaluation metrics?

2. In the Table 3 experiment, it would be valuable to see the performance improvements across all baselines when using your approach. While line 429 mentions that the LLaVA backbone with your method surpasses existing approaches, it is worth noting that the original LLaVA-1.5 already performed well compared to other models. Demonstrating consistent improvements across various VLLMs could serve as strong evidence of your approach’s generalizability.

3. It is clear from Table 3 that your approach does not allow LLaVA-1.5 to surpass the higher-performing baselines on the MM-Vet benchmark. Additionally, Table 4 shows that fine-grained rewards do not yield an advantage on some benchmarks, including MME^c, POPE, and CHAIR. I am particularly interested in understanding which types of benchmarks or backbone architectures benefit most from your approach and where it shows superior performance.

4. In Figure 4, you illustrate the comparison of reward distributions for generated objects on LLaVA-1.5 before and after training. It seems reasonable that training the model with an RL algorithm on the same reward function results in higher average rewards. However, I am unclear about the purpose of showing the shift in reward distributions. Could you elaborate on the rationale behind presenting this distribution shift? Additionally, could you provide a detailed explanation for the design of Equation (8) and the reasoning behind its specific form?

5. Currently, new MLLMs leverage not only CLIP-based models but also other visual encoders, such as DINO-v2 (self-supervised) and SigLip. How adaptable is your approach when applied to MLLMs that incorporate multiple visual encoders? Could you explain any modifications or considerations necessary for your method to handle such configurations effectively?

6. Your approach primarily focuses on object hallucination. I am curious to know whether it also helps mitigate other types of hallucinations, such as those related to actions or spatial relationships. Additionally, could you elaborate on how the size of the expanded set C contributes to the observed performance improvements?

### Questions
1. In Figure 2, you show that the correlation between CLIP-based sentence rewards and conventional evaluation metrics is weak. Could you also present the correlation between token-level rewards and conventional evaluation metrics?

2. In the Table 3 experiment, it would be valuable to see the performance improvements across all baselines when using your approach. While line 429 mentions that the LLaVA backbone with your method surpasses existing approaches, it is worth noting that the original LLaVA-1.5 already performed well compared to other models. Demonstrating consistent improvements across various VLLMs could serve as strong evidence of your approach’s generalizability.

3. It is clear from Table 3 that your approach does not allow LLaVA-1.5 to surpass the higher-performing baselines on the MM-Vet benchmark. Additionally, Table 4 shows that fine-grained rewards do not yield an advantage on some benchmarks, including MME^c, POPE, and CHAIR. I am particularly interested in understanding which types of benchmarks or backbone architectures benefit most from your approach and where it shows superior performance.

4. In Figure 4, you illustrate the comparison of reward distributions for generated objects on LLaVA-1.5 before and after training. It seems reasonable that training the model with an RL algorithm on the same reward function results in higher average rewards. However, I am unclear about the purpose of showing the shift in reward distributions. Could you elaborate on the rationale behind presenting this distribution shift? Additionally, could you provide a detailed explanation for the design of Equation (8) and the reasoning behind its specific form?

5. Currently, new MLLMs leverage not only CLIP-based models but also other visual encoders, such as DINO-v2 (self-supervised) and SigLip. How adaptable is your approach when applied to MLLMs that incorporate multiple visual encoders? Could you explain any modifications or considerations necessary for your method to handle such configurations effectively?

6. Your approach primarily focuses on object hallucination. I am curious to know whether it also helps mitigate other types of hallucinations, such as those related to actions or spatial relationships. Additionally, could you elaborate on how the size of the expanded set C contributes to the observed performance improvements?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Fine-Grained Self-Alignment Optimization (FiSAO), a method designed to improve vision-language alignment in Vision-Language Large Models (VLLMs). Unlike traditional alignment techniques that use coarse, sentence-level feedback, FiSAO leverages token-level feedback from the model’s visual encoder, requiring no additional external data or annotations. This token-level approach addresses hallucination issues with more precise differentiation between hallucinated and correctly grounded outputs.

### Strengths
- Token-level rewards is an emerging area of research that is worth exploring. So far, only contemporary work has begun to consider token-level reward methods for VLMs, with this paper being one of the first works in this space.
- The methodological framework is well-defined, with both empirical and theoretical foundations.
- Evaluation is comprehensive, with many baselines and benchmarks.

### Weaknesses
 - Table 1 does not seem to be very representative of relevant literature. Neither the motivation nor the related work covers existing methods for NLP token-level reward [1,2]. Would be nice to also cover concurrent works for VLMs [3,4] so that differences with recent work are better highlighted (albeit not taken into consideration as a weakness in my review, to the contrary, this shows this area of research is very important).

- It is unclear why not use OpenCHAIR which addresses the limitations of CHAIR for benchmarking object hallucinations.

- Figure 2 alone does not robustly support the observation that sentence-level rewards are unreliable indicators of model performance. To be exact, Figure 2 suggests there exists no *linear* relationship between the CLIP-based sentence rewards and the conversational metrics. Sentence-level CLIP scores might still have value, but in ways not captured by simple linear correlation with BLEU or ROUGE. Perhaps the figure could also show the linear correlation for token-level rewards to make a comparative argument, which would be stronger. 

- Theoretical analysis assumes linear transformations and relationships between the latent representations of the image and text modalities (e.g., in the data generative model for v and t). It also relies on orthogonal matrices U_v and U_t​ for projecting latent variables to high-dimensional representations. While this simplifies the theoretical analysis, it assumes a degree of independence or decorrelation between features that may not exist in complex multimodal settings. There are other simplifications such as sub-Gaussian noise, Gaussian generative likelihood, an infinite data setting, and modeling token-level feedback as a regression problem, all of which understandably simplify (and make possible) the analysis but perhaps should be stated clearly as assumptions.

- The current method relies on predefined sets of objects and labels (from datasets like Detic and COCO) to define common objects for fine-grained reward calculation and the fine-grained reward calculation uses predefined thresholds to distinguish correct and hallucinated tokens. Seems both would require careful tuning.

- Calculating token-level rewards for every token in a generated sequence seems computationally intensive? The paper contains no analysis of the performance - computational overhead tradeoffs against sentence-level rewards.

- The reward in Eq. (8) is too difficult to parse, perhaps consider improving clarity in the draft notation presentation format.

- Please explain what is POVID, etc., in the main paper? The appendix does not seem to be a good place to add this information since these methods are crucial in understanding the results. Also briefly mention what are the eval metrics used for each Table 2 column? I could not locate this information easily.  

- Also, it is unclear if Table 2 shows results where FiSAO is added on top of other methods such as POVID, Human-Prefer, etc. Would it make more sense to evaluate the method with just RLHF sentence-level or token-level feedback to show clear differences?

### Questions
- What are the major differences between this work and recent token-level reward papers in NLP and VLMs?

- What is the correlation between CLIP-based **token-level** rewards and conversational metrics?

-  What are the eval. metrics used for each Table 2 column?

-  To my understanding, Table 2 shows results where FiSAO is added **on top of** other methods such as POVID, Human-Prefer, etc.? Would it make more sense to evaluate the method with just RLHF sentence-level or token-level feedback to show clear differences? 

I find the work interesting and timely, and look forward to the rebuttal.

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
The paper presents Fine-Grained Self-Alignment Optimization (FiSAO) to improve the alignment of visual and linguistic modalities in vision-language large models (VLLMs). It addresses the challenges of misalignment caused by independent pre-training, which can lead to biased outputs and hallucinations. By leveraging token-level feedback from the vision encoder, FiSAO enhances alignment more effectively than traditional methods that rely on coarse feedback. The findings suggest that this approach reduces the need for external data and improves performance in tasks requiring precise integration of visual and language information.

### Strengths
- The paper is well-structured and clearly articulated, making it accessible for readers.
- The introduction of FiSAO is grounded in sound analysis and presents a logical approach to addressing alignment issues.
- Extensive experimental validation supports the effectiveness of FiSAO, showcasing its practical applicability.
- The authors offer valuable insights into enhancing alignment in vision-language large models, contributing meaningfully to the field.

### Weaknesses
 - In the comparison with other state-of-the-art methods, FiSAO did not achieve results on MM-Vet that are comparable to leading approaches. It would be beneficial to include an analysis of the factors contributing to this outcome and to outline potential strategies for improvement in future iterations. Understanding the specific challenges faced in this context could guide refinements to FiSAO and the design of models.
- Efficiency of FiSAO should be analysed as well.  And how the dependency of pretrained vision model affects the performance?

### Questions
Please see above.

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
The paper proposes Fine-Grained Self-Alignment Optimization (FiSAO) to improve vision-language alignment in VLMs. The core idea is to leverage token-level, fine-grained feedback from the model's own visual encoder to guide the training process. The method avoids the need for external annotations or tools by utilizing the vision encoder as a fine-grained verifier, providing token-level rewards during training.

### Strengths
- The paper addresses a critical challenge in morden VLMs. The approach of token-level, fine-grained rewards to improve alignment make much sense to me. 

- The paper presents a theoretical framework, including mathematical proofs.

- The experimental evaluation is thorough and well-designed. The experiments support the benefits of token-level rewards in reducing hallucinations and improving benchmark performance.

### Weaknesses
1. The theoretical analysis assumes that the CLIP provides perfect vision-langauge alignment, which is a bit unrealistic as CLIP models are known to have alignment errors in practice. Under this assumption, it’s unsurprising that it can be proved that incorporating the CLIPScore improves the performance. Also, the presented theorem cannot support the benifit of _fine-grained_ reward, which is the core point of this paper. Additionally, the framework also relies on linear relationships between inputs and outputs and the infinite data setting.

2.  The introduction of the MDP perspective seems unnecessary and is not well-justified within the context of the paper. Framing language generation as an MDP may not capture the long-range dependencies and context inherent in language, potentially violating the Markov property. At the end of Section 3.3.1, the author state that “This perspective highlights how fine-grained rewards can be applied ...”--I am unsure about how introducing the MDP framework demonstrates this point.

3. Regarding Section 3.1

   Overall, this section looks a bit unclear to me. Firstly, the calculation process of token-level reward is not introduced, leading to confusion. Whether it is token-level CLIPScore? (additional question: whether per-sentence average of token-level reward is the same as sentence-level reward?)

   The authors state that sentence-level rewards show a weak correlation with conventional metrics, implying that sentence-level rewards are not effective. However, metrics like BLEU and ROUGE are known to have limitations in measuring semantic similarity, consider using CiDEr or SBERT semantic simialrity score can make the results more convincing. Also, the paper does not clarify whether token-level rewards have a stronger correlation.

5. Issues with Clarity and Readibility

   - Symbols like $S$ in Equation (7) and the normalization function \( \mathcal{N} \) are not properly defined when first introduced. The S also overlapps with the S in MDP.

   - Figure 1 shows distributions of two types of rewards before the concept and calculation of ‘reward’ is introduced.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper first demonstrates the advantages of token-level over sentence-level approaches in handling hallucinations. It then utilizes the similarity between each text token and visual features as a reward to achieve a token-level preference optimization. This optimization method employs expert models to make judgments on entity targets, enabling automatic construction of preference data. Ultimately, it achieves a certain level of performance improvement.

### Strengths
This paper:
1. analyzes the significant advantages of token-level processing over sentence-level processing in handling hallucinations, laying a solid foundation for subsequent research on token-level rewards.
2. claims a token-level visual reward, which relies on expert models to discriminate entity targets. Although the approach is not novel, the idea is commendable.
3. conducts some simple experiments and analyses to verify the effectiveness of the method.

### Weaknesses
1. The paper overuses formula derivations while glossing over specific methodological details, making the overall writing quite confusing. Especially in section 3.2 and equation 5, there’s a lack of necessary logic, making it difficult to understand. The connection between the derived equations and the actual implementation is not clearly established. For example, it's unclear how the token-level similarity scores are actually computed from visual features, and how these scores are then used to construct the reward signal. The paper would benefit from a more detailed explanation of the practical steps involved in applying these formulas.
2. I understand that the data construction method mentioned in the article still relies on fuzzy matching with ground truth based on entities. This seems to be a rather manual and primitive way of data construction, potentially introducing significant systematic errors. Have you tried more precise token selection methods?
3. Overall, I find the experiments still insufficient. The experimental baselines are quite outdated, and the tested benchmarks are not comprehensive enough. Particularly, why is there a claim about handling hallucinations, but the final experiments lack an evaluation of hallucinations? Also, why is there almost no improvement on POPE? What’s the reason for this?

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

### Contribution
3
