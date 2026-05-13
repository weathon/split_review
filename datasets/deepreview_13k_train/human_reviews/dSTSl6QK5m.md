# Enhancing Trust in Large Language Models with Uncertainty-Aware Fine-Tuning

- Decision: Reject
- Scores: 5, 5, 3, 6, 6

## Abstract
Large language models (LLMs) have revolutionized the field of natural language processing with their impressive reasoning and question-answering capabilities. However, these models are sometimes prone to generating credible-sounding but incorrect information, a phenomenon known as LLM hallucinations. Reliable uncertainty estimation in LLMs is essential for fostering trust in their generated responses and serves as a critical tool for the detection and prevention of erroneous or hallucinated outputs. To achieve reliable and well-calibrated uncertainty quantification in open-ended and free-form natural language generation, we propose an uncertainty-aware fine-tuning approach for LLMs. This approach enhances the model's ability to provide reliable uncertainty estimates without compromising accuracy, thereby guiding them to produce more trustworthy responses. We introduce a novel uncertainty-aware causal language modeling loss function, grounded in the principles of decision theory. Through rigorous evaluation on multiple free-form question-answering datasets and models, we demonstrate that our uncertainty-aware fine-tuning approach yields better calibrated uncertainty estimates in natural language generation tasks than fine-tuning with the standard causal language modeling loss. Furthermore, the experimental results show that the proposed method significantly improves the model's ability to detect hallucinations and identify out-of-domain prompts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to equip LLMs with the capability to generate natural language text along with reliable uncertainty estimates. The authors propose an uncertainty-aware language modeling loss focused on a key objective: increasing uncertainty for incorrect token predictions while optimizing for both accuracy and confidence in correct token predictions. They evaluated the uncertainty estimation of LLMs trained with this loss on tasks such as hallucination detection, uncertainty-guided selective generation, and out-of-domain detection. Compared to standard LLMs, the proposed method improves hallucination detection performance while maintaining similar QA accuracy.

### Strengths
* This paper is well written and very easy to follow.
* The proposed method, targeting QA and VQA tasks, appears effective for fine-tuning single-task LLMs when a sufficient amount of fine-tuning data is available.
* It is very meaningful to study the model’s uncertainty on its own response.

### Weaknesses
 * **The experimental setup is very limited**: The experiments were conducted on single-task LLMs with enough fine-tuning data, which may be somewhat restrictive in the current LLM era. I am interested in seeing how effective the proposed approach would be in low-resource settings and in multi-task fine-tuning scenarios. Specifically, the paper lacks experiments that demonstrate the method's effectiveness when fine-tuning data is scarce, or when the model is adapted to multiple tasks simultaneously. The current experiments only show results on single tasks with sufficient data, which does not reflect the common use case of LLMs.
* **Insufficient critical technical details**: It is unclear what tokens are included in $\widetilde{C}$ and how many there are. The paper mentions that $\widetilde{C}$ includes incorrectly predicted tokens, but it does not specify how these tokens are identified during training. Are they determined based on the top-1 prediction or a broader set of possible incorrect tokens? The lack of clarity on this point makes it difficult to reproduce the results.
* **Missing latency analysis**: I am interested in seeing the change in latency (training time) introduced by the proposed approach. The paper does not include any analysis of the computational overhead of the proposed uncertainty-aware loss function. This is a critical aspect, as any increase in training time could limit the practical applicability of the method, especially when dealing with large models.

### Questions
This might be a naïve question, but in Eq2, should $P(w_i|w_{0:i-1})$ be in the correct tokens part, and the $1- P(w_i|w_{0:i-1})$ be in the incorrect part? Apologies if I misunderstood.

### Soundness
3

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
4

### Summary
This paper proposes an uncertainty-aware objective function for causal language model (LM) optimization. The loss encourages the predicted token distribution to have high certainty (low entropy) for correctly predicted tokens and low certainty (high entropy) for incorrectly predicted tokens. Experiments show fine-tuning LMs with the proposed objective leads to improved uncertainty estimates when combined with commonly used uncertainty estimators (mean token entropy, perplexity, predictive entropy, semantic entropy) in several freeform short answer settings.

### Strengths
1. The proposed objective is straightforward and simple to adopt in existing frameworks and codebases.
2. Numerous experiments are presented that assess the reliability of LM confidence estimates in several scenarios. This includes hallucination detection (AUROC), selective generation (AUARC), and detecting out-of-domain queries. The ability of the proposed loss to improve uncertainty estimates under several estimators is compelling.
3. Experiments are conducted with LMs and VLMs demonstrating the generality of the proposed loss.

