# PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training

- Decision: Accept
- Avg Score: 7.40
- Scores: 8, 8, 5, 8, 8

## Abstract
This paper aims to address the challenge of hallucinations in Multimodal Large Language Models (MLLMs)  particularly for dense image captioning tasks. To tackle the challenge, we identify the current lack of a metric that finely measures the caption quality in concept level. We hereby introduce HalFscore, a novel metric built upon the language graph and is designed to evaluate both the  accuracy and completeness of dense captions at a
granular level. Additionally, we identify the root cause of hallucination as the model's over-reliance on its language prior. To address this, we propose PerturboLLaVA, which reduces the model's reliance on the language prior by incorporating adversarially perturbed text during training. This method enhances the model's focus on visual inputs, effectively reducing hallucinations and producing accurate, image-grounded descriptions without incurring additional computational overhead.  PerturboLLaVA significantly improves the fidelity of generated captions, outperforming existing approaches in handling multimodal hallucinations and achieving improved performance across general multimodal benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper pointed out the hallucination issue in MLLM, where pretrained linguistic knowledge overshadow the visual information. Therefore, this paper proposes a training strategy by augment the text into the one that conflict with the visual content but still aligns with general knowledge. To quantitize the hallucination in fine-grained fashion, it proposes HalFscore (I actually lol at this wordplay), which uses GPT4-o to generate the two scene graph from the two captions and then use GPT4-o to compare them.

### Strengths
1.	This paper proposes a new metric to evaluate fine-grained hallucination while also validating the metric by analyzing the correlation with human
2.	This paper proposes a training method that is more fundamental than contrastive decoding.
3.	The paper also provides persuasive experiment results indicating that the hallucination is reduced while preserving the original general VL understanding capability.

### Weaknesses
1.	Use GPT-4o as an additional source for perturbation. However, using GPT-o is always expensive on large-scale datasets. I would like to study the impact of the quality of the adversarial language  that is augmented by open-sourced VLMs such as InternVL/QwenVL

### Questions
I would like to study the effect of the size of such adversarially augmented data. Would more of such data be more helpful?

I would like to discuss more deeply about such robustness interrupt. Basically you want to construct the data that is unlikely to be generated purely using language bias, thus able to alleviate the overshadowing of the language knowledge. Can we directly construct this training dataset by asking GPT-o to generate these kinds of questions and answers, which directly achieve the paper's goal, instead of purely doing such perturbing over the given QA data? I am concerned actually this perturbing is decreasing the normal VL understanding capability, but because it reduces the hallucination, the general knowledge evaluation (MMbench) is still good

### Soundness
4

### Presentation
4

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
This paper studies hallucination problem in MLLM, especially on dense captioning task. The authors first propose a new metric that can capture both precision recall based on scene graph parsed by a GPT model. The author then propose a training method PerturboLLava which can reduce the model’s reliance on language prior so that the model can focus more on the visual inputs thus reducing hallucination. The authors show the effectiveness of the proposed method on a selected 1k images from DCI dataset.

### Strengths
Nice ablation on different version of training templates as well as different relevance levels of perturbation.
The proposed method can be combined with other decoding-based methods to further improve performance.
The authors introduce a new well motivated metric and show that it correlates more strongly with human judgment.
The method is conceptually simple and effective, requiring no additional inference cost. It not only enhances dense captioning but also benefits general multimodal capabilities. Although the authors primarily focus on the dense captioning task, the method is not designed with no specificity on captioning but generally aims to help the model focus on image input over language priors.

### Weaknesses
The proposed metric is very similar to SPICE(SPICE: Semantic Propositional Image Caption Evaluation) however the authors do not mention this related work. The main difference is SPICE is using a traditional parser but this paper uses GPT. I hope the authors can add the comparison against SPICE.

I think figure 1 is not super accurate. The authors do use extra data (although augmented from existing data), and also the longer training examples will lead to extra training cost as well.

Having Section 4.2 is good, but I have some concern. I do think equation 5-10 holds, but I think the explanation following the equations is problematic. “During the training of multimodal models, we can assume that the world knowledge embedded in the language model remains unchanged, so p(xk|xp<k) is a perturbation term that cannot be optimized. Therefore, in the training process of multimodal models, our perturbation training method guides the model to optimize towards p(xk|x−p<k,I), transforming it into a fully multimodal model that is unaffected by language priors and relies entirely on image information to answer questions.”
- The statement here holds no matter with or without perturbation.
- My own explanation is, for cross entropy loss, if the model already predicts well, the gradient will be low so the model wouldn’t pay much attention to this token. Without the perturbation, the prior term can already predicts well, so the gradient is low. With the perturbation, the prior term is perturbed to be low, so the gradient is high for the unprior term.
- Essentially originally, for a caption, the tokens that can be inferred from language prior will have less effect on parameter gradients whereas now the gradient is kind of balanced across tokens.

