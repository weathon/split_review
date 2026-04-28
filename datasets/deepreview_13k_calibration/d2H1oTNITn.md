# Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6

## Abstract
Large language models (LLMs) exhibit hallucinations (i.e., unfaithful or nonsensical information) when serving as AI assistants in various domains. Since hallucinations always come with truthful content in the LLM responses, previous factuality alignment methods that conduct response-level preference learning inevitably introduced noises during training. Therefore, this paper proposes a fine-grained factuality alignment method based on Direct Preference Optimization (DPO), called Mask-DPO.  Incorporating sentence-level factuality as mask signals, Mask-DPO only learns from factually correct sentences in the preferred samples and prevents the penalty on factual contents in the not preferred samples, which resolves the ambiguity in the preference learning. Extensive experimental results demonstrate that Mask-DPO can significantly improve the factuality of LLMs responses to questions from both in-domain and out-of-domain datasets, although these questions and their corresponding topics are unseen during training. Only trained on the ANAH train set, the score of Llama3.1-8B-Instruct on the ANAH test set is improved from 49.19% to 77.53%, even surpassing the score of Llama3.1-70B-Instruct (53.44%), while its FactScore on the out-of-domain Biography dataset is also improved from 30.29% to 39.39%. We further study the generalization property of Mask-DPO using different training sample scaling strategies and find that scaling the number of topics in the dataset is more effective than the number of questions. We provide a hypothesis of what factual alignment is doing with LLMs, on the implication of this phenomenon, and conduct proof-of-concept experiments to verify it. We hope the method and the findings pave the way for future research on scaling factuality alignment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors introduce an alignment method to improve factuality in LM responses.
The method, based on DPO, leverages factuality annotations at the sentence level to avoid optimizing non-factual sentences in chosen responses and to avoid penalizing factually correct sentences in rejected responses during preference optimization.
Experiments in and out of domain demonstrate the effectiveness of the strategy on improving response factuality.
Most intriguing, the authors provide a hypothesis, accompanied with preliminary experiments, about how factuality alignment influence topic representation and the generalization capabilities of an LM.

### Strengths
S1. The proposed method is well presented and supported mathematically.

### Weaknesses
W1. Even though the experimental setup includes a wide range of model families, it does not include transparent SFT+PO (instruction tuning + preference optimization) training setups, training PO directly over instruct models. Previous work in PO encourages starting from a base model (not instruction-tuned), perform SFT over chosen responses, and then perform PO. Such setup provides high transparency on the training procedure of a final chat / PO model. For reference, please refer to the DPO paper.

W2. There is a lack of comparison against relevant, recent PO strategies. Similar work that implement some form of masking or granularity below response are: TDPO, DPOP, SePO, to name a few.

W3. Whilst the paper presents extensive results on factuality metrics, a more comprehensive evaluation on standard benchmarks is needed. In this way, we could appreciate the effect of factuality alignment over other LLM capabilities, e.g. mathematical reasoning or harmful generation.

### Questions
## Appendix A
-	Regarding the inference setup, temperature=0.8, was hyper-parameter tuning performed? Ideally, it would be helpful to show how performance varies across temperature values (e.g. 0, 0.25, 0.5, 0.75, 1.0), as it is done in PO literature.

## Granularity of Annotation
In the paper, annotation is gathered at the sentence level. Would it be possible to apply this same annotation procedure to more fine-grained syntactic units? For instance, clauses, noun phrases, verb phrases. Do you have an intuition as to how impactful such a setup would be?

## Reporting results
-	Was a statistical significance test performed on the reported metric results?
-	I am not familiar with ANAH and FactScore metrics, would it be safe to assume they follow a gaussian distribution? If not, it is important to consider that, in cases where the metric score distribution cannot be considered gaussian, it is better to report results over bootstrap resampling of the metric scores. Please refer to EleutherAI’s Evaluation Harness (lm-eval), a popular evaluation library for LLMs, for details.

[4] https://github.com/EleutherAI/lm-evaluation-harness

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
4

### Summary
This paper proposes a novel fine-grained factuality alignment method called Mask-DPO to mitigate hallucinations in large language models (LLMs). Mask-DPO incorporates sentence-level factuality information as a mask signal to guide the preference learning, avoiding the reward for incorrect sentences in preferred samples and the penalty for factual sentences in non-preferred samples. Experiments demonstrate that Mask-DPO significantly improves the factuality of LLM responses on both in-domain and out-of-domain datasets, even when the test questions and topics are unseen during training. The authors also study the generalization property of Mask-DPO and find that scaling the number of topics in the training data is more effective than scaling the number of questions. They hypothesize an internal knowledge graph learned by LLMs and provide proof-of-concept experiments to verify it.

