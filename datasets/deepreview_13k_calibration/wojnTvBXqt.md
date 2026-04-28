# Learning to Rewrite: Generalized Detection of LLM-Generated Text

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Large language models (LLMs) present significant risks when used to generate non-factual content and spread disinformation at scale. Detecting such LLM-generated content is crucial, yet current detectors often struggle to generalize in open-world contexts. We introduce **Learning2Rewrite**, a novel framework for detecting AI-generated text with exceptional generalization to unseen domains. Our method leverages the insight that LLMs inherently modify AI-generated content less than human-written text when tasked with rewriting. By training LLMs to minimize alterations on AI-generated inputs, we amplify this disparity, yielding a more distinguishable and generalizable edit distance across diverse text distributions. Extensive experiments on data from 21 independent domains and four major LLMs (GPT-3.5, GPT-4, Gemini, and Llama-3) demonstrate that our detector outperforms state-of-the-art detection methods by up to 23.04% in AUROC for in-distribution tests, 37.26% for out-of-distribution tests, and 48.66% under adversarial attacks. Our unique training objective ensures better generalizability compared to directly training for classification, when leveraging the same amount of learned parameters. Our findings suggest that reinforcing LLMs’ inherent rewriting tendencies offers a robust and scalable solution for detecting AI-generated text.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a novel method, coined Learning2Rewrite, which employs an LLM to rewrite an input text and determines whether it is written by human or a generative model based on the differences between the original text and the rewrite. Instead of training a classifier, it enhances an LLM in such a way that it makes few edits if a text is written by a model, while makes substantial edits if a text is written by human. Their experiments on data from 21 domains demonstrate the effectiveness of this approach.

### Strengths
* The proposed method is simple and effective.
* The experiments mitigate potential domain bias by covering the data in 21 domains.
* Most parts of the manuscript are easy-to-follow.
* There are nice illustrations, such as Figure 1, which help understand the key ideas.
* The examples in Figure 2 are great qualitative examples for understanding the effectiveness of the method.
* It is great to consider dfferences between prompts in the experiments.

### Weaknesses
 * It lacks of an ablation study to justify the effectiveness of the calibration loss. 
* It is unclear to me to what extend the fine-tuning is useful. I cannot find the details of Llama Rewrite so that it is not clear how well the fine-tuned model is compared with the one without fine tuning.


### Questions
* Why edit distance is choosen for similarity comparision? Why not use the other similarity measures, e.g. MAUVE?
* Is the proposed method model agnostic? It would be great to learn if the proposed method is applicable to the other model families.
* Table 2 shows that Llama L2R performs better than Llama Rewrite only with reduced parameters in the OOD setting. How does the OOD performance vary across domains?

### Soundness
3

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
4

### Summary
This paper proposes the L2R framework for detecting AI-generated text, leveraging the insight that LLMs inherently modify AI-generated content less than human-written text when tasked with rewriting. By fine-tuning an LLM to amplify this tendency, the L2R framework demonstrates significantly improved performance across diverse domains and even under adversarial conditions.

### Strengths
- The paper is clear and easy to follow. 
- The approach of using LLM edit distance to detect AI-generated text is innovative. 
- The experiments demonstrate the method’s strong performance and robustness to some extent.

### Weaknesses
(1) The motivation behind the dataset collection process is unclear. Although the proposed dataset spans various domains, it is flawed because the AI-generated text is initially written by humans and then revised by an LLM—similar to a non-native speaker using AI to polish their writing. While detecting AI-generated content is important, I believe using LLMs specifically to rewrite text is one of the less risky applications. Thus, I’m not convinced that this dataset adds substantial value for benchmarking models that detect LLM-generated content.

(2) The superior performance of Llama logits on ID setting, and its poor performance on OOD setting confirms that there’s a gap between the dataset built by the authors and the real-world scenario of LLM-generated content detection. (The ID performance of Llama logits is also skipped in Table 1).

(3) I would recommend the authors to compare L2R with baseline methods on conventional datasets such as XSum, SQuAD, and WritingPrompts; due to the dataset proposed in the paper only contains LLM rewritten text.

