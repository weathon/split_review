# Targeted Model Inversion: Distilling Style Encoded in Predictions

- Decision: Reject
- Scores: 5, 8, 5, 6

## Abstract
Previous model inversion (MI) research has demonstrated the feasibility of reconstructing images representative of specific classes, inadvertently revealing additional feature information. However, there are still two remaining challenges for practical black-box MI: (1) reconstructing a high-quality input image tailored to the observed prediction vector, and (2) minimizing the number of queries made to the target model. We introduce a practical black-box MI attack called Targeted Model Inversion (TMI). Our approach involves altering the mapping network in StyleGAN, so that it can take an observed prediction vector and transform it into a StyleGAN latent representation, which serves as the initial data point for subsequent MI steps. Later, TMI leverages a surrogate model that is also derived from StyleGAN to guide instance-specific MI by optimizing the latent representation. These mapping and surrogate networks work together to conduct high-fidelity MI while significantly decreasing the number of necessary queries. Our experiments demonstrate that TMI outperforms state-of-the-art MI methods, demonstrating a new upper bound on the susceptibility to black-box MI attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a new model inversion (MI) attack leveraging StyleGAN as an image prior in a blackbox fashion -- i.e., without requiring access to the model's weights to compute gradients through it. The goal of a MI attack is to successfully reconstruct the input image to a classifier, based only on the predictions from it, as a result of which, MI can be used to recover samples from the training dataset, leaking potentially sensitive information (personal details, health scans, face images etc.). Developing better MI attacks are useful so they can be defended against more effectively for sensitive applications. 

While there has been significant progress in white-box MI attacks, black box methods still have a way to go because they are harder, and typically require several hundreds of thousands of queries for any reasonable inversion. Further, some existing methods tend to produce generic class-representative images, at the cost of intra-class differences, which undermines the goal of reproducing privacy preserving attacks. 

This paper presents a _Targeted Model Inversion (TMI)_  attack, that modifies StyleGAN's latent mapper ($g: \mathcal{Z} \rightarrow \mathcal{W}$), that goes from a random prior distribution (like Gaussian) to the W space of StyleGAN. The modified mapper, $m( . )$ directly predicts the $w \in \mathcal{W}$, which is then passed to the generator to obtain the image; this is trained by optimizing in the W space. A surrogate model, $f'$ is obtained by fine-tuning adapting the pre-trained discriminator to mimic the original model, while the images are sampled from the pre-trained StyleGAN.

### Strengths
MI is an important problem to study, especially considering the potential for damage that can be caused with sensitive data. The paper addresses blackbox MI attacks, which is a more practical scenario where the attacker only has access to the model via an API call.
* The use of StyleGAN as an image prior, and the discriminator as the surrogate makes intuitive sense, and exploiting it for MI is a realistic scenario.
* Use of a general, strong prior like StyleGAN also produces sufficient intra-class diversity  -- the empirical results also show that in terms of diversity TMI outperforms other whitebox methods, significantly which is encouraging.
* Evaluations are convincing, and the different metrics considered demonstrate the superiority of TMI over blackbox and whitebox methods. 
* The data efficiency for similar or better accuracy in MI attack over baselines is promising

### Weaknesses
 * **Image Prior** An unacknowledged weakness of the paper is the generality of the approach to a broader set of application domains. By choosing a StyleGAN prior, the applicability of the current method becomes restricted to the domains on which (or domains related to) to the StyleGAN's training distributions. The evaluations, and experiments -- while impressive are of less impactful in my opinion. 
* Two potential mitigation strategies come to mind -- (a) in order to work with more SoTA foundation models like StyleGAN-XL, the current approach will require to work with conditional generative models, which can make it much more potent and realistic; or (b) Leverage stronger inversion techniques on _unconditional_ StyleGAN that are able to invert arbitrary OOD images using pre-trained styleGAN as well -- for example 
	* GAN inversion for out-of-range images with geometric transformations, CVPR'21
	* Image2stylegan++: How to edit the embedded images?, CVPR'21
	* Improved StyleGAN-v2 based Inversion for Out-of-Distribution Images, ICML'22
* The examples of images that are "significant" deviation from the original dataset, unfortunately are not that OOD. It's well known that most encoders (including pSp or e4e ) do a reasonable job of inverting these paintings and other closely related domains. So i think a more accurate test of TMI will be to use a much more generic dataset, which will likely fail. 
* The feature distance measure appears to be poorly correlated to image quality -- i think the metric maybe misleading since an approach like AMI, which arguably fails on most of the evaluations conducted, has a reasonable F-dist score comparable or bette than some of the other baselines which are clearly better.

### Questions
In addition to some of my comments above -- 
* Can the ablations on query budget be done for one of the baselines as well to see how well (or badly ) they behave as the budget decreases?
* How does the surrogate perform on the original dataset? is it an actual surrogate in the sense that it come close to the original model's performance? this might be an interesting ablation as well. 
* A (non-technical) question -- is the use of gendered language for describing the attacker common? 

>"..where the adversary _(Eve)_ is able to.." 

>".. *She* uses $D_{aux}$ to train their *her* StyleGAN network".. 

I found that a bit odd but i am not closely familiar with how this is done in security and safety research so I will defer to the authors.

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
The authors seek to perform model inversion (creating the input that generated a prediction) by modifying a StyleGAN. Specifically, the StyleGAN mapping network is adapted to project a prediction vector into the GAN's latent space while the discriminator is adapted to be a surrogate model. Then to perform model inversion, a latent is created from the prediction vector and then optimized to generate an image that causes the surrogate model to emit a similar prediction vector. The authors are able to convincingly regenerate the input for a variety of  datasets.