### Questions
- In table4,5 the authors show different variants of perturbative visual training. I am wondering if the authors try combining these different versions.
- The training and inference has some discrepancy where training has the perturbation as input but inference does not. Why this kind of discrepancy is not an issue?
- The metric highly rely on the scene graph representation. What are the limitations of this representation?
- Is there analysis on how good the gpt4 model perform perturbation task?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an evaluation metric called HalFscore to measure the fine-grained image captioning quality in terms of object, attribute, and relation hallucinations. The authors also propose a method to reduce hallucinations by injecting generated perturbation text into training prompts and show that it helps reduce the hallucination compared to several baselines.

### Strengths
1. The proposed hallucination metric HalFscore is straightforward but helpful in detecting fine-grained hallucination in terms of objects, attributes, and relations.
2. Based on perturbation text, the proposed training framework PerturboLLaVA forces the model to balance the image content and language prior, avoiding generating hallucinated text in fine-grained captions.

### Weaknesses
Both HalFscore and PertuboLLaVA are pretty straightforward. PerturboLLaVA is a simple prompting technique to revise the text prompts for model finetuning. The results are mixed, and there are still performance gaps compared to recent models based on advanced language models like Qwen2 and LLama3.

### Questions
Questions:
Can you provide more details on the inconsistent results of RLAI-F in Table 3 between Object HalBench (CHAIRs and CHAIRi) and HalBench?
Comments:
Lines 430, 463: The results in "Table 2"... --> Should be "Table 3"

### Soundness
3

### Presentation
3

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
This paper aims to address the issue of hallucination in current multimodal large language models applied to dense image captioning tasks. The authors argue that there is no appropriate metric for evaluating the hallucinations in this context. To address this gap, they introduce HalFscore, a metric based on a language graph that assesses both the accuracy and completeness of dense captions. Additionally, they propose the incorporation of perturbed text to alleviate the over-reliance of language-prior issue, thereby mitigating the hallucination issue. Experimental results on several general multimodal benchmarks demonstrate the effectiveness of their approach.

### Strengths
1. The proposed PerturboLLaVA is simple, interesting and effective. By modifying the original training data without employing additional training techniques or supplementary data, this method effectively addresses the hallucination issue when compared to the baseline LLaVA-1.5 (Table 2 & Table 3).

### Weaknesses
1. Defination of dense captioning task is unclear: 
As noted in Lines 012 and 038, this paper focuses on addressing the hallucination problem in dense captioning tasks. The authors reference [1] and [2], both of them are related to dense captioning tasks. However, the definitions of dense captioning tasks in [1] and [2] differ from those presented in this paper. Additionally, this paper does not conduct standard evaluations for these tasks as outlined in [1] and [2]. It remains unclear whether this discrepancy constitutes a citation issue, and the authors should provide clarification on this matter.

[1] DenseCap: Fully Convolutional Localization Networks for Dense Captioning, 2016.
[2] Context and attribute grounded dense captioning, 2019.

2. No comparison between HalFscore and existing methods:
The authors solely rely on user studies to justify the effectiveness of the proposed metric. However, they do not provide a comparison with existing metrics. One commonly used baseline is to using gpt-score as evaluation metric (e.g., [3])

[3] LLaVA-RLHF: Aligning Large Multimodal Models with Factually Augmented RLHF, 2023.


3. Additional training cost compare with existing methods.

The methods need to re-train the whole model and cost more training time (the training samples are longer).

4. No evaluation on stronger models.

The paper conducts experiments solely on LLaVA-1.5, which is publicly available as of 2023. More recent and stronger models, such as LLaVA-Next, Intern VL-1.5, and LLaVA-UHD, are not evaluated. It is recommended that the authors include at least one of these recent models to demonstrate the effectiveness of their methods.

### Questions
Please refer to weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper has two main contributions: (1) Introducing an evaluation pipeline for dense image captioning, HalFscore, that measures the quality of dense caption more holistically by constructing a language graph and computing the precision and recall. (2) Introducing an adversarial augmentation method during training that reduces the reliance on language prior, which reduces hallucination.

### Strengths
1. This paper addresses a significant gap in the current evaluation of MLLMs
2. The augmentation method is intuitive, and shows nice improvements in the benchmarks checked
3. The authors conduct extensive experiments to demonstrate the effectiveness of the augmentation method

### Weaknesses
1. Regarding the human survey, it is unclear to me who the human raters are (the authors, Amazon Mechanical Turk Workers, etc.)
2. Since all the experiments are done on LLaVA-1.5, it is unclear what the effect of the perturbation method on stronger models
3. Seems like [1] is also a relevant related work, they also suggest a method for dense image captioning evaluation based on precision and recall.

### Questions
If the annotators are from Amazon Mechanical Turk, how were they recruited? 
If the annotators reported in the paper are the authors, could you also add a comparison with external annotators?

### Soundness
3

### Presentation
3

### Contribution
3
