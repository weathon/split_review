# From Generalist to Specialist: Adapting Vision Language Models via Task-Specific Visual Instruction Tuning

- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
Large vision language models (VLMs) combine large language models with vision encoders, demonstrating promise across various tasks. However, they often underperform in task-specific applications due to domain gaps between pre-training and fine-tuning.
We introduce VITask, a novel framework that enhances task-specific adaptability of VLMs by integrating task-specific models (TSMs). VITask employs three key strategies: exemplar prompting (EP), response distribution alignment (RDA), and contrastive response tuning (CRT) to improve the task-specific performance of VLMs by adjusting their response distributions. 
EP allows TSM features to guide VLMs, while RDA enables VLMs to adapt without TSMs during inference by learning from exemplar-prompted models. CRT further optimizes the ranking of correct image-response pairs, thereby reducing the risk of generating undesired responses.
Experiments on 12 medical diagnosis datasets across 9 imaging modalities show that VITask outperforms both vanilla instruction-tuned VLMs and TSMs, showcasing its ability to integrate complementary features from both models effectively.
Additionally, VITask offers practical advantages such as flexible TSM integration and robustness to incomplete instructions, making it a versatile and efficient solution for task-specific VLM tuning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a VITask framework that enhances the adaptability of Vision Language Models (VLMs) for specific tasks by integrating Task-Specific Models (TSMs). It employs strategies like guiding VLMs with TSM features, enabling adaptation without TSMs during inference, and optimizing the ranking of correct image-response pairs. Experiments on medical diagnosis datasets demonstrate that VITask outperforms standard VLMs and TSMs, providing flexible integration and robustness to incomplete instructions.

### Strengths
1.	The overall writing is relatively smooth and easy to understand. 
2.	The paper has made a detailed design in the method of constructing the dataset. 
3.	The paper has conducted detailed experiments on existing medical datasets.

### Weaknesses
1.	The overall motivation is to finetune existing VLM for downstream tasks. After fine-tuning, the model can only be used for a specific task, which may hinder the original generalizability of VLM. The authors seem do not consider this issue.
2.	From the experiment, it can be observed EP is most useful, while other modules bring marginal improvements. Whether the other two modules are necessary requires to be further explored.
3.	Lisa [1] also adopts similar prompt tuning techniques like EP, and what’s the difference between these methods, and what is the technical advantage of EP?
4.	The comparison lacks comprehensiveness, as numerous medical VLMs exist in the field.
5.	The effectiveness of the proposed method is only demonstrated in the medical field, therefore the title is kind of over claimed. If the method is general, more experiments on other datasets are required.

### Questions
See the comments

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a combination of strategies, exemplar prompting (EP), response distribution alignment (RDA), and contrastive response tuning (CRT), to adapt general-purpose generative VLMs for specialized medical classification tasks. Through experiments, the authors show that their method VITask , leveraging these three algorithmic components, can outperform task-specific models (TSMs), which are essentially fine-tuned ViTs, on a variety of medical classification tasks. In ablation experiments, the authors demonstrate that EP contributes the most performance boost while RDA and CRT are also complementary.

### Strengths
The paper states the problem it aims to solve clearly. The proposed method is validated on a wide range of medical datasets.

### Weaknesses
The biggest issue of the paper is the lack of depth. While it ablates the impact of each of the algorithmic components, they authors spent little effort trying to understand why each of them work and to compare them against existing methods.

1. It’s not clear what makes EP successful.
    - I strongly suspect the performance gain is mostly due to the fine-tuning of the connector module. The critical experiment of simply having both the connector and the LLM (LoRA params) trainable is missing.
    - Additionally, an experiment comparing EP with prefixing tuning [1] will tell whether it’s necessary to condition the prefix (additional tokens to the LLM’s embedding space) on the image at all to get good performance. Essentially, I need to see experiments showing me EP > fine-tuning the original VLM’s connector + prefix tuning to be convinced it’s novel.
    - I also don’t buy the claim that fine-tuning the Vision model in VLM will distort vision language alignment at all. If fine-tuning the Vision model is harmful, wouldn’t the trained LoRA weights be more harmful as well? A controlled experiment where the vision encode is also trained is needed. I am confident this will make EP perform even better.
    - Finally, other works with the same core methodology should be discussed. For example, Graph Neural Prompting [2] builds a knowledge graph based on the prompt and multiple choice candidates and generates a conditional prefix to prompt the LLM. I think the idea is extremely similar to EP.
