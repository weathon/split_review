# Identifiable Latent Polynomial Causal Models through the Lens of Change

- Decision: Accept
- Avg Score: 5.40
- Scores: 3, 6, 6, 6, 6

## Abstract
Causal representation learning aims to unveil latent high-level causal representations from observed low-level data. One of its primary tasks is to provide reliable assurance of identifying these latent causal models, known as \textit{identifiability}. A recent breakthrough explores identifiability by leveraging the change of causal influences among latent causal variables across multiple environments \citep{liu2022identifying}. However, this progress rests on the assumption that the causal relationships among latent causal variables adhere strictly to linear Gaussian models. In this paper, we extend the scope of latent causal models to involve nonlinear causal relationships, represented by polynomial models, and general noise distributions conforming to the exponential family. Additionally, we investigate the necessity of imposing changes on all causal parameters and present partial identifiability results when part of them remains unchanged. Further, we propose a novel empirical estimation method, grounded in our theoretical finding, that enables learning consistent latent causal representations. Our experimental results, obtained from both synthetic and real-world data, validate our theoretical contributions concerning identifiability and consistency.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The present manuscript is concerned with the extension of Liu et al. 2022's identifiability result to non-linear models with more general noise terms. The authors present as core contribution a theorem that allows for polynomial models and exponential family noise. A brief discussion on the violation of change of the exogenous terms is presented. Finally, an empirical section on non- and synthetic data sets.

### Strengths
IMHO the paper's noteworthy strengths are limited to their idea rather than the execution, therefore, they should be considered (where applicable) as counterfactuals for the moment. Said "potential" strengths are considered one-by-one in the following list (the list is ordered in correspondence to the paper presentation):
* Causal Representation Learning is an exciting and challenging avenue of research, naturally, extending prior results, especially the generalization sort of results, through precise characterization of key necessities is of great value. The authors place an effort in getting prior results to work for larger model classes such as polynomials.
* An effort of presenting a self-enclosed treatise, covering both theory and empirics.
* A discussion of partiality, as arguably most of the time in practice we work with approximations.
* Although this should IMO not count as "strength", given that a large portions of papers within the community don't abide by this, but the fact that the authors present a clear and transparent communication of their assumptions.

### Weaknesses
The paper suffers from several disadvantages, ranging in importance from minor to more fundamental. The more fundamental ones are of major content/technical concern, and given that this review takes a content-centric approach, they weigh the most for the low scoring. The following list - again one-by-one - aims to provide specific pointers with improvement suggestions if applicable (please note, the list is unordered):
* Liu et al. 2022 plays a central role in this work, since this work poses a direct successor in the form of an incremental improvement. While an incremental improvement can be of substantial nature, IMHO this work poses a Corollary-type of discussion over Liu et al. Furthermore, the presentation (especially in direct comparison to Liu et al.) does not provide any further justice to the present manuscript's proposed contribution. There is an abundance of repetition of the form "we've extended it now" accompanied by a lack of how alleged extension was achieved. Consulting the appendix did not resolve this major concern. The core issue is not just that the work builds on Liu et al., but that the specific technical advancements and their necessity are not clearly articulated. The manuscript fails to demonstrate why the move to polynomial models and exponential family noise is non-trivial, and what specific challenges these extensions introduce and overcome. The reader is left with the impression that these are merely substitutions rather than significant theoretical contributions.
* Kronecker product definition is not clear, not the usual definition e.g. $(a_1, a_2) \times B = (a_1\cdot B, a_2\cdot B)$. The notation used for the Kronecker product is non-standard and not adequately explained. The authors should clearly define their specific variant of the Kronecker product, highlighting how it differs from the standard definition and why this particular variant is necessary for their theoretical framework. Without a precise definition, the subsequent mathematical derivations become difficult to follow and verify.
* Although I'm confident in being able to guess what the authors refer to in their convoluted discussion on the data-generating process, it really does not help the fact that all shades of exogenous/latent terms (z, u, n) are not being explored thoroughly from first principles. Putting myself in the shoes of a reader who would be unfimiliar with the literature, I'd be tempted to expect that this portion would lead to major confusion. The roles of the latent variables z, u, and n are not clearly distinguished, and their relationships within the data-generating process are not rigorously defined. The authors should provide a more detailed explanation of how these variables interact and influence the observed data, including a discussion of the assumptions made about their distributions and dependencies. A more thorough treatment from first principles is needed to ensure the accessibility and clarity of the model.
* Unusual, and IMHO absurd, number of assumptions paired with severity in some cases (e.g. bijectivity of $\mathbf{f}$ is exploited oftentimes and arguably standard within the literature, although this should be questioned as well at some point, but existence of a suitable $\mathbf{L}$ seems more tricky). This point shines especially in considerations of claims of appraisal made by the authors, such as "[...] significantly bridg[ing] the divide between foundational theory and practical applications", that seem to overestimate the presented contribution(s) and this, with all due to respect, in a debatably arrogant manner. The assumptions, particularly the existence of a suitable matrix $\mathbf{L}$, are not sufficiently justified. The authors should provide a more detailed discussion of the implications of these assumptions and the conditions under which they are likely to hold in practice. The claim of bridging the gap between theory and practice is not supported by the current presentation, as the assumptions appear quite restrictive and potentially unrealistic in many real-world scenarios.
* Corollary 3.2. seems to carry no value when considering that the whole paradigm of change of causal influence is based on the complete change assumption. The purpose and implications of Corollary 3.2 are unclear. It is not evident why this result is important or how it contributes to the overall understanding of the identifiability problem. The authors need to provide a clearer explanation of the motivation behind this corollary and its relevance to the main findings of the paper.

