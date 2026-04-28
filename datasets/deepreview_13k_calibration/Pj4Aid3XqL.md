# Should VLMs be Pre-trained with Image Data?

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Pre-trained LLMs that are further trained with image data perform well on vision-language tasks. 
While adding images during a second training phase effectively unlocks this capability, it is unclear how much of a gain or loss this two-step pipeline gives over VLMs which integrate images earlier into the training process. 
To investigate this, we train models spanning various datasets, scales, image-text ratios, and amount of pre-training done before introducing vision tokens.
We then fine-tune these models and evaluate their downstream performance on a suite of vision-language and text-only tasks.
We find that pre-training with a mixture of image and text data allows models to perform better on vision-language tasks while maintaining strong performance on text-only evaluations.
On an average of 6 diverse tasks,  we find that for a 1B model, introducing visual tokens 80\% of the way through pre-training results in a 2\% average improvement over introducing visual tokens to a fully pre-trained model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Brief Summary: This is an experiment heavy paper tackling the question of how to best pre-train Vision-Language Models (VLMs). In particular, the authors investigate the best time to provide vision-text data to the existing LLM model, how much visual data should be provided to maintain scores on language-only tasks. 

The experiments on multiple VQA datasets and text-benchmarks (noted in appendix E) suggest some key takeaways such as timing of introducing the vision data in the cooldown phase of the LLM training, the fraction of the vision data being limited compared to text data, and using instruction fine-tuning tokens for downstream tasks during fine-tuning is better.

### Strengths
Pros:

1. This is an experiment heavy paper aiming to empirically provide a guideline for training with image data for image-language downstream tasks. The authors suggest they have performed over 300 runs (some on 79M some on 1B model) which is generally sufficient.

2. The takeaways make sense. The improvements by following the guidelines are significant (~2% on vqa benchmarks). 

3. The authors provide heavy ablations, the experiments are well thought out in general.

### Weaknesses
 Cons:

1. The authors should provide some qualitative analysis, of where the model scoring lower misses compared to other models. Currently, it is not directly clear what kind of questions the 2% drop come from. 

2. One concern is that the chosen VQA benchmark is a bit restrictive. The authors should chose a larger set of evaluation benchmark such as MMMU, OCR-Bench to name a few (Qwen2-VL has a good set of possible evaluation benchmarks [Ref1]). 

3. Related to previous point, the authors should also include some caption/description as well as OCR heavy datasets as well. 

4. (Minor) The provided methodology is shown on 1B models but not on larger models such as 7B and 70B. While in general it is expected the findings will carry forward, an explicit experiment would be better. However, it might be prohibitively expensive. 

5. (Minor) One issue with the guidelines is that these can be only applied at training time by the authors of the original work. Thus, if someone else wants to improve an existing VLM, it requires the original authors to have open-sourced their checkpoints including the optimizers weights and schedule which may be difficult to obtain. 

### Questions
Q1. Is there a particular reason for choosing OpenLM instead of other models such as LLaMa and Qwen adjacent models (those in Table 1)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Authors investigate the common multi-step training procedure of VLMs, where first an LLM is trained, and then this LLM is further trained with image-text data to turn it into a VLM. They probe when and how to exactly add the image-text data into the training, and how to set the learning rate schedules. Also, they research the impact of setting different ratios of image/text tokens in the visual pretraining stage, and how to exactly use the image instruction data for the last last finetuning stage. 

Their findings show that image-text data should be added during the cooldown phase of the LLM training, and not as a second step with a second warmup phase. They further find that adding instruction fine-tuning data during the pretraining stage hurts performance, and that 10-20% of tokens should be visual during the image-text pretraining stage.

### Strengths
The paper is very well presented visually and also very well written, as it is fluent to read and understandable. This combination of nice figures and well written text makes it well digestable. The authors highlight potential weaknesses or difficulties, e.g. in figure 4 highlighting the points that are trained with a different learning rate schedule.

The research question is interesting and valuable, since most VLM pretraining happens in (semi-)proprietary setups where details are hidden, or in setups were many training choices are not discussed since ablating them would be difficult.

The finding that image-text data should be injected earlier into the training process is relevant for many existing VLM training pipelines.

### Weaknesses
Note that these weaknesses are in descending order of importance.

1) The comparison to other VLMs is missing: The authors introduce a new metric “vision stable-score” as their main empirical evidence, but then evaluate only their own trained models on this metric. This makes comparing this work to other works difficult. Authors should show the benchmark numbers for some of the models in table 1. This work does not need to be top 1 in this table since the goal is not to train a SOTA model but to investigate training behaviour. However the comparison table is needed to evaluate how close this work is to the SOTA VLMs, because if the model is too far away, the findings might not relevant for SOTA models.