### Strengths
1. Mask-DPO addresses a critical issue of hallucination in LLMs, which hinders their practical applications in various domains. The proposed method provides a more effective solution compared to existing response-level preference learning approaches by leveraging fine-grained sentence-level factuality signals.

2. The paper provides valuable insights into the generalization property of Mask-DPO by studying different training data scaling strategies. The finding that scaling the number of topics is more effective than scaling the number of questions sheds light on how to efficiently construct training data for factuality alignment.

3. The hypothesis of an internal knowledge graph learned by LLMs during pre-training is intriguing and opens up new research directions. The authors provide proof-of-concept experiments to support this hypothesis, such as ablating different topic sampling strategies and comparing the factuality of best-of-N responses before and after alignment.

### Weaknesses
1. While the paper compares Mask-DPO with DPO, it would be beneficial to include a more comprehensive comparison with other state-of-the-art factuality alignment methods. Specifically, a comparison with methods that focus on different aspects of factuality, such as knowledge retrieval or verification, would help to better position Mask-DPO in the context of existing approaches and highlight its unique advantages. The current comparison only focuses on DPO, which is a general preference learning method, and does not sufficiently address the specific challenges of factuality alignment.

2. The hypothesis of the internal knowledge graph learned by LLMs is intriguing but lacks sufficient theoretical justification and empirical evidence. The authors could provide a more rigorous theoretical analysis of how the knowledge graph is formed during pre-training, perhaps by linking it to known mechanisms of representation learning in neural networks. Furthermore, the empirical evidence could be strengthened by visualizing the graph structure or quantitatively measuring the affinity between nodes using metrics beyond simple distance measures, such as graph-based metrics that capture the connectivity and structure of the graph. The current evidence is limited to ablation studies and best-of-N comparisons, which do not directly validate the existence of an internal knowledge graph.

3. The paper would benefit from a more thorough proofreading to fix minor typos and grammatical errors (e.g., "anachronistic sentences" in Figure 2 caption, "preferece" in line 169 of Section 2.1).

### Questions
Section 3.1: It would be helpful to provide more details on the specific subset of the Biography dataset used for out-of-domain evaluation, such as the criteria for selecting the questions and the diversity of the topics covered.

Section 3.2: The authors could consider adding a case study or qualitative analysis of the generated responses before and after applying Mask-DPO. This would give readers a more intuitive understanding of how Mask-DPO improves factuality at the sentence level.

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
4

### Summary
It proposes Mask-DPO, a fine-grained factuality alignment method, which performs a sentence-level masking to denoise inaccurate training signals inherent from noisy sentences by utilizing external factuality evaluator. Conducting experiments with various base models, Mask-DPO outperforms vanilla-DPO and a existing factuality alignment method (FactTune) in both in-domain and out-of-domain datasets. Furthermore, it explores the generalization property of the method, which hypothesizes two corollaries to prove the characteristics of factuality alignment achieved by MASK-DPO.

### Strengths
**Reasonable Analysis of Factuality Alignment Through Data Scaling**

The study provides a well-founded hypothesis on the effects of factuality alignment by comparing outcomes based on the number of topics and questions. The subsequent proof-of-concept experiments offer a valid approach to support this hypothesis.

**Novelty of provided Methods"

The authors provide a novel mask-DPO method which hinders to learn unfactual text fragments lied in each sentence.

### Weaknesses
 **Potential for Errors Due to Sentence-Level Annotation**

The paper ranks responses through sentence-level evaluation, but this method may not always accurately reflect factuality. Depending on the type of sentence or factual argument, sentence-level evaluation may misalign with actual factual accuracy. For instance, consider two responses conveying the same information:
        - Response 1: Consists of 10 short sentences.
        - Response 2: Consists of 3 long sentences.
If hallucination occurs in only one part of each response, the annotation scores could vary significantly (e.g., 9/10 vs. 1/3). Factors such as sentence segmentation and fact placement can impact response ratings, introducing potential errors in sentence-level evaluation. This is particularly concerning when the factual content is densely packed within a few sentences, as the method might penalize longer, more comprehensive responses unfairly if they contain a single hallucination.

**concerns about overall quality of the responses**

When it comes to response coherence, it raises concerns that the quality of the response may be compromised when certain sentences are masked. While masking can improve factual accuracy by filtering out incorrect signals from sampled responses, it risks disrupting the overall coherence and completeness of the response, as preference learning is based on responses where specific sentences have been removed partway through. Therefore, it may potentially leads to unexpected or lower-quality outputs even if they are factually correct. I understand that the primary focus of the paper is on the factuality of model responses, yet factuality itself aims to enhance overall response quality in LLMs.  Given this, I wonder if there is any evaluation or consideration of how the sentence removal approach in Mask-DPO's preference data construction might negatively impact response quality. The masking process could lead to a model that prioritizes fragmented, factually isolated sentences over coherent, well-structured responses, potentially undermining the overall utility of the generated text.

