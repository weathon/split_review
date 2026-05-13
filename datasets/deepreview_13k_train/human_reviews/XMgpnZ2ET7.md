# Modeling Unseen Environments with Language-guided Composable Causal Components in Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Generalization in reinforcement learning (RL) remains a significant challenge, especially when agents encounter novel environments with unseen dynamics. Drawing inspiration from human compositional reasoning—where known components are reconfigured to handle new situations—we introduce World Modeling with Compositional Causal Components (WM3C). This novel framework enhances RL generalization by learning and leveraging compositional causal components. Unlike previous approaches focusing on invariant representation learning or meta-learning, WM3C identifies and utilizes causal dynamics among composable elements, facilitating robust adaptation to new tasks. Our approach integrates language as a compositional modality to decompose the latent space into meaningful components and provides theoretical guarantees for their unique identification under mild assumptions. Our practical implementation uses a masked autoencoder with mutual information constraints and adaptive sparsity regularization to capture high-level semantic information and effectively disentangle transition dynamics. Experiments on numerical simulations and real-world robotic manipulation tasks demonstrate that WM3C significantly outperforms existing methods in identifying latent processes, improving policy learning, and generalizing to unseen tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
After reading the rebuttal, I agree that language information could be somewhat generally available and I appreciate the effort in fixing writing issues with the paper, so I decided to slightly increase my score.  

This paper proposes a verb/object decomposed world model where the verb and object for a task are given beforehand.  There is improved sample complexity on metaworld, but the method seems like it’s much more complicated and using quite a bit of domain knowledge.  The analytical experiments are good.  

notes from reading the paper: 
  -RL generalization to new environments is difficult, especially if there are unseen dynamics.  
  -World modeling with composition causal components.  
  -Causal dynamics over composable elements.  
  -Language as a compositional modality.  
  -Masked autoencoder with MI constraint and sparsity to capture high-level semantic information and disentangle transition dynamics.  
  -Experiments on real robots and numerical simulations, method is called WM3C.  
  -DRL algorithms have a difficult time to adapt to changes in the environment.  Many ways of getting around this problem require domain-specific knowledge.  
  -Composable causal components and dynamics can be uniquely identified (this seems surprising to me).  
  -Language-controlled components are a subset of state dimensions that are directly controlled by individual language components.  
  -[o_t, r_t] = g(s_t, \eps_t).  s_t is defined as set of composable components.  The c_{it} is defined as a distribution conditioned on the language l_t and the previous state and action.  
  -Blockwise identifiability requires the mixing function to be invertible and smooth.  Also every state must have density.  
  -Utilize model-based RL algorithm DreamerV3.  
  -Additional sparsity constraint. 
  -Only reward-relevant states are used for the policy model.

### Strengths
Good analytical experiments, some improvements in sample complexity on metaworld.

### Weaknesses
Method adds substantial complexity and also seems to require much more domain knowledge than the baseline. The requirement of pre-defined controllable composable components, while enabling modularity, introduces a significant constraint. This contrasts with methods that learn representations directly from observations, which are more generally applicable. The paper does not fully explore the limitations of this assumption, particularly in scenarios where the underlying causal structure is not easily decomposed into verb/object components. The gains in sample complexity on meta-world, while present, are not overwhelmingly significant given the added complexity and domain knowledge requirements. Figure 6 remains difficult to interpret, even with the intervention on the verb component, it's hard to discern how the action or object is being changed. The blurry effect of the arm does not clearly demonstrate the disentanglement of the verb component from the object or action components.

### Questions
-Typo on first page, poorly is spelled “pooly”.  
  -How much effort needs to go into figuring out the “controllable composable components”?  This might be less desirable than a system which works for any general MDP, by processing the observations.  
   -Experiments show effective component identification over the course of training in a synthetic task.  
  -The gains in sample complexity on meta-world still seem to be significant.  
  -Figure 6 looks fairly unprofessional and is hard to make sense of.  Intervention the verb component makes the arm blurry, which is good to verify.  However, it doesn’t really clearly show a change what the action or the object are.  This may be related to the nature of pixel-space reconstructions.

### Soundness
3

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
3

### Summary
The paper presents World Modeling with Compositional Causal Components (WM3C), a novel approach in reinforcement learning (RL) aimed at improving generalisation in novel environments. Inspired by human reasoning, WM3C identifies and utilizes causal, compositional elements, leveraging language as a guiding modality. The approach builds on the causal structure of RL tasks by combining theoretical identifiability guarantees with a masked autoencoder architecture and adaptive sparsity. WM3C outperforms existing methods in identifying causal components and supports efficient policy learning and generalization, as shown through synthetic data simulations and robotic manipulation tasks in the Meta-World environment. Although promising, the results’ scalability in more diverse real-world scenarios remains unclear.

### Strengths
1. An exciting and important problem is being tackled. 
2. Comprehensive conceptual and theoretical analysis.

### Weaknesses
My main concern is a relatively lean experimental section; see the questions and points below.

