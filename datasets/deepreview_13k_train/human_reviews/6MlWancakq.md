# COBias and Debias: Minimizing Language Model Pairwise Accuracy Bias via Nonlinear Integer Programming

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
When performing classification tasks with language models, would you prefer having only one highly accurate class or having every class deliver reliable performance? Obviously, a more balanced accuracy among classes better reflects the expectations of the majority of users. \color{black}Especially for large language models (LLMs), the fact that they achieve a fair overall accuracy by in-context learning (ICL) obscures a large difference in individual class accuracies. In this work, we uncover and tackle language models' imbalance in per-class prediction accuracy by reconceptualizing it as the Contextual Oddity Bias (COBias), and we are the first to engage nonlinear integer programming (NIP) to debias it. Briefly, the proposed COBias metric measures accuracy differences among class pairs, with which we reveal the large per-class accuracy differences exhibited in LLMs of varied scales and families. \color{black}Then we propose Debiasing as Nonlinear Integer Programming (DNIP) to correct ICL per-class probabilities towards lower COBias and higher overall accuracy. Our optimization objective is directly based on the evaluation scores by COBias and accuracy metrics, which is non-differentiable and solved by the simulated annealing metaheuristic\color{black}. Evaluations on three LLMs across seven NLP classification tasks show that DNIP simultaneously achieves significant COBias reduction (-27\%) and accuracy improvement (+12\%) over the conventional ICL approach, suggesting that modeling pairwise class accuracy differences is a direction in pushing forward more accurate, more reliable LLM predictions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper shows that accuracy metric hides large differences in individual class accuracies. Focusing on the LLM In Context Learning setting,  the paper defines a new metric called COBias to uncover and measure this imbalance in per class prediction accuracy. 
Further, the authors propose a technique called DNIP (based on integer programming) to mitigate this bias problem by post-hoc correcting the predicted class probabilities. DNIP greatly reduces the COBias while also leading to large accuracy gains.

### Strengths
- The paper studies a really cool topic that is very important but quite under-explored. 
- We know that the widely reported accuracy metric probably masks lot of per class / inter-class details. This by itself if not at all surprising, but the authors quantitatively show that this does happen a lot.
- The COBias metric definition makes intuitive sense and is easy to compute.
- Strong empirical results on a variety of benchmarks. What's cool is that the DNIP technique not only reduces COBias but also leads to increase in overall accuracy.
- This contribution could spur lot of follow-up work. Could also encourage researchers to go beyond accuracy when evaluating results in a classification task.

### Weaknesses
The ICL setup only uses 1-shot example. Given that the main motivation for the paper is demonstrate and mitigate COBias in the ICL setting, I would have expected more baselines. Eg: How does COBias change as you increase the number of shots? What happens in the case where you ensure that each class is represented by at least one example in the prompt? How does more sophisticated prompt engineering impact COBias and DNIP?
Adding these baselines and investigation would improve the paper greatly.

Minor point: In terms of metrics, all the focus is on COBias and Accuracy. But it would have been helpful to at least contrast with some other metrics like macro F1 and micro F1 - do they also uncover issues masked by accuracy?

### Questions
Is COBias also an issue when LLMs are fine-tuned?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Within few-shot in-context learning (ICL), LLMs can achieve great performance for classification tasks. However the raw accuracy can hide prohibitive differences in per-class accuracies. In this paper, this phenomenon is defined as Contextual Oddity Bias (COBias). COBias is a proposed measure of the bias in prediction. Then the authors explore the use of Nonlinear Integer Programming for debiasing existing LLM. The results are reported on seven NLP classification tasks with success.

### Strengths
The paper consider the per-class imbalance in performance for in-context learning classification, as a  bias embedded by the model. This is a nice idea. Then the proposition to debias the model with nonlinear integer programming is also a promising contribution. The experimental results show great improvement in both accuracy and debiasing.

### Weaknesses
There are two main weaknesses.  The first one is about clarity. The paper is sometimes  difficult to read and sentences seem really obscure. Just to take the abstract as example, the first two sentences are really confusing. Maybe it is a problem of order in the ideas. These two first sentences could be easier to understand later in the paper, with more context,  but as a starting point it is really unclear. I will add more examples in the questions part.
Consider: "For language model classification, would you prefer having only one workable class or having every class working? The latter makes more practical uses."  You want to classify language models ? or you want to perform text classification with LLMs ? What do you mean by "workable" here ? and so on. 

We have the same issue with the  first two sentences of the introduction: "We rethink language models’ imbalance in per-class prediction accuracy and reconceptualize it as the Contextual Oddity Bias (COBias). In a nutshell, COBias refers to the difference in accuracy
by a class A compared to its “odd” class, which holds the majority wrong predictions of class A."  To start a paper, more context would be appreciated. 

My second and  scientific concern is about the equation 1. COBias is presented as an attempt to detect when a class is not predicted while it is the good one, and in favor of another one.  It is not completely clear why the equation 1 measures this kind of bias. The definition of the odd class is very interesting: "an odd class to be a class at inference time where predictions of another class are often biased towards it. An odd class is relative to the other class.". However equation 1 does not quantify exactly that, since it relies only on per-class accuracies.
Moreover, the absolute value ignores the fact that one class is better classified than the other.

### Questions
You could open the paper by " For large language models (LLMs), the fact that
they achieve remarkable test accuracy over all class labels by few-shot in-context learning (ICL)
(Brown et al., 2020) can obscure a large difference in individual class accuracies."

The name "liking" is usually followed by "for"

l 161 : it times a correction weight ...  I don't understand the verb times here ? 


Could you define the pointwise mutual information term more precisely ? The footnote helps, but it is not sufficient to understand the motivation of this term, its importance and the sensitivity to the smoothing factor.
The paragraph starting at line 194 remains obscure to me while it is an important aspect of the contributions.  

