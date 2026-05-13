# Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment

- Decision: Accept
- Scores: 10, 8, 8

## Abstract
Aligning large language models (LLMs) with human preferences becomes a key component to obtaining state-of-the-art performance, but it yields a huge cost to construct a large human-annotated preference dataset. To tackle this problem, we propose a new framework, Spread Preference Annotation with direct preference judgment (SPA), that boosts the alignment of LLMs using only a very small amount of human-annotated preference data.
Our key idea is leveraging the human prior knowledge within the small (seed) data and progressively improving the alignment of LLM, by iteratively generating the responses and learning from them with the self-annotated preference data.
To be specific, we propose to derive the preference label from the logits of LLM to explicitly extract the model's inherent preference. 
Compared to the previous approaches using external reward models or implicit in-context learning, we observe that the proposed approach is significantly more effective.
In addition, we introduce a noise-aware preference learning algorithm to mitigate the risk of low quality within generated preference data.
Our experimental results demonstrate that the proposed framework significantly boosts the alignment of LLMs.
For example, we achieve superior alignment performance on AlpacaEval 2.0 with only 3.3% of the ground-truth preference labels in the Ultrafeedback data compared to the cases using the entire data or state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This work proposes SPA, a framework to lower the high costs of collecting large preference datasets for alignment. SPA uses an LLM's logits to generate pairwise preference data, without reward model learning or in-context learning, which is then used for preference learning for LLMs. The authors show the practical usefulness of SPA by aligning mistral 7B on 3.3% of Ultrafeedback preference data to achieve strong performance compared to state-of-the-art methods on AlpacaEval 2.0 and MT-Bench

### Strengths
1. The paper is well-written and very easy to follow throughout. The paper contextualizes itself within the alignment literature well, covering the fundamentals of pairwise preference learning (Bradley-Terry modeling) to direct alignment algorithms like DPO (Section 3)
2. SPA is able to use only a small seed preference dataset to then directly score preference labels using the implicit reward model learned by DPO (Section 4.1). Since these predictions can be noisy, the authors introduce a novel self-refinement denoising technique using a confidence prediction (eq 9) to smooth the preference label (eq 10)
3. Reproducibility: the authors provide implementation details and hyperparameters in Section 5 (*L311-321*). The authors will open-source the code and models after acceptance, which is appreciated. Lastly, because the modification to the DPO objective is minimal, the authors mention only a few lines of change to the DPO codebase, which is another advantage for practical utility of SPA
4. The authors compare to popular categories of baselines: iterative DPO methods, LLM-as-judge methods, and explicit reward-modeling + RLHF methods (*L288 - L291*) and achieve strong results on AlpacaEval 2.0 and MT-Bench
5. The authors show SPA extends beyond Mistral to other popular LLMs like Phi and Llama (Table 5) and is robust, in the win rate variance sense, to the seed of the initial preference data (Table 4)

### Weaknesses
No major weaknesses, mainly minor clarifications:
1. Can the authors provide a little more description about the "length control" aspect of AlpacaEval 2.0 in the main paper? This setting is used in nearly all results, but is not explained clearly where first introduced (Section 5.2)
2. What is "gold label" (Table 1, 5)? Is this the Ultrafeedback preference data? Please make this explicit in the writeup

### Questions
Minor Typos
1. "Lengh-control" in Figure 2
2. "additional codes" , L267

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an efficient LLM alignment method, namely Spread Preference Annotation, aiming at reducing the demand for human-labeled preference data. By leveraging the inherent preference of current aligned model, this work generates new preference data points and conducts alignment iteratively. To reduce the potential noise caused by distribution shift, this work incorporates a self-refinement mechanism on preference labels, where this approximate a more strongly aligned model to better identify noise through a linearly extrapolated prediction method. Through experiments this paper proves that SPA can achieve better alignment performance with much less data.

### Strengths
1. This work inherits the idea of self-rewarding, but leverages the inherent preference of current aligned model in an intuitive way, which sounds novel to me.
2. The reduction on data usage seems promising, and the performance is robust.

### Weaknesses
1. 'De-coupled noise preference detection' is not stated clearly enough in section 4.2. Based on my understanding, $z_{\tilde{\theta}}$ is used to substitute for $z_{\theta}$ in the 'Self-refinement' part, which is also supported in Algorithm 1. If I am correct, I think it would be easier for readers to understand if the final usage of the approximated logits and labels are stated in the main text.
2. Lacks some explanatory discussion on why this method can work on such a small subsets and even perform better than DPO with the full dataset (Details in questions part).

### Questions
1. What is the model used for the 'LLM-as-judge' method in Table 2 ? Have you tried using ${\pi}_{i-1}$ in this baseline?
2. There are lines out of the border in references and appendix.
3. (corresponding to weakness 2) Why this method can work with only 3.3% of total data? Does this method elicit the latent human preference knowledge from pre-trained model, or the 3.3% subset is already enough to define the human preference in UltraFeedback dataset? (Note that this is not a fatal question, feel free to provide any discussion or hypothesis).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes SPA, an approach to enhance the alignment performance of large language models by using minimal human-annotated preference data.
Introduce a confidence-based refinement of preference labels to reduce the risk of noise in preference learning with generated data.
It is experimentally verified that a tiny percentage of preference data (3.3%) achieves results comparable to or exceeding those obtained using the entire data and the existing optimal baseline method in the AlpacaEval 2.0 evaluation.

### Strengths
1. The overall idea is relatively simple, but the method achieves good performance and has great potential with limited human labeling.
2. The paper is well-structured and presents a rigorous methodology, with comprehensive experimental validation that supports the claims made about SPA’s effectiveness.

### Weaknesses
This is a very solid piece of work. The proposed method is simple yet effective. I don't have any particular concerns or issues with it.

### Questions
1. How do you choose the initial seed data? Are the data randomly chosen as seeds? Are there differences in human preferences across data? How do you handle such differences?
2. In section 4.1, can you elaborate on the sampling process used to generate the responses y1 and y2? In particular, does the model use specific diversity techniques to ensure diversity of reactions, or does it rely purely on randomness in the generation process?
3. How does it ensure the reliability of the expanded data?

### Soundness
4

### Presentation
4

### Contribution
3
