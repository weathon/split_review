# A multi-region brain model to elucidate the role of hippocampus in spatially embedded decision tasks

- Decision: Reject
- Avg Score: 4.80
- Scores: 3, 3, 8, 5, 5

## Abstract
We present a multi-region brain model exploring the role of structured memory circuits in spatially embedded decision-making tasks.
We simulate decision-making processes that involve the cognitive maps formed within the CA1 region of the hippocampus during an evidence integration task, which animals learn through reinforcement learning (RL).
Our model integrates a bipartite memory scaffold architecture that incorporates grid and place cells of the entorhinal cortex and hippocampus, with an action-selecting recurrent neural network (RNN) that integrates hippocampal representations.
Through RL-based simulations, we demonstrate that joint encoding of position and evidence within medial entorhinal cortex, along with sensory projection to hippocampus, replicates experimentally observed place cell representations and promotes rapid learning and efficient spatial navigation relative to alternative circuits.
Our findings predict conjunctive spatial and evidence tuning in grid cells, in addition to hippocampus, as essential for decision-making in space.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce a modular architecture which integrates position and sensory evidence to create a RL agent capable of performing a common experimental neuroscience task. They specifically show that integration of sensory information in the module responsible for grid cell activity is essential for performance of this task.

### Strengths
The methodology described in section 3.2 seems to accurately match the previously published methodology. The methods relating to learned representations (5.2-5.3.1) show a strong similarity to experimental properties such as place-field location biases. The conjunctive tuning curves (eg: Figure 3 & 7) are particularly convincing.

### Weaknesses
-	Overall, it is difficult to follow the logic of the paper. The introduction begins with a very specific example of neurophysiological findings and then seeks to justify the choice of Vector-HaSH. However, the justification for this starting point is extremely weak (line 122-123). Given that the proposed model is a slight modification of this previously published work, by the introduction of an MLP, there must be a much stronger argument for the validity of the chosen base model. The authors should more clearly articulate why Vector-HaSH is the most appropriate base model, especially given the existence of other models of grid cell activity. The current justification feels insufficient and lacks a detailed comparison to alternatives.
-	Relatedly, the model is a small modification of the previously published vector-hash, followed by detailed investigation of performance and similarity of learned representations to experimental findings. The work therefore seems more appropriate for a neuroscience venue. In the current format, it is unclear what the implications for representation learning are. The paper does not adequately address how the specific modifications to Vector-HaSH contribute to generalizable principles in representation learning. The focus on replicating specific neurophysiological findings overshadows the potential for broader insights into representation learning.
-	Section 2.3 is an odd aside, and the text does not seem to link it to the proposed model or findings at hand. The connection between the literature cited in Section 2.3 and the specific model architecture and results of this paper is not clearly established. The section reads as a general discussion of grid cell relevance to ML, but it lacks a concrete link to the work presented in this paper.

### Questions
- How can these findings be more directly linked to representation learning and machine learning at large? Beyond explaining specific phenomenon in neuroscience, there do not appear to be any general ML findings. While there are paragraphs (2.3 and discussion) claiming that neuroscience findings can guide neuro-inspired AI, no concrete predictions or general findings are made.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors extend the Vector-HaSH model (Chandra et al. 2023), a recently developed neural network model inspired by the hippocampal (HPC)-entorhinal cortex (EC) circuit, to include an MLP-based model of the sensory neocortex and an RNN module to model the brain circuits involved action selection and reinforcement learning. The authors demonstrate the model’s ability to rapidly learn the accumulating tower task, and to generate place cell maps that resemble those observed in the brain (based on data from Nieh et al. 2021). Drawing comparison across 5 models with different architecture and grid and place cell coding schemes, the authors conclude that location-evidence conjunctive coding in grid cells and non-grid EC inputs to the HPC are important for rapid learning and the formation of conjunctive maps in the HPC.

### Strengths
Understanding how the HPC-EC circuit interact with other brain regions in spatial cognition tasks is an important open question. Extensive modeling effort has been focused on the HPC-EC circuit, while sophisticated models linking HPC-EC with other brain regions remain lacking. Hence this study is an important step towards the right direction.

