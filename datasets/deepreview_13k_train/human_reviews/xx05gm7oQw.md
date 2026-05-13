# Debias your VLM with Counterfactuals: A Unified Approach

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Recent advances in vision-language research have produced numerous foundation models that excel in tasks such as image classification, image-text retrieval, and image captioning. However, these models are shown to exploit spurious correlations in biased training data, raising fairness concerns for discrimination against underprivileged groups. 
In this work, we propose CVLD, a unified framework for quantifying and mitigating vision-language biases in a task and domain-agnostic setting. By defining a causal intervention module that produces counterfactual image-text pairs, we apply causal fairness metrics to capture the discrepancy between model predictions on original and counterfactual distributions.
Building on the universal fairness notion, we propose a set of bias-free adaptation techniques to mitigate the bias of pre-trained VL models by optimizing their robustness to interventions on the protected attribute, requiring minimal modification to the naive training pipeline. CVLD demonstrates robust debiasing results on image classification, retrieval and captioning using adaptation datasets of varying sizes, validating the importance of counterfactual data in studying vision-language bias.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a simple framework to debias vision-language models. First, one generates a text prompt for the target image that can guide the image editing procedure. Second, one generates a counterfactual image from the text prompt that has been edited by flipping the bias-related word (e.g., boy -> girl). Third, one fine-tunes the target VLM with the generated counterfactual images. The empirical results show that this method can be used to mitigate the gender bias of many VLMs.

### Strengths
- **Soundness.** The proposed framework is very reasonably designed; it makes perfect sense that such a method will work, given access to well-performing LLMs and text-based image editors.

- **Novelty.** As far as I know, the method CVLD is novel.

- **Significance of the topic.** VLMs are now one of the core backbones of most machine learning applications, and thus having a safety guarantee on such foundation models is a very important yet understudied topic.

- **Writing.** The paper is clearly written and easy to read, despite having many typos.

### Weaknesses
 - **Limited Empirical Evaluation.** The proposed method has been evaluated almost exclusively on a specific type of bias---the gender bias. This is a very severe limitation for a paper which frames itself as targeting general bias in VLMs; the paper exemplifies racial bias multiple times in the text. If the authors are exclusively targeting the gender bias, a significant portion of this paper should be re-written to clarify this point. The lack of experiments on other biases, such as racial or age bias, makes it difficult to assess the generalizability of the proposed method. It is unclear if the method's effectiveness is specific to gender bias or if it can be applied to other types of biases with similar success. The paper should include experiments on other types of biases to demonstrate the method's broader applicability.

- **Relies on external models, which may be prone to other types of bias.** The debiasing procedure of this paper relies on the generative/editing capabilities of existing models (e.g., prompt-to-prompt editing). This is a vulnerability in terms of a bias, because such edited images may be prone to other types of biases that may be difficult to detect (see, e.g., Bias-to-Text by Kim et al. (2023)). I wonder if authors could demonstrate any "robustness" of the proposed paradigm to the potential biases hidden in the LLMs or prompts. Specifically, the paper does not address the potential for the editing process to introduce new biases or amplify existing ones. For example, if the editing model has a bias towards generating images of a certain race or age, this could negatively impact the debiasing process. The authors should investigate the potential for bias in the editing model and provide a discussion of how this could affect the results.

- **(minor) Clarity.** Figure 1 is not very informative and difficult to parse what the figure is trying to say. What the sketch part is trying to say is unclear (perhaps more details in the caption will be better). Also, it took me some time to notice that "M -> F" means male -> female. The "lock" figures are somewhat difficult to tell whether they are locked or unlocked (maybe use frozen <-> fire analogy, like many other papers, or use additional color cues?). The figure lacks clear labels and explanations, making it difficult for the reader to understand the proposed method. The authors should improve the figure's clarity by adding more details and explanations.

### Questions
Please see the "weaknesses" section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to unify the study of biases across vision-language problems. It attempts to create counterfactuals to swap the gender in an image-text pair using readily available tools like LLMs and image-editing methodologies. With the help of the generated counterfactuals, it is shown that the model performances improve for multiple tasks like image retrieval, image classification and image captioning.

