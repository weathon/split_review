# Self-Alignment with Instruction Backtranslation

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
We present a scalable method to build a high quality instruction following language model by automatically labelling human-written text with corresponding instructions. Our approach, named {\em instruction backtranslation}, starts with a language model finetuned on a small amount of seed data, and a given web corpus. The seed model is used to construct training examples by generating instruction prompts for web documents ({\em self-augmentation}), and then  selecting high quality examples from among these candidates ({\em self-curation}).  This data is then used to finetune a stronger model.  Finetuning LLaMa on two iterations of our approach yields a model that outperforms all other LLaMa-based models on the Alpaca leaderboard not relying on distillation data, demonstrating highly effective self-alignment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to generate instruction tuning data from unlabelled data by posing the problem as an ‘instruction back translation’ problem ie. given a piece of text, generate potential instructions that can be answered by the text. This model is learnt by finetuning a base LLM with seed instruction data in the reverse direction. The examples thus generated are filtered using the seed model, and iteratively the seed model is improved with the filtered data. Unlike distillation-based approaches, the data is not generated using an external, more powerful model – rather this is self-augmentation that bootstraps a model's capabilities.

### Strengths
* The paper proposes a method for generating diverse, high-quality instruction datasets using a baseline LLM that does not require an external, more powerful LLM.  
* The instruction-tuned models so created are better than models trained on small, human-curated corpora and competitive with models trained on data distilled from more powerful models. 
* Evaluation on a diverse set of benchmarks shows the generalizability of this method.

### Weaknesses
While instruction tuning backtranslation is a useful method, it is not clear how it compares with self-instruct. If the same seed dataset had also been used to generate instruction tuning data from the same base LLM, that would provide a  good comparison. The distilled models considered in the paper have been trained on different seed datasets and use more powerful LLMs for distillation. Although I don’t see this as a serious limitation of the paper, this study would have helped shed light on how the two approaches compare.

### Questions
* What is the impact of self-curation iterations? Is there a value to performing multiple iterations? Did you also consider inference of the document collection on an improved reverse model from the data extracted (making the augmentation step also iterative)?
* Can you add some samples of extracted instruction dataset instances to the paper? 
* How are the segments selected from ClueWeb. Are entire documents chosen, is there some filtering on criteria like length, etc? Are the inputs to the reverse models entire documents or smaller units like paragraphs? 
* Table 5: What is the model size used in this study? On which benchmark dataset? Does this observation hold over different model sizes? Which configuration has been used to report results in the rest of the paper?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a scalable and simple method to curate high-quality instruction data for fine-tuning language models.  Specifically, the proposed method includes two stages: self augmentation, i.e., generate prompts for raw documents, and self curation, i.e., select high-quality augmented data iteratively.  After two rounds of data curation, the constructed data is used to finetune a stronger model, which is demonstrated to outperform non-distilled models. Also this paper presents comprehensive analysis and ablation experiments to show the effectiveness of the proposed method.

### Strengths
1). An intuitive and effective method to construct high-quality and diverse instruction data. It will significantly reduce the human annotation efforts or potential bias of distilled data from strong LLMs like ChatGPT. 

2). The self-curation step provides continuous data quality improvement in terms of fine-tuned models performances and the diversity of augmented data can complement seed instruction data.

3). The paper is well-written with comprehensive and clear analysis / experiments.

### Weaknesses
No obvious weakness but it would be better to clarify the choices of unlabeled data for augmentation.

### Questions
1). One scaling law question:  will the performance be stable (not increase) with the increased numbers of augmented data (w/ curation)? 

2).  In the first paragraph of Section 3.3,  does $A^{(2)}_{5}$ mean the subset that scores more than 4.5? 

3). In Table7, what if the results of Humpback 65B with 5-shot demonstrations?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims to build an instruction following language model by fine-tuning. To collect high quality instruction-response pairs automatically, the paper proposes instruction backtranslation, which first uses a seed dataset to fine-tune to generate instructions given a web corpus, and then fine-tunes a stronger model on the filtered instructions. Experiments show the resulting LM outperforms non-distilled LMs on both generation quality and downstream performance. Analysis shows that the self-curation step is critical in selecting high-quality data which leads to further improvement while simply scaling the data size does not.

