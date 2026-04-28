# RetroDiff: Retrosynthesis as Multi-stage Distribution Interpolation

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
Retrosynthesis poses a fundamental challenge in biopharmaceuticals, aiming to aid chemists in finding appropriate reactant molecules and synthetic pathways given determined product molecules. With the reactant and product represented as 2D graphs, retrosynthesis constitutes a conditional graph-to-graph generative task.
Inspired by the recent advancements in discrete diffusion models for graph generation, we introduce Retrosynthesis Diffusion (RetroDiff), a novel diffusion-based method designed to address this problem. 
However, integrating a diffusion-based graph-to-graph framework while retaining essential chemical reaction template information presents a notable challenge.
Our key innovation is to develop a multi-stage diffusion process. In this method, we decompose the retrosynthesis procedure to first sample external groups from the dummy distribution given products and then generate the external bonds to connect the products and generated groups. Interestingly, such a generation process is exactly the reverse of the widely adapted \textit{semi-template} retrosynthesis procedure, \emph{i.e.} from reaction center identification to synthon completion, which significantly reduces the error accumulation. 
Experimental results on the benchmark have demonstrated the superiority of our method over all other \textit{semi-template} methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
a new diffusion model for retrosynthesis is presented

### Strengths
- diffusion has not been applied much to retrosynthesis
- results are decent but not impressive

### Weaknesses
 - several baselines were missing
- the design of the model seems to be very complex
- inference times are not reported
-citation of graph2edit is missing, which is semi-template, and very strong https://www.nature.com/articles/s41467-023-38851-5


### Questions
- why are so many complex steps and rule checking needed? a good generative model would learn all of that from the data. have the author ablated this properly?
- in the current form, the paper is a bit unmotivated. will the community just apply any new generative model to retrosynthesis? autoregressive -> GANs -> VAE -> diffusion -> next is flow matching I guess?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes RetroDiff: a model casting retrosynthesis prediction as a two-stage discrete diffusion process. In the denoising direction, the first stage generates the missing atoms (those that were part of side products and hence are not seen on the product side) and then the second stage generates the bonds between the product and the added atoms. Finally, there is a final (unlearned) stage, which breaks at most one pre-existing bond. The authors experiment on USPTO-50K as well as analyse the behaviour of their method qualitatively.

