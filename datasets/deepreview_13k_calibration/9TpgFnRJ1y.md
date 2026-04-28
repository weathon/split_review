# Interpretable and Efficient Counterfactual Generation for Real-Time User Interaction

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5

## Abstract
Among the various forms of post-hoc explanations for black-box models, counterfactuals stand out for their intuitiveness and effectiveness. However, longstanding challenges in counterfactual explanations involve the efficiency of the search process, the likelihood of generated instances, their interpretability, and in some cases, the validity of the explanations themselves. In this work we introduce a generative framework designed to address all of these issues. Notably, this is the first framework capable of generating interpretable counterfactual images in real-time, making it suitable for human-in-the-loop classification and decision-making. Our method leverages a disentangled regularized autoencoder to achieve two complementary goals: generating high-quality instances and promoting label disentanglement to provide full control over the decision boundary. This allows the model to sidestep expensive gradient-based optimizations by directly generating counterfactuals based on the adversarial distribution. A user study conducted on a challenging human-machine classification task demonstrates the effectiveness of the approach in improving human performance, highlighting the critical role of counterfactual explanations in achieving this advantage.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper generates interpretable counterfactual images in real-time leveraging a disentangled
regularized autoencoder for labels and instances making it more accessible for HITL-approach
The approach appears to be theoretically rigorous, using disentanglement and latent
space regularization efficiently for counterfactual sampling. The method is theoretically
robust, with well-founded training and selection mechanisms supported by rigorous
yet somewhat obvious proofs (so the theoretical contribution is limited).
While experimental methods are robust, including additional datasets would enhance
statistical generalizability and validate findings. The paper is well-written, with effective
visuals and a logical flow. Some additional annotations on the figures would make them more accessible.
The framework has possibly some limited potential to impact AI explainability in real-time decision-making,
particularly in human-centered applications but some points need yet to be clarifed (see points below).
It addresses a gap by making counterfactual explanations feasible in interactive settings.
Real-world deployment could face challenges due to computational demands and the
complex training setup. Furthermore, the dependency on a well-defined latent space
might limit the framework’s adaptability to highly complex or noisy data, which might
restrict real-world deployment.
Some suggestions for improvement:
-Expand the empirical evaluation with a broader range of datasets to improve robustness
and generalizability.
-Clarify the "100% validity" claim with a more nuanced discussion of potential limitations.
(might be redundant if the math already proves 100% validity).
-Conduct quantitative comparisons with other methods to offer a clearer perspective on
relative strengths and weaknesses.

### Strengths
The approach has some potential to enhance counterfactual generation by balancing efficiency and interpretability, both of which are essential for real-time, human-centered applications. A user study indicates that the generated counterfactuals may potentially enhance
human task performance, which would be valuable in practical settings. The methodology is well-structured and includes clear descriptions of each step in the counterfactual generation pipeline. It seems that the user study is scientifically valid and includes appropriate metrics. With a generation time of about 1.2 seconds, the framework seems ready for real-time, interactive AI applications. The authors claim that their framework is the first of this kind.

### Weaknesses
The evaluation is limited to a single dataset (BloodMNIST) and task, which may impact the method's broader applicability. A wider evaluation, including datasets with different modalities and complexities, would give a better sense of its utility across different contexts. The claim of “100% validity” might be overconfident; while the method may ensure that generated counterfactuals are classified as the target class, it does not guarantee that these counterfactuals are realistic or plausible, especially in high-dimensional edge cases. The reliance on a disentangled latent space, while beneficial for interpretability, may also limit the method's applicability to datasets where such disentanglement is difficult to achieve or where the latent space does not capture the full complexity of the data. Furthermore, the computational demands of the method, particularly the training of the disentangled autoencoder and the auxiliary model, could be a significant barrier to real-world deployment, especially in resource-constrained environments.

### Questions
-Could the authors clarify how are the “associated concepts” at line 348 identified? Does the framework directly offer human-comprehensable concepts for latent features? If so, how this is achieved?

-What does “unsupervised” in line 406 mean? It seems that the training of the framework requires massive labeled data, therefore against the claim of being “unsupervised”.

-Could the authors elaborate more on why the decoder $\mathrm{DEC}$ is not suitable for generation? Both $\mathrm{ENC}_s$ and $\mathrm{ENC}_u$ learn distributions for the latent space, sampling a point from a specific Gaussian should generate a synthetic instance.

