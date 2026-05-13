# Exploring Diffusion Time-steps for Unsupervised Representation Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Representation learning is all about discovering the hidden modular attributes that generate the data faithfully. We explore the potential of Denoising Diffusion Probabilistic Model (DM) in unsupervised learning of the modular attributes. We build a theoretical framework that connects the diffusion time-steps and the hidden attributes, which serves as an effective inductive bias for unsupervised learning. Specifically, the forward diffusion process incrementally adds Gaussian noise to samples at each time-step, which essentially collapses different samples into similar ones by losing attributes, \eg, fine-grained attributes such as texture are lost with less noise added (\ie, early time-steps), while coarse-grained ones such as shape are lost by adding more noise (\ie, late time-steps). To disentangle the modular attributes, at each time-step $t$, we learn a $t$-specific feature to compensate for the newly lost attribute, and the set of all $\{1,\ldots,t\}$-specific features, corresponding to the cumulative set of lost attributes, are trained to make up for the reconstruction error of a pre-trained DM at time-step $t$. On CelebA, FFHQ, and Bedroom datasets, the learned feature significantly improves attribute classification and enables faithful counterfactual generation, \eg, interpolating only one specified attribute between two images, validating the disentanglement quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a unique perspective on exploiting the image-noise ratio across different time steps in diffusion models and offers a framework for learning useful and disentangled representations from diffusion models. The authors argue that as t increases, images progressively loss information starting from details to global structures during noise injection, and learning a complementary feature representation conveying the corrupted information can help make the representation more disentangled. Experiments are performed on multiple image datasets.

### Strengths
1. The idea of systematically studying the representation changes during the noise injection of diffusion models is interesting and has great potential in further understanding the diffusion models. 

2. The paper is written in good presentation quality in general. The definitions such as attribute loss are adequately formulated and illustrated with figures. 

3. The quantitative results in Table 1 seem strong. 

4. The method is built on top of pretrained diffusion models, which I believe can help reduce the cost of representation learning.

### Weaknesses
The empirical discussions on counterfactual generation (section 5.3) are relatively weak as the effectiveness is only supported by a few examples. Especially for the bedroom experiments, I personally feel like it's not easy to justify the authors' claim that 'DiTi is the only method that generates faithful counterfactuals' based on the given examples.

And since this paper focuses on unsupervised representation learning, more empirical results regarding how the learned disentanglement can improve the overall representation quality can be a huge plus. 

For example, do the learned disentangled representations enable human intervention to mitigate spurious correlations?

How is the quality of the representation when evaluated in a more general setting such as ImageNet-style recognition?

One concern I do have is that as diffusion is trained by image reconstruction, the learned feature will inevitably contain considerable information regarding the background (probably in late step t), and how will this affect the general representation quality?

### Questions
Could the authors provide a brief discussion for [1]?


---
[1] Diffusion Based Representation Learning, arxiv

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work aims to disentangle the modular attributes in the DDPM framework by exploiting the granularity of feature details at different time steps of the diffusion models. The work finds that the fine feature components are encoded in the earlier time steps of the forward diffusion process while the coarse details are at the later time steps. A encoder decoder approach with partitioned features  at different time steps are proposed to allow for disentangled representations. Experiments are performed on bedroom, CelebA and FFHQ datasets where the method outperforms prior art.

### Strengths
+ The paper is well-written and easy to read. The motivation of the work related to learning the disentangled modular attributes in diffusion models is promising. Claims are supported with theoretical reasoning. 

+ The experiments are performed on different face datasets such as CelebA, FFHQ, and the Bedrooms dataset. The approach outperforms prior work on metrics such as AP, Pearson-r, and MSE. 

+ Ablations are provided regarding the choice of partitioning and optimization strategies.

### Weaknesses
- The qualitative results shown in figure 5 do not show consistent improvements wrt to modular editing. In the second row, for example, the eyeglasses appear in the middle range and disappears again in the final ranges.  Are the time steps plotted in a cumulative fashion within the  early/middle/late “t” range. 

- On the use of timesteps [100-300] and it corresponding to the maximum value of the loss: One would expect the loss to be greater at the later stages when the image becomes complete noise. Eg: it should be difficult to construct image from t =1000 to t =700. Can a plot be included for different samples to validate this? 

- Comparison to SIMCLR: SimCLR does obtain a higher accuracy on attributes affecting local appearances (e.g., “Hat”). We postulate that its contrastive training has some effects in regularizing f as an injective mapping” . This is not clear. What is being implied in these findings. Does this mean that the proposed approach depends on attribute correlations?

### Questions
- From point 2 above, it will be great to include the plot to validate the time steps and loss. 
-The results presented in the manuscript hold for unconditional models. Do the findings also extend to conditional models? 
Also see weaknesses above.


Minor: The equations are missing parenthesis on expectation.

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
This work proposes DiTi, a method that learns disentangled representations in an unsupervised fashion. The work first provides insights into the inductive bias of Denoising Diffusion Probabilistic Models that can be leveraged for learning decoupled features, with theoretical grounding. Then the work proposes to leverage the inherent connection between timesteps and modular attributes to learn a set of features from the residuals. Finally, the feature can be used for both downstream inference (e.g., attribute prediction) and counterfactual generation, surpassing prior works in both tasks.