### Weaknesses
1) The neocortex is modeled as a MLP and appears to the only channel by which sensory input enters the EC-HPC circuit. Since the MLP module plays the important role of extracting the evidence velocity and conveying to the Vector-HaSH module, it is unclear comparison with Models 0-2, which do not have the MLP module, is fair.
2) It is not entirely clear how the different coding schemes of the grid cells (position only, disjoint pos+evi, joint pos+evi) are incorporated into the model. In line 309, the authors claim that the joint coding scheme emerged in M4, while Table 2 seems to claim otherwise? Do different grid codes in Models 3-5 emerge due to difference in the architecture? Or other network parameters?  It would be greatly helpful if the authors can provide more implementation details clarifying how the models differ from each other, which would also help distinguish which observed phenomena arise by design and which emerge due to optimizing for task performance?
3) The authors show that M5, with a joint grid code and non-grid input to HPC, yielded faster learning. However, there lacks an intuitive insight on why this is the case. Could the author provide a mechanistic insight and some supporting analyses? 
4) The comparison between model dynamics and biological data appear largely qualitative. For example, the PCA results show some visual clusters in B but less so in A, but how can we be sure there are no separable clusters in high dimensional space?  
5)  Other implementation details, such as how the RNN is trained in an RL framework, is lacking.

### Questions
1) Could the authors clearify how the 5 models differ in architecture, external input, and/or hyperparameter? 
2) Could the authors provide mechanistic intuition on why the joint grid emerged (or is incorporated by design) in M3 &5? (please also clairfy on the claim regarding M4 in line 309-310)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a multi-region brain model for the hippocampo-entorhinal-neocortical circuit in a spatially embedded decison-making task. The purpose of the model is to understand the neural mechanism underlying the conjunctive encoding of position and evidence in the hippocampus in the accumulating tower task. By simulating the task as a RL problem, this paper demonstrates that 1) conjunctive encoding of position and evidence in the MEC and 2) non-grid sensory input from EC to HPC are necessary for the conjunctive representation in the HPC. The conclusion is reached by performing a rigorous testing of mutiple alternative hypothesese and comparing the model representations with hippocampal representations obtained experimentally. Overall, this is a solid paper that asks and answers a very interesting neuroscience question with well-designed experiments making use of an existing model.

### Strengths
- Rigorous testing of alternative hypotheses to the proposed one: I really appreciate the examinations of other possible mechanisms of conjunctive hippocampal encoding (Table 1 and 2) in the paper, which is sometimes missing in many computational neuroscience papers. These examinations not only serve as an ablation study that makes the results more robust but are also biologically interpretable, which definitely strengthens the argument of the paper
- Reference to experimental results (i.e., Nieh et al., 2021): Many computational neuroscience works assume the reader, usually from a computational background, understands the experimental setup they simulate very well. In such cases the reader has to carefully go through the original experimental work to fully understand the context of the model. This paper does quite a good job in this regard by clearly presenting the simulated task very early and referring to the experimental results from Nieh et al. 2021 frequently.

### Weaknesses
 - I didn't find any significant weakness of this paper that can be summarized under general topics. There are some detailed questions/unclarity I wish the authors could address, which I noted under Questions.

 - Why do the authors study the two specific reasons i.e., conjunctive encoding of space and evidence in the MEC and sensory inputs, other than other possible mechanisms underlying the conjunctive hippocampal encoding? Are there any experimental evidence demonstrating that these two are the most likely/important ones? I understand these two reasons are related to the interactions between (M)EC and HPC, but is it possible that the conjunctive representation in HPC is also due to internal reasons e.g., interactions between HPC subregions? The authors might want to add a sentence or two to highlight why they chose to study these two reasons specifically.
