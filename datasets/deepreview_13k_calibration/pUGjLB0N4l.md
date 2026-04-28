# Big Learning Variational Auto-Encoders

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 5, 5, 3

## Abstract
As a representative latent variable model, the Variational Auto-Encoder (VAE) is powerful in modeling high-dimensional signals like images and texts. 
However, practical applications often require versatile data capabilities, such as conditional generation/completion, inference with incomplete/marginal data, \emph{etc}, which are challenging to harvest from a conventional/joint VAE.
To satisfy those requirements, we leverage the recently proposed big learning to upgrade the joint VAE to its big-learning variant termed BigLearn-VAE, which delivers joint, marginal, and conditional generation/completion, inference, and reconstruction capabilities, simultaneously. 
In addition, we also reveal that the BigLearn-VAE can be constructed based on one foundation model, manifested as one universal model possessing plenty of versatile capabilities. 
Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a modification to the Variational Autoencoder (VAE) framework by incorporating conditional encoding and decoding processes capable of handling incomplete data inputs. Here's a summary of the modifications:

Conditional Encoder: Instead of requiring a complete data point 'x', the new encoder can work with partial data. It is designed as a transformer architecture, where missing values in 'x' are masked. A special 'CLS' token is used in the final position to generate a probability distribution over the latent variable 'z'.
Conditional Decoder: The decoder is adapted to accept both the latent variable 'z' and a partial 'x'. It then reconstructs the missing components of 'x' sequentially. This is achieved through a transformer setup with masking for the missing values, using an index-based approach to handle the decoding of missing elements of 'x'.
Additionally, the authors introduce a distribution over which positions in the input are missing. The decoder is trained across all possible combinations of missing and present data.

### Strengths
It is an interesting and novel idea to train the VAE across all possible combinations of missing and present data, thereby learning a comprehensive generative process even with incomplete inputs. This approach enhances the model's capability to handle and predict missing data within a given dataset.

### Weaknesses
The primary contribution of the paper is section 3.2.2 which is filled with inconsistencies
 1) > $\text{The marginal } p_\theta(x_T, z) \text{ is readily derived from the joint } p_\theta(x, z) \text{ via index selection with } T; \text{ with specific } T = L, \text{ the MarginELBO in (4) reduces to the JointELBO in (1);}$

Note that none of these group of distributions are consistent wrt each other. Consider a 2 dimensional x = (x1, x2), then 
$$p(x1| mask, x2, z)p(x2|mask, mask, z) \neq p(x2|x1, mask, z)p(x1|mask, mask, z)$$

So, unlike expected by the authors, this approach doesn't allow for modelling arbitrary conditional distributions $p(x_T|x_S, z)$

 2) > $\text{Both optima have already been modeled in the parameterized } p_\Phi(z | x_{S'}).$

This is incorrect. The definition of optimal $q_M(z|x_T)$, that is, $p_\theta(z|x_T)$, is a distribution that follows from Bayes' rule, that is
$$p_\theta(z|x_T) \propto p_\theta(x_T|z)p(z) $$
$p_\Phi(z | x_{T})$ doesn't model this distribution 

3) The notations used throughout the paper are very confusing. The same q had been used to represent the emprical data distribution, the posteriors and the distribution over indices q(S,T). 

4) The writing of the paper can be improved. Primarily, it is not a good idea to present the paper as a special case of big-learning [1] (an unknown unpublished/rejected work that claims to be all-encompassing). I tried reading the big-learning paper but there were too many errors in that paper to go-through.

### Questions
1) How is q(S,T) chosen in equation (7)? 
2) What is index-based decoding mentioned at the beginning of page 6?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present "Big Learning" variational autoencoders that attempt to train VAEs and their respective marginals and conditional distributions simultaneously.  The aim is to demonstrate that such an approach is better able to handle incomplete data than vanilla VAEs.  Experiments are designed to validate these claims.

### Strengths
The key idea is simple, and it extends the capabilities of VAEs -- effectively transferring computational time from inference to training time.

### Weaknesses
The novelty of this work is a bit limited over top of Cong and Zhao, 2022.

The main idea is relatively simple, but the explanation of that idea is a bit rambling.  In particular, I found Definition 1 initially confusing. The presentation would benefit from a clear problem statement.

