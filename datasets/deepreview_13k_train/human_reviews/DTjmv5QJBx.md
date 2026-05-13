# Language Models Can Help to Learn High-Performing Cost Functions for Recourse

- Decision: Reject
- Scores: 5, 8, 3, 6

## Abstract
Algorithmic recourse is a specialised variant of counterfactual explanation, concerned with offering actionable recommendations to individuals who have received adverse outcomes from automated systems. Most recourse algorithms assume access to a cost function, which quantifies the effort involved in following recommendations. Such functions are useful for filtering down recourse options to those which are most actionable. In this study, we explore the use of large language models (LLMs) to help label data for training recourse cost functions, while preserving important factors such as transparency, fairness, and performance. We find that LLMs do generally align with human judgements of cost and can label data for the training of effective cost functions, moreover they can be fine-tuned with simple prompt engineering to maximise performance and improve current recourse algorithms in practice. Previously, recourse cost definitions have mainly relied on heuristics and missed the complexities of feature dependencies and fairness attributes, which has drastically limited their usefulness. Our results show that it is possible to train a high-performing, interpretable cost function by consulting an LLM via careful prompt engineering. Furthermore, these cost functions can be customised to add or remove biases as befitting the domain and problem.
Overall, this study suggests a simple, accessible method for accurately quantifying notions of cost, effort, or distance between data points that correlate with human intuition, with possible applications throughout the explainable AI field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel approach for obtaining a cost function for recourse. In the first step, an LLM (GPT-4o in this study) is queried to decide which recourse actions are low-cost. In the second step, a cost function is learned based on the LLM responses. The points at which the LLM is queried are selected to obtain good coverage of possible recourse actions. 

The paper considers four desirable criteria (feature cost, relative cost, dependant cost, and fair cost) along which the final cost function is evaluated. 

The paper uses chain-of-thought prompting and finds that instructing the LLM with the desired cost function criteria improves the LLM responses.

The paper also compares human and LLM judgements of cost in a study with human participants, finding that there is often alignment, but not always.

### Strengths
The research question studied in this paper is interesting and of practical relevance. 

The proposed methodology is interesting and could prove helpful in designing cost functions in practice. 

The paper is well-written (apart from some minor hiccups), and the experiments are reasonably well-documented.

### Weaknesses
 **Missing Baselines:** I find it hard to judge how "high-performing" the final cost functions actually are, and also how much the proposed approach improves upon alternative approaches, because there is only very limited comparison against alternative approaches. In Section 4.3, the paper compares the recommended recourse on Adult with the recourse proposed by the L1-norm, but this is a rather limited comparison and a weak baseline. As a matter of fact, I wonder how difficult the problem of designing a recourse functions actually is. For the small datasets that are considered in this study, it seems to me that it should be possible to design relatively good recourse functions "by hand", that is, with a limited amount of human labelling after taking into account the restrictions imposed by the four desiderata. Of course, and LLM might again help, but by how much does the LLM actually help here?

**Limited Evaluation:** While the newly proposed approach is well-described in the paper, it is much less discussed how a cost function should be evaluated. Indeed, this seems to be a fairly tricky question, and I suspect that the authors are well aware of this (For example: Who decides what are "relevant dependencies" in Desiderata 3). However, without clearly specifying how a cost function should be evaluated, the key claim of the paper that the obtained cost functions are "high-performing" remains subjective.

I do understand, of course, that there are evaluations in Table 1 and Figure 3 of the paper. However, these evaluations seem relatively ad-hoc to me and are not motivated in any earlier sections of the paper.

As a bit of a side note, if we were to specify very clearly how a cost function should be evaluated, should this not give rise to fairly explicit constraints on the cost function that could then be used as restrictions on the cost function during learning?