### Strengths
(S1): The idea to apply discrete diffusion to reaction prediction is, to my knowledge, novel (or at least doesn't appear in any established work). It also seems potentially promising given recent advances in diffusion models overall. 

(S2): The paper includes some useful qualitative visualizations (Figures 5-6), which help get intuition about how RetroDiff works.

### Weaknesses
 (W1): The empirical results are not too impressive. In the paper, the results appear more promising than they actually are, as several baselines are missing, and the presentation is also somewhat biased.

- (a) Strong baselines are missing: for example RetroKNN [1] on the template-based side, and RootAligned SMILES [2] on the template-free side. Both of these models outperform RetroDiff by a large margin (a few %) across top-k values. Note that recent work [3] corrected some of the previously reported results on USPTO-50K, showing that e.g. results for LocalRetro and RetroKNN were somewhat inflated, but even after the correction RetroKNN is stronger than RetroDiff. The lack of comparison with these established methods makes it difficult to assess the true performance of RetroDiff. Furthermore, the specific performance gap should be quantified more precisely, rather than stating 'a few %', and should be provided for each reported top-k value.

- (b) Only accuracy with top-k for k <= 10 is reported, while it is standard to also report top-50. Seeing unpromising scaling from top-5 to top-10, I imagine top-50 is not very impressive, but it should nonetheless be reported, to make sure the downsides of the presented method are explicitly shown. Although top-50 doesn't differentiate well between some models as they approach 100% on simple datasets such as USPTO-50K, it is still important, because it shows whether the model is able to at least in principle cover the full distribution. Also, popular multi-step search approaches often query the single-step model for up to 50 reactions. The absence of top-50 results makes it difficult to evaluate the method's ability to generate a diverse set of plausible reaction pathways.

- (c) The authors focus their comparison within semi-template methods, noting how their preformance is strong within that class. This to me seems a bit artificial, as belonging to the semi-template class doesn't convey strong benefits in itself that would warrant not looking at other model classes. One could argue that template-free methods are too unconstrained and not interpretable, and hence not focus on them in a potential comparison, but template-based methods are usually at least as interpretable as semi-template-based ones, and sometimes more intepretable (because interpretablity is usually implemented by looking up the literature reactions that gave rise to a particular template that got applied, and this method is not applicable to some semi-template-based methods like RetroDiff). In consequence, I mostly looked at performance among all reaction models overall, and in that setting RetroDiff doesn't perform too favourably. The justification for focusing on semi-template methods is weak, and the paper should be evaluated against all state-of-the-art methods, regardless of their class. The interpretability argument for template-based methods is also not fully addressed.

- (d) Finally, the authors also show improved SMILES validity score compared to popular models based on the Transformer architecture. This is a good sanity check, although I wouldn't put too much weight into that result, as many highly performant template-based models (e.g. LocalRetro, RetroKNN) have 100% validity by design. It is still good to see RetroDiff getting near-perfect validity, but it's important to remember that this limitation is actually absent in some model classes. The validity score should be considered a necessary but not sufficient condition for a good model, and the paper should not overemphasize this result.

(W2): In Section 2.1.3 on post-adaptation, the authors explain that in the final stage, zero or one bond is broken in the transformed product graph to form the reactant graphs. To me, this seems to assume there are at most two reactants. This may be true in USPTO-50K, but would not be true overall. While the number of reactants is usually small, in larger reaction databases one can find a lot of examples with 3 or even 4 reactants. Am I correct in assuming that the current post-adaptation procedure only works if there are 2 reactants? If so, this limitation should be highlighted, as it would be a significant hindrance to real-world usability. The paper needs to explicitly state whether the post-adaptation step is limited to two reactants, and if so, discuss the implications of this limitation.

(W3): Several parts of the work are not clear, which prevent full understanding of some of the modelling or algorithmic details – see the "Questions" section for concrete examples. Finally, the writing needs improvement to make the paper reasonably easy to read (see the "Nitpicks" section below for concrete suggestions). The lack of clarity in the methodology section makes it difficult to reproduce the results, and the writing style needs to be improved to enhance readability.

### Questions
(Q1): Is Equation 4 fully mathematically correct? I am a bit confused by the notation and the disappearance of the integral. 

(Q2): Could you elaborate on "We have obtained a trained network $p_θ$ in the last stage, so we freeze g and x in the graph and continue to train $p_θ$."? Is the overall networks trained in stages utilizing different training "datasets"? 

(Q3): Could you elaborate on Section 2.2? I feel like the reader needs to fill in a lot of details to understand it, e.g. infer the exact structure of $a_1$, $b_1$ and $b_2$ (how many ones/zeros); it is also confusing that these are used to define $v_1$ and $v_2$ before being properly introduced themselves.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method for generating reactants of a product as two-stage diffusion model: first one generates additional atoms needed, and then connects them with the product.

### Strengths
- The main idea of predicting in two stages is good, and connects seemingly to how reactions work. The first stage can be seen as gathering the required extra atoms, and second stage is motivated by finding the reaction center. This part could have been strenghtened with more chemical analysis and motivation.
- The performance is competetive, but perhaps a bit inconclusive.

### Weaknesses
 - The paper is poorly written, and is not up to par of ICLR publications. The math suffers from adhoc presentation wrt densities, distributions and mappings. I'm not convinced the method is mathematically correctly presented. Specifically, the use of notation like f(p()) and f(p*p/P_X) is unclear and likely incorrect. Mapping a density value to something else, or dividing a density evaluation by a distribution, does not make mathematical sense. The notation f^{-1} is also problematic, as the mapping f is unlikely to be invertible in practice.
- The method is incremental: the diffusion models are taken off-the-shelf, and also the overall approach of group/bond generation is already seemingly known. It’s difficult to see why this method works well, and I suspect it’s mostly transformer tuning. This is not elaborated in the paper. Finally, the method is poorly motivated and novelties are vague. I think this is a succesful engineering effort towards solving an important problem, but scientifically there is very little contribution.



### Questions
- The introduction is vaguely written and I couldn’t follow what are the open problems this work tackles, or what are its contributions or their motivations. Many sentences are just impossible to understand. A good example of this is the incomprehensible sentence: “However, directly following the chemical reaction tem-plate could render the property of exploration on the distribution transformation of the diffusion model also be contrast to the data inherent structure by adding artifacted order to the motif and bonds.” (??) The intro also claims that autoregressive models are bad (yet this paper proposes a diffusion model), and that accumulating errors is somehow good. I don’t understand what the paper means by “reset”.
- The f is unlikely to be invertible, so the notation f^{-1} seems quite adhoc.
- The f(p()) notation seems nonsensical. You are mapping a density value to something. This does not seem to make sense. Similarly, the f( p*p/P_X ) is also nonsense: you can’t divide a density evaluation with a distribution, and then map it to something.
- I don’t understand fig2. So we start with 3 balls in the left: what are these? Then they become 3 colored balls with one edge. What does this mean? Are the balls atoms and colors the atom types?
- How do you know how many extra atoms to add (the external group)? What does “noisy” external group mean?
- Eq 6 feels nonsensical: what does it mean to have a loss between x and p(x)? One is a graph, another is a scalar.

### Soundness
2 fair

### Presentation
1 poor

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
This paper proposes a retrosynthesis prediction method under the semi-template setting which leverages some chemical logics. Specifically, whereas the existing semi-template methods consist of predicting the reaction center and then predicting the synthon completion, the authors decompose the retrosynthesis into three steps: 1) the external group generation, 2) the external bond generation, and 3) the post-adaption. The first two steps (i.e. the external group generation and the external bond generation) are modeled by the discrete denoising diffusion model, and in the last step (i.e. the post-adaption) the retrosynthesis is completed by leveraging the prior knowledge of the chemical reactions. The authors compare the proposed method with the template-based, template-free, and semi-template methods.

