# From Bricks to Bridges: Product of Invariances to Enhance Latent Space Communication

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
It has been observed that representations learned by distinct neural networks conceal structural similarities when the models are trained under similar inductive biases. 
From a geometric perspective, identifying the classes of transformations and the related invariances that connect these representations is fundamental to unlocking applications, such as merging, stitching, and reusing different neural modules. However, estimating task-specific transformations a priori can be challenging and expensive due to several factors (e.g., weights initialization, training hyperparameters, or data modality).
To this end, we introduce a versatile method to directly incorporate a set of invariances into the representations, constructing a product space of invariant components on top of the latent representations without requiring prior knowledge about the optimal invariance to infuse. 
We validate our solution on classification and reconstruction tasks, observing consistent latent similarity and downstream performance improvements in a zero-shot stitching setting. 
The experimental analysis comprises three modalities (vision, text, and graphs), twelve pretrained foundational models, nine benchmarks, and several architectures trained from scratch.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper expands on Relative Representations by allowing several distances to be combined, which allows incorporating additional invariances in the resulting representation.

They first present evidence that single distances aren’t sufficient as they are data/model dependent (the original work used Cosine distance), they then explore adding 3 new distances (Euclidean, L1, L_\infty) in Text, Image and Graph domains.

This is a rather simple yet very clear and well-executed paper, which brought back Relative Representations to my attention, a nice idea which got washed up in the recent wave of LLM excitement. It might have limited scope, but currently I lean favorably.

### Strengths
1. The paper has a clear focus, presents the problem well, and is overall extremely well executed. 
2. It was easy to follow and the extensions to the math were very well brought up.
3. It explores appropriate choices of distances and aggregations. Good details and interpretations were provided for what one should expect from them (e.g. Table 6 in the Appendix was exactly what I was looking for)
4. Results are clear and do improve in predictable fashion over baselines.

### Weaknesses
1. I feel like too much of the paper is spent on presenting evidence for the sub-optimality of single distance relative representations. I did not really understand why that point was made so repeatedly (Figure 1, Figure 3, Figure 4, Appendix Figure 8 and 9), instead of spending more time presenting different *combinations* of distances and their benefits/implications. In effect Table 1 is the first time a clear combination of distances is shown, and it is clearly better than the rest, so I would have wanted more of that.
2. Equally, as a result, less emphasis and space was spent explaining the results in 4.2, 4.3 and 4.4. I had to go back to the original paper to remember/understand what “zero-shot stitching” meant and how it was implemented.
3. Details were lacking in a few places, for example which aggregation function was used for most of the results. I assume MLP+sum given it performed the best in Section 4.3, but this isn’t spelt out?
4. Section 4.4 is also lacking in details and could benefit from some improvements, see below.
5. It is potentially of limited scope, but I would defer to the majority vote to see if that is a blocker or not.

### Questions
1. Do you really need to spend that much space and energy on presenting the failures of single distance Relative Representations? 
   1. Figure 1, 3 and 4 are all making a similar point, and Section 4.1 does not feel as crucial as its length suggests it.
   2. I would probably recommend re-balancing this down and using the extra space to expand on the other Results sections.
   3. I would recommend keeping either 3 or 4 in the main text but not both.
   4. I am not sure that Figure 1 is the best framing figure to open the paper with, I might prefer to start with Figure 2.
2. The aggregations functions are presented well in Section 3, but it would have been useful to present implications for the choices of Sum and SelfAttention, in a similar manner to Concat (“giving to M the structure of a cartesian product space”).
   1. The Sum aggregation is actually a DeepSet by implementation. I would have liked having this spelt out explicitly and discussed?
3. The choice of Anchor points A_X and their implications on the invariances or properties of the relative representations are not discussed.
   1. Section 4.2 mentions using 1280 randomly selected fixed anchors. Did you try changing it? Does it affect distances differently?
4. I could not find which aggregation function was used for results in Table 1, 2 and 3. This should be specified clearly.
5. It feels like showing other combinations of distances (instead of “single” vs “all”) would have been helpful, especially if different domains require different distances.
   1. Section 4.4 tries to go in that direction, but the Transformer aggregation is not the best one and combined with my issue 4, I wasn’t sure what you used, so it muddles the results.