The choice of simulated annealing is not straightforward. I would think that Branch-and-Bound algorithm are more efficient for this kind of optimization program. However beyond efficiency, maybe there is another motivation in this choice ?

The definition of the odd class looks like an adversarial class maybe you could comment on this since there is a large body of work on that topic.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the phenomenon of Contextual Oddity Bias (COBias), wherein large language models (LLMs) exhibit inconsistent accuracy across distinct classes within classification tasks. Despite attaining high overall accuracy in few-shot in-context learning (ICL) settings, LLMs frequently demonstrate a propensity to over-predict certain classes while exhibiting diminished performance on others. This work formally introduces COBias as a quantifiable metric to assess this imbalance, revealing its prevalence even among sophisticated LLMs with diverse architectures and scales.


To mitigate this issue, the authors propose methodology termed Debiasing as Nonlinear Integer Programming (DNIP). DNIP employs a combinatorial optimization approach to refine per-class probabilities through the introduction of corrective weights, explicitly targeting the reduction of COBias while concurrently enhancing overall accuracy.

### Strengths
In this paper the authors introduced COBias as a new metric to explicitly quantify the pairwise class accuracy differences that characterize this pervasive LLM issue. By focusing on these pairwise relationships, COBias offers a more nuanced understanding of the accuracy imbalance compared to simply observing disparities in individual class accuracies.

The development of DNIP, a debiasing method based on nonlinear integer programming, represents a creative and innovative solution. Unlike conventional post-hoc correction techniques commonly employed in traditional machine learning, DNIP is specifically tailored to address the unique sources of bias inherent in LLMs, particularly those stemming from in-context learning (ICL) and pre-training data.

The paper shows thorough evaluation. The authors conduct a comprehensive evaluation of DNIP across three different LLMs (GPT-2-XL, Llama-2-7B, and Llama-2-13B), spanning a diverse set of seven NLP tasks, both general and biomedical. This breadth of evaluation demonstrates the generalizability of the proposed approach and its potential applicability across various domains

### Weaknesses
The computational cost of DNIP could pose challenges when dealing with tasks involving a large number of classes or when requiring a very fine-grained weight scale. In such scenarios, the optimization process might become prohibitively time-consuming. The paper does not provide a clear analysis of how the computational time scales with the number of classes or the granularity of the weight scale, making it difficult to assess the practical limitations of the method.

The need for powerful hardware to run DNIP efficiently could limit its accessibility for researchers or practitioners with limited computational resources. The paper mentions that DNIP can be run on CPUs, but it does not specify the required CPU resources (e.g., number of cores, memory) for different problem sizes. This lack of detail makes it difficult to determine the feasibility of using DNIP in resource-constrained environments.

Though the authors demonstrate that DNIP can achieve significant improvements even with relatively small optimization set sizes, which suggests that it might be possible to reduce the computational burden by carefully selecting a subset of training data for the optimization process. They may provide some recipe in selecting those subset of training data. The paper lacks a systematic investigation into the impact of different subset selection strategies on the performance and computational cost of DNIP. Without clear guidelines on how to select the optimization subset, it is difficult to ensure the robustness and efficiency of the method.

While the paper discusses related work on LLM biases, the direct empirical comparison to other debiasing techniques is somewhat limited. A more comprehensive comparison with existing calibration techniques, particularly those designed for ICL, would strengthen the paper's claims. The paper should include a more thorough comparison with a wider range of calibration methods, including those that explicitly address class imbalances, to better contextualize the advantages and disadvantages of DNIP.

**Minor**
The proposed technique is limited to open-source LLMs due to the unavailability of full probability distributions from closed LLMs

### Questions
All the analysis are on 1-shot in-context learning. It would be good if the author can explain why 1-shot in-context leaning is the suitable set up for this problem. They may also consider providing a many-shot (5-shot) analysis, to show whether the proposed method scales well. 

Can you share your thoughts of combining DNIP with other debiasing approaches, such as those focusing on prompt engineering or data augmentation, to achieve even greater reductions in COBias and improvements in accuracy.

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
3

### Summary
The paper addresses the issue of per-class prediction accuracy imbalance in LLMs by introducing the concept of COBias. COBias measures the difference in accuracy between a class and its "odd" class, which holds the majority of wrong predictions for the former. The authors propose a novel method called Debiasing as Nonlinear Integer Programming (DNIP) to adjust per-class probabilities to reduce COBias while maintaining or improving overall accuracy. The paper reports significant reductions in COBias and improvements in accuracy across three different LLMs on seven NLP classification tasks.

### Strengths
1. The research problem is novel and the DNIP method is innovative, leveraging combinatorial optimization to address the debiasing problem directly at the output level.
2. The paper provides extensive experimental results demonstrating the effectiveness of DNIP in reducing COBias and improving accuracy across a variety of LLMs and NLP tasks.

### Weaknesses
1. As the metric COBias is also newly proposed in this paper, I think authors should design more baseline methods to validate the effectiveness of the proposed method DNIP. E.g., adapting other debiasing methods. The current evaluation lacks a strong comparative analysis against existing debiasing techniques, particularly those that aim to improve per-class accuracy, even if they do not explicitly target COBias. The absence of such comparisons makes it difficult to assess the true novelty and practical advantage of DNIP.
2. Clarity needs further improvements, for example, font size for labels in Figure 7 is too small.

### Questions
1. How does the change in β, τ, K parameters affect the performance of DNIP?
2. The performance of DNIP seems to depend heavily on the number and quality of optimization examples. So if there's limited data or noisy labels, what can we do to better utilize DNIP?

### Soundness
3

### Presentation
2

### Contribution
2
