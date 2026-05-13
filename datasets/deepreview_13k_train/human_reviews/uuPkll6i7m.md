# Towards Certification of Uncertainty Calibration under Adversarial Attacks

- Decision: Accept
- Scores: 6, 8, 8, 5

## Abstract
Since neural classifiers are known to be sensitive to adversarial perturbations that alter their accuracy, \textit{certification methods} have been developed to provide provable guarantees on the insensitivity of their predictions to such perturbations. Furthermore, in safety-critical applications, the frequentist interpretation of the confidence of a classifier (also known as model calibration) can be of utmost importance. This property can be measured via the Brier score or the expected calibration error. We show that attacks can significantly harm calibration, and thus propose certified calibration as worst-case bounds on calibration under adversarial perturbations. Specifically, we produce analytic bounds for the Brier score and approximate bounds via the solution of a mixed-integer program on the expected calibration error. Finally, we propose novel calibration attacks and demonstrate how they can improve model calibration through \textit{adversarial calibration training}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work addresses a critical vulnerability in neural network classifiers by examining how adversarial attacks can significantly harm model calibration (the reliability of confidence scores) while leaving accuracy unchanged - a particular concern for safety-critical applications. The authors introduce two new metrics for certified calibration: the Certified Brier Score (CBS) with a closed-form bound, and the Certified Calibration Error (CCE) approximated through mixed-integer programming. They also propose a novel training method called Adversarial Calibration Training (ACT) with two variants (Brier-ACT and ACCE-ACT) to improve certified calibration while maintaining accuracy.

### Strengths
1. Identifies an important security vulnerability (calibration under adversarial attacks) that wasn't previously well-studied
2. Well-formulated mathematical foundations for certified calibration

### Weaknesses
1. The entire certification framework relies heavily on the binning strategy used in ECE computation. Specifically, the choice of bin boundaries and the number of bins can significantly impact the resulting ECE value, and consequently, the certified calibration metrics. This dependence introduces a potential instability in the certification process, as different binning strategies could lead to varying conclusions about the model's calibration under attack. The lack of a principled method for selecting the optimal binning strategy is a concern.
2. Complex hyperparameter tuning required for ADMM solver. The ADMM algorithm, while powerful, is known to be sensitive to the choice of hyperparameters, such as the penalty parameter and the step size. The need for extensive tuning can make the proposed approach less practical, especially for users who may not have the expertise or resources to perform such tuning. This complexity also raises questions about the robustness of the method, as suboptimal hyperparameter choices could lead to inaccurate or unreliable certification results.

### Questions
1. How does the certification process scale with the number of classes? Would the approach be practical for problems with hundreds or thousands of classes?
2. Could the proposed methods be extended to other uncertainty estimation approaches beyond softmax confidence scores?
3. How sensitive is the certification to the choice of binning strategy in the ECE computation?

Additional Advice:
You should follow the ICLR submission format.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors show that it is possible to generate adversarial examples that don't change accuracy but impact confidence scores heavily. Thus, confidence scores can not really be trusted by introducing a parametrized attack that can raise and lower confidence scores without impacting the classification. Then they introduce *certified calibration*, a method to provide guarantees on the calibration of certified models under adversarial attacks. Then a training scheme is proposed to improve the certified uncertainty calibration.

### Strengths
The certified calibration is an important and currently not very developed problem. The authors do a good job in motivating the problem and proposing solutions. The paper is mostly easy to follow, though the reviewer feels that illustrations would sometimes have improved readability. The approach is novel and interesting.

### Weaknesses
 - It is unclear how large the effect is in Table 2. The Brier Score although defined in simple terms is appears somewhat uninterpretable. Specifically, it is difficult to gauge the practical significance of the reported ACCE values. For instance, a difference of 8 in ACCE (e.g., 49.30 vs 41.32) lacks a clear interpretation in terms of real-world impact on model predictions. It's not immediately obvious if such a difference represents a substantial or minor improvement in calibration.
- The authors did not report mean and std of their results over different seeds.  
- The reviewer has the feeling that explanations could be made more concise from time to time while improving readability further. 