### Questions
TL;DR: No questions.

Even though I've checked the appendix, I've not done so in utmost detail, still, I'm confident in being able to guess what the authors actually mean or refer to in situations of uncertainty, therefore, no questions are derived on that end. Furthermore, the lack of discussions on the actual key insights, for making the transition to polynomials & the exponential family work, does not allow me to raise any further questions.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The papers deal with the identification of latent causal models from high-dimensional observations and provide results for the case of polynomial causal relationships, which extends over the prior results that were limited to linear causal relationships along with gaussian noise. They utilize the commonly used assumption of an exponential family distribution conditioned on surrogate variables for the noise variables, which helps them identify the noise variables up to permutation and scaling. Then they show how the identification guarantees on the noise variables can be used to get identification guarantees on the latent variables themselves using the assumption of polynomial functional relationships that show variation with the surrogate variable, similar to recent works leveraging interventional data for latent identification.

### Strengths
* The paper is well-written with a clear description of the various assumptions needed for the theoretical results, along with an extremely good proof sketch! Further, the discussion on prior work is quite easy to follow and places the contributions of the work in a good manner as compared to them.

* The identification result provided in the paper uses fairly standard assumptions in the literature, but the application for the task of learning the latent causal relationships (not just the latent causal variables) is novel, and also somewhat significant as it is not limited only to the case of linear gaussian latent causal model.

* The proposed approach is principled and the claims made in the paper are supported by experimentation over various benchmarks, however, the scale of the experiments is limited (refer to the Weaknesses section below for more details).

### Weaknesses
 * My major concern with the work is regarding the technical contribution and significance of the proposed identification result. The proof uses common ideas of exponential family distribution [1] to obtain identification guarantees up to permutation and scaling for the noise variables. Further, the idea of using the changing distribution of latent variables identified up to polynomial mixing can be used to obtain permutation and scaling identification guarantees has been explored in prior works [2]. While I agree that the application of these ideas to the task of learning latent causal relationships is not trivial (as noted in the Strengths section above), I am not convinced by the significance of the proposed identification result. Specifically, the reliance on the exponential family assumption for noise variable identification, while standard, limits the applicability of the method in real-world scenarios where noise distributions may deviate significantly from this assumption. Moreover, while the authors extend the identification to polynomial relationships, the core idea of leveraging surrogate variables and distributional changes for identification remains similar to existing approaches. In terms of only the latent identification (not recovering causal relationships), the prior works that leverage interventional data can already provide permutation and scaling guarantees with much more general latent structures. For the task of learning the latent causal relationships, the permutation indeterminacy in the learned latents would pose a huge challenge which the authors circumvented by assuming the correct topological order. This makes it difficult for me to assess the importance of the proposed identification result.