### Questions
(4) Would you explain why the Fast-DetectGPT performance drops so much on OOD examples, since it doesn’t require any training?

(5) In DetectGPT paper, their hypothesis is 
> Minor rewrites of model-generated text tend to have lower log probability un- der the model than the original sample, while minor rewrites of human-written text may have higher or lower log prob- ability than the original sample.

Do your findings agree or contradict with their hypothesis?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Learning2Rewrite (L2R) is an innovative framework for detecting AI-generated text by exploiting LLMs' tendency to modify human-written content more extensively than AI-generated text during rewriting. The framework's core innovation lies in its training objective, which minimizes edits on AI-generated text while maximizing changes to human-written content, creating a clear classification boundary. A calibration loss mechanism prevents overfitting and ensures stable performance across domains.

Comprehensive evaluations across 21 domains using GPT-3.5, GPT-4, Gemini, and Llama-3 demonstrate L2R's effectiveness. It surpasses existing detectors like RAIDAR and Fast-DetectGPT with up to 23.04% higher AUROC in in-distribution tests and 37.26% in out-of-distribution scenarios. The framework is robust against adversarial attacks and effective generalization to new domains, validated through a diverse evaluation dataset that serves as a reliable benchmark for AI text detection methods.

### Strengths
**Originality**: L2R introduces two key innovations in AI text detection: using LLMs' rewriting behaviour as a detection mechanism rather than traditional classification and implementing a training objective that minimizes AI text edits while maximizing human text edits. Enhanced by a calibration loss mechanism, this approach offers a fundamentally new way to distinguish between human and AI-generated content.

**Quality**: The evaluation spans 21 domains using GPT-3.5, GPT-4, Gemini, and Llama-3, with L2R outperforming RAIDAR and Fast-DetectGPT on both in-distribution and out-of-distribution tasks. The method is robust against adversarial attacks, and its effectiveness is validated through comprehensive ablation studies examining parameter impacts and training configurations.

**Clarity**: The paper presents its technical contributions precisely and clearly. The methodology and training objectives are thoroughly documented and supported by illustrative visualizations of edit distance distributions. The experimental setup and results are systematically organized, providing clear evidence for the method's performance.

**Significance**: L2R advances AI text detection through improved cross-domain generalization and adversarial robustness. Its interpretable detection mechanism and practical effectiveness in identifying AI-generated content make it particularly valuable for real-world applications in misinformation detection.

Overall, I like this paper's approach, which presents an elegant and effective solution for AI text detection.

### Weaknesses
 - The paper's robustness evaluation, while covering decoherence and rewriting attacks, could benefit from exploring more adversarial scenarios. Testing against AI text modified by advanced paraphrasing tools or examining mixed human-AI content would provide deeper insights into L2R's limitations.

- Moreover, while L2R's success relies on diverse training data and prompt variations, the paper would benefit from an analysis of how reduced data diversity affects its performance.

- The method appears limited in handling cases involving mixed human and AI-authored text, where the task is to identify specific AI-generated segments. This limitation could be significant, as human-AI collaborative writing is increasingly common. Addressing this challenge would broaden the method's applicability and practical value.

### Questions
How does the calibration loss mechanism specifically prevent overfitting compared to standard training? While Figure 4 in the appendix illustrates training loss behavior, how does this confirm the effectiveness of the calibration loss? Shouldn't the impact of preventing overfitting be more evident in the experiments on out-of-distribution test set performance, with or without the use of calibration loss?

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
5

### Summary
The paper introduces a novel method for detection of AI-generated text. The method involves finetuning a LLaMA 8B model to rewrite its input text such that human-written text gets rewritten quite a lot and AI-generated text gets re-written very little. At inference time, by thesholding the normalized Levenshtein distance between the input text sequence and the sequence outputted by the finetuned LLaMA, a prediction is made of either "AI-generated" or "human-written." In experiments, this method outperforms baseline approaches.

