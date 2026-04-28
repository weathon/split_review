# DPLM-2: A Multimodal Diffusion Protein Language Model

- Decision: Accept
- Avg Score: 6.33
- Scores: 3, 8, 8

## Abstract
Proteins are essential macromolecules defined by their amino acid sequences, which determine their three-dimensional structures and, consequently, their functions in all living organisms. Therefore, generative protein modeling necessitates a multimodal approach to simultaneously model, understand, and generate both sequences and structures. However, existing methods typically use separate models for each modality, limiting their ability to capture the intricate relationships between sequence and structure. This results in suboptimal performance in tasks that requires joint understanding and generation of both modalities.
In this paper, we introduce DPLM-2, a multimodal protein foundation model that extends discrete diffusion protein language model (DPLM) to accommodate both sequences and structures.
To enable structural learning with the language model, 3D coordinates are converted to discrete tokens using a lookup-free quantization-based tokenizer.
By training on both experimental and high-quality synthetic structures, DPLM-2 learns the joint distribution of sequence and structure, as well as their marginals and conditionals.
We also implement an efficient warm-up strategy to exploit the connection between large-scale evolutionary data and structural inductive biases from pre-trained sequence-based protein language models.
Empirical evaluation shows that DPLM-2 can simultaneously generate highly compatible amino acid sequences and their corresponding 3D structures eliminating the need for a two-stage generation approach.
Moreover, DPLM-2 demonstrates competitive performance in various conditional generation tasks, including folding, inverse folding, and scaffolding with multimodal motif inputs, as well as providing structure-aware representations for predictive tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces DPLM-2, a multimodal discrete diffusion protein language model that can simultaneously generate both protein sequences and their 3D structures. The model extends the DPLM protein language model by incorporating structural information through a lookup-free quantization-based tokenizer that converts 3D coordinates into discrete tokens. DPLM-2 is trained on both experimental structures from PDB and synthetic structures from AFDB-SwissProt.

### Strengths
1. The paper is clearly written.

2. The model achieves simultaneous structure-sequence generation without requiring a two-stage training approach.

3. The experiments on learning structure tokenization are valuable for the community.

### Weaknesses
1. The DPLM-2 model is trained starting from the weights of DPLM model. As evident from e.g. Table 2 (poor diversity) and Table 5 (high AAR), DPLM suffers from mode collapse. Training DPLM-2 starting from such a checkpoint  leads to severe mode collapse in DPLM-2. Generating the same result over and over again makes a generative model useless. Training both models from scratch rather than finetuning might help and provide the insight on how adding structural information to the DPLM architecture affects the generation ability. Even better would be a thourough ablation study of the training procedure.

2. Authors compare DPLM and DPLM-2 only with EvoDiff on unconditional sequence generation. Adding more baselines of different architectures (AR transformers, CARP, continuous diffusion, flow-matching, etc.) would greatly improve the work.

3. There are some issues with model evaluation. First, the model is evaluated only structurally, but it is langugae model after all. Using sequence-based evaluation metrics, including sequence clustering for the diversity should benefit the soundness of the work. Second, it is not clear, why the Authors use pdb-TM (claculate TM-score against PDB), if the model is trained also on the synthetic data. Third, the designability metric used in this work evaluates the consistensy between the generated structure and the prediction of ESMFold on the generated sequence. It does not measure protein "quality".

4. Authors compare DPLM-2 on inverse folding task with weak baselines. Adding recognized IF models would greatly benefit the work. The same goes to other tasks, e.g. representation learning.

5. The dataset preparation included random cropping. It is not clear if it has a detrimental effect on the model behaviour.

6. The paper lacks analysis on the trained structural tokens. Additional exploration of the interpratability of the tokens themselves and untilization of the codebooks would greatly benefit the paper. Do the tokens correspond to some local environments in structure, or are they just abstract entities?

### Questions
1. The model does not learn the distribution of protein lengths. Have you tried to overcome this limitation?

2. The ablation results presented in 4.1.3 and table 3 are controversial. Could you please clarify the procedure, how many samples was used for evaluation and so on? 

3. On page 9, line 442 is stated that DPLM-2 adopts argmax decoding. In the original DPLM paper argmax did not work. Can you elaborate on this?