2. Regarding RDA: this is essentially a fancy way of saying knowledge distillation but no relevant papers are cited. Regarding implementation, the author mentions gradient detachment. If I understood it correctly, this just means the TSM, or the “teacher”, is not trained while the goal is to train the student. Shouldn’t this be the default setting anyway?
3. Contrastive Response Tuning: as part of the core methodology, the paper should compare its effectiveness against existing methods, such as contrastive decoding [3][4].

Issues mentioned above should be addressed. Otherwise this work should aim for a more application-oriented venue.

The notations issues.

- In equations (1), (2), (3), (5), (6), why is there a min() operator on the left hand side? The author seems to mix it up with the argmin notation. I think the author should remove the min() and avoid argmin() like notation since not all parameters are trained.

Minor grammar issues
- For example, Takeaway #1: TSM features can prompts (prompt) VLMs to generate desired responses.

### Questions
1. For TSM, does it use the same encoder as the one used by the target VLM? How about the connector?
2. What parameters are tuned in RDA exactly? I also don’t get how is it really different from tuning from the ground truth labels, which are used anyway. In other words, isn’t p_theta(response | exemplar) just an approximation of the ground truth label? In fact, this pseudo-label is worse since it can be wrong? Also for classification tasks, if the model only decodes a single label, does it really matter to learn the whole distribution instead of an one-hot label? If we look at table 2, RDA indeed improves upon vanilla, but what does vanilla mean? Is it just the base VLM that’s not fine-tuned at all for those medical tasks? I need to see an experiment where you just fine-tune with the ground truth labels in the training set to really understand the role of RDA. Now I tend to think you can totally get rid of it. 
3. For both RDA and CRT, what did you do to deal with the situation when the label consists of more than 1 token due to tokenization?
4. I want to know the implementation detail of how you extract the answer from the generated output from the VLM. Apparently since it’s free-form generation the format might be slightly off. Are there any instances where the model outputs a semantically equivalent label that’s not an exact match? What’s the percentage of such instances before and after your fine-tuning?
5. I wonder if the authors can explain more on the motivation of adapting the VLM for classification tasks. I think this task is only meaningful if either 1) the original generative capabilities can be preserved, or 2) the fine-tuned VLM is actually better than SoTA vision models, otherwise we might as well use a predictive classifier that’s smaller and easier to fine-tune. Thus, I think the authors should either 1) present evaluations on non-medical tasks to show there’s very little degradation, or 2) compare against the SoTA vision model, which is probably not a ViT pretrained in 2020.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Although VLMs have excelled in understanding generic images, they fall apart for out-of-distribution task-specific applications. This paper claims that this could be due to the lack of comprehensive image representation and indirect tuning objective VLMs used to optimize. This paper proposes a framework that leverages representation from task-specific models as complementary information and optimizes the VLMs. Additionally, it explores how the inference can be done without task-specific models using two proposed methods RDA and CRT.
Considering the high costs of fine-tuning and inference with LLMs, along with the minimal performance gains, why should a user prefer using VITask over enhancing TSMs?

The paper is well-written but could be improved for better readability.

### Strengths
The motivation of the paper is clear and the authors provided adequate evidence to show why the proposed method can be useful in task-specific applications.

The task-specific instruction tuning section is quite interesting and the papers validate how each proposed component improves the performance of VLMs.

The paper has a detailed section providing intuition and empirical evidence to support the claims.

### Weaknesses
As mentioned in the limitations section, exploration of the method is highly limited to classification tasks. Additional tasks would be more interesting using an LLM, which has rich information embeddings.

Given the high computation budget and a marginal improvement in performance compared to TSMs, I would try to improve the TSMs which are cost-effective for training and inference. ( I consider the results as marginal improvement, the considered dataset is comparably simpler than the actual applications.) For example, optimize the model architecture, focused hyperparameter selection, Select and Fuse futures, and an ensemble of smaller models.

