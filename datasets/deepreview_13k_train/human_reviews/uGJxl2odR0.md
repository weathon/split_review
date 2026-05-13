# Dimension Agnostic Neural Processes

- Decision: Accept
- Scores: 8, 6, 6, 3, 6

## Abstract
Meta-learning aims to train models that can generalize to new tasks with limited labeled data by extracting shared features across diverse task datasets. Additionally, it accounts for prediction uncertainty during both training and evaluation, a concept known as uncertainty-aware meta-learning. Neural Process (NP) is a well-known uncertainty-aware meta-learning method that constructs implicit stochastic processes using parametric neural networks, enabling rapid adaptation to new tasks. However, existing NP methods face challenges in accommodating diverse input dimensions and learned features, limiting their broad applicability across regression tasks. To address these limitations and advance the utility of NP models as general regressors, we introduce Dimension Agnostic Neural Process (DANP). DANP incorporates Dimension Aggregator Block (DAB) to transform input features into a fixed-dimensional space, enhancing the model's ability to handle diverse datasets. Furthermore, leveraging the Transformer architecture and latent encoding layers, DANP learns a wider range of features that are generalizable across various tasks. Through comprehensive experimentation on various synthetic and practical regression tasks, we empirically show that DANP outperforms previous NP variations, showcasing its effectiveness in overcoming the limitations of traditional NP models and its potential for broader applicability in diverse regression scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce Dimension Agnostic Neural Process (DANP) that incorporates Dimension Aggregator Block (DAB) to transform input features into a fixed-dimensional space, in an attempt to enhance the model's ability to handle diverse datasets. Leveraging a transformer architecture and latent encoding layers, the proposed approach learns a wide range of features, generalizable across various tasks. 

To evaluate the approach the authors present a comprehensive evaluation, including synthetic and practical regression tasks. The empirical results, consisting of comparisons with exiting state-of-the-art methods and ablations show that the effectiveness of the proposed approach.  The authors outperforms past existing Neural Process methods, demonstrating advantages and improvements on GP regression, Image and Video Completion and Bayesian Optimization tasks.

### Strengths
Originality 
 - The paper seem it has an evident level of novelty, tackling the diverse input and output dimensions challenge in the uncertainty aware meta-learning methods such as neural processes. Two novelties seems to be the case here, the dimension aggregation block and the latent path, in a transformer-like arhitecture.

Quality
- The paper is well motivated, structured and presented, the problem is well introduces and connected to existing work. The writing is good. There is extensive and diverse evaluation over synthetic and publicly available data sets for the GP regression, Image and Video Completion, and Bayesian Optimization tasks. The Ablation study is also useful.

Clarity
- The proposed approach is nicely presented and explained.

Significance
- The approach shows effectiveness of such methods under evaluated dataset and seems to hold potential for applicability in diverse regression scenarios

### Weaknesses
Presentation of the tasks/problems that the method addresses
- The presentation is sufficiently clear. I find that more on the actual task considered here can help to appreciate more the significance and the benefits of this approach. In particular related how the GP regression and the image completion tasks benchmarks help to validate the broad applicability of the approach?

Evaluations
- Non consistent result and seem to be marginal improvements in the GP Regression (from-scratch case) and the image completion task.

### Questions
In Table 1, it seems that the proposed approach has only marginal advantage over the proposed methods, in the GP Regression in the from-scratch case. Since, I'm able to see and it appears that between TNP and DANP (proposed approach) across 1D RBF, 1D Matern, 2D RBF and 2D Matern at the target column the only difference (improvement) is at the second (third) decimal. 

What is the reason for that?

I would have expected higher improvement (e.g. on the first decimal). I'm not sure I can consider this to be statistically significant. Can I ask also whether confidence intervals are available and would it be possible to share them?  

Similar performance is for the image completion task.

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
This paper introduces a new model, Dimension Agnostic Neural Process (DANP), which addresses the limitations of current Neural Processes (NP) in handling inputs with varying dimensions. DANP includes a Dimension Aggregator Block (DAB) that converts input features into a fixed-dimensional space, while also incorporating Transformer architecture and latent encoding layers to enhance adaptability across different tasks. Experimental results show that DANP performs well on multiple regression tasks, highlighting its potential as a versatile, general-purpose regressor.