-The denosing serves for shaping latent space structure, couldn’t it be applied during the training of the autoencoder? The decoder should be able to handle noises at an appropriate level, which makes the auxiliary model somehow redundant.

### Soundness
2

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
This work proposes a new counterfactual explanation technique for image classification. The technique uses a regularized latent space model and searches for suitable counterfactual candidates in the learned latent space, which should have favorable interpretability characteristics. The technique is evaluated through a human-subject study.

### Strengths
Strengths:
* Overall, the technique is well explained and the writeup is good to follow 
* I did not discover any major flaws regarding soundness
* User evaluation is important, and not often considered in XAI

### Weaknesses
Weaknesses:

*   **Related Work.** Unfortunately, there are many related techniques for counterfactual image generation that are not discussed in this work. In general, the idea of using latent-variable models to generate counterfactuals cannot be considered novel and is well covered in the literature, e.g., by Sauer & Geiger (2021). A recent work (Melistas et al., 2024, Section 2) lists more than 10 approaches to tackle the problem presented using VAEs, GANs, Deep-SCM, Diffusion models, Flows, ... Unfortunately, these related works are not mentioned here. It is not clear why they are insufficient and yet another method to tackle this problem is required. While some of these methods do require a causal graph, many do not. The authors should more clearly articulate the specific limitations of existing methods that their approach addresses, as simply building an "interpretable" latent space without theoretical guarantees is insufficient to justify novelty.

*   **Grounding for disentanglement claims.** The authors claim that their method yields interpretable, disentangled representations. However, while regularization can help disentanglement in practice, it should be noted that there is theoretical backing for this claim (unless some rigid assumptions or knowledge of causal models is assumed). For instance, Locatello et al. (2019) prove that disentanglement without additional information is impossible, and Leemann et al. (2023) study the topic for conceptual explanations. It is therefore questionable whether the mentioned trade-off between disentanglement and reconstruction quality really exists. The references given (e.g., BetaVAE and its derivatives) do not reflect the current state of research.

*   **Evidence for claims.** It is okay to make claims like in Section 6 (l.406-407, "this is the first unsupervised concept based counterfactual generating technique suited for a real time interaction") but this requires evidence to back them. For instance, at this point I would have expected a run-down of runtimes of other CFE techniques for images when using encoders/decoders of the same complexity.