6. Section 4.4 would benefit from being extended, I do not think it contains enough details currently.
   1. The experimental setup needs more details, there is no description of the transformer aggregation anywhere I could find.
   2. Table 5 should contain the value for the best other aggregation (e.g. MLP+sum?), as currently it makes it harder to see if QKV opt is sufficiently accurate or not.
   3. It is unfortunate that the Transformer aggregation performs poorly. It would be good to bring the MLP+Transformer one to the main text, or at least present more clearly what model is used. It is not my expectation that a DeepSet should outperform a Transformer if it has enough layers?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends the work on Relative Representation by ensembling multiple relative representations obtained by different distances. The combination of four distances cos, Euc, L1, $L_\infty$ and three ensemble methods concat, sum, and attention are explored in the text. Extensive experiments across text, graph, and vision domains demonstrated that the ensembled version can improve the performance of zero-shot stitching.

### Strengths
1. Ensembling multiple relative representations is a reasonable idea and it enhances the power of the original cosine relative representation.
2. The experiments are extensive. There are 28 tables including the appendix.
3. The writing style is formal.

### Weaknesses
 1. The selection of distances seems arbitrary.
    - (a) While the Euclidean distance is invariant under the Euclidean isometries and is a reasonable candidate beyond the Cosine distance. What is the rationale of the rest of the distances? Any geometric intuitions? Specifically, the $L_1$ and $L_\infty$ distances are not directly related to common geometric transformations like rotations or scalings. What specific invariances do they introduce, and why are these relevant for the task of zero-shot stitching? What are the specific properties of the transformations that are captured by $L_1$ and $L_\infty$ distances, and how do these complement the invariances provided by cosine and Euclidean distances?
    - (b) The Euclidean isometry is a special case of conformal (angle-preserving) map. For experiments that show better performance on Euclidean distances than on Cosine distances, what can we say about the underlying symmetries of the neural representation? Does it mean that that latent space contain less invarinace? I am asking this question because I want to see what extra understanding on neural representations we can get from this new formulation. It would be beneficial to explore the specific types of transformations that each distance is invariant to, and how these relate to the underlying structure of the data and the learned representations. For instance, how does the performance vary when the data undergoes specific transformations (e.g., rotations, scaling, shearing) in the input space?
    - (c) Page 2 "... which, combined, can capture arbitrary complex transformations of the latent space". It seems an overstatement to claim that the four chosen distances can capture "arbitrary complex transformations". This claim needs to be justified with a more rigorous analysis or at least a more precise definition of what constitutes a "complex transformation" in this context. It is unclear how the combination of these four distances spans the space of all possible transformations.
2. The Assumption in page 3 does not read smoothly. 
    - (a) The equivalence class of encoders is defined as the set of E such that $ \pi_\mathcal{M}TE=\pi_M E, \forall T\in\mathcal{T}$. This definition is confusing. I fail to see why it is an equivalence class. For example, say, $\mathcal{T}_1$ is scalings, and $\mathcal{T}_2$ is rotations, and $E$ is a constant mapping to the origin. Does $\mathcal{T}_1$ and  $\mathcal{T}_2$ induces two different equivalence classes of transformations? But clearly $E$ belongs to both classes of transformations. The definition needs to be clarified to specify how the choice of $\mathcal{T}$ and $\mathcal{M}$ affects the resulting equivalence classes. It is not clear if the equivalence classes are disjoint or if they form a partition of the space of all encoders.
    - (b) Suppose $\mathcal{M}$ is a single point. Then $\pi_{\mathcal{M}}TE=\pi_{\mathcal{M}}E$ for all $E$ and all $T$. This definition does not contain any useful info then. The definition needs to be more robust to degenerate cases and should provide a meaningful characterization of the encoders.
