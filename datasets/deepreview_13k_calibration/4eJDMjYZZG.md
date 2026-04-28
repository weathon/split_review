# Language Model Detectors Are Easily Optimized Against

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The fluency and general applicability of large language models (LLMs) has motivated significant interest in detecting whether a piece of text was written by a language model. While both academic and commercial detectors have been deployed in some settings, particularly education, other research has highlighted the fragility of these systems. In this paper, we demonstrate a data-efficient attack that fine-tunes language models to confuse existing detectors, leveraging recent developments in reinforcement learning of language models. We use the `human-ness' score (often just a log probability) of various open-source and commercial detectors as a reward function for reinforcement learning, subject to a KL-divergence constraint that the resulting model does not differ significantly from the original. For a 7B parameter Llama-2 model, fine-tuning for under a day reduces the AUROC of the OpenAI RoBERTa-Large detector from 0.84 to 0.63, while perplexity on OpenWebText increases from 8.7 to only 9.0; with a larger perplexity budget, we can drive AUROC to 0.30 (worse than random). Similar to traditional adversarial attacks, we find that this increase in 'detector evasion' generalizes to other detectors not used during training. In light of our empirical results, we advise against continued reliance on LLM-generated text detectors. Models, datasets, and selected experiment code will be released at https://github.com/charlottttee/llm-detector-evasion.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores the feasibility of optimizing language models to evade language model detectors. The authors propose a data-efficient attack using reinforcement learning to fine-tune language models and confuse existing detectors. They demonstrate the effectiveness of this approach by reducing the AUROC of the OpenAI RoBERTa-Large detector from 0.84 to 0.62 in a 7B parameter Llama-2 model. The results show that it is relatively easy and cheap to train language models to be less detectable, and the evasion generalizes to other detectors not used during training.

### Strengths
- The paper introduces a new method for optimizing language models to evade detectors using reinforcement learning. The use of direct preference optimization (DPO) and the KL-divergence constraint provides a simple and stable training procedure.

- The authors conduct a comprehensive set of experiments to evaluate the effectiveness of the proposed approach. They consider both open-source and commercial detectors, and demonstrate the generalization of evasion across detectors.

- The results of the study have important implications for the reliability of machine-generated text detectors. The findings suggest that current detectors are not robust and can be easily evaded, which raises concerns about the widespread use of language models.

### Weaknesses
 - The paper focuses primarily on empirical evaluations and does not provide a theoretical analysis of the proposed approach. A deeper understanding of the underlying principles and limitations of the method would enhance the contribution of the paper. For example, the paper does not explore why the DPO method is effective at evading detectors, or what properties of the fine-tuned model make it less detectable. A theoretical framework could help to understand the generalizability of the approach and its limitations.

- The paper does not extensively discuss potential countermeasures that could be employed to improve the robustness of language model detectors. It would be valuable to explore possible strategies for detecting and mitigating evasion attacks. For instance, the paper could investigate whether adversarial training or other robust learning techniques could make detectors more resilient to the proposed evasion method. The lack of discussion on this front limits the practical implications of the work.

- The paper does not compare the proposed approach with existing evasion techniques. It would be beneficial to evaluate the performance of the proposed method against other state-of-the-art methods for evading language model detectors. For example, the paper could compare its method with techniques that involve paraphrasing or manipulating text at the character level. Without such comparisons, it is difficult to assess the novelty and effectiveness of the proposed approach.

### Questions
None

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into the rising interest in identifying text generated by large language models (LLMs). Although detection systems have been implemented in various sectors, notably education, their vulnerability has been a significant concern. The authors present a data-efficient method that fine-tunes LLMs to deceive these detectors by employing the latest advancements in reinforcement learning for language models. They use the 'human-ness' score of several detectors as a reward function and set a constraint to ensure the modified model remains close to the original. Through this method, the effectiveness of the OpenAI RoBERTa-Large detector is notably reduced. The findings suggest that this enhanced 'detector evasion' can generalize to other detectors not part of the initial training. Consequently, the authors caution against depending on detectors for LLM-generated text.

### Strengths
- The paper is well-written and clearly presented; 
- The paper tackles a critical and timely topic concerning the detection of LLM-generated text and proposed a novel data-efficient RL-based attack to deceive existing detector; 
- The paper shows empirical evidence of the fragility of current LLM-based detectors, offering actionable insights for future research and development of LLM detectors, the experiments are based on three runs which show the robustness of the proposed methods, abolition regarding the sample efficiency has also been provides to show the design choices;

### Weaknesses
 - The scalability of the proposed methods could be good to include to show whether the evasion of detector only happens when the model size of small like 7B in the most of the experiments; 
- Besides the perplexity, it will be good to include some evaluations on popular benchmark to assess the post-evasion model performance (whether the improved evasion is under the sacrifice of the general performance of the attack model);

### Questions
- Could the authors list the training preference data and evaluation data in detail to understand whether there is a generalization due to the data in the experiments; 
- Could author offer more explanation towards the generalization of cross-detectors and the mixture of the effectiveness from different sources in Table 1 and 2, as well as how the attack performance correlates with the generalization;

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work mainly studies why direct preference optimization (DPO) can be used to train a generator to evade detection. Following DPO, two samples are generated, and the preference is determined by the humanness score outputed by a given detector. 

In experiments, a range of detectors are optimized against, including classifiers and metric-based detectors such as DetectGPT. Empirically, AUROC metrics is reduced to below 0.5 against several strong public and commercial detectors. Also interestingly, attack against one detector could generalize to other detectors.

### Strengths
The attacks for detectors is a very relevant research question especially in the era of LLMs.

Within the scope of detection, using techniques from RL (DPO) is quite novel.

The attack result is quite strong, and quite concerning. Since it does not require white-box access to the detector.

### Weaknesses
From a ML perspective, this paper does not propose a completely novel algorithm. Therefore my rating will be higher if this is a NLP conference.

From an adversarial attack perspective, the result is not very surprising.

I think the author should not only report PPL, but also the diversity of the generated texts.

How to defense against such attack is not explored.

### Questions
You should put comma or period after the equations. They are also part of a sentence.

A lot of paragraphs are very long. Please break up at some points.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
