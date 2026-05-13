# Turning Challenges into Opportunities: How Distribution Shifts Enhance Identifiability in Causal Representation Learning

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Causal representation learning seeks to uncover latent causal variables and their relationships from observed, unstructured data, a task complicated by identifiability challenges. While distribution shifts, viewed as natural interventions on latent causal variables, often present difficulties in traditional machine learning tasks, they also create valuable opportunities for identifiability by introducing variability in latent variables. In this paper, we study a non-parametric condition characterizing the types of distribution shifts that contribute to identifiability within the context of latent additive noise models. We also present partial identifiability results when only a portion of distribution shifts meets the condition. Furthermore, we extend our findings to latent post-nonlinear causal models. Building on our theoretical results, we propose a practical algorithm facilitating the acquisition of reliable latent causal representations. Our algorithm, guided by our underlying theory, has demonstrated outstanding performance across a diverse range of synthetic and real-world datasets. The empirical observations closely align with the theoretical findings, affirming the robustness and effectiveness of our proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies non-parametric identifiability of latent variables in causal representation learning based on distribution shifts encoded in a conditional 2-parameter exponential family for noise variables, an additive noise model among latents, and a smooth invertible "observation function" mapping latents and additional independent noise to the observations. It provides conditions for full identifiability based on a novel assumption and provides partial (component-wise) identifiability based on the same assumption for certain components.

### Strengths
Overall, the paper is well structured, relatively easy to follow, provides a good overview of existing work on what assumptions can be leveraged for identifiability in CRL, and is attempts to provide some intuition for the problem setting.

### Weaknesses
What I consider to be the main weaknesses are (a) a suspected lack of novelty ('suspected' because I could not properly diagnose this due to a lack of mathematical rigor in the proofs) and (b) limited applicability due to the strong untestable results.
Finally, I do not see relevant methodological advances even though these are claimed as a contribution (l.078-079). As far as I understand from section 5, the developed method is a straight forward variational approximation of matching the required marginals with a canonical L_1 sparsity regularizer.

(a) As far as I understand, assumptions (i)-(iii) in Theorem 3.1 are well established and the way they are used in this work is also predominantly based on known results (Step I in the proof of Thm 3.1 using Sorrensen et al., 2020). Step II essentially "weaves in" the additional step from n to z, which is invertible by the additive noise assumption (another strong assumption, see below). Finally, the main novel contribution of the submission is in leveraging assumption (iv), step III, which in my view in and of itself is not a substantial addition to the existing literature, especially since assumption (iv) appears extremely restrictive (see (b)).
I also have to questions regarding the proofs:
* Throughout the proof of 3.1 in the appendix, there are multiple references to some "hatted" function 'having to belong to the same function class' to transfer properties of a non-hatted function to a hatted one. I do not see, where this assumption(?) comes from and what it means on a technical level? This appears to be a crucial element in various proofs, e.g., in lines 888-889.
* I am not yet 100% convinced by the sufficiency proof (Thm 3.5). In particular, the authors state that 944 that the required equality for matching marginals *can* be true even when $J_{\Phi_{2,1}}$ has a non-zero value, but I don't see why such a situation must always exist within the problem setting? I am thinking of situations where the partial derivative of a given component may be 0 except for a compact set where the noise distribution puts zero mass. (It was only assumed to be finite everywhere, but not positive everywhere...) Then one certainly should find counterexamples to the sufficiency statement?

(b) A key consideration when it comes to the impact of this work is whether the made (partially untestable!) assumptions can be defended in interesting real-world applications.
* In this regard, the authors mention in line 214, that 'these assumptions have been verified to be practicable in [...] application scenarios'. First, I'm not sure what it means for assumptions to be practicable, I suppose they're defendable or justified? However, when looking at the cited works, I do not see how these works justify the made assumptions in practice?
* In l.65, it is mentioned that 'additive noise models are particularly powerful in modern deep learning'. I believe this is disguising that additive noise models are another (possibly restrictive) assumption. Their assumptions happen to fit well to L2 minimization for which we have powerful deep learning techniques, but as I understand it, there is nothing inherently 'powerful' about additive noise models besides them being a heavily constrained class of models that happen to often allow for feasible theoretical analysis and are compatible with our practical learning algorithms.
* Leaving aside assumptions (i)-(iii), which may have been justified better elsewhere that I am not aware of, asusmption (iv) also appears very restrictive to me. I appreciate the attempt to justify it in protein-protein interactions (l.220+). When following up on the references, I believe (Forbes & Krueger, 2019) somehow snuck in there accidentially (not related to PPI or small molecules at all)? While I agree with PPI inhibition through small molecules is a hot and important area for drug discovery and that it appears to fit assumption (iv) on the surface level, it glances over many subtleties such as full inhibition (to the level of a partial derivative being zero) is rather unlikely and some sort of modulation being more the norm, such small molecules typically having other effects on the mechanisms involved beyond a mere soft intervention on a single protein concentration, PPI not even remotely being compatible with the DAG or additive noise assumption, etc. In short, I see the appeal of having mathematically identified a necessary and sufficient (see above) condition for identifiability, but do not see the relevance of these findings. At the same time, in my view the results are not sufficient for a purely theoretical contribution towards the mathematical aspects of identifiability in CRL.
* Lines 216-217 mention that for Theorem 3.1 one does not need to know the $\ell$ the dimensionality of the latent variable. However, for assumption (ii) to hold, one *at least* needs to know that there are $2\ell + 1$ different values of $u$. (When $u$ is an environment indicator, I could easily imagine there only to be a handful of different ones.) Hence, some form of implicit knowledge about $\ell$ is required to even have a chance that the assumptions hold?