- The grid-cells module in the model takes pos and evidence as inputs. I understand that the evidence is a MLP-projected representation of the sensory inputs, which the authos presented quite clearly in lines 215-222. However, it is unclear how position is represented and input into the grid cells. Is it encapsulated in the CAN module?
- The MLP module models how evidence is extracted from sensory inputs, and from Fig1B, it seems to receive sensory inputs directly from non-grid EC. Biologically, is this a known mechanism? Could it be receiving inputs directly from sensory regions? Which brain region and what neural mechanism does this MLP correspond to? Maybe something to include in the Discussion.
- How did you achieve disjoint grid cell encoding of space and evidence in your model? i.e., computationally and mathematically, how did you make a difference between joint and disjoint grid cell codes? You may want to include this in section 3.2 Model Setup, or in the appendix.
- In line 309 'we show that our multi-region brain model (M4)' - you mean M5 right?
- Fig3 left: if space allows, you may want to include Fig1d from Nieh et al. 2021 to make a contrast to right-choice-selective place cells, as readers unfamiliar with their work might struggle to understand what this diagram means.
- Section 5.3.1: I feel this whole subsection is a bit unclear. I wish you can check/clarify the following points:
    - I think this section aims to demonstrate only M5 shows separable clusters of tasks variables, but the title says 'only joint integration model exhibits...' - both M3 and M5 are joint integration model, but M3 doesn't have activated EC pathway right? So I guess what you want to say is 'only joint integration model with activated EC pathway exhibit...'? This is also related to the fact that you are showing in Fig5 that both M4 and M5 are action-separable, but M4 is a disjoint model.
    - On line 431, you refer to Fig 5 A1/A2 for separable clsuters. I guess you should refer to B1/B2?
    - On line 467, you mentioned that you did not observe separability in accumulated evidence. Can you show some example, at least in the appendix?
    - I also feel the whole Fig5 could improve with a re-wording of the caption clarifying which model (M3,4,5) each row (A, B) and each column (1,2,3,4) correspond to. Currently it is not very clear.

### Questions
- Why do the authors study the two specific reasons i.e., conjunctive encoding of space and evidence in the MEC and sensory inputs, other than other possible mechanisms underlying the conjunctive hippocampal encoding? Are there any experimental evidence demonstrating that these two are the most likely/important ones? I understand these two reasons are related to the interactions between (M)EC and HPC, but is it possible that the conjunctive representation in HPC is also due to internal reasons e.g., interactions between HPC subregions? The authors might want to add a sentence or two to highlight why they chose to study these two reasons specifically.
- The grid-cells module in the model takes pos and evidence as inputs. I understand that the evidence is a MLP-projected representation of the sensory inputs, which the authos presented quite clearly in lines 215-222. However, it is unclear how position is represented and input into the grid cells. Is it encapsulated in the CAN module?
- The MLP module models how evidence is extracted from sensory inputs, and from Fig1B, it seems to receive sensory inputs directly from non-grid EC. Biologically, is this a known mechanism? Could it be receiving inputs directly from sensory regions? Which brain region and what neural mechanism does this MLP correspond to? Maybe something to include in the Discussion.
- How did you achieve disjoint grid cell encoding of space and evidence in your model? i.e., computationally and mathematically, how did you make a difference between joint and disjoint grid cell codes? You may want to include this in section 3.2 Model Setup, or in the appendix.
- In line 309 'we show that our multi-region brain model (M4)' - you mean M5 right?
- Fig3 left: if space allows, you may want to include Fig1d from Nieh et al. 2021 to make a contrast to right-choice-selective place cells, as readers unfamiliar with their work might struggle to understand what this diagram means.
- Section 5.3.1: I feel this whole subsection is a bit unclear. I wish you can check/clarify the following points:
    - I think this section aims to demonstrate only M5 shows separable clusters of tasks variables, but the title says 'only joint integration model exhibits...' - both M3 and M5 are joint integration model, but M3 doesn't have activated EC pathway right? So I guess what you want to say is 'only joint integration model with activated EC pathway exhibit...'? This is also related to the fact that you are showing in Fig5 that both M4 and M5 are action-separable, but M4 is a disjoint model.
    - On line 431, you refer to Fig 5 A1/A2 for separable clsuters. I guess you should refer to B1/B2?
    - On line 467, you mentioned that you did not observe separability in accumulated evidence. Can you show some example, at least in the appendix?
    - I also feel the whole Fig5 could improve with a re-wording of the caption clarifying which model (M3,4,5) each row (A, B) and each column (1,2,3,4) correspond to. Currently it is not very clear.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper models the entorhinal-hippocampal-neocortical circuit in the brain using a Vector-Hash + RNN model and trains it with reinforcement learning to accumulate sensory evidence and make decisions. The authors test several model hypotheses, including whether the MEC receives sensory evidence, whether sensory information and spatial information are co-represented, and whether the HPC binds sensory and spatial information through associative memory. Their results indicate: (1) in terms of task performance, inputting both spatial and sensory information to the MEC improves learning speed; (2) in terms of neural experiment interpretation, the mixing of sensory and spatial information in the MEC results in cotuning of evidence and position in HPC place cells, as well as choice-specific firing patterns, similar to experimental findings. These results suggest that integrating multimodal information in the MEC for abstract path integration may be a biological strategy for decision-making tasks.

