# SMAAT: Scalable Manifold-Aware Adversarial Training for Large Language Models

- Decision: Reject
- Scores: 6, 8, 5, 6, 5

## Abstract
Adversarial Training (AT), the method of finetuning a deep learning model with adversarially generated examples, is the most reliable form of making a model robust against future adversarial perturbations. However, AT is substantially expensive than standard training as it requires several full forward and backward passes to compute adversarial examples. In this paper, we introduce SMAAT, an efficient AT method that uses only adversarial examples generated in the last layer to finetune encoder-based large language models. The basis of our approach are the following three observations (i) the intrinsic dimensionality of the embedding space spanned by different layers of a deep model is substantially lower than the explicit dimensionality of the token embeddings; (ii) Encoder-based language models exhibit a monotonic behavior in their intrinsic dimensionality, i.e., deeper layers (closer to the output) have much lower intrinsic dimensionality than the shallow layers (closer to the input); (iii) off-manifold examples tend to persist across layers, i.e., an image of an off-manifold example generated in a shallow layer continues to remain off-manifold with respect to the embedding space of the later layers. We empirically demonstrate the effectiveness of SMAAT and show that it increases robustness by 8.6%, 15.7%, and 28.8% for BERT and 6.0%, 5.8%, and 19.0% for RoBERTa over the previous state-of-the-art results on AGNEWS, IMDB, and YELP, respectively. These improvements are achieved while maintaining comparable generalization and reducing the computational cost to approximately 1/3 to 1/4 of the GPU times required by the Projected Gradient Descent algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces SMAAT, an efficient Adversarial Training method that uses only adversarial examples generated in the last layer of a model in encoder-based large language models. The proposed method has fast training and inference speed since we do not have to do a full forward-backward passes.

### Strengths
- The proposed method is intuitive and backed by good motivation, and both theoretical and experimental findings.
- The proposed method outperforms most of the previous methods on various attacks and datasets.

### Weaknesses
- Argument about the manifolds between the layers is not very clear to the reader.
- Results on Table 1 are difficult to interpret. I would suggest just to boldify the best result for every attack in each dataset without having any underlined results.
- I believe that the method is probably not very novel or of high contribution.

### Questions
- Have you conducted any experiments where you use adversarial examples generated from other layers instead of the only the last one. Sometimes theorems and experiments can provide very different outcomes.
- I read the limitations at the end of the paper. Although this is not in the scope of this work I would suggest to still try this method with image data.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents SMAAT, an efficient approach for adversarial training of language models, which relies on fine-tuning a pretrained model using adversarial examples generated from the last layer of the model. To motivate the approach, the paper discusses the link between inputs being out of manifold for consecutive layers, and the difference in the intrinsic dimensionality of these layers. Then, since language models exhibit a monotonically decreasing *intrinsic dimensionality (ID)* of their representations throughout layers, the optimal layer to generate adversarial examples from is the last layer. Using only the last layer in the forward-backward passes of PGD to generate adversarial examples is much more efficient than using the full model. Finally, the paper shows that on top of the efficiency of the proposed approach, the defended models are more robust than recent defenses against common adversarial attacks for text on three text classification benchmarks.

### Strengths
- **Robustness and Natural Accuracy:** The paper demonstrates substantial improvements in model robustness when compared to other defense methods, without compromising natural accuracy. It achieves consistent results across three benchmark datasets using two different models.  
- **Efficient Adversarial Training:** The paper offers a very efficient approach to adversarial training. By concentrating on the last layer of the model for generating adversarial examples, it significantly reduces the computational overhead associated with this process. This efficiency is a significant contribution, making adversarial training more accessible for practical applications.
- **Clear Presentation and Context Setting:** The paper is well-organized and presents related work in the field clearly. The description of the approach is also easy to understand.

### Weaknesses
In general, the formulation and description of the motivation behind the approach is not very clear and lacks rigor. This makes the foundations of the approach unsound. There are several quantities vaguely defined, such as the basis $U_l$ obtained from the SVD, the formulation of the theorem 3.1 and its proof, or the Intrinsic Dimension of a layer that is discussed and used before being defined. This leads to critical misunderstandings that require clarification.

### Typos
Here are some typos I noticed:
- conjoncture -> conjecture (in figure 2 and in last paragraph of page 3)
- the $\exists$ should be $\forall$ in equation 4 and equation 9
- orhonormal -> orthonormal (in 3.1, between equation 4 and equation 5)
- Emperical -> Empirical (in title of 3.3)

