# Generative Visual Instruction Tuning

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 6, 3

## Abstract
We propose to use automatically generated instruction-following data to improve the zero-shot capabilities of a large multimodal model with additional support for generative and image editing tasks.
We achieve this by curating a new multimodal instruction-following set using GPT-4V and existing datasets for image generation and editing. Using this instruction set and the existing LLaVA-Finetune instruction set for visual understanding tasks, we produce \model, a Generative Large Language and Visual Assistant. 
\model is built through a strategy that combines three types of large pretrained models through instruction finetuning: Mistral for language modeling, SigLIP for image-text matching, and StableDiffusion for text-to-image generation.
Our model demonstrates visual understanding capabilities superior to LLaVA and additionally demonstrates competitive results with native multimodal models such as Unified-IO~2, paving the way for building advanced general-purpose visual assistants by effectively re-using existing multimodal models.git}}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
GenLLaVA, a novel approach aimed at enhancing the zero-shot capabilities of a single unfied large multimodal model to perform image understanding, image generation, and image editing tasks is proposed with the following contributions:
1. Construction of a new multimodal instruction-following dataset that combines image understanding, image generation, and image editing data.
2. A unified model, GenLLaVA, is trained in a single-stage training process, which is a departure from its predecessor, LLaVA.
3. GenLLaVA outperforms LLaVA and is competitive with native multimodal models like Unified-IO 2, setting a new benchmark for building advanced general-purpose visual assistants by effectively reusing existing multimodal models.

### Strengths
Originality:
- New Dataset Curation: The creation of a new multimodal instruction-following dataset that amalgamates image understanding, generation, and editing is innovative. It addresses the need for diverse training data to support complex multimodal tasks. 
- Single-Stage Training Strategy: Moving away from the traditional multi-stage training pipeline to a single-stage training recipe is a significant departure that simplifies the training process while maintaining performance.

Quality:
- State-of-the-Art Comparisons: With new dataset, GenLLaVA establishes its competitive standing within the field comparing to LLaVA in multi-modal understanding, GILL, AnyGPT, Unified-IO 

Significance:
- The work moves towards the development of a unified MLLM, which is able to simultaneously perform image generation and image understanding. This is a rather important direction for the development of MLLM.

### Weaknesses
1. Conciseness of the Methodology Section: The methodology section lacks sufficient depth, particularly in explaining how the model integrates outputs from large language models with Diffuser models for tasks in image generation and editing. Specific details, such as the configuration of attention masks, inputs and target outputs during image generation, and the loss functions employed, are absent. Including these would enhance clarity.

2. Limited Originality in Methodology: Due to its brevity, the methodology section does not adequately establish the originality of the proposed approach. A more detailed explanation of the unique methods used is essential to distinguish this work from similar studies, such as GILL[1] and Unified-IO 2[2] As depicted in Figure 1, the only observable difference between GLLaVA and GILL appears to be the choice of image encoders, language models, and Diffuser models—none of which are novel. If these component substitutions introduce significant innovation, or if additional design elements are integral, these should be clearly outlined to affirm the model’s originality in achieving image understanding, generation, and editing capabilities.

3. Experimental Support for Claims: The experiments presented do not convincingly substantiate the paper's claims of achieving image understanding, generation, and editing without compromising individual performance. As Table 1 indicates, the model underperforms in image generation tasks compared to its peers, with no comparison provided against other multimodal understanding models. Additionally, while the model uses data from ShareGPT[3], the performance is lower, scoring 66.8 on MMB[4] for a 7B LLM compared to ShareGPT’s 68.8. If this discrepancy is due to factors beyond inter-task conflicts, ablation studies could help clarify. Further, the single-stage pipeline is chosen and no ablation is performed, the author follows Prismatic vlms[5]. It's a main contribution claimed in paper which should contains some experiments to support it.

4. Inadequacy of Ablation Studies: The ablation studies presented are insufficient in addressing inter-task conflicts. Table 2(a) reveals a significant drop in performance when handling all three tasks concurrently. Although the authors propose enhancing understanding performance by adding more understanding data, no specific performance comparison is provided for image understanding alone. Moreover, the use of Task Tokens boosts performance in Table 2(a), but the underlying reasons for this improvement remain unexplored. This suggests that explicit task format definition is essential during inference, warranting further analysis in the discussion.

### Questions
1. Could you provide a detailed explanation of how the model integrates outputs from large language models with Diffuser models specifically for image generation and editing? 
2. The paper references similarities with existing models like GILL and Unified-IO 2, particularly in Figure 1, where the only discernible differences appear to be the use of certain image encoders, language models, and Diffuser models. Could you elaborate on the original aspects of GLLaVA, if any, beyond component substitution? 
3. While the paper claims to achieve balanced performance across image understanding, generation, and editing tasks, Table 1 suggests that the model falls short of peers in image generation, and no comparisons are made against other multimodal understanding models. Could you address this by clarifying if factors other than inter-task conflicts influence this performance gap?
4. Your decision to adopt a single-stage pipeline, inspired by Prismatic VLMS, is an essential component of the methodology, yet no ablation studies are provided to justify this choice over a multi-stage approach. Could you explain if any experiments were conducted to compare the performance of the single-stage pipeline with a more conventional multi-stage process?
5. Table 2(a) indicates a notable performance improvement with Task Tokens, yet no explanation is provided for this boost. Could you delve into the role of Task Tokens in explicitly defining the task format during inference?
6. The paper proposes an improvement in understanding capabilities by adding more data, yet no specific comparison is provided for image understanding performance alone. Would you be able to offer more insights into the impact of this additional data specifically for image understanding?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a composite model, GenLLaVA, for image understanding, generation, and editing. The authors create a generative multimodal instruction-following dataset using GPT-4V and existing datasets for image generation and editing. They also explore various training strategies and model designs, including single-stage training, the selection of a vision encoder, and the use of task tokens. Quantitative results across multiple benchmarks demonstrate GenLLaVA's effectiveness across all three tasks.

