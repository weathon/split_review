# 3DS: Decomposed Difficulty Data Selection’s Case Study on LLM Medical Domain Adaptation

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Large Language Models (LLMs) excel in general tasks but struggle in specialized domains like healthcare due to limited domain-specific knowledge. Supervised Fine-Tuning (SFT) data construction for domain adaptation often relies on heuristic methods, such as GPT-4 annotation or manual data selection, with a data-centric focus on presumed diverse, high-quality datasets. However, these methods overlook the model’s inherent knowledge distribution, introducing noise, redundancy, and irrelevant data, leading to a mismatch between the selected data and the model’s learning task, resulting in suboptimal performance. To address this, we propose a two-stage \textit{model-centric} data selection framework, \textbf{Decomposed Difficulty Data Selection (3DS)}, which aligns data with the model’s knowledge distribution for optimized adaptation. In \textbf{Stage 1}, we apply Prompt-Driven Data Selection via Explicit Alignment, where the model filters irrelevant or redundant data based on its internal knowledge. In \textbf{Stage 2}, we perform Decomposed Difficulty Data Selection, where data selection is guided by our defined difficulty decomposition, using three metrics: \textit{Instruction Understanding}, \textit{Response Confidence}, and \textit{Response Correctness}. Additionally, an \textit{attention-based importance weighting mechanism} captures token importance for more accurate difficulty calibration. This two-stage approach ensures the selected data is not only aligned with the model's knowledge and preferences but also appropriately challenging for the model to learn, leading to more effective and targeted domain adaptation. In the case study of the medical domain, our extensive experiments on real-world healthcare datasets demonstrate the superiority of \M~over existing methods in accuracy by over 5.29\%. Our dataset and code will be open-sourced at \url{https://anonymous.4open.science/r/3DS-E67F}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors introduce a method to address limitations of domain adaptation in LLMs within the medical domain. The method is termed 3DS: Decomposed Difficulty Data Selection. 3DS introduces a better focus on data selection that aligns with the target model’s current knowledge distribution (limiting knowledge gaps), as well as a way to avoid overfitting and allow for increases in difficulty by evolving the data selection to address the changing model.

3DS is divided into two distinct stages 1) Prompt-Driven Data Selection using the target model to select high quality data and 2) Decomposed Difficulty Data Selection to select data of reasonable difficulty to facilitate efficient domain adaption. Difficulty is assessed through three measures: i) Instruction Understanding Difficulty (comprehension assessment using a perplexity score); ii) Response Confidence Difficulty (measured by the model’s conditional perplexity when generating a response given an instruction) and iii) Response Correctness Difficulty (measured by perplexity as well). Additionally, an attention-based importance weighting mechanism is used for ii) and ii) which helps clarify uncertainty in the model further, by adjusting perplexity-based measurements by weighting token according to their semantic importance 

3DS outperforms existing methods, which use proprietary LLMs and/or reward models, demonstrating improvements in domain ability (accuracy) by outperforming baselines, as well as claiming improved scalability and generalisability.

### Strengths
**Originality:**

- Attempts to build on previous work by swapping out a proprietary LLM with the target model to identify data necessary for alignment

- Motivation for, and the subsequent inclusion of a different metric (attention-based importance weighting mechanism), beyond the commonly used perplexity is supported by evidence from the literature, and in the positive results

**Quality:**
- The approach to the problem of data filtering for (medical) domain adaptation in LLMs is motivated well, and the methods presented in the paper build on previous work and address the limitations indicated in related work (e.g. avoid overfitting, and address increasing data complexity as the model’s knowledge evolves during adaptation)
- The chosen evaluation metrics: perplexity and attention-based and attention-based importance weighting mechanisms, are appropriate for the problem, with the latter addressing some limitations of perplexity which may lead to less important tokens (e.g. prepositions) skewing uncertainty estimates.
- These metrics are used to assess the method's performance against multiple baselines, almost all showing a positive improvement
- Please see the questions for a note on considering an additional metric for assessing excluded out-of-distribution data

**Clarity:**
- The paper generally reads well and is well structured making the background motivations, as well as the methods and results easy to follow. 
- Please see comments and suggestions for minor suggestions on improving accessibility

**Significance:**
- Medical domain applications have the potential for significant impact and, despite some concerns about the dataset (see weaknesses), if the dataset is released responsibly, the 1.9 million instances can also have broader applicability and support further research in this domain
- The positive improvement on the baselines is a strong motivator for the beneficial utility of the proposed methods.