**insufficient details**

1) Ranking and Pairwise selection process
2) Prompts
3) Section 4.3: Proof of concept
    - embedding details
    - clustering topic vectors
    - choosing the far group and the near group

### Questions
[missing references] Long-form factuality generation in related work

1) Long-form Factuality in Large Language Models (Wei et al., 2024)
2) OLAPH: Improving Factuality in Biomedical Long-form Question Answering (Jeong et al., 2024)

[Sampling strategy] In line 344, it is quite hard to understand the first sentence that explains about the non-policy model effectiveness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a method for training models via preference optimization in order to produce more factually correct responses and as a result mitigate halluciantions. This is achieved by (1) creating preference data where chosen responses are more factually correct than dispreferred ones and (2) by masking parts of each response if they contain inacccurate information. 
To realise the above, the authors use an external sentence-level factual evaluator to measure the correctness of each sentence inside each response and consider the ratio of correct sentences as the preference score. Then, a binary mask is employed into the DPO loss thus increasing the probability of correct facts and decreasing the probability of incorrect facts.

Results on in- and out-of-domain datasets suggest that the resulting models show significantly better performance across two different evaluators.
In addition, the authors hypothesize that such an alignment impacts the internal knowledge of LLMs, which they showcase via clustering responses on specific topics and best-of-N responses. Topics close to each other have better factuality.

### Strengths
- The authors propose a simple and straighforward method to improve models to produce more factually correct responses
- Results on the evaluated benchmarks indicate significant improvements
- Proof of concept experiments are designed to explain the performance of the models and the effect that factual alignment has in their internals

### Weaknesses
 - One could argue that even in a single sentence, there can be factually incorrect information. For example, if the sentence is long enough, different clauses can contain conflicting information. How would you be able to mitigate this without completely ignoring the entire sentence?
- The method looks general enough, however it is targeted on factuality alone. Do you think if you replaced factual checking with cohesiveness / fluency / some other metric that is easy to obtain, models could also improve towards that direction too?

### Questions
Questions:
- Line 262: You mention that the models are post-trained versions, what do you mean by that? That the models are instruction tuned?
- I am kinda missing the point of the ablation in Table 3. Do you aim to show that the quality of responses depends on the underlying model used to generate them? In this setting, the data are generated by model X but LLaMA is trained with Mask-DPO? I think it is already proved that the model needs to be in-distribution for DPO to work (original DPO paper) - which explains why llama3 works best in this case too?

Comments:
- Line 219: inaccuracies facts -> incaccurate facts
- Line 283: un-preferred -> dispreferred (in other places as well)
- Line 323: rewarding hackers -> reward hacking
- Table 4: what does the +X refer to? which is the baseline score?
- I feel the name "Mask-DPO" is quite misleading as it is very generic and it is not directly associated with factuality.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a fine-grained factuality tuning method, referred to as Mask-DPO, designed to incorporate sentence-level factuality. Extensive experiments demonstrate the effectiveness on both in-domain and out-of-domain datasets. It also provides an analysis from two dimensions: the number of different topics and the diversity of the questions.

### Strengths
1.The approach of filtering out false sentences within preference pairs is particularly intriguing, as it helps refine the dataset by ensuring that only factual information is prioritized.

2.The paper establishes well-founded hypotheses regarding the functionality of the factual alignment process and conducts experiments to validate these assumptions.

### Weaknesses
1.Mask-DPO operates at the sentence-level granularity, employing a sentence-level hallucination annotator to mask undesired sentences within training preference pairs. However, it's worth noting that many responses mix true and false information in a single sentence. I'm curious how Mask-DPO handles these cases since pulling apart accurate details from inaccuracies can be tricky. Clarifying this might help us see how well the model deals with more complex responses.

2.The experiments seem focused on long-form generation, which raises the question of how the model would perform on shorter, QA-style tasks.

3.The proof of Corollary 2 in Section 4.3 is less convincing. How did you arrive at this knowledge structure corollary based on the hypothesis you mentioned earlier? Specifically, if the model-specific graph were focused on questions rather than topics, would we still arrive at the same conclusions? Please clarify this.

### Questions
Please see weakness.

Additionally, in Table 5, it’s intriguing that using embeddings from other models seems to make the differences less distinct. Why alternative embeddings are used instead of relying solely on those from the policy model itself?

I would like to increase my score if my concerns are addressed properly.

### Soundness
2

### Presentation
3

### Contribution
2
