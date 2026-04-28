# Information-theoretic Generalization Analysis for Vector-Quantized VAEs

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Encoder--decoder models, which transform input data into latent variables, have achieved a significant success in machine learning. Although the generalization capability of these models has been theoretically analyzed in supervised learning focusing on the complexity of latent variables, the contribution of latent variables in generalization and data generation capabilities are less explored theoretically in unsupervised learning. To address this gap, our study leverages information-theoretic generalization error analysis (IT analysis). Using the supersample setting in recent IT analysis, we demonstrate that the generalization gap for reconstruction loss can be evaluated through mutual information related to the posterior distribution of latent variables, conditioned on the input data, without relying on the decoder's information. We also introduce a novel permutation-symmetric supersample setting, which extends the existing IT analysis and shows that regularizing the encoder's capacity leads to generalization. Finally, we guarantee the 2-Wasserstein distance between the true data distribution and the generated data distribution, offering insights into the model’s data generation capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors study the generalization capabilities of autoencoder models using the "supersample" setting from statistical learning theory. In the supersample setting, we assume we have a dataset, and we randomly select half of the data to train our model and use the other half for testing. Then, supersample bounds aim to show that the generalization error of our models is upper bounded by the amount of information the model's test loss reveals about how we created the train-test split.

The authors prove such supersample bounds for the settings where the generalization error is measured by the model's average reconstruction loss and the 2-Wasserstein distance between the ground truth data distribution and the model's reconstruction distribution.

### Strengths
The authors' bounds are unique among supersample generalization bounds in that they explicitly involve the information gain between the train-test split mask $U$ and the latent variables of the generative model $J$.

I have skimmed the proofs in Appendix C, which seem correct.

### Weaknesses
As someone who does not work directly on supersample methods but has past experience with statistical learning theory, I find the significance of the authors' results for the ICLR community unclear.

This assessment is due to a combination of two factors: 1) on the theoretical side, the authors' results for bounding the generalization error involve practically incomputable quantities and only work under restrictive assumptions. In particular, I find the supersample setting quite artificial. 2) The authors' experiments appear to show that their bounds are extremely loose, as they are four orders of magnitude larger than the generalization error they are attempting to upper bound.

As such, I don't believe that the authors' results support the practical design principles they advocate for, such as "To improve the generalization and data generation capabilities, it is desirable to use a complex decoder..." on line 436. The issue with this statement is that given how loose the authors' bounds are, following this advice (in the context of the paper) is only useful to make the bounds less vacuous and is far from guaranteed to lead to practical benefits. To make such claims, the authors would have to perform more detailed experiments demonstrating that this advice leads to improvements.

In a similar vein, as the last sentence of the abstract, the authors claim, "Finally, we guarantee the 2-Wasserstein distance between the true data distribution and the generated data distribution, offering insights into the model's data generation capabilities." - in a similar manner as above, after reading the paper, I do not feel like the authors' results bear out this claim.

As things currently stand, I believe the paper is much better suited to a more specialized venue, such as COLT; this would also allow their claimed results to be scrutinized much more.

The paper's presentation could be improved a lot as well. The biggest missing component is providing intuition about the quantities and results; the authors should spend a lot more time explaining (to a machine learning audience) why the settings and results are sensible. I also suggest that the authors merge Section 1.1 with Section 3.4 and rewrite it in the same style, meaning that not only do they list the related works but also say how their own work is different. Wading through the literature review in the introduction is quite challenging and does not add much value to the paper.

### Questions
n/a

### Soundness
3

### Presentation
1

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
The authors present an information-theoretic generalization analysis for VQ-VAEs, focusing on the role of latent variables. The authors develop a novel generalization error bound using IT analysis, which evaluates the reconstruction loss without using the decoder. They also introduce a permutation-symmetric supersample setting, which in turn allows for controlling the generalization gap by regularizing the encoder's capacity. In addition, the authors provide an upper bound on the 2-Wasserstein distance between the true and generated data distributions, supporting insights into the model’s data generation capabilities.​

### Strengths
* The authors present novel theoretical bounds on the generalization of VQ-VAE. providing insights that can potentially lead to improved data generation capabilities.
* The task of deriving practical bounds for useful models such as VQ-VAE is Herculean, and when successful can have large impact. This paper can potentially be a step towards such bounds.

