# On the Identifiability of Nonlinear Representation Learning with General Noise

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 5, 5, 8, 5

## Abstract
Noise is pervasive in real-world data, posing significant challenges to reliably uncovering latent generative processes. While evolution may have enabled the brain to solve such problems over millions of years, machine learning faces this task in just a few years. Most prior identifiability theories, even under restrictive assumptions like linear generating functions, are limited to handling only additive noise and fail to address nonparametric noise. In contrast, we study the problem of provably learning nonlinear representations in the presence of nonparametric noise. Specifically, we show that, under certain structural conditions between latent and observed variables, latent factors can be identified up to element-wise transformations, even when both the generative processes and noise are nonlinear and lack specific parametric forms. We further present extensions of the general framework, demonstrating trade-offs between different assumptions and the identifiability of latent variables in the presence of both noise and distortions. Moreover, we prove that the underlying directed acyclic graph can be recovered even with nonlinear measurement errors, offering independent insights into structure learning. Our theoretical results are validated on both synthetic and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper gives conditions for identifying latent variables up to an element-wise transformation under general noise (i.e. there's no assumption of additive noise in the mixing / generative function). The show results under general noise with three main assumptions (Nondegeneracy, variability and structural sparsity), and then show how assuming additive noise allows them to drop the variability assumption. Finally in theorem 3 they give a more general noise condition, which can be extended to learning a causal DAG.

### Strengths
The theory gives strong results: they have a more general noise condition (in that they do not need to assume additivity), while reducing the number environments needed to identify the latents from n (where n is the number of latents) to 2. 

They are also able to identify causal DAGs of the form given in figure 5, by leveraging the equivalence between the mixing function and the DAG for problems of that form (there are many problems in causal representation learning where that won't be true because there isn't a fixed DAG that connects latents & observations; but it is still a useful observation).

### Weaknesses
My complaints are mostly around presentation. I felt that the paper does a poor job of explaining its results & it tends to oversell the practical relevance.

* **Explanation** I am very familiar with this literature and I found it hard to see why the assumptions leveraged in this paper lead to just strong identifiability results. For example, whether or not *(Variability exists)* is assumed, is the key difference between Theorem 1 and 2 (assuming additive noise allow one to drop the assumption that variability exists), but I couldn't see where in the proof the assumption that variability exists is used (it isn't referenced anywhere).
  
  Lines 226 - 230 explain (correctly) that most identifiability results need at least O(n) (where n is the number of latents) to disentangle latents, but it doesn't explain *how* this approach avoids that requirement? What are you leveraging to avoid that? The example doesn't give any insight because it is a case where there's only two parameters & two environments, so it's not surprising that its sufficient. Is it that you only require two environments to separate the noise from the latents or something else?
  
  Finally, I think giving a proof sketch in the main paper is a far better use of space than some of the examples that were given. I think the reader should be able to understand the main steps of the proofs in the main text without having to go through all the details in the appendix.
* **Overselling applications** the paper lists many applications from medical imaging to finance where general noise models are necessary, and makes it sound like extending identifiability results to these settings is all that stands in the way of applications. E.g. in the statement *"the capacity to handle general, nonparametric noise extends the applicability of the proposed theory across a wide range of real-world scenarios, regardless of the complexity of the noise"*. Or *"This is crucial for applications such as dependable patient monitoring systems. [line 302]"*.

  While it's good to know that these settings are identifiable, we need to be far more upfront about the limitations of causal representation learning methods. There is a big gap between theory and practice. These methods all assume that we perfectly fit the data distribution with no constraints on model capacity & it's not at all clear how they perform in finite samples with estimation error. That is likely to be a far bigger block to practical application than identifiability. Or put differently, identifiability is necessary, but far from sufficient for practical application, and making that clear is important (or alternatively, provide convincing experiments in real world settings, not toy problems like MNIST / fashion MNIST).  
* **Unconvincing experiments** Simple simulations are fine as a sanity check, but we have to move past these synthetic problems in evaluation. The simulation results don't give enough detail to properly evaluate, but the data generating process appears to be just a simple diffeomorphism defined by a normalizing flow model (I'm guessing here). If that's the case, you're in the well-specified case, so it's far more simple than any real world scenario. 
* I liked the MNIST and FashionMNIST examples a little more - but they also expose just how unreliable and hard-to-work-with these methods are in practice. For example, in the MNIST example, panel 2 and 3 are interpreted as capturing hight and "right slope" respectively, but they're also clearly entangled with stroke width (the right most columns uses thinner pen strokes than the left most columns in both images). And I couldn't understand the latents in the FashionMNIST examples. I think its better to be upfront about these limitations in the main text rather than bury it in the appendix.

