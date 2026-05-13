# Boosting the visual interpretability of CLIP via adversarial fine-tuning

- Decision: Accept
- Scores: 6, 6, 6, 8, 8

## Abstract
CLIP has achieved great success in visual representation learning and is becoming an important plug-in component for many large multi-modal models like LLaVA and DALL-E. However, the lack of interpretability caused by the intricate image encoder architecture and training process restrict its wider use in high-stake decision making applications. In this work, we propose an unsupervised adversarial fine-tuning (AFT) with norm-regularization to enhance the visual interpretability of CLIP. We provide theoretical analysis showing that AFT has implicit regularization that enforces the image encoder to encode the input features sparsely, directing the network's focus towards meaningful features. Evaluations by both feature attribution techniques and network dissection offer convincing evidence that the visual interpretability of CLIP has significant improvements. With AFT, the image encoder priorities pertinent input features, and the neuron within the encoder exhibit better alignment with human-understandable concepts. Moreover, these effects are generalizable to out-of-distribution datasets and can be transferred to downstream tasks. Additionally, AFT enhances the visual interpretability of derived large vision-language models that incorporate the pre-trained CLIP an integral component. The code of this work will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper puts itself in a new area of study — studying interpretability in the context of the vision language models. Whereas the previous works have majorly focused on the interpretation of multimodal interactions, for example, how different text tokens interact with different image regions. However, this paper tries to probe and improve the interpretability of the image encoder of the vision language model (CLIP). They further show that the enhanced interpretability of the vision encoder is transferable - plugging in the same image encoder in a different vision language model (e.g. LLAVA)  provides better attention maps for interpretation. The proposed unsupervised adversarial fine tuning (AFT) method is finally evaluated extensively against various benchmarks and provides mathematical insights into its workings.

### Strengths
1. The paper is organized and very well written.
2. The paper reports the evaluation of the proposed AFT approach with good coverage.
3. They show that optimising the upper bound for a sparse set of concepts of vision encoder using L1 regularization is independent of the text embedding and, hence, can be optimized in isolation.
4. They cover the evaluation of saliency map explanations quite well- using transferability, feature importance (ROAR benchmark), attention maps and pointing game.
5. It also provides concept explanation visualization using concept detectors through network dissection.

### Weaknesses
1. There are studies that connect adversarial robustness and saliency explanations [2] that attempt to use adversarial training [1] to improve interpretability. Such studies are missing in the related works section in the entirety. Coverage of such studies and then comparing them with the proposes AFT method could significantly enhance the value of the paper and place it in the literature.
2. Because, in real-life scenarios, the features a black box relies on might be non-trivial in image space. For example, both a 'classroom' and a 'movie theatre' have collection of chair, and what differentiates them is the orientation of the furnitures, size of the room and so on. Such concepts can not be highlighted using saliency on the image space. Concept of saliency maps only works in a simple (e.g. object detection) framework.
3. The explanations were initially intended to help the end user (e.g. driver of a car with a deep learning autonomous driving agent) of the application to understand the system better. Such studies determine, irrespective of an explanation being more/less accurate, how much the end user is benefitted from the explanations to perform the enf task [3].


### Questions
Refer to the weaknesses.

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
This paper proposes an unsupervised adversarial fine-tuning (AFT) strategy for improving the visual
interpretability of CLIP. Understanding and improving the interpretability of CLIP is crucial since it has been utilized as a visual encoder in multiple image generation and vision-language models (VLMs). This paper demonstrates the effectiveness of the proposed method in improving interpretability, both qualitatively and quantitatively, on multiple feature attribution and neuron explainability methods.

### Strengths
1. The paper is well-motivated, making it easier to follow the main ideas and claims.
2. The theoretical result on the duality between the regularised norm of adversarial perturbations and the input gradients is interesting and non-trivial. Further, the proposed unsupervised objective function helps alleviate the need for paired image-text datasets.
3. Improvements in interpretability have been demonstrated on multiple feature attribution and neuron explainability methods.
4. The proposed method does not significantly change the zero-shot generalization ability of CLIP while improving interpretability, as demonstrated by the linear probing results.

### Weaknesses
1. One of the primary motivations of this work is to improve the interpretability and performance of VLMs. However, only qualitative results are provided in Sec 4.3 and Fig 7, and the paper does not provide any quantitative results for the same.
2. VLMs and image generation models need vision encoders without any explicit need for encoders trained with contrastive loss. Is this method applicable to vision encoders in general or limited to CLIP?
3. The empirical performance difference between training unsupervised upper bound in Eq 7 vs Eq 1 has not been quantified. $T_x$ calculation should not significantly increase the computation overhead on smaller datasets and quantifying the difference in performance would give a better understanding of the tradeoff with use of Eq 7.
4. Ln 206: Should be $T_x$

