# Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning

- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
Large language models (LLMs) have achieved remarkable performance on vari-
ous natural language tasks. However, they are trained on static corpora and their
knowledge can become outdated quickly in the fast-changing world. This moti-
vates the development of knowledge editing methods designed to update certain
knowledge in LLMs without changing unrelated others. To make selective edits,
previous efforts often sought to update a small amount of parameters in some spe-
cific layer(s) of a LLM. Nonetheless, in challenging scenarios, they still fall short
in making successful edits while preserving knowledge irrelevant to the updates
simultaneously, resulting in a notable editing-locality trade-off. In this work, we
question if the trade-offs are caused by the fact that parameter-based updates have
a global effect, i.e., edited parameters affect all inputs indiscriminately. In light of
this, we explore the feasibility of representation fine-tuning, which applied some
linear update to a few representations in a learned subspace, for knowledge edit-
ing. While being effective to enhance an LLM’s general ability as demonstrated in
the previous work, we theoretically show that this linear update imposes a tension
in editing-locality trade-off. Subsequently, BaFT is proposed to break the linear-
ity. BaFT computes a weight for each basis that spans a dimension of the subspace
based on the input representation. This input-dependent weighting mechanism al-
lows BaFT to manage different types of knowledge in an adaptive way, thereby
achieving a better editing-locality trade-off. Experiments on three LLMs with five
editing benchmarks in diverse scenarios show the superiority of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper discusses the challenge of updating LLMs with new knowledge without disturbing the existing knowledge they hold. Traditional methods of parameter-based updates have limitations in achieving this, as they tend to affect all inputs globally. The study introduces a new method called BaFT which achieves a better balance between making necessary updates and preserving unrelated knowledge. The effectiveness of BaFT is demonstrated through experiments on several LLMs across different editing benchmarks, showing superior performance compared to previous methods.

### Strengths
1. This paper is well-written and easy to follow. It also provides a clear introduction of the Knowledge Editing task matter, enhancing its accessibility to a broad audience.

2. The paper addresses a significant problem within the field of Knowledge Editing, focusing on a pertinent limitation associated with current methodologies. The investigation into this particular trade-off is could potentially lead to substantial advancements in the field of Knowledge Editing.

3. The experimental design and execution are robust, utilizing well-chosen benchmarks to effectively demonstrate the proposed method’s validity.

### Weaknesses
1. This paper lacks visual illustrations such as diagrams or figures, which would significantly aid in the comprehension of the methods and results. I recommend the authors add figures to enhance the reader’s understanding and engagement with the content.

2. There is an absence of publicly shared code in the paper or on platforms such as OpenReview. This hinders the reproducibility of the proposed method. I would suggest sharing the code through an anonymous GitHub repository or similar platform. This would greatly aid other researchers and reviewers in replicating and understanding the research.


3. While the motivation behind the study is well-articulated, the methods deployed are somewhat conventional. This paper devotes considerable space to arguing for directly applying the ReFT method to the Knowledge Editing tasks faces limitations. However, the proposed solutions introduced by the authors do not add intriguing or novel aspects to the existing array of techniques in the field.

### Questions
Please refer to the previous section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Building on the ReFT, this paper introduces a novel method called Basis-level Representation Fine-tuning (BaFT) for editing knowledge within Large Language Models (LLMs) while preserving unrelated information. The authors perform a theoretical analysis that highlights the inherent limitations of existing approaches, particularly linear representation fine-tuning, which often necessitates a trade-off between editing effectiveness and the retention of unrelated knowledge (locality). To address these challenges, BaFT calculates the weight for each basis in the subspace based on the input representation, facilitating a more adaptive management of diverse knowledge types. The authors conducted experiments across three different LLMs and evaluated them against five editing benchmarks, demonstrating that BaFT surpasses existing methods in both editing performance and parameter efficiency. Ultimately, BaFT strikes a superior balance between integrating new knowledge and maintaining existing unrelated information.

### Strengths
1. BaFT introduces a non-linear, input-dependent weighting mechanism for basis-level representation fine-tuning, which is a significant departure from traditional parameter-based updates.

2. The authors demonstrate the effectiveness of BaFT through extensive experiments on three different LLMs and five editing benchmarks, showing superior performance in various scenarios.

3. This paper provides a detailed and clear explanation of the proposed method BaFT in conjunction with the theory.

### Weaknesses
1. Innovation and Improvement Effect: The improvements of the method presented in this paper compared to ReFT are limited. Although the authors propose the ReFT-based enhancement method BaFT, experimental results indicate that these improvements show weak effectiveness in knowledge editing benchmark, thus suggesting a lack of innovation in this work.

