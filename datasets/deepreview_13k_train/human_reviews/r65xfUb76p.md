# UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition

- Decision: Accept
- Scores: 8, 3, 6

## Abstract
Large language models (LLMs) have demonstrated remarkable generalizability, such as understanding arbitrary entities and relations. 
Instruction tuning has proven effective for distilling LLMs into more cost-efficient models such as Alpaca and Vicuna. Yet such student models still trail the original LLMs by large margins in downstream applications. 
In this paper, we explore {\it targeted distillation} with mission-focused instruction tuning to train student models that can excel in a broad application class such as open information extraction.
Using named entity recognition (NER) for case study, we show how ChatGPT can be distilled into much smaller \longname models for open NER. 
For evaluation, we assemble the largest NER benchmark to date, comprising 43 datasets across 9 diverse domains such as biomedicine, programming, social media, law, finance.
Without using any direct supervision, \longname attains remarkable NER accuracy across tens of thousands of entity types, outperforming general instruction-tuned models such as Alpaca and Vicuna by over 30 absolute F1 points in average. 
With a tiny fraction of parameters, \longname not only acquires ChatGPT's capability in recognizing arbitrary entity types, but also outperforms its NER accuracy by 7-9 absolute F1 points in average. 
Remarkably, \longname even outperforms by a large margin state-of-the-art multi-task instruction-tuned systems such as InstructUIE, which uses supervised NER examples.
We also conduct thorough ablation studies to assess the impact of various components in our distillation approach. 
We release the distillation recipe, data, and \longname models to facilitate future research on targeted distillation.\footnote{Project page: \url{https://universal-ner.io/}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a targeted distillation model for open-named entity recognition. It also assembled a large and diverse NER benchmark with 43 NER datasets.

### Strengths
Although the knowledge distillation from powerful LLM such as ChatGPT is not a novel idea, this paper explored distillation and further improvement. The dataset constructed in this paper is essential and I would love it will be released soon.  Experiment results demonstrated the effectiveness of the proposed model, and the UniNER is better than ChatGPT on open domain NER, making the UniNER a better choice for local deployment for NER tasks.

### Weaknesses
Some details were missing in this paper, which may reduce the reproducibility of this research. For example, the dataset processing step has a filter on entity type; how to select the entity type ( the exact standard) and the entity types removed from each dataset need to be released as an appendix.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper explores targeted distillation with mission-focused instruction tuning to train student models that excel in open information extraction. The case study focuses on named entity recognition (NER), demonstrating how ChatGPT can be distilled into smaller UniversalNER models for open NER. UniversalNER achieves remarkable NER accuracy across tens of thousands of entity types, outperforming general instruction-tuned models like Alpaca and Vicuna by over 30 absolute F1 points on average. Furthermore, UniversalNER outperforms state-of-the-art multi-task instruction-tuned systems like InstructUIE, even without using supervised NER examples.

### Strengths
- The paper proposed a novel approach to distill LLMs into more cost-efficient models.
- The experiments are sufficient. The writing and presentation are clear and easy to read.

### Weaknesses
 - Lack of some supervised baselines such as [a]. The “BERT” column in Table 2 did not represent the SoTA supervised baselines. Even so, the presented results in Table 2 show that the UniNER with such a large scale of parameters did not improve significantly and are not comparable with supervised small models in some dataset. Therefore, it is doubtful to use prompt-based method with LLM to solve NER problems. Moreover, the training cost are not presented explicitly. The motivation should be clarified carefully.
- The proposed method could be very unstable as the dataset construction includes several uncontrol factors. Thus the reproduction of the results could be problematic.  I suggest the authors should claim the related limitations clearly.   

### Questions
- How to control the data quality constructed by ChatGPT?
- The collecting of the passage-query pairs of instruction tuning is not detailed enough for reproduction.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors distill a general NER model from ChatGPT data and propose a large NER benchmark. Their model seems to perform well when the types are known ahead of time.

### Strengths
I have read the author reply and have raised my score by one point.

----------------------

Thanks to the authors for the hard work on this paper. I have marked it a 5, but plan to raise my score if the weaknesses are adequately addressed. 

Strengths:
- Good performance
- Nice benchmark contribution
- Ablations are largely good

### Weaknesses
 - It's not clear why ChatGPT is doing worse even though you are distilling from it. You write: for "ChatGPT (gpt-3.5-turbo-0301). We use the prompting template in Ye et al. (2023) for NER." For fairness, it also makes sense to use your UniversalNER prompting template with ChatGPT. Otherwise we don't know what the cause is for you beating ChatGPT while distilling from it. Please add this experiment.
- In section 5.5, about entity type paraphrasing - this issue seems inherited from your silver training data where generated types are likely not unique while referring to the same underlying type. Seems like this issue isn't really a concern because you provide the known types from each dataset, but would be a concern for true open-domain NER where the types are not known ahead of time. No changes are requested here, but I would appreciate hearing your response to this observation.
- The section "Recognition of diverse entity types" does not "effectively demonstrate our model’s capacity to capture entities of various types." It's just a single picked example. Please consider doing a manual evaluation on 100 samples to actually demonstrate what you claim here.

### Questions
- In section 3.2, you write "Then, for each entity type that appears in the output, we transform it into a natural language query “What describes it?” - To be clear, here you don't ask the model to output the entity types, but you did in 3.1? 
- In sec 4, Dataset processing you write "This is because some entity types (e.g., ELSE) are not coming from consistent sources across
the different datasets." Shouldn't this be addressed by the "Dataset-specific Instruct Tuning Template"?
- In figure 6, the biggest gains are for the most famous datasets. Can you try to check if these datasets have somehow been included in LLaMA's pre-training dataset?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