### Questions
What makes the general noise setting fundamentally different from the noiseless setting? If I have method that can identify latents in the noiseless setting with n variables, can I not just treat the noise variable as the n+1'th latent and apply an existing approach?

Assuming the above is true, why didn't you empirically compare to any existing methods?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors consider the problem of Element-wise Identifiability of the latent variables $\mathbf{z}$, i.e. up to the permutation and element-wise (coordinate-wise) invertible transformation of these latent variables. As the main contribution authors propose sufficiency conditions under which the latent variables $\amthbf{z}$ are element-wise identifiable for the general case of generative models. Additionally, they consider two subcases of this generative model one of which is generative models with additive noise, and prove similar results. Also, the authors provide the result of causal structure learning for the specific subcase of the causal model with additive noise.

### Strengths
As the main result, authors propose the sufficiency conditions for the element-wise identifiability of the latent variables under general assumptions, i.e:
- no restrictions on the noise (e.g. as non-Gaussian, etc);
- no restrictions on the generative mechanism f() (e.g. as additive noise model, etc).
This generality of the result is very interesting from a theoretical point of view that the latent space can be learned uniquely up to some permutation and element-wise invertible transformation.

### Weaknesses
 - The paper is missing the citation of some important theoretical results from the field. For example:
  -  Peters, Jonas, et al. "Causal discovery with continuous additive noise models." (2014). This work solves the causal discovery problem for the general SEM with additive noise, while the authors in section 4.3 consider a subcase of the general SEM with additive noise. It is important to specify the limitations of both works and the importance of the proposed results compared to already existing ones.
- The paper is hard to read due to the lack of sufficient explanatory details of the theoretical constructs and manipulations. More details in the questions below.
- The paper proposes only identifiability guarantees, but there is no method proposed to identify the latent variable $\mathbf{z}$. Moreover, guarantees of identifiability of the latent variables up to element-wise invertible transformation are quite restrictive since the invertible transformation can be very complex and infeasible to learn.
- The generative model in Section 4.2 is just a specific case of the model considered in theorem 1, therefore it is not clear what is new contribution of the results presented in section 4.2 with respect to theorem 1.
- It is not clear how restrictive the assumption "Variability exists". More specifically, it is not obvious for me why Example 1 satisfy this assumption. More details in the question part.

### Questions
- The assumption "Variability exists" is an analogy for the assumption of "Domain Variability" (Kong et al. 2022). However, (Kong et al. 2022) require that for any set A there exist two realizations of unobserved variables $\mathbf{u}$ (domains) such that two integrals are not equal. However, in this work authors require that there exist two domains $d_1$ and $d_2$ such that for any set A the two specific integrals are not equal, that is much much stronger assumption. Additionally, it is not clear what these domains $d_1$ and $d_2$ are in the given model. Finally, the authors provide example 1 in which they propose a model that should satisfy the assumption "Variability exists". However, it is not clear from the given explanations why the considered integral would not be equal to 0. Moreover, the statement is only given for the set A of a specific structure, but it has to be true for arbitrary set A that satisfies the conditions from the assumption "Variability exists".
- In the proof of theorem 1 the authors refer to steps 1, 2, and 3 in the proof of Theorem 4.2 Kong et al. (2022) from which they conclude that some part of Jacobian is zero. However, it is not clear how the assumptions of (Kong et al. (2022)) correspond to the assumptions considered in this work and how the setting of the problems maps to each other. Therefore it's not clear and hard to follow how the results of steps 1, 2, and 3 (which take a few pages in Kong et al. (2022)) adjust to the proof considered in this work. I think all of these steps should be rewritten explicitly in the proof so anyone can follow it.
- Also, the latent variables $\mathbf{z}$ and noise $\epsilon$ are symmetric with respect to the generating mechanism $\mathbf{x}=f(\mathbf{z}, \mathbf{\epsilon})$. Therefore I would like to ask the authors if there is anything that can stop noise $\mathbf{\epsilon}$ to follow the same assumptions considered for $\mathbf{z}$. And if not, then how we can make sure that our algorithm recovers latent variables $\mathbf{z}$ instead of noise $\mathbf{\epsilon}$?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper explores learning the latent structure of data in the presence of non-parametric noise. The author derived conditions for model generation under which the latent variables can be identified. The analysis was then extended to various data generation models, establishing identifiable conditions for each.