1. As the proposed method is quite complicated, it is unclear if the effects can be due to the described mechanisms.  Specifically, the interaction between the masked autoencoder, adaptive sparsity, and the causal component identification is not thoroughly dissected. It's difficult to isolate which component contributes most to the observed performance gains, and whether the gains are truly due to the causal structure learning or other factors.
2. Only one real-world environment is tested (I am aware that it might be partially due to a lack of proper benchmarks). The Meta-World environment, while useful, is limited in its complexity and diversity compared to real-world robotic scenarios. Testing on a single environment makes it difficult to assess the generalizability of the proposed method.
3. Only one algorithm is tested. While DreamerV3 is a strong baseline, it would be beneficial to compare against other model-based RL algorithms or even some strong model-free baselines to better understand the relative strengths and weaknesses of the proposed approach.
4. The transfer and generalization results are relatively weak (at the same time, I am not quite sure if the current scale of experiments is large enough to reveal strong effects.) The adaptation performance in Figure 5, for example, does not show a substantial improvement over the baseline, raising concerns about the practical benefits of the proposed method in few-shot adaptation scenarios.

### Questions
1. How is the presented setup related to hierarchical RL?
2. How is it possible that WM3C can acquire the latent language structure with only 20 tasks? It feels very nice but somewhat implausible.   
3. Adaptation results in Fig 5 feel somewhat poor. Could you comment on that?
	1. I'm wondering if pure Dreamer is a proper baseline. E.g., recent [1] shows that transfer is better if forgetting mitigation is applied
4. Could you describe the applicability of the proposed approach? Is it a multi-task setting like Meta-World or perhaps pertaining? 

[1] Fine-tuning Reinforcement Learning Models is Secretly a Forgetting Mitigation Problem, Wolczyk et al.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to identify the underlying composable causal components in reinforcement learning (RL) environments to facilitate policy generalization. The main idea is to leverage language descriptions of the task to identify the underlying latents that govern the data generation process. The paper implements this theoretical result based on the model-based RL framework Dreamer V3, with additional constraints to foster sparsity and modularity of the learned components. The proposed method is empirically verified on synthetic data and robot manipulation tasks in Meta-World.

### Strengths
- The identification result in Theorem 1 is interesting and implies an advantage of language-driven RL agents compared to non-language counterparts.

- Empirical results are generally good. I also like the intervention results in Figure 6.

### Weaknesses
I think the biggest weakness of the paper in its current form is the discrepancy between the motivation, theoretical results, and the algorithm.
- The authors motivate their algorithm by the need to identify composition causal components in the underlying data generation model, which possesses some ideal traits like modularity and sparsity, as introduced in the causal learning literature. However, if our aim is to identify "causal" components, then we need to recover not only those components but also their causal structure (as also noted by the authors in Lines 74-75), or the word "causal" itself would become meaningless. Yet, the identification result presented in Theorem 1 gives no guarantee of recovering such a causal structure. The theorem only establishes the identifiability of the latent variables given language descriptions, but it does not address how these identified latents interact causally. This is a critical gap, as causal understanding requires knowing the direction and nature of influences between variables, not just their existence.

- On the other hand, the algorithm indeed uses modularity and sparsity constraints. However, such constraints are not reflected in the identification results, making the theory and the algorithm not really consistent. It feels to me that those constraints are more heuristics inspired by the causal learning literature, rather than motivated by Theorem 1. The theoretical result does not explain why these specific constraints are necessary or sufficient for causal identification. The use of L1 regularization and mutual information constraints seems somewhat ad-hoc without a clear theoretical justification within the framework of Theorem 1.

I think to rectify the potential understanding, the authors should explicitly make it clear that the theoretical results do not guarantee "causal" identification.

Also, I think the authors should make the relationship between their theoretical results and prior results in representation identifiability more clear.

- The authors have claimed that prior methods for identifying latent variables use "different priors like functional form prior, independent noise conditions and auxiliary variables" (Line 176), which limits their scalability. Yet, the "language components" used by the paper can also be modeled as "auxiliary variables", which indeed play a crucial role in the identifiability result. The paper needs to clarify how their use of language components as auxiliary variables differs fundamentally from existing approaches using other forms of auxiliary variables, and why this difference leads to improved scalability.

- Technically, the high-level idea of proving identifiability is similar to the results in [1, 2], which rely heavily on the conditional independence between latent variables and observable variables. The authors could include a discussion of those results.

Minor:

- Typo: Line 252 -> bfrom.

### Questions
- What is the relation between the identifiability result in Theorem 1 and prior results in non-linear ICA?

- What is the effect of each constraint in the algorithm? It seems that no ablation on them is presented in the experiments section.

Minor:

- Typo: Line 252 -> bfrom.

### Soundness
3