4. The experiment on DeepLoc is not described in sufficient detail. Why you chose to use only one tiny dataset? Could you provide experiments that show the described catastrophic forgetting issue, which is of high importance?

5. One of the main claims of the paper states that the co-generation guarantees consistency between structure and sequence. This is a strong statement that requires strong evidence. However on line 223 the assumption of conditional independence is made. Can you provide a rigorous mathematical proof that garantees such consistensy?

### Soundness
3

### Presentation
3

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
The paper presents DPLM-2, a multimodal protein foundation model designed to represent and generate protein sequences and structures. DPLM-2 introduces a token-based approach to protein structures, converting 3D backbone coordinates into discrete structure tokens. The model then processes structure token sequences alongside amino acid sequences, with aligned position encodings to reinforce residue-level correspondence between them, and is trained using a denoising objective.

Addressing the limitations of previous models like Multiflow, which lack sequence-based pretraining to capture co-evolutionary relationships, DPLM-2 leverages pretraining on unlabeled sequences and finetuning on structures, to learn the joint distribution of sequences and structures. This allows DPLM-2 to capture both modalities effectively and enables it to model joint, marginal, and conditional distributions.

Additionally, DPLM-2 demonstrates competitive performance across tasks such as unconditional generation, folding, inverse folding, and motif-scaffolding, showing its capability as a comprehensive multimodal protein modeling tool.

### Strengths
- Originality: The work's originality lies primarily in (1) the DPLM framework that combines sequence tokens and structure tokens with a lookup-free quantization (LFQ) VAE, and (2) the use of sequence pretraining followed by LoRA fine-tuning. These contributions provide valuable insights to the field. The authors also address relevant concurrent work effectively.

- Clarity: The paper is generally easy to follow, though some sections would benefit from further explanation and technical details.

- Empirical Performance: DPLM-2 demonstrates strong empirical performance across a wide range of generative tasks, including sequence-structure co-generation, folding, inverse folding, and motif-scaffolding. The paper also includes valuable ablation studies on sequence pretraining and data augmentation, offering insights into the model’s effectiveness and robustness.

### Weaknesses
 -Missing Details: Key details are missing in certain sections.

     (1)A core contribution is the DPLM-2 model itself, but essential details, such as how sequence and structure tokens are combined and how the structure tokenizer is trained, are not included in the main text. Moving these details from the appendix to the primary text, with clear explanations including the frozen pretrained structure encoder and the sequence prediction head on top of the structure decoder, would significantly improve clarity.

     (2)The distinct noise level for each modality could be better explained, as this aspect is currently underdeveloped. Specifically, the paper should clarify how the noise schedules are determined for each modality and how these choices affect the model's ability to learn joint distributions, as well as conditional and marginal distributions. The lack of detail makes it difficult to assess the impact of this design choice.

     (3)In Section 4.2, the authors mention that performance can improve with supervised fine-tuning using a folding objective; however, the paper lacks details on this fine-tuning process. The paper should specify the exact loss function used, the learning rate schedule, and the number of training steps for this fine-tuning process.

- Clarity and Consistency Issues: Minor inconsistencies reduce clarity, such as inconsistent bolding of best results in Tables 2 and 6. In Table 4, DPLM-2 is presented as performing well in zero-shot folding, yet its RMSD is high compared with ESM3, PVQD, and ESMFold, achieving competitive performance only after fine-tuning (SFT). Additionally, clarifying the presentation of mean and median values could help with data interpretation. The paper should also clarify whether the reported RMSD values are calculated over all residues or only over the aligned regions, as this can significantly affect the interpretation of the results.

- Mixed Results: The results on certain tasks are not fully convincing. In particular, while DPLM-2 exhibits high scTM in unconditional protein generation, it does not achieve lower scRMSD compared to other methods, indicating potential limitations in generation quality. The paper should provide a more detailed analysis of the generated structures, including secondary structure content and the presence of physically unrealistic features. A comparison of the distributions of these features with those of native proteins would be beneficial.