### Strengths
The motivations and results are clearly presented, despite the theoretical focus and extensive mathematical derivations. The assumptions and extensions of the results are explained in detail. The main result (Theorem 1) is effectively extended to several commonly encountered models in Theorems 2, 3, and 4.

### Weaknesses
1. It is unclear how Definition 1 (element-wise identifiability) is commonly used in the field of latent variable identification, as only two papers (by the same author) are cited below this definition.
2. In all the theorems, the author notes that the dataset should be sufficiently large. However, it is unclear what qualifies as 'large' and how this requirement is applied in the proofs. This lack of specificity makes it difficult to assess the practical applicability of the theoretical results. It is not clear if the 'sufficiently large' requirement implies a specific sample complexity, or if it is merely an asymptotic condition.
3. The main challenge of proving Theorem 1, as compared to previous works, is not clearly explained. The novelty of the approach is not clearly articulated, making it difficult to assess the significance of the contribution. It is not clear what specific assumptions or techniques from previous works are being relaxed or improved upon.

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper clearly sets up a set of nonparametric assumptions that allow for identifiability of latent factors, a fundamental problem in theoretical machine learning.

### Strengths
This paper clearly sets up a set of nonparametric assumptions that allow for identifiability of latent factors, a fundamental problem in theoretical machine learning. The assumptions are somewhat strong but are nicely set up and create a framework where proofs seem relatively straightforward.

The framework is applied to a wide variety of special cases that have arisen in the literature, yielding strong results in each case.

If the questions below are addressed, I believe this result would be a strong contribution to the space.

### Weaknesses
While notation is thoroughly defined and overall there is a lot of discussion, still there are many key places where details are either missing or difficult to ascertain (see questions).

The structural sparsity assumption is extremely strong, albeit somewhat understandable. That said, the paper could be somewhat more realistic when discussing the assumptions - many references are made to real-world data types that do not immediately seem to necessarily follow this framework exactly. 

The assumptions on nondegeneracy preclude linear functions, which is also understandable. 

Technically, the variability assumption is not satisfiable, since A = Z x E is not disallowed (since Z, E are not subsets of themselves). Hence p(A|d_1) = p(A|d_2) = 1 identically, violating the assumption. I think this is possibly a typo.

### Questions
Several parts of the assumptions are not clear to me. For instance, is it assumed that the 2 domains are labeled? Also, in Eq (30), it is stated that \hat{F} is estimated under a sparsity constraint - what is this constraint and where is it listed in the assumptions? 

Eq (35) - why is this without loss of generality?

In the experiment section, can more details be provided on this split between latent factors and noise factors in the synthetic data, or is this as extremely simple as it sounds? What is the "base" experiment in this case?

For the variability assumption - why are rectangular sets not included? Where is this assumption used in the proof of Thm 1, for instance?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In recent years, there has been an active development on theoretical and practical research towards learning identifiable representations. 
The most common family of data generation assumptions take the following form -- z ~Pz, x <--f(z), where z is some latent variable sampled from a distribution Pz, and f is a diffeomorphism that mixes the latents to generate the observation x. For varying assumptions either on Pz or mixing maps or other forms of assumptions on weak supervision, there has been a large body of work that establishes varying forms of identification guarantees. In contrast to existing works, this work places a special emphasis on the role of noise in generation of x. The authors propose a family of results under different assumption. 

In Theorem 1, the authors study x <--f(z,e), where z is latent, e is noise, f is diffeomorphism. 
In Theorem 2, the authors study x <-- f(z) +e, and show that some of the requirements on multiple domains in Theorem 1 can be relaxed. 
In Theorem 3 and 4, the authors study, a model with non-linear distortions and measurement error and arrive at identification guarantees (representation identification and structure identification). 

Towards, the end the authors conduct experiments to reflect the theoretical claims.

### Strengths
The current frameworks on identifiability have mostly studied additive noise models and here the authors mean to go beyond that family of models. This is an important problem, which has not been well studied and it is good to see authors taking a stab at it.    The paper tries does a good job of dividing the analysis based on family of assumptions -- i) with non-additive noise models x <--f(z,e), ii) additive noise models x <--f(z) +e, iii) non-linear distortion models with noise, and finally to iv)models with measurement error.