### Weaknesses
1. In NLG settings, uncertainty can arise for other reasons than a lack of answer confidence such as semantic equivalence of different paraphrases. Both would appear as incorrect token predictions and are therefore handled identically within the proposed loss. It is plausible that this could lead to significantly degraded performance in longer-form settings due to increasing entropy when only a few options are plausible. Unfortunately, all experiments are in short-form QA settings, leaving this issue unaddressed. This is a significant gap given the motivation to "achieve reliable and well-calibrated uncertainty quantification in open-ended and free-form natural language generation".
2. No alternative fine-tuning baselines are presented. All experiments compare standard fine-tuning to fine-tuning LMs using the proposed loss. This makes it difficult to understand the effectiveness of the proposed approach amidst alternatives from the literature. The post-hoc rescaling works (cited in the paper) appear to be at least one source of reasonable baseline. Other reasonable baselines include simply not computing loss over "incorrect tokens", or applying unlikelihood training to incorrectly predicted tokens, a method that appears closely related to the current work [1]. Alternative lines of closely related work detect hallucinations with probes [2, 3], directly fine-tune LMs to abstain when uncertain [4, 5], or fine-tune LMs to provide calibrated linguistic statements of confidence [6]. In many settings, it may be more useful to have LMs confidently abstain as opposed to outputting high-entropy token distribution, a trade-off that is not discussed in this work.
3. Key details of the proposed loss function are unclear. In particular, the paper does not provide a precise definition of an "incorrect token prediction," a core element of the approach. My assumption is these are tokens where the argmax of the predicted distribution is not equal to the ground truth, but I'm unsure. Other choices should also be more clearly motivated. Is there a particular reason to use tanh over other functions mapping to [0, 1] such as x / (1 + x)? In general, a more detailed analysis of the proposed loss would be beneficial and aid understanding. Examples include visualizations of the ranges of the loss over correctly and incorrectly predicted tokens and analysis of gradients and their analytic form.

### Questions
1.  Does the proposed loss degrade performance in longer-form settings?
2.  How does the proposed approach compare to alternative methods like probes and fine-tuning LMs to abstain?
3.  Does removing incorrect generations have similar effects due to not fine-tuning LMs to be confident in these tokens?
4. Is there a motivation for tanh over alternatives?

**Edit: Post Author Response**

I have reviewed the author's response. Many of my questions have been addressed and I have raised my score accordingly. 
My primary remaining concern is that the experiments do not demonstrate the approach generalizes beyond short-form QA settings where quality may be significantly impacted by increased entropy.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a fine-tuning approach to better calibrate language models with their uncertainty levels. Specifically, they introduce an uncertainty-aware objective that encourages models to associate high uncertainty with incorrect token predictions and low uncertainty with correct predictions.  The authors experiment with their fine-tuned models with hallucination detection, selective generation, and out-of-domain detection tasks on CoQA, TriviaQA, and OK-VQA datasets. They show that uncertainty-aware model tuning can provide more reliable uncertainty estimates than standard fine-tuning and improves alignment between uncertainty estimates and response quality.

### Strengths
1. The proposed training objective (UA-CLM loss function) shows improved uncertainty estimation in terms of token entropy, perplexity, predictive entropy, and semantic entropy compared to standard fine-tuning.
2. The set of metrics they chose for the experiment is comprehensive, and the gap between the uncertainty-aware and standard fine-tuning is notable.
3. They performed experiments to show the new objective does not negatively impact the generation quality (compared to standard fine-tuning).