### Strengths
The first strength lies in the novelty of the model architecture. This paper introduces a new framework for modeling the entorhinal-hippocampal-neocortical loop, combining an RNN trained with gradient backpropagation with a hand-designed, Hebbian-learning-based Vector-Hash module. This approach offers a unique testbed for exploring hypotheses about brain region function and information transfer, providing valuable insights for future research in this area.  

Another strength is the linkage between experimental neural findings and the model’s performance on specific tasks. The paper connects cotuning of evidence and spatial location, as well as choice-specific place cell firing, with efficient spatial navigation and rapid learning in the network, potentially advancing brain-inspired intelligence research.

### Weaknesses
The primary limitation is the oversimplification of the biological network and the lack of rigorous model comparisons, which affects the credibility of the findings. First, the model reduces the entorhinal-hippocampal circuit to a Vector-Hash model, which, while capable of explaining associative and episodic memory functions attributed to these areas, significantly simplifies the actual biological network. For instance, CA3 in the hippocampus has extensive recurrent connections, whereas the Vector-Hash model lacks internal connections, reducing the hippocampus to an intermediary layer connecting MEC and LEC. This simplification may have critical effects when studying how the model produces co-tuned place cells and choice-specific firing since it removes internal computation within the hippocampus, relying instead on upstream grid cell networks.  

Secondly, when proposing joint integration of evidence and spatial velocity in the MEC as a means to enhance learning, the paper lacks a fair comparison of different models' capabilities. For a balanced evaluation, it would be essential to compare the performance of a standalone RNN (without Vector-Hash) receiving both physical velocity and sensory evidence, with an equivalent number of neurons. This is a minimal comparison proposal to clarify Vector-Hash’s role, although it alone may not be fully sufficient for rigorous validation.

### Questions
Overall, I appreciate the paper’s attempt to model the entorhinal-hippocampal-neocortical circuit, especially combining classic theoretical models with RNNs. However, I am somewhat skeptical about the reliability of the conclusions, which impacts my overall assessment. I have several questions, including both major and minor ones, related to the results and model details.

**Major Questions:**
1. In hypothesis M2, where sensory evidence is bound to the HPC, and downstream RNN receives HPC activity as input, why does the network fail to learn effectively, performing worse than an RNN receiving sensory evidence directly? Since spatial location is also useful in this task, as the agent needs spatial navigation for reward acquisition, the paper suggests that coupling both inputs makes it difficult for the downstream RNN to decouple them. Could the authors elaborate on this point?

2. According to Figure 2B, the RNN in M0 can perform efficient navigation, even outperforming the network in M3. This seems counterintuitive, as M3 includes additional spatial location information, which is crucial in a spatial navigation task. Could the authors discuss this in more detail?

3. In the disjoint integration model (M4), no co-tuned place cells emerge in the HPC. Under this model framework, is it because separate grid cell modules lead to orthogonal representations of evidence and position? If so, a natural prediction would be that "evidence cells," tuned purely to evidence spacing, might appear in the HPC. Is this observed in the actual results?

4. I believe that omitting recurrent connections within the HPC contributes to the lack of co-tuned cells when evidence and spatial location are combined in the HPC. If the HPC were replaced with a standard RNN receiving both MEC spatial input and LEC evidence input, would co-tuning place cells still emerge even if the MEC does not receive evidence or integrates evidence and position disjointly? I recommend the authors investigate this, as it may determine whether the findings are artifacts due to biological oversimplification.