### Weaknesses
1. **On noise modeling**:  The authors seem to overclaim that they are the first to arrive at identifcation guarantees with general noise. I believe they are referring to the first theorem. In the first theorem the authors use the following model x<-- f(z,e), where f is a diffeomorphism. I would argue that existing frameworks on partial identification already cover these types of problems even though they do not state it like this.  One can always state existing works on partial identification in the above light. Suppose I divide my latents z into two parts z1 and z2, and x <--f(z1,z2). In this case, one can seek partial identification guarantees, where one estimates \hat{z}1 that only identifies z1 element-wise and rest of the z2 terms correspond to noise that we don't care about identifying. 
Let us take the work from Kugelgen et al. https://proceedings.neurips.cc/paper_files/paper/2021/file/8929c70f8d710e412d38da624b21c3c8-Paper.pdf. One could re-interpret their result and say the following. In their result, the authors show that there are two types of latents, content latent and style latent. If one observes a pair of observations where style latent changes but the content latent stays the same, then one can separate the content latents. At this point the problem reduces to standard noise free representation identification. 
One could also use frameworks https://arxiv.org/pdf/2401.04890 and divide latents into two blocks. The actions of an agent may impact only the latents u want to identify. 
Then there is the framework from https://arxiv.org/pdf/2306.06510, which I believe the authors are already using in their results. I would like to better understand the take of authors on the above perspective and why do they not acknowledge this properly in their work. By overclaiming about noise, the authors are not highlighting the specific challenges that they face beyond separation of content and style. 



2. **On Theorem 1**:

   a) The structure and assumptions in Theorem 1 are reminiscent of the assumptions in Theorem 1 in https://proceedings.neurips.cc/paper_files/paper/2022/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf and Theorem 4.1 in https://proceedings.neurips.cc/paper_files/paper/2023/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf. 
     Can the authors contrast their proof technique from the above papers and give some intutions on what differs?

   b) In existing works on structural sparsity, e.g., https://proceedings.neurips.cc/paper_files/paper/2022/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf, the authors relied on independence assumption on the latents. In this work, the authors do not seem to require that assumption. What is the assumption that the authors make that allows them to get rid of independence assumption? Also, this seems a bit odd because it seems to imply having noise in the setting makes the problem easier than https://proceedings.neurips.cc/paper_files/paper/2022/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf, which is fairly counterintuitive.  

   c) As I stated above, the problem of identification under noise has been reduced in the authors framework to that of block identification. For block identification, the authors proof of Theorem 1 is a direct combination of result from Kong et al. and structrual sparsity work https://proceedings.neurips.cc/paper_files/paper/2022/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf. Can the authors better tell if there is really new proof techniques that were needed to solve the problem? I again emphasize that authors seemed to highlight noise as a very difficult problem but reduce it to two well studied cases -- block identification (Kugelgen et al., Kong et al.) or deconvolution via additive noise models (Khemakhem et al.).

3. **On Theorem 2**: In this Theorem, the authors rely on additive noise assumption. Here I would like to understand why is this result any different from a generalization of Theorem 1 in https://proceedings.neurips.cc/paper_files/paper/2022/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf to additive noise models? I would argue that due to additive noise models this generalization is trivial because you rely on the deconvolution argument from Khemakhem et al.. In Khemakhem's argument, one requires to know the noise distribution to cancel both sides out in the Fourier transform (See equation 20-27 in https://arxiv.org/pdf/1907.04809). If you resort to the same sort of assumptions as Khemakhem et al., then I don't think you are going beyond what already exists in identification literature in your results (Theorem 2 to 4 all rely on additive noise models).

4. **On Theorem 3**:  The setup of Theorem 3, i.e., equations 3 and 4 seem to combine the models used in Theorem 1 and 2. Can the authors clarify this? For equation 4, we can use Theorem 2 to obtain elementwise transform of x*. After that one could use the inferred x* and use Theorem 1 for obtaining z. Why is presented as a special thing? This could just be a corollary. 

5.  **On experiments:** It would have been nice if there was one experiment reflecting the unique settings of the different theorems. I do not see that is the case. For instance, synthetic expmts for Theorem 2-4 would have been nice, both representation identification ones and causal discovery ones. 

6.  **On the writing**: I found the writing quite verbose in many places. The authors seem to give examples without giving citations. For instance,  see lines 165-188, lines 298-308, lines 357-369.

### Questions
In the weaknesses section itself I have mentioned my concerns and questions. Please refer to that section.

### Soundness
2

### Presentation
2

### Contribution
2
