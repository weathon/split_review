# Time-Dependent Mirror Flows and Where to Find Them

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
Explicit regularization and implicit bias are often studied separately, though in practice, they act in tandem. However, their interplay remains poorly understood. In this work, we show that explicit regularization modifies the behavior of implicit bias and provides a mechanism to control its strength. By incorporating explicit regularization into the mirror flow framework, we present a general approach to better understand implicit biases and their potential in guiding the design of optimization problems. Our primary theoretical contribution is the characterization of regularizations and reparameterizations that induce a time-dependent Bregman function, with a discussion of the implications of its temporal variation. Importantly, our framework encompasses single-layer attention, and application to sparse coding. Extending beyond our core assumptions, we apply this framework to LoRA finetuning, revealing an implicit bias towards sparsity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper show that explicit regularization modifies the behavior of implicit bias and provides a mechanism to control its strength. The primary theoretical contribution is the characterization of regularizations and parameterizations that induce a time-dependent Bregman potential, with a discussion of the implications of its temporal variation. This framework encompasses single-layer attention, and application to sparse coding.

### Strengths
1. This paper presents sufficient conditions for incorporating explicit regularizations into the mirror flow framework and characterizes their effects by analyzing three main aspects of implicit bias: shifts in positional bias, the type of bias introduced, and the reduction in the range of values.

2. This paper proposes a systematic method for identifying these regularizations and establishes a general convergence result within this framework.

3. This paper emphasizes the impact of regularization on implicit bias, demonstrating these effects in experiments such as sparse coding, transformer attention mechanisms, and LoRA fine-tuning in large language models.

4. This paper reveals that weight decay modulates the degree of sparsification brought about by quadratic parameterizations, including those in attention mechanisms and LoRA adjustments.

### Weaknesses
1.However, their interplay remains poorly understood. This inference lack support.

2. More experiments on real world datasets are needed to verify the validity of their method.

3. This paper lacks the motivation about the behavior of implicit bias

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper studies mirror flows, with the goal of identifying how explicit regularization and the inducing parameterization affect implicit regularization.
For certain parameterizations and regularizations, it characterizes their impact.

### Strengths
- **S1: Novelty and generality** Making the interplay of explicit and implicit
  regularization concrete is certainly a relevant goal, as it provides the
  possibility to modulate the explicit regularization with time to achieve a
  specific implicit regularization. The mirror flow framework, in which the
  paper expands on this goal, provides a general framework, and the presented
  results seem general.

### Weaknesses
I found the paper extremely challenging to follow. This may be because I am only
partially familiar with mirror flows (reflected by my confidence), but I also
believe the presentation is at many points not self-consistent, lacking clarity,
and missing interpretation and relation to practical contexts. In the following,
I am pointing out some aspects that prevented me from comprehending and
appreciating the paper's contribution:

- **W1 Self-consistency and clarity:** The introduction to mirror flows is
  confusing.

  Specifically, I struggled to keep up with relating the presented math in
  Sections 3+4 to that in the introduction: the primal objective $f(x)$,
  (Equation 4), primal explicit regularization $h(x)$ (Equation 4), dual
  objective $f(g(w))$, and dual explicit regularization $h(w)$ (Equation 5). I
  think the paper would be much clearer if Sections 3+4 used notation that made
  the connections to these objects obvious. Sometimes, it is also hard to follow
  along because objects do not have names, for instance there is a function $R$
  that is always referred to as 'the function $R$'; is there a more meaningful
  name, e.g. is it related to the distance-generating function in mirror
  descent? Same with the 'Bregman potential', that is mentioned in the abstract,
  but does not seem to show up in the main text. I also found the introduction
  to mirror flows in A.1 not very helpful as it mainly consists of an
  enumeration of definitions.

  Another problem I had in keeping up with the presentation is that some of the
  steps were not clearly motivated or outlined. Therefore, I could only
  acknowledge the existence of some results, specifically the examples on
  different parameterizations in Examples 3.1+3.2, as well as their paragraphs
  in Sections 4+5, but not understand how they contribute to the bigger picture.

  Lastly, the authors introduce the concepts of positional bias and range
  shrinking in the introduction, but never explain what exactly they mean.

- **W2 Interpretation and relation to practical contexts** I could not follow
  certain interpretations, explanations, and motivations, e.g. why is it
  interesting to study the setup in Corollary 3.2? Are the parameterizations
  presented in the examples relevant in practise? How does the paragraph below
  Equation 8 relate to its math? What is the theory's prediction for LoRA in
  Section 5, and is it reflected by the empirical results? I think these are
  currently just not explained clearly enough, making it hard to assess the
  paper.

### Questions
Please see W1 and W2.

I am willing to re-assess my score if the authors find ways to clarify the presentation and motivation.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Prior work has shown that, under some conditions, the optimization dynamics of overparameterized models can be formulated as a mirror flow (Li et al. 2022). The current work extends that framework to explicitly regularized losses. In particular, it establishes a sufficient condition under which gradient flow over the explicitly regularized objective can be described as a (possibly time-varying) mirror flow. This enables proving convergence to a minimizer when the loss function is convex. Then, for several types of overparameterizations, explicitly writes the potential of the mirror flow induced by certain explicit regularizers, and discusses implications to the resulting implicit bias.

Experiments support the theoretical results.

### Strengths
Explicit regularizers, such as $L_2$ regularization, are commonly applied in practice. Hence, understanding how they modify the implicit bias of optimization for a given model is an important question in the theory of deep learning. This paper makes progress towards addressing this question. While the logarithmic parameterization $\log (u) - \log (v)$ is quite unorthodox (it is not clear where one may encounter it), the $m \odot u$ and $u^{2n} - v^{2n}$ parameterizations have been widely studied in the past in the context of linear diagonal networks, and so may be of interest to the community.