### Strengths
1. The use of LLMs and other models like Instruct Pix2Pix is smart to generate counterfactuals.
2. The authors adopt different ways to incorporate these counterfactuals into multiple downstream tasks as it is not always possible to alter the pretraining itself.
2. Using existing VLMs on top of the original datasets along with the counterfactuals seem to help reducing the bias while also maintaining model performance.

### Weaknesses
1. Lack of novelty: The paper simply uses some state-of-the-art LLM to generate counterfactual text, and null text inversion/InstructPix2Pix to generate the counterfactual images. The combination of these tools, while effective, does not present a novel methodological contribution. The approach is essentially an application of existing tools rather than a development of new techniques in bias mitigation.
2. The paper only covers gender biases - no experiments on other biases like racial/age. Biases may exist even in non-social cases (like the water-land bias in the popular Waterbirds dataset). This has not been explored. The lack of exploration into other biases limits the generalizability of the proposed method. The paper should investigate how the method performs on other types of biases, such as those related to object co-occurrence or scene composition, which are also known to affect VLM performance.
3. No comparison with other debiasing VLM methods. The paper does not benchmark against existing debiasing techniques, making it difficult to assess the relative performance of the proposed approach. The lack of comparison makes it hard to determine if the proposed method offers any advantages over existing techniques. Specifically, methods that use adversarial training or re-weighting of training samples should be considered as baselines.
4. The paper advocates generating counterfactuals for bias mitigation. However, not many sample examples are shown even in the supplementary. The absence of a detailed qualitative analysis of the generated counterfactuals makes it difficult to assess the quality of the generated data and whether it introduces new artifacts or biases. The paper should include more examples to demonstrate the effectiveness of the counterfactual generation process.
5. Not all biases (for example, models are seen to learn various spurious correlations like camels can only be present in deserts, airplanes can only be in the sky, etc) are quantifiable like gender. Is generating counterfactuals the solutions for those kinds of biases too?

### Questions
1. The method of generating counterfactuals does not generate diverse images, but only modifies the existing images. Generating diverse images can help the models further. Can this be addressed?
2. What if multiple biases are present at once? Like gender and race together. Can this method of generating counterfactuals handle such scenarios?

### Soundness
4 excellent

### Presentation
3 good

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
This work considers the problem of bias mitigation on vision-language models (VLMs). The authors introduced Counterfactual vision-language debiasing (CVLD), a technique that can be summarized in two main contributions: 1- a data generation pipeline based on off-the-shelf generative models to create counterfactual augmentations from real data; 2- a bias mitigation strategy based on fine-tuning a VLM using the generate counterfactuals. The authors evaluate the proposed approach empirically on 3 tasks: image classification, image-text retrieval, and image captioning. Experiments are carried out using a model from the BLIP family and considering both fairness and task performance metrics. Overall, results show that the proposed yields the best trade-off between improving fairness (i.e. mitigating biases) and attaining good performance in the task.

### Strengths
- The paper tackles a critical problem and very relevant open research question: how to mitigate bias on foundation models;

- The manuscript is overall well-written and most sections are easy to follow; 

- The counterfactual augmentation approach is grounded in formal definitions from the counterfactual fairness literature;

- The experimental evaluation is extensive in the number of considered tasks.

### Weaknesses
 - One of the central claims of the work is that the proposed approach is a unified way to mitigate bias in VLMs across multiple tasks, as per the following evidence:
  - In the title (Debias your VLM with Counterfactuals: A **Unified** Approach, bold text by myself).
  - Also throughout text: e.g. In Section 2 "[...] we focus on a task-agnostic fairness framework for VLMs, unifying the study of bias across different tasks and domains." ).

   Claiming that the proposed approach is unified and task-agnostic seemed reasonable until Section 4. However, after reading through the details of how fine-tuning with synthetic data should be carried out for the three considered tasks, it seems to me that CVLD practical instantiation takes a very different format from task to task, rendering it a specific and not-unified framework for debiasing. The core of the method, counterfactual data augmentation, is indeed task-agnostic, but the fine-tuning process requires task-specific modifications. For image classification and captioning, the training data is augmented with counterfactual examples, weighted by a hyperparameter. For image-text retrieval, the contrastive loss is modified to account for counterfactual candidates. These differences in fine-tuning procedures across tasks undermine the claim of a unified approach.