### Questions
- Sequence tokens use a smaller vocabulary than structure tokens. Are the corresponding structural embeddings in DPLM-2 trained from scratch during fine-tuning?
- While DPLM-2 enables flexible generation, what are the trade-offs in structural invariance when using structure tokens instead of 3D coordinates?
- In Table 2, what is meant by DPLM-2 (seq → structure) or (structure → seq)? If these indicate modality-by-modality generation, could you clarify how this is implemented?
- For the protein representation learning evaluation, it might be useful to include a broader range of baselines, such as GNN-based models, for a more comprehensive comparison.
- In Section 3.3, you state, “Recent efforts have applied this approach to protein structure coordinates (Van Kempen et al., 2024; Liu et al., 2023; Gao et al., 2024; Lu et al., 2024). This allows language models to better learn the composition of local structural elements. However, how to learn an effective structure tokenizer remains an active research question.” Given the similarity of your method to prior approaches, particularly with the use of LFQ as in Gao et al., 2024, could you elaborate on how your method contributes to addressing this active research question?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents a multimodal diffusion protein language model that integrates information from both sequence and structure modalities. The model is built upon a pre-trained DPLM model, using LoRA technology to extend the original sequence-only model’s capability to process structural knowledge. This approach not only reuses the knowledge embedded in the existing sequence-based protein language model but also reduces training costs and expenses. Compared to traditional autoregressive language models, the diffusion language model offers more flexible generation capabilities, making it better suited for modeling protein data with extensive non-unidirectional semantic dependencies. Overall, this work represents a natural extension and generalization of the DPLM model, exploring the performance of such diffusion language models on multimodal protein data and demonstrating the potential advantages of multimodal protein language models.

### Strengths
1. This is the first multimodal diffusion protein language model, which effectively explores the application of such models in multimodal scenarios. Considering the potential of diffusion language models, I believe this is a highly meaningful research question.

2. The paper has a clear logical structure, and its content is straightforward and easy to understand.

3. The paper demonstrates the performance of DPLM-2 across a variety of tasks, providing substantial and comprehensive content that analyzes the model’s performance from multiple perspectives.

### Weaknesses
1. The main results reported in this paper are based on unconditional generation tasks; however, some evaluation metrics may have inherent limitations.

2. The model in this paper is trained on a relatively small protein structure dataset, lacking exploration on larger-scale structural data. I believe that extending multimodal protein language models to larger protein sequence and structure datasets could further unlock the potential of this approach.

3. There are some minor spelling and formatting errors: the equation on line 197 is missing a right parenthesis, and $ b_{i}(t) $ introduced in equation (1) (on line 192) is undefined in the paper.

4. The structure tokens appear to be concentrated in alpha helix and beta sheet regions, with lower density in loop regions. Given that loops are highly flexible and variable, this may indicate that the structure tokens in loop regions are not well-learned, potentially resulting in weaker modeling capability in these regions. This is further supported by the observation that the model’s designability is notably worse in regions with a higher proportion of loops.

5. Under the unconditional backbone generation task, DPLM-2 achieves the highest scTM metric while also showing a significantly worse scRMSD metric, both in terms of mean and variance, which are at high levels. Given that these two metrics should have a certain level of correlation, this discrepancy is somewhat unusual and warrants further investigation.

6. Comparing the performance of ESM3 and DPLM-2 in the inverse folding task reveals a pattern where DPLM-2 often exhibits a higher AAR while frequently showing a lower scTM. This could be due to biases in the protein structure prediction model (ESMFold) or because the sequences generated by DPLM-2, despite having higher ARR, may deviate further from the target protein’s data distribution.

7.  I am curious about the vocabulary usage rate of VQ-VAE when the vocabulary size is 1024. I noticed a significant performance difference between VQ-VAE and LFQ in this case, so I wonder if the vocabulary usage rate might be a contributing factor to this issue.

8. I would like to confirm whether DPLM-2 in Table 7 still utilizes structural pre-training, given that neither of these models used large-scale sequence pre-training. If structural pre-training was indeed applied to DPLM-2, then there are two differences between DPLM and DPLM-2: one is the difference in model architecture, and the other is that DPLM-2 was pre-trained on structural data. With these two variables present, how can we determine that the performance decline in DPLM-2 is due to catastrophic forgetting?

9. Similar to ESM-3, the model uses discrete structure tokens to represent structural information. While this approach offers scalability, it limits the model’s ability to capture finer structural details accurately. This trade-off represents an important challenge in the current field of multimodal protein language models.

