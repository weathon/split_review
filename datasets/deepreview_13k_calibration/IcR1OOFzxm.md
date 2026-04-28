# Towards Generative Abstract Reasoning: Completing Raven’s Progressive Matrix via Rule Abstraction and Selection

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Endowing machines with abstract reasoning ability has been a long-term research topic in artificial intelligence. Raven's Progressive Matrix (RPM) is widely used to probe abstract visual reasoning in machine intelligence, where models will analyze the underlying rules and select one image from candidates to complete the image matrix. Participators of RPM tests can show powerful reasoning ability by inferring and combining attribute-changing rules and imagining the missing images at arbitrary positions of a matrix. However, existing solvers can hardly manifest such an ability in realistic RPM tests. In this paper, we propose a deep latent variable model for answer generation problems through \textbf{R}ule \textbf{A}bstract\textbf{I}on and \textbf{SE}lection (RAISE). RAISE can encode image attributes into latent concepts and abstract atomic rules that act on the latent concepts. When generating answers, RAISE selects one atomic rule out of the global knowledge set for each latent concept to constitute the underlying rule of an RPM. In the experiments of bottom-right and arbitrary-position answer generation, RAISE outperforms the compared solvers in most configurations of realistic RPM datasets. In the odd-one-out task and two held-out configurations, RAISE can leverage acquired latent concepts and atomic rules to find the rule-breaking image in a matrix and handle problems with unseen combinations of rules and attributes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a novel method (RAISE) for solving Raven's Progressive Matrices (RPM) abstract visual reasoning problems. RAISE is a deep latent variable model, that learns the underlying rules in an RPM problem as latent variables and then uses the learned rules to conditionally (based on the context rows/columns present in one problem) generate the target image. The authors show that this leads to strong results for standard RPM reasoning tasks, generalizes better to more esoteric tasks (like answer selection at random locations). The visualization of latent concepts also shows that the latent variables are able to reasonably capture the atomic rules underlying the reasoning problem.

### Strengths
* The motivation of building a generative solver versus a selective one to avoid shortcuts in discriminative reasoning task is very valid and has been highlighted in prior literature [1, 2]. I commend the authors for trying to solve the harder problem in RPM reasoning: mapping the underlying data generative process.  
* The RAISE model is very well thought our and describe in the paper. The modelling choices make sense for the few-shot style reasoning tasks in RPM problems. Also see weaknesses regarding the motivation and usability in a broader context.


**References** 

1. Hu, S., Ma, Y., Liu, X., Wei, Y. and Bai, S., 2021, May. Stratified rule-aware network for abstract visual reasoning. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 35, No. 2, pp. 1567-1574).
2. Geirhos, R., Jacobsen, J.H., Michaelis, C., Zemel, R., Brendel, W., Bethge, M. and Wichmann, F.A., 2020. Shortcut learning in deep neural networks. Nature Machine Intelligence, 2(11), pp.665-673.

### Weaknesses
 * In Sec 1. Introduction: "It has been suggested that Bayesian inference with shared latent concepts can explain the emergence of in-context learning in LLMs, which is the foundation of few-shot reasoning in tasks like RPM tests." This premise has several logical leaps which the authors don't explain. For example, Chan et al [1] showed that the nature of training data for natural language enables few-shot reasoning from in-context learning. This does not hold for RPM reasoning tasks - the data distribution does not have the same long tailed and co-occurence properties as natural language. Similarly, Bayesian inference of shared latent concepts being able to explain in-content learning is just one lens of explainability for this empirical phenomenon, and there can be other lenses which are purely frequentist (e.g. the one showed by Chan et al). Overall, the motivation derived for RAISE from this statement is very loose and falls apart on deeper inspection.

* My chief concern witht this paper, and the overall idea behind structuring latent representations and re-combining them at inference is how scalable is it beyond toy problems like RPMs? The bottleneck with DLVMs like RAISE is two-fold: learnability (e.g. authors re-use encoder parameters between generative and inference process) and reliance on human knowledge to design the graphical model. RPMs have a very limited rule set, and the visual abstraction process is vastly simpler than human scenes. These reasons why existing concept learning methods that rely on similar modelling and inference have not been able to scale to harder visual reasoning problems are yet to be solved.  Specifically, the paper does not address the combinatorial explosion of latent variable interactions as the complexity of the visual scene increases. The fixed set of atomic rules, while effective for RPM, might not generalize to more complex scenarios where the rule set itself needs to be learned or adapted. Furthermore, the reliance on a predefined graphical model limits the model's ability to discover novel relationships or rules that were not explicitly encoded in the model structure. The paper would benefit from a discussion on how the model would handle scenarios with a dynamic rule set or where the underlying relationships are not known a priori.