### Weaknesses
1. Lack of reflection on limitations
- The authors do not engage at all with the potential limitations of their own approach, and how these might be contrasted with “other” methods that use proprietary LLMs. It is my belief that both these approaches are subject to some sort of inherent bias due to bias amplification. Bias amplification would be when one mode that is used in a machine learning pipeline has its own biases being amplified within the downstream task [1]. Specifically, the use of the target model itself for data selection, while innovative, could lead to a self-reinforcing loop where the model's existing biases are further entrenched through the selection of data that aligns with its current, potentially flawed, understanding. This could manifest as an over-representation of certain types of medical cases or a skewed interpretation of medical instructions, ultimately limiting the model's ability to generalize to a broader range of scenarios. This is particularly concerning given the high-stakes nature of medical applications, where fairness and accuracy across diverse patient populations are paramount.
- More broadly, data filtering is also subject to bias issues, as demonstrated by Hong et al., with CLIP [2]. Without acknowledging these potential limitations, it is very difficult to assess this method’s ability to mitigate these potential, but known effects 

2. Dataset curation:
- The authors have not included a Datasheet for Datasets [3] in the appendix. The code and data have not been released: https://anonymous.4open.science/r/3DS-E67F/README.md. The omission of this documentation makes making it even more difficult to assess the following points:

   - The authors claim the data come from open sourced sites, but do not expand on whether the individual terms of services for these sites explicitly allow for this data to be used for machine learning (as one example of a potential terms of service violation)
   - Despite being crawled data, the sensitive nature of the data, particularly the Q&A data crawled from the doctor-patient exchanges, raises ethical concerns [4].