### Questions
Besides the questions worked into the weaknesses above, there are a few minor details:

* there are multiple capitalized letters where they shouldn't be (l.63,884,...)
* l.116: we explores
* l.142: "models elucidate the underlying processes" (uncommon wording?)
* l.175: ...modulated by as outlined
* l.213: We here consider unitizes ...
* l.235: exists a team bz_1...
* l.237: groundturth
* l.239: both lambda' and lambda' must belong...
* l.250: "The whole function cl"
* some missing articles, e.g., l.387: we formulate prior model as; l.888: we have point u_i'...
* l.382: re-parametric trick
* l.393: "we simply impose L1 norm, other methods may also be flexible" (unusual wording?)
* l.888: must to belong the same

### Soundness
3

### Presentation
3

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
This paper addresses the challenge of identifiability in causal representation learning by examining how distribution shifts can be leveraged to uncover latent causal variables and their relationships. The authors establish a non-parametric condition that characterizes which types of distribution shifts contribute to identifiability within latent additive noise models, and prove partial identifiability results when only some distribution shifts meet this condition. They extend their theoretical findings to latent post-nonlinear causal models, making their framework more flexible. The authors translate their theoretical insights into a practical algorithm for learning reliable latent causal representations. Through experiments on synthetic data, image datasets, and fMRI data, they demonstrate their theoretical findings about identifiability.

### Strengths
- The paper provides complete and partial identifiability results - i.e. when not all distribution shifts adhere to Ass. (iv). This makes the results much more general and gives some hope for practical applications.
- I like the structure of how the theoretical results are introduced. First, the additive noise case is fully discussed. Then, the results are extended to the postnonlinear case. This reduces complexity for the main results and makes it easier to follow.

### Weaknesses
 - This paper touches upon a CRL setting which is quite similar to the mutli-environment setting in [1]. One main difference that I can see is the assumed intervention type. However, the authors do not contrast their results to [1]. How is this work a generalization of that?
- The experimental evaluation is lacking many important details. E.g. for the synthetic data, the used mixing function $f$ is not stated. We know from prior work that recovering latents becomes harder with increasing complexity of $f$. Also, most or all (not familiar with all) baselines are misspecified regarding the problem due to assumptions of independent latents etc. In the experimental section, this is not explicitly mentioned, and it makes it seem like the proposed method is outperforming baselines that were developed for the same setting. Furthermore, no CRL method, such as e.g. [1] and others, is compared against. This makes it difficult to understand the practical applicability of the proposed approach.

**Minor:**

- L132: There seems to be a word missing.



### Questions
- I'm confused about Assumption (iv): The setting is introduced as using soft interventions, however, as far as I understand, Ass. (iv) constrains the interventions to behave almost like a hard intervention. I.e. there exists an exogenous setting for each of the parents of a given variable such that the parents have no influence on the child. How is this assumption more general than a hard intervention?
- L160: Why do you only consider two parameter exponential family distributions? Is this a simplifying assumption, or is there some fundamental reason other distributions wouldn't work?
- L432: What is a method vs. a model?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper develops a non-parametric model of latent additive noise models to investigate the identifiability problem of general latent causal variables, extending previous linear [Liu et al., 2022] and polynomial [Liu et al., 2024] models to more general nonlinear cases. Specifically, the core Theorems 3.1 and 3.5 proposed in this work categorize distribution shifts induced by soft interventions, demonstrating that the latent causal variables $z_i$ are identifiable under certain assumptions. The authors further generalize latent additive noise models to latent post-nonlinear models to better accommodate real-world application scenarios. Finally, the learning algorithm developed based on their theoretical framework demonstrates promising performance on extensive synthetic and real-world datasets.