* In Sec 3.1 "Previous studies have emphasized the role of abstract object representations in the abstract reasoning of infants, which is similar to the idea of object-centric representation learners that decompose complex scenes into object representations. Both views reflect the compositionality of human cognition (Lake et al., 2011)." I don't know if the human analogy to concept learning should drive artificial concept learning agents, particularly because the underlying constraints (inductive biases?) on human and artificial systems are vastly different. A much more recent work from Lake et al [2] shows that neural network based reasoning combined with a meta learning objective can solve similar systematic generalization problems. I would also refer the authors to the discussion section of the paper for a much more nuanced discussion on Bayesian vs Neural approaches to learning systematicity. For a similar treatment of systematic reasoning by learning the underlying rule structure and routing at inference but from a purely neural treatment, I would refer the authors to [3] which also reports strong results on RPM style reasoning tasks.

### Questions
I don't have particular questions regarding the paper: I think it is a good paper, and the authors achieve what they set out to do in the introduction. My main concern is whether this is the right thing to do, especially for more "real-world" reasoning problems where the cardinality of the rule set is exponentially larger. I think the paper would benefit from the authors providing a more comprehensive discussion on Bayesian vs Neural concept learning since their current motivation on building a DLVM is not very convincing. 

Minor question: In Sec 5. "Too much noise will make a problem have a large number of solutions (e.g., PGM (Barrett et al., 2018)), such data may not be proper for validating the generative reasoning ability of models" I am not exactly sure what the authors mean by "a problem have a large number of solutions" - does this refer to potentially many rule compositions satisfying the bottom-right answer selction in RPMs.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a conditional generative model for Raven progressive matrices. It is trained from images, encoding each image into a set of C Gaussian latents, which can be decoded back to images, while also learning a set of K rules governing how a target image is composed (given its position in the grid and what the inferred progressive rule is). It is trained through an ELBO loss with some partial auxiliary rule supervision.

It shows clear advantages compared to existing baselines, both in terms of actual accuracy, but also in flexibility, as it can generate images in arbitrary cells of the RPM.

Overall, the generative model is rather straightforwardly designed, albeit feels rather specific to RPM problems, hence this is addressing a very specific problem and significance might be limited. I also have a few reservations about some baselines (in particular the Transformer one).

### Strengths
1. The paper is very clear, presents the problem well, and the math is clear and easy to follow. Figure 1 is very helpful to unpack the generative process, and overall I feel like it made all its choices clear. I could find nearly all details I needed about the implementational details (see questions below)
2. Experiments are comprehensive and well executed, with a good choice of baselines (I am not an expert in RPM however)
3. From results shown in Figure 2, I think it’s fair to say that it “solves” PGM quite effectively, but an expert might be able to comment better on the complexity of this problem for current SOTA.

### Weaknesses
1. This is a generative model designed specifically for RPM, and it is unclear how one would leverage this work or its findings in any other context.
2. It is equally a “straightforward” application of an ELBO-based generative process. It is well executed, but not surprising and I did not find particularly interesting pieces of technical/insightful choices throughout the paper.
3. It is unfortunate that some amount of rule annotation is still used. It oscillates between amounts (5% for non-grids, 20% for O_IG and 100% for 2x2 and 3x3 grids), but I was wondering what the performance would have been with 0% supervision, as this seems like the “optimal” solution target for RPMs. The reliance on even partial rule supervision limits the practical applicability of the model, as obtaining such annotations can be costly and time-consuming. Furthermore, the varying levels of supervision across different RPM types introduce an inconsistency in the experimental setup, making it harder to assess the true capabilities of the model under a unified framework.
4. The Transformer baseline lacked details, even in Appendix C.3. 
   1. Which encoder did you use? Was it a discrete representation? Transformers behave much better on VQ-like latents.
   2. I somehow expected it to do better, e.g. if attributes were provided instead of pixels, isn’t a Transformer a pretty strong baseline?