2. Questions of Method Applicability: 
- In Assumption 2.1, the authors assume as follows: "Let text x encode s and r; text y generated by the LM will convey o if its intermediate representation takes some targeted value t." For instance, a sentences in the WikiData dataset: “The name of the country which Goursez Vreizh is associated with is []” is input into the model, and the generation probabilities are used to assess the accuracy of knowledge editing. Although multiple datasets are presented in this paper, these datasets exhibit high homogeneity in type. 

- In contrast, there are more complex benchmark datasets in the field of knowledge editing, such as MQuAKE[1] and KEBench[2]. These datasets require inputting questions into the model and determining whether the generated responses contain the corresponding answers. For example, the question from MQuAKE, “Which sport is Dudley Town F.C. associated with?” is answered with, “Dudley Town F.C. is associated with the sport of association football.” The complexity of such questions is significantly higher than that of the datasets used in this paper, making them more aligned with real-world application scenarios and challenging the authors' assumptions in Assumption 2.1. The generality of the methods in this paper has been questioned.

3. Choice of Baselines: The baselines in this paper are relatively limited. Key literature, including LTE [1], MELO [2], StaleKE [3], and InstructEdit [4], which are fine-tuning-based methods, are not discussed or compared, resulting in a lack of comprehensiveness regarding the current field of knowledge editing.

4. Performance of Baseline Results: The baseline results reported in the paper are significantly lower than those in existing literature, especially in the Batch Editing and Continual Editing settings, where the performance of the MEMIT method is notably inferior to previous reports. This starkly contrasts with results from several studies (e.g., [1, 2, 3]), casting doubt on the validity of this paper.

Additionally, in the paper [1], it is mentioned that the SERAC and MEND methods, which demonstrate better Locality performance, were not reported in this paper. Additionally, the Fluency metric provided in the paper [1] is also absent from this paper. Based on our experience, when using Eazyedit for evaluation, this metric is usually calculated alongside several other metrics reported in your paper. However, it seems that the authors intentionally overlooked this metric and the aforementioned methods, which is puzzling.

Furthermore, a major concern remains: the performance of BaFT appears to be significantly limited compared to other baselines, such as ReFT and WISE, even in terms of locality. Furthermore, the authors do not seem to provide a clear explanation for this in the experiments. For instance, it is unclear why BaFT's performance does not surpass that of the baselines.

Additionally, some statements in the paper seem to contradict each other. For example:

1. "BaFT and ReFT used a subspace of the same rank, so its editing performance should be upper bounded by ReFT in this case," and
2. "BaFT was capable of maintaining a better editing-locality trade-off: it achieved better locality and portability than ReFT with no degradation of the editing effectiveness."

In my opinion, these two statements cannot both be true.

### Questions
1. Should anLM in line 187 be changed to an LM?

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
4

### Summary
This paper addresses the challenge of updating specific knowledge within Large Language Models (LLMs) while preserving other unrelated knowledge. Traditionally, methods have attempted to update only a small number of parameters in specific layers of LLMs, but these methods often fail to maintain the precision required for effective knowledge editing due to the inherent trade-off between editing and locality. The authors propose a novel approach called Basis-level Fine-Tuning (BaFT), which builds upon the Representation Fine-Tuning (ReFT) method. Theoretical analysis supports the introduction of BaFT, highlighting the limitations of linear representation fine-tuning and suggesting that a more precise method could improve both the specificity and locality of knowledge edits.  Instead of applying a uniform linear update across the subspace, BaFT computes a unique weight for each basis vector depending on the input representation. This allows BaFT to handle different types of knowledge adaptively, potentially resolving the inherent tension between editing performance and locality. The experiments on several models under different settings demonstrate the effectiveness of the proposed model.

### Strengths
1. The prposed method obtains great performance under different knowledge editing settings including the single，continual and batch editing.
2. The motivation is clear and reasonable and the experiments consider different kind of knowledge dataset which makes the evaluation strong.

### Weaknesses
1. There are some details missing from the main part and I have listed in the question part.
2. The proof for the failure in the ReFT is reasonable, but why the loss used in RaFT can alleviate the problem is not clear. A proof here can make the method and theory complete and robust.
3. I agree that editing the knowledge in a single space would lead to the general-loc trade-off, but I think the assumption about the ball in is a bit subjective, it would be better to provide more related work here.
4. Some typos: L187, missing blank ‘anLM’.