### Strengths
I thought this paper was well-written, and the results were quite convincing. The method clearly outperforms other competing baselines, and is able to generate something resembling the model input. I appreciated that they chose two very different image datasets (celeba and chestxray). 

 I think this could also be neat as an interpretability tool (e.g., to generate what images are on the border between two classes).

### Weaknesses
What is an example scenario where we do have access to the full prediction vector (e.g., the probabilities and not just the most likely class) but we (a) do not have the input and (b) we have limited queries to the model?  

Regarding (b) I'm not sure query budget is necessarily the right metric (querying the surrogate model also takes time). It would be nice to see some scalability numbers on how long this method takes.

### Questions
How many queries do you have to perform to the surrogate model? I'd imagine that this can be just as expensive as querying the original model (if compute is the issue, I'm not sure "query budget" is the right metric to optimize).

How important is the surrogate model? If you used the original model instead (ignoring the query budget), how much better are your images?

Is this method specific to GANs (could you adapt one of the current off-the-shelf diffusion models for example).

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper tackles the problem of black-box model inversion. The objective is to obtain the input data sample (or its surrogates) corresponding to a given prediction. While it is an undesirable scenario, it is important to make the attacks stronger and more pragmatic to be able to construct better countermeasures. 

Previous methods on black-box model inversion are slow and do not often correspond to data samples that are specific to the given prediction. 

This paper claims to address these issues effectively by learning a surrogate StyleGAN generator, followed by transforming the label prediction vectors onto the latent space of the generator, to be used for image generation.

### Strengths
1. The idea of using a surrogate generator and operating on the latent space of the same is good. 

2. The paper positions itself well (describing the exact problem and gap in the literature). 

3. Writing is fairly good (despite typos).

### Weaknesses
1. Dependence on a surrogate generator (and dataset).

2. Increased space-complexity.

3. Sloppy notations and incomplete math.

### Questions
1. The main problem I have about this method is that this demands training of a StyleGAN on a  dataset ``similar'' to that used in the predictor. This is not a fair assumption in my opinion. While the Authors do argue that the attacker can "leverage a pre trained StyleGAN network available on the Internet", it is a weak argument. How would the attacker know which dataset is ``similar" to the one used in the predictor? More grounding is needed in this respect, seems too handwavy currently.  

2. Adding to the above point, the proposed method imposes an additional space constraint, in terms of the large stylegan that is to be trained. 

3. Given the above two points, I do not see the comparisons to be fair as the proposed method has the luxury of using an additional full-blow generator network which the previous methods don't have. Therefore, I recommend that the Authors have to try modifying the other methods while they have access to a generator, albeit on a surrogate dataset.

4. The method seems very stylegan specific. Can a different GAN architecture be used? I am asking specifically because, in my experience, the latent spaces of other GANs are not as versatile as that of StyleGAN. 

5. The description of the method has to be more formal. For instance, before Eq. 2, it is said that there is a loss function that is getting minimized. The optimization problem has to be stated neatly (using formal math). 

6. A lot of mathematical details are missing - What is the expectation over, in Eq. 2 and 3? As I understand, they both are over two different distributions but are not mentioned. 

7. While the Authors show a few images when there is a distributional shift between the surrogate model and the predictor, it is very minor and insignificant in my opinion. Both the datasets are facial images. What happens if you take a stylegan trained on cars dataset and use it for a predictor trained on human faces?

Overall, while the method is interesting, I have reservations about recommending it for acceptance given my concerns above. I shall wait to see other reviewers' comments and discussions with authors before making up my mind. Right now, I am leaning towards rejecting it.

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
The paper introduces a new Model Inversion (MI) method that exploits the hierarchical latent features of a separately trained StyleGAN architecture. A goal of MI is to recover the input x of a classifier given the output probability vector y. The MI model can then be used for malicious attacks aimed at extracting private information, since the predictions y are easier to obtain than x in most privacy regulations. The new MI methods show substantially higher performance than a wide range of both black-box and white box baselines on several image datasets.

### Strengths
- The approach is simple but well-motivated.
- The recovered images are substantially better than the baseline models both qualitatively and quantitatively. 
-The paper is well-written and the methodology is well-explained. 
-The experiments are rigorous and rather comprehensive.

### Weaknesses
I am struggling to find a good societal application of this work as the explicit aim of the paper is to improve performance of a family of malicious attacks that can be used to leak private information. While I do agree that open research on attacks is important, it seems to me that this work is very helpful to potential attackers while not providing any real insight concerning possible defense strategies.  Note that the paper does not introduce a conceptually novel way to perform attacks, which would provide important information to the public. Instead, it offers a highly optimized approach that exploits several, rather standard, techniques. For this reason, I am not convinced that a paper like this has a place in a machine learning conference.

I do appreciate the technical skills shown by the authors, I think that equal effort should be spent in considering the societal implications and in discussing possible defense strategies.

Apart from ethical consideration, I find the domain of application to be rather narrow and more suitable for a more specialized venue. All in all, the paper does not introduce any conceptually new technique since the use of proxy classifiers and generative models is common in the reconstruction literature.

### Questions
Could you discuss the ethical implications of your work and provide some insights concerning possible defense methods?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