### Strengths
1.	Instruction-following is an important aspect of applying LLMs in practice, while high-quality labeled data is critical to elicit this behavior from LLMs. The proposed method does not rely heavily on human annotation and could scale the data size with the data quality being guaranteed.
2.	The paper conducts extensive experiments with both human and automatic evaluation to demonstrate the effectiveness of the proposed method across downstream tasks and model size. In particular, the analysis verifies that data quality plays an important role in improving performance when scaling up the data size.
3.	The paper is easy to follow and well-organized.

### Weaknesses
1.	The paper assumes that the seed model M0 can somehow provide meaningful evaluation for the generated instructions by just following instructions. This might need further investigation. For example, M0 could be just selecting instructions that are similar to the seeds while discarding other instructions which are still useful but may vary in style or format, etc. Also, the work could consider other filtering methods such as using the language modeling probabilities as the scores or using external models such as those trained with NLI. The reliance on M0 for evaluation introduces a potential bias towards instructions that align with its training data, potentially limiting the diversity of the generated instruction set. This could lead to a model that excels on tasks similar to the seed data but struggles with novel or out-of-distribution instructions. Further, the paper does not explore the sensitivity of the final model to the choice of M0, which could be a significant factor in the overall performance.
2.	The paper assumes that a proportion of the unlabeled data should have the corresponding instructions which is not quite intuitive. One limitation is that this might greatly limit the types of instructions that the backtranslation model can generate. I would suggest a further study to understand the types of segments that do have meaningful instructions and the types of instructions that we could collect from the web corpus. The assumption that web text inherently contains segments with corresponding instructions is a strong one. It's not clear what proportion of web text actually fits this criteria, and the paper does not provide any analysis on this. This assumption could limit the applicability of the method to datasets where such a correspondence is not prevalent. Furthermore, the paper does not discuss the potential for generating spurious instructions for text segments that do not naturally have an associated instruction, which could introduce noise into the training data.

### Questions
1.	Could you show more concrete examples of the generated instructions and the corresponding text segments? That would be helpful for users to understand why certain texts should have an underlying instruction.
2.	What are the benefits brought by the proposed method compared to the distilled method?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work investigates scaling the instructing tuning with limited seed data.
The authors suggest an iterative self-training approach to increase training instances from large-scale unlabeled data.
They first train a instruction generation model (backward model) with high-quality seed data to predict instruction for unlabelled data.
Then, the initial instruction following model, which is finetuned on the seed data, is prompted to score the pseudo labeled instances.
Next, a new instruction model is trained on the compound of seed data and selected high-quality pseudo data with system prompt conditioning.
This new improved model can continue the next cycle scoring on the pseudo labeled data, then finetuning the second improved model, again and again.
The pseudo data is not updated in the above iteration.
The authors conducted extensive experiments using LLaMA 7B, 33B, 65B models.
Model performance is evaluated by the win rate of each model against text-davinci-003 from GPT-4 judgements (AlpacaEval).
The generated instructions can increase the task diversity, show better data scaling coefficient than other data sources.
Models finetuned on the selected data achieved best performance among non-distilled models.

### Strengths
1.  The paper cleverly utilizes the traditional self-training method to enhance the instruction data and model performance.  
2.  The experiments are solid.

### Weaknesses
no significant negative issues.

### Questions
1. section 3.3, Data quality vs. data quantity. "We find that training on augmented data without self-curation **does not improve** instruction following performance despite scaling up data quantity". I did not find any clear evidence from Figure 2 to support the statement "does not improve." Perhaps adding the win rate of the M0 model could help me better understand?

2. What does the ± in Table 5 mean? Multiple inference of models?

3. I am curious about the performance if we update the backward model using augmented data. It's worth exploring to see how it would perform.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