* While I appreciate the experimentation over several benchmarks, the scale (dimension of the latent variables) of the experiments is too small, with the maximum dimension of the latent space being 5. It would be nice to see the results with the proposed approach for larger latent dimensions ($d= 10$ or $d=20$ at least) for the synthetic benchmark. Furthermore, the evaluation could be strengthened by including more complex synthetic datasets that incorporate non-polynomial relationships or more realistic noise structures, which would provide a more robust assessment of the method's performance.

### Questions
I would mostly like a follow-up discussion on the concerns I raised in the Weaknesses section above. There are some other minor question mentioned below:

* Is there any particular reason why the authors did not compare against several latent identification works that leverage interventional data? That would be a better choice of baselines as compared to Beta-VAE, which does not explicitly utilize the variation of latent variables with auxiliary variables. 

* It would be good to plot the F1 score along with SHD for the performance of latent causal discovery as well. The authors could maybe set a threshold to determine the latent causal structure from the functional relationships and compare that against the true latent causal graph.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel theoretical result for causal representation learning, where the latent causal variables and structures are identified by exploiting the changes of causal influences across multiple environments. Built upon (Liu et al., 2022), the paper generalizes this previous result from linear Gaussian models to polynomial models with exponential family noise, as well as reducing the number of required environments. Identifiability results under different scenarios of changing coefficients were also discussed in detail. The paper also presents an empirical estimation method and validates it on synthetic and real-world data

### Strengths
- In general the writing and presentation of the relatively clear and easy to understand.

- The paper tackles an important and challenging problem of learning latent causal representations from observational data,  and makes significant theoretical contributions by extending the scope of latent causal models to nonlinear and non-Gaussian cases, and relaxing the number of required environments. 
- The paper did not stop after presenting their main results, but also provides in-depth discussions on partial identifiability results which is very useful and insightful. This will help provide more guidance under more realistic scenarios in practice.

### Weaknesses
I appreciate your feedback. Here's an improved version of the weaknesses section:

1. **Latent structure identifiability**: While the paper makes significant strides in latent variable identifiability, it does not discuss the identifiability of the latent structure under the equivalence class. I understand that once the latent variable values are identified, the latent structure can be recovered trivially. However, given that the latent variables are only recovered up to an equivalence class, especially for partial identification case, it is unclear how would these affect the latent structure identification. Specifically, the paper does not address whether the identified equivalence class of latent variables leads to a unique or an equivalence class of causal graphs. This is a crucial aspect in causal representation learning, as understanding the underlying causal structure is often more important than identifying individual variables. The paper could benefit from a more thorough discussion or analysis on this aspect, including a formal definition of identifiability for the latent graph structure.

2. **Functional assumption**: The necessity and expressiveness of the polynomial assumption are not adequately addressed in the paper. While it's understood that this assumption is needed for identifiability, it would be beneficial to have a more detailed discussion on why this specific form is chosen and how expressive it can be in capturing complex causal relationships. It would also be interesting to explore if there are other forms or assumptions that could achieve similar results. For example, the paper could discuss whether the polynomial assumption limits the types of causal relationships that can be modeled, and whether other function classes like splines or neural networks could be considered, even if they require different identifiability conditions. The practical implications of using a polynomial model, such as the potential for overfitting with high-degree polynomials, should also be addressed.

3. **Presentation**: Given that most of the assumptions have a strong graphical interpretation, the paper could benefit from adding more illustrations or visualizations to help readers better understand these assumptions and their implications. For example, visual representations of the different types of coefficient changes, or the impact of different noise distributions on the identifiability results, would greatly enhance the clarity of the paper.

### Questions
See my concerns in previous sections.

### Soundness
4 excellent

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
UPDATE: The revised manuscript seems to address the concerns I had, though have not had the opportunity to re-review it. I have increased my score accordingly.

This paper approaches the problem of identifying the latent variable causal model from observed data, by leveraging changes in the causal mechanisms across environments. Identification here means finding the graph as well as the causal mechanisms. The causal mechanisms are generalized compared to previous work, allowing polynomial equations and exponential family noise distributions.