2) Similarly, the text stable score is very low, below 20% everywhere. This might be due to subtracting the random baseline. However there needs to be a comparison to the DCLM-1B text model before any image training, as well as maybe one more SOTA/popular LLM.

3) In 3.1 the peak learning rate is set to 3e-3 for the 100% checkpoint model. This choice is not argued for or ablated. The best peak learning rate in this chapter seems to be the green cosine 80% curve in figure 3 (around 1e-4 however it is hard to read the exact number from the graph), therefore authors should have at least tried this best peak learning rate also for their 100% checkpoint model. Otherwise, the risk remains that the main finding of the paper in chapter 3.1 can be just attributed to different hyperparameters.

4) Evaluating only on accuracy metric benchmarks has significant drawbacks, since only short and exactly matching answers can be correct. Considering that this model is trained on image-caption pairs, there should be at least a captioning benchmark added.

5) In the abstract: “a 1B model (retains) performance within 2% of our text-only baseline”. I could not easily find this in the paper. Assuming you compare the 80% model from figure 4 with ~15% text stable score and ~54% text arc easy. The text-only baseline should then be the DCLM-1B model without any image-text training and without image-text finetuning. However that model reports ~75% text arc easy results. So: Which models are you comparing to make this statement, on which metrics? If the text-only baseline is not the DCLM-1B model, why?

6) The decision to freeze the vision encoder was done on a 79M model. However there is no argument why this should hold for bigger models, it would be good to have at least one unfrozen run on the 1.4B model.

7) Training on interleaved image-text data is omitted in this work. This is a weakness acknowledged by the authors but it is reasonable to first evaluate the findings on image-text pairs and potentially in the future extend to interleaved data.

Summary: I believe that points 1 to 3 must be addressed before the paper can be published, because otherwise the scientific evidence for the findings is not strong enough.

### Questions
- The LLM is only trained for 28B tokens in this work, while it is originally trained for 4.3T tokens in the DCLM-1B work, a factor 150x more data. Authors argue with the scaling laws from the Chinchilla paper, which would suggest “20 times number of params” of tokens is enough. But then, why use a LLM that is trained on “3070 times number of params” tokens?

- How many (approximate) GPU hours were used for each experiment, or at least, how expensive is one run of the 1.4B model on 28B tokens? Appendix A shows GPU hours for the text-only training but not for the image-text training.

### Soundness
2

### Presentation
4

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
This paper studied when to integrate image tokens to the training process of LVLM. The authors trained models spanning various datasets, scales, image-text ratios, and amount of pre-training done before introducing vision tokens. It experimentally found that incorporating image data during pre-training generally helps and the fraction of visual data and time of introducing visual instruction tuning are also important.

### Strengths
1. This paper systematically studies the time of introducing visual tokens during language pre-training, image-text pre-training and instruction finetuning. 
2. It demonstrates several key findings such as incorporating image data during pre-training, and the time of introducing instruction fine-tuning image tokens. 
3. Compared with fully pre-trained model, introducing visual tokens 80% of the way through pre-training results in a 2% average improvement in VQA tasks.

### Weaknesses
1. This study is very limited to the parameter size of the LLM. It seems hard to generalize to different size of LLMs. It seems this paper adopted 1B LLM, commonly used 7B and 13B LLM should also be studied. How do authors expect the findings might change at different model scales? It is unclear if the observed trends, such as the optimal point for introducing visual tokens, would remain consistent with larger models that have different training dynamics and convergence properties. The paper lacks a discussion on how the optimal timing for visual token integration might be affected by model capacity and the amount of pre-training data.
2. Some findings are already well-studied, such as mixing together instruction fine-tuning during the image-text pre-training can hurt the model. While the paper confirms this, it does not provide a novel perspective or deeper analysis of why this occurs in the context of the proposed training regime. The paper could benefit from a more detailed explanation of the underlying mechanisms that cause this performance degradation.
3. Current LVLM starts with a fully pre-trained LLM. But it seems not many strong LLMs can release their weight at 80%. What are the practical implications of this paper's' findings given the limited availability of partially trained LLM checkpoints? The paper does not address the practical challenges of implementing the proposed approach in real-world scenarios where access to intermediate checkpoints is limited. The paper should discuss alternative strategies or approximations that could be used with fully trained models.
4. Would like to see the final model trained by this paper compared with existing LVLMs such as mentioned in paper's Table 1 or well-recognized models such as LLaVA-Next, LLaVA-One-Vision etc. The paper lacks a direct comparison with state-of-the-art LVLMs, making it difficult to assess the practical significance of the proposed training strategy. A comparison with established models would provide a more concrete understanding of the performance gains achieved by the proposed method.