### Strengths
1. Introduces the DAB module, enabling the model to handle inputs and outputs of varying dimensions, adding flexibility.
2. Covers multiple tasks and scenarios, demonstrating the model's stability across different conditions.
3. Performs well in regression, hyperparameter tuning, and other tasks, showing promise for broad applications.

### Weaknesses
1. Model Complexity. The design is complex, making replication and understanding challenging. 
2. Lacks Analysis of Computational Costs. There’s no discussion of the model's time and resource requirements, impacting assessments for practical use.
3. Limited Application Scope. Primarily validated on regression tasks, with little exploration of classification or other tasks.

### Questions
I mainly have concerns about the practical aspects of this work. It would be helpful if the authors could provide more concrete examples and relate them to more complex, real-world applications.

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
2

### Summary
This work introduces a novel approach to meta-learning, specifically addressing the challenges of accommodating diverse input dimensions and learned features in Neural Process (NP) methods. 
- The authors propose the Dimension Agnostic Neural Process (DANP), which incorporates a Dimension Aggregator Block (DAB) to transform input features into a fixed-dimensional space, enhancing the model's ability to handle varied datasets. 
- By leveraging the Transformer architecture and latent encoding layers, DANP is capable of learning a broader range of features that are generalizable across different tasks. 
- Through extensive experimentation on various synthetic and practical regression tasks, the authors demonstrate that DANP outperforms previous NP variations, effectively overcoming the limitations of traditional NP models and showcasing its potential for broader applicability in diverse regression scenarios.

### Strengths
- DANP is a novel extension of NP, that addresses the limitations of existing NP methods in handling diverse input dimensions and learned features.
- This work not only points out the shortcomings of current NP methods but also proposes a robust solution through the DAB and the integration of Transformer architecture.
- The paper is clear in its structure and presentation.

### Weaknesses
 - The paper focuses on regression tasks, but its applicability to other tasks such as classification is not thoroughly explored. It could benefit from additional experiments or a theoretical discussion on how DANP might perform in non-regression tasks.
- While DANP shows promising results, the paper lacks a detailed discussion on the model's interpretability. The paper should include an analysis or discussion on how the components of DANP contribute to its predictions, especially given its complex architecture involving the DAB and Transformer-based latent path.

### Questions
- How does the authors' proposed DANP model perform in tasks outside of regression, such as classification or time-series forecasting? Are there any modifications needed for effective application in these domains?
- Are there any plans to conduct longitudinal studies to evaluate the long-term performance and stability of DANP in dynamic environments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper works on neural processes and studies the case when there exist diverse input dimensions and learned features. Tot this end, the Dimension Agnostic Block (DANP) is developed to transform input features into a fixed embedding and then combined with neural process modules. It conducts experiments in zero-shot and few-shot scenarios.

### Strengths
I can easily follow this work and the layout is clear. However, there are severe writing and examination issues.

### Weaknesses
(1) Overall, this work includes several engineering tricks to handle diverse input dimension cases and lacks theoretical analysis to examine the proposal. 

(2) It seems the motivation of this work also considers the uncertainty, however, I did not see sufficient results to illustrate this part when the dimension of the output is high.

(3) In the related work [1], it has been demonstrated the Eq. (19) is not a valid ELBO. Hence, Line 266-269 should be revised. In line279, I disagree that NP is the earliest to address uncertainty as CNP can also achieve this in experiments. It seems several related works [2-9] are not discussed in the literature.

(4) In line 316 and the following experiments, I am afraid that the zero-shot and finetune scenarios are not appropriate in evaluation as NP families require the context and amortize the few-shot adaptation without gradient updates. I am not convinced by the meaning of fine-tune or zero-shot in the task concept.

(5) The computational complexity towards the modules and other ablations are required in examining the performance. Meanwhile it seems a lot of results in the context are nearly the same in scales in Table2-3. Details about the number of shots are missing in experiments, further weakening the results.

### Questions
See the above

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper describes the existing challenges of Neural Processes (NP) when using a variable number of input dimensions and learned features. The authors proposed to tackle this problem by extending the Transformer Neural Process architecture with a Dimension Aggregator Block, using Positional Embeddings to take into account the different input dimensions before transforming the features into a fixed dimensional space. The paper tests the performance of the proposed method on zero-shot and fine-tuning settings using synthetic regression tasks and image completion datasets well-known in the NP literature.

