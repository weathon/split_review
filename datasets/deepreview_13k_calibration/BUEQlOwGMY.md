# Object-Based Sub-Environment Recognition

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Deep learning agents are advancing beyond laboratory settings into the open and realistic environments driven by developments in AI technologies. Since these environments consist of unique sub-environments, empirical recognition of such sub-environments that form the entire environment is essential. Through sub-environment recognition, the agent can 1) retrieve relevant sub-environments for a query, 2) track changes in its circumstances over time and space, and 3) identify similarities between different sub-environments while solving its tasks. To this end, we propose the Object-Based Sub-Environment Recognition (OBSER) framework, a novel Bayesian framework for measuring object-environment and environment-environment relationships using a feature extractor trained with metric learning. We first design the ($\epsilon,\delta$) Statistically Separable (EDS) function to evaluate to show the robustness of trained representations both theoretically and empirically that the optimized feature extractor can guarantee the precision of the proposed measures. We validate the efficacy of the OBSER framework in open-world and photorealistic environments. The result highlights the strong generalization capability and efficient inference of the proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose a framework for an agent to infer its sub-environment through the measurements of object-object, object-environment, and environment-environment relationships. The authors validate their framework in Minecraft, while also providing some preliminary results on the ImageNet dataset. The paper is well structured, and the authors show several relevant results, including the relevance of statistically separable EDS functions to achieve accurate measures for their downstream environment inference.

### Strengths
The paper is generally well structured. The authors explain each part of their proposed method in detail, including for example the relevance of statistically separable EDS functions to achieve accurate measures for their downstream environment inference, and the empirical implication of hyperparameter choice for downstream inference (e.g. the choice of Tau for KL divergence in Figure 6.).

### Weaknesses
It is hard to quickly have a notion of which parts of the proposed methods, exactly, are novel. The authors use several existing methodologies in their proposed framework, but fail to appropriately specify which of these, in particular, are novel propositions or implications. It is also hard to connect the motivation of this work to the tasks and results shown. In particular, the emphasis on the motivation for "real-world" applications, and complex natural environments is lost by the simplicity of the test settings (e.g. virtual world or fixed datasets).

It would be worthwhile to adjust the tone of the claims in the paper to better align with the results shown. The results may show interesting results in a "simulated environment, towards more complex environmental settings" perhaps even eventually leading to real-world, but as far as this work goes there is a wide gap between simulated and real-world settings, since no robotic experiments were provided. Below are some of the most relevant parts, strongly suggesting (non-existing) results in real-world settings
     - The abstract
     - The introduction should reflect this (3rd claim)
     - Figure 1: The caption should be updated (it is not, in fact, a real-world agent)  
     - Title in 6.2 should change

- Section 4: Which of these are new propositions and which of these are derived from existing work? This should be made very explicit.
- Missing y-label in Fig. 5 and Fig. 6
- English should be improved throughout:
  e.g. "which computes the kernel density accumulated with class-wise distribution.", or "We utilized pretrained weights for every models." etc.

### Questions
- It would be worthwhile to adjust the tone of the claims in the paper to better align with the results shown. The results may show interesting results in a "simulated environment, towards more complex environmental settings" perhaps even eventually leading to real-world, but as far as this work goes there is a wide gap between simulated and real-world settings, since no robotic experiments were provided. Below are some of the most relevant parts, strongly suggesting (non-existing) results in real-world settings
     - The abstract
     - The introduction should reflect this (3rd claim)
     - Figure 1: The caption should be updated (it is not, in fact, a real-world agent)  
     - Title in 6.2 should change

- Section 4: Which of these are new propositions and which of these are derived from existing work? This should be made very explicit.
- Missing y-label in Fig. 5 and Fig. 6
- English should be improved throughout:
  e.g. "which computes the kernel density accumulated with class-wise distribution.", or "We utilized pretrained weights for every models." etc.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a Bayesian framework to recognize sub-environments within complex, dynamic environments. OBSER enables agents, like robots, to identify sub-environments based on objects present, facilitating task-driven navigation and inference in open-world scenarios. The framework introduces EDS function to improve the robustness of feature representations and utilizes metric learning for object-object, object-environment, and environment-environment relationships.

### Strengths
OBSER provides a holistic approach to sub-environment recognition, measuring three relationships—object-object, object-environment, and environment-environment—which enables better contextual awareness.

The introduction of the EDS function to assess separability and concentration offers a robust way to manage feature representations, addressing a gap in object-based environmental recognition.

### Weaknesses
I find that this method may be challenging to implement for embodied robots. First, constructing episodic memory seems crucial for task completion success, yet several questions arise: (1) How was this memory constructed? (2) How could it be constructed effectively with limited experience? (3) How can retrieval be managed efficiently as memory size increases?

Most importantly, I am uncertain about how the object-object, object-environment, and environment-environment relationships contribute to embodied tasks. Without ablation studies or proof, it’s hard to determine the critical importance of these relationships.

Are there other baselines with which EDS could be compared? The paper would benefit from broader comparisons with other state-of-the-art environment recognition frameworks to better highlight OBSER's distinct advantages and limitations in context.

The diversities of Minecraft environment and objects seems limited.

