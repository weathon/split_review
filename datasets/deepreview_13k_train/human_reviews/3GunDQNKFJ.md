# Learning-Retrieval-Revision For Large Language Model Domain Adaptation

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
While large language models (LLMs) like GPT-4 have recently demonstrated astonishing zero-shot capabilities in general domain tasks, they often generate content with hallucinations in specific domains such as Chinese law, hindering their application in these areas. This is typically due to the absence of training data that encompasses such a specific domain, preventing GPT-4 from acquiring in-domain knowledge. A pressing challenge is that it’s not plausible to continue training LLMs of such scale on in-domain data.

This paper introduces a simple and effective domain adaptation framework for GPT-4 by reformulating generation as an adapt-retrieve-revise process. The initial step is to adapt an affordable 7B LLM to the target domain by continuing learning on public in-domain data. When solving a task, we leverage the adapted LLM to generate a draft answer given a task query. Then, the draft answers will be used to retrieve supporting evidence candidates from an external in-domain knowledge base. Finally, the draft answer and retrieved evidence are concatenated into a whole prompt to let GPT-4 assess the evidence and revise the draft answer to generate the final answer.

Our proposal combines the advantages of the efficiency of adapting a smaller 7B model with the evidence-assessing capability of GPT-4 and effectively prevents GPT-4 from generating hallucinatory content. In the zero-shot setting of four Chinese legal tasks, our method improves accuracy by 33.3% compared to the direct generation by GPT-4. When compared to two stronger retrieval-based baselines, our method outperforms them by 15.4% and 23.9%. Our code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a domain adaptation framework for LLMs, reimagining generation as a three-step adapt-retrieve-revise process. The authors present a straightforward yet effective technique for adapting a smaller LLM to a specific target domain through continued learning on in-domain data. Subsequently, the adapted LLM is employed to generate an initial draft in response to a task query. This draft is then used to achieve more precise retrieval compared to using the query alone. The proposed method has been shown to significantly enhance the accuracy of LLMs in knowledge-intensive domains (i.e., legal domain).

### Strengths
1. This paper investigates an important research question: how to adapt LLMs (e.g., GPT-*) to knowledge-intensive domains. Their proposed pipeline is simple yet effective for solving tasks within the legal domain.
2. The high-level idea of using candidate answers to create a more informative query for improving retrieval performance is novel.
3. The authors conduct comprehensive experiments and ablation studies across several legal tasks to demonstrate the effectiveness of the proposed pipeline.

### Weaknesses
1. More established retrieval modules (e.g., BM25, Contriever, or GPT embeddings) should be investigated to enhance the robustness of the findings. The current study uses a single embedding model, which may not be sufficient to demonstrate the generalizability of the proposed method across different retrieval techniques. It is important to evaluate the method's performance with other common retrieval methods to ensure that the observed improvements are not specific to the chosen embedding model.
2. The study is limited to GPT-4 models and explores only a subset of each task. The authors should consider including other open-source LLMs, such as Llama-2, to demonstrate the generalizability of the proposed methods. The reliance on a single closed-source model limits the applicability of the findings, and it is crucial to assess the method's effectiveness with other models, especially those that are more accessible to the research community. Furthermore, the limited scope of task subsets might not fully represent the complexity of the legal domain.

### Questions
In real-world scenarios, training domain-specific smaller LLMs may still be computationally intensive and time-consuming. Is there a way to mitigate these challenges without significantly compromising the model's performance that can be generally extended to other knowledge-intensive domains (e.g., medical, financial)?

### Soundness
3 good

### Presentation
2 fair

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
In this paper the authors proposed an adapt retrieve revise process for domain adaptation. They first train a model for certain domain and then use it to create a draft answer. This draft answer is used to retrieve evidence from some external knowledge base. Finally they use the draft answer and entire retrieved document ans query GPT 4 to revise the answer based on the evidence collected.

They conducted experiments on Chinese Legal corpora and show good improvements over the retrieval based generation.

### Strengths
The authors have contributed towards retrieval based generation and showed significant improvement over QA on certain domains like Chinese Legal QA. 

This is an important area of research to improve the performance of LLM on low resource languages.

### Weaknesses
While this approach shows promise, it would be good to showcase if the sameis applicable or showing equivalent gains in other domains. 
It would be good to run some ablation where using GPT4 used for retrieval as well as reviser. Also it would be interesting to understand how many evidence document is needed for a better revise mechanism. It seems that retrieval from the 7B model is zero shot, can that performance be improved ?

Is the revise a few shot generation? Also the author may discuss how just doing the revise of the draft based on the evidence have improved the recall so much in LCR, CP ad LegalQA.

The proposed approach seems to gain significant improvement over just retrieval based approach. Can the author provide some more details about what the retrieval mechanism used in the baseline? Also a comparison on the quality of retrieved evidence would be easier to understand.

Minor: The metrics etc should be mentioned in the table description for better understanding

### Questions
Please refer weaknesses,

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a combination of continual training and retrieval-augmentation approaches to enhance GPT-4's performance in Chinese legal domain tasks. The proposed method consists of three steps: (1) first it adapts a 7B Chinese LM to the target domain using 50B Chinese legal data, (2) retrieves supporting evidence to a draft answer generated by the fine-tuned LM, and (3) feed the draft answers and evidence to GPT-4. Experimental results show improvements in Chinese legal QA datasets. 
I have several major concerns about this paper: narrow problem focus and applicability to other languages or domains, limited novelties and soundness of evaluations, and presentations.