### Strengths
- The paper has a good and concise summary of the Neural Processes setting and it highlights clearly the problem of fixed dimensions, as opposed to variable ones.
- The authors submitted the source-code to reproduce their experiments, which is a neat way to connect the ideas exposed on the main body with practical details of the implementation. Great work here.
- The idea of leveraging positional embeddings on the dimensions axis is I believe novel, and interesting on itself.

### Weaknesses
Post rebuttal: The authors have addressed many of the weaknesses I've listed below, added new ablations that show case the limitations of extrapolation and RoPE vs Positional Ebeddings among others. Hence I've increased my score. Reviewer utkY still has some methodological and novelty concerns, which I think are valid points, but I still think the empirical value of this work is enough to be accepted. Thanks to the authors for engaging on the rebuttal process.

**Limitations of positional embeddings on the proposed DAB module:**

Positional Embeddings is a well-studied part of the transformer architecture, specially in Language Models. Generally speaking, while there has been progress since the original Transformer, the community agrees that length extrapolation is an open-problem and positional embeddings do not extrapolate on further sequence lengths, see [1] for example, where the sinusoidal embeddings used by DAB are the worst in extrapolation. In LLMs (arguably the biggest current application of transformers and positional embeddings) the community has largely moved on from Sinusoidal embeddings and into other approaches such as RoPE [2] [3]. Thereby, while the setting here is very different I see the following weaknesses with the current paper given that positional embeddings is a crucial part for the DAB module to be dimension-agnostic:

- Concretely, Positional Embeddings have a hard time in transformers when extrapolating from small to large context lengths. This warrants a discussion on whether they’re applicable to the setting on this paper.
- There has been a substantial amount of work on newer and better positional embeddings, I believe this warrants at least a discussion and acknowledgement of recent work, and a stronger argument for using Sinusoidal Embeddings.
- At best this warrants an ablation which justifies the choice in the architecture.
- I believe highlighting the failure modes of using Positional Embeddings (sinusoidal or otherwise) do not diminish the contributions of the paper, quite on the contrary. But in my view, it’s important to highlight the limitations of the proposed approach, and if there’s evidence that these failure modes do not exist on the setting exposed here, it makes even an stronger paper.

**Experimental weaknesses (dimension generalisation):**

Connecting to the previous section, I believe that the experiments need to be more robust to analyse more carefully the failure modes of the proposed approach. In some cases, this is already in the appendix, but unfortunately this is not properly referenced from the main body. I urge the authors to present the failure modes of the approach in the main body more clearly, and when pushing results to the appendix, to reference them from the main body **explicitly,** calling out from the main body what are the strengths or weaknesses of the appendix results.

- On the 0-shot scenario of GP regression (section 5.1), the model is either trained on {2,4} or {2,3,4} dimensions and evaluated on {1,2,3,4,5,7}. Given the above discussion about positional embeddings, I think that this setting benefits evaluating on dimensions {1,3} since they’re covered by interpolation. A better experimental setting would involve fully non-overlapping dimensions in train and validation, such as {1,2,3} and {4,5,6}. Even better, would be to try different configurations and report the threshold where the performance breaks down or when the performance is better. I hypothesise this model is better when it is evaluated during interpolation. At the very least, there should be an open discussion about this in the paper; however, as this is core to the contribution of this work, I believe it’s important to address these experimental weaknesses. Some of this is already in Appendix B.2 and in Table 16, however it is not clear if the kernels are the same (names are present in table 16 but not in table 2a); irrespective of this, given the arguments above, I strongly believe this discussion on the limitation of the approach belongs to the main body and should be **clearly stated on the conclusions** **and contributions sections** since it paints a full picture of the failure modes. The whole appendix B is barely referenced (it’s very big with very different subsections), and it’s very easy to miss the discussion of table 16.
- For the fine-tuning section of GP regression, I have similar concerns. In the positional embedding LLMS literature, typically what you do to extend to longer contexts is to finetune on context lengths which are larger. Here, however, the finetuning happens on 1-dimensional tasks, after being pretrained on 2,3,4. Again, a likely failure mode is that when fine tuning on dimensions which are bigger than in pretraining the model won’t extrapolate very well. Unfortunately, as opposed to the zero-shot section, the appendix does not have experiments which reflect this setting.

