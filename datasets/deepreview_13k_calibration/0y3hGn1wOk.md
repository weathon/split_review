# Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset

- Decision: Accept
- Avg Score: 5.40
- Scores: 6, 5, 6, 5, 5

## Abstract
Machine unlearning has emerged as an effective strategy for forgetting specific information in the training data. However, with the increasing integration of visual data, privacy concerns in Vision Language Models (VLMs) remain underexplored. To address this, we introduce Facial Identity Unlearning Benchmark (FIUBench), a novel VLM unlearning benchmark designed to robustly evaluate the effectiveness of unlearning algorithms under the Right to be Forgotten setting. Specifically, we formulate the VLM unlearning task via constructing the Fictitious Facial Identity VQA dataset and apply a two-stage evaluation pipeline that is designed to precisely control the sources of information and their exposure levels. In terms of evaluation, since VLM supports various forms of ways to ask questions with the same semantic meaning,  we also provide robust evaluation metrics including membership inference attacks and carefully designed adversarial privacy attacks to evaluate the performance of algorithms.  Through the evaluation of four baseline VLM unlearning algorithms within FIUBench, we find that all methods remain limited in their unlearning performance, with significant trade-offs between model utility and forget quality. Furthermore, our findings also highlight the importance of privacy attacks for robust evaluations. We hope FIUBench will drive progress in developing more effective VLM unlearning algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an unlearning benchmark for Vision Language Models (VLMs) under the Right to be Forgotten setting. After defining the VLM unlearning tasks, this benchmark assigns a two-stage evaluation pipeline with a newly proposed Fictitious Facial Identity VQA dataset. The proposed benchmark offers a comprehensive evaluation by computing both forget quality and model utility, with further assessment under membership inference attack and adversarial privacy extraction. Another contribution of the work is its evaluating four baseline unlearning algorithms, which indicates that none of them achieve good unlearning performance considering both model utility and forget quality. In addition, the divergent performance of Preference Optimization with and without membership inference attacks underscores the importance of privacy attacks for robust evaluations. This benchmark is good to foster the community’s further research on developing better unlearning methods for VLMs under the setting of Right to be Forgotten.

### Strengths
1. This paper addresses an important ethics problem of AI, i.e., to fulfill the right to be forgotten for VLM, which is underexplored relatively. To my understanding, few works have been done in the literature. 

2. The benchmark, together with the evaluation metrics, is validated, especially via the assessment of four baseline unlearning algorithms. The results imply that existing unlearning algorithms are far from being mature when considering both model utility and forget quality. 

3. The benchmark is good to foster the community’s further research on developing better unlearning methods for VLMs.

### Weaknesses
I am confused by the dataset constructed. As described in Line 165~172, 400 faces are sampled, which are then divided into 400 clusters by using K-means algorithm. How can 400 faces clustered into 400 clusters?

And, to me, a dataset with 400 faces is relatively small for evaluating the unlearning problem. I am also not convinced why only synthetic faces are used for this evaluation. Is there any difference between real faces and synthetic faces for this evaluation purpose?

### Questions
Please reply my concerns mentioned in the Weaknesses part.

### Soundness
3

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
4

### Summary
This paper introduces Facial Identity Unlearning Benchmark (FIUBENCH), a VLM unlearning benchmark designed to robustly evaluate the effectiveness of unlearning algorithms under the Right to be Forgotten setting. Moreover, FIUBENCH further incorporates membership inference attacks and adversarial privacy extraction to robustly evaluate unlearning performance, testing whether the private information is unlearned even under attacks.

### Strengths
1.	Unlike unlearning in LLMs, which primarily focuses on forgetting sensitive text information, unlearning in VLMs extends to both images and text. This paper formalizes VLM unlearning as the task of unlearning private image and text-paired information.
2.	To study privacy under the Right to be Forgotten scenario, a two-stage evaluation pipeline with Fictitious Facial Identity VQA dataset is proposed.

### Weaknesses
1.	This paper proposes FIUBENCH, a VLM unlearning benchmark designed to robustly evaluate the effectiveness of unlearning algorithms under the Right to be Forgotten setting, which is interesting. However, the effectiveness of this benchmark is unclear. Specifically, the benchmark's ability to truly simulate real-world unlearning scenarios, particularly concerning the distribution of the generated faces, needs further justification.
2.	Since the faces are generated by StyleGAN2, it is necessary to evaluate the distance between the generated face distribution and the real one. From the figure 1, the synthetic face images seem different from the real faces. Will it hurt the evaluations on the Vision Language models. The use of StyleGAN2 raises concerns about the authenticity of the generated faces and their impact on the evaluation of VLM unlearning. The visual discrepancies between synthetic and real faces could introduce biases, potentially leading to inaccurate assessments of unlearning performance.
3.	For the experiments, you’d better involve more Vision Language models for evaluations. The current evaluation lacks breadth, and it is crucial to assess the benchmark's effectiveness across a wider range of VLM architectures and sizes to ensure its generalizability.

### Questions
My major concerns lie in the effectiveness of the proposed benchmark and the experiments. If you can well address these problems, I am happy to improve my rating.

### Soundness
2

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
5

### Summary
This paper introduces FIUBENCH, a benchmark designed to evaluate unlearning algorithms for Vision Language Models (VLMs) under the Right to be Forgotten setting. FIUBENCH includes a Fictitious Facial Identity VQA dataset and a two-stage evaluation pipeline to control information exposure levels. To handle VLMs’ ability to process semantically similar queries, FIUBENCH incorporates robust evaluation metrics, including membership inference and adversarial privacy attacks. Initial results on four baseline algorithms show limitations in unlearning performance, with trade-offs between model utility and forget accuracy.

