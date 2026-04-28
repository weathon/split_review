# EVA: Geometric Inverse Design for Fast Protein Motif-Scaffolding with Coupled Flow

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6, 6

## Abstract
Motif-scaffolding is a fundamental component of protein design, which aims to construct the scaffold structure that stabilizes motifs conferring desired functions. Recent advances in generative models are promising for designing scaffolds, with two main approaches: training-based and sampling-based methods. Training-based methods are resource-heavy and slow, while training-free sampling-based methods are flexible but require numerous sampling steps and costly, unstable guidance. To speed up and improve sampling-based methods, we analyzed failure cases and found that errors stem from the trade-off between generation and guidance. Thus we proposed to exploit the spatial context and adjust the generative direction to be consistent with guidance to overcome this trade-off. Motivated by this, we formulate motif-scaffolding as a Geometric Inverse Design task inspired by the image inverse problem, and present Evolution-ViA-reconstruction (EVA), a novel sampling-based coupled flow framework on geometric manifolds, which starts with a pretrained flow-based generative model. EVA uses motif-coupled priors to leverage spatial contexts, guiding the generative process along a straighter probability path, with generative directions aligned with guidance in the early sampling steps. EVA is 70× faster than SOTA model RFDiffusion with competitive and even better performance on benchmark tests. Further experiments on real-world cases including vaccine design, multi-motif scaffolding and motif optimal placement searching demonstrate EVA's superior efficiency and effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the motif scaffolding problem - one of the most challenging problems in protein design, where one wants to find a 3D protein structure accommodating a certain functional motif. The authors define motif scaffolding as a Geometric Inverse Design problem on the SE(3) manifold. They approach this using a flow matching, sampling-based strategy that does not require training and can be implemented within any pre-trained unconditional model, which they call Evolution-ViA-reconstruction (EVA). Their sampling strategy adjusts the overall generative direction with the guidance of motif residues with the aim of defining a straighter probability path towards meaningful posterior distribution. They achieve so by implementing coupled flow with the spatial motif-aligned prior and motif-interpolated posterior. The resulting approach matches the performance of state-of-the-art pre-trained models and sampling-based algorithms while significantly reducing inference time.

### Strengths
1. Authors identify failure cases in motif scaffolding and draw an informative analogy with the image inverse problem.
2. The authors clearly define the questions they aim to address in their experiments.
3. Indeed, EVA achieves the best performance or is on par with both SOTA sampling and training-based methods on well-established benchmarks.

### Weaknesses
1. The core ideas, the motif-aligned prior and interpolated posterior, are barely explained, if at all. The concept and reasoning behind choosing a motif-aligned prior appear to be justified by leveraging some spatial context; however, what this spatial context means is never explained. Figure 2, which attempts to build intuition for the modified prior, is highly convoluted and unreadable (please improve this). The authors never showed (and to the best of my knowledge, there is no empirical evidence) that their choice of prior would lead to a straighter probability path *per se*. I believe the optimal transport performance of EVA could be assessed in terms of the normalized path energy and compared to the baselines, similar to [1].

2. The strategy of pre-aligning the prior with the motif does not appear to be novel. Moreover, the authors never referred to the Chroma paper [2], which first introduced the concept of motif-aligned priors and optimal motif index selection. EVA employs a very similar approach to Chroma (Appendix K.2) by aligning the initial prior $\mathbf{g_0}$ with the motif $\mathbf{m}$. The only significant difference is that, in Chroma, classifier guidance is used to approximate the conditional probability $p(\mathbf{g_1} \mid \mathbf{g_t}, \mathbf{m})$, with an analytical classifier that quantifies the distance between the predicted and target motifs to estimate $p(\mathbf{m} \mid \mathbf{g_t})$. EVA is expected to be faster than Chroma, but the novelty of the spatial motif-aligned prior is questionable.

