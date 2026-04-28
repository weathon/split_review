# Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Synthetic data has been widely used to train large language models, but their generative nature inevitably introduces noisy, non-informative, and misleading learning signals. In this paper, we propose \textsc{Montessori-Instruct}, a novel data synthesis framework that tailors the data synthesis ability of the teacher language model toward the student language model's learning process. Specifically, we utilize local data influence of synthetic training data points on students to characterize students' learning preferences. Then, we train the teacher model with Direct Preference Optimization (DPO) to generate synthetic data tailored toward student learning preferences. Experiments with Llama3-8B-Instruct (teacher) and Llama3-8B (student) on Alpaca Eval and MT-Bench demonstrate that Montessori-Instruct significantly outperforms standard synthesis methods by 18.35\% and 46.24\% relatively. Our method also beats data synthesized by a stronger teacher model, GPT-4o. Further analysis confirms the benefits of teacher's learning to generate more influential training data in the student's improved learning, the advantages of local data influence in accurately measuring student preferences, and the robustness of Montessori-Instruct across different student models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Montessori-Instruct, a new framework for generating synthetic training data to enhance the learning of student language models. The authors propose a method that aligns data synthesis by a teacher model (e.g., Llama3-8B-Instruct) with the learning process of the student model (e.g., Llama3-8B). The approach involves assessing the local data influence of synthetic data points on the student model to understand its learning preferences, followed by training the teacher model using Direct Preference Optimization (DPO) to generate data better suited for the student. Experiments show that Montessori-Instruct significantly improves performance on benchmarks like Alpaca Eval and MT-Bench.

### Strengths
* The concept of aligning the teacher model to better match the student model’s learning preferences is well-motivated.

* The method of assessing the impact of individual data points on student learning (i.e., local data influence) is a interesting approach backed by theoretical guarantees.

### Weaknesses
 * Including experiments with multiple runs and reporting the mean and standard deviation would strengthen the reliability of the results.

* The performance gains, particularly on out-of-domain benchmarks, appear minimal when weighed against the additional computational cost involved in training the teacher model.

* The idea of local data influence, which is the crucial algorithm for the proposed solution, is not new but taken from a previous paper, as the authors have mentioned. This reliance on existing techniques may reduce the perceived originality of the paper.

### Questions
See weaknesses above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a customized synthetic data generation pipeline that seeks to improve the expert model towards generating more useful and debiased data for the student model by aligning the expert model towards data distribution with higher influences on the student model via DPO. Specifically, this paper (1) first adopts an established influence function in active learning to measure the utility of a single data point in the probing set, (2) then they construct preference data using the positive and negative data influences sampled from a same prompt, and use this data to align the expert model. Finally, they regenerate data from the updated expert model and finetune the student model with this data. While the method proposed in this paper generally make sense, it suffers from a lack of ablation study and analysis on the additional cost (e.g. manual curation cost of the reference set, per sample influence inference cost, training cost of DPO on expert model) incurred by this data selection process.

### Strengths
This paper proposes a synthetic data generation pipeline to customizedly align the expert model towards higher data utility over the student model. Specifically, 
+ the method proposed is sound and can intuitively address the OOD issue with the synthetic data to enhance the generalizability of the student model.
+ this paper has good presentations and conveys the idea clearly.

### Weaknesses
The paper lacks more informative ablation study and in-depth explanation and analysis, especially,
+ How do the authors pick the reference dataset and determine its size? It seems this dataset is critical to judge the influence of the data samples on the student model and highly determine the performance of the fine-tuned student model later. 
+ Can the author provide some ablation study on the size of the reference dataset and its selection method?
+ How many samples do the authors obtain for each prompt in order to get a pair of positive and negative instruction? What are the additional costs behind these?
+ Calculating the inference for each data point in the probing set seems a bit costly as it involves an LLM optimization (even if just one step). Can the authors provide an ablation study on the sample size of the probing set and the final performance?
+ It also introduces some other additional costs as the proposed method involves DPO on the expert model, while most of the baselines do not. As the expert model is large in size, this training cost seems also non-negligible.

