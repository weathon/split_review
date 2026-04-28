# LLM Performance Predictors are good initializers for Architecture Search

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 6

## Abstract
In this work, we utilize Large Language Models (LLMs) for a novel use case: constructing Performance Predictors (PP) that estimate the performance of specific deep neural network architectures on downstream tasks. We create \textit{PP prompts} for LLMs, comprising (i) \textit{role} descriptions, (ii) \textit{instructions} for the LLM, (iii) \textit{hyperparameter} definitions, and (iv) \textit{demonstrations} presenting sample architectures with efficiency metrics and `training from scratch' performance. In machine translation (MT) tasks, GPT-4 with our PP prompts (LLM-PP) achieves a SoTA mean absolute error and a slight degradation in rank correlation coefficient compared to baseline predictors. Additionally, we demonstrate that predictions from LLM-PP can be distilled to a compact regression model (LLM-Distill-PP), which surprisingly retains much of the performance of LLM-PP. This presents a cost-effective alternative for resource-intensive performance estimation. Specifically, for Neural Architecture Search (NAS), we introduce a \textit{Hybrid-Search} algorithm (HS-NAS) employing LLM-Distill-PP for the initial search stages and reverting to the baseline predictor later. HS-NAS performs similarly to SoTA NAS, reducing search hours by approximately 50\%, and in some cases, improving latency, GFLOPs, and model size.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an innovative approach to using Large Language Models (LLMs) for building performance predictors (PP). The authors have designed PP prompts for LLMs and demonstrated that GPT-4, when equipped with these prompts, can predict the performance of architectures with significant accuracy. The paper further introduces a distilled regression model, LLM-Distill-PP, and proposes a hybrid search algorithm for Neural Architecture Search (NAS), demonstrating its efficiency and potential.

### Strengths
- Innovative use of LLMs for the purpose of performance prediction.
- The introduction of LLM-Distill-PP and the Hybrid-Search algorithm significantly reduces the latency in searching for architectures.
- Extensive experiments demonstrate the efficiency of the proposed methods, highlighting their practicality.

### Weaknesses
 - The paper could benefit from a more in-depth exploration of the validation methods used. The explanations in Sections 3 and 4 do not clearly articulate the problem statement and baseline comparisons. Specifically, the paper lacks a detailed discussion on how the training, validation, and test sets were constructed for the performance prediction task. It is unclear how the architectures were sampled, and whether the sampling strategy introduces any bias. Furthermore, the paper does not clearly define the scope of the problem, i.e., what types of architectures are considered, and what range of performance is being predicted. The baseline comparisons are also not well-defined; it is not clear which existing methods are being compared against and why those specific methods were chosen.
- While the concept of distillation is critical, the paper's narrative feels disjointed. The scientific discourse between Chapters 5 and 6 appears fragmented and could be more cohesively presented. The transition from the LLM-based performance predictor to the distilled model is abrupt, lacking a clear rationale for why distillation is necessary and how it addresses the limitations of the LLM-based approach. The paper does not adequately explain the training process of the distilled model, including the choice of the regression model, the loss function, and the optimization algorithm. The connection between the LLM's predictions and the training data for the distilled model is also unclear.
- The figures require refinement; the font aesthetics are lacking, particularly in Figure 2. Algorithm 1 needs redesigning for better readability. The overall structure of the paper could be improved for clarity and flow. Figure 2, for example, is difficult to interpret due to the small font size and lack of clear labels. Algorithm 1, as presented, is hard to follow, making it difficult to understand the exact steps of the proposed hybrid search algorithm. The paper would benefit from a more logical organization of sections, with a clear introduction, problem definition, methodology, experiments, and conclusion.

### Questions
- How does the LLM-Distill-PP model's efficiency and accuracy compare to other existing models?
- Could the authors elaborate on the rationale and design process behind the PP prompts used for LLMs?
- Is the proposed Hybrid-Search algorithm scalable for larger datasets or more complex architectures, and if so, how?

### Soundness
3 good

### Presentation
1 poor

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
The authors design a new algorithm for neural architecture search that uses an LLM subroutine to predict the performance of neural architecture candidates (LLM-PP). They also introduce a modification which trains an MLP on the LLM-based predictions, to estimate architectures even beyond the ones that were predicted by the LLM (LLM-Distill-PP). The authors use an existing NAS framework with their LLM-Distill-PP method to perform NAS, which consists of using their method along with a supernetwork. The authors show several experiments on machine translation benchmarks.

### Strengths
Using LLMs for performance prediction is interesting and fairly novel.

Since LLMs are trained on the whole internet, with an emphasis on code, it is reasonable that an LLM would have an idea on the performance of architectures, especially well-known architectures.

The authors use the LLM-based supernet at the start of training, and then replace with a supernet. This fits the intuition that LLMs are strongest at performance prediction early on, but are no match for computational-based methods after a handful of iterations.

### Weaknesses
Overall, I am concerned that the paper is a bit too narrow in a few parts.

**Comparison to other methods.** The authors use three baselines, all of which are supernetwork-based performance predictors. The authors also make the statement, “The SOTA approach for building performance predictors (f_T ) is to train a weight-sharing supernet model on the task T.” It is highly unclear that this sentence is true. There are many different types of performance predictors, such as zero-cost proxies and learning curve extrapolation, each with different tradeoffs for runtime and accuracy. Furthermore, the performance of weight-sharing methods has been debated (e.g., the papers referenced here https://blog.ml.cmu.edu/2020/07/17/in-defense-of-weight-sharing-for-nas/).

I would have a better opinion of the experimental methodology if the authors compared to performance prediction methods beyond just supernetworks. Here are a few references:
- https://arxiv.org/abs/2008.03064
- https://proceedings.neurips.cc/paper_files/paper/2021/file/2130eb640e0a272898a51da41363542d-Paper.pdf
- https://proceedings.mlr.press/v188/laube22a/laube22a.pdf
- https://arxiv.org/abs/2101.08134

I would especially point out that recently, the extremely simple baseline, "number of parameters" [has been found](https://arxiv.org/abs/2008.03064) to be a surprisingly strong baseline for performance prediction, so this would be great to add as a baseline e.g. in Table 1.

Other than extending the set of baselines, I think the paper could be more impactful in other ways as well. For example, the authors only test their performance predictor on a single NAS framework; the one from HAT. There are other NAS frameworks too, for example, [Bayesian optimization](https://arxiv.org/abs/2110.10423) or BOHB.

Finally, the paper could also be more impactful if it tested search spaces / tasks beyond machine translation. For example, some of the above links use datasets based on computer vision, other NLP tasks, and speech recognition (like [this paper](https://arxiv.org/abs/2101.08134)).

It is surprising that LLM-Distill-PP performs better than LLM-PP. The authors give a few explanations. I think the paper would be stronger if the authors gave more insight and experiments into explaining this observation.

The authors mention that they share their code, but I couldn't find it. Can the authors share their code, e.g. with https://anonymous.4open.science/?

### Questions
If the authors can address some of the points in the weakness section, I would be open to raising my score. Specfiically, comparing to baselines would be important.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper uses GPT4 and few-shot learning with a specially designed prompt to predict model performance, and also employs a regression model trained on the distilled data to save costs (LLM-Distill-PP). Additionally, the paper proposes a hybrid search for NAS based on LLM-Distill-PP.

### Strengths
This paper presents an interesting method to predict model performance on a common model architecture, such as the transformer-base encoder-decoder version, and on a common dataset like WMT'14.

### Weaknesses
The effectiveness of the proposed method largely depends on how much information GPT-4 has "memorized." Since GPT-4 is a language model, its impressive prediction performance on WMT'14 (or WMT'19), transformer-base, translation direction, and BLEU is primarily because **these elements are commonly used for machine translation**. The authors need to recognize the limitations when dealing with less conventional models, datasets, translation directions, metrics, and other tasks and discuss these in the paper. For instance:

- What would occur if training and testing were done on WMT'22 data?
- What if the testing were on a low-resource language, say, Wolof?
- What would be the outcome when examining the results of COMET-22, or the recently released [COMET-kiwi-10B](https://huggingface.co/Unbabel/wmt23-cometkiwi-da-xxl) model, which GPT-4 lacks knowledge about?
- What if the chosen model were the [CNN-based embedding](https://arxiv.org/pdf/2305.14280.pdf) for machine translation, where GPT-4 has limited familiarity?

It's very likely that GPT has already encountered the architecture selection and results for your model, data, and metric settings since they have been prevalent in recent years. It is very possible that the author is **testing the model that it had been trained on the test dataset**. However, the author didn't explicitly address the performance in less conventional settings in the paper, rendering the study meaningless.

### Questions
Please see weaknesses above.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the use of Large Language Models (LLMs) to build Performance Predictors (PP) for deep neural network architectures. These PP models aim to predict the performance of a given architecture on downstream tasks. The authors design PP prompts for LLMs, providing them with the role, instructions, architecture-specific hyperparameters, and demonstrations to guide the performance prediction process.

### Strengths
1. Applied LLM to Performance Prediction: The paper successfully applies Large Language Models (LLMs) to performance prediction for deep neural network architectures. This innovative use of LLMs for performance estimation can potentially benefit a wide range of applications in the field of deep learning.

2. Distillation Technology for Cost Reduction: The paper introduces a valuable approach to reduce the cost of using LLMs for performance prediction. The distillation process allows the transfer of knowledge from the LLM-PP models to smaller, more efficient regression models, making it a cost-effective alternative for performance estimation.

3. Hybrid Search Algorithm Accelerates Search Time: The Hybrid-Search algorithm (HS-NAS) presented in the paper demonstrates significant advantages in accelerating search time for Neural Architecture Search (NAS). It reduces search hours by approximately 50% and offers potential improvements in latency, GFLOPs, and model size. This can be a substantial advantage for practitioners looking to optimize their deep learning models.

4. Good Ablation Experiments: The paper conducts thorough ablation experiments to assess the effectiveness of their methods. This provides a clear understanding of the impact of different components and helps validate the proposed techniques.

### Weaknesses
1. Insufficient Innovation in Hybrid Search Algorithm: One potential drawback is the perceived lack of significant innovation in the Hybrid-Search algorithm. While it effectively accelerates search time, it may not introduce groundbreaking advancements in the field of NAS. The combination of LLM and supernet predictors, while practical, does not represent a fundamental shift in search methodologies. More innovative aspects of the algorithm, such as adaptive sampling strategies or dynamic weight adjustments based on the LLM's uncertainty, could enhance its contribution.

2. Fixed Downstream Tasks, Unknown Effects on Other Tasks: The paper primarily focuses on performance prediction for specific machine translation downstream tasks. However, it does not explore the potential impact or applicability of LLM-PP or LLM-Distill-PP models on a broader range of tasks, such as image classification, object detection, or other NLP tasks like sentiment analysis or question answering. This lack of generalizability limits the scope of the approach and its potential in different contexts. The performance of LLM-based predictors might be highly task-dependent, and the current evaluation does not address this concern. The absence of experiments on established NAS benchmarks, such as NAS-Bench-101 or NAS-Bench-201, further restricts the understanding of the approach's versatility.

### Questions
- Is the prediction result provided by LLM repeatable? How is it handled if the results given each time are different?
- The article mentioned that LLM  exhibits a "general understanding" of the DNN architectures.But how do you ensure that LLM understands the DNN framework rather than "reading memory" from its training data to provide prediction results?
- Since the final search should use the model distilled from LLM-PP instead of LLM-PP itself, why not use a PP that performs better than LLM-PP for distillation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