3. I think the authors' statement that they directly approximate $\mathbb{E}_{q} \left[ \mathbf{g_1} \mid \mathbf{g_t}, \mathbf{m} \right]$ is not self-explanatory. At least from the paper, it is not clear how exactly their sampling procedure fundamentally differs from gradient guidance as in [3]. EVA will most certainly have a shorter length of the motif residues trajectory, but how much better is it than FrameFlow-guidance? One could compute the trajectory length of the motif residues in terms of rotation and translation for EVA and compare with the baselines.

4. The authors trained their own protein structure generative model, OT-Flow, and reported both its unconditional and motif-conditioned generation performance to demonstrate that EVA's sampling strategy is compatible with and efficient for any pre-trained model. However, it is absolutely unclear how the model was trained; neither there are any details of the training procedure in the appendix, which the authors referred to. Referring to the original FrameFlow [4] and FoldFlow [5] papers for training details is insufficient; I checked and they have different training set cut-off dates and hyperparameters. Inference settings are not mentioned either...

5. From Table 1, it follows that EVA is about 70x faster than RFdiffusion. For vanilla FrameFlow [4], the inference speed with the same number of timesteps for unconditional generation of a protein with 100 amino acids is about 6 seconds, making EVA more than 5x faster than the underlying flow model. Again, the authors never specify the inference settings in this experiment. Is there any batching? Can unconditional FrameFlow sampling achieve the same performance given EVA's inference settings? Is FrameFlow-guidance significantly slower because the gradient computation is needed on top of the unconditional prediction? Further studies, including a timestep study (with success rate as a function of timesteps), would be informative.

6. It is unclear why in Section 5.7 the authors only qualitatively assess the method's performance on two motifs, despite performing computations for the RFdiffusion and vaccine design benchmarks. A table summarizing the metrics would be informative.

### Questions
**Conclusion**

Overall, the approach introduced and its implementation in the paper is interesting and seems to be efficient. However, the paper is hard to follow. The concepts underlying the choice of the prior and the interpolation strategy are formulated in a very convoluted way, which can be done in simpler terms and explicitly explained in the text accompanying equations, e.g. see [3]. Many crucial details required for reproducibility of the experiments are absent from the paper. One key prior work that introduced similar ideas is not mentioned at all. **I'm willing to raise the score if the authors address all issues raised above, especially:**

1. Improve the readability of the text, improve figures and conduct additional experiments (mentioned above) and introduce explanations. Please, also structure Appendix and properly refer to the concrete Appendix sections within the main text.
2. Critical comparison with Chroma's analytical solution to the motif guidance.
3. Detailed statement on inference settings, training details of the OT-Flow model and explicit explanation why EVA is so much faster.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a method that improves the flow-based generative model for motif-scaffolding (a kind of protein design). The proposed algorithm, Evolution ViA Reconstruction (EVA), leverages the protein’s geometric properties through two main strategies: (1) motif-aligned priors for improved initialization, and (2) motif-reconstruction guidance, a time-varying adjustment from the condition (motif) that enables adaptive guidance during the sampling process. EVA demonstrated faster sampling speeds than baseline methods on two motif-scaffolding benchmarks, including a newly introduced vaccine design benchmark.

### Strengths
1. They frame the motif-scaffolding problem as an inverse-design problem, primarily studied in computer vision, and effectively leverage geometric properties, which appear to have significant practical value.

2. The idea of using geometric properties to improve prior and guidance is both straightforward and novel. It's particularly interesting that the resulting guidance is heavily influenced by the condition (motif) during the early sampling steps, with this effect gradually decreasing over time.
3. This paper introduces a new dataset, which is a valuable contribution to the research community.

4. The proposed method demonstrated improved efficiency without compromising the quality of the designed protein.

### Weaknesses
First, I want to note that I’m not an expert in this domain (protein design or geometric deep learning), so I may not have fully understood all aspects of the paper.