**Usage of highly popular datasets without discussion of data contamination:** This paper uses the Adult, German Credit and HELOC datasets. While these datasets are historically popular in the literature relevant to this paper, their usage with GPT-4o is problematic because of data contamination. Quite likely, GPT-4o has seen a lot of information about these highly popular datasets during pre-training. The Adult dataset, for example, is known to be partly memorized in GPT-4 (see https://arxiv.org/abs/2404.06209).

While the precise consequences of pre-training contamination on the results in this paper are very hard to judge, using (only) highly popular datasets in an evaluation with GPT-4o is not state-of-the-art. High-impact work on LLMs and tabular data (see literature references below) always attempts to include datasets that are either very recent (for example, derived from recent US census data) or datasets that have not been publicly released on the internet.    

**Missing References (minor):** In the last two years, LLMs have been broadly applied to various tasks with tabular datasets other than recourse. Here are some examples:

Feature Engineering: https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c2df4c35cdbee764ebb9e9d0acd5197-Abstract-Conference.html

Classification: https://proceedings.mlr.press/v206/hegselmann23a.html

Generation: https://arxiv.org/abs/2210.06280

None of this is cited in the paper. The authors should examine this literature and include it in their relative works section.

### Questions
- Why do you use the Adult dataset? There are better alternatives, see https://arxiv.org/abs/2108.04884 and https://github.com/socialfoundations/folktables

- Why do you choose to use latin in the paper? for example *"ad libitum"* I don't think that this terminology really helps. Also when you write *"To enforce Desideratum 2"* I would find it more helpful to write *"To enforce the relative cost criterion"*

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a method to learn cost-functions for recourse using LLMs. It uses LLMs to label pairwise comparisons comparing the ease-of-modification costs for recourse, and then fits models on this labelled data. A user study is conducted to show that LLM labels match human labels. In order to improve the LLM labelling capability, information about the desired cost functions is included in the LLM prompts. Spearman's correlation coefficient is used to determine whether the LLM output labels match this apriori information from the prompt, and additional model accuracy is reported upon being fit to the LLM label data.

### Strengths
This is a good paper and I would like to see it accepted. It presents a refreshingly original method to tackle a real-world problem that has been persistent in the literature. The use of LLMs to learn recourse costs is promising.

### Weaknesses
My primary concerns with this paper lie in the evaluation strategies employed. In the first experiment, the LLM is reportedly unsure of the answer 49% of the time, which suggests that more creative approaches may be needed to reliably elicit cost judgments from LLMs. I would recommend that the authors explicitly address this high level of uncertainty, including a discussion of its impact on the overall feasibility and reliability of their proposed method.

In the following experiments, the conclusions are challenging to interpret. Including information about the desired cost behavior in the prompt improves Spearman correlation coefficients, and models trained on these labels show higher accuracy. However, the use of a “custom prompt” seems unrealistic as it assumes an oracle can encode information about recourse costs apriori. The paper’s stated goal is to learn cost functions for recourse, so beginning with existing cost functions only to later recover them may not be particularly meaningful. While including the answer in an LLM prompt naturally brings its output closer to the target values, I don’t see the value in aiming to recover an answer that was effectively already embedded in the prompt. I would suggest the authors clarify how these results add practical value, beyond simply reproducing known information within the prompt. Demonstrating how their method might perform in more realistic scenarios would strengthen this section.

Similarly, the accuracy comparison in Table 1 - showing how well LLM responses are modeled by either a tree-based model or an MLP - is difficult to interpret in terms of the paper’s objective. I recommend the authors expand on the significance of these comparisons, particularly in light of their goal to develop effective recourse cost functions. Further clarification on the insights this offers for their method’s performance would make this section more impactful. It seems to me that the choice of model here should be agnostic to the objective of the paper. The experiments show that pairwise comparisons can be learned with reasonable accuracy, which I think is enough to justify the paper’s merit, but the relative accuracy comparisons confused me - perhaps I missed the underlying point?

### Questions
I'm unable to understand the comparisons between the standard and custom prompts, and the bearing they have on the use of LLMs to learn recourse cost functions. Perhaps a search over LLM prompts (without including the desired answer directly) to best match human intuition would be more valuable. Similarly, the accuracy comparison reported in table 1 needs better justification: what does the comparison indicate - are we just checking to ensure that LLM output labels can indeed be learned by the models?

### Soundness
2

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors study empirically the problem of learning a cost function for algorithmic recourse by replicating a Bradley-Terry model from LLM-generated data. The authors provide a framework to generate a suitable dataset, by asking an LLM to judge pairs of recourse options. Lastly, the authors evaluate their approach by training and MLP and a tree-based model to replicate the LLM-generated comparison data on three different datasets taken from the literature.

### Strengths
The problem studied by the authors is interesting and timely. The lack of suitable cost functions for recourse is a long-standing problem in the community, and the lack of reasonable data limits immensely the evaluation of recourse techniques. Exploiting LLMs to generate recourse-specific data is an interesting and novel application.

### Weaknesses
While the topic is interesting, the main issue of the present work lies in the not convincing experimental evaluation. Given that learning the cost function using a Bradley-Terry model is standard, and given that there were examples of (I believe) more realistic interactive approaches where they propose to query directly the users to elicit their cost function [1,2], I would like the evaluation of the LLM contribution to be rock solid.

**[Human-LLM Comparison]** The empirical comparison the authors presented in Section 4.1 is not enough to claim LLMs can decide as humans in the context of recourse. The analysis has mainly two issues:
- The authors ask only 6 questions for each dataset which is too few compared to the potential number of pairs $(x_i, x_i’)$ available. The number of participants is limited and might not be representative of the population (e.g., all of them are AI researchers). Lastly, the six questions might have been unintentionally cherry-picked to show this correlation. 
- The LLM was unsure 49% of the time, meaning that of those 18 questions, 9 were randomly answered. The authors claimed it is fine since humans randomly select if they are unsure, however, the authors must prove this has been the case for their experiments (e.g., 49% of the answers are also given randomly by the users).

I would suggest the authors perform a more thorough experimental analysis by increasing their sample size and the number of comparisons and evaluating how many times users answer randomly to their questions. Right now, the claim that LLMs can generate the same answers given to users is not convincingly confirmed.

**[Cost function evaluation]** In Section 4.2, the authors evaluate two different prompts by taking a standard and custom one (with additional information about the constraints of the cost function). However, the research questions and the description of the experiment results (Table 1 and Section 4.2) are hard to understand. For example, it is not clear what ground truth the authors compare against in all the experiments (e.g., from the text, it is generated by the LLMs, but using which prompt?). Moreover, it would have been interesting to generate a ground truth _from_ user comparison which would have yielded a more attractive comparison. Please see below also a question regarding Section 4.3).