### Questions
1. Do you have any suggestions for what one can learn from your model that can be generalized away from the RPM setting? Any specific insights / technical novelty compared to previous works?
2. Most decisions were extremely clear, but it was not that well explained how candidate answer selection was performed (Section 4.1 and 4.2)
   1. Do you generate a sample x_t and compare to the x_candidates in pixel space?
   2. Do you generate a z_t and compare g^enc(x_candidates)?
   3. Do you instead do a likelihood test?
3. Finding values for C and K required going into the Appendix (C=8, K=4), and their choice wasn’t discussed.
   1. How sensitive is the model to varying C or K?
   2. How were these chosen? How adapted to the number of attributes and real rule numbers do they have to be? I’m aware they are different, but how sensitive is it e.g. can you use K=100?
4. The Transformer baseline lacked details, even in Appendix C.3.
   1. Which encoder did you use? Was it a discrete representation? Transformers behave much better on VQ-like latents.
   2. I somehow expected it to do better, e.g. if attributes were provided instead of pixels, isn’t a Transformer a pretty strong baseline?
5. How needed was the rule supervision?
   1. Do you have numbers when you drop this to 0?
6. Nits/typos:
   1. It would have helped to explicitly write that r^c takes values between 1 and K.
   2. \mu_T^c -> \mu_t^c in (4)
   3. z_T^c -> z_t^c in (6)

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A new model -- RAISE has been proposed by the authors for RAVENs. The model contains several components, such as an image encoder, two variation autoencoder, and a global knowledge set. This model first extracted image features and then used these features to generate answers by a conditional generative process. The proposed model was evaluated through experiments on RAVEN and I-RAVEN datasets and showed better performance than other generative-based methods. Ablation studies showed the proposed RAISE can better handle the selection in arbitrary positions.

### Strengths
1. The paper is generally well-written and the main idea is easy to follow.

2. The authors proposed a new generative model -- RAISE that can explicitly encode rule-related information. It will be more useful to construct interpretable machine learning algorithms in this community.

3. The authors showed that their RAISE can perform better than previous generative methods, and is also on par with some of the existing selection-based methods.

4. The authors also analyze the proposed models with different experiments.

### Weaknesses
1. The authors fail to convince me, why we need to generate answers in arbitrary positions? I am eager to see what is the advantage of generating an arbitrary position over generating the right-bottom answer, not only the final performance, but also the rationale or the motivation behind this design.

2. Whether the model shown in App is used in all configurations or not?

3. Too many hyper-parameters should be tuned.

4. Experiments are not enough. I suggest using PGM-Neutral, PGM-Interpolation and PGM-Extrapolaton to confirm the effectiveness of RAISE.

5. The authors also should clearly state why to use rule annotations, but not the answer images. Which indeed violates the RPM question.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes RAISE, Rule AbstractIon and SElection model for generative abstract reasoning. In particular, the model is evaluated on Raven's Progressive Matrices. To solve a Raven problem, the model first encodes the context images and samples the latent rule for different latent concepts and generates the answer. On both RAVEN and I-RAVEN, the model shows improved performance while being generative, and also the model enables arbitrary panel generation and odd-one-out problem testing.

### Strengths
The best generative solution I'm aware of for solving the abstract reasoning problem, while problem structure has been taken into the design. To the best of my knowledge, previously similar performance is only attained by discriminative models and this is the first of the generative model to achieve similar performance. The authors have also tested the model on different setups, and the results are good enough.

The authors have shown sufficient experiments to show the meaningfulness of the latents: by varying the latents, they could get desired image results.

While the problem formulation follows the conventional approach, the problem decomposition makes sense and is intuitive.

### Weaknesses
The formulation for conditional generation is rather standard. While it is not exactly the same as conditional VAE, the derivation follows the same principles and the tweaks are only made due to the structured inference prior employed in modeling.

In general, I don't think the comparison is completely fair compared to other baselines, as some of the baselines only use the ground truth answers. While RAISE only uses the rule annotations, grounding of rules to corresponding hidden concepts is also implicitly encoded in the matrix. So supervisory signals could actually be backpropagated to the attribute / concept part. Besides, in evaluation, I do note that PrAE and ALANS are only trained on a specific split whereas RAISE are trained on more than one, and that is at least twice the data.

One thing I'm not particularly sure is how is the answer selected in RAISE. When you generate the answer, how do you pick the candidate from the given set? PrAE and ALANS actually only generate the hidden latents and compare in the latent space. Do you compare in the pixel space? Do you think comparing in the hidden space would help further improve performance of RAISE?

### Questions
Check above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