OBSER's reliance on object distribution might limit its effectiveness in sub-environments where objects are scarce or ambiguous, which could impact performance in less structured real-world spaces.

### Questions
Please refer to the weakness.

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
The paper proposes the Object-Based Sub-Environment Recognition (OBSER) framework, a novel Bayesian framework for measuring object-environment and environment-environment relationships using a feature extractor trained with metric learning. The key idea is the introduction of a statistically separable (EDS) function and using it to perform (i) object-object similarity, which involves obtaining the closest class of objects from a list given a query object, (ii) object-environment recognition, which involves retrieving the closest environment to a given object and (iii) environment-environment recognition, which defines the difference between two sub-environments. Experiments to recognize environments are done on two datasets, the ImageNet based dataset, and a dataset of curated environments from Minecraft.

### Strengths
-	The primary motivation behind the paper is sound. Indeed, environment recognition using relationships between objects and environments is an interesting problem in embodied agents.
-	The results do illustrate the claim that higher difference between epsilon and delta values lead to a better accuracy score. This is reflected in models for both Tables 1 and 2.

### Weaknesses
 - Not clear what objects and environment are: By reading the paper starting from the introduction, it is not clear what constitutes an "object" and an "environment" in the context of the ImageNet dataset. The authors provide examples of objects and biomes as environments in the Minecraft example, but the lack of analogous examples for ImageNet hinders a clear understanding of the proposed framework's applicability to this widely used dataset. Providing concrete examples of what constitutes an object and environment within the ImageNet dataset would improve clarity.
- Results are difficult to interpret: The paper presents classification accuracies in Tables 1 and 2 for ImageNet and Minecraft datasets, respectively. However, the relationship between the presented results and the core claims of the paper is not immediately obvious. For instance, it is unclear whether the primary observation is the difference between metric learning and self-supervised learning methods, or the relationship between EDS values and different models. A more detailed explanation connecting the results in these tables to the statistically separable (EDS) function and the three types of recognition tasks would enhance interpretability. Additionally, the rationale behind choosing specific classifiers (linear, mean, KNN) and their respective shot values (1,3,5 vs 3,5,7) is not provided, making it difficult to assess the experimental design choices.
- Real-world applications are unclear: The paper's motivation centers around environment recognition in embodied agents. However, the connection between the proposed framework and real-world object and scene recognition is not adequately established. The absence of experiments or examples involving real-world object scenes or object recognition tasks limits the perceived impact of this work. Demonstrating the framework's performance on a dataset with human-centric objects and environments, beyond the simulated Minecraft environment, would strengthen the claim of real-world applicability.
- [Minor] Unnecessary math: The mathematical formulations presented in Sections 3-5, while potentially relevant, detract from the main contribution outlined in Section 4.1. Streamlining these sections or moving some of the mathematical details to the supplementary material could improve the paper's readability.
- [Minor] Many details are missing from the main paper and are present in the supplementary. The authors should consider transferring some details about the implementation, such as the process of generating artificial environments within ImageNet, from the supplementary to the main paper. This would improve the flow of the paper and reduce the need for the reader to constantly switch between the main paper and the supplementary material.

### Questions
-	Is there any justification for the type of classifiers provided in Tables 1 and 2? In Table 1, linear, mean and KNN classifiers are used, while only mean and KNN classifiers are used in Table 2. Also, why the difference between the shots of mean vs KNN (1,3,5 vs 3,5,7).
-	For the ImageNet dataset, what are some examples of objects and environments? It is unclear from reading the paper.
-	In conclusion, the authors mention that by integrating the proposed method with embodied object recognition or navigation modules, inference accuracy can be improved. Can the authors provide some justification with a real-world use-case about what is the intuition behind this?
-	What classification accuracies are mentioned in Tables 1 and 2? Is it the object-object similar classes?

### Soundness
3

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
1

### Summary
This paper proposes the Object-Based Sub-Environment Recognition (OBSER) framework. OBSER identifies sub-environments with three relationships: object-object, object-environment, and environment-environment relationship. The effectiveness of OBSER is measured with the proposed statistically separable (EDS) function in the Minecraft environment.

### Strengths
- OBSER identifies sub-environments with three relationships between objects and environments, and exhibits better distinguishability in terms of EDS compared to other off-the-shelf vision models.

### Weaknesses
 - The application of OBSER is not clear. I'm not sure how OBSER will facilitate downstream tasks, e.g. decision agents in Minecraft like DreamerV3[1], Voyager [2], or GITM [3].

 - The evaluation of OBSER is limited to the Minecraft environment and a single metric (EDS). It is unclear how the proposed framework would perform in more complex or diverse environments. The current evaluation does not sufficiently demonstrate the generalizability of the approach.

 - While the framework considers object-object, object-environment, and environment-environment relationships, the specific mechanisms for how these relationships are encoded and utilized are not fully explained. The paper lacks detailed information on the feature extraction process and how the different relationship types are integrated into the final sub-environment representation. This makes it difficult to assess the novelty and robustness of the approach.

### Questions
- What if the category of possible objects is unknown, e.g. in the open-set setting?

### Soundness
2

### Presentation
2

### Contribution
2