### Weaknesses
1. Perhaps the main weakness of the paper is a rather severe lack of clarity, which in turn makes it difficult to assess the implications and significance of the results. As detailed below, some definitions are missing, notation is often used without proper introduction, some theorem statements are vague, terms such as "positional bias" are used without any intuitive or formal definition, and the implications of results are also not sufficiently discussed.

2. The significance of the results may be limited due to the parameterizations that they support. I find that the discussion around which parameterizations and regularizations are captured by the proposed framework and which are not can be strengthened. In particular, is there hope of using the framework for analyzing more practical models?

3. The fact that $L_2$ regularization in matrix factorization induces a bias towards low nuclear norm for the matrix product has been shown in prior work (see, e.g., [1]). The significance and novelty of the empirical observation for attention layers and LoRA is therefore limited, in my opinion (a discussion on the relation between $L_2$ regularization and nuclear norm in attention layers also appears in [2]).

Overall, while the paper has potential to further our understanding of how explicit regularization affects the implicit bias of optimization, at its current form I do not believe it is suitable for publication. I would recommend the authors to thoroughly revise the paper and improve its clarity, for which I hope the comments below can be useful. Furthermore, the significance of the results can be strengthened by further mapping out which parameterizations and regularizations fall under the proposed framework and which do not. Currently, the most practical models captured by the framework are matrix factorizations, which appear as part of different factorized layers. However, as mentioned above, the fact that an $L_2$ regularization translates to nuclear norm minimization for matrix factorization is already known (e.g., [1]) and does not necessitate the more complex machinery.

Detailed remarks regarding clarity:
- In Definition 3.1, it is not specified what the definition of a Legendre function is. I assume the intention was to use the same definition from Li et al. 2022. I recommend either stating the definition explicitly or at least referring to an existing definition in the literature (e.g. that from Li et al. 2022).

- In line 223, it is stated that $Q$ is defined in Theorem 3.1, however, it is not clear what the precise definition of $Q$ is. Seems that it is implicitly defined by $y = Q(x, a_t)$? Though since $y$ is actually $h(w)$ and $x$ is actually $g(w)$ there is no dependence on $a_t$, which leads me to believe the definition of $Q$ is not $Q(x, a_t) = h(w)$ as one may currently infer. Please explicitly define $Q$.

- In Definition 3.2, Bregman functions are not defined. I would recommend either explicitly defining this concept or at least referring to a specific place where they are defined. I assume the intended definition is Definition A.6 from Li et al. 2022.

- It can be useful to give examples for contracting parameterized Bregman functions around Definition 3.2 to help the reader understand this concept.

- In line 242 it is stated “assume that $\nabla f$ is locally Lipschitz and $argmin \\{ f(x) : x \in dom R_{a_\infty} \\}$”. It is not clear what the second part of the assumption is, that the argmin exists?

- In line 267 it is stated that the result for separable parameterizations encompasses “all previous settings”. Which previous settings does this refer to?

- In Corollary 3.1, what do $g_{i, j}$ and $w_{i, j}$ stand for? Is it assumed here that $g(w)$ and $w$ are matrices and that $i,j$ indexes an entry in them? In that case, what are $g_i$ and $w_i$?

- In Corollary 3.1, I find the statement “To apply Theorem 3.1 we need that…” to be too vague. Is the result that the conditions of Theorem 3.1 hold if and only if this holds? Or is it just a sufficient condition? Either way it is worth explicitly stating what the conditions are. An analogous comment applies to Corollary 3.2.

- In line 345, the regularization is defined as $y = m^2 + w^2$, where $m$ and $w$ are vectors, but isn’t the regularization $y = h(w)$ supposed to be a scalar?

- In line 361, it is not clear what “positional bias” means. This term is used in several places in the paper, but nowhere is it defined even on an intuitive level. What does “positional bias” refer to?

- The paragraph starting at line 364 claims to consider an attention layer. I find this to be quite misleading as the effect of the remaining components in an attention layer (value matrix and softmax) are not considered.

- In line 366, what are the $A_j$ matrices in this case? Are they not determined by the parameterization, in which case whether or not the condition holds is determined rather than something that you can/need to assume? It is also not clear where the nuclear norm comes from in Theorem 3.3.

- In line 411 it is stated that “The shift is centered at…”. What shift does this refer to? It is not clear what is being shifted and where.

- In line 418 it is stated that the rescaling changes the implicit bias from $L_1$ to $L_2$ regularization. It is worth clarifying why this is the case.

Additional (more minor comments):
- Typo in line 32: an unnecessary apostrophe.

- I find Figure 1 to be too vague (related to the remarks on clarity above). In particular, aside from the $L_2$ to $L_1$ change in implicit bias, it is not clear what “positional bias” or “range shrinking” refers to. Would be best to either make it more understandable from the figure itself or from the caption.

- In line 73, Pesme et al. 2024 is cited for showing that gradient descent converges to the solution with lowest $L_1$ distance from initialization for overparameterized linear regression. I believe this is not the correct citation, as Pesme et al. 2024 consider classification problems. Also, this claim is not true for all overparameterized linear models, rather for some parameterizations (e.g. linear diagonal networks) and under certain technical conditions (e.g. small initializations).


[1] Dai, Z., Karzand, M., & Srebro, N. Representation costs of linear neural networks: Analysis and design. NeurIPS 2021.

[2] Khodak, M., Tenenholtz, N., Mackey, L., & Fusi, N. Initialization and regularization of factorized neural layers. ICLR 2021.

### Questions
--

### Soundness
3

### Presentation
2

### Contribution
2
