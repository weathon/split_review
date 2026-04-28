# UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
We present UniDetox, a universally applicable method designed to mitigate toxicity across various large language models (LLMs).
Previous detoxification methods are typically model-specific, addressing only individual models or model families, and require careful hyperparameter tuning due to the trade-off between detoxification efficacy and language modeling performance. 
In contrast, UniDetox provides a detoxification technique that can be universally applied to a wide range of LLMs without the need for separate model-specific tuning. 
Specifically, we propose a novel and efficient dataset distillation technique for detoxification using contrastive decoding. 
This approach distills detoxifying representations in the form of synthetic text data, enabling universal detoxification of any LLM through fine-tuning with the distilled text. 
Our experiments demonstrate that the detoxifying text distilled from GPT-2 can effectively detoxify larger models, including OPT, Falcon, and LLaMA-2. 
Furthermore, UniDetox eliminates the need for separate hyperparameter tuning for each model, as a single hyperparameter configuration can be seamlessly applied across different models. 
Additionally, analysis of the detoxifying text reveals a reduction in politically biased content, providing insights into the attributes necessary for effective detoxification of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces UniDetox, a universal detoxification method for LLMs that avoids model-specific tuning by generating detoxifying text via dataset distillation with contrastive decoding. This distilled text derived from GPT-2 can detoxify other models like LLaMA-2 without additional hyperparameter adjustments. Experiments validate UniDetox's ability to mitigate toxicity and reduce political bias consistently across models. The paper also discusses insights into the features necessary for detoxification.

### Strengths
- Proposes a universally applicable detoxification approach, addressing limitations of existing model-specific methods by utilizing dataset distillation.
- Provides a theoretical basis by aligning detoxification with the direction opposite to a "toxic vector" in model parameter space (Sec. 2.2, Eq. 5)
- Reduces the need for model-specific hyperparameter tuning, as evidenced by successful application to different models with consistent results with a single hyperparameter configuration.

### Weaknesses
 - The paper lacks a comparison with alternative alignment algorithms such as DPO or other detoxification baselines using task arithmetic between a base model and a tuned model, such as [1][2].
- Although UNIDETOX is free from downstream model-specific hyperparameter tuning, results are sensitive to the selected learning rate and α parameters (Section 3.4). The need for different UNIDETOX configurations impacting performance lacks sufficient justification or analysis.
- UniDetox demonstrates a drop in diversity metrics compared to other methods. A broader evaluation on other LM tasks would help validate its capability to preserve language quality.

### Questions
- Would the authors provide examples of the distilled detoxifying text for tuning? This would help clarify the properties and coherence of the distilled data.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
UniDetox proposes a framework for the detoxification of Language Models via a three-step process.
* Step 1 : Create a Toxic Model
* Step 2 : Distill Detoxifying Text
* Step 3 : Finetune on Detoxifying Text

It is valuable in that it proposes a way to detoxify LLMs in an efficient manner and also show that the steps till Step 2, could be independent of the actual model. 
This is very favorable as models are getting larger and detoxifying them with common methods like task vectors can get computationally expensive (since they involve training another model of identical specs)

### Strengths
* Definitely an interesting idea combining the core principles of task arithmetic and dataset distillation (i.e  showing that fine-tuning on data from a specific distribution also pivots a model’s representation internally in that direction and applying it to the toxicity setting) 
* The idea that detoxifying text can be independent of the final model and can come from a smaller model is also favorable
* Their baseline approach also contains the straightforward “prompt” variants which is a useful data point for comparison as models get more powerful.

### Weaknesses
I would like to list the following weakness fully ensuring the authors that I am not unreasonable and am completely open to increasing my score if these are addressed/answered satisfactorily.