Minor:
- 232/233 - the sentence here does not appear to be grammatically correct

### Questions
- For Table 1: could the authors (possibly via bootstrapping) estimate variances here? 
- What is the final loss that is optimized to solve equation 2? As in how did you encode it? 
- Is the certificate actually sound or just approximate (see Line 238)?
- Is $a_{i,j}$ only for 1 $j$ allowed to be 1 while the others are 0?
- What where the considerations for choosing ADMM? 
- Does the reviewer suppose correctly that the runtimes in G1 where reported for CIFAR-10?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper discusses the importance of model calibration and solutions for determining a model's certified calibration and training models to be robust against calibration attacks. The paper starts by highlighting the importance of considering model calibration along with model accuracy by showing attacks degrading calibration and discussing applications in which this could have a strong negative consequences. The paper generalizes existing attacks on confidence estimation to form their new $(\eta, \omega)$-ACE attacks. The authors go on to describe certified Brier scores and certified calibration error providing a closed form solution for the first and detailing how to approximate the later with a MIP and solving it using ADMM. The paper then explores a new method of adversarial training building off SmoothAdv which they call adversarial calibration training (ACT). Finally, through an extensive set of experiments they show the effectiveness of ACT.

### Strengths
I found this paper to very well written and argued. The paper is structured well and there is an appropriate level of formality and theorems which motivate the work. To the best of my knowledge they propose the novel metrics of certified brier score and certified calibration error and give algorithms to compute these. They also provide a novel algorithm, ACT, for training models to have better uncertainty calibration. I also found the paper to have extensive experiments showing the performance of ACT in various scenarios.

### Weaknesses
1. The main issue I have with this paper is that it does not at all address the extensive work in non-probabilistic verification/certification of Neural Networks (Abstract Interpretation: IBP, CROWN, DeepPoly, etc. SMT Solvers: Ehlers et al 2017, Marabou, etc. Relaxation: Neurify, etc. Certified Training: IBP, DiffAI, COLT, CROWN, SABR, etc.). The paper defines formal certificates (C1, C2) but does not note that the certificates it proves/approximates are based on randomized smoothing and thus probabilistic in nature (i.e. certifying a score above a certain probability threshold). I am also curious as to what the authors think about using non-probabilistic verification/certified training methods in the calibration certification case. Smoothed classifiers tend to have good performance at the cost of inference time (i.e. performing 10s-100s of inference passes to get a classification). Do the authors think that adapting abstract interpretation based approaches could work in this case for verification or training?
2. This paper also lists training times in the 100s of GPU hours and verification times in the 1000s of GPU hours (Appendix N) using a total of 5000 GPU hours for the experiments in the paper (although admittedly there are many experiments). These finetuning times are approaching multibillion parameter LLM finetuning times. 
3. While the authors bring up valid motivations in Section 2.2 I find them a bit hard to see in practice. Currently accuracy still dominates as a metric for most practical applications, most SOTA defense methods protecting model accuracy against attackers actually sacrifice accuracy and thus even these have a hard time finding real-world use. The premise of this paper leans on these methods being used but not being protective enough of calibration (although the papers experiments do show that their method can be used without sacrificing much certified accuracy). This point along with (2) make me think this method seems a bit hard to justify in practice.

**Minor Weaknesses**

1. While I found the paper to be well written and easy to follow, I think it would greatly benefit from some overarching example which could help provide insight and make Section 3 a bit easier to follow.

### Questions
The main reasoning for my score is the 3 points above in the weaknesses section, I am happy to raise my score if these are addressed. The following list of comments I think could make the paper clearer but I don't think significantly impact my grading.

**Clarity**

