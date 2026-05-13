# Which Examples to Annotate for In-Context Learning? Towards Effective and Efficient Selection

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Large Language Models (LLMs) can adapt to new tasks via in-context learning (ICL). ICL is efficient as it does not require any parameter updates to the trained LLM, but only few annotated examples as input for the LLM. In this work, we investigate an active learning approach for ICL, where there is a limited budget for annotating examples. We propose a model-adaptive optimization-free algorithm, termed \adaicl, which identifies examples that the model is uncertain about, and performs semantic diversity-based example selection. Diversity-based sampling improves overall effectiveness, while uncertainty sampling improves budget efficiency and helps the LLM learn new information. Moreover, \adaicl poses its sampling strategy as a Maximum Coverage problem, that dynamically adapts based on the model's feedback and can be approximately solved via greedy algorithms. Extensive experiments on nine datasets and seven LLMs show that \adaicl improves performance by 4.4\% accuracy points over SOTA (7.7\% relative improvement), is up to $3\times$ more budget-efficient than performing annotations uniformly at random, while it outperforms SOTA with $2 \times$ fewer ICL examples.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an active learning approach for ICL, which combines diversity-based sampling and uncertainty-based sampling. It introduces three versions of the proposed framework, including ADAICL-BASE, ADAICL, and ADAICL+. The base version performs k-means clustering over the identified hard examples, while ADAICL quantifies whether each example can help the model learn new information, and the plus version further equips a reweighting schema for the MAXCOVER problem to ensure dense regions with hard examples are preferred. Experiments study nine NLP datasets and GSM8K, with 1.3B to 65B LLMs across several model families.

### Strengths
1. The paper is presented in a coherent manner and easy to follow.
2. The logical progression connecting the various methodological variants is well-articulated. 
3. The improvements over the baseline is good.

### Weaknesses
1. Active learning for NLP is a well-studied area. This paper lacks the illustration of why AL for ICL is challenging or the key difference compared to AL for fine-tuning based NLP. Otherwise, why do not directly apply multiple sophisticated query policies proposed in AL to the ICL example selection problem?

2. Although not for ICL, combining diversity and uncertainty for data selection have been studied in previous literature:\
Entropy-Based Active Learning for Object Detection With Progressive Diversity Constraint;\
Cold-start data selection for few-shot language model fine-tuning: A prompt-based uncertainty propagation approach;\
ACTUNE: Uncertainty-Based Active Self-Training for Active Fine-Tuning of Pretrained Language Models.

3. The baseline methods are limited. Although the related work discusses a batch of work for active learning in ICL/NLP, only a few simple baselines are compared in experiments. How does ADAICL compare to other AL methods? Meanwhile, I am also wondering about the performance of zero-shot GPT-4 or GPT-3.5-turbo.

4. The method relies on the estimation of model uncertainty, which is only suited for the LLMs with moderate scales, For those most recent LLMs with hundreds billions parameters, usually we do not have a way to obtain its uncertainty.

### Questions
See above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an example selection method for in-context learning via active learning techniques. Given an unlabeled set $\mathcal{U}$ of examples, the authors first choose the set of hard examples $\mathcal{U}_h$ based on model's confidence score $u_i$. Then choose examples up to a given budget $B$ from centroids of each k-mean cluster, which is termed as $\texttt{AdaIcl-base}$. To improve the method, the Maximum Coverage problem is applied. The goal is then to choose $B$ most representative example that cover the most semantic space by building a global graph based on the semantic embedding space ($\texttt{AdaIcl}$). To further improve the method, hard examples are selected from denser regions (instead of outliers) by implementing the re-weighting schema ($\texttt{AdaIcl+}$). The results show effective improvement over nine datasets and seven LLM models.

### Strengths
+ The authors provide an intuitive approach which does make sense with additional efficiency.
+ The paper is well structured.
+ Results over many models and datasets showing great performance of variants of $\texttt{AdaICL}$.