* The related section definitely lacks coverage of methods that are available for detoxification. Few of them include : Parameter-Efficient Detoxification with Contrastive Decoding, etc
* There is a lack in comparison with more recent methods. An efficient method to benchmark against would be the cited LM Steering work(Han et al)
* Most work in Detoxification uses the Perspective API in their evaluations, but it has been omitted here without any explanation. 
* An example of what the generated“detoxifying” text looks like would help. Is this just “non-toxic” text ? Or does it have other interesting lexical properties? Some more analysis would be welcome here( even if in the appendix)

### Questions
* Very curious to know why recent methods weren’t benchmarked against?
* Is there an obvious reason the Perspective API wasn’t used ?

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
5

### Summary
This work proposes an approach to detoxify LLMs via fine-tuning (UniDetox), with the novelty of using dataset-distilled exemplars. The authors propose to distill datasets using contrastive decoding. An analysis based in fine-tuning gradients is provided, showing that the proposed fine-tuning strategy is indeed moving the model weights in the opposite direction of the toxicity vector. UniDetox requires (1) fine-tuning a base model (B) to be toxic, obtaining model (T), (2) obtaining distilled text with contrastive decoding according to (B-T) and (3) fine-tuning a target model with such data. The authors claim that the obtained data and fine-tuning parameters are universal (i.e. can be applied to any LLM). 
Experiments show better toxicity mitigation than DExperts (Liu et al. 2021) on the source GPT2 model, as well as on other LLMs that are fine-tuned with distilled data using GPT2. Additionally, perplexity and n-gram metrics are provided as proxies for fluency.

### Strengths
**Originality:**

* Using dataset distillation in the setting of LLMs in an actionable way is original, to the best of my knowledge.
* The use of contrastive decoding is also an interesting aspect of this work.

**Clarity:**

* The paper is well written, with clear language. The mathematical notation and formulation is also clear and easy to follow. The figures are also self-explanatory and provide good insights on the work.

**Significance:**

* Toxicity mitigation is an extremely important topic, this work can be of interest to the community. However, see weaknesses and questions for suggestions on how to increase the impact.

### Weaknesses
 **Quality:**

*   The experimental setup can be improved to convince the community about the validity of the proposed method. I suggest the authors to include some zer/few-shot metrics (eg. MMLU) to understand how the model abilities are impacted. I also have concerns about the perplexity reported and the performance on OOD data (see questions).
*   Ablations:
    *   The proposed method has an important hyper-parameter $\lambda$. I missed an ablation study on $\lambda$, showing the impact of this choice in the final performance. 
    *   The amount of data produced via distillation is of great importance. Can the authors discuss about the data required for UniDetox to be effective? Additionally, I would be really curious in seeing some of the distilled sentences produced by UniDetox, as well as examples generated by the detoxified model. Such qualitative results can help the reader understand the method.

**Clarity:**