1. (line 160) When $\omega = \hat{y}$ it seems that Equation 2 would read as maximizing $\mathcal{L}_{CE}(f(x,\gamma), f(x,\gamma))$, I think the notation here is a bit unclear, I think you mean $\hat{y} = f(x)$?
2. (table 1) What metric is actually given here? The drop in AdaECE compared to the untracked version? I think at this point it is still slightly confusing how one should interpret these numbers, is higher better? worse? does it depend on $\eta$ and/or $\omega$?
3. (line 168) Can you be a bit clearer about how this adversarial training is happening? The existing model is adversarially finetuned? A new model is trained with adversarial training? Standard PGD adversarial training? Does the accuracy of the adversarially trained model change? Or reference somewhere where this information can be found.
4. (line 180) This is slightly confusing, a practitioner deploys a model with a threat model budget? I guess you are trying to say that the deployed model is certified for all $R \leq R_n$? How are they receiving a guarantee? What is being guaranteed? This should be individual certificates on individual points, is this being generalized to a data distribution? I think there should be a clearer way to defined the certified accuracy here.
5. (line 190) I think it is important to note that Gaussian smoothing gives probabilistic certificates. The certificate defined in C1,C2 are deterministic. There also exist methods for obtaining deterministic $l_p$ certificates through abstract interpretation/LP solvers/etc, so I think a distinction should be made here as these methods more accurately fit the certificates above.
6. I think throughout the Section 3 it would make the argument easier to follow if there was a toy example of some sort.

**Minor Comments**

1. (line 34) This sentence reads strangely maybe "...neural network classifiers **can be** extremely sensitive... human eye **for which** $x + \gamma$ ..."
2. (line 42) "and thus **provide guarantees on** model accuracy"? otherwise the last clause it strange
3. (line 45) "average mismatch"? undefined at this point
4. (line 128) extra comma
5. (line 137) There is no example being extended, it was mentioned in line 124 but has not been explained yet
6. (line 166) This is an incomplete sentence, "**For** a ResNet50 *model* on ImageNet, **a** $(1,y)$-ACE **attack**...$?
7. (line 168) missing a word after the comma "**but**" or "**however**", also should it be "a $(1,\hat{y})$" or "an $(1,\hat{y})$"
8. (line 184) I think the notation/wording is a bit confusing here. "**for all** perturbations **s.t.**"? I guess $\forall ||\gamma_n|| \leq R_n$ seems slightly weird I understand what is trying to be said $\forall \gamma_n \in \[\gamma \text{ s.t. } ||\gamma|| \leq R_n\]. F(x_n + y_n) = F(x_n)$. I guess you don't need to change this but it seems like a slight abuse of notation.
9. (line 184) Why is this an assumption? Isn't it more like a definition?
10. (line 208) Is this an assumption or are you saying that a model has these properties by definition, or clarify what the assumption is here i.e. is there some case where this doesn't hold?
11. (line 214) Maybe place a dot between $l$ and $c$ otherwise it kind of seems like $lc$ is a new variable.
12. (line 233) "that **is** possible"
13. (line 244) is this backward? should it be (4) to (5)?
14. (line 268) define $\mathbf{1}_M^\top$

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors consider the problem of constructing certifications for neural networks in parallel with the task of improving confidence. The authors achieve this through the development of a new approximate certification measure, and support their work with significant experimentation.

### Strengths
The authors investigate an interesting extension of the certification literature, which moves beyond more traditional (and incremental) advances in the field of image based certifications. 

In doing this, the authors introduce new techniques and approaches, which are novel and interesting, and the mathematical presentation is well detailed (although I have issues regarding specificity and rigour in explanations, see below).

### Weaknesses
 I hold a number of concerns regarding this paper. One of the primary issues relates to this technique relying on an approximation to construct ACCE. I'm intrinsically cautious about any result that presents itself as a certification while relying on breaking the guarantees of the certification in order to calculate results. Expectations around certifications guide their use, and violating the precepts of a certification while still labelling it as a certification is problematic to me. To me,  an approximation to a guarantee is only useful in rare circumstances, where other insights can be gained by the approximation process - something that I would argue is not present within this work. 

When it comes to the motivation for their work, the authors discuss possible reasons for an attack on calibration, however I would suggest that the current presentation of this is a bit sparse - it is sufficiently detailed for comparisons, but the ultimate applicability of this attack could require more justification. This perception is reinforced by statements being made regarding risk and processes that might support this work without citations - leaving this reader curious as to if the justifications actually exist. 