### Strengths
- The paper is well-structured and written fluently, with the various assumptions needed for the theoretical results clearly presented.

- The explanations of intuition and insights are particularly excellent, making the paper easy to understand and enhancing its readability.

- The main results of the paper are meaningful and insightful for real-world applications. Theorems on the partial identifiability of latent causal variables provide valuable insights and suggest feasible future approaches in the fields of domain generalization and domain adaptation.

### Weaknesses
 - The paper relies on [Liu et al., 2024], extending the structural causal equation $g_i$ from polynomial functions to nonlinear functions, and modifying condition (iv) from the existence of a function class $\lambda_{i,j}(\mathbf{u})=0$ to the existence of an environment $\mathbf{u}_{i^\prime}$ such that the partial derivative of $g_i$ with respect to each parent node is zero. Although the relaxation of these assumptions significantly enhances the model's applicability to real-world scenarios, the core motivation of leveraging distribution shifts to assess identifiability based on changes in the coefficients of $z_i$ overlaps substantially with [Liu et al., 2024]. Thus, as a follow-up work, I tend to view this paper as an incremental improvement.
- What is the essential difference between the nonlinear assumption in condition (iv) and the scenario where the coefficient of $z_i$ is zero? Is $\frac{\partial g_i}{\partial z_{i}^{\prime}}=0$ equivalent to having the coefficient $\lambda_{i,j}(\mathbf{u})=0$ in $\lambda_{i,j}(\mathbf{u})h(z_{i}^{\prime})+n$? For example, in the polynomial case $z_2=\lambda_{1,2}(\mathbf{u})z^2_1+n_2$ and the nonlinear case $z_2=\lambda_{1,2}(\mathbf{u})cos(z_1)+n_2$, it seems that condition (iv) can be uniformly reduced to the coefficient $\lambda_{1,2}(\mathbf{u})=0$. I would like to ask what makes the nonlinear condition (iv) particularly different from the scenario where the coefficient $\lambda_{i,j}(\mathbf{u})=0$ in the polynomial case.
- Could you provide some examples of unidentifiable nonlinear $g_i$? I noticed that the examples in Remark 3.2 and the Model Capacity section are all polynomial. It would be helpful if the authors could include examples illustrating condition (iv) in the nonlinear case to aid readers in understanding how it differs from condition (iv) in [Liu et al., 2024].

**Some Minor Issues**:

- Are the number of latent causal variables and the causal order given as prior information? How does the proposed theory perform with a larger number of latent causal variables? I observed that the experiments were conducted with 3-6 latent causal variables.
- More visual examples would help readers better understand these assumptions and their implications, especially indicating in a causal graph which $z_i$ are identifiable and which are not.

### Questions
- In the part of Remark 3.8 (Subspace identifiability), are the latent causal variables $z_i$ that vary across domains identifiable? In the context of OOD generalization, does the invariant feature $C$ violate condition (iv), while the spurious feature $S$ satisfies condition (iv)?
- Line 208: definition in 2 -> definition in Eq. 2
- Line 235: team $bz_1$ -> term $bz_1$
- Line 239: $\lambda^{\prime}$ and $\lambda^{\prime}$ -> $\lambda$ and $\lambda^{\prime}$
- In the paragraph "Model Capacity," should Corollary 3.1 on line 356 and line 358 be changed to Corollary 4.1?
- Line 437: Corollary 3.5 -> Theorem 3.5?

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
4

### Summary
==Post rebuttal update==

*Soft intervention*. I appreciate the authors' clarification in the rebuttal. The notion itself is clearer, but I still suspect how useful this notion is for understanding the method. Again, I cannot see how previous work's requirement of sample data of specific $u_i$ is related to hard interventions. In the context of current work, incorporating soft intervention seems no more than a notational tweak.

*Assumptions related to the noise distribution*. 
- The theory, as in Sorrenson et al. (2020) it is based on, requires certain special two-parameter exponential family members. So, instead of "we focus on two-parameter exponential family members", we should honestly say "we assume..."
- I believe the theory does *not* “eliminate the need to make assumptions about the dimensionality of latent causal or noise variables”, the same as in Sorrenson et al. (2020). 

The *“Model Capacity” remark* has not yet been updated.

The following two *similarities to Liu et al. (2022; 2024)* should be mentioned in Related work. 1) They share the same causal graphs (though the current paper does not require $g_i$ to be linear or polynomial). 2) they also use iVAE in the inference process.