The paper is comprised of a lot of detailed text, which also seems to be a weakness of the paper. Authors could provide more visualization to interpret the results and behaviour of each module. Overall, the interpretation of results could be improved for better readability. You may provide more visualization to explain the benefits of the proposed modules or interpretation analysis how the proposed module benefits  compared to TSMs or vanilla VLMs.

The paper presents a few concerns :

1. The figure related to the RDA analysis referenced in Lines 264-266 is missing. As it stands, the current figure appears to be a bar chart of the EP results. Could please provide the figure?

2. The authors should consider using different formatting styles for equations (3-6). When the terms in the equations are presented in the same style as the surrounding text, it can be confusing (Line 280). Differentiating the formatting will enhance readability.

3. There are spelling errors in Figure 1 (d).

4. The word "often" is repeated in Line 041.

### Questions
1. Authors should explain why using Vision-Language Models (VLMs) with a high computational budget is more beneficial than improving Task-Specific Models (TSMs). I would recommend an empirical analysis of the cost and performance benefits of VITask versus TSMs to.

2. TSMs provide better task-specific representations than general vision encoders. Could you clarify why the results decline significantly when embeddings are completely replaced by task-specific representations? Did you utilize the CLS token from Vision Transformers (ViT) or the entire patch embeddings?

3. Why do we need to optimize Stage 2 with the same loss functions used in Stage 1 without scaling them? After optimizing the Stage 1 model to minimize the Stage 1 loss, using it in Stage 2 could potentially harm the fine-tuning process. Have you considered applying a scale to the Stage 1 loss functions?

4. In line 423, it is mentioned that a novel vision-language connector is introduced in the paper, but no details about this connector are provided in the text. Could you please include more information about it?

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
This paper first investigate why fine-tuned (VLMs) often lag behind TSMs in performance (use image classification as a case study) and then propose a new framework that can enhance the performance of VLMs on task-specific applications. They conduct it through integrating task-specific models (TSM) into VLMs in fine-tuning with 3 strategies, exemplar prompting (EP), response distribution alignment (RDA), and contrastive response tuning (CRT). EP allow TSM features to guide VLMs while RDA enables VLMs to adapt without TSMs during inference by learning from exemplar-prompted models. CRT further optimizes the ranking of correct image-response pairs by maximizing likelihood of correct image-response pairs while minimizing that of  incorrect pairs. They conduct two-stages training. The first stage is fine-tuning VLMs using vanilla visual instruction tuning in conjunction with EP and RDA. The second stage is fine-tuning VLMs using all strategies. The experiments focus on classification tasks on medical domain.

### Strengths
- The idea and strategies used to combine TSMs to VLMs to boost performance of VLMs (without using TSMs to VLMs on inference stage based on RDA mechanism) on task-specific applications are interesting. It helps to remove the limitation of VLMs when fine-tuning on task-specific applications.
- The performance of experiments on medical image classification are good.
- The paper is well-written and easy to follow.

### Weaknesses
 - The current experiment results are good, but the number of experiments and baseline models are insufficient, only 4 baseline models (including task-specific model). Can you compare your method with more other baselines, including some works you have mentioned in related works section which attempt to integrate VLMs with task-specific models and more VLMs such as InstructBLIP, BLIP-2, and Qwen-VL-Chat? 
- Because you did classification experiments on medical domain and there are currently many VLMs pre-trained on medical datasets, why you chose to test on the particular VLMs used in the study. In my opinion, it is important to test this approach on more VLMs which were pre-trained on medical datasets such as LLaVA-Med, Biomed GPT, etc. to make sure applying this method on these VLMs give significant improvement results.
- I am concerned about the time used to fine-tune a VLM using your method, because you need to fine-tune a task-specific model on the dataset first before combining it with VLMs and then fine-tune the VLMs. Can you give me more detail about the resource you use to fine-tune VLMs and the total time for the training process to finish using your method and vanilla methods (comparisons between your method and baseline approaches) ?

### Questions
As you have mentioned in the paper, testing this approach only on medical domain is not enough to make sure your method is good. I hope that you can give more experiment results on other non-medical domains such as natural images.

### Soundness
3

### Presentation
4

### Contribution
3
