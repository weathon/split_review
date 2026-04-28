# Towards Unifying Interpretability and Control: Evaluation via Intervention

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
With the growing complexity and capability of large language models (LLMs), a need to understand model reasoning has emerged, often motivated by an underlying goal of controlling and aligning models.
While numerous interpretability and steering methods have been proposed as solutions, they are typically designed either for understanding or for control, seldom addressing both, with the connection between interpretation and control more broadly remaining tenuous. Additionally, the lack of standardized applications, motivations, and evaluation metrics makes it difficult to assess these methods' practical utility and efficacy.
To address the aforementioned issues, we propose intervention as a fundamental goal of interpretability and introduce success criteria to evaluate how well methods are able to control model behavior through interventions. We unify and extend four popular interpretability methods—sparse autoencoders, logit lens, tuned lens, and probing—into an abstract encoder-decoder framework. This framework maps intermediate latent representations to human-interpretable feature spaces, enabling interventions on these interpretable features, which can then be mapped back to latent representations to control model outputs.
We introduce two new evaluation metrics: intervention success rate and the coherence-intervention tradeoff, designed to measure the accuracy of explanations and their utility in controlling model behavior. Our findings reveal that (1) although current methods allow for intervention, they are inconsistent across various models and features, (2) lens-based methods outperform others in achieving simple, concrete interventions, and (3) interventions often compromise model performance and coherence, underperforming simpler alternatives, such as prompting, for steering model behavior and highlighting a critical shortcoming of current interpretability approaches in real-world applications requiring control. 
\vspace{-10pt}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the disconnect between interpretability and control in LLMs, proposing intervention as a core goal of interpretability. The authors introduce two novel metrics, intervention success rate and coherence-intervention tradeoff. They are designed to evaluate how well interpretability methods can effectively alter LLM outputs. The paper unifies four interpretability methods under an encoder-decoder framework, enabling human-interpretable feature interventions. Evaluated across three models (GPT-2, Gemma2-2b, Llama2-7b), the authors compare the framework against simpler methods like steering vectors and prompting. The study reveals limitations in existing methods, highlighting lens-based approaches as superior for simple interventions but indicating potential issues with performance degradation.

### Strengths
- The encoder-decoder framework consolidates multiple interpretability methods, allowing for unified evaluation and intervention capabilities
- The intervention success rate and coherence-intervention tradeoff metrics are intuitive ways of assessing the effectiveness of interventions and their impact on model coherence
- The paper offers insights into method-specific trade-offs
- Experiments are well-detailed, covering various aspects of intervention efficacy and model coherence, providing a comprehensive assessment across multiple models and features

### Weaknesses
- Lack of experiments on latest and advanced larger models. Llama-2 is not as advanced as the Llama3 to 3.2 family models, Gemma 2b is on the smaller side and GPT2 is quite dated. It would be interesting to see how this worked on some of the SOTA 7B+ models

- Some of the results in table 1 are missing, I couldn't find a reason for this, there could be a valid reason for this but having it in the table caption would be much clearer

- The evaluation primarily focuses on low-level features (e.g., “yoga,” “coffee”), which doesn't offer concrete insights into the framework’s utility for high-level or abstract features. It would be very interesting to see the set of intervention topics include more complex concepts. The authors do note that low-level features are more valuable, which I agree with, testing high level features would still be useful

- The coherence-evaluation setup primarily measures internal coherence without explicitly assessing task-related performance, which may differ in applied settings

### Questions
- As LLMs are intervened, edited, or steered with guardrails, behavior changes and concept drift may affect feature mapping and intervention fidelity. Does the framework account for this, or would it require retraining to maintain accurate interventions over time?

- How does the framework scale, e.g. for a 70b-200b model? What are the time and memory complexities? 

- Is using Llama3 8b sufficient for coherence? It would be good to get some discussion on the limitations of this and if there are potential alternatives, e.g. using a human teacher etc

- Can the font and line width in the figures be made a little larger?

- In Appendix A.5 there is a broken reference

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
4

### Summary
This paper aims to unify a few interpretability methods (SAEs, logit/tuned lens, probing) via a metaphor to encoder-decoder architectures. Specifically, the paper articulates what the "encoder" and "decoder" are for each of these interpretability methods. Explanations are evaluated by intervention-based evals: "intervention success rate" and "intervened token probability". Lens-based methods are claimed to achieve "more simple, concrete" interventions.

### Strengths
The idea of inverting the explanations in order to get a "natural" notion of intervention seems promising, especially if it is supplemented with theoretical analysis for why this is better than existing intervention-based evals.

