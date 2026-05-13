# In-Context Unlearning: Language Models as Few Shot Unlearners

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Machine unlearning, the study of efficiently removing the impact of specific training instances on a model, has garnered increased attention in recent years due to regulatory guidelines such as the \emph{Right to be Forgotten}. Achieving precise unlearning typically involves fully retraining the model and is computationally infeasible in case of very large models such as Large Language Models (LLMs). 
To this end, recent work has proposed several algorithms which approximate the removal of training data without retraining the model. These algorithms crucially rely on access to the model parameters in order to update them, an assumption that may not hold in practice due to computational constraints or having only query access to the LLMs. In this work, we propose a new class of unlearning methods for LLMs called ``In-Context Unlearning.'' This method unlearns instances from the model by simply providing specific kinds of inputs in context, without the need to update model parameters. To unlearn specific training instances, we present these instances to the LLMs at inference time along with labels that differ from their ground truth. Our experimental results demonstrate that in-context unlearning performs on par with, or in some cases outperforms other state-of-the-art methods that require access to model parameters, effectively removing the influence of specific instances on the model while preserving test accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper looks at the problem of machine unlearning in the context of LLM. In particular, the authors look at in-context unlearning, where the forget example is fed into the model context window with a flipped sign, and no gradient update is necessary. The authors show that the proposed method is competitive regarding unlearning effectiveness and accuracy on the retain set.

### Strengths
The paper poses a very interesting problem and it can motivate future works. The paper is written nicely and it is easy to follow.

### Weaknesses
I found the particular setting in this paper to be a little restrictive (but it's not crucial since this paper is almost initiating a new setting) that only one example is forgetting.



### Questions
1. In eq(2), what is $\hat \theta$, does this mean in different scenarios, you test with different estimators, e.g. the ERM $\theta(S)$ and the unlearned model $\bar f$?
2. When you actually perform the LRT in eq(2), do you take each (x,y) as one test samples?
3. When you fine-tune with GA, what are the stopping criteria? Do you have a suggestion on some rule-of-thumb?
4. One related prior work should be included and discussed, see [1].

[1] KGA: A General Machine Unlearning Framework Based on Knowledge Gap Alignment

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces an innovative method called "In-Context Unlearning" (ICUL) designed for large language models (LLMs). ICUL facilitates the unlearning of specific training instances by providing contextual inputs at the inference stage, thereby eliminating the need for modifying model parameters. Experiments confirm that ICUL can effectively remove targeted training information while maintaining performance levels.

### Strengths
* The paper brings a novel approach to the domain of machine unlearning, effectively leveraging the In-Context Learning (ICL) paradigm to achieve unlearning in text classification tasks without any modification to model parameters.
* The design of ICUL requires minimal computational resources, offering a cost-effective alternative to traditional unlearning methods that involve model retraining.
* The paper includes a thorough ablation study, which affirms the effectiveness of the key components in ICUL, specifically label flipping and the addition of unforgotten samples.

### Weaknesses
 * The experiments are conducted only on Bloom's 560M and 1.1B models, lacking comparison with newer, larger models like LLaMA, Falcon, or ChatGPT. Moreover, ICUL is compared to only a single benchmark method (GA), which in some settings even outperforms ICUL, making it difficult to assert ICUL's superiority.
* The method is tailored for binary classification tasks and does not easily extend to multi-class or more complex NLP tasks. The paper also falls short in clarifying the real-world scenarios and problems it aims to address, leaving its practical utility ambiguous.
* The method's design, focusing on unlearning single samples in classification tasks, makes it less suitable for handling large volumes of unlearning requests in realistic scenarios.
* The paper doesn't delve into the theoretical underpinnings that explain why ICUL is effective at unlearning, leaving a gap in our understanding of the method's robustness.
The paper fails to compare or reference highly related work in the area of concept erasure in NLP, e.g., 1,2,3.

### Questions
How is ICUL designed to scale for real-world applications that demand continuous unlearning?

### Soundness
3 good

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
The authors introduce an innovative method termed 'Incontext machine unlearning.' A standout feature of this method is its ability to operate without needing access to the model's parameters, instead relying on in-context querying during inference. The crux of their work is a unique approach to unlearn specific training data points. Instead of resorting to computationally expensive retraining or finetuning, they suggest querying the language model with a carefully curated prompt during inference. This prompt is crafted to give the impression to the language model that it hasn't encountered a specific training instance. To implement this, upon receiving a deletion request, they recommend flipping the label of the targeted instance and appending it accordingly. Subsequent steps involve incorporating a set of randomly selected labeled example pairs, followed by the query input. The intention behind this structured query prompt is to effectively unlearn a designated training instance. While I find the core idea compelling, I feel the experiments section could benefit from enhanced clarity and depth. The presented results, especially the ROC curves, demonstrate the method's superiority over baseline techniques. The concept genuinely intrigues me, but I believe its presentation in the paper could be further refined for clarity and impact. I also think comparisons with prompt based adversarial attack methods would be necessary ([1] or related works). I have explained in detail about this below.

[1] Raman, Mrigank, et al. "Model-tuning Via Prompts Makes NLP Models Adversarially Robust." arXiv preprint arXiv:2303.07320(2023).

### Strengths
1) The idea of unlearning a subset of the training dataset through Incontext querying is particularly intriguing. This approach could significantly lessen the computational burden compared to previous machine unlearning techniques, like gradient ascent.