### Questions
1. **Regarding structure tokens:** Figure 2B shows that most structure tokens are concentrated in alpha helix and beta sheet regions, with lower density in loop regions. However, in line 409 of the paper, you state that "loops are highly flexible." Could this pose a potential issue? More variable regions typically contain richer and more diverse information, which may require more structure tokens to model this diversity effectively. Yet, your experimental results do not align with this. Moreover, your results in Figure 4B also indicate that the model’s designability is notably worse in regions with a higher proportion of loops. Could one possible reason for this issue be that the structure tokens in loop regions are not well-learned, resulting in weaker modeling capability?

2. **Regarding the pLDDT metric:** Table 2 shows that MultiFlow (retrained on our training data) and DPLM-2 (co-generation) perform similarly on scTM and scRMSD metrics but diverge significantly on the pLDDT metric. A similar trend is observed when comparing Figures 3A and 3C. In Figure 3A, scTM and scRMSD metrics remain relatively stable as sequence length increases, with scRMSD even increasing for sequences of length 500. However, Figure 3C shows a notable upward trend in pLDDT as sequence length increases (from 100 to 300), without a significant drop in pLDDT even for sequences of length 500. These phenomena indicate that the scTM and scRMSD metrics convey somewhat contradictory information to the pLDDT metric. Generally, a significant drop in pLDDT should correspond with a decrease in scTM and an increase in scRMSD. My question here is whether this inconsistency might indicate that the pLDDT metric is unreliable. I raise this because, in previous experiments, we observed that pLDDT, being predicted by a neural network (e.g., ESM-2) trained on natural protein datasets, sometimes fails to handle model-generated proteins that deviate significantly or exhibit severe irregularities, leading to inflated pLDDT values. This phenomenon is quite common in unconditional generation. Therefore, I believe using a more diverse set of metrics is essential. However, you did not provide evaluation results for MultiFlow (retrained on our training data) on the Novelty and Diversity dimensions, which makes it harder to assess the model’s performance on this part of the task.

3. **Regarding scTM and scRMSD metrics:** In Table 2, under the unconditional backbone generation task, DPLM-2 achieves the highest scTM metric while also showing a significantly worse scRMSD metric, both in terms of mean and variance, which are at high levels. Is this phenomenon somewhat unusual? Given that these two metrics should have a certain level of correlation.

4. **Regarding the inverse folding task:** Comparing the performance of ESM3 and DPLM-2 in Table 5 reveals a pattern where DPLM-2 often exhibits a higher AAR while frequently showing a lower scTM. Could this possibly be due to biases in the protein structure prediction model (ESMFold) or because the sequences generated by DPLM-2, despite having higher ARR, may deviate further from the target protein’s data distribution?

5. **Regarding repetition:** In practice, we observed that diffusion protein language models tend to generate a large number of repetitive amino acids. I noticed that DPLM employed a resampling scheme to address this issue (code link: [here](https://github.com/bytedance/dplm/blob/5545c6d4166f515b4eb66ada41d0ab3178dfe6ca/src/byprot/models/lm/dplm.py#L279)). Therefore, regarding the DPLM-2 model, I would like to know whether it also encounters similar repetition issues. If so, what approach did you adopt to resolve it? If not, I would like to know what prevented this issue in DPLM-2.

6. **Regarding VQ-VAE:** I am curious about the vocabulary usage rate of VQ-VAE when the vocabulary size is 1024. I noticed a significant performance difference between VQ-VAE and LFQ in this case, so I wonder if the vocabulary usage rate might be a contributing factor to this issue.

7. **Regarding catastrophic forgetting:** I would like to confirm whether DPLM-2 in Table 7 still utilizes structural pre-training, given that neither of these models used large-scale sequence pre-training. If structural pre-training was indeed applied to DPLM-2, then there are two differences between DPLM and DPLM-2: one is the difference in model architecture, and the other is that DPLM-2 was pre-trained on structural data. With these two variables present, how can we determine that the performance decline in DPLM-2 is due to catastrophic forgetting?

8. **Regarding the structural information:** Similar to ESM-3, you also use discrete structure tokens to represent structural information. This approach offers scalability benefits for the model, yet it also limits the model’s ability to capture finer structural details accurately. This trade-off represents an important challenge in the current field of multimodal protein language models. I am interested to know whether you would consider any methods to mitigate this issue when applying DPLM-2 to more structure-related tasks, as you described in Section 5.

### Soundness
3

### Presentation
4

### Contribution
3