### Questions
1. Some details of the method are not clear and I'm wondering when conducting ReFT or BaFT, how to decide the position for the fine-tuning? Is it the same position for different knowledge? In addition, is the experiment conducted on all layers of the specific LLM? This may be the basic information in ReFT, but for readers, it's a bit confusing.
2. I agree that editing the knowledge in a single space would lead to the general-loc trade-off, but I think the assumption about the ball in is a bit subjective, it would be better to provide more related work here.
3. Some typos: L187, missing blank ‘anLM’.

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
This paper presents BaFT, a method designed to improve knowledge editing in large language models by fine-tuning representations instead of model parameters. Unlike traditional parameter-based approaches, BaFT performs selective edits at the basis level within a learned subspace, using an input-dependent weighting mechanism. This enables precise updates to targeted knowledge while preserving unrelated knowledge. Experimental results demonstrate that BaFT excels across multiple benchmarks in single, continual, and batched editing tasks, achieving efficient knowledge updates with fewer parameters. BaFT shows strong potential for effective, dynamic knowledge editing in real-world applications.

### Strengths
1.This paper introduces BaFT, which performs updates at the basis-vector level within a representation subspace, rather than relying on traditional parameter-based updates.

2.The paper provides substantial theoretical and empirical support for BaFT. The theoretical section thoroughly analyzes the limitations of existing linear update methods, offering a solid rationale for BaFT’s nonlinear representation fine-tuning approach.

3.BaFT offers a more efficient solution for knowledge editing in large language models, especially valuable in applications that require frequent knowledge updates.

### Weaknesses
1.Although the article presents the BaFT method and demonstrates its advantages in knowledge editing, the analysis of its limitations and potential flaws is relatively sparse. Specifically, the paper does not thoroughly discuss the sensitivity of BaFT to hyperparameter choices, such as the selection of layers and the rank of the subspace used for editing. Furthermore, the method's computational overhead, particularly in scenarios with very large models, is not sufficiently explored.

2.The experiments in the article primarily focus on a few specific benchmark datasets, which may not comprehensively reflect the performance of BaFT in various real-world applications. The lack of experiments on more diverse and challenging datasets, including those with unstructured data or those requiring more complex reasoning, limits the generalizability of the findings. Additionally, the paper does not adequately address the potential for negative transfer when applying BaFT to different types of knowledge or tasks.

3.The paper asserts that it is the first work to explore an alternative selective representation-based update for knowledge editing. However, to my knowledge, REMEDI, as an established editing method, has already conducted preliminary investigations in this area.

4.Assumption 2.2 has been proposed in GRACE, authors should cite it.

5.Almost editing methods have examined the ‘locality’ of these methods to downstream tasks. I recommend that the authors incorporate an evaluation of downstream tasks in the paper to ensure the reliability of the proposed editing methods.

6.In the experimental section, I have concerns regarding the validity of the baseline evaluation methods. The authors did not specify the evaluation framework or the parameter choices employed. If the authors utilized the EasyEdit framework to evaluate ROME and MEMIT, I suggest a unified re-evaluation of the baseline methods, as the EasyEdit evaluation framework has known mistakes.

7.In the context of continual(sequential) editing, BAFT exhibits slightly inferior performance compared to WISE, which is achieved at the cost of faster training and inference speeds. How should the trade-off between these two aspects be effectively balanced?

8.As an update representation for achieving editing, I believe this is not a reliable knowledge editing method compared to directly updating parameters.

9.There are several expression issues in the paper, such as "anLLM"; however, this did not influence my overall score.

### Questions
1.The paper asserts that it is the first work to explore an alternative selective representation-based update for knowledge editing. However, to my knowledge, REMEDI[1], as an established editing method, has already conducted preliminary investigations in this area.

2.Assumption 2.2 has been proposed in GRACE[2]，authors should cite it.

3.Almost editing methods have examined the ‘locality’ of these methods to downstream tasks. I recommend that the authors incorporate an evaluation of downstream tasks in the paper to ensure the reliability of the proposed editing methods.

4.In the experimental section, I have concerns regarding the validity of the baseline evaluation methods. The authors did not specify the evaluation framework or the parameter choices employed. If the authors utilized the EasyEdit[3] framework to evaluate ROME and MEMIT, I suggest a unified re-evaluation of the baseline methods, as the EasyEdit evaluation framework has known mistakes.

5.In the context of continual(sequential) editing, BAFT exhibits slightly inferior performance compared to WISE, which is achieved at the cost of faster training and inference speeds. How should the trade-off between these two aspects be effectively balanced?

6.As an update representation for achieving editing, I believe this is not a reliable knowledge editing method compared to directly updating parameters.

7.There are several expression issues in the paper, such as "anLLM"; however, this did not influence my overall score.

[1].https://github.com/evandez/REMEDI

[2].https://arxiv.org/abs/2211.11031

[3].https://github.com/zjunlp/EasyEdit?tab=readme-ov-file

### Soundness
2

### Presentation
3

### Contribution
2