### Questions
**Primary questions and suggestions:**
- Was there an ethics review process involved in the development of this dataset? This seems pertinent given the sensitive nature of the data?
- A Datasheet for Datasets [1] can improve transparency around the dataset and highlight considerations for the user, such as how it was curated and expected use cases. 
- A deeper consideration of the limitations of this method, particularly with regards to societal impact and potential biases that might arise (e.g. bias amplification through , would strengthen motivations for using this method, as well as inspire future research to address these concerns.
- Have the authors considered the potential limitation of excluding out-of-distribution data that may still be useful downstream? The current metrics treat this out-of-distribution data as ‘noise’, but including an additional evaluation step, such as human-in-the-loop evaluation of the subset data to be excluded could ensure relevant data is still included.

**Minor suggestion for readability:**
- The baselines section is a little difficult to follow without clarification of the baselines used. I believe readability will be improved by introducing the acronyms in more detail there. Equally, the Appendix can be made more accessible by including the citations for the baselines there as well

**References:**

[1] Gebru *et al.*, 2021. Datasheets for Datasets: https://arxiv.org/abs/1803.09010

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a method to select a subset of the fine-tuning data to fine-tune a language model. Their method is tested on healthcare language data setting where the specificity of the prompts requires models to be fine-tuned in order for the model to perform well. The objective of the data selection algorithm is to find examples which have little noise, are informative, and not too difficult for the model. The authors suggest a two stage algorithm for selection of the samples. The first consists of prompting a language model for useful points and the second looking at the perplexity of prompts, responses and predictions. They fine-tune the model using fine-tuning data that they curated, containing mixtures of different healthcare language data that is composed of 19 million samples. The authors show that their method is the only method that consistently outperforms random acquisition of fine-tuning points.

### Strengths
The paper shows that their method clearly outperforms against the benchmarks they tested against. The paper is clearly written, easy to understand, and structured well. The ablation studies related to the size of the model and its ability learn from more difficult points backed up their hypothesis that some points are too difficult for some models to learn, which is one of the motivations for the design of the algorithm.

### Weaknesses
## References
Given that selecting fine-tuning points is very relevant to the field of active learning, I was surprised to see zero references to the field unless I missed them, especially since the techniques used in this algorithm are very similar to active learning. Hence the score for presentation, since the work was not contextualised well within prior work. Active learning also deals with quantification of uncertainty of points, much like this paper does using perplexity of models, which I believe is analogous to the uncertainty of a model. There have also been many papers in the field of active learning relating to the topic of finding informative, noise-free and learnable points.
See for example:
Mind Your Outliers! Investigating the Negative Impact of Outliers on Active Learning for Visual Question Answering. Sören Mindermann et al.
Prioritized Training on Points that are Learnable Worth Learning, and Not Yet Learnt. Siddharth Karamcheti et al

There were no references to the metrics BLEU1,4 and Rouge. Even if they are traditional metrics, it would be good to provide a reference for those who are unfamiliar with them. Especially since it is used in one of the two tables that present the main results.

## Further examination of the algorithm
If this paper consisted of just of looking at perplexity of various aspects of the model's perplexity (step 2), then this paper would lack novelty, since this would basically be the same as a standard uncertainty based active learning acquisition method. However, the acquisition algorithm has an additional step (step 1) that directly queries the language model to respond to a set of evaluation criteria designed to rule out low quality examples. This makes the algorithm different from existing active learning methods.
There are some ablation studies in the table showing the removal of different parts of step 2 of the algorithm (D1 to D3). However, there are no ablations for removing completely step 1 or 2 of the algorithm. I would be curious to see what effect of removing completely the step 1 of the algorithm and the effect of removing step 2. I wonder which part of the algorithm is doing the biggest leg work. Couldn't we also prompt the model to ask about its uncertainty of the prompt ? essentially collapsing step 2 of the process in to a few additional prompts in to step 1 of the process.
I would be happy to increase my 'contribution' score and the 'overall' score to 8 if this ablation is added that convinces me that both steps are necessary in the algorithm. i.e. can we get similar results but removing step 1 completely? Can we get similar results by removing step 2 but prompting the model to acquire the uncertainty of prompts and using that as an additional scoring mechanism to score points, removing the need to compute the perplexity of queries. This would add more to the general understanding of what steps are useful when selecting fine-tuning points, which would be a very useful contribution to the field. A confirmation that prompting as well as inspection of perplexity are both integral to the algorithm’s success will be very informative.  

## Fairness considerations
Finally, since this paper relates to the healthcare domain where fairness and bias are more important than in other domains, it would be worth mentioning somewhere in the paper the effect that data-selection can have on the fairness of a model and some references to the appropriate literature. Since the paper already has a section on limitations, perhaps the authors could mention that the implications on safety of this method has not been examined and it is left for future work. Some examples of the effects of fine-tuning on models can be found here as a baseline:
The Trade-off between Performance, Efficiency, and Fairness in Adapter Modules for Text Classification. Minh Duc Bui

### Questions
How would a practitioner choose the appropriate percentage range of difficulty of prompts for a particular model? How do we know that the model being used is sufficiently large that we can put a higher upper bound for the difficulty scores for the points which will be acquired?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a model-centric approach for data selection, which can be used for supervised fine tuning of LLMs. The authors identify a gap in the existing data selection strategies, which can lead to suboptimal model performance and propose 3DS, a strategy that uses the model’s inherent knowledge during data selection, while also accounting for 3 kinds of data difficulty – related to instruction understanding, response confidence and correctness. The paper identifies a way to tackle a known problem, related to data selection in supervised fine tuning of LLMs.

### Strengths
•	Significance: The authors have proposed a solution for a known problem in supervised fine tuning, specific to the medical domain.

•	Clarity: The paper is quite well written and relatively easy to follow along. Clarifications needed in the draft are mentioned in the Questions section of the review.

•	Quality: The authors have evaluated their framework on 3 different datasets.

•	Originality: The use of attention based weighting is an interesting approach to tackle the relative semantic importance of tokens.

•	Others: The limitations have also been acknowledged.

### Weaknesses
•	The authors have provided a link for the code and data, but it is not yet available publicly. Making the data available publicly would be greatly beneficial to the community.

•	Since the authors propose the 3DS data selection framework as an alternate to GPT-4 annotation based or manual data selection based strategies, it would be good to include a comparison with these techniques in the experiments. Specifically, a cost-benefit analysis comparing the proposed method with the cost of using GPT-4 for data annotation would be valuable.

•	Since the focus is on medical domain and LLMs, there needs to be a comparison against LLMs developed / tuned for the medical domain, like MedPALM[1], MediTron[2] etc. The lack of comparison with these models makes it difficult to assess the true impact of the proposed method in the medical domain. Furthermore, it is unclear if the performance gains are due to the proposed data selection strategy or the inherent capabilities of the base LLMs used.


### Questions
•	The authors mention “the model’s inherent knowledge distribution” in the introduction (Line 056, 057) – it would be good to clarify if they are referring to distribution with respect to labels, or tasks being considered.

•	How do the authors ensure that the data selected by 3DS indeed follows the “model’s inherent knowledge distribution”? 

•	What is the intuition behind having less diverse data in the data selected (this is mentioned as an issue of prior data selection strategies)? (Line 055) Does the addition of data similar to the inherent knowledge distribution end up reinforcing what the model already knows?

•	In Stage I, the target model is used to provide a data quality score (detailed in Appendix A). However it is a bit unclear if the overall score is a combination of the 5 dimensions listed in Appendix A. Please provide a reference for why the 5 dimensions listed in the Appendix are good indicators of data quality.

•	Lines 198-206: The authors identify 3 components from general problem solving – it would be good to add a reference/citation for why these 3 aspects are crucial and the basis of consideration in this paper.

•	In Equation 5, how is the aggregate function defined? 

•	Lines 278-283: how does the selection ensure non-redundant data (already known to the model) is not captured? Please include details of k-centre sampling for better readability.

•	In Algorithm 1, were there any situations when $S_{mid}$ was an empty set? Was this also a consideration in choosing $\tau^{low}$ and $\tau^{high}$?

•	It would be good to have an experiment showing sensitivity to training data budget (currently set to 5K, line 351).

•	In Table 3, kindly clarify the metric used for comparison.

•	Please include details (maybe in the Appendix) on selection of hyperparameters, steps taken to ensure reproducibility of results.

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
This work proposes an approach to selecting data likely to lead to effective adaptation of an LLM to a new domain. The approach proceeds in the two steps, with the first step using a prompt-based filter for data quality and the second step using a collection of entropy-based metrics that essentially assess the likelihood of the instruction, generated response and reference response under the model. They also offer an attention-weighting approach that weights tokens in the calculation based on their semantic importance, with the attention weights extracted directly from the attention layer of the transformer. Data are further filtered such that each of the entropy metrics fall into a pre-specified moderate range. A further contribution of the work is a new curated dataset of Chinese medical questions, to be released as a part of this work. In the experiments, they compare supervised tuning using all of this data with approaches that select subsets using the proposed approach and baselines. They find that the proposed approach improves performance.

### Strengths
* The approach does appear to be effective empirically, in that it leads to improvements in performance over baselines. Notably, they show that the method actually improves substantially over fine-tuning on all of the available fine-tuning data.
* The dataset contribution is significant and has potential for broad use.

### Weaknesses
 * Regarding presentation, I generally found the description of the problem and the motivation for the proposed approach to be technically imprecise, with several of the core concepts not clearly defined or motivated. Overall, the work provides a reasonable heuristic and intuitive presentation of the problem and motivation that feels a bit “hand-wavy”, without clear theoretical grounding. This makes it difficult to address the soundness of the approach, regardless of whether it is empirically effective.
* The terminology used is technically imprecise. I have included some examples below:
  * It is not clear how a “model’s inherent knowledge distribution” or the “inherent preferences” are defined, nor what it means to align to it, nor why this might be relevant for identifying data for supervised fine-tuning.
  * Related to the above, the concept of “data difficulty” is not clearly defined. Furthermore, the work does not make a compelling case to motivate regarding why data difficulty is the key quantity to control for data selection. Ideally, there would be some clear technical justification for why a predefined middle range of the difficulty metrics is a good heuristic for selecting samples that would lead to effective supervised fine-tuning.
  * Some other examples of unclear terminology: “preference gaps” (lines 117-118), “learning requirements” (line 119), “target model” (line 161, 184, and elsewhere).
Misuse of terminology: The use of the term “domain adaptation” is not correct in this work. Domain adaptation has a specific technical meaning in machine learning that refers to adapting a classifier to a related domain without labeled data in that target domain (see Ben-David 2010 for example; https://dl.acm.org/doi/abs/10.1007/s10994-009-5152-4 ).

### Questions
* The work would be improved if the issues regarding the presentation raised in the weaknesses could be addressed.
* It would be helpful to elaborate on “k-center sampling based on instruction embeddings” (line 281-283).
* Threshold selection: “We determine the difficulty thresholds through experiments” (Line 355). Do you use a separate held-out validation set to select these thresholds, or are they selected on the test data? If they are selected on the test data, this would make me skeptical of the generalizability of the results.
* Given that the dataset contribution is a key contribution of the work, further details regarding the curation process and of the data itself would improve the work (in addition to what is currently included in Appendix B). 
* RE: Instruction Understanding Difficulty: “A higher perplexity value indicates greater difficulty for the model to comprehend the instruction” (Line 221). Is this true? To my understanding, this is just a measure of the likelihood of the model of generating the instruction text. It is not clear whether this is actually a reasonable measure of whether the LLM comprehends the instruction.

### Soundness
3

### Presentation
2

### Contribution
3