### Weaknesses
While the proposed framework is interesting, this paper is not quite ready for acceptance at ICLR 2025; it overall appears incomplete and rushed.

1. Missing large areas of related work, which significantly weakens the claim of "unification", and undermines some claims of novelty. 

- There is a whole subfield of intervention-based evals for interpretability; see the review paper below. This undermines the novelty of "we propose intervention as a fundamental goal of interpretability and introduce success criteria to evaluate how well methods are able to control model behavior though interventions" (Abstract, lines 18-20).

Mueller, A., Brinkmann, J., Li, M., Marks, S., Pal, K., Prakash, N., Rager, C., Sankaranarayanan, A., Sen Sharma, A., Sun, J., Todd, E., Bau, D., & Belinkov, Y. (2024). The quest for the right mediator: A history, survey, and theoretical grounding of causal interpretability. arXiv. https://arxiv.org/abs/2408.01416

- The closest citation to this field is Geiger et. al. (2021) in line 127, which is neither recent nor representative of causal abstractions. 

- Consequently, the "intervention success rate" of Section 3.2 (which is barely defined, in lines 112, 242-244) seems quite similar to Interchange Intervention Accuracy, which has already been well-studed: see for instance

Geiger, A., Lu, H., Icard, T., & Potts, C. (2021). Causal abstractions of neural networks. arXiv. https://arxiv.org/abs/2106.02997

Geiger, A., Ibeling, D., Zur, A., Chaudhary, M., Chauhan, S., Huang, J., Arora, A., Wu, Z., Goodman, N., Potts, C., & Icard, T. (2024). Causal abstraction: A theoretical foundation for mechanistic interpretability. arXiv. https://arxiv.org/abs/2301.04709

Geiger, A., Wu, Z., Potts, C., Icard, T., & Goodman, N. (2024). Finding alignments between interpretable causal variables and distributed neural representations. arXiv. https://arxiv.org/abs/2303.02536

2. The evaluation metrics (Section 3.2, lines 237-249) lack crisp definitions, despite being listed as a main contribution.

3. Experiments and figures appear rushed.

- The captions of Figures 3 and 4 lack detail. 

- It's not clear how many methods are tested, and different parts of the paper state different things. There are only 3 methods in Table 1; line 291 in the Experiments section says there are 5 methods; line 531 in the Conclusion says 4 interpretability methods.

- The prompts in lines 316-318 are not counterfactual: they change more than the target attribute.

- The data (lines 300-308) is quite restrictive, which may explain the 100% training and test accuracy of the probes (line 320).

- What exactly is the function used to measure coherence? Coherence does not appear to be defined anywhere: in line 388 it is simply stated that "we measure coherence ...as a function of the normalized latent edit distance...". What function exactly?

4. The encoder-decoder framework isn't motivated; assumptions are not discussed

- It's not clear (e.g. lines 82-88) what the encoder-decoder framework buys over e.g. mediation analysis.

In sum, this appears to be a preliminary research draft more appropriate for a conference workshop.

### Questions
1) Can you please position this paper relative to causal interpretability methods discussed in the review (Mueller 2024) cited above? 

2) Is the goal of this paper to unify "interpretability" and "control" as mentioned in the title, or "unifying and extending four popular interpretability methods" (line 530-531)? These are very different!

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The proposed approach adopts an "intervention" based perspective to LLM interpretability. Two metrics for evaluating mechanistic interpretability approaches are proposed: a "intervention success rate" that quantifies how often changes in an interpretable feature yield desired changes in model outputs, and a "coherence-intervention tradeoff" that quantifies tradeoffs between intervention success and the coherence of model outputs. Extensive experiments demonstrate that different interpretability techniques yield interventions with varying  differing success rates and levels of output-coherence after the intervention.

### Strengths
* The problem area is well-motivated and timely — indeed, there's a gap in evaluating the "quality" of different interpretability techniques for LLMs. The proposed approach fills the gap by proposing concrete quality metrics to that end, and the experiments comprise multiple proofs-of-concept for how one could use the proposed metrics to evaluate interpretability techniques. 
* Some of the proposed metrics are intuitive and easy to measure. I particularly like the "intervention success" metric — while simple, it's a really intuitive proxy for whether an interpretability technique actually provides an "intervene-able" interpretation. 
* Contributing a benchmark of open-ended prompts from a variety of domains is also valuable — it's not simply another "task/capability" for LLMs to solve, but a natural test-bed for diversifying the space of possible interventions under the proposed framework.