### Weaknesses
1. This paper lacks a comprehensive literature review, and several claims are unsupported. For instance, the paper does not mention existing works on calibration in long-form language model generations, while many relevant studies exist (e.g., https://arxiv.org/pdf/2310.19208, https://arxiv.org/abs/2404.00474). Additionally, “confabulation” is presented as a subcategory of hallucinations, though it is replacing the hallucination term as it better describes a model’s state of fabricating inaccuracies from a clinical perspective. The authors state they are focusing on confabulation but do not specify which aspects of hallucinations they are addressing, so clarifying the definition and usage of "confabulation" in the context of their work is helpful. Also, they assert that LLMs are often poorly calibrated, though larger models have shown improved calibration compared to smaller ones (https://arxiv.org/abs/2207.05221). Finally, Supervised fine-tuning (SFT) may exacerbate hallucinations not only through overfitting but also due to potential conflicts between the SFT data and the model’s pre-existing knowledge, leading to further inconsistencies. Overall, a more thorough literature review and attention to the accuracy of statements would benefit the paper.
2. The paper only compares the UA fine-tuned models with standard fine-tuned models and does not conduct comparisons with the vanilla, pre-fine-tuning model. So, including comparisons with the pre-fine-tuning model as an additional baseline could be helpful.
3. The experiments do not clarify how token-level labels were assigned for long-form generation tasks. For instance, while TriviaQA is a short-form QA task, models often generate lengthy answers. It is unclear whether target answers in fine-tuning were based on raw dataset responses or if adjustments were made to adapt these answers to LM-style outputs. Please provide more details on their data preparation process, specifically how different responses at different lengths have been handled.
4. The tuned model should be evaluated across additional capabilities, such as reasoning, creative writing, and coding, to ensure these skills are unaffected by the proposed technique; such experiments are currently missing.
5. The BioASK dataset is used for the out-of-domain detection task, but it is unclear if this data is truly out of the models' training knowledge or if it was part of the pre-training data and how this can affect the findings. Providing information on how authors verified that the BioASK dataset was indeed out-of-domain for their models could be helpful.

### Questions
Please refer to the weaknesses section for the questions and clarifications requested.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes uncertainty-aware fine-tuning as a method to increase the reliability of existing uncertainty quantification metrics. The method is simple, unlike negative log-likelihood (or cross-entropy), by distinguishing correct tokens and incorrect tokens and adding a loss term for entropy in the optimization objective, it can lower predictive uncertainty in the case of correct tokens and vice versa. With this objective, language models and even vision language models are fine-tuned and compared with standard fine-tuned models, on existing entropy based uncertainty metrics, such as token entropy, perplexity, predictive entropy and semantic entropy.

### Strengths
By designing uncertainty loss based on decision theory, it ensures the loss can theoretically converge to 0, leading to improved performance of general entropy-based metrics without compromising accuracy.
The authors provide rigorous evaluations across multiple question-answering datasets, showcasing the method’s efficacy in various contexts. These experimental results demonstrate that the uncertainty-aware fine-tuning improves in four aspects, hallucination detection, selective generation, out-of-prompt detection and calibration analysis.

### Weaknesses
The authors said that (Rouge-L >0.3) was used to measure accuracy as same as (Khun et al., 2023). However, as also pointed out in the previous work, the Rouge-L score is a very brittle metric, and unlike the previous work that only draw curves according to temperature, this paper needs to capture the trade-off between accuracy and uncertainty calibration. As shown in Table 2, we can see that the accuracy of UA-CLM is higher than that of CLM except for Gemma, which is quite weird because the authors mention the trade-off. The reason for this is not adequately explained.

It is also unclear how the uncertainty loss is weighted against the standard language modeling loss. The paper mentions adding a loss term for entropy, but without a clear hyperparameter controlling the balance between the two, it's difficult to understand how the model avoids simply optimizing for lower entropy at the expense of accuracy. This is particularly concerning given the observation that UA-CLM sometimes achieves higher accuracy than CLM, which suggests the uncertainty loss might be inadvertently improving accuracy rather than just improving uncertainty calibration. The lack of ablation studies on this hyperparameter is a significant weakness.

### Questions
Are there any experimental results conducted using standard fine-tuning other than LoRA? (or any other PEFT methods, such as prompt tuning.)

Looking at the loss term alone, there seems to be problems like longer training time or faster loss convergence. Are there any reports on these?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new approach to align the confidence and accuracy of causal (auto-regressive) large language models. This approach is based on low-rank fine-tuning, adding a component to the fine-tuning loss that incorporates not only the auto-regressive negative log likelihood but also aligns token entropy with prediction accuracy. In other words, this new objective for fine-tuning large language models aligns their prediction accuracy with the uncertainty. The paper presents experiments using various LLMs, such as Llama and Gemma, and evaluates the approach on tasks like hallucination detection, selective generation, out-of-prompt detection, and visual question answering. The results show effective compared to baseline LLMs.

### Strengths
The paper is written very clearly. 
The related literature review is thorough and nicely structured. 
The proposed loss and the corresponding optimization with two objectives of optimizing accuracy as well as aligning the accuracy with confidence is a sound and interesting idea.  
The results compared to the baseline LLMs on the datasets and with selected metrics show very effective.

### Weaknesses
--While the approach looks effective empirically, the results have not been compared to the related work. For example some of your QA benchmarks overlap with [2] but there is no comparisons made. This makes it hard to see how the proposed technique is compared to other existing techniques for the same purpose.  Can you clarify further on this issue? 

--Can you clarify, why the expected calibration error ECE is not reported? [see this paper that reports ECE [1]] 

--It will be useful to define the evaluation metrics, their motivation, and how those are computed. This will make the paper self-contained for its major concepts. 
--Related to the above question, it wasn’t clear to me how we would solicit the model's uncertainty for each instance, for example,  in the QA setting? do you compute H?

### Questions
See above.

### Soundness
3

### Presentation
4

### Contribution
3