My concerns about the paper are as follows:
1. **Scope and Applicability**: I wonder if the proposed method could be applied to general inverse problems beyond motif scaffolding, such as inverse imaging. Since ICLR is a machine learning conference, a problem-specific approach may have limited impact. Note that I am questioning the broader applicability of the proposed method, rather than suggesting the authors need to show state-of-the-art performance in various domains.
2. **Lack of Experimental Details**: Important experimental details are lacking. For example, the paper doesn’t specify the number of random seeds tested or the values of key hyperparameters (e.g., $t_0$ and $\gamma$). Additionally, standard deviations are not reported, making it difficult to assess the significance of the results against baselines, such as the similarity between “w/o our Prior” and EVA results in Table 4. The absence of standard deviations across all 24 targets in Table 1 makes it difficult to assess the consistency of the method's performance and compare it rigorously with baselines like RFDiffusion. Reporting only the average performance across diverse targets can mask significant variations in performance on individual targets, which is crucial for understanding the method's robustness.
3. **Writing and Presentations:** (including minor ones)  
3.1. Lines 114, 119, 130, 151, and etc: Inappropriate citation command is used. I think when you want to use the cited paper as a subject or object in a sentence, you may use "\citet" command in latex.  
3.2. Line 554: Year is missing. The BibTeX must have some problem.  
3.3. In section 3, there is only one subsection 3.1. You may just replace "3. Backgrounds -> 3. Flow Matching for Non-geometric Domains" without using a subsection. Another option is to make Section 3.2 with the first paragraph of Section 4.2 (lines 250-269) since it can be considered as a background and is not a contribution of this work.  
3.4. Line 183: Subscripts should be removed, i.e., $p^{batch}_0$ => $p^{batch}$ and $q^{batch}_1$ => $q^{batch}$  
3.5. Line 269, 315, 518, and maybe more: "Appendix". An indication of a specific part of the appendix is needed.  
3.6. Line 279: $y$ seems to be a typo. Maybe it should be $x_m$.  
3.7. Line 265: "The formula of transitional vector field seems **sightly** different ..." -> "The formula of transitional vector field seems **slightly** different ...".  
3.8. In Eq. 7, is **x**$_0=(x^1, x^2, \ldots, x^N)$ without subscript 0? Also, the subscript m is used inconsistently: Eq. 4 uses a plain $m$ but Eq. 7 uses a bold **m**.  
3.9. Some inconsistent usage of $x$ and $x_0$ in Eq. 1 and Eq. 2 (and maybe more elsewhere).  
3.10. Line 367: $\hat{\pi}^*$ -> $\bar{\pi}^*$  
3.11. Line 58: the -> The  
3.12. Line 503: "Table.1." -> "Table 1."; BTW, why the Table 1 is at page 8 when they are referred at page 10 for the first time?  
3.13. I don't think experiment 5.2 provides any message or insights about the proposed method.

### Questions
1. Lines 121-123 say that the training-based methods "rely on expensive pre-training". But, as far as I understand, EVA also uses a pre-trained model (FrameFlow). In what sense can we say the pre-training of a conditional flow model is more "expensive"?
2. What makes EVA much faster than others? Is it primarily due to using fewer timesteps? I’d appreciate an algorithm-level explanation that compares EVA to both sampling-based and training-based methods.
3. The performance, except the sampling speed, seems not so remarkable. Does the sampling time really matter in motif-scaffolding (i.e., was the sampling time a bottleneck)? Can EVA generate better protein by running the algorithm longer (e.g., with more fine-grained timesteps)?
4. What is the $\alpha_t$ in line 239?
5. Does the proposed algorithm solve Eq.7 exactly or approximately? And, how is the $\pi^*$ selected?
6. Is the runtime for obtaining $R^*$ with the Kabsch algorithm negligible?
7. How was $t_0$ in Algorithm 1 set in each experiment?  
8. How sensitive is the algorithm against the hyperparameter $\gamma$ and $t_0$?  
9. Do you have a specific plan to release the source code and the vaccine design benchmark?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
In this paper, motif-scaffolding is formulated as a geometric inverse design task, with a lot of inspiration from the image inversion problems. Their approach, namely evolution via reconstruction, proposes a sampling-based coupled flow framework. The method is built upon a pretrained flow-based generative model, and does not train the model any further. Instead, EVA employs motif-coupled priors to utilize spatial contexts, causing the generative process to follow a more "direct" probability path, where the generative directions are more aligned to "guidance" during the initial sampling steps.