**Conditioning on that authors will fix the latter three issues and make a full go-through of the draft to ensure consistent presentation, I am fine with an acceptance. But, given the current draft, I maintain my score 5.**

The issue of soft intervention is harder and I encourage the authors to elaborate more (but a fully satisfiable development could be left for future work.

==End update==

This paper builds on Liu et al. (2022; 2024), which applies nonlinear ICA to noise variables while using ANMs as a bridge between hidden causes and the noises. The main contribution here is relaxing parametric assumptions on causal relationships among hidden causes. Notably, assumption (iv) is shown to be both necessary and sufficient for identifiability, given assumptions (i)-(iii) inherited from nonlinear ICA. Empirical results demonstrate promising performance.

### Strengths
The necessary and sufficient condition (iv) is a meaningful theoretical contribution that seems both practically relevant and theoretically significant (though I haven’t verified the proof).

The approach of applying nonlinear ICA to noise variables and ANMs as a bridge is an interesting direction.

### Weaknesses
The paper could be more transparent about its limitations and the relationship to prior work; for example, the general exponential family in Eq. (1) and the novelty of the model structure and learning method are not fully clarified.

The concepts of hard vs. soft/natural interventions are unclear and add little to the understanding of the model.

The writing is unclear in places, especially in Remark 3.2 and the “Model Capacity”, which are important because they contain example models.

The experimental comparison with existing causal discovery methods could be added.

### Hard vs. Soft/Natural Interventions
The notion of “soft intervention” seems to vaguely refer to "intervention different from the standard definition". The only example given is “applying functional transformations,” which are not convincingly “particularly relevant” or “wider”. If we consider Eq. (2), assignments on $u$ could be seen as changing functions applied to $pa_i$, but this is because $u$ and $pa_i$ are separate variables, not because “soft interventions” are inherently broader.

The concept seems unnecessary for the paper, as the assignment on $u$ still formally models distribution shifts, which is a hard intervention, although $u$ may not be intentionally controlled by an agent.

Regarding assumption (iv), I see it does not require data specific to a particular $u_i$ value, but I’m unclear why previous work would. Could you clarify this with an example from previous work? It seems that whether $u$ values are necessary depends on how assumptions are used in proofs (e.g., matrix $L$ is required to construct $P$), which is the thing that needs clarification, not on the hard vs. soft intervention distinction, which seems unnecessary and confusing. Similar comments apply to Remark 3.7 from L291.

If “soft intervention” is central, a formal definition would help, along with connecting it to prior causal inference work (e.g., possibly the natural experiments [1] in economics).

### Transparency
The proposed model extends Liu et al. (2022; 2024) by removing the requirement for $g_i$ to be linear or polynomial, though the paper could clarify that the model itself is not novel.

Learning Method: The proposed approach resembles iVAE with added order and sparsity constraints, which, I believe, were considered in Liu et al. (2022; 2024).

Component-wise identifiability isn’t achieved for general exponential family distributions, as indicated in Sorrenson et al. (2020), which your proof depends on. The two-parameter requirement is for each $z_i$, and $l$ is unrestricted also in prior work. So I think your method does not differ from “existing methods that require prior knowledge of dimensionality due to the two-parameter exponential family”?

### Writing
In Remark 3.2, it would help to clarify that an unidentifiable and identifiable example are being considered from the outset. Presenting the identifiable example first might improve readability. Phrasing such as “Moreover” could be replaced with “On the other hand.” Better examples could be provided; currently, the unidentifiable example violates both (iii) and (iv), while the identifiable example satisfies both. A clearer illustration would be examples that satisfy (iii) but only one satisfies (iv).

In Remark 3.4, the sentence “In addition, linear Gaussian models…” seems unrelated and could be removed (though itself correct).

In Thm. 3.5(a), a root node vacuously satisfies (iv), so it would be clearer to state this outside the theorem and remove “if it is a root node or.”

L307: I think identifying $n$ does guarantee identifiability of $z$, though not component-wise identifiability of each $z_i$.

Both Remark 4.2 and Intuition regarding Corollary 4.1 could be removed, as they merely repeat “we can construct a new injective function f by composing f with …” in the proof sketch. Similarly, the proof sketch for Corollary 4.3 could be omitted.

The “Model Capacity” explanations are confusing, with a confusion between Thm. 3.1 and Cor. 4.1, and the examples are not clearly explained, e.g., the second example assumes $\lambda(u)=0$ for some $u$ values.

### Experiments
It would be informative to see if this method outperforms "iVAE to recover $z$ and then existing causal discovery methods to build causal graphs among $z$", particularly in the cases of Fig. 1 (right) and Fig. 7.

The synthetic and image data are limited to chain structures; if time permits, additional synthetic data with more complex structures would add value.

Why does $\beta$-VAE perform so well on the fMRI data for reasonable $\beta$ values?

### Mino/typo:

L62: “Given space constraints” could be removed.

L66: MLPs are not particularly “advanced architectures.”

L239: Typo, $\lambda’$ appears twice.

L445: “Discussion 1” →  “Intuition.” However, per the “Writing” section, “as mentioned in Discussion 1 for Corollary 4.1” could be omitted.

L483: Typo, “top to bottom and…”

### Questions
### Hard vs. Soft/Natural Interventions
The notion of “soft intervention” seems to vaguely refer to "intervention different from the standard definition". The only example given is “applying functional transformations,” which are not convincingly “particularly relevant” or “wider”. If we consider Eq. (2), assignments on $u$ could be seen as changing functions applied to $pa_i$, but this is because $u$ and $pa_i$ are separate variables, not because “soft interventions” are inherently broader.

The concept seems unnecessary for the paper, as the assignment on $u$ still formally models distribution shifts, which is a hard intervention, although $u$ may not be intentionally controlled by an agent.

Regarding assumption (iv), I see it does not require data specific to a particular $u_i$ value, but I’m unclear why previous work would. Could you clarify this with an example from previous work? It seems that whether $u$ values are necessary depends on how assumptions are used in proofs (e.g., matrix $L$ is required to construct $P$), which is the thing that needs clarification, not on the hard vs. soft intervention distinction, which seems unnecessary and confusing. Similar comments apply to Remark 3.7 from L291.

If “soft intervention” is central, a formal definition would help, along with connecting it to prior causal inference work (e.g., possibly the natural experiments [1] in economics).

[1] Rosenzweig, M. R., & Wolpin, K. I. (2000). Natural “natural experiments” in economics. Journal of Economic Literature, 38(4), 827-874.

### Transparency
The proposed model extends Liu et al. (2022; 2024) by removing the requirement for $g_i$ to be linear or polynomial, though the paper could clarify that the model itself is not novel.

Learning Method: The proposed approach resembles iVAE with added order and sparsity constraints, which, I believe, were considered in Liu et al. (2022; 2024).

Component-wise identifiability isn’t achieved for general exponential family distributions, as indicated in Sorrenson et al. (2020), which your proof depends on. The two-parameter requirement is for each $z_i$, and $l$ is unrestricted also in prior work. So I think your method does not differ from “existing methods that require prior knowledge of dimensionality due to the two-parameter exponential family”?

### Writing
In Remark 3.2, it would help to clarify that an unidentifiable and identifiable example are being considered from the outset. Presenting the identifiable example first might improve readability. Phrasing such as “Moreover” could be replaced with “On the other hand.” Better examples could be provided; currently, the unidentifiable example violates both (iii) and (iv), while the identifiable example satisfies both. A clearer illustration would be examples that satisfy (iii) but only one satisfies (iv).

In Remark 3.4, the sentence “In addition, linear Gaussian models…” seems unrelated and could be removed (though itself correct).

In Thm. 3.5(a), a root node vacuously satisfies (iv), so it would be clearer to state this outside the theorem and remove “if it is a root node or.”

L307: I think identifying $n$ does guarantee identifiability of $z$, though not component-wise identifiability of each $z_i$.

Both Remark 4.2 and Intuition regarding Corollary 4.1 could be removed, as they merely repeat “we can construct a new injective function f by composing f with …” in the proof sketch. Similarly, the proof sketch for Corollary 4.3 could be omitted.

The “Model Capacity” explanations are confusing, with a confusion between Thm. 3.1 and Cor. 4.1, and the examples are not clearly explained, e.g., the second example assumes $\lambda(u)=0$ for some $u$ values.

### Experiments
It would be informative to see if this method outperforms "iVAE to recover $z$ and then existing causal discovery methods to build causal graphs among $z$", particularly in the cases of Fig. 1 (right) and Fig. 7.

The synthetic and image data are limited to chain structures; if time permits, additional synthetic data with more complex structures would add value.

Why does $\beta$-VAE perform so well on the fMRI data for reasonable $\beta$ values?

### Mino/typo:

L62: “Given space constraints” could be removed.

L66: MLPs are not particularly “advanced architectures.”

L239: Typo, $\lambda’$ appears twice.

L445: “Discussion 1” →  “Intuition.” However, per the “Writing” section, “as mentioned in Discussion 1 for Corollary 4.1” could be omitted.

L483: Typo, “top to bottom and…”

### Soundness
3

### Presentation
2

### Contribution
3
