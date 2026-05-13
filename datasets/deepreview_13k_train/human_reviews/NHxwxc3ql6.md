# It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Very large language models (LLMs) such as GPT-4 have shown the ability to handle complex tasks by generating and self-refining step-by-step rationales. Smaller language models (SLMs), typically with < 13B parameters, have been improved by using the data generated from very-large LMs through knowledge distillation. However, various practical constraints such as API costs, copyright, legal and ethical policies restrict using large (often opaque) models to train smaller models for commercial use. Limited success has been achieved at improving the ability of an SLM to explore the space of possible rationales and evaluate them by itself through self-deliberation. To address this, we propose COALITION, a trainable framework that facilitates interaction between two variants of the same SLM and trains them to generate and refine rationales optimized for the end-task. The variants exhibit different behaviors to produce a set of diverse candidate rationales during the generation and refinement steps. The model is then trained via Selective Rationale Optimization (SRO) to prefer generating rationale candidates that maximize the likelihood of producing the ground-truth answer. During inference, COALITION employs a controller to select the suitable variant for generating and refining the rationales. On five different datasets covering mathematical problems, commonsense reasoning, and natural language inference, COALITION outperforms several baselines by up to 5%. Our ablation studies reveal that cross-communication between the two variants performs better than using the single model to self-refine the rationales. We also demonstrate the applicability of COALITION for LMs of varying scales (4B to 14B parameters) and model families (Mistral, Llama, Qwen, Phi). We release the code for this work here.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Training on rationale or chain-of-thoughts have been known to be effective at enhancing a smaller LM's ability, yet due to transparency, copyright issues, this method has a fundamental limitations. The authors propose Coalition, a method that trains multiple LMs on different data splits & constructs a CoT preference dataset by comparing the likelihood (of producing the correct answer by conditioning on the CoT candidates) from the different models. This is effective because when training a single model, it could not generate a diverse set of response candidates. Compared to prompting-based baselines or iterative self-training baselines, the proposed methods show stronger performance on 5 benchmarks.

### Strengths
The paper compares with multiple baselines (Table 1), show that their method works across various scales (Table 3), and is supported by ablation experiments that each component does make the method more effective (Table 4,5).

### Weaknesses
* In addition to extrinsic measurements, perhaps it would be great to include intrinsic measurements of how the preference data quality improves through (1) choosing a winner rationale and (2) refinement.

* It is not clear how the number of LLM variants are decided and how the dataset is divided to train each LLM variant. Considering that this is the first step of the overall pipeline, an ablation experiment of deciding the number of variants or protocols for dividing data splits seems crucial but is missing.

* Compared to using LLM-as-a-Judge or reward models to choose winner rationale/eliminated rationale, how much effective is using rationale-conditioned GT answer likelihood heuristic? There should also be an experiment for this as it is a trivial baseline.

### Questions
Please see the questions mentioned in weaknesses. I will change my scores accordingly based on the author's response!

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a COALITION framework to improve the rationale generated from smaller language models without more powerful teacher models. LLMs typically excel at generating complex rationale but have limitations in their cost. COALITION addresses the limitations of SLMs by enabling two variants of the same model to generate and refine diverse rationales, optimizing them using a Selective Rationale Optimization (SRO) process to maximize task performance. 

Their experiments verify the effectiveness of their method on three base models on five datasets. The result shows that cross-communication between model variants can boost performance compared to self-refinement and other baselines by up to 5%.

### Strengths
The paper contributes to rationale generation by addressing a gap: improving the performance of smaller language models without relying on more powerful large language models. While existing work often emphasises knowledge distillation or prompt-based methods involving LLMs, this paper introduces COALITION, a unique framework that leverages two variants of the same model to collaboratively generate and refine rationales.

Their IFT trains two variants of an SLM on separate data splits to exhibit distinct behaviours in generating and refining rationales. During SRO, these variants independently generate and cross-refine rationales for a given task, with utility scores assigned based on the likelihood of producing correct answers. This scoring guides DPO in refining the models’ outputs. The controller, trained on preference data from DPO, dynamically selects the optimal variant for generation and refinement during inference. This coordinated approach generates a higher-quality rationale, boosting SLM performance without external supervision.

The writing is well structured, and their experiments consistently improve on different models and tasks compared with the baseline method.

