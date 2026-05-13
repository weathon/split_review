# Optimizing Knowledge Distillation in Transformers: Enabling Power of Multi-Head Attention without Alignment Barriers

- Decision: Reject
- Scores: 5, 5, 5, 8

## Abstract
Knowledge distillation has been proven effective for compressing transformer architectures by transferring knowledge from teacher to student models. Logits-based methods of knowledge distillation cannot fully capture the intermediate representations and features within the teacher model, which may result in the student model not fully learning all the knowledge from the teacher model. Thus, previous work focuses on transferring knowledge through intermediate features or attention maps. However, leveraging multi-head attention maps in transformers for knowledge distillation presents challenges due to head misalignment and suboptimal feature alignment, often requiring projectors to align features or special modifications to the model architecture. To address above limitations, we propose the Squeezing-Heads Distillation (SHD) method. This method reduces the number of attention maps to any desired number through linear approximation, without requiring additional projectors or parameters. This facilitates better alignment and knowledge transfer between models with different numbers of heads, enhancing both flexibility and efficiency. Experimental results demonstrate significant improvements in both language and vision generative models, validating the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new feature-based knowledge distillation method, specially tailored to Transformers. Specifically, the method reduces the number of attention maps to any desired number through linear approximation, without requiring additional projectors or parameters. The experiments are conducted on both vision tasks and language tasks, validating the effectiveness of the method.

### Strengths
1. The method is straightforward and reasonable, which is easy to understand. 
2. The experiments are performed on both vision tasks and language tasks.

### Weaknesses
1. Fundamentally, the paper criticizes previous feature distillation methods because they often require projectors to align features (or special modifications to the model architecture), which introduce additional training costs. However, to the best of my knowledge, the prevalent of feature projectors (such as linear projectors, conv projectors, and MHA projectors) are rather lightweight, compared with the overhead of the teacher model and the student model.  The paper does not provide the FLOPs and training speed comparison between FD and SHD to show the necessity of designing SHD.

2. Furthermore, although the paper criticizes previous FD methods, it only compares with the most basic FD (with the basic linear projector) in the ablation study. The paper should cover the performance comparisons with various Top FD methods to enhance this claim.

3. In these experiments, it seems that SHD must be applied with logit-based methods and the improvement seems rather limited.  I wish to see the results that SHD independently applied to the network pair.


3. Although SHD does not have special designs for generative tasks,  all experiments are performed on image-generative tasks and text-generative tasks. I wish to see more results on image classification tasks, which are feasible to make comparisons with various Top FD methods.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines knowledge distillation in transformer architectures. Based on three observations in transformer attention maps, the proposed method investigates attention compression through linear approximation, using the squeezed attention maps for knowledge transfer between teacher and student models. Experiments are conducted on image generation and language model training tasks to demonstrate the effectiveness of the approach.

### Strengths
- This paper addresses a critical challenge in the era of large language models (LLMs): compressing transformer models using knowledge distillation techniques.

- The proposed method is easy-to-follow.

### Weaknesses
 - Observations on transformer attention maps lack clarity and sufficient justification. For instance, the statement that “the number of heads is redundant to some degree” is not well-supported.

- The experiments do not adequately demonstrate the effectiveness of the proposed method. Key baseline and comparison methods are missing, which makes it difficult to evaluate the method’s impact on improving knowledge distillation in transformer architectures.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work investigates the knowledge distillation specially tailored for transformer architectures. Specifically, the authors study the misalignment of attention heads between the teacher and student. They propose the squeezing-head module to compress multiple attention heads into single one, alleviating the mismatch of attention heads between different architectures. More specifically, the authors formulate the attention heads as a convex hull and aim to seek a substitute with minimal reconstruction error. Experiments on image generation and natural language processing show effectiveness.

### Strengths
1. The motivation is important to KD in transformer architectures. Due to computation budget, different models vary from depth to width. This work proposes to address the problem of misalignment of attention heads between teacher model and student model without learnable projectors.
2. The experiments are thorough. The authors show competitive results of their method on various tasks and dataset.

### Weaknesses
1. I have some concerns about the formulation starting from line 258. The authors formulate the *random convex hull* among multiple attention heads (*vertices*) and aim to find a substitute with minimal reconstruction error through **convex combination**. The problem is that no evidence reveals and supports the linearity (Eq. 5, line 266)  between two attention maps. In other words, it is less meaningful if we use the linear combination of two attention maps to approximate the other attention map. The core issue is that attention maps are complex, high-dimensional objects, and a simple linear combination may not capture the intricate relationships between different heads. This approach assumes that the information encoded in different attention heads can be meaningfully combined through a weighted average, which is a strong assumption that lacks theoretical justification. Specifically, the attention mechanism learns non-linear relationships between input tokens, and these relationships are unlikely to be preserved through a linear combination of attention maps. It is unclear why a linear combination would be a suitable approximation for the complex interactions captured by different attention heads. As an alternative, I think PCA, optimal transport, and kernel method can be the better tools.
2. It seems like Eq. 9 (line 291) does not guarantee global minimum. 
3. The experiments mainly focus on the heterogeneous architecture where two models have different attention heads. I wonder about the result of homogeneous architectures.

### Questions
1. If teacher and student has the same attention heads, can this approach consistently beats existing KD methods?
2. In addition to efficiency and well alignment, one advantage of multi-head attention over single-head attention is their descriptive power. How is Figure 1 after you combine multi-head into single head?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a new method which tries to solve the issue of head misalignment in multi-head attention mechanism for knowledge distillation. The main idea of the paper is to compress multiple attention heads into a single one, and distill this knowledge. The authors show  experimental results in image generation, (small) LLM pretraining and finetuning, outperforming several other methods. Furthermore, they present an excellent collection of ablation studies, in regards to relation with other distillation models, main hyperparameters, alternatives to their method and the loss function.