### Strengths
* This work provides a link between the timesteps and the modular attributes with an intuitive explanation and theoretical proof.
* This work proposes a simple yet effective approach to learn disentangled features along with the diffusion model training that follows from the discoveries during the analysis.
* This work outperforms previous unsupervised feature learning methods that do not disentangle the features on attribute classification tasks. This work also shows higher-quality counterfactual generations compared to previous works.

### Weaknesses
 * This work trains models from scratch. Due to the introduced term for disentangled feature learning, the model needs to be re-trained. Specifically, the method requires training a feature extractor alongside the diffusion model, which necessitates additional computational resources and time compared to methods that leverage pre-trained diffusion models directly. This retraining requirement poses a barrier to adoption for researchers with limited computational resources, as it prevents the direct use of publicly available pre-trained diffusion models.
* The authors only evaluated the proposed method with datasets that are domain-specific (e.g., CelebA, FFHQ). The method has not been evaluated on large models trained on more diverse and general image datasets (e.g., LAION). Therefore, it does not indicate whether the method can scale to more complicated settings. The reliance on datasets like CelebA and FFHQ, which are relatively narrow in scope, limits the generalizability of the findings. It remains unclear how the proposed disentanglement approach would perform on datasets with more complex and varied image content, such as those found in LAION or ImageNet.

### Questions
* Do the subsets have to be uniform? Does it benefit the method if we have more features for coarser or finer features?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
I was one of the reviewers for this paper for NeurIPS 2023, I have carefully revisited the paper again for the ICLR submission, and write my new reviews as below.

This paper studies unsupervised representation learning with generative diffusion probabilistic models with specific exploration of the diffusion steps. The main research idea originates from the observation/assumption that image attributes are gradually lost along the diffusion process with increasing levels of Gaussian noises. The authors propose DiTi (named after Diffusion Time-step) to learn a step-specific feature to capture the information of lost attributes, and then leverage this feature of modular attributes as the inductive bias for unsupervised learning. Experimental tests of the feature are conducted on two settings, namely the attribute classification and counterfactual generation.

### Strengths
- The paper elaborates well on the concept of attribute loss, which is the fundamental observation for the proposed DiTi method, and is in general easy to follow.

- The idea to learn a step specific feature to encode the lost attribute information as the inductive bias for unsupervised learning is reasonable and intuitive.

- Experimental results show improvement over several baseline methods on CelebA, FFHQ and LSUN-Bedroom datasets.

- Compared to the previous manuscript from NeurIPS, it seems that the authors have incorporated the comparison of the proposed work with several existing works that touch on the representation learning with DMs, which helps to clarify the differences between this paper and existing literature (but this part is also a little biased, as specified below).

### Weaknesses
Since this is my second time reviewing this paper, I think most of my questions concerning the technical details have been resolved and clarified. While I acknowledge that the paper is well-written and has its merits to enlighten the studies of combining representation learning and diffusion models, there are a few of my concerns.

- First, I echo with my previous NeurIPS reviewers folks on the concern: whether it is the direct direction to actually integrate DMs into the current representation learning paradigm? Based on our previous discussions, the proposed method has a higher computational/time cost compared to its contrastive counterparts. And if the argument here is because the contrastive paradigms lose attribute information, then it seems to me the proposed DiTi may not be the optimal method to introduce the attribute inductive bias. The core issue remains that the computational overhead of diffusion models, even when leveraging a pre-trained model, is substantial compared to contrastive methods. This makes it less practical for large-scale representation learning tasks where efficiency is paramount. Furthermore, while the authors claim that contrastive methods lose attribute information, it is not clear that the proposed method is the most efficient way to address this, as other techniques might be more computationally viable.

- Second, in the related work section, the authors include a comparison with the current DM for representation learning methods. I find this new part slightly biased, because the approaches in 2) and 3) are not really proposed under the context of representation learning. For instance, (Kwon et al., 2022) proposed the bottleneck feature of the U-Net under the context of image editing; similar to (Preechakul et al., 2022), in which separate autoencoders are learned to achieve editing purposes. I think while these works do touch the latent features/attributes in DMs, they tackle different scenarios other than representation learning. In other words, the first concern is not resolved by comparing these works. The comparison with methods focused on image editing or manipulation using diffusion models is not directly relevant to the core problem of representation learning. These methods, while utilizing diffusion models, have different objectives and therefore do not serve as a fair comparison for the proposed approach. The inclusion of these works does not address the fundamental concern about the efficiency and practicality of using diffusion models for representation learning.

- Going towards the technical level, one concern (less urgent in my sense) is that the proposed DiTi method shares quite similarities with PDAE, with the main difference in the disentanglement, with the cost of more hyper-parameters. The reliance on PDAE's architecture and hyperparameter choices, while potentially simplifying implementation, raises questions about the novelty of the approach. The disentanglement aspect, which is the main contribution, comes at the cost of additional hyperparameters, which may require careful tuning and could limit the generalizability of the method.

### Questions
In general, I don’t have specific questions to ask at this time and still have mixed feelings as in my first-time review of this work. I think this paper has its own merits/advantages and drawbacks/disadvantages at the same time, and thus keep my tentative rating as borderline but will update it according to other reviewers and further discussions later.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