### Strengths
1. The authors did try to motivate the work by identifying a problem in the data, relating it to sibling areas in machine vision problems, visualizing it on a few examples, and then proposing a solution.

2. The suite of experiments support the computational efficiency of the proposed method.

3. The core idea of straightening the inference paths and making the optimization process "easier" is reasonable at its base.

### Weaknesses
1. The paper is based more around "proposing a solution", than following the proper scientific steps. There are too many moving parts and it is difficult to identify how much each of the "motif-aligned prior", the "motif-aligned posterior", or the other numerous approximations are contributing or inducing risks to the end result. It is difficult to assess the quality of the proposed method in other contexts out of this paper.

2. Unfortunately, the paper is not in a proper shape of writing in my humble opinion; it was quite a difficult read. The mathematical definitions are quite clunky, and the in-line style of latex math expressions made it too dense and difficult to comprehend, refernce, or look up. I cannot excuse this problem for page limitations, as many other ICLR papers handle the same problem much better. Referencing equations by number is almost impossible due to this style of writing. Irrelevant and secondary information also keeps distracting the reader from the main trajectory.

The notations are also odd at numerous instances:

  * The "batch" superscript in $p^{batch}$ and $q^{batch}$ is too long and distracting. 

  * The notations, subscripts, and superscripts are inconsistently italic or upright, e.g., $\sigma_{\min}$ in Line 165 vs $\sigma_{min}$ in Line 170.

    * Both the italic and upright versions can be found in the same Equation (1). 

    * $Exp$ and $Log$ are both italic in Equation 8. Equation 4 uses $\exp$ and $\log$ instead. This is inappropriate.
  
  * $x$ is sometimes bold-faced, e.g., Line 191, and sometimes not, e.g., Line 152.
    
    * if bold-facing is linked to the $N$-scaled dimensionality, then how come "0" is bold-faced in both Line 165 and 202?  

  * $m$ is oddly both a subscript and a vector in Line 205.

Having coding-style comments in a latex algorithm description is inappropriate; see Lines 329 and 333. If the algorithm has different sections, you may want to consider breaking the algorithm to smaller modules. Coding-style comments in a formal algorithmic description are not a proper solution for this problem.

### Questions
1. Since the authors propose an example from the vision area, I would like to see how the proposed method at reconstructing the same example image for a frame of reference. I understand the authors mainly provide this example to support reader's understanding, but I think for this comparison to be relevant, the image in-painting example using the proposed method of the paper should be also demonstrated. I'm afraid there is too much discussion about "image inverse problems" without any related data about this context **in this paper**.

2. In Table 1, it seems that the proposed method is having a poor performance under long residue lengths. This is quite concerning as high-dimensional porteins are somewhat the main target application for this class of generative models, and specifically, speed-ups are more essential for this type of problem.

3. There are too many metric "hyper-parameter" choices that may affect the downstream conclusions. Examples are the "mRMSD%<1", "scRMSD%<2", and "TM-score threshold of 0.5" for diversity. I understand some of the choices, e.g., "scTM>0.5", "pLDDT>70", and "pAE<5", were referred back to ESM/AlphaFold. 

  * How are the arbitrary thresholds chosen? 
  
  * How sensitive are the conclusions with respect to these choices?

  * Can you provide other non-parametric metrics for evaluation?

4. The 70x speed-up claim is unjustified in my opinion. The RFDiffusion method is producing much higher quality results according to the results in this paper, and is competing in a different league. The proposed method is advertised as a "computationally efficient" option, and the speed up must be reported w.r.t. the much faster FF-G method, for instance. 

5. Since the inference speed is emphasized as the main contribution, the paper should also consider more computationally efficient baseline methods and approximations and a more thorough set of time-complexity analyses must be included. Just reporting three time statistics without any confidence intervals, categorizations, hardware-related considerations, etc. is awfully inadequate.