- One of the key parts of the introduced approach is the counterfactual data generation. However, the authors did not mention at any part of the manuscript details of the evaluation of the data generation pipeline. Moreover, it is not clear how the quality of generated counterfactuals could affect the performance of CVLD. Moreover, other fine-grained aspects such as *how much synthetic data is needed* and how the number of synthetic samples used at training time affects performance were not addressed in the manuscript, making it difficult to judge to what extent this framework would generalize to other scenarios where it might be difficult to generate high quality counterfactuals.  The lack of quantitative evaluation of the generated counterfactuals, such as measuring their realism or the degree of attribute change, makes it difficult to assess the effectiveness of the data generation process. It is also unclear how the number of generated samples impacts the debiasing performance. For instance, is there a point of diminishing returns, or does more data always lead to better results? This is critical for understanding the practical applicability of the method.

- Some parts of the text do not seem to reflect the actual insights that can be extracted from the results. For example, in the introduction, the authors mentioned that CVLD "demonstrates striking effectiveness for the most studied problems in the bias literature" while it is not clear from the results that the CVLD demonstrates **striking** effectiveness, neither there are references to support the statement that the considered problems in this work are the most studied ones in the bias literature. The claim of "striking effectiveness" is not supported by the presented results, which show moderate improvements in fairness metrics. Moreover, the assertion that the chosen tasks are the most studied in bias literature is not substantiated with any evidence or references.

- The experimental results are a bit confusing and hard to parse. The employed metrics in the evaluation are not standard in the literature and it is not clear whether an improvement is observed when a metric increases or decreases. Moreover, it is not clear why some methods were grouped in different parts of the tables (e.g. in Table 1 it is not clear why both CVLDs are in different sections from BLIP-PT and the ResNet-50, aren't they directly comparable?). On a similar note, it is not clear how the different bolded numbers in the tables represent and how they should be compared against each other. The use of non-standard metrics makes it difficult to compare the results with existing work. The tables lack clarity in terms of grouping methods and highlighting the best results. For instance, it is not clear why the CVLD results are separated from the baseline BLIP-PT results, as they should be directly comparable. The meaning of the bolded numbers and how they should be interpreted is not clearly explained.

### Questions
- How can all the three different approaches to fine-tune VLMs with counterfactual data be seen as a unified framework? Also, how would this generalize to other tasks such as, for example, counting and object detection?

- How is CVLD performance affected by counterfactual data generation quality? How did the authors assess the quality of generated data in order to know whether it was "good enough" to be employed for bias mitigation?

- How computationally expensive is the data generation approach? How does it compare to techniques that do not rely on data generation for bias mitigation?

- How is the performance of CVLD affected by the choice of the lambda hyperparameter?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Vision-language models (VLMs) have achieved impressive performance on various tasks but have been shown to exhibit biases due to biased training data. In this study, the authors propose a simple debiasing framework, counterfactual vision-language debiasing
(CVLD), that aims to quantify and mitigate biases in vision-language models. CVLD introduces a causal intervention module to generate counterfactual image-text pairs and use causal fairness metrics to measure the difference in model predictions between original and counterfactual distributions. The authors also propose bias-free adaptation techniques to minimize bias in pre-trained models, achieving promising results in image classification, retrieval, and captioning tasks.

### Strengths
1. The paper provides a robust framework that scales to different visual-language downstream tasks like image classification, image retrieval, and image captioning tasks.

2. The proficiency of CVLD is demonstrated in a set of fine-tuning experiments across different tasks using well-established fairness measures.

3. The paper is well-written and details the objectives and results for each of the downstream tasks separately.

### Weaknesses
1. One of the primary weaknesses of the paper is its novelty in terms of the main framework. In order to infuse fairness, Agarwal et al. [1] introduced a triplet-based objective that maximizes the agreement between the original graph and its counterfactual views. Given that CVLD follows suit and incorporates a similar framework, the novelty is limited.

2. In most cases, the counterfactual image seems noisy and is non-reflective of the counterfactual protected attribute (e.g., in Fig. 3, we don't observe women riding the rowboat). In such cases, are the counterfactual just some noisy version of the original image? How do we attribute the debiasing to a protected attribute if the quality of the counterfactuals is not good?

3. The framework is a data-extensive approach, i.e., for debiasing, it needs a counterfactual version of each image-text pair and expensive fine-tuning of VLMs for debiasing.

### Questions
Please see the weaknesses for more details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