### Strengths
The latent causal representation learning problem is important, and I believe the extension proposed here is a significant improvement compared to previous work.

The writing is overall of a good quality. I appreciate the "proof sketch" and "insights" paragraphs following the main results.

### Weaknesses
The formal presentation needs work: most importantly, core concepts are ambiguous (see below for details). As a result, I am currently not confident about the soundness of the results. I hope these issues can be addressed with relatively little work.

"Identifiability": It is expected that it is impossible to exactly reconstruct the latent variables from the observed ones, e.g. due to the possibilities of permutation and scaling. So I would expect that your objective is identification up to certain transformations. However, a definition is not given and it remains unclear what you mean precisely by "identifiability" (and by "unidentifiability", rendering the claims of the corollaries unclear).

Changes across environments: These are mentioned frequently in section 3.3, but it difficult to determine from the text what the precise meaning is: for a coefficient, is it (A) that there exist two environments such that the coefficient is different between those, or (B) that for each pair of distinct environments, the coefficient is different between them?

Theorem 3.1 (i), "measure zero (i.e., has at the most countable number of elements)" - I assume you are referring to Lebesgue measure. In dimension 2 or higher, Lebesgue measure zero does not imply that the number of elements is countable. For instance, the set $\{(x,0)| x \in \mathbb{R} \}$ has Lebesgue measure zero, but uncountably many elements.

Theorem 3.1 (iii) - What do you mean by "takes up"? Is it that the vectors $\mathbf{u}_0$ etc are possible values that the random variable $\mathbf{u}$ can take? (I expected that footnote 1 would say something about the distinction between random variables and their values, but I'm not sure that's what it says.)

A "DAG constraint" is first mentioned in the proof sketch of the main theorem. It would be better form to introduce this assumption prior to the proof.

Start of section 3, "even if the causal relationships are nonlinear and noise distributions are non-Gaussian" - isn't the linear Gaussian case the least likely to be identifiable?

What is the $\phi$ in the proof of Corollary 3.2?

Section 4 (and elsewhere): To say that $z_1$ comes first in the causal order, write $z_1 \prec z_2 \prec \ldots$.

Equation (6): What does the $=\mathcal{N}(\ldots)$ mean? It contains unexplained notation, and $z_i$ doesn't appear except in indices.

Other comments (e.g. typographical):
Pages 5 and 7: "identifyable" -> "identifiable"
Page 5: "polynomial propriety" -> "the property"
Corollary 3.2: This statement does not appear to follow from the preceding theorem, so the name "corollary" doesn't seem appropriate.
Appendix A.4: "support that" -> "suppose that"
Appendix A.4, "proof of corollary A.3" -> "proof of corollary 3.2"
End of section 4: "APPENDIX" -> "Appendix"

### Questions
"Identifiability": It is expected that it is impossible to exactly reconstruct the latent variables from the observed ones, e.g. due to the possibilities of permutation and scaling. So I would expect that your objective is identification up to certain transformations. However, a definition is not given and it remains unclear what you mean precisely by "identifiability" (and by "unidentifiability", rendering the claims of the corollaries unclear).

Changes across environments: These are mentioned frequently in section 3.3, but it difficult to determine from the text what the precise meaning is: for a coefficient, is it (A) that there exist two environments such that the coefficient is different between those, or (B) that for each pair of distinct environments, the coefficient is different between them?

Theorem 3.1 (i), "measure zero (i.e., has at the most countable number of elements)" - I assume you are referring to Lebesgue measure. In dimension 2 or higher, Lebesgue measure zero does not imply that the number of elements is countable. For instance, the set $\\{(x,0)| x \in \mathbb{R} \\}$ has Lebesgue measure zero, but uncountably many elements.

Theorem 3.1 (iii) - What do you mean by "takes up"? Is it that the vectors $\mathbf{u}_0$ etc are possible values that the random variable $\mathbf{u}$ can take? (I expected that footnote 1 would say something about the distinction between random variables and their values, but I'm not sure that's what it says.)