### Weaknesses
The authors quantitatively analyse the quality of the rationales based on the final task accuracy, determining rationale effectiveness by how well it leads to correct answers. However, they did not focus on conducting human evaluations or employing LLMs as judges to assess rationales to provide more insight into the rationale coherence or human preferences.

### Questions
The two variants model seems to be the most important part of the framework. How effectively do the two variants trained on separate data splits capture genuinely diverse reasoning paths? Could these variants' differences be further quantified or analysed to understand better their distinct contributions, e.g., what is the minimum data we need to train the variants?

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
4

### Summary
[Edit] I have updated my score based on the authors' response. 

This paper proposes a novel framework "COALITION" that can be used with smaller language models (<13B) to generate rationales that lead to higher accuracy. COALITION uses two variants of a language model (variant in terms of instruction-finetune training data), and employs self/cross-refinement + DPO to train them. Finally during inference, a controller model picks a rationale to be used between the ones generated by the two variants. The authors present strong empirical results and a thorough ablation study.

### Strengths
* Strong empirical results including (1) Varied, thorough and strong set of baselines show the numerical significance of COALITION, and (2) results with multiple base-LLMs such as Phi3, Qwen, Mistral, Llama3
* Useful ablation studies that demonstrate the usefulness of their proposed components.

### Weaknesses
 * Section 3 presents difficulty in understanding the training of LLM variants - I suggest the authors to clearly explain the initial training data differences between LV1, LV2, and M_IFT. It is my understanding that M_IFT was trained with the entire IFT data, whereas LV1 and LV2 (before refinement) were trained with different splits of the IFT data to ensure that they exhibited different behaviours, but I invite the authors to correct me if this is wrong, and also add a simplified, non-mathematical summary of the same in Section 3.
* To clarify, each LLM variant was trained wth DPO with both (1) generated rationales raked by utility scores, and (2) refined rationales ranked by utility scores?
* Section 3.3: What is the purpose of training a controller C to rank the variants, when M_IFT was already performing that role with its utility scores? It's unclear why a separate controller is needed if M_IFT can already assess rationale quality during training.
* Since this paper depends heavily on rationales, I suggest the authors to perform a human study on the rationales (generated, refined, and final) to check their quality. I understand that this work is primarily focused on improvement of accuracy, however, a preliminary understanding of the quality of the rationales generated is essential to have trust in this system. Specifically, it is important to understand if the refined rationales are actually better than the generated ones, and if the selected rationales are indeed the best among the generated ones.
* Lastly, I suggest the authors to discuss the explainability aspect of their framework in the Ethics section.

### Questions
[covered in Weaknesses]

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
In the paper, COALITION is introduced to improve the performance of smaller LLMs in generating rationales through cross-communication. This is done by two variants of the same model fine-tuned in different ways.

### Strengths
- Presents COALITION framework, which refines smaller LLMs output by the same model
- Conduct experiments 6 LLMs ranging from 3B to 14B on 6 datasets
- Ablation study on components: distinct LLM variants, rationale selection and sample filtration

### Weaknesses
 - One paper might be missing: Mixture-of-Agent (https://arxiv.org/abs/2406.04692) for cross-communication
- In line 196, I believe the utility score alone may not be sufficient in this case. A multi-dimensional evaluation, such as using LLM-as-judge, might be necessary. Additionally, the correctness of the refined generations is unclear, as LLMs often struggle with self-correction (https://openreview.net/forum?id=IkmD3fKBPQ, https://aclanthology.org/2024.findings-acl.826/). The reliance on a single utility score, specifically the likelihood of the ground truth answer, may lead to a bias towards answers that are easily predicted, rather than those that are truly well-reasoned. This could result in the selection of rationales that are superficially aligned with the correct answer but lack genuine depth or robustness. Furthermore, the paper does not adequately explore the potential for error propagation during the refinement process. If the initial rationale is flawed, the subsequent refinement by another variant of the model may not necessarily correct the error, and could instead amplify it, leading to a refined rationale that is even less valid. The paper needs to provide a more thorough analysis of these risks.


### Questions
- In lines 77–78, you mention not relying on "external" LLMs. However, in lines 85–86, you refer to two distinct variants of SLM, which are trained differently. From my perspective, they are essentially no longer the same model. 
- For evaluation, I think one important baseline is missing: self-refine (Madaan et al. 2023, https://openreview.net/forum?id=S37hOerQLB), which uses self-generated feedback to refine the rationales iteratively.

### Soundness
2

### Presentation
3

### Contribution
3