I would suggest the authors state more clearly the research question in Section 4.2, the evaluation procedure and better describe their results in Section 4.2.2, considering also the desiderata described in Section 2.



### Questions
- Why did you not use a specific algorithm to find recourses while you relied simply on permutations? 
- What is the point of pairing the recourses in a graph (Section 3.2)?
- What is the baseline used to evaluate the approaches in Section 4.2? Do you have some ground truth evaluation/cost function?
- Why do you pick only different recourses to compare against the $L_1$ norm and the trained MLP (Section 4.3)? Are you not forcing them to have a different cost? (e.g., consider three recourses A, B and C. A and B have minimal cost for the MLP, while B and C have minimal cost for the $L_1$. By picking C and A, you might say that the MLP finds cheaper options than the $L_1$ norm).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to learn more realistic cost functions for algorithmic recourse (than commonly used L1/L2 costs) with the help of large language models (LLMs). The LLM's role is to assess pairs of two recourses and to decide which one is harder to implement. The ordering is then used to train an explicit cost function using learnable function approximators (e.g., trees, neural networks). The authors show that LLMs align with human judgements and background knowledge and that constraints the costs of feature manipulation can be explicitly added through the prompt.

### Strengths
Strengths:
* I think it is important to have more realistic cost functions for recourse and the problem of obtaining them is under-explored in the literature. This work contributes to this goal.
* Overall, the write-up is good to follow
* I do not have major concerns regarding soundness and see no major technical flaws in the described method

