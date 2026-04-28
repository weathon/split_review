# Initializing and Retrofitting Key-Value Adaptors for Traceable Model Editing

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
As the insight of knowledge storage in language models deepens, the ability to perform CRUD (Create, Read, Update, Delete) operations on language models becomes increasingly indispensable for satisfying the demands of managing rapidly updating knowledge. Considering the high cost of fine-tuning language models, model editing methods with low cost are usually required to manipulate models’ knowledge. Evident suggests that modules carrying knowledge in a Transformer module are primarily the MLP blocks, thus we propose iReVa, a method that explicitly initializes and retrofits key-value pairs into MLP blocks to construct a new mapping of a piece of knowledge without damaging the irrelevant knowledge. In comparison to existing methods, iReVa reveals better interpretability and a stronger capacity for carrying traceable edits. Experiment results on a series of GPT series models show our prominent performance on edit success and generalization without influencing specificity. We also made the first attempt to conduct a knowledge withdrawal test of iReVa. Our codes are available on this website.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an approach to editing knowledge in large language models called iReVa. The authors focus on the MLP blocks within Transformer modules, which they follow previous work and cast them as key knowledge carriers. Their method, iReVa, aims to insert new information into these blocks without disrupting existing knowledge. iReVa explicitly initializes and retrofits key-value pairs into MLP blocks to construct a new mapping of a piece of knowledge, aiming not damaging the irrelevant knowledge. The authors apply their approach on GPT-2, GPT-NEO and GPT-J models on two benchmark datasets, showing its potential in knowledge editing and maintaining the model's overall performance.

### Strengths
* The idea of iReVa is quite intuitive and straightforward. Un-edited data should keep their hidden states unchanged after knowledge editing, while edited data should have activation activated as expected.

* The results on two knowledge editing benchmark seem quite impressive, and especially the analysis of Figure 2, which compare baseline results of edits in various layers on zsRE dataset.

* The writing and idea are well presented. Figure 1 provides a very good and clear overview of iReVa.

### Weaknesses
 * Although the authors run evaluations on three language models, namely GPT-2, GPT-NEO and GPT-J, these base models are not state-of-the-art any more. In addition, the evaluations are mainly for base models, where in real applications, practitioners may want to update their knowledge after fine-tuning with real world defeats feedbacks. Therefore, it will be interesting to see more results of LLaMA 3.1 models and their chat versions, as well.

* The knowledge editing tasks are somewhat too simple and target output seems quite short. Knowledge is a complex concept and a natural language sentence can include dense knowledge. For these two benchmarks used in this paper, their input prompts seem quite short. It is unclear that how this method is applicable in real world applications. For example, a new medical paper may have some new findings in their paper and how to use this paper' method inject these new knowledge into a medical language model?

* The generalization task evaluation is also not comprehensive. Although NQ dataset covers different types of knowledge, their scope is quite limited. It will be interesting to evaluate models on MMLU or MMLU-Pro benchmark data, which is much diverse and comprehensive than NQ dataset used in this paper.

* The multi-task object during knowledge editing involve multiple hyper-parameters for task balancing during training, which will introduce the complexity of tuning for specific domain and tasks.

### Questions
See comments in the Weaknesses.

### Soundness
2

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
3

### Summary
To address the high costs of fine-tuning in Knowledge Editing, it proposes a method called iReVa, which initializes and retrofits key-value pairs within MLP modules to construct new mappings of knowledge without affecting irrelevant information. Experiments show that iReVa outperforms existing methods in terms of edit success and generalization in two Knowledge editing benchmarks, and it also conducts the first knowledge withdrawal test.

### Strengths
* This paper presents a novel approach by expanding the original MLP's kv-pairs to store additional knowledge, thereby achieving knowledge updates. This idea is quite innovative.

* A new knowledge editing dataset is released.

* The method outperforms other major knowledge editing baselines on two benchmarks.

* The code is released.

### Weaknesses
1. L072-L073:  "In contrast, Meng et al. (2023a), through a cosine similarity analysis on hidden states experiment, posed viewpoints that the self-attention module can extract various types of knowledge". Is this a citation error? I don't believe the ROME paper conducted such an experiment. Please correct me if my understanding is incorrect.

2. It would be much more convincing if we could see some performance results on the LLaMA series models, such as LLaMA2-7B or LLaMA3-8B. Based on experience. Because knowledge editing methods tend to show varying performance differences when applied to LLaMA models.

3. L143-L146: Please double check the computation formulas inside the transformers block. Why is self-attention computed twice? It should only be computed once.

4. It would be helpful when the results include the "Probability" metric, which reflects whether the editing effects can cover other related knowledge. The details of this metric can be found in [1] and [2].

**Writing:**

(1) Please be careful of the \citep and \citet usage in the paper to make it more readable.

### Questions
Please see the Weaknesses section above.

### Soundness
3

