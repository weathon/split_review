# Detecting Hallucination Before Answering: Semantic Compression Through Instruction

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Large language models (LLMs) excel in various tasks but often suffer from hallucinations, providing incorrect information with high confidence. To address this, we focus on detecting when an LLM knows or does not know an answer, a concept referred to as the ``feeling of knowing'' (FoK). We propose a novel approach called Semantic Compression by trying to Answer in One-word (SCAO), which enables efficient FoK detection before generating full sentences, with only minimal computational cost. Additionally, we introduce a method to measure confounding variable effects in benchmarks, an Approximate Misannotation Effect (AME) test. Our experiments demonstrate that the feature fusion model of our SCAO and probing achieves enhanced performance in FoK detection in both short and long-form entity questions. The code and the dataset is available online (https://anonymous.4open.science/r/SCAO-2FF8).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a method for detecting when an LLM knows the answer to a question *before* generating it. This method relies on probing the last token logits and hidden state obtained via a special "answer-in-one-word" prompt attached to the original query. The paper also introduces a procedure for identifying datasets with misannotations and excludes these from the analysis. Experimental results on entity-centric datasets suggest that the proposed method significantly improves the accuracy of detecting questions where the LLM is likely to provide a correct answer.

### Strengths
- The problem formulation of detecting a hallucination *without* generating an answer is quite interesting and potentially useful.
- The main idea of representing the query via a "answer-in-one-word" prompt is intuitive and interesting.
- Several baselines are evaluated and the proposed methods shows notable gains in accuracy of detecting hallucinated answers.

### Weaknesses
 - The AME analysis for detecting misannotations is unconvincing. The main idea is that if a classifier can detect hallucinated answers based on the question alone, this points to some issue with the question. But such a classifier might be simply detecting difficult questions or questions about tail knowledge. In this case, it is not clear why datasets with such questions should be excluded? Moreover there isn't any further evidence provided that the datasets excluded based on AME were indeed problematic.
- Max token length is set to 50 when generating answers for the long-form QA datasets -- this seems very short for a dataset like ELI5. Further, it is not clear why a new dataset like Explain was used rather than other existing long-form QA datasets (e.g., ASQA).
- The main motivation for detecting a hallucination before generating is to save the cost of decoding. However, most of the empirical analysis in this paper is on datasets where the answers are short entities. In such a case, appending the answer-in-one-word prompt is perhaps equally expensive as decoding the answer. Hence, the paper would benefit from evaluating on more realistic setups where the answers are longer. (There are some results in Table 3, but these are not very convincing).

### Questions
- How does SCAO compare to R-tuning on the same datasets as used in the latter paper?

### Soundness
2

### Presentation
4

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
This work focuses on addressing hallucinations in large language models, by estimating to what extent the model has relevant knowledge— relying on the fact that model hallucinations primarily arise when the model is making extrapolations. The work proposes a method “semantic compression via trying to answer in one word” to estimate to what extent the model has relevant knowledge or not (FOK).

### Strengths
(1) The paper is well-written and clear.

(2) The experimental methodology is well laid out and the rationale behind various decisions is clearly explained in the manuscript.

(3) This work joins a growing line of research in estimating model confidence and knowledge, which is an interesting research direction.

### Weaknesses
(1) The evaluation is mostly done focusing on QA tasks where there is a concept of a right answer or a set of right answers. However, many times hallucinations can happen in more open-ended settings, like with the prompt “Tell me a Biography of Barack Obama” (see Min et al., 2023). Models may interleave true facts and false facts when generating a response, how can this method be extended to these typical long-form settings?

(2) It would be great to include more analysis of when this method works and when it doesnt, for example where in the model response the correct answer string occurs when making the FOK dataset.

### Questions
Could the authors explain how SCAO works when a question is not answerable by a single word?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a method namely SCAO to detect the hallucination before full generation of LLMs. The key idea is to prompt LLMs to answer in one word. It can compress the semantic information, and assess the model's confidence. This work also introduced a method namely AME to measure mis-annotation effects in benchmarks.

### Strengths
1. The experiments are thorough. The method AME assessing benchmark quality is a valuable contribution.

2. The paper is well-written and easy to follow. The key concepts like FoK and SCAO are explained clearly. It is important for LLMs on hallucination detection, especially before full generation. It minimizes the computational overhead.

### Weaknesses
1. Although the retriever analogy is interesting, it is not very clear to me that why compressing to one word should work better than other forms of compression.

2. The gains are relatively modest in some cases. It will be great if more in-depth analysis of when and why the proposed SCAO can outperform.

### Questions
Did you try different forms of semantic compression rather than with one-word answers?

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
4

### Summary
The paper presents a novel approach to detect when a large language model (LLM) knows or doesn't know an answer, a concept referred to as the "feeling of knowing" (FoK). The authors propose Semantic Compression by trying to Answer in One-word (SCAO), an efficient method for FoK detection that requires minimal computational resources. The paper also introduces a method to measure the impact of confounding variables in benchmarks, called the Approximate Misannotation Effect (AME) test. The experiments show that combining SCAO and probing improves FoK detection in both short and long-form entity questions. The paper argues that LLMs are structurally similar to dense retrievers and that token-level confidence can be a key source of information representing the vividness of memory. It also highlights the issue of misannotation in previous research and proposes an AME test to measure it. The results show enhanced performance of the feature fusion model of SCAO and probing, demonstrating their synergistic nature.

### Strengths
1) The authors propose a novel approach, Semantic Compression by trying to Answer in One-word (SCAO), to detect when a Large Language Model (LLM) knows or doesn't know an answer. The paper also introduces the Approximate Misannotation Effect (AME) test, a new method to measure confounding variable effects in benchmarks. 
2) By detecting when an LLM knows or doesn't know an answer before generating a full sentence, the SCAO method could significantly reduce computational cost and improve user experience. The AME test could also help researchers better understand and control the effect of misannotation in benchmarks.