**Experimental weaknesses (practical regression tasks)**

- While I understand the engineering challenges of video datasets, I believe the authors should tone down section 5.2. The proposed adaptation of CelebA does not make it a Video dataset — hence I believe it’s wrong to call this a Video Completion task, I suggest this is rephrased throughout the paper to reflect that this is just an image completion task with a synthetically generated extra dimension. Alternatively, it’d be really interesting to test this on an actual short video dataset, such as [4], however I understand this can be fully out of scope. Perhaps it’s useful to reference it as future work.
- I believe the extra dimension added to CelebA is a rather weak task, since it’s a very simple subtraction over the brightness. I wonder if using off-the-shelf dimensions such as CelebA landmarks [5] [6] would be a better task (there are 5 different landmarks locations for each face, tagged as 2d coordinates). This has the benefit of being an already established benchmark in the literature, and arguably a more real-world and practical regression task. If the proposed method does not work well on these harder tasks, it’s still interesting to highlight the limitations of the model.
- The core results of section 5.2 rely on pre-training on both the CelebA and EMNIST datasets, while interesting to see some positive transfer, after reading the framing of the paper and the GP regression section, I would have expected some zero-shot results on image tasks (for both pretraining and validation), which arguably is more relevant to meta-learning than fine-tuning. A Video Completion experiment in a zero-shot setting would make a stronger contribution, which is more consistent with the GP regressions section.

**Experimental weaknesses (other)**

- The log-likelihood is likely an incomplete picture of the results. As done in [7] I believe a stronger analysis should include other metrics such as calibration error.
- The context provided about confidence interval coverage is worth mentioning on the main body, instead of being in the appendix where it’s hardly accessible and referenced directly from the main body.
- In general, Appendix B is too broad and many interesting conclusions that should be in the main body are there without a direct reference.
- In my opinion, the details that have been mentioned to be in the appendix, deserve to be in the main body to have a better complete picture of the strengths and limitations of the proposed approach. While I understand the page-limit is a limitation, I’d argue that what I have mentioned is of more relevance compared to the mostly positive results of section 5.4 — these can be in the appendix and mentioned briefly with a direct reference for interested readers. Another alternative is to leave the tables in the appendix but still mention the relevant conclusion in the main body.
- NDP is mentioned as a relevant baseline and briefly tried on Appendix B - Table 11/12. Since this is the most relevant baseline according to the authors, I believe results with this relevant baseline from prior work should be in the main body as much as possible (it’s clear that it’s only comparable with dimension-agnostic methods for x when y=1) with a discussion about the quantitative results, not just qualitative as in section 4. There’s clearly at least two settings where it’s possible to do this, but they’re in the appendix.

**Misc:**

- The Dimension Aggregator Block implementation uses a linear projection **with bias [8].** This renders equation 10 incorrect since the bias term is missing there. I believe this is a common blind spot because the bias is set by default to True in Pytorch, so I urge the authors to revise all linear layers and either update the manuscript or the code/results. Note that I do not expect this to change the results much, but it’s better to address this for reproducibility and clarity.
- Table 2a does not have the 2nd or 1st best performance marked with underline or boldfaced underline. This makes it harder to read.
- Table 2a does not state which kernels were used, as compared to table 1 and table 16.
- It’s hard to read table 1 and table 2 separately, and as the authors mentioned, it’s helpful to read them in context.
- While I appreciate the detail problem setting on section 2, if there are concerns of page limits, I’d suggest the authors to prioritise space for experimental results and discussion as suggested in the previous section — this can be either added as an Appendix and referenced directly from the main body, or just cite from previous work as appropriate.

### Questions
- In the 0-shot evaluation on GP regression (section 5.1), why is dimension 6 not included in the validation? It seems straightforward to do and would paint a complete picture. Can this experiment be included? If it’s a matter of space in the manuscript or computational resources, I believe dimension 6 is better than dimension 7.
- What are your thoughts on the inherent limitations of Positional Embeddings extrapolation? Is the lack of extrapolation a concern in the dimension-agnostic setting?
- Did you experiment with Zero-Shot on image tasks? Given that you had results for fine-tuning, I imagine it is possible to get zero-shot results, unless I’m missing something.

### Soundness
3

### Presentation
3

### Contribution
2