### Presentation
2

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
This paper introduces the World Modeling with Compositional Causal Components (WM3C) framework for reinforcement learning (RL). The framework aims to address the problem of generalization to unseen environments by leveraging compositional causal components by incorporating language-guided compositional causal reasoning inspired by human reasoning. Using language as a compositional modality, the framework decomposes latent space into semantically meaningful modular components with causal dynamics. Unlike prior methods focusing on invariant representation learning or meta-learning, WM3C aims to learn compositional components and utilize them to generalize effectively to new environments. The paper provides theoretical guarantees for the identifiability of these components under certain assumptions and implements the concept using a masked autoencoder (MAE) with mutual information constraints and adaptive sparsity regularization. WM3C's effectiveness is demonstrated through experiments on (synthetic) numerical simulations and (real-world) robotic manipulation tasks on the MetaWorld environment, where it outperforms existing approaches on generalization/adaptation to unseen tasks.

### Strengths
- **Originality**: WM3C's approach of integrating causal reasoning with compositional learning in RL is interesting. The use of language-guided decomposition adds a unique dimension to generalization in RL.

- **Quality**: Theoretical grounding is generally robust, with guarantees on the identifiability of compositional components. While the presented experimental results support the overarching claim, the strength and suitability of the experiments have room for improvements.

- **Clarity**: The clarity of the technical writing could be improved. Discussed further in the ‘Presentation’ section of the review.

- **Significance**: Generalization in RL is a well-known challenge. The paper tackles this critical problem in RL—generalization to unseen environments—and presents a solution with potential for significant impact in real-world applications.

### Weaknesses
 
**Discussion** 
The crux of the work's novelty lies in the mapping between orthographic components (as we understand it: textual, visual, etc.) and latent space blocks, thereby allowing generalization to unseen tasks through the composition of these learned invariant primitive blocks. Such compositional generalization is a well-researched (and active) area, especially in the NLP, VQA, and EAI domains. For example, numerous papers using the CLEVR images and captions dataset, along with mixing the attributes in the VQA domain, explore such generalization using text and image modalities. One key enabler of these models was applying masked object encoders, thereby infusing the models with knowledge of what the objects are.
In this work, the effect of using MAE (vs. CNN) is not entirely clear or conclusive (from Fig. 5). However, the point remains: for the visual modality, the object and latent space mapping is fairly well-established and by no means novel, especially if object masking is in play. The mapping between textual semantics — especially explicit mapping of complex verbs or actions with latent space blocks — is, however, quite promising and, to my knowledge, novel for this specific domain. However, the experiments conducted to show the efficacy use very simple instantiations of the language modality. There are a fairly large number of environments in the embodied AI space (like AI2Thor's ALFRED, Habitat, etc.) that have more realistic textual instructions for task completion scenarios—which, in my opinion (IMO), would be much more convincing to demonstrate the efficacy of this approach, the effectiveness of textual component identifiability, and the overall claim of the effectiveness of using causal RL.


* **Limited Evaluation** The presented experiments are weak. Experiment 1 using synthetic data (3 tokens, 3 control groups) should not be a major experiment with supporting figures in the main paper, but rather should have been a preliminary ‘smoke-test’ \- maybe getting a subsection of an appendix section at best. I have major concerns about the baselines of Experiment 2 conducted on MetaWorld’s robotic manipulation tasks.  The only baseline comparison is against DreamerV3 (2 variants).  I am wondering why any of the available, known, easily replicable RL models (e.g. MT-[SAC|PPO]) were not included as baselines? 

* **Evaluation environments**: Given the claim of mapping ‘textual components’, the choice of environments and models could be more commensurate. Specifically, the proposed approach should be evaluated on environments that allow richer text+vision modality and agent interaction. There are a slew of such multi-modal environments across subdomains, like in the embodied AI domain: RoboThor (the ALFRED task), Habitat or, simpler HomeGrid. Given the richer, realistic text instructions on these domains, the claim of unique identification of causal textual components would be far better convincing. 

* **Scalability**: The scalability of WM3C to environments with more complex dynamics and a higher number of compositional components has not been fully explored. Future work should test the framework in larger-scale environments.

* **Limited Analysis of Failure Cases**: It would be helpful to include a discussion on the limitations of WM3C, particularly regarding situations where the causal components may overlap or cannot be distinctly identified. Understanding where and why the model fails is crucial for improving the framework.

### Questions
**Questions**:

1. Can the authors elaborate on the train/test methodology of the baseline model (Dreamer V3) on MetaWorld? Were textual task descriptions included in the encodings? Did the authors use any existing implementation of Dreamer V3 on MetaWorld, or is it novel for this paper?

2. Why didn’t the authors include performance comparisons with generic RL models like Multitask-[SAC|PPO], which are provided out-of-the-box with the MetaWorld environment?

3. Could the authors provide more intuition or real-world examples where the faithfulness assumption might fail? How sensitive is the performance of WM3C to violations of this assumption?

4. What are the key limitations of WM3C in environments with highly overlapping causal components (more likely in richer/complex language instructions)? How might the model be adjusted to handle such scenarios?

5. How sensitive is the framework to the choice of language components? Would other compositional modalities (e.g., visual <-> auditory signals) work as effectively?

### Soundness
3

### Presentation
2

### Contribution
3