3. Page 5 "it is not possible to connect latent spaces of models with different initializations ..." It seems that the Pearson correlation for Cosine is higher than 0.94 in the left subfigure of Fig. 3 and higher than 0.8 in the right subfigure. What is the criterion for the statement of "no connection"? Any reference for the choice of criterion? I do not see this as "challenges the assumption in Moschella et al.". The statement needs to be supported by a clear definition of what constitutes a "connection" between latent spaces and a justification for the chosen threshold for considering two spaces as disconnected. The Pearson correlation alone might not be sufficient to capture the complex relationships between latent spaces.
4. Please clarify the aggregation used in Tab. 1 to Tab. 3, since there are multiple possibilities. It is important to specify the exact aggregation function used in the experiments to ensure reproducibility and to allow for a fair comparison with other methods. The details of the aggregation function, including any learnable parameters or specific operations, should be clearly stated.
5. Sec. 4.4 leads confusion. What is the difference between SelfAttention and SelfAttention + MLP opt? Isn't the SelfAttention trained (finetuned)? If not, what is the exact computation formula for the SelfAttention aggregation? Where is the initial values of the attention weights come from? Also, the numbers in Tab. 5 does not match that of in Tab. 15. The experimental setup in Section 4.4 needs to be clarified, particularly the training procedure for the SelfAttention mechanism and the differences between the various optimization strategies. The discrepancy in the results between Tables 5 and 15 needs to be addressed, and the reasons for using a different classifier in this section should be explained.

### Questions
See weakness section.

typo:

1. page 4, invriances
2. page 9, fourth row -> fifth row

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a product projection mechanism to generalize the framework of relative representation. In particular, the authors incorporate a set of invariances into the representation by constructing a production space of invariances. The findings are intuitive that multiple projections behave differently across different choices on initialization, model architecture, etc. Experimental results proved the effectiveness of the proposed method.

### Strengths
(1) The motivation is well presented of infusing multiple invariances into relative representation.

(2) The explanations and illustrations are mostly clear and intuitive of the manifold assumption and the product projection mechanism.

### Weaknesses
(1) On Page 5, the result analysis presents the discovery challenges the assumption in Moschella et al. (2022). More explanations are required to make this point clear. Besides, wondering if the experimental results are just a normal fluctuation due to different runs.

(2) On Page 6, the authors used 1280 randomly selected but fixed anchors. This is also a kind of randomness that is not explained away. In fact, for different choice of anchors, the sensitivity is different of the projection and measure function.

(3) On the experiments, the employed datasets and models are in small-scale and probably prone to overfitting issues. Do the analysis conclusions hold for large-scale models such as Stable Diffusion and GPT? There should be large-scale results to support the findings.

### Questions
No.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is about enhancing the relative representation. Relative representation is determined with dissimilarity measure between target data and anchor that is invariant to angle transformation. The former work of Moschella et al. (2022) uses cosine angle as this dissimilarity, but in this paper, it aggregates other dissmilarity to enhance latent communication. The results of this aggregation is assessed by accuracy of zero-shot classification using stiching models.

### Strengths
The paper gives evidences that why the relative representation only using cosine angle can be inappropriate.

### Weaknesses
1. The definition of the RR framework is strange. It is stated that RR is concatenation of $d(z, a_i)$, but $z$ and $a_i$ should be in different domain $(\mathcal{Z},$ and $\mathcal{X})$. I am assuming that the anchors are also encoded with $E_\theta$ so that $a_i$'s in the latent space $\mathcal{Z}$

2. The experiments setting in the section 4 is unclear. I am having trouble figuring out what is a stiching model for this downstream task and how it is trained. I am assuming it is the same definition as the stiching model defined in Moschella et al. (2022), but I am having trouble how the decoder for this down-stream task is (pre-)tained.

3. The enhancement of relative representation through aggregating is not convincing for me. In Table 2, the aggreagated accuracies closely matches with using $L_1$ encoder. Using MLP or SelfAttention in aggreagation does not seems to be fair in that it requires an addtional training to get the additional parameters for these layers (correct me if I am wrong.)

### Questions
1. In experiment in Section 4.3 ~ 4.4, is the MLP and self-attention aggregation trained (fine-tuned) in end-to-end fashion? 

2. Does the downstream task with relative representation presented also enhance the performance of other tasks? (e.g. generation)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