### Strengths
This paper systematically examines forgetting in Vision Language Models and introduces FIUBENCH, a new benchmark for robust evaluation of unlearning algorithms.
The paper is well-written and easy to understand.

### Weaknesses
The proposed benchmark uses a forget set and a retain set to assess the forgetting quality and model utility of unlearning algorithms. However, is this setting appropriate? In my view, the privacy concerns in Vision Language Models are more about forgetting specific sensitive information, such as identity or email, rather than simply forgetting individual samples. The current setup, which focuses on removing all information related to a small set of images, might not fully capture the nuances of real-world privacy risks where specific attributes or details need to be unlearned while preserving other aspects of the data.

The forget set is limited to 5% of the total dataset, comprising only 20 images. Could you explain the rationale behind selecting this specific proportion? How was this number determined? This small size raises concerns about the generalizability of the findings. It is unclear if the observed unlearning performance would hold with larger, more diverse forget sets, or if the small size of the forget set makes the unlearning task artificially easier. Furthermore, the paper does not explore the impact of varying the forget set composition, such as including images with similar semantic content or different levels of sensitivity.

### Questions
Please refer to the Strengths and Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This submission touches an important privacy-related topic in vision language model - the forgetting of specified content, e.g. unlearning. To evaluate the performance of unlearning, the authors construct a Facial Identity Unlearning Benchmark (FIUBENCH), with protocol and several methods as baseline. This is an interesting work. From the reviewer's point of view, this is still a preliminary work in considering of dataset size, and the methods of evaluation and face generation. However, it is worthwhile to continue to advance it to become a consensus for the community.

### Strengths
A novel dataset, Facial Identity Unlearning Benchmark (FIUBENCH) is constructed which can support the evaluation of the ‘Right to be Forgotten’ in Visual Language Model. Possible privacy risks are avoided through fictitious facial images. This submission is well written and easy to follow. The protocol provides settings to support different kinds of evaluations, including membership inference attack and adversarial privacy attack, etc.

### Weaknesses
The database size is too small to fit the task of evaluate the performance of unlearning in the wild. Although the fictitious facial images avoid the privacy risk, the synthetic images bring some flaws, such as artifacts in style, and these could become an unexpected feature for recognition. In addition the database has taken some action to ‘Filtering out similar faces with K-means’, which leads to an imposed environment for face recognition, and make the evaluation is far from real world case.

### Questions
As mentioned in weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper, based on the Right to be Forgotten setting, defines a VLM unlearning scenario that is closer to real-world use cases. The primary contributions are as follows:
1. Formalizing the VLM unlearning tasks. It emphasizes that VLM unlearning algorithms should focus on sensitive information linked to images rather than the visual attributes themselves.
2. Defining a two-stage evaluation pipeline with the Fictitious Facial Identity VQA dataset. In the first stage, personal information is injected into the VLM, and in the second stage, the unlearning algorithm is performed.
3. Providing various metrics for robust evaluation in terms of forget quality and model utility.

### Strengths
Based on the "Right to be Forgotten" setting, this paper defines a new VLM unlearning scenario closer to real-world use cases. 
The writing is clear.

### Weaknesses
1. The rationale behind the research motivation requires further substantiation (Q1).
2. Some experimental details are not clearly described or potentially contain errors. (Q2, Q3, Q6).
3. The analysis of the experimental results does not sufficiently consider the characteristics of unlearning algorithms, namely, the trade-off of model utility and forget quality for unlearning algorithms (Q4).
4. Some metrics appear to lack robustness when the VLM category changes (Q5).



### Questions
1. My first question is whether it is necessary to store individual private information within VLMs in real-world use cases. In practical applications, the best approach is to separate individual private information from the VLM and use retrieval-augmented generation (RAG) techniques to provide appropriate responses. Under such techniques, the Right to be Forgotten can be easily ensured by deleting individual private information from the relevant databases. The authors need to further elaborate on the motivation for their research.
2. In line 290, it is described that the score range for GPT-Eval is 0-1, but in Table 1 and Table 2, there are scores that exceed this range. This appears to be an error.
3. Line 366 mentions that “early stopping based on training loss” is employed. Are the results reported in Table 2 based on this early stopping setting? What criteria are used for early stopping? I would like to know more details.
4. Unlearning algorithms involve a trade-off between model utility and forget quality. It might be necessary to compare the forget quality scores at fixed model utility levels, or vice versa. Alternatively, plotting a Model Utility-Forget Quality curve could be more informative. In fact, in Figure 3, representing the effectiveness of the unlearning algorithm with a single point is also unreasonable; a Model Utility-Forget Quality curve would likely be a more appropriate choice.
5. On certain metrics, the VLM category significantly affects the model utility and forget quality of an unlearning algorithm. Why is this the case? Comparing the performance of the unlearning algorithm with the Retain Model reveals many such instances: (1) The difference between the Retain Model and GA for LLaVA-Phi-mini-3B is 42.4 (93.7 v.s. 50.6), whereas, for LLama-3.2-Vision-Instruct-11B, the difference is 84.5 (88.8 v.s. 4.30). (2) The difference between the Retain Model and KL for LLaVA-Phi-mini-3B is -29.8 (12.3 v.s. 42.1), whereas, for LLama-3.2-Vision-Instruct-11B, the difference is -1.5 (12.2 v.s. 13.7). The significant impact of the VLM category on certain metrics raises the question of whether these metrics can provide robust testing results. Please provide a more detailed discussion on this matter.
6. In line 464, it is stated that you "finally decided to fine-tune the parameters from LLM." However, from Table 3, it is evident that the MIA of $E_{x_3}$ is the highest among the four fine-tuning strategies. This choice seems to lack sufficient justification.

### Soundness
2

### Presentation
3

### Contribution
2