### Weaknesses
Major 
* [W1] Comparability of approaches: Given that the learned $D$ has different columns depending on the approach (esp. SAE vs. the others), it is not immediately clear how one can compare different approaches directly. Furthermore, it's unclear if low "intervenability" (success rate and coherence) as measured by the proposed approach is attributable to a poor process for learning $D$, or the inability of the base LLM to "steer" along the relevant feature. More generally, the metrics could reflect either the behavior of the base LLM or the feature extraction approach.
* [W2] Evaluation metrics: I like the definition of intervention success, but coherence is much less clear. The explanation in the paper is "This can be done by any oracle, such as a human or another capable LLM" — but these approaches have disadvantages, since human annotation may be expensive, and an LLM-as-judge approach is not necessarily well-calibrated w.r.t. human annotations. 
* [W3] Undefined notation: $x$ is not defined at the top of 3.1, and $\theta$ is not defined (L200) in the explanation of probing. Again, I can guess what these mean from related works/Figure 1, but there's a high risk of misunderstanding. 

Minor 
* Lack of clarity in Figure 1: I know that symbols such as $D$ are defined later in the manuscript, but given that we encounter figure 1 at the top of page 2, it's a difficult to understand what the columns of the table are. This also makes it hard for me to appreciate the extent of the papers' contributions. I think the Table in Fig. 1 would be valuable later in the paper, after some expectations have been set about  desiderata for LLM interpretability evaluations.  At the very least, I think I need to see Section 3.1 before seeing the Table.
* Limited to open-weight models: while this limitation is shared by many approaches for interpretability/controllability, it would be nice to hear about potential extensions to models where the only access to a model is via API. For example, one could still intervene at the prompt level. Ultimately, this is very minor and wouldn't sway my score.

### Questions
Answers to the following questions would be most likely to sway my score:
* **Re [W1]:** Could the authors provide more details on how one can make SAEs comparable to the other approaches for the purposes of comparing interprtability techniques (i.e., expand on the description in 4.1)?
* **Re [W1]:** In the experiments, high intervenability is equivalent to "frequency of word in sentence" due to the setup. Doesn't this give an unfair advantage to LogitLens/approaches where the feature space under interpretation is already the vocabulary? 
* **Re [W2]:** How might one design a more systematic/rigorous metric for coherence (*e.g.*, why not simply use rules-based tools to check for grammatical errors)? Are "grammar" and "comprehension" the only relevant dimensions for coherence (as used in the LLM-as-judge prompt in the paper)? How did/how might the authors plan to validate their coherence metric?

### Soundness
2

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
2

### Summary
To bridge the gap between research and techniques focused primarily on one of either understanding or control in LLMs, this paper presents a framework to unify interpretability and control through intervention.  They propose an encoder-decoder framework to enable both explanations from and interventions on latent representations, mapping human-interpretable features back to the model's latent space.  Two metrics, intervention success rate and coherence-intervention tradeoff, are introduced to assess the methods in a more holistic and direct way than was previously possible. The results show that while current methods can enable intervention, they are inconsistent across models and features, and can compromise model coherence.

### Strengths
The paper demonstrates originality by unifying interpretability and control, addressing a key gap in popular research directions where most work focuses on either understanding or steering models. Its introduction of a unified encoder-decoder framework and new evaluation metrics (intervention success rate and coherence-intervention tradeoff) provides a novel perspective for benchmarking existing interpretability techniques more uniformly and on a more level playing field. The experiments evaluate multiple popular methods across various models, exposing the relative strengths and weaknesses of different approaches.  The method and evaluation framework are clearly explained, and supported by a useful Figure 1.  This paper seems like a significant contribution to the field, offering a framework to unify the pursuit of interpretability and control, an obvious yet elusive goal in LLM interpretability.  I believe it can stand as a valuable resource for ongoing research on model safety and alignment.

### Weaknesses
The primary weakness of the paper is the lack of extension to complex, real-world applications.  Evaluation is limited to relatively simple interventions, such as word-level steering (e.g., 'coffee' or 'yoga') w.r.t. concrete concepts, which may not fully capture the challenges of more abstract, high-stakes tasks such as ethical decision-making, bias reduction, or truthfulness.  While this limitation is addressed acknowledged by the authors, and common in this research area, it does stand as a challenge in being able to draw any strong conclusions from the experiments.

### Questions
It seems that the experiments rely heavily on data/prompts generated by LLMs.  Is this data inspected by humans, or otherwise validated for correctness?

### Soundness
3

### Presentation
3

### Contribution
3