### Weaknesses
 * The assumption of discrete latents and Gaussian decoder are very strong (I want to commend the authors for pointing them out), and as such are leading to interesting bounds but with limited practical use (e.g., decoder based on normalizing flows or over discrete data cannot   be used in this setting).
* The MI estimator (Kraskov) will not work for high dimensional data or data that is far away from uniformity (i.e., highly clustered). This puts strong limitation on the applicability of the method in the general case.
* A major issue with the paper is the limited experimentation setting. The experiments focus on the generalization gap but fail to show the implication in practice for the quality of the generation. That is, how a tighter bound on the generalization gap can be used in practice, for instance to predict the usefulness of the learned representations in downstream tasks, or the quality of the generation samples. 
* Also, the choice of MNIST (a simple dataset that can often lead to conclusions that do not generalize to more complex data such as ImageNet) is falling short in demonstrating that the proposed analysis is practical for more complex datasets.

### Questions
* Did you try more complex datasets, other than MNIST?
* Can the method be used with an auto-regressive Gaussian decoder?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this article, the authors provide various bounds on the generalization and generative capabilities of encoder-decoder models, and support some of their findings with numerical experiments. Specifically, the study focuses on encoder-decoder models in an unsupervised setting with a discrete latent space. The authors present novel bounds that emphasize the role of latent variables.

Using what is known as the "supersample setting", the authors derive an upper bound on the generalization error that does not depend on information from the decoder. Additionally, by introducing a new setting, referred to as the "permutation symmetry (supersample) setting", the authors establish a new upper bound that vanishes as the number of samples increases, provided appropriate regularization is applied. This bound underscores the benefits of regularization in these models.

Their final bound addresses the generative capability of the model: the 2-Wasserstein distance between the true and generated distributions is shown to be upper-bounded. Notably, the authors' analysis includes the fact that the models are trained. Lastly, the authors estimate the quantities appearing in their bounds on real models, demonstrating that the model behavior aligns with their theoretical bounds.

### Strengths
The paper is well-written, with a clear structure, precise notation, and sound results. The studied models - encoder-decoder models with discrete latent variables - are not only of theoretical interest but have also shown strong empirical performance, making them deserving of attention. This study builds on and extends previous work by incorporating the effects of training and focusing on the role of latent variables. Additionally, the authors introduce a novel setting, the "permutation symmetry supersample setting," which enables new proofs for bounds. The proofs are clearly explained in the appendix. Overall, this work represents a valuable step toward a better understanding of the theoretical capabilities of encoder-decoder models.

### Weaknesses
My main criticism of the work lies in the numerical experiments. The increase in log K (line 468) seems to be provided with relatively limited numerical evidence. There are only four data points, and no fitting or estimation is conducted to verify if the obtained points indeed behave as log K. Moreover, the behavior in log K could be better highlighted by appropriately adjusting the scales on the plot. Additional data points for both Figures 1 and 2, and an increased K range for Figure 2, would, in my opinion, provide more solid evidence. Specifically, the right-hand side of Figure 2, which shows the KL divergence, is not discussed in detail, and its relationship to the other plots is unclear. It is also not clear if the log K behavior is a theoretical result or an empirical observation.

As a second criticism, while the formal results appear mathematically sound, their interpretation is sometimes vague or overstated. For example, the phrase "obscuring the role of latent variables" (lines 97–98) is somewhat unclear, and the term "comprehensive" (lines 97–98) also seems exaggerated, given the limitations in the considered setting and the lack of evidence that better bounds could not exist. I would recommend clarifying that these interpretations arise from bounds and should be viewed as "hints" toward the true behavior of the generalization or generative capabilities. The claim that the encoder determines the generalization capability (as stated in the response to lines 97-98) is not fully supported by the current analysis, as the bounds still involve terms related to the decoder, even if indirectly. The interpretation of the bounds should be more nuanced, acknowledging that they provide insights into the role of the encoder but do not entirely isolate it.