*   I kindly ask the authors to provide the steps followed to derive the Taylor approximation in Eq. 5 (from $s(x)$ in Eq. 1.

**Significance:**

*   The evaluation proposed (methods compared) and metrics (ppl, n-gram) are too weak given the current abilities of LLMs and the thorough evaluations many works provide nowadays.

### Questions
* In Section 3.1, I encourage the authors to include some metric related to zero/few-shot abilities. For example, the overall score in MMLU seems a good candidate.

* Results in Table 1. I have some concerns about the methods used for comparison. Although DExperts was a successful method when it was proposed, several methods have shown superior performance in recent years. For example, [SuauICML24] proposes a method to reduce toxicity without any inference cost and not requiring fine-tuning, showing superior performance compared to DExperts or pre-prompting. Similarly, [PozzobonEMNLP23] propose an efficient method for toxicity mitigation.  I encourage the authors to consider comparing with some newer method than DExperts, this work's imact could strongly benefit from that.
I also suggest adding these recent methods in the Related Work.

> [SuauICML24] Suau, X., Delobelle, P., Metcalf, K., Joulin, A., Apostoloff, N., Zappella, L., & Rodríguez, P. (2024). Whispering experts: Neural interventions for toxicity mitigation in language models. ICML 2024.

> [PozzobonEMNLP23] Pozzobon, Luiza, et al. "Goodtriever: Adaptive toxicity mitigation with retrieval-augmented models." EMNLP 2023 Findings.

* Results in Table 1. Could the authors comment on the fact that PPL goes down from 17.28 to 12.23 when using UniDetox? To me, this behavior is counterintuitive, since the PPL of a LLM rarely goes down when one intervenes on the LLM. In this case, fine-tuning on distilled data is an intervention on the original model. It is surprising that fine-tuning on a small synthetic dataset brings the LLM perplexity to 12.23 (which would be the PPL of a much larger/stronger LLM).
I encourage the authors to provide details about the PPL evaluation, and a conclusive justification of why such PPLs are strongly decreasing. 

  * Additinally, in Table 2, UniDetox reduces PPL for OPT, Falcon and increases PPL for LLama2. Conversely, using lr=1e-5, the PPL strongly increases for OPT, Falcon and decreases for LLama2. This hints that the fine-tuning parameters and/or distilled data are not _universal_ but rather well suited for the combinations of parameters and models chosen.

* Results in Table 1. Why is OOD toxicity reduction stronger than ID reduction? I would have expected a fine-tuning based approach like UniDetox to be much more effective on ID. Could the authors comment on this aspect? 

* Results in Table 1. For the safety preprompt to be effective, have the authors considered evaluating an instruction-tuned model such as gemma-2-2b-it? I believe safety preprompts are much better designed for instruction tuned models than for decoder only (and arguably older) models like GPT2. 

**Comments**:

* This work has some interesting proposals such as using dataset distillation to address model alignment. However, the _universality_ claims are only validated using a small number of models and a non-comprehensive set of metrics. I find very confusing the fact that PPL strongly decreases when the intervention is applied. Moreover, details about the choice of $\lambda$ and the data produced are lacking. Considering all the above, I cannot recommend this paper for acceptance as is, however, I am open to reconsider my score upon rebuttal.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The research presents a novel and universally applicable detoxification approach to a wide range of language models without the prior understanding or fine-tuning of the specific hyperparameters and architectures. The work introduces an efficient data distillation method by incorporating contrastive decoding, which helps to identify the toxicity vector within the initial parameter space and generate detoxifying text sets. Later, the language model is fine-tuned on the distilled datasets to mitigate the toxicity in the base language model. The approach was evaluated and analyzed based on various baseline methods and UniDetox to understand the technique's effectiveness. Overall, the method, UniDetox, introduces a novel data distillation algorithm with contrastive decoding to significantly mitigate the level of toxicity in the base language models.

### Strengths
The work provides a novel approach and insights into the following points 
1. Novel dataset distillation method using contrastive decoding
2. Complete evaluation across a range of commonly used detoxification methods from the references 
3. Significant results based on the PT and EMT metrics across different benchmarks

As for the paper, the strengths are
1. Well-structured and written paper
2. Well-styled and formatted paper
3. Thoughtful introduction and rigorous reasoning

### Weaknesses
1. The size of the model might mitigate UniDetox's effectiveness since the ratio of parameter space and the volume of detoxifying text might be increased significantly, and no further preventive techniques could be introduced.
2. Compared to other methods, UniDetox still requires model fine-tuning to mitigate the toxicity from the base models, making this approach's computational intensity a further challenge or question to understand.
3. Limited to the text-only language models, as the emerging traction of multi-modal language models, how this approach further mitigates toxicity with a vast data modality remains challenging to this technique.

### Questions
The following points suggest further investigation and evaluation of this method's potential weaknesses or limitations.
1. Does this method apply to the scope beyond the text-only model? Can this approach apply to the multimodal language models as well?
2. What are the costs regarding the computational resources, time required, or other considerations?
3. What is the impact of the larger parameters space, like using larger models from 14B to even 405B models, on the small set of detoxifying text?

### Soundness
3

### Presentation
4

### Contribution
3