### Questions
- As mentioned in the paper, the basis $U_l$ obtained through SVD is an orthonormal basis. Thus, $U_l U_l^\top = I$, which makes the projection error as defined in the paper always equal to zero. 
- Can the authors clarify how to derive equation 7 from equation 6 ? It is critical as it links the search for the optimal layer $l^*$ to theorem 3.1.
- In theorem 3.1, the proof in Appendix is given for the opposite side: If $||(I - U_{(i-1)} U_{(i-1)}^\top)\delta_{(i-1)}|| < ||(I-U_i U_i^\top)\delta_i||$ then $rank(i-1) < rank(i)$. There is also the equality case that is included in the theorem but not in the proof. Maybe the inequalities should be reversed in the formulation of the theorem, which would make a proof by contraposition ? This would also make sense with the remaining of the paper, since we observe decreasing ID and not increasing ID.
- Similarly, for the objectives of SMAAT (eq. 9 and 10), the inequalities on the ID do not make sense since we observe decreasing ID throughout the layers. I think the inequality should be reversed as well, i.e. $ID(i) < ID(i-1)$.
-  What is k and $U_l^k$ in the computation of ID (equation 11) ? I assume it is the k first rows and columns of $U_l$, which would make ID close to the rank of the representation. This should be clarified, as well as the link between ID and the rank, since the theorem is stated using the *rank operator*.
-  What is $\lambda_{max}$ ? Is it the maximum eigenvalue ? If so, I'm unsure about the assumption used in the proof of theorem 3.1 about the ratio of $\lambda_{max}$. There is an additional layer in the network from which the jacobian is computed in the numerator, thus the Lipschitz constant of the numerator is greater than the one of the denominator, making the ratio greater than 1. Does the remaining of the proof holds with this ? 
-  The proposed approach is interestingly the opposite of YOPO [1], can the authors develop on the link and differences regarding this method ?

[1] Zhang et al., You Only Propagate Once: Accelerating Adversarial Training via Maximal Principle, NeurIPS 2019.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an efficient adversarial training (AT) method, particularly for language models, called SMAAT. SMAAT speeds up AT by only using the last several layers to generate adversarial samples. In this way, it does not need to back-propagation through all the layers while generating adversarial training data, thus reducing the training time. Empirical results seem to validate the effectiveness of SMAAT in efficiently learning a robust and generalizable language model.

### Strengths
1. The empirical results on three datasets seem to justify the effectiveness of the SMAAT.

2. The authors try to provide some theoretical derivation to motivate the proposed method.

### Weaknesses
1. I am confused about the definition of ‘off-manifold’ and ‘on-manifold’. It would be better for the authors to provide more clear definitions and high-level explanations to help understand.

2. I am confused about the choice of $l^* = n$. In the objection function in Eq. (10), it seems that any $l^*$ satisfies when $ID(i-1)<ID(i), \forall I < l^*$. Based on my observation of Figure 3, $l^*$ can be chosen any number smaller than 13 since ID is monotonically decreasing. Therefore, based on Eq. (10), I cannot understand why the choice of $l^* = n$ is optimal.

3. Empirical results are limited. The evaluation should be conducted on various datasets in the GLUE benchmark.

4. The title seems to overclaim the contribution of this paper. All the results in this paper are shown on two language models, i.e., BERT and RoBERTa. However, I did not see the results of ‘large language models (LLMs)’ such as Llama2-70b. I am wondering whether the proposed method can be scalable to LLMs. If so, please show the empirical justification.  

Minor comments: keep a consistency of the term ‘ROBERTA’ in Section 3.3 and ‘RoBerta’ in Introduction.

### Questions
Please refer to “Weaknesses”.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a manifold-aware approach to enhance the scalability and efficiency of adversarial training. Specifically, the model generates adversarial examples from higher layers in the deep neural network thereby shortening the gradient-based propagation and accelerating the generation of adversarial examples. Extensive experiments verified the effectiveness of the method.

### Strengths
1. Observations and theories are very interesting. Generating adversarial examples from the higher layers of the neural network reduces the distance of gradient propagation, and Table 2 also shows the efficiency of the method.

2. The method compares with multiple strong baselines for LLM defense and shows outperformance. The experimental results look good.

3. The paper is clearly presented and easy to follow, with many intuitions discussed in detail and the related work adequately discussed. Although the proposed method has some limitations, it is inspiring for future adversarial training of LLMs.

### Weaknesses
1. The three observations mentioned in the abstract appear not to be discussed in detail in the paper. How do these observations motivate the methodology?

2. How effective are SMAAT generated adversarial examples compared to standard adversarial examples in attacking LLMs?

3. Are the baseline and adversarial training models being compared in the paper using the same augmentation or training strengths? The strength and budget of the baselines appear not to be presented in the paper.

4. It is unclear about the generalizability of the method. Will the proposed method be effective against other types of attacks such as typos?

### Questions
See the above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces SMAAT, a scalable manifold-aware adversarial training method for large language models. This paper proposes to generate adversarial examples efficiently via the last layer of the model, based on the hypothesis and observation of monotonically decreasing intrinsic dimensionality of the embedding space. The empirical evaluations on AGNEWS, IMDB, and YELP demonstrate improvements in robustness and scalability over previous state-of-the-art methods.

### Strengths
+ originality, this paper proposes to adversarially training the last layer of language model to gain adversarial robustness, with seeking scalability.

+ clarity, this paper is clear to follow and easy to read.

### Weaknesses
- lack of evidence for scalability: does the hypothesis of intrinsic dimensionality still hold for larger language models? 

- ablation study of adversarial training on different layers: since this paper proposes to only fine-tune the last layer, what will happen if we include more layers for adversarial training? do we gain better robustness since more model parameters are included for adversarial training?

- lack of adaptive attack: I strongly recommend the authors to design the adaptive attack [1] to approximate the lower bound of empirical adversarial robustness under their defense. This paper only evaluates model robustness under a simple 5-step PGD attack, which is not enough.

[1] Florian Tramer, Nicholas Carlini, Wieland Brendel, Aleksander Madry, On Adaptive Attacks to Adversarial Example Defenses

### Questions
no question

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