This also leads me to reflect on the significance of the work: while the new bounds improve upon previous bounds and extend the setting, and the novel idea in the proof—the "permutation symmetric setting"—is valuable, the insights provided by these bounds into the workings of encoder-decoder models seem moderate. However, given my limited knowledge of the literature in this domain, I may reevaluate my opinion on the significance of this work, whether in its mathematical contributions or its interpretation, after discussion with the authors.

Some more specific comments, reflecting the points above, are provided in the next section. In particular, some parts of the appendix are lacking in clarity and seem unpolished (e.g. 1012-1019 seems unfinished).

### Questions
Comments, Questions, and Suggestions:
- Lines 97–98: This is discussed later in the manuscript, but it might be helpful to clarify earlier what is meant by "obscuring the role of latent variables." Why is it problematic that the bounds depend on the learned decoder parameters?- 
- Line 115: This claim should be nuanced. Perhaps specify the setting and its limitations. The term "comprehensive" might be an overstatement, as there are limitations in the considered setting (e.g., finite latent variables, as mentioned on page 9).
- Line 185: It may help to provide additional details on how you translate the theorem from Hellström & Durisi (2022) to your setting, as there is no "R" term, no 1/n, and no summation.
- Lines 263–269: This part is confusing: why do you mention f_\phi just after the deterministic decoder? Did you mean the encoder? What is obtained by using Theorem 8 from Hellström & Durisi (2022)? Be more precise about the regularization required for the result to hold.
- Line 270: Do you have only numerical evidence that the empirical KL term is much larger than the CMI? Please clarify.
- Lines 274–279: What exactly do you deduce from the use of the Vamp prior in Theorem 2? Specify what you prove in Appendix C.3.
- Line 312: Similar to before, why is f_phi referred to as the decoder?
- Line 330: "whereas the decoder's capacity does not affect the generalization gap" — can you confirm this applies only to this specific bound? In other settings, the decoder's capacity could impact the generalization gap. If so, consider nuancing this sentence.
- Lines 340 and 347: Perhaps clarify that the theorem does not provide quantitative information on the amount of improvement.
- Line 352: Could you clarify what is meant by the "stability of KL divergence under different data points"?
- Line 440: What does "highlighting [...] of the latent variables as the regularization" mean? Which regularization is being referred to?
- Lines 453–454: "the excellent generalization performance" — Please specify a point of comparison; excellent compared to what? Additionally, avoid using "excellent" here.
- Line 455: "Elucidate" may be too strong a term.
- Line 464: Could you explore using a prior other than the uniform distribution? Is it feasible to implement a prior in the supersample setting? If not, clarify this here. The discussion on line 482 might fit better here.
- Line 467: If the claim "This result indicates that our bound increases only by log K " is based solely on Figure 2, it seems to have relatively limited evidence. Either significantly nuance this claim or generate additional data (e.g., for a larger K and a plot that better highlights the log behavior).
- Line 474: "first comprehensive analysis" — As in the introduction, "comprehensive" may be overstated. Specify here that the study focuses on quantized encoder-decoder models rather than general encoder-decoder models. Briefly mention the bounds provided by your analysis.
- Line 778: Consider providing more detail on how you use the sub-Gaussian property.
- Line 798: Could you clarify why the inequality in line 795 demonstrates that the decoder information cannot be eliminated from the naive IT bound? From what I understand, we have gen<=Delta \sqrt(2/n ... <= I(theta...)+I(e_J...), but the fact that I(theta…) appears here does not necessarily show that it influences the naive IT bound.
- Figure 1: Please add a note in the legend about where to find definitions of the different terms.
- Figures 1 and 2: Please specify what the gray and red areas represent (I assume these are standard deviations). Is there no standard deviation for the CMI/n vs. n curves?
- Figures 1 and 2: Are there specific reasons why there are only four points per graph?
- Lines 1012–1019: This section seems incomplete.
- Appendix D1 Proof: It could be helpful to divide the proof into steps with more explanation.
- Line 1088: "Finally, we remark the CMI of Eq. (7)." — This phrase is unclear; please clarify.
- Line 1662: Is there a reason for not using more samples?
- Line 1663: The dataset splitting method is unclear. Section 2.2 does not mention validation datasets. How do you transition from {1000, 2000, 4000, 8000} to [250,1000, 2000, 4000]?
- Line 1670: Did you observe that the training loss stopped decreasing after 200 epochs? What is the rationale for choosing this number of iterations?
- Line 1688: Could you provide more details on how mutual information was estimated? This paragraph lacks specificity.

Typos and Suggested Reading Improvements (No response needed for these; ignore if irrelevant):
- Lines 38 and 607: Grnwald → Grünwald
- Line 145: It might help to specify that "randomized algorithm" is defined in Section 2.2, as this could confuse readers otherwise.
- Line 152: Typo: ", fo" → ". For"
- Lines 174–175: Clarify "associated" in this context; it may be clearer to define only U in this sentence, and its purpose becomes obvious just by continuing reading.
- Line 231: Typo: "information;" → "information."
- Line 238: Typo: missing second "|" in KL term.
- Line 247: Rephrase as "Since [...] are equivalent, we can express the first term [...]"
- Line 330: Typo: "deconder" → "decoder"
- Line 350: Typo: missing "|" in KL divergence term.
- Line 354: Typo: ";" should likely be ":".
- Line 446: Typo: "Of our provided in" → unclear phrasing.
- Line 453: Typo: "relaxation Jang et al. (2017), ..." → "relaxation (Jang et al., 2017, ...)"
- Line 453: Typo: "the excellent" → "an excellent"
- Line 561: Is the URL necessary here?
- Line 607: Verify the second author’s name.
- Line 632: Typo: "Natarajan" should be capitalized.
- Standardize author name formatting in the bibliography (either use full names or initials consistently).
- Line 772: Possible typo: X should consistently use a tilde in this line and the next.
- Line 772: Possible typo: J_mm  should have a bar at the end.
- Line 810: Should this be "generalization gap"?
- Line 830: Should it be J_n instead of j_n
​-  Equation 11: Indicate here that the 2nd and 3rd lines yield zero if that’s how the term was obtained.
- Line 863: Typo: only one "|" in KL.
- Line 882: Define "coefficients of stability" in Lemma 1.
- Line 1007: Consider clarifying "by optimizing λ".
- Line 1182: Typo: "then" appears twice.
- Line 1282: Typo: "does" → "do".
- Line 1265: Typo: ";" should likely be ":".
- Line 1314: Typo: "The the".
- Line 1382: Typo: "uuper bound".
- Line 1450: Specify which theorem.
- Line 1566: Typo: ";" should likely be ":".
- Line 1597: Typo: "settings in" → "settings of".
- Line 1608: Typo: should be sigma squared in second mention of normal distribution

### Soundness
3

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
2

### Summary
This work aims to provide insight on the generalization property of encoder-decoder models in unsupervised settings. In particular, the authors focus on encoder-decoder models with discrete latent space, e.g. Vector-quantized VAEs. For such specific architecture, the authors show theoretically that the generalization gap can be evaluated with the mutual information and that, surprisingly, it does not depend on the decoder's parameter. This can be traced back to the use of the permutation symmetric super-sample setting, which makes the empirical KL term vanish.

### Strengths
- the result that the generalization bound does not depend on the decoder's parameter is indeed interesting

### Weaknesses
 - The structure of the results and most of the proof techniques are similar to [1]. The novel part comes from considering encoder-decoder models with discrete latent space and the permutation symmetric setting, which is also limiting its applicability.



### Questions
Since the topic of this paper is not exactly my area of expertise, I gave a low confidence (2) to my judgment and I am happy to read and take into consideration what other reviewers opinions. 

I would like to make some comments and questions:
- could the authors clarify on why generalization bounds that depend on the encoder parameter would obfuscate the role of latent variables? (line 98)
- I would make clear in the abstract that the theoretical results of the paper are limited to encoder-decoder architectures with discrete latent variables, and not any (continuous) latent variables. Currently, this is mentioned only in the title with "Vector-quantized VAEs", but I believe it should be stressed in the abstract as well (e.g. in lines 17-18-19).
- Would the authors consider using the terminology "discrete latent variables" (as in the original VQ-VAEs paper) instead of "finite latent variables"? (e.g. line 106) I think it would help improve the scope of the paper.

Minor typos:
- line 152 "fo" should be "of"
- line 152-152 I think the sentence should be re-written
- line 330 "where as" should be "whereas"

### Soundness
3

### Presentation
3

### Contribution
2
