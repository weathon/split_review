# PromptNER : Prompting For FewShot Named Entity Recognition

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
In a surprising turn, Large Language Models (LLMs) together with a growing arsenal of prompt-based heuristics
now offer powerful off-the-shelf approaches providing few-shot solutions to myriad classic NLP problems. 
However, despite promising early results, these LLM-based few-shot methods remain far from the state of the art in Named Entity Recognition (NER), where prevailing methods include learning representations via end-to-end structural understanding and fine-tuning on standard labeled corpora. 
In this paper, we introduce \toolname, 
 a new state-of-the-art algorithm for few-Shot and cross-domain NER. To adapt to any new NER task \toolname requires \emph{a set of entity definitions} in addition to the standard few-shot examples. 
Given a sentence, \toolname prompts an LLM to produce  a list of potential entities along with corresponding explanations justifying their compatibility with the provided entity type definitions. 
\toolname achieves state-of-the-art performance on few-shot NER,
achieving a 4\% (absolute) improvement in F1 score on the ConLL dataset, a 9\% (absolute) improvement on the GENIA dataset, and a 4\% (absolute) improvement on the FewNERD dataset.
\toolname also moves the state of the art on Cross Domain NER, outperforming prior methods (including those not limited to the few-shot setting), setting a new mark on $3/5$ CrossNER target domains, with an average F1 gain of $3\%$, despite using less than $2\%$ of the available data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed to use LLM to perform named entity recognition which is widely studied in the academia of natural language processing. The proposed method involves the definition of the entity types, few-shot demonstrations, and chain-of-thought templates for generation. The experiments results show a great improvement compared  with baselines on NER tasks and cross-domain NER tasks.

### Strengths
Since LLMs are quite popular these days, it is worth to see how LLMs can be used in the classic NLP tasks. This work explores the potential of LLMs in NER tasks and show they are useful in terms of cross-domain and low-resource scenarios.

### Weaknesses
The biggest concern is that the method seems straightforward to me, and thus I think it lacks the core innovation in terms of the methodology. It is intuitive to inform the model of the definition, few-shots, and chain-of-thought to accomplish the task. I wish to see how these prompts are interacting with the final outputs so as to provide more insights on how the future work can learn from the prompt design or use the LLMs properly in classic NLP tasks. Also, I think it is more innovative to design specialized modules in the prompt engineering for NER tasks. Otherwise, the current work is similar to a strong baseline which is helpful to future work for sure, but may not be ready for a long research paper.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a PROMPTNER framework integrating entity definitions and few-show learning in a large language model prompt. Experiments on GPT-4 LLM show the proposed model is better on several datasets.

### Strengths
This paper demonstrated that with the GPT4 as the backbone, the proposed PROMPTNER showed good cross-domain NER identification ability. Several ablation experiments showed the effectiveness of each component.

### Weaknesses
There are various studies on improving prompt strategies in this LLM area.  Adding the entity definition on the prompt of LLM is not an innovative method. Based on the experiment, the most improvement of the proposed method comes from the powerful GPT 4 backend. Comparing the GPT4-driven model with models with much weaker LLM is not necessary and not fair (Table 2-4). The paper lacks a thorough analysis of the computational cost associated with using GPT-4, which is a significant factor in real-world applications. The experiments also do not explore the sensitivity of the proposed method to different prompt formulations or the impact of varying the number of few-shot examples, which could reveal potential weaknesses or limitations.

### Questions
None

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a prompting template for the NER tasks. With GPT3.5 and GPT4, it can achieves the SOTA on a list of few-shot NER tasks measured by F1 scores. The paper also achieves the SOTA performance on 3/5 Cross Domain NER tasks. The prompting techniques uses few-short in-context learning and chain-of-thoughts. In the ablation study, the paper shows that the size of the LLM and few-shot examples are critical to the performance gains.

### Strengths
The paper introduces a very simple prompting template which can be easily integrated into relevant applications.
The paper is clearly written and is easy to follow. it gives the detailed ablation study to help us understand the contribution of each components. 
The paper compares against a comprehensive list of previous work in its experiments.

### Weaknesses
It seems to me that the major contribution of the SOTA performance comes from GPT4 more than some advanced prompting techniques of the paper where most of cases, the best performance is achieved only by GPT 4. T5 is way worse than the current SOTA. The prompting template is simply an application of CoT with few shot in-context learning. I am not convinced if whether this prompt template is very novel or has a significant originality of ideas and I was wondering whether other similar template can't achieve similar performance.

### Questions
For the Cross Domain NER tasks, as Table 2 shows, only 2 examples are used in prompting and the F1 scores for AI and Sciences are not the highest. Why can't we add more examples (e.g. up to 200) to improve performance? Did we also consider fine-tune GPT to see if we can get the higher F1 scores?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces PromptNER, a prompt-based algorithm for few-shot and cross-domain Named Entity Recognition (NER). It utilizes a Large Language Model (LLM) to generate potential entities along with explanations for their compatibility with entity types. The method requires modular entity type definitions, few-shot examples, and explanatory text. PromptNER achieves better performance on few-shot NER and cross-domain NER over baseline methods. The study demonstrates the flexibility and adaptability of PromptNER across domains with minimal computational cost.

### Strengths
This work emphasizes the importance of prompt-based heuristics and in-context learning in advancing few-shot learning for NLP. It presents a promising approach for flexible and easy-to-apply NER systems that can adapt to different settings with limited human involvement.

### Weaknesses
1. Concerning the introduced PromptNER methodology, I didn't discern any noteworthy technical novelty. In essence, the idea that the paper alludes to strikes me as rather naive. Almost every LLM-based NER initiative could effortlessly incorporate the strategy of embedding entity definitions within prompt texts, facilitating the LLM's comprehension. In a nutshell, I'm unconvinced that this paper heralds any significant fresh technological insights.

2. The related work section falls short of explicitly highlighting how the proposed method differentiates from, and potentially improves upon, existing works. Such delineations are crucial for situating a new method in the context of established research.

3. There's a palpable omission of numerous standard few-shot NER benchmarks, such as WNUT-2017, MIT-Movie and MIT-Restaurant, JNLPBA, among others. Moreover, there's a conspicuous absence of comparative analysis with many of the state-of-the-art few-shot NER models.

4. Of paramount concern is the author's decision to juxtapose their model, based on GPT3.5/GPT4, directly with the baselines. This presents an overtly skewed comparison, heavily favoring the presented model. Such disparities render any conclusions derived from the experiments to be questionably validated. It's evident that OpenAI's LLM models outclass the baselines by multiple magnitudes, and the proprietary nature of these models further impedes reproducibility. A more equitable comparison would necessitate evaluating the proposed prompt methodology and baseline techniques using identical open-source LLMs, ensuring both type and size compatibility.

### Questions
1. Given the stated weaknesses, how do the authors justify the claimed novelty of the PromptNER methodology, especially in light of its evident simplicity and seemingly naive approach?
   
2. Could the authors amplify on the differentiators between their proposed method and existing literature, providing a clearer positioning of their research contribution?

3. What rationale underpins the selection of benchmarks for evaluation, and why were certain prominent few-shot NER benchmarks omitted?

4. Can the authors elucidate their choice to compare their model based on GPT3.5/GPT4 directly with the baselines, given the glaring discrepancies in terms of model scale and accessibility?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