### Presentation
2

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
This work proposes an alternative methodm, **iReVa**, to update/insert $(s, r, o)$ knowledge tuples in autoregressive transformer LMs. The authors propose expanding number of neurons in the middle representation (output of `up_proj`) of 2 layer MLP blocks (`up_proj` followed by a `down_proj`). A (set of) such additional neurons uniquely correspond to an updated knowledge tuple, and the authors showed that they can leverage this to "turn off" those neurons to retrieve the LMs original prediction before that specific update.

### Strengths
* The proposed method scales to batch updates upto 10K knowledge tuples. Many of the knowledge editing methods fail to reach that kind of scale.
* The added neurons are traceable to specific knowledge tuples, and thus the method is more interpretable. 
    * For frequently changing facts a set of iReVa neurons can also be reusable (I think, the authors didn't really mention this in the paper)
* Seems to beat other methods in benchmarks (I am a bit suspicious on this, see questions)

### Weaknesses
 I think the paper introduces a nice idea and is decently written. But I have some concerns about the scores presented in their evaluations as they don't match the scores reported in existing works (see Questions, please). On that ground I am choosing a borderline reject. I will be happy to increase my score if the authors can give reasonable explanations.

**Edit:** Score increased to 6 (borderline accept) after authors' rebuttal.

### questions:
 * You mentioned CRUD operations in the abstract. Do you think your method can be applied to **delete** an existing knowledge from the LM?

* Do you add one neuron (one K row and one V column) per knowledge tuple? Or, is that $n$? I am assuming $n$ is the batch size (?), but I got a bit confused later by some of the languages in the paper.

* For multi-token objects such as $P(s, r) = $ `Ran Blake used to teach in` $o = $ `New England Conservatory of Music`, you split that tuple into multiple individual facts. You split it into $P(s, r) \rightarrow$ `New`, $P(s, r) +$ `New` $\rightarrow$ `England` ..., if I am not wrong. I feel you need further tests to make sure if that is alright. Does the model forget to map `New` to other valid continuations, like `New Zealand`? I think this should be tested with targetted cases designed specificly for the multi-token object in question. Randomly sampling unrelated facts and doing a specificity test is not enough to address this issue.

* Evaluation

    * The score $S$ used in ROME, MEMIT ([Meng et al, 2022](https://arxiv.org/pdf/2202.05262)) is the ***harmonic*** mean of $ES$, $PS$, and $NS$; which penalizes more for lower individual scores. Fix this in your paper.

    * You didn't use CounterFact (by [Meng et al, 2022](https://arxiv.org/pdf/2202.05262)) or other datasets, but proceeded to make your own dataset. I am not sure what prompted you to do this considering that your dataset is very similar, both in structure and in scale, to CounterFact (I think). And if I know correctly CounterFact also adapts zsRE, PARAREL, (and WikiData). Did you find some limitations in the existing dataset/benchmarks?

    * Can you give examples of what kind of paraphrases you test generalization (PS) with? I am a bit surprised that you were able to reach this good generalization scores by targeting the last token of the input pormpt $P(s, r)$. If I understand right, the main reason ROME/MEMIT targets subject last position instead is to achieve better generalization. You should also check cosine similarity of representations with different paraphrases to justify this design choice.

    * I was surprised to see such poor scores for MEMIT on Table 1. I expected atleast the efficacy score (ES) to remain high across all the LMs as MEMIT calculates $V$ of the $K \rightarrow V$ map with a gradient optimization. MEMIT reported scores on GPT-j (Figure 5 on CounterFact 10K and Table 1 on zsRE 10K,  [Meng et al, 2023](https://arxiv.org/pdf/2210.07229)), and you also include GPT-J results on Table 4. Your scores just doesn't seem to match. This makes me suspicious of your reported scores. (I am choosing to believe Meng et al's reported scores over yours as their paper is already published and multiple followup works has evaluated and extended that work.) Are you applying MEMIT on the last token of the prompt instead of the last token of the subject? Is it possible that you have made some other errors while setting up these benchmark methods? ... As far as I could understand, your dataset is not that different to justify this discrepancy.

### Questions
* You mentioned CRUD operations in the abstract. Do you think your method can be applied to **delete** an existing knowledge from the LM?

* Do you add one neuron (one K row and one V column) per knowledge tuple? Or, is that $n$? I am assuming $n$ is the batch size (?), but I got a bit confused later by some of the languages in the paper.

* For multi-token objects such as $P(s, r) = $ `Ran Blake used to teach in` $o = $ `New England Conservatory of Music`, you split that tuple into multiple individual facts. You split it into $P(s, r) \rightarrow$ `New`, $P(s, r) +$ `New` $\rightarrow$ `England` ..., if I am not wrong. I feel you need further tests to make sure if that is alright. Does the model forget to map `New` to other valid continuations, like `New Zealand`? I think this should be tested with targetted cases designed specificly for the multi-token object in question. Randomly sampling unrelated facts and doing a specificity test is not enough to address this issue.

* Evaluation

    * The score $S$ used in ROME, MEMIT ([Meng et al, 2022](https://arxiv.org/pdf/2202.05262)) is the ***harmonic*** mean of $ES$, $PS$, and $NS$; which penalizes more for lower individual scores. Fix this in your paper.

    * You didn't use CounterFact (by [Meng et al, 2022](https://arxiv.org/pdf/2202.05262)) or other datasets, but proceeded to make your own dataset. I am not sure what prompted you to do this considering that your dataset is very similar, both in structure and in scale, to CounterFact (I think). And if I know correctly CounterFact also adapts zsRE, PARAREL, (and WikiData). Did you find some limitations in the existing dataset/benchmarks?

    * Can you give examples of what kind of paraphrases you test generalization (PS) with? I am a bit surprised that you were able to reach this good generalization scores by targeting the last token of the input pormpt $P(s, r)$. If I understand right, the main reason ROME/MEMIT targets subject last position instead is to achieve better generalization. You should also check cosine similarity of representations with different paraphrases to justify this design choice.

    * I was surprised to see such poor scores for MEMIT on Table 1. I expected atleast the efficacy score (ES) to remain high across all the LMs as MEMIT calculates $V$ of the $K \rightarrow V$ map with a gradient optimization. MEMIT reported scores on GPT-j (Figure 5 on CounterFact 10K and Table 1 on zsRE 10K,  [Meng et al, 2023](https://arxiv.org/pdf/2210.07229)), and you also include GPT-J results on Table 4. Your scores just doesn't seem to match. This makes me suspicious of your reported scores. (I am choosing to believe Meng et al's reported scores over yours as their paper is already published and multiple followup works has evaluated and extended that work.) Are you applying MEMIT on the last token of the prompt instead of the last token of the subject? Is it possible that you have made some other errors while setting up these benchmark methods? ... As far as I could understand, your dataset is not that different to justify this discrepancy.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new method to perform model-editing and allow potential knowledge withdrawing.

### Strengths
- The topic is important.
- The proposed idea is simple. 
- The experimental results seem to show the effectiveness of this method

### Weaknesses
 - **Method Design**: The paper proposes to add the adaptor to the original model, however, as stated in line 201 "To avoid damaging the
original behavior of the edit model, the edit block merely works on the final token, which is the last token before generation", this means some **oracle information** is used in this model, i.e., **this method needs to let the model know which is the final token**. This is impractical in real world. When we edit the knowledge in the model, we want the model to answer correctly no matter what users ask, and we would never know when the model is going to reveal the knowledge that is supposed to be edited. For instance, when the knowledge "sky is blue" is edited to "sky is green", then for various questions such as "is the color of the sea and the sky the same?" the model would fail as this method would not know when to add the adaptors. The limitation of only applying the adaptor at the final token severely restricts the method's applicability to direct editing scenarios, making it unsuitable for more complex reasoning tasks or situations where the edited knowledge is embedded within a longer context. This design choice fundamentally limits the method's practical use cases.

- **Experimental Results**: For zsRE-10k, the authors did not use the deduplicated dataest from MEMIT, which may yield unfair comparisons. As the results in the original paper show that MEMIT can achieve 96.7 (ES), 89.7 (PS) and 26.6 (Specificity) on 10000 edits, and it is only 52.62, 47.29, 27.63 as reported in this paper. I would doubt if the implementation is correct and the hyper-parameter is properly tuned. The ideal case would be evaluating iReVa on the exactly same dataset used in MEMIT. The authors' choice to deviate from the established evaluation protocol for zsRE-10k raises concerns about the validity and comparability of their results. Furthermore, the significantly lower performance compared to the reported results in the MEMIT paper, even with the same dataset size, suggests potential issues with the implementation or hyperparameter tuning of the proposed method. The lack of direct comparison on the same dataset makes it difficult to assess the true effectiveness of iReVa.

- **Withdrawing knowledge experiments**: The authors stated in line 377: "Notably, this test is not applicable to any other editing methods as their edited parameters are untraceable. This is the first attempt at conducting more flexible knowledge editing." However, It is feasible to withdraw knowledge from MEMIT, GRACE, etc. Please refer to [2], where the authors withdraw the knowledge by editing "The president of United States is Joe Biden" to "The president of United States is <endoftext>", i.e., using the token "<endoftext>" can allow these model-editing methods to edit the model, which shows pretty good results. Besides, it seems to be quite trivial for this method to be able to withdraw the knowledge as they can just remove the related adaptors. The claim that other methods cannot withdraw knowledge is incorrect, as demonstrated by the ability of methods like MEMIT and GRACE to achieve this by editing to a specific token. The fact that iReVa can easily withdraw knowledge by removing adaptors, while a potential advantage, does not make it fundamentally different from other methods in terms of knowledge withdrawal capability.

### Questions
I do not have extra questions.

### Soundness
2

### Presentation
3

### Contribution
2