6. I think the language in the trailing sentence of the abstract, i.e., "multi-motif scaffolding and motif optimal placement searching demonstrate EVA's superior efficiency and effectiveness" should be modified and toned down; the presented experimental results do not suggest "superior effectiveness" by any measure, for instance.

## Minor Comments

1. Line 90: "In detail, we exploit flow-based method pre-trained with flow matching objective" is grammatically incorrect.

2. Line 95: In the Figure caption, the "MCG" acronym was never defined in the paper.

3. Line 314: "desingable" should be "designable".

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a flow-based generative model guidance method named EVA for motif scaffolding in protein design. EVA claims to achieve faster inference times while maintaining performance comparable to SOTA methods. Unlike previous approaches that rely on approximating the distribution of the motif given the prior using Tweedie's formula, EVA approximates the distribution of correct residue frames conditioned on both the prior and the motif. Overall, the method presented seems to be novel; however, I found the paper to be a bit difficult to follow, particularly the correspondence between Figure 2, Algo 1, and the text body. Please see the questions below.

### Strengths
1. Faster inference, on-par results with SOTA.
2. Does not require retraining.

### Weaknesses
1. Requires running the pre-trained model inference at every time step. It is unclear how the computational cost of this compares to other methods, especially considering that the method requires sampling from the unconditional posterior at each step. This could be a significant bottleneck, particularly for large proteins or when generating multiple designs. The paper should provide a more detailed analysis of the computational overhead associated with this iterative process.
2. Difficult to following the correspondence between the paper's main body, Figure 2, and Algo 1. The flow of information and operations is not clearly presented, making it hard to understand the exact implementation of the method. The lack of clear alignment between the text, figure, and algorithm makes it difficult to assess the method's validity and reproducibility.
3. Notation a bit confusing at times. The paper uses a variety of symbols and terms that are not consistently defined or used, making it hard to follow the mathematical derivations and understand the underlying concepts. For example, the relationship between the different vector fields and their impact on the final design is not clearly explained.

### Questions
1. How are the residues of the prior selected for comparison to the motif residues in Eq. 7? Does this refer to "Motif index selection" in Figure 2?
2. Is the Eq number in line 1 of Algo 1 correct?
3. Does the order of the steps in Algo 1 match Figure 2?
4. More elaboration on the far-right plot in Figure 2 would be helpful.
5. It would be helpful if the text mentioned in Figure 2 matched 1 to 1 with the text in the body of the paper. E.g. "compositional gradient" is not mentioned anywhere else. It would also be helpful to put (ours) next to the "coupled vector field".
6. Can you elaborate on the cost of computing the unconditional posterior at every time step? Especially in comparison to other works?
7. How do you decide the coupling strength in Eq 12 - 13?
8. How do your vector fields in Eq 9 and 11 relate to the self-conditioning approach of https://openreview.net/forum?id=XTrMY9sHKF and references therein?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This study models motif-scaffolding as a Geometric Inverse Design task and proposes a sampling-based flow framework, Evolution-ViA-reconstruction (EVA), that incorporates spatial information of the motif. The reconstructed motif in the early stage guides the whole generation process by aligning generative directions with motif reconstruction. Experimental results show that EVA generates desirable proteins with significantly reduced time.

### Strengths
- The idea of modeling motif-scaffolding as a geometric inverse design task is intriguing, and addressing the trade-off between generation and reconstruction is important in this context.
- Directly utilizing the spatial information of the target motif and guiding the generative process through motif reconstruction seems practical.
- The inclusion of real-world tasks enhances the applicability of the proposed method.

### Weaknesses
My primary concern is that the experimental results do not sufficiently demonstrate the advantages of the proposed method over existing approaches, particularly RFDiffusion, for the following reasons:

- The results are reported based on a single run, and the performance differences are not significant enough to conclusively determine which method performs better. Specifically, in Table 1, the mRMSD values for < 100 are 48, 47, and 46, which are too close to confidently claim superiority. Furthermore, the lack of error bars or standard deviations makes it difficult to assess the statistical significance of these differences. The previous work [2] reports error bars in Fig 2, and it is important to include them here for a fair comparison.
- In Table 1, RFDiffusion, a training-based method, appears to perform better with a computation time of 61 seconds. These computation times seem acceptable, especially when considering subsequent synthesis processes. It is unclear if the reported times are for single samples or batches, and if batch generation is possible, the time difference may be less significant.
- The mRMSD scores of EVA are not higher than those of other methods in Table 1 (≥100) and Table 2, even though accurate reconstruction is crucial in this work. In Table 2, RFDiff achieves a Pareto performance with only a 1% higher mRMSD, which is a marginal difference, and without standard deviation, it is difficult to determine if this difference is significant.

Additionally, the manuscript could benefit from improved consistency in terminology, clearer notations, and enhanced coherence. Please refer to minor comments for further suggestions.

- There is inconsistent use of terms regarding the trade-off, such as "trade-off between generation and guidance," "generation vs. reconstruction trade-off," and "Evolution Verse Adoption trade-off" (mentioned in the Appendix).
- The term "Evolution via adaptation" appears in the appendix.
- Section 5.4 discusses the fast computation of EVA rather than directly addressing Question 2: "Can EVA generate designable proteins of various lengths with accurate motif reconstruction?"

### Questions
- In Algorithm 1, \pi* is assumed to be given. Is this assumption realistic in practice? If not, I wonder whether obtaining \pi* and R* in Eq. 7 is tractable for large proteins.
- If one prefers to generate a more desirable protein with more accurate motif reconstruction, even if it requires more computation time, is this feasible with the proposed method?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the problem of motif scaffolding, which requires the construction of scaffold structure stabilzing motifs corresponding to desired functions. Towards this goal, the work leverages spatial context in order to guide the generation process. Motif scaffolding is interpreted as a Geomtric Inverse Design problem which leads to the formulation of Evolution-Via Reconstruction (EVA). EVA is a sampling-based coupled flow framework which utilizes motif-coupling in its prior as spatial contexts. This leads to the construction of a straighter probability path wherein generative directions are aligned with the sampling steps. EVA improves sampling time by a signficant margin while presenting competitive performance on RFDiffusion benchmark and in-silico vaccine design task.

### Strengths
* The paper is well written and easy to understand.
* The paper tries to address an important and challenging problem from a geometric perspective.

### Weaknesses
 * **Benefits of Motif Geometry:** My main concern is the benefits of motif geometry. Addition of motif-aligned prior and motif-interpolated posterior only benefits the model at sampling time. If we are using motif-coupled information with a rich prior, this should improve sample quality (especially designability) as well. However, empirical evaluation on benchmarks in Tables 1, 2 and 3 shows that additiona of motif-coupled information deteriorates designability of sampled complexes. What benefits does motif information provide for sampling novel complexes aside from faster sampling? How can motif information aid in the designability of sampled complexes?
* **Improvement over OT-Flow:** The work presents empirical evaluation for motif-coupling on the RFDiffusion benchmark and an in-silico vaccine design benchmark. In most experiments on the RFDiffusion benchmark, backbone models (such as OT-Flow) are better for designability and success rates. What improvements does EVA offer over the backbone models? If the main contribution of the work is the addiiton of geometry information and motif-interpolation, then do these design choices benefit over prior backbones?
* **Unconditional Generation:** Figure 3 and Table 2 present results for the backbone flow models. I am struggling to understand the presence of these results in the main text. If these experiments are not directly related to EVA, could they be better placed in the appendix? From my understanding, these results can be understood as ablations over backbone models in determining the choice of flow for motif coupling.
* **Scallbility:** While EVA demonstrates consistent improvements on the RFDiffusion benchmark, it still remains unclear whether the method is scalable for real-world applicability. Table 1 demonstrates that EVA performs best on smaller lengths of residues (< 100). Intuitively, motif geometry is informative only for smaller complexes. Can the authors comment on the use of motif coupling for larger residue lengths? How can EVA be adopted/improved for larger complex sizes?

### Questions
Please refer to the weaknesses section above.

### Soundness
2

### Presentation
2

### Contribution
2