### Strengths
- This paper proposes a new method for domain adaption in Chinese legal domains, which conducts continual training of a Chinese LM on the target domain corpus and then retrieves relevant documents that suports or refutes the answers drafted by the smaller LM.  
- By feeding the draft answer and retrieved evidence, proposed method obtains strong improvements on multiple Chinese legal QA datasets.

### Weaknesses
There are three main concerns about the papers about focus and motivations, soundness of evaluations, and the paper presentations.

**1. Narrow focus of the problem and wider applicability of the proposed method**

While improving the reliability of LMs in legal domains, especially more resource-constrained non-English language is important, this work focuses on a single language, and the proposed method heavily relies on the availability of 7B-size LMs in the target language and dozens of billions of domain corpus for continual pre-training. In many languages such rich resources are not available, and as the evaluations are mostly on Chinese legal domain datasets, it is unclear if the proposed method is applicable to other languages or not. If this work only focuses and improves zero-shot performance in Chinese legal domain tasks, it may not be interesting to wider audience of ICLR.

**2. Soundness of evaluations**

- **Evaluation metrics**

In Section 3.2, the authors mention that their evaluation simply relies on whether the answer includes the ground-truth law clause title is included or not.
> For tasks LCR, CP, and LegalQA, our metric is the recall of whether the title of the ground-truth law clause is included in the generated answer. This is because, in real-world applications, with the correct title, the contents of the law clause can be easily revised by the rule-based system, indicating that the title is more important than the content.

I don't think it is the proper way to evaluate accuracy or factuality of LM generation to legal domain related questions. For example, although this is an extreme case, if the only one metric is recall, a baseline always generating all clause titles can get perfect score. Using a recall of certain substrings to assess the quality of legal QA questions doesn't seem approppriate. Or if the end goal is to simply find a title of clause titles, I don't think using LM to generate full answers is the most optimal way to achieve such goal, and improving domain adapted retrieval system might be more suitable.
I checked the LegalQA dataset Github page, and their metrics seem to be MAP, MRR, and P@1, not recall. This makes me wonder why authors decided to use different metrics.
https://github.com/siatnlp/LegalQA

- **Baselines**
Given that the evaluation tasks are mostly evaluating whether a model can generate the correct title or a retrieval task, I think authors should include stronger retrieval models (at least multilingual encoder-based retrievals) as part of the pipelines or even as baselines to compare the proposed methods with. While authors claim that GPT-4with retrieval  (Query-based) is not as good as the proposed method, I suspect it is because their retrieval model is E5, which is not competitive compared to more recent embedding-based methods, and is not a multilingual retrieval system and the retrieval quality is poor. For instance, what happens if the authors use mContriever (Izacard et al., 2022) or even conduct continual pre-training of mContriever on the Chinese legal domain corpus used for 7B LM training?
Also except for JEC-QA, the evaluations are essentially retrieval tasks, so I wonder how well a competitive retrieval-based method perform on this task (given a question query, retrieves the clause text and title directly).

**3. Technical contributions or novelties of this work**

Continual training for domain adaptations or retrieval-augmentation for domain adaptations have been already studies. While drafting an answer from a small LM to search relevant document sounds somewhat new and interesting, due to the limited focus and evaluation protocol, I am not sure whether this can be widely applicable to other domains or indeed effective to enhance final generation quality.

**4. Presentation**

Occasionally, I found the paper is hard to follow, making it difficult to understand what the true contributions of this work is. Having a better structure might improve the paper presentations. For instance, Section 2 consists of low-level experimental details (the compuational requirements) as well as high-level ideas.

### Questions
- Why did you use recall as an evaluation metric? 
- Did you try different retrieval methods, especially multilingual retrieval models?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the domain adaptation of large language models (LLMs) by focusing on the Chinese law domain. An adapt-retrieve-revise framework is proposed to adapt GPT-4 to the domain without modifying its own parameters. The initial step of the framework is to adapt a 7B LLM to the target domain through continual pre-training and the continual pre-trained model will be used to provide a draft answer. The framework will then use the draft answer to retrieve information and then call GPT-4 to revise the answer. The study shows that answer-based evidence retrieval yields much better results than question-based retrieval. The reported results also show that the proposed framework leads to much less hallucination and better recall on a series of tasks in the Chinese law domain.

### Strengths
1. The proposed framework is simple but effective. Tuning an affordable LLM to adapt GPT-4 can be viewed as another kind of parameter-efficient tuning. The draft output acts as a symbolic representation to link the trainable module and the fixed LLM. While many continual pre-training or continual learning methods cannot be applied to GPT-4, the work provides a general approach to use previous continual learning ideas to adapt GPT-4 to specific domains.
2. The experimental results are strong. Although this work is more empirical and does not have many theoretical contributions, the thorough analysis can bring interesting insights to the practitioners.

### Weaknesses
1. The presentation of this work needs improvement, especially the illustrations and their captions. Concise explanations should be added to the caption besides the caption title to make the illustrations more self-contained.
2. Some related works are missing. I think the paper should also discuss the literatures related to continual pre-training since it's a crucial part in the proposed adapt-retrieve-revise framework.
3. Regarding Table 1, I think one key experiment is missing: What's the result of using GPT-4 to provide a draft, retrieve with the draft answer, and revise the answer? I think the effect of continual pre-training is not adequately ablated in the current experiments.

### Questions
1. Could you provide the data statistics of datasets used in this work?
2. Is *recall* a commonly used metric on tasks LCR, CP, and LegalQA? I feel that with this metric alone, we cannot track whether the output contains some law causes that are related to the question. For example, the output can cover all the necessary law causes and also include some irrelevant law causes or hallucinate some non-existent law causes at the same time.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