### Weaknesses
- The construction of the graph is highly dependent on other off-the-shelf encoders, which might not be representative of the target model.
- The method requires multiple prompts to get LLM feedbacks (probability scores) for each example, which is expensive.
- Quite outdated models used (even given the ICLR submission date), so it is hard to verify if the method is applicable to more up-to-date LLMs.

### Questions
- How are you performing k-mean clustering for $\texttt{AdaIcl-base}$? 

- What embedder are you using for choosing top-k examples?

- Have you compared to any similarity based baselines?

- Have you compared to any retriever-based baselines?

- Question about the practical setting. If we need to annotate the selected examples on demand based on the query, then why not annotate directly the query? 

- Why are you choosing top-$N_{\theta}$ examples based on probability scores? Would uncertain examples mean bottom-$N_{\theta}$? 

- RQ4. is provided but not addressed in the main paper nor referred to Appendix?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method to select samples to present for ICL based on set coverage in an embedding space. The proposed method, AdaICL, uses a greedy approximation for the MaxCover problem to select sets that cover as many hard problems as possible. AdaICL outperforms baselines on a wide variety of tasks and does not appear to be too expensive to run.

I think this paper is closer to a 7 than 6 but unfortunately 7 is not an option on the rating scale.

### Strengths
- Good empirical performance on a wide variety of LLMs and datasets.
- AdaICL appears to outperform kMeans based retrievers such as Votek and AdaICL base
- AdaICL appears to be more robust to sample presentation order than the baselines on some tasks

### Weaknesses
- Why is the semantic similiarity space determined by a 3rd party embedding model such as SBERT? Shouldn't this be from the LLM itself, such as from an embedding layer?
- How does overall performance depend on $m$ in $G_m$?
- My understanding is that AdaICL queries a LLM many times to get confidence scores *before* feeding the final prompt in to get $y_{test}$. How do the various baselines and AdaICL compare when limited to the same LLM query budget? For example, random selection requires 0 queries, which could be far cheaper than running AdaICL.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores in-context learning (ICL) for Large Language Models (LLMs) where the goal is to adapt the model to new tasks with minimal annotation. It introduces ADAICL, an active learning approach that efficiently selects examples for annotation within a limited budget. ADAICL identifies uncertain examples for the model and uses semantic diversity-based selection. This approach, treated as a maximum coverage problem, dynamically adapts based on the model's feedback. Experiments across datasets and LLMs demonstrate ADAICL's superiority, improving accuracy over state-of-the-art works and being up to 3 times more budget-efficient than random annotation. It also outperformed existing methods with half the number of annotated examples.

### Strengths
- The motivation is clear. It is significant to study how to determine which unlabeled instances should be labeled. This is important to reduce the cost of annotations in in-context learning. 
- Experimental results are overall great. On a series of tasks, the proposed method can achieve the best performance.

### Weaknesses
- The contributions are somewhat overclaimed.
- Technical contributions are not sufficient. 
- The writing also should be polished. For the current form, there are a series of unclear justifications.

More details about the above weaknesses can be checked below.

### Questions
- It is possible to meet outliers if the method overemphasizes the selection of diverse data. However, in the current form, it is not clear how to address the issue. 
- Does the $k$-NN retriever equal the similar retriever in the Vote-$k$ paper?
- This paper claims that "However, these approaches do not consider which examples help the LLM learn new information and may waste resources for annotating examples whose answers are already within the model’s knowledge." I am somewhat confused about this claim. The method Vote-$k$ also uses the feedback of LLMs. Could the paper give more details about this?
- Does the uncertain with respect to one example equal that the LLM can learn it accurately?
- The paper argues that previous work assumes a high-resource setting, where a large set of ICL examples is already annotated. Could the paper provide some detailed examples for better understanding?
- For Section 4.1, could the paper provide more details about how to obtain the probability with respect to the label or demonstrations?
- Compared with previous work such as Vote-$k$, the method proposed by this work is more complex. It introduces a series of hyper-parameters. How to balance them in practice? Also, is there a time advantage of the proposed method over baselines?
- What is the definition of "egonet" in this paper?
- For Figure 5, could the paper supplement the comparison between all methods not just the best baseline?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