### Weaknesses
Weaknesses
* **User Study (Section 4.1.).** I have some concerns regarding the study:
    * I am not sure whether the independence test is a good measure of agreement. Independence would also not be obtained if the LLM responses and human responses are inversely correlated. In the social sciences, agreement measures such as Cohan’s kappa are established, and could be a suitable alternative to assess how high agreement beyond chance is between humans and the LLM. This scale also allows for a better interpretation of the values.
    * What exact test was used? The classical Chi2 test (https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test)  uses the null hypothesis of the observations being independent. Thus, rejecting the null hypothesis means we have sufficient evidence that they are dependent and small p values would imply dependency. However, in the Figure, it seems that large p values indicate dependency. This remains unclear to me and makes it hard to interpret the p-values. Please provide more details.
    * I am also not sure how the rejected pairs (where the LLM is uncertain) influence the score. How would the results change if scores where only the accepted pairs by the LLM are used were obtained?
    * Selection of examples: how exactly were the samples selected, how was made sure that they were realistic examples and of sufficient complexity (for straight-forward examples agreement would be obvious)? The number of two examples per dataset/desiderata seems rather low

* **Usefulness of incorporating constraints (Section 4.2).** 
    * I am not sure what the advantage of using the LLM to incorporate constraints is over explicit methods like Ustun et al. (2019). Optimization-based procedures like this one allow to directly incorporate them and also come with guarantees. However, while the LLM seems to follow the constraints given, there are no guarantees. Thus, while it is interesting to see that we can incorporate these kinds of constraints it is not a unique advantage of this method and should potentially be compared with explicit recourse models that can handle constraints.

* **The LLM seems to fail to inherently model dependencies.** To me, the most important question is whether we can leverage implicit knowledge available in LLMs to speed up modeling of feature dependencies. Specification of all these causal relationships and mutual feature dependencies is what requires most effort when specifying cost functions, because (as mentioned) the effort for these grows exponentially with the number of features. Adding non-linear cost functions for a single feature (e.g., assigning a higher general weight to it, or making changes harder in certain ranges) is still feasible and already done in many works, for instance through quantile normalization and weighting (as mentioned, see Ustun et al., 2019 and Karimi et al., 2020). It would be much more interesting to test if the LLM can help model common causal relations, e.g., (adult dataset) it is extremely hard to increase the education from bachelors to PhD in 2 years or that marital status might be related to hours worked, when children have to be taken care of etc. This is the task where I think the LLM can save most manual effort. Unfortunately, the results regarding Desideratum 3 in Table 1 show that the LLM does not automatically take care of such dependencies when not explicitly specified. Therefore, I am unsure if the current approach does really reduce the effort, as  manual specification of all dependencies seems to be required still.
* **The application of the cost function in popular recourse frameworks is missing.** I wonder how the more complex cost function affects the efficiency of recourse frameworks and how easy it is to integrate. It seems in the case study, a brute-force approach to recourse was chosen. This makes me question if the new cost function works efficiently with other recourse frameworks, e.g. through SGD, or manifold based (e.g., FACE, Poyiadzi et al., 2019) or latent space methods (e.g., Pawelczyk et al., 2020).

**Summary:** This work tackles the relevant problem of learning better cost functions for recourse. However, the results are not unexpected  and it seems that for the most challenging issue of modeling mutual feature dependencies, manual specification is still necessary. This makes it hard for me to see why this approach would be substantially better and less time-consuming than directly specifying constrains in an optimization-based recourse framework, which on the other hand come with guarantees that the constraints will be obeyed. In conclusion, while this work is technically sound and the write-up good to follow, I remain a bit doubtful that the proposed method has substantial advantages in practice.

### Questions
* Can the authors specify more details about the independence test used?
* What are the user study scores without the undecisive cases?
* Why doesn't the LLM seem to have implicit knowledge about feature dependencies in Table 1? Can the authors think of an example where the model uses its background knowledge to reason about dependencies?
* I would appreciate additional discussion on how the learned cost function can be integrated in recourse frameworks

### Soundness
3

### Presentation
4

### Contribution
2