**Minor Questions:**
1. In Equation (1), the operation CAN(.) is not clearly defined in the main text or the Appendix. As CAN is a classic, well-studied dynamical model with various implementations, could the authors clarify the specific form used here?

2. In the joint-integration model, how exactly are evidence and position information combined before being input to the MEC? Is it a simple summation?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors proposed a multi-regional reinforcement learning model to solve the evidence accumulation task. The model comprised of MEC for grid cells, EC for sensory cells, hippocampus for place cells, RNN as neocortex and perhaps the policy network as the striatum. The authors proposed 5 different model variants with different network connectivity and information passed into the hippocampus layer and evaluated its learning behavior and analyzed its representation. Based on the results, the authors propose that place cells that conjunctively integrate position and sensory information was important to solve the task.

### Strengths
-- clearly explained the rationale for the model development.
-- presented 5 hypothesis for grid-place interaction for evidence accumulation navigation and showed how they deferred across behavior and representation. 
-- The authors demonstrated that the model recapitulates the neural representations observed in experiments.

### Weaknesses
 -- The authors only demonstrated that their model replicated the representations observed in 1 experiment (Nieh et  al. 2021). The authors should consider recapitulating 1 other neural phenomena to increase the generality of their proposed model e.g. representational drift (Qin et al. 2023 Nature Neuro.), or increase the variety of simulations e.g. 5 arm decision navigation (Baraduc, Duhamel, Wirth, 2019 Science).

-- Although the title specifies the role of hippocampus (instead of the entorhinal cortex), the authors only varied their models using different entorhinal activity to formulate the hypothesis in Table 1. This could be to demonstrate how the type of input to the hippocampus influences navigation learning behavior. Nonetheless, the authors should consider previous models that use different hippocampal representations for navigation learning (Brown & Sharp, 1995; Arleo & Gerstner, 2000; Foster et al. 2000; Zannone et al. 2018; Kumar et al., 2022). For instance, will an RNN based RL agent with place cells and sensory evidence as input learn to solve the task (Kumar et al. 2022 Cerebral Cortex, https://doi.org/10.1093/cercor/bhab456; Singh et al. 2023 Nat Mach. Int., https://doi.org/10.1038/s42256-022-00599-w), similar to M0 but with place cell position inputs? This proposal also suggests a EC-MEC-hippocampus-neocortical-striatum pathway but was not considered.

-- the claim that the model enables rapid learning in spatially embedded task is not warranted. how do the authors define rapid learning and efficient navigation (red and brown curves in Fig. 2)? These agents still require close to 1000 episodes to converge instead of 1 or a few episodes (Foster et al. 2000 Hippocampus https://doi.org/10.1002/(SICI)1098-1063(2000)10:1<1::AID-HIPO1>3.0.CO;2-1 ; Kumar et al. 2024 https://doi.org/10.48550/arXiv.2106.03580)? Rapid learning is usually used under the context of zero, one, or few-shot learning, and not thousands of trials. 

-- it is unclear why M3 and M5 show similar increase in success rates of learning (Fig. 2A) when M3 does not get evidence from EC? Additionally, it is unclear why M0 and M5 show similar decrease in steps spent per episode (Fig. 2B). Representational analysis for M0 and M3 should be included in Fig. 3,4 and 5.

### Questions
-- the authors proposed a mechanistic hippocampus-entorhinal setup. However, it is unclear whether they used a biologically plausible learning rule or backpropagation for policy learning i.e. policy gradient. The former will make the model very appealing. But this is a minor point. 

-- why is there a disparity in M0's and M5's learning performance in Fig. 2A and 2B? Shouldn't we expect a model with a slower increase in cum. success rate to demonstrate a slower decrease in steps spent per episode? Maybe I am missing something. 

-- Since separability of clusters is not a prerequisite for navigation behavior (M3 vs M5 Fig. 9 vs Fig. 2), how can we make sense of the representation to behavior?

### Soundness
2

### Presentation
3

### Contribution
2