*   **Evaluation is insufficient and qualitative results are not convincing.** I think a user-study is a good start for evaluation, but it not sufficient on its own. I think other metrics for image quality such as FID and edit-distance (in input and latent space) should be checked and reported as well, in particular in contrast to other techniques. Unfortunately, the counterfactuals shown in the Figure look blurry and not like realistic scans. Disentanglement claims should be checked using synthetic datasets with known concepts such as 3DShapes (https://github.com/google-deepmind/3d-shapes).

*   **Ablation studies are missing.** There are no ablation studies that allows to verify the necessity of each component in the framework. For instance, I am wondering whether the complex calculation of the mean is necessary or if some point a specific distance behind the decision boundary on the segment from the input embedding and the counterfactual class embedding would be sufficient.

*   **Accuracy considerations.** The work proposes to use a specific generative image classification model that allows to directly generate counterfactuals. However, I think the accuracy of this model will be lower than that of state-of-the-art models. This trade-off is not discussed.
----------------

**Summary.** Unfortunately, I don’t think the technique developed is highly innovative and an evaluation against competing techniques is missing. If there is a specific advantage of the technique that I am missing, I suggest that a comparative analysis with the techniques in Melistas et al. (2024) should be added to show this advantage. In its current state the motivation why the existing techniques are insufficient for the counterfactual generation problem is not clear at all.

--------------------

**References**

Locatello, Francesco, Stefan Bauer, Mario Lucic, Gunnar Raetsch, Sylvain Gelly, Bernhard Schölkopf, and Olivier Bachem. "Challenging common assumptions in the unsupervised learning of disentangled representations." In international conference on machine learning, pp. 4114-4124. PMLR, 2019.

Tobias Leemann, Michael Kirchhof, Yao Rong, Enkelejda Kasneci, Gjergji Kasneci Proceedings of the Thirty-Ninth Conference on Uncertainty in Artificial Intelligence (UAI), PMLR 216:1207-1218, 2023.

Sauer, Axel, and Andreas Geiger. "Counterfactual Generative Networks." International Conference on Learning Representations, 2021

Melistas, T., Spyrou, N., Gkouti, N., Sanchez, P., Vlontzos, A., Papanastasiou, G., & Tsaftaris, S. A. (2024). Benchmarking Counterfactual Image Generation. arXiv preprint arXiv:2403.20287.

Minor points: There are a couple of issues with the writeup
* Please check capitalization of bullet points in lines 122-132.
* L.141-152 is hard to follow.
* Typo L.176 (caption): “regularize”
* L. 215 “DDPM” is not introduced
* L. 344 Concept-based (section title)
* L. 346 class-relevant
* When you refer to the appendix, please include a link to the exact section or figure (e.g. l. 347)
* L. 410 hyper-parameter configuration
* Table 1: Please use the same number of digits for each result
* I noticed that on page 27 of this submission (Figure 13), it seems to be indicated that the study was conducted at the University of Trento, potentially revealing the affiliation of the authors and thereby violating the double-blind review principle.

### Questions
* User study: I have some questions regarding the user study: Was the study IRB approved? Was the study preregistered? The number of 50 participants divided over multiple conditions seems rather low, how was the number chosen? A survey by Rong et al. (2022) shows the average number of participants in XAI user studies with a between-subjects design to be greater than 300. 

* The study relies on a specific classification model which performs the classification through a regularized latent space. What are the costs of explainability here, i.e., what is the performance difference of this model (91% accuracy is reported) vs. using a state-of-the-art black-box model that is trained on the dataset without any constraints?

* Technical Derivation: In Equation (9), how is the formula for the weights determined? If one is interested in the expected value, shouldn't the weight of each segment be the integrated density over the segment? Here it seems that only the density at the respective center is used. Suppose we have a constant density, then the length of the segment would not play a role in the weight? is this intentional?

**Reference**

Rong, Yao, Tobias Leemann, Thai-trang Nguyen, Lisa Fiedler, Peizhu Qian, Vaibhav Unhelkar, Tina Seidel, Gjergji Kasneci, and Enkelejda Kasneci. "Towards human-centered explainable AI: user studies for model explanations.", IEEE Transactions on Pattern Analysis and Machine Intelligence (2022)

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on the topic of generating visual counterfactual explanations for predictive models in computer vision. The proposed method is based on a Denoising Disentangled Regularized Autoencoder trained in a two stage manner. The first stage deterministically trains an encoder-decoder architecture with the encoder split into two separate parts responsible for label-based and label-independent information. The second stage introduces stochasticity to the learning process and, after freezing the previously learned weights, trains an additional autoencoder on the combined latents. The introduced architecture is utilized for the counterfactual explanation generation by encoding the factual image into its two-part latent representation, modifying the label-relevant part to identify candidate counterfactuals, computing the `expected counterfactual', extracting the most important concepts based on a proposed metric, and decoding the modified label-based latent together with label-irrelevant part to obtain the explanation. The work explicitly defines the properties of the mentioned counterfactual candidates and develops a theoretical result to more efficiently search for the best candidate. The proposed method is evaluated through a user study based on the BloodMNIST dataset with detailed analysis of the obtained results, showing how the proposed approach can guide humans to improved decision-making.

### Strengths
S1. The authors provide a clear introduction and motivation to the problem addressed in their work.

S2. The method's overview clearly explains how specific components of the proposed architecture aim to address the mentioned limitations of previous works. The description of each component of the optimized loss is properly described. Overall, despite the complexity of the framework, the authors succeed in clearly communicating its inner workings using the attached figures and pseudocode.

S3. In addition to the practical side of the framework (two-step training procedure), the authors propose an interesting theoretical result to efficiently search for the `optimal' counterfactual candidate in the model's latent space. I also enjoyed the introduced relevance scores for concept selection, Fig. 2 that nicely summarizes the candidate selection procedure and the attached pseudocode in Algorithm 1.

S4. The experimental evaluation is based on a properly designed user study with detailed analysis of the obtained results. Interesting research questions were proposed and the provided results were very well processed to provide principled answers. 

S5. The overall writing is clear and properly redacted, except some small typos, e.g., $S_1$ in line 270.

S6. Source code is provided as an anonymised repository to ensure reproducibility.

### Weaknesses
W1. Both the abstract and the introduction mention specific limitations of previous works, specifically: efficiency, likeliness, interpretability, validity and sparsity. While the paper provides motivation on how each of the component's framework addresses those, I must argue that the paper struggles to provide empirical evidence for these claims. While some quantitative results are provided (e.g., average generation time in line 408), they are mainly focused on the influence of the method on human decision-making and do not address the limitations. Also, no comparison with previous work is given. The above measures could be quantified using, e.g., some variation of FID [5] and S3 [2,6] (likeliness, validity), and COUT [7] for sparsity.

W2. While the paper is well-written, I got confused with how the authors position their work in the XAI domain, its connection to counterfactual explanations for deep learning models as post-hoc explanations and their required properties. To the best of my understanding, the proposed method is not able to provide post-hoc explanations for any predicitve model other than the Gaussian-mixture-based classifier trained together with other components. This is problematic since the described limitations are mentioned as problems of generally applicable methods and their relationship with the authors work is unclear.

W3. The authors mention real-time generation as one of the main contributions of their method. However, the paper lacks quantitative results comparing the proposed approach to any of the previous works in this context, making it unclear whether the improvements are only incremental or actually ground-breaking. While the method might indeed be an effective real-time generator, it is not clear how this relates to previous works which address a more general class of models (see W2.).

W4. The paper mainly cites works from the 2018-2022 period. While I do not consider myself a highly-educated expert in either the topic of contrastive explanations, deterministic regularized autoencoders nor latent disentanglement, I cannot escape the feeling that there are more recent papers that could be mentioned in these contexts. This is not an explicit weakness of the paper, but I would be happy if the authors could address why more recent works do not appear in the literature section (has the field somehow slowed down or community lost interest in it?). My another concern is the specific connection of this work to the topic of contrastive explanations - I must argue that mentioning specific works on visual counterfactual explanations (VCEs) would better reflect the paper's connection to the field. In this case, the authors fail to mention a large amount of work combining generative models and VCEs from the recent years, e.g. [1,2,3,4] to name a few. How does the authors' paper place itself in the context of these works?

W5. From a theoretical point of view, the paper often provides very strong claims like `the non-existence of a strictly better counterfactual' (lines 259-260), `such counterfactual intrinsically optimizes the trade-off between the likelihood of the explanation and the distance
from the instance to explain` (lines 281-283) which are true only when assuming that the Gaussian mixture model perfectly preserves the relationships between the samples from the original data distribution. This should be stated explicitly in the paper and I would like to authors to further elaborate on the assumptions and limitations of this approach.

W6. Another contribution mentioned by the authors is the possibility of extracting interpretable concepts associated with the latent dimenions of the proposed architecture. It should be stated clearly that the identification of these concepts requires a human expert that will properly label them. For example, to the best of my understanding, examples like those in Fig. 10 include descriptions of concepts that were first labelled by the expert. In terms of experiments, I think that the influence of these concepts on the human decision-making has not been properly studied, making it difficult to disentangle their contributions to the overall process.

W7. To maintain the review's structure, I will include my question regarding the theoretical derivations here. I must stress that these are very detailed and I was generally satisfied with them. My concern is the pharsing from line 850, where it is stated that `the expected value, according to an isotropic Gaussian, of the elements in a segment $S$ (...)`. Could the authors clarify whether this sentence assumes that elements in $S$ follow an isotropic Gaussian distribution? To the best of my understanding, $S$ forms a bounded interval since $S = \{ (1 - t) \cdot a + t \cdot b \mid t \in [0, 1] \}$, hence its elements cannot follow a Gaussian distribution which assumes infinite support.

### Questions
I would be happy if the authors could address each specific weakness mentioned above. In general, I would say that the paper has great potential but mentions contributions that are clearly not addressed. My suggestion for the authors would be to refocus the text on the human-machine interaction, since this is the most promising result, and deviate from the counterfactual explanation domain. It is difficult to be convinced that the proposed framework is in fact a counterfactual explanation generator if it only allows to provide them for a model trained inherently in the framework which is a very simple Gaussian-mixture-based classifier. Both the experimental design and theoretical derivations are very elegant and I encourage the authors to just focus on those with an extended empirical evaluation. Overall, the paper shows great promise that it might be worth training the framework from scratch for each new problem, since it may greatly improve the understanding of complex domains by inexperienced users.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework for counterfactual explanations based on a generative autoencoder. By refining the process of counterfactual selection, the proposed method effectively generates counterfactuals that fulfill a list of desired properties in real-time. The resultant explanations facilitate human-machine interactions and demonstrate the potential for improving user performance, as evidenced by the experimental results.

### Strengths
1. The paper is well-structured and self-contained, offering a clear definition of the objectives for counterfactual construction.
2. The definition of counterfactual candidates is sound, significantly narrowing the search space and enabling real-time generation.
3. The carefully designed experiment demonstrates the potential benefits of providing complementary information in human-machine interaction.

### Weaknesses
1. Similar to other generator-based explanation frameworks, the transparency of the explanation process itself is limited due to the black-box nature of the neural-network-implemented generator. The claim that human-understandable concepts address this is not entirely convincing. The derivation of these concepts requires additional effort from human experts, raising questions about scalability. Furthermore, there is a potential gap between the generator's actual behavior and the patterns inferred by humans, with no clear mechanism to guarantee faithful concept derivation.
2. The flexibility of the proposed method is another concern, as the delivered explanations appear to be model-specific. The requirement of a gaussian-mixture loss limits the applicability to a subset of models, and while this loss can achieve comparable performance to softmax, it still restricts the method's generality. The need for a decoding model for input space explanations further adds to the model-specific nature of the approach.
3. The expected counterfactual violates $\mathcal{P}_2$ stated in Definition 1. While the authors claim the deviation is bounded, the core issue remains that the selected counterfactual is not necessarily the best possible, suggesting room for improvement in the selection process.
4. The benefit of the rotation for accelerating expectation computation is unclear. While the rotation might reduce variance in aligned dimensions, it concentrates variance in the final dimension, which is then redistributed. The claim of computational efficiency needs further justification, especially considering that the segment is one-dimensional, and a univariate Monte-Carlo estimator might be sufficient.

### Questions
1. The definition of counterfactual candidates is well-motivated. However, recalling that the expected counterfactual is a weighted average of $\mathbb{S}_1$ and $\mathbb{S}_2$, the final result seems to deviate from both segments, thereby violating $\mathcal{P}_2$. This suggests that some counterfactuals are strictly better than the one selected. Could the authors provide clarification on how this should be interpreted?
2. How does the rotation in Section 5.2 contribute to accelerating the computation of expectation? Given two points $a$ and $b$, let $\mathbb{S}=\lbrace(1-t)a + tb|t\in [0,1]\rbrace$ be the segment connecting them, which is a one-dimensional element regardless of the dimensionality of the feature space. Finding the weighted average of $\mathbb{S}$ involves determining the expected position on the segment, which only depends on the variable $t$. An estimate can be acquired with a univariate Monte-Carlo estimator by interpolating between 0 and 1 for $t$. While the rotation in the paper appears to eliminate estimation variance in the aligned dimensions, it instead concentrates the variance in the final dimension, which is later redistributed to the others during the reverse of the rotations.
3. Could the authors elaborate more on sparsity? Line 376 says "the label-irrelevant generative factors are shared ensuring sparsity". According to Appendix.C.1, $z_u$ accounts for only one-fourth of the total latent encoding $z$. With modifications applied to $z_s$, which constitutes 75% of the latent features, the resultant counterfactual seems to deviate from the intended sparsity.
4. What do the different variants of $\mathbb{S}_1$ mean? Most of them are marked blackboard bold, with one exception at line 270 which is italicized. Some variants differ in the presence of the superscript $\mathcal{C}$.
5. The experimental results are appealing. To support the claim that the human-machine interaction serves as "a training process for the participants", could the authors provide the accumulated accuracies of initial user predictions over the number of seen instances?
6. Some parts of writing can be polished for clarity, for example:
    - Line 185 states "They propose to **apply to** the latent representation …" — it is unclear what is being applied.
    - The caption of Figure 6 reads “Labels are treated as a random variable to **also** sample.” — what does “also sample” mean?

### Soundness
2

### Presentation
3

### Contribution
2