### Questions
Please see weaknesses [1-3]

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
3

### Summary
The paper studies the interpretability of VLMs like CLIP and and LVLMs like LLAVa. The authors propose a adversarial fine-tuning based loss which includes a regularization term and addition of Gaussian noise in the standard adversarial training loss. The resulting method AFT, achieves better interpretability in terms of saliency maps, feature importance etc in comparison to standard ERM based CLIP.

### Strengths
- The paper is nicely motivated and easy to follow.
- The set of experiments is extensive and helps to highlight the effectiveness of the proposed AFT loss.
- The experiment cover both CLIP and LVLMs like LLaVA.
- AFT yields better interpretable saliency maps and also attains zero-shot robustness similar to baselines.

### Weaknesses
 - The novelty aspect of this work is not enough, it is known adversarially robust models yield more interpretable models [1, 2, 3], and this work also comes to a similar conclusion albeit with a different formulation of objective. Would FARE loss not yield similar interpretability?
see next points.  
- The loss equation. 7 is similar to the objective of FARE [4] (upto Gaussian noise and the regularizer, h(.)) - there needs to be a discussion regarding this (which is missing in the current version - only a small sentence regarding this is found in the appendix).
- If one removes the noise term and h(.) - one retrieves FARE objective - How does this loss perform in the same setup as the figures 2 and 3?
- Would FARE not be an apt baseline in addition to original CLIP?

- Gaussian term is motivated by "avoid being stuck in the non-trivial stationary point" - using PGD for AT one can start at a random location in the $\ell_p$-ball, this randoms start already helps with not being stuck. It seems gaussian noise is sampled every iteration, as this seems an important part of the loss - the effect this term has is not discussed

### Questions
Some questions are already present in Weakness section. A few general queries are listed here.

- The experiment with LLaVA is interesting, how much does the sparsity inducing term h(.) help here? It is interesting as now attention weights from LLM are used and this should have an effect in noise/smoothing issues mentioned earlier in the paper regarding h(.).

- Is the gaussian noise sampled at every PGD iteration?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an unsupervised adversarial fine-tuning (AFT) method to alleviate the issues of insufficient representation and poor interpretability in visual representation learning of CLIP. The paper provides theoretical evidence for the feasibility of the method and presents a rigorous derivation process with well-defined formulas. The experimental results provided in the paper demonstrate the effectiveness of the proposed approach.

### Strengths
1. There is a clear definition of the research problem, which is to enhance the visual interpretability of CLIP. The problem is visualized through the form of saliency maps.
2. The proposed method in the paper demonstrates a good level of originality. The extensive formalized equations provide evidence of the method's rigor and credibility. The abundance of experimental data and visualization results further confirm the effectiveness of the AFT method.
3. The paper presents a clear and well-structured expression, making it easy to read and follow.

### Weaknesses
1. From the experimental results, AFT appears to be an effective method. However, it is unclear whether this method introduces additional complexity. I would like to see comparative experiments that evaluate the parameter quantity, computational cost, and other factors before and after applying this method.
2. Although the paper designs the AFT method based on CLIP and achieves good results on relevant datasets, it is mentioned that the AFT method can be extended to any base model that includes intermediate embedding layer connection patterns. More experiments should be provided for this claim. In other words, selecting a few base models other than CLIP and applying the AFT method to demonstrate its general applicability would be beneficial.

### Questions
1. Does AFT introduce additional complexity? It would be better to provide comparative experiments regarding the parameter number, computational cost, and other factors before and after applying this method.
2. Can the proposed method be applied to base models other than CLIP? These experiments could show the generalizability of the method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors propose an unsupervised adversarial fine-tuning (AFT) method with norm-regularization to enhance the visual interpretability of CLIP.  Overall, this paper proposes a comprehensive theoretical analysis of their motivation and provides extensive experiments to prove the correctness of their ideas. However, it still has some issues.

### Strengths
1. The theoretical analysis of their method is supportive
2. The experimental results are enough to support their motivation and demonstrate its correctness.

### Weaknesses
1. Too few content is with regard to the implemental details.  At least, an overview of the proposed method should be provided.

2. Though the proposed method is interesting, a single novel norm-regularization might not be enough to support the high standard of ICLR. More introduction content of your main contributions should be added. For instance, the innovation of the proposed method or the creative construction of your method.

### Questions
1. Could you please provide more easy-understanding and plain descriptions of what you do? For example, the architecture of your propose method, and the final loss function of your method.

2. Make more claims on your contributions. For instance, the innovation of your ideas, or the creative construction of your method.

3. why do you call your methods as the adversarial fine-tuning?

### Soundness
3

### Presentation
3

### Contribution
3