While the sentence-by-sentence writing is overall well done (although a touch clunky at times), I would argue that the ordering of content is somewhat jumbled, and it hinders readability and accessibility. For example, certifications are required knowledge to understand content long before they are formally introduced on Line 177. The document, as structured, has multiple examples of such structural issues that would make it difficult for a reader to parse content if they were unfamiliar with the space. 

These issues with presentation extend to how some of the results are presented. Take Table 1 as an example - what  is the reader meant to get out of this? If I understand it correct the Unattacked rows correspond to the base values, and ideally the AdaECE should decrease in the case of a successful attack? But when there is the switching behaviour about $\eta$, interpreting this table is nigh on impossible. Moreover, the compressed nature of the table, and its positioning within the document further hinder accessibility. 

General comments regarding identified issues follow below: 
- L118 "has been discussed" -> "have been discussed". Moreover, in this sentence you use "label attacks" without explaining what these are, nor what an adversarial attack even is. 
- L119 "their immediate effects" - what is the subject of their: adversarial attacks? The literature? Label attacks? 
- L119 "effects on the reliability of uncertainty estimation are often overlooked" you can affect somethings reliability, but you cant affect the reliability. The reliability is a downstream consequence of the impact made. 
- L120 after the colon - why is this colon required? And why are these things overlooked if this is a statement that can be made without citation, suggesting it is so well known that such a justification is unnecessary. 
- L121 "Beyond label attacks" - the subject of this paragraph, to this point, has been label attacks. If a different framework is to be introduced, this should be a new paragraph. Is the point here not that it's not only that attacks can indirectly influence confidence, motivated attackers can attempt to directly manipulate the confidence scores as well?
- L125 "We note that this impacts system-level uncertainty and conclude that both label and confidence attacks leave system calibration vulnerable" - you're noting the very things you've just stated in the preceding sentences, without stating why this is important. 
- Line 127 "for both, their" - comma is unnecessary
- Line 128  "when uncertainty estimates...." - this sentence fragment is disconnected from its context. Is it not "machine learning systems incorporating uncertainty estimates in their decision processes are monitored regularly for both their .... in safety-critical applications." ?
- Line 127-129 - this is a statement of fact, are there any citations available for it? 
- Line 132 Denial of Service should be capitalised appropriately, as it is the name of a thing. 
- Line 120 and line 132 - incorrect use of colons. For one, they're unnecessary in these contexts, and for two they shouldn't have capitalisation after the colon (although there's some nuance here between British and American English, still, fundamentally, the colons are unnecessary). 
- Line 132: The defences are again a whole new concept, should this not be a new paragraph for readability? 
- Line 137: Discussion centred around certified models without properly defining what these are? Readers who are not familiar with the certification literature will have limited opportunities to catch up up here. 
- Table 1 - font too small, it's what, half the size of the standard maths font, and is really jammed in to the paper. 
- Line 195 "The certificate on the prediction" - is the first the necessary?. And what does "showing a certificate on the confidence" mean. 
- "extended by Salman et al. (2019) and Kumar et al. (2020) showing a certificate on the confidence" - this implies that both Salman AND Kumar certified confidence, rather than just Kumar.

### Questions
Answers to the following questions from the authors would be appreciated:
- Could you comment upon how you view the process of calculating/employing an approximate certification?
- Which norm (see, for example, line 179-188) are you using? 
- Is there any sensitivity to the number of bins (M), or their partitioning?
- Are there any uncertainties that could be calculated on Figure 3 or Table 2? For table 2 how did you settle upon selecting "within 3% of the ihghest certified accuracy"
- In Figure 4, you claim "ACCE-ACT significantly improves certified calibration at larger radii" - why is this not present at smaller radii, and how much is this actually an improvement? The overlapping nature of the circles makes it very difficult to parse out the exact impact here, beyond tea-leaf reading.

### Soundness
2

### Presentation
3

### Contribution
2