The performance comparison in Figure 2 shows comparable performance to the vanilla VAE (which honestly isn't that surprising given the training setup). These are really the only quantitative results.  To me, it makes more sense to compare against the sampling methods that provide similar capabilities to the big learned model.  In a sense, this approach is pushing the computational load to the training phase instead of the inference phase, which makes sense, but you'd still want to verify that the resulting model has competitive performance on the proposed task against existing approaches.  

Overall, I found the experiments a bit underwhelming and the details of the experimental setup/evaluation are scant.

### Questions
See the above.  

Additional questions:
-  What is the difference in training time between the vanilla VAE and this approach? 


Minor typos/suggestions:
-  The citation style is not correct.  Please use parenthetical citations instead of in-text citations to make the paper more readable.
-  "-in-paining" -> "in-painting"
-  "review the preliminary Variational"
-  "be selected base on"
-  "space is important and many works" -> "space is important, and many works"
- "can not" -> "cannot"
- "one need two foundation"

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed the BigLearn-VAE, inspired by the big learning theorem.  The paper presents extensive analysis and derivation associated with how BigLearn-VAE is motivated, and presents empirical evidences to justify the effectiveness of the method.

### Strengths
S1: The paper introduces the BigLearn-VAE, drawing inspiration from the big learning theorem. 

S2: It provides a comprehensive analysis and derivation of the underlying principles driving the BigLearn-VAE approach, supported by empirical evidence that substantiates its efficacy.

S3: Empirical evidence shows that the proposed method achieves better ELBO than the vanilla VAE model. The proposed method also can lead to better (visually) generative samples.

### Weaknesses
However, the paper seems to lack clarity, which makes the algorithm flow hard to interpret. For example, some of my confusions (owing to the clarity issue) are: 

W1: Take for instance, what exactly is the conditional distribution $q(x_t, Z| x_s )$ is, and how to sample from it? I am confused why samples $x_t$ should be dependent on other samples such as $x_s$ rather than independent with each other. 

W2: This model seems to be exactly the same as in the conditional VAE, e.g., CVAE in [A]. Can you please distinguish your Biglearn with the work in CVAE [A] ?

W3: It seems the algorithm is only compared with vanilla VAE, whereas there have been many other SOTA version of VAE. The empirical evidence does not address the comparisons with these methods. 

W4: An algorithmic flow will probabaly help in terms of clarity when presenting the sampling procedure. 

### Questions
Please see the 4 weakness above for my questions. Please correct me during rebuttal if I misunderstood anything.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies learning the Variational Auto-encoder (VAE) with the "Big-learning" scheme, which is inspired by the foundation models. Such a learning scheme aims to exploit the large-scale training data with diverse domains exhaustively. The experiments demonstrate the inference capability of such learned VAE.

### Strengths
1. The motivation for learning a robust VAE is clear and can contribute to such active research fields for generative models. 
2. The organization of the paper is generally well-presented.
3. Although I have only limited experience with such a "big-learning" scheme, I feel like the potential of VAE should be further explored, as many prior works did, and this paper addresses this with a promising direction in a big picture.

### Weaknesses
1. I don't have much experience in this particular field, so it is quite difficult for me to follow the paper. The authors intend to apply a robust and general learning scheme for the VAE, with exhaustive data utilization in a multi-modal learning manner (e.g., text and image domains), but some notations seem to be confusing, such as the "joint matching" for marginal distribution p(x). Specifically, the paper needs to clarify how the joint distribution of the complete data p(x), which includes both observed and unobserved modalities, is modeled and how this relates to the marginal distribution p(x_T) where T represents a subset of modalities. The explanation of how the model handles missing modalities during training and inference is also unclear. It is not immediately obvious how the model ensures consistency between the joint and marginal distributions, especially when dealing with diverse data types.
2. With such a powerful learning scheme, the experiments only demonstrate the inference capability. So I wonder how such a learned VAE performs for generation quality, cross-domain sampling, adversarial robustness, and other standard benchmarks. The paper lacks a comprehensive evaluation of the generative capabilities of the proposed VAE. While the inpainting task demonstrates a form of conditional generation, it does not fully explore the model's ability to generate novel samples from the learned latent space. Furthermore, the absence of experiments on cross-domain sampling, adversarial robustness, and other standard generative model benchmarks raises concerns about the practical utility and robustness of the proposed approach.

### Questions
Please see the Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose big learning VAE to model the inputs from a more general and universal loss perspective. The authors introduce some high-level ideas on big learning, whose objectives should comprise of joint, conditional, and marginal matching tasks. The paper mostly explains the motivation and insights of such big learning concept. The contents also mostly summarizes all different VAE objectives. The final proposed biglearn-VAE is validated on MNIST, FashionMNIST and CelebA, on some inference and in-painting tasks.

### Strengths
1. The paper provides and describes many insightful thoughts regarding the universal learning objective for VAE. 
2. The core notations and concepts are explained in a self-contained manner.
3. The experiments showcase some capabilities of biglearn-VAE.

### Weaknesses
1. Many claims are made on top of the ideal assumptions, while such assumptions are usually hard to achieve. Actually, VAE framework itself is developed based on the fact that $p(x)$ is intractable.
2. Even though you are proposing some universal framework, it's still better to introduce some running examples to facilitate the understanding of your claims. For example, you can use a MNIST example for illustration of different modeling scenarios.
3. During my reading, I do have a feeling that you are more or less re-introducing big learning from a high level, without more concrete or statistical analysis.
4. Section 3.2.3 essentially proposes a more general form of VAE ELBO. However, regarding the specific cases, one still have to reduce the form to more specific ones that we are more familiar with. Moreover, when you claim sth big, readers expect some more convincing and comprehensive experimental results.
5. MNIST, FashionMNIST are well-studied datasets. I'm not sure if they really need large foundation models.
6. Also, the major results you are showing are mostly qualitative, lacking more concrete quantitative ones.

### Questions
1.Have you tried your method on some larger-scale datasets?
2. You mentioned text tasks multiple times in the paper, however, there is no text applications in the experimental section?
3. As you mentioned the utilization of large foundation models, maybe it's more convincing if you can give a use case?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