### Questions
1. This is a clarification question: When incorporate image at a early time, does that mean more visual data is trained or seen by model? 
2. I think the name of "LLaVa" should be "LLaVA".

### Soundness
3

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
4

### Summary
This paper investigates the effect of image-text pretraining in large vision-language models using a one-stage approach, in contrast to the typical two-stage method where a text-only language model is adapted into a vision-language model. The study examines various factors during pretraining, such as the amount of text-only pretraining data, and the quantity, type, and ratio of image pretraining data. Specifically, after text-only training, the authors investigate the impact of when to start image-text training, the ratio of image-text pairs when performing image-text training, the impact of instruction-tuning data, and the finetuning epochs on image instruction tuning. After each factor is implemented, the model is followed by image instruction-based tuning, and each factor is then evaluated on VQA and text-only QA tasks. Experiments are conducted on a 1B model, with 28B tokens following the scaling law of (parameters x 20). Interesting findings in multimodal pretraining are deduced.

### Strengths
Generally, many strong insights that can advance the research of vision-language pretraining and Multimodal LLMs are deduced. 

- I find that the insight of continued training at 80% preferable to training from the 100% pretrained text model, with a 90-10 image-text ratio, very interesting and will likely have a good impact on the community. 

- The training from scratch insight (3.3) is also very interesting. This will highlight the importance of having a strong text-only model before interfering images. Interestingly, many old (2020-2022 century) vision-language models such as OSCAR, UNITER...etc, were following this "from-scratch" paradigm. 

- I also find the insight on image instruction finetuning to also be degrading text-only task performance (3.5), interesting. This allows the community to deduce that when multimodal LLMs are instructed with text-only, they dont perform at their best. This could be helpful for systems to select the non-finetuned model when the prompt does not include an image.

### Weaknesses
 - [W1] My main problem is that these insights are only demonstrated on QA and VQA tasks, which I dont find enough for deducing generalizable insights. Good VQA performance does not necessarily reflect general performance. There are a suit of benchmarks (e.g., those used in LLava) used to evaluate the vision-language models. At least include other vision-language tasks such as image captioning and its variations? Visual entailment? VQA with Textual Explanations (VQA-X) and visual entailment with explanations (e-SNLI-VE) can also be good dataset for testing. 

- [W2] Something in Figure 5 caught my attention. When the image ratio is 0% (as if no image data is added, and we continue training on text-only data, as in a normal text-only LLM), the VQA performance is already around 75%, even though the model has seen no images. This makes me wonder that the model is answering questions without really looking at the image (this is a well-known bias problem in VQA models, presented in [R1]). Therefore, i am afraid these results may reflect biased models. I wonder what the results are without using any images? What about other VQA reasoning datasets such as A-OK-VQA? 

- [W3] The authors mention in L739 in the appendix: “This time, we also make sure to mask out any system prompt and human question, only keeping the model responses unmasked.” If no question is there in the image instruction tuning stage, then this is not *instruction* finetuning (this is just a different dataset of image-text pretraining, similar form to the DataCompDR-1B). What is the point of conducting *instruction* tuning then? Im not sure exactly what is the rationale behind masking out the question from the instruction? 

Other minor points (do not affect my decision):

- How is the image-text training on DataCompDR-1B dataset done? Is it to generate the caption autoregressively? Is it via Masked VL modelling? The authors dont mention this. I understand from section C that the authors dont use prefixLM (no image-image attention), and only casual modeling and text-image attention. Therefore, I assume that they predict the caption autoregressively? If so, please mention this, as this is not a trivial point, since many works in the literature use different VL pretraining objectives. 

- In 3.4, when x% of image instruction tuning data is added during the image-caption training, is the same data repeated during the image instruction finetuning stage? 

- L182-187, I feel this should go to the related work.

### Questions
My biggest problem is W1, and im afraid no general conclusions can be drawn. If time permits, I would like that the authors verify their insights on at least another task (e.g., captioning, VQA-X, e-SNLI-VE). I will increase my score if the authors address this concern. W2 is also concerning.

### Soundness
3

### Presentation
4

### Contribution
4