### Strengths
1. To my knowledge, this work is the first work to apply the diffusion model for planning the retrosynthesis.
2. By splitting the prediction of retrosynthesis into three stages, the proposed method is advantageous to reduce the search space. First, the external group generation and external bond generation have similar properties with the reaction center prediction and the synthon completion, which are an easier way to directly predict the retrosynthesis. Also, leveraging the chemical knowledge in the post-adaption stage is an efficient way to reduce the search space of the previous two stages.
3. The ablation study is insightful to understand the proposed method and well-designed to compare with the baselines.

### Weaknesses
1. The diffusion models usually require more time. In this paper, the two stage diffusion models could be less efficient than other baselines in terms of the inference time. Specifically, the iterative nature of the denoising process in diffusion models, involving multiple forward and reverse passes, can lead to significant computational overhead, especially when compared to direct prediction methods. The two-stage approach, while beneficial for breaking down the problem, might exacerbate this issue by requiring two separate diffusion processes.
2. For the top-1 accuracy, the performance gain of the proposed method is marginal. However, it outperforms in top-3, 5, and 10 accuracy. The marginal improvement in top-1 accuracy suggests that while the method is capable of generating correct retrosynthetic routes, it does not consistently identify the single best route. This could indicate a limitation in the model's ability to rank or prioritize the generated routes, which is crucial for practical applications where a single, highly accurate prediction is often desired.

### Questions
1. How to preprocess the dataset to get the intermediates right before the post-adaption?
2. Can the proposed post-adaption cover all the reactions?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