### Weaknesses
The paper has some foundamental flaws as outlined. Nonetheless, after addressing these problems, it could potentially be a captivating piece of work.
1) The problem that the paper is attempting to solve is not well justified. The concept of "Detecting hallucination before answering" appears contradictory for two primary reasons. Firstly, the term "detecting" implies that an answer already exists to be detected, which is inconsistent with the concept of doing so prior to providing an answer. From my perspective, it appears more akin to "predicting hallucination before answering". Secondly, the necessity for "predicting" before answering is not adequately explained. Although there may be valid reasons for this, the paper fails to provide them.
2) The paper conflates the concept of "feeling of knowing" with actual "hallucination". The authors assert that their focus is on determining when a Large Language Model (LLM) knows or does not know an answer, but they do not reference or compare their work to existing studies on the subject, such as the well-regarded "Do Large Language Models Know What They Don't Know? (Z Yin, 2023)". Furthermore, while the "feeling of knowing" is related to hallucination, the two are not identical.
3) The experimental design is biased. The paper specifies that "Our baseline should predict FoK label y from question q without allowing the target LLM \theta to infer more than two steps". However, this limitation is based on the paper's specific methodology, not the task itself, and as such is unfair to the baselines.
4) The research on the impact of misannotation does not have a significant link with the SCAO, suggesting it could be divided into two separate papers.

### Questions
LN013: "we focus on detecting when an LLM knows or does not know an answer", feeling of knowing is a different task from hallucination detection.

LN068: "the effect of misannotation", what specific effect does it refer to?

LN080: I cannot see the connections between the contribution 1) and 2).

LN105: "FoK of LLM" misses the studies about "know and don't know in LLMs". For example, "Do Large Language Models Know What They Don't Know? (Z Yin, 2023)"

LN312: "misannotation effect" need literature support or justification. Why is it a problem and why is it important for your topic?

LN388: "Our baseline should predict FoK label y from question q without letting the target LLM \theta infer more than two steps", why should the baseline follow the restriction of your method?

LN429: "impossible to address without further clue", what does it mean? Need further explanation.

LN430: "we only use English questions and exclude instances with multiple labels", why?

### Soundness
2

### Presentation
2

### Contribution
3