### Strengths
The problem of detection of AI-generated text is very important, and the proposed method tackling it is not one I had seen before. The method is described in sufficient detail I could probably reproduce the main ideas.

### Weaknesses
## Weaknesses of the Proposed Method
1. I am concerned with how expensive the proposed method is. Doing hundreds of tokens of generation using an 8B model in order to create a single binary prediction feels extremely inefficient. "Llama Logits" is a much more efficient approach since it only needs to do a single prediction. I would like to see a figure plotting the avg number of FLOPs each method uses for a single prediction against the method's performance at the task. The authors should provide a more detailed analysis of the computational cost, including the number of forward passes, the number of tokens generated, and the time required for both training and inference. This should be compared to the baseline methods to give a clear picture of the trade-offs.
2. This is more of a question than an obvious weakness, but why choose the method described in 3.2 for regularization instead of just adding a second term in the loss which is the standard next-token prediction language modeling loss (similar to what RLHF does to keep the RLHF'ed model from straying from the reference model)? It is unclear why the authors chose to use a calibration loss based on the Levenshtein distance between the original text and the rewritten text, rather than a more standard language modeling loss. The authors should provide a more detailed justification for their choice, and discuss the potential benefits and drawbacks compared to other regularization techniques.

## Weaknesses of the Experimental Design
1. There are key flaws in the baselines L2R is compared against. Most concerning is line 260: "For ’Llama Logits,’ we train its Llama model using the same LoRA configurations as the rewrite model in L2R for a fair comparison." If I understand this correctly, the authors did hyperparamter search to find a good finetuning configuration configuration for *their* method (L2R), and then applied this same configuration to the Llama Logits baseline. This is the opposite of a fair comparison; a fair comparison would be to use equal compute and effort to identify a good hparam configuration for the Llama Logits baseline as for L2R. From the third line in Table 2, it is apparent that the authors did not find a good set of hyperparameters for tuning LLama Logits, as the discrepancy between between in-distribution and out-of-distribution performance suggests considerable overfitting. The authors should provide a more thorough hyperparameter search for the baseline methods, and report the best results for each method. The current approach of using the same hyperparameters for all methods is not sufficient to draw meaningful conclusions about the relative performance of the different approaches.
2. The paper does not explain what decoding strategy was used for generating the LLM-generated examples. This can make a big difference in terms of detectability, so it is very important to report this. I would expect this to be mentioned in Section 4.1. The authors should specify the decoding strategy used for generating the LLM-generated examples, including the temperature, top-p, and any other relevant parameters. This information is crucial for reproducibility and for understanding the characteristics of the generated text.
3. It is also unclear what prompts were used for generated the LLM-generated examples. This should also be mentioned in Section 4.1. The authors should provide the specific prompts used for generating the LLM-generated examples. The choice of prompts can significantly impact the characteristics of the generated text, and it is important to report this information for reproducibility and to understand the scope of the evaluation.
4. I would like to see some text added to motivate why an average sequence length of 120 words was chosen for the task. The authors should provide a justification for the choice of an average sequence length of 120 words. This should include a discussion of how this length was determined, and how it relates to the typical length of text in the domains being considered. It is also important to consider how the performance of the method might vary with different sequence lengths.
5. In Appendix A.3, the authors say "to prove the superiority of our dataset in training more capable detection models, we create a parallel nondiverse dataset ..." This statement doesn't sit well with me since the authors are only proving the superiority of their dataset over an obviously worse version of their dataset. A more valid comparison would be to compare their dataset to other publicly available datasets intended for the detection task. The authors should compare their dataset to other publicly available datasets for AI-generated text detection, rather than just comparing it to a non-diverse version of their own dataset. This would provide a more meaningful evaluation of the quality and relevance of their dataset.
6. There are many ways for eval data to be OOD for a detection system: it could come from a different model than the one used to collect training data for the detection system; it could be shorter or longer than the training data; it could be generated using a different decoding strategy; it could be in a different writing style (e.g. news vs. stories). The authors only focus on this very last definition of OOD; I would like to see at least some exploration or discussion of other ways eval data could be OOD. The authors should explore other ways that the evaluation data could be out-of-distribution, such as using different models, different decoding strategies, or different text lengths. This would provide a more comprehensive evaluation of the robustness of the proposed method.

## Weaknesses of the Discussion of Prior Work
1. It is unclear from the Related Work section how the proposed method differs from prior methods, especially RAIDAR, which has a very similar core idea. I would like the Related Work section to contain more sentences along the line of "In contrast to Paper X which does approach Y, we do approach Z." For example, I cannot parse what is meant by the one sentence in the related work section that does attempt to compare to RAIDAR (line 130): "Despite the attempt on capturing rewrite edit distance as a domain-agnostic feature, the rewrite amount still varies across distributions, which limits its full potential." Why does the rewrite amount differing across distributions limit RAIDAR? What do the authors do differently in their approach to solve this? The authors should provide a more detailed comparison of their method to RAIDAR, highlighting the key differences and advantages of their approach. The current discussion is too vague and does not clearly explain how their method improves upon existing work.
2. The only pre-2020 paper referencd in the Related Work section is to the GPT-2 open-weight release whitepaper, despite there being several seminal works on detection of generated text which came out around then. A couple notable omissions are GLTR (https://arxiv.org/abs/1906.04043) and "Automatic Detection is Easiest when Humans are Fooled" (https://arxiv.org/abs/1911.00650), although there are undoubtedly otfhers. The authors need to expand their literature review (and possibly their choice of baselines), as several of these simple methods from the (slightly) older literature continue to work quite well under some conditions, as can be seen in the RAID paper (https://arxiv.org/abs/2405.07940), which is another missing citation. The authors should expand their literature review to include more relevant prior work, particularly seminal papers on the detection of AI-generated text. This would provide a more comprehensive context for their work and help to position it within the existing literature. The authors should also consider including some of these methods as baselines in their experiments.
3. The Datasets section starts with the following sentences: "Existing detectors are often evaluated on datasets such as SQuAD (Rajpurkar et al., 2016), XSum (Narayan et al., 2018), Writing Prompts (Fan et al., 2018), and others (Bao et al., 2024; Mao et al., 2024). However, these datasets typically represent a narrow subset of available data, both in terms of timeliness and domain coverage." There are two issues with these sentences. First, "datasets ... such as others" is not an informative statement. If the authors plan to site Bao and Mao, they should list what type of data these methods evaluated on. Second, this list is missing several key detection benchmarks, which are also trying to solve the "real-world scenarios" challenge that the authors mentioned being concerned about in the next sentence in the paragraph. Missing references include RAID (linked above), RuATD (https://arxiv.org/abs/2206.08029), MAGE (https://arxiv.org/abs/2305.13242), and probably others as well. The authors should explain what their new benchmark accomplishes that these existing benchmarks do not. The authors should provide a more detailed discussion of the existing datasets used for AI-generated text detection, including their strengths and weaknesses. They should also clearly explain how their new dataset addresses the limitations of existing datasets and what unique contributions it offers.

## Weaknesses in the Writing/Presentation
1. Equations 3 could be greatly simplified by formulating the problem such that label y = 1 is AI and **y = -1 is (human)**. This would eliminate the need for the indicator function and the funky arithmetic. The authors should consider simplifying Equation 3 by using a more standard formulation for binary classification, such as using labels of +1 and -1 for AI-generated and human-written text, respectively. This would make the equation more concise and easier to understand.
2. Equation 4 reads like a Python program which the authors attempted to turn into math. It would be much more comprehensible if the authors instead wrote what this in pseudocode, or even just English. The authors should rewrite Equation 4 using pseudocode or English to make it more understandable. The current mathematical notation is difficult to follow and does not clearly convey the intended meaning.
3. In Table 1, under "EducationalMaterial" the bolded value should be "Llama Rewrite" not "Llama L2R." Speaking of which, is the difference between the values here statistically significant?
4. Many of the references are formatted incorrectly with missing capitalization in the paper titles.

### Questions
See above.

### Soundness
2

### Presentation
1

### Contribution
2