A "DAG constraint" is first mentioned in the proof sketch of the main theorem. It would be better form to introduce this assumption prior to the proof.

Start of section 3, "even if the causal relationships are nonlinear and noise distributions are non-Gaussian" - isn't the linear Gaussian case the least likely to be identifiable?

What is the $\phi$ in the proof of Corollary 3.2?

Section 4 (and elsewhere): To say that $z_1$ comes first in the causal order, write $z_1 \prec z_2 \prec \ldots$.

Equation (6): What does the $=\mathcal{N}(\ldots)$ mean? It contains unexplained notation, and $z_i$ doesn't appear except in indices.

Other comments (e.g. typographical):
Pages 5 and 7: "identifyable" -> "identifiable"
Page 5: "polynomial propriety" -> "the property"
Corollary 3.2: This statement does not appear to follow from the preceding theorem, so the name "corollary" doesn't seem appropriate.
Appendix A.4: "support that" -> "suppose that"
Appendix A.4, "proof of corollary A.3" -> "proof of corollary 3.2"
End of section 4: "APPENDIX" -> "Appendix"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on identifying a causal graph in the latent space. The paper extends previous methods as follows: 1) the dependencies between the latent variables can be polynomial (previously linear), 2) the noise of the latent variables can be in the exponencial family (previously Gaussian). The paper presents a theorem for the identifiability of such models, which in general is based on the principle of observing the system in multiple different environments. The number of environments required in the proof is smaller than previous proofs (2l+1 environments vs. the previous quadratic number). The paper also presents proofs for partial (un)identifiability, basically stating that for those parts of the model where the environments behave differently the latent variable can be learned, otherwise the latent variable is unidentifiable.

My overall initial view of this article is cautiously positive. However, I have multiple questions for clarifications.

### Strengths
1) The paper is very well written. The background is clearly explained and sufficient. Sketches of proofs are given for the theorems, which nicely give intuition. Mathematical parts (model, theorems, training) are rigorously presented. Overall, the presentation makes a nice trade-off between accessibility and rigorousness.
2) The topic of latent causal modeling is challenging and the paper makes a few novel contributions in this challenging domain.
3) The experiments are reasonably thorough and demonstrate and complement the theoretical developments in an intuitive way.

### Weaknesses
1) The paper relies quite a bit on a previous (unpublished) paper (Liu et al., 2022), which affects novelty. Overall, the paper makes a few contributions but none of these seems strikingly novel or signficant. However, the overall significance/novelty seems sufficient for acceptance in my opinion.
2) The empirical experiments are somewhat artificial, and do not demonstrate real-world relevance (often the case in papers in this domain). The results are only shown for those setups where the method worked: LinearGamma, LinearBeta, PolyGamma, and not for the difficult cases: e.g. inverse Gamma etc. These could have been included in the Appendix at least, even if they didn’t work well (which the paper openly mentions).
3) Some assumptions (additivity, knowledge of the number of latent variables) seem quite strong.

### Questions
1) Could you comment on how to obtain the number of latent variables in practice? You are assuming it’s known in this paper, right?
2) Condition (iii) in Thm 3.1 has u_{2l+1} although u’s exist only until 2l. Possible typo?
3) Could you include additional intuition for conditions (iii) and (iv) of Thm 3.1?
4) Proof sketch of Thm 3.1 says  “arises from the fact that additive noise models are identifiable”. If I remember correctly, additive linear Gaussian models are not identifiable? Could you clarify how this is compatible with the sentence?
5) About Corollary 3.2: There is a condition: “if there is an unchanged coefficient in Eq 4 across environments, z is unidentifiable.”. What prevented such a condition from happening in Theorem 3.1?
6) Second line of Equation (6): Where is z hidden on the RHS of the equation?
7) Prior on lambda: you encure acyclicity by assuming lambda is lower-dimensional. Does this mean that you have to assume the causal order?
8) MPC metric: correlation between what exactly?
9) The last sentence of Discussion: “even with identifiability guarantees, it is still challenging to learn causal graphs in latent space”. It would have been interesting to explore how the number of samples affects this. Do I understand it correctly that the theory guarantees that in the limit of large number of samples the correct graph should be recovered?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