### Strengths
The paper has the following strengths:

1) Motivation - the paper is naturally well-motivated, starting with some clear observations: i) the head redundancy in Transformers; ii) alignment missmatch where teacher and student have different dimensions (which they almost always do); 3) attention matrices being rank deficient. While all of these have been observed in the past, it is still a good way of formalizing them and then giving the solution by proposing the attention head compression using the linear optimization method (section 4.2).

2) The method provided here to merge the attention heads is elegant, mathematically justified, and to me makes sense. Its derivations is also quite complete and just.

3) The method is shown to improve over standard knowledge distillation models in different settings: Image generation, small LLM pretraining, and small LLM finetuning. The results in all cases are quite significant, convincingly outperform the baseline and in some cases are (almost) as good as the much larger teacher.

4) The ablation study at the end of the paper is excellent, showing the robustness of the method under different hyperparameter settings, comparison with other methods (hard selection, constant merging of heads) and comparing the KD loss with MSE.

### Weaknesses
I think the paper has some room for improvement:

1) While the paper explains how 2 attention heads can be merged, the paper mentions that multiple attention heads can be merged. That part is quite unclear to me and would be nice if the authors can clarify the following points:

a) How this is done, is it simply merging each pair of attention heads, thus reducing them by half, or if there is some iterative procedure.

b) If there is some iterative procedure, how this is done in the first place, is it done for several heads alltogether on in pairs. If for several heads, how does the procedure in 4.2 is extended, and furthermore do the alphas need to sum up to 1?

c) How are the heads to be selected chosen in the first place?

2) The size misalignment where the teacher has larger hidden dimensions than the student, is a real issue. Simply projecting the features of the teacher to smaller dimensions, or those of students to larger dimensions, usually destroys information making the KD process not work. However, there are some remedies of this that completely mitigate this issue, for example by using orthogonal projections, as the following paper, making the standard KD techniques work.

[A] Miles et al., VkD: Improving Knowledge Distillation using Orthogonal Projections, CVPR 2024.

While this paper and [A] target the problem quite differently, the motivations are quite similar, so it would be interesting if the paper can be discussed and compared with under some setting (image generation being the closest setting in them).

3) All the results are shown in generative tasks. It would be interesting to see if the method works in discriminative tasks (e.g., image classification and/or object detection), showing the method to be more general.

4) All the NLP results are shown in relatively small LLMs. It would be interesting to see if the method scales well to larger real-world LLMs. From my experience, this is always not the case, and what works in 'small' (tens to hundreds of millions of weights) does not neccesarily work in 'large' language models (billions of weights). If possible, it would be interesting to see how the method works when distilling the knowledge in LLama models. The ideal case would be Llama 13B -> Llama 7B, if that is not possible then something like Llama 7B -> TinyLlama 1.1B. Would be fine to use different alternatives to Llama (Mistral, Qwen-2), but it would be nice if they are a) relatively modern, b) relatively large.

5) Missing citation. The observation in equation 3 and 4, the idea that value-output multiplication can be considered as a single circuit (similar to query-key) has been done before, and it would be nice for the authors to cite it.

[B] Elhage et al., A Mathematical Framework for Transformer Circuits, Anthropic 2021, https://transformer-circuits.pub/2021/framework/index.html

6) Some clarification in Figure 1 is needed. If the results are from a single example, then that is very obviously expected. Of course that most attention heads are not going to produce anything meaningful (get 'activated'), that is by design. If not:

a) How did the authors choose the example?

b) Wouldn't it be better to check lots of inference examples, and merge the results?

7) Some writing issues:

a) Please rewrite the contributions in active instead of passive.

b) Figure 1 cannot be well read, and cannot be read at all if it is in printed paper. The authors should redesign it so it is more readable (probably by making it larger)

c) It is unclear to me what precision and recall means in the context of image generation (Table 1).

### Questions
I have already included several questions in the weaknesses. In particular:

1) The authors should ideally clarify the questions under weakness (1) and (6)

2) The authors should give credit to papers [A] and [B] and ideally compare with paper [A] under some setting.

3) If possible, the authors should compare their method on other settings: a) discriminative tasks; b) larger LLMs.

I am initially positive, the paper makes sense, seems to work in different settings, and reach good results. Thus, I am scoring it initially as (6) Borderline accept. However, I acknowledge that the paper has some issues with clarity, more comparisons, writing, and putting it in context of other works. Providing that the authors would well-address the mentioned issues, I will switch to (8) Accept.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After rebuttal:

I thank the authors for their excellent and detailed rebuttal.

1) I expressed some confusion about the merging process. The authors have adequately addressed this and provided additional results.

2) I mentioned VkD as missing reference and a recent paper that addresses a similar problem. The author have integrated the comparison with it in the manuscript, showing that their method outperforms VkD.

3) I mentioned lack of discriminative tasks. The authors have compared their method with other methods in a discriminative benchmark, showing that it outperforms the other methods.

4) I mentioned lack of experiments in real LLMs. The authors have shown an additional experiments in LLama13B-LLama7B setting.

5-6-7) The authors have adequately addressed my concerns about clarify, missing citation and metrics.

I was initially positive about the paper. After the rebuttal, the authors have adequately addressed all of my concerns, and have provided results that further improve the paper. Furthermore, checking the criticism from other reviewers, and the response by the authors, I do not think that the paper has any weakness that might warrant blocking the publications.

I think this is a very good to excellent paper. As promised, I am increasing my score to 8 and I am happy to further champion it.

### Soundness
3

### Presentation
2

### Contribution
3