### Strengths
1.	Developing generative multimodal instruction-following data could be highly valuable for future research and applications.
2.	The model shows strong performance across image understanding, image editing, and image generation tasks.
3.	The paper is well-presented, making it easy to follow and understand.

### Weaknesses
1.	Although the authors promise to open-source all materials, including data, code, and pre-trained weights, none of these resources are provided for review. Since the dataset is a key contribution of this work, it would strengthen the paper to include these materials in the revised manuscript (with anonymity). I would consider recommending acceptance only if these resources are included in the final version.
2.	The novelty of this paper appears limited, as the model seems to be a straightforward combination of existing techniques, such as the framework, task tokens, vision encoder, and single-stage training.



### Questions
1.	What makes single-stage training preferable over multi-stage training in GenLLaVA.
2.	The performance of GenLLaVA significantly trails behind recent state-of-the-art models. For instance, the new version of LLaVA, LLaVA-OV [A], achieves an 80.8 on MMB, outperforming GenLLaVA by 14 points. I'm curious how the proposed dataset would perform if a stronger model and large-scale understanding data were used. Would a new mix of data be necessary, or would the current amount of generative data suffice?

[A] Li, B., Zhang, Y., Guo, D., Zhang, R., Li, F., Zhang, H., ... & Li, C. (2024). Llava-onevision: Easy visual task transfer. arXiv preprint arXiv:2408.03326.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new MLLM that has multi modal capabilities on both input and output. It also presents a new instruction following dataset, which is a non-trival combination and selection from a large amount of existing datasets for various specific tasks.
The paper adopts a less commonly used single-stage instruction tuning pipeline, which according to the text is more effective than extending previous multi-stage pipeline. 
Result evaluation shows that the model surpasses many major MLLMs on visual understanding tasks, and is roughly on par with previous models emphasizing visual generation tasks. 

The author claims that model checkpoint and the new dataset will be released.

### Strengths
While the task and the approach are not completely new, the paper proposed several improvements on current approach to build MLLMs, and demonstrated their effectiveness using relatively comprehensive evaluations, resulting in a new model that is strong on both visual understanding and visual generation.

The paper is largely clear about the goal, approach and results, though it will be better if more details on the reason of several design choices can be made clear.

### Weaknesses
The biggest weakness is the incremental nature of the work.  For example, 
the paper claims it unifies visual understanding and generation, but there are similar models such as SEED-X, which is also capable of both, as well as the compared work such as Unified-IO 2.

the paper claims they contribute a dataset for instruction tuning, but the dataset is composed of multiple existing datasets. The novelty to me would be insights on why these sets are selected, and why for some datasets such as IPr2Pr only a subset is selected. The paper can be much more impactful if there are more discussions on these decisions.

### Questions
Similar as putting MGIE as a baseline model, which is a domain expert on image editing, it would be great if other domain expert models can be put as references as well. The proposed model doesn't have to beat these models, but it will give readers a more comprehensive understanding of how good a combined model can be compared with domain experts.

The paper acknowledges that task specific tokens such as [T2I] and [I2T] are needed to achieve this balanced performance. In real user queries these tokens are not likely to be provided, I wonder if there are other more natural approaches to improve user intent understanding.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a multimodal instruction tuning set that combines image understanding, image generation, and image editing data. It further introduces a model GenLLaVA, which unifies visual understanding and generation using open-source models.

### Strengths
1. The authors build a multimodal instruction tuning dataset by aggregating a diverse set of supervised datasets and tasks including text understanding, image comprehension, generation and editing.
2. The paper is generally easy to follow.

### Weaknesses
1. Unified multimodal understanding and generation has become a highly popular direction recently, with many significant models introduced this year that can achieve image understanding, generation, and editing. However, this method simply adopts the same framework as GILL, which translates the hidden representations of an LLM into text embeddings of a pre-existing stable diffusion model. The mention of "using a Q-former as the generation head" in the paper cannot be considered a distinguishing feature from the GILL approach. From a methodological standpoint, this work appears to lack any innovation.
2.  This paper only compares a few outdated and underperforming models as baselines. The recent multimodal LLMs with unified comprehension and generation should be compared including Emu [1], Emu-2.0 [2], SEED-LLaMA [3], SEED-X [4], Mini-Gemini [5], etc.
3. The claim that "To our knowledge, this is the first time such capability has been achieved" is unfounded. As I mentioned earlier, several works have already accomplished unified image understanding, generation, and editing.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