### Questions
See the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Montessori-Instruct, a novel framework that optimizes the teacher model's data generation capabilities by aligning them with student learning preferences. The framework uses local data influence measurements to estimate how synthetic data impacts student learning, then employs DPO to tune the teacher model accordingly. Experiments with Llama-3 and TinyLlama models showed significant improvements over baseline methods.

### Strengths
- A novel data influence-driven approach where the teacher model actively learns to generate training data by optimizing against student's learning preferences, in contrast to previous works that use a static teacher.
- The experimental comparisons and benchmarks are comprehensive, the proposed method shows significant improvements, and the ablation and analysis experiments are thorough.

### Weaknesses
The main drawback of this work is the excessive computational overhead beyond the objective of training the student model. Although the authors discussed this additional computation in detail in Section 6 and Appendix E, I believe that the impact on the paper's practicality cannot be dismissed through discussion alone. The majority of the additional computational cost comes from local data influence for the student, where one step of training is required for each sample, along with evaluation on the reference dataset. To accelerate this process, the authors used 8xH100, which is a very expensive overhead. This makes me question whether we could actually achieve similar gains by investing these resources in using stronger teacher models and building more sophisticated reward model pipelines[1]. I encourage the authors to (1) discuss potential directions that could directly reduce the unit cost of local data influence, rather than encouraging more computational resources, thereby enhancing the promise of local data influence-based approaches. (2) present the additional monetary costs for each method (i.e., APIs used for baseline methods and computational resources used for acceleration) to improve the fairness and transparency of the comparison.

### Questions
- In lines 226-228, how were the 6,792 preference pairs collected from the 10K probing dataset?
- Will the general capabilities of the optimized teacher model deteriorate?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MONTESSORI-INSTRUCT, a framework to generate synthetic data for training student language models - tailored for the student model's learing process / ability. The method first uses local data influence to measure the utility of synthetic data points for student learning. Then, it optimizes a teacher model with DPO to generate more effective synthetic training data by aligning with the student model's learning preferences. 

The authors evaluate MONTESSORI-INSTRUCT using `Llama3-8B-Instruct` as the teacher and `Llama3-8B/Tinyllama-1`.1B as students. Evaluation on Alpaca Eval and MT-Bench shows that Montessori-Instruct outperforms existing methods like Self-Instruct. The authors also show that Montessori-Instruct can beat GPT-4o on in-domain and out-of-domain evaluation. Ablation studies highlight the effectiveness of using data influence to capture student preferences, the benefits of optimizing teacher parameters, and the robustness across different configurations.

### Strengths
**Writing**. 
- Introduction is well-written. The motivation is clear, the problem is well-defined, key contributions are listed and aligned with the structure of the paper.
- Related work is well-written, extensive, and up-to-date. Related works is also well-organized in logic, and set up a good foundation between existing line of works and the proposed method.

**Evaluation**.
- Evaluation has good coverage of different baselines, and the selection of baselines are realistic. Generally, the evaluation is comprehensive and thorough.
- Ablation study is comprehensive and thorough. The ablation studies the effectiveness of teacher optimization, seed data, (multiple) iterations, and very clearly demonstrates the generalizability of the method.

**Originality**. The idea of the paper is novel, and well-motivated. 

**Significance**. The proposed method is a good contribution to the field of synthetic data generation for language model training. The proposed method is generalizable to other domains, though with additional overhead as stated in the limitation section.

### Weaknesses
 **Scale of experiment.** The limitation section points out that in the experiment, the scale is chosen as a fixed 10k data points. Ablation on the scale of experiment will be helpful to show the generalizability of the method on the scale of data.

### Questions
1. Is there an easy way to see how the effectiveness of the framework scales with the data? You are welcome to scale down / scale up, to a point where the experiment is reasonable.

### Soundness
3

### Presentation
3

### Contribution
3