2) The presented ROC curves for the ICUL method are close to the diagonal, sufficiently backing the hypothesis that the proposed method is indeed successful in reducing the likelihood of the forget set belonging to the training set. (However, there are a few points that I would like to make regarding the presentation. Please see below.)

### Weaknesses
Firstly, thank you for an insightful work. I hope my comments will further strengthen your work.

1) Though, the presented idea is labeled as machine unlearning, I would like to point out that the presented approach queries the language model using a specific prompt designed to reduce the confidence of the model on a few training instances from the forget set. When queried using alternative prompts, there is no guarantee that the language model would perform with similar characteristics. Empirical evidence is the “Dependence on forget point” ablation study where using a random instance instead of the forget instance (i.e., a changed prompt) lead to inferior results. However, methods such as gradient ascent, though computationally more expensive than the proposed method, would lead to a reduction in likelihood of the forget set belonging to the training set irrespective of the query. In Fact they alter the weights such that the traces of forget set on the model weights would be minimized. Hence I believe this setting would ideally be more suitable for machine unlearning context. Speaking about the computational complexity of the gradient ascent method, I believe since the forget set cardinality is much less than the training set, the computational cost would not be very demanding and also it will be similar to finetuning language model on extremely low-resource scenarios.

2) I think it is necessary to compare with a few prompt based adversarial attack methods such as [1] or related methods. As stated above, the presented approach queries the language model using a specific prompt designed to reduce the confidence of the model on a few training instances from the forget set. So an alternative way to view the proposed method (deviating from machine unlearning) is to query a language model with a prompt such that the likelihood of the forget set belonging to the training set is reduced. Thus, it is like learning the perturbations to the input prompts that change the model predictions. Thus learn for such perturbations to the prompts only for the forget set. I believe that it serves a crucial baseline.

[1] Raman, Mrigank, et al. "Model-tuning Via Prompts Makes NLP Models Adversarially Robust." arXiv preprint arXiv:2303.07320(2023).

3) The presentation of the experiments section needs to be improved. For instance, i) Section 4.2 is redundant and is better explained in the ablations section. ii) In table 1, ICUL is mentioned without the query length (s) however it is mentioned with the query length in table 2. It is important to maintain consistency. Also it makes it more clear for the reader to mention what it means by ICUL (s) in the caption of the tables.

4) Baselines are not clearly mentioned in the experiments section. For instance, GA is not clearly mentioned. Also when mentioning the ‘Baseline’ in section 5.2, “consists of the decision not to unlearn the point from the model”. It is not clear what it means. I am assuming that the authors are referring to "Compare train vs. held out samples on the initial model fθ(S)" in section 5.1. Maybe mentioning it directly where they first introduce will make it less confusing.

5) The experiments section requires further elaboration. While the authors assert that their method outperforms the baselines, they should delve into why this is the case. For example, the claim that their method consistently surpasses the GA baseline is supported by empirical evidence however remains unexplained. Intuitively, the GA method, which uses gradient ascent to intentionally forget the 'forget set', should be on par with or even superior to the proposed method. Clarifying this would provide valuable insight.

### Questions
1) The format for the incontext unlearning is as follows: “[Forget Input] [Flipped Label] \n [Input 1]1 [Label 1]1 \n · · · [Input s]s [Label s]s [Query Input]s+1 ”. My question is if I want to query on [Forget Input] again the format is as follows, “[Forget Input] [Flipped Label] \n [Input 1]1 [Label 1]1 \n · · · [Input s]s [Label s]s [Forget Input] ”. Is my understanding correct? If so, it would be interesting to know how many times the output of the language model is [Flipped Label]? We can understand the broader impact of such a querying by further knowing these dynamics.
2) Also from the results, it is evident that the method performs at par with the GA method however it is not really clear why the GA method performs worse than the Baseline (especially the sudden spike towards 10^(-1) FPR for Amazon and Yelp). Could you explain why that is the case? We are optimizing by performing gradient ascent so it has to be below baseline at least?
3) In section 4, it is mentioned that “For finetuning, we are using the standard causal language loss which encourages the model to predict the next token correctly”. So when the models are fine-tuned on the downstream dataset, why is the result on the train set low, especially for ICUL(6) on SST-2 dataset (Table-2).
4) Please correct the typos and ensure consistency in notation. For example, 'membership inference' is abbreviated in some instances, while in others, it's written out in full.
5) The authors claim "This finding challenges earlier research that argued label flipping of context examples had an insignificant impact on smaller LLMs " in the conclusions. It would be more insightful if the authors can point out why is the case? Or if there is any assumption difference between these works and the proposed work.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
